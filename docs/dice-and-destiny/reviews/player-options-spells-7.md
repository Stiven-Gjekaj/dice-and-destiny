# Review request: player options, spells batch 7

Spells batch 6 is on main (b8922da, docs 935f56d), with all of your
changes: Arc Jump is an action; Wither Limb has a save and a repeat save;
Black Flame ends on an action or a Dexterity save; Body Swap ends at 0 Hit
Points and is never permanent; Tear in the World throws lost creatures
alive onto a random plane and allows Legendary Resistance. In the review
file, "Grasping Vine" (not in the SRD 5.2) is now "Entangle". Spells: 191
of 220.

## The batch

- File: `compendium/content/spells/craft_and_cosmos.py` (not committed).
- Entries: 23 spells. Spells: 191 to 214 of 220.
- Build: `compendium/build.sh` passes. 153 tests pass, the checks are OK.
  Player 270 pages, GM 296. I read page 247. There is no overflow.
- I searched every content file for each new name. "Steal Memory" is a
  level 3 subclass feature (`subclasses/part3.py`) with a similar idea, so
  the spell is now "Memory Theft". The spell works at range with a save,
  and the feature works by touch. Tell me if the overlap is too close.

Themes: craft and repair, the city and the court, the mind, and the sky.

## The gap table after this batch (SRD + original)

| Class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bard | 10+6 | 23+11 | 23+9 | 17+7 | 10+7 | 17+4 | 8+8 | 11+2 | 6+4 | 5+3 |
| Cleric | 7+4 | 15+11 | 17+10 | 19+11 | 9+9 | 13+6 | 11+6 | 8+6 | 5+5 | 5+6 |
| Druid | 11+7 | 18+14 | 21+11 | 13+9 | 18+8 | 15+7 | 10+4 | 6+6 | 8+6 | 4+5 |
| Paladin | 0+1 | 13+10 | 11+10 | 6+8 | 4+9 | 4+7 | - | - | - | - |
| Ranger | 0+3 | 13+11 | 15+9 | 12+7 | 5+7 | 3+6 | - | - | - | - |
| Sorcerer | 16+8 | 21+12 | 27+9 | 21+8 | 13+4 | 12+6 | 11+7 | 8+5 | 6+6 | 5+7 |
| Warlock | 7+4 | 12+11 | 10+11 | 11+7 | 5+10 | 7+6 | 4+8 | 4+4 | 5+6 | 7+5 |
| Wizard | 15+10 | 30+21 | 36+23 | 29+14 | 26+14 | 24+7 | 19+14 | 15+7 | 12+9 | 12+4 |

Original spells now: 214.

## The spells, with the SRD spell that each is equal to

| Level | Spell | Classes | Equal to |
|---|---|---|---|
| 0 | Mote of Starlight | C, D, S, W | Fire Bolt with Faerie Fire (1d8, no Invisible) |
| 1 | Hammerfall | C, P | Inflict Wounds-type melee spell attack (2d8 Force, push) |
| 1 | Tracer Mark | R, B, W | Locate Object / Locate Creature (one marked target) |
| 1 | Thorn Rebuke | D, R | Hellish Rebuke (2d8 Piercing) |
| 1 | Rain Call | D, C | Control Weather, much smaller (ritual) |
| 2 | Phantom Thief | B, K, W | Mage Hand plus Sleight of Hand |
| 2 | Smoldering Blade | S, W, P | Magic Weapon (no bonus, +1d6 Fire) |
| 2 | Borrowed Authority | B, K, W | Enthrall / Friends-type social spell |
| 2 | Shooting Star | S, D, W | Guiding Bolt at level 2 (3d8, Blinded 1 turn) |
| 2 | Swap Places | S, K, W | Misty Step (swap with a creature, save to resist) |
| 3 | Great Mending | W, C, D, S | Fabricate / Mending for structures |
| 3 | Night Terror | B, K, W | Dream (one night, Exhaustion) |
| 4 | Memory Theft | B, K, W | Modify Memory, smaller (take, not change) |
| 4 | Bone Cage | K, W, C | Hold Monster for Restrained (3d8 each turn) |
| 4 | Echoes of the Fallen | W, C, B | Legend Lore for one place (ritual) |
| 5 | Force Box | W, S | Forcecage, smaller (10 ft, save, Concentration) |
| 6 | Rewind | W, S, B | Heal for one hit (Reaction) |
| 6 | Great Dispelling | W, S, C, B | Dispel Magic in an area |
| 6 | Planar Window | W, K, C | Scrying for a place on another plane |
| 7 | Ironskin Host | C, W, D | Stoneskin for 6 creatures (no Concentration, 500 GP) |
| 8 | Spreading Wildfire | D, S, W | Incendiary Cloud (5d10, grows) |
| 8 | Soul Lantern | K, W, C | Magic Jar / Imprisonment for a soul (story) |
| 9 | Second Sun | C, D, S | Sunburst over 1 mile (6d10 to Fiends and Undead each turn) |

## Things that I am not sure of

1. Rewind (level 6): it undoes all the damage of one hit, as a Reaction.
   Against a very large hit (for example a Disintegrate) it is strong. Heal
   (level 6) restores 70 HP.
2. Soul Lantern (level 8): while a soul is in the lantern, the creature
   can't return to life. It is a story spell for villains and for the
   party. It ends if the lantern breaks.
3. Great Dispelling (level 6): it ends all chosen spells of level 5 or
   lower in 30 feet, without a check.

## Next

The feats (65 of 120). The first feat batch is ready: 4 fighting styles,
8 epic boons, and 10 general feats. The last 6 spells come later, from the
gaps in the table (for example Paladin and Ranger cantrips, and Bard
level 7).
