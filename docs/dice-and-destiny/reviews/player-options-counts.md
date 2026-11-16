# Review request: player options, the counts in the chapter intros

This is not a batch of entries. It is a small change to shared files. I
asked about it in `player-options-spells-2.md` (the question about shared
text). It is not committed.

## The problem

Two chapter intros in `compendium/books/player.src.html` had numbers
written by hand that were wrong after the batches:

- "Twelve new backgrounds and two new species." (now 40 and 20)
- "Forty-seven new spells, from cantrips to 9th level." (now 220)

## The change (one commit)

It uses the same pattern as your `render_counts.py`, so that the counts
come from the content and stay correct.

- `compendium/build/render_counts.py`: added `origin_counts`,
  `spell_counts`, `all_origin_counts`, and `all_spell_counts` (lines
  added, nothing else changed).
- `compendium/build/build.py`: added two placeholders,
  `{{O_COUNTS_ORIGINS}}` and `{{O_COUNTS_SPELLS}}` (two lines added).
- `compendium/books/player.src.html`: the two intro lines now use the
  placeholders.
- `compendium/tests/test_render_counts.py`: two tests that build their own
  lists.

The book now says "40 new backgrounds and 20 new species." and "220 new
spells, from cantrips to 9th level." I checked this in the PDF text.

## Not changed

`compendium/build/cover.py` line 58 still says "47 new spells". The cover
belongs to you. The same `all_spell_counts()` can give the number there.
