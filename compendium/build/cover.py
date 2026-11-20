"""Full-colour wraparound covers: back | spine | front.

Two kinds:
  paperback  A4 trim with 3 mm bleed.
  hardcover  Lulu A4 casewrap: boards, a wrap around the edges, and a safety margin.
"""
import importlib, re, sys, subprocess, os
from math import cos, sin, pi, radians
from pypdf import PdfReader

BLEED, W, H = 3.0, 210.0, 297.0
MM_PER_PAGE = 0.0572  # typical 50–60 lb white paper; confirm with your printer's spine calculator

# Lulu A4 casewrap hardcover, from the Lulu cover template (196 pages, uploaded 2026-11-15).
HC_TRIM_W, HC_TRIM_H = 216.41, 309.63   # the board, larger than A4
HC_WRAP = 15.87                         # wrap around each edge
HC_SAFE = 15.87                         # safety margin inside the board edge
HC_MIN_PAGES = 24                       # Lulu prints no casewrap hardcover with fewer pages
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
        if not HC_MIN_PAGES <= pages <= 800:
            raise ValueError(f"Lulu prints a casewrap hardcover with {HC_MIN_PAGES} to 800 pages, not {pages}")
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
 "western-sea": dict(title="Beyond the Western Sea", t1="Beyond the", t2="Western Sea",
   sub="A storm wrecks your ship on an island that is on no map. Find the way home before the storm season comes back.",
   back="A short campaign from level 1 to level 5. A lost colony, one island, and a storm that everyone can see coming.",
   bullets=["A wreck and a shore to start, an island of sites to explore in any order, and a last chapter in the storm season",
            "Play with the dice of a backgammon set, or with normal dice: each roll is printed in both forms",
            "The Storm Cube: a clock on the table that each player can see, and a risk that each player can take",
            "{WS_COUNTS}, each in an appendix from A to Z",
            "A player's guide with no spoilers, a gazetteer of the island, a map, and handouts on their own pages"],
   icons=["compass", "dice", "people", "chest"],
   compat="A campaign for levels 1 to 5 &middot; Requires Edition 2",
   note="Uses the rules of Dice &amp; Destiny: The Player's Compendium and The Game Master's Compendium, Edition 2."),
}
# The colors of each book: the background (center, middle, edge), the accent of the lines and the small text,
# and the hue of the die in degrees (None: the red die). Each book has its own color.
PALETTES = {
    "player": dict(bg=("#1f3560", "#101b33", "#080d1a"), accent="#cfa954", hue=218),
    "gm": dict(bg=("#4a1913", "#22100c", "#140806"), accent="#c99a3e", hue=None),
    "waking": dict(bg=("#3d2352", "#1b1028", "#0d0714"), accent="#d6a64e", hue=280),
    "western-sea": dict(bg=("#0f474a", "#0a2527", "#051011"), accent="#c9b27c", hue=186),
}

# The space in mm between the inner line of a frame and the nearest text. A line of text that comes nearer
# to a line of the frame goes onto a new line.
CLEAR_MM = 8
# The distance in mm from the outer line of a frame to its inner line.
FRAME_GAP_MM = 1.8

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


# Each campaign token and the content package that gives its counts.
CAMPAIGN_TOKENS = {"{DW_COUNTS}": "content.dawnwatch", "{WS_COUNTS}": "content.western_sea"}


def campaign_counts(module, token):
    """The counts of the content of a campaign, for the back cover of the book. token is for example "{DW_COUNTS}"."""
    n = lambda k, one, many: f"{k} {one if k == 1 else many}"
    return {token: f"{n(len(module.MON), 'new creature', 'new creatures')}, "
                   f"{n(len(module.NPCS), 'person', 'people')}, and {n(len(module.ITEMS), 'treasure', 'treasures')}"}


def cover_pages(pages, kind):
    """The page count for the geometry of a cover, and a warning or None.
    A book that is not complete can have fewer pages than Lulu prints as a hardcover.
    Then the hardcover uses the minimum count, so that the build can continue."""
    if kind == "hardcover" and pages < HC_MIN_PAGES:
        return HC_MIN_PAGES, (f"WARNING: the book has {pages} pages. The hardcover cover uses "
                              f"{HC_MIN_PAGES} pages, the minimum that Lulu prints.")
    return pages, None


