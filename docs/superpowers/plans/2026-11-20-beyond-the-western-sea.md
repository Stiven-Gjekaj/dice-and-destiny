# Beyond the Western Sea Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and release the short campaign book "Dice & Destiny: Beyond the Western Sea" (levels 1 to 5, 120 to 140 pages), with each dice roll in two forms.

**Architecture:** The Waking build in `compendium/build/waking.py` becomes a general campaign engine in `compendium/build/campaign.py`, driven by a `Campaign` record. Waking and the new book are two records. A new module `six_sided.py` adds the six-sided bracket to the HTML of the new book only. The new content is in `compendium/content/western_sea/`, the book text in `compendium/books/western-sea/`, and the final maps in `compendium/maps/western-sea/`.

**Tech Stack:** Python 3, pytest, headless Chrome (PDF), pypdf, poppler-utils, inkland (`cargo build --release -p inkland-cli`), GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-11-20-beyond-the-western-sea-design.md`. Read it before each task. The story, the names, and the dice rules are there.

## Global Constraints

- All text in ASD-STE100 Simplified Technical English, except the book text in `compendium/books/western-sea/`, the text strings in `compendium/content/western_sea/`, and read-aloud text.
- No em-dash anywhere, also not in the book text or the PDFs. No emoji.
- One change per commit. Code and its tests in one commit. Documentation in a separate commit. A rename alone in its own commit. No version number in a subject line.
- Git identity: "Stiven Gjekaj" <stivenagostingjekaj@gmail.com>. No Co-Authored-By line, no tool footer.
- Work on `main`. Push only when the human asks.
- A test builds its own state. It does not read the book text or the example content.
- Waking and the two Compendiums must not change. Their HTML stays byte-identical.
- Book size: 120 to 140 pages in the Lulu interior.
- Levels 1 to 5. DCs from 8 to 15. Armor class from 10 to 16.
- Random tables use d66 or 2d6, never d20 or d100.
- Names must sound real (spec, section "Names"). No two capitalized English words joined into one name, for example "Stormheart".
- No link to the plot of the Dawnwatch: no Hush, no Malgrath, no black stones, no Dawnfire.
- Maps must look hand drawn.

## Review Focus

1. A dice expression with a Unicode minus or no spaces, for example "(4d8 − 4)" or "(2d6+3)", gets the correct bracket. Test in Task 2.
2. A second pass over the HTML does not add a second bracket. Test in Task 2.
3. A roll with only d6s, for example "(2d6 + 1)", gets no bracket. Test in Task 2.
4. A roll with more than one die size, for example "(1d8 + 1d6 + 2)", gets one bracket with both terms converted. Test in Task 2.
5. A "d20" or "d100" in the book source, or a table with a d20 header, stops the build. "Recharge 5–6" and dice inside HTML attributes do not change. Tests in Task 2 and Task 4.

---

### Task 1: Move the book engine out of waking.py

A refactor. Waking does not change.

**Files:**
- Create: `compendium/build/campaign.py`
- Modify: `compendium/build/waking.py`
- Test: `compendium/tests/test_waking.py` (no change; it must still pass), `compendium/tests/test_campaign.py`

**Interfaces:**
- Produces: `campaign.Campaign`, a frozen dataclass with these fields:
  - `name: str` (the output name, for example `"waking"`)
  - `book: str` (the source folder)
  - `content: Callable[[], ModuleType]` (returns the content package)
  - `front: dict` (`title`, `sub_title`, `sub`, `compat`)
  - `css: str` (the book stylesheet, for example `"waking.css"`)
  - `parts: dict[str, str]` (the descriptions of the parts "run", "story", "world", "reference")
  - `chapters: Callable[[str], list[tuple[int, str, str]]]`
  - `maps: str` (the name of the maps module, for example `"maps"`)
  - `extra_forms: dict`, `not_before: dict`, `index_terms: list`
  - `post: Callable[[str], str]` (an HTML filter after the mentions are marked; default: no change)
- Produces: `campaign.expand(c: Campaign, screen=False, inside_mm=None, dw=None) -> tuple[str, list]` and `campaign.build_book(c: Campaign, screen=False) -> None`. These are the functions of `waking.py` with the module constants replaced by fields of `c`.
- Produces: `waking.WAKING: Campaign`. `waking.py` keeps its CLI (`--screen`, `--check-maps`) and the Waking-only functions (`tutorial_text`, `drop_one_shot`, `chapters`). It re-exports the names that `test_waking.py` uses.

- [ ] **Step 1: Save the Waking HTML before the change**

Set `SCRATCH` to a folder outside the repository, for example the scratchpad of the session.


Run: `cd compendium && PYTHONPATH=.:build python3 -c "import waking; open('$SCRATCH/waking-before.html','w').write(waking.expand()[0])"`
Expected: the file exists and is not empty.

- [ ] **Step 2: Write the failing test `test_campaign.py::test_post_filter_runs_on_the_body`**

Build a `Campaign` in a temporary folder with one chapter "x" and a stub content module with empty `MON`, `NPCS`, `ITEMS`, `PLACES`. Give it `post=lambda h: h.replace("x", "y")`. Assert that `"y"` is in `campaign.expand(c)[0]` and that the front matter does not change.

- [ ] **Step 3: Run it to see it fail**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q tests/test_campaign.py`
Expected: FAIL, `ModuleNotFoundError: campaign`.

