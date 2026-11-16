# Review request: systems, batch 11 (Factions and renown: format, renderer, rules)

Systems batch 11: the format of a Faction entry, the renderer and its tests,
and the rules text of Factions and renown (no factions yet). Not committed.
It is on top of batches 8, 9, and 10, also not committed. build.sh passes
with all four: 228 tests, content check, page check, Type 3 check. GM 400
pages. No em-dash.

## Files

Proposed commits (after approval):

1. `feat: render the Factions of the optional systems`
   - `compendium/content/systems/__init__.py`: the format, and `FACTIONS`.
   - `compendium/build/render_systems.py`: `faction_errors`,
     `faction_html`, `factions_html`, `all_factions_html`.
   - `compendium/tests/test_render_systems.py`: 6 new tests.
   - `compendium/build/check_content.py`: the "systems" line also reads the
     names of `FACTIONS`.
2. `feat: add the Factions and Renown chapter`
   - `compendium/books/gm.src.html`: the chapter "Factions and Renown"
     after "Journeys", with the placeholder `{{SYS_FACTIONS}}`.
   - `compendium/build/build.py`: the placeholder and the chapter icon.

## Format

Faction (dict): name, summary, goal, gain, lose, rival, ranks (exactly 5 of
(title, reward)). The book shows a table of the ranks with the renown that
each needs: 3, 10, 20, 35, 50 (a table in the renderer).

## The rules that I set (the design gives 0 to 50, ranks, rewards, enemies, and the faction tables)

- Renown for each character with each faction, 0 to 50, open (not secret).
- +1 a small service, +2 a mission, +5 a great deed; -1 to -5 for work
  against the faction; a betrayal sets it to 0 and makes the faction an
  enemy. A single deed never gives more than 5.
- From the third rank, a promotion task is also necessary.
- A faction with a rival: at the third rank, the rival treats the character
  as an enemy.
- An enemy faction closes doors and sends agents. Amends: a costly task,
  then renown starts again at 0.
- A general reward ladder (Friend, Member, Trusted, Officer, Leader): up to
  an Uncommon item loan at 20, a Rare item or a free spell service of level
  5 or lower at 35, a Very Rare item or a stronghold at 50.
- The chapter tells the GM to build a faction with the Faction Builder and
  the other faction tables in World-Building Tables.
- Power: count faction items as treasure (give less treasure elsewhere); a
  follower of a CR near the party's level counts as one more character.

## Things I am not sure of

1. The Very Rare item at 50 renown. It needs a long campaign with one
   faction, and the chapter says to count it as treasure.
2. Renown is for each character. Some tables prefer one score for the
   party; the chapter does not say this yet. Tell me if it must.
3. Next (batch 12): about 10 sample factions, each with its 5 ranks.
