"""Build Dice & Destiny: Beyond the Western Sea.

The book has these sources:
  books/western-sea/how-to-run.md, players-guide.md, gazetteer.md
  books/western-sea/chapters/NN-name.md     the chapters
  books/western-sea/handouts/NN-name.md     one handout on each page
  content/western_sea/                      the creatures, people, treasures, and places
  maps/western-sea/<id>.svg                 the final maps (farholm_maps.py)

The engine is in campaign.py. This file holds the Campaign record of the book. The book shows
each dice roll in two forms: the normal dice and, in brackets, the six-sided form (six_sided.py).

Usage: python3 build/western_sea.py [--screen | --check-maps | --check]   (run it in the compendium folder)
"""
import glob
import os
import sys

import campaign
import six_sided
from campaign import read

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the compendium folder
BOOK = os.path.join(ROOT, "books", "western-sea")

PAGES = (120, 140)  # the permitted page count of the print interior


def chapters(book=BOOK):
    """The chapters in order, as (number, key, Markdown). The number comes from the file name."""
    out = []
    for path in sorted(glob.glob(os.path.join(book, "chapters", "[0-9][0-9]-*.md"))):
        num = int(os.path.basename(path)[:2])
        out.append((num, f"ch{num}", read(path)))
    return out


def content():
    import content.western_sea as ws
    return ws


FRONT = dict(
    title="Beyond the Western Sea", sub_title="",
    sub="A ship sails west, past the edge of every chart. Nobody has ever come back to say what is out there.",
    compat="A campaign for levels 1 to 5. Requires the Dice &amp; Destiny Compendiums, Edition 2.",
)

PARTS = dict(
    run="How to run this book, the six-sided rules, the Storm Cube, and the guide to give to the players.",
    story="The story of the book, from the wreck on the shore to the storm season.",
    world="The island of Farholm: its colony, its two peoples, and its history.",
    reference="The creatures, people, treasures, and places of the book from A to Z, the handouts, and the index.",
)

WESTERN_SEA = campaign.Campaign(
    name="western-sea", book=BOOK, content=content, front=FRONT, css="western-sea.css", parts=PARTS,
    chapters=chapters, maps="farholm_maps", post=six_sided.add_brackets,
)


def check_pages(n):
    """A message when the page count n is outside PAGES, else None."""
    low, high = PAGES
    if low <= n <= high:
        return None
    return f"{WESTERN_SEA.name}: the print interior has {n} pages. It must have {low} to {high} pages."


def source_dice_errors(book=BOOK):
    """One message for each "d20" or "d100" in a Markdown file of the book."""
    msgs = []
    for path in sorted(glob.glob(os.path.join(book, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(path, book)
        msgs += [f"{rel}: {m}" for m in six_sided.check_dice(read(path))]
    return msgs


def missing_maps():
    """The ids of the maps with no final file. The book is not released while this list is not empty."""
    return campaign.missing_maps(WESTERN_SEA)


def pdf_pages(path):
    """The page count of the PDF at path."""
    from pypdf import PdfReader
    return len(PdfReader(path).pages)


def build_book(screen=False, build=campaign.build_book, count=pdf_pages):
    """Build the print interior (western-sea.pdf) or the screen interior (western-sea_screen.pdf).

    The build stops if the print interior has a page count outside PAGES."""
    build(WESTERN_SEA, screen)
    if not screen:
        msg = check_pages(count(f"{WESTERN_SEA.name}.pdf"))
        if msg:
            raise SystemExit(msg)


def main(args):
    if "--check-maps" in args:
        gone = missing_maps()
        if gone:
            raise SystemExit("western-sea: these maps have no final file in compendium/maps/western-sea/: "
                             + ", ".join(gone))
        print("western-sea: each map is final")
        return
    if "--check" in args:
        errs = source_dice_errors()
        if errs:
            raise SystemExit("western-sea: the book source has dice that are not permitted:\n  " + "\n  ".join(errs))
        print("western-sea: the dice of the book source are correct")
        return
    build_book("--screen" in args)
    print(WESTERN_SEA.name, "screen" if "--screen" in args else "print", "done")


if __name__ == "__main__":
    main(sys.argv[1:])