# The cut at each corner of a frame, in mm. A small diamond sits in each cut.
CUT_MM = 8

FONTS = """
@font-face { font-family: "Fell"; src: url("books/fonts/IMFellEnglish-Regular.ttf") format("truetype"); font-style: normal; }
@font-face { font-family: "Fell"; src: url("books/fonts/IMFellEnglish-Italic.ttf") format("truetype"); font-style: italic; }
@font-face { font-family: "Fell SC"; src: url("books/fonts/IMFellEnglishSC-Regular.ttf") format("truetype"); }
@font-face { font-family: "Inter"; src: url("books/fonts/Inter-Regular.ttf") format("truetype"); font-weight: 400; font-style: normal; }
"""


def frame_svg(w, h, color):
    """A frame of two lines with cut corners and a diamond in each corner, w x h mm."""
    c, g = CUT_MM, FRAME_GAP_MM

    def cut(i):
        return (f"M{c + i:g} {i:g} H{w - c - i:g} V{c:g} H{w - i:g} V{h - c:g} H{w - c - i:g} V{h - i:g} "
                f"H{c + i:g} V{h - c:g} H{i:g} V{c:g} H{c + i:g} Z")
    inner = (f"M{c + g:g} {g:g} H{w - c - g:g} V{c + g:g} H{w - g:g} V{h - c - g:g} H{w - c - g:g} V{h - g:g} "
             f"H{c + g:g} V{h - c - g:g} H{g:g} V{c + g:g} H{c + g:g} Z")
    dia = "".join(f'<path d="M{x:g} {y - 1.4:g} L{x + 1.4:g} {y:g} L{x:g} {y + 1.4:g} L{x - 1.4:g} {y:g} Z" fill="{color}"/>'
                  for x, y in ((c / 2, c / 2), (w - c / 2, c / 2), (c / 2, h - c / 2), (w - c / 2, h - c / 2)))
    return (f'<svg class="frame" viewBox="0 0 {w:g} {h:g}" style="width:{w:g}mm;height:{h:g}mm" fill="none" stroke="{color}">'
            f'<path d="{cut(0)}" stroke-width=".42"/><path d="{inner}" stroke-width=".2"/>{dia}</svg>')


def divider_svg(color):
    """A rule with a diamond in the middle, 46 mm wide."""
    return (f'<svg class="divider" viewBox="0 0 132 9" fill="{color}" stroke="{color}">'
            '<line x1="0" y1="4.5" x2="56" y2="4.5" stroke-width=".8"/><line x1="76" y1="4.5" x2="132" y2="4.5" stroke-width=".8"/>'
            '<path d="M66 0 L70.5 4.5 L66 9 L61.5 4.5 Z" stroke="none"/>'
            '<circle cx="58.5" cy="4.5" r=".9" stroke="none"/><circle cx="73.5" cy="4.5" r=".9" stroke="none"/></svg>')


