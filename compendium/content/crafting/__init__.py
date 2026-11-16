"""The Crafting and gathering optional system. Each file adds lists MATERIALS and RECIPES.

A material entry is a dict with these keys:
  name: the name of the material
  source: "Monster" (harvested from a creature) or "Biome" (gathered in a place)
  origin: the creature (for example "Troll", or "any Dragon of CR 7 to 12") or the biome (for example "Forest")
  rarity: "Common", "Uncommon", "Rare", "Very Rare", or "Legendary". The rarity sets the value and the DC.
  check: the check to harvest or gather it, for example "Wisdom (Survival)"
  text: what it is and what it is good for

A recipe entry is a dict with these keys:
  item: the exact name of the item it makes: an SRD magic item, or an original magic item of this book
  rarity: the rarity of that item. The build checks it against the item.
  consumable: True for a potion, an oil, or another item that is used up
  tool: the tool that the crafter must be proficient with
  materials: a list of material names. A name can be in the list more than one time.
  gold: the gold pieces that the crafter spends, apart from the materials
  days: the workdays (8 hours each) that the crafting takes
  note: anything else that the recipe needs, for example a base item, or ""

A gear recipe (in the list GEAR) is a dict with these keys:
  item: the exact name of SRD equipment with a price, for example "Potion of Healing"
  tool: the tool that the crafter must be proficient with
  materials: a list of material names, or an empty list
  gold: the gold pieces that the crafter spends, apart from the materials
  days: the workdays that the crafting takes
  note: anything else that the recipe needs, or ""
The materials and the gold of a gear recipe cost at least 80% of half the price of the item.

In all text, [[label]] shows the label in bold.
"""
from content.collect import collect_list

MATERIALS = collect_list(__name__, "MATERIALS")
RECIPES = collect_list(__name__, "RECIPES")
GEAR = collect_list(__name__, "GEAR")
