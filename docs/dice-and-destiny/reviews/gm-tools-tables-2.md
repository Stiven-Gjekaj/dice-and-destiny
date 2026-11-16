GM tools: traps batch 2 is on main (0fca873, 0251e41, 1045c4b, docs 18b76cc). Before the commit I made your two changes: every check uses the band DC ("against the DC"), except the Gilded Cage bars (DC 20 and 18, with the reason in the text: the iron cage is the same at every level). Ashfall and Scouring Sandstorm give Advantage on the save to a creature with proper gear. "Dispel Magic (DC N)" is now "A Dispel Magic spell", as in traps batch 1. Traps: 43 of 80.

Tables batch 2 is ready for review. Nothing of the batch is committed yet.

Build: compendium/build.sh passes (154 tests, content check, page check, font check with no Type 3). GM book: 306 pages. I read the new pages.

## Commits

1. fix: keep the name of a table set with its first table
   - build/render_tables.py: the name, the summary, and the first table of a set are now in one block (div.ts-head), and books/book.css has one line that keeps that block in one piece. One new test in tests/test_render_tables.py.
   - Reason: in the build, the heading "Personal Names" and its summary were alone at the bottom of a page, and its tables started on the next page. A CSS "break-after: avoid" on the summary did not work in Chrome (the summary split across columns), so the renderer makes the block.
2. feat: add 10 world-building table sets
   - compendium/content/tables/wide_world.py

## Entries: 10 sets, 36 tables. Totals after the batch: 20 of 50 sets

- Regions: Mountain Heights (d8 kind, d10 landmark, d8 sign, d8 inhabitants), Swamp and Fen (d8, d10, d8, d8), Desert and Wastes (d8 kind, d10 buried things, d8 sign, d6 who crosses it)
- Settlements: Port Towns (d8 trade, d10 dock scenes, d6 waterfront trouble)
- Factions: Cults and Secret Orders (d10 what it serves, d8 how it hides, d6 how it recruits, d6 what it is about to do), Noble Houses (d8 power, d10 arms, d8 head, d8 scandal)
- People: Villain Builder (d10 want, d8 because, d8 method, d8 weakness)
- Rumors: Bounties and Notices (d12 notice, d6 reward, d6 catch)
- Names: Personal Names (d20 soft given names, d20 hard given names, d12 family names)
- Lore: Omens and Portents (d12 omen, d6 what people think, d6 what it means)

Sets by theme after the batch: Settlements 3, Factions 3, Regions 4, Dungeons 2, Rumors 2, Names 2, People 2, Lore 2.

Power: no rules power. Creatures named are SRD creatures (dwarves, giants, a dragon, a hag, giant lizards). I replaced "lizardfolk" (not in the SRD data) with "hunters who ride giant lizards". The region sets have no encounter tables (Journeys owns those).

## Things I am not sure of

1. Page space: the d20 tables of one-word names are tall (Personal Names, Rooms and Passages). They leave white space when they don't fit in a column. A later fix could print a long table of short entries in two or four columns of rows. Do you want that now, or later?
2. The arms in Noble Houses are words only (no symbols), as the brief asks.

Tell me to commit, or what to change.
