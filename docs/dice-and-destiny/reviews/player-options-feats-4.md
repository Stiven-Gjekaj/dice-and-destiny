# Review request: player options, feats batch 4 (the last 6)

## The batch

- File: `compendium/content/feats/new_classes.py` (not committed).
- Entries: 6 General feats. Feats: 114 to 120 of 120.
- Build: the same build as spells batch 8 (169 tests pass, the checks are
  OK). I searched the PDF text: all 6 feats are in the book.
- I searched every content file for each name. No name is in use.
- I read the features of the 4 new classes in `content/classes/` (I did
  not change them) and the Techniques in `content/systems/`.

| Feat | Prerequisite | Benefit | Equal to |
|---|---|---|---|
| Field Marshal | Captain Orders feature | +1 Command Die, Orders at 60 ft | Grappler-level, improves one feature |
| Master Brewer | Apothecary Concoctions feature | +1 concoction each Long Rest, bombs at 60 ft | Grappler-level |
| Steady Channel | Shaper Strain feature | Strain Limit +1, a DC 15 Con save to avoid the Overstrain Exhaustion | Grappler-level |
| Deep Bond | Spiritbinder Bound Spirit feature | spirit HP + your level, +1 Bond Point | Grappler-level |
| Battle Caller | none | one Captain Order with a d6, PB/LR | Magic Initiate-type (borrow a class feature) |
| Technique Adept | the Techniques optional rules | learn 2 more techniques, +1 technique point | Grappler-level, for the optional system |

## Things that I am not sure of

1. Technique Adept adds a technique point. The style guide says that no
   optional system adds more than one extra use of a resource each short
   rest at level 1. This feat is for level 4+, and it costs a feat.
   Please check it with the systems workstream.
2. Field Marshal gives one extra Command Die. A Captain has 2 to 6 dice,
   so the extra die matters most at low levels.
3. The class feats name features of classes that another workstream owns.
   If a feature is renamed, these prerequisites need the same change.
