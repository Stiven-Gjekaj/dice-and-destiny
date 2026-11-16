"""Render the optional rules systems (content/systems) into HTML for the two books.

The Player's Compendium shows the Blessings, the Curses, and the Bonds.
The Game Master's Compendium shows the Taints with their hidden prices.
The Player's Compendium also shows the Techniques and the Legend paths.
The Game Master's Compendium also shows the Journey biomes and the Factions.
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
# The types of Techniques, in the order of the book.
TECH_TYPES = {"Stance": "Stances", "Maneuver": "Maneuvers", "Shaping": "Spell Shapings"}
TECH_KEYS = {"name", "type", "cost", "level", "timing", "text"}
TECH_LEVELS = (1, 5, 11, 17)
TECH_COST = (1, 3)
LEGEND_KEYS = {"name", "summary", "deeds", "fall", "tiers"}
# The legend points and the character level that each tier needs.
LEGEND_TIERS = [("I", 1, 1), ("II", 3, 5), ("III", 6, 9), ("IV", 10, 13), ("V", 15, 17)]
BIOME_KEYS = {"name", "summary", "navigate", "forage", "weather", "encounters"}
BIOME_DC = (5, 25)
FACTION_KEYS = {"name", "summary", "goal", "gain", "lose", "rival", "ranks"}
# The renown that each rank of a faction needs.
FACTION_RANKS = (3, 10, 20, 35, 50)


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


def technique_errors(t):
    """Return a list of the problems of one Technique entry. An empty list means no problem."""
    name = t.get("name", "?")
    errors = [f"Technique '{name}': missing key '{k}'" for k in sorted(TECH_KEYS - set(t))]
    errors += [f"Technique '{name}': unknown key '{k}'" for k in sorted(set(t) - TECH_KEYS)]
    if errors:
        return errors
    if t["type"] not in TECH_TYPES:
        errors.append(f"Technique '{name}': type '{t['type']}' is not one of {list(TECH_TYPES)}")
    if not (isinstance(t["cost"], int) and TECH_COST[0] <= t["cost"] <= TECH_COST[1]):
        errors.append(f"Technique '{name}': cost must be a whole number from {TECH_COST[0]} to {TECH_COST[1]}")
    if t["level"] not in TECH_LEVELS:
        errors.append(f"Technique '{name}': level must be one of {list(TECH_LEVELS)}")
    return errors


def technique_html(t):
    """One Technique: the name, a line with the type, the cost, the timing and the level, then the text."""
    _stop_on(technique_errors(t))
    pts = "1 point" if t["cost"] == 1 else f'{t["cost"]} points'
    meta = f'{t["type"]} · {pts} · {E(t["timing"])}'
    if t["level"] > 1:
        meta += f' · level {t["level"]}+'
    return (f'<div class="entry sys-tech"><h4 class="sp-name">{E(t["name"])}</h4>'
            f'<div class="sp-meta"><i>{meta}</i></div><p>{feature_text(t["text"])}</p></div>')


def techniques_html(techs):
    """All Techniques, grouped by type, each group in the order of the names. Return "" if there are none."""
    _stop_on([e for t in techs for e in technique_errors(t)])
    out = []
    for ty, plural in TECH_TYPES.items():
        group = sorted((t for t in techs if t["type"] == ty), key=lambda t: t["name"])
        if group:
            out.append(f'<h2>{plural}</h2><div class="cols2 compendium">')
            out += [technique_html(t) for t in group]
            out.append("</div>")
    return "\n".join(out)


def all_techniques_html():
    from content.systems import TECHNIQUES
    return techniques_html(TECHNIQUES)


def legend_errors(p):
    """Return a list of the problems of one Legend path entry. An empty list means no problem."""
    name = p.get("name", "?")
    errors = [f"Legend '{name}': missing key '{k}'" for k in sorted(LEGEND_KEYS - set(p))]
    errors += [f"Legend '{name}': unknown key '{k}'" for k in sorted(set(p) - LEGEND_KEYS)]
    if errors:
        return errors
    if len(p["tiers"]) != len(LEGEND_TIERS):
        errors.append(f"Legend '{name}': needs exactly {len(LEGEND_TIERS)} tiers")
    elif any(len(t) != 2 for t in p["tiers"]):
        errors.append(f"Legend '{name}': each tier must be (title, benefit)")
    return errors


def legend_html(p):
    """One Legend path: the summary, the deeds, the fall, then the five tiers with their points and levels."""
    _stop_on(legend_errors(p))
    out = [f'<div class="entry sys-legend"><h4 class="sp-name">{E(p["name"])}</h4>',
           f'<p><i>{feature_text(p["summary"])}</i></p><dl class="feat">',
           f'<dt>Deeds</dt><dd>{feature_text(p["deeds"])}</dd>',
           f'<dt>The fall</dt><dd>{feature_text(p["fall"])}</dd>']
    for (num, pts, lv), (title, text) in zip(LEGEND_TIERS, p["tiers"]):
        word = "point" if pts == 1 else "points"
        out.append(f'<dt><span class="lv">{num}</span>{E(title)} <span class="small muted">({pts} {word}, level {lv}+)</span></dt>'
                   f'<dd>{feature_text(text)}</dd>')
    out.append("</dl></div>")
    return "\n".join(out)


def legends_html(paths):
    """All Legend paths, in the order of the names. Return "" if there are none."""
    _stop_on([e for p in paths for e in legend_errors(p)])
    if not paths:
        return ""
    group = sorted(paths, key=lambda p: p["name"])
    return '<div class="cols2 compendium">' + "\n".join(legend_html(p) for p in group) + "</div>"


def all_legends_html():
    from content.systems import LEGENDS
    return legends_html(LEGENDS)


def biome_errors(b):
    """Return a list of the problems of one Journey biome entry. An empty list means no problem."""
    name = b.get("name", "?")
    errors = [f"Biome '{name}': missing key '{k}'" for k in sorted(BIOME_KEYS - set(b))]
    errors += [f"Biome '{name}': unknown key '{k}'" for k in sorted(set(b) - BIOME_KEYS)]
    if errors:
        return errors
    for k in ("navigate", "forage"):
        if not (isinstance(b[k], int) and BIOME_DC[0] <= b[k] <= BIOME_DC[1]):
            errors.append(f"Biome '{name}': {k} must be a DC from {BIOME_DC[0]} to {BIOME_DC[1]}")
    if len(b["weather"]) != 6 or any(len(w) != 2 for w in b["weather"]):
        errors.append(f"Biome '{name}': weather must be 6 rows of (name, effect)")
    if len(b["encounters"]) != 8:
        errors.append(f"Biome '{name}': encounters must be 8 rows")
    return errors


def biome_html(b):
    """One biome: the DCs, the summary, a d6 weather table, and a d8 encounter table."""
    _stop_on(biome_errors(b))
    weather = "".join(f'<tr><td class="c">{i}</td><td><b>{E(n)}</b></td><td>{feature_text(t)}</td></tr>'
                      for i, (n, t) in enumerate(b["weather"], start=1))
    enc = "".join(f'<tr><td class="c">{i}</td><td>{feature_text(t)}</td></tr>' for i, t in enumerate(b["encounters"], start=1))
    return (f'<div class="entry sys-biome"><h4 class="sp-name">{E(b["name"])}</h4>'
            f'<div class="sp-meta"><i>Navigation DC {b["navigate"]} · Foraging DC {b["forage"]}</i></div>'
            f'<p>{feature_text(b["summary"])}</p>'
            f'<table class="compact"><caption>{E(b["name"])} Weather</caption><thead><tr><th class="c">d6</th><th>Weather</th><th>Effect</th></tr></thead>'
            f'<tbody>{weather}</tbody></table>'
            f'<table class="compact"><caption>{E(b["name"])} Encounters</caption><thead><tr><th class="c">d8</th><th>Encounter</th></tr></thead>'
            f'<tbody>{enc}</tbody></table></div>')


def biomes_html(biomes):
    """All Journey biomes, in the order of the names. Return "" if there are none."""
    _stop_on([e for b in biomes for e in biome_errors(b)])
    if not biomes:
        return ""
    return '<div class="cols2 compendium">' + "\n".join(biome_html(b) for b in sorted(biomes, key=lambda b: b["name"])) + "</div>"


def all_biomes_html():
    from content.systems import BIOMES
    return biomes_html(BIOMES)


def faction_errors(f):
    """Return a list of the problems of one Faction entry. An empty list means no problem."""
    name = f.get("name", "?")
    errors = [f"Faction '{name}': missing key '{k}'" for k in sorted(FACTION_KEYS - set(f))]
    errors += [f"Faction '{name}': unknown key '{k}'" for k in sorted(set(f) - FACTION_KEYS)]
    if errors:
        return errors
    if len(f["ranks"]) != len(FACTION_RANKS) or any(len(r) != 2 for r in f["ranks"]):
        errors.append(f"Faction '{name}': ranks must be {len(FACTION_RANKS)} rows of (title, reward)")
    return errors


def faction_html(f):
    """One Faction: the summary, the goal, how renown is won and lost, the rival, and a table of the ranks."""
    _stop_on(faction_errors(f))
    rows = "".join(f'<tr><td class="c">{n}</td><td><b>{E(t)}</b></td><td>{feature_text(r)}</td></tr>'
                   for n, (t, r) in zip(FACTION_RANKS, f["ranks"]))
    return (f'<div class="entry sys-faction"><h4 class="sp-name">{E(f["name"])}</h4>'
            f'<p><i>{feature_text(f["summary"])}</i></p><dl class="feat">'
            f'<dt>Goal</dt><dd>{feature_text(f["goal"])}</dd>'
            f'<dt>Gain renown</dt><dd>{feature_text(f["gain"])}</dd>'
            f'<dt>Lose renown</dt><dd>{feature_text(f["lose"])}</dd>'
            f'<dt>Rival</dt><dd>{feature_text(f["rival"])}</dd></dl>'
            f'<table class="compact"><caption>{E(f["name"])} Ranks</caption><thead><tr><th class="c">Renown</th><th>Rank</th><th>Reward</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')


def factions_html(factions):
    """All Factions, in the order of the names. Return "" if there are none."""
    _stop_on([e for f in factions for e in faction_errors(f)])
    if not factions:
        return ""
    return '<div class="cols2 compendium">' + "\n".join(faction_html(f) for f in sorted(factions, key=lambda f: f["name"])) + "</div>"


def all_factions_html():
    from content.systems import FACTIONS
    return factions_html(FACTIONS)
