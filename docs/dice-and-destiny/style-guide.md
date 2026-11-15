# Dice & Destiny style and balance guide

Each session that writes content for Edition 2 reads this guide first.
The design is in
[the Edition 2 design](../superpowers/specs/2026-11-15-edition-2-expansion-design.md).
The rules for the repository are in [`AGENTS.md`](../../AGENTS.md).

## 1. Voice

Write for a person who plays for the first time, but do not talk down to
that person. Use plain words, short sentences, and the second person
("you"). Use a dry, friendly tone. Give rules first and flavor second.

These two passages from the books are the model:

> Dice & Destiny is a game of collaborative storytelling. You play one hero;
> the Game Master (GM) plays the world and everyone else in it. There's no
> winning or losing, just a story you tell together, with dice deciding the
> uncertain moments.

> You are not the players' opponent. You are the person making sure everyone
> has a good story to tell afterwards.

Rules text uses the terms of the SRD 5.2: "Bonus Action", "Magic action",
"the Prone condition", "Long Rest", "Fire damage". Use capitals as the SRD
does.

## 2. Writing rules

- The text in `compendium/content/` and `compendium/books/` does not have to
  be in STE. All other text (code, comments, docs, commit messages) is in
  STE.
- Do not use an em-dash anywhere. Use a comma, a colon, a semicolon,
  parentheses, or a new sentence. An en-dash is correct in a number range, for example "levels 1–4".
- Do not use an emoji.
- Do not write "Dungeons & Dragons" or "D&D". Write "the game" or "fifth
  edition".
- Keep distances in feet, as the SRD does.

## 3. What "original" means

The SRD 5.2 is free to use. Content from a paid book is not. An entry can
fill the same role as content in a paid book, but its rules, its name, and
its text must be new.

- **Correct:** a sorcerer subclass whose power comes from a dragon. The
  idea is common. Write new features, a new name, and new text.
- **Not correct:** a subclass that uses the features of a paid subclass in
  a different order, or with new names.
- **Correct:** a large creature with many eyes that fires rays. Design new
  rays and give it a new name.
- **Not correct:** the same creature with the name and the rays of a paid
  monster.

