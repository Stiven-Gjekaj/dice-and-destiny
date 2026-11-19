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


def test_fill_counts_puts_each_count_into_the_text():
    from cover import fill_counts
    text = fill_counts("Options: {PLAYER_COUNTS} and {SPELL_COUNTS}",
                       {"{PLAYER_COUNTS}": "2 new classes", "{SPELL_COUNTS}": "9 new spells"})
    assert text == "Options: 2 new classes and 9 new spells"


def test_cover_bullets_have_no_counts_written_by_hand():
    import re
    from cover import BOOKS
    for book in BOOKS.values():
        for bullet in book["bullets"]:
            for match in re.finditer(r"\d+ (?:original|new) ", bullet):
                raise AssertionError(f"a count written by hand: {match.group(0)!r} in {bullet!r}")


def test_the_dawnwatch_counts_come_from_the_content():
    import types
    from cover import dawnwatch_counts
    dw = types.SimpleNamespace(MON=[1, 2], NPCS=[1], ITEMS=[])
    assert dawnwatch_counts(dw) == {"{DW_COUNTS}": "2 new creatures, 1 person, and 0 treasures"}


def test_the_waking_cover_says_that_it_needs_edition_2_and_the_compendiums_do_not():
    from cover import cover_html
    waking = cover_html("waking", 120, "hardcover")[0]
    assert "Requires Edition 2" in waking and "{DW_COUNTS}" not in waking and "The Dawnwatch" in waking
    for book in ("player", "gm"):
        h = cover_html(book, 300, "paperback")[0]
        assert "Requires Edition" not in h and "A rules-compatible guide for fifth edition (2024)" in h


def test_the_waking_spine_gives_the_full_title():
    import re
    from cover import cover_html
    for kind in ("paperback", "hardcover"):
        h = cover_html("waking", 310, kind)[0]
        spine = re.search(r'<div class="panel spine">(.*?)</div></div>', h).group(1)
        assert "The Dawnwatch, Book One: Waking" in spine
