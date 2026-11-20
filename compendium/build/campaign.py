"""The book engine of a Dice & Destiny campaign book.

A Campaign record holds the parts that are different in each book: the name, the source folder,
the content, the front page, the stylesheet, the texts of the parts, the chapters, and the index
terms. The functions of this module build the book from a Campaign record.

A campaign book has these sources in its book folder:
  how-to-run.md, players-guide.md, gazetteer.md
  chapters/NN-name.md          the chapters (the Campaign record finds them)
  handouts/NN-name.md          one handout on each page

A source that does not exist yet is left out. The book builds with the files that exist.
"""
import dataclasses
import glob
import html
import importlib
import importlib.util
import os
import re
import subprocess
from types import ModuleType
from typing import Callable

import build as B
import waking_md as wm
from icons import big_d20, divider, icon

E = html.escape
COPYRIGHT = chr(0xA9)  # the copyright sign. The style linter of the repository refuses the sign in the source.

WARNINGS = []      # the problems that do not stop the build, for example a statblock that is not found
ANCHOR_MARK = {}   # an anchor id, to the marker of the page that holds it


def no_change(h):
    return h


@dataclasses.dataclass(frozen=True)
class Campaign:
    """The parts of one campaign book that the engine does not know."""
    name: str                                         # the output name, for example "waking"
    book: str                                         # the source folder
    content: Callable[[], ModuleType]                 # gives the content package (MON, NPCS, ITEMS, PLACES)
    front: dict                                       # title, sub_title, sub, compat
    css: str                                          # the book stylesheet in books/, for example "waking.css"
    parts: dict                                       # the texts of the parts "run", "story", "world", "reference"
    chapters: Callable[[str], list]                   # the book folder to the chapters, as (number, key, Markdown)
    maps: str = "maps"                                # the name of the maps module
    extra_forms: dict = dataclasses.field(default_factory=dict)   # an entry name to its other forms in the text
    not_before: dict = dataclasses.field(default_factory=dict)    # a name to the words that must not come after it
    index_terms: list = dataclasses.field(default_factory=list)   # (the name in the index, the forms in the text)
    post: Callable[[str], str] = no_change            # an HTML filter after the mentions are marked


def warn(text):
    WARNINGS.append(text)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


# ------------------------------------------------------------------ sources

def handouts(book):
    """The handouts in order, as (id, title, Markdown). The id is the file name with no .md."""
    out = []
    for path in sorted(glob.glob(os.path.join(book, "handouts", "*.md"))):
        hid = os.path.basename(path)[:-3]
        text = read(path)
        out.append((hid, wm.title_of(text, hid), text))
    return out


def section_file(name, book):
    path = os.path.join(book, name)
    return read(path) if os.path.isfile(path) else None


# ------------------------------------------------------------------ names

def person_name(entry):
    """A person is (role, M(...)), or (role, "Name") for a person with no statblock."""
    return entry[1] if isinstance(entry[1], str) else entry[1].name


def place_name(p):
    if isinstance(p, str):
        return p
    if isinstance(p, dict):
        return p["name"]
    if isinstance(p, (tuple, list)):
        return p[0]
    return p.name


def place_text(p):
    """The short text of a place, if the place has one."""
    if isinstance(p, dict):
        return p.get("summary") or p.get("text") or p.get("desc") or p.get("description") or ""
    if isinstance(p, (tuple, list)):
        return p[1] if len(p) > 1 and isinstance(p[1], str) else ""
    return getattr(p, "text", "") if not isinstance(p, str) else ""


# ------------------------------------------------------------------ directives

def _find(name, items, key):
    low = name.strip().lower()
    return next((x for x in items if key(x).strip().lower() == low), None)


def _orig_item_html(item):
    n, cat, rar, att, tx = item
    a = f" ({E(att)})" if att else ""
    return (f'<div class="mitem"><h4 class="sp-name">{E(n)}</h4>'
            f'<div class="sp-meta"><i>{E(cat)}, {E(rar)}{a}</i></div><p>{item_text(tx)}</p></div>')


