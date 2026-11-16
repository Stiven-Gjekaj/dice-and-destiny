# Review request: bestiary batch 7, coast monsters

## Batch

- File: `compendium/content/monsters/coast.py` (new, not committed).
- Entries: 30 monsters from cliffs, beaches, tide pools, lighthouses, sea
  caves, and wrecks on the shore.
- Coast goes from 14 to 44 monsters.
- Coast had few monsters at CR 0 to 4 and above CR 16. The batch adds 16
  monsters at CR 0 to 4 and 4 at CR 17 or more.

## Build

- `compendium/build.sh` passes on `main` be74fd6 (119 tests, the content
  checks, the page check, and the font check).
- The GM book goes to 271 pages (hardcover count).
- I examined pages 173 and 193 as images. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 8, 2 to 4: 8, 5 to 10: 4, 11 to 16: 6, 17 to 24: 4.
- Types: 7 Monstrosity, 6 Undead, 5 Beast, 1 swarm of beasts, 4 Elemental,
  3 Fey, 1 Construct, 1 Aberration, 1 Dragon, 1 Giant.
- AC: the highest override is 2 above the target (Shellcastle Crab 15 at
  CR 1/2, Rockbreaker Crab 17 at CR 6, Harbor Guardian 17 at CR 7,
  Capewrecker 21 at CR 18, Drowned Titan 21 at CR 21). The HP multiplier is
  1.0 for all.
- Shared traits (Amphibious, Legendary Resistance) use the `M.ref()` loop.

## Strongest entries and the SRD entry that each is equal to

- **Drowned Titan** (CR 21, Gargantuan Giant): 3 chain attacks at 34 (reach
  30 feet, grapple), a 12d10 Thunder Emanation, Control Water and Control
  Weather 1/Day, legendary lightning 6d10. Equal to Ancient Blue Dragon
  (CR 23), a little below.
- **Great Wave** (CR 20, Elemental): 3 crests at 30 that knock Prone, 4d10
  to a creature in its space, a 16d10 line 60 feet wide. Equal to Ancient
  Brass Dragon (CR 20).
- **Capewrecker** (CR 18, Gargantuan crab): 3 attacks up to 35 (claws
  grapple), Rise (12d10 to creatures, double to ships within 60 feet).
  Equal to Dragon Turtle (CR 17) plus 1 for legendary actions.
- **Old Man of the Sea** (CR 17, Fey): 3 strangling attacks at 29 that
  grapple. He climbs onto a grappled creature; the mount moves only where he
  directs and takes half of the damage that he takes. Command of the Rider
  (10d10 Psychic and the mount attacks an ally). Equal to Adult Red Dragon
  (CR 17).
- **Drowned Corsair King** (CR 16, Undead): 3 cutlass attacks at 31, Black
  Spot (10d10 Necrotic and no healing until a Long Rest), rejuvenation that
  ends when its treasure goes back to its owners. Equal to Planetar (CR 16).
- **Salt Dragon** (CR 15): 3 Rends at 24, a 13d8 Necrotic Cone that gives
  Disadvantage on Constitution saves. Equal to Adult Bronze Dragon (CR 15).

## Not sure

1. **Old Man of the Sea, Rider.** The mount shares half of the damage that
   the Old Man takes. This makes the party hurt its own ally. Tell me if
   this is too mean for the table.
2. **Drowned Corsair King, Black Spot.** No healing until a Long Rest on a
   failed save. A strong effect, but a single target and on a recharge.
3. **Tide Horse** (CR 1, Fey): a rider sticks to it and it swims into deep
   water. The drowning risk at CR 1 is the classic water-horse story. The
   escape uses `{dc:str}` (DC 13).
4. **Keeper of the Black Light** (CR 12): Call the Drowned brings up to six
   Wreck Ghouls (CR 2, also in this batch) once each day.

## Next

After approval: `feat: add 30 coast monsters`, then the progress docs
commit. Then batch 8: underdark (14 now). Its draft is ready.
