"""Check the original content before a build, and the page count after it.

Usage:
  python3 check_content.py content          check all content packages
  python3 check_content.py pages FILE...    check the page count of each PDF

Each check returns a list of error strings. An empty list means that the
check found no problem. The command prints each error and exits with 1 if
there is an error.
"""
import re
import sys

from pypdf import PdfReader

from monster_engine import TARGET, M, avg

# Names that a publisher owns and that are not in the SRD 5.2.
BANNED = {
    "beholder", "mind flayer", "illithid", "githyanki", "githzerai", "yuan-ti",
    "displacer beast", "carrion crawler", "umber hulk", "kuo-toa", "slaad",
    "forgotten realms", "faerun", "faer" + chr(0xFB) + "n", "eberron", "ravenloft", "greyhawk",
    "waterdeep", "baldur's gate", "strahd", "vecna", "mordenkainen", "bigby",
    "tasha", "melf", "tenser", "otiluke", "drizzt",
    "elder brain", "star spawn", "hook horror", "hookhorror",
}

# Spell damage curve: level to (single target, area), in average damage.
# Each value is the highest damage of an SRD 5.2 spell of that level and kind,
# or a higher value from a level below (a higher level never has a lower cap).
# Level 9 single target is 99, near Power Word Kill (100 Hit Points).
# A spell may go 25% above the curve. A test checks that every SRD spell passes.
SPELL_CAP = {
    0: (6, 4), 1: (14, 10), 2: (16, 14), 3: (27, 28), 4: (36, 37),
    5: (49, 37), 6: (75, 75), 7: (75, 75), 8: (75, 75), 9: (99, 140),
}
SPELL_MARGIN = 1.25

# Monster limits. Low AC does not make a monster too strong, so only a floor applies.
AC_ABOVE_TARGET = 4
AC_FLOOR = 5
# The current monsters use HP multipliers from 1.0 to 1.1. The range adds a margin of 0.1.
HP_MULT = (0.9, 1.2)

PAGE_LIMIT = 700

EM_DASH = chr(0x2014)
TRADEMARKS = ("D&D", "D&amp;D", "Dungeons & Dragons", "Dungeons &amp; Dragons")
AREA_WORDS = re.compile(r"\b(Cone|Sphere|Cube|Line|Cylinder|Emanation|each creature|each target|wall|radius|up to \w+ (?:creatures|targets))\b", re.I)
# Up to three words between the dice and "damage", for example "Fire or Cold damage".
DAMAGE = re.compile(r"(\d+d\d+(?:\s*[+-]\s*\d+)?)\s+(?:[\w,]+\s+){0,3}?damage", re.I)
SENTENCE = re.compile(r"(?<=[.!?])\s+")
FEAT_TYPES = {"Origin", "General", "Fighting Style", "Epic Boon"}
RARITIES = {"Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact"}
SRD_CLASSES = {"barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger",
               "rogue", "sorcerer", "warlock", "wizard"}


def duplicates(category, names):
    seen, errors = {}, []
    for n in names:
        key = n.strip().lower()
        if key in seen:
            errors.append(f"{category}: duplicate name '{n}'")
        seen[key] = n
    return errors


def _banned_pattern(b):
    # Also match the plural forms, for example "beholders" and "slaadi".
    return re.compile(rf"(?<![\w-]){re.escape(b)}(?:s|es|i)?(?![\w-])", re.I)


def _straight(text):
    return text.replace(chr(0x2019), "'").replace(chr(0x2018), "'")


def forbidden(category, names, banned):
    errors = []
    for n in names:
        for b in banned:
            if _banned_pattern(b).search(_straight(n)):
                errors.append(f"{category}: '{n}' uses the name '{b}', which is not permitted")
    return errors


def unknown_values(category, values, allowed):
    """A value that the book does not know makes the book drop the entry."""
    return [f"{category}: '{v}' is not one of {sorted(allowed)}" for v in values if v not in allowed]


def bad_source(root, banned):
    """Check the text of every Python file under root, also in folders that no check knows."""
    import os
    errors = []
    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in sorted(files):
            if f.endswith(".py"):
                path = os.path.join(folder, f)
                text = _straight(open(path, encoding="utf-8").read())
                errors += bad_text(path, text)
                errors += [f"{path}: uses the name '{b}', which is not permitted"
                           for b in sorted(banned) if _banned_pattern(b).search(text)]
    return errors


def unregistered_packages(content_dir, registered):
    import os
    found = sorted(d for d in os.listdir(content_dir)
                   if os.path.isfile(os.path.join(content_dir, d, "__init__.py")))
    return [f"content: the package '{d}' is not registered in check_content.REGISTRY"
            for d in found if d not in registered]


def bad_text(where, text):
    errors = []
    if EM_DASH in text:
        errors.append(f"{where}: has an em-dash")
    for t in TRADEMARKS:
        if t in text:
            errors.append(f"{where}: has the trademark '{t}'")
    return errors


