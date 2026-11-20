"""The six-sided form of a dice expression.

A group with a backgammon set has only six-sided dice. Each roll in the book
shows the normal dice and, in brackets, a six-sided form with about the same
average, for example "7 (1d8 + 3) [d6 + 4]". This module makes that form.
"""
import re

MINUS = "−"

# For each die size: the flat value to add for each die that becomes a d6.
FLAT = {4: -1, 6: 0, 8: 1, 10: 2, 12: 3}

SIGN = r"(?:\+|-|−|&minus;)"
TERM = r"\d*d\d+|\d+"
EXPR = rf"\s*\d*d\d+(?:\s*{SIGN}\s*(?:{TERM}))*\s*"
# A parenthesized dice expression that " [" does not follow yet.
PAREN = re.compile(rf"\(({EXPR})\)(?!\s*\[)")
PART = re.compile(rf"({SIGN})?\s*(\d*)d(\d+)|({SIGN})?\s*(\d+)")
# "d20" or "d100" as a die, with or without a count. "d200" and "d66" do not match.
BAD_DIE = re.compile(r"(?<![A-Za-z])\d*d(20|100)(?!\d)")


def convert(expr):
    """Return the six-sided form of one dice expression.

    Return None when the form is the same, that is, when the expression has only d6s.
    Raise ValueError for a d100, for a d20 count other than 1, or for a die size
    that has no rule.
    """
    dice, flat, same = 0, 0, True
    pos = 0
    text = expr.strip()
    while pos < len(text):
        m = PART.match(text, pos)
        if not m or m.end() == pos:
            raise ValueError(f"not a dice expression: {expr!r}")
        pos = m.end()
        while pos < len(text) and text[pos].isspace():
            pos += 1
        if m.group(3):
            sign = -1 if m.group(1) and m.group(1) != "+" else 1
            n = int(m.group(2) or 1)
            size = int(m.group(3))
            if size == 20:
                if n != 1 or sign < 0:
                    raise ValueError(f"a d20 count other than 1: {expr!r}")
                dice += 3
                same = False
                continue
            if size not in FLAT:
                raise ValueError(f"no six-sided rule for d{size}: {expr!r}")
            if sign < 0:
                raise ValueError(f"a negative die term: {expr!r}")
            dice += n
            flat += n * FLAT[size]
            if size != 6:
                same = False
        else:
            sign = -1 if m.group(4) and m.group(4) != "+" else 1
            flat += sign * int(m.group(5))
    if same:
        return None
    out = "d6" if dice == 1 else f"{dice}d6"
    if flat > 0:
        out += f" + {flat}"
    elif flat < 0:
        out += f" {MINUS} {-flat}"
    return out


def _bracket(m):
    form = convert(m.group(1))
    return m.group(0) if form is None else f"{m.group(0)} [{form}]"


def add_brackets(html):
    """Add " [form]" after each parenthesized dice expression in the text of the HTML.

    The tags and their attributes do not change. An expression that " [" already
    follows does not change, so a second pass adds nothing.
    """
    out = []
    for tok in re.split(r"(<[^>]*>)", html):
        out.append(tok if tok.startswith("<") else PAREN.sub(_bracket, tok))
    return "".join(out)


def check_dice(text):
    """Return one message for each "d20" or "d100" in the source text."""
    msgs = []
    for i, line in enumerate(text.splitlines(), 1):
        for m in BAD_DIE.finditer(line):
            msgs.append(f"line {i}: {m.group(0)} is not permitted. Use d66 or 2d6.")
    return msgs
