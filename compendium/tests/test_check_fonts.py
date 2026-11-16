"""Tests for build/check_fonts.py. Each test builds its own pdffonts output."""
from check_fonts import problems

HEADER = ("name                                 type              encoding         emb sub uni object ID\n"
          "------------------------------------ ----------------- ---------------- --- --- --- ---------\n")


def fonts(*rows):
    return HEADER + "".join(f"{n:<36} {t:<17} Identity-H       yes yes yes      4  0\n" for n, t in rows)


def test_allowed_truetype_fonts_pass():
    assert problems(fonts(("AAAAAA+Caladea-Regular", "CID TrueType"), ("BAAAAA+Inter-Bold", "CID TrueType"))) == []


def test_a_type3_font_fails_even_when_the_family_is_allowed():
    assert len(problems(fonts(("AAAAAA+Inter-Regular", "Type 3")))) == 1


def test_an_unknown_family_fails():
    assert len(problems(fonts(("AAAAAA+DejaVuSerif", "CID TrueType")))) == 1
