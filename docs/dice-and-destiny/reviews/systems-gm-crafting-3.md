# Review request: Crafting and gathering batch 3 (the last batch)

Workstream: GM optional systems (the classes session).

## State

- On `main`: injuries batch 2 (the full d20 table, 20 injuries), the
  crafting renderer change (the biome check and the gear guard, with 7 new
  tests), the gear section of the chapter with your sentence ("Very Rare and
  Legendary recipes need your permission, and most of them need an adventure
  to find a material"), and crafting batch 2 (24 materials, 24 recipes, 6
  gear recipes).
- Not committed: `compendium/content/crafting/batch3.py`, 10 materials and
  11 recipes. With them, the system has 40 materials and 40 recipes, plus 6
  gear recipes. The guard passes for all of them. `build.sh` passes with the
  batch (BUILD_OK; the Game Master's Compendium is 394 pages).

## Materials (10)

| Material | Source | Rarity |
|---|---|---|
| Bog Myrtle | Swamp | Common |
| Hill Clover | Hill or Grassland | Common |
| Sewer Lichen | Urban | Common |
| Wisp Spark | Will-o'-Wisp (CR 2) | Common |
| Cube Jelly | Gelatinous Cube (CR 2) | Common |
| Ectoplasm | Ghost (CR 4) | Uncommon |
| Shambling Vine | Shambling Mound (CR 5) | Uncommon |
| Salamander Scale | Salamander (CR 5) | Uncommon |
| Medusa Lock | Medusa (CR 6) | Uncommon |
| Storm Gland | Behir (CR 11) | Rare |

The creature names and CRs are from the SRD data. Each rarity matches the CR
band of the chapter.

## Recipes (11, all for original items of this book)

| Item | Rarity | Materials | Gold | Total | Days |
|---|---|---|---|---|---|
| Candle of Calm Sleep | Common | Bog Myrtle | 40 | 50 GP | 5 |
| Lantern of Small Hours | Common | Wisp Spark | 40 | 50 GP | 5 |
| Potion of Bright Eyes | Common, consumable | Hill Clover | 15 | 25 GP | 3 |
| Gloves of Clean Hands | Common | Cube Jelly | 40 | 50 GP | 5 |
| Shroud of the Quiet Dead | Uncommon | Ectoplasm | 150 | 200 GP | 10 |
| Moss Cloak | Uncommon | Shambling Vine | 150 | 200 GP | 10 |
| Potion of Ironskin | Uncommon, consumable | Medusa Lock | 50 | 100 GP | 5 |
| Hilt of Kindling | Uncommon | Salamander Scale (+ base weapon) | 150 | 200 GP | 10 |
| Lockbreaker's Pick | Uncommon | Sewer Lichen, Phase Silk | 140 | 200 GP | 10 |
| Bracers of Thunderous Blows | Rare | Storm Gland | 1,500 | 2,000 GP | 50 |
| Wings of the Storm Rider | Rare | Roc Plume, Storm Gland | 1,000 | 2,000 GP | 50 |

## After this batch

Both GM systems reach their targets: Injuries and scars has the full d20
table (20 injuries), and Crafting and gathering has 40 materials, 40
recipes, and 6 gear recipes. When the systems session puts its BIOMES list
on `main`, I will change the biome check to read from it (one small commit
with a test), as you asked.
