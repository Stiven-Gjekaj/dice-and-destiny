# Review request: player options, magic items batch 3 (Legend paths)

Magic items batch 2 is on main (30ae263, docs 8dda536), with your changes:
Shroud of the Second Death doesn't work on a death outright or in the same
turn as Relentless Endurance or Second Death; the Fireproof Wax Coat says
that Resistance and Vulnerability cancel out.

## The batch

- File: `compendium/content/items/options_legends.py` (not committed).
- Entries: 24 magic items, 2 for each of the 12 Legend paths in
  `content/systems/legends.py` (a28baf9). Player options items: 73 to 97.
- Build: `compendium/build.sh` passes. 212 tests pass, the checks are OK.
  Player 278 pages, GM 402. I read GM page 297. No overflow.
- I searched every content file and the SRD magic items for each name.
  "Hourglass of Borrowed Time" was in use, so that item is now "Sand of the
  Last Breath". Every spell that an item names is in the SRD data.

The same pattern as the heritage items: anyone can use each item, and a
creature on the named path gets a small extra benefit. Each path gets one
smaller item (Common to Uncommon, or Rare) and one stronger item.

| Path | Item | Rarity | Attunement | Equal to |
|---|---|---|---|---|
| Dragonslayer | Scale-Tooth Charm | Uncommon | no | Advantage against fear of Dragons |
| Dragonslayer | Wyrmbane Spear | Very Rare | yes | Dragon Slayer weapon at +2 (2d10, not 3d6) |
| Saint | Pilgrim's Candle | Common | no | a small trick |
| Saint | Halo of the Humble | Rare | yes | Cure Wounds-type healing 1/day (2/day on the path) |
| Tyrant | Iron Crown of Obedience | Rare | yes | Command 1/day, Advantage on Intimidation |
| Tyrant | Chain of Fealty | Very Rare | yes | track 3 sworn vassals, Disadvantage on their saves against you |
| Wanderer | Road-Worn Boots | Uncommon | no | a travel item (10 hours a day) |
| Wanderer | Map of Every Road | Very Rare | no | Find the Path; Teleport once in 7 days on the path |
| Spellbreaker | Nullstone Amulet | Uncommon | yes | Mantle of Spell Resistance, levels 1 and 2 only |
| Spellbreaker | Gauntlet of Unweaving | Very Rare | yes | Counterspell 1/day |
| Liberator | Broken Shackle | Uncommon | no | Knock 1/day, Advantage to escape |
| Liberator | Banner of the Free | Very Rare | yes | an aura against Charmed and Frightened for 1 minute, 1/day |
| Lorekeeper | Quill of Remembering | Common | no | a small trick |
| Lorekeeper | Atlas of Forgotten Kingdoms | Rare | no | a history book; Legend Lore 1/day on the path |
| Warden of the Wild | Acorn of the Old Grove | Common | no | a small trick |
| Warden of the Wild | Antler Crown of the Warden | Very Rare | yes | Speak with Animals and Plants at will, Commune with Nature 1/day |
| Shadow | Smoke Pellets of the Quiet Way | Uncommon | no | Fog Cloud-type smoke, 5 pellets |
| Shadow | Mask Without a Face | Rare | yes | Nondetection-type for the face, Pass without Trace on the path |
| Peacemaker | White Ribbon of Parley | Common | no | a small trick |
| Peacemaker | Olive Staff of Calm | Rare | yes | Staff with Calm Emotions and Sanctuary (5 charges) |
| Deathless | Sand of the Last Breath | Rare | yes | one Death Saving Throw success each day |
| Deathless | Phylactery of the Unbowed | Legendary | yes | return from death at the next dawn, once in 7 days |
| Founder | Cornerstone of the First Hall | Rare | no | a building item (half the time, weatherproof) |
| Founder | Charter of the Free Town | Very Rare | yes | Guards and Wards 1/day in your settlement |

## Things that I am not sure of

1. Phylactery of the Unbowed (Legendary): return from death once in 7 days.
   The Deathless path already has a similar Tier IV and V benefit. The
   item does not stack with them in a useful way: a character who has both
   still dies only once. I think that Legendary is right.
2. Chain of Fealty is a Tyrant item that works on willing vassals. A
   forced oath allows a Wisdom save. It needs a talk at the table, like the
   Tyrant path itself.
3. Wyrmbane Spear deals 2d10 extra to Dragons at Very Rare. The SRD Dragon
   Slayer (Rare) deals 3d6 extra at +3. Mine is +2 with 2d10, plus a throw
   on the path.

## Next

The player options work in my brief is complete: species 20, backgrounds
40, feats 120, spells 220, and 97 player options magic items.