- [ ] **Step 4: Move the engine into `campaign.py` and make `waking.py` a `Campaign` record**

Move the functions that do not depend on the tutorial. Replace `NAME`, `BOOK`, `FRONT`, `STYLES`, `EXTRA_FORMS`, `NOT_BEFORE`, `INDEX_TERMS`, and the part texts with fields of the `Campaign`. `post` runs in `expand` after `mark_mentions` and before `keep_tables`.

- [ ] **Step 5: Run all tests**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q`
Expected: all pass.

- [ ] **Step 6: Check that Waking does not change**

Run: `cd compendium && PYTHONPATH=.:build python3 -c "import waking; open('$SCRATCH/waking-after.html','w').write(waking.expand()[0])" && cmp $SCRATCH/waking-before.html $SCRATCH/waking-after.html`
Expected: no output (the files are the same).

- [ ] **Step 7: Commit**

```bash
git add compendium/build/campaign.py compendium/build/waking.py compendium/tests/test_campaign.py
git commit -m "refactor: move the book engine of waking.py into campaign.py"
```

### Task 2: The six-sided bracket

**Files:**
- Create: `compendium/build/six_sided.py`
- Test: `compendium/tests/test_six_sided.py`

**Interfaces:**
- Produces: `six_sided.convert(expr: str) -> str | None`. It returns the six-sided form of one dice expression, or `None` when the form is the same (only d6s). It raises `ValueError` for d100 or for a d20 count other than 1.
- Produces: `six_sided.add_brackets(html: str) -> str`. It adds " [form]" after each parenthesized dice expression in the text of the HTML, not inside tags.
- Produces: `six_sided.check_dice(text: str) -> list[str]`, one message for each "d20" or "d100" in the source text.

Rules (spec, "The six-sided rules"), for each term NdX:

| X | Six-sided term |
|---|---|
| 4 | Nd6 and a flat −N |
| 6 | Nd6 |
| 8 | Nd6 and +N |
| 10 | Nd6 and +2N |
| 12 | Nd6 and +3N |
| 20 (N = 1 only) | 3d6 |

Add the d6 counts together and add the flat values together. Write "d6" for one die, "Nd6" for more. Write the flat value as " + k" or " − k" with the Unicode minus (U+2212), as `monster_engine.py` does. Leave out a flat value of 0.

- [ ] **Step 1: Write the failing tests**

```python
from six_sided import convert, add_brackets, check_dice

