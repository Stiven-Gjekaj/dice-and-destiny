# Review request: player options, spells batch 4

Spells batch 3 is on main (b4a3070 the check, d38e0a4 the fix, bb2533e the
spells, d533c65 the docs). Rally the Fallen now says "has 0 Hit Points and
isn't dead". Spells: 119 of 220.

## The batch

- File: `compendium/content/spells/storm_and_faith.py` (not committed).
- Entries: 24 spells. Spells: 119 to 143 of 220.
- Build: `compendium/build.sh` passes. 131 tests pass, the checks are OK
  (this includes the half-caster check). Player 252 pages, GM 269. I read
  page 234. There is no overflow.
- I searched every content file for each new name. No name is in use.
- My first draft put Apotheosis (level 9) on the Paladin list. The new
  check rule found it before the build. It is now Cleric and Sorcerer.

Themes: weather and the elements, and faith (protection for allies, and
light against Fiends and Undead).

## The gap table after this batch (SRD + original)

| Class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bard | 10+5 | 23+8 | 23+4 | 17+5 | 10+4 | 17+2 | 8+4 | 11+2 | 6+4 | 5+3 |
| Cleric | 7+3 | 15+5 | 17+7 | 19+7 | 9+5 | 13+5 | 11+3 | 8+4 | 5+4 | 5+5 |
| Druid | 11+5 | 18+8 | 21+7 | 13+5 | 18+6 | 15+6 | 10+3 | 6+3 | 8+4 | 4+4 |
| Paladin | 0+1 | 13+8 | 11+7 | 6+7 | 4+8 | 4+6 | - | - | - | - |
| Ranger | 0+2 | 13+8 | 15+6 | 12+5 | 5+5 | 3+6 | - | - | - | - |
| Sorcerer | 16+6 | 21+7 | 27+5 | 21+5 | 13+2 | 12+4 | 11+3 | 8+3 | 6+4 | 5+4 |
| Warlock | 7+4 | 12+6 | 10+5 | 11+4 | 5+7 | 7+5 | 4+5 | 4+4 | 5+3 | 7+3 |
| Wizard | 15+8 | 30+12 | 36+12 | 29+9 | 26+8 | 24+4 | 19+8 | 15+5 | 12+5 | 12+2 |

Original spells now: 143.

## The spells, with the SRD spell that each is equal to

| Level | Spell | Classes | Equal to |
|---|---|---|---|
| 0 | Rime Touch | D, S, W | Chill Touch / Ray of Frost (1d10, no Dash) |
| 0 | Cinder Breath | S, K, W | Thunderclap-type area cantrip (1d6, 15 ft Cone) |
| 1 | Stone Hail | D, S, W | Thunderwave (2d6, 10 ft radius) |
| 1 | Devoted Shield | P, C | Shield for an ally (reduce 1d10 + mod) |
| 1 | Shadow Grasp | K, W | Ray of Sickness (2d6 Necrotic, -10 Speed) |
| 1 | Fanfare | B, P | Bless (attacks only, one attack) |
| 1 | Distant Whisper | K, B, W | Message at 1 mile (ritual) |
| 2 | Sucking Mire | D, R, W | Web (Restrained until the start of its turn) |
| 2 | Static Field | S, W | Spirit Guardians-type aura at level 2 (2d6) |
| 2 | Bastion of Faith | C, P | Shield of Faith plus Resistance to Necrotic |
| 3 | Rime Field | D, S, W | Sleet Storm (3d6 and Prone) |
| 3 | Avenging Light | P, C | Hellish Rebuke for an ally (4d8) |
| 3 | Voice of the River | D, R, C | Speak with Dead / Commune with Nature (smaller) |
| 4 | Hex of Ruin | K, B, W | Bestow Curse at level 4 (Vulnerability, save each turn) |
| 4 | Raven Storm | D, R, K | Insect Plague (smaller, 3d8, moves) |
| 4 | Pillar of Dawn | C, P | Flame Strike (5d8 Radiant, level 4) |
| 5 | Hunter's Shroud | R | Greater Invisibility (self, reveals location on a hit) |
| 5 | Chains of Judgment | P, C | Hold Monster (Fiends and Undead only, area) |
| 5 | Shockwave Leap | S, K | Destructive Wave (6d8 Thunder, with a leap) |
| 6 | Avalanche | D, S, W | Chain Lightning area (10d6, buried) |
| 6 | Hallowed Vigil | C, B | Heroes' Feast / Death Ward for 10 |
| 7 | Unmoored Moment | S, W | Banishment at level 7 (no plane, up to 3 rounds) |
| 8 | Eternal Winter | D, S, W | Incendiary Cloud (6d8 Cold, larger) |
| 9 | Apotheosis | C, S | Holy Aura plus Fly (self avatar) |

## Things that I am not sure of

1. Hex of Ruin (level 4): Vulnerability to one damage type, with a save at
   the end of each turn. It can double the damage of a party that uses the
   same type. I put it at level 4 for this reason.
2. Chains of Judgment (level 5): Paralyzed for Fiends and Undead in 30 ft,
   with a save each turn. Hold Monster paralyzes any one creature. In a
   crypt or a hell this spell is very strong.
3. Apotheosis (level 9): Resistance to all damage, a Fly Speed, +4d8 once
   each turn, and 10 HP for each ally each turn, for 1 minute with
   Concentration. I compare it with Holy Aura plus Mass Heal over time.

## Next

Spells batch 5 is ready (25 spells: intrigue, the spirit, the deep earth,
and the sea).
