# Review request: the 3 Spiritbinder subclasses

Workstream: classes and subclasses.

## State

- On `main`: `ee8bb0b feat: add the Spiritbinder class` (Interpose once
  each round, Joined Souls gives half of the spirit's HP), and the progress
  docs.
- A fix commit goes with this request:
  `fix: recommend Epic Boons and backgrounds that are in the SRD`. The
  Shaper and the Spiritbinder recommended Boon of Fortitude, and the
  quick builds named the Hermit background. Neither is in the SRD 5.2 data
  (`data/all_feats.json`, `data/all_backgrounds.json`). The Shaper now
  recommends Boon of Irresistible Offense and the Sage. The Spiritbinder
  now recommends Boon of Fate and the Acolyte.
- The batch is not committed: `compendium/content/subclasses/part10.py`,
  3 entries under `SUBS["spiritbinder"]`, at levels 3, 6, 10, and 14.
- `build.sh` passes with the batch (BUILD_OK, fonts OK, no Type 3). The
  Player's Compendium is 236 pages. I looked at page 209: the "Spiritbinder
  Subclasses" heading follows the Shaper subclasses, and the text is clean.
  All the characters in the file are ASCII.

## The entries

### 1. Bond of the Great Beast (a bigger, stronger spirit)

- 3 Mighty Spirit: the spirit's HP maximum + 2 x Spiritbinder level. Spirit
  Strike is 1d10 (1d12 in Claw Form) instead of 1d6 (1d8).
- 3 Pack Sense: you and the spirit have Advantage on Perception within 30
  feet of each other, and neither can be Surprised.
- 6 Grown Spirit: the spirit is Large, its reach is +5 feet, and a creature
  of your size or smaller can ride it.
- 10 Rampage: when the spirit drops a creature to 0 HP, it moves half its
  Speed and makes one more Spirit Strike (no action).
- 14 Titan Soul: the spirit has Resistance to Bludgeoning, Piercing, and
  Slashing, and Spirit Strike deals +1d8 Force.

### 2. Bond of the Twin Lights (a second spirit for support only)

- 3 Wisp: a Tiny wisp (AC 13 + PB, 1 HP, Fly 30, Bright Light 10 feet). It
  can't attack. It moves with the spirit. When you command the spirit, the
  wisp can also take the Help action. It does not need its own command, so
  it is not a second attacker.
- 3 Carried Light: Mend can target a creature within 30 feet of the wisp
  and heals + Cha more.
- 6 Guiding Glow: you and allies within 10 feet of the wisp add 1 to saves.
- 10 Soul Shelter: a Reaction and 2 Bond Points: an ally within 30 feet of
  the wisp drops to 1 HP instead of 0.
- 14 Thousand Wisps: a Bonus Action and 3 Bond Points: each chosen ally
  within 30 feet of the wisp regains 2d8 + Cha HP and can end one of
  Blinded, Charmed, Frightened, or Poisoned.

### 3. Bond of the Spirit Mantle (wear the spirit as armor)

- 3 Wear the Spirit: a Bonus Action. While worn, the spirit takes no turns.
  You use its AC if it is higher. With the Attack action, you make Spirit
  Strikes (its bonus and damage, the number in the Spirit Attacks column) in
  place of your weapon attacks. Damage goes to the spirit's HP first. At 0
  HP, the spirit returns to your soul.
- 3 Mantle Training: Shields and Martial weapons.
- 6 Mantle Step: +10 feet of Speed while worn, and one free Pounce each
  turn.
- 10 Lashing Shroud: reach 10 feet while worn, and a Reaction Spirit Strike
  when a creature enters your reach.
- 14 Spirit Fury: a critical range of 19 to 20 while worn, and one free
  Unsettle each turn.

## Balance

Damage a round, 65% to hit, Cha +4 at 5, +5 at 11 and 17. The base class
(Claw Form, spirit plus your crossbow) is 14.6 at 5, 21.8 at 11, and 30.9
at 17.

- Great Beast: Claw 1d12 instead of 1d8 is +2 a hit. At 5: 2 x (6.5 + 4) x
  0.65 = 13.7 + 3.6 = 17.3 (base 14.6). At 11: 2 x (6.5 + 5 + 4.5) x 0.65 =
  20.8 + 3.6 = 24.4. At 17 with Titan Soul: 3 x (6.5 + 5 + 9) x 0.65 = 40.0
  + 3.6 = 43.6. Spirit HP at 17: 90 + 34 = 124. The SRD equal is the
  Berserker's Frenzy (3) and Retaliation (10). Level 14 to 17 is the
  highest number in the workstream, so this is the entry that I am least
  sure of. I can drop the extra 1d8 of Titan Soul and keep the Resistance.
  Then level 17 is 3 x 16 x 0.65 + 3.6 = 34.8.
- Twin Lights: no damage. The wisp helps with the spirit's command. Carried
  Light is about +4 healing for each Mend. Soul Shelter is the same idea as
  the Captain's Unfallen Colors. Thousand Wisps (14) heals about 14 for each
  ally in range for 3 Bond Points. The SRD equal is the Life Domain's
  Preserve Life.
- Spirit Mantle: you attack with the spirit, and the spirit does not act.
  The damage is the same as the base class, without your crossbow (at 5:
  11.1). Your AC is 13 + PB (16 at 5, 19 at 17), plus a Shield. Lashing
  Shroud adds a Reaction attack. The SRD equal is the Fighter's Champion
  for a melee character. The spirit's HP pool stands in front of yours, as
  the base class spirit does when enemies attack it.

## Questions

1. Great Beast at 17: keep Titan Soul's +1d8, or only the Resistance?
2. Spirit Mantle: damage to you goes to the spirit's HP first, which is
   like Polymorph. With Mend (1d8 + Cha for 1 point) you can heal the
   spirit. Is this too much defense for a melee character? I can make the
   spirit take only half of the damage.