INLINE_TAG = re.compile(r"&lt;(/?)(b|i|em|strong)&gt;")


def item_text(text):
    """Escape the text of a treasure. Keep the bold and italic tags, as in "<b>Daylight</b> (1 charge)"."""
    return INLINE_TAG.sub(r"<\1\2>", E(text))


def dw_stat_html(m, kind):
    """The statblock of a creature or person of the book. The engine writes the name in lower case in the
    Multiattack and Legendary Actions text ("The hush night warden"). A name of the book is a proper name,
    so it keeps its capitals: "The Hush Night Warden makes two attacks", "Osk makes two attacks"."""
    h, low = m.html(), E(m.ref())
    proper = E(re.sub(r"^The\s+", "", m.name))
    if kind == "person":
        return h.replace(f"The {low} ", f"{proper} ").replace(f"the {low} ", f"{proper} ")
    return h.replace(f"The {low} ", f"The {proper} ").replace(f"the {low} ", f"the {proper} ")


def statblock_html(name, dw):
    """The statblock of a creature or a person. Look in the content of the book, then in the
    original Compendium content, then in the SRD bestiary."""
    from content.monsters import MON
    from content.npcs import NPCS
    people = [e[1] for e in dw.NPCS if not isinstance(e[1], str)]
    for group, kind in ((dw.MON, "creature"), (people, "person"), (MON, None), ([e[1] for e in NPCS], None)):
        m = _find(name, group, lambda x: x.name)
        if m:
            return f'<div class="inline-stat">{dw_stat_html(m, kind) if kind else m.html()}</div>'
    import compendium as comp
    c = _find(name, comp.creatures(), lambda x: x["name"])
    if c:
        return f'<div class="inline-stat">{comp.creature_html(c)}</div>'
    warn(f"statblock not found: {name}")
    return f'<div class="missing">Statblock not found: {E(name)}</div>'


def treasure_html(name, dw):
    """The full entry of a treasure: a treasure of the book, an original magic item, or an SRD magic item."""
    from content.items import ITEMS
    for group in (dw.ITEMS, ITEMS):
        it = _find(name, group, lambda x: x[0])
        if it:
            return f'<div class="inline-stat">{_orig_item_html(it)}</div>'
    import compendium as comp
    low = name.strip().lower()
    it = next((i for i in comp.magic_items_grouped()
               if i["title"].lower() == low or low in (n.lower() for n in i["names"])), None)
    if it:
        return f'<div class="inline-stat">{comp.magic_item_html(it)}</div>'
    warn(f"treasure not found: {name}")
    return f'<div class="missing">Treasure not found: {E(name)}</div>'


def map_html(map_id, screen=False, maps="maps"):
    """A map from the maps module: map_svg(map_id) gives the final map in compendium/maps/ or a preview.
    An id that the module does not know, or no module, gives a placeholder. The maps are black and white,
    so the screen edition uses the same map."""
    if importlib.util.find_spec(maps) is not None:
        mod = importlib.import_module(maps)
        try:
            return f'<figure class="map" id="map-{wm.slug(map_id)}">{mod.map_svg(map_id.strip())}</figure>'
        except KeyError:
            pass
    warn(f"map not drawn: {map_id}")
    return f'<div class="map-placeholder">Map: {E(map_id)}</div>'


def missing_maps(c):
    """The ids of the maps that the book uses or that the maps module knows, with no final map in
    compendium/maps/. A book is not released while this list is not empty."""
    mod = importlib.import_module(c.maps)
    texts = [t for _, _, t in c.chapters(c.book)] + [t for _, _, t in handouts(c.book)]
    texts += [section_file(n, c.book) or "" for n in ("how-to-run.md", "players-guide.md", "gazetteer.md")]
    used = {a.strip() for t in texts for k, a in wm.directives(t) if k == "map"}
    ids = sorted(set(mod.MAP_IDS) | used)
    return [i for i in ids if i not in mod.MAP_IDS or i in mod.missing_maps([i])]


