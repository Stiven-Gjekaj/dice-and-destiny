# Review request: player options, spells batch 6

Spells batch 5 is on main (13ad07e, docs 2b78e6e), with all of your
changes: Stolen Verse uses the Counterspell save and lasts to the end of
the bard's next turn; Spell Mirror says single target only, the original
DC and attack, and no area spells; Severance suppresses magic items and
allows Legendary Resistance; Severing Bolt gives Disadvantage on the
Concentration save; Ward of Clear Minds gives Advantage only. Spells: 168
of 220.

## The batch

- File: `compendium/content/spells/beasts_and_shadows.py` (not committed).
- Entries: 23 spells. Spells: 168 to 191 of 220.
- Build: `compendium/build.sh` passes. 153 tests pass, the checks are OK.
  Player 268 pages, GM 278. I read page 248. There is no overflow.
- I searched every content file for each new name. "Strangling Roots" was
  a subclass feature, so that spell is now "Binding Roots".
- I used your notes from batch 5 before I sent this batch: every Reaction
  spell has its trigger in the casting time, and no spell removes a
  creature for good on one failed save.

Themes: beasts, shadows, the edges of the world, and the camp and the road.

## The gap table after this batch (SRD + original)

| Class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bard | 10+6 | 23+10 | 23+7 | 17+6 | 10+5 | 17+4 | 8+6 | 11+2 | 6+4 | 5+3 |
| Cleric | 7+3 | 15+9 | 17+10 | 19+10 | 9+7 | 13+6 | 11+4 | 8+5 | 5+4 | 5+5 |
| Druid | 11+6 | 18+12 | 21+10 | 13+8 | 18+8 | 15+7 | 10+4 | 6+5 | 8+5 | 4+4 |
| Paladin | 0+1 | 13+9 | 11+9 | 6+8 | 4+9 | 4+7 | - | - | - | - |
| Ranger | 0+3 | 13+9 | 15+9 | 12+7 | 5+7 | 3+6 | - | - | - | - |
| Sorcerer | 16+7 | 21+12 | 27+6 | 21+7 | 13+4 | 12+5 | 11+5 | 8+5 | 6+5 | 5+6 |
| Warlock | 7+4 | 12+11 | 10+8 | 11+6 | 5+8 | 7+6 | 4+7 | 4+4 | 5+5 | 7+5 |
| Wizard | 15+9 | 30+20 | 36+18 | 29+12 | 26+11 | 24+6 | 19+11 | 15+6 | 12+7 | 12+4 |

Original spells now: 191.

## The spells, with the SRD spell that each is equal to

| Level | Spell | Classes | Equal to |
|---|---|---|---|
| 1 | Hidden Pocket | W, S, K | Rope Trick for one small object (ritual) |
| 1 | Shared Strength | C, P, D | Healing Word (paid with your own Hit Point Dice) |
| 1 | Sense the Unseen | R, C, W | See Invisibility (location only, 30 ft) |
| 1 | Arc Jump | S, W | Misty Step at level 1 (20 ft, 1d8) |
| 1 | Beacon Fire | C, D, S, W | Continual Flame (8 hours, ritual) |
| 2 | Mimic Voice | B, K, W | Minor Illusion (voice only, 1 hour) |
| 2 | Wither Limb | K, D, W | Ray of Enfeeblement plus 3d8 (melee) |
| 2 | Ward the Threshold | C, P, W | Protection from Evil and Good on a door (ritual) |
| 2 | Light Step | D, R, W | Longstrider / Pass without Trace (terrain only, ritual) |
| 2 | Camp Vigil | C, P, R | Alarm plus no Surprise (ritual) |
| 2 | Clear Eyes | B, C, K, W | See Invisibility (10 ft) plus Advantage against illusions |
| 3 | Bond of the Wild | D, R | Animal Friendship plus beast senses |
| 3 | Spirit Shield | C, P | Shield for an ally (3d8 + mod temp HP) |
| 4 | Black Flame | K, S, W | Fire damage over time (6d6, then 2d6 each turn) |
| 4 | Binding Roots | D, R | Grasping Vine / Hold Monster for Restrained (2d8 each turn) |
| 4 | Oasis | D, C, R | Create or Destroy Water plus a short rest place (ritual) |
| 5 | Body Swap | B, K, W | Magic Jar for willing Humanoids (no spells) |
| 5 | Cleansing Fire | C, P | Flame Strike (6d8 Radiant, enemies only) |
| 6 | Rain of Ash | S, K, W | Incendiary Cloud at level 6 (4d6) |
| 6 | Mindcage | B, K, W | Hold Monster (Incapacitated, not Paralyzed) |
| 7 | Ancestral Host | C, D | Spirit Guardians for weapon attacks (2d6 Radiant) |
| 8 | Drowning Vortex | D, K, W | Tsunami-type water area (6d8, pull) |
| 9 | Tear in the World | S, K, W | Banishment for an area (pull, then lost only after a full minute) |

## Things that I am not sure of

1. Tear in the World (level 9): creatures pulled in come back if the spell
   ends early. They are lost only if the caster keeps Concentration for the
   full minute, like Banishment.
2. Drowning Vortex works only on a body of water. It deals 50 damage to a
   ship each turn, which can sink a small ship in one battle.
3. Shared Strength lets a caster spend their own Hit Point Dice to heal
   others. It does not create healing, so I think level 1 is fair.

## Next

Spells batch 7 is ready (23 spells: craft, the city, the mind, and the
sky). It brings the total to 214. I report the last 6 of the 220 as a
quality limit, unless I find strong ideas for them. Then I start the feats
(65 of 120).
