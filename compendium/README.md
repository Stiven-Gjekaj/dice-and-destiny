# The Dice & Destiny compendiums

This folder holds the source of the two Dice & Destiny books and the code
that builds them:

- *Dice & Destiny: The Player's Compendium*
- *Dice & Destiny: The Game Master's Compendium*

The build makes four PDFs for each book:

- **Screen:** color, with a front cover, links in the contents, and bookmarks.
- **Home print:** A4, black and white, with a front page and a blank back.
- **Lulu interior:** A4, black and white, with no cover.
- **Lulu hardcover cover:** the full color wraparound cover for a Lulu A4
  casewrap hardcover.

You do not have to build the books to read them. Each push to `main` that
changes this folder makes a preview release with the PDFs. See
[Releases](https://github.com/Stiven-Gjekaj/dice-and-destiny/releases).

## Build

You need these tools:

- Python 3.10 or later.
- Google Chrome. The build uses headless Chrome to make each PDF.
- `poppler-utils`. The build uses `pdftotext` to find the page numbers for
  the table of contents.
- The fonts Caladea and Liberation Serif. On Ubuntu, install
  `fonts-crosextra-caladea` and `fonts-liberation`. Other fonts change the
  page breaks. Inter is in `books/fonts/` (TrueType), so you do not install
  it.

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
| `build/` | The build code. `build.py` fills the placeholders, adds the chapter headings, makes the table of contents, and makes the PDFs. `cover.py` makes the hardcover covers. `editions.py` makes the front pages and joins the screen and home-print PDFs. `classes.py` and `compendium.py` make the SRD sections. `orig_render.py` and the `render_*.py` files make the original content sections (one renderer for each new category). `check_content.py` checks the content, and `check_fonts.py` checks the fonts of the PDFs. `monster_engine.py` calculates the monster statistics. `icons.py` holds the icons. |
| `data/` | The SRD 5.2 data in JSON, and `fetch.py`, which downloads the data again. |
| `build.sh` | Builds the print and screen interiors, the hardcover covers, and the editions of both books, and copies the 8 PDFs into `dist/`. |

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

## Print

- Interior: A4, black and white, with mirrored margins (22 mm inside and
  14 mm outside). The home-print PDF and the Lulu interior use it.
- Screen: the same text in color, with the same margin on each side and no
  blank pages before the parts.
- Hardcover cover: the spine width comes from a table of Lulu spine widths
  (`HC_SPINE_IN` in `build/cover.py`). Check it against the Lulu cover
  template for the page count of the book.
- The back cover has a white box for a barcode.
- The build does not make a paperback cover any more. `cover_html` in
  `build/cover.py` can still make one.

## Check the layout

`build/overflow.py` finds text that goes out of its box. It needs
`playwright`. `requirements.txt` installs it, but the build does not use it.

## License

See [`NOTICE.md`](../NOTICE.md).
