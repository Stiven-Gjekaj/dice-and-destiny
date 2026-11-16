# Review request: the 3 Apothecary subclasses

Workstream: classes and subclasses.

## State

- On `main`: `feat: add the Apothecary class` with your two changes. Master
  Batch is now Perfect Dose (15): a Healing Tonic restores the maximum, once
  each Short Rest. Quick Hands: on a turn when you throw a bomb as a Bonus
  Action, you can't throw another bomb with your action, but you can still
  use Vial Toss.
- The batch is not committed: `compendium/content/subclasses/part11.py`,
  3 entries under `SUBS["apothecary"]`, at levels 3, 6, 10, and 14.
- `build.sh` passed with the batch (BUILD_OK, fonts OK). The Player's
  Compendium is 242 pages. The "Apothecary Subclasses" section starts on
  page 210, after the Spiritbinder subclasses. All the characters in the
  file are ASCII.

## The entries

### 1. Field Surgeon (more healing)

- 3 Triage: a Bonus Action stabilize also heals one Brew Die + Int.
- 3 Steady Hands: a Healing Tonic that you feed to another creature heals
  one more Brew Die.
- 6 Double Dose: when you feed a Healing Tonic, a second creature within 5
  feet of you regains half as much.
- 10 Stitch in Time: a Reaction feeds a Healing Tonic to a creature within 5
  feet that drops to 0 HP.
- 14 Miracle Worker: Revival Draught costs 1 Reagent and 100 GP of herbs,
  and once each Long Rest it costs nothing.

### 2. Grenadier (bombs)

- 3 Bandolier: Int modifier extra concoctions at each Long Rest. They must
  be Fire Bombs or Smoke Bombs.
- 3 Careful Throw: Int modifier creatures automatically succeed and take no
  damage from your bomb (as the Evoker's Sculpt Spells).
- 6 Sticky Mix: a creature that fails against your Fire Bomb has its Speed
  halved until the end of its next turn.
- 10 Cluster Charge: when you throw a bomb, you can throw a second one at a
  different point. A creature in both areas makes one save.
- 14 Grand Detonation: once each Long Rest, combine three bombs into one: a
  30-foot Sphere, two rolls of the Potency dice + Int, Prone on a failure.

### 3. Hexbrewer (poisons and debuffs)

- 3 Bitter Vial (a new concoction): thrown at a creature within 30 feet
  (Utilize, or a Bonus Action with Quick Hands). Con save. On a failure, it
  subtracts one Brew Die from its attack rolls and saves until the end of
  its next turn.
- 3 Envenom: a Bonus Action coats a weapon or 10 pieces of ammunition with
  a Bitter Vial or a Fire Bomb. For 1 minute, a hit deals +1d4 Poison (1d6
  at 10).
- 6 Lingering Fumes: a Fire Bomb leaves fumes until the end of your next
  turn. A creature that enters or starts its turn there makes a Con save or
  has the Poisoned condition until the end of its next turn.
- 10 Toxic Mastery: your Poison damage ignores Resistance. Bitter Vial works
  on a creature with Immunity to Poison damage or to Poisoned.
- 14 Witch's Draught: once each Long Rest, thrown as an action. Con save. On
  a failure, Poisoned and Incapacitated for 1 minute, with a save at the end
  of each of its turns.

## Balance

Concoctions each day for the base class: 5 + 2 at level 5, 8 + 2 at 11,
11 + 2 at 17.

- Field Surgeon: Steady Hands adds one Brew Die to each fed tonic (+4.5 at
  5, +6.5 at 17). Double Dose adds half of a tonic to a second creature.
  That is about +60% healing for each fed tonic. The SRD equal is the Life
  Domain's Disciple of Life and Blessed Healer. Miracle Worker (14) is one
  free Revivify a day. The SRD equal is Life's Supreme Healing.
- Grenadier against the bomb budget: Bandolier gives +3 to +5 concoctions a
  day, but only bombs. Cluster Charge does not add bombs; it spends two in
  one throw. With Quick Hands, the most is 2 bombs in a turn (one Bonus
  Action throw with Cluster Charge), and only Vial Toss with the action. At
  level 11: 2 bombs of 4d10 + 5 = 27 each, in two areas. The total each day
  stays inside the pool. Grand Detonation (14): 2 x 4d10 + 5 = 49 in a
  30-foot Sphere, for 3 bombs, once a day. The SRD equal is a level 5 or 6
  area spell (Cone of Cold is 8d8 = 36). The Grenadier is the highest
  damage of the three. Careful Throw is the SRD Sculpt Spells.
- Hexbrewer: Bitter Vial is like Bane (level 1) for one creature for one
  round, but it costs a concoction. Lingering Fumes uses the SRD Poisoned
  condition with no change. Toxic Mastery: the Resistance part is the same
  as the SRD Elemental Adept feat for Poison. Witch's Draught (14): Poisoned
  and Incapacitated for up to 1 minute, with a save each turn. The SRD
  equal is Hold Monster (level 5), which gives Paralyzed and is stronger.

## Questions

1. Grenadier, Bandolier: +Int modifier bombs each day (up to +5). I can make
   it +PB instead, or only +2.
2. Hexbrewer, Toxic Mastery: "works on a creature with Immunity to Poison"
   only for Bitter Vial (a debuff, no damage). Many undead and constructs
   have that Immunity. I think a debuff from a brew that is not a poison in
   the body can still work, but you may prefer that the Immunity stays.