def test_convert():
    assert convert("1d8 + 3") == "d6 + 4"
    assert convert("2d8+3") == "2d6 + 5"
    assert convert("4d8 − 4") == "4d6"
    assert convert("1d4") == "d6 − 1"
    assert convert("2d10") == "2d6 + 4"
    assert convert("1d12 + 1") == "d6 + 4"
    assert convert("1d8 + 1d6 + 2") == "2d6 + 3"
    assert convert("1d20") == "3d6"
    assert convert("2d6 + 1") is None

def test_add_brackets():
    assert add_brackets("<p>Hit: 7 (1d8 + 3) Slashing</p>") == "<p>Hit: 7 (1d8 + 3) [d6 + 4] Slashing</p>"
    once = add_brackets("<p>2 (1d4) Cold</p>")
    assert add_brackets(once) == once
    assert add_brackets("<p>(2d6) Fire</p>") == "<p>(2d6) Fire</p>"
    assert add_brackets('<p title="(1d8)">Recharge 5–6</p>') == '<p title="(1d8)">Recharge 5–6</p>'

def test_check_dice():
    assert check_dice("| d66 | Event |") == []
    assert len(check_dice("| d20 | Event |")) == 1
    assert len(check_dice("Roll a d100.")) == 1
```

- [ ] **Step 2: Run them to see them fail**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q tests/test_six_sided.py`
Expected: FAIL, `ModuleNotFoundError: six_sided`.

- [ ] **Step 3: Write `six_sided.py`**

`add_brackets` splits the HTML on tags (the method of `campaign.mark_mentions`) and changes only the text parts. It does not change an expression that " [" already follows.

- [ ] **Step 4: Run them to see them pass**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q tests/test_six_sided.py`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add compendium/build/six_sided.py compendium/tests/test_six_sided.py
git commit -m "feat: add the six-sided form of a dice expression"
```

### Task 3: The content package of the new book

**Files:**
- Create: `compendium/content/western_sea/__init__.py`, `creatures.py`, `people.py`, `treasures.py`, `places.py` (each with an empty list)
- Modify: `compendium/build/check_content.py` (the `REGISTRY` and the checks at lines 191 to 272)
- Test: `compendium/tests/test_check_content.py`

**Interfaces:**
- Produces: `content.western_sea` with `MON`, `NPCS`, `ITEMS`, and `PLACES`, in the formats of `content/dawnwatch/__init__.py`. `places.py` also has `ROADS` and `place(name)`, as in `content/dawnwatch/places.py`.
- Produces: `check_content` checks the new package as it checks `dawnwatch`: rarities, clashes with Compendium names, and clashes with Dawnwatch names.
- Produces: `check_content.limit_errors(mons) -> list[str]`, one message for each creature of the new book with an armor class above 16 or a save DC above 15 (spec, "What 3d6 changes"). It uses `M.stats()` and the `{dc:...}` values of `M.fmt`.

- [ ] **Step 1: Write the failing test `test_western_sea_name_clash`**

Give `campaign_clashes` a stub campaign list with "Goblin" and a Compendium list with "Goblin". Assert one message that starts with `"western_sea: 'Goblin'"`.

Also write `test_limit_errors`: an `M` with `ac=17` gives one message. An `M` with CR 1 and `ac=13` gives none. An `M` of CR 5 with a Wisdom of 20 and a `{dc:wis}` action (DC 16) gives one message.

- [ ] **Step 2: Run it to see it fail**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q tests/test_check_content.py -k western_sea`
Expected: FAIL.

- [ ] **Step 3: Add the package, give `campaign_clashes` a `label` parameter (default `"dawnwatch"`), and add `limit_errors` to the content check of the new package**

- [ ] **Step 4: Run the tests and the content check**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q && PYTHONPATH=.:build python3 build/check_content.py content`
Expected: all pass, and no errors.

- [ ] **Step 5: Commit**

```bash
git add compendium/content/western_sea compendium/build/check_content.py compendium/tests/test_check_content.py
git commit -m "feat: add the content package of Beyond the Western Sea"
```

### Task 4: The book build for Beyond the Western Sea

