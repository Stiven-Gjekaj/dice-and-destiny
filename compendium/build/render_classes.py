"""Render the original classes (content/classes) into HTML for the Player's Compendium."""
import html

from content.classes import CLASSES
from icons import icon
from orig_render import feature_text

E = html.escape
TRAITS = [("Primary Ability", "primary"), ("Saving Throws", "saves"), ("Skills", "skills"),
          ("Weapons", "weapons"), ("Tools", "tools"), ("Armor Training", "armor"),
          ("Starting Equipment", "equipment")]


def prof(level):
    """The Proficiency Bonus at a level, as text."""
    return f"+{2 + (level - 1) // 4}"


def level_table(c):
    """The rows of the features table: one list of feature names for each level 1 to 20."""
    rows = [[] for _ in range(20)]
    for lv, name, _ in c["features"]:
        rows[lv - 1].append(name)
    for name, levels in c.get("also_at", {}).items():
        for lv in levels:
            rows[lv - 1].append(name)
    for lv in c["subclass_levels"][1:]:
        rows[lv - 1].append("Subclass feature")
    return rows


def class_html(c, subs=(), newpage=True):
    """The full chapter of one class. `subs` is the list of the names of its subclasses."""
    hd = c["hit_die"]
    nb = " newpage" if newpage else ""
    out = [f'<div class="class-banner{nb}"><div class="ch-num">Class</div><h1 class="classname">{E(c["name"])}</h1>'
           f'<div class="tagline">{E(c["tagline"])}</div><span class="crest">{icon(c["icon"], 40, "#c99a3e", 1.4)}</span></div>']
    out.append('<div class="class-head"><div>')
    out.append(f'<p><span class="tag">{E(c["role"])}</span><span class="tag">Difficulty: {E(c["difficulty"])}</span></p>')
    out.append(f'<h3>How to Play</h3><p>{E(c["guide"]["play"])}</p>')
    out.append(f'<div class="box"><h4>Quick beginner build</h4><p>{E(c["guide"]["build"])}</p></div>')
    out.append('</div><div class="traits">')
    out.append(f'<div><b>Hit Point Die</b>d{hd} per {E(c["name"])} level</div>')
    for label, k in TRAITS:
        out.append(f'<div><b>{label}</b>{E(c[k])}</div>')
    out.append(f'<div><b>HP at Level 1</b>{hd} + Con modifier</div>')
    out.append(f'<div><b>HP per Level After</b>1d{hd} (or {hd // 2 + 1}) + Con modifier</div>')
    out.append('</div></div>')

    head = "".join(f'<th class="c">{E(n)}</th>' for n, _ in c["columns"])
    out.append(f'<table class="compact"><caption>{E(c["name"])} Features by Level</caption><thead><tr>'
               f'<th class="c">Lvl</th><th class="c">Prof.</th><th>Features</th>{head}</tr></thead><tbody>')
    for lv, names in enumerate(level_table(c), start=1):
        cells = "".join(f'<td class="c">{E(str(v[lv - 1]))}</td>' for _, v in c["columns"])
        out.append(f'<tr><td class="c">{lv}</td><td class="c">{prof(lv)}</td><td>{E(", ".join(names)) or "–"}</td>{cells}</tr>')
    out.append('</tbody></table>')

    out.append(f'<h2>{icon("book", 16)}Class Features</h2><dl class="feat cols2">')
    for lv, name, text in c["features"]:
        out.append(f'<div class="avoid"><dt><span class="lv">{lv}</span>{E(name)}</dt><dd>{feature_text(text)}</dd></div>')
    out.append('</dl>')
    for title, entries in c.get("lists", []):
        out.append(f'<h3>{E(title)}</h3><dl class="feat cols2">')
        for name, text in entries:
            out.append(f'<div class="avoid"><dt>{E(name)}</dt><dd>{feature_text(text)}</dd></div>')
        out.append('</dl>')
    if subs:
        out.append(f'<p class="small muted"><b>Subclasses in this book (Chapter 24):</b> {E(", ".join(subs))}.</p>')
    return "\n".join(out)


def classes_html():
    """All original classes, in the order of the files."""
    from content.subclasses import SUBS
    return "\n".join(class_html(c, [s[0] for s in SUBS.get(c["key"], [])], newpage=i > 0)
                     for i, c in enumerate(CLASSES))
