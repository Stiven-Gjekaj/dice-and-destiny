GM tools: the compact layout for long tables of short entries is ready for review (approved as the last item of my brief). Nothing of it is committed yet. Tables batch 5 (gm-tools-tables-5.md) is also still waiting, in the same working tree; the two are separate commits.

Build: compendium/build.sh passes with both in place (208 tests, content check, page check, font check with no Type 3). GM book: 387 pages (388 before the compact layout). I read the Names pages: the whole Names section (Epithets and Titles, Named Things, Personal Names) now fits on one page (page 373); before, it took about two.

## Commit

1. feat: print long tables of short entries in two columns
   - build/render_tables.py: `is_compact(entries)` is true for a table with 10 or more entries, each of 3 words or fewer. `table_html` prints such a table with two results in each row: results 1 to n/2 on the left, the others on the right, so the order reads down each column. An odd count leaves the last right cell empty.
   - tests/test_render_tables.py: 3 new tests that build their own tables: which tables are compact, the row layout and order, and the empty cell for an odd count.

No CSS change: the table keeps the classes compact and roll-table (and adds two-col), so it stays in one piece.

## Tables that become compact (11 of 157)

Named Things (Ship Names, Weapon Names, Horse Names), Rooms and Passages (What the Room Was For), Place Names (First Part, Second Part, Inn Name), Epithets and Titles (Epithet), Personal Names (Given Names Soft, Given Names Hard, Family Names).

## Things I am not sure of

1. The limit of 3 words is your example. Titles such as "Lord or Lady of the Marches" (6 words) stay in one column.

Tell me to commit, or what to change.
