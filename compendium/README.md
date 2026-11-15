# The Compendiums — my own edition of 5e (2024 rules)

Two print-ready paperback books, generated from code:

- **The Player's Compendium** — learning to play, all 12 classes (guides + full rules text), species, backgrounds, feats, equipment, all 339 SRD spells, the full rules reference, plus original subclasses, species, backgrounds, feats and spells.
- **The Game Master's Compendium** — running the game, the full SRD bestiary and magic items, plus 166 original monsters, 250 original magic items, a stronghold system, and GM cheat sheets and templates.

Finished PDFs are in [`dist/`](dist/): A4 black & white interiors and full-color wraparound covers with 3 mm bleed.

## Build

Requirements: Python 3.10+, Google Chrome (headless, used to render HTML to PDF), and `poppler-utils` (`pdftotext`, used to find page numbers for the table of contents).

```bash
pip install -r requirements.txt
./build.sh
```

The build renders each book several times: it fills in real page numbers in the contents and inserts blank pages so every Part starts on a right-hand page. Expect a few minutes.

## Project layout

| Path | What it is |
|---|---|
| `player.src.html`, `gm.src.html` | Hand-written chapters with `{{PLACEHOLDERS}}` for generated sections |
| `build.py` | Expands placeholders, adds chapter headings/icons, builds the contents, renders PDFs |
| `classes.py` | Class chapters: guides, level tables, feature summaries + full SRD text |
| `compendium.py` | SRD sections: spells, bestiary, magic items, equipment, feats, species, backgrounds, rules |
| `orig_*.py` | **Original content** — edit these to change or add your own material |
| `monster_engine.py` | Turns compact monster specs into balanced stat blocks (AC/HP/attack/DC by CR) |
| `orig_render.py` | Renders the original content |
| `cover.py` | Generates wraparound covers (spine width from page count) |
| `icons.py` | Hand-drawn SVG icons |
| `style.css`, `book.css` | Base design + black & white paperback overrides (A4, mirrored margins) |
| `data/` | SRD 5.2 data (JSON) and `fetch.py` to re-download it |
| `overflow.py` | Optional checker for text overflowing its boxes |

## Adding your own content

- **Monster:** add an `M(...)` entry to any `orig_mon*.py`. Give it a size, type, CR and ability scores; AC, HP, attack bonuses, damage averages and save DCs are calculated for you. Use `{dc:con}`, `{atk:str}` and `{2d6}` in text.
- **Magic item:** add a tuple to `orig_items*.py`: `(name, category, rarity, attunement, text)`.
- **Subclass:** add to the class list in `orig_sub*.py`: `(name, tagline, [(level, feature, text), ...])`.
- **Spell / feat / background / species:** see `orig_spells.py` and `orig_options.py`.

Then run `./build.sh`.

## Printing

- Interior: A4, black & white. Mirrored margins (22 mm inside / 14 mm outside).
- Cover: full color with 3 mm bleed; spine width assumes ~0.057 mm per page. Check your printer's spine calculator and change `MM_PER_PAGE` in `cover.py` if needed.
- A white box on the back cover is reserved for a barcode.

See [NOTICE.md](NOTICE.md) for licensing.
