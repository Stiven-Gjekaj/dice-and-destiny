# Review request: systems, batch 10 (10 Journey biomes)

Systems batch 10: 10 biomes for Journeys, each with a navigation DC, a
foraging DC, a d6 weather table, and a d8 encounter table. Not committed.
It is on top of batch 8 (Legend paths) and batch 9 (Journeys format), also
not committed. build.sh passes with all three: 215 tests, content check,
page check, Type 3 check. GM 392 pages (the biomes add 4). No em-dash.

## Files

One commit after approval: `feat: add 10 Journey biomes`.

- `compendium/content/systems/biomes.py`: Arctic, Coast, Desert, Forest,
  Grassland, Hills, Mountains, Swamp, Underground, Roads and Farmland.
- `compendium/books/gm.src.html`: the heading "Biomes" before
  `{{SYS_BIOMES}}` (it comes with the entries, so no commit has an empty
  heading).

## Contents

- DCs: navigation 5 (roads) to 16 (underground); foraging 8 to 20.
- Weather: each row has one clear effect with SRD terms (Lightly or
  Heavily Obscured, difficult terrain, Exhaustion on a failed DC 10
  Constitution save, Disadvantage for the guide). The harshest rows:
  Mountain avalanche (DC 13 Dexterity, 4d10 Bludgeoning, after a DC 15
  Survival check to see it), desert sandstorm (Slow pace only).
- Encounters: 80 rows. About half are monsters, the rest are people,
  places, and signs. Every monster name is in the SRD 5.2 data (69 names,
  checked against `data/all_creatures.json`). The tables give no numbers of
  monsters; the GM picks a number for the party's level.

## Things I am not sure of

1. The monsters cover a wide range of CR in one table (for example Wolves
   and a Frost Giant in the Arctic). The chapter tells the GM to pick a
   number that fits; a table for each tier would be 4 times the size.
2. A table can break across the two columns (Arctic Encounters row 8 goes
   to the next column). It reads correctly. Tell me if you want each table
   kept in one column.
3. Next: Factions and renown (format and rules).
