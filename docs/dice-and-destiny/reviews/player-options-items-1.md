# Review request: player options, magic items batch 1

The last spells and feats are on main (518ab4c the counts, f7664e2 the
spells, 98b5ef2 the feats, 7e684e1 the docs, d7ff02d the cover counts).
Spells: 220 of 220. Feats: 120 of 120.

## The batch

- File: `compendium/content/items/options_classes.py` (not committed).
- Entries: 33 magic items: 6 for each of the 4 new classes (24), and 3
  each for Marks, Bonds, and Techniques (9). The Legend paths have no
  content yet (`LEGENDS` is empty), so their items come later.
- Build: `compendium/build.sh` passes. 175 tests pass, the checks are OK.
  Player 276 pages, GM 324. I read GM page 258. The items are in the
  alphabetical list, with no overflow.
- I searched every content file and the SRD magic items for each name. No
  name is in use.
- I read the class features in `content/classes/` and the system rules in
  `content/systems/` and the Marks and Bonds design. I changed none of them.

## The items, by rarity, with the SRD item that each is equal to

| Item | For | Rarity | Attunement | Equal to |
|---|---|---|---|---|
| Signal Whistle of the Line | Captain | Common | no | a small trick |
| Ever-Clean Mortar | Apothecary | Common | no | a small trick |
| Element Stone | Shaper | Common | no | a small trick |
| Spirit Bell | Spiritbinder | Common | no | a small trick |
| Marshal's Baton | Captain | Uncommon | Captain | Wand of the War Mage +1 (range, one free Order each Short Rest) |
| Field Map of the Hundred Battles | Captain | Uncommon | Captain | +1 AC for one round after a plan |
| Bandolier of Quick Vials | Apothecary | Uncommon | no | Gloves of Thievery-type utility |
| Gloves of the Steady Pour | Apothecary | Uncommon | Apothecary | Wand of the War Mage +1 for Vial Toss |
| Bracers of the Focused Will | Shaper | Uncommon | Shaper | Wand of the War Mage +1 for Elemental Bolt |
| Collar of the Bound | Spiritbinder | Uncommon | Spiritbinder | +1 armor and weapon for the spirit |
| Twin Lockets | Bonds | Uncommon | no | Sending-type link |
| Training Weights of the Old Master | Techniques | Uncommon | yes | one extra resource (Pearl of Power-type) |
| Stance Sash | Techniques | Uncommon | no | one free use each Short Rest |
| Standard of the Unbroken Company | Captain | Rare | Captain | Banner aura, 1/day |
| Spyglass of the Watch Captain | Captain | Rare | no | Eyes of the Eagle plus a lore check |
| Alembic of Lasting Brews | Apothecary | Rare | Apothecary | one concoction lasts 3 Long Rests |
| Mask of the Plague Doctor | Apothecary | Rare | yes | Periapt of Proof against Poison |
| Strain Ward Amulet | Shaper | Rare | Shaper | Pearl of Power-type (3 Strain each day) |
| Cinder Heart | Shaper | Rare | Shaper | +Wis damage once a turn, lost on Overstrain |
| Lantern of Returning | Spiritbinder | Rare | Spiritbinder | free return of the spirit, 1/day |
| Talisman of the Shared Breath | Spiritbinder | Rare | Spiritbinder | regain a Bond Point on a kill |
| Charm of the Slow Tide | Marks | Rare | yes | stops one track growth, 1/day |
| Mirror of Hidden Burdens | Marks | Rare | no | shows the shapes of Marks (information) |
| Knot of the Unbroken Bond | Bonds | Rare | no | stops one strain (single use) |
| Oathstone | Bonds | Rare | shared | a larger bond die for one Oath Bond |
| Scroll of Hidden Forms | Techniques | Rare | no | Manual-type, learn one technique (single use) |
| Gorget of Command | Captain | Very Rare | Captain | larger Command Dice, one die back each Initiative |
| Reagent Satchel of the Wandering Healer | Apothecary | Very Rare | Apothecary | +1 concoction each day, a double Field Brewing |
| Crown of the Four Answers | Shaper | Very Rare | Shaper | change element at a Short Rest, +1 DC |
| Ring of the Twin Soul | Spiritbinder | Very Rare | Spiritbinder | spirit HP + 2 x level, share senses |
| Censer of Confession | Marks | Very Rare | no | lowers one track by 1, once in 30 days |
| Mantle of the Calm Storm | Shaper | Legendary | Shaper | Strain Limit +2, one free Overstrain each day |
| Reliquary of the First Binder | Spiritbinder | Legendary | Spiritbinder | +2 Bond Points, the spirit attacks without a command |

## Things that I am not sure of

1. Oathstone makes the bond die of an Oath Bond one size larger, up to
   d12. The Bonds rules stop at d10. If you want to keep d10 as a hard
   limit, I can change it to "a d10 bond die can't shrink from strain".
2. Training Weights of the Old Master give one extra technique point. That
   is the same benefit as the Technique Adept feat (you approved it). With
   both, a character has two extra points.
3. Charm of the Slow Tide and Censer of Confession let a player fight a
   Mark with an item. The GM gives these items, so the GM controls this.
4. Reliquary of the First Binder (Legendary): the bound spirit attacks
   every turn without the Spiritbinder's Bonus Action. This frees the
   Bonus Action for the whole game, so I made it Legendary.

## Next

Items batch 2 is ready: 40 heritage items, 2 for each original species.
