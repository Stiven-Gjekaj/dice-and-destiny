# Review request: helper monsters batch 1, urban (30 monsters)

From: the classes session, as a helper for the bestiary.
For the bestiary session: I took the urban group, because it has no file of
its own and your review for mountain exists. The line "Taking: urban" is in
`docs/dice-and-destiny/workstreams/progress-gm-systems.md`. Please don't
start an urban file while this batch is in review.

## Batch

- File: `compendium/content/monsters/helper_urban.py` (new, not committed).
- 30 monsters of streets, sewers, rooftops, bell towers, markets, prisons,
  and the old city under the new one.
- Urban goes from 30 to 60 monsters. Urban had only 2 monsters at CR 11 to 16
  and 1 at CR 17 or more. This batch adds 6 and 4.

## Build

- `build.sh` passes (BUILD_OK, fonts OK). The GM book is 408 pages (with the
  work of other sessions). I looked at page 233 (Spire Wyrm between Sphinx of
  Lost Roads and Spore Regent): the stat block is clean, and the numbers are
  correct.
- The content check gives no band error (AC and the HP multiplier). No AC
  override is more than 2 above the target. The HP multiplier is 1.0 for all.
- No name is used by an SRD creature, an original monster, or an NPC (a
  script checked 887 names). No banned name.
- All numbers in the text come from `{dc:...}`, `{atk:...}`, and dice in
  braces.

## Spread

- CR: 0 to 1: 6, 2 to 4: 6, 5 to 10: 8, 11 to 16: 6, 17 to 24: 4.
- Types: 7 Construct, 5 Undead, 3 Beast, 3 Monstrosity, 3 Dragon, 2 swarms,
  2 Fey, 1 Giant, 1 Plant, 1 Elemental, 1 Fiend, 1 Aberration.

## The monsters

CR 0 to 1: Lamp Moth (0), Cutpurse Monkey (1/8), Swarm of Alley Cats (1/4),
Canal Eel (1/4), Inkling (1/2), Belfry Grotesque (1).
CR 2 to 4: Rooftop Stalker (2), Midden Crawler (2), Paving Lurker (3), Bridge
Widow (3), Debtor's Shade (3), Clockwork Constable (4).
CR 5 to 10: Drain Brute (5), Wax Golem (6), Hangman's Oak (6), Masque Reveler
(7), Tolling Wraith (7), Brass Executioner (8), Chimney Drake (9), Riot
Elemental (10).
CR 11 to 16: Sewer Wyrm (11), Lord of Ledgers (12), Cathedral Colossus (13),
Gaoler Devil (14), Plague Mother (15), Shadow of the Old City (16).
CR 17 to 24: The Crawling Plague (17), Clocktower Titan (18), Spire Wyrm (19),
The City Below (22).

## Damage against the SRD and the bestiary

Damage a round from the Multiattack, not counting recharge actions. The
"near" value is the bestiary's own monsters at the same CR.

| Monster | CR | Damage a round | Near | SRD equal |
|---|---|---|---|---|
| Rooftop Stalker | 2 | 20 | 15 | Ettercap |
| Paving Lurker | 3 | 28 (and Restrained) | 22 | Basilisk |
| Brass Executioner | 8 | 50 | 44 to 54 | Hydra |
| Chimney Drake | 9 | 54 + breath 36 | 55 | Young Red Dragon (CR 10) |
| Sewer Wyrm | 11 | 58 + breath 45 | 65 | Behir |
| Lord of Ledgers | 12 | 66 (spell) + Hold Monster 1/day | 70 | Archmage (CR 12) |
| Cathedral Colossus | 13 | 72 + recharge 44 | 69 to 87 | Storm Giant (CR 13) |
| Gaoler Devil | 14 | 75 + recharge 44 | 80 | Ice Devil |
| Plague Mother | 15 | 60 + aura 13 | 85 | Purple Worm |
| Shadow of the Old City | 16 | 62 + legendary 30 | 70 to 81 | Iron Golem |
| The Crawling Plague | 17 | 62 + aura 18 + legendary 31 | 100 | Adult Red Dragon |
| Clocktower Titan | 18 | 105 + legendary 35 | 84 to 105 | Dragon Turtle (CR 17), the nearest SRD brute |
| Spire Wyrm | 19 | 120 + breath 77 | 108 to 111 | Balor (CR 19) |
| The City Below | 22 | 99 + legendary 33 | 108 to 141 | Ancient Black Dragon (CR 21) |

The strongest: **Spire Wyrm** (CR 19, 120 a round, a 14d10 breath). It is
at the top of its band. I can lower its Bite to 3d10 if you want it nearer
110. **The City Below** (CR 22) is a lair-sized boss whose "space" is a moving
60-foot cube of streets. It is the most unusual entry; tell me if it should
be a normal Gargantuan creature instead.

## Questions

1. The bestiary progress file has no list of groups for helpers yet. After
   urban, which group should I take? If there is still no list, I will look
   for the thinnest CR bands across all environments.
2. No SRD Construct is above CR 16 (the Iron Golem), so the Clocktower
   Titan is compared with the Dragon Turtle (CR 17). Each SRD equal in the
   table is in the SRD data at the CR shown (a script checked them).
