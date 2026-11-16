# Review request: systems, batch 3 (Bonds)

Systems batch 3: the rules of Bonds and the 4 Bond kinds. Not committed.
This batch is on top of batch 2 (the 20 sample Marks, also not committed).
build.sh passes with both batches: 81 tests, content check, page check,
Type 3 check. Player 242 pages (Bonds add 2), GM 233 pages. No em-dash.

## Files

Proposed commits (after approval, and after batch 2):

1. `feat: add the Bonds chapters`
   - `compendium/books/player.src.html`: Chapter 29 "Bonds" after Chapter 28,
     with the placeholder `{{SYS_BONDS}}`. Sections: what a Bond is, forming,
     growing the die, using a Bond, strain, Bonds and Marks.
   - `compendium/books/gm.src.html`: Chapter 22 "Running Bonds" after
     Chapter 21. Sections: starting Bonds, defining scenes, strain without
     cruelty, power and encounters. "Cheat Sheets & Templates" is now
     Chapter 23.
   - `compendium/build/build.py`: the placeholder `{{SYS_BONDS}}` and 2
     chapter icons.
2. `feat: add the four kinds of Bond`
   - `compendium/content/systems/bonds.py`: Friend, Rival, Debt, Oath.

## The rules (from the design, with the numbers that I set)

- Up to 2 Bonds for each character. Two characters share only one Bond.
- The die starts at d4 and grows one step after a defining scene: d6, d8,
  d10 (maximum). I set: at most one step each session.
- One use each Short Rest, shared by the two partners. The partners must see
  or hear each other. The uses: add the die to the partner's d20 Test after
  the roll; a Reaction to reduce damage to the partner by the die plus the
  Proficiency Bonus; the special of the kind; or stop a Taint from growing.
- Strain: the die is one size smaller. Below d4, the Bond breaks. The
  partners can also end a Bond in peace, with no break.
- Link to Marks: as in the design. A Curse that blocks bond help blocks the
  die, the damage reduction, and the specials, but not the stop of a Taint.

## The specials (the strongest entries)

- Friend, "I've Got You": a Reaction to move up to half Speed to the friend
  and become the target of an attack that hit. Compare: the Protection
  fighting style and the Sentinel-type features. It costs the shared use.
- Rival, "Not to Be Outdone": when the rival succeeds, add the die to your
  next d20 Test. Compare: Bardic Inspiration (one use).
- Debt, "Called In": once each adventure, the die on each d20 Test for one
  task until the end of the scene. This is the strongest special in a skill
  scene (about +5.5 on each roll with a d10), but only once each adventure.
- Oath, "Sworn Purpose": a Bonus Action; both partners have Advantage on
  d20 Tests that serve the oath until the start of the next turn of the
  spender.

## Power and encounters (GM chapter)

A d10 Bond adds about 5 to one roll or prevents about 10 damage once each
Short Rest. With most Bonds at d8 or d10: add one monster of the lowest CR of
the encounter for each 4 characters, or give each important enemy 10% more
Hit Points.

## Things I am not sure of

1. "At most one step each session" for the die is my number. The design does
   not limit it.
2. The Debt special is "once each adventure" (from the design), and it also
   uses the shared Short Rest use. Tell me if it must not use the shared use.
3. Oath: when the oath is fulfilled, the die grows one step. This is a second
   way to grow the die, outside the defining scenes.
4. The heading "The Four Kinds of Bond" is in the book source. In commit 1 it
   has no entries under it until commit 2 adds them.
