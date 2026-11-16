# Review request: NPC batch 2

## Batch

- Files: `compendium/content/npcs/wilds.py` (16) and
  `compendium/content/npcs/towns.py` (14). New, not committed.
- Entries: 30 NPCs. NPCs go from 30 to 60.
- The batch fills the three thin roles of batch 1 and adds everyday people.

## Build

- `compendium/build.sh` passes on `main` (166 tests, the content checks, the
  page check, and the font check). I built this batch alone, without the
  forest batch.
- The GM book part page now says "406 new monsters and 60 people with full
  stat blocks". The count comes from the content.
- I examined page 251 as an image. No text goes out of a box, and the numbers
  are correct.

## Spread

- Roles: Wilderness Folk 6, Scholars and Mages 5, Assassins and Duelists 5,
  Merchants and Townsfolk 4, Guards and Soldiers 2, Nobles and Officials 2,
  Priests and the Faithful 2, Criminals and Spies 2, Cultists 1, Sailors and
  Pirates 1.
- Totals with batch 1: Guards 7, Nobles 6, Priests 7, Merchants 7,
  Criminals 5, Cultists 4, Sailors 4, Scholars 7, Wilderness 7, Assassins 6.
- CR: 1/8: 3, 1/4: 2, 1/2: 2, 1: 3, 2: 3, 3: 3, 4: 1, 5: 3, 6: 3, 7: 1, 8: 2,
  9: 1, 10: 1, 11: 1, 13: 1.
- No name is an SRD name, an original monster, or an NPC of batch 1. Every
  spell name is in the SRD 5.2. I checked both with a script. (The script
  found "Thorn Whip", which is not in the SRD 5.2. I changed it to
  Shillelagh.)

## Strongest entries and the SRD entry that each is equal to

- **Shadow Envoy** (CR 13): 3 dagger attacks at 20 plus Sneak Attack 6d6
  (about 81 a round), Evasion, Dimension Door, Dominate Person, and Greater
  Invisibility 1/Day. Equal to Assassin (CR 8) plus 5 for spells and
  damage.
- **Warden of the Wilds** (CR 11): 2 attacks (Moonfire 5d10 Radiant at range,
  or scimitar with Poison), Conjure Animals, Ice Storm, Wall of Thorns 1/Day,
  a Brown Bear shape 1/Day. Equal to Druid (CR 2) at the level of a CR 11
  boss.
- **Spymaster of the Crown** (CR 10): 2 sword-cane attacks at 23.5, a charm
  that deals 6d8 Psychic, Signal lets two allies attack as a Reaction. Equal
  to Spy (CR 1) at the level of a CR 10 boss.
- **Grave Scholar** (CR 9): 2 Necrotic bolts at 18, Animate Dead,
  Counterspell, Vampiric Touch 1/Day, and 1d4 + 2 SRD Zombies or Skeletons.
  Equal to Mage (CR 6) plus 3 for the servants.

## Not sure

1. **Companions from the SRD.** The Beast Tamer has a Wolf, Brown Bear, or
   Giant Eagle. The Mounted Lancer rides a Warhorse. The Grave Scholar has
   1d4 + 2 Zombies or Skeletons. The CR of each NPC does not count the
   companion. The SRD Druid and Mage stat blocks do the same.
2. **Royal Guard** (CR 6): "Take the Blow" moves a hit from its charge to
   itself. "Sworn Protector" imposes Disadvantage on an attack against its
   charge with no action. Together they are strong for one guard, but they
   only protect one creature.
3. **Masked Executioner** (CR 8): it scores a Critical Hit on 19 or 20 against
   a Prone, Restrained, or Grappled creature.

## Next

After approval: `feat: add 30 NPC stat blocks` (batch 2), then the progress
docs commit. Then the next monster batch (planar or mountain, 21 each).
