# Review request: systems, batch 2 (the 20 sample Marks)

Systems batch 2: the 20 sample Marks. Not committed. Rebased on main (c2bc317) first. build.sh passes: 81 tests, content check, page check, Type 3 check. Player 240 pages, GM 233 pages (the Marks add 6 player pages and 2 GM pages). No em-dash. The track uses digits and text only, no symbol glyphs.

FILES (one commit: "feat: add 20 sample Marks")
- compendium/content/systems/marks_taints.py: 7 Taints (hidden, GM book): Envy, Pride, Greed, Wrath, Lust, Gluttony, Sloth. Each has a secret.
- compendium/content/systems/marks_blessings.py: 7 Blessings (open, player book): Humility, Charity, Patience, Kindness, Devotion (the virtue against Lust; I did not use "Chastity"), Temperance, Diligence.
- compendium/content/systems/marks_curses.py: 6 Curses (open, player book): Curse of the Lone Path (no benefit, blocks_bonds=True; the model is Silvio's curse), Liar's Curse, Curse of the Stone Heart, Curse of the Restless Dead, Curse of the Forgotten Name, Curse of Ill Fortune.

BUDGET (benefit before 5 = Uncommon; give in = Rare)
Strongest benefits, before 5:
- Envy: +1d6 (1d8 at 1, 2d6 at 3) on the next hit after an ally outshines you. Compare: Flame Tongue (Rare, 2d6 on each hit). The 2d6 at 3 comes with a cost that grows.
- Wrath: +PB, then +1d6+PB, on the next hit against a creature that damaged you. Compare: +1 weapon / Uncommon.
- Stone Heart: +1 AC, Resistance to Bludgeoning at 2, with -5 then -10 Speed and Disadvantage on Dex saves. Compare: +1 armor (Uncommon).
- Ill Fortune: once each Long Rest, a reaction that forces a reroll and the lower result (near Silvery Barbs, a level 1 spell, once a day). The GM gets the same against you.
- Spells before 5 are levels 1 to 2, once each Long Rest: Charm Person, Suggestion (Lust at 4), Invisibility (Forgotten Name at 2), Gentle Repose (Restless Dead at 2), Locate Object (Greed, only after giving in).
Strongest give-in powers:
- Envy: +3d6 once each turn while an ally did better this scene. Compare: Rare (Flame Tongue 2d6 each hit). Near the top of the budget.
- Wrath: +1d6 + 2xPB on every hit against a creature that damaged you this scene, and Immunity to Frightened while Bloodied.
- Pride: once each Long Rest, turn a failed save into a success, plus 2 rerolls of saves. Compare: Rare.
- Stone Heart: +2 AC, Resistance to Bludgeoning, Immunity to Petrified. Compare: +2 armor (Rare).
- Temperance: Immunity to Charmed, Poisoned, and Poison damage.
- Restless Dead: Speak with Dead once each Long Rest, plus a Specter servant for 1 hour once each Long Rest. Compare: Figurine of Wondrous Power (Rare).
- Forgotten Name: Greater Invisibility (level 4) once each Long Rest.

THINGS I AM NOT SURE OF
1. Balance changes that I already made: Stone Heart's give-in first had Resistance to all B/P/S (too strong); Wrath's give-in first had B/P/S Resistance while Bloodied (removed); Restless Dead had Speak with Dead (level 3) at threshold 2, which was above the Uncommon budget, so I moved it to give-in.
2. Envy's give-in (3d6 each turn) and Wrath's give-in are near the top of Rare. Tell me if you want them lower.
3. Some secrets are dark (Gluttony at 5: a creature that you bite to 0 HP can't be raised by a spell below level 7; Wrath at 5: the Sin asks for a life). The GM chapter already tells the GM to leave out Taints that the table does not want.
4. In the GM book, a Taint's hidden-price box can go to the next column, after its entry (the layout breaks the columns there). It stays next to its entry, so I left it.
5. Each Blessing's give-in has the line "Even a virtue can own you." Tell me if you want it removed.
