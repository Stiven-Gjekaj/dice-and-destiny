# Review request: NPC batch 4 (the last 10)

## Batch

- File: `compendium/content/npcs/last.py` (new, not committed).
- Entries: 10 NPCs. NPCs go from 90 to 100, the target in the brief.
- After this batch, each of the 10 roles has exactly 10 NPCs.

## Build

- `compendium/build.sh` passes on `main` (205 tests, the content checks, the
  page check, and the font check). I built this batch alone, without the
  mountain batch.
- The GM book part page now says "100 people with full stat blocks".
- I examined page 267 as an image. No text goes out of a box, and the numbers
  are correct.

## Spread

- Roles: Cultists 3, Sailors and Pirates 3, Criminals and Spies 2, Nobles and
  Officials 1, Assassins and Duelists 1.
- CR: 1/8: 1, 1/2: 2, 2: 2, 4: 1, 5: 1, 7: 1, 11: 1, 14: 1.
- CR of all 100 NPCs: every CR from 1/8 to 15 has at least one NPC (I
  checked this with a script). The brief stops at CR 15.
- No name is an SRD name, an original monster, or an earlier NPC. Every spell
  name is in the SRD 5.2. I checked both with a script.
- Each NPC with companions or summons has the line "When you build an
  encounter, count ... as a separate monster" (Voice of the Abyss, Old Duke).
- I lowered the Blackmailer to CR 2 because its threat is social.

## Strongest entries and the SRD entry that each is equal to

- **Voice of the Abyss** (CR 14, Cultist): 2 Necrotic lashes at 33 (range 120
  feet), Word of Ruin (10d8 Psychic and Frightened), Dominate Person, Plane
  Shift, Wall of Fire 1/Day, and Demon Pact (the first time each day it drops
  to 0 HP, an SRD Hezrou appears and the voice regains 30 HP). Equal to
  Archmage (CR 12) plus 2 for the demon.
- **Admiral of the Black Fleet** (CR 11, Sailor): 3 attacks at 15, Parry,
  Broadside (8d10 in a line, only on its ship). Equal to Pirate Captain
  (CR 6) at the level of a CR 11 boss.
- **Old Duke** (CR 7, Noble): 2 sword-cane attacks at 16.5, Command the House
  (four allies move and attack), and a household guard. Equal to Noble (CR 1/8)
  at the level of a CR 7 boss with guards.

## Not sure

1. **Voice of the Abyss, Demon Pact.** A second life that also adds a CR 8
  demon. The Hezrou counts as a separate monster in the encounter budget.
  Tell me if you prefer that the voice only regains HP.
2. **Ship's Surgeon** (CR 2): a Short Rest bonus for allies (an extra 1d8 when
  they spend Hit Point Dice). It is a small benefit for a party that has one
  as an ally.

## Next

After approval: `feat: add 10 NPC stat blocks (batch 4)`, then the progress
docs commit. Then the NPC target is done, and I go on with monster batches:
urban (30 now) and the CR gaps.
