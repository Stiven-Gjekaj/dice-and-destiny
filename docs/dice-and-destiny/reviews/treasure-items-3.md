# Review request: treasure, magic items batch 3

From: the treasure session. Batch 2 is on main (`d99b9d2`, progress in the
next docs commit). The traps are with the GM tools session (handover sent).

Batch 3 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part6.py`. Entries: 40. Original items:
  330 to 370.
- Build: `compendium/build.sh` passes (128 tests, the content checks, the
  page check, and the font check). I read GM page 238: no text goes out
  of a box. No name is the same as an SRD item or another original item.
  Each spell that an item names is in the SRD spell data. The text is
  plain ASCII.
- By category: Ring 10, Wand 8, Armor 8, Staff 7, Rod 7. These were the
  smallest groups after batch 2 (Rod 7, Staff 8, Wand 10, Ring 15, Armor
  21).
- By rarity: Common 5, Uncommon 11, Rare 11, Very Rare 8, Legendary 5.

## The strongest entries

- Ring of a Hundred Doors (Legendary): 3 charges, Dimension Door (1) or
  Teleport (3). Teleport is level 7, so Legendary in the guide.
- Wand of the Final Word (Legendary): Hold Monster (3 charges) or Power
  Word Stun (5 charges, level 8).
- Staff of the Turning Seasons (Legendary, druid): +3 Quarterstaff, +3
  spell attacks, 20 charges: Plant Growth, Ice Storm, Sunbeam, Control
  Weather (level 8). Compare Staff of the Magi and Staff of Power.
- Rod of the Sealed Gate (Legendary): Banishment (1 charge), Plane Shift
  (3 charges, level 7), and once per dawn a Reaction that stops a teleport.
- Shield of the Dawnless Wall (Legendary): +3 Shield (Very Rare in the SRD)
  plus once per dawn group Evasion for allies within 10 feet.
- Ring of the Bound Storm (Very Rare): Lightning and Thunder Resistance,
  Lightning Bolt (1 charge), Chain Lightning (3 charges, level 6).
- Ring of the Unshaken Mind (Very Rare): Advantage on Int, Wis, and Cha
  saves and on Concentration saves. Compare Ring of Mind Shielding plus the
  War Caster benefit.
- Wand of Withering (Very Rare): Blight (2 charges), Circle of Death (5
  charges, level 6).
- Wand of the Watchful Eye (Very Rare): Arcane Eye (2), Scrying (5).
- Rod of the Unbent Line (Very Rare): Wall of Force once per dawn (level 5).
- Rod of the Second Sun (Very Rare): sunlight, Sunbeam once per dawn
  (level 6).
- Staff of the Long Watch (Very Rare): +2 Quarterstaff, Alarm, Arcane Eye,
  Hold Monster, and you can't be surprised.
- Half Plate of the Glacier (Very Rare): +2, Cold Resistance, and a
  melee attacker that hits you loses 10 feet of Speed.

## Things that I am not sure of

1. Ring of the Unshaken Mind gives Advantage on three saving throws and on
   Concentration. Is that too much for Very Rare? I can limit it to
   Wisdom and Charisma.
2. Staff of the Turning Seasons and the existing Staff of the World Tree
   are both Legendary druid staffs. The spells and the theme are different
   (weather and seasons, not trees and healing).
3. Rod of the Sealed Gate: the Reaction that stops a teleport has no save.
   It works once per dawn. Should the creature get a Charisma save?
