# Review request: bestiary batch 11, mountain monsters

## Batch

- File: `compendium/content/monsters/mountain.py` (new, not committed).
- Entries: 30 monsters from high passes, cliffs, volcanoes, and the halls
  under the peaks.
- Mountain goes from 21 to 51 monsters. Mountain had only 4 monsters at CR 5
  to 10 and 1 at CR 17 or more. This batch adds 9 and 4.

## Build

- `compendium/build.sh` passes on `main` da7c44d (180 tests, the content
  checks, the page check, and the font check).
- The GM book goes to 382 pages (hardcover count, with the work of other
  sessions).
- I examined page 231 as an image. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 6, 2 to 4: 6, 5 to 10: 9, 11 to 16: 5, 17 to 24: 4.
- Types: 8 Monstrosity, 5 Elemental, 4 Beast, 1 swarm of beasts,
  3 Construct, 3 Undead, 2 Fey, 2 Dragon, 2 Giant.
- AC: the highest override is 2 above the target. The HP multiplier is 1.0
  for all.
- Three monsters use the new thrown kind: Crag Ape, Cliff Giant, and
  Sky-Shouldering Titan.
- The adult **Thunder Roc** (CR 18) goes with the existing Thunder Roc Chick
  (CR 1) of the first bestiary.

## Strongest entries and the SRD entry that each is equal to

- **Magma Leviathan** (CR 21, Gargantuan Elemental): 3 bites at 47 (Piercing
  plus Fire), a 3d10 Fire touch aura, Rain of Fire (16d10 in a 40-foot
  Sphere at 300 feet). Equal to Ancient Blue Dragon (CR 23), a little below.
- **Sky-Shouldering Titan** (CR 20, Giant): 3 attacks up to 43 (a thrown
  mountain stone at 120/480 feet), Let the Sky Fall (14d10 within 90
  feet). While it holds the sky, its Speed is 0 and it has Advantage on all
  saving throws. Equal to Ancient Brass Dragon (CR 20).
- **Anvil Colossus** (CR 19, Construct): 2 hammers at 44, a 3d8 Fire touch
  aura, BPS resistance, Forge Blast (16d10 Fire in a 60-foot Cone). Equal to
  Balor (CR 19).
- **Thunder Roc** (CR 18): 3 attacks at 25.5, a 2d10 Lightning aura while it
  flies, Thunderclap (12d10 within 60 feet). Equal to Dragon Turtle (CR 17)
  plus 1 for legendary actions.
- **Granite Dragon** (CR 16): 3 Rends at 26, BPS resistance, a 12d8 Cone that
  Restrains until the end of the next turn. Equal to Adult Blue Dragon
  (CR 16).

## Not sure

1. **Granite Dragon, BPS resistance at CR 16.** A stone dragon with
  resistance to all weapon damage is strong. Its AC is 20 (+2). Tell me if
  you want only Resistance to Piercing.
2. **Avalanche Wraith and Avalanche Titan**: "buried" means Restrained and
  can't breathe until a creature uses an action to dig it out. Both are
  limited (1/Day and a recharge).
3. **Basalt Golem**: Fire damage heals it (half) and adds 2d6 Fire to its
  next attack, the same idea as the SRD golem absorption traits.

## A note on the People of the World text

You changed my line in the People of the World introduction to "in Monsters
A–Z". Chapter "Original Bestiary" also has a section named "Monsters A–Z"
(an `h2`), so a reader could look there. A clearer text: "in the SRD
bestiary (the chapter Monsters A–Z)". Tell me if I should change it, or
if you prefer to.

## Next

After approval: `feat: add 30 mountain monsters`, then the progress docs
commit. NPC batch 4 (the last 10 NPCs) has its own review request.
