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


# ---- Fixes from the review of the foundation ----
from check_content import (bad_source, unknown_values, unregistered_packages)
from monster_engine import avg


def test_avg_counts_flat_bonus():
    assert avg("1d8+3") == 7
    assert avg("2d6-1") == 6
    assert avg("2d6") == 7


def test_spell_damage_with_two_words_before_damage_is_checked():
    assert len(spell_damage_too_high("T", 1, "takes 8d10 Fire or Cold damage", False)) == 1


def test_spell_damage_in_one_sentence_is_added_up():
    text = "The target takes 2d10 Fire damage and 2d10 Cold damage."
    assert len(spell_damage_too_high("T", 1, text, False)) == 1
    two = "The target takes 2d10 Fire damage. Next turn, it takes 2d10 Cold damage."
    assert spell_damage_too_high("T", 1, two, False) == []


def test_area_words_include_wall_radius_and_several_targets():
    from check_content import is_area
    assert is_area("You create a wall of fire")
    assert is_area("in a 20-foot radius")
    assert is_area("up to three creatures you can see")
    assert not is_area("one creature you can see")


def test_forbidden_catches_plurals_and_curly_apostrophes():
    banned = {"beholder", "mind flayer", "slaad", "baldur's gate"}
    assert len(forbidden("m", ["Beholders"], banned)) == 1
    assert len(forbidden("m", ["Mind Flayers"], banned)) == 1
    assert len(forbidden("m", ["Slaadi"], banned)) == 1
    assert len(forbidden("m", ["Baldur’s Gate"], banned)) == 1


def test_unknown_values_reports_keys_that_the_book_drops():
    assert len(unknown_values("subclasses", ["bard", "Bard", "warden"], {"bard"})) == 2
    assert unknown_values("feats", ["General"], {"General"}) == []


def test_bad_source_checks_every_file_in_a_new_folder(tmp_path):
    (tmp_path / "npcs").mkdir()
    (tmp_path / "npcs" / "a.py").write_text("X = ['a D&D guard " + chr(0x2014) + " tall']\n")
    (tmp_path / "npcs" / "b.py").write_text("X = ['a beholder friend']\n")
    errors = bad_source(str(tmp_path), {"beholder"})
    assert len(errors) == 3


def test_unregistered_packages_are_reported(tmp_path):
    for name in ("monsters", "npcs"):
        (tmp_path / name).mkdir()
        (tmp_path / name / "__init__.py").write_text("")
    (tmp_path / "__pycache__").mkdir()
    assert unregistered_packages(str(tmp_path), {"monsters"}) == ["content: the package 'npcs' is not registered in check_content.REGISTRY"]
