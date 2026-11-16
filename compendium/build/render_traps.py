"""Render the original traps and hazards (content/traps) into HTML for the GM's book.

Each entry is a dict with the keys in KEYS. The "bands" key holds one row for
each level band in which the entry is used: (first level of the band, DC, damage).
The damage of a band must not be above the improvised damage of the entry's
severity for that band (the Improvised Damage table in "Exploration, Travel & the World" in the GM's book).
"""
import html
import re

from monster_engine import avg
from orig_render import feature_text

E = html.escape

KEYS = {"name", "kind", "where", "severity", "summary", "trigger", "effect", "find", "stop", "bands"}
KINDS = {"Trap": "Traps", "Hazard": "Hazards"}
SEVERITIES = ("Setback", "Dangerous", "Deadly")
# First level of a band: (label, improvised damage for Setback, Dangerous, Deadly).
BANDS = {
    1: ("1–4", ("1d10", "2d10", "4d10")),
    5: ("5–10", ("2d10", "4d10", "10d10")),
    11: ("11–16", ("4d10", "10d10", "18d10")),
    17: ("17–20", ("10d10", "18d10", "24d10")),
}
DC_RANGE = (10, 20)
DICE = re.compile(r"^\d+d\d+(\s*\+\s*\d+)?$")


def band_label(first):
    return BANDS[first][0]


def damage_cap(first, severity):
    """The highest average damage for a band and a severity."""
    return avg(BANDS[first][1][SEVERITIES.index(severity)])


def trap_errors(t):
    """Return a list of the problems of one entry. An empty list means no problem."""
    name = t.get("name", "?")
    errors = [f"Trap '{name}': missing key '{k}'" for k in sorted(KEYS - set(t))]
    errors += [f"Trap '{name}': unknown key '{k}'" for k in sorted(set(t) - KEYS)]
    if errors:
        return errors
    if t["kind"] not in KINDS:
        errors.append(f"Trap '{name}': kind '{t['kind']}' is not one of {list(KINDS)}")
    if t["severity"] not in SEVERITIES:
        errors.append(f"Trap '{name}': severity '{t['severity']}' is not one of {list(SEVERITIES)}")
    rows = t["bands"]
    if not rows:
        return errors + [f"Trap '{name}': needs at least one band"]
    firsts = [r[0] for r in rows]
    if any(f not in BANDS for f in firsts):
        return errors + [f"Trap '{name}': a band must start at one of {list(BANDS)}"]
    if firsts != sorted(set(firsts)):
        errors.append(f"Trap '{name}': the bands must be in order, each band one time")
    dcs = [r[1] for r in rows]
    if any(not DC_RANGE[0] <= dc <= DC_RANGE[1] for dc in dcs):
        errors.append(f"Trap '{name}': a DC must be from {DC_RANGE[0]} to {DC_RANGE[1]}")
    if dcs != sorted(dcs):
        errors.append(f"Trap '{name}': the DC must not go down in a higher band")
    for first, _, dmg in rows:
        if not dmg:
            continue
        if not DICE.match(dmg):
            errors.append(f"Trap '{name}': damage '{dmg}' is not a dice expression such as '2d10'")
        elif t["severity"] in SEVERITIES and avg(dmg) > damage_cap(first, t["severity"]):
            errors.append(f"Trap '{name}': damage {dmg} for levels {band_label(first)} is above "
                          f"{damage_cap(first, t['severity'])}, the {t['severity']} limit")
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def bands_html(t):
    """A small table with the DC and the damage for each level band."""
    has_damage = any(r[2] for r in t["bands"])
    head = "<th>Levels</th><th class=\"c\">DC</th>" + ('<th class="c">Damage</th>' if has_damage else "")
    rows = []
    for first, dc, dmg in t["bands"]:
        cells = f'<td>{band_label(first)}</td><td class="c">{dc}</td>'
        if has_damage:
            cells += f'<td class="c">{E(dmg) if dmg else "None"}</td>'
        rows.append(f"<tr>{cells}</tr>")
    return f'<table class="compact trap-bands"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>'


def trap_html(t):
    """One trap or hazard."""
    _stop_on(trap_errors(t))
    meta = f'{t["kind"]} · {E(t["where"])} · {t["severity"]}'
    rows = [("Trigger", t["trigger"]), ("Effect", t["effect"]), ("Find it", t["find"]), ("Stop it", t["stop"])]
    return "\n".join([
        f'<div class="entry trap"><h4 class="sp-name">{E(t["name"])}</h4><div class="sp-meta"><i>{meta}</i></div>',
        f'<p><i>{feature_text(t["summary"])}</i></p>',
        bands_html(t),
        '<dl class="feat">' + "".join(f"<dt>{k}</dt><dd>{feature_text(v)}</dd>" for k, v in rows) + "</dl>",
        "</div>",
    ])


def traps_html(traps):
    """All entries, grouped by kind, each group in the order of the names. Return "" if there are none."""
    _stop_on([e for t in traps for e in trap_errors(t)])
    out = []
    for kind, plural in KINDS.items():
        group = sorted((t for t in traps if t["kind"] == kind), key=lambda t: t["name"])
        if group:
            out.append(f'<h2>{plural}</h2><div class="cols2 compendium">')
            out += [trap_html(t) for t in group]
            out.append("</div>")
    return "\n".join(out)


def traps_index_html(traps):
    """The names of the entries for each level band. An entry shows in each band that it has."""
    if not traps:
        return ""
    out = ['<div class="cols2 cr-index">']
    for first, (label, _) in BANDS.items():
        names = sorted(t["name"] for t in traps if first in [r[0] for r in t["bands"]])
        out.append(f"<p><b>Levels {label}</b> <span class=muted>({len(names)})</span><br>"
                   f"{', '.join(E(n) for n in names) or 'None yet.'}</p>")
    out.append("</div>")
    return "\n".join(out)


def all_traps_html():
    from content.traps import TRAPS
    return traps_html(TRAPS)


def all_traps_index_html():
    from content.traps import TRAPS
    return traps_index_html(TRAPS)
