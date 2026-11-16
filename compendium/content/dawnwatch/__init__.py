"""The content of The Dawnwatch campaign books.

The Compendiums do not read this package. Only the build of a Dawnwatch book reads it.

Each file adds one list, in the same format as the Compendium content:
  creatures_*.py  MON    monsters, as in content/monsters
  people_*.py     NPCS   pairs (role, M(...)), as in content/npcs. The role is one free line of text.
                         A person with no statblock is a pair (role, "Name").
  treasures_*.py  ITEMS  tuples (name, category, rarity, attunement, text), as in content/items
  places.py       PLACES the places for the maps and the index
"""
from content.collect import collect_list

MON = collect_list(__name__, "MON", "creatures_")
NPCS = collect_list(__name__, "NPCS", "people_")
ITEMS = collect_list(__name__, "ITEMS", "treasures_")
PLACES = collect_list(__name__, "PLACES", "places")
