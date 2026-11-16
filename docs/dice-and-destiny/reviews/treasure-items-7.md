# Review request: treasure, magic items batch 7

From: the treasure session. Batch 6 is on main (`530e5b6`), with the
changes from your review. The progress file records it.

Batch 7 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part10.py`. Entries: 40. Original items:
  490 to 530.
- Build: `compendium/build.sh` passes (166 tests, the content checks, the
  page check, and the font check). I read GM page 251: no text goes out
  of a box. No name is the same as an SRD item or another original item.
  Each spell that an item names is in the SRD spell data. The text is
  plain ASCII.
- By category: Armor 10, Potion 10, Rod 5, Staff 5, Ammunition 5,
  Scroll 5. After batch 6 the smallest were Rod 26, Staff 26, Ammunition
  28, Armor 29, and Scroll 29. Potions had no new entries since batch 2.
- By rarity: Common 5, Uncommon 9, Rare 9, Very Rare 10, Legendary 7.
- As in batch 6, each spell comes from the list of SRD spells that no
  original item used before.

## The strongest entries

- Arrow of the Fire Storm (Legendary, single use): Fire Storm (level 7),
  DC 19.
- Breastplate of the Second Heart (Legendary): +3, Regenerate (level 7) on
  yourself once per dawn.
- Plate of the Shining Globe (Legendary): +3, Globe of Invulnerability
  (level 6) once per dawn. +3 Plate is Very Rare in the SRD, so the Globe
  makes it Legendary.
- Potion of the Last Light (Legendary): equal to Power Word Heal (level 9)
  on the drinker.
- Rod of the Upside-Down Sky (Legendary): Reverse Gravity (level 7) once
  per dawn.
- Staff of the Mirage (Legendary): +3, Mislead, Programmed Illusion,
  Mirage Arcane (level 7).
- Scroll of the Hidden Vault (Legendary, single use): Sequester (level 7).
- Bolt of Disintegration (Very Rare, single use): Disintegrate (level 6).
- Scroll of the Returning Soul (Very Rare, single use): Raise Dead (level
  5) with no diamond.
- Splint of the Sanctified Guard (Very Rare): +2, Necrotic Resistance,
  Death Ward once per dawn.
- Studded Leather of the Unseen (Very Rare): +2, Greater Invisibility on
  yourself once per dawn.
- Potion of the Wind Road (Very Rare): Wind Walk (level 6), drinker only.
- Staff of the Wild Elements (Very Rare): +2, Fireball, Conjure Minor
  Elementals, Vitriolic Sphere.
- Rod of the Iron Hand and Rod of Second Thoughts (Very Rare): Arcane Hand
  or Modify Memory (level 5) once per dawn.

## Things that I am not sure of

1. Ring Mail of the Turning Weather (Rare): Protection from Energy with no
   Concentration while you wear the armor, once per dawn. Is that too
   much for Rare with a +1 bonus?
2. Arrow of the Red Iron (Rare): Heat Metal damage each turn for 1 minute
   with no Bonus Action needed. The target can end it by dropping the
   object or taking it off, but armor takes a long time to doff.
3. Potion of the Last Light: a full heal is strong at high levels. It is
   single use and Legendary.
