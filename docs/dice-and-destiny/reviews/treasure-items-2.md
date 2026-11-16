# Review request: treasure, magic items batch 2

From: the treasure session. Batch 1 is on main (`57940ae`, with the
progress file in `e8910bc`).

Batch 2 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part5.py`. Entries: 40. Original items:
  290 to 330.
- Build: `compendium/build.sh` passes (102 tests, the content checks, the
  page check, and the font check). I read GM page 214: no text goes out
  of a box. No name is the same as an SRD item. Each spell that an item
  names is in the SRD spell data. The text is plain ASCII, so no symbol
  can print as a Type 3 font.
- By rarity: Common 8, Uncommon 12, Rare 12, Very Rare 7, Legendary 1.
- By category: Weapon 13, Potion 12, Scroll 8, Ammunition 7.

## Gaps that this batch fills

Before this batch, 13 SRD weapon types had no original item. This batch
gives each of them one item: Club, Dart, Sickle, Blowgun, Shortbow,
Battleaxe, Morningstar, War Pick, Hand Crossbow, Pistol, Pike, Greatclub,
and Musket. Each armor type already has an item. Potions, scrolls, and
ammunition were the smallest consumable groups (25, 5, and 7 items).

## The strongest entries

- Draught of the Waking Dream (Legendary potion): the effect of Foresight
  (level 9) for 8 hours. One for each Long Rest.
- Scroll of the Unbroken Circle (Very Rare, single use): a 60-foot ward
  against one creature type for 8 hours, with 5d10 Radiant each turn.
  Equal to Forbiddance (level 6), with a shorter duration.
- Bolt of Banishing (Very Rare, single use): a Charisma save or the target
  leaves for 1 minute. Like Banishment (level 4) with no Concentration.
- Bullet of the Falling Mountain (Very Rare, single use): +6d10 Force, a
  push, and Prone. Compare Arrow of Slaying (6d10).
- Potion of Renewal (Very Rare): 4d8 + 8 Hit Points and Greater
  Restoration (level 5).
- Thunderbark Musket (Very Rare): +3, ignores Half and Three-Quarters
  Cover. Equal to a +3 weapon.
- Pike of the Long Wall (Very Rare): +2, a Reaction attack when a creature
  enters your reach, and the creature stops on a hit.
- Oakheart Greatclub (Very Rare): +2, push and Prone (DC 17), and Reach
  with +2d6 for 1 minute once per dawn.
- Potion of Sudden Spring (Rare): the effect of Haste (level 3) for 1
  minute with no Concentration, then the same lethargy.
- Sleeve Crossbow (Rare): +1, hidden, and once per dawn a save or
  Unconscious for 1 minute (it ends on damage). Like Sleep on one target.
- Scroll of the Safe Cottage (Rare): a shelter for 8 creatures for 8 hours.
  Compare Tiny Hut (level 3).

## Things that I am not sure of

1. Potion of Sudden Spring repeats the Haste rules almost word for word.
   It is a potion form of an SRD spell, not a new mechanic. Is that filler?
   I can replace it.
2. Draught of the Waking Dream at Legendary: Foresight is a level 9 spell,
   so the guide puts it at Legendary. The SRD has no Foresight potion.
3. Sleeve Crossbow: is a save-or-Unconscious effect once per dawn correct
   at Rare with a +1 bonus?

## Note: the traps work

The traps request is still open in `treasure-traps-1.md`. Since the split
in `5caee92`, the traps belong to the GM tools session. The traps changes
are still uncommitted in my working tree, and the full diff is in that
file. I do no more work on traps until you tell me option A or option B
from that file.
