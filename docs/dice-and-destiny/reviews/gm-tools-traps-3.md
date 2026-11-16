GM tools: tables batch 2 is on main (61d16cf, 0ce54cd, docs 7b1f573). Sets: 20 of 50. The compact layout for long tables of short entries is in my progress file under "Work to do later".

Traps batch 3 is ready for review. Nothing of the batch is committed yet. It uses the treasure format with no change to the renderer.

Build: compendium/build.sh passes (167 tests, content check, page check, font check with no Type 3). GM book: 325 pages. I read the new entries: no overflow, the band tables stay in one piece.

## Commit

1. feat: add 21 traps and hazards for high levels and strange places
   - compendium/content/traps/high_halls.py (13 traps), compendium/content/traps/far_places.py (8 hazards)

## Entries: 21 (13 traps, 8 hazards). Totals after the batch: 64 of 80

Traps: Banishing Circle, Basalt Eye, Contract Lectern, Crushing Hand Gate, Ghostlight Procession, Pendulum Bridge, Reversed Vault, Rune of Unmaking, Sealed Breath Tomb, Soul Lantern, Stained Glass Sentinel, Swapping Mirrors, Thunderhead Chamber.
Hazards: Crushing Deep, Hailstorm, Lava Crust, Planar Undertow, Singing Crystal Cave, Stampede, Wild Magic Zone, Withering Fog.
Severity: Setback 3, Dangerous 13, Deadly 5.
Entries by band after the batch (all 64): levels 1-4: 43, 5-10: 60, 11-16: 54, 17-20: 26 (was 10). The batch puts weight on the high levels, as the progress file planned.

Every check uses the band DC ("against the DC"). The only fixed number is the 3d6 Bludgeoning when a creature falls back to the floor in the Reversed Vault (a normal 30-foot fall is about the same at every level).

Strongest entries:
- Rune of Unmaking (Deadly, levels 11 to 20): 18d10 / 24d10 Force in a 30-foot radius, Con save for half, ends spells of level 3 or lower on a failure. A creature reduced to 0 HP by it turns to dust (as the SRD Disintegrate). Exactly at the Deadly limit. It has a key, a 3-check way to unpick it, and it is safe if nobody touches the door or casts near it.
- Crushing Hand Gate (Deadly, levels 5 to 20): 8d10 / 15d10 / 20d10 Bludgeoning, Dex save, Grappled on a failure. Under the Deadly limit. An offering of 10 GP for each creature stops it.
- Reversed Vault (Deadly, levels 11 to 20): 10d10 / 18d10 Piercing from the ceiling spikes, Dex save for half, then 3d6 from the fall back. The total is near the Deadly limit (18d10 + 3d6 = 109.5 at levels 17 to 20, under 132).
- Basalt Eye (Dangerous, levels 5 to 20): damage, then Restrained, then Petrified for 1 hour on a second failed save. Equal to the SRD Flesh to Stone (level 6), with a shorter Petrified time.
- Banishing Circle (Dangerous, levels 11 to 20): a failed Cha save sends the creature to an empty pocket world for up to 1 minute (a save each turn), then Force damage on return. Equal to the SRD Banishment (level 4) at a higher DC.

Repeating damage (a way out in about 3 rounds): Stained Glass Sentinel (leave the 20-foot square of light, or cover the window), Soul Lantern (move 15 feet away, holy water, or break it), Thunderhead Chamber (the room is 40 feet long: one Dash crosses it; the grounding rod), Pendulum Bridge (60 feet; a Dash crosses in 1 or 2 rounds; a rope stops a fall), Lava Crust (a Strength check as an action, with Advantage from a rope), Withering Fog (leave the fog), Planar Undertow (move away; a rope gives Advantage).

## Things I am not sure of

1. Wild Magic Zone has its own d6 table of results inside the effect text. It is original and has no rules from a paid book, but it fills the same role as a "wild magic" table. Tell me if you want it changed.
2. Crushing Deep: I wrote that Water Breathing doesn't protect against pressure, but Freedom of Movement does. The SRD doesn't name pressure, so this is my ruling.
3. Sealed Breath Tomb has no damage. It uses the SRD suffocation rules, and it ends after 10 minutes or with Dispel Magic.

Tell me to commit, or what to change.
