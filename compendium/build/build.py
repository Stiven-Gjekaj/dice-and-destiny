import re, sys, subprocess, os
from icons import icon, big_d20, divider
import classes, compendium as comp, orig_render as orig

ICON_COLOR = "#000"
CH_ICONS = {
    # GM
    "Your Job as Game Master": "crown", "For Writers": "quill", "Calling for Rolls": "dice",
    "Advantage, Disadvantage &amp; Difficulty": "scales", "Running Combat": "swords",
    "Hit Points, Death &amp; Resting": "heart", "Conditions": "skull", "Levels, XP &amp; Progression": "up",
    "Building Encounters": "dragon", "Exploration, Travel &amp; the World": "compass",
    "Treasure &amp; Magic Items": "chest", "Session Prep": "scroll", "Cheat Sheets &amp; Templates": "d20",
    "Using the Bestiary": "eye", "Monsters A–Z": "dragon", "Magic Items by Rarity": "spark",
    "Magic Items A–Z": "chest", "Poisons": "skull",
    "Traps &amp; Hazards": "warn",
    "World-Building Tables": "dice",
    "Pantheons": "crown",
    "Downtime Activities": "scroll",
    # Player
    "Welcome to the Table": "d20", "The Six Abilities": "sheet", "Skills, Proficiency &amp; Rolling": "dice",
    "Creating a Character": "quill", "Reading a Character Sheet": "eye", "Your Turn in Combat": "swords",
    "Hit Points, Healing &amp; Rest": "heart", "Spellcasting": "spark", "Weapons &amp; Armor": "swords",
    "Leveling Up &amp; Feats": "up", "Glossary": "scroll", "The Twelve Classes": "crown",
    "Species": "people", "Backgrounds": "book", "Feats": "star", "Adventuring Gear": "chest",
    "Tools": "scroll", "Mounts &amp; Vehicles": "compass", "Trade Goods &amp; Trinkets": "chest",
    "Spell Lists": "book", "Original Subclasses": "star", "Original Backgrounds &amp; Species": "people",
    "Original Feats": "star", "Original Spells": "spark", "Original Bestiary": "dragon", "Original Magic Items": "chest",
    "Strongholds": "shield", "Marks": "star", "Running Marks": "eye", "Bonds": "people", "Running Bonds": "people", "Techniques": "swords", "Running Techniques": "swords", "Legend Paths": "crown", "Running Legend Paths": "crown", "Spell Descriptions": "spark", "Rules Reference": "scales", "Character Sheet": "sheet",
}

TOC = []  # (kind, label, marker)


def marker(kind, label):
    n = len(TOC)
    TOC.append((kind, label, f"@@T{n}@@"))
    return f'<span class="mark">@@T{n}@@</span>'


def chapter_heads(s):
    """Number the chapters of a book in order. A chapter with the attribute data-unnumbered gets no number."""
    count = [0]

    def rep(m):
        np_, attrs, name = m.group(1), m.group(2), m.group(3).strip()
        num = None
        if "data-unnumbered" not in attrs:
            count[0] += 1
            num = count[0]
        ic = CH_ICONS.get(name, "d20")
        cls = "ch-head newpage" if np_ else "ch-head"
        kicker = f'<div class="ch-num">Chapter {num}</div>' if num else ""
        mk = marker("ch", (f"{num}. " if num else "") + name)
        return (f'<div class="{cls}">{mk}<span class="ch-badge">{icon(ic, 26, ICON_COLOR, 1.5)}</span>'
                f'<div>{kicker}<h1 class="chapter">{name}</h1></div></div>{divider()}')
    return re.sub(r'<h1 class="chapter((?: newpage)?)"([^>]*)>(.*?)</h1>', rep, s)


def class_marks(s):
    def rep(m):
        return m.group(0) + marker("sub", m.group(1))
    return re.sub(r'<h1 class="classname">(.*?)</h1>', rep, s)


def parts(s):
    def rep(m):
        num, title, desc = m.group(1), m.group(2), m.group(3)
        mk = marker("part", f"Part {num} · {title}")
        return (f'<!--PARTSTART--><section class="part">{mk}<div class="pn">Part {num}</div><h1>{title}</h1>'
                f'<div class="orn">{divider()}</div><div class="pd">{desc}</div></section>')
    return re.sub(r"\{\{PART:([^|]+)\|([^|]+)\|([^}]*)\}\}", rep, s)


def box_icons(s):
    s = re.sub(r'(<div class="box red">\s*<h4>)', lambda m: m.group(1) + icon("warn", 14), s)
    s = re.sub(r'(<div class="box dark">\s*<h4>)', lambda m: m.group(1) + icon("d20", 14), s)
    s = re.sub(r'(<div class="box">\s*<h4>)', lambda m: m.group(1) + icon("tip", 14), s)
    s = re.sub(r'<h4 data-i="(\w+)">', lambda m: "<h4>" + icon(m.group(1), 14), s)
    s = re.sub(r'<h2((?: class="[^"]*")?) data-i="(\w+)">', lambda m: f"<h2{m.group(1)}>" + icon(m.group(2), 16), s)
    return s


