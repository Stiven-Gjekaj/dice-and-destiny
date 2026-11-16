Player options: species batch 4 is on main (23be9b5 with docs; 77 tests, the checks are OK, including Type 3). Species: 20 of 20.

Backgrounds batch 1 is ready for review. Nothing is committed yet.
File: compendium/content/backgrounds/walks_of_life.py. Entries: 18 (30 of 40 after this batch). Build: 77 tests pass, the checks are OK, player 234 pages, GM 231. I read pages 208 to 211: alphabetical order, no overflow, no Type 3.

Walks of life by region:
- Sea and river: Pearl Diver (Str/Dex/Con; Athletics, Perception; Jeweler's Tools; Hardy), Lighthouse Keeper (Con/Int/Wis; Perception, Nature; Glassblower's Tools; Lamplighter's Knack), Shipwright (Str/Con/Int; Athletics, Investigation; Carpenter's Tools; Skilled).
- Desert and steppe: Dune Guide (Con/Int/Wis; Survival, Nature; Navigator's Tools; Wilderness Born), Tomb Robber (Dex/Int/Wis; Investigation, Sleight of Hand; Thieves' Tools; Alert), Horse Breaker (Str/Dex/Wis; Animal Handling, Athletics; Leatherworker's Tools; Hardy).
- City and underworld: Rat Catcher (Dex/Con/Wis; Animal Handling, Stealth; Woodcarver's Tools; Iron Stomach), Chimney Sweep (Str/Dex/Con; Acrobatics, Athletics; Mason's Tools; Alert), Fence (Dex/Int/Cha; Deception, Insight; Forgery Kit; Haggler).
- Frontier and wilds: Trapper (Str/Dex/Wis; Nature, Stealth; Leatherworker's Tools; Sharp Ears), Caravan Guard (Str/Con/Wis; Athletics, Perception; Gaming Set; Savage Attacker), Mountain Guide (Str/Con/Wis; Athletics, Survival; Navigator's Tools; Pack Mule), Leech Doctor (swamp; Con/Int/Wis; Medicine, Nature; Herbalism Kit; Magic Initiate (Druid)).
- Court: Herald (Str/Int/Cha; History, Persuasion; Musical Instrument (horn); Skilled), Food Taster (Con/Wis/Cha; Insight, Medicine; Cook's Utensils; Iron Stomach), Duelist's Second (Dex/Int/Cha; Insight, Persuasion; Calligrapher's Supplies; Steady Nerves).
- Temple: Pilgrim (Con/Wis/Cha; Religion, Survival; Cook's Utensils; Pack Mule), Exorcist's Apprentice (Int/Wis/Cha; Arcana, Religion; Calligrapher's Supplies; Magic Initiate (Cleric)).

Checks that I ran myself (the content check does not do them): every feat is an existing origin feat (the 4 SRD ones and the 10 originals); no name is the same as an SRD background. The equipment in option A is about 50 GP or less at SRD prices (the Mountain Guide is 52 GP, because Navigator's Tools and a Climber's Kit cost 25 GP each).

Things I am not sure of:
1. Feat variety: there are only 14 origin feats, so Hardy now appears 4 times in 30 backgrounds, and Steady Nerves and Iron Stomach 3 times each. The best fix is new origin feats first (the feat category is mine too). I propose a small origin feat batch (about 8, for example a sea feat, a desert feat, a court feat, an underworld feat), then the last 10 backgrounds use them.
2. The content check does not test that a background's feat exists. Do you want me to add that check (in check_content.py, with a test), or does it belong to you?
3. Tomb Robber vs the SRD Criminal: they share Thieves' Tools, but the skills, the feat, and the role are different.

Tell me to commit, or what to change.
