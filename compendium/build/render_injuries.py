"""Render the Injuries and scars optional system (content/injuries) for the Game Master's Compendium."""
import html

from orig_render import feature_text

E = html.escape

INJURY_KEYS = {"name", "roll", "severity", "effect", "treatment", "scar"}
# Each severity and the d20 results that give it, in the order of the book.
SEVERITY = {"Minor": range(1, 11), "Serious": range(11, 18), "Lasting": range(18, 21)}


def injury_errors(i):
    """Return a list of the problems of one injury entry. An empty list means no problem."""
    name = i.get("name", "?")
    errors = [f"Injury '{name}': missing key '{k}'" for k in sorted(INJURY_KEYS - set(i))]
    errors += [f"Injury '{name}': unknown key '{k}'" for k in sorted(set(i) - INJURY_KEYS)]
    if errors:
        return errors
    if i["severity"] not in SEVERITY:
        errors.append(f"Injury '{name}': severity '{i['severity']}' is not one of {list(SEVERITY)}")
    elif i["roll"] not in SEVERITY[i["severity"]]:
        r = SEVERITY[i["severity"]]
        errors.append(f"Injury '{name}': a {i['severity']} injury needs a roll from {r.start} to {r.stop - 1}")
    if len(i["scar"]) != 2:
        errors.append(f"Injury '{name}': scar must be (name, benefit)")
    return errors


def table_errors(injuries):
    """Return the problems of the whole table: the problems of each entry, and a d20 result used two times."""
    errors = [e for i in injuries for e in injury_errors(i)]
    seen = {}
    for i in injuries:
        r = i.get("roll")
        if r in seen:
            errors.append(f"Injury '{i.get('name')}': roll {r} is also used by '{seen[r]}'")
        seen[r] = i.get("name")
    if not errors and injuries and min(i["roll"] for i in injuries) != 1:
        errors.append("Injury table: the lowest roll must be 1, so that each d20 result has an injury")
    if not errors:
        for text, i in roll_ranges(injuries):
            top = int(text.split("–")[-1])
            if top not in SEVERITY[i["severity"]]:
                errors.append(f"Injury '{i['name']}': its range {text} goes past the {i['severity']} results; "
                              "add an entry at the first result of the next severity")
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def roll_ranges(injuries):
    """Give each injury the range of d20 results that point to it.

    An entry covers its own roll and the results above it, up to the next entry's roll.
    Return a list of (text of the range, injury), in the order of the rolls.
    """
    rows = sorted(injuries, key=lambda i: i["roll"])
    out = []
    for n, i in enumerate(rows):
        top = rows[n + 1]["roll"] - 1 if n + 1 < len(rows) else 20
        text = str(i["roll"]) if top == i["roll"] else f'{i["roll"]}–{top}'
        out.append((text, i))
    return out


def injury_table_html(injuries):
    """The d20 Injury table: the result, the injury, and its severity."""
    rows = "".join(f'<tr><td class="c">{r}</td><td>{E(i["name"])}</td><td>{i["severity"]}</td></tr>'
                   for r, i in roll_ranges(injuries))
    return ('<table class="compact"><caption>Injury Table</caption><thead><tr><th class="c">d20</th>'
            f'<th>Injury</th><th>Severity</th></tr></thead><tbody>{rows}</tbody></table>')


def injury_html(i):
    """One injury: the name, the severity and the d20 result, then the effect, the treatment, and the scar."""
    scar, benefit = i["scar"]
    return (f'<div class="entry sys-injury"><h4 class="sp-name">{E(i["name"])}</h4>'
            f'<div class="sp-meta"><i>{i["severity"]} injury · d20 result {i["roll"]}</i></div><dl class="feat">'
            f'<dt>Effect</dt><dd>{feature_text(i["effect"])}</dd>'
            f'<dt>Treatment</dt><dd>{feature_text(i["treatment"])}</dd>'
            f'<dt>Scar: {E(scar)}</dt><dd>{feature_text(benefit)}</dd></dl></div>')


def injuries_html(injuries):
    """The Injury table, then each injury grouped by severity. Return "" if there are none."""
    _stop_on(table_errors(injuries))
    if not injuries:
        return ""
    out = [injury_table_html(injuries)]
    for sev in SEVERITY:
        group = sorted((i for i in injuries if i["severity"] == sev), key=lambda i: i["roll"])
        if group:
            out.append(f'<h2>{sev} Injuries</h2><div class="cols2 compendium">')
            out += [injury_html(i) for i in group]
            out.append("</div>")
    return "\n".join(out)


def all_injuries_html():
    from content.injuries import INJURIES
    return injuries_html(INJURIES)
