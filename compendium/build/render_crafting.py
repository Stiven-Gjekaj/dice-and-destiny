"""Render the Crafting and gathering optional system (content/crafting) for the Game Master's Compendium.

A recipe must not make a magic item much cheaper or faster than the crafting
rules of the 2024 core rules. BASE holds those costs and times. A recipe's
total cost (its gold and the value of its materials) and its days must be
at least MARGIN of the base. A party that harvests its own materials saves
their value, which is the small advantage that the system gives.
"""
import html
import json
import os

from orig_render import feature_text

E = html.escape

RARITIES = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
# The cost in GP and the workdays to craft a magic item of each rarity. A consumable takes half of both.
BASE = {"Common": (50, 5), "Uncommon": (200, 10), "Rare": (2000, 50), "Very Rare": (20000, 125), "Legendary": (100000, 250)}
MARGIN = 0.8
# The value of a material and the DC to harvest or gather it, by rarity. The DC also applies to a recipe.
MATERIAL_VALUE = {"Common": 10, "Uncommon": 50, "Rare": 500, "Very Rare": 5000, "Legendary": 25000}
DC = {"Common": 10, "Uncommon": 13, "Rare": 15, "Very Rare": 18, "Legendary": 20}
SOURCES = {"Monster": "Monster Materials", "Biome": "Biome Materials"}
MATERIAL_KEYS = {"name", "source", "origin", "rarity", "check", "text"}
RECIPE_KEYS = {"item", "rarity", "consumable", "tool", "materials", "gold", "days", "note"}


def base_cost(rarity, consumable):
    """The base (gold, days) of an item of this rarity. A consumable takes half of both."""
    gold, days = BASE[rarity]
    return (gold / 2, days / 2) if consumable else (gold, days)


def material_errors(m):
    """Return a list of the problems of one material entry. An empty list means no problem."""
    name = m.get("name", "?")
    errors = [f"Material '{name}': missing key '{k}'" for k in sorted(MATERIAL_KEYS - set(m))]
    errors += [f"Material '{name}': unknown key '{k}'" for k in sorted(set(m) - MATERIAL_KEYS)]
    if errors:
        return errors
    if m["source"] not in SOURCES:
        errors.append(f"Material '{name}': source '{m['source']}' is not one of {list(SOURCES)}")
    if m["rarity"] not in RARITIES:
        errors.append(f"Material '{name}': rarity '{m['rarity']}' is not one of {RARITIES}")
    return errors


def recipe_total(r, materials):
    """The total cost of a recipe in GP: its gold and the value of each material in its list."""
    return r["gold"] + sum(MATERIAL_VALUE[materials[n]["rarity"]] for n in r["materials"])


def recipe_errors(r, materials, items):
    """Return a list of the problems of one recipe.

    materials: {name: material entry}. items: {item name: rarity} of the items that a recipe can make.
    """
    name = r.get("item", "?")
    errors = [f"Recipe '{name}': missing key '{k}'" for k in sorted(RECIPE_KEYS - set(r))]
    errors += [f"Recipe '{name}': unknown key '{k}'" for k in sorted(set(r) - RECIPE_KEYS)]
    if errors:
        return errors
    if r["rarity"] not in RARITIES:
        return [f"Recipe '{name}': rarity '{r['rarity']}' is not one of {RARITIES}"]
    if name not in items:
        errors.append(f"Recipe '{name}': the item is not an SRD magic item or an original magic item of this book")
    elif items[name] != r["rarity"]:
        errors.append(f"Recipe '{name}': the item is {items[name]}, not {r['rarity']}")
    missing = [n for n in r["materials"] if n not in materials]
    errors += [f"Recipe '{name}': unknown material '{n}'" for n in missing]
    if not r["materials"]:
        errors.append(f"Recipe '{name}': needs at least one material")
    if errors:
        return errors
    ranks = [RARITIES.index(materials[n]["rarity"]) for n in r["materials"]]
    if max(ranks) != RARITIES.index(r["rarity"]):
        errors.append(f"Recipe '{name}': needs at least one material of its own rarity, and none above it")
    gold, days = base_cost(r["rarity"], r["consumable"])
    total = recipe_total(r, materials)
    if total < MARGIN * gold:
        errors.append(f"Recipe '{name}': costs {total} GP in all; the floor is {MARGIN * gold:g} GP ({MARGIN:.0%} of {gold:g})")
    if r["days"] < MARGIN * days:
        errors.append(f"Recipe '{name}': takes {r['days']} days; the floor is {MARGIN * days:g} ({MARGIN:.0%} of {days:g})")
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def all_errors(materials, recipes, items):
    """The problems of all entries, and a material name used two times."""
    errors = [e for m in materials for e in material_errors(m)]
    names = [m.get("name") for m in materials]
    errors += [f"Material '{n}': the name is used two times" for n in sorted({n for n in names if names.count(n) > 1})]
    if errors:
        return errors
    by_name = {m["name"]: m for m in materials}
    return [e for r in recipes for e in recipe_errors(r, by_name, items)]


