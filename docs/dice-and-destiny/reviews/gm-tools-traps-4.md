GM tools: tables batch 3 is on main (docs c541a72). Sets: 30 of 50.

Traps batch 4 is ready for review. It is the last traps batch: 80 of 80 after it. Nothing of the batch is committed yet. It uses the treasure format with no change to the renderer.

Build: compendium/build.sh passes (177 tests, content check, page check, font check with no Type 3). GM book: 353 pages. I read the new entries: no overflow, the band tables stay in one piece.

## Commit

1. feat: add the last 16 traps and hazards
   - compendium/content/traps/last_traps.py (9 traps), compendium/content/traps/last_hazards.py (7 hazards)

## Entries: 16 (9 traps, 7 hazards). Totals after the batch: 80 of 80

Traps: Caltrop Spill, Endless Corridor, Fool's Gold Hoard, Greased Slope, Guardian Spears, Murder Gate, Starfall Orrery, Toppling Shelves, Wasp Nest Snare.
Hazards: Acid Rain, Fey Ring, Flash Flood, Forest Fire, Groundquake, Leech Pool, Mirage Lake.
Severity: Setback 7, Dangerous 8, Deadly 1.
Entries by band after the batch (all 80): levels 1-4: 54, 5-10: 75, 11-16: 67, 17-20: 32. All 80 by kind: 47 traps, 33 hazards.

Names: after your note on Soul Lantern, I checked all 80 trap names against every other content category and every name in the SRD data. No clash. One draft name was the SRD spell "Earthquake"; the hazard is now "Groundquake".

Every check uses the band DC. The one fixed number is the 20-foot fall into a crack in Groundquake (the SRD falling damage, the same at every level).

Strongest entries:
- Starfall Orrery (Deadly, levels 11 to 20): 12d10 / 18d10 Bludgeoning each round for 3 rounds, Dex save (no half), pushed 15 feet. Under the Deadly limit each round. Ways out: it stops after 3 rounds, the door is never locked, lying Prone gives Advantage, and an iron bar can jam the gears.
- Guardian Spears and Groundquake (Dangerous, levels 5 to 20): 4d10 / 9d10 / 16d10. The Spears repeat each round in a 40-foot hall (one Dash crosses it; the old gesture stops it). Groundquake lasts 1d4 rounds; open ground or a doorway gives Advantage.
- Fey Ring (Setback, levels 1 to 20): Charmed until dawn on a failed Cha save, then damage and 1 Exhaustion level; on a d6 roll of 1 or 2, the dance lasted a day or a week. No death and no permanent loss. The rules are a night-long Charmed condition, with one save to resist; there is no save each turn as in a spell.
- Murder Gate (Dangerous, levels 1 to 16): trapped between portcullises, then 3 rounds of boiling oil. Ways out: lift a portcullis (Strength (Athletics) against the DC + 2), a shield overhead gives Advantage, the oil runs out after 3 rounds.

## Things I am not sure of

1. Fool's Gold Hoard and the Fey Ring use the Charmed condition for a long time (1 hour, or until dawn). Each has a way to end it early: an ally pleads or the creature takes damage (Hoard, a new save), or a friend pulls the dancer out (Ring).
2. Acid Rain damages gear (a cumulative -1 each hour for leather, cloth, or wood in the open). It is small, but it is permanent until repaired. Tell me if you want it removed.

Tell me to commit, or what to change.
