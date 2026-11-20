"""Tests for the book build of Beyond the Western Sea.

Each test makes its own book in a temporary folder and its own content
in a small module. No test reads the book text that the writers edit.
"""
import dataclasses
import types

import pytest

import build as B
import campaign
import waking
import western_sea as WS
from monster_engine import M


def crab_content():
    mod = types.ModuleType("stub_content")
    mod.MON = [M("Test Crab", "M", "Beast", "Unaligned", 1, "14 12 13 3 10 5",
                 attacks=[("Claw", "m", "1d8", "Slashing")])]
    mod.NPCS, mod.ITEMS, mod.PLACES = [], [], []
    return mod


def crab_book(tmp_path):
    book = tmp_path / "book"
    (book / "chapters").mkdir(parents=True)
    (book / "chapters" / "02-the-shore.md").write_text("# The Shore\n\nA crab.\n\n{{statblock: Test Crab}}\n")
    return book


@pytest.fixture(autouse=True)
def clean():
    B.TOC.clear()
    campaign.WARNINGS.clear()
    campaign.ANCHOR_MARK.clear()
    campaign.IDX.clear()
    yield


def test_statblock_gets_bracket(tmp_path):
    book = crab_book(tmp_path)
    mod = crab_content()
    c = dataclasses.replace(WS.WESTERN_SEA, book=str(book), content=lambda: mod)
    h, _ = campaign.expand(c)
    assert "Test Crab" in h
    assert "[d6 + " in h


def test_waking_has_no_bracket(tmp_path):
    book = crab_book(tmp_path)
    c = waking.waking(book=str(book), tutorial=str(tmp_path / "no-tutorial"))
    h, _ = campaign.expand(c, dw=crab_content())
    assert "Test Crab" in h
    assert " [d6" not in h


def test_check_pages():
    assert WS.check_pages(119)
    assert WS.check_pages(141)
    assert WS.check_pages(120) is None
    assert WS.check_pages(140) is None


def test_source_dice_errors(tmp_path):
    book = tmp_path / "book"
    (book / "chapters").mkdir(parents=True)
    (book / "chapters" / "02-x.md").write_text("# X\n\n| d20 | x |\n|---|---|\n| 1 | y |\n")
    (book / "how-to-run.md").write_text("# How to Run\n\n| d66 | Event |\n")
    errs = WS.source_dice_errors(str(book))
    assert len(errs) == 1
    assert "02-x.md" in errs[0] and "d20" in errs[0]


def test_the_title_has_no_empty_sub_title(tmp_path):
    book = crab_book(tmp_path)
    mod = crab_content()
    c = dataclasses.replace(WS.WESTERN_SEA, book=str(book), content=lambda: mod)
    h, _ = campaign.expand(c)
    assert "<title>Beyond the Western Sea</title>" in h
    assert "<h1>Beyond the Western Sea</h1>" in h
    assert "Dice &amp; Destiny: Beyond the Western Sea</b>" in h


def test_a_map_with_no_final_file_is_a_placeholder(tmp_path, monkeypatch):
    import farholm_maps as FM
    monkeypatch.setattr(FM, "MAP_DIR", str(tmp_path))
    monkeypatch.setattr(FM, "MAP_IDS", ["farholm", "colony-town"])
    assert FM.missing_maps() == FM.MAP_IDS
    with pytest.raises(KeyError):
        FM.map_svg("farholm")
    with pytest.raises(KeyError):
        FM.map_svg("no-such-map")
    (tmp_path / "farholm.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><path id="a" fill="#000"/></svg>')
    assert FM.missing_maps() == ["colony-town"]
    assert 'id="farholm-a"' in FM.map_svg("farholm")
    h = campaign.map_html("colony-town", maps="farholm_maps")
    assert 'class="map-placeholder"' in h


def test_page_count_stops_the_build():
    with pytest.raises(SystemExit) as e:
        WS.build_book(build=lambda c, screen: None, count=lambda path: 100)
    assert "120 to 140" in str(e.value)
    WS.build_book(build=lambda c, screen: None, count=lambda path: 137)
    WS.build_book(screen=True, build=lambda c, screen: None, count=lambda path: 100)
