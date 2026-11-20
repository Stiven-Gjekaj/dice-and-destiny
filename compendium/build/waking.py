"""Build The Dawnwatch, Book One: Waking.

The book has these sources:
  books/waking/how-to-run.md, players-guide.md, gazetteer.md
  books/waking/chapters/NN-name.md          chapters 2 to 10
  books/waking/handouts/NN-name.md          one handout on each page
  adventures/tutorial-one-shot/             chapter 1 (the build reads it from there)
  content/dawnwatch/                        the creatures, people, treasures, and places

A source that does not exist yet is left out. The book builds with the files that exist.
The engine is in campaign.py. This file holds the Campaign record of Waking and the parts that
only Waking has: chapter 1 from the tutorial adventure.

Usage: python3 build/waking.py [--screen] [--check-maps]   (run it in the compendium folder)
"""
import dataclasses
import glob
import importlib.util  # noqa: F401  (the tests replace importlib.util.find_spec through this module)
import os
import re
import sys

import campaign
import waking_md as wm
from campaign import (  # noqa: F401  (the names that the tests and the other modules use)
    ANCHOR_MARK, HIDE_MARKS, IDX, KINDS, WARNINGS, chapter_head, chapters_line, dw_stat_html, entries, fill,
    handout_ref_html, handouts, handouts_html, hide_marks, index_html, insert_blanks, letter_of, map_html,
    marks_in_pages, page_list, passes, place_name, place_text, publish, read, recto_marks, remove_work,
    section_file, section_html, sort_key, statblock_html, treasure_html, warn, without_chapters, work_name,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the compendium folder
BOOK = os.path.join(ROOT, "books", "waking")
TUTORIAL = os.path.join(ROOT, "..", "adventures", "tutorial-one-shot")


# ------------------------------------------------------------------ sources

TUTORIAL_PARTS = ["README.md", "sessions/01-the-last-watch/README.md", "statblocks.md", "pregens.md", "cheat-sheet.md"]
MD_FILE_LINK = re.compile(r"^- \[[^\]]+\]\([^)]*\.md[^)]*\)\s*\n", re.M)


def tutorial_text(root=TUTORIAL, title="The Last Watch"):
    """Chapter 1 from the tutorial adventure, as one Markdown text.

    The overview comes first, then the scenes, then the statblocks, the pregenerated
    characters, and the cheat sheet. The list of files and the links to them go out."""
    readme, session, *rest = [read(os.path.join(root, p)) for p in TUTORIAL_PARTS]
    readme = wm.drop_section(wm.drop_title(readme), "Files")
    session = drop_one_shot(MD_FILE_LINK.sub("", wm.drop_title(session)))
    return "\n\n".join([f"# {title}", readme, session] + [wm.demote(t) for t in rest])


# The one-shot ends with hooks for a second session of a GM's own. They do not fit the campaign, so the book
# leaves them out: from this paragraph to the next heading of the same level or higher, or to the end.
ONE_SHOT = re.compile(r"^If you play this adventure alone\b.*?(?=^#{1,2} |\Z)", re.M | re.S)


def drop_one_shot(text):
    """The session text with no hooks for a second one-shot session."""
    return ONE_SHOT.sub("", text).rstrip() + "\n"


def chapters(book=BOOK, tutorial=TUTORIAL):
    """The chapters in order, as (number, key, Markdown). Chapter 1 is the tutorial.

    A chapter file has a name such as 02-brannocks-ford.md. The number comes from the name."""
    out = [(1, "ch1", tutorial_text(tutorial))] if os.path.isdir(tutorial) else []
    for path in sorted(glob.glob(os.path.join(book, "chapters", "[0-9][0-9]-*.md"))):
        num = int(os.path.basename(path)[:2])
        if num != 1:
            out.append((num, f"ch{num}", read(path)))
    return out


def content():
    import content.dawnwatch as dw
    return dw


# ------------------------------------------------------------------ the record of the book

FRONT = dict(
    title="The Dawnwatch", sub_title="Book One: Waking",
    sub="Five heroes wake after three hundred years. The world forgot them. Their enemy did not.",
    compat="A campaign for levels 1 to 10. Requires the Dice &amp; Destiny Compendiums, Edition 2.",
)

PARTS = dict(
    run="How to run this book, and the guide to give to the players.",
    story="The story of Book One, from the waking in the crypt to the empty crystal in the old capital.",
    world="The land of today: its regions, its towns, and the ruins of the old kingdom.",
    reference="The creatures, people, treasures, and places of the book from A to Z, the handouts, and the index.",
)

# A name that does not match before these words. "The Corrin side" and "the Tey half" are the halves of
# Corrantey, the old towns, not the rivers. The shorter name ("Corrin", "Tey") matches them.
NOT_BEFORE = {"The Corrin": r"\s+(?:side|half)\b", "The Tey": r"\s+(?:side|half)\b"}

# Other forms of an entry name in the text. The text calls the black stone "the black stone", in lower case.
EXTRA_FORMS = {"The Black Stone": ["black stone"]}

# Index terms that are not content names: (the name in the index, the forms in the text).
# A term has no appendix entry, so it has no link.
INDEX_TERMS = [
    ("Wick", ["Wick"]),
    ("Malgrath, the Unlit King", ["Malgrath", "Unlit King"]),
    ("The Morning Flame", ["Morning Flame"]),
    ("The Grey Winter", ["Grey Winter"]),
    ("The Dawn Door", ["Dawn Door"]),
    ("The Hush", ["Hush"]),
    ("Church of the Five Sleepers", ["Church of the Five Sleepers", "Church"]),
    ("Lampwrights", ["Lampwrights", "Lampwright"]),
    ("Hall of Sleepers", ["Hall of Sleepers"]),
    ("The Dawnfire", ["Dawnfire"]),
    ("Bonds", ["Bonds"]),
    ("Journeys", ["Journeys"]),
    ("Marks", ["Marks"]),
    ("Factions and Renown", ["Factions and Renown", "Renown"]),
    ("Crafting and Gathering", ["Crafting and Gathering", "Crafting"]),
    ("Strongholds", ["Strongholds", "Stronghold"]),
    ("Techniques", ["Techniques"]),
    ("Injuries and Scars", ["Injuries and Scars", "Injuries"]),
]

WAKING = campaign.Campaign(
    name="waking", book=BOOK, content=content, front=FRONT, css="waking.css", parts=PARTS,
    # TUTORIAL is read when the build runs, so a test can change it.
    chapters=lambda book: chapters(book, TUTORIAL),
    maps="maps", extra_forms=EXTRA_FORMS, not_before=NOT_BEFORE, index_terms=INDEX_TERMS,
)


def waking(book=BOOK, tutorial=TUTORIAL):
    """The record of Waking with other source folders."""
    return dataclasses.replace(WAKING, book=book, chapters=lambda b: chapters(b, tutorial))


# ------------------------------------------------------------------ the engine with the forms of Waking

def mention_pattern(names):
    return campaign.mention_pattern(names, NOT_BEFORE)


def named_in(name, chs):
    return campaign.named_in(name, chs, EXTRA_FORMS, NOT_BEFORE)


def mark_mentions(h, es, screen=False):
    return campaign.mark_mentions(h, es, screen, EXTRA_FORMS, NOT_BEFORE)


def index_terms(es, terms=INDEX_TERMS):
    return campaign.index_terms(es, terms)


def entry_html(e, chs):
    return campaign.entry_html(e, chs, EXTRA_FORMS, NOT_BEFORE)


def appendices_html(dw, chs):
    return campaign.appendices_html(dw, chs, EXTRA_FORMS, NOT_BEFORE)


def front(screen=False):
    return campaign.front(WAKING, screen)


def body_parts(dw, book=BOOK, tutorial=TUTORIAL, screen=False):
    return campaign.body_parts(waking(book, tutorial), dw, screen)


def expand(screen=False, inside_mm=None, book=BOOK, tutorial=TUTORIAL, dw=None):
    return campaign.expand(waking(book, tutorial), screen, inside_mm, dw)


def missing_maps(book=BOOK):
    """The ids of the maps with no final file. Waking is not released while this list is not empty."""
    return campaign.missing_maps(dataclasses.replace(WAKING, book=book))


def build_book(screen=False):
    """Build the print interior (waking.pdf) or the screen interior (waking_screen.pdf).
    The build calls expand and passes through this module, so a test can replace them."""
    campaign.build_book(WAKING, screen, expand_fn=lambda s, i: expand(s, i),
                        passes_fn=lambda *a, **k: passes(*a, **k))


if __name__ == "__main__":
    if "--check-maps" in sys.argv[1:]:
        gone = missing_maps()
        if gone:
            raise SystemExit("waking: these maps have no final file in compendium/maps/: " + ", ".join(gone))
        print("waking: each map is final")
        sys.exit(0)
    build_book("--screen" in sys.argv[1:])
    print(WAKING.name, "screen" if "--screen" in sys.argv[1:] else "print", "done")
