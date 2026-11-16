# Review request: player options, magic items batch 2

Magic items batch 1 is on main (b2e3967, docs d6d32cf), with your changes:
Oathstone keeps the d10 limit (a d10 die can't shrink from strain, except
from a broken oath); Training Weights give their benefit for only one pair
at a time; Charm of the Slow Tide mends after 7 days and can't stop a track
from reaching 5.

## The batch

- File: `compendium/content/items/options_heritage.py` (not committed).
- Entries: 40 heritage items, 2 for each of the 20 original species.
  Player options items: 33 to 73.
- Build: `compendium/build.sh` passes. 180 tests pass, the checks are OK.
  Player 276 pages, GM 378. I read GM page 292. No overflow.
- I searched every content file and the SRD magic items for each name. No
  name is in use.

Each species gets one small item (a Common or Uncommon trick that shows its
culture) and one stronger item (Uncommon or Rare). Anyone can use the
items. Where an item says "A Lumen who..." or similar, a member of that
species gets a small extra benefit, so that the item feels like theirs
without being useless to others. No item is above Rare.

| Species | Item | Rarity | Attunement | Equal to |
|---|---|---|---|---|
| Lumen | Starglass Pendant | Common | no | a small trick |
| Lumen | Lumen Choir Harp | Rare | yes | temp HP for allies 1/day (Instrument of the Bards-type) |
| Hollowborn | Grave-Bell Ring | Uncommon | yes | Advantage on Death Saving Throws |
| Hollowborn | Shroud of the Second Death | Rare | yes | drop to 1 HP instead of 0, 1/day |
| Brinewrought | Salt-Crust Gauntlets | Uncommon | yes | Gauntlets of Ogre Power, much smaller |
| Brinewrought | Tide Horn | Rare | no | Fog Cloud or Gust of Wind 1/day |
| Kilnborn | Kiln-Fired Hammer | Uncommon | no | +1 weapon |
| Kilnborn | Ashen Apron | Common | no | a small trick (nonmagical fire only) |
| Sporekin | Spore Lantern | Common | no | a small trick |
| Sporekin | Memory Cap | Rare | yes | a skill proficiency that changes each Long Rest |
| Glassborn | Dune Glass Lens | Common | no | a small trick |
| Glassborn | Mirage Cloak | Rare | yes | Disadvantage on one attack, 1/day (2 for a Glassborn) |
| Windkin | Aerie Feather Cloak | Uncommon | yes | Feather Fall always on |
| Windkin | Wind Chime of the High Peaks | Uncommon | no | Gust of Wind 1/day |
| Hoarfolk | Frost-Bead Necklace | Common | no | a small trick |
| Hoarfolk | Storyteller's Fire Stone | Uncommon | no | a camp item, Advantage against Exhaustion |
| Oathborn | Witness Quill | Uncommon | no | a small story item |
| Oathborn | Seal of the Kept Word | Rare | yes | Advantage against Charmed, know when a promise breaks |
| Rootkin | Seed of the Mother Tree | Uncommon | no | a shelter for one night |
| Rootkin | Barkskin Bracers | Rare | yes | AC can't be lower than 15 (Barkskin always on, lower) |
| Peatborn | Bog Ancestor's Charm | Uncommon | yes | Advantage on one check each day |
| Peatborn | Mire Boots | Uncommon | no | Boots of Striding and Springing-type terrain item |
| Rillfolk | Ferryman's Coin | Common | no | a small trick |
| Rillfolk | River Ring | Uncommon | yes | Ring of Swimming |
| Sunrunner | Horse-Tail Fetish | Common | no | a small trick |
| Sunrunner | Saddle of the Endless Steppe | Rare | no | a mount item (+20 Speed, long travel) |
| Hushfolk | Silence Stone | Uncommon | no | Silence (10 ft, outward only) 1/day |
| Hushfolk | Echo Cloak | Rare | yes | Cloak of Elvenkind (silence instead of sight) |
| Dreamborn | Dreamcatcher of Soft Nights | Common | no | a small trick |
| Dreamborn | Pillow of Shared Dreams | Rare | no | a story item (shared dream) |
| Gloamkin | Dusk Lantern | Uncommon | no | makes Dim Light in a 20 ft radius |
| Gloamkin | Shadow-Silk Gloves | Rare | yes | Hide as a Bonus Action in shadow |
| Cairnborn | Cairn Stone | Common | no | a small trick |
| Cairnborn | Standing-Stone Shield | Rare | yes | +1 Shield, +2 if you don't move |
| Foldfolk | Fireproof Wax Coat | Uncommon | yes | Resistance to Fire (Ring of Resistance-type, one type) |
| Foldfolk | Book of Living Pages | Rare | no | a copying book, a messenger 1/day |
| Feverblooded | Plague Nurse's Kit | Uncommon | no | 10 uses of ending Poisoned or a disease |
| Feverblooded | Ward Bell of the Walled Town | Rare | no | an area ward against disease for 24 hours, 1/day |
| Relicborn | Ruin Compass | Uncommon | no | a finder of magic items |
| Relicborn | Imperial Ward Circlet | Rare | yes | Advantage against traps and Constructs |

## Things that I am not sure of

1. Shroud of the Second Death gives anyone the Hollowborn trait (and the
   Orc's Relentless Endurance) once a day, at Rare with attunement.
2. Barkskin Bracers: AC can't be lower than 15 with any armor. It helps
   only characters with low AC, so I made it Rare.
3. Fireproof Wax Coat: for a Foldfolk, it removes the Fire Vulnerability.
   The Fireproofed Pages feat does the same. If a Foldfolk has both, the
   feat is wasted. I kept it, because a GM gives the coat.

## Next

The Legend path items (about 2 for each of the 12 paths), when
`content/systems/legends.py` is on main.