def handout_ref_html(hid, known, screen=False):
    """A note that the handout is in the appendix, with its page number.
    known maps a handout id to its title. The page comes from the marker of the handout."""
    hid = hid.strip()
    if hid not in known:
        warn(f"handout not found: {hid}")
        return f'<div class="missing">Handout not found: {E(hid)}</div>'
    title = E(known[hid])
    t = f'<a href="#handout-{hid}">{title}</a>' if screen else title
    return (f'<p class="handout-ref">{icon("scroll", 14)}<b>Handout:</b> {t}. '
            f'It is in the Handouts appendix, on page @@PAGE:handout-{hid}@@.</p>')


def handlers(dw, known_handouts, screen=False, maps="maps"):
    return {
        "statblock": lambda a: statblock_html(a, dw),
        "treasure": lambda a: treasure_html(a, dw),
        "map": lambda a: map_html(a, screen, maps),
        "handout": lambda a: handout_ref_html(a, known_handouts, screen),
    }


# ------------------------------------------------------------------ sections

CHAPTER_PREFIX = re.compile(r"^Chapter\s+\d+\s*[:.]\s*", re.I)


def chapter_head(name, num=None, ic="d20", newpage=True, anchor=None):
    """The head of a chapter, as build.chapter_heads makes it, with the given number."""
    kicker = f'<div class="ch-num">Chapter {num}</div>' if num else ""
    mk = B.marker("ch", (f"{num}. " if num else "") + name)
    if anchor:
        ANCHOR_MARK[anchor] = B.TOC[-1][2]
    aid = f' id="{anchor}"' if anchor else ""
    return (f'<div class="ch-head{" newpage" if newpage else ""}"{aid}>{mk}<span class="ch-badge">{icon(ic, 26, B.ICON_COLOR, 1.5)}</span>'
            f'<div>{kicker}<h1 class="chapter">{name}</h1></div></div>{divider()}')


def section_html(text, hs, prefix, num=None, ic="d20"):
    """One Markdown file as HTML. Its first # heading is the chapter head. In a chapter, it has the number."""
    h = wm.render(text, hs, prefix)
    first = [True]

    def head(m):
        name = CHAPTER_PREFIX.sub("", m.group(1).strip())
        is_first, first[0] = first[0], False
        return chapter_head(name, num if is_first else None, ic, anchor=prefix if is_first and prefix else None)
    return re.sub(r"<h1>(.*?)</h1>", head, h, flags=re.S)


def part(num, title, desc):
    return f"{{{{PART:{num}|{title}|{desc}}}}}"


def full_title(f, sep=", "):
    """The title and the sub title, with sep between them. A book with no sub title has only the title."""
    return f["title"] + sep + f["sub_title"] if f["sub_title"] else f["title"]


def front(c, screen=False):
    f = c.front
    d20 = big_d20(150, flat=True) if screen else B._dark_text(B.gray(big_d20(150, "#000", flat=True)))
    full = full_title(f)
    return f'''<section class="titlepage">
<div class="kicker">Dice &amp; Destiny</div>
<h1>{full_title(f, "<br>")}</h1><div class="rule"></div>
<div>{d20}</div>
<div class="sub" style="margin-top:8mm">{f["sub"]}</div>
<div class="compat">{f["compat"]}</div></section>
<section class="credits">
<p><b>Dice &amp; Destiny: {full}</b></p>
<p>Copyright {COPYRIGHT} 2026 Stiven Gjekaj. The original text and content of this book are licensed under CC BY-NC-SA 4.0 (creativecommons.org/licenses/by-nc-sa/4.0). You can share and adapt them for non-commercial use if you give credit and share your changes under the same license.</p>
<p>An independent work. Not affiliated with, endorsed, sponsored, or approved by Wizards of the Coast. Dungeons &amp; Dragons is a trademark of Wizards of the Coast LLC.</p>
<p>This work includes material from the System Reference Document 5.2 ("SRD 5.2") by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode. The statblocks of SRD 5.2 monsters in this book are laid out again.</p>
<p>The story, the places, the people, the new creatures, the treasures, the maps, and the handouts are original to this book. They are not part of the SRD 5.2. The rules that this book uses are in Dice &amp; Destiny: The Player's Compendium and The Game Master's Compendium, Edition 2.</p>
<p>{"A4 edition for reading on a screen." if screen else "Printed in black and white on A4 paper."}</p>
</section>'''


