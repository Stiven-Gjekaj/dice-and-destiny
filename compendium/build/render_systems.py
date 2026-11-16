"""Render the optional rules systems (content/systems) into HTML for the two books.

The Player's Compendium shows the Blessings, the Curses, and the Bonds.
The Game Master's Compendium shows the Taints with their hidden prices.
"""
import html

from orig_render import feature_text

E = html.escape

# The kinds of Marks, in the order of the book, and the book that shows each kind.
KINDS = {"Blessing": "player", "Curse": "player", "Taint": "gm"}
PLURAL = {"Blessing": "Blessings", "Curse": "Curses", "Taint": "Taints"}
MARK_KEYS = {"name", "kind", "hidden", "summary", "benefit", "cost", "grows", "thresholds",
             "give_in", "scar", "ends", "ends_after", "secret", "blocks_bonds"}
BOND_KEYS = {"name", "summary", "special", "strain", "example"}
TRACK_TOP = 5


def mark_errors(m):
    """Return a list of the problems of one Mark entry. An empty list means no problem."""
    name = m.get("name", "?")
    errors = [f"Mark '{name}': missing key '{k}'" for k in sorted(MARK_KEYS - set(m))]
    errors += [f"Mark '{name}': unknown key '{k}'" for k in sorted(set(m) - MARK_KEYS)]
    if errors:
        return errors
    if m["kind"] not in KINDS:
        errors.append(f"Mark '{name}': kind '{m['kind']}' is not one of {list(KINDS)}")
    if m["kind"] != "Curse" and not m["benefit"]:
        errors.append(f"Mark '{name}': only a Curse can have no benefit")
    if m["secret"] and m["kind"] != "Taint":
        errors.append(f"Mark '{name}': only a Taint can have a secret, because the player reads the other kinds")
    values = [v for v, _ in m["thresholds"]]
    if not values:
        errors.append(f"Mark '{name}': needs at least one threshold")
    if any(not 1 <= v < TRACK_TOP for v in values):
        errors.append(f"Mark '{name}': a threshold must be from 1 to {TRACK_TOP - 1}")
    if values != sorted(set(values)):
        errors.append(f"Mark '{name}': the thresholds must be in order, each value one time")
    return errors


def bond_errors(b):
    """Return a list of the problems of one Bond entry. An empty list means no problem."""
    name = b.get("name", "?")
    errors = [f"Bond '{name}': missing key '{k}'" for k in sorted(BOND_KEYS - set(b))]
    errors += [f"Bond '{name}': unknown key '{k}'" for k in sorted(set(b) - BOND_KEYS)]
    if not errors and len(b["special"]) != 2:
        errors.append(f"Bond '{name}': special must be (name, text)")
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def track_html(m):
    """A track from 0 to 5 that a player can mark with a pencil. Thresholds and the crisis are in bold."""
    marks = {v for v, _ in m["thresholds"]}
    cells = []
    for v in range(TRACK_TOP + 1):
        label = "5 Crisis" if v == TRACK_TOP else str(v)
        cells.append(f'<td class="c"><b>{label}</b></td>' if v in marks or v == TRACK_TOP else f'<td class="c">{label}</td>')
    return f'<table class="compact sys-track"><tbody><tr><th>Track</th>{"".join(cells)}</tr></tbody></table>'


def mark_html(m, gm=False):
    """One Mark. The secret part of the price shows only in the GM's book."""
    _stop_on(mark_errors(m))
    seen = "hidden" if m["hidden"] else "open"
    meta = f'{m["kind"]} · {seen} by default'
    if m["blocks_bonds"]:
        meta += " · blocks bond help"
    out = [f'<div class="entry sys-mark"><h4 class="sp-name">{E(m["name"])}</h4><div class="sp-meta"><i>{meta}</i></div>',
           f'<p><i>{feature_text(m["summary"])}</i></p><dl class="feat">']
    rows = [("Benefit", m["benefit"] or "None."), ("Cost", m["cost"]), ("The track grows", m["grows"])]
    out += [f"<dt>{k}</dt><dd>{feature_text(v)}</dd>" for k, v in rows]
    out.append("</dl>")
    out.append(track_html(m))
    out.append('<dl class="feat">')
    out += [f'<dt><span class="lv">{v}</span>Threshold</dt><dd>{feature_text(t)}</dd>' for v, t in m["thresholds"]]
    out.append(f'<dt><span class="lv">5</span>Give in</dt><dd>{feature_text(m["give_in"])}</dd>')
    out.append(f'<dt><span class="lv">5</span>Break free</dt><dd>{feature_text(m["scar"])}</dd>')
    out.append(f'<dt>Ending the Mark</dt><dd>{feature_text(m["ends"])}</dd>')
    out.append(f'<dt>Ending it after you give in</dt><dd>{feature_text(m["ends_after"])}</dd>')
    out.append("</dl>")
    if gm and m["secret"]:
        out.append(f'<div class="box red"><h4>The hidden price</h4><p>{feature_text(m["secret"])}</p></div>')
    out.append("</div>")
    return "\n".join(out)


def marks_html(marks, book):
    """The Marks of one book, grouped by kind, each group in the order of the names.

    Return "" if the book has no Marks. Stop on a Mark with a problem, also a Mark of the other book.
    """
    _stop_on([e for m in marks for e in mark_errors(m)])
    out = []
    for kind in [k for k, b in KINDS.items() if b == book]:
        group = sorted((m for m in marks if m["kind"] == kind), key=lambda m: m["name"])
        if group:
            out.append(f'<h2>{PLURAL[kind]}</h2><div class="cols2 compendium">')
            out += [mark_html(m, gm=book == "gm") for m in group]
            out.append("</div>")
    return "\n".join(out)


def bond_html(b):
    """One Bond kind with its special use, its strain, and an example."""
    _stop_on(bond_errors(b))
    special, text = b["special"]
    return (f'<div class="entry sys-bond"><h4 class="sp-name">{E(b["name"])}</h4>'
            f'<p><i>{feature_text(b["summary"])}</i></p><dl class="feat">'
            f'<dt>Special: {E(special)}</dt><dd>{feature_text(text)}</dd>'
            f'<dt>Strain</dt><dd>{feature_text(b["strain"])}</dd></dl>'
            f'<div class="example"><p>{feature_text(b["example"])}</p></div></div>')


def bonds_html(bonds):
    """All Bond kinds, in the order of the files. Return "" if there are none."""
    if not bonds:
        return ""
    return '<div class="cols2 compendium">' + "\n".join(bond_html(b) for b in bonds) + "</div>"


def player_marks_html():
    from content.systems import MARKS
    return marks_html(MARKS, "player")


def gm_marks_html():
    from content.systems import MARKS
    return marks_html(MARKS, "gm")


def all_bonds_html():
    from content.systems import BONDS
    return bonds_html(BONDS)
