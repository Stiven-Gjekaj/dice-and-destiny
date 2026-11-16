# Review request: treasure, magic items batch 5

From: the treasure session. Batch 4 is on main (`f364d06`), with the
changes from your review. The progress file records it.

Batch 5 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part8.py`. Entries: 40. Original items:
  410 to 450.
- Build: `compendium/build.sh` passes (153 tests, the content checks, the
  page check, and the font check). I read GM page 258 (the artifacts): no
  text goes out of a box. No name is the same as an SRD item or another
  original item. Each spell that an item names is in the SRD spell data.
  The text is plain ASCII.
- By category: Scroll 10, Ammunition 8, Rod 6, Staff 5, Wand 6, and 5
  artifacts (4 Wondrous, 1 Weapon). These were the smallest categories
  (Scroll 13, Ammunition 14, Rod 14, Staff 15, Wand 18), and Artifact was
  the smallest rarity (6).
- By rarity: Common 4, Uncommon 8, Rare 10, Very Rare 8, Legendary 5,
  Artifact 5.
- The item renderer shows the text as it is, with no bold labels. So the
  artifacts use plain labels such as "Curse:" and "Destroying the Blade:".
- When I read the artifact page, I found that one draft (a book that binds
  agreements) was too close to The Ledger of All Debts. I replaced it with
  The Chalice of the Second Spring. I made it a cup, not a seed, so that
  it does not look like The World Tree Seed.

## The artifacts

Each has a benefit while attuned, charges or a strong use, a curse or a
price, and a way to destroy it.

- The Lantern of the First Dawn: sunlight; Resistance to Necrotic and
  Radiant; Fiends and Undead in its light can't heal; Daylight, Sunbeam,
  Sunburst; once per 7 days it destroys Undead of CR 10 or lower within
  60 feet.
- The Chalice of the Second Spring: Plant Growth and Speak with Plants at
  will; Revivify, Mass Cure Wounds, Heal; once per year it heals 10 miles
  of land. Curse: 4 hours of sunlight each day.
- The Tidebell: breathe water, Swim 60, Cold Resistance; Control Water,
  Conjure Elemental, Tsunami (level 8). Curse: Tsunami can call a sea
  creature of CR 15 or lower.
- The Nameless Blade: +3 Longsword, +2d6 Necrotic; learns the names of
  the creatures it kills, which only Wish or True Resurrection can return
  to life; once per dawn Disadvantage on saves against you. Curse: no
  other weapon, and you forget your name each dawn.
- The Ninth Key: opens any lock; Plane Shift once per dawn; Gate once per
  7 days. Curse: a Gate can let something hostile through.

## The strongest entries that are not artifacts

- Arrow of the Falling Star (Legendary, single use): one meteor of Meteor
  Swarm (10d6 Fire + 10d6 Bludgeoning, DC 19, 40-foot Sphere).
- Staff of the Unbound Sky (Legendary): +3, Fly, Chain Lightning, Control
  Weather, Storm of Vengeance (level 9). Compare Staff of the Magi.
- Rod of the Locked Room (Legendary): Forcecage (level 7) once per dawn.
- Wand of Seven Colors (Legendary): Prismatic Spray (level 7, all 7
  charges) or Color Spray (1 charge).
- Scroll of the Last Refuge (Legendary, single use): Demiplane (level 8)
  that stays for 7 days.
- Scroll of the Severed Bond (Very Rare, single use): equal to Dispel Evil
  and Good (level 5) plus the end of curses.
- Staff of the Ninefold Gate (Very Rare): +2, Misty Step, Dimension Door,
  Teleportation Circle.
- Staff of the Long Winter (Very Rare): +2, Cold Resistance, Ice Storm,
  Cone of Cold, Wall of Ice (level 6).
- Rod of Ashes (Very Rare): Fire and Poison Resistance, Cloudkill (level 5)
  once per dawn.
- Rod of the Shepherd King (Very Rare): Mass Suggestion (level 6) once per
  dawn.
- Wand of the Hollow Mind (Very Rare): Suggestion, Dominate Person (level
  5).
- Arrow of the Bound Storm and Sling Stone of Stillness (Very Rare, single
  use): 4d10 + two leaps of 4d10; Paralyzed like Hold Monster.

## Things that I am not sure of

1. Scroll of the Second Breath (Rare, single use): a Reaction Revivify with
   no material cost. Is the Reaction too strong for Rare?
2. The Lantern of the First Dawn destroys Undead of CR 10 or lower with no
   save, once per 7 days. I think that is right for an artifact, but I can
   give the Undead a save.
3. The Nameless Blade: no return to life except by Wish or True
   Resurrection. This is strong against the players if a villain holds it.
