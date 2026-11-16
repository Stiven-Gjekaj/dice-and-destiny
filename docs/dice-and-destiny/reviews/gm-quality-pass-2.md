GM tools: quality pass 2, the Player's Compendium (gm-quality-pass-1.md has the GM book). It also asks for approval of one layout fix, which changes both books.

Base: main at 4c3d738 (my GM report, on top of c21414a and the commits before it). With main as it is, compendium/build.sh passes. Player's book: 278 pages. GM book: 412 pages.

## How I checked

The same checks as in pass 1, on all 278 pages: build/overflow.py (with the local browser path), the PDF text (em-dashes, "Chapter N", "the X chapter" references), headings alone at the foot of a column, columns that end far above the foot of the page, and the flagged pages read as images.

## What I found

| Page | Problem | File that owns it |
|---|---|---|
| 71 | The Elven Lineages table splits across the columns: the Drow row is at the foot of the left column, and the High Elf and Wood Elf rows are at the top of the right column. The label "Elven Lineages" is alone above the first part. | build/compendium.py (the SRD species text) |
| 152 to 153 | The Proficiency Bonus table splits: its label and the first rows are at the foot of page 152, the last row "29–30, +9" is alone at the top of page 153. | build/compendium.py (the SRD rules text) |
| 173 to 174 | The multiclass spell slot table (20 rows) splits at the page break, and only the row for level 20 is at the top of page 174, above the Conditions chapter. | build/compendium.py (the SRD rules text) |
| 166 | The table of the twelve classes (12 rows) splits, and its last row (Wizard) is alone at the top of the page. | books/player.src.html or build/compendium.py |
| (class text) | "see the Weapons chapter" in the Weapon Mastery text of two classes: the chapter is called "Weapons & Armor". | build/classes.py, lines 34 and 142 |

No other problem: overflow 0 in print (the script reports two tables as wider than a column, the Sorcerer spell table and the Elven Lineages table, but that is in its screen view of 650 pixels; in the PDF both fit), em-dashes 0, "Chapter N" 0, and the three headings near the foot of a column (pages 260, 268, 272, in the optional systems) each have three or more lines under them.

The names that a reader can confuse are the same as in pass 1 (Apothecary, Blade Dancer, Bounty Hunter, Trapper, Smuggler, Silver Tongue, Gladiator).

## A layout fix for approval (not committed)

Commit: `fix: keep small tables and their labels in one piece`

- New file build/keep_tables.py: `keep_small_tables(html)` adds the class "keep" to each table with at most 10 body rows. If a short bold label paragraph (`<p><strong>...</strong></p>`) comes just before such a table, the label and the table go into one `<div class="keep">`, so the label doesn't stay behind.
- build/build.py: one line added after `comp.no_em_dash(s)`, which calls it for both books.
- books/book.css: one line, `table.keep, div.keep { break-inside: avoid; }`.
- tests/test_keep_tables.py: 7 tests that build their own HTML (the count of body rows, the class added to a table with a class or with no class, a large table not changed, each table handled alone, a label kept with a small table, a label before a large table not changed).

Result, measured on the same main with and without the fix:

| | Without the fix | With the fix |
|---|---|---|
| Player's book pages | 278 | 278 |
| GM book pages | 412 | 412 |
| Player's book, short columns (more than 20% of the page empty at the foot) | 56 | 55 |
| GM book, short columns | 56 | 58 |

- Fixed: pages 71 (the Elven Lineages table and its label are now together in the right column) and 152 to 153 (the Proficiency Bonus table and its label are now together at the top of page 153).
- Not fixed: the 20-row spell slot table (page 174) and the 12-row class table (page 166), because they have more than 10 rows. I tried a limit of 12: each book grew by 2 pages and the short columns went up, so I kept 10.
- The cost: 2 new short columns in the GM book, on page 132 (the Staff of Fire table moves whole to the next page) and page 345 (the crafting Gear table moves whole to the next page). I think a little white space is better than a split table, but it is your choice.

The fix changes build.py and book.css, which are shared. It adds lines only. Tell me to commit it, or to drop it. If you approve, I commit it alone and run the full build before the push.
