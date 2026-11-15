"""Render original (non-SRD) content into HTML for the compendiums."""
import html, re
from collections import defaultdict
import content.backgrounds
import content.feats
import content.species
import content.spells
from content.subclasses import SUBS
import content.downtime
import content.items
from content.monsters import MON
from monster_engine import crs, XP

E = html.escape
ORDER = "barbarian bard cleric druid fighter monk paladin ranger rogue sorcerer warlock wizard".split()
MONSTERS = sorted(MON, key=lambda m: m.name)
ITEMS = sorted(content.items.ITEMS, key=lambda i: i[0])
TAG = '<span class="orig">Original</span>'


LABEL = re.compile(r"\[\[([^\[\]]+)\]\]")


def feature_text(text):
    """Escape the text of a subclass feature. Show each [[label]] in bold."""
    return LABEL.sub(r"<b>\1</b>", E(text))


def sub_names(c):
    return [s[0] for s in SUBS[c]]


def subclass_order(subs, new_keys):
    """The SRD classes, then each new class that has subclasses, in the order of new_keys."""
    return ORDER + [k for k in new_keys if k in subs and k not in ORDER]


def subclasses_html():
    from content.classes import CLASS_KEYS
    out = []
    for c in subclass_order(SUBS, CLASS_KEYS):
        out.append(f'<h2>{c.capitalize()} Subclasses</h2><div class="cols2 compendium">')
        for name, tag, feats in SUBS[c]:
            out.append(f'<div class="entry"><h4 class="sp-name">{E(name)}</h4><div class="sp-meta"><i>{c.capitalize()} subclass · {E(tag)}</i></div>')
            for lv, fn, tx in feats:
                out.append(f'<div class="ft"><h4><span class="lv">{lv}</span>{E(fn)}</h4><p>{feature_text(tx)}</p></div>')
            out.append("</div>")
        out.append("</div>")
    return "\n".join(out)


def backgrounds_html():
    out = ['<div class="grid2">']
    for n, ab, sk, tool, feat, eq, flav in content.backgrounds.BACKGROUNDS:
        out.append(f'<div class="box"><h4>{E(n)}</h4><p><i>{E(flav)}</i></p><p><b>Ability Scores:</b> {E(ab)}<br><b>Feat:</b> {E(feat)}<br>'
                   f'<b>Skill Proficiencies:</b> {E(sk)}<br><b>Tool Proficiency:</b> {E(tool)}<br><b>Equipment:</b> Choose A or B: (A) {E(eq)}; or (B) 50 GP</p></div>')
    out.append("</div>")
    return "\n".join(out)


def species_html():
    out = []
    for n, size, speed, desc, traits in content.species.SPECIES:
        out.append(f'<div class="species"><h3>{E(n)}</h3><p><i>{E(desc)}</i></p><p><b>Size:</b> {E(size)} · <b>Speed:</b> {E(speed)}</p><div class="cols2 compendium">')
        for tn, tt in traits:
            out.append(f'<div class="entry"><p><b><i>{E(tn)}.</i></b> {E(tt)}</p></div>')
        out.append("</div></div>")
    return "\n".join(out)


def feats_html():
    out = []
    for t in ["Origin", "General", "Fighting Style", "Epic Boon"]:
        out.append(f'<h3>{t} Feats</h3><div class="cols2 compendium">')
        for n, ty, pre, tx in [f for f in content.feats.FEATS if f[1] == t]:
            p = f" (Prerequisite: {E(pre)})" if pre else ""
            out.append(f'<div class="entry"><h4 class="sp-name">{E(n)}</h4><div class="sp-meta"><i>{t} Feat{p}</i></div><p>{E(tx)}</p></div>')
        out.append("</div>")
    return "\n".join(out)


def spells_html():
    sp = sorted(content.spells.SPELLS, key=lambda s: s[0])
    by = defaultdict(lambda: defaultdict(list))
    for s in sp:
        for c in s[3]:
            by[c][s[1]].append(s[0])
    out = ['<h2>Original Spells by Class</h2><div class="cols3 tight-list">']
    for c in sorted(by):
        out.append(f'<div class="lvl-block"><h4>{c}</h4><ul>')
        for lv in sorted(by[c]):
            out.append(f'<li><b>{"Cantrips" if lv == 0 else "Level " + str(lv)}:</b> {", ".join(E(n) for n in by[c][lv])}</li>')
        out.append("</ul></div>")
    out.append('</div><h2>Original Spell Descriptions</h2><div class="cols2 compendium">')
    for n, lv, sch, cls, t, rng, comp, dur, conc, rit, desc, hi in sp:
        line = f"{sch} Cantrip" if lv == 0 else f"Level {lv} {sch}"
        ct = t + (" or Ritual" if rit else "")
        d = ("Concentration, up to " + dur) if conc else dur
        h = f'<p><b><i>{"Cantrip Upgrade." if lv == 0 else "Using a Higher-Level Spell Slot."}</i></b> {E(hi)}</p>' if hi else ""
        out.append(f'<div class="spell"><h4 class="sp-name">{E(n)}</h4><div class="sp-meta"><i>{line} ({", ".join(cls)})</i></div>'
                   f'<div class="sp-stats"><b>Casting Time:</b> {E(ct)}<br><b>Range:</b> {E(rng)}<br><b>Components:</b> {E(comp)}<br><b>Duration:</b> {E(d)}</div>'
                   f'<div class="sp-desc"><p>{E(desc)}</p>{h}</div></div>')
    out.append("</div>")
    return "\n".join(out)


def bestiary_index_html():
    by = defaultdict(list)
    for m in MONSTERS:
        by[m.cr].append(m.name)
    out = ['<div class="cols3 cr-index">']
    for cr in sorted(by):
        out.append(f'<p><b>CR {crs(cr)}</b> <span class=muted>({XP[cr]:,} XP)</span><br>{", ".join(E(n) for n in by[cr])}</p>')
    out.append("</div>")
    return "\n".join(out)


def bestiary_html():
    out, letter = ['<div class="cols2 compendium">'], None
    for m in MONSTERS:
        L = m.name[0].upper()
        if L != letter:
            letter = L; out.append(f'<div class="letter">{L}</div>')
        out.append(m.html())
    out.append("</div>")
    return "\n".join(out)


RAR = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact"]


def items_index_html():
    by = defaultdict(list)
    for i in ITEMS:
        by[i[2]].append(i[0])
    out = ['<div class="cols3 cr-index">']
    for r in RAR:
        out.append(f"<p><b>{r}</b> <span class=muted>({len(by[r])})</span><br>{', '.join(E(n) for n in by[r])}</p>")
    out.append("</div>")
    return "\n".join(out)


def items_html():
    out, letter = ['<div class="cols2 compendium">'], None
    for n, cat, rar, att, tx in ITEMS:
        L = n[0].upper()
        if L != letter:
            letter = L; out.append(f'<div class="letter">{L}</div>')
        a = f" ({att})" if att else ""
        out.append(f'<div class="mitem"><h4 class="sp-name">{E(n)}</h4><div class="sp-meta"><i>{E(cat)}, {rar}{a}</i></div><p>{E(tx)}</p></div>')
    out.append("</div>")
    return "\n".join(out)


def strongholds_html():
    return content.downtime.STRONGHOLDS


if __name__ == "__main__":
    for f in [subclasses_html, backgrounds_html, species_html, feats_html, spells_html, bestiary_index_html, bestiary_html, items_index_html, items_html]:
        print(f.__name__, len(f()))
