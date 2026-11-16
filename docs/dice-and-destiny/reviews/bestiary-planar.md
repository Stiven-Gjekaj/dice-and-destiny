# Review request: bestiary batch 10, planar monsters

## Batch

- File: `compendium/content/monsters/planar.py` (new, not committed).
- Entries: 30 monsters from the burning pits, the heavens, the planes of the
  elements, order, chaos, and dreams, and the starry void between them.
- Planar goes from 21 to 51 monsters. Planar had only 7 monsters at CR 0 to
  4. This batch adds 16 there.

## Build

- `compendium/build.sh` passes on `main` 9e7b478 (177 tests, the content
  checks, the page check, and the font check).
- The GM book goes to 353 pages (hardcover count). This count includes the
  work of other sessions since my last batch.
- I examined pages 198 and 247 as images. No text goes out of a box, and the
  numbers are correct.

## Spread

- CR: 0 to 1: 8, 2 to 4: 8, 5 to 10: 6, 11 to 16: 5, 17 to 24: 3.
- Types: 7 Fiend, 6 Celestial, 5 Aberration, 4 Construct, 3 Elemental,
  1 Undead, 1 swarm of monstrosities, 1 Fey, 1 Monstrosity, 1 Dragon.
- AC: the highest override is 2 above the target. The HP multiplier is 1.0
  for all.
- No plane name that a publisher owns. I wrote "the plane of order", "the
  plane of chaos", "the plane of dreams", and "the starry void".
- One fiend ties into the Marks system: the Envy Devourer (CR 11), a fiend of
  envy. It does not use the Marks rules.

## Strongest entries and the SRD entry that each is equal to

- **Wheel of Eyes** (CR 22, Gargantuan Celestial): 3 attacks up to 40 (fire
  rim with Radiant, or a holy gaze at 300 feet), a 16d10 Radiant area that
  Blinds, a legendary action that Stuns one creature. Equal to Ancient Green
  Dragon (CR 22). The idea is the wheel angel of old scripture (public
  domain).
- **Lord of Contracts** (CR 20, Fiend): 3 attacks at 27.5 to 31 (quill at
  range or seal), Collect the Debt (16d10 Necrotic, a creature killed by it
  loses its soul), Dominate Monster, Geas, Plane Shift 1/Day. Equal to Pit
  Fiend (CR 20). I removed Wish from my first draft.
- **Planar Gatekeeper** (CR 18, Construct): 3 fists at 28.5, BPS resistance,
  no teleport or plane travel within 120 feet, Banish (12d10 Force and a push
  of 60 feet). Equal to Dragon Turtle (CR 17) plus 1 for legendary actions.
- **Rift Dragon** (CR 15): 3 Rends at 24, a 12d8 Force Cone that teleports
  each creature that fails up to 60 feet, Plane Shift on itself at will.
  Equal to Adult Bronze Dragon (CR 15).
- **Angel of Mercy** (CR 14, Celestial): 2 attacks at 31, Healing Light 3/Day
  (4d10 to each ally within 60 feet), Heal and Raise Dead 1/Day. Equal to
  Planetar (CR 16) minus 2, because it is mostly a healer.

## Not sure

1. **Lord of Contracts, Collect the Debt.** A creature killed by it loses its
   soul (into the ledger). The SRD has similar effects for strong fiends. The
   soul can be freed by a story, so I did not give a rule for it.
2. **Flux Mite and Flux Titan.** Each rolls a d4 at the start of its turn for
   a random benefit. This is the chaos theme, but it adds a roll for the GM.
3. **Star Whale** (CR 10): a mostly friendly giant of the void that can carry
   forty passengers. It is in the bestiary because a GM can also fight it.

## Two notes for you

1. **Thrown attacks (done).** The engine has the new kind "t" (commit
   `feat: add a thrown attack that uses Strength to the monster engine`).
   The four giants use it now (the orchestrator named three; the Lightless
   Giant in the underdark batch also used the workaround). The attack numbers
   in the PDF are the same before and after. One text change: the
   Multiattack line now says "using Club or Rock in any combination" in place
   of the old extra sentence.
2. **My push rule.** Each full build takes about 4.5 minutes, and five pushes
   in a row lost the race to other sessions. My push script now works like
   this: after a full build passes, if a push loses the race and the new
   remote commits change only `docs/` or the content folders of other
   sessions, it rebases, runs the tests and the content check (a few
   seconds), and pushes. If the new commits change the build code, the book
   sources, the tests, or my folders, it runs the full build again. Tell me
   if you want a full build after every rebase in all cases.

## Next

After approval: `feat: add 30 planar monsters`, then the progress docs
commit. Then NPC batch 3 (ready: 30 NPCs).
