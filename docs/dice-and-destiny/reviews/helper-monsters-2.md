# Review request: helper monsters batch 2, underwater and underdark (28 monsters)

From: the classes session, as the first helper of the bestiary.

## Groups

The bestiary progress file lists the groups that are open for a helper. I
take two whole groups from that list (the line "Taking: underwater and
underdark" is in `progress-gm-systems.md`):

- underwater: 36 monsters, 18 to reach about 54. File
  `compendium/content/monsters/helper_underwater.py`, 18 monsters.
- underdark: 44 monsters, 10 to reach about 54. File
  `compendium/content/monsters/helper_underdark.py`, 10 monsters.

A correction: before the list was on `main`, my progress file claimed "CR 11
to 16 for five environments". I withdrew that claim in commit 643acbd,
because the bestiary keeps desert and arctic, and the second helper prefers
grassland. I wrote no desert, arctic, or grassland file.

## Build

- `build.sh` passes (BUILD_OK). The GM book is 426 pages (with the work of
  other sessions). I looked at page 199 (Hullbreaker Crab): the stat block is
  clean.
- No band error. No AC override is more than 2 above the target. The HP
  multiplier is 1.0 for all.
- No name is used by an SRD creature, an original monster, or an NPC (a
  script checked them). No banned name.
- I read the existing monsters of both groups first. Two of my drafts were
  too close to existing ones (a pearl-scaled water dragon, like the Pearl
  Dragon; a walking fungus giant, like the Mycelial Colossus), so I replaced
  them with the Hullbreaker Crab and the Gloomweaver Matron.

## Spread

- Underwater (18): 0 to 1: 2, 2 to 4: 3, 5 to 10: 4, 11 to 16: 6, 17 to 24: 3.
  Underwater goes from 36 to 54. Its thinnest band, 11 to 16, goes from 5 to
  11.
- Underdark (10): 5 to 10: 2, 11 to 16: 6, 17 to 24: 2. Underdark goes from
  44 to 54. Its 11 to 16 band goes from 6 to 12.

## The monsters

Underwater: Bubblecap Drifter (1/8), Thunderpunch Shrimp (1), Wreck Haunt (2),
Clamjaw Sentinel (3), Tide Witch (4), Brine Wailer (5), Vent Elemental (6),
Kelp Hydra (7), Ship-Eater Squid (8), Reef Tyrant (11), Drowned Admiral (12),
Trench Horror (13), Hullbreaker Crab (14), Maelstrom Serpent (15), Abyssal
Choir (16), Abyssal Leviathan (17), Coral Throne (19), Tidal Sovereign (20).

Underdark: Glimmerworm (5), Stalagmite Ambusher (8), Crystal Basilisk Queen
(11), Gloomweaver Matron (12), Lightless Sea Kraken (13), Echo Wyrm (14),
Hollow King's Golem (15), Deep Mother (16), Queen Below the Roots (17),
Mountain-Eater Worm (19).

## Damage against the SRD and the bestiary

Damage a round from the Multiattack. "Plus" is an aura, a legendary attack,
or a recharge action. The "near" value is the bestiary's own monsters at
that CR.

| Monster | CR | Damage a round | Near | SRD equal |
|---|---|---|---|---|
| Kelp Hydra | 7 | 52 (five fronds) | 45 | Hydra (CR 8), the same regrowth idea with fronds and fire |
| Reef Tyrant | 11 | 58 | 65 | Behir |
| Trench Horror | 13 | 66 + aura 11 | 69 to 87 | Storm Giant |
| Hullbreaker Crab | 14 | 71 + recharge 55 | 80 | Ice Devil |
| Maelstrom Serpent | 15 | 80 + recharge 45 | 85 | Purple Worm |
| Deep Mother | 16 | 72 + legendary 31 + brood | 70 to 81 | Iron Golem |
| Abyssal Leviathan | 17 | 82 + swallow 21 + legendary 30 | 100 | Dragon Turtle |
| Queen Below the Roots | 17 | 82 + legendary 41 | 100 | Adult Gold Dragon |
| Coral Throne | 19 | 97 + legendary 48 | 110 | Balor |
| Mountain-Eater Worm | 19 | 104 + legendary 45 | 110 | Balor |
| Tidal Sovereign | 20 | 102 + legendary 34 | 108 to 111 | Ancient Black Dragon (CR 21) |

The strongest: **Coral Throne** (CR 19). It regains 20 HP each turn
underwater, and its legendary action hurts each creature that its Reef
Prison holds. **Kelp Hydra** (CR 7) uses the same idea as the SRD Hydra
(parts that grow back unless they burn) with fronds; tell me if it is too
close to the Hydra.

## Questions

1. Kelp Hydra: keep the frond rule, or give it a different trick?
2. After this batch, the open groups left are grassland, hill, swamp, and
   coast. The second helper prefers grassland and hill. Shall I take swamp and
   coast (10 each) next?