**Files:**
- Create: `compendium/build/western_sea.py`, `compendium/build/farholm_maps.py`, `compendium/books/western-sea.css`, `compendium/books/western-sea/` (with `how-to-run.md`, `players-guide.md`, `gazetteer.md`, and `chapters/`, each with one heading only)
- Test: `compendium/tests/test_western_sea.py`

**Interfaces:**
- Consumes: `campaign.Campaign`, `campaign.build_book`, `six_sided.add_brackets`, `six_sided.check_dice`, `content.western_sea`.
- Produces: `western_sea.WESTERN_SEA: Campaign` with `name="western-sea"`, `post=six_sided.add_brackets`, `maps="farholm_maps"`, and `front` set to:
  - `title="Beyond the Western Sea"`, `sub_title=""`
  - `sub`: one line from the premise, written in Task 9
  - `compat="A campaign for levels 1 to 5. Requires the Dice &amp; Destiny Compendiums, Edition 2."`
- Produces: `western_sea.PAGES = (120, 140)` and `western_sea.check_pages(n: int) -> str | None` (a message when n is outside the range).
- Produces: `western_sea.source_dice_errors(book: str) -> list[str]` runs `check_dice` on each Markdown file of the book.
- Produces: CLI `python3 build/western_sea.py [--screen | --check-maps | --check]`. `--check` stops with an error if `source_dice_errors` is not empty.
- Produces: `farholm_maps.MAP_IDS = ["farholm", "colony-town"]`, `farholm_maps.map_svg(map_id, size=None) -> str`, `farholm_maps.missing_maps(ids=None) -> list[str]`. The final maps are `compendium/maps/western-sea/<id>.svg`. `map_svg` uses `maps.check_print` and `maps.scope_ids`. With no final file, it raises `KeyError`, so the book shows a placeholder.

- [ ] **Step 1: Write the failing tests**

- `test_statblock_gets_bracket`: a temporary book with a chapter that holds `{{statblock: Test Crab}}`, and a stub content module with one `M("Test Crab", ..., attacks=[("Claw", "m", "1d8", "Slashing")])`. Assert that `"[d6 + "` is in `campaign.expand(WESTERN_SEA with book=tmp, content=stub)[0]`.
- `test_waking_has_no_bracket`: the same stub with `waking.WAKING`. Assert that `" [d6"` is not in the HTML.
- `test_check_pages`: `check_pages(119)` and `check_pages(141)` return a message. `check_pages(120)` and `check_pages(140)` return `None`.
- `test_source_dice_errors`: a temporary book with "| d20 | x |" in a chapter gives one error.

- [ ] **Step 2: Run them to see them fail**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q tests/test_western_sea.py`
Expected: FAIL, `ModuleNotFoundError: western_sea`.

- [ ] **Step 3: Write `western_sea.py`, `farholm_maps.py`, the CSS, and the stub book folder**

The CSS starts as a copy of `waking.css`. `build_book` prints the `check_pages` message as a WARNING while the book is not complete. Task 13 makes it an error.

- [ ] **Step 4: Run the tests, then build the stub book**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q && PYTHONPATH=.:build python3 build/western_sea.py`
Expected: all tests pass. `western-sea.pdf` exists. A WARNING says that the page count is below 120.

- [ ] **Step 5: Commit**

```bash
git add compendium/build/western_sea.py compendium/build/farholm_maps.py compendium/books/western-sea.css compendium/books/western-sea compendium/tests/test_western_sea.py
git commit -m "feat: build Beyond the Western Sea from its own book folder"
```

### Task 5: Covers, front pages, and build.sh

**Files:**
- Modify: `compendium/build/cover.py` (`BOOKS`, and `dawnwatch_counts` becomes `campaign_counts(module, token)`)
- Modify: `compendium/build.sh`
- Test: `compendium/tests/test_cover.py`

