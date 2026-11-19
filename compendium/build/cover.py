"""Full-colour wraparound covers: back | spine | front.

Two kinds:
  paperback  A4 trim with 3 mm bleed.
  hardcover  Lulu A4 casewrap: boards, a wrap around the edges, and a safety margin.
"""
import sys, subprocess, os
from pypdf import PdfReader
from icons import big_d20, icon

BLEED, W, H = 3.0, 210.0, 297.0
MM_PER_PAGE = 0.0572  # typical 50–60 lb white paper; confirm with your printer's spine calculator

# Lulu A4 casewrap hardcover, from the Lulu cover template (196 pages, uploaded 2026-11-15).
HC_TRIM_W, HC_TRIM_H = 216.41, 309.63   # the board, larger than A4
HC_WRAP = 15.87                         # wrap around each edge
HC_SAFE = 15.87                         # safety margin inside the board edge
HC_BARCODE = (92, 32)                   # mm, at the bottom of the back cover, HC_SAFE from the spine
# Lulu casewrap spine width in inches, by the highest page count of each step.
# The template confirms 0.75 in at 196 pages. Confirm other steps with a Lulu template.
HC_SPINE_IN = [(84, .25), (140, .5), (168, .625), (194, .688), (222, .75), (250, .813), (278, .875),
               (306, .938), (334, 1.0), (360, 1.063), (388, 1.125), (416, 1.188), (444, 1.25),
               (472, 1.313), (500, 1.375), (528, 1.438), (556, 1.5), (584, 1.563), (612, 1.625),
               (640, 1.688), (668, 1.75), (696, 1.813), (724, 1.875), (752, 1.938), (780, 2.0),
               (800, 2.063)]


def cover_size(pages, kind):
    """The geometry of a cover in mm. edge_mm is the bleed (paperback) or the wrap (hardcover)."""
    if kind == "paperback":
        spine = round(pages * MM_PER_PAGE, 1)
        return dict(width_mm=2 * W + spine + 2 * BLEED, height_mm=H + 2 * BLEED, spine_mm=spine,
                    edge_mm=BLEED, panel_w_mm=W, panel_h_mm=H, safe_mm=0.0,
                    barcode_w_mm=50, barcode_h_mm=30)
    if kind == "hardcover":
        if not 24 <= pages <= 800:
            raise ValueError(f"Lulu prints a casewrap hardcover with 24 to 800 pages, not {pages}")
        spine = round(next(inch for top, inch in HC_SPINE_IN if pages <= top) * 25.4, 2)
        return dict(width_mm=2 * HC_WRAP + 2 * HC_TRIM_W + spine, height_mm=2 * HC_WRAP + HC_TRIM_H,
                    spine_mm=spine, edge_mm=HC_WRAP, panel_w_mm=HC_TRIM_W, panel_h_mm=HC_TRIM_H,
                    safe_mm=HC_SAFE, barcode_w_mm=HC_BARCODE[0], barcode_h_mm=HC_BARCODE[1])
    raise ValueError(f"unknown cover kind {kind!r}")

