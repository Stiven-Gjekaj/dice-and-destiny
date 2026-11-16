# Review request: treasure, magic items batch 12 (last general batch)

From: the treasure session. Batch 11 is on main (`618d592`), with the
three changes from your review. The progress file records it.

Batch 12 is ready for review. Nothing is committed yet. It is the last
general batch, as you asked.

- File: `compendium/content/items/part15.py`. Entries: 35.
- Counts (I counted each item file in `compendium/content/items/` with the
  batch in place):
  - General items (`part1.py` to `part15.py`): 690 to 725.
  - Player options items on main: 73 (`options_classes.py` 33,
    `options_heritage.py` 40).
  - All original items: 798. Items for the optional systems, if the player
    options session still adds them, are not in this number.
- Build: `compendium/build.sh` passes (212 tests, the content checks, the
  page check, and the font check). GM book: 396 pages. I read GM page 290:
  no text goes out of a box. No name is the same as an SRD item or another
  original item, the options files included. The text is plain ASCII.
- By category: Wondrous 13, Weapon 5, Potion 5, Armor 4, Scroll 4,
  Ammunition 4.
- By rarity: Common 6, Uncommon 11, Rare 8, Very Rare 7, Legendary 3.
- All items in this batch have their own effects, not spells.

## The strongest entries

- Orb of the Turning Stars (Legendary): once per 7 days, you and up to
  eight creatures teleport to a place you have seen on the same plane, with
  no mishap. Like Teleport (level 7) with no chance of error.
- Hammer of the Mountain King (Legendary): +3, push and Prone on a hit (DC
  19 Strength), and once per dawn a 30-foot shockwave (Difficult Terrain,
  DC 19 Dexterity or Prone).
- Scroll of the Second Morning (Legendary, single use): a Long Rest in 1
  minute for you and up to eight creatures, once per 24 hours.
- Saddle of the Sky Steed (Very Rare): your mount has a Fly Speed equal to
  its Speed while you ride it.
- Cloak of the Twin Step (Very Rare): 3 charges, once per turn a Reaction
  teleport of 10 feet that makes a hit miss.
- Sword of the Shared Pain (Very Rare): +2, once per turn an ally regains
  half the damage you deal.
- Shield of the Sheltering Wing (Very Rare): +2 Shield, once per dawn
  Resistance for an adjacent ally against one hit.
- Potion of Stone Flesh (Very Rare): 10 minutes of Resistance to all damage
  except Psychic, with half Speed.
- Scroll of the Iron Ring (Very Rare, single use): +2 AC and Advantage on
  saves for six creatures for 1 minute.
- Arrow of the Shattered Shield (Very Rare, single use): +3d10 Force and -2
  AC for 1 minute.

## Things that I am not sure of

1. Cloak of the Twin Step: three automatic misses each day is strong. It
   needs a Reaction each time. Should it be 2 charges?
2. Saddle of the Sky Steed: flight for a mount at all times gives the
   party flight at level 11 or so. Should it be Legendary, or limited to 1
   hour each dawn?
3. Scroll of the Second Morning: a full Long Rest in a minute can break a
   GM's plans for a day. It is single use and Legendary.

## After this batch

I stop here, as you asked, and wait for your check of the total of 800.