When you are not sure, design from the role ("a tank that protects
allies"), not from a known entry.

## 4. Names

- A name is unique in its category. The build stops on a duplicate.
- Do not use a name that a publisher owns and that is not in the SRD 5.2.
  The build stops on each name in `BANNED` in
  [`check_content.py`](../../compendium/build/check_content.py). The list
  includes beholder, mind flayer, githyanki, yuan-ti, displacer beast, the
  names of published settings, and the names of characters in spell names
  (for example Mordenkainen, Bigby, Tasha). Other names that a publisher
  owns are also not permitted, even if the list does not have them.
- Do not use the name of an SRD entry for a new entry.

## 5. Entry formats

Each content folder in `compendium/content/` is a package. Put a new file in
the folder. The build finds it with no other change. Use the format of the
files that are already in the folder.

| Folder | Variable | Format |
|---|---|---|
| `subclasses/` | `SUBS` | `{"class": [(name, tagline, [(level, feature, text), ...]), ...]}` |
| `species/` | `SPECIES` | `(name, size, speed, description, [(trait, text), ...])` |
| `backgrounds/` | `BACKGROUNDS` | `(name, abilities, skills, tool, origin feat, equipment, flavor)` |
| `feats/` | `FEATS` | `(name, type, prerequisite, text)`. Type is Origin, General, Fighting Style, or Epic Boon. |
| `spells/` | `SPELLS` | `(name, level, school, classes, time, range, components, duration, concentration, ritual, description, higher levels)` |
| `monsters/` | `MON` | `M(name, size, type, alignment, CR, "Str Dex Con Int Wis Cha", ...)`. See `build/monster_engine.py`. |
| `items/` | `ITEMS` | `(name, category, rarity, attunement, text)` |
| `downtime/` | `STRONGHOLDS`, `DOWNTIME` | `STRONGHOLDS` is HTML for the GM book. `DOWNTIME` is a list of downtime activities (new format). |

The build only shows values that it knows. A subclass under a class key
that is not a class, a feat type other than Origin, General, Fighting Style,
or Epic Boon, or an item rarity other than Common, Uncommon, Rare, Very Rare,
Legendary, or Artifact disappears from the book. The content check stops on
each of these. A new class adds its key to `CLASS_KEYS` in
`content/classes/__init__.py`.

A new content folder must have one line in `REGISTRY` in
`compendium/build/check_content.py`. The line tells the check how to read
the names of the entries. The check stops on a folder that is not in
`REGISTRY`. The check also reads the text of every file in every folder for
em-dashes, the trademark, and banned names.

A new category (classes, NPCs, traps, tables, pantheons, systems, downtime
activities) needs a format. The workstream session proposes the format in
its first batch, with a renderer in `compendium/build/`, a placeholder in
the book source, and a test. The orchestrator approves the format before
more entries use it.

## 6. Power budgets

### Monsters

`build/monster_engine.py` calculates AC, hit points, attack bonuses, damage,
and save DCs from the CR and the ability scores. Use the engine. Do not
write these numbers by hand.

- In the text, write `{dc:con}`, `{atk:str}`, and `{2d6}`. The engine
  calculates the numbers.
- An `ac=` value can be lower than the target for the CR (for example, an
  ooze). It must not be more than 4 above the target. The minimum is 5.
- An `hp=` multiplier stays from 0.9 to 1.2.
- The build checks these limits.

The target table (from `monster_engine.py`):

| CR | AC | HP | Prof. | | CR | AC | HP | Prof. |
|---|---|---|---|---|---|---|---|---|
| 0 | 12 | 4 | +2 | | 9 | 16 | 155 | +4 |
| 1/8 | 12 | 9 | +2 | | 10 | 17 | 170 | +4 |
| 1/4 | 13 | 13 | +2 | | 11 | 17 | 185 | +4 |
| 1/2 | 13 | 22 | +2 | | 12 | 17 | 200 | +4 |
| 1 | 13 | 30 | +2 | | 13 | 18 | 215 | +5 |
| 2 | 13 | 45 | +2 | | 14 | 18 | 230 | +5 |
| 3 | 14 | 60 | +2 | | 15 | 18 | 245 | +5 |
| 4 | 14 | 75 | +2 | | 16 | 18 | 260 | +5 |
| 5 | 15 | 95 | +3 | | 17 | 19 | 290 | +6 |
| 6 | 15 | 110 | +3 | | 18 to 20 | 19 | 310 to 360 | +6 |
| 7 | 15 | 125 | +3 | | 21 to 24 | 20 to 21 | 400 to 500 | +7 |
| 8 | 16 | 140 | +3 | | | | | |

### Spells

The highest damage of a spell must not be more than 25% above this curve.
The build checks it. "Area" means the text has a Cone, Sphere, Cube, Line,
Cylinder, Emanation, wall, radius, "each creature", "each target", or "up to
N creatures". Damage in one sentence is added up. The values are average
damage. Each value is the damage of the strongest SRD spell of that level
and kind, so every SRD spell passes the check.

| Level | Single target | Area | SRD spell at the limit |
|---|---|---|---|
| Cantrip | 6 | 4 | Poison Spray, Produce Flame |
| 1 | 14 | 10 | Guiding Bolt, Burning Hands |
| 2 | 16 | 14 | Acid Arrow, Shatter |
| 3 | 27 | 28 | Fireball |
| 4 | 36 | 37 | Blight, Vitriolic Sphere |
| 5 | 49 | 37 | Contagion |
| 6 to 8 | 75 | 75 | Disintegrate |
| 9 | 99 | 140 | Power Word Kill, Meteor Swarm |

A spell that does not deal damage must have an effect that is equal to an
SRD spell of the same level. Name that SRD spell in the batch summary.

### Magic items

Compare each item with SRD items of the same rarity.

| Rarity | Examples of the power level |
|---|---|
| Common | A small trick or comfort. No bonus to a roll. |
| Uncommon | A +1 weapon or armor, or a spell of level 1 to 2 a few times each day. |
| Rare | A +2 weapon or armor, or a spell of level 3 to 4 once each day. |
| Very Rare | A +3 weapon or armor, or a spell of level 5 to 6. |
| Legendary | Changes how a character plays. A spell of level 7 or more. |

Attunement is necessary for an item that gives a constant bonus or a spell
that a character can cast many times.

### Feats

- **Origin** (level 1): a small benefit that a level 1 character can use.
  No ability score increase.
- **General** (level 4 or more): an ability score increase of 1, and a
  benefit equal to an SRD general feat.
- **Fighting Style:** equal to an SRD fighting style.
- **Epic Boon** (level 19 or more): an increase of 1 to an ability score
  (maximum 30), and one strong benefit.

### Subclasses

A new subclass gets features at the same levels as the SRD subclasses of
its class:

| Class | Levels | | Class | Levels |
|---|---|---|---|---|
| Barbarian | 3, 6, 10, 14 | | Monk | 3, 6, 11, 17 |
| Bard | 3, 6, 14 | | Paladin | 3, 7, 15, 20 |
| Cleric | 3, 6, 17 | | Ranger | 3, 7, 11, 15 |
| Druid | 3, 6, 10, 14 | | Rogue | 3, 9, 13, 17 |
| Fighter | 3, 7, 10, 15, 18 | | Sorcerer | 3, 6, 14, 18 |
| | | | Warlock | 3, 6, 10, 14 |
| | | | Wizard | 3, 6, 10, 14 |

Each feature is equal in power to the feature of the SRD subclass at the
same level.

### The optional systems

The optional systems can make characters stronger. They do not cost a feat
or a class feature. Each system chapter in the GM's book tells the GM how to
make encounters harder when the system is on (for example, "use monsters of
1 CR more" or "add one monster for each 4 characters"). A resource that a
system gives grows with the proficiency bonus. For example, Techniques give
points equal to the proficiency bonus, and they return on a short rest (the
design says this).

## 7. How a batch is made

1. A batch has entries from one category only, and at most 40 entries.
2. Run `compendium/build.sh`. It runs the tests, the content checks, the
   build, and the page check. All must pass.
3. Read the new pages in the PDF. Look for text that goes out of a box, bad
   breaks, and errors in the numbers.
4. Send the batch to the orchestrator session. Give the file names, the
   count of entries, and a list of the entries that are the most powerful,
   each with the SRD entry that it is equal to.
5. The orchestrator examines the batch against this guide. When the batch
   is correct, the orchestrator tells the session to commit and push.
6. Commit on `main`, with the human as the writer. A batch of entries is one
   commit, for example `feat: add 30 swamp and coast monsters`. A batch that
   also brings a new format is more than one commit, because each commit has
   one change only (`AGENTS.md`): first the renderer and its test, then the
   placeholder and the chapter in the book, then the entries.
7. If the push fails because `main` has new commits, fetch and rebase. Then
   run `compendium/build.sh` again before you push. If the rebase had a
   conflict in a line of another session, tell the orchestrator.
