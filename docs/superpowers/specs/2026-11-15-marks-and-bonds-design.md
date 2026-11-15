# Design: Marks and Bonds

Date: 2026-11-15.
Status: draft. All questions have answers. The human must approve the full
design before the systems session starts.

Parent design: [Edition 2 expansion](2026-11-15-edition-2-expansion-design.md).

## Intent

Marks and Bonds are two of the 8 optional systems of Edition 2. They are in
the Player's Compendium, in the "Optional Rules" part.

The model is the campaign *The Fountain of Divine*:

- Silvio has a curse that the story gave him. The curse has a cost and no
  benefit. Everyone at the table knows about it.
- Saimon took a gift (the Ember of the Unseen) without knowing its cost.
  Each time he uses its power, the GM secretly adds an Envy point. At 3 and
  5 points, the Witch of Envy gets more power over him.
- The Witch wants to break the friendship of Silvio and Saimon.

Marks make the curse and the Envy points into general rules. Bonds make the
friendship into rules. The two systems connect, so that "can the friendship
survive the Sin?" is a story that any group can play.

Each system also works alone. A GM can use one without the other.

## Goals

- A rules chapter for Marks and a rules chapter for Bonds, in the voice of
  the books.
- About 20 sample Marks: the 7 Sins, 7 Virtues, and about 6 Curses.
- One example of each Bond kind, and play examples.
- A GM section for each system: how to give it, how to run it, and how to
  make encounters harder when it is on.

## Non-goals

- No setting. The Sins and Virtues are general, not gods of one world.
- No change to the campaign files. The campaign can use the system later.

## Anti-goals

- A player must never lose a character without making a choice for it.
- A hidden Mark must not take the control of a character from the player
  except at the moments that the Mark text names.
- No Mark or Bond can stack with itself.

## Marks (all decided by the human)

| Part | Rule |
|---|---|
| Kinds | Blessing, Curse, Taint. A character carries up to 3 Marks. |
| Visibility | Each Mark is open or hidden. The player tracks an open Mark. The GM tracks a hidden Mark in secret, and the player only feels its effects. |
| How a character gets a Mark | From the story, or because the character looks for a bargain. The GM sets the price. A hidden Mark can hide a part of its price. |
| Parts of a Mark | A benefit (a Curse can have none), a cost, a track from 0 to 5, thresholds where the Mark changes, a trigger, and a way to end it. |
| What makes the track grow | A Taint grows when the character uses its power. A Blessing grows when the character acts on its virtue. A Curse grows through the story (the GM decides). |
| At 5 | A crisis. The player chooses: **give in** (the full power of the Mark, and the GM steers the character at the key moments that the Mark names), or **break free** (the Mark ends and leaves a scar: a small permanent trace). |
| How a Mark ends | Usually a quest or a choice, not a spell. Each Mark says how it ends. |

### Sample Marks

- **Taints (7):** Pride, Greed, Wrath, Envy, Lust, Gluttony, Sloth. The Envy
  Taint follows the Ember of the Unseen: extra damage when an ally does
  better than you, and the Sin hears you at 3 and whispers to you at 5.
- **Blessings (7):** one for each Sin, for example Humility, Charity,
  Patience, Kindness, Chastity, Temperance, Diligence. The writer can choose
  better names.
- **Curses (about 6):** for example a curse that blocks all help from allies
  (the model is Silvio's Curse of the Green Hollow).

## Bonds (all decided by the human)

| Part | Rule |
|---|---|
| Who | A character has up to 2 Bonds, with player characters or important NPCs. |
| Kinds | Friend, Rival, Debt, Oath. |
| Bond die | Starts at d4. When the two share a defining scene, the GM grows it one step: d6, d8, d10 (the maximum). |
| Use | Once each Short Rest, either partner can spend the bond to do one of these: add the die to the other's d20 Test after seeing the roll; as a Reaction, reduce damage to the other by the die plus the Proficiency Bonus; or use the special of the kind. |
| Specials | Friend: take a hit that was meant for the friend. Rival: when the rival succeeds, a bonus on your next roll. Debt: the one who owes can be called on once each adventure. Oath: both get an advantage when they act on the oath. The writer sets the exact rules. |
| Strain | Betrayal, abandonment, or a broken oath makes the bond die one size smaller. If it goes below d4, the Bond breaks. |

## The link between Marks and Bonds (decided by the human)

- When a character's Taint would grow, a bonded partner can spend the bond
  to stop it ("I'm not letting you become that").
- When a Bond breaks, the betrayed character gains 1 on a Taint that fits,
  for example Wrath or Envy. If the character has no such Taint, the GM can
  give one.
- A Curse can say that it also blocks bond help. Example: a Curse like
  Silvio's blocks the die and the damage reduction, but it does not block a
  partner who stops a Taint from growing.

## Power

The systems can make characters stronger (the parent design says this).
The GM section of each chapter says how to make encounters harder when the
system is on. The style guide gives the general rule.

## Where the content goes

- Folder: `compendium/content/systems/`. The format is new. The systems
  session proposes it in its first batch.
- The renderer: `compendium/build/render_systems.py`.
- One `REGISTRY` line in `compendium/build/check_content.py`.

## Decisions of the agent (after the builder check)

- **Books.** The Player's Compendium has the rules of both systems, the
  Bonds, and the open Marks (Blessings and Curses). The Game Master's
  Compendium has the Taints with their hidden prices, how to give and run
  Marks, and how to make encounters harder. A player does not read the
  hidden price of a Taint.
- **Bond use.** One use for each Bond each Short Rest, shared by the two
  partners. To stop a Taint uses it. The GM spends the bond for an NPC
  partner.
- **Power.** The benefit of a Mark before 5 is equal to an Uncommon magic
  item. The full power after a character gives in is equal to a Rare magic
  item.
- **Visibility.** Each Mark entry has a default (Taints hidden, Blessings
  and Curses open). The GM can change it.

## Answers of the human (after the builder check)

1. **A partner can stop a hidden Taint.** When a hidden Taint would grow,
   the GM describes a sign that the table can see (for example "a flicker of
   green in Saimon's eyes"). The bonded partner can spend the bond to stop
   it without knowing what the sign means. The Taint stays secret. At the
   crisis at 5, the GM reveals the Mark to its player.
2. **Giving in can be undone.** After a character gives in, the character
   keeps the full power and the steering of the GM. The way to end the Mark
   stays open, at a higher price that the Mark names. To break free still
   leaves a scar. A character is never lost unless the player chooses it.

## Left to the systems session

- The names of the Blessings and the Curses.
- The exact numbers of each Mark and of each Bond special.
- The format of a Mark entry and of the chapter.
- The play examples.
