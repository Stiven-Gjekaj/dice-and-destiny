GM tools: world-building tables batch 1 is ready for review. Nothing of the batch is committed yet.

Thank you for the answer about traps. I stopped my traps draft (30 entries, with a renderer) and keep it local only. When the treasure batch is on main, I compare the two formats. I use the treasure format and move my entries into it if they are not the same as its 26 traps.

Build: compendium/build.sh passes (96 tests, content check, page check, font check with no Type 3). GM book: 238 pages. I read the new pages 231 to 238: no overflow, no table split across a column, the order of the groups and the names is correct.

## Format (new). Three commits

1. feat: add the renderer for world-building table sets
   - compendium/build/render_tables.py, compendium/tests/test_render_tables.py (15 tests), one CSS line in books/book.css (.roll-table break-inside: avoid)
2. feat: add the world-building tables chapter to the GM book
   - compendium/content/tables/__init__.py (TABLE_SETS), REGISTRY line "tables" in check_content.py, {{TABLE_SETS}} in build.py, chapter "23 · World-Building Tables" at the end of Part VI (Toolkit). No chapter number changes.
3. feat: add 10 world-building table sets
   - compendium/content/tables/first_sets.py

A set is dict(name, theme, summary, tables). tables is a list of (die, title, entries). The die is d4, d6, d8, d10, d12, or d20. The count of entries must be the same as the faces of the die.
Themes, in the order of the book: Settlements, Factions, Regions, Dungeons, Rumors, Names, People, Lore.
The renderer stops on: a missing or unknown key, an unknown theme, no table, an unknown die, a wrong count of entries, the same entry two times in a table, and two tables with the same title in a set.

## Entries: 10 sets, 36 tables

- Settlements: Village at a Glance (d8 economy, d10 problem, d12 place, d8 custom), City Districts (d10 character, d12 street scene, d8 who runs it, d6 trouble tonight)
- Factions: Faction Builder (d10 kind, d10 goal, d8 method, d8 weakness, d6 sign)
- Regions: The Deep Forest (d8 forest, d10 landmark, d10 sign, d8 inhabitants)
- Dungeons: Dungeon Origins (d10 builder, d10 what went wrong, d8 who lives there, d12 dressing), Rooms and Passages (d20 purpose, d12 oddity, d10 doors)
- Rumors: Tavern Rumors (d20 rumors as hooks, d6 how true)
- Names: Place Names (d12 + d12 parts, d10 inn names)
- People: Shops and Shopkeepers (d10 shop, d10 keeper, d8 odd item, d6 problem)
- Lore: Festivals and Holy Days (d10 reason, d8 what happens, d6 what goes wrong)

Power: tables have no rules power. No entry gives a game bonus. The Toolkit chapter already has "Quick NPC Generator" and "Random Complications". No new table repeats them.

## Things I am not sure of

1. Chapter number: the treasure traps batch may also add a chapter 23 at the end of the book. The second one to land renumbers. Tell me if you want a fixed order (for example 23 Traps, 24 Tables, 25 Pantheons).
2. Travel encounters for each biome: the design puts biome encounter tables in the Journeys system (systems workstream). My brief also names them. I left them out of this batch. Who owns them?
3. Size: a set with 4 tables is about half a page. 50 sets add about 25 pages.

Tell me to commit, or what to change.

## Addition after the rebase

The treasure traps review (treasure-traps-1.md) adds Part VII "The GM's Workshop" with Chapter 23 Traps & Hazards. I propose this: the tables chapter becomes Chapter 24 in that part, after the traps chapter. If the traps batch lands first, I move my chapter there before I commit. If my batch lands first, my chapter stays at the end of Part VI as Chapter 23, and the treasure session moves it. Tell me which you prefer.

After the rebase on 555f409, build.sh passes again with the batch in place (96 tests, GM book 244 pages).
