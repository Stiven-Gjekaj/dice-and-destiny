# Review request: systems, batch 4 (Techniques: format, renderer, rules)

Systems batch 4: the format of a Technique entry, the renderer and its
tests, and the rules text of Techniques (no techniques yet). Not committed.
This batch is on top of batches 2 and 3 (Marks, Bonds), which are also not
committed. build.sh passes with all three: 93 tests, content check, page
check, Type 3 check. No em-dash.

## Files

Proposed commits (after approval, and after batches 2 and 3):

1. `feat: render the Techniques of the optional systems`
   - `compendium/content/systems/__init__.py`: the format in the docstring,
     and `TECHNIQUES` with `collect_list`.
   - `compendium/build/render_systems.py`: `technique_errors`,
     `technique_html`, `techniques_html`, `all_techniques_html`.
   - `compendium/tests/test_render_systems.py`: 12 new tests.
   - `compendium/build/check_content.py`: the "systems" REGISTRY line also
     reads the names of `TECHNIQUES`.
2. `feat: add the Techniques chapters`
   - `compendium/books/player.src.html`: Chapter 30 "Techniques", with the
     placeholder `{{SYS_TECHNIQUES}}`.
   - `compendium/books/gm.src.html`: Chapter 23 "Running Techniques".
     "Cheat Sheets & Templates" is now Chapter 24.
   - `compendium/build/build.py`: the placeholder and 2 chapter icons.

## Format

Technique (dict): name, type ("Stance" | "Maneuver" | "Shaping"), cost (a
whole number from 1 to 3), level (1, 5, 11, or 17), timing (text, for
example "Bonus Action"), text. The renderer stops the build on a missing or
unknown key or a bad value. The book groups the techniques by type
(Stances, Maneuvers, Spell Shapings), each group in the order of the names.
The meta line is "Maneuver · 1 point · Reaction · level 5+".

## The rules that I set (the design gives only the points)

- Technique points = Proficiency Bonus. All return on a Short or Long Rest.
  (From the design.)
- Techniques known = Proficiency Bonus + 1 (3 at level 1, 7 at level 17).
  Replace one at each level.
- Technique DC = 8 + Proficiency Bonus + Strength or Dexterity modifier.
  A Spell Shaping uses the spell save DC.
- Stance: enter with the action on its line, pay then, lasts 1 minute, one
  stance at a time; ends on Incapacitated or a new stance.
- Spell Shaping: needs Spellcasting or Pact Magic; only on a spell cast with
  a slot unless the shaping says cantrips; one shaping for each spell; not
  with Metamagic on the same spell.
- One technique on each of your turns, and one more as a Reaction.
- Monsters do not use techniques. An important NPC can have 2.

## Power and encounters (GM chapter)

One point is worth about one extra die of weapon damage or one small
effect. Levels 1 to 4: no change. Level 5 or more: add one monster of the
lowest CR for each 4 characters, or 10% more HP for important enemies.

## Things I am not sure of

1. The design does not say how many techniques a character knows. I chose
   PB + 1. The design says "about 60 techniques", so a character knows about
   one tenth of them.
2. The SRD has Metamagic. The Spell Shapings will not copy a Metamagic
   option (Careful, Distant, Empowered, Extended, Heightened, Quickened,
   Seeking, Subtle, Transmuted, Twinned). The SRD has no Battle Master, so
   the maneuvers will be new designs and will not copy the paid maneuvers.
3. The GM chapter suggests "regain half the points after a fight" for
   tables with few Short Rests. Tell me if that is too generous.
4. The entries come next, in 2 batches of about 30 (stances and maneuvers,
   then more maneuvers and the spell shapings).
