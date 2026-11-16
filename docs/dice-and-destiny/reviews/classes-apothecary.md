# Review request: the Apothecary class

Workstream: classes and subclasses.

## State

- On `main`: `8e47bfb fix: recommend Epic Boons and backgrounds that are in
  the SRD`, and `feat: add 3 subclasses for the Spiritbinder` (Titan Soul
  keeps only the Resistance; the worn spirit takes half of the damage).
- The class is not committed: `compendium/content/classes/apothecary.py`.
- `build.sh` passes with it (BUILD_OK, fonts OK, no Type 3). The Player's
  Compendium is 240 pages (+4). I looked at pages 176 to 178: the banner,
  the table, the features, and the "Concoctions" list are clean. All the
  characters in the file are ASCII.
- Icon: "scales". The names that I use are in the SRD 5.2 data: Alchemist's
  Supplies, Herbalism Kit, Boon of Fate, and the Sage and Acolyte
  backgrounds.

## The class

Tagline: A healer and chemist who prepares brews, salves, and bombs before
the day begins. Role: Healer and support, with no god and no spell slots.
Difficulty: Medium.

Hit die d8. Primary: Intelligence. Saves: Constitution and Intelligence.
Skills: choose 2 of Insight, Investigation, Medicine, Nature, Perception,
Sleight of Hand, Survival. Weapons: Simple. Tools: Herbalism Kit and
Alchemist's Supplies. Armor: Light. Equipment: (A) Leather Armor, Dagger,
Light Crossbow, 20 Bolts, Herbalism Kit, Alchemist's Supplies, a bandolier
of empty vials, Explorer's Pack, 5 GP; or (B) 110 GP. Subclass levels 3, 6,
10, 14.

Columns: Reagents 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11,
12, 12. Brew Die d6 (1 to 4), d8 (5 to 10), d10 (11 to 16), d12 (17 to 20).
Potency (the number of Brew Dice) 2 (1 to 4), 3 (5 to 10), 4 (11 to 16), 5
(17 to 20).

- 1 Concoctions: at a Long Rest, 1 hour with the tools prepares concoctions
  equal to Reagents. They lose their power at the next Long Rest. Any
  creature can use them. Drinking one, or feeding one to a creature within 5
  feet, is a Bonus Action (as a potion in the 2024 rules). Throwing a bomb
  is the Utilize action, at 30 feet. Save DC 8 + Int + PB.
- 1 Vial Toss: an action, a ranged attack at 30 feet, 1d6 + Int Acid, +1d6
  at 5, 11, and 17 (as a cantrip).
- 1 Field Medic: Expertise in Medicine. Stabilize as a Bonus Action.
- 2 Quick Hands: throw a bomb as a Bonus Action, once each turn.
- 2 Field Brewing: after a Short Rest, prepare 1 concoction (up to the
  normal number).
- 3 Subclass. 4, 8, 12, 16 ASI.
- 5 Long Arm: bombs and Vial Toss at 60 feet. It learns the Quickening
  Draught.
- 7 Inured: Resistance to Acid and Poison, and Advantage on saves against
  Poisoned.
- 9 Restorative (learned). 13 Revival Draught (learned).
- 11 Potent Brews: + Int once to the healing or damage of a concoction.
- 15 Master Batch: Field Brewing prepares 2.
- 17 Panacea: a Healing Tonic can also end Blinded, Deafened, Paralyzed,
  Poisoned, or Stunned.
- 18 Never Without: on Initiative with no concoctions, prepare 1.
- 19 Epic Boon (Boon of Fate recommended).
- 20 Elixir of Life: one extra concoction each Long Rest. It restores all
  HP, ends all conditions except Exhaustion, and gives Resistance to all
  damage for 1 minute.

List "Concoctions" (each with its SRD equal):

- Healing Tonic: Potency dice + Int (Cure Wounds).
- Bracing Draught: Temporary HP equal to Potency dice, and Advantage on the
  next Con save within 1 hour (False Life).
- Antidote: ends Poisoned and one disease, and Advantage against Poisoned
  for 1 hour (Lesser Restoration, in part).
- Fire Bomb (or Acid or Cold): a 10-foot Sphere, Dex save, Potency dice,
  half on a success. At level 1 it is 2d6 (Burning Hands is 3d6). At level
  5 it is 3d8 (Fireball is 8d6).
- Smoke Bomb: a 20-foot Sphere, Heavily Obscured for 1 minute (Fog Cloud).
- Quickening Draught (5): 1 minute, +10 Speed, Dash or Disengage as a Bonus
  Action (Expeditious Retreat, in part).
- Restorative (9): removes 1 Exhaustion level, or ends Charmed, Petrified,
  or a curse (Greater Restoration, in part).
- Revival Draught (13): a creature that died within 1 minute returns with 1
  HP. It costs 2 Reagents and herbs worth 300 GP (Revivify, which costs a
  300 GP diamond).

## Balance against the Cleric

65% to hit; Int +3 at 1, +4 at 5, +5 at 11 and 17; 2 Short Rests a day.

| Level | Healing Tonic | Concoctions each day | Healing each day if all are tonics | Fire Bomb | Vial Toss each round |
|---|---|---|---|---|---|
| 1 | 2d6 + 3 = 10 | 3 | 30 | 7 | 4.2 |
| 5 | 3d8 + 4 = 17.5 | 5 + 2 = 7 | 122 | 13.5 | 7.2 |
| 11 | 4d10 + 10 = 32 | 8 + 2 = 10 | 320 | 27 | 10.1 |
| 17 | 5d12 + 10 = 42.5 | 11 + 4 = 15 | 638 | 37.5 | 12.3 |

The Cleric: level 1 has 2 slots (2 x Cure Wounds 2d8 + 3 = 25). Level 5 has
9 slots, about 150 healing if the Cleric spends every slot on Cure Wounds.
Level 17 has 22 slots, with Heal (70) and Mass Cure Wounds. Vial Toss is
close to Sacred Flame (1d8 to 4d8). The Apothecary has no other spells, so
its healing and its bombs come out of one pool.

## Questions

1. The level 17 total (638 a day if every concoction is a tonic) is high.
   Master Batch (15) is the main cause. I can drop Master Batch and give a
   different level 15 feature (for example, a tonic heals the maximum once
   each Short Rest). Then level 17 is 13 concoctions, 552 a day.
2. Quick Hands lets the Apothecary throw a bomb as a Bonus Action and
   attack with Vial Toss in the same turn. Bombs come from the same daily
   pool, so I think it is fair. It is close to the Sorcerer's Quickened
   Spell, but it costs no extra resource.
3. Concoctions that other creatures use: the party can hold the tonics and
   drink them on their own turns. This is the identity of the class. It
   adds healing in the action economy of the other characters.
4. The planned subclasses: Field Surgeon (more healing), Grenadier (bombs),
   and Hexbrewer (poisons and debuffs).