BOOKS = {
 "gm": dict(title="The Game Master's Compendium", t1="The Game Master's", t2="Compendium",
   sub="Run the game. Know every monster. Reward every hero.",
   back="Everything you need behind the screen, in one book.",
   bullets=["A plain-language guide to running your first table, and your hundredth", "Combat, conditions, resting, travel and encounter-building, explained with examples",
            "A complete bestiary: all 331 monsters and animals of the 2024 System Reference Document with full stat blocks",
            "Every SRD magic item with full descriptions, indexed by rarity", "{GM_COUNTS}",
            "Poisons, an NPC generator, random complications, trackers and session prep sheets"],
   icons=["crown", "dragon", "chest", "scroll"]),
 "player": dict(title="The Player's Compendium", t1="The Player's", t2="Compendium",
   sub="Build a hero. Learn the rules. Master your class.",
   back="From your first roll to level 20: every rule a player needs.",
   bullets=["A friendly guide to dice, abilities, combat, magic and leveling up", "All twelve classes with level tables, plain-English feature guides and the complete SRD 5.2 rules text",
            "Every species, background and feat of the 2024 System Reference Document", "All 339 spells with full descriptions, plus spell lists for every class",
            "Expanded options: {PLAYER_COUNTS}, new species, backgrounds, feats and {SPELL_COUNTS}",
            "Equipment, the complete rules reference, conditions, a glossary and a blank character sheet"],
   icons=["swords", "spark", "fighter", "book"]),
 "waking": dict(title="The Dawnwatch, Book One: Waking", t1="The Dawnwatch", t2="Book One: Waking",
   sub="Five heroes wake after three hundred years. The world forgot them. Their enemy did not.",
   back="A campaign from level 1 to level 10. It starts in the crypt where the tutorial starts.",
   bullets=["Ten chapters, from the waking in Dawnwatch Keep to the empty crystal in the old capital",
            "Read-aloud text, a box for each new rule, and scaling for 3 to 6 characters in every fight",
            "A player's guide with no spoilers, and a gazetteer of the land of today",
            "{DW_COUNTS}, each in an appendix from A to Z",
            "Maps, handouts on their own pages, and an index of every name"],
   icons=["compass", "dragon", "people", "scroll"],
   compat="A campaign for levels 1 to 10 &middot; Requires Edition 2",
   note="Uses the rules of Dice &amp; Destiny: The Player's Compendium and The Game Master's Compendium, Edition 2."),
}
COMPAT = "A rules-compatible guide for fifth edition (2024)"
NOTE = "Compatible with the fifth edition (2024) rules. For players and Game Masters."


def fill_counts(text, counts):
    """Put each count into the text. `counts` maps a token such as "{SPELL_COUNTS}" to its words."""
    for token, words in counts.items():
        text = text.replace(token, words)
    return text


def content_counts():
    """The counts of the original content, from the content itself."""
    import render_counts as rc
    return {"{GM_COUNTS}": rc.all_gm_counts(), "{PLAYER_COUNTS}": rc.all_player_counts(),
            "{SPELL_COUNTS}": rc.all_spell_counts()}


def dawnwatch_counts(dw=None):
    """The counts of the Dawnwatch content, for the back cover of a Dawnwatch book."""
    if dw is None:
        import content.dawnwatch as dw
    n = lambda k, one, many: f"{k} {one if k == 1 else many}"
    return {"{DW_COUNTS}": f"{n(len(dw.MON), 'new creature', 'new creatures')}, "
                           f"{n(len(dw.NPCS), 'person', 'people')}, and {n(len(dw.ITEMS), 'treasure', 'treasures')}"}


def cover_html(name, pages, kind="paperback"):
    b = BOOKS[name]
    g = cover_size(pages, kind)
    spine, tw, th = g["spine_mm"], g["width_mm"], g["height_mm"]
    E, PW, PH, safe = g["edge_mm"], g["panel_w_mm"], g["panel_h_mm"], g["safe_mm"]
    hard = kind == "hardcover"
    frame = 19 if hard else 12          # the frame stays inside the safety margin
    small_w = PW - 24 - g["barcode_w_mm"] - safe - 4 if hard else 110
    # Paperback: the barcode box is in the corner of the text area.
    # Hardcover: Lulu puts it HC_SAFE from the bottom and from the spine.
    barcode_in = "" if hard else '<div class="barcode"></div>'
    barcode_out = (f'<div class="barcode" style="right:{safe}mm;bottom:{safe}mm;width:{g["barcode_w_mm"]}mm;'
                   f'height:{g["barcode_h_mm"]}mm"></div>') if hard else ""
    ic = "".join(f'<span class="cb">{icon(i, 22, "#d6aa55", 1.4)}</span>' for i in b["icons"])
    counts = content_counts()
    if any("{DW_COUNTS}" in x for x in b["bullets"]):
        counts.update(dawnwatch_counts())
    bl = "".join(f"<li>{fill_counts(x, counts)}</li>" for x in b["bullets"])
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: {tw}mm {th}mm; margin: 0; }}
@font-face {{ font-family: "Inter"; src: url("books/fonts/Inter-Regular.ttf") format("truetype"); font-weight: 400; font-style: normal; }}
@font-face {{ font-family: "Inter"; src: url("books/fonts/Inter-Italic.ttf") format("truetype"); font-weight: 400; font-style: italic; }}
@font-face {{ font-family: "Inter"; src: url("books/fonts/Inter-SemiBold.ttf") format("truetype"); font-weight: 600; font-style: normal; }}
@font-face {{ font-family: "Inter"; src: url("books/fonts/Inter-Bold.ttf") format("truetype"); font-weight: 700; font-style: normal; }}

