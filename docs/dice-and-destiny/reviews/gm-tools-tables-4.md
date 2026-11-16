GM tools: traps batch 4 is on main (one commit, docs d84fd70). Traps: 80 of 80. Before the commit I made your changes. Starfall Orrery: round 1 is as before; in rounds 2 and 3 a creature takes 8d10 (12d10 at levels 17 to 20) on a failed Dex save, or half on a success. Both are under the Dangerous limits (10d10 and 18d10), and the worst case at levels 17 to 20 is now about 231, down from about 300. All ways out stay. Acid Rain: the penalty stops at -3, magic items are not affected, and the Mending spell or a day of work removes it.

Tables batch 4 is ready for review. Nothing of the batch is committed yet.

Build: compendium/build.sh passes (180 tests, content check, page check, font check with no Type 3). GM book: 360 pages. I read the new pages: no overflow, each set name stays with its first table.

## Commit

1. feat: add 10 world-building table sets for towns, courts, and faiths
   - compendium/content/tables/town_and_court.py

## Entries: 10 sets, 28 tables. Totals after the batch: 40 of 50 sets

- People: What's in Their Pockets (quick: d20 small things, d6 coins), Secrets and Motives (d20 secret, d10 drive)
- Settlements: Tavern Menus and Prices (quick: d10 dish, d8 drink, each with a price; d6 the room tonight), Temples and Shrines (d10, d8, d8, d6), Market Day (d12 stalls, d8 today, d6 bargaining)
- Factions: Guilds and Trades (d10, d8, d8, d6), Rival Adventurers (d10, d8, d6)
- Lore: Strange and Magical Places (d10, d8, d6), Holy Days of the Two Pantheons (d12 holy days, d6 what goes wrong)
- Rumors: Court Gossip (d12 gossip, d6 source)

Sets by theme after the batch: Settlements 7, Factions 5, Regions 7, Dungeons 4, Rumors 4, Names 3, People 5, Lore 5.

Power and prices:
- Coins in pockets: at most 2d6 GP or about 10 GP of foreign coins. Small loot.
- Tavern prices are my own plain-tavern prices: 1 CP to 1 SP for food and drink, 2 SP for a pitcher of wine or a plate of festival pig. A fine place doubles them, a poor one halves them.
- Strange and Magical Places say in the summary that any game effect is the GM's choice. No entry gives a rule.

Links: Temples and Shrines and Holy Days refer to "the Pantheons chapter" by name. Holy Days names 12 of the 24 gods (6 from each pantheon), each with one custom that matches the worshippers text of the god.

## Things I am not sure of

1. The guild names in Guilds and Trades ("the Brewers", "the Masons") are generic trade names, not names of a setting.
2. The last batch (10 sets) will finish at 50. Then the compact layout for long tables of short entries, in its own commit with a test, as you asked.

Tell me to commit, or what to change.
