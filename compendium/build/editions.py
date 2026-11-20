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

import cover
from cover import BOOKS, PALETTES

def front_page_html(name, theme):
    """An A4 front cover page, with the design of the front of the printed cover. theme is "color" or "bw"."""
    b = BOOKS[name]
    if theme == "color":
        pal = PALETTES[name]
        bg = "radial-gradient(ellipse at 50% 38%, {} 0%, {} 55%, {} 100%)".format(*pal["bg"])
        colors = dict(ink="#f3e6cc", soft="#e2cfa8", accent=pal["accent"], ground=pal["bg"][1], disc=pal["bg"][2])
    else:
        # Black ink on white paper only: no grey that a home printer can fade.
        bg = "#fff"
        colors = dict(ink="#000", soft="#000", accent="#000", ground="#fff", disc="#fff")
    frame = 12
    pad = frame + cover.FRAME_GAP_MM + cover.CLEAR_MM
    top = frame + cover.CUT_MM + cover.CLEAR_MM
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 0; }}
{cover.FONTS}
:root {{ --ink: {colors["ink"]}; --soft: {colors["soft"]}; --acc: {colors["accent"]}; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; width: 210mm; height: 297mm; position: relative; overflow: hidden; background: {bg}; color: {colors["ink"]};
  font-family: Caladea, serif; }}
.frame {{ position: absolute; left: {frame}mm; top: {frame}mm; }}
{cover.STACK_CSS}
.stack {{ top: {top:g}mm; bottom: {top:g}mm; left: {pad:g}mm; right: {pad:g}mm; }}
</style></head><body>{cover.frame_svg(210 - 2 * frame, 297 - 2 * frame, colors["accent"])}{cover.front_html(b, name, colors)}</body></html>'''


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
