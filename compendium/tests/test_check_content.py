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
    # 4d6 (14) is above the level 1 area cap 10 times 1.25, but not above the single-target cap 14 times 1.25.
    assert len(spell_damage_too_high("T", 1, "takes 4d6 Fire damage", True)) == 1
    assert spell_damage_too_high("T", 1, "takes 4d6 Fire damage", False) == []


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


def test_level_9_single_target_curve_matches_power_word_kill():
    # Power Word Kill ends a creature with 100 Hit Points or fewer, so the level 9 curve is 99.
    assert spell_damage_too_high("T", 9, "takes 20d10 Force damage", False) == []
    assert len(spell_damage_too_high("T", 9, "takes 30d10 Force damage", False)) == 1


def test_every_srd_spell_passes_the_curve():
    # The curve must not be stricter than the free rules that the books print.
    import json
    import os
    from check_content import is_area
    path = os.path.join(os.path.dirname(__file__), "..", "data", "all_spells.json")
    failures = []
    for s in json.load(open(path)):
        failures += spell_damage_too_high(s["name"], s["level"], s["desc"], is_area(s["desc"]))
    assert failures == []


from check_content import background_feat_errors, srd_origin_feats


def _background(name, feat):
    return (name, "Strength, Dexterity, Constitution", "Athletics, Stealth", "Gaming Set", feat, "Rope, 10 GP", "flavor")


def test_background_with_an_origin_feat_passes():
    assert background_feat_errors([_background("Diver", "Hardy")], {"Hardy"}) == []


def test_background_feat_ignores_the_note_in_parentheses():
    assert background_feat_errors([_background("Acolyte", "Magic Initiate (Cleric)")], {"Magic Initiate"}) == []


def test_background_with_an_unknown_feat_fails():
    errors = background_feat_errors([_background("Diver", "Deep Breath")], {"Hardy"})
    assert len(errors) == 1 and "Diver" in errors[0] and "Deep Breath" in errors[0]


def test_srd_origin_feats_include_the_four_srd_feats():
    assert {"Alert", "Magic Initiate", "Savage Attacker", "Skilled"} <= srd_origin_feats()


from check_content import spell_class_level_errors


def _spell(name, level, classes):
    return (name, level, "Evocation", classes, "Action", "60 feet", "V", "Instantaneous", False, False, "text", None)


def test_half_caster_spell_above_level_5_fails():
    errors = spell_class_level_errors([_spell("Big Wall", 6, ["Druid", "Ranger"])])
    assert len(errors) == 1 and "Big Wall" in errors[0] and "Ranger" in errors[0]


def test_half_caster_spell_at_level_5_passes():
    assert spell_class_level_errors([_spell("Small Wall", 5, ["Paladin", "Ranger"])]) == []


def test_full_caster_spell_above_level_5_passes():
    assert spell_class_level_errors([_spell("Big Wall", 9, ["Wizard"])]) == []
