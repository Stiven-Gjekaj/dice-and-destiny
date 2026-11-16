"""Tests for the content of Act I of The Dawnwatch, Book One.

Each test asks the engine or the checks about the entries of the act1 files.
"""
import re

from check_content import monster_out_of_band
from content.dawnwatch import creatures_act1

PLACEHOLDER = re.compile(r"\{(?:dc|atk):\w+\}|\{\d+d\d+")


def test_act1_creatures_are_inside_the_bands_of_their_cr():
    for m in creatures_act1.MON:
        assert monster_out_of_band(m) == [], m.name


def test_act1_creatures_render_with_no_placeholder_left():
    for m in creatures_act1.MON:
        html = m.html()
        assert m.name in html
        assert not PLACEHOLDER.search(html), m.name


def test_the_hush_has_three_tiers_that_grow_in_cr():
    tiers = [m.cr for m in creatures_act1.MON if m.name.startswith("Hush ")]
    assert len(tiers) == 3
    assert tiers == sorted(tiers) and len(set(tiers)) == 3


def test_act1_people_with_statblocks_are_inside_their_bands_and_render():
    from content.dawnwatch import people_act1
    fighters = [m for _, m in people_act1.NPCS if not isinstance(m, str)]
    assert fighters
    for m in fighters:
        assert monster_out_of_band(m) == [], m.name
        assert not PLACEHOLDER.search(m.html()), m.name


def test_each_act1_person_has_a_role_and_a_name():
    from content.dawnwatch import people_act1
    for role, person in people_act1.NPCS:
        name = person if isinstance(person, str) else person.name
        assert role.strip() and name.strip()


def test_act1_treasures_use_known_rarities_and_plain_text():
    from check_content import RARITIES
    from content.dawnwatch import treasures_act1
    for name, category, rarity, attunement, text in treasures_act1.ITEMS:
        assert rarity in RARITIES, name
        # The item renderer escapes the text, so a tag would print as text.
        assert "<" not in text, name
