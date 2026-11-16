"""Render the world-building table sets (content/tables) into HTML for the Game Master's Compendium.

A table set is a group of random tables on one subject. The book shows the sets
grouped by theme, in the order of THEMES, and each group in the order of the names.
"""
import html

from orig_render import feature_text

E = html.escape

THEMES = ["Settlements", "Factions", "Regions", "Dungeons", "Rumors", "Names", "People", "Lore"]
SET_KEYS = {"name", "theme", "summary", "tables"}
DICE = {"d4": 4, "d6": 6, "d8": 8, "d10": 10, "d12": 12, "d20": 20}


def set_errors(t):
    """Return a list of the problems of one table set. An empty list means no problem."""
    name = t.get("name", "?")
    errors = [f"Table set '{name}': missing key '{k}'" for k in sorted(SET_KEYS - set(t))]
    errors += [f"Table set '{name}': unknown key '{k}'" for k in sorted(set(t) - SET_KEYS)]
    if errors:
        return errors
    if t["theme"] not in THEMES:
        errors.append(f"Table set '{name}': theme '{t['theme']}' is not one of {THEMES}")
    if not t["tables"]:
        errors.append(f"Table set '{name}': needs at least one table")
    titles = []
    for table in t["tables"]:
        if len(table) != 3:
            errors.append(f"Table set '{name}': each table must be (die, title, entries)")
            continue
        die, title, entries = table
        titles.append(title)
        if die not in DICE:
            errors.append(f"Table set '{name}': table '{title}' uses '{die}', use one of {list(DICE)}")
        elif len(entries) != DICE[die]:
            errors.append(f"Table set '{name}': table '{title}' has {len(entries)} entries for a {die}")
        if len(set(entries)) != len(entries):
            errors.append(f"Table set '{name}': table '{title}' has the same entry two times")
    if len(set(titles)) != len(titles):
        errors.append(f"Table set '{name}': two tables have the same title")
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def table_html(die, title, entries):
    """One random table: a caption with the die and the title, then one row for each result."""
    rows = "".join(f'<tr><td class="c">{i}</td><td>{feature_text(e)}</td></tr>' for i, e in enumerate(entries, 1))
    return (f'<table class="compact roll-table"><caption>{die} {E(title)}</caption>'
            f'<thead><tr><th class="c">{die}</th><th>Result</th></tr></thead><tbody>{rows}</tbody></table>')


def set_html(t):
    """One table set: the name, a short summary, and its tables. The theme is the heading of the group."""
    _stop_on(set_errors(t))
    out = [f'<div class="entry table-set"><h4 class="sp-name">{E(t["name"])}</h4>',
           f'<p><i>{feature_text(t["summary"])}</i></p>']
    out += [table_html(*table) for table in t["tables"]]
    out.append("</div>")
    return "\n".join(out)


def sets_html(sets):
    """All table sets, grouped by theme. Return "" if there are none. Stop on a set with a problem."""
    _stop_on([e for t in sets for e in set_errors(t)])
    out = []
    for theme in THEMES:
        group = sorted((t for t in sets if t["theme"] == theme), key=lambda t: t["name"])
        if group:
            out.append(f'<h2>{theme}</h2><div class="cols2 compendium">')
            out += [set_html(t) for t in group]
            out.append("</div>")
    return "\n".join(out)


def all_tables_html():
    from content.tables import TABLE_SETS
    return sets_html(TABLE_SETS)
