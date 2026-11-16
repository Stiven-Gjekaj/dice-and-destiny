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


def test_im_fell_english_of_the_maps_passes():
    rows = [("AAAAAA+IM_FELL_English_Roman", "CID TrueType"), ("BAAAAA+IM_FELL_English_Italic", "CID TrueType"),
            ("CAAAAA+IM_FELL_English_SC", "TrueType")]
    assert problems(fonts(*rows)) == []


def test_another_new_family_still_fails_next_to_im_fell_english():
    rows = [("AAAAAA+IM_FELL_English_Roman", "CID TrueType"), ("BAAAAA+EBGaramond-Regular", "CID TrueType")]
    assert problems(fonts(*rows)) == ["uses EBGaramond"]


def test_im_fell_english_as_type3_fails():
    assert problems(fonts(("AAAAAA+IM_FELL_English_Roman", "Type 3"))) == ["has IM_FELL_English_Roman as a Type 3 font"]
