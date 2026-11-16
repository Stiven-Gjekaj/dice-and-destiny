# Review request: player options, feats batch 2

Spells batch 7 is on main (942dfe6, docs 8776e60), with all of your
changes: Rewind reduces the damage by up to 70 and undoes nothing else;
Soul Lantern needs a creature that died in the last minute or a willing
one, and Wish or the caster frees it; Bone Cage has a save each turn;
Night Terror gives at most 1 Exhaustion and Advantage on a second try
within 7 days; Second Sun is Concentration for 1 minute. Spells: 214 of
220.

(Feats batch 1 was the 8 origin feats, 5d1c579.)

## The batch

- File: `compendium/content/feats/roles.py` (not committed).
- Entries: 22 feats (4 Fighting Style, 8 Epic Boon, 10 General). Feats: 65
  to 87 of 120.
- Build: `compendium/build.sh` passes. 166 tests pass, the checks are OK.
  Player 272 pages, GM 311. I read pages 230 and 231. There is no overflow.
- I searched every content file and the SRD feats for each name. No name
  is in use.
- Each feat fills a role that the SRD feats and the 57 original feats do
  not have. I left out each idea that is a copy of a paid feat (for
  example Sentinel, Polearm Master, Mounted Combatant, Healer, Chef).

## The feats, with the SRD feat or feature that each is equal to

| Type | Feat | Benefit | Equal to |
|---|---|---|---|
| Fighting Style | Rider Style | +1 melee attack while mounted, mount uses your AC | Archery (+2), split |
| Fighting Style | Phalanx Style | +1 AC to you and an adjacent ally, with a Shield | Defense (+1 AC) |
| Fighting Style | Wrestler Style | grapple with one hand, +2 damage with Light or Unarmed on the grappled creature, escape DC +2 | Two-Weapon Fighting |
| Fighting Style | Braced Shot Style | +2 to attack with Heavy ranged weapons and crossbows if you did not move | Archery (with a condition) |
| Epic Boon | Boon of the Wilds | never lost, Beasts and Plants friendly, Speak with Animals and Plants at will | Boon of Truesight |
| Epic Boon | Boon of the Deep Sea | breathe water, Swim Speed x2, Control Water 1/LR | Boon of Dimensional Travel |
| Epic Boon | Boon of the Storm | Immunity to Lightning and Thunder, 2d10 to melee attackers | Boon of Energy Resistance-type |
| Epic Boon | Boon of Renown | Advantage on Charisma checks with common folk, one failed Charisma check becomes a success 1/LR | Boon of Fate |
| Epic Boon | Boon of the Bulwark | Reaction: take an ally's hit within 10 ft, halved | Boon of Combat Prowess |
| Epic Boon | Boon of the Quarry | track one creature for 24 hours, no Invisible against you, Advantage on attacks | Boon of Irresistible Offense |
| Epic Boon | Boon of the Lorekeeper | all languages, Legend Lore 1/LR | Boon of Spell Recall |
| Epic Boon | Boon of the Phoenix | return from death 1/LR with half HP, 6d6 Fire burst | Boon of the Night Spirit (strong survival) |
| General | Seafarer | ship tools, Swim Speed, no Prone on a ship, faster ship | Skilled-type utility plus +1 |
| General | Beast Bond | a CR 1/4 Beast companion that Dodges unless commanded with a Bonus Action | Ranger beast companion, much weaker |
| General | Siege Engineer | double damage to objects and structures, build quickly | Grappler-level niche benefit |
| General | Monster Slayer | +1d6 once per turn against one creature type | Grappler-level, close to Hunter's Mark |
| General | Escape Artist | Advantage against Grappled and Restrained, slip out of bonds | Grappler (the reverse) |
| General | Light Sleeper | sleep in armor, no Surprise while asleep, 6-hour Long Rest | utility plus +1 |
| General | Last Stand | below half HP: +1 AC and saves, 18 to 20 on Death Saving Throws | Grappler-level |
| General | Spell Echo | after a successful save against a level 3 or lower spell, cast it once, 1/LR | Grappler-level, with a long limit |
| General | Bodyguard | Reaction: an attack on an adjacent ally targets you, with Disadvantage | Grappler-level (defensive) |
| General | Trapsmith | Thieves' Tools (or Expertise), Advantage to find traps, half damage from traps | Skilled-type utility plus +1 |

## Things that I am not sure of

1. Boon of the Phoenix: return from death once per Long Rest. The SRD
   Epic Boons are strong, and this works only after you die. I think that
   it fits level 19.
2. Beast Bond: a companion for any class is a big feature. I kept the
   Beast weak (CR 1/4) and it only Dodges unless you spend a Bonus Action.
3. Spell Echo: the caster casts a spell that it does not know, once per
   Long Rest. It needs the Spellcasting or Pact Magic feature.

## Next

Feats batch 3 is ready: 27 feats. 20 of them are species feats, one for
each original species, and each deepens the species' main trait (for
example Living Forge for the Kilnborn). The others are 5 General and 2
Origin feats. Feats: 87 to 114. I report the last 6 feats as a quality
limit, unless I find strong ideas.
