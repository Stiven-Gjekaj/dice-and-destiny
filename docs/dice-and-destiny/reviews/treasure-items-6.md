# Review request: treasure, magic items batch 6

From: the treasure session. Batch 5 is on main (`12aeafd`), with the
changes from your review. The progress file records it.

Batch 6 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part9.py`. Entries: 40. Original items:
  450 to 490.
- Build: `compendium/build.sh` passes (166 tests, the content checks, the
  page check, and the font check). I read GM page 267: no text goes out
  of a box. No name is the same as an SRD item or another original item.
  Each spell that an item names is in the SRD spell data. The text is
  plain ASCII.
- By category: Ring 8, Wand 8, Rod 6, Staff 6, Scroll 6, Ammunition 6.
  These were still the smallest categories (Rod 20, Staff 20, Ammunition
  22, Scroll 23, Wand 24, Ring 25).
- By rarity: Common 3, Uncommon 9, Rare 10, Very Rare 10, Legendary 8.
  Legendary was the smallest rarity after Artifact (38).
- Variety: before I wrote this batch, I listed the SRD spells that no
  original item used. Every spell in this batch except Wall of Stone
  comes from that list, so the batch adds new effects, not new names for
  the same spells.

## The strongest entries

- Arrow of the Last Word (Legendary, single use): Power Word Kill (level 9)
  on a creature with 100 Hit Points or fewer after the hit.
- Scroll of the Sealed Tomb (Legendary, single use): Imprisonment (level
  9), only the Burial, Chaining, or Slumber form.
- Rod of the Silent Field (Legendary): Antimagic Field (level 8) once per
  dawn, centered on the planted rod, with Concentration.
- Rod of the Endless Maze (Legendary): Maze (level 8) once per dawn.
- Wand of the Last Breath (Legendary): Finger of Death (level 7), all 7
  charges.
- Ring of the Second Self (Legendary): Project Image (level 7) once per
  dawn, and you can cast spells through the image.
- Staff of the Blade Storm (Legendary): +3, Spiritual Weapon, Blade
  Barrier, Arcane Sword (level 7).
- Staff of Earth's Fury (Legendary): +3, can't be knocked Prone, Meld into
  Stone, Wall of Stone, Earthquake (level 8).
- Ring of Living Stone (Very Rare): Tremorsense 30 feet, Stoneskin with no
  Concentration once per dawn. Stoneskin is level 4; the missing
  Concentration is the reason for Very Rare.
- Rod of the Stone Shaper (Very Rare): Stone Shape, Passwall, Move Earth
  (level 6).
- Wand of Freezing Spheres (Very Rare): Freezing Sphere (level 6).
- Bolt of the Stone Gaze (Very Rare, single use): Flesh to Stone (level 6)
  with no Concentration.
- Arrow of the Ninefold Rain (Very Rare, single use): nine attacks of 2d10
  each against creatures within 20 feet of a point.

## Things that I am not sure of

1. Ring of the Second Self: casting spells through the image is a strong
   addition to Project Image. I can remove it.
2. Bolt of the Stone Gaze: Flesh to Stone with no Concentration can end a
   creature after three failed saves. Is that correct for Very Rare, or
   should it be Legendary?
3. Arrow of the Last Word: Power Word Kill on an arrow lets a martial
   character use a level 9 effect once. It is single use and Legendary.
