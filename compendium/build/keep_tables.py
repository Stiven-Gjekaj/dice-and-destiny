"""Keep small tables in one piece across a column or a page break.

A table with few body rows looks broken when one or two of its rows go to the next column
or page. This marks each such table with the class "keep", and book.css keeps it whole.
A short bold label just before the table stays with it.
"""
import re

MAX_ROWS = 10
TABLE = re.compile(r"(?P<label><p><strong>[^<]{1,80}</strong></p>\s*)?(?P<table><table(\s[^>]*)?>.*?</table>)", re.S)


def body_rows(table):
    """The count of rows of a table that are not in its head."""
    body = re.sub(r"<thead.*?</thead>", "", table, flags=re.S)
    return len(re.findall(r"<tr[\s>]", body))


def mark(table):
    head = re.match(r"<table(\s[^>]*)?>", table).group(0)
    m = re.search(r'class="([^"]*)"', head)
    if m:
        new = head.replace(m.group(0), f'class="{m.group(1)} keep"', 1)
    else:
        new = head[:-1] + ' class="keep">'
    return new + table[len(head):]


def keep_small_tables(html, max_rows=MAX_ROWS):
    """Add the class "keep" to each table with at most max_rows body rows.

    If a short bold label paragraph comes just before such a table, put the label and the
    table in one block that is also kept whole, so that the label does not stay behind.
    """
    def one(m):
        table, label = m.group("table"), m.group("label") or ""
        if body_rows(table) > max_rows:
            return m.group(0)
        if label:
            return f'<div class="keep">{label}{mark(table)}</div>'
        return mark(table)
    return TABLE.sub(one, html)
