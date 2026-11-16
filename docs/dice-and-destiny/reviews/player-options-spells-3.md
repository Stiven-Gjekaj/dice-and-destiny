# Review request: player options, spells batch 3

Spells batch 2 is on main (b51aac4, docs 89ecd35). Spells: 94 of 220.

## The batch (3 parts, 3 commits)

1. A new check (`compendium/build/check_content.py`, lines added, and 3
   tests): a spell above level 5 can't be on the Paladin or the Ranger
   list. The SRD half casters stop at level 5. The check found one fault.
2. The fix of that fault: Siege of Thorns (level 6, in
   `content/spells/core.py`) was on the Ranger list. It is now Druid only.
3. `compendium/content/spells/roads_and_rites.py`: 25 spells. Spells: 94
   to 119 of 220.

Build: `compendium/build.sh` passes. 122 tests pass, the checks are OK.
Player 250 pages, GM 253. I read pages 236 and 237. There is no overflow.
I searched every content file for each new name. "Riptide" was a subclass
feature, so that spell is now "Breaking Wave".

A large world needs travel magic, so this batch has some travel and
exploration spells (rituals where it makes sense). The other spells fill the
thin lists: Paladin, Ranger, Warlock 4 to 8, and the high levels.

## The gap table after this batch (SRD + original)

| Class | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bard | 10+5 | 23+6 | 23+4 | 17+5 | 10+3 | 17+2 | 8+3 | 11+2 | 6+4 | 5+3 |
| Cleric | 7+3 | 15+4 | 17+6 | 19+5 | 9+4 | 13+4 | 11+2 | 8+4 | 5+4 | 5+4 |
| Druid | 11+4 | 18+7 | 21+6 | 13+3 | 18+5 | 15+6 | 10+2 | 6+3 | 8+3 | 4+4 |
| Paladin | 0+1 | 13+6 | 11+6 | 6+6 | 4+7 | 4+5 | - | - | - | - |
| Ranger | 0+2 | 13+8 | 15+5 | 12+4 | 5+4 | 3+5 | - | - | - | - |
| Sorcerer | 16+4 | 21+6 | 27+4 | 21+4 | 13+2 | 12+3 | 11+2 | 8+2 | 6+3 | 5+3 |
| Warlock | 7+3 | 12+4 | 10+5 | 11+4 | 5+5 | 7+4 | 4+5 | 4+4 | 5+3 | 7+3 |
| Wizard | 15+6 | 30+9 | 36+10 | 29+8 | 26+7 | 24+4 | 19+7 | 15+4 | 12+4 | 12+2 |

Original spells now: 119.

## The spells, with the SRD spell that each is equal to

| Level | Spell | Classes | Equal to |
|---|---|---|---|
| 0 | Sacred Spark | C, B | Guiding Bolt as a cantrip (1d8, +2 to the next attack) |
| 0 | Wayfinder's Mark | B, D, S, W | Message (utility) |
| 1 | Traveler's Hearth | B, D, R, W | Alarm (ritual, camp comfort) |
| 1 | Read the Trail | R, D | Detect Poison and Disease (ritual, information) |
| 1 | Warding Smite | P | Searing Smite (1d6, +2 AC) |
| 1 | Sudden Gale | S, D, W | Thunderwave (2d8, Line, push) |
| 2 | Warden's Mark | P, R | Compelled Duel (2d6 when it hits another) |
| 2 | Cloak of Shade | K, S, W | Blur (only in dim light) plus Darkvision |
| 2 | Parting Brush | D, R, W | Pass without Trace (ritual, plants only) |
| 2 | Word of Waking | C, B, P | Lesser Restoration (3 creatures, Charmed or Frightened only) |
| 3 | Lantern of the Lost | C, B, P, R | Locate Object (water, shelter, road, settlement) |
| 3 | Rally the Fallen | P, C, B | Revivify (1 HP, 3 creatures, no death) plus temp HP |
| 3 | Orbiting Embers | S, K, W | Scorching Ray / Flaming Sphere |
| 4 | Leaden Curse | K, B, W | Slow (one creature) |
| 4 | Unstoppable Charge | P | Staggering Smite (3d8, charge, Prone) |
| 4 | Sanctified Ground | C, P | Aura of Life / Aura of Vitality |
| 5 | Wilderness Road | R, D, B | Wind Walk (lower: double pace, no getting lost) |
| 5 | Grasp of the Drowned | K, D, W | Cloudkill (4d8, half Speed) |
| 5 | Aura of Valor | P | Circle of Power / Bless for all allies (attacks only) |
| 5 | Breaking Wave | S, D, W | Cone of Cold (6d10 Line, push, Prone) |
| 6 | Marionette | B, K, W | Dominate Person (movement and one attack, repeat save) |
| 7 | Dread Monolith | K, C, W | Symbol / Fear (4d10 each turn) |
| 8 | Requiem | B, C, K | Sunburst (12d6 Necrotic) |
| 9 | Rewild the Land | D | Mirage Arcane (permanent, slow) |
| 9 | Encore of Life | B, C | Mass Heal / True Resurrection (6 creatures, died in the last minute) |

## Things that I am not sure of

1. Encore of Life (level 9): up to 6 creatures that died in the last
   minute return with half their HP. It costs 1,000 GP of diamonds.
   Revivify does this for one creature at level 3 with 1 HP. I think that
   level 9 is fair for 6.
2. Marionette (level 6): you move the target and can make it attack, with
   a save each turn. Dominate Person (level 5) gives full control of a
   Humanoid. Marionette works on any creature, so I put it at level 6.
3. Aura of Valor: +1d4 to attack rolls for all allies in 30 ft, with
   Concentration. Bless gives this to 3 creatures at level 1 (plus saves).

## Next

Spells batch 4 is ready (24 spells: weather, the elements, and faith).
