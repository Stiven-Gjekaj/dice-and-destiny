"""Tests for the icons. The interior is printed in black and white at Lulu, so its art has no transparency."""
from icons import big_d20


def test_flat_d20_has_no_transparency():
    svg = big_d20(150, "#111", flat=True)
    for word in ("opacity", "filter", "glow"):
        assert word not in svg


def test_cover_d20_keeps_its_glow():
    assert "glow" in big_d20(230)
