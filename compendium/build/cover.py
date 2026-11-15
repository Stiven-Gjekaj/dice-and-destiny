"""Full-colour wraparound paperback covers: back | spine | front, A4 trim with 3 mm bleed."""
import sys, subprocess, os
from pypdf import PdfReader
from icons import big_d20, icon

BLEED, W, H = 3.0, 210.0, 297.0
MM_PER_PAGE = 0.0572  # typical 50–60 lb white paper; confirm with your printer's spine calculator

BOOKS = {
 "gm": dict(title="The Game Master's Compendium", t1="The Game Master's", t2="Compendium",
   sub="Run the game. Know every monster. Reward every hero.",
   back="Everything you need behind the screen, in one book.",
   bullets=["A plain-language guide to running your first table — and your hundredth", "Combat, conditions, resting, travel and encounter-building, explained with examples",
            "A complete bestiary: all 331 monsters and animals of the 2024 System Reference Document with full stat blocks",
            "Every SRD magic item with full descriptions, indexed by rarity", "166 original monsters, 250 original magic items and a stronghold system",
            "Poisons, an NPC generator, random complications, trackers and session prep sheets"],
   icons=["crown", "dragon", "chest", "scroll"]),
 "player": dict(title="The Player's Compendium", t1="The Player's", t2="Compendium",
   sub="Build a hero. Learn the rules. Master your class.",
   back="From your first roll to level 20 — every rule a player needs.",
   bullets=["A friendly guide to dice, abilities, combat, magic and leveling up", "All twelve classes with level tables, plain-English feature guides and the complete official rules text",
            "Every species, background and feat of the 2024 System Reference Document", "All 339 spells with full descriptions, plus spell lists for every class",
            "Expanded options: 36 original subclasses, new species, backgrounds, feats and 47 new spells",
            "Equipment, the complete rules reference, conditions, a glossary and a blank character sheet"],
   icons=["swords", "spark", "fighter", "book"]),
}


def cover_html(name, pages):
    b = BOOKS[name]
    spine = round(pages * MM_PER_PAGE, 1)
    tw, th = 2 * W + spine + 2 * BLEED, H + 2 * BLEED
    ic = "".join(f'<span class="cb">{icon(i, 22, "#d6aa55", 1.4)}</span>' for i in b["icons"])
    bl = "".join(f"<li>{x}</li>" for x in b["bullets"])
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: {tw}mm {th}mm; margin: 0; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; width: {tw}mm; height: {th}mm; position: relative; overflow: hidden; font-family: "Bitstream Charter", serif;
  background: radial-gradient(ellipse at 78% 38%, #4a1913 0%, #22100c 55%, #140806 100%); color: #f3e6cc; }}
.panel {{ position: absolute; top: {BLEED}mm; height: {H}mm; }}
.back {{ left: {BLEED}mm; width: {W}mm; }}
.spine {{ left: {BLEED + W}mm; width: {spine}mm; }}
.front {{ left: {BLEED + W + spine}mm; width: {W}mm; }}
.frame {{ position: absolute; inset: 12mm; border: 1.2pt solid #c99a3e; outline: .5pt solid #c99a3e; outline-offset: -3.5mm; }}
.front .inner {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0 26mm; }}
.kicker {{ font-family: Inter, sans-serif; letter-spacing: .32em; font-size: 9pt; color: #c99a3e; text-transform: uppercase; margin-bottom: 10mm; }}
h1 {{ font-family: "GFS Baskerville", Caladea, serif; font-weight: normal; font-size: 44pt; line-height: 1.02; margin: 0; color: #f6e7c8; }}
.compat {{ font-family: Inter, sans-serif; letter-spacing: .12em; font-size: 8pt; color: #c99a3e; text-transform: uppercase; margin-top: 8mm; }}
.subt {{ font-style: italic; font-size: 13pt; color: #e2cfa8; margin-top: 10mm; }}
.icons {{ display: flex; gap: 5mm; justify-content: center; margin-top: 12mm; }}
.cb {{ width: 11mm; height: 11mm; border-radius: 50%; border: 1pt solid #c99a3e; display: inline-flex; align-items: center; justify-content: center; }}
.foot {{ position: absolute; bottom: 22mm; left: 0; right: 0; text-align: center; font-family: Inter, sans-serif; font-size: 7.5pt; letter-spacing: .12em; color: #b9a27a; text-transform: uppercase; }}
.back .inner {{ position: absolute; inset: 26mm 24mm; }}
.back h2 {{ font-family: Caladea, serif; color: #f6e2b8; font-size: 23pt; margin: 0 0 6mm; line-height: 1.2; }}
.back ul {{ padding-left: 5mm; font-size: 12.5pt; line-height: 1.5; color: #ead9b6; }}
.back li {{ margin-bottom: 4mm; }}
.back .rule {{ border-top: .8pt solid #c99a3e; width: 40mm; margin: 8mm 0; }}
.back .small {{ font-size: 7.5pt; color: #b9a27a; line-height: 1.45; position: absolute; bottom: 0; left: 0; width: 110mm; }}
.barcode {{ position: absolute; right: 0; bottom: 0; width: 50mm; height: 30mm; background: #fff; }}
.spine .st {{ position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%) rotate(90deg); white-space: nowrap;
  font-family: Caladea, serif; font-size: {min(11, spine * 1.6):.1f}pt; color: #f6e2b8; letter-spacing: .06em; }}
.spine .st span {{ color: #c99a3e; margin: 0 3mm; }}
.spine::before, .spine::after {{ content: ""; position: absolute; left: 0; right: 0; border-top: .8pt solid #c99a3e; }}
.spine::before {{ top: 18mm; }} .spine::after {{ bottom: 18mm; }}
</style></head><body>
<div class="panel back"><div class="frame"></div><div class="inner">
  <h2>{b["back"]}</h2><ul>{bl}</ul><div class="rule"></div>
  <p style="font-style:italic;color:#e2cfa8;font-size:10pt">Fifth Edition · 2024 Rules · Unofficial reference for players and Game Masters.</p>
  <div class="small">Includes material from the System Reference Document 5.2 by Wizards of the Coast LLC, licensed under CC-BY-4.0. Not affiliated with or endorsed by Wizards of the Coast.</div>
  <div class="barcode"></div>
</div></div>
<div class="panel spine"><div class="st">Dice &amp; Destiny<span>◆</span>{b["title"]}</div></div>
<div class="panel front"><div class="frame"></div><div class="inner">
  <div class="kicker">Dice &amp; Destiny</div>
  <h1>{b["t1"]}<br>{b["t2"]}</h1>
  <div style="margin-top:12mm">{big_d20(230)}</div>
  <div class="subt">{b["sub"]}</div>
  <div class="compat">A rules-compatible guide for fifth edition (2024)</div>
  <div class="icons">{ic}</div>
</div><div class="foot">Unofficial Reference · {pages} pages</div></div>
</body></html>''', spine, tw, th


if __name__ == "__main__":
    for n in sys.argv[1:]:
        pages = len(PdfReader(f"{n}.pdf").pages)
        h, spine, tw, th = cover_html(n, pages)
        open(f"{n}_cover.html", "w").write(h)
        subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={os.getcwd()}/{n}_cover.pdf", f"file://{os.getcwd()}/{n}_cover.html"],
                       stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        print(n, f"{pages} pages, spine {spine} mm, cover {tw:.1f} × {th:.1f} mm")