**Interfaces:**
- Produces: `cover.BOOKS["western-sea"]` with `t1="Beyond the"`, `t2="Western Sea"`, the bullets with the token `{WS_COUNTS}`, `compat="A campaign for levels 1 to 5 &middot; Requires Edition 2"`, and the `note` of Waking.
- Produces: `cover.campaign_counts(module, token: str) -> dict[str, str]`. `cover_html` fills `{DW_COUNTS}` from `content.dawnwatch` and `{WS_COUNTS}` from `content.western_sea`.

- [ ] **Step 1: Write the failing test `test_campaign_counts`**

Use a stub module with 2 `MON`, 1 `NPCS`, and 3 `ITEMS`. Assert `campaign_counts(stub, "{WS_COUNTS}") == {"{WS_COUNTS}": "2 new creatures, 1 person, and 3 treasures"}`.

- [ ] **Step 2: Run it to see it fail, then write the change, then run all tests**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q`
Expected: first FAIL, then all pass. The Waking cover HTML does not change: compare `cover_html("waking", 312, "hardcover")` before and after with `cmp`.

- [ ] **Step 3: Add the book to `build.sh`**

Add `python3 build/western_sea.py --check`, the print and screen builds, `western-sea` in the `check_content.py pages`, `cover.py`, and `editions.py` lines, and `"western-sea:Beyond the Western Sea"` in the `dist/` loop.

- [ ] **Step 4: Run the full build**

Run: `cd compendium && ./build.sh`
Expected: "Done. PDFs are in dist/". `dist/` has 15 PDFs. `check_fonts.py` passes.

- [ ] **Step 5: Commit**

```bash
git add compendium/build/cover.py compendium/build.sh compendium/tests/test_cover.py
git commit -m "feat: make the covers and the editions of Beyond the Western Sea"
```

### Task 6: The release workflow

**Files:**
- Modify: `.github/workflows/release.yml`

**Interfaces:**
- Produces: a tag `western-sea-N` makes a release "Beyond the Western Sea, version N" with 5 files, and fills the rolling release `western-sea-latest`. A preview release has the files of all three products. The file slug is `beyond-the-western-sea`.

- [ ] **Step 1: Change the workflow**

Use the Waking steps as the model:
- add the tag pattern
- add `assets-western-sea.txt`, with the assertion `test "$(wc -l < assets-western-sea.txt)" -eq 5`
- run the map check `python3 build/western_sea.py --check-maps` and the dice check `--check` for a `western-sea-*` tag
- add the publish step with `PRODUCT=western-sea` and `ROLLING=western-sea-latest`

- [ ] **Step 2: Check the workflow file**

Run: `python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/release.yml'))" && grep -c "western-sea" .github/workflows/release.yml`
Expected: no error, and a count of 6 or more.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/release.yml
git commit -m "ci: release Beyond the Western Sea from a western-sea tag"
```

### Task 7: The world bible facts and the places of Farholm

**Files:**
- Modify: `docs/superpowers/specs/2026-11-16-dawnwatch-world.md` (the timeline: year -60, the fleet; the map: Farholm in the Western Sea, off the map edge)
- Modify: `compendium/content/western_sea/places.py`

**Interfaces:**
- Produces: `PLACES` and `ROADS` for Farholm, with `x` and `y` in miles on a map of the island only. These include the colony town, the Corrin Light, the wreck of the *Good Intent*, the wreck of the *Morning Star*, the way to the heart, and about 10 sites in two rings (spec, "The parts of the campaign").

- [ ] **Step 1: Write the world bible rows**

The rows are: the fleet of year -60, the storm wall, and Farholm.

- [ ] **Step 2: Write `places.py`**

Use the name rules of the spec. Each site has `ring` ("outer" or "inner") and `chapters`.

- [ ] **Step 3: Run the tests and the content check**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q && PYTHONPATH=.:build python3 build/check_content.py content`
Expected: all pass.

- [ ] **Step 4: Commit, in two commits**

```bash
git add docs/superpowers/specs/2026-11-16-dawnwatch-world.md
git commit -m "docs: add the fleet of year -60 and Farholm to the world bible"
git add compendium/content/western_sea/places.py
git commit -m "feat: add the places of Farholm"
```