def styles(c, screen=False):
    """The stylesheet links of the page: the shared sheets, the book sheet, and the sheet of the edition."""
    edition = "screen.css" if screen else "bw.css"
    return "".join(f'<link rel="stylesheet" href="{s}">' for s in ("style.css", "book.css", c.css, edition))


def body_parts(c, dw, screen=False):
    """The sections of the book in order, as HTML with placeholders. The order:
    front matter, how to run, the player's guide, the chapters, the gazetteer,
    the appendices, the handouts, and the index."""
    book = c.book
    hs_list = handouts(book)
    hs = handlers(dw, {h[0]: h[1] for h in hs_list}, screen, c.maps)
    out = [front(c, screen), "{{TOC}}"]
    before = [(n, p, ic) for n, p, ic in (("how-to-run.md", "run", "crown"), ("players-guide.md", "guide", "sheet"))
              if section_file(n, book) is not None]
    if before:
        out.append(part("I", "Before You Play", c.parts["run"]))
        out += [section_html(section_file(n, book), hs, p, ic=ic) for n, p, ic in before]
    chs = c.chapters(book)
    if chs:
        out.append(part("II", "The Adventure", c.parts["story"]))
        out += [section_html(text, hs, key, num=num) for num, key, text in chs]
    gaz = section_file("gazetteer.md", book)
    if gaz is not None:
        out.append(part("III", "The World", c.parts["world"]))
        out.append(section_html(gaz, hs, "gazetteer", ic="compass"))
    out.append(part("IV", "Reference", c.parts["reference"]))
    out.append(appendices_html(dw, chs, c.extra_forms, c.not_before))
    out.append(handouts_html(hs_list, hs))
    out.append("<!--PARTSTART-->" + chapter_head("Index", ic="book", anchor="index") + "{{INDEX}}")
    return out, hs_list, hs


# ------------------------------------------------------------------ appendices

IDX = []  # (name, marker, main): a page that names an entry. main is True for the page of the entry itself.

# kind: (anchor prefix, appendix title, icon)
KINDS = {"creature": ("c", "Creatures", "dragon"), "person": ("p", "People", "people"),
         "treasure": ("t", "Treasures", "chest"), "place": ("l", "Places", "compass")}


def idx_mark(name, main=False):
    n = len(IDX)
    IDX.append((name, f"@@I{n}@@", main))
    return f'<span class="mark">@@I{n}@@</span>'


def entries(dw):
    """Each name of the book with its kind, its anchor, and its data, A to Z inside each kind.
    A name that two kinds share keeps the first kind, in the order of KINDS."""
    raw = ([("creature", m.name, m) for m in dw.MON] + [("person", person_name(e), e) for e in dw.NPCS]
           + [("treasure", i[0], i) for i in dw.ITEMS] + [("place", place_name(p), p) for p in dw.PLACES])
    out, seen = [], set()
    for kind, name, obj in raw:
        if name.lower() in seen:
            continue
        seen.add(name.lower())
        out.append(dict(kind=kind, name=name, obj=obj, anchor=f"{KINDS[kind][0]}-{wm.slug(name)}"))
    return sorted(out, key=lambda e: (list(KINDS).index(e["kind"]), sort_key(e["name"])))


ARTICLE = re.compile(r"^(?:The|A|An)\s+(?=\S)")


def sort_key(name):
    """Sort a name without its first article: "The Black Stone" goes under B."""
    return ARTICLE.sub("", name).lower()


def letter_of(name):
    return ARTICLE.sub("", name)[0].upper()


def mention_pattern(names, not_before=None):
    """One pattern for all names. A longer name wins over a shorter name inside it.
    not_before maps a name to the words that must not come after it."""
    names = sorted({n for n in names if n}, key=len, reverse=True)
    if not names:
        return None
    return re.compile(r"(?<![\w])(" + "|".join(_name_regex(n, not_before or {}) for n in names) + r")(?![\w])")


