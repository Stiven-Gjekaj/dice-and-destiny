"""IM Fell English, the font of the map labels, embeds as TrueType when Chrome prints a page with waking.css.

The test prints its own small page with an SVG label. It needs Chrome and pdffonts, as the build does.
"""
import os
import re
import shutil
import subprocess

import pytest

from check_fonts import fonts, problems

BOOKS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "books")
FACE = re.compile(r'font-family: "([^"]+)"; src: url\("fonts/([^"]+)"\)')


def test_each_im_fell_face_in_waking_css_points_to_a_file_in_the_folder():
    css = open(os.path.join(BOOKS, "waking.css"), encoding="utf-8").read()
    faces = FACE.findall(css)
    assert {f for f, _ in faces} == {"IM Fell English", "IM Fell English SC"}
    for _, path in faces:
        assert os.path.isfile(os.path.join(BOOKS, "fonts", path)), path
    assert os.path.isfile(os.path.join(BOOKS, "fonts", "OFL-IMFellEnglish.txt"))


@pytest.mark.skipif(not (shutil.which("google-chrome") and shutil.which("pdffonts")), reason="needs Chrome and pdffonts")
def test_a_map_label_in_im_fell_english_embeds_as_truetype(tmp_path):
    css = os.path.abspath(os.path.join(BOOKS, "waking.css"))
    page = tmp_path / "map.html"
    page.write_text(
        f'<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="file://{css}">'
        '<svg xmlns="http://www.w3.org/2000/svg" width="100mm" height="40mm" viewBox="0 0 100 40">'
        '<text x="5" y="12" font-family="IM Fell English" font-size="8" fill="#000">Kingsholm</text>'
        '<text x="5" y="24" font-family="IM Fell English" font-style="italic" font-size="8" fill="#000">The Grey Teeth</text>'
        '<text x="5" y="36" font-family="IM Fell English SC" font-size="8" fill="#000">Ostrey</text></svg>')
    pdf = tmp_path / "map.pdf"
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", f"file://{page}"], capture_output=True, timeout=120)
    out = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True, check=True).stdout
    found = {family: kind for family, kind in fonts(out)}
    assert set(found) == {"IM_FELL_English_Roman", "IM_FELL_English_Italic", "IM_FELL_English_SC"}, out
    assert problems(out) == []
