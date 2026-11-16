# Review request: player options, origin feats batch 1

Backgrounds batch 1 is on main (463d955 the feat check, 29adb82 the 18
backgrounds, c2bc317 the docs). Backgrounds: 30 of 40.

## The batch

- File: `compendium/content/feats/walks_of_life.py` (not committed).
- Entries: 8 origin feats. Feats: 57 to 65 of 120.
- Build: see the last section.

Each feat is tied to a region or a walk of life, so that the last 10
backgrounds can use them. The SRD has only 4 origin feats (Alert, Magic
Initiate, Savage Attacker, Skilled).

| Feat | Region or walk of life | Benefit | Equal to |
|---|---|---|---|
| Sea Legs | Sea | Swim Speed, hold breath 10 min, Advantage against Prone on a ship, predict the weather at sea | Skilled (utility) |
| Desert Walker | Desert | Half water, adapted to heat, sand and glare do not obscure, Survival (or Expertise) | Wilderness Born |
| Courtly Poise | Court | Deception or Persuasion, Disadvantage on Insight to read you, +PB to Initiative in a social setting | Alert (narrow) |
| Streetwise | City, underworld | Deception or Stealth, 1 hour to find rumors, a fence, or who holds power, Advantage to notice that you are followed in a settlement | Skilled |
| Steadfast Faith | Temple | PB/LR: add 1d4 to a failed save, Religion | Alert. Weaker than a Lucky-type feat |
| Born Rider | Steppe | Mount for 5 ft, Advantage to stay mounted, mount Speed +10, Dash or Disengage for the mount as a Bonus Action, Animal Handling | Savage Attacker (for a mounted character) |
| Crag Walker | Mountains | Climb Speed, no extra cost for rubble, scree, ice, or slopes, Advantage on Athletics to climb in bad weather | Wilderness Born |
| Cave Eyes | Underground, night | Darkvision 60 (or +30), Advantage on sight Perception in Dim Light | Alert (narrow) |

## Things that I am not sure of

1. Steadfast Faith is the strongest in combat: 1d4 on a failed save, PB
   times each Long Rest. It is like a small Bless on yourself. I think
   that it is fair for an origin feat. I can make it 1/LR.
2. Crag Walker: my first draft also reduced falling damage by 5 times
   the level. I removed it, because it is the Monk Slow Fall (level 4).
3. Cave Eyes gives Darkvision to a species that has none. Many species
   in the SRD have Darkvision 60 or 120, so I think that this is fair.
4. Born Rider: in the SRD, a controlled mount can take only Dash,
   Disengage, or Dodge. The feat lets the rider pay for the Dash or
   Disengage with a Bonus Action, so that the mount can Dodge.

## Build

`compendium/build.sh` passes: 81 tests, the checks are OK, player 238
pages, GM 231. I read pages 221 and 222. The feats are in their boxes, and
there is no overflow.

## Names

I searched every content file for each new name. Two names were already in
use in other categories, so I changed them:

- "Night Eyes" is a warlock subclass feature in `subclasses/part4.py`, with
  almost the same text. The feat is now "Cave Eyes".
- "Sure-Footed" is a trait of two rams in the monster files. The feat is now
  "Crag Walker".

The duplicate check only compares names inside one category, so it did not
find these.

## Next

The last 10 backgrounds are ready. They use these feats (Whaler, Island
Wayfinder, Salt Trader, Envoy, Gang Runner, Temple Guard, Steppe Scout,
Goatherd, Deep Forager, Night Watchman). I send them for review after this
batch is on main.