def _name_regex(name, not_before):
    """A name that starts with "The" also matches with "the", as in "they carry the Fennick Candle".
    A space in a name matches any white space, so a name can wrap over a line break of the source."""
    stop = f"(?!{not_before[name]})" if name in not_before else ""
    if name.startswith("The "):
        return r"[Tt]he\s+" + _words(name[4:]) + stop
    return _words(name) + stop


def _words(name):
    return r"\s+".join(re.escape(w) for w in name.split(" "))


def canonical(text):
    """The stored form of a matched name: one space between the words, and a first "the" becomes "The"."""
    text = re.sub(r"\s+", " ", text)
    return "The " + text[4:] if text.startswith("the ") else text


def forms_of(e, extra_forms=None):
    """The forms of an entry or a term in the text: its own forms or its name, and the extra forms."""
    return list(e.get("forms") or [e["name"]]) + (extra_forms or {}).get(e["name"], [])


def named_in(name, chs, extra_forms=None, not_before=None):
    """The numbers of the chapters whose text names `name`."""
    pat = mention_pattern([name] + (extra_forms or {}).get(name, []), not_before)
    return [num for num, _, text in chs if pat.search(text)]


def chapters_line(nums):
    """The chapters that name an entry, for example "Named in chapters 2, 3, and 9"."""
    if not nums:
        return ""
    n = [str(x) for x in nums]
    text = f"chapter {n[0]}" if len(n) == 1 else f"chapters {n[0]} and {n[1]}" if len(n) == 2 else \
        "chapters " + ", ".join(n[:-1]) + f", and {n[-1]}"
    return f'<div class="named-in">Named in {text}</div>'


AUTHORED_CHAPTERS = re.compile(r"\s*\bChapters?\s+\d+(?:\s*(?:,\s*and|,|and)\s*\d+)*\.?\s*$")


def without_chapters(text):
    """Remove a last sentence such as "Chapters 2 and 3." The build shows the chapters itself."""
    return AUTHORED_CHAPTERS.sub("", text)


def entry_html(e, chs, extra_forms=None, not_before=None):
    kind, name, obj = e["kind"], e["name"], e["obj"]
    head = f'<div class="entry" id="{e["anchor"]}">{idx_mark(name, main=True)}'
    line = chapters_line(named_in(name, chs, extra_forms, not_before))
    if kind == "creature":
        return f"{head}{dw_stat_html(obj, 'creature')}{line}</div>"
    if kind == "treasure":
        return f"{head}{_orig_item_html(obj)}{line}</div>"
    if kind == "person":
        role, m = obj
        role = without_chapters(role) if line else role
        if isinstance(m, str):
            return f'{head}<h4 class="sp-name">{E(name)}</h4><div class="role">{E(role)}</div>{line}</div>'
        # The statblock has the name as its heading. The role and the chapters go under its type line.
        stat = dw_stat_html(m, "person")
        cut = stat.index("</div>", stat.index('<div class="mon-type">')) + len("</div>")
        return f'{head}{stat[:cut]}<div class="role">{E(role)}</div>{line}{stat[cut:]}</div>'
    text = place_text(obj)
    text = without_chapters(text) if line else text
    return f'{head}<h4 class="sp-name">{E(name)}</h4>{f"<p>{E(text)}</p>" if text else ""}{line}</div>'


def appendices_html(dw, chs, extra_forms=None, not_before=None):
    """One appendix for each kind that has entries, A to Z, with the chapters that name each entry."""
    es = entries(dw)
    out, letter_no = [], 0
    for kind, (_, title, ic) in KINDS.items():
        group = [e for e in es if e["kind"] == kind]
        if not group:
            continue
        label = f"Appendix {chr(ord('A') + letter_no)}: {title}"
        letter_no += 1
        out.append(chapter_head(label, ic=ic, anchor=f"appendix-{title.lower()}"))
        out.append('<div class="appendix cols2 compendium">')
        letter = None
        for e in group:
            first = letter_of(e["name"])
            if first != letter:
                letter = first
                out.append(f'<div class="letter">{E(letter)}</div>')
            out.append(entry_html(e, chs, extra_forms, not_before))
        out.append("</div>")
    return "\n".join(out)


