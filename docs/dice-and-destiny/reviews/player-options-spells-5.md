# Review request: player options, spells batch 5

Spells batch 4 is on main (bcfb764, docs 7ea442e). Hex of Ruin now doubles
only the first damage of the type on each turn. Chains of Judgment now
targets up to 3 creatures. Spells: 143 of 220.

## The batch

- File: `compendium/content/spells/masks_and_mountains.py` (not committed).
- Entries: 25 spells. Spells: 143 to 168 of 220.
- Build: `compendium/build.sh` passes. 141 tests pass, the checks are OK.
  Player 254 pages, GM 272. I read page 241. There is no overflow.
- I searched every content file for each new name. "Hall of Mirrors" was a
  subclass feature, so that spell is now "Mirror Maze".

Themes: intrigue (illusion, enchantment, divination for courts and
cities), the spirit, the deep earth, and the sea.

## The gap table after this batch (SRD + original)

| Class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bard | 10+6 | 23+10 | 23+5 | 17+6 | 10+5 | 17+3 | 8+5 | 11+2 | 6+4 | 5+3 |
| Cleric | 7+3 | 15+6 | 17+7 | 19+9 | 9+6 | 13+5 | 11+4 | 8+4 | 5+4 | 5+5 |
| Druid | 11+6 | 18+10 | 21+8 | 13+7 | 18+6 | 15+7 | 10+4 | 6+4 | 8+4 | 4+4 |
| Paladin | 0+1 | 13+8 | 11+7 | 6+7 | 4+9 | 4+6 | - | - | - | - |
| Ranger | 0+3 | 13+8 | 15+7 | 12+6 | 5+5 | 3+6 | - | - | - | - |
| Sorcerer | 16+7 | 21+9 | 27+6 | 21+7 | 13+3 | 12+5 | 11+4 | 8+5 | 6+5 | 5+5 |
| Warlock | 7+4 | 12+10 | 10+5 | 11+6 | 5+7 | 7+5 | 4+5 | 4+4 | 5+4 | 7+4 |
| Wizard | 15+9 | 30+16 | 36+13 | 29+12 | 26+10 | 24+5 | 19+9 | 15+6 | 12+6 | 12+3 |

Original spells now: 168.

## The spells, with the SRD spell that each is equal to

| Level | Spell | Classes | Equal to |
|---|---|---|---|
| 0 | Dazzle | B, S, W | Vicious Mockery (1d4 Radiant, Disadvantage) |
| 0 | Seed Burst | D, R | Acid Splash (1d6, 5 ft) |
| 1 | Lucky Coin | B, K, S | Guidance / Bless (one reroll in 1 hour) |
| 1 | Eavesdrop | B, K, W | Clairvoyance at level 1 (hearing, through 1 ft) |
| 1 | Wisp Lure | K, D, W | Command (approach), for several creatures |
| 1 | Last Words | C, K, W | Speak with Dead (one thought, ritual) |
| 1 | Fair Wind | D, S, W | Longstrider for a ship (ritual) |
| 2 | Vine Bridge | D, R | Rope Trick-type utility (ritual) |
| 2 | Borrowed Skill | B, S, W | Enhance Ability (proficiency) |
| 3 | Spirit Walk | K, C, W | Gaseous Form (keeps actions, no attacks) |
| 3 | Hedge of Thorns | D, R | Wall of Thorns at level 3 (smaller, 2d8) |
| 3 | Rumor Mill | B, K | Suggestion for a whole town (story spell) |
| 3 | Ricochet Bolt | S, W | Scorching Ray (4d8 plus 2d8) |
| 3 | Calm the Waves | D, C, S, W | Control Water (calm only, ritual) |
| 4 | Severing Bolt | S, W | Dispel Magic plus 5d8 (ends Concentration only) |
| 4 | Chorus of Spite | B | Vicious Mockery for 4 creatures (3d6) |
| 4 | Ward of Clear Minds | C, P, W | Mind Blank, much smaller (6 creatures) |
| 5 | Volcanic Vent | S, D, W | Flame Strike that moves (5d8, Concentration) |
| 5 | Stolen Verse | B | Counterspell up to level 5, plus a stolen spell up to level 3 |
| 6 | Grove of Renewal | D, C | Heroes' Feast (rest and Hit Point Dice) |
| 6 | Mirror Maze | B, S, W | Hypnotic Pattern / Confusion at level 6 |
| 7 | Earthsplitter | D, S | Earthquake fissure (10d10 Line) |
| 7 | Spell Mirror | S, W | Counterspell plus reflection (level 6 or lower, single target only) |
| 8 | Glimpse of the Void | K, S, W | Sunburst (8d10 Psychic, Incapacitated) |
| 9 | Severance | K, S, W | Feeblemind (no spells or magic items, 24 hours) |

## Things that I am not sure of

1. Stolen Verse (level 5): it stops a spell up to level 5, and if the spell
   was level 3 or lower, the bard can cast it once within a minute. The SRD
   Bard list has no Counterspell, so this fills a gap. The steal is the
   strongest part.
2. Spell Mirror (level 7): it reflects a single-target spell of level 6 or
   lower back at its caster.
3. Severance (level 9): no spells and no magic items for 24 hours, on a
   failed Charisma save. Feeblemind (level 8) stops spells too, and it
   lasts until it is cured.
4. Rumor Mill: a story spell with no combat use. A GM can always say no.

## Next

Spells batch 6 is ready (18 spells: beasts, shadows, and the edges of the
world). After it, about 34 spells remain to reach 220.
