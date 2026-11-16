# Review request: bestiary batch 12, desert monsters (second set)

## Batch

- File: `compendium/content/monsters/desert_2.py` (new, not committed).
- Entries: 20 monsters from the deep waste, lost tombs, and cities of mirage.
- Desert goes from 34 to 54 monsters. The batch puts most entries where
  desert was thin: 7 at CR 11 to 16 (desert had 4) and 4 at CR 17 or more
  (desert had 2).

## Build

- `compendium/build.sh` passes on `main` 52b6a74 (228 tests, the content
  checks, the page check, and the font check). GM book: 428 pages
  (hardcover count, with the work of other sessions).
- After the build, I lowered two AC overrides (see "Spread"). The tests and
  the content check pass after that change. I run the full build again
  before the commit.
- I examined page 176 as an image. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 2, 2 to 4: 3, 5 to 10: 4, 11 to 16: 7, 17 to 24: 4.
- Types: 5 Monstrosity, 3 Construct, 2 Beast, 2 Fey, 2 Fiend, 2 Undead,
  1 Giant, 1 Elemental, 1 Celestial, 1 Dragon.
- AC: the highest override is 2 above the target. A monster with
  Resistance to Bludgeoning, Piercing, and Slashing has no AC above the
  target (your rule for the Granite Dragon). I lowered the Jackal-Headed
  Sentinel to AC 15 and the Tomb General to AC 17 for this reason.
- The Dune Giant uses the thrown kind. The Glass Wyrm is the old form of the
  Glassfire Dragon (CR 13) of the first desert batch.
- The name of the file is `desert_2.py`, because `desert.py` exists.

## Strongest entries and the SRD entry that each is equal to

- **Glass Wyrm** (CR 21, Dragon): 3 Rends at 40, a 16d10 Fire Cone that
  leaves glass, Mirror Scales (a missed ranged spell attack can bounce to
  another creature). Equal to Ancient Blue Dragon (CR 23), a little below.
- **Eternal Pharaoh** (CR 20, Undead): 2 flail attacks at 44.5, BPS
  resistance, Decree of Dust (14d10 Necrotic and a lower HP maximum until a
  Long Rest), Dominate Monster, Insect Plague, Power Word Stun 1/Day, four
  canopic jars for rejuvenation. Equal to Lich (CR 21), a little below.
  The role is the SRD Mummy Lord at a higher tier, with new rules.
- **Herald of the Noon Sun** (CR 18, Celestial): 3 attacks up to 33, a glare
  that gives Disadvantage to attacks against it in its light, a 12d10
  Radiant burst. Equal to Solar (CR 21) minus 3.
- **Hunger of the Waste** (CR 17, Fiend): 3 claws at 36, no healing within
  30 feet, Drink the Land (12d10 Necrotic and 1 Exhaustion level). Equal to
  Adult Red Dragon (CR 17).
- **Scorpion Queen** (CR 15): 3 attacks at about 28; the sting can Paralyze
  until the end of the next turn on a failed Con save. Equal to Purple Worm
  (CR 15).

## Not sure

1. **Scorpion Queen, Paralyzed on a sting.** Up to three stings each turn can
  each force a save. Tell me if you want it on the first sting each turn only.
2. **City of Mirages** (CR 13): a creature that fails its save wants to stay
  in the city and repeats the save each dawn. It is a story trap more than a
  fight.
3. **Eternal Pharaoh, Power Word Stun.** A level 8 spell at CR 20.

## A problem in another file (not mine)

In `compendium/content/monsters/helper_urban.py`, the shared Legendary
Resistance text is never filled in with the monster's name. The book prints
"If the creature fails a saving throw" for 8 monsters: Sewer Wyrm, Lord of
Ledgers, Plague Mother, Shadow of the Old City, The Crawling Plague,
Clocktower Titan, Spire Wyrm, and The City Below. A loop like the one at the
end of my files fixes it. I did not change the helper's file.

## Next

After approval: `feat: add 20 desert monsters (second set)`, then the
progress docs commit. Then an arctic second set (19 or 20).