def handouts_html(hs_list, hs):
    """The handouts appendix. Each handout starts on a right-hand page. In print, the page after it is blank."""
    if not hs_list:
        return ""
    out = [chapter_head("Handouts", ic="scroll", anchor="handouts"),
           '<p class="chapter-intro">Each handout starts on a right-hand page. A handout of one page has nothing '
           "on the back. Copy the pages or print them, and give them to the players when the chapter tells you.</p>"]
    for hid, title, text in hs_list:
        mk = B.marker("sub", title)
        ANCHOR_MARK[f"handout-{hid}"] = B.TOC[-1][2]
        # The page break is on the flex box that holds the marker, as in a chapter head. When the
        # break is on a parent of the marker, Chrome puts the marker on the page before the break.
        out.append(f'<!--PARTSTART--><div class="handout-top" id="handout-{hid}">{mk}</div>'
                   f'<section class="handout">{wm.render(text, hs, f"handout-{hid}")}</section>')
    return "\n".join(out)


# ------------------------------------------------------------------ index

SKIP_TAGS = {"h1", "h2", "a", "title", "style", "script", "svg"}
# A name in a small heading, such as the name of a statblock or a treasure in a chapter, gets a marker
# but no link. The chapter and section heads (h1, h2) keep their text.
HEAD_TAGS = {"h3", "h4", "h5", "h6"}
OPEN_TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)")


def mark_mentions(h, es, screen=False, extra_forms=None, not_before=None):
    """Put an index marker after each name of an entry in the text. On the screen, the name links to its entry.
    The text of chapter and section heads, links, SVG, and markers does not change. A name in a small
    heading gets a marker but no link."""
    names = {}
    for e in es:
        for form in forms_of(e, extra_forms):
            names.setdefault(E(form, quote=False), (e["name"], e["anchor"]))
    pat = mention_pattern(names, not_before)
    if not pat:
        return h
    out, skip, spans, head = [], 0, [], 0

    def rep(m):
        name, anchor = names[canonical(m.group(1))]
        link = screen and anchor and not head
        word = f'<a class="xref" href="#{anchor}">{m.group(1)}</a>' if link else m.group(1)
        return word + idx_mark(name)
    for tok in re.split(r"(<[^>]*>)", h):
        if tok.startswith("<"):
            m = OPEN_TAG.match(tok)
            if m and not tok.endswith("/>"):
                close, tag = m.group(1) == "/", m.group(2).lower()
                if tag in SKIP_TAGS:
                    skip += -1 if close else 1
                elif tag in HEAD_TAGS:
                    head += -1 if close else 1
                elif tag == "span":
                    if not close:
                        spans.append('class="mark"' in tok)
                        skip += spans[-1]
                    elif spans:
                        skip -= spans.pop()
            out.append(tok)
        elif skip > 0 or not tok.strip():
            out.append(tok)
        else:
            out.append(pat.sub(rep, tok))
    return "".join(out)


def index_terms(es, terms):
    """The index terms as entries with no anchor. A term with the name of an entry is left out."""
    known = {e["name"].lower() for e in es}
    return [dict(kind="term", name=n, anchor=None, obj=None, forms=forms) for n, forms in terms if n.lower() not in known]


def page_list(all_, mains):
    """The pages of a name: a run of three or more pages becomes a range, as in "12-15".
    The page of the entry itself is in bold and stays alone."""
    out, run = [], []

    def flush():
        if len(run) >= 3:
            out.append(f"{run[0]}-{run[-1]}")
        else:
            out.extend(str(p) for p in run)
        run.clear()
    for p in sorted(all_):
        if p in mains:
            flush()
            out.append(f"<b>{p}</b>")
        elif run and p == run[-1] + 1:
            run.append(p)
        else:
            flush()
            run.append(p)
    flush()
    return ", ".join(out)


