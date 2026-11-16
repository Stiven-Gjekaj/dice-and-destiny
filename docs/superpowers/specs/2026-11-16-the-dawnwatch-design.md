# Design: The Dawnwatch

Date: 2026-11-16.
Status: draft. The human reviews it before work starts.

Related designs: [Dice & Destiny](2026-11-15-dice-and-destiny-design.md),
[Edition 2 expansion](2026-11-15-edition-2-expansion-design.md).

## Intent

Edition 2 gives the GM the parts to build any world. It has no setting and
no campaign. The Edition 2 design says: "Ready-made campaign books come
later."

The Dawnwatch is the first campaign book. It is a third book, next to the
Player's Compendium and the Game Master's Compendium. It continues the
tutorial adventure, [The Last Watch of the Sleepers](../../../adventures/tutorial-one-shot/README.md),
into a full story from level 1 to level 20.

The short form: Edition 2 gives you the parts. The Dawnwatch gives you a
world to play in.

## The story base

The tutorial already starts the story:

- Three hundred years ago, **Malgrath, the Unlit King**, tried to put out
  the sun. The old kingdom pushed him back into the dark.
- The kingdom put five guards, **the Dawnwatch**, to sleep in crystal under
  **Dawnwatch Keep**. They wait for his return.
- Today the crystal cracks. The characters are the Dawnwatch. Their guide
  is **Wick**, a talking brass lantern.
- The tutorial ends when the characters reach the surface and see how much
  the world changed.

The campaign starts at that moment. The finale is the fight against
Malgrath for the sun.

## Name and versions (decided by the human)

- The book is **The Dawnwatch**, a campaign for Dice & Destiny.
- It is not "Edition 3". An edition is a new version of the two
  Compendiums. The Dawnwatch is a new product, and it does not change the
  Compendiums.
- The Dawnwatch has its own versions: `dawnwatch-1`, `dawnwatch-2`, and so
  on. The Compendiums keep `edition-N`.
- Each Dawnwatch release says which Compendium edition it needs, for
  example "Requires Edition 2".

## Goals

- A campaign from level 1 to level 20 (decided by the human).
- The tutorial is chapter 1 of the book, with no change to its rules
  lessons.
- A gazetteer of the present-day world (decided by the human).
- New content for the story: monsters, NPCs, and unique magic items
  (decided by the human).
- A short player's guide (decided by the human).
- A reference part, so that the GM can find each name fast.
- Print as an A4 hardcover at Lulu, as the two Compendiums are.

## Non-goals

- No change to the two Compendiums. Their page counts and spines stay the
  same.
- No new player options (classes, subclasses, species, feats, spells). The
  players use the Player's Compendium.
- No new rules system. The story uses the 8 optional systems of Edition 2.

## Anti-goals

- **Filler.** The Edition 2 rule applies: an entry that only renames
  another entry does not count.
- **Copied paid content and trademarks.** The Edition 2 rules apply.
- **Spoilers in the player's part.** The player's guide and the handouts
  must not tell anything about the present-day world.
- **Em-dashes.** None anywhere. `AGENTS.md` has the rule.
- **A book that is too large.** The book stays below 700 pages, as the
  Compendiums do.

## Structure of the book

### For the GM

1. **How to run this campaign.** The arc, the level of each chapter, and
   how to start with new players or with a group that knows the game.
2. **Chapter 1: The Last Watch.** The tutorial. It still teaches the core
   rules, one rule for each scene.
3. **The chapters of the campaign.** Each chapter is one part of the story
   and one region of the world. Each chapter adds one of the 8 optional
   systems when the story needs it (for example Journeys for a long road,
   Strongholds for a base). So the book teaches the full game, step by
   step, as the tutorial teaches the core rules.
4. **The finale.** Malgrath and the sun.

### The world: then and now (decided by the human)

The Dawnwatch slept for 300 years. They know the old world only. The book
uses this gap:

- **The player's guide shows the world as it was 300 years ago.** The old
  kingdom, the Dawnwatch oath, the first war against Malgrath, and
  backgrounds from that time. It cannot spoil the campaign, because the
  campaign is about how much that picture is now wrong.
- **Wick tells the player's guide**, in his own voice. The GM can read it
  aloud, or the players can read it.
- **The gazetteer shows the world of today.** It is in the GM's part only.
  The players find it at the table. The gazetteer has the regions, the
  factions, the history of the 300 lost years, and a map. A GM can also
  run new stories in it.

### Handouts

An appendix of handouts: maps, letters, and notes from Wick. Each handout
is on its own page with nothing on the back, so that the GM can print or
copy it.

### Reference (the "wiki" part)

- **In the chapters:** a creature that appears in only one scene has its
  statblock on that page. The GM does not turn pages in a fight.
- **Appendices, from A to Z:**
  - **Creatures:** the new monsters, with full statblocks.
  - **People:** each named NPC, with a one-line role, the chapters where
    the NPC appears, and a statblock if the NPC fights.
  - **Places:** the gazetteer entries, with the chapters that use them.
  - **Treasures:** the unique magic items.
- **Index:** each name, with its page numbers.
- **Screen edition:** each name is a link to its entry.

## The tutorial after the change (decided by the human)

The tutorial lives in two places:

- It is chapter 1 of The Dawnwatch.
- It stays as a free adventure in `adventures/tutorial-one-shot/`. It still
  works alone. At the end, it gets a short hook into the book.

One source makes both. The adventure must not exist as two copies that
change apart.

## Content and build

- The new content goes into `compendium/content/dawnwatch/`. The collector
  reads each file in a content folder, so the Compendium folders must not
  hold Dawnwatch content. A separate folder keeps the Compendiums the same.
- The new content uses the same formats, the same balance guide, and the
  same checks as the Compendium content.
- The build makes a third book from `compendium/books/dawnwatch.src.html`,
  in the same forms as the Compendiums: screen, home print, Lulu interior,
  and Lulu hardcover cover.
- The build makes the index with the page numbers. It finds them in the
  same way as it finds the page numbers of the table of contents.

## Releases and the README (decided by the human)

- A tag `edition-N` makes a release of the two Compendiums. A tag
  `dawnwatch-N` makes a release of The Dawnwatch.
- GitHub has only one "latest" release for each repository. So the
  workflow also keeps one rolling release for each product:
  `compendium-latest` and `dawnwatch-latest`. Each release of a product
  replaces the files of its rolling release.
- The README links to the files of the rolling releases, for example
  `releases/download/dawnwatch-latest/<file>.pdf`. These links always give
  the newest version, and no commit is necessary after a release.
- The README has one row for each product: its newest PDFs, its Lulu
  hardcover, and the Compendium edition that it needs. A product that comes
  later gets its own row and its own rolling release.
- The release workflow does not write commits. A commit has a human writer.

## Questions for the human

1. The name of the world and of the present-day kingdom or kingdoms.
2. The number of chapters, and the level range of each chapter.
3. A map: who makes it, and in which style. The books have no art at this
   time.
4. Is Wick with the party for the full campaign, or only for part of it?
5. The tone after the tutorial. The tutorial is spooky with a funny guide.
   Does the campaign stay light, or does it become darker toward the end?

## Left to the builder

- The order of the work after the human answers the questions.
- The page budget of each chapter, inside the 700-page limit.
- The names of the chapters.