def emblem(name, ink, acc, ground):
    """The emblem of a book, in a box of 150 x 150, inside two rings."""
    rings = (f'<circle cx="75" cy="75" r="72" fill="none" stroke="{acc}" stroke-width="1.4"/>'
             f'<circle cx="75" cy="75" r="66" fill="none" stroke="{acc}" stroke-width=".5"/>')
    if name == "player":  # a sword behind a shield: the hero
        # The sword from the top: the pommel, the wrapped grip, the crossguard, then the blade under the guard.
        art = ('<g transform="translate(0 6)">' f'<path d="M71 41 H79 V112 L75 124 L71 112 Z" fill="{ink}"/>'
               f'<line x1="75" y1="44" x2="75" y2="108" stroke="{ground}" stroke-width=".8"/>'
               f'<circle cx="75" cy="18" r="4" fill="{acc}"/>'
               f'<path d="M72.3 22 H77.7 L78.3 35 H71.7 Z" fill="{acc}"/>'
               + "".join(f'<line x1="71.9" y1="{y}" x2="78.1" y2="{y + 2}" stroke="{ground}" stroke-width=".7"/>' for y in (24.5, 28, 31.5))
               + f'<path d="M51 39 C51 35 56 35 60 36 H90 C94 35 99 35 99 39 C99 41 95 41.5 90 41 H60 C55 41.5 51 41 51 39 Z" fill="{acc}"/>'
               f'<path d="M52 50 H98 V78 C98 97 88 108 75 116 C62 108 52 97 52 78 Z" fill="{ground}" stroke="{acc}" stroke-width="1.6"/>'
               f'<path d="M57 55 H93 V78 C93 94 85 103 75 110 C65 103 57 94 57 78 Z" fill="none" stroke="{acc}" stroke-width=".5"/>'
               # Two chevrons with sharp ends. Each end stops on the inner line of the shield (x 57 and x 93).
               f'<path d="M57 62 L75 78 L93 62 V67.5 L75 83.5 L57 67.5 Z" fill="{ink}"/>'
               f'<path d="M57 76 L75 92 L93 76 V81.5 L75 97.5 L57 81.5 Z" fill="{ink}"/>'
               '</g>')
    elif name == "gm":  # the die of the game master, drawn in lines
        T, UR, LR, B, LL, UL = (75, 20), (121, 46), (121, 104), (75, 130), (29, 104), (29, 46)
        ct, cl, cr = (75, 50), (46, 99), (104, 99)
        edges = [(T, UR), (UR, LR), (LR, B), (B, LL), (LL, UL), (UL, T), (ct, cl), (cl, cr), (cr, ct), (T, ct), (UL, ct),
                 (UR, ct), (UL, cl), (LL, cl), (B, cl), (B, cr), (LR, cr), (UR, cr)]
        art = (f'<path d="M{ct[0]} {ct[1]} L{cl[0]} {cl[1]} L{cr[0]} {cr[1]} Z" fill="{ink}"/>'
               + "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{acc}" stroke-width="1.5" '
                         f'stroke-linecap="round"/>' for a, b in edges)
               + f'<text x="75" y="89" text-anchor="middle" font-family="Fell" font-size="26" fill="{ground}">20</text>')
    elif name == "waking":  # Wick, the lantern of the Dawnwatch, in a ring of the rays of the dawn
        rays = "".join(f'<line x1="{75 + 40 * cos(a):.2f}" y1="{70 + 40 * sin(a):.2f}" x2="{75 + (40 + l) * cos(a):.2f}" '
                       f'y2="{70 + (40 + l) * sin(a):.2f}" stroke="{acc}" stroke-width="{w}" stroke-linecap="round"/>'
                       for a, l, w in ((radians(i * 45 - 90), 10, 1.4) for i in range(8)))
        art = ('<g transform="translate(0 4)">' + rays
               + f'<path d="M66 33 C66 21 84 21 84 33" fill="none" stroke="{acc}" stroke-width="1.8"/>'
               f'<circle cx="75" cy="22.5" r="2.2" fill="{acc}"/>'
               f'<path d="M59 41 C62 33 69 30 75 30 C81 30 88 33 91 41 Z" fill="{acc}"/>'
               f'<rect x="57" y="41" width="36" height="4" rx="1" fill="{acc}"/>'
               f'<rect x="61" y="45" width="28" height="51" fill="{ground}" stroke="{ink}" stroke-width="2"/>'
               f'<path d="M64.5 49 H85.5 V92 H64.5 Z" fill="none" stroke="{acc}" stroke-width=".5"/>'
               f'<line x1="68" y1="45" x2="68" y2="96" stroke="{acc}" stroke-width=".7"/>'
               f'<line x1="82" y1="45" x2="82" y2="96" stroke="{acc}" stroke-width=".7"/>'
               +
               f'<path d="M75 55 C84 64 84 78 75 88 C66 78 66 64 75 55 Z" fill="{ink}"/>'
               f'<path d="M75 66 C79 71 79 78 75 83 C71 78 71 71 75 66 Z" fill="{acc}"/>'
               f'<rect x="57" y="96" width="36" height="4" rx="1" fill="{acc}"/>'
               f'<path d="M61 100 H89 L85 106 H65 Z" fill="{acc}"/>'
               f'<path d="M64 106 h5 v3 h-5 Z M81 106 h5 v3 h-5 Z" fill="{acc}"/></g>')
    else:  # western-sea: a ship under full sail on the waves, with the north star
        waves = "".join(f'<path d="M{75 - 6 * n} {y} q6 -4 12 0' + " t12 0" * (n - 1) + f'" fill="none" stroke="{acc}" '
                        f'stroke-width="1.3" stroke-linecap="round"/>' for n, y in ((7, 106), (5, 114)))
        sail = lambda x0, x1, y0, y1, bulge: (f'<path d="M{x0} {y0} H{x1} Q{x1 + bulge} {(y0 + y1) / 2} {x1} {y1} '
                                              f'H{x0} Q{x0 + bulge} {(y0 + y1) / 2} {x0} {y0} Z" fill="{ink}"/>')
        art = ('<g transform="translate(75 75) scale(.9) translate(-81 -72)">'
               f'<line x1="64" y1="30" x2="64" y2="96" stroke="{acc}" stroke-width="1.6"/>'
               f'<line x1="88" y1="38" x2="88" y2="96" stroke="{acc}" stroke-width="1.6"/>'
               + sail(53, 74, 36, 50, 4) + sail(51, 76, 53, 70, 5) + sail(52, 75, 73, 88, 5)
               + sail(79, 96, 44, 56, 3) + sail(78, 98, 59, 74, 4) + sail(79, 97, 77, 89, 3)
               + f'<line x1="104" y1="93" x2="128" y2="88" stroke="{acc}" stroke-width="1.4"/>'
               f'<path d="M103 48 L124 89 L103 90 Z" fill="{ink}"/>'
               f'<path d="M64 30 L56 27 L64 24 Z" fill="{acc}"/><path d="M88 38 L80 35 L88 32 Z" fill="{acc}"/>'
               f'<path d="M34 92 H112 L104 101 Q75 104 44 101 Z" fill="{acc}"/>'
               + waves
               + f'<path d="M36 34 L37.8 39.2 L43 41 L37.8 42.8 L36 48 L34.2 42.8 L29 41 L34.2 39.2 Z" fill="{ink}"/></g>')
    return rings + art


