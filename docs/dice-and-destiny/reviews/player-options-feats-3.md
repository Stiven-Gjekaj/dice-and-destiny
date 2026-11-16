# Review request: player options, feats batch 3

Feats batch 2 is on main (59217c6, docs 4985d14), with all of your
changes: Boon of the Phoenix works at 0 Hit Points or on a killing blow,
not against Power Word Kill or dust; Beast Bond does not grow and returns
after a Long Rest; Spell Echo spends your own slot before the end of your
next turn; Boon of the Quarry is chosen at a Long Rest; Phalanx Style
needs you to be within 5 feet and not Incapacitated. The review file now
names Boon of Recovery. Feats: 87 of 120.

## The batch

- File: `compendium/content/feats/peoples.py` (not committed).
- Entries: 27 feats (20 species feats and 5 other General feats, all
  General; 2 Origin feats). Feats: 87 to 114 of 120.
- I searched every content file for each name. Three names were in use, so
  I changed them: "Tidal Strength" (a monster trait) is now "Deepwater
  Strength", and "Heart of Winter" (a subclass feature) is now "Frozen
  Heart". I dropped "Tunnel Fighter", because a subclass feature has the
  same name and almost the same idea.

## Species feats

Each original species gets one feat (prerequisite: level 4 and that
species). Each feat makes the species' main trait stronger or adds a use,
plus +1 to an ability score. The model is a General feat that improves one
feature, at the power of Grappler or a +1 feat.

| Species | Feat | Benefit |
|---|---|---|
| Lumen | Starborn Radiance | Star Flare 2/LR, its light is sunlight |
| Hollowborn | Deathless Vigor | Second Death leaves 2 x PB HP, Advantage against max HP loss |
| Brinewrought | Deepwater Strength | Swim +10, Undertow pulls 15 ft and knocks Prone in water |
| Kilnborn | Living Forge | Kiln Flare +1d6, heat metal by touch |
| Sporekin | Deep Colony | two-way telepathy 60 ft, Spore Burst also stops Reactions |
| Glassborn | Prism Skin | Mirage miss blinds the attacker for its turn, Radiant Resistance |
| Windkin | Sky Hunter | Updraft PB/LR, Advantage on sight Perception while flying |
| Hoarfolk | Frozen Heart | Breath of Winter deals 1d6 + PB Cold, no Exhaustion from cold |
| Oathborn | Sworn Witness | Witness 2/LR, Zone of Truth 1/LR |
| Rootkin | Ancient Bark | unarmored AC 13 + Con (Shield allowed), roots slow Large creatures too |
| Peatborn | Bog Body | Poison Resistance, Bog Grasp also Restrains for a turn |
| Rillfolk | Current Rider | Slip Away moves full Speed, Advantage on Dex saves in water |
| Sunrunner | Endless Stride | Speed +5, Windrun gives PB temp HP |
| Hushfolk | Silent Hunter | Blindsight 30 ft, Hush 2/LR |
| Dreamborn | Lucid Dreamer | Fade lasts to the end of your next turn, Dream Message can be answered |
| Gloamkin | Shadow Kin | Shadow Step 60 ft, Advantage on the next attack |
| Cairnborn | Unmoving Stone | while Standing Stone is active: can't be moved or knocked Prone, Advantage on Str saves |
| Foldfolk | Fireproofed Pages | no Fire Vulnerability, Fold Flat as a Bonus Action |
| Feverblooded | Plague Ward | Draw the Fever heals 2 x PB, Advantage against Poisoned |
| Relicborn | Imperial Blood | one more attunement slot, learn an item's properties in 1 minute |

## Other feats

| Type | Feat | Benefit | Equal to |
|---|---|---|---|
| General | Spirit Speaker | see the Ethereal Plane within 30 ft, talk to spirits, Speak with Dead 1/LR | Skilled-type utility plus +1 |
| General | Master Artisan | Expertise with one Artisan's Tools, craft in half the time | Skilled-type utility plus +1 |
| General | Silent Casting | cast without V and S components, PB/LR | Grappler-level (a small part of Subtle Spell) |
| General | Disarmer | once per turn on a hit, a Str save or drop an object | Grappler-level |
| General | Familiar Bond | Find Familiar at will, the familiar adds PB and gains HP | Magic Initiate-type |
| Origin | Gambler's Luck | Gaming Set, reroll one failed ability check 1/LR | Origin (small) |
| Origin | Bloodhound Nose | Advantage on smell checks, smell poison, know people by scent | Origin (small) |

## Things that I am not sure of

1. Imperial Blood gives a fourth attunement slot. That is a strong
   benefit for a General feat, but it costs a feat, and the Relicborn has
   no combat traits.
2. Fireproofed Pages removes the Foldfolk's Fire Vulnerability. You told me
   to keep that cost for the species, so the feat is the only way to remove
   it, and it costs a feat at level 4.
3. Ancient Bark: unarmored AC 13 + Con. It is like a Barbarian's
   Unarmored Defense without Dexterity, with a Shield allowed.

## Build

`compendium/build.sh` passes: 166 tests, the checks are OK. Player 272
pages (the feats filled free space at the end of the chapter, so the page
count did not change), GM 313. I read pages 228 and 229 and searched the
PDF text: all 27 feats are in the book, and there is no overflow.

## Next

The last 6 spells and the last 6 feats, from gaps (Paladin and Ranger
cantrips, Bard level 7, and feats for the new classes and the optional
systems), when the other items are done.
