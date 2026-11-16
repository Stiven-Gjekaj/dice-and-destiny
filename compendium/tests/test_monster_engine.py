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


def test_thrown_attack_uses_strength_and_a_range():
    m = M("Test Thrower", "H", "Giant", "Unaligned", 7, "23 8 20 8 12 8",
          attacks=[("Club", "m", "3d8", "Bludgeoning"), ("Rock", "t", "3d10", "Bludgeoning", "", "60/240 ft.")], multi=2)
    text = m.html()
    # PB +3 and Str +6: the attack bonus is +9 and the damage bonus is +6. Dex (-1) is not used.
    assert "Rock.</i></b> <i>Ranged Attack Roll:</i> +9, range 60/240 ft. <i>Hit:</i> 22 (3d10 + 6) Bludgeoning damage." in text


def test_thrown_attack_has_a_default_range():
    m = M("Test Thrower", "M", "Humanoid", "Neutral", 1, "14 10 12 10 10 10",
          attacks=[("Javelin", "t", "1d6", "Piercing")])
    assert "range 20/60 ft." in m.html()
