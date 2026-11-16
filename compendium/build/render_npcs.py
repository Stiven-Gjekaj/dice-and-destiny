"""Render the original NPC stat blocks (content/npcs) into HTML for the GM's book.

Each entry is a pair (role, monster). The role is one of the keys of ROLES.
The monster is an M from monster_engine, so the engine calculates the
numbers in the same way as for the monsters.

An NPC is a Humanoid with a CR from 1/8 to 15.
"""
import html

from monster_engine import XP, M, crs

E = html.escape

# Role: the short line under the role heading in the book.
ROLES = {
    "Guards and Soldiers": "People who keep the peace, or break it for pay.",
    "Nobles and Officials": "People with titles, offices, and the guards to protect them.",
    "Priests and the Faithful": "People who serve a god, a temple, or a cause.",
    "Merchants and Townsfolk": "The ordinary people of a town, and the ones who sell to them.",
    "Criminals and Spies": "Thieves, smugglers, informers, and the people who hire them.",
    "Cultists": "Followers of dark powers, from the new recruit to the high priest.",
    "Sailors and Pirates": "People of the decks, the docks, and the open sea.",
    "Scholars and Mages": "People who study, teach, and cast spells for a living.",
    "Wilderness Folk": "Hunters, guides, and the people who live far from the roads.",
    "Assassins and Duelists": "People who kill with skill, for money or for honor.",
}
CR_RANGE = (0.125, 15)


def npc_errors(entry):
    """Return a list of the problems of one entry. An empty list means no problem."""
    if not (isinstance(entry, tuple) and len(entry) == 2):
        return [f"NPC entry {entry!r}: must be a pair (role, M(...))"]
    role, m = entry
    if not isinstance(m, M):
        return [f"NPC entry with role {role!r}: the second value must be an M"]
    errors = []
    if role not in ROLES:
        errors.append(f"NPC '{m.name}': role {role!r} is not one of {list(ROLES)}")
    if not m.typ.startswith("Humanoid"):
        errors.append(f"NPC '{m.name}': type '{m.typ}' is not a Humanoid")
    if not CR_RANGE[0] <= m.cr <= CR_RANGE[1]:
        errors.append(f"NPC '{m.name}': CR {crs(m.cr)} is outside 1/8 to 15")
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def _key(m):
    return (m.cr, m.name)


def npcs_html(npcs):
    """All entries, grouped by role in the order of ROLES, each group by CR and name. Return "" if there are none."""
    _stop_on([e for n in npcs for e in npc_errors(n)])
    out = []
    for role, line in ROLES.items():
        group = sorted((m for r, m in npcs if r == role), key=_key)
        if group:
            out.append(f'<h2>{E(role)}</h2><p class="chapter-intro">{E(line)}</p><div class="cols2 compendium">')
            out += [m.html() for m in group]
            out.append("</div>")
    return "\n".join(out)


def npcs_index_html(npcs):
    """For each role, the names with their CR, from the lowest CR. Return "" if there are none."""
    if not npcs:
        return ""
    _stop_on([e for n in npcs for e in npc_errors(n)])
    out = ['<div class="cols2 cr-index">']
    for role in ROLES:
        group = sorted((m for r, m in npcs if r == role), key=_key)
        if group:
            names = ", ".join(f"{E(m.name)} <span class=muted>(CR {crs(m.cr)}, {XP[m.cr]:,} XP)</span>" for m in group)
            out.append(f"<p><b>{E(role)}</b><br>{names}</p>")
    out.append("</div>")
    return "\n".join(out)


def all_npcs_html():
    from content.npcs import NPCS
    return npcs_html(NPCS)


def all_npcs_index_html():
    from content.npcs import NPCS
    return npcs_index_html(NPCS)
