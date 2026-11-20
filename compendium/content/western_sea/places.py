"""The places of Beyond the Western Sea.

This list is the single source for the maps, the Places appendix, and the
index. Each place is a dict with the keys of content/dawnwatch/places.py.
"""

PLACES = []

# Each road is (from, to, kind, era, via), as in content/dawnwatch/places.py.
ROADS = []


def place(name):
    """Return the place with this name. Raise KeyError if there is none."""
    for p in PLACES:
        if p["name"] == name:
            return p
    raise KeyError(name)