def monster_out_of_band(m):
    errors = []
    target_ac = TARGET[m.cr][0]
    if m.ac and m.ac > target_ac + AC_ABOVE_TARGET:
        errors.append(f"monsters: {m.name} has AC {m.ac}, above {target_ac + AC_ABOVE_TARGET} for CR {m.cr}")
    if m.ac and m.ac < AC_FLOOR:
        errors.append(f"monsters: {m.name} has AC {m.ac}, below {AC_FLOOR}")
    if not HP_MULT[0] <= m.hp <= HP_MULT[1]:
        errors.append(f"monsters: {m.name} has an HP multiplier of {m.hp}, outside {HP_MULT}")
    return errors


def is_area(text):
    return bool(AREA_WORDS.search(text))


def spell_damage_too_high(name, level, text, area):
    cap = SPELL_CAP[level][1 if area else 0] * SPELL_MARGIN
    # Damage in one sentence is added up ("2d10 Fire damage and 2d10 Cold damage").
    found = [sum(avg(d.replace(" ", "")) for d in DAMAGE.findall(s)) for s in SENTENCE.split(text)]
    if found and max(found) > cap:
        return [f"spells: {name} (level {level}) deals {max(found)} average damage, above {cap:g}"]
    return []


def too_many_pages(pdf, limit=PAGE_LIMIT):
    n = len(PdfReader(pdf).pages)
    return [f"pages: {pdf} has {n} pages, above {limit}"] if n > limit else []


def _strings(obj):
    """Yield every string inside an entry."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, M):
        yield from _strings(list(obj.__dict__.values()))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from _strings(k)
            yield from _strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _strings(v)


# Each content package and how to read the names of its entries.
# A session that adds a package adds one line here. The check stops on a
# package that is not in this list.
REGISTRY = {
    "subclasses": lambda m: [s[0] for subs in m.SUBS.values() for s in subs],
    "species": lambda m: [e[0] for e in m.SPECIES],
    "backgrounds": lambda m: [e[0] for e in m.BACKGROUNDS],
    "feats": lambda m: [e[0] for e in m.FEATS],
    "spells": lambda m: [e[0] for e in m.SPELLS],
    "monsters": lambda m: [e.name for e in m.MON],
    "items": lambda m: [e[0] for e in m.ITEMS],
    "downtime": lambda m: [e["name"] for e in m.DOWNTIME],
    "classes": lambda m: [e["name"] for e in m.CLASSES],
    "injuries": lambda m: [e["name"] for e in m.INJURIES],
    "crafting": lambda m: [e["name"] for e in m.MATERIALS] + [e["item"] for e in m.RECIPES],
    "systems": lambda m: [e["name"] for e in m.MARKS + m.BONDS + m.TECHNIQUES + m.LEGENDS + m.BIOMES + m.FACTIONS],
    "traps": lambda m: [e["name"] for e in m.TRAPS],
    "tables": lambda m: [e["name"] for e in m.TABLE_SETS],
    "pantheons": lambda m: [p["name"] for p in m.PANTHEONS] + [g["name"] for p in m.PANTHEONS for g in p["gods"]],
    "npcs": lambda m: [e[1].name for e in m.NPCS],
    "dawnwatch": lambda m: [e.name for e in m.MON] + [person_name(e) for e in m.NPCS] + [e[0] for e in m.ITEMS],
    "western_sea": lambda m: [e.name for e in m.MON] + [person_name(e) for e in m.NPCS] + [e[0] for e in m.ITEMS],
}

# Beyond the Western Sea can use 3d6 in place of a d20. 3d6 makes a high number much harder to roll.
# Thus the creatures of that book keep these limits (spec, "What 3d6 changes").
WESTERN_SEA_AC = 16
WESTERN_SEA_DC = 15
DC_VALUE = re.compile(r"\bDC (\d+)")


def person_name(entry):
    """A Dawnwatch person is (role, M(...)) or (role, "Name") for a person with no statblock."""
    return entry[1] if isinstance(entry[1], str) else entry[1].name


def campaign_clashes(campaign, compendium, label="dawnwatch", other="Compendium"):
    """A campaign name that is also a Compendium name makes a statblock directive point at two entries."""
    known = {n.strip().lower() for n in compendium}
    return [f"{label}: '{n}' is also the name of a {other} entry" for n in campaign if n.strip().lower() in known]


def limit_errors(mons):
    """Give one message for each creature with an armor class or a save DC above the limits of Beyond the Western Sea."""
    errors = []
    for m in mons:
        ac = m.stats()[0]
        if ac > WESTERN_SEA_AC:
            errors.append(f"western_sea: {m.name} has AC {ac}, above {WESTERN_SEA_AC}")
        dcs = [int(d) for text in _strings(m) for d in DC_VALUE.findall(m.fmt(text))]
        if dcs and max(dcs) > WESTERN_SEA_DC:
            errors.append(f"western_sea: {m.name} has a save DC of {max(dcs)}, above {WESTERN_SEA_DC}")
    return errors


def background_feat_errors(backgrounds, origin_feats):
    """Each background names an Origin feat. A note in parentheses, such as "(Cleric)", is not part of the name."""
    errors = []
    for b in backgrounds:
        feat = re.sub(r"\s*\(.*\)$", "", b[4])
        if feat not in origin_feats:
            errors.append(f"backgrounds: {b[0]} names the feat {b[4]!r}, which is not an Origin feat")
    return errors


def srd_origin_feats():
    import json
    import os

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "all_feats.json")
    with open(path) as f:
        return {e["name"] for e in json.load(f) if e.get("type") == "Origin"}


# Half casters learn spells up to level 5 only.
HALF_CASTER_MAX = {"Paladin": 5, "Ranger": 5}


def spell_class_level_errors(spells):
    """A spell above level 5 can't be on the Paladin or the Ranger list."""
    errors = []
    for sp in spells:
        for cls, top in HALF_CASTER_MAX.items():
            if cls in sp[3] and sp[1] > top:
                errors.append(f"spells: {sp[0]} (level {sp[1]}) is on the {cls} list, which stops at level {top}")
    return errors


