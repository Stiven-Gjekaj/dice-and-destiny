# Review request: treasure, magic items batch 10

From: the treasure session. Batch 9 is on main (`ef501fd`); the Druid's
Walking Staff now requires attunement by a druid or a ranger. The progress
file records it.

Batch 10 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part13.py`. Entries: 40. Original items
  in the general categories: 610 to 650. (On main, `content/items/` has no
  `options_*.py` file yet, so the count on main is 610 before this batch.)
- Build: `compendium/build.sh` passes (180 tests, the content checks, the
  page check, and the font check). GM book: 354 pages. I read GM page
  275: no text goes out of a box. No name is the same as an SRD item or
  another original item. Each spell that an item names is in the SRD spell
  data. The text is plain ASCII.
- By category: Wondrous 24, Potion 8, Ring 4, Weapon 4.
- By rarity: Common 5, Uncommon 13, Rare 11, Very Rare 6, Legendary 5.
- More of these items have their own effects instead of a spell (for
  example Cape of the Diving Hawk, Paired Courier Satchels, Greataxe of
  the Sundered Ward). When I read the page, one entry was too close to
  Mantle of the Duskling (Darkvision 120 feet), so I changed Eye of the
  Watchful Owl to sight-based Perception and See Invisibility.

## The strongest entries

- Potion of the True Shape (Legendary): True Polymorph on yourself for 1
  hour, into a creature of CR up to your level, no Concentration.
- Mask of the Second Self (Legendary, spellcaster): Simulacrum (level 7)
  once per 30 days, no costly materials; only one simulacrum at a time.
- Chalk of the Final Sign (Legendary): Symbol (level 7), 3 uses, once per 7
  days.
- Ring of the Closed Mind (Legendary): Mind Blank (level 8) on yourself
  once per dawn.
- Greataxe of the Sundered Ward (Legendary): +3, ignores Resistance, and
  Immunity becomes half damage.
- Rapier of the Mad Dance (Very Rare): +2, Irresistible Dance (level 6) on
  a hit once per dawn.
- Ring of the Called Blade (Very Rare): Instant Summons (level 6) once per
  dawn for one bound object.
- Glove of the Far Reach, Crystals of the Shared Mind, Dragon Egg Pendant
  (Very Rare): Telekinesis, Telepathic Bond, or Summon Dragon (level 5)
  once per dawn.
- Potion of the New Body (Very Rare): Reincarnate (level 5).

## Things that I am not sure of

1. Greataxe of the Sundered Ward: turning Immunity into Resistance is a
   strong effect against some monsters. Is it right for Legendary?
2. Cape of the Diving Hawk (Rare): +3d6 on an attack after a fall of 30
   feet or more. It needs height, so I think it is fair at Rare.
3. Potion of the True Shape: the CR limit is the drinker's level. Should it
   be lower (for example half the level)?
