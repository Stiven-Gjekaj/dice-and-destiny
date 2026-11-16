# Review request: helper monsters batch 3, swamp and coast (20 monsters)

From: the classes session, as a helper for the bestiary.
For the bestiary session: you gave me swamp and coast. The line "Taking:
swamp and coast" is in
`docs/dice-and-destiny/workstreams/progress-gm-systems.md`.

## Batch

- Files: `compendium/content/monsters/helper_swamp.py` (10) and
  `compendium/content/monsters/helper_coast.py` (10). Both are new and not
  committed.
- Both files have the loop that puts the name of the monster into
  Legendary Resistance.

## Build

- `build.sh` passes (BUILD_OK). The GM book is 450 pages, with the work of
  other sessions.
- I looked at page 206 (Hurricane Lord). The stat block is clean. The
  Legendary Resistance trait says "If the hurricane lord fails". Gale Fist
  shows 29 (4d10 + 7) plus 13 (3d8).
- The content check passes. It gives no band error for AC or HP.
- A script checked all 604 monsters. No two monsters have the same name.
  No new name is the name of an SRD creature or an NPC.
- All numbers in the text come from `{dc:...}`, `{atk:...}`, and dice in
  braces.

## Spread

- CR: 0 to 1: 3, 2 to 4: 4, 5 to 10: 3, 11 to 16: 7, 17 to 24: 4.
- Types: 6 Monstrosity, 3 Elemental, 2 Fey, 2 Construct, 1 Ooze, 1 Undead,
  1 swarm of Undead, 1 Beast, 1 Plant, 1 Dragon, 1 Aberration.

## The monsters

Swamp: Cattail Archer (1/2), Quagmire Ooze (2), Mosquito Matriarch (3), Peat
Fire Spirit (8), Drowned Abbot (11), Bog Iron Golem (12), Snapping Titan
(13), Blackwater Coil (14), Weeping Willow Matriarch (17), Plague-Moon Wyrm
(21).

Coast: Tidepool Mimic (1), Skeleton Crew (4), Dune-Shore Wurm (6), Fogbank
Elemental (9), Undertow Horror (11), Selkie Tide Queen (12), Kraken Priest
(14), Moon-Tide Behemoth (15), The Last Lighthouse (17), Hurricane Lord (19).

## Damage against the targets and the SRD

Damage a round is the Multiattack with the strongest attack. A script
calculated it from the stat blocks. The recharge column is the average
damage of the recharge action.

| Monster | CR | Damage a round | Recharge | Target | SRD equal |
|---|---|---|---|---|---|
| Mosquito Matriarch | 3 | 24 | - | 21 | |
| Skeleton Crew | 4 | 32 | - | 27 | Ghost |
| Dune-Shore Wurm | 6 | 37 | - | 39 | |
| Peat Fire Spirit | 8 | 47 | - | 50 | Hydra |
| Fogbank Elemental | 9 | 53 | 36 | 55 | Bone Devil |
| Drowned Abbot | 11 | 64 | 36 | 65 | Behir |
| Undertow Horror | 11 | 67 | - | 65 | Behir |
| Bog Iron Golem | 12 | 69 | 40 | 70 | Archmage |
| Selkie Tide Queen | 12 | 70 | 44 | 70 | Archmage |
| Snapping Titan | 13 | 71 | - | 75 | Storm Giant |
| Blackwater Coil | 14 | 72 | - | 80 | Ice Devil |
| Kraken Priest | 14 | 72 | 49 | 80 | Ice Devil |
| Moon-Tide Behemoth | 15 | 83 | 55 | 85 | Purple Worm |
| Weeping Willow Matriarch | 17 | 102 + legendary | 66 | 100 | Adult Red Dragon |
| The Last Lighthouse | 17 | 98 + legendary | 66 | 100 | Adult Red Dragon |
| Hurricane Lord | 19 | 127 + legendary | 55 | 110 | Balor |
| Plague-Moon Wyrm | 21 | 106 + legendary | 88 | 120 | Ancient Black Dragon |

A script checked that each SRD equal is in the SRD data at the CR shown.

## Questions

1. **Hurricane Lord** (CR 19) is 127 a round, above the target of 110. Its
   recharge is low (55). I can lower Gale Fist to 3d10, which gives 111.
   Do you want this?
2. **Plague-Moon Wyrm** (CR 21) is 106 a round, below 120. Its breath (88)
   and legendary actions make up the difference. I can add 1d10 to its Bite
   if you want it nearer 120.
3. **Blackwater Coil** and **Kraken Priest** (CR 14) are at 72, below 80.
   The Kraken Priest has a recharge of 49. The Coil has a grapple and
   constrict instead. Tell me if you want more damage on either.
4. After this batch, which group do I take next? The open groups that I
   know are grassland and hill, and they belong to the second helper.
