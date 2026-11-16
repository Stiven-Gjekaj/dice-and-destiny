# Review request: bestiary batch 6, swamp monsters

## Batch

- File: `compendium/content/monsters/swamp.py` (new, not committed).
- Entries: 30 monsters from fens, bogs, mangroves, and drowned temples.
- Swamp goes from 14 to 44 monsters.
- The batch adds high CRs, because swamp had no monster above CR 9.

## Build

- `compendium/build.sh` passes on `main` 555f409 (81 tests, the content
  checks, the page check, and the font check).
- The GM book goes from 239 to 247 pages.
- I examined pages 182 and 209 as images. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 6, 2 to 4: 5, 5 to 10: 9, 11 to 16: 7, 17 to 24: 3.
- Types: 4 Beast, 2 swarms of beasts, 1 swarm of undead, 4 Monstrosity,
  3 Undead, 4 Plant, 3 Fey, 2 Aberration, 2 Construct, 2 Dragon,
  1 Elemental, 1 Fiend, 1 Humanoid (Reedfolk, an existing people).
- AC: the highest override is 2 above the target (Idol of the Sunken Temple,
  19 at CR 10). The HP multiplier is 1.0 for all.
- Shared traits (Amphibious, Legendary Resistance) use the `M.ref()` loop.

## Strongest entries and the SRD entry that each is equal to

- **The Drowned God** (CR 22, Gargantuan Aberration): 3 tentacles at 43
  (4d10 + 8 plus 3d8 Psychic) that grapple, The Flood recharge (16d10 in a
  60-foot Emanation, can't breathe, pulled 30 feet), 4 Legendary Resistance.
  Equal to Ancient Green Dragon (CR 22). Its trait "Dreams of Water" stops a
  Long Rest within 10 miles unless a creature succeeds on a Wisdom save.
- **Bog Behemoth** (CR 19): 3 attacks up to 105, a 12d10 Thunder Cone.
  Equal to Ancient Brass Dragon (CR 20), a little below.
- **Rot Mother** (CR 18, Plant): 3 attacks at 33.5 that grapple,
  Regeneration 20 (Fire stops it), a 14d8 Acid Emanation. Equal to Dragon
  Turtle (CR 17) plus 1 for regeneration and legendary actions.
- **Lord of Fevers** (CR 16, Fiend): 2 claws at 35, a fever aura (Con save
  or 1 Exhaustion level, at most 2 levels until a Long Rest, the same cap as
  the Thirst Wraith), a 12d8 Poison Cone, Contagion and Insect Plague 1/Day.
  Equal to Planetar (CR 16).
- **Queen of the Drowned Lanterns** (CR 15, Fey): 2 lashes at 27 (Lightning),
  False Path (10d8 Psychic and a charm that leads to deep water), 1d4
  Will-o'-the-Wakes. Equal to Mummy Lord (CR 15).
- **Moss Dragon** (CR 14): 3 Rends at 24, a 12d8 Poison Cone that
  Incapacitates. Equal to Adult Green Dragon (CR 15), a little below.
- **Thousand-Year Crocodile** (CR 13, Gargantuan Beast): bite 4d10 + 8 that
  grapples, Death Roll 6d10 on a grappled creature. A larger Giant
  Crocodile (CR 5), at the level of an Adult Brass Dragon (CR 13).

## Not sure

1. **The Drowned God, Dreams of Water.** No Long Rest within 10 miles
   without a save. It is a campaign pressure, not a combat effect. Tell me if
   it is too strong, or if 1 mile is better.
2. **Rot Mother.** Regeneration 20 each turn and a legendary action that
   heals 4d10. The SRD Troll pattern (Fire stops it).
3. **Leech Mother** (CR 7): when she first drops to 0 HP, she becomes a
   Swarm of Bloodleeches (CR 2, also in this batch) at full HP and flees. It
   is a second life, but a weak one.
4. **Bloated Toad King** (CR 5): swallows a Medium or smaller creature
   (3d6 Acid each turn, spits it out at 20 damage). The SRD swallow pattern.
5. **Idol of the Sunken Temple** (CR 10): it can't leave its temple, so its
   AC 19 and BPS resistance matter only there.

## Next

After approval: `feat: add 30 swamp monsters`, then the progress docs
commit. Then batch 7: coast or underdark (14 each).
