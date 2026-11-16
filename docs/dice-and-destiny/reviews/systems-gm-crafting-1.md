# Review request: Crafting and gathering, batch 1 (format, renderer, rules, samples)

Workstream: GM optional systems (the classes session).

## State

Nothing is committed. `build.sh` passes (BUILD_OK, fonts OK). All 196 tests
pass. The Game Master's Compendium is 328 pages. I looked at page 287: the
rules, the two tables, and the start of the lists are clean. The 5-column
cost table wraps "2,000 GP" in the narrow column, which still reads clearly.

## Planned commits

1. `feat: render the crafting materials and recipes`:
   `build/render_crafting.py`, `tests/test_render_crafting.py` (13 tests;
   each builds its own materials, recipes, and items),
   `content/crafting/__init__.py` with no entries, and the REGISTRY line
   `"crafting": lambda m: [e["name"] for e in m.MATERIALS] + [e["item"] for e
   in m.RECIPES]`.
2. `feat: add the Crafting and Gathering chapter`: three lines in `build.py`
   (`{{CRAFT_BASE}}`, `{{CRAFT_MATERIALS}}`, `{{CRAFT_RECIPES}}`) and the
   chapter in `gm.src.html`, after "Injuries and Scars", before Part VI. The
   heading has no number.
3. `feat: add the first crafting materials and recipes`:
   `content/crafting/samples.py`.

## The format

- `MATERIALS`: `name`, `source` ("Monster" or "Biome"), `origin` (the
  creature or the biome), `rarity`, `check` (for example "Wisdom
  (Survival)"), `text`. The rarity sets the value and the DC: Common 10 GP /
  DC 10, Uncommon 50 / 13, Rare 500 / 15, Very Rare 5,000 / 18, Legendary
  25,000 / 20. A material is worth about a quarter of the item.
- `RECIPES`: `item` (the exact name of an SRD magic item or an original
  magic item), `rarity`, `consumable`, `tool`, `materials` (names), `gold`,
  `days`, `note`.

## The guard against cheap items (your rule)

`render_crafting.BASE` has the cost and the workdays of crafting a magic
item in the 2024 core rules: Common 50 GP / 5 days, Uncommon 200 / 10, Rare
2,000 / 50, Very Rare 20,000 / 125, Legendary 100,000 / 250. A consumable
takes half of both. The build stops if a recipe:

- costs less than 80% of the base in all (its gold plus the value of its
  materials), or takes less than 80% of the base workdays;
- makes an item that is not in the SRD data (`data/all_magicitems.json`) or
  in the original items, or gives it a different rarity than the item has;
- has no material of its own rarity, or a material of a higher rarity, or an
  unknown material.

So a party saves money only by harvesting its own materials (about 25% of
the cost), and time not at all. The chapter text says this plainly.

## The rules (the chapter text, in short)

- Harvesting: 10 minutes (Medium or smaller) to 1 hour (Huge or larger), the
  material's check against the DC of its rarity; a failure by 5 or more
  ruins it. The rarity comes from the CR: 0 to 2 Common, 3 to 6 Uncommon, 7
  to 12 Rare, 13 to 18 Very Rare, 19+ Legendary.
- Gathering: 1 hour in a biome during travel or downtime. Common and
  Uncommon materials are found in most places of the biome; rarer ones only
  where the GM places them.
- Selling: half the value. Buying: full value, where the GM allows it.
- Crafting: tool proficiency; for a permanent magic item, also Arcana or
  spellcasting; the materials, the gold, any base item, and the workdays. A
  check with the tool at the end (the DC of the item's rarity). On a
  failure, half the gold and the time are lost; the materials are kept. Two
  crafters with the right proficiencies can work together; each workday of
  both counts as two.
- Power and encounters: crafted items count as treasure (give one fewer item
  of that rarity in the next treasures). If the party has more items than
  planned: +10% HP for important enemies, or one more low-CR monster for
  each four characters.

## The samples

Materials: Moonpetal (Common, Forest), Spinner's Gland (Common, Giant
Spider), Frost Salt (Uncommon, Arctic), Kelp Heart (Uncommon, Coast or
Underwater), Winter Wolf Pelt (Uncommon, Winter Wolf), Young Dragon Scale
(Rare, any Dragon of CR 7 to 12).

| Recipe | Rarity | Materials | Gold | Total | Days | Base |
|---|---|---|---|---|---|---|
| Potion of Climbing | Common, consumable | Moonpetal, Spinner's Gland | 5 | 25 GP | 3 | 25 GP, 2.5 days |
| Potion of Resistance | Uncommon, consumable | Frost Salt | 50 | 100 GP | 5 | 100 GP, 5 days |
| Potion of Water Breathing | Uncommon, consumable | Kelp Heart | 50 | 100 GP | 5 | 100 GP, 5 days |
| Boots of the Winterlands | Uncommon | Winter Wolf Pelt | 150 | 200 GP | 10 | 200 GP, 10 days |
| Armor of Resistance | Rare | Young Dragon Scale (+ base armor) | 1,500 | 2,000 GP | 50 | 2,000 GP, 50 days |

## Next batches

About 40 materials (monsters by CR band and the biomes of the Journeys
system) and about 40 recipes, most of them Common to Rare. I will check the
creature names against the SRD and the original bestiary.

## Questions

1. I could not confirm that the SRD 5.2 itself has the crafting table of the
   2024 core rules (my local data has no crafting rules). The chapter states
   the table as its own rule, so it works either way. Is that acceptable?
2. Two crafters halve the days. The 2024 rules let crafters combine their
   work, so the total person-days stay the same. Keep it?
3. Potion of Healing is adventuring gear in the SRD data, not a magic item,
   so the guard can't check it. Should recipes for gear (with the 2024 rule
   of half the price in materials) be in this system, or only magic items?
