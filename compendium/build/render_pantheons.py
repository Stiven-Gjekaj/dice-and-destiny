"""Render the sample pantheons (content/pantheons) into HTML for the Game Master's Compendium.

Each pantheon has an overview table and then one entry for each god. A god names the
cleric domains that suit it. The check stops on a domain that is not a cleric subclass.
"""
import html

from orig_render import feature_text

E = html.escape

PANTHEON_KEYS = {"name", "summary", "gods"}
GOD_KEYS = {"name", "title", "portfolio", "alignment", "symbol", "domains", "wants", "worshippers"}
ALIGNMENTS = {"Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic Neutral",
              "Lawful Evil", "Neutral Evil", "Chaotic Evil", "Unaligned"}
SRD_DOMAINS = {"Life Domain"}


def god_errors(g, domains):
    """Return the problems of one god. `domains` is the set of cleric subclass names."""
    name = g.get("name", "?")
    errors = [f"God '{name}': missing key '{k}'" for k in sorted(GOD_KEYS - set(g))]
    errors += [f"God '{name}': unknown key '{k}'" for k in sorted(set(g) - GOD_KEYS)]
    if errors:
        return errors
    if g["alignment"] not in ALIGNMENTS:
        errors.append(f"God '{name}': alignment '{g['alignment']}' is not an SRD alignment")
    errors += [f"God '{name}': '{d}' is not a cleric domain in this book" for d in g["domains"] if d not in domains]
    if len(set(g["domains"])) != len(g["domains"]):
        errors.append(f"God '{name}': names the same domain two times")
    return errors


def pantheon_errors(p, domains):
    """Return a list of the problems of one pantheon and its gods. An empty list means no problem."""
    name = p.get("name", "?")
    errors = [f"Pantheon '{name}': missing key '{k}'" for k in sorted(PANTHEON_KEYS - set(p))]
    errors += [f"Pantheon '{name}': unknown key '{k}'" for k in sorted(set(p) - PANTHEON_KEYS)]
    if errors:
        return errors
    if not p["gods"]:
        errors.append(f"Pantheon '{name}': needs at least one god")
    for g in p["gods"]:
        errors += god_errors(g, domains)
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def full_name(g):
    return f'{g["name"]}, {g["title"]}' if g["title"] else g["name"]


def domains_text(g):
    return ", ".join(d.replace(" Domain", "") for d in g["domains"]) or "Any"


def overview_html(p):
    """A table with one row for each god, in the order of the file."""
    rows = "".join(f'<tr><td><b>{E(full_name(g))}</b></td><td>{E(g["portfolio"])}</td><td>{E(g["alignment"])}</td>'
                   f'<td>{E(domains_text(g))}</td><td>{feature_text(g["symbol"])}</td></tr>' for g in p["gods"])
    return ('<table class="compact pantheon-table"><thead><tr><th>God</th><th>Portfolio</th><th>Alignment</th>'
            f'<th>Domains</th><th>Symbol</th></tr></thead><tbody>{rows}</tbody></table>')


def god_html(g):
    """One god: the name, the alignment, the portfolio, the wants, and the worshippers.

    The overview table gives the symbol and the domains, so the entry does not repeat them.
    """
    return (f'<div class="entry god"><h4 class="sp-name">{E(full_name(g))}</h4>'
            f'<div class="sp-meta"><i>{E(g["alignment"])} · {E(g["portfolio"])}</i></div><dl class="feat">'
            f'<dt>What the god wants</dt><dd>{feature_text(g["wants"])}</dd>'
            f'<dt>Worshippers</dt><dd>{feature_text(g["worshippers"])}</dd></dl></div>')


def pantheon_html(p, domains):
    _stop_on(pantheon_errors(p, domains))
    out = [f'<h2>{E(p["name"])}</h2>', f'<p>{feature_text(p["summary"])}</p>', overview_html(p),
           '<div class="cols2 compendium">']
    out += [god_html(g) for g in p["gods"]]
    out.append("</div>")
    return "\n".join(out)


def pantheons_html(pantheons, domains):
    """All pantheons, in the order of the files. Return "" if there are none. Stop on a problem."""
    _stop_on([e for p in pantheons for e in pantheon_errors(p, domains)])
    return "\n".join(pantheon_html(p, domains) for p in pantheons)


def cleric_domains():
    """The SRD cleric domain and the original cleric subclasses of this book."""
    from content.subclasses import SUBS
    return SRD_DOMAINS | {s[0] for s in SUBS.get("cleric", [])}


def all_pantheons_html():
    from content.pantheons import PANTHEONS
    return pantheons_html(PANTHEONS, cleric_domains())
