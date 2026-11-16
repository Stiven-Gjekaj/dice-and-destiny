GM tools: pantheons batch 1 is on main (9c87496, 635b2a5, 947849e, docs cf8235e).

Downtime batch 1 is ready for review. Nothing of the batch is committed yet.

Build: compendium/build.sh passes (138 tests, content check, page check, font check with no Type 3). I read the new pages: no overflow, each table stays in one piece. After the rebase on 4cab49f (magic items batch 2), the GM book has 272 pages and the build passes again.

## Format (new). Three commits

1. feat: add the renderer for downtime activities
   - compendium/build/render_downtime.py, compendium/tests/test_render_downtime.py (10 tests), one CSS line in books/book.css (.downtime-table break-inside: avoid)
2. feat: add the downtime activities chapter to the GM book
   - the format in the docstring of content/downtime/__init__.py (added lines only), {{DOWNTIME}} and one CH_ICONS line in build.py, Chapter 26 "Downtime Activities" in Part VII after Pantheons
   - one changed line in check_content.py: REGISTRY "downtime" was `lambda m: []`. It is now `lambda m: [e["name"] for e in m.DOWNTIME]`, so that the duplicate and BANNED checks see the activity names. This line was yours. Tell me if you want it different.
3. feat: add 10 downtime activities
   - compendium/content/downtime/activities.py (strongholds.py is not changed)

An activity is dict(name, summary, time, cost, check, results, complications). results is a list of 2 to 6 (check total, text). complications is a list of exactly 6 (a d6).
The renderer stops on: a missing or unknown key, a wrong count of results or complications, a result that is not (total, text), and the same complication two times.
The chapter tells how downtime works: a workweek is 5 days, one activity at a time, the cost comes on top of food and lodging, helpers give advantage and pay the cost too, and a natural 1 (or the GM's choice) gives a roll on the complications table.

## Entries: 10 activities

Each has 4 result rows (9 or lower, 10 to 14, 15 to 20, 21 or higher) and a d6 of complications.
Spreading a Story, Mapping the Region, Gathering Herbs, Hosting a Feast, Writing a Book, Seeking a Patron, Shadowing Someone, Helping the Community, Training an Animal, Making a Pilgrimage.

Strongest rewards (the SRD has no downtime activities, so I compare with SRD costs and rules):
- Writing a Book: 4 workweeks and 20 GP. The average income is 35 GP (10 to 14), 70 GP (15 to 20), or 140 GP (21 or higher). An SRD skilled hireling earns 2 GP each day, so 40 GP in the same 20 days. The top result is 3.5 times that, but it is a small sum of gold at any level. Fame is the main reward.
- Seeking a Patron: on 15 or higher, 50 GP each month or one item up to 200 GP (nonmagical equipment), and the patron asks for favors. No magic item.
- Making a Pilgrimage: on 10 or higher, Heroic Inspiration at the start of the next adventure (the SRD gives it to a Human each Long Rest, so one use is small).
- Gathering Herbs: up to 50 GP of herbs in a workweek, used as raw materials for Herbalism Kit crafting under the SRD rules. No potion is free.
- Mapping the Region: advantage on checks to find your way and no getting lost in the mapped area (equal to a ranger's favored terrain idea, limited to one area).

Originality: I did not use the names or the mechanics of the downtime activities of a paid book. There is no crime, gambling, pit fighting, carousing, training of a language, or magic item trade.

## Things I am not sure of

1. Hosting a Feast points to "the d20 Tavern Rumors table in Chapter 24". If a chapter is added before Part VII, the number goes out of date. Do you want links by chapter name only?
2. The Crafting and gathering system (systems workstream) can later replace the herb result. I kept it to SRD crafting.
3. Totals: downtime 10 of 10 after this batch. Next: more table sets, then traps batch 2 (my local draft, moved to the treasure format, without near copies of its 26).

Tell me to commit, or what to change.
