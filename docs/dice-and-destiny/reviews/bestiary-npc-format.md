# Review request: the NPC format and NPC batch 1

This request has two parts: the new format (part A) and the first 30 NPCs
(part B). The style guide asks the orchestrator to approve a new format
before more entries use it.

## Part A: the format

### Entry format

- Folder: `compendium/content/npcs/` (new). Each file adds a list `NPCS`.
- Each entry is a pair `(role, M(...))`. The `M` is the monster engine, so
  the engine calculates AC, HP, attacks, and DCs, and the AC and HP limits
  of the content check apply.
- The role is one of 10 fixed roles in `ROLES` in the renderer: Guards and
  Soldiers, Nobles and Officials, Priests and the Faithful, Merchants and
  Townsfolk, Criminals and Spies, Cultists, Sailors and Pirates, Scholars and
  Mages, Wilderness Folk, Assassins and Duelists.
- `npc_errors` stops the build on: an entry that is not a pair, a value that
  is not an `M`, an unknown role, a type that is not Humanoid, or a CR
  outside 1/8 to 15 (the range in the brief).

### Files and commits (in this order)

1. `feat: add the renderer and the tests for the NPC stat blocks`
   - `compendium/build/render_npcs.py` (new): `npc_errors`, `npcs_html`
     (grouped by role in the order of `ROLES`, then by CR and name),
     `npcs_index_html` (each role with name, CR, and XP).
   - `compendium/tests/test_render_npcs.py` (new): 10 tests. Each test
     builds its own entries.
2. `feat: add the People of the World section to the GM's book`
   - `compendium/content/npcs/__init__.py` (new, empty list).
   - `compendium/build/check_content.py`: one new line in `REGISTRY`, and two
     new lines that run `monster_out_of_band` on each NPC. Lines added only.
   - `compendium/build/build.py`: two new lines for `{{O_NPCS_IDX}}` and
     `{{O_NPCS}}`. Lines added only.
   - `compendium/books/gm.src.html`: a new section "People of the World" at
     the end of Chapter 18 (Original Bestiary), after `{{O_BEST}}`. It is an
     `h2` in an existing chapter, so no chapter number changes. Lines added
     only.
3. `feat: add 30 NPC stat blocks` (part B).

### Book layout

- The section has a short introduction, an index by role (name, CR, XP),
  and then the stat blocks by role. Each role has a heading and a one-line
  description.
- I examined pages 220 and 221 as images. The index and the blocks show
  correctly.

## Part B: NPC batch 1

- Files: `compendium/content/npcs/civic.py` (15), `faith.py` (8),
  `roads.py` (7). 30 NPCs.
- CR: 1/8: 5, 1/4: 2, 1/2: 2, 1: 2, 2: 5, 3: 1, 4: 2, 5: 2, 6: 1, 7: 1,
  8: 1, 9: 2, 10: 1, 12: 1, 14: 1, 15: 1.
- Roles: Guards 5, Nobles 4, Priests 5, Merchants 3, Criminals 3, Cultists 3,
  Sailors 3, Scholars 2, Wilderness 1, Assassins 1. Later batches fill the
  last three roles.
- No name is an SRD name (Guard, Knight, Mage, Priest, Spy, and so on) or the
  name of an existing original monster. I checked this with a script.
- Every spell name is in the SRD 5.2 spell list. I checked this with a
  script.
- Build: `compendium/build.sh` passes with parts A and B (138 tests, the
  content checks, the page check, and the font check). GM book: 277 pages
  (hardcover count).

### Strongest entries and the SRD entry that each is equal to

- **Magister of the Arcane College** (CR 15): 3 Force lances at 27.5,
  Magic Resistance, Counterspell and Dispel Magic 2/Day, Cone of Cold,
  Globe of Invulnerability, Teleport, and Wall of Force 1/Day, a Reaction
  that ends a spell on a failed Con save (2/Day). Equal to Archmage (CR 12)
  plus 3 for its attacks and its counter-Reaction.
- **Nightblade Master** (CR 14): 3 attacks at 22 plus Sneak Attack 8d6,
  Evasion, Uncanny Dodge. Equal to Assassin (CR 8) plus 6 for its damage
  (about 94 a round).
- **High Inquisitor** (CR 12): 2 maces at 30 (Radiant), a Judgment area
  effect (8d10 and Incapacitated), Hold Monster and Zone of Truth 1/Day,
  immune to Charmed and Frightened. Equal to Archpriest (CR 12 in the 2024
  rules).
- **Marshal of the Realm** (CR 10): 3 attacks at 20, Parry, Order the Charge.
  Equal to Knight (CR 3) at the level of a CR 10 boss.

### Not sure

1. **The role list.** Are the 10 roles right? I can add "Performers and
   Entertainers" or "Laborers" if you want more townsfolk.
2. **Duchess of Many Masks** (CR 7): Reaction "Not Me" moves a hit to an ally
   within 5 feet. Bodyguards are part of her design.
3. **Battle Wizard** (CR 5): a Reaction gives +5 AC against one hit, 2/Day.
   I did not give it the Shield spell at will.

## A note for the human

The GM's book says "166 new monsters" in the Part IV line of
`compendium/books/gm.src.html`. The real number is now 346 (after the swamp
batch), and it grows with each batch. I did not change it, because that line
also counts items. A fix could print the counts from the content. Tell me if
the bestiary workstream should do it.
