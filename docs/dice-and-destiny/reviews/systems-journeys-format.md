# Review request: systems, batch 9 (Journeys: format, renderer, rules)

Systems batch 9: the format of a Journey biome entry, the renderer and its
tests, and the rules text of Journeys (no biomes yet). Not committed. The
Legend paths of batch 8 are also in the working copy, not committed.
build.sh passes with both: 190 tests, content check, page check, Type 3
check. GM 358 pages. No em-dash.

## Files

Proposed commits (after approval):

1. `feat: render the Journey biomes of the optional systems`
   - `compendium/content/systems/__init__.py`: the format, and `BIOMES`.
   - `compendium/build/render_systems.py`: `biome_errors`, `biome_html`,
     `biomes_html`, `all_biomes_html`.
   - `compendium/tests/test_render_systems.py`: 10 new tests.
   - `compendium/build/check_content.py`: the "systems" line also reads the
     names of `BIOMES`.
2. `feat: add the Journeys chapter`
   - `compendium/books/gm.src.html`: the chapter "Journeys" after "Running
     Legend Paths" (the build numbers it: Chapter 25), with the placeholder
     `{{SYS_BIOMES}}`. The heading "Biomes" comes with the biome entries.
   - `compendium/build/build.py`: the placeholder and the chapter icon.

## Format

Biome (dict): name, summary, navigate (DC 5 to 25), forage (DC 5 to 25),
weather (exactly 6 rows of (name, effect), for a d6), encounters (exactly 8
texts, for a d8). The book shows the DCs, a d6 weather table, and a d8
encounter table for each biome, in the order of the names.

## The rules that I set (the design gives the parts)

- A travel day: weather (d6), the role checks, an encounter (d6: 1, or 1 to
  2 at a Fast pace; then d8 on the table), the supply die.
- Paces from the SRD: 30, 24, or 18 miles a day.
- Roles: Guide (Survival against the Navigation DC; failure = lost), Scout
  (Perception or Stealth DC 12; see an encounter first), Quartermaster
  (Survival against the Foraging DC; no supply roll today), Lookout (Nature
  DC 12; know tomorrow's weather, camp can't be surprised). A second role
  has Disadvantage. A hireling has +3. Slow pace: Advantage for the guide
  and the scout; Fast pace: Disadvantage.
- Supply die d4 to d12: on a 1 or 2 it goes down one size; below d4 the
  supplies run out (then the SRD food and water rules). One step costs 5 GP
  for each traveler. Without a mule or cart, the largest die is d10.
- Lost: the party goes the wrong way for the day; next morning the guide
  repeats with Advantage. Failed by 5 or more: the party does not know that
  it is lost.
- Power: Journeys give no power, so the encounter rules do not change. The
  chapter says so.

## Things I am not sure of

1. The design puts Journeys only in the GM's book. The players learn the
   roles from the GM. Tell me if the player book needs a short summary of
   the four roles.
2. The DC 12 for the scout and the lookout is fixed for all biomes. Only the
   guide and the quartermaster use the DCs of the biome.
3. Next: about 10 biomes (arctic, coast, desert, forest, grassland, hills,
   mountains, swamp, underground, and roads and farmland), with SRD monsters
   in the encounter tables. I checked the monster names against the SRD
   data; many common names are not in the SRD 5.2, and I do not use them.
