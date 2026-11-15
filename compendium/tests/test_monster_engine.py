"""Tests for the monster names in the text of build/monster_engine.py."""
from monster_engine import M


def _monster(name):
    return M(name, "M", "Beast", "Unaligned", 5, "16 12 14 3 10 5",
             attacks=[("Bite", "m", "1d8", "Piercing")], multi=2,
             leg=[("Bite", "The beast makes one Bite attack.")])


def test_name_that_starts_with_the_prints_one_article():
    text = _monster("The Test Beast").html()
    assert "The test beast makes two attacks" in text
    assert "the test beast can expend a use" in text
    assert "the the" not in text.lower()


def test_normal_name_is_unchanged():
    text = _monster("Test Beast").html()
    assert "The test beast makes two attacks" in text
    assert "the test beast can expend a use" in text


def test_word_the_inside_a_name_is_kept():
    text = _monster("Wolf of the Long Winter").html()
    assert "The wolf of the long winter makes two attacks" in text