def base_table_html():
    """The table of the base cost and time of each rarity, from BASE."""
    rows = "".join(f'<tr><td>{r}</td><td class="c">{g:,} GP</td><td class="c">{d}</td>'
                   f'<td class="c">{base_cost(r, True)[0]:,g} GP</td><td class="c">{base_cost(r, True)[1]:g}</td></tr>'
                   for r, (g, d) in BASE.items())
    return ('<table class="compact"><caption>Crafting Cost and Time by Rarity</caption><thead><tr><th>Rarity</th>'
            '<th class="c">Cost</th><th class="c">Workdays</th><th class="c">Consumable cost</th>'
            f'<th class="c">Consumable workdays</th></tr></thead><tbody>{rows}</tbody></table>')


def harvest_table_html():
    """The table of the value and the DC of a material of each rarity."""
    rows = "".join(f'<tr><td>{r}</td><td class="c">{MATERIAL_VALUE[r]:,} GP</td><td class="c">{DC[r]}</td></tr>' for r in RARITIES)
    return ('<table class="compact"><caption>Materials by Rarity</caption><thead><tr><th>Rarity</th>'
            f'<th class="c">Value</th><th class="c">DC</th></tr></thead><tbody>{rows}</tbody></table>')


def material_html(m):
    meta = (f'{m["rarity"]} {m["source"].lower()} material · {E(m["origin"])} · '
            f'{E(m["check"])} DC {DC[m["rarity"]]} · {MATERIAL_VALUE[m["rarity"]]:,} GP')
    return (f'<div class="entry sys-material"><h4 class="sp-name">{E(m["name"])}</h4>'
            f'<div class="sp-meta"><i>{meta}</i></div><p>{feature_text(m["text"])}</p></div>')


def materials_html(materials):
    """The materials, grouped by source, each group in the order of the names. Return "" if there are none."""
    _stop_on([e for m in materials for e in material_errors(m)])
    out = []
    for src, title in SOURCES.items():
        group = sorted((m for m in materials if m["source"] == src), key=lambda m: m["name"])
        if group:
            out.append(f'<h2>{title}</h2><div class="cols2 compendium">')
            out += [material_html(m) for m in group]
            out.append("</div>")
    return "\n".join(out)


def recipe_html(r, materials):
    kind = "consumable" if r["consumable"] else "permanent"
    meta = f'{r["rarity"]} · {kind} · {E(r["tool"])}, DC {DC[r["rarity"]]}'
    mats = ", ".join(f'{E(n)} ({MATERIAL_VALUE[materials[n]["rarity"]]:,} GP)' for n in r["materials"])
    total = recipe_total(r, materials)
    out = [f'<div class="entry sys-recipe"><h4 class="sp-name">{E(r["item"])}</h4>',
           f'<div class="sp-meta"><i>{meta}</i></div><dl class="feat">',
           f'<dt>Materials</dt><dd>{mats}</dd>',
           f'<dt>Cost and time</dt><dd>{r["gold"]:,} GP and the materials ({total:,} GP in all), {r["days"]} workdays</dd>']
    if r["note"]:
        out.append(f'<dt>Note</dt><dd>{feature_text(r["note"])}</dd>')
    out.append("</dl></div>")
    return "".join(out)


def recipes_html(materials, recipes, items):
    """The recipes, grouped by rarity, each group in the order of the items. Return "" if there are none."""
    _stop_on(all_errors(materials, recipes, items))
    by_name = {m["name"]: m for m in materials}
    out = []
    for rar in RARITIES:
        group = sorted((r for r in recipes if r["rarity"] == rar), key=lambda r: r["item"])
        if group:
            out.append(f'<h2>{rar} Recipes</h2><div class="cols2 compendium">')
            out += [recipe_html(r, by_name) for r in group]
            out.append("</div>")
    return "\n".join(out)


def known_items():
    """{item name: rarity} of the SRD magic items and the original magic items.

    An SRD item with variants, such as "Armor of Resistance (Plate)", also gives its base name.
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "all_magicitems.json")
    items = {}
    for x in json.load(open(path, encoding="utf-8")):
        rar = x["rarity"] if isinstance(x["rarity"], str) else x["rarity"]["name"]
        items[x["name"]] = rar
        if x["name"].endswith(")") and " (" in x["name"]:
            items.setdefault(x["name"].rsplit(" (", 1)[0], rar)
    from content.items import ITEMS
    for e in ITEMS:
        items.setdefault(e[0], e[2])
    return items


def all_base_html():
    return base_table_html() + harvest_table_html()


def all_materials_html():
    from content.crafting import MATERIALS
    return materials_html(MATERIALS)


def all_recipes_html():
    from content.crafting import MATERIALS, RECIPES
    return recipes_html(MATERIALS, RECIPES, known_items())
