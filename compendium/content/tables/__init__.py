"""World-building table sets. Each file adds a list TABLE_SETS.

A TABLE_SETS entry is a dict with these keys:
  name: the name of the set
  theme: one of the THEMES in build/render_tables.py, for example "Settlements"
  summary: one or two sentences that tell how to use the set
  tables: a list of (die, title, entries). The die is "d4", "d6", "d8", "d10",
    "d12", or "d20". The count of entries is the same as the faces of the die.

In all text, [[label]] shows the label in bold.
"""
from content.collect import collect_list

TABLE_SETS = collect_list(__name__, "TABLE_SETS")