def index_html(pages, es, screen=False):
    """Each name, A to Z, with its pages. The page of the entry itself is in bold."""
    found = {}
    for name, mk, main in IDX:
        p = pages.get(mk)
        if p:
            all_, mains = found.setdefault(name, (set(), set()))
            all_.add(p)
            if main:
                mains.add(p)
    anchors = {}
    for e in es:
        anchors.setdefault(e["name"], e["anchor"])
    out, letter = ['<div class="index">'], None
    for name in sorted(anchors, key=sort_key):
        first = letter_of(name)
        if first != letter:
            letter = first
            out.append(f'<div class="letter">{E(letter)}</div>')
        all_, mains = found.get(name, (set(), set()))
        pg = page_list(all_, mains)
        nm = f'<a href="#{anchors[name]}">{E(name)}</a>' if screen and anchors[name] else E(name)
        out.append(f'<p>{nm} <span class="pg">{pg}</span></p>')
    out.append("</div>")
    return "\n".join(out)


PAGE_REF = re.compile(r"@@PAGE:([\w-]+)@@")


def fill(body, pages, es, screen=False):
    """Put the page numbers into the contents, the index, and the page references."""
    s = body.replace("{{TOC}}", B.toc_html(pages, links=screen)).replace("{{INDEX}}", index_html(pages, es, screen))
    return PAGE_REF.sub(lambda m: str(pages.get(ANCHOR_MARK.get(m.group(1)), "?")), s)


def recto_marks(body):
    """The first marker of each chunk that must start on a right-hand page, in order."""
    return [re.search(r"@@T\d+@@", c).group(0) for c in body.split("<!--PARTSTART-->")[1:]]


def insert_blanks(s, blanks):
    chunks = s.split("<!--PARTSTART-->")
    return chunks[0] + "".join(('<div class="blankpage"></div>' if i in blanks else "") + c for i, c in enumerate(chunks[1:]))


# ------------------------------------------------------------------ build

def expand(c, screen=False, inside_mm=None, dw=None):
    """The full HTML of the book with placeholders for the page numbers, and the entries.
    c.post filters the HTML after the front matter, after the mentions are marked."""
    B.TOC.clear()
    IDX.clear()
    ANCHOR_MARK.clear()
    WARNINGS.clear()
    dw = dw if dw is not None else c.content()
    out, _, _ = body_parts(c, dw, screen)
    es = entries(dw)
    es = es + index_terms(es, c.index_terms)
    s = B.parts("\n".join(out))
    head, rest = s.split("{{TOC}}", 1)
    s = head + "{{TOC}}" + c.post(mark_mentions(rest, es, screen, c.extra_forms, c.not_before))
    import compendium as comp
    import keep_tables
    s = keep_tables.keep_small_tables(comp.no_em_dash(s))
    B.TOC.sort(key=lambda t: s.index(t[2]))
    return page_html(c, s, screen, inside_mm), es


def find_marks(out):
    """The page of each marker in <out>.pdf: the contents markers and the index markers."""
    txt = subprocess.run(["pdftotext", f"{out}.pdf", "-"], capture_output=True, text=True).stdout
    return marks_in_pages(txt.split("\f"))


def marks_in_pages(pages_text):
    """The page of each marker in the text of the pages. A marker at the top of a page after a page
    break also shows at the end of the page before it. The last page is the page of the marker."""
    pages = {}
    for i, pg in enumerate(pages_text):
        for m in re.findall(r"@@[TI]\d+@@", pg):
            pages[m] = i + 1
    return pages


