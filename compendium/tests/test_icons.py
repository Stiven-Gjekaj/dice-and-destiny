"""Tests for the icons. The interior is printed in black and white at Lulu, so its art has no transparency."""
from icons import big_d20


def test_flat_d20_has_no_transparency():
    svg = big_d20(150, "#111", flat=True)
    for word in ("opacity", "filter", "glow"):
        assert word not in svg


def test_cover_d20_keeps_its_glow():
    assert "glow" in big_d20(230)


def test_d20_numbers_have_no_outline():
    # Chrome prints outlined text as a Type 3 font, and Lulu warns about Type 3 fonts.
    for svg in (big_d20(230), big_d20(150, "#111", flat=True)):
        assert 'stroke-width=".4">20' not in svg