FRONT = {
 "gm": dict(title="The Game Master's<br>Compendium", sub="Running the game, a complete bestiary, every magic item, and the tools to prep any session."),
 "player": dict(title="The Player's<br>Compendium", sub="How to build a hero, how to play one, and the complete reference: every class, spell, feat and rule."),
}


def gray(svg):
    def g(m):
        h = m.group(1)
        r, gg, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        y = int(0.3 * r + 0.59 * gg + 0.11 * b)
        y = min(255, int(y * 1.5 + 40))  # lighten so faces stay distinct on paper
        return "#%02x%02x%02x" % (y, y, y)
    return re.sub(r"#([0-9a-fA-F]{6})\b", g, svg).replace('fill="#ffffff"', 'fill="#fff"')


def _dark_text(svg):
    return re.sub(r'(<text[^>]*?)fill="#[0-9a-f]{6}"', r'\1fill="#000"', svg)


def front(name):
    f = FRONT[name]
    return f'''<section class="titlepage">
<div class="kicker">Dice &amp; Destiny</div>
<h1>{f["title"]}</h1><div class="rule"></div>
<div>{_dark_text(gray(big_d20(150, "#000", flat=True)))}</div>
<div class="sub" style="margin-top:8mm">{f["sub"]}</div>
<div class="compat">A rules-compatible guide for fifth edition (2024)</div></section>
<section class="credits">
<p><b>Dice &amp; Destiny: {f["title"].replace("<br>", " ")}</b></p>
<p>Copyright © 2026 Stiven Gjekaj. The original text and content of this book are licensed under CC BY-NC-SA 4.0 (creativecommons.org/licenses/by-nc-sa/4.0). You can share and adapt them for non-commercial use if you give credit and share your changes under the same license.</p>
<p>An independent work. Not affiliated with, endorsed, sponsored, or approved by Wizards of the Coast. Dungeons &amp; Dragons is a trademark of Wizards of the Coast LLC.</p>
<p>This work includes material from the System Reference Document 5.2 ("SRD 5.2") by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode. The SRD 5.2 text in this book is changed: it is reorganized and laid out again, and some sentences no longer name the trademark.</p>
<p>Explanatory chapters, examples, tips, icons and layout are original to this book, as is everything in the Expanded Options, Expanded Bestiary &amp; Treasure and Optional Rules parts (classes, subclasses, backgrounds, species, feats, spells, monsters, magic items, strongholds and the optional rules systems); that original content is not part of the SRD 5.2. Subclasses, backgrounds and other options mentioned by name but not included in the SRD 5.2 are referenced only; see the Player's Handbook and Dungeon Master's Guide for their rules. The encounter-building and improvised-damage tables follow the 2024 Dungeon Master's Guide. The "Lazy GM" prep checklist is by Michael E. Shea (Sly Flourish).</p>
<p>Printed in black and white on A4 paper.</p>
</section>'''


def toc_html(pages):
    items = []
    for i, (kind, label, mk) in enumerate(TOC):
        p = pages.get(mk, "")
        cls = {"part": "part-entry", "ch": "", "sub": "sub"}[kind]
        items.append(f'<li class="{cls}"><span class="t">{label}</span><span class="dots"></span><span class="p">{p}</span></li>')
    return (f'<div class="frontmatter"><div class="ch-head"><span class="ch-badge">{icon("book", 26, ICON_COLOR, 1.5)}</span>'
            f'<div><h1 class="chapter" style="string-set:none">Contents</h1></div></div>{divider()}'
            f'<ul class="toc2">{"".join(items)}</ul></div>')