def medal_svg(name, ink, acc, ground, disc, size_mm):
    """The emblem in a dark disc with a fine sunburst, as on the Soultale covers."""
    rays = "".join(f'<line x1="{118 + 84 * cos(a):.2f}" y1="{118 + 84 * sin(a):.2f}" x2="{118 + r2 * cos(a):.2f}" '
                   f'y2="{118 + r2 * sin(a):.2f}" stroke="{acc}" stroke-width="{w}"/>'
                   for a, r2, w in ((i / 96 * 2 * pi, 116 if i % 2 == 0 else 104, .7 if i % 2 == 0 else .5) for i in range(96)))
    return (f'<svg class="medal" viewBox="0 0 236 236" style="width:{size_mm}mm;height:{size_mm}mm">{rays}'
            f'<circle cx="118" cy="118" r="80" fill="{disc}"/><g transform="translate(43 43)">{emblem(name, ink, acc, disc)}</g></svg>')


def mini_svg(name, ink, acc, disc, size_mm):
    return (f'<svg class="mini" viewBox="0 0 150 150" style="width:{size_mm}mm;height:{size_mm}mm">'
            f'<circle cx="75" cy="75" r="72" fill="{disc}"/>{emblem(name, ink, acc, disc)}</svg>')


def keep_together(text):
    """The text with a no-break space between "level" and its number, so that a line never ends between them."""
    return re.sub(r"\blevel (\d+)", r"level&nbsp;\1", text)