### Task 8: The maps of Farholm

**Files:**
- Create: `compendium/build/farholm_inkland.py`, `compendium/maps/western-sea/farholm.inkland.json`, `compendium/maps/western-sea/farholm.svg`, `compendium/maps/western-sea/colony-town.svg`
- Test: `compendium/tests/test_farholm_inkland.py`

**Interfaces:**
- Consumes: `content.western_sea.places.PLACES`, and the helpers of `inkland_config.py` (`organic_outline`, `_hidden_labels`).
- Produces: `farholm_inkland.config() -> dict` (the inkland config of the island) and a CLI that writes `farholm.inkland.json`.

- [ ] **Step 1: Write the failing test `test_every_place_is_an_overlay_place`**

Use a stub list of two places. Assert that `config()` has each place as an overlay place, that `pins.points == []`, and that `labels.generated` is `False`. These are the rules of the Waking converter.

- [ ] **Step 2: Run it to see it fail, then write `farholm_inkland.py`, then run it to see it pass**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q tests/test_farholm_inkland.py`
Expected: first FAIL, then PASS.

- [ ] **Step 3: Generate the island map**

Build the newest inkland release tag with `-p inkland-cli`, and check `--version` against the tag. Then generate the map from the config. Check that it looks hand drawn: a rough coast, organic forest and hills, and no straight lines. Copy it to `maps/western-sea/farholm.svg`.

- [ ] **Step 4: Make the town map**

Try inkland for the colony town. If inkland cannot make a good town map, stop and ask the human before you use another tool (spec, "Maps").

- [ ] **Step 5: Check the maps**

Run: `cd compendium && PYTHONPATH=.:build python3 build/western_sea.py --check-maps`
Expected: "each map is final".

- [ ] **Step 6: Commit, in two commits**

```bash
git add compendium/build/farholm_inkland.py compendium/tests/test_farholm_inkland.py
git commit -m "feat: make the inkland config of Farholm"
git add compendium/maps/western-sea
git commit -m "feat: add the final maps of Farholm"
```

### Tasks 9 to 12: The book text

Each task writes book text and the content that it uses. The book text follows the authoring rules of `docs/superpowers/specs/2026-11-16-dawnwatch-authoring.md`, where they apply:
- read-aloud text
- a box for each new rule
- a Scaling box for 3 to 6 characters in each fight
- statblocks by `{{statblock: Name}}`
- treasures by `{{treasure: Name}}`
- maps by `{{map: id}}`
- handouts by `{{handout: NN-name}}`

Each task ends with the same verification steps, then its own commits:

- [ ] **Verify A:** `cd compendium && PYTHONPATH=.:build python3 -m pytest -q && PYTHONPATH=.:build python3 build/check_content.py content`. Expected: all pass.
- [ ] **Verify B:** `cd compendium && PYTHONPATH=.:build python3 build/western_sea.py --check && PYTHONPATH=.:build python3 build/western_sea.py`. Expected: no dice error, and no WARNING about a statblock, a treasure, a map, or a handout that the build does not find.
- [ ] **Verify C:** `grep -rn "$(printf '\342\200\224')" compendium/books/western-sea compendium/content/western_sea`. Expected: no output.
- [ ] **Verify D:** read each new statblock in the PDF. Each roll that is not only d6 has a bracket.

The content of a task goes in a separate commit from its book text: `feat: add the <part> creatures and people of Beyond the Western Sea`, then `feat: write <part> of Beyond the Western Sea`.

#### Task 9: How to run, the six-sided rules, the Storm Cube, and the player's guide

**Files:** `books/western-sea/how-to-run.md`, `books/western-sea/players-guide.md`, `build/western_sea.py` (the `sub` line)

- How to run (about 10 pages):
  - the arc and the level of each part
  - the six-sided rules, on one page, with the exact rules and table of the spec
  - the Storm Cube: how it starts, what turns it, at 64 the last chapter starts, the "double" and a table of its benefits, and the form for normal dice
  - the pace: the middle takes the cube from 2 to about 32
  - the level points: the end of chapter 1, then a number of sites in each ring
- Player's guide (about 6 pages): Corrantey, the *Good Intent*, and the voyage. No secret of the island.
- A cheat sheet for the players, at the end of the player's guide: the six-sided rules and the table of the dice, for players who use the backgammon dice with Compendium characters.

#### Task 10: Chapter 1, "The Wreck of the *Good Intent*"

**Files:** `books/western-sea/chapters/01-*.md`, `content/western_sea/creatures.py`, `people.py`, `treasures.py`

- Linear, levels 1 to 2, about 12 pages.
- It teaches the island, the Storm Cube, and the six-sided rules.
- It ends at the first meeting with the colony.

#### Task 11: The island, the outer ring and the inner ring

**Files:** `books/western-sea/chapters/02-*.md` (one file for the island, with one section for each site), the content files.

- About 10 sites, about 50 pages:
  - **The outer ring:** levels 2 to 3, the coast, the colony town, the Corrin men, and the Tey folk.
  - **The inner ring:** levels 3 to 4, the interior, the wreck of the *Morning Star*, and the way to the Grandam.
- Each site lists the events that turn the cube.
- The parts of the Corrin Light and the clues to the heart are in different sites, so each order of sites works.
- Factions and renown for the two sides. Journeys, Crafting and gathering, and Injuries and scars where the spec says.

#### Task 12: The last chapter, "Storm Season", the gazetteer, and the handouts

**Files:** `books/western-sea/chapters/03-*.md`, `books/western-sea/gazetteer.md`, `books/western-sea/handouts/*.md`, the content files.

- The last chapter (level 5, about 10 pages) gives the three choices and the result of each (spec, "The end").
- The gazetteer of Farholm (about 14 pages): the history of the fleet, the colony town, the two sides, and the legend of the saint who lit a fire on the Grandam.
- The handouts: each on its own page. No spoilers.

### Task 13: Finish the book

**Files:**
- Modify: `compendium/build/western_sea.py` (`check_pages` stops the build)
- Modify: `compendium/tests/test_western_sea.py`
- Modify: `README.md`, `NOTICE.md`, `compendium/README.md`, `docs/superpowers/specs/2026-11-20-beyond-the-western-sea-design.md` (the status line)

- [ ] **Step 1: Write the failing test `test_page_count_stops_the_build`**

`build_book` with a stub render that gives 100 pages raises `SystemExit`. The message names 120 to 140.

- [ ] **Step 2: Run it to see it fail, make `check_pages` an error, then run all tests**

Run: `cd compendium && PYTHONPATH=.:build python3 -m pytest -q`
Expected: first FAIL, then all pass.

- [ ] **Step 3: Build everything and measure**

Run: `cd compendium && ./build.sh && pdfinfo dist/*Western\ Sea*Interior*.pdf | grep Pages && pdffonts dist/*Western\ Sea*Interior*.pdf | grep -c "Type 3"`
Expected: the build passes, the interior has 120 to 140 pages, and the Type 3 count is 0. Tell the human the measured page count.

- [ ] **Step 4: Commit the code**

```bash
git add compendium/build/western_sea.py compendium/tests/test_western_sea.py
git commit -m "feat: stop the build of Beyond the Western Sea outside 120 to 140 pages"
```

- [ ] **Step 5: Change the documentation, in separate commits**

- README: a row in "The newest files of each product", a box in "The books", a line in the note at the top, and the release kind `western-sea-N`.
- NOTICE.md: add the new folders to the content license row.
- compendium/README.md: the new build files.
- The design status: "The book builds. The tag `western-sea-1` releases it."

Commit each file alone, for example `docs: add Beyond the Western Sea to the README`.

- [ ] **Step 6: Ask the human about the release**

Do not push or tag. Ask the human to read the PDF, and ask if they want the tag `western-sea-1`.
