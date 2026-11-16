"""Tests for the inside (spine) margin of the black and white print interior.

The numbers come from the Lulu gutter table (recommended interior margin, no bleed):
https://help.lulu.com/en/support/solutions/articles/64000255590-interior-formatting-the-basics
"""
import pytest
from build import lulu_inside_mm, margin_css, expand, INSIDE_MM


@pytest.mark.parametrize("pages, mm", [
    (24, 13), (60, 13), (61, 16), (150, 16), (151, 25), (400, 25), (401, 29), (600, 29), (601, 32), (800, 32),
])
def test_inside_margin_follows_the_lulu_table(pages, mm):
    assert lulu_inside_mm(pages) == mm


def test_margin_css_sets_the_inside_margin_on_both_page_sides():
    css = margin_css(29)
    assert "@page :right { margin-left: 29mm; }" in css
    assert "@page :left { margin-right: 29mm; }" in css


def test_margin_css_keeps_title_pages_in_the_middle_of_the_paper():
    # The outside margin is 14 mm. The extra right margin is inside minus outside.
    # Two rules, not one list: a text step in expand() removes ", ." from the page.
    css = margin_css(29)
    assert ".titlepage { margin-right: 15mm; }" in css
    assert ".part { margin-right: 15mm; }" in css


def test_print_interior_gets_the_inside_margin_of_its_book():
    for name in ("player", "gm"):
        assert margin_css(INSIDE_MM[name]) in expand(name, screen=False)


def test_screen_edition_keeps_even_margins():
    for name in ("player", "gm"):
        assert margin_css(INSIDE_MM[name]) not in expand(name, screen=True)
