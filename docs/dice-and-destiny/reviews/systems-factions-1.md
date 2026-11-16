# Review request: systems, batch 12 (10 sample factions)

Systems batch 12: 10 sample factions, each with a goal, the deeds that win
and lose renown, a rival, and 5 ranks. Not committed. build.sh passes: 228
tests, content check, page check, Type 3 check. GM 428 pages (the factions
add 4). No em-dash. This is the last batch of the systems workstream.

## Files

One commit after approval: `feat: add 10 sample factions`.

- `compendium/content/systems/factions.py`: The Grey Hand, The Lantern
  Watch, The Masked Hours, The Road League, The Quill Archive, The Chained
  Crown, The Antlered Wardens, The Red Banner Company, The Anvil Guild,
  The Barrow Keepers.
- `compendium/books/gm.src.html`: the heading "Sample Factions" before
  `{{SYS_FACTIONS}}` (it comes with the entries).

## Ties to other chapters

- Gods of the Pantheons chapter: Nessaly (Grey Hand), Aurenne (Lantern
  Watch), Ombrel (Masked Hours), Vessa (Road League), Ilvane (Quill
  Archive), Varrak (Chained Crown), the Antlered Mother (Antlered Wardens),
  Sereth (Red Banner Company), Hald (Anvil Guild), the Hollow Queen (Barrow
  Keepers). Rivals name other gods (Mother Rot, the Horned Rider).
- The rival pairs give a GM ready conflicts: Lantern Watch and Masked
  Hours; Quill Archive and Chained Crown; Anvil Guild and Masked Hours.
- The Road League fits Journeys; the Anvil Guild fits crafting ("help
  that halves the time of a crafting project").
- The chapter already points to the Faction Builder and the other faction
  tables in World-Building Tables for more factions.

## Budget (the reward ladder of the chapter)

Every faction follows the ladder: rank 3 a small comfort, 10 a discount of a
fifth and a contact, 20 a safe place and an Uncommon item on loan, 35 a band
to command and a Rare item or a free spell service of level 5 or lower
(Greater Restoration, Legend Lore once a month, Speak with Dead), 50 a seat
of power and a Very Rare item, counted as treasure.

## Things I am not sure of

1. The Chained Crown is a villain faction (Varrak, tyranny). Its ranks
   work for characters who infiltrate it, or for the GM's NPCs. Its rank 5
   reward is a story reward (a throne, or the power behind one).
2. The names all start with "The", so they sort by the second word in the
   reader's eye but by "The" in the code. The order is still alphabetical.
