"""Tests for the screen version of the books: links in the contents and bookmarks."""
from pypdf import PdfReader, PdfWriter

import build


def test_a_marker_has_an_id_that_a_link_can_find():
    build.TOC.clear()
    html = build.marker("ch", "1. Rolling Dice")
    assert html == '<span class="mark" id="t0">@@T0@@</span>'


def test_the_screen_contents_link_to_the_markers():
    build.TOC[:] = [("ch", "1. Rolling Dice", "@@T0@@")]
    linked = build.toc_html({"@@T0@@": 7}, links=True)
    plain = build.toc_html({"@@T0@@": 7})
    assert '<a href="#t0">1. Rolling Dice</a>' in linked
    assert "<a " not in plain


def test_the_outline_puts_chapters_under_parts_and_classes_under_chapters():
    entries = [("part", "Part I · Basics", "@@T0@@"), ("ch", "1. Rolling &amp; Dice", "@@T1@@"),
               ("sub", "Bard", "@@T2@@"), ("ch", "2. Missing", "@@T3@@")]
    items = build.outline(entries, {"@@T0@@": 3, "@@T1@@": 4, "@@T2@@": 9})
    assert items == [(0, "Part I · Basics", 2), (1, "1. Rolling & Dice", 3), (2, "Bard", 8)]


def test_the_bookmarks_are_written_into_the_pdf(tmp_path):
    w = PdfWriter()
    for _ in range(4):
        w.add_blank_page(100, 100)
    pdf = tmp_path / "book.pdf"
    with open(pdf, "wb") as f:
        w.write(f)
    build.add_outline(str(pdf), [(0, "Part I", 0), (1, "Chapter 1", 1), (1, "Chapter 2", 2), (0, "Part II", 3)])
    r = PdfReader(str(pdf))
    top = [o for o in r.outline if not isinstance(o, list)]
    assert [o.title for o in top] == ["Part I", "Part II"]
    children = r.outline[1]
    assert [o.title for o in children] == ["Chapter 1", "Chapter 2"]
    assert r.get_destination_page_number(children[1]) == 2
