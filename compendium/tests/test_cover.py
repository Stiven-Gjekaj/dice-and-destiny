"""Tests for the cover sizes. The hardcover numbers come from the Lulu cover template
for an A4 casewrap hardcover with 196 pages (uploaded by the human, 2026-11-15)."""
import pytest

from cover import cover_size


def test_paperback_size_is_unchanged():
    g = cover_size(196, "paperback")
    assert g["spine_mm"] == pytest.approx(11.2, abs=0.05)
    assert g["width_mm"] == pytest.approx(2 * 210 + 11.2 + 2 * 3, abs=0.05)
    assert g["height_mm"] == pytest.approx(303, abs=0.05)


def test_hardcover_matches_the_lulu_template_at_196_pages():
    g = cover_size(196, "hardcover")
    assert g["spine_mm"] == pytest.approx(19.05, abs=0.05)
    assert g["width_mm"] == pytest.approx(483.62, abs=0.5)
    assert g["height_mm"] == pytest.approx(341.38, abs=0.5)
    assert g["edge_mm"] == pytest.approx(15.87, abs=0.05)
    assert g["safe_mm"] == pytest.approx(15.87, abs=0.05)
    assert (g["barcode_w_mm"], g["barcode_h_mm"]) == (92, 32)


def test_hardcover_spine_grows_with_the_page_count():
    assert cover_size(400, "hardcover")["spine_mm"] > cover_size(196, "hardcover")["spine_mm"]


def test_hardcover_refuses_a_page_count_that_lulu_does_not_print():
    with pytest.raises(ValueError):
        cover_size(801, "hardcover")
