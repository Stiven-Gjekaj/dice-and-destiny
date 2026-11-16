GM tools: tables batch 4 is on main (a79c6cc, docs 266d9c3). Sets: 40 of 50.

Tavern prices: I checked the SRD equipment data in compendium/data. It has no food, drink, or lodging table (no mug of ale, no meal, no inn). The only food price is Rations, 5 SP for a day. The tavern prices (1 CP to 2 SP, about 1 SP for a day of three plain meals) stay below that, so I kept them. I wrote this in the progress file. I pushed with your new push rule: after the full build passed, the new remote commits changed only docs and other sessions' content folders, so I ran pytest and the content check and pushed.

Tables batch 5 is ready for review. It is the last tables batch: 50 of 50 after it. Nothing of the batch is committed yet.

Build: compendium/build.sh passes (180 tests, content check, page check, font check with no Type 3). GM book: 382 pages. I read the new pages: no overflow, each set name stays with its first table.

## Commit

1. feat: add the last 10 world-building table sets
   - compendium/content/tables/last_sets.py

## Entries: 10 sets, 28 tables. Totals after the batch: 50 of 50 sets

- Factions: Underworld Jobs (d10 job, d8 target, d6 complication), Mercenary Companies (d10 company, d8 famous for, d6 right now)
- People: Hirelings and Retainers (d12, d8, d6), Guards on Duty (quick: d10 guard, d8 doing, d6 to get past)
- Dungeons: Why the Monster Is Here (d10 why, d8 wants, d6 a way without a fight)
- Lore: Prophecies (d10 when, d8 then, d6 twist), Fallen Empires (d10, d8, d6)
- Settlements: Crimes and Punishments (d10 crime, d8 punishment, d6 local quirk)
- Rumors: Travelers' Tales (d12 tale, d6 teller)
- Names: Epithets and Titles (quick: d20 epithets, d10 titles)

All 50 sets by theme: Settlements 8, Factions 7, Regions 7, Dungeons 5, Rumors 5, Names 4, People 7, Lore 7.

Power and prices: no rules power. Coin sums: a 1 SP toll and a 1 GP bribe (Guards on Duty), a fine of "a few silver pieces". Hirelings and Retainers says that a skilled hireling costs 2 GP a day and an untrained one 2 SP. These are the SRD 5.2 hireling prices as I know them, but the SRD data in this repository has no services table, so I could not check them in the repository. Please confirm or tell me to remove the numbers.

## What is left in my brief after this batch

- Traps and hazards: 80 of 80 (done).
- World-building table sets: 50 of 50 (after this batch).
- Gods: 24 of 24 (done).
- Downtime activities: 10 of 10 (done).
- One item: the compact layout for long tables of short entries (approved for after the 50 sets). I will send it next, as its own commit with a test.

After that, nothing is left in the brief. I am ready for new work.

Tell me to commit, or what to change.
