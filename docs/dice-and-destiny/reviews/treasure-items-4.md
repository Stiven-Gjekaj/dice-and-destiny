# Review request: treasure, magic items batch 4

From: the treasure session. Batch 3 is on main (`94abaeb`), with the two
changes from your review. The progress file records it.

Batch 4 is ready for review. Nothing is committed yet.

- File: `compendium/content/items/part7.py`. Entries: 40, all Wondrous
  Items. Original items: 370 to 410.
- Build: `compendium/build.sh` passes (153 tests, the content checks, the
  page check, and the font check). I read GM page 229: no text goes out
  of a box. No name is the same as an SRD item or another original item.
  Each spell that an item names is in the SRD spell data, and the Dire Wolf
  is in the SRD creatures. The text is plain ASCII.
- By rarity: Common 4, Uncommon 10, Rare 12, Very Rare 10, Legendary 4.
  Before this batch, the wondrous items were C31 U61 R32 VR14 L10, so this
  batch adds most to Rare and Very Rare.
- When I read the pages, I found two entries that were too close to
  current items, and I replaced them before this request: a lantern
  (like Gravedigger's Lantern) became Chalk of the Hidden Door, and a
  watch badge (like Helm of the Watch) became Seeker's Compass.

## The strongest entries

- Pocket Watch of the Stopped Moment (Legendary): Time Stop (level 9) once
  every 7 days.
- Mirror of the Hidden Hall (Legendary): Magnificent Mansion (level 7) once
  per dawn.
- Crown of the Unbroken Oath (Legendary): Holy Aura (level 8) once per
  dawn, and Advantage against the Charmed condition.
- Cloak of a Thousand Steps (Legendary): Freedom of Movement at all times,
  and a 30-foot teleport as a Bonus Action once per turn.
- Pelt of the Moonlit Pack (Very Rare): once per dawn, Polymorph into a
  Dire Wolf for you and up to four willing creatures, no Concentration.
- Gloves of the Spellthief (Very Rare): see a spell of level 1 to 5, then
  cast it once with your own slot.
- Cloak of the Starless Night (Very Rare): Invisible in Darkness while you
  move no more than half your Speed.
- Banner of the Last Stand (Very Rare): for 1 minute, each ally within 30
  feet drops to 1 Hit Point instead of 0, once each.
- Drum of the Thundering Host (Very Rare): once per dawn, allies within 60
  feet get +10 Speed, Advantage on attacks, and 10 Temporary Hit Points
  until the end of your next turn.
- Tea Set of the Short Hour (Very Rare): a Short Rest in 1 minute for six
  creatures, once per dawn.
- Bracers of the Mage Hunter (Very Rare): Advantage on saves against
  spells, plus a teleport to the caster on a success. Compare Mantle of
  Spell Resistance (Rare).
- Lens of the Hidden Truth (Very Rare): True Seeing (level 6) once per dawn.
- Orb of the Waking Earth (Very Rare): Tremorsense 60 feet, and Wall of
  Stone with no Concentration once per dawn.

## Things that I am not sure of

1. Cloak of a Thousand Steps: a Bonus Action teleport at will is a large
   change to how a character moves. I put it at Legendary for that reason.
   I can limit it to Proficiency Bonus uses per Long Rest.
2. Gloves of the Spellthief: a character can cast a spell from any class
   list once. Is level 5 the right maximum for Very Rare?
3. Pelt of the Moonlit Pack: a group Polymorph for 1 hour with no
   Concentration. I compared it to five castings of a level 4 spell.