def front_html(b, name, colors, pages=None):
    """The front of a cover: a centered stack of the kicker, the title, the tagline, the medal, and the compat line."""
    ink, acc, disc = colors["ink"], colors["accent"], colors["disc"]
    foot = f'<div class="foot">Dice &amp; Destiny · {pages} pages</div>' if pages else ""
    return (f'<div class="stack"><div class="kicker">Dice &amp; Destiny</div>{divider_svg(acc)}'
            f'<h1>{b["t1"]}<br>{b["t2"]}</h1><div class="subt">{b["sub"]}</div>'
            f'{medal_svg(name, ink, acc, colors["ground"], disc, 100)}{divider_svg(acc)}'
            f'<div class="compat">{b.get("compat", COMPAT)}</div>{foot}</div>')


STACK_CSS = """
.stack { position: absolute; display: flex; flex-direction: column; align-items: center; text-align: center; }
.kicker { font-family: "Fell SC", serif; font-size: 11pt; letter-spacing: .5em; padding-left: .5em; color: var(--acc); }
.divider { width: 46mm; height: 3.2mm; margin-top: 4mm; flex: none; }
h1 { font-family: "Fell", serif; font-weight: normal; font-size: 46pt; line-height: 1.05; margin: 7mm 0 0; color: var(--ink); text-wrap: balance; }
.subt { font-family: "Fell", serif; font-style: italic; font-size: 14pt; line-height: 1.4; margin-top: 5mm; max-width: 130mm; color: var(--soft); text-wrap: balance; }
.medal { margin: auto 0; flex: none; }
.compat { font-family: "Fell SC", serif; font-size: 10pt; letter-spacing: .22em; padding-left: .22em; line-height: 1.7; margin-top: 4mm;
  color: var(--ink); text-wrap: balance; }
.foot { font-family: Inter, sans-serif; font-size: 6.5pt; letter-spacing: .14em; color: var(--acc); text-transform: uppercase; margin-top: 3mm; }
"""


def cover_html(name, pages, kind="paperback"):
    b = BOOKS[name]
    g = cover_size(pages, kind)
    spine, tw, th = g["spine_mm"], g["width_mm"], g["height_mm"]
    E, PW, PH = g["edge_mm"], g["panel_w_mm"], g["panel_h_mm"]
    hard = kind == "hardcover"
    pal = PALETTES[name]
    acc = pal["accent"]
    colors = dict(ink="#f3e6cc", soft="#e2cfa8", accent=acc, ground=pal["bg"][1], disc=pal["bg"][2])
    frame = 19 if hard else 12          # the frame stays inside the safety margin
    pad = frame + FRAME_GAP_MM + CLEAR_MM  # the nearest place for text, at the sides
    top = frame + CUT_MM + CLEAR_MM        # the nearest place for text, at the top and the bottom
    counts = content_counts()
    for token, package in CAMPAIGN_TOKENS.items():
        if any(token in x for x in b["bullets"]):
            counts.update(campaign_counts(importlib.import_module(package), token))
    bl = "".join(f"<p>{keep_together(fill_counts(x, counts))}</p>" for x in b["bullets"])
    bg0, bg1, bg2 = pal["bg"]
    fw, fh = PW - 2 * frame, PH - 2 * frame
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: {tw}mm {th}mm; margin: 0; }}
{FONTS}
:root {{ --ink: {colors["ink"]}; --soft: {colors["soft"]}; --acc: {acc}; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; width: {tw}mm; height: {th}mm; position: relative; overflow: hidden; font-family: Caladea, serif;
  background: radial-gradient(ellipse at 78% 38%, {bg0} 0%, {bg1} 55%, {bg2} 100%); color: var(--ink); }}
