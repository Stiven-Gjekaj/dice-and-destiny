"""Sample pantheons. Each file adds a list PANTHEONS.

A PANTHEONS entry is a dict with these keys:
  name: the name of the pantheon
  summary: a short text that tells who worships the pantheon and how its gods relate
  gods: a list of gods. A god is a dict with these keys:
    name: the name of the god
    title: a title such as "the Lantern Queen", or ""
    portfolio: what the god rules, in a few words
    alignment: an SRD alignment, for example "Lawful Good"
    symbol: the holy symbol, in words
    domains: a list of the cleric domains that suit the god. Each is the SRD
      "Life Domain" or an original cleric subclass. An empty list means any domain.
    wants: what the god wants
    worshippers: who worships the god, and one custom of the faithful

In all text, [[label]] shows the label in bold.
"""
from content.collect import collect_list

PANTHEONS = collect_list(__name__, "PANTHEONS")
