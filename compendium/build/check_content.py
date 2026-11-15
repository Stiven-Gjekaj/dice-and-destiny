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
}

# Spell damage curve: level to (single target, area). A spell may go 25% above it.
SPELL_CAP = {
    0: ("1d10", "1d6"), 1: ("2d10", "2d6"), 2: ("3d10", "4d6"), 3: ("5d10", "6d6"),
    4: ("6d10", "7d6"), 5: ("8d10", "8d6"), 6: ("10d10", "11d6"), 7: ("11d10", "12d6"),
    8: ("12d10", "13d6"), 9: ("15d10", "14d6"),
}
SPELL_MARGIN = 1.25

# Monster limits. Low AC does not make a monster too strong, so only a floor applies.
AC_ABOVE_TARGET = 4
AC_FLOOR = 5
# The current monsters use HP multipliers from 1.0 to 1.1. The range adds a margin of 0.1.
HP_MULT = (0.9, 1.2)

# These spells go above the curve. They were in the books before this check.
# The human decides if they change. Until then, the check skips them.
SPELL_EXCEPTIONS = {"Storm Lance", "Sunder the Veil", "Tidal Collapse", "Unmaking"}

PAGE_LIMIT = 700

EM_DASH = chr(0x2014)
TRADEMARKS = ("D&D", "D&amp;D", "Dungeons & Dragons", "Dungeons &amp; Dragons")
AREA_WORDS = re.compile(r"\b(Cone|Sphere|Cube|Line|Cylinder|Emanation|each creature)\b", re.I)
DAMAGE = re.compile(r"(\d+d\d+(?:\s*\+\s*\d+)?)\s+(?:\w+\s+)?damage", re.I)


def duplicates(category, names):
    seen, errors = {}, []
    for n in names:
        key = n.strip().lower()
        if key in seen:
            errors.append(f"{category}: duplicate name '{n}'")
        seen[key] = n
    return errors


def forbidden(category, names, banned):
    errors = []
    for n in names:
        for b in banned:
            if re.search(rf"(?<![\w-]){re.escape(b)}(?![\w-])", n, re.I):
                errors.append(f"{category}: '{n}' uses the name '{b}', which is not permitted")
    return errors


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


def spell_damage_too_high(name, level, text, area):
    cap = avg(SPELL_CAP[level][1 if area else 0]) * SPELL_MARGIN
    found = [avg(d.replace(" ", "")) for d in DAMAGE.findall(text)]
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


def check_all_content():
    import content.backgrounds
    import content.downtime
    import content.feats
    import content.items
    import content.monsters
    import content.species
    import content.spells
    import content.subclasses

    names = {
        "subclasses": [s[0] for subs in content.subclasses.SUBS.values() for s in subs],
        "species": [e[0] for e in content.species.SPECIES],
        "backgrounds": [e[0] for e in content.backgrounds.BACKGROUNDS],
        "feats": [e[0] for e in content.feats.FEATS],
        "spells": [e[0] for e in content.spells.SPELLS],
        "monsters": [m.name for m in content.monsters.MON],
        "items": [e[0] for e in content.items.ITEMS],
    }
    errors = []
    for category, ns in names.items():
        errors += duplicates(category, ns)
        errors += forbidden(category, ns, BANNED)
    entries = {
        "subclasses": content.subclasses.SUBS, "species": content.species.SPECIES,
        "backgrounds": content.backgrounds.BACKGROUNDS, "feats": content.feats.FEATS,
        "spells": content.spells.SPELLS, "monsters": content.monsters.MON,
        "items": content.items.ITEMS, "downtime": content.downtime.STRONGHOLDS,
    }
    for category, data in entries.items():
        for s in _strings(data):
            errors += bad_text(category, s)
    for m in content.monsters.MON:
        errors += monster_out_of_band(m)
    for s in content.spells.SPELLS:
        name, level, desc = s[0], s[1], s[10]
        if name in SPELL_EXCEPTIONS:
            continue
        errors += spell_damage_too_high(name, level, desc, bool(AREA_WORDS.search(desc)))
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
