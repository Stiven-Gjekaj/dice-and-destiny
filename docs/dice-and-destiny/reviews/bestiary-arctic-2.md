# Review request: bestiary batch 13, arctic monsters (second set)

## Batch

- File: `compendium/content/monsters/arctic_2.py` (new, not committed).
- Entries: 20 monsters from the ice sea, the lands of the snow giants, and
  the court of winter.
- Arctic goes from 35 to 55 monsters. Arctic was thin at CR 11 to 16 (6) and
  at CR 17 or more (2). This batch adds 7 and 4.
- With this batch, the bestiary has 594 monsters (by my count of all files,
  with the helper files).

## Build

- `compendium/build.sh` passes on `main` 5fe4644 (232 tests, the content
  checks, the page check, and the font check). GM book: 463 pages
  (hardcover count, with the work of other sessions).
- After the build, I removed one AC override (see "Spread"). The tests and
  the content check pass after that change. I run the full build again
  before the commit.
- I examined page 299 as an image. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 2, 2 to 4: 3, 5 to 10: 4, 11 to 16: 7, 17 to 24: 4.
- Types: 5 Beast, 5 Monstrosity, 3 Dragon, 2 Undead, 2 Giant, 2 Elemental,
  1 Fey.
- AC: the highest override is 2 above the target (White Wyrm of the Pole,
  21 at CR 20). A monster with Resistance to Bludgeoning, Piercing, and
  Slashing has no AC above the target. I removed the override of the Winter
  King (AC 21 to the target 20) for this rule.
- The Snow Giant Seer and the Rime Titan use the thrown kind.
- Two links to the first arctic set: the Winter King is the lord whom the
  Midwinter Queen serves, and the White Wyrm of the Pole is the parent of the
  glacier dragons in this set.

## Strongest entries and the SRD entry that each is equal to

- **Walking Glacier** (CR 22, Gargantuan Elemental): 3 attacks at 36.5
  (reach 30 feet, push 15 feet), 4d10 to a creature in its space, Calve
  (16d10 within 90 feet and Prone), BPS resistance, Fire vulnerability.
  Equal to Ancient Green Dragon (CR 22).
- **Winter King** (CR 21, Fey): 3 sword attacks at 41, BPS resistance,
  Frozen Court (14d10 Cold within 60 feet and Restrained), Control Weather,
  Dominate Monster, Wall of Ice 1/Day. Equal to Lich (CR 21).
- **White Wyrm of the Pole** (CR 20): 3 Rends at 33.5, a 16d10 Cold Cone that
  Restrains. Equal to Ancient Brass Dragon (CR 20).
- **Wolf Who Eats the Sun** (CR 18): 3 attacks up to 30, BPS resistance,
  light within 60 feet becomes Dim Light, a 12d10 Cold howl that Frightens.
  Equal to Dragon Turtle (CR 17) plus 1 for legendary actions.
- **Glacier Dragon** (CR 16): 3 Rends at 25, a 13d8 Cold Cone that sets Speed
  to 0. Equal to Adult Blue Dragon (CR 16).

## Not sure

1. **Spirit of the Long Night** (CR 14): its aura gives 1 Exhaustion level
  each turn to a creature without a light source, up to 2 levels until a
  Long Rest. This uses the same cap as the Thirst Wraith and the Thirst
  Demon. A torch protects a creature.
2. **Frost Hydra** (CR 11): five heads and the head rule of the SRD Hydra,
  with Fire as the counter. The Sewer Hydra was in my unused urban draft, so
  this is the only hydra of mine in the book.
3. **Under-Ice Kraken** (CR 12): its Bonus Action pulls grappled creatures
  through the ice into freezing water. A GM must handle the cold water (the
  extreme cold rules of the SRD).

## Next

After approval: `feat: add 20 arctic monsters (second set)`, then the
progress docs commit. Then the bestiary workstream keeps no more groups.
Grassland, hill, swamp, and coast are open for the helpers. If they do not
take them, I can write the last groups. Tell me which you prefer.
