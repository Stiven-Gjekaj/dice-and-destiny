"""Compendium sections generated from the SRD 5.2 (2024) data, CC-BY-4.0 Wizards of the Coast."""
import json, re, html
from collections import defaultdict, OrderedDict
import markdown as mdlib

import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
load = lambda n: json.load(open(f"{D}/{n}"))


def md(text, small_tables=True):
    if not text:
        return ""
    t = text.replace("[Column data]", "").replace("\r", "")
    t = re.sub(r"^\s*Table:\s*(.+)$", r"\n**\1**\n", t, flags=re.M)
    # make sure pipe tables are separated from paragraphs
    lines, out = t.split("\n"), []
    for ln in lines:
        if ln.lstrip().startswith("|") and out and out[-1].strip() and not out[-1].lstrip().startswith("|"):
            out.append("")
        if out and out[-1].lstrip().startswith("|") and ln.strip() and not ln.lstrip().startswith("|"):
            out.append("")
        out.append(ln)
    t = "\n".join(out)
    h = mdlib.markdown(t, extensions=["tables", "sane_lists"])
    if small_tables:
        h = h.replace("<table>", '<table class="compact">')
    return h


def esc(s):
    return html.escape(s or "")


def sign(n):
    return f"+{n}" if n >= 0 else f"−{abs(n)}"