html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; width: {tw}mm; height: {th}mm; position: relative; overflow: hidden; font-family: "Bitstream Charter", serif;
  background: radial-gradient(ellipse at 78% 38%, #4a1913 0%, #22100c 55%, #140806 100%); color: #f3e6cc; }}
.panel {{ position: absolute; top: {E}mm; height: {PH}mm; }}
.back {{ left: {E}mm; width: {PW}mm; }}
.spine {{ left: {E + PW}mm; width: {spine}mm; }}
.front {{ left: {E + PW + spine}mm; width: {PW}mm; }}
.frame {{ position: absolute; inset: {frame}mm; border: 1.2pt solid #c99a3e; outline: .5pt solid #c99a3e; outline-offset: -3.5mm; }}
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
.back .small {{ font-size: 7.5pt; color: #b9a27a; line-height: 1.45; position: absolute; bottom: 0; left: 0; width: {small_w:g}mm; }}
.barcode {{ position: absolute; right: 0; bottom: 0; width: 50mm; height: 30mm; background: #fff; }}
.spine .st {{ position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%) rotate(90deg); white-space: nowrap;
  font-family: Caladea, serif; font-size: {min(11, spine * 1.6):.1f}pt; color: #f6e2b8; letter-spacing: .06em; }}
.spine .st span {{ color: #c99a3e; margin: 0 3mm; }}
/* A drawn diamond, not the character: Chrome prints a rotated symbol glyph as a Type 3 font. */
.spine .st .dia {{ display: inline-block; width: 1.5mm; height: 1.5mm; background: #c99a3e; transform: rotate(45deg); vertical-align: middle; }}
.spine::before, .spine::after {{ content: ""; position: absolute; left: 0; right: 0; border-top: .8pt solid #c99a3e; }}
.spine::before {{ top: 18mm; }} .spine::after {{ bottom: 18mm; }}
</style></head><body>
<div class="panel back"><div class="frame"></div><div class="inner">
  <h2>{b["back"]}</h2><ul>{bl}</ul><div class="rule"></div>
  <p style="font-style:italic;color:#e2cfa8;font-size:10pt">{b.get("note", NOTE)}</p>
  <div class="small">Includes material from the System Reference Document 5.2 by Wizards of the Coast LLC, licensed under CC-BY-4.0. Not affiliated with or endorsed by Wizards of the Coast. Original content © 2026 Stiven Gjekaj, licensed under CC BY-NC-SA 4.0.</div>
  {barcode_in}
</div>{barcode_out}</div>
<div class="panel spine"><div class="st">Dice &amp; Destiny<span class="dia"></span>{b["title"]}</div></div>
<div class="panel front"><div class="frame"></div><div class="inner">
  <div class="kicker">Dice &amp; Destiny</div>
  <h1>{b["t1"]}<br>{b["t2"]}</h1>
  <div style="margin-top:12mm">{big_d20(230)}</div>
  <div class="subt">{b["sub"]}</div>
  <div class="compat">{b.get("compat", COMPAT)}</div>
  <div class="icons">{ic}</div>
</div><div class="foot">Dice &amp; Destiny · {pages} pages</div></div>
</body></html>''', spine, tw, th


if __name__ == "__main__":
    for n in sys.argv[1:]:
        pages = len(PdfReader(f"{n}.pdf").pages)
        for kind, out in (("paperback", f"{n}_cover"), ("hardcover", f"{n}_cover_hardcover")):
            h, spine, tw, th = cover_html(n, pages, kind)
            open(f"{out}.html", "w").write(h)
            subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={os.getcwd()}/{out}.pdf", f"file://{os.getcwd()}/{out}.html"],
                           stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            print(n, kind, f"{pages} pages, spine {spine} mm, cover {tw:.1f} × {th:.1f} mm")
