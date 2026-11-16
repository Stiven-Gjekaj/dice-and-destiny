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
