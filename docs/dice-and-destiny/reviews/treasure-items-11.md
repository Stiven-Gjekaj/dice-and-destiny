# Review request: treasure, magic items batch 11

From: the treasure session. Batch 10 is on main (`157ed3e`), with the two
clarifications from your review. The progress file records it.

Batch 11 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part14.py`. Entries: 40. General items:
  650 to 690. After this, one last batch of about 35 reaches about 725.
- Build: `compendium/build.sh` passes (180 tests, the content checks, the
  page check, and the font check). GM book: 360 pages. I read GM page
  296: no text goes out of a box. No name is the same as an SRD item or
  another original item. The text is plain ASCII.
- By category: Wondrous 14, Staff 6, Rod 6, Wand 6, Weapon 4, Armor 4.
  After batch 10 the smallest categories were Staff (37), Rod (38), and
  Wand (38). Rods had no Common item, and staffs had one, so this batch
  adds two Common rods and two Common staffs.
- By rarity: Common 6, Uncommon 14, Rare 11, Very Rare 6, Legendary 3.
- Most items in this batch have their own effects, not spells.

## The strongest entries

- Wand of the Black Star (Legendary): all 7 charges for a 20-foot Sphere
  for 1 minute, 8d10 Force each turn (DC 18 Strength, half on a success)
  and Speed 0. Compare Incendiary Cloud (level 8, 10d8 in a 20-foot
  Sphere).
- Half Plate of the Undying Sun (Legendary): +3, Radiant Resistance, regain
  5 Hit Points each turn in sunlight while you have at least 1 Hit Point.
- Bow of the Thousand Hunts (Legendary): +3, triple range, ignores all
  cover except Total Cover.
- Staff of the Stormcrow (Very Rare): +2, 1 to 5 charges, each a spell
  attack (+9) for 2d8 Lightning. Five crows average 45 damage if all hit,
  equal to a level 5 or 6 single-target spell.
- Wand of Split Lightning (Very Rare): 3 charges, up to three targets, 6d6
  each (DC 17 Dex). Compare Chain Lightning (level 6, 10d8 to four
  targets).
- Rod of Returned Blows (Very Rare): 3 charges, a Reaction that deals half
  the damage you took back to the attacker as Force.
- Phylactery of the Saint (Very Rare): once per 7 days, you return to life
  at the next dawn with half your Hit Points.
- Hourglass of the Wasted Turn (Very Rare): once per dawn, a creature makes
  a DC 17 Wisdom save or loses its action for one turn.
- Mail of the Last Guardian (Very Rare): +2, allies within 10 feet get +1
  AC.

## Things that I am not sure of

1. Phylactery of the Saint: a weekly return from death at Very Rare. It is
   slower than Ring of the Last Hour (Legendary), because the wearer stays
   dead until dawn. Should it be Legendary?
2. Mail of the Last Guardian: +1 AC to every ally within 10 feet does not
   stack with itself, but two wearers could cover a whole party. Say that
   the bonus does not stack?
3. Wand of the Black Star at Legendary: it uses all 7 charges, so once per
   day. Is 8d10 each turn for 1 minute too strong?
