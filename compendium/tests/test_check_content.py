"""Tests for build/check_content.py. Each test makes its own entries."""
from pypdf import PdfWriter

from check_content import (bad_text, duplicates, forbidden, monster_out_of_band,
                           spell_damage_too_high, too_many_pages)
from monster_engine import M

EM, EN = chr(0x2014), chr(0x2013)


def test_duplicates_ignores_case():
    assert len(duplicates("feats", ["Alert", "alert"])) == 1
    assert duplicates("feats", ["A", "B"]) == []


def test_forbidden_matches_whole_words_only():
    assert len(forbidden("monsters", ["Elder Beholder"], {"beholder"})) == 1
    assert forbidden("monsters", ["Beholden Knight"], {"beholder"}) == []


def test_forbidden_matches_names_with_spaces():
    assert len(forbidden("monsters", ["The Mind Flayer Queen"], {"mind flayer"})) == 1


def test_bad_text_finds_em_dash_and_trademark():
    assert len(bad_text("x", f"fast {EM} slow")) == 1
    assert len(bad_text("x", "a D&D game")) == 1
    assert len(bad_text("x", "a D&amp;D game")) == 1
    assert len(bad_text("x", "Dungeons & Dragons")) == 1
    assert bad_text("x", f"26{EN}30") == []


def test_monster_with_too_high_ac_fails():
    assert len(monster_out_of_band(M("T", "M", "Beast", "U", 1, "10 10 10 10 10 10", ac=20))) == 1
    assert monster_out_of_band(M("T", "M", "Beast", "U", 1, "10 10 10 10 10 10")) == []


def test_monster_with_low_ac_passes_above_floor():
    assert monster_out_of_band(M("T", "M", "Ooze", "U", 1, "10 10 10 10 10 10", ac=7)) == []
    assert len(monster_out_of_band(M("T", "M", "Ooze", "U", 1, "10 10 10 10 10 10", ac=3))) == 1


def test_monster_with_hp_multiplier_out_of_range_fails():
    assert len(monster_out_of_band(M("T", "M", "Beast", "U", 1, "10 10 10 10 10 10", hp=2.0))) == 1


def test_spell_damage_above_curve_fails():
    assert len(spell_damage_too_high("T", 1, "takes 8d10 Fire damage", False)) == 1
    assert spell_damage_too_high("T", 1, "takes 2d10 Fire damage", False) == []


def test_spell_damage_uses_area_curve_for_area_spells():
    # 3d6 (10) is above the level 1 area cap 2d6 (7) times 1.25, but not above the single-target cap.
    assert len(spell_damage_too_high("T", 1, "takes 3d6 Fire damage", True)) == 1
    assert spell_damage_too_high("T", 1, "takes 3d6 Fire damage", False) == []


def test_too_many_pages(tmp_path):
    pdf = tmp_path / "two.pdf"
    w = PdfWriter()
    w.add_blank_page(100, 100)
    w.add_blank_page(100, 100)
    w.write(str(pdf))
    assert len(too_many_pages(str(pdf), limit=1)) == 1
    assert too_many_pages(str(pdf), limit=2) == []



def test_avg_counts_flat_bonus():
    from monster_engine import avg
    assert avg("1d8+3") == 7
    assert avg("2d6-1") == 6
    assert avg("2d6") == 7
