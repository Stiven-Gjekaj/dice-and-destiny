# Review request: player options, backgrounds batch 2

Origin feats batch 1 is on main (5d1c579, docs 8a7824a). Feats: 65 of 120.

## The batch

- File: `compendium/content/backgrounds/far_places.py` (not committed).
- Entries: 10 backgrounds. Backgrounds: 30 to 40 of 40.
- Build: `compendium/build.sh` passes. 81 tests pass, the checks are OK
  (this includes the new feat check). Player 238 pages, GM 237. I read
  pages 211 to 215. The boxes are in alphabetical order, and there is no
  overflow.

Each background uses one of the new origin feats, except the Night
Watchman (Alert). The places are the regions that batch 1 covered less.

| Background | Region | Abilities | Skills | Tool | Feat |
|---|---|---|---|---|---|
| Whaler | Open sea | Str, Con, Wis | Athletics, Survival | Water Vehicles | Sea Legs |
| Island Wayfinder | Islands | Int, Wis, Cha | Nature, Survival | Navigator's Tools | Sea Legs |
| Salt Trader | Deep desert | Con, Int, Cha | Persuasion, Survival | Weaver's Tools | Desert Walker |
| Envoy | Court | Int, Wis, Cha | History, Insight | Calligrapher's Supplies | Courtly Poise |
| Gang Runner | City underworld | Dex, Con, Cha | Athletics, Stealth | Gaming Set | Streetwise |
| Temple Guard | Temple | Str, Con, Wis | Athletics, Religion | Smith's Tools | Steadfast Faith |
| Steppe Scout | Steppe | Dex, Con, Wis | Animal Handling, Perception | Leatherworker's Tools | Born Rider |
| Goatherd | Mountains | Str, Dex, Wis | Animal Handling, Athletics | Musical Instrument (pipes) | Crag Walker |
| Deep Forager | Deep caves | Con, Int, Wis | Nature, Survival | Cook's Utensils | Cave Eyes |
| Night Watchman | City at night | Str, Con, Wis | Insight, Perception | Thieves' Tools | Alert |

## Checks that I ran

- No name is the same as an SRD background or an original background.
- The equipment in option A is 50 GP or less at SRD prices.
- After this batch, no origin feat is used more than 4 times in the 40
  backgrounds (Hardy 4).

## Things that I am not sure of

1. Night Watchman has Thieves' Tools (taken from thieves). The SRD Criminal
   has the same tool. The skills and the role are different.
2. Whaler: "Harpoon (Spear)" uses the Spear statistics. I did not add a new
   weapon.

## Next

Spells batch 2 is ready (11 spells for the thin class lists: Bard 2 to 5,
Paladin 2, Ranger 4, Druid 6 and 7, Cleric 7, Sorcerer 5 to 9, Warlock 9).
I send it after this batch is on main.
