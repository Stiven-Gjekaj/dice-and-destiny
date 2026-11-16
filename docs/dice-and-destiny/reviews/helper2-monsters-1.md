# Review request: second helper, monsters batch 1 (grassland and hill)

From: the treasure session, now the second bestiary helper. The general
magic items are done (`c21414a`, 725 items).

I took grassland and hill, as whole groups from "Open for a helper" in
`progress-bestiary.md` (my claim is in `progress-treasure-and-tools.md`).
These two have the biggest gaps at CR 17 to 24.

Batch 1 is ready for review. Nothing is committed yet.

- Files: `compendium/content/monsters/helper2_grassland.py` (16) and
  `helper2_hill.py` (14). Entries: 30.
- After this batch: grassland 38 to 54, hill 39 to 53.
- Build: `compendium/build.sh` passes (228 tests, the content checks, the
  page check, and the font check). GM book: 432 pages. I read GM page 229
  (Queen Beneath the Hill): no text goes out of a box.
- I read `grassland.py`, `hill.py`, and the grassland and hill monsters of
  `part1.py` to `part4.py` first. No name is the same as another monster,
  and no monster repeats the role of one in the same environment. The
  SRD creatures named in the text (Warhorse, Zombie, Wyvern) are in the SRD
  data, and Barrow Thane is an original monster.
- AC and HP come from the engine (only default HP multipliers; AC set by
  hand only on a few low-CR and armored creatures, all within the limits).
  Damage uses {dc:...}, {atk:...}, and dice in the text. I checked the
  damage per round of each monster against the existing files and the SRD
  (about 55 at CR 11, 90 at CR 18, 100 to 120 at CR 20 to 24), and I added
  a third attack to six monsters that were low.

## CR spread

| Environment | 0 to 1 | 2 to 4 | 5 to 10 | 11 to 16 | 17 to 24 |
|---|---|---|---|---|---|
| grassland | 2 | 2 | 2 | 5 | 5 |
| hill | 2 | 2 | 2 | 4 | 4 |

## Each monster with an SRD equal of the same CR

Grassland:

- Locust Cloud (1/2): Swarm of Insects. Scarecrow Watcher (1): Animated
  Armor. Dust Devil Hound (2): Dust Mephit role, stronger bite. Butcher
  Shrike (3): Giant Eagle with a grapple and impale.
- Mound Serpent (7): Giant Constrictor Snake scaled up. Mirage Stag (8):
  Displacement-style defense, a charm like a Succubus lure.
- Thunderwing (11): Roc. Sod Kraken (12): a buried tentacle monster, near
  a Remorhaz in damage. Khan of the Endless Ride (13): Vampire role, mounted
  archer. Steppe Behemoth (14): a high-CR beast, near a Purple Worm in hit
  points. Sun Lion (16): a Planetar-like celestial beast with a breath-like
  roar.
- Famine Rider (17): a horseman fiend, near a Death Knight. Cloud Grazer
  (19): a sky whale, near an Ancient Bronze Dragon in damage. Plainsunder
  Wurm (21): a bigger Purple Worm. The Hungry Meadow (22): a plant swarm, no
  SRD equal; damage near a Kraken. Ancient Horizon Dragon (24): Ancient Red
  Dragon role, with Thunder breath.

Hill:

- Cairn Adder (1/4): Venomous Snake. Drystone Walker (1): Animated Armor.
  Gorse Boar (2): Giant Boar. Barrow Hound (3): Death Dog role.
- Dolmen Witch (6): a hag role (Green Hag, but stronger). Beacon Spirit (7):
  Fire Elemental scaled up.
- Downs Wyvern Matriarch (11): a big Wyvern. Two-Headed Hill Tyrant (12):
  Ettin scaled up, with new rules. Stonecircle Witch (14): an Archmage-like
  caster tied to stones. Bonfire Giant (15): Fire Giant role.
- Mother of Cairns (18): an earth titan, no SRD equal; near a Kraken at
  lower damage. Barrow Emperor (20): Lich role, melee. Ancient Barrow
  Dragon (22): Ancient Green Dragon role, with Necrotic breath. Queen
  Beneath the Hill (23): a fey queen, no SRD equal; near a Solar in damage.

## Things that I am not sure of

1. Sod Kraken: four Tentacle attacks plus Drag Under, which suffocates.
   Is CR 12 right, or should it be 13?
2. The Hungry Meadow is a 60-foot square that other creatures can share.
   This is new for a creature. Is a field as a creature clear enough in the
   book?
3. Barrow Emperor: Command of the Dead turns killed Humanoids into Zombies.
   Is that too much on top of the summoned Barrow Thanes?
