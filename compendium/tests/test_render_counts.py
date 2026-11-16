"""Tests for render_counts. Each test builds its own small lists."""
from render_counts import gm_counts, player_counts


def test_gm_counts_count_each_list():
    text = gm_counts(["m"] * 3, [("Cultists", "n")] * 2, ["i"] * 5)
    assert "3 new monsters" in text
    assert "2 people" in text
    assert "5 new magic items" in text


def test_gm_counts_work_with_empty_lists():
    assert "0 new monsters and 0 people" in gm_counts([], [], [])


def test_player_counts_add_the_subclasses_of_all_classes():
    text = player_counts(["c1", "c2"], {"Fighter": ["a", "b"], "Wizard": ["c"]})
    assert text == "2 new classes, 3 new subclasses"


from render_counts import origin_counts, spell_counts


def test_origin_counts_count_backgrounds_and_species():
    assert origin_counts(["b"] * 4, ["s"] * 2) == "4 new backgrounds and 2 new species"


def test_spell_counts_count_the_spells():
    assert spell_counts(["a", "b", "c"]) == "3 new spells"
