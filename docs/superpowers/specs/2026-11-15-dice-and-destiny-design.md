# Design: Dice & Destiny repository

Date: 2026-11-15.
Status: draft. The human must approve this design before work starts.

## Intent

This repository becomes the home of **Dice & Destiny**.
Dice & Destiny is the human's own edition of fifth edition (2024 rules).
It has two books: *Dice & Destiny: The Player's Compendium* and
*Dice & Destiny: The Game Master's Compendium*.
Python code builds the books from source.
The human wants to publish the books at a later time.

The campaigns that the human runs stay in the same repository.

## Goals

- Import the compendium build system from the upload
  `dnd-compendium.zip` into `compendium/`.
- Sort the compendium into clear folders (approach B, below).
- Rename the books to Dice & Destiny.
- Add a license.
- Add a GitHub Actions workflow that builds the books on each push and
  publishes the PDFs as a GitHub release.
- Move the campaigns to `campaigns/`.
- Make the root `README.md` the home page of Dice & Destiny.

## Non-goals

- Do not add new game content. The human adds new content after this work
  and before the first edition.
- Do not change what the build makes. After each step, the books have the
  same page count and the same text as the PDFs in the upload.
- Do not rewrite the build system as a package with tests (approach C).

## Anti-goals

- Do not use "Dungeons & Dragons", "D&D", or other trademarks of Wizards of
  the Coast in a title, on a cover, or in the name of the edition.
  A "compatible with fifth edition" line is permitted.
- Do not commit built PDFs to git. PDFs go only to releases.
- Do not break the build in any commit.

## Constraints

- All work goes on `main`. The human asked for this.
- `AGENTS.md` applies to all commits: one change in each commit,
  documentation in a different commit, no agent attribution, and
  Simplified Technical English (STE).
- The human is the writer of each commit. Set `user.name` and `user.email`
  in the repository config to the values of the earlier commits in this
  repository.
- Two other sessions write on the branches `fountain-of-divine` and
  `tutorial-one-shot`. These branches start from the old layout.
- The build needs Python 3.10 or later, Google Chrome, `pdftotext`, and the
  fonts Bitstream Charter, Caladea, GFS Baskerville, and Inter.
  If a font is missing, the page breaks change.

## Approaches

- **A. Import as it is.** Put the flat folder of the upload into
  `compendium/`. This is fast, but the original content and the build code
  stay mixed in one folder of 30 files.
- **B. Import, then sort into folders.** Import as in A, then move the files
  into folders, one step in each commit. Run the full build after each step
  and compare it with the PDFs in the upload. **The human chose B.**
- **C. Rewrite as a Python package with tests.** This gives the cleanest
  result, but it changes much working code, and no current need asks
  for it.

## Decisions

### Name and trademark

- Name of the edition: **Dice & Destiny**. The human chose it.
- The covers and the title pages show a line such as
  "A rules-compatible guide for fifth edition (2024)".
- `NOTICE.md` keeps the statement that the work is not official and not
  endorsed by Wizards of the Coast.

### Layout

    README.md               Home page of Dice & Destiny
    AGENTS.md
    LICENSE                 MIT, for code
    LICENSE-CONTENT.md      CC BY-NC-SA 4.0, for original text and content
    NOTICE.md               SRD 5.2 attribution, trademarks, license map
    .github/workflows/
      release.yml
    compendium/
      README.md             How to build, and how to add content
      build.sh
      requirements.txt
      build/                build.py, cover.py, classes.py, compendium.py,
                            monster_engine.py, orig_render.py, icons.py,
                            player_icons.py, overflow.py
      content/              orig_*.py (original monsters, items,
                            subclasses, spells, options)
      books/                player.src.html, gm.src.html, style.css,
                            book.css
      data/                 SRD 5.2 JSON and fetch.py
    campaigns/
      the-fountain-of-divine/
    adventures/             The tutorial one-shot goes here.
    docs/superpowers/specs/ Design documents

The `dist/` folder of the upload does not go into git. Add it to
`.gitignore`.

### License (decision of the agent)

The human asked the agent to choose. The agent chose this split:

- **Code: MIT.** This is the usual license for code.
- **Original text and content: CC BY-NC-SA 4.0.** This includes the book
  chapters, the original content, the layout, the icons, the covers, and the
  campaigns. Other people can share and change it if they give credit and do
  not sell it. The human keeps all rights to sell it.
- **SRD 5.2 material: CC BY 4.0.** The SRD license requires this.
  `NOTICE.md` gives the attribution.

`NOTICE.md` shows which license applies to which folder.

### Release workflow

- Trigger: a push to `main` that changes `compendium/**` or
  `.github/workflows/release.yml`. A change to only a campaign does not
  start a build.
- The job installs Chrome, `poppler-utils`, the fonts, and the Python
  requirements. Then it runs `compendium/build.sh`.
- **Before the first edition (decision of the agent):** each build makes a
  *pre-release* with the tag `preview-YYYY.MM.DD-<short sha>`. The four
  PDFs are attached. The workflow keeps the 5 newest previews and deletes
  the older ones.
- **First edition and later editions:** the human asks for an edition.
  The agent pushes a tag `edition-N` (for example `edition-1`). The workflow
  sees the tag and makes a full release, not a pre-release.
- The tag has a name that the workflow makes. No commit changes a version
  number. This agrees with `AGENTS.md`.

### STE scope (decision of the agent, the human must confirm)

`AGENTS.md` says that all text is in STE. The book chapters and the
original content are prose for readers, not STE. A rewrite into STE would
damage the books.

Proposal: add one rule to `AGENTS.md`. The rule says that the book text
(`compendium/books/` and the text strings in `compendium/content/`) and
the read-aloud text in campaigns and adventures are exempt from STE.
All other text stays in STE: documentation, code comments, commit messages,
and DM notes.

### Other sessions

After the move, send a message to the two sessions. Tell them the new paths
(`campaigns/the-fountain-of-divine/` and `adventures/tutorial-one-shot/`)
and tell them to rebase onto `main`.

### Repository settings

This session cannot change repository settings. The human does these steps:

- Rename the repository from `DnD` to `dice-and-destiny`.
- Set the description and the topics. The agent gives the text.

## Order of the commits

Each line is one commit. The build must pass after each code commit.

1. Set up the repository: `.gitignore` for build output and `dist/`.
2. Import the compendium as it is into `compendium/` (no `dist/`).
3. Move the SRD data into `compendium/data/` (if not there already) and fix
   the paths.
4. Move the book sources and CSS into `compendium/books/`.
5. Move the original content into `compendium/content/`.
6. Move the build code into `compendium/build/` and update `build.sh`.
7. Rename the books to Dice & Destiny (titles, covers, title pages).
8. Add `LICENSE` and `LICENSE-CONTENT.md`, and update `NOTICE.md`.
9. Add the release workflow.
10. Move the campaign to `campaigns/`.
11. Add the STE exemption to `AGENTS.md`.
12. Rewrite the root `README.md` and `compendium/README.md` (documentation).

## How to verify

- After each move commit, run `compendium/build.sh`. Compare the page count
  of each PDF with the PDF in the upload, and compare the `pdftotext` output.
  The text must be the same, except the title text in commit 7.
- Run the workflow on GitHub. Download the PDFs from the preview release and
  compare them in the same way.

## Left to the builder

- How to make the moved modules find each other (for example, a path setup
  in `build.sh` or a small package file).
- Which Ubuntu packages give the fonts on the GitHub runner.
- The exact text of the "compatible" line.