def expand(name):
    s = open(f"books/{name}.src.html").read()
    s = s.replace('<link rel="stylesheet" href="style.css">', '<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="book.css">')
    s = s.replace("{{FRONT}}", front(name))
    reps = {
        "{{CLASSES}}": lambda: classes.all_classes(),
        "{{CLASS_CARDS}}": lambda: classes.cards(),
        "{{SPECIES}}": comp.species_html, "{{BACKGROUNDS}}": comp.backgrounds_html, "{{FEATS}}": comp.feats_html,
        "{{GEAR}}": lambda: comp.equipment_html({"Adventuring Gear", "Ammunition", "Spellcasting Focus", "Equipment Pack"}),
        "{{TOOLS}}": lambda: comp.equipment_html({"Tools"}),
        "{{MOUNTS}}": lambda: comp.equipment_html({"Mount", "Land Vehicle", "Waterborne Vehicle"}),
        "{{TRADE}}": lambda: comp.equipment_html({"Trade Good"}, with_desc=False),
        "{{TRINKETS}}": comp.trinkets_html,
        "{{SPELL_LISTS}}": comp.spell_lists_html, "{{SPELLS}}": comp.spells_full_html,
        "{{RULES}}": lambda: '<div class="rules">' + comp.rules_html() + "</div>",
        "{{BESTIARY}}": comp.bestiary_html, "{{BY_CR}}": comp.monsters_by_cr_html, "{{BY_TYPE}}": comp.monsters_by_type_html,
        "{{MAGIC_ITEMS}}": comp.magic_items_html, "{{ITEMS_BY_RARITY}}": comp.magic_items_by_rarity_html,
        "{{POISONS}}": lambda: comp.equipment_html({"Poison"}),
        "{{O_SUBS}}": lambda: orig.subclasses_html(), "{{O_BG}}": lambda: orig.backgrounds_html(),
        "{{O_SPECIES}}": lambda: orig.species_html(), "{{O_FEATS}}": lambda: orig.feats_html(),
        "{{O_SPELLS}}": lambda: orig.spells_html(), "{{O_BEST_IDX}}": lambda: orig.bestiary_index_html(),
        "{{O_BEST}}": lambda: orig.bestiary_html(), "{{O_ITEMS_IDX}}": lambda: orig.items_index_html(),
        "{{O_ITEMS}}": lambda: orig.items_html(), "{{O_STRONG}}": lambda: orig.strongholds_html(),
        "{{O_CLASSES}}": lambda: __import__("render_classes").classes_html(),
        "{{INJURIES}}": lambda: __import__("render_injuries").all_injuries_html(),
        "{{SYS_MARKS}}": lambda: __import__("render_systems").player_marks_html(),
        "{{SYS_TAINTS}}": lambda: __import__("render_systems").gm_marks_html(),
        "{{SYS_BONDS}}": lambda: __import__("render_systems").all_bonds_html(),
        "{{SYS_TECHNIQUES}}": lambda: __import__("render_systems").all_techniques_html(),
        "{{SYS_LEGENDS}}": lambda: __import__("render_systems").all_legends_html(),
        "{{O_TRAPS_IDX}}": lambda: __import__("render_traps").all_traps_index_html(),
        "{{O_TRAPS}}": lambda: __import__("render_traps").all_traps_html(),
        "{{O_NPCS_IDX}}": lambda: __import__("render_npcs").all_npcs_index_html(),
        "{{O_NPCS}}": lambda: __import__("render_npcs").all_npcs_html(),
        "{{O_COUNTS_GM}}": lambda: __import__("render_counts").all_gm_counts(),
        "{{O_COUNTS_PLAYER}}": lambda: __import__("render_counts").all_player_counts(),
        "{{O_COUNTS_ORIGINS}}": lambda: __import__("render_counts").all_origin_counts(),
        "{{O_COUNTS_SPELLS}}": lambda: __import__("render_counts").all_spell_counts(),
        "{{TABLE_SETS}}": lambda: __import__("render_tables").all_tables_html(),
        "{{PANTHEONS}}": lambda: __import__("render_pantheons").all_pantheons_html(),
        "{{DOWNTIME}}": lambda: __import__("render_downtime").all_downtime_html(),
    }
    for k, f in reps.items():
        if k in s:
            s = s.replace(k, f())
    TOC.clear()
    s = parts(s)
    s = chapter_heads(s)
    s = class_marks(s)
    s = box_icons(s)
    s = comp.no_em_dash(s)
    TOC.sort(key=lambda t: s.index(t[2]))
    return s


def render(name, s):
    open(f"books/{name}.html", "w").write(s)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.getcwd()}/{name}.pdf", f"file://{os.getcwd()}/books/{name}.html"],
                   stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, timeout=900)


def find_pages(name):
    txt = subprocess.run(["pdftotext", f"{name}.pdf", "-"], capture_output=True, text=True).stdout
    pages = {}
    for i, pg in enumerate(txt.split("\f")):
        for m in re.findall(r"@@T\d+@@", pg):
            pages.setdefault(m, i + 1)
    return pages


def build(name):
    body = expand(name)
    toc_entries = list(TOC)
    blanks = set()
    pages = {}
    for it in range(12):
        TOC[:] = toc_entries
        s = body.replace("{{TOC}}", toc_html(pages))
        # parts start on right-hand pages: add a blank page before any part that would land on a left page
        chunks = s.split("<!--PARTSTART-->")
        s = chunks[0] + "".join(("<div class=\"blankpage\"></div>" if i in blanks else "") + c for i, c in enumerate(chunks[1:]))
        render(name, s)
        new = find_pages(name)
        moved = False
        for i, (kind, label, mk) in enumerate([t for t in toc_entries if t[0] == "part"]):
            p = new.get(mk)
            if p and p % 2 == 0:
                if i in blanks:
                    blanks.discard(i)
                else:
                    blanks.add(i)
                moved = True
                break
        print(f"  pass {it + 1}: {len(new)}/{len(toc_entries)} markers found, blanks={sorted(blanks)}", flush=True)
        if not moved and new == pages:
            break
        pages = new
    # final: strip markers (zero-size, so layout is unchanged)
    s = re.sub(r'<span class="mark">@@T\d+@@</span>', '<span class="mark"></span>', s)
    render(name, s)
    return pages


if __name__ == "__main__":
    for n in sys.argv[1:]:
        p = build(n)
        print(n, "done")
