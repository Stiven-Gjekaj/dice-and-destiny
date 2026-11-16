"""Original NPC stat blocks. Each file adds a list NPCS of entries.

Each entry is a pair (role, M(...)). The format is in build/render_npcs.py.
"""
from content.collect import collect_list

NPCS = collect_list(__name__, "NPCS")
