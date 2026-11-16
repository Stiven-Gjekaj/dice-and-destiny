# Authoring rules: The Dawnwatch

Date: 2026-11-16.
Status: the rules for each writer and for the build of The Dawnwatch.

Parent design: [The Dawnwatch](2026-11-16-the-dawnwatch-design.md).
Facts: [World bible](2026-11-16-dawnwatch-world.md).

## Where the files go

| What | Where | Lane |
|---|---|---|
| How to run Book One | `compendium/books/waking/how-to-run.md` | Guide and gazetteer |
| Chapter 1 | `adventures/tutorial-one-shot/` (the build reads it from there) | Build |
| Chapters 2 to 10 | `compendium/books/waking/chapters/NN-name.md`, for example `02-brannocks-ford.md` | Chapters |
| The player's guide | `compendium/books/waking/players-guide.md` | Guide and gazetteer |
| The gazetteer | `compendium/books/waking/gazetteer.md` | Guide and gazetteer |
| Handouts | `compendium/books/waking/handouts/NN-name.md` | The lane that writes the chapter |
| New creatures | `compendium/content/dawnwatch/creatures_*.py`, list `MON` | Chapters |
| New people with statblocks | `compendium/content/dawnwatch/people_*.py`, list `NPCS` | Chapters |
| New treasures | `compendium/content/dawnwatch/treasures_*.py`, list `ITEMS` | Chapters |
| Places for the maps and the index | `compendium/content/dawnwatch/places.py`, list `PLACES` | Maps |

Each content file uses the same format as the files in
`compendium/content/monsters/`, `compendium/content/npcs/`, and
`compendium/content/items/`. Read one of them before you write. The lane
for chapters 2 to 5 uses the suffix `_act1`. The lane for chapters 6 to 10
uses `_act2`. Two lanes never write the same file.

## The language of the text

- The chapters, the player's guide, the gazetteer, and the handouts are
  book text for readers. They do not have to be in STE. They follow the
  voice of the tutorial: clear, short, and friendly to a new GM.
- The notes in this folder and the code comments stay in STE.
- No em-dash anywhere. The release workflow stops if a PDF has one.
- Distances are in feet, as in the Compendiums.
- Use the rules terms of the Compendiums with the same capitals, for
  example "Difficult Terrain", "Short Rest", and "Advantage".
- Use the names in the world bible. Do not make a second name for a person
  or a place.

## Markdown in a chapter

The chapters use the same Markdown as the tutorial. Read
`adventures/tutorial-one-shot/sessions/01-the-last-watch/README.md` first.

- `#` is the chapter title. `##` is a scene. `###` is a part of a scene.
- **Read-aloud text** is a block quote with no bold label at the start:

      > The road bends, and you see the river.

- **A box for the GM** is a block quote that starts with a bold label:

      > **GM tip:** If the players are slow, cut this scene.
      > **Teach: Journeys.** "Each of you takes a role for the day."
      > **Thread (the Shadow):** The collector offers 500 GP.

  The labels are `GM tip`, `Teach`, `Thread (...)`, `Scaling`, and
  `Secret (chapter N)`. A secret box holds a fact that a later chapter
  shows. The GM must not tell it before that chapter.
- Each chapter starts with a short table: the levels, the time at the
  table, the places, and the system that starts.
- Each chapter ends with a section `## Rewards`, and with the milestone:
  "The characters go to level N."

## Directives

A directive is a line with only the directive on it. The build changes it
into book content.

| Directive | What the build puts there |
|---|---|
| `{{statblock: Name}}` | The statblock of a creature or a person, by its name in the content files or the Compendiums. |
| `{{treasure: Name}}` | The full entry of a treasure. |
| `{{map: id}}` | A map. The ids are in `compendium/build/maps.py`. |
| `{{handout: NN-name}}` | A note that the handout is in the appendix, with its page number. |

Put a statblock in a chapter only if the creature appears in one scene.
The build puts each new creature, person, and treasure in the appendices
too.

## Encounters

- Use the XP budgets of Building Encounters in the Game Master's
  Compendium. Give a `Scaling` box for 3, 4, 5, and 6 characters.
- Use monsters from the Compendiums first. Make a new creature only when
  the story needs it.
- New content follows the style and balance guide:
  `docs/dice-and-destiny/style-guide.md`.

## Check before each commit

- `cd compendium && python3 -m pytest -q` passes.
- `grep` finds no em-dash in your files.
- Each name in your text is in the world bible.
