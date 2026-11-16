# Review request: systems, batch 6 (Techniques, set 2: 26 entries)

Systems batch 6: 11 Spell Shapings and 15 maneuvers for skills and
movement. Not committed. This batch is on top of batches 2 to 5, which are
also not committed. build.sh passes with all five: 93 tests, content check,
page check, Type 3 check. Player 252 pages. No em-dash. With batch 5, the
total is 59 techniques (the design says about 60): 10 stances, 38
maneuvers, 11 shapings.

## Files

One commit after approval: `feat: add 26 spell shapings and skill maneuvers`.

- `compendium/content/systems/techniques_shaping.py`: 26 Techniques.

## Originality

No shaping copies an SRD Metamagic option. I left out shapings that were
too near: a change of damage type (Transmuted), protecting allies in an area
(Careful), more range (Distant), a longer duration (Extended), a second
target (Twinned), no components (Subtle), and a counterspell. The nearest
is Push the Weave (cast one slot level higher), which no Metamagic does.
Maneuvers that I left out because a class feature in the SRD has them: Hide,
Dash, Disengage, or Use an Object as a Bonus Action (Rogue), Slow Fall
(Monk). Roll With the Fall (half falling damage, 1 point, Reaction) is the
nearest to Slow Fall.

## Budget

Strongest entries, with the SRD entry that each is equal to:

- Push the Weave (3 points, level 11): cast as one slot level higher. Once
  each Short Rest for most characters at level 11 (4 points).
- Held Breath (2, level 5): delay an area spell to the start of the next
  turn and move its origin up to 30 feet.
- Binding Word (2, level 5): Speed 0 for one creature that failed the save.
  Compare: the rider of Ray of Frost, stronger, for 2 points.
- Untouchable Passage (3, level 11): no Opportunity Attacks, move through
  creatures, ignore Difficult Terrain for one turn. Compare: Freedom of
  Movement (level 4) for one turn.
- Spell Ward (1): add the Proficiency Bonus to a save against a spell.
  Compare: Resistance cantrip (1d4), stronger, as a Reaction.
- Listen Closely (1): know where creatures within 15 feet are, also
  invisible ones, for one turn. Compare: Blindsight 15 feet for one turn.

## Things I am not sure of

1. Spell Ward is a maneuver (anyone can learn it), not a shaping, because it
   does not change a spell that you cast.
2. Second Spark is the only technique for cantrips. It is 1 point for a
   reroll of a missed cantrip attack.
3. Next: Legend paths (a new format: a renderer and the rules first, then
   the paths).
