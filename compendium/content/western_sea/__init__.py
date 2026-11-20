"""The content of the campaign book Beyond the Western Sea.

The Compendiums do not read this package. Only the build of this book reads it.

Each file adds one list, in the same format as the Dawnwatch content:
  creatures.py  MON    monsters, as in content/monsters
  people.py     NPCS   pairs (role, M(...)), as in content/npcs. The role is one free line of text.
                       A person with no statblock is a pair (role, "Name").
  treasures.py  ITEMS  tuples (name, category, rarity, attunement, text), as in content/items
  places.py     PLACES the places for the maps and the index

The book can use 3d6 in place of a d20. Thus a creature has an armor class of 16 or less,
and each save DC is 15 or less. The content check stops on a higher value.
"""
from content.collect import collect_list

MON = collect_list(__name__, "MON", "creatures")
NPCS = collect_list(__name__, "NPCS", "people")
ITEMS = collect_list(__name__, "ITEMS", "treasures")
PLACES = collect_list(__name__, "PLACES", "places")
