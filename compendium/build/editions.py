"""Make the screen and home-print PDFs of each book.

  screen      A4 front cover in color, then the color interior with links and bookmarks.
  home print  A4 front cover in black and white, a blank back, then the black and white interior.

The Lulu hardcover uses the black and white interior and the hardcover cover as they are.

Usage: python3 editions.py BOOK [BOOK ...]
  Needs BOOK.pdf (print interior) and BOOK_screen.pdf (screen interior).
  Makes BOOK_front_color.pdf, BOOK_front_bw.pdf, BOOK_screen_edition.pdf, and BOOK_home_print.pdf.
"""
import os
import subprocess
import sys

from pypdf import PdfReader, PdfWriter

from cover import BOOKS, COMPAT
from icons import big_d20, icon

FONTS = "\n".join(
    f'@font-face {{ font-family: "Inter"; src: url("books/fonts/Inter-{f}.ttf") format("truetype"); '
    f'font-weight: {w}; font-style: {s}; }}'
    for f, w, s in (("Regular", 400, "normal"), ("Italic", 400, "italic"), ("SemiBold", 600, "normal"), ("Bold", 700, "normal")))

# Color: the design of the front of the printed cover. Black and white: black ink on white paper only.
THEMES = {
    "color": dict(bg="radial-gradient(ellipse at 50% 38%, #4a1913 0%, #22100c 55%, #140806 100%)", ink="#f6e7c8",
                  accent="#c99a3e", soft="#e2cfa8"),
    "bw": dict(bg="#fff", ink="#000", accent="#000", soft="#000"),
}


def front_page_html(name, theme):
    """An A4 front cover page. theme is "color" or "bw"."""
    b, t = BOOKS[name], THEMES[theme]
    d20 = big_d20(200) if theme == "color" else big_d20(200, "#000", flat=True)
    if theme == "bw":
        # Flat black outline and white faces: no grey that a home printer can fade.
        import re
        d20 = re.sub(r"<defs>.*?</defs>", "", d20, flags=re.S)
        d20 = re.sub(r'fill="#[0-9a-fA-F]{6}"', 'fill="#fff"', d20)
        d20 = d20.replace('fill="url(#face)"', 'fill="#fff"')
        d20 = re.sub(r'(<text[^>]*?)fill="#fff"', r'\1fill="#000"', d20)
    ic = "".join(f'<span class="cb">{icon(i, 22, t["accent"], 1.4)}</span>' for i in b["icons"])
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 0; }}
{FONTS}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; width: 210mm; height: 297mm; position: relative; overflow: hidden; background: {t["bg"]}; color: {t["ink"]}; }}
.frame {{ position: absolute; inset: 12mm; border: 1.2pt solid {t["accent"]}; outline: .5pt solid {t["accent"]}; outline-offset: -3.5mm; }}
.inner {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0 26mm; }}
.kicker {{ font-family: Inter, sans-serif; letter-spacing: .32em; font-size: 9pt; color: {t["accent"]}; text-transform: uppercase; margin-bottom: 10mm; }}
h1 {{ font-family: "GFS Baskerville", Caladea, serif; font-weight: normal; font-size: 44pt; line-height: 1.02; margin: 0; color: {t["ink"]}; }}
.subt {{ font-family: Caladea, serif; font-style: italic; font-size: 13pt; color: {t["soft"]}; margin-top: 10mm; }}
.compat {{ font-family: Inter, sans-serif; letter-spacing: .12em; font-size: 8pt; color: {t["accent"]}; text-transform: uppercase; margin-top: 8mm; }}
.icons {{ display: flex; gap: 5mm; justify-content: center; margin-top: 12mm; }}
.cb {{ width: 11mm; height: 11mm; border-radius: 50%; border: 1pt solid {t["accent"]}; display: inline-flex; align-items: center; justify-content: center; }}
</style></head><body><div class="frame"></div><div class="inner">
  <div class="kicker">Dice &amp; Destiny</div>
  <h1>{b["t1"]}<br>{b["t2"]}</h1>
  <div style="margin-top:12mm">{d20}</div>
  <div class="subt">{b["sub"]}</div>
  <div class="compat">{b.get("compat", COMPAT)}</div>
  <div class="icons">{ic}</div>
</div></body></html>'''


def render_front(name, theme):
    out = f"{name}_front_{theme}"
    open(f"{out}.html", "w").write(front_page_html(name, theme))
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.getcwd()}/{out}.pdf", f"file://{os.getcwd()}/{out}.html"],
                   stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, timeout=300)
    return f"{out}.pdf"


def join(out, front, interior, blank_back=False):
    """Write front + (a blank page) + interior to out. Keep the bookmarks of the interior, moved by the new pages."""
    w = PdfWriter()
    f = PdfReader(front)
    w.append(f)
    if blank_back:
        box = f.pages[0].mediabox
        w.add_blank_page(width=box.width, height=box.height)
    inside = PdfReader(interior)
    w.append(inside, import_outline=True)
    if inside.outline:
        w.page_mode = "/UseOutlines"
    with open(out, "wb") as fh:
        w.write(fh)
    return out


def main(names):
    for n in names:
        join(f"{n}_screen_edition.pdf", render_front(n, "color"), f"{n}_screen.pdf")
        join(f"{n}_home_print.pdf", render_front(n, "bw"), f"{n}.pdf", blank_back=True)
        print(n, "screen and home-print PDFs done")


if __name__ == "__main__":
    main(sys.argv[1:])
