# Review request: treasure, magic items batch 9

From: the treasure session. Batch 8 is on main (`60998cd`), with the
changes from your review (the Greatsword and the Lance are now +2 and
Very Rare). The progress file records it.

Batch 9 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part12.py`. Entries: 40. Original items:
  570 to 610.
- Build: `compendium/build.sh` passes (175 tests, the content checks, the
  page check, and the font check). GM book: 333 pages. I read GM page
  273: no text goes out of a box. No name is the same as an SRD item or
  another original item (the `options_*.py` files included). Each spell
  that an item names is in the SRD spell data. The text is plain ASCII.
- By category: Wondrous 15, Ammunition 7, Staff 6, Scroll 6, Armor 6.
  After batch 8 the smallest were Staff (31), Ammunition (33), Scroll
  (34), and Armor (39).
- By rarity: Common 11, Uncommon 10, Rare 8, Very Rare 7, Legendary 4.
  Common was the smallest of the main rarities (76), so this batch adds
  more Common items: small tricks and comforts with no bonus to a roll.
- As before, each spell comes from the list of SRD spells that no original
  item used before.

## The strongest entries

- Staff of the Celestial Choir (Legendary, cleric or paladin): +3,
  Prayer of Healing, Conjure Celestial (level 7), Power Word Heal (level
  9, 9 charges).
- Arrow of the Burning Cloud (Legendary, single use): Incendiary Cloud
  (level 8) for 1 minute with no Concentration.
- Scroll of the Second Body (Legendary, single use): Clone (level 8) with
  the scroll as the vessel.
- Studded Leather of the Ghost Step (Legendary): +3, Etherealness (level 7)
  on yourself once per dawn.
- Arrow of Harm (Very Rare, single use): Harm (level 6).
- Scroll of the Binding Oath (Very Rare, single use): Geas (level 5).
- Scroll of the Guarded House (Very Rare, single use): Guards and Wards
  (level 6).
- Bell of Hallowed Ground (Very Rare): Hallow (level 5) once per 7 days.
- Staff of the Awakened Wood (Very Rare, druid): +2, Commune with Nature,
  Awaken, Conjure Fey (level 6).
- Staff of Planar Binding (Very Rare): +2, Planar Binding, Planar Ally
  (level 6).
- Plate of the Untouched (Very Rare): +2, Antilife Shell (level 5) once per
  dawn.

## Things that I am not sure of

1. Staff of the Celestial Choir: Power Word Heal from a staff that regains
   charges is strong. I set it to 9 charges of 20, so it works at most
   about once each day.
2. Druid's Walking Staff (Uncommon): Shillelagh and Guidance at will with
   no other benefit. Is that enough for Uncommon, or should it be Common?
3. Half Plate of the Living Aura (Rare): +1 and Aura of Life (level 4) once
   per dawn. Level 4 is at the top of the Rare range in the guide.
