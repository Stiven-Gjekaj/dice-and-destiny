# Review request: quality pass 1 of the Player's Compendium

Magic items batch 3 is on main (accf4d9, docs 9006797), with your changes:
Wyrmbane Spear is Rare; Chain of Fealty says "Talk with your table before
you use this item"; Phylactery of the Unbowed can't work in the same turn
as another effect that stops a death. The rename of the spell Silver Tongue
to Honeyed Words is on main (0c7e47c).

## How I checked

- I built main at 0c7e47c (278 pages) and read every page in contact
  sheets of 24 pages, then read the suspect pages at a larger size.
- A script read the text of each page and looked for: an em-dash, the
  trademark, "Chapter" with a number, raw markup (`{{`, `[[`), a bad glyph,
  and a short heading-like line at the bottom of a page.
- I compared the names of all entries in all content packages with each
  other and with the SRD data.
- I listed every reference to a chapter in the text and compared it with
  the chapter names.

Results with no problem: no em-dash, no "Chapter N" reference, no raw
markup, no bad glyph, no text outside a box. The chapter intros and the
cover give the right counts (40 backgrounds, 20 species, 220 spells; 4
classes and 96 subclasses). "Seven new subclasses for every SRD class" is
correct (7 for each SRD class).

## Problems

| # | Page | Problem | Owner | What I propose |
|---|---|---|---|---|
| 1 | 24, 31, 50 | A class starts at the bottom of a page. The class banner and the top of its trait box are on one page, and the rest of the trait box (for example SAVING THROW, TOOL) is on the next page. Pages 24 (Bard), 31 (Druid), 50 (Rogue). | classes renderer and CSS (`build/classes.py`, `books/style.css`) | A layout fix in `books/style.css`, one of two: (a) `.class-banner { break-before: page; }`, so that every class starts on a new page (about 10 more pages, but each class opens cleanly); or (b) `.class-head .traits { break-inside: avoid; }` and `.class-head { break-inside: avoid; }` (fewer pages, but the banner can still stay alone at the bottom, because Chrome ignores break-after before a grid). I recommend (a). |
| 2 | 15, 36 and others (Weapon Mastery) | "see the Weapons chapter": the chapter is "Weapons & Armor". | `build/classes.py` lines 34 and 142 | Change to "see the Weapons & Armor chapter". |
| 3 | - | Name clash: "Trapper" is a background (mine, `backgrounds/walks_of_life.py`), a subclass (`subclasses/`), and an NPC (`npcs/`). | player options, classes, bestiary | I can rename my background to "Fur Trapper" in its own commit, if you agree. The subclass and the NPC belong to other sessions. |
| 4 | - | Name clash: "Smuggler" is a background (`backgrounds/core.py`) and a subclass. | player options, classes | I can rename the background to "Contraband Runner". Or the classes session renames the subclass. Your choice. |
| 5 | - | Name clash: "Blade Dancer" is a General feat (`feats/core.py`) and an NPC. | player options, bestiary | An NPC can share a name with a feat without confusion in play, so I only report it. |
| 6 | - | Name clash: "Bounty Hunter" is a subclass and an NPC. | classes, bestiary | Report only. |
| 7 | - | "Silver Tongue" is still a subclass feature (`subclasses/part3.py`) and an NPC action (`npcs/realm.py`), and a Technique. Features and actions are not entries, so the check does not see them. | classes, bestiary, systems | Report only. |
| 8 | 2 | The credits page names "Dungeons & Dragons" in the legal notice ("Not affiliated with... Dungeons & Dragons is a trademark of..."). | orchestrator (book source) | Probably on purpose (a disclaimer). The content check allows it there. Report only. |
| 9 | 76, 88, 146 | Blank or almost blank pages before a part page. | book layout | Probably on purpose (a part page starts on a right-hand page). Report only. |

Crafting recipes have the same names as the items they make (for example
"Potion of Speed"). This is on purpose, so I do not count it as a clash.

## After your answer

I fix only my own files (3, 4) after your approval, each in its own small
commit. For 1 and 2, the owner or you decide.
