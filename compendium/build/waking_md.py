"""Change the Markdown of a Dawnwatch book into HTML.

The Markdown is the Markdown of the tutorial adventure:
  #   the title of a chapter
  ##  a scene, ###  a part of a scene
  >   a block quote is read-aloud text
  > **Label:** a block quote that starts with a bold label is a box for the GM.
      The labels are "GM tip", "Teach", "Thread (...)", and "Scaling".

A directive is a line with only the directive on it:
  {{statblock: Name}}   {{treasure: Name}}   {{map: id}}   {{handout: NN-name}}

The caller gives one function for each directive kind. A function gets the
argument of the directive and returns HTML.
"""
import html
import re

import markdown as mdlib

DIRECTIVE = re.compile(r"^[ \t]*\{\{\s*(statblock|treasure|map|handout)\s*:\s*(.+?)\s*\}\}[ \t]*$", re.M)
TOKEN = "WAKINGDIRECTIVE{}X"
# A link to another Markdown file or to an anchor does not work in a book. Keep the text only.
LOCAL_LINK = re.compile(r"\[([^\]]+)\]\((?!https?:|mailto:)[^)]*\)")
GM_LABEL = re.compile(r"<blockquote>\s*<p>\s*<strong>\s*(GM tip|Teach|Thread \(|Scaling)")
GM_KIND = {"GM tip": "tip", "Teach": "teach", "Thread (": "thread", "Scaling": "scaling"}


def slug(text):
    """A plain anchor name: lower case letters, digits, and hyphens."""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).lower().replace("'", "").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def directives(text):
    """The (kind, argument) pairs of all directives in a Markdown text, in order."""
    return DIRECTIVE.findall(text)


def classify_quotes(h):
    """Give each block quote a class: "gm-box gm-<kind>" for a box with a label, else "read-aloud"."""
    def rep(m):
        kind = GM_KIND[m.group(1)]
        return m.group(0).replace("<blockquote>", f'<blockquote class="gm-box gm-{kind}">', 1)
    h = GM_LABEL.sub(rep, h)
    return h.replace("<blockquote>", '<blockquote class="read-aloud">')


def number_headings(h, prefix):
    """Give each h2 and h3 an id. The prefix keeps the ids of two files apart."""
    seen = {}

    def rep(m):
        level, attrs, inner = m.group(1), m.group(2), m.group(3)
        if "id=" in attrs:
            return m.group(0)
        base = f"{prefix}-{slug(inner)}" if prefix else slug(inner)
        seen[base] = seen.get(base, 0) + 1
        hid = base if seen[base] == 1 else f"{base}-{seen[base]}"
        return f'<h{level}{attrs} id="{hid}">{inner}</h{level}>'
    return re.sub(r"<h([23])([^>]*)>(.*?)</h\1>", rep, h)


def render(text, handlers, prefix=""):
    """Change one Markdown text into HTML.

    handlers maps a directive kind to a function of one argument that returns HTML.
    A kind with no handler stays in the text as it is.
    """
    found = []

    def keep(m):
        found.append((m.group(1), m.group(2)))
        return "\n\n" + TOKEN.format(len(found) - 1) + "\n\n"
    text = DIRECTIVE.sub(keep, text)
    text = LOCAL_LINK.sub(r"\1", text)
    h = mdlib.markdown(text, extensions=["tables", "sane_lists"])
    h = classify_quotes(h)
    h = number_headings(h, prefix)
    for i, (kind, arg) in enumerate(found):
        f = handlers.get(kind)
        out = f(arg) if f else html.escape("{{%s: %s}}" % (kind, arg))
        h = h.replace(f"<p>{TOKEN.format(i)}</p>", out).replace(TOKEN.format(i), out)
    return h


def demote(text, levels=1):
    """Move each Markdown heading down by `levels`, so that one file fits inside another."""
    return re.sub(r"^(#{1,6})(?=\s)", lambda m: m.group(1) + "#" * levels, text, flags=re.M)


def title_of(text, default=""):
    """The text of the first # heading, or the default."""
    m = re.search(r"^#\s+(.+?)\s*#*\s*$", text, re.M)
    return m.group(1) if m else default


def drop_title(text):
    """Remove the first # heading."""
    return re.sub(r"^#\s+.*\n?", "", text, count=1, flags=re.M)


def drop_section(text, heading):
    """Remove a ## section and its text up to the next ## or # heading."""
    return re.sub(rf"^##\s+{re.escape(heading)}\s*\n.*?(?=^#{{1,2}}\s|\Z)", "", text, flags=re.M | re.S)
