GM tools: traps batch 3 is on main (54e7f38, docs 48859fe). Before the commit I made your changes: Soul Lantern is now Ghost Lamp (no other content uses that name); Crushing Deep says that a creature native to the deep (a Swim Speed and water breathing) ignores the pressure; Sealed Breath Tomb has a hidden vent (an Intelligence (Investigation) check against the DC, then an action to open it), so a party with no caster can escape. The Wild Magic Zone results are short, and each one follows a failed save; none kills or removes a creature with no save. Traps: 64 of 80.

Tables batch 3 is ready for review. Nothing of the batch is committed yet.

Build: compendium/build.sh passes (175 tests, content check, page check, font check with no Type 3). GM book: 332 pages. I read the new pages: no overflow, each set name stays with its first table.

## Commit

1. feat: add 10 world-building table sets for castles, coasts, caverns, and legends
   - compendium/content/tables/far_and_hidden.py

## Entries: 10 sets, 35 tables. Totals after the batch: 30 of 50 sets

- Settlements: Castles and Keeps (d8 who holds it, d10 what stands out, d8 what is wrong inside, d6 a way in)
- Regions: Coast and Islands (d8, d10, d8, d8), Deep Caverns (d8, d10, d8, d8), Plains and Steppe (d8, d10, d8, d6)
- Dungeons: Lairs and Hideouts (d10 where, d8 guards, d8 inside, d6 surprise), Secret Doors and Hidden Things (d10 hidden, d8 opens, d8 behind)
- Rumors: Letters and Messages (d10 what it says, d6 writer, d6 seal)
- Names: Named Things (d12 ships, d12 weapons, d10 horses)
- People: Travelers on the Road (d12 traveler, d8 cargo, d6 want)
- Lore: Lost Treasures and Legends (d10 treasure, d8 where, d6 truth)

Sets by theme after the batch: Settlements 4, Factions 3, Regions 7, Dungeons 4, Rumors 3, Names 3, People 3, Lore 3.

Power: no rules power. Creatures named are SRD creatures (merfolk, centaurs, kobolds, dwarves, a dragon) or plain words. I replaced "deep gnomes" and "hook horrors" (not in the SRD, and hook horror is a publisher's name) with "gnome miners" and "blind hunters, big as bears, that track by sound". The region sets have no encounter tables.

## Things I am not sure of

1. Regions now has 7 sets. The last 20 sets will lean on Factions, People, Lore, Rumors, and Settlements (for example: guilds, temples, taverns, villages by region, merchants' goods, weather and seasons, NPC secrets, magical places, heraldry of cities, holidays of the two pantheons). Tell me if you want a different mix.
2. Weapon names such as "Widowmaker" and "Kingsbane" are common words, not names from any one book.

Tell me to commit, or what to change.
