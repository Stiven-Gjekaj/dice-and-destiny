# The Dice & Destiny compendiums

This folder holds the source of the Dice & Destiny books and the code
that builds them:

- *Dice & Destiny: The Player's Compendium*
- *Dice & Destiny: The Game Master's Compendium*
- *The Dawnwatch, Book One: Waking*, a campaign for levels 1 to 10. It
  needs Edition 2 of the two Compendiums.

The build makes five PDFs for each book:

- **Screen:** color, with a front cover, links in the contents, and bookmarks.
- **Home print:** A4, black and white, with a front page and a blank back.
- **Lulu interior:** A4, black and white, with no cover.
- **Lulu hardcover cover:** the full color wraparound cover for a Lulu A4
  casewrap hardcover.
- **Paperback cover:** the full color wraparound cover for an A4 paperback,
  with 3 mm bleed. It uses the same interior as the hardcover.

You do not have to build the books to read them. Each push to `main` that
changes this folder or `adventures/` makes a preview release with the PDFs. See
[Releases](https://github.com/Stiven-Gjekaj/dice-and-destiny/releases).

## Build

You need these tools:

- Python 3.10 or later.
- Google Chrome. The build uses headless Chrome to make each PDF.
- `poppler-utils`. The build uses `pdftotext` to find the page numbers for
  the table of contents.
- The fonts Caladea and Liberation Serif. On Ubuntu, install
  `fonts-crosextra-caladea` and `fonts-liberation`. Other fonts change the
  page breaks. Inter and IM Fell English are in `books/fonts/` (TrueType), so
  you do not install them.

Then run these commands:

```bash
pip install -r compendium/requirements.txt
compendium/build.sh
```

You can run `build.sh` from any folder. The PDFs go into `compendium/dist/`.
Git ignores this folder.

The build stops if a PDF has a font that is not expected, or a Type 3 font.
Printers such as Lulu warn about Type 3 fonts.

The build makes each book more than one time. It puts the real page numbers
in the table of contents. It adds blank pages so that each Part starts on a
right-hand page. The full build takes some minutes.

## Folders

| Path | Contents |
|---|---|
| `books/` | The chapters that a human writes (`player.src.html`, `gm.src.html`) and the styles (`style.css` for the design, `book.css` for the page layout, `bw.css` for print, `screen.css` for the screen). A `{{PLACEHOLDER}}` marks a section that the build makes. |
| `content/` | The original content. Each category is a folder: `classes/`, `subclasses/`, `species/`, `backgrounds/`, `feats/`, `spells/`, `monsters/`, `npcs/`, `items/`, `traps/`, `tables/`, `pantheons/`, `downtime/` (with the strongholds), `systems/`, `injuries/`, and `crafting/`. The `__init__.py` of each folder collects the entries of all its files. |
| `build/` | The build code. `build.py` fills the placeholders, adds the chapter headings, makes the table of contents, and makes the PDFs. `cover.py` makes the hardcover and paperback covers. `editions.py` makes the front pages and joins the screen and home-print PDFs. `classes.py` and `compendium.py` make the SRD sections. `orig_render.py` and the `render_*.py` files make the original content sections (one renderer for each new category). `check_content.py` checks the content, and `check_fonts.py` checks the fonts of the PDFs. `monster_engine.py` calculates the monster statistics. `icons.py` holds the icons. `waking.py` builds The Dawnwatch, Book One: Waking, and `waking_md.py` changes its Markdown into HTML. |
| `maps/` | The final maps of The Dawnwatch (`<id>.svg`) and `places.json`, the places for the map tool. See [The maps of The Dawnwatch](#the-maps-of-the-dawnwatch). |
| `data/` | The SRD 5.2 data in JSON, and `fetch.py`, which downloads the data again. |
| `books/waking/` | The Markdown text of The Dawnwatch, Book One: Waking: `how-to-run.md`, `players-guide.md`, `gazetteer.md`, `chapters/NN-name.md` (chapters 2 to 10), and `handouts/NN-name.md`. `books/waking.css` holds the styles of the book. |
| `content/dawnwatch/` | The creatures (`creatures_*.py`, list `MON`), people (`people_*.py`, list `NPCS`), treasures (`treasures_*.py`, list `ITEMS`), and places (`places.py`, list `PLACES`) of The Dawnwatch. The Compendiums do not read this package. |
| `build.sh` | Builds the print and screen interiors, the hardcover covers, and the editions of the three books, and copies the 15 PDFs into `dist/`. |

## Add your own content

Add a new file to a folder in `content/`, or add entries to a file that is
already there. The build finds a new file with no other change. Then run
`build.sh`.

Use the format of the files that are already in the folder. The format of
each category is in the "Entry formats" section of the
[style and balance guide](../docs/dice-and-destiny/style-guide.md), which
also gives the power budgets. Two examples:

- **Monster:** add an `M(...)` entry to the list `MON` in a file in
  `content/monsters/`. Give the size, the type, the CR, and the ability
  scores. The engine calculates the AC, the hit points, the attack bonuses,
  the average damage, and the save DCs. In the text, use `{dc:con}`,
  `{atk:str}`, and `{2d6}`.
- **Magic item:** add a tuple to the list `ITEMS` in a file in
  `content/items/`: `(name, category, rarity, attunement, text)`.

The content check (`build/check_content.py`) runs in each build. It stops
the build on a duplicate name, a name that a publisher owns, an em-dash, a
monster outside the AC and hit point limits, and a spell above the damage
limit. A new category folder needs one line in `REGISTRY` in that file.

To change a chapter, edit `books/player.src.html` or `books/gm.src.html`.

## The maps of The Dawnwatch

A chapter puts a map in the book with the directive `{{map: id}}`.
`build/maps.py` gives the SVG of each map.

| Id | Map | Size (mm) |
|---|---|---|
| `ostrey-then` | Ostrey, 300 years ago. A player handout. | 167 x 250 (page) |
| `land-today` | The land of today. For the GM. | 167 x 250 (page) |
| `act-1` | The Wolds and Saint Ivo's, chapters 2 to 5. | 167 x 120 (half page) |
| `act-2` | The south, chapters 5 to 10. | 167 x 250 (page) |

### Final maps

- Put the final map of an id in `maps/<id>.svg`, for example `maps/act-1.svg`.
- When the file exists, the build uses it. When the file does not exist, the
  build draws a simple preview.
- Give the file the size of its id in the table. Set `width` and `height` in
  mm, and set the `viewBox` in mm, for example
  `width="167mm" height="250mm" viewBox="0 0 167 250"`.
- Use only black and white: `#000`, `#000000`, `black`, `#fff`, `#ffffff`,
  `white`, or `none`. Do not use grey or colour.
- Do not use transparency, an opacity, a filter, a mask, a gradient, or an
  image. Lulu prints the interior in black and white and warns about
  transparency.
- Do not give a text an outline (`stroke`). Chrome prints outlined text as a
  Type 3 font.
- Use IM Fell English for the labels (the font families `IM Fell English`
  and `IM Fell English SC`, regular or italic). Use Caladea or Inter for any
  other text. Do not use another font, for example EB Garamond. The font
  check of the build refuses it.
- The IM Fell English files are in `books/fonts/`, and `books/waking.css`
  loads them. You do not install the font.
- The build refuses a file that breaks these rules.

### The places for the map tool

- `content/dawnwatch/places.py` is the single source of the places and their
  positions in miles.
- `maps/places.json` holds the same places for the map tool. It also holds
  the areas, the rivers, the roads, the coast, and the bounds of each map in
  miles. The map tool does not move a place.
- After a change to `places.py`, write the file again:

      python3 build/maps.py --places-json

  A test fails when the file does not match `places.py`.

### Make the final maps with inkland

[inkland](https://github.com/Stiven-Gjekaj/inkland) 1.3.3 or later draws the
final maps from `maps/places.json`. The config uses these options of
inkland:

- 1.2.0: the character areas and the hand-drawn look.
- 1.2.1: the main river and the relief of each map.
- 1.3.0: the climate preset and the coast bends.
- 1.3.2: the peaks and the `only_in` option.

Before 1.3.3, the river names along the rivers print with letters out of
line. Build the binary from the package `inkland-cli`:

    cargo build --release -p inkland-cli

A version before 1.1.2 gives each label a white outline, and Chrome prints
outlined text as a Type 3 font.

`build/inkland_config.py` holds the choices that `places.json` does not
give:

- the character areas (`CHARACTER_AREAS`)
- the height of the lowland
- the number of generated rivers
- the main river (`MAIN_RIVERS`)
- the roughness of the coast and its bends
- the height of the hills (`HILL_LOW`, the lowest height with a hill symbol)
- the relief symbols (`RELIEF`)
- the regions that the map of old Ostrey shows with no relief
  (`THEN_HIDE_RELIEF`)

1. Write the inkland config again from `places.json`:

       python3 build/inkland_config.py

   This writes `maps/dawnwatch.inkland.json`. A test fails when the file
   does not match `places.json`.

2. Make the maps into a folder outside the repository:

       inkland generate --config maps/dawnwatch.inkland.json --out-dir OUT --preview OUT/preview.png

3. Read each `OUT/<id>.report.json`. Each check must pass. `relief.pins`
   gives the symbols in each region, for example only hills in the Wolds. The check
   `no_generated_labels` fails if a map shows a name that `places.json`
   does not give.
4. Look at each `OUT/preview-<id>.png`.
5. Copy each `OUT/<id>.svg` to `maps/<id>.svg`.

The seed is in `SEED` in `build/inkland_config.py`. The same seed and the
same `places.json` give the same maps.

### Look at the maps, and the release check

- `python3 build/maps.py FOLDER --png` writes each map as an SVG, an HTML
  page, and a PNG into `FOLDER`.
- `maps.missing_maps()` lists the ids with no final map in `maps/`. A
  preview build can use the previews. A Dawnwatch release stops while this
  list is not empty.

## The Dawnwatch, Book One: Waking

`build/waking.py` builds the book from the files that exist. A file that
does not exist yet is left out. The order of the book:

1. The front page, the credits, and the contents.
2. How to run the book and the player's guide.
3. Chapters 1 to 10. Chapter 1 is the tutorial adventure. The build reads it
   from `adventures/tutorial-one-shot/`, so the adventure has one source.
4. The gazetteer.
5. The appendices from the content: Creatures, People, Treasures, and
   Places, each from A to Z, with the chapters that name each entry.
6. The handouts. Each handout starts on a right-hand page. In print, the
   page after it is blank.
7. The index, with the page numbers of each name.

The Markdown is the Markdown of the tutorial. A block quote is read-aloud
text. A block quote that starts with a bold label (`GM tip`, `Teach`,
`Thread (...)`, or `Scaling`) is a box for the GM. A line with only a
directive on it becomes book content:

| Directive | What the build puts there |
|---|---|
| `{{statblock: Name}}` | The statblock from the Dawnwatch content, the original Compendium content, or the SRD bestiary. |
| `{{treasure: Name}}` | The full entry of a treasure or a magic item. |
| `{{map: id}}` | The map from `maps.map_svg(id)` in `build/maps.py`: the final map in `maps/` or a preview. An id that `maps.py` does not know shows a placeholder. |
| `{{handout: NN-name}}` | A note with the page of the handout. |

The build prints a warning for a statblock, treasure, map, or handout that
it does not find, and puts a note in the book in its place.

In the screen edition, each name of an entry is a link to its entry.

## Print

- Interior: A4, black and white, with mirrored margins. The outside margin is
  14 mm. The inside margin comes from the Lulu gutter table, by page count:
  25 mm for 151 to 400 pages and 29 mm for 401 to 600 pages. Each Compendium
  has its value in `INSIDE_MM` in `build/build.py`. The build stops if the
  page count needs a different value. `build/waking.py` takes the value for
  Waking from the table for its page count, and builds again if the value
  changes. The home-print
  PDF and the Lulu interior use this interior.
- Screen: the same text in color, with the same margin on each side and no
  blank pages before the parts.
- Hardcover cover: the spine width comes from a table of Lulu spine widths
  (`HC_SPINE_IN` in `build/cover.py`). Check it against the Lulu cover
  template for the page count of the book.
- The back cover has a white box for a barcode.
- Paperback cover: full color with 3 mm bleed. The spine width uses
  0.0572 mm for each page (`MM_PER_PAGE` in `build/cover.py`). Check it
  against the cover template of your printer.

## Check the layout

`build/overflow.py` finds text that goes out of its box. It needs
`playwright`. `requirements.txt` installs it, but the build does not use it.

## License

See [`NOTICE.md`](../NOTICE.md).
