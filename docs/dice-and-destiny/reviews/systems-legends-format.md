# Review request: systems, batch 7 (Legend paths: format, renderer, rules)

Systems batch 7: the format of a Legend path entry, the renderer and its
tests, and the rules text of Legend paths (no paths yet). Not committed.
This batch is on top of batches 2 to 6, which are also not committed.
build.sh passes with all six: 135 tests, content check, page check, Type 3
check. Player 254 pages, GM 257 pages. No em-dash.

## Files

Proposed commits (after approval, and after the batches before it):

1. `feat: render the Legend paths of the optional systems`
   - `compendium/content/systems/__init__.py`: the format, and `LEGENDS`.
   - `compendium/build/render_systems.py`: `legend_errors`, `legend_html`,
     `legends_html`, `all_legends_html`.
   - `compendium/tests/test_render_systems.py`: 4 new tests.
   - `compendium/build/check_content.py`: the "systems" line also reads the
     names of `LEGENDS`.
2. `feat: add the Legend paths chapters`
   - `compendium/books/player.src.html`: Chapter 31 "Legend Paths" with
     `{{SYS_LEGENDS}}`.
   - `compendium/books/gm.src.html`: Chapter 24 "Running Legend Paths".
   - `compendium/build/build.py`: the placeholder and 2 chapter icons.

## Format

Legend (dict): name, summary, deeds, fall, tiers (exactly 5 of (title,
benefit)). The renderer prints each tier with its points and level, from a
table in the renderer: I (1 point, level 1), II (3, 5), III (6, 9), IV (10,
13), V (15, 17).

## The rules that I set (the design gives the idea and the 5 tiers)

- One path at a time. To leave a path loses its points and benefits.
- 1 legend point for a deed of the path (2 for a legendary deed); at most 1
  each session unless legendary. The fall of the path takes away 1 or more.
- A tier needs its points and its level. The tiers stack.
- After Tier V, each 5 more points give an Epic Boon (once each). This is
  how the path "continues after level 20".
- Power: Tier I = Common item, II = Uncommon, III = Rare, IV = Very Rare,
  V = Legendary. Encounters: most characters at Tier III, build for one
  level higher; at Tier V, two levels higher, and give important enemies
  Legendary Actions.

## Chapter numbers of other sessions (please check)

The GM chapter numbers are written by hand. My pending chapters (Running
Bonds 22, Running Techniques 23, Running Legend Paths 24) move these lines
of other sessions in my working copy: "Cheat Sheets & Templates" 22 -> 25,
"Traps & Hazards" 23 -> 26 (treasure workstream), "World-Building Tables"
24 -> 27 (GM tools workstream). Each rebase has a conflict in the
placeholder lines of build.py when another session adds a placeholder; I
keep both sides. A build step that numbers the chapters would stop these
conflicts. Tell me if you want me to commit the systems batches sooner, so
that the other sessions see the new numbers.

## Next

Batch 8: 12 Legend paths (Dragonslayer, Saint, Tyrant, Wanderer, and 8
more).