def check_all_content():
    import importlib
    import os

    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content")
    errors = unregistered_packages(root, set(REGISTRY))
    errors += bad_source(root, BANNED)
    mods = {c: importlib.import_module(f"content.{c}") for c in REGISTRY}
    for category, names in REGISTRY.items():
        ns = names(mods[category])
        errors += duplicates(category, ns)
        errors += forbidden(category, ns, BANNED)

    # The source check above does not see escapes such as "\\u2014". Check the loaded values too.
    for category, mod in mods.items():
        for value in [v for k, v in vars(mod).items() if k.isupper()]:
            for text in _strings(value):
                errors += bad_text(category, text)

    new_classes = set(getattr(mods.get("classes"), "CLASS_KEYS", []))
    errors += unknown_values("subclasses", list(mods["subclasses"].SUBS), SRD_CLASSES | new_classes)
    errors += unknown_values("feats", [e[1] for e in mods["feats"].FEATS], FEAT_TYPES)
    errors += unknown_values("items", [e[2] for e in mods["items"].ITEMS], RARITIES)
    origin = srd_origin_feats() | {e[0] for e in mods["feats"].FEATS if e[1] == "Origin"}
    errors += background_feat_errors(mods["backgrounds"].BACKGROUNDS, origin)
    for m in mods["monsters"].MON:
        errors += monster_out_of_band(m)
    for _, m in mods["npcs"].NPCS:
        errors += monster_out_of_band(m)
    dw = mods["dawnwatch"]
    errors += unknown_values("dawnwatch", [e[2] for e in dw.ITEMS], RARITIES)
    for m in list(dw.MON) + [e[1] for e in dw.NPCS if not isinstance(e[1], str)]:
        errors += monster_out_of_band(m)
    errors += campaign_clashes(REGISTRY["dawnwatch"](dw), [m.name for m in mods["monsters"].MON]
                               + [e[1].name for e in mods["npcs"].NPCS] + [e[0] for e in mods["items"].ITEMS])
    ws = mods["western_sea"]
    errors += unknown_values("western_sea", [e[2] for e in ws.ITEMS], RARITIES)
    ws_mons = list(ws.MON) + [e[1] for e in ws.NPCS if not isinstance(e[1], str)]
    for m in ws_mons:
        errors += monster_out_of_band(m)
    errors += limit_errors(ws_mons)
    ws_names = REGISTRY["western_sea"](ws)
    errors += campaign_clashes(ws_names, [m.name for m in mods["monsters"].MON]
                               + [e[1].name for e in mods["npcs"].NPCS] + [e[0] for e in mods["items"].ITEMS],
                               label="western_sea")
    errors += campaign_clashes(ws_names, REGISTRY["dawnwatch"](dw), label="western_sea", other="Dawnwatch")
    errors += spell_class_level_errors(mods["spells"].SPELLS)
    for sp in mods["spells"].SPELLS:
        name, level, desc = sp[0], sp[1], sp[10]
        errors += spell_damage_too_high(name, level, desc, is_area(desc))
    return errors


def main(argv):
    if argv[:1] == ["content"]:
        errors = check_all_content()
    elif argv[:1] == ["pages"] and argv[1:]:
        errors = [e for pdf in argv[1:] for e in too_many_pages(pdf)]
    else:
        print(__doc__)
        return 2
    for e in errors:
        print("CHECK ERROR:", e)
    if not errors:
        print("checks OK:", " ".join(argv))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
