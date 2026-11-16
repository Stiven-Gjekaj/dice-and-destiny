# Review request: NPC batch 3

## Batch

- Files: `compendium/content/npcs/realm.py` (18) and
  `compendium/content/npcs/far.py` (12). New, not committed.
- Entries: 30 NPCs. NPCs go from 60 to 90.
- After this batch, each role has 7 to 10 NPCs: Guards 10, Merchants 10,
  Priests 10, Scholars 10, Wilderness 10, Nobles 9, Assassins 9,
  Criminals 8, Cultists 7, Sailors 7.

## Build

- `compendium/build.sh` passes on `main` (177 tests, the content checks, the
  page check, and the font check). I built this batch alone, without the
  planar batch.
- The content check found one error in my first build: the Templar of the Sun
  had AC 20, above the limit of 19 for CR 7. I lowered it to 19. The AC and
  HP limits for NPCs work as planned.
- The GM book part page now says "90 people with full stat blocks".
- I examined page 262 as an image. No text goes out of a box, and the numbers
  are correct.

## Spread

- CR: 1/8: 2, 1/4: 1, 1/2: 2, 1: 6, 2: 3, 3: 2, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2,
  9: 2, 10: 1, 12: 1, 13: 1, 15: 1.
- No name is an SRD name, an original monster, or an earlier NPC. Every spell
  name is in the SRD 5.2. I checked both with a script. (It found "Toll the
  Dead", "Friends", and "Shape Water", which are not in the SRD 5.2. I
  replaced them with Sacred Flame, Suggestion, and Druidcraft.)
- I lowered the CR of five NPCs whose threat is social, not damage: Royal
  Steward (1/4), Moneylender (1/8), Apothecary (1/2), Ambassador (1), and Con
  Artist (1).
- Each NPC with a companion or servants has the line "When you build an
  encounter, count ... as a separate monster" (Queen Regent, Merchant Prince,
  Flesh Sculptor, Clockwork Tinker, Shepherd).
- The Clan Chieftain uses the new thrown kind for its throwing axes.

## Strongest entries and the SRD entry that each is equal to

- **Living Saint** (CR 15): 2 Radiant rays at 33 (range 120 feet), Holy Aura
  (Advantage on saves for allies within 30 feet), Miracle (10d10 Radiant to
  Fiends and Undead, half and Blinded to other enemies, 4d10 healing to
  allies), Heal, Mass Cure Wounds, Raise Dead 1/Day. Equal to Archpriest
  (CR 12) plus 3 for its aura and Miracle.
- **Chronomancer** (CR 13): 2 Force lances at 27.5, Haste and Slow 2/Day,
  Counterspell and Time Stop 1/Day, Rewind (1/Day: no damage from one hit,
  and it moves back). Equal to Archmage (CR 12) plus 1.
- **Vessel of the Hidden God** (CR 12): 2 attacks at 31, BPS resistance, an
  area effect of 8d10 Psychic that Stuns until the end of the next turn.
  Equal to a CR 12 boss (Archpriest).
- **Blade Dancer** (CR 10): 4 attacks at 13, no Opportunity Attacks against
  it, Riposte and Parry. Equal to Gladiator (CR 5) plus 5.

## Not sure

1. **Time Stop** on the Chronomancer (CR 13, 1/Day). It is a level 9 spell.
   The 2024 Archmage (CR 12) has strong spells of the same kind. Tell me if
   you prefer a level 7 spell.
2. **Vessel of the Hidden God**: its area effect Stuns. I lowered similar
   area effects to Incapacitated in the monster batches. It is a CR 12 boss
   on a recharge, so I kept Stunned. Tell me if you want Incapacitated.
3. **Siege Captain** (CR 8): Fire the Engines (6d10 in a 20-foot Sphere)
   works only if it has siege engines and crews. Without them, it is a
   weaker CR 8.

## Next

After approval: `feat: add 30 NPC stat blocks (batch 3)`, then the progress
docs commit. Then the next monster batch (mountain, 21 now). The last NPC
batch (10 NPCs, to reach 100) comes after it.