# ------------------------------------------------------------------ spells
LEVEL_NAME = {0: "Cantrip", 1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th"}
CAST = {"action": "Action", "bonus-action": "Bonus Action", "reaction": "Reaction",
        "1minute": "1 minute", "10minutes": "10 minutes", "1hour": "1 hour", "8hours": "8 hours"}
CLASSES = ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"]


def spells():
    return sorted(load("all_spells.json"), key=lambda s: s["name"])


def spell_line(s):
    lv = s["level"]
    school = s["school"]["name"]
    return f"{school} Cantrip" if lv == 0 else f"Level {lv} {school}"


def spell_lists_html():
    sp = spells()
    out = []
    for c in CLASSES:
        bylvl = defaultdict(list)
        for s in sp:
            if any(x["name"] == c for x in s["classes"]):
                bylvl[s["level"]].append(s)
        if not bylvl:
            continue
        out.append(f'<div class="spell-list keep-head"><h3>{c} Spells</h3><div class="cols3 tight-list">')
        for lv in sorted(bylvl):
            items = "".join(
                f'<li>{esc(s["name"])}{" <i>C</i>" if s["concentration"] else ""}{" <i>R</i>" if s["ritual"] else ""}</li>'
                for s in bylvl[lv])
            out.append(f'<div class="lvl-block"><h4>{"Cantrips" if lv == 0 else LEVEL_NAME[lv] + " level"}</h4><ul>{items}</ul></div>')
        out.append("</div></div>")
    return "\n".join(out)


def spell_html(s):
    comps = []
    if s["verbal"]: comps.append("V")
    if s["somatic"]: comps.append("S")
    if s["material"]:
        m = "M"
        if s.get("material_specified"):
            m += f" ({esc(s['material_specified'])})"
        comps.append(m)
    ct = CAST.get(s["casting_time"], s["casting_time"])
    if s["casting_time"] == "reaction" and s.get("reaction_condition"):
        ct += f", {esc(s['reaction_condition'])}"
    if s["ritual"]:
        ct += " or Ritual"
    dur = s["duration"].capitalize() if s["duration"] else "—"
    if s["concentration"]:
        dur = "Concentration, up to " + s["duration"]
    classes = ", ".join(x["name"] for x in s["classes"])
    hl = ""
    if s.get("higher_level"):
        label = "Cantrip Upgrade." if s["level"] == 0 else "Using a Higher-Level Spell Slot."
        hl = f'<p><b><i>{label}</i></b> {esc(s["higher_level"])}</p>'
    return (f'<div class="spell"><h4 class="sp-name">{esc(s["name"])}</h4>'
            f'<div class="sp-meta"><i>{spell_line(s)} ({classes})</i></div>'
            f'<div class="sp-stats"><b>Casting Time:</b> {ct}<br><b>Range:</b> {esc(s["range_text"])}<br>'
            f'<b>Components:</b> {", ".join(comps) or "—"}<br><b>Duration:</b> {esc(dur)}</div>'
            f'<div class="sp-desc">{md(s["desc"])}{hl}</div></div>')


def spells_full_html():
    sp = spells()
    out, letter = ['<div class="cols2 compendium">'], None
    for s in sp:
        L = s["name"][0].upper()
        if L != letter:
            letter = L
            out.append(f'<div class="letter">{L}</div>')
        out.append(spell_html(s))
    out.append("</div>")
    return "\n".join(out)


# ------------------------------------------------------------------ monsters
ABBR = [("strength", "Str"), ("dexterity", "Dex"), ("constitution", "Con"),
        ("intelligence", "Int"), ("wisdom", "Wis"), ("charisma", "Cha")]


def cr_str(cr):
    return {0.125: "1/8", 0.25: "1/4", 0.5: "1/2"}.get(cr, str(int(cr)) if cr == int(cr) else str(cr))


def prof_from_cr(cr):
    if cr < 5: return 2
    return 2 + int((cr - 1) // 4)


def creatures():
    return sorted(load("all_creatures.json"), key=lambda c: c["name"])


def creature_html(c):
    sp = c["speed"]
    parts = [f'{sp.get("walk", 0)} ft.']
    for k in ("burrow", "climb", "fly", "swim"):
        if sp.get(k):
            parts.append(f'{k.capitalize()} {sp[k]} ft.' + (" (hover)" if k == "fly" and sp.get("hover") else ""))
    sz, ty = c["size"]["name"], c["type"]["name"]
    sub = f" ({c['subcategory']})" if c.get("subcategory") else ""
    ac = f'{c["armor_class"]}' + (f' ({esc(c["armor_detail"])})' if c.get("armor_detail") else "")
    hp = f'{c["hit_points"]} ({c["hit_dice"]})' if c.get("hit_dice") else str(c["hit_points"])
    init = c.get("initiative_bonus") or 0
    rows = ""
    for k, a in ABBR:
        sc = c["ability_scores"][k]; mo = c["modifiers"][k]; sv = c["saving_throws"].get(k, mo)
        rows += f'<td><b>{a}</b></td><td>{sc}</td><td>{sign(mo)}</td><td>{sign(sv)}</td>'
    ab = ('<table class="mon-ab"><thead><tr>' + '<th></th><th></th><th>Mod</th><th>Save</th>' * 3 + '</tr></thead><tbody>'
          + f'<tr>{rows[: rows.index("<td><b>Int")]}</tr><tr>{rows[rows.index("<td><b>Int"):]}</tr></tbody></table>')
    lines = []
    if c.get("skill_bonuses"):
        lines.append("<b>Skills</b> " + ", ".join(f"{k.replace('_', ' ').title()} {sign(v)}" for k, v in c["skill_bonuses"].items()))
    ri = c["resistances_and_immunities"]
    if ri.get("damage_vulnerabilities_display"): lines.append("<b>Vulnerabilities</b> " + esc(ri["damage_vulnerabilities_display"].title()))
    if ri.get("damage_resistances_display"): lines.append("<b>Resistances</b> " + esc(ri["damage_resistances_display"].title()))
    imm = "; ".join(x for x in [ri.get("damage_immunities_display", "").title(), ri.get("condition_immunities_display", "").title()] if x)
    if imm: lines.append("<b>Immunities</b> " + esc(imm))
    senses = []
    for k, n in (("blindsight_range", "Blindsight"), ("darkvision_range", "Darkvision"), ("tremorsense_range", "Tremorsense"), ("truesight_range", "Truesight")):
        if c.get(k): senses.append(f"{n} {int(c[k])} ft.")
    senses.append(f"Passive Perception {c.get('passive_perception', 10)}")
    lines.append("<b>Senses</b> " + ", ".join(senses))
    lang = (c.get("languages") or {}).get("as_string") or "None"
    lines.append("<b>Languages</b> " + esc(lang))
    cr = c["challenge_rating"]
    xp = c.get("experience_points")
    lines.append(f"<b>CR</b> {cr_str(cr)} (XP {xp:,}; PB +{c.get('proficiency_bonus') or prof_from_cr(cr)})" if xp is not None else f"<b>CR</b> {cr_str(cr)}")

    def block(title, items, intro=""):
        if not items: return ""
        s = f'<div class="mon-sec">{title}</div>' + intro
        for a in items:
            nm = esc(a["name"])
            ul = a.get("usage_limits")
            if ul:
                if ul["type"] == "RECHARGE_ON_ROLL": nm += f" (Recharge {ul['param']}–6)" if ul["param"] < 6 else " (Recharge 6)"
                elif ul["type"] == "PER_DAY": nm += f" ({ul['param']}/Day)"
                elif ul["type"] == "RECHARGE_AFTER_REST": nm += " (Recharges after a Short or Long Rest)"
            desc = esc(a["desc"]).replace("\n\n", "</p><p>").replace("\n", "<br>")
            desc = re.sub(r"(Melee Attack Roll:|Ranged Attack Roll:|Melee or Ranged Attack Roll:|\w+ Saving Throw:|Failure:|Success:|Failure or Success:|Hit:|Trigger:|Response:|First Failure:|Second Failure:)", r"<i>\1</i>", desc)
            s += f"<p><b><i>{nm}.</i></b> {desc}</p>"
        return s

    acts = sorted(c["actions"], key=lambda a: (a.get("order_in_statblock") or 0, a["name"]))
    g = lambda t: [a for a in acts if a["action_type"] == t]
    leg_intro = ""
    if g("LEGENDARY_ACTION"):
        leg_intro = (f"<p class='small'><i>Legendary Action Uses: 3. Immediately after another creature's turn, the {esc(c['name'].lower())} "
                     "can expend a use to take one of the following actions. It regains all expended uses at the start of each of its turns.</i></p>")
    body = (block("Traits", [{"name": t["name"], "desc": t["desc"], "usage_limits": None} for t in c.get("traits", [])])
            + block("Actions", g("ACTION")) + block("Bonus Actions", g("BONUS_ACTION"))
            + block("Reactions", g("REACTION")) + block("Legendary Actions", g("LEGENDARY_ACTION"), leg_intro))
    return (f'<div class="monster" id="m-{c["key"]}"><h4 class="mon-name">{esc(c["name"])}</h4>'
            f'<div class="mon-type"><i>{sz} {ty}{esc(sub)}, {esc(c.get("alignment") or "unaligned").title()}</i></div>'
            f'<div class="mon-top"><b>AC</b> {ac} &nbsp; <b>Initiative</b> {sign(init)} ({10 + init})<br><b>HP</b> {hp}<br><b>Speed</b> {", ".join(parts)}</div>'
            f'{ab}<div class="mon-lines">{"<br>".join(lines)}</div>{body}</div>')


def bestiary_html():
    out, letter = ['<div class="cols2 compendium">'], None
    for c in creatures():
        L = c["name"][0].upper()
        if L != letter:
            letter = L; out.append(f'<div class="letter">{L}</div>')
        out.append(creature_html(c))
    out.append("</div>")
    return "\n".join(out)


def monsters_by_cr_html():
    by = defaultdict(list)
    for c in creatures():
        by[c["challenge_rating"]].append(c)
    out = ['<div class="cols3 cr-index">']
    for cr in sorted(by):
        xp = by[cr][0].get("experience_points")
        names = ", ".join(esc(c["name"]) for c in by[cr])
        out.append(f'<p><b>CR {cr_str(cr)}</b>{f" <span class=muted>({xp:,} XP)</span>" if xp is not None else ""}<br>{names}</p>')
    out.append("</div>")
    return "\n".join(out)


def monsters_by_type_html():
    by = defaultdict(list)
    for c in creatures():
        by[c["type"]["name"]].append(c)
    out = ['<div class="cols3 cr-index">']
    for t in sorted(by):
        names = ", ".join(f'{esc(c["name"])} <span class=muted>({cr_str(c["challenge_rating"])})</span>' for c in by[t])
        out.append(f"<p><b>{t}</b><br>{names}</p>")
    out.append("</div>")
    return "\n".join(out)


# ------------------------------------------------------------------ magic items
RARITY_ORDER = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact", "Varies"]


TITLE_FIX = {"Ammunition": "Ammunition, +1, +2, or +3", "Ammunition of": "Ammunition of Slaying",
             "Battleaxe": "Weapon, +1, +2, or +3", "Breastplate": "Armor, +1, +2, or +3", "Berserker": "Berserker Axe",
             "Dancing": "Dancing Sword", "Demon": "Demon Armor", "Dwarven": "Dwarven Plate",
             "Glaive of Life Stealing": "Sword of Life Stealing", "Glaive of Sharpness": "Sword of Sharpness",
             "Glaive of Wounding": "Sword of Wounding", "Half Plate Armor of Etherealness": "Armor of Etherealness",
             "Shield": "Shield, +1, +2, or +3", "Vicious": "Vicious Weapon", "Vorpal": "Vorpal Sword"}


def magic_items_grouped():
    m = load("all_magicitems.json")
    groups = OrderedDict()
    for x in sorted(m, key=lambda x: x["name"]):
        groups.setdefault(x["desc"], []).append(x)
    items = []
    for desc, xs in groups.items():
        names = [x["name"] for x in xs]
        if len(xs) == 1:
            title = names[0]
        else:
            base = re.sub(r"\s*\(.*?\)\s*$", "", names[0])
            pref = names[0]
            for n in names[1:]:
                k = 0
                while k < min(len(pref), len(n)) and pref[k] == n[k]:
                    k += 1
                pref = pref[:k]
            pref = re.sub(r"[\s(,+]+$", "", pref).strip()
            title = base if all(n.startswith(base) for n in names) else (pref or base)
            if not title:
                title = names[0]
        title = TITLE_FIX.get(title, title)
        rar = sorted({x["rarity"]["name"] for x in xs}, key=lambda r: RARITY_ORDER.index(r) if r in RARITY_ORDER else 9)
        cat = xs[0]["category"]["name"]
        att = xs[0].get("requires_attunement")
        attd = xs[0].get("attunement_detail") or ""
        items.append(dict(title=title, names=names, rarity=rar, cat=cat, att=att, attd=attd, desc=desc,
                          rar_of={x["name"]: x["rarity"]["name"] for x in xs}))
    return sorted(items, key=lambda i: i["title"])


def magic_item_html(i):
    rar = " or ".join(i["rarity"]) if len(i["rarity"]) <= 2 else f'{i["rarity"][0]} to {i["rarity"][-1]}'
    att = ""
    if i["att"]:
        att = " (Requires Attunement" + (f" {esc(i['attd'])}" if i["attd"] else "") + ")"
    var = ""
    if 1 < len(i["names"]) <= 12:
        var = ('<p class="small muted"><b>Variants:</b> '
               + ", ".join(f'{esc(n)} <i>({i["rar_of"][n]})</i>' if len(i["rarity"]) > 1 else esc(n) for n in i["names"]) + "</p>")
    elif len(i["names"]) > 12:
        var = f'<p class="small muted"><b>Variants:</b> available in {len(i["names"])} versions (one per eligible weapon or armor type).</p>'
    return (f'<div class="mitem"><h4 class="sp-name">{esc(i["title"])}</h4>'
            f'<div class="sp-meta"><i>{esc(i["cat"])}, {rar}{att}</i></div>{md(i["desc"])}{var}</div>')


def magic_items_html():
    out, letter = ['<div class="cols2 compendium">'], None
    for i in magic_items_grouped():
        L = i["title"][0].upper()
        if L != letter:
            letter = L; out.append(f'<div class="letter">{L}</div>')
        out.append(magic_item_html(i))
    out.append("</div>")
    return "\n".join(out)


def magic_items_by_rarity_html():
    by = defaultdict(list)
    for i in magic_items_grouped():
        for r in i["rarity"]:
            by[r].append(i["title"])
    out = ['<div class="cols3 cr-index">']
    for r in RARITY_ORDER:
        if by.get(r):
            out.append(f"<p><b>{r}</b> <span class=muted>({len(by[r])})</span><br>{', '.join(esc(n) for n in sorted(set(by[r])))}</p>")
    out.append("</div>")
    return "\n".join(out)


# ------------------------------------------------------------------ equipment
def items_2024():
    return [i for i in load("all_items.json") if i["key"].startswith("srd-2024_")]


def money(c):
    try:
        v = float(c)
    except Exception:
        return "—"
    if v == 0: return "—"
    if v >= 1: return f"{v:,.0f} GP" if v == int(v) else f"{v:g} GP"
    if v * 10 >= 1 and abs(v * 10 - round(v * 10)) < 1e-9: return f"{v * 10:g} SP"
    return f"{v * 100:g} CP"


def weight(i):
    try:
        w = float(i["weight"])
    except Exception:
        return "—"
    return "—" if w == 0 else f"{w:g} lb."


def equipment_html(cats, with_desc=True, title=None):
    its = sorted([i for i in items_2024() if i["category"]["name"] in cats], key=lambda i: i["name"])
    rows = "".join(f'<tr><td>{esc(i["name"])}</td><td>{money(i["cost"])}</td><td>{weight(i)}</td></tr>' for i in its)
    out = [f'<table class="compact"><thead><tr><th>Item</th><th>Cost</th><th>Weight</th></tr></thead><tbody>{rows}</tbody></table>']
    if with_desc:
        descs = [i for i in its if i.get("desc")]
        if descs:
            out.append('<div class="cols2 compendium">')
            for i in descs:
                out.append(f'<div class="entry"><p><b>{esc(i["name"])}</b> <span class="muted small">({money(i["cost"])})</span>. {md(i["desc"])[3:] if md(i["desc"]).startswith("<p>") else md(i["desc"])}</div>')
            out.append("</div>")
    return "\n".join(out)


# ------------------------------------------------------------------ feats, species, backgrounds
def feats_html():
    fs = load("all_feats.json")
    order = ["Origin", "General", "Fighting Style", "Epic Boon"]
    out = []
    for t in order:
        group = sorted([f for f in fs if f["type"] == t], key=lambda f: f["name"])
        out.append(f'<h3>{t} Feats</h3><div class="cols2 compendium">')
        for f in group:
            pre = f'<div class="sp-meta"><i>{t} Feat' + (f' (Prerequisite: {esc(f["prerequisite"])})' if f.get("prerequisite") else "") + "</i></div>"
            body = md(f.get("desc", ""))
            for b in f.get("benefits", []):
                body += md(b["desc"])
            out.append(f'<div class="entry"><h4 class="sp-name">{esc(f["name"])}</h4>{pre}{body}</div>')
        out.append("</div>")
    return "\n".join(out)


def species_html():
    out = []
    for s in sorted(load("all_species.json"), key=lambda s: s["name"]):
        out.append(f'<div class="species"><h3>{esc(s["name"])}</h3>{md(s.get("desc", ""))}<div class="cols2 compendium">')
        for t in sorted(s["traits"], key=lambda t: t.get("order") or 0):
            body = md(t["desc"])
            lead = f'<b><i>{esc(t["name"])}.</i></b> '
            body = body.replace("<p>", "<p>" + lead, 1) if body.startswith("<p>") else f"<p>{lead}</p>" + body
            out.append(f'<div class="entry">{body}</div>')
        out.append("</div></div>")
    return "\n".join(out)


def backgrounds_html():
    out = ['<div class="grid2">']
    for b in sorted(load("all_backgrounds.json"), key=lambda b: b["name"]):
        out.append(f'<div class="box"><h4>{esc(b["name"])}</h4>{md(b.get("desc", ""))}')
        for x in b["benefits"]:
            out.append(f'<p><b>{esc(x["name"])}:</b> {md(x["desc"])[3:-4] if md(x["desc"]).startswith("<p>") else md(x["desc"])}</p>')
        out.append("</div>")
    out.append("</div>")
    return "\n".join(out)


# ------------------------------------------------------------------ rules text
RULE_ORDER = ["Rhythm of Play", "The Six Abilities", "D20 Tests", "Proficiency", "Social Interaction",
              "Exploration", "Combat", "Damage and Healing", "Create Your Character", "Multiclassing"]


def rules_html(names=RULE_ORDER):
    rs = {r["name"]: r for r in load("all_rulesets.json")}
    out = []
    for n in names:
        r = rs[n]
        out.append(f'<h2>{esc(n)}</h2>{md(r.get("desc", ""))}')
        for x in sorted(r["rules"], key=lambda x: x.get("index") or 0):
            out.append(f'<h3>{esc(x["name"])}</h3>{md(x["desc"])}')
    return "\n".join(out)


def trinkets_html():
    rs = {r["name"]: r for r in load("all_rulesets.json")}
    h = md(rs["Trinkets"]["desc"])
    return h.replace('<table class="compact">', '<table class="compact trinkets">')


# ------------------------------------------------------------------ class full text
def class_full_text(c):
    d = load(f"{c}.json")
    skip = {"CLASS_TABLE_DATA", "PROFICIENCY_BONUS", "SPELL_SLOTS", "CORE_TRAITS_TABLE"}
    feats = []
    for f in d["features"]:
        if f["feature_type"] in skip or len(f["desc"]) < 40:
            continue
        if f["name"].endswith("Spell List"):
            continue
        lv = min([g["level"] for g in f["gained_at"]] or [99])
        feats.append((lv, f["name"].replace("Studdied", "Studied").replace("Unarmoed", "Unarmored"), f["desc"], f["feature_type"]))
    feats.sort(key=lambda x: (x[0], x[1]))
    out = []
    for lv, n, desc, ft in feats:
        lab = f'<span class="lv">{lv}</span>' if lv < 99 else '<span class="lv">opt</span>'
        out.append(f'<div class="ft"><h4>{lab}{esc(n)}</h4>{md(desc)}</div>')
    return "\n".join(out)


def subclass_full_text(c):
    allc = load("all.json")["results"]
    s = [r for r in allc if r["subclass_of"] and r["subclass_of"]["key"] == f"srd-2024_{c}"]
    if not s:
        return ""
    s = s[0]
    out = [f'<h3>{esc(s["name"])}</h3>{md(s.get("desc", ""))}']
    for f in sorted(s["features"], key=lambda f: min([g["level"] for g in f["gained_at"]] or [0])):
        lv = min([g["level"] for g in f["gained_at"]] or [0])
        out.append(f'<div class="ft"><h4><span class="lv">{lv}</span>{esc(f["name"])}</h4>{md(f["desc"])}</div>')
    return "\n".join(out)


if __name__ == "__main__":
    print(len(spells()), len(creatures()), len(magic_items_grouped()), len(items_2024()))
    print(spell_html([s for s in spells() if s["name"] == "Fireball"][0])[:800])
    print(creature_html([c for c in creatures() if c["name"] == "Goblin Warrior"][0])[:1500])
