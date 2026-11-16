# Review request: treasure, magic items batch 8

From: the treasure session. Batch 7 is on main (`db20758`), with the
changes from your review. The progress file records it.

Batch 8 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part11.py`. Entries: 40. Original items:
  530 to 570.
- Build: `compendium/build.sh` passes (171 tests, the content checks, the
  page check, and the font check). GM book: 326 pages. I read GM page
  277: no text goes out of a box. No name is the same as an SRD item or
  another original item. Each spell that an item names is in the SRD spell
  data. The text is plain ASCII.
- By category: Weapon 20, Ring 7, Rod 7, Wand 6. No weapons were added
  since batch 2, and Rod (31), Wand (32), and Ring (33) were among the
  smallest categories.
- By rarity: Common 5, Uncommon 9, Rare 11, Very Rare 8, Legendary 7.
- None of these items is for a new class, an original species, or an
  optional system, so they don't overlap the player options items.
- As in batches 6 and 7, each spell comes from the list of SRD spells that
  no original item used before.

## The strongest entries

- Whip of the Beast Lord (Legendary): +3, Dominate Monster (level 8) once
  per dawn.
- Blade of the Divine Word (Legendary): +3, Divine Word (level 7) once per
  dawn.
- Crossbow of the Slow Fuse (Legendary): +3, Delayed Blast Fireball (level
  7) once per dawn.
- Wand of the Sevenfold Wall (Legendary): Prismatic Wall (level 9), all 7
  charges.
- Ring of the Wandering Soul (Legendary): Astral Projection (level 9) on
  yourself once per 7 days.
- Rod of the Shunned Ground and Rod of the Empty Mind (Legendary):
  Antipathy/Sympathy or Befuddlement (level 8) once per dawn.
- Ring of the Waiting Spell (Very Rare): Contingency (level 6) once per 7
  days, for a spell of level 5 or lower.
- Wand of the Restless Grave (Very Rare): Animate Dead (3), Create Undead
  (6 charges, level 6).
- Greatsword of the Watchful Spirit (Very Rare): +3, Guardian of Faith once
  per dawn.
- Lance of the Faithful Steed (Very Rare): +3, Find Steed with a Fly Speed
  once per dawn.
- Maul of the Giant's Grip (Very Rare): +2, Enlarge on yourself for 1
  minute, no Concentration, once per dawn.
- Flail of Confusion (Very Rare): +2, Confusion (level 4) once per dawn.

## Things that I am not sure of

1. Rapier of the Quick Riposte (Uncommon): +1 and a Reaction attack once
   per Short Rest. Is the Reaction attack too much for Uncommon? I can
   make it once per dawn.
2. Moon-Edge Scimitar and Mace of the Sacred Flame (Uncommon): each gives
   an attack cantrip at will, so a non-caster gets a ranged attack. Is that
   correct for Uncommon?
3. Wand of the Restless Grave: Create Undead from a wand gives a player a
   strong army over time. Should it be Legendary, or should the undead last
   only 24 hours?
