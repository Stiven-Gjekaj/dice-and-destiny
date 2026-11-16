# Review request: Injuries and scars, batch 1 (format, renderer, rules, 8 samples)

Workstream: GM optional systems (the classes session).

## State

Nothing is committed. `build.sh` passes (BUILD_OK, fonts OK). All 196 tests
pass. The Game Master's Compendium is 328 pages. I looked at pages 284 to
286: the chapter, the Injury table, and the entries are clean.

## Planned commits

1. `feat: render the injuries of the optional systems`:
   `build/render_injuries.py`, `tests/test_render_injuries.py` (12 tests;
   each builds its own entries), `content/injuries/__init__.py` with no
   entries, and the REGISTRY line `"injuries": lambda m: [e["name"] for e in
   m.INJURIES]`.
2. `feat: add the Injuries and Scars chapter`: one line in `build.py`
   (`{{INJURIES}}`) and the chapter in `gm.src.html`, after "Running Legend
   Paths", before Part VI. The heading has no number ("Injuries and Scars"),
   for the coming automatic numbering. The text refers to other chapters by
   name only.
3. `feat: add the first 8 injuries`: `content/injuries/samples.py`.

## The format

`INJURIES`: a list of dicts with `name`, `roll` (the d20 result, 1 to 20),
`severity` ("Minor" 1 to 10, "Serious" 11 to 17, "Lasting" 18 to 20),
`effect`, `treatment`, and `scar` (name, benefit).

The renderer stops the build on: a missing or unknown key; an unknown
severity; a roll outside its severity's results; a d20 result used two
times; a table that does not start at 1; and a range that goes past the
results of its severity. Each entry covers its own roll up to the next
entry's roll, so the table can grow from 8 to 20 entries with no change to
the format.

## The rules (the chapter text, in short)

- An injury can happen when a creature scores a Critical Hit against a
  character, or when a character drops to 0 HP and isn't killed outright.
  The same hit gives one injury, not two.
- **The player's choice:** before any roll, the player chooses to take the
  injury (roll on the table) or to shake it off (gain 1 Exhaustion level and
  no injury). An injury never kills a character and never takes one out of
  the game. A permanent loss happens only when the player chooses it (the
  Lost Eye).
- Roll a d20. Add 5 if the character dropped to 0 HP (above 20 counts as
  20). At most three injuries at once; a fourth replaces one that the
  player chooses, and that one heals with no scar.
- Healing HP doesn't heal an injury. Minor: a Long Rest, some after care.
  Serious: several Long Rests with care, or Lesser Restoration. Lasting: 30
  days of downtime rest with care, or Greater Restoration, Heal, or
  Regenerate.
- **Scars:** an injury that heals with rest and care (not magic) leaves its
  scar. A character can have scars up to their Proficiency Bonus (the style
  guide: a system's resource grows with the PB). Magic heals at once and
  leaves nothing; time heals slowly and leaves a scar.
- **Power and encounters:** injuries weaken for a while, scars strengthen a
  little. While characters carry injuries, don't add danger, and give them a
  chance to rest. When most characters have three or more scars, give each
  important enemy 10% more HP.
- Making your own injuries: a short guide to the size of each severity and
  of a scar.

## The 8 sample injuries

| d20 | Injury | Effect | Scar |
|---|---|---|---|
| 1 to 3 | Ringing Ears (Minor) | Disadvantage on Perception by hearing | Advantage on saves against Deafened |
| 4 to 7 | Twisted Ankle (Minor) | Speed -10 | Advantage on saves to avoid Prone |
| 8 to 10 | Cut Above the Eye (Minor) | Disadvantage on the first attack of each combat | Advantage on Intimidation |
| 11 to 12 | Cracked Ribs (Serious) | Disadvantage on Concentration saves, no Dash | +1 to Concentration saves |
| 13 to 15 | Deep Gash (Serious) | -1 HP for each Hit Point Die spent | once each Long Rest, +PB HP when spending Hit Dice |
| 16 to 17 | Broken Arm (Serious) | one arm can't hold a Shield, a weapon, or cast Somatic; Disadvantage on Str checks | Advantage to keep hold or keep a grapple |
| 18 to 19 | Shattered Knee (Lasting) | Speed -10, no Dash | Advantage on saves against Restrained |
| 20 | Lost Eye (Lasting) | Disadvantage on Perception by sight and on ranged attacks past 30 feet; the player chooses a lost eye or a deep wound | Advantage on Intimidation and on saves against Blinded |

The strongest scar is Old Wound (+PB HP once each Long Rest). The SRD equal
is less than the Tough feat. The scars are narrow on purpose.

## Next batch

12 more injuries to fill the table (each d20 result one entry). The ranges
of the samples will shrink as entries come in between them.

## Questions

1. The "shake it off" choice costs 1 Exhaustion level. Is that the right
   cost? A lighter option is "lose one unspent Hit Point Die".
2. The chapter has no players' side in the Player's Compendium. The Part V
   description says "How to run the optional systems of the Player's
   Compendium". That line belongs to the systems session; it may need "and
   two GM-only systems". I did not change it.
