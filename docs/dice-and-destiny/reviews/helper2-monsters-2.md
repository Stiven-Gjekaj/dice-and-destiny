# Review request: second helper, monsters batch 2 (last 7, grassland and hill)

From: the treasure session, second bestiary helper. Batch 1 is on main
(`4a99574`), with your three changes (Sod Kraken escape, Hungry Meadow
movement and targeting, at most six Zombies for the Barrow Emperor). The
progress file records it.

Batch 2 is ready for review. Nothing is committed yet.

- Files: 3 new monsters at the end of
  `compendium/content/monsters/helper2_grassland.py` and 4 at the end of
  `helper2_hill.py`. Entries: 7.
- Build: `compendium/build.sh` passes (228 tests, the content checks, the
  page check, and the font check). GM book: 448 pages. I read GM page 250
  (Sky Khan): no text goes out of a box. No name is a duplicate.

## The count to 650 (no overlap)

I counted the monsters on main with this batch in place: 591. All open
groups are now taken. The batches that the others plan, from the
bestiary progress file and the first helper's progress file:

| Who | Group | Planned |
|---|---|---|
| First helper | swamp, coast | about 20 |
| Bestiary session | desert | 20 |
| Bestiary session | arctic | 19 |

591 + about 59 = about 650. This batch is the part of the last few that
falls in my own groups (grassland and hill), so no other session writes
there. After it, grassland has 57 and hill 57. I stop here unless you or
the bestiary session ask for more.

## The monsters, each with an SRD equal of the same CR

- Thunder Hare (1/4, grassland): Giant Badger role, a fast alarm animal.
- Chalk Weaver (2, hill): Giant Spider, with a blinding web.
- Siege Ram (9, hill): a construct near a Stone Golem in damage, with a
  charge.
- Boar King of the Downs (13, hill): a high-CR beast monster, near a
  Remorhaz in damage, with Relentless and a charge line.
- Grass-Sea Serpent (15, grassland): a Purple Worm role above ground, with
  invisibility in grass.
- Tor Storm (17, hill): Air Elemental scaled up, with four lashes and hail.
- Sky Khan (23, grassland): Storm Giant role at CR 23, mounted on a storm
  cloud, with legendary actions.

## Things that I am not sure of

1. Grass-Sea Serpent: Invisible while it moves in tall grass. On open
   plains this is a strong defense. Should it be "Heavily Obscured" instead?
2. Sky Khan: damage about 130 a round at CR 23. That is at the top of the
   range of the existing CR 22 to 24 monsters.
