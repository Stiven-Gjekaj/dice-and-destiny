# The Dice & Destiny compendiums

This folder holds the source of the two Dice & Destiny books and the code
that builds them:

- *Dice & Destiny: The Player's Compendium*
- *Dice & Destiny: The Game Master's Compendium*

The build makes four print-ready PDFs: an A4 black and white interior and a
full color wraparound cover with 3 mm bleed for each book.

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
| `books/` | The chapters that a human writes (`player.src.html`, `gm.src.html`) and the styles (`style.css`, `book.css`). A `{{PLACEHOLDER}}` marks a section that the build makes. |
| `content/` | The original content: `orig_mon*.py` (monsters), `orig_items*.py` (magic items), `orig_sub*.py` (subclasses), `orig_spells.py` (spells), and `orig_options.py` (backgrounds, species, feats). The strongholds are in `orig_items3.py`. |
| `build/` | The build code. `build.py` fills the placeholders, adds the chapter headings, makes the table of contents, and makes the PDFs. `cover.py` makes the covers. `classes.py` and `compendium.py` make the SRD sections. `orig_render.py` makes the original content sections. `monster_engine.py` calculates the monster statistics. `icons.py` holds the icons. |
| `data/` | The SRD 5.2 data in JSON, and `fetch.py`, which downloads the data again. |
| `build.sh` | Builds both books and both covers, and copies the PDFs into `dist/`. |

## Add your own content

Edit the files in `content/`. Then run `build.sh`.

- **Monster:** add an `M(...)` entry to an `orig_mon*.py` file. Give the
  size, the type, the CR, and the ability scores. The engine calculates the
  AC, the hit points, the attack bonuses, the average damage, and the save
  DCs. In the text, use `{dc:con}`, `{atk:str}`, and `{2d6}`.
- **Magic item:** add a tuple to an `orig_items*.py` file:
  `(name, category, rarity, attunement, text)`.
- **Subclass:** add an entry to the class list in an `orig_sub*.py` file:
  `(name, tagline, [(level, feature, text), ...])`.
- **Spell, feat, background, or species:** see `orig_spells.py` and
  `orig_options.py`.

To change a chapter, edit `books/player.src.html` or `books/gm.src.html`.

## Print

- Interior: A4, black and white, with mirrored margins (22 mm inside and
  14 mm outside).
- Cover: full color with 3 mm bleed. The spine width uses 0.0572 mm for each
  page. Use the spine calculator of your printer, and change `MM_PER_PAGE` in
  `build/cover.py` if necessary.
- The back cover has a white box for a barcode.

## Check the layout

`build/overflow.py` finds text that goes out of its box. It needs
`playwright`. `requirements.txt` installs it, but the build does not use it.

## License

See [`NOTICE.md`](../NOTICE.md).
