GM tools: quality pass 1, the Game Master's Compendium. Factions and Renown is stopped, as you asked; nothing of it was committed, and I removed it from my working copy.

Base: main at 63a4a09. compendium/build.sh passes (212 tests, the checks are OK, no Type 3). GM book: 400 pages. The compact table layout (gm-tools-compact-layout.md) is still waiting for review; I took it out of the build for this pass, so these pages are main as it is.

## How I checked

1. Overflow: build/overflow.py on books/gm.html (text out of a cell, a box, or a stat block, a table wider than its column). The script in the repo can't start the browser in this container (the pip Playwright and the installed Chromium differ), so I ran a copy with `executable_path="/opt/pw-browsers/chromium"`. Result: 0 issues.
2. Text of the PDF (pdftotext): em-dashes 0. "Chapter N" references 0. Every "the X chapter" reference names a chapter that exists (Marks, Bonds, Techniques, and Legend Paths are chapters of the Player's Compendium, and the text says so).
3. Headings alone at the foot of a column: from `pdftohtml -xml` (font size and position of each line) on pages 140 to 340. 2 hits, both false: page 3 is the contents, and page 328 is the big title "Injuries and Scars".
4. Columns that end far above the foot of the page, pages 140 to 340: each hit is a chapter end, a part page, or the planned blank page before a part (page 320), or a false hit from the gutter of an even page (pages 278 to 316).
5. Pages read as images: contact sheets of pages 140 to 340 at low resolution, and these pages at full size: 251, 252 (People of the World), 277, 278 (Items A to Z), 318 to 321 (Strongholds, Part V), 322 to 327 (Running Marks, Bonds, Techniques, Legend Paths), 328, 329 (Injuries and Scars), 334, 339 (Crafting and Gathering).
6. Names: each name of the original content against every other category and against the SRD data.

## What I found

No layout problem. I found no text out of a box, no heading alone at the foot of a page, no table or stat block split badly, no wrong cross-reference, no "Chapter N", and no em-dash. So I propose no layout fix.

### Names that a reader can confuse (for the owners to decide)

The build allows these, because the categories are different. Each one is the same name for two different things in the books.

| Name | Where | Owner of the files |
|---|---|---|
| Apothecary | the new class, and an NPC stat block | classes (content/classes/), bestiary (content/npcs/) |
| Blade Dancer | a feat, and an NPC stat block | player options (content/feats/), bestiary (content/npcs/) |
| Bounty Hunter | a subclass, and an NPC stat block | classes (content/subclasses/), bestiary (content/npcs/) |
| Trapper | a background, a subclass, and an NPC stat block | player options (content/backgrounds/), classes (content/subclasses/), bestiary (content/npcs/) |
| Smuggler | a background, and a subclass | player options (content/backgrounds/), classes (content/subclasses/) |
| Silver Tongue | a spell, and a Technique | player options (content/spells/), systems (content/systems/) |
| Gladiator | an original subclass, and the SRD creature "Gladiator" | classes (content/subclasses/) |

An NPC stat block with the name of a class or a background (Apothecary, Trapper, Bounty Hunter) may be on purpose: a stat block for a person of that trade. The spell and the Technique "Silver Tongue" are the clearest case for a new name, as with the trap Soul Lantern.

The crafting recipes have the names of the items that they make (for example "Ring of Regeneration", an SRD item, and "Moss Cloak", an original item). That is correct.

### One question about the trademark

The copyright page of both books (build/build.py, line 114) says: "Dungeons & Dragons is a trademark of Wizards of the Coast LLC." The design says: no "Dungeons & Dragons" or "D&D" in the book text. This sentence is a legal notice, not book text, and check_content does not read build.py. I think it is correct to keep it, but it is your decision.

### The overflow script

build/overflow.py can't start its browser in the cloud container (the version of the pip Playwright does not match /opt/pw-browsers). A small fix: try `p.chromium.launch()` first, and use `executable_path="/opt/pw-browsers/chromium"` if that fails. It is not my file and it is not a book fix, so I did not change it. Tell me if you want it as a commit.

Next: the same pass on the Player's Compendium, as player-quality-pass-1.md.
