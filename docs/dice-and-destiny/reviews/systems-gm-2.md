# Review request: Injuries and scars batch 2, and Crafting and gathering batch 2

Workstream: GM optional systems (the classes session).

## State

- On `main`: batch 1 of both systems, in the planned order (renderer and
  tests, chapter, samples), with your two added sentences in the Injuries
  chapter (the table agrees first; one injury from Critical Hits in each
  turn). Also `fix: name the two GM systems in the description of Part V`
  (one line, with "and two systems for the GM alone: injuries and
  crafting" added at its end).
- Nothing below is committed. `build.sh` passes with all of it (BUILD_OK, 212 tests). I looked at pages 324 and 327 of the Game Master's Compendium: the injuries and the gear table are clean.

## Injuries batch 2 (12 entries, `content/injuries/table.py`)

With these, each d20 result has its own injury (a script checked: 20
entries, rolls 1 to 20, no name used two times).

| d20 | Injury | Effect | Scar |
|---|---|---|---|
| 2 | Split Lip (Minor) | Disadvantage on Performance and Persuasion | Advantage on Deception to hide what you feel |
| 3 | Bruised Knuckles (Minor) | Disadvantage on checks with tools | Unarmed Strikes deal 1 extra damage |
| 5 | Winded (Minor) | no Dash on your first turn of each combat | hold your breath twice as long |
| 6 | Pulled Shoulder (Minor) | Disadvantage on Athletics; no throw past normal range | thrown weapons' normal range +10 feet |
| 7 | Black Eye (Minor) | Disadvantage on Perception by sight | Advantage on Insight to tell whether a creature will attack |
| 9 | Gashed Leg (Minor) | Speed -5, Disadvantage on Acrobatics | long jump +5 feet, high jump +1 foot |
| 10 | Concussion (Minor) | Disadvantage on Intelligence checks | Advantage on saves against Stunned |
| 12 | Torn Muscle (Serious) | Disadvantage on Strength checks and saves | Advantage on Strength checks to escape a grapple |
| 14 | Burned Hands (Serious) | Disadvantage on weapon attacks and tool checks | reduce Fire damage by PB |
| 15 | Infected Wound (Serious) | no HP from spending Hit Point Dice | Advantage on saves against diseases |
| 17 | Dislocated Hip (Serious) | Speed halved | Advantage on Acrobatics to escape a grapple |
| 19 | Crushed Hand (Lasting) | Disadvantage on attacks with that hand, no tools with it; the player chooses lost fingers or a deep wound | Unarmed Strikes with that hand deal 1d6 |

The strongest scars: Fire-Kissed (reduce Fire damage by PB) and Thick Skull
(Advantage against Stunned). Both are narrow. The SRD equal for Fire-Kissed
is smaller than the Heavy Armor Master reduction, which works on all
weapon damage.

## Crafting batch 2

### Renderer change (its own commit, with 7 new tests)

`feat: check the biomes and add gear recipes to the crafting system`:

- A Biome material's `origin` must name SRD biomes ("Arctic", "Coast",
  "Desert", "Forest", "Grassland", "Hill", "Mountain", "Swamp",
  "Underdark", "Underwater", "Urban"), joined by " or ". The Journeys
  system does not exist yet; when it does, the list can follow its biomes.
- A new list `GEAR` (your request): `item` (SRD equipment), `tool`,
  `materials` (can be empty), `gold`, `days`, `note`. The guard reads the
  price from `data/all_items.json` (a name that is there two times keeps
  its higher price) and stops the build if a recipe costs less than 80% of
  half the price, or takes less than 80% of one workday for each 10 GP of
  the price (minimum 1). The workday rule is the chapter's own rule. The
  recipes print as one small table, "Gear Recipes".
- The chapter gets one placeholder (`{{CRAFT_GEAR}}`, one line in
  `build.py`) and a short paragraph "Gear" before the material lists.

### Content (`content/crafting/batch2.py`)

24 more materials and 24 more recipes, and 6 gear recipes. With batch 1:
30 materials and 29 recipes. The guard passes for all of them. Each total
cost equals the base for its rarity (half for a consumable), and the days
are at the base or a little above it (rounded up for half days).

Materials by band: CR 0 to 2 (Glowing Gland from a Giant Fire Beetle,
Stirge Proboscis, Mephit Cinder, Griffon Feather), CR 3 to 6 (Phase Silk,
Basilisk Eye, Hell Hound Ember, Troll Blood, Owlbear Pinion, Elemental
Mote, Unicorn Hair "given freely", Wyvern Stinger), CR 7 to 12 (Hydra Heart,
Frost Giant Marrow, Treant Heartwood, Roc Plume), CR 13 to 18 (Adult Dragon
Scale, Vampire Dust), CR 19+ (Ancient Dragon Heart), and biomes (Shade Moss
in the Underdark, Sun Thistle in Grassland, Glass Sand in the Desert, Storm
Pearl on the Coast, Mountain Heartstone). All creature names are in the SRD
data with those CRs.

Recipes: 4 Common (original items: Ever-Burning Torch Stub, Inkless Quill,
Potion of Warm Hands, Homing Darts), 10 Uncommon (Cloak of Elvenkind,
Slippers of Spider Climbing, Goggles of Night, Periapt of Wound Closure,
Ring of Warmth, Elemental Gem, Potion of Growth, Potion of Poison, Periapt
of Health, Eyes of the Eagle), 5 Rare (Staff of the Woodlands, Boots of
Levitation, Necklace of Fireballs, Potion of Invisibility, Ring of
Resistance), 4 Very Rare (Ring of Regeneration, Frost Brand, Dragon Scale
Mail, Potion of Speed), 1 Legendary (Ring of Elemental Command, which also
needs a bound elemental: "an adventure of its own").

Gear: Potion of Healing (50 GP: 25 in materials and gold, 5 days), Antitoxin
(the same), Alchemist's Fire (the same), Acid (25 GP: 10 gold, 2 days),
Healer's Kit (5 GP: 2 gold, 1 day), Holy Water (25 GP: 10 gold, 2 days, and
a blessing with a level 1 slot).

## Questions

1. Ring of Elemental Command and Ring of Regeneration are strong targets.
   The guard keeps their price and time at the full base (100,000 GP and
   250 days; 20,000 GP and 125 days). Keep them, or leave Legendary items
   out of the recipe lists?
2. The next crafting batch (to about 40 materials and 40 recipes) would add
   mostly Common to Rare recipes for the original items of this book and
   the biomes that are thin now (Hill, Swamp, Urban). Is that the right
   balance?
