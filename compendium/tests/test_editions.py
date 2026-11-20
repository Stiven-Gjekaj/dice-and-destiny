"""Tests for the screen and home-print editions."""
import re

from pypdf import PdfReader, PdfWriter

import editions


def _pdf(path, pages, outline=None):
    w = PdfWriter()
    for _ in range(pages):
        w.add_blank_page(595, 842)
    for title, page in outline or []:
        w.add_outline_item(title, page)
    with open(path, "wb") as f:
        w.write(f)
    return str(path)


def test_the_screen_edition_is_the_cover_then_the_interior_with_its_bookmarks(tmp_path):
    front = _pdf(tmp_path / "front.pdf", 1)
    inside = _pdf(tmp_path / "inside.pdf", 5, [("Part I", 0), ("Part II", 3)])
    out = editions.join(str(tmp_path / "out.pdf"), front, inside)
    r = PdfReader(out)
    assert len(r.pages) == 6
    assert [o.title for o in r.outline] == ["Part I", "Part II"]
    # Each bookmark moves one page, past the cover.
    assert [r.get_destination_page_number(o) for o in r.outline] == [1, 4]


def test_the_home_print_has_a_blank_back_so_the_interior_starts_on_a_front_side(tmp_path):
    front = _pdf(tmp_path / "front.pdf", 1)
    inside = _pdf(tmp_path / "inside.pdf", 3)
    r = PdfReader(editions.join(str(tmp_path / "out.pdf"), front, inside, blank_back=True))
    assert len(r.pages) == 5
    assert r.pages[1].extract_text() == ""


def test_the_black_and_white_front_page_has_no_color_or_grey():
    html = editions.front_page_html("player", "bw")
    colors = {c.lower() for c in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", html)}
    assert colors <= {"#000", "#fff", "#000000", "#ffffff"}, colors
    assert "gradient" not in html


def test_the_color_front_page_names_the_book():
    html = editions.front_page_html("gm", "color")
    assert "The Game Master's<br>Compendium" in html
    assert "size: A4" in html


def test_the_waking_front_page_has_its_own_compat_line():
    from editions import front_page_html
    h = front_page_html("waking", "color")
    assert "Book One: Waking" in h and "Requires Edition 2" in h


def test_the_color_front_page_has_the_colors_of_its_cover():
    import cover
    for name in cover.BOOKS:
        html = editions.front_page_html(name, "color")
        assert cover.PALETTES[name]["bg"][0] in html
        assert cover.PALETTES[name]["accent"] in html
