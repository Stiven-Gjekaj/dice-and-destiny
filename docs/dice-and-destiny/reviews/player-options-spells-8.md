# Review request: player options, spells batch 8 (the last 6)

Feats batch 3 is on main (2e585fb, docs e536c44), with your changes:
Imperial Blood doesn't stack with other extra attunement; Ancient Bark
doesn't combine with other ways to calculate AC; Disarmer uses 8 +
Strength modifier + Proficiency Bonus, and a two-handed grip gives
Advantage. Feats: 114 of 120.

## The batch

- File: `compendium/content/spells/last_gaps.py` (not committed).
- Entries: 6 spells. Spells: 214 to 220 of 220.
- Build: `compendium/build.sh` passes (with feats batch 4 and the counts
  change in the same tree). 169 tests pass, the checks are OK. Player 274
  pages, GM 320. I searched the PDF text: all the new spells are in the
  book.
- I searched every content file for each name. No name is in use.

Each spell fills a gap from the table that you named.

| Level | Spell | Classes | Gap | Equal to |
|---|---|---|---|---|
| 0 | Warden's Call | P, R, C, D | Paladin and Ranger cantrips (through a Fighting Style that grants cantrips) | Vicious Mockery (no damage, a taunt for one turn) |
| 0 | Snapping Vine | R, D, W | Ranger cantrips | Ray of Frost (1d8 Piercing, -10 Speed) |
| 6 | Shadow Road | K, W | Warlock 6 | Teleport, smaller (500 miles, only into shadow, no mishap) |
| 7 | Heroic Anthem | B | Bard 7 | Bless at level 7 (6 creatures, 1d6, Immunity to Frightened) |
| 7 | Living Forest | D | Druid 7 | Wall of Thorns / Entangle in a large area |
| 8 | Masterwork Illusion | B, W | Bard 8 | Mirage Arcane / Programmed Illusion (permanent, 1,000 GP) |

## Things that I am not sure of

1. Shadow Road (level 6) has no mishap, but it needs shadow at both ends
   and reaches only 500 miles. Teleport (level 7) has a mishap table and
   no distance limit on the same plane.
2. Heroic Anthem gives 1d6 to attacks and saves for 6 creatures. Bless at
   level 7 gives 1d4 to 9 creatures.
