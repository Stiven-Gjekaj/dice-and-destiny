GM tools: downtime batch 1 is on main (4628956, 9ee86d7, dee16d3, docs 634887d). The Hosting a Feast link now names "World-Building Tables", not a chapter number.

Traps batch 2 is ready for review. Nothing of the batch is committed yet. It uses the treasure format with no change to the renderer.

Build: compendium/build.sh passes (141 tests, content check, page check, font check with no Type 3). GM book: 277 pages. I read the new entries: no overflow, the band tables stay in one piece.

## Commits

1. fix: name the chapter of the damage table in the traps chapter
   - books/gm.src.html: "the Improvised Damage table in Chapter 10" becomes "... in Exploration, Travel & the World" (your rule: chapter names only).
2. fix: list the chapters of Part VII in its description
   - books/gm.src.html: the Part VII line said "traps and hazards, and more to come". It now lists traps and hazards, world-building tables, two sample pantheons, and downtime activities.
3. feat: add 17 traps and hazards
   - compendium/content/traps/dungeon_2.py (11 traps), compendium/content/traps/wilds_2.py (6 hazards)

## Entries: 17 (11 traps, 6 hazards). Totals after the batch: 43 of 80

Traps: Blot Glyph, Bone Chimes, Gilded Cage, Grasping Mosaic, Hall of Faces, Hush Chamber, Oubliette Chute, Sawn Rope Bridge, Soulbrand Threshold, Spark Moth Jar, Warding Bell.
Hazards: Ashfall, Bloodthorn Ivy, Geyser Field, Razor Coral, Scouring Sandstorm, Sinkhole.
Severity: Setback 5, Dangerous 11, Deadly 1. Entries by band after the batch (all 43): levels 1-4: 36, 5-10: 43, 11-16: 33, 17-20: 10.

These come from my earlier draft of 30. I dropped 13 that were near copies of the 26 in traps batch 1 (same name or same idea): Lodestone Floor, Rockslide, Storm Ridge, Riptide (same names), and Grinding Stair, Scything Lintel, Counterweight Crusher, Poppy Breath Vents, Weeping Censer, Flooding Vault, Sucking Mire, Bog Gas, Glowcap Spores (same ideas as Collapsing Stair, Scything Hall Blade, Grinding Ceiling, Sleep-Spore Censer, Flooding Chamber, Quickmud, Firedamp Pocket, Choking Bloom).

Strongest entries:
- Sawn Rope Bridge (Deadly): 3d10 / 6d10 / 12d10 Bludgeoning from a fall, Dex save, no half damage. Under the Deadly limit at each band; equal to a deep Hinged Flagstone Pit.
- Warding Bell (Dangerous, levels 1 to 20): 2d10 / 4d10 / 10d10 / 18d10 Psychic in a 20-foot Sphere, Wis save for half, Incapacitated until the end of the next turn on a failure, and an alarm. It shares Psychic damage with the Whispering Idol, but the Idol lures one creature with Charmed; the Bell is an area alarm.
- Bone Chimes and Hush Chamber (Dangerous, levels 1 to 20): the same damage rows as the Bell. Necrotic with no healing until the next turn (Chimes), and Thunder with Deafened, on each loud noise (Hush Chamber).
- Soulbrand Threshold (Dangerous, levels 5 to 20): 4d10 / 10d10 / 18d10 Radiant or Necrotic, Cha save for half, a 24-hour mark (no benefit from Invisible, the maker's servants know where the creature is). Equal to Glyph of Warding at the higher bands.

Repeating damage (your rule: a way out in about 3 rounds):
- Spark Moth Jar: changed to 3 rounds in all; a creature can swat it to end it 1 round sooner, water or a wet blanket makes it harmless.
- Grasping Mosaic: an action and a Strength (Athletics) check escapes; each hand breaks (AC 15, 10 HP); saying the god's name stops it.
- Bloodthorn Ivy: a save at the end of each turn, a waved torch ends Restrained, the ivy has Vulnerability to Fire.
- Hall of Faces: a failed save gives Frightened, and the creature must use its movement to leave the hall.

## Things I am not sure of

1. Ashfall and Scouring Sandstorm repeat each hour of travel, not each round. Each also gives 1 Exhaustion level on a failed save. Shelter ends them.
2. Some find and stop texts give a fixed DC that is not the DC of the band (for example "a DC 13 Wisdom (Perception) check"). The chapter says "the DC ... unless the text says otherwise", so this is permitted, but traps batch 1 mostly uses "against the DC". Tell me if you want the band DC everywhere.

Tell me to commit, or what to change.
