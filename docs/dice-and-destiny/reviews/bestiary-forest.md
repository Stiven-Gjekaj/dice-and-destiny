# Review request: bestiary batch 9, forest monsters

## Batch

- File: `compendium/content/monsters/forest.py` (new, not committed).
- Entries: 30 monsters from old woods, fey glades, hunting grounds, and
  haunted groves.
- Forest goes from 20 to 50 monsters. Forest had few monsters at CR 5 to 16
  (4 in all). This batch adds 17 there.

## Build

- `compendium/build.sh` passes on `main` 9a8f7f3 (166 tests, the content
  checks, the page check, and the font check).
- The GM book goes to 319 pages (hardcover count).
- I examined pages 184 and 232 as images. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 5, 2 to 4: 5, 5 to 10: 10, 11 to 16: 7, 17 to 24: 3.
- Types: 8 Fey, 6 Plant, 5 Beast, 1 swarm of beasts, 2 Undead, 2 Dragon,
  2 Monstrosity, 2 Celestial, 1 Construct, 1 Giant.
- AC: the highest override is 2 above the target (Thornback Hedgehog 14 at
  CR 0, Oak King 19 at CR 12). The HP multiplier is 1.0 for all.
- Shared traits (False Appearance as a tree, Legendary Resistance) use the
  `M.ref()` loop.
- The Wildwood Giant's Rock uses the thrown-attack workaround (an action with
  `{atk:str}`), as you approved for the hill giants. This is the third
  monster with it. Tell me if I should now add the thrown kind ("t") to the
  engine in its own commit.

## Strongest entries and the SRD entry that each is equal to

- **The Wakened Wood** (CR 22, Gargantuan Plant): 3 root attacks at 36.5
  (reach 30 feet, grapple), Regeneration 20 (Fire stops it), Close In
  (14d10 within 60 feet, Restrained). Equal to Ancient Green Dragon (CR 22).
- **Wolfmother of the World** (CR 19, Fey): 3 attacks up to 31 (bite knocks
  Prone), a 10d10 Psychic howl that Frightens, Call the Pack (2d6 Dire Wolves
  1/Day). Equal to Balor (CR 19). The wolves add danger; the GM can skip
  them.
- **Eternal White Stag** (CR 17, Celestial): 3 attacks up to 36, BPS
  resistance, can't be Grappled or Restrained, a 12d8 Radiant burst, a
  legendary heal of 4d10 for an ally. Equal to Adult Red Dragon (CR 17).
- **Gallows King** (CR 16, Undead): 2 noose attacks at 35 that grapple and
  stop breathing, Final Verdict (12d10, a creature that dies rises as a
  Zombie), raises up to four Zombies as a Bonus Action. Equal to Planetar
  (CR 16).
- **Amber Dragon** (CR 15): 3 Rends at 24, a 12d8 Acid Cone that Restrains,
  a legendary action that crushes Restrained creatures (3d10). Equal to
  Adult Bronze Dragon (CR 15).
- **Holly King** (CR 14) and **Oak King** (CR 12): a pair of fey kings. Each
  has Advantage on attacks in his half of the year and sleeps in the other
  half. Holly King: 3 spears at 29 (Cold). Oak King: 3 clubs at 22.5. Equal
  to Adult Bronze Dragon (CR 15) and Storm Giant (CR 13), a little below.

## Not sure

1. **Oak King and Holly King, half-year sleep.** A GM can meet only one of
   them at a time, unless the fight is at midsummer or midwinter. That is the
   story hook, but it makes them harder to use.
2. **Gallows King, Hanging Wood.** Up to four Zombies as a Bonus Action, with
   no limit on uses. The number of bodies on the trees is the limit. Tell me
   if you want "(1/Day)".
3. **Wandering Cottage** (CR 5): a house on bird legs that can lock a creature
   inside. The idea is old folklore (public domain). I gave it new rules and
   no name from any book.
4. **Briar Wolf** (CR 7): Regeneration 10 (Fire stops it) and a thorn aura.

## Next

After approval: `feat: add 30 forest monsters`, then the progress docs
commit. Then NPC batch 2 (ready: 30 NPCs that fill the Wilderness, Scholars,
and Assassins roles).