def passes(out, body, es, screen=False, render=None, find=None, count=None):
    """Render the book until the page numbers do not change. In print, each recto chunk starts on a
    right-hand page. The method is the method of build.build. Return the pages and the contents.

    count(out) gives the page count of a render. With it, the build stops if the last render, with no
    marker text, does not have the page count of the render that gave the page numbers."""
    render, find = render or B.render, find or find_marks
    toc_entries, rectos = list(B.TOC), recto_marks(body)
    blanks, pages = set(), {}
    for it in range(12):
        B.TOC[:] = toc_entries
        s = fill(body, pages, es, screen)
        if not screen:
            s = insert_blanks(s, blanks)
        render(out, s)
        new = find(out)
        if not screen and it == 0 and rectos and all(mk in new for mk in rectos):
            rp = [new[mk] for mk in rectos]
            blanks = B.plan_blanks(rp)
            pages = B.shift_pages(new, rp, blanks)
            print(f"  pass {it + 1}: {len(new)} markers, planned blanks={sorted(blanks)}", flush=True)
            continue
        moved = False
        for i, mk in enumerate([] if screen else rectos):
            p = new.get(mk)
            if p and p % 2 == 0:
                blanks.symmetric_difference_update({i})
                moved = True
                break
        print(f"  pass {it + 1}: {len(new)} markers, blanks={sorted(blanks)}", flush=True)
        if not moved and new == pages:
            break
        pages = new
    measured = count(out) if count else None
    # The last render keeps the markers and hides them. A hidden box keeps its place, so the layout is the
    # layout that gave the page numbers, and Chrome does not print the hidden text. When the build removed
    # the text, the layout changed and the book had one page more.
    render(out, hide_marks(s))
    if count and count(out) != measured:
        raise SystemExit(f"{out}: the last render has {count(out)} pages, not {measured}. "
                         "Hiding the markers changed the layout. Check .mark in the book stylesheet.")
    return pages, toc_entries


HIDE_MARKS = "<style>.mark { visibility: hidden; }</style>"


def hide_marks(s):
    """The page with each marker hidden. visibility: hidden does not change the layout."""
    return s.replace("</head>", HIDE_MARKS + "</head>", 1) if "</head>" in s else HIDE_MARKS + s


INSIDE_START_MM = 16  # the first guess. The build changes it to the value of the Lulu table for the page count.


def work_name(out, pid=None):
    """The name of the work files of one build: books/<work>.html and <work>.pdf. Each process has its own
    work files, so two builds at the same time do not write into the PDF of the other build."""
    return f"{out}-work-{os.getpid() if pid is None else pid}"


def publish(work, out):
    """Move the finished work files to books/<out>.html and <out>.pdf. A move in one folder is atomic."""
    os.replace(os.path.join("books", f"{work}.html"), os.path.join("books", f"{out}.html"))
    os.replace(f"{work}.pdf", f"{out}.pdf")


def remove_work(work):
    for path in (os.path.join("books", f"{work}.html"), f"{work}.pdf"):
        if os.path.exists(path):
            os.remove(path)


def build_book(c, screen=False, expand_fn=None, passes_fn=None):
    """Build the print interior (<name>.pdf) or the screen interior (<name>_screen.pdf).

    expand_fn(screen, inside_mm) and passes_fn replace expand and passes. The default is the
    functions of this module."""
    from pypdf import PdfReader
    expand_fn = expand_fn or (lambda s, i: expand(c, s, i))
    passes_fn = passes_fn or passes
    out = f"{c.name}_screen" if screen else c.name
    work = work_name(out)
    inside = None if screen else INSIDE_START_MM
    try:
        for _ in range(4):
            body, es = expand_fn(screen, inside)
            pages, toc_entries = passes_fn(work, body, es, screen, count=lambda o: len(PdfReader(f"{o}.pdf").pages))
            if screen:
                B.add_outline(f"{work}.pdf", B.outline(toc_entries, pages))
                break
            n = len(PdfReader(f"{work}.pdf").pages)
            need = B.lulu_inside_mm(n)
            if need == inside:
                print(f"  {n} pages, inside margin {inside} mm", flush=True)
                break
            print(f"  {n} pages need a {need} mm inside margin, not {inside} mm. Build again.", flush=True)
            inside = need
        else:
            raise SystemExit(f"{c.name}: the inside margin does not settle")
        publish(work, out)
    finally:
        remove_work(work)
    for w in sorted(set(WARNINGS)):
        print("WARNING:", w)


def page_html(c, body, screen=False, inside_mm=None):
    style = styles(c, screen) + (B.margin_css(inside_mm) if inside_mm else "")
    title = full_title(c.front)
    return (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>{title}</title>\n'
            f'{style}\n</head>\n<body class="{"screen" if screen else "print"}">\n{body}\n</body>\n</html>\n')
