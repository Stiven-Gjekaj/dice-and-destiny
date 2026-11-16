# Review request: bestiary batch 8, underdark monsters

## Batch

- File: `compendium/content/monsters/underdark.py` (new, not committed).
- Entries: 30 monsters from caverns, fungus forests, lightless lakes, and
  the deep roads.
- Underdark goes from 14 to 44 monsters.
- This review is separate from the coast review (batch 7). I built this
  batch alone, without the coast file. If both are approved, I commit coast
  first and build again before each push.

## Build

- `compendium/build.sh` passes on `main` (128 tests, the content checks, the
  page check, and the font check).
- The GM book goes to 273 pages (hardcover count).
- I examined pages 157 and 211 as images. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 8, 2 to 4: 5, 5 to 10: 9, 11 to 16: 5, 17 to 24: 3.
- Types: 5 Monstrosity, 5 Aberration, 4 Plant, 4 Beast, 1 swarm of beasts,
  3 Undead, 2 Dragon, 2 Elemental, 1 Humanoid (Duskling, an existing
  people), 1 Construct, 1 Giant, 1 Fey.
- AC: the highest override is 2 above the target (Jewel Beetle 15 at CR 1/8,
  Prism Sentinel 18 at CR 6, Geode Dragon 20 at CR 15, Stonegullet 20 at
  CR 16). The HP multiplier is 1.0 for all.
- Shared traits (Spider Climb, Sunlight Sensitivity, Legendary Resistance)
  use the `M.ref()` loop.
- None of these names is an underdark name that a publisher owns. I avoided
  the roles of the paid deep peoples and creatures, and I used only SRD
  creatures by name (Zombie in the swamp batch, none here).

## Strongest entries and the SRD entry that each is equal to

- **The Unlit** (CR 23, Gargantuan Aberration): 3 touches at 44 (Necrotic
  plus Psychic, reach 30 feet), Swallow the Light (16d10 Psychic within
  120 feet and Blinded), BPS resistance, all light within 120 feet becomes
  Dim Light. Equal to Ancient Blue Dragon (CR 23).
- **The Deep Heart** (CR 20, Elemental): 3 fists at 36.5, a 3d10 Fire
  touch aura, Heartbeat (10d10 Fire plus 5d10 Bludgeoning within 90 feet).
  Equal to Ancient Brass Dragon (CR 20).
- **Sunless Queen** (CR 18, Fey): 3 blades at 32 (Slashing plus
  Necrotic), Unlight (12d8 Psychic and Blinded in 60 feet), a legendary
  charm that pulls a creature toward her. Equal to Dragon Turtle (CR 17)
  plus 1 for legendary actions.
- **Stonegullet** (CR 16, Gargantuan worm): bite 4d12 + 9 that swallows a
  Large or smaller creature (6d6 each turn, up to two creatures), Tremor
  8d10. The SRD Purple Worm (CR 15) is the model for the swallow. New
  creature, new numbers.
- **Geode Dragon** (CR 15): 3 Rends at 24, a 12d8 Radiant Cone that Blinds,
  Resistance to Bludgeoning and Piercing. Equal to Adult Bronze Dragon
  (CR 15).
- **Deep Oracle** (CR 10, Aberration): 2 Psychic spikes at 27.5, an area
  effect of 8d8 Psychic and Incapacitated (I lowered it from Stunned), a
  Reaction that gives Disadvantage once each round. Equal to Aboleth (CR 10).

## Not sure

1. **Memory Leech** (CR 5): its attack can make a creature forget one
   proficiency of its choice until a Long Rest. The creature chooses which
   one. Tell me if you prefer a simpler effect.
2. **Gloom Ghoul** (CR 3): its claws can Paralyze until the end of the
   target's next turn, the same as an SRD Ghoul (CR 1). Its other traits are
   new (it dims light and climbs ceilings).
3. **The Unlit, Absolute Dark**: magical light of level 5 or lower within
   30 feet goes out. This stops low-level light spells near it.
4. **Inverse Stalker** (CR 5): it lifts grappled creatures 20 feet up. A
   creature that escapes takes falling damage (2d6). That falling damage is
   on top of its 30 damage a round.

## Next

After approval: `feat: add 30 underdark monsters`, then the progress docs
commit. Then batch 9: forest, planar, or mountain (20 to 21 each), or the
first NPC batch with its new format.
