# Note from the systems workstream to the classes session: BIOMES is on main

This is a note, not a review request.

The Journey biomes are on `main`. The crafting system can read the biome
names from them, in place of its own list.

- Import: `from content.systems import BIOMES`.
- Names: `[b["name"] for b in BIOMES]`. They are: Arctic, Coast, Desert,
  Forest, Grassland, Hill, Mountain, Swamp, Underdark, Roads and Farmland.
- The names follow the SRD biome names. "Underwater" and "Urban" are not
  Journey biomes (a party does not travel through them in the same way).
  If the crafting check must also accept them, add them to its own list next
  to the names from `BIOMES`.
- The format of a biome entry is in the docstring of
  `compendium/content/systems/__init__.py`.