.panel {{ position: absolute; top: {E}mm; height: {PH}mm; }}
.back {{ left: {E}mm; width: {PW}mm; }}
.spine {{ left: {E + PW}mm; width: {spine}mm; }}
.front {{ left: {E + PW + spine}mm; width: {PW}mm; }}
.frame {{ position: absolute; left: {frame}mm; top: {frame}mm; }}
{STACK_CSS}
.stack {{ top: {top:g}mm; bottom: {top:g}mm; left: {pad:g}mm; right: {pad:g}mm; }}
.back h2 {{ font-family: "Fell", serif; font-weight: normal; font-size: 19pt; line-height: 1.3; margin: 0; max-width: 140mm; color: var(--ink); text-wrap: balance; }}
.blurb {{ margin-top: 3mm; max-width: 135mm; font-size: 11.5pt; line-height: 1.5; color: #ead9b6; }}
.blurb p {{ margin: 0; padding: 3.2mm 0; text-wrap: balance; }}
.blurb p + p {{ border-top: .2mm solid color-mix(in srgb, var(--acc) 45%, transparent); }}
.middle {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
.mini {{ margin-top: 8mm; flex: none; }}
.note {{ font-style: italic; font-size: 10pt; line-height: 1.45; color: var(--soft); margin: 5mm 0 0; text-wrap: balance; }}
.small {{ font-style: italic; font-size: 7.5pt; line-height: 1.5; color: #b9a27a; margin-top: 3mm; text-wrap: balance; }}
.spine .st {{ position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%) rotate(90deg); white-space: nowrap;
  font-family: "Fell SC", serif; font-size: {min(13, spine * 1.5):.1f}pt; color: var(--ink); letter-spacing: .14em; }}
/* A drawn diamond, not the character: Chrome prints a rotated symbol glyph as a Type 3 font. */
.spine .st .dia {{ display: inline-block; width: 1.4mm; height: 1.4mm; background: var(--acc); transform: rotate(45deg); vertical-align: middle; margin: 0 3mm; }}
.band {{ position: absolute; left: 0; width: 100%; height: 12mm; }}
.band.t {{ top: 16mm; }} .band.b {{ bottom: 16mm; }}
</style></head><body>
<div class="panel back">{frame_svg(fw, fh, acc)}<div class="stack">
  <div class="kicker">Dice &amp; Destiny</div>{divider_svg(acc)}
  <div class="middle"><h2>{keep_together(b["back"])}</h2><div class="blurb">{bl}</div>
  {mini_svg(name, colors["ink"], acc, colors["disc"], 22)}</div>
  <p class="note">{b.get("note", NOTE)}</p>
  <div class="small">Includes material from the System Reference Document 5.2 by Wizards of the Coast LLC, licensed under CC-BY-4.0. Not affiliated with or endorsed by Wizards of the Coast. Original content © 2026 Stiven Gjekaj, licensed under CC BY-NC-SA 4.0.</div>
</div></div>
<div class="panel spine">{band_svg(acc, "t")}<div class="st">Dice &amp; Destiny<span class="dia"></span>{b["title"]}</div>{band_svg(acc, "b")}</div>
<div class="panel front">{frame_svg(fw, fh, acc)}{front_html(b, name, colors, pages)}</div>
</body></html>''', spine, tw, th


def band_svg(color, where):
    """A band of two cords and a diamond across the spine."""
    return (f'<svg class="band {where}" viewBox="0 0 68 40" preserveAspectRatio="xMidYMid meet" stroke="{color}" fill="{color}">'
            '<line x1="14" y1="6" x2="54" y2="6" stroke-width="1.2"/><line x1="14" y1="10" x2="54" y2="10" stroke-width=".5"/>'
            '<path d="M34 15 L39 20 L34 25 L29 20 Z" stroke="none"/>'
            '<line x1="14" y1="30" x2="54" y2="30" stroke-width=".5"/><line x1="14" y1="34" x2="54" y2="34" stroke-width="1.2"/></svg>')


if __name__ == "__main__":
    for n in sys.argv[1:]:
        pages = len(PdfReader(f"{n}.pdf").pages)
        for kind, out in (("paperback", f"{n}_cover"), ("hardcover", f"{n}_cover_hardcover")):
            size, warning = cover_pages(pages, kind)
            if warning:
                print(n, warning)
            h, spine, tw, th = cover_html(n, size, kind)
            open(f"{out}.html", "w").write(h)
            subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={os.getcwd()}/{out}.pdf", f"file://{os.getcwd()}/{out}.html"],
                           stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            print(n, kind, f"{size} pages, spine {spine} mm, cover {tw:.1f} × {th:.1f} mm")
