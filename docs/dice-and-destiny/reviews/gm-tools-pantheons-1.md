GM tools: tables batch 1 is on main (6851043, f008c4c, 59ebddb, docs 53c9372). The chapter is Chapter 24 in Part VII, after Traps & Hazards, as you asked.

Pantheons batch 1 is ready for review. Nothing of the batch is committed yet.

Build: compendium/build.sh passes (128 tests, content check, page check, font check with no Type 3). GM book: 257 pages. I read the new pages 253 to 257: no overflow, the overview tables stay in one piece.

## Format (new). Three commits

1. feat: add the renderer for sample pantheons
   - compendium/build/render_pantheons.py, compendium/tests/test_render_pantheons.py (9 tests), one CSS line in books/book.css (.pantheon-table break-inside: avoid)
2. feat: add the pantheons chapter to the GM book
   - compendium/content/pantheons/__init__.py (PANTHEONS), REGISTRY line "pantheons" (the names of the pantheons and the gods), {{PANTHEONS}} and one CH_ICONS line in build.py, Chapter 25 "Pantheons" in Part VII after the tables chapter
3. feat: add the Lantern Court and the Old Circle
   - compendium/content/pantheons/two_pantheons.py

A pantheon is dict(name, summary, gods). A god is dict(name, title, portfolio, alignment, symbol, domains, wants, worshippers). title can be "".
The book shows each pantheon as: a heading, the summary, an overview table (god, portfolio, alignment, domains, symbol), and then one entry for each god (alignment, portfolio, what the god wants, worshippers).
The renderer stops on: a missing or unknown key, an alignment that is not an SRD alignment, a domain that is not a cleric subclass in the book (the SRD Life Domain or an original cleric subclass, read from content/subclasses), the same domain two times, and a pantheon with no god. An empty domain list shows "Any".

## Entries: 2 pantheons, 24 gods

- The Lantern Court (cities, fields, roads; a royal court with one empty chair): Aurenne the Lantern Queen (sun, rule, oaths; LG; Life), Corvane the Grey Warden (death, threshold; LN; Ash), Mirel the Hearthmother (home, guests, birth; NG; Hearth, Life), Tobbin the Wheatfather (harvest, feasts; NG; Harvest), Vessa of the Roads (travel, trade, luck; N; Crossroads), Hald the Anvil (craft, stone; LN; Mountain, Hearth), Sereth the Red Banner (war, courage; N; Any), Ilvane the Quill (knowledge, law; LN; Any), Nessaly the Healer in Grey (sickness and cure; N; Plague, Life), Ombrel the Masked Prince (secrets, thieves; CN; Crossroads), Liathe of the Tides (sea, moon; CN; Tide), Varrak the Unbidden (tyranny; LE; Any; the exiled consort).
- The Old Circle (wild places, clans, nomads, sea folk; no ranks): the Antlered Mother (beasts, hunt; N; Life, Harvest), Grandfather Stone (mountains, ancestors; LN; Mountain), the Bell Below (deep sea, drowned dead; CN; Tide), Kesh the Ember-Eater (wildfire, renewal; CN; Ash), the Thousand-Eyed Night (stars, dreams; N; Crossroads), Mother Rot (decay, fungus; N; Plague), Wren the Little Thief (tricks, lost things; CG; Crossroads), Old Hungry (winter, famine; NE; Any), the Weaver at the Ford (fate, rivers; N; Tide, Life), Ysmay of the Hearthsmoke (clan, shared fire; NG; Hearth), the Horned Rider (plains storms, horses, raids; CN; Any), the Hollow Queen (barrow dead, memory; LN; Ash).

Power: gods have no rules power. Every domain named is the SRD Life Domain or one of the 7 original cleric domains (Hearth, Tide, Ash, Harvest, Crossroads, Mountain, Plague). Every domain is used at least once.

Originality: the names are new. I checked them against the warlock patrons of the book and renamed one god (the Drowned Bell became the Bell Below, near "The Drowned King" and "The Ninth Bell"). The content check passes the BANNED list. The Lantern Court fits the paladin Oath of the Lantern, but no text links them.

## Things I am not sure of

1. Five gods have no domain that fits ("Any"): war, knowledge, tyranny, winter, and plains storms. A War or Knowledge domain would belong to the classes workstream, which is complete. I do not add one.
2. The two evil gods (Varrak, Old Hungry) are written for villains and for the GM. Neither text asks a player to worship them.
3. The overview table puts the symbol and the domains in one place, so the god entries do not repeat them.

Tell me to commit, or what to change.
