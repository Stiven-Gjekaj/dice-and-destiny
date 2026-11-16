"""Original traps and hazards. Each file adds a list TRAPS of entries.

The format of an entry is in build/render_traps.py.
"""
from content.collect import collect_list

TRAPS = collect_list(__name__, "TRAPS")
