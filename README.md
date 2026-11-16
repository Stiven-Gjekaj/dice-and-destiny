# Dice & Destiny

Dice & Destiny is an independent tabletop roleplaying game.
It is a rules-compatible guide for fifth edition (2024).

Dice & Destiny has two books:

- **The Player's Compendium.** It teaches new players how to play. It holds
  all twelve SRD classes, the species, the backgrounds, the feats, the
  equipment, all SRD spells, and the full rules reference. It also holds
  original content: 4 classes, 96 subclasses, 20 species, 40 backgrounds,
  120 feats, 220 spells, and the player rules of the optional systems.
- **The Game Master's Compendium.** It teaches the GM how to run the game.
  It holds the SRD bestiary and magic items, and original content:
  651 monsters, 100 NPCs, 822 magic items, 80 traps and hazards,
  50 sets of world-building tables, 2 pantheons with 24 gods,
  10 downtime activities, strongholds, cheat sheets, and templates.

The 8 optional systems are Marks, Bonds, Techniques, Legend paths, Journeys,
Factions and renown, Injuries and scars, and Crafting and gathering. The
player rules are in the Player's Compendium. The GM rules are in the Game
Master's Compendium.

## Get the books

Go to [Releases](https://github.com/Stiven-Gjekaj/dice-and-destiny/releases).
Each release has four files for each book. Choose the files for what you
want to do:

| Use | File | What it is |
|---|---|---|
| Read on a screen | `...-screen.pdf` | Color, with a front cover. The contents link to the chapters, and the bookmarks list the parts and chapters. |
| Print at home | `...-home-print.pdf` | A4, black and white, with a front page and a blank back. Print it on both sides. The wide inside margin has space for punched holes. |
| Print a hardcover at Lulu | `...-lulu-interior.pdf` and `...-lulu-cover.pdf` | The interior with no cover, and the wraparound cover for a Lulu A4 casewrap hardcover. Upload the two files to Lulu. |

- A **preview** release comes from each change to the books.
- An **edition** release is a finished edition.

To build the books yourself, read [`compendium/README.md`](compendium/README.md).

## What is in this repository

| Folder | Contents |
|---|---|
| [`compendium/`](compendium/) | The source of the two books and the build system |
| [`campaigns/`](campaigns/) | Campaigns that use Dice & Destiny |
| [`adventures/`](adventures/) | One-shots and short adventures |
| [`docs/`](docs/) | Design documents and plans |

Each campaign and each adventure has its own folder. Each of these folders
has a `sessions/` folder. Each session has its own folder, with a number in
front of the name.

## Campaigns

- [The Fountain of Divine](campaigns/the-fountain-of-divine/README.md)

## Adventures

- [The Last Watch of the Sleepers](adventures/tutorial-one-shot/README.md): a
  tutorial one-shot that teaches new players the rules.

## License

- The code is under the MIT license. See [`LICENSE`](LICENSE).
- The original text and content are under CC BY-NC-SA 4.0. See
  [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md).
- The SRD 5.2 material is under CC BY 4.0.

[`NOTICE.md`](NOTICE.md) shows which license applies to each folder.
Dice & Destiny is not affiliated with, endorsed, sponsored, or approved by
Wizards of the Coast.
