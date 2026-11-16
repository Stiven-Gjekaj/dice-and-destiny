# Review request: the final consistency check of the 4 new classes

Workstream: classes and subclasses.

## State

- On `main`: `feat: add 3 subclasses for the Apothecary` and `fix: give the
  real counts of the new classes and subclasses in Part VII` ("four new
  classes, 96 new subclasses").
- The content now has 4 classes (Apothecary, Captain, Shaper, Spiritbinder)
  and 96 original subclasses: 84 for the SRD classes (7 for each) and 12 for
  the new classes (3 for each). A count of `CLASS_KEYS` and `SUBS` gives
  these numbers. The targets of the workstream are met.

## What I checked

- Each subclass of a new class has features at the subclass levels of its
  class (a script compared the levels of all 12).
- Each class table has 20 values in each column.
- Each class has Ability Score Improvement at 4, the Epic Boon at 19, and a
  "<Class> Subclass" feature at 3 that names the right levels.
- The equipment names are in the SRD data (`all_items`, `all_weapons`,
  `all_armor`), apart from one flavor item (a carved spirit token).
- The recommended Epic Boons and backgrounds are in the SRD data (fixed in
  `8e47bfb`).

## What I found, and the fixes (not committed)

1. In all 4 level tables, the rows for levels 8, 12, and 16 showed "–". The
   SRD tables show Ability Score Improvement at those levels. The feature
   text says "You gain this feature again at levels 8, 12, and 16", but the
   table did not show it.
   - Commit 1 (renderer and test): `feat: show a class feature again in the
     level table at its repeat levels`. A new optional class key `also_at`:
     `{feature name: [levels]}`. The level table shows the name at those
     levels. The feature text is shown one time only. 2 new tests. With no
     `also_at`, the HTML of the 4 classes is the same as before (cmp).
   - Commit 2 (content): `fix: show the repeated Ability Score Improvements
     and fill the empty level 5 of the Shaper`. Each class gets
     `also_at={"Ability Score Improvement": [8, 12, 16]}`.
2. The Shaper's level 5 row was empty, although Tier 3 Surges and a second
   Bolt come at level 5. The same commit 2 adds a short feature, "Rising
   Power" (5): "You can now use Tier 3 Surges, and your Elemental Bolt makes
   two Bolts. Your Strain Limit, Highest Tier, and Bolts keep growing as the
   Shaper Features table shows." It gives no new power.
3. The Apothecary's equipment had "a bandolier of empty vials", which is not
   an SRD item. Commit 2 changes it to "5 Vials" (an SRD item).

`build.sh` passes with both fixes. The 4 tables now show a feature on every
row except the levels with only a subclass feature.

## Open questions for the human (also in the progress file)

None that block the work. One note: the Spiritbinder's "carved spirit token"
is a flavor item with no rules and no price. It stays unless you want an SRD
item in its place.

If you approve, I commit the two fixes and push. Then the workstream is
complete, and I stop.
