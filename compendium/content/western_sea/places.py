"""The places of Beyond the Western Sea.

This list is the single source for the maps, the Places appendix, and the
index. The facts come from the world bible:
docs/superpowers/specs/2026-11-16-dawnwatch-world.md, section "Farholm,
beyond the map".

Each place is a dict with the keys of content/dawnwatch/places.py, with
these changes:

- x, y: the position in miles from the north-west corner of the map of
  Farholm, not of the land. x goes east and y goes south. The map is W miles
  from west to east and H miles from north to south.
- kind: one of KINDS below.
- chapters: 1 is "The Wreck of the Good Intent", 2 is the island, and 3 is
  "Storm Season".
- era: always "now". The book has no old map.
- ring: "outer" (levels 2 to 3) or "inner" (levels 3 to 4) for a site of
  the island in chapter 2. None for a place that is not a site.
"""

W, H = 24, 16  # the size of the map of Farholm in miles

PLACES = [
    # ---- The island ----
    dict(name="Farholm", kind="island", x=12, y=8, area=(2, 2, 22, 14), era="now",
         ring=None, chapters=(1, 2, 3),
         summary="The island on no map, the back of the sleeping Grandam. The colonists named it."),
    dict(name="The Fleet", kind="river", x=15, y=9, era="now", ring=None, chapters=(1, 2),
         course=[(12, 6), (13, 7.5), (14.5, 8.5), (15.5, 10), (17, 11), (17.5, 12)],
         summary="A small stream from the Kettles to the sea at Hythe. Its banks split the town."),

    # ---- Chapter 1: the wreck and the shore ----
    dict(name="The wreck of the Good Intent", kind="wreck", x=10, y=15, era="now", ring=None,
         chapters=(1,),
         summary="The merchant ship of the party, broken on the reef off Wreckers' Bay."),
    dict(name="Wreckers' Bay", kind="bay", x=10.5, y=13.5, era="now", ring=None, chapters=(1,),
         summary="A wide bay of grey sand on the south coast. The sea brings the wrecks here, and the colonists come for them."),

    # ---- The outer ring: the coast, the colony, and the two sides ----
    dict(name="Hythe", kind="town", x=17.5, y=11.5, era="now", ring="outer", chapters=(1, 2, 3),
         summary="The colony town at the mouth of the Fleet. The Corrin men live on the east bank and the Tey folk on the west."),
    dict(name="The Corrin Light", kind="ruin", x=21, y=8, era="now", ring="outer", chapters=(2, 3),
         summary="The broken lighthouse of the fleet on the east point, toward home. The Corrin men guard it."),
    dict(name="Founders' Hill", kind="hill", x=16, y=9.5, era="now", ring="outer", chapters=(2,),
         summary="A green hill above Hythe with the graves of the first colonists and the old church of the Morning Flame."),
    dict(name="The Saltpans", kind="works", x=14, y=13, era="now", ring="outer", chapters=(1, 2),
         summary="Shallow pans on the shore where the colony boils sea water for salt. The path from Wreckers' Bay to Hythe crosses them."),
    dict(name="Gull Rock", kind="rock", x=14, y=1.5, era="now", ring="outer", chapters=(2,),
         summary="A white stack of rock off the north coast, loud with birds. It is a hard climb at low tide."),
    dict(name="The Boneyard", kind="shore", x=4, y=5, era="now", ring="outer", chapters=(2,),
         summary="A beach on the north-west coast, deep in the timbers of old ships. The Corrin men go there for wood and iron."),

    # ---- The inner ring: the interior, the fleet, and the way to the heart ----
    dict(name="The Kettles", kind="springs", x=12, y=5.5, era="now", ring="inner", chapters=(2,),
         summary="Hot pools that smoke in the cold air at the head of the Fleet. The ground there is warm, and on still nights it seems to rise and fall."),
    dict(name="The Ribs", kind="hills", x=8, y=8, area=(5, 6, 11, 10), era="now", ring="inner",
         chapters=(2,),
         summary="Long bare ridges of grey stone that run north to south across the middle of the island."),
    dict(name="The wreck of the Morning Star", kind="wreck", x=8.5, y=7, era="now", ring="inner",
         chapters=(2,),
         summary="The flagship of the old fleet, high on the Ribs, miles from the sea. Nobody knows how it got there."),
    dict(name="The Saint's Hearth", kind="shrine", x=5.5, y=11, era="now", ring="inner", chapters=(2,),
         summary="A black hollow in the turf where the saint lit his fire. The Tey folk keep a cross there."),
    dict(name="The Grandam's Well", kind="cave", x=10, y=10.5, era="now", ring="inner",
         chapters=(2, 3),
         summary="The holy well of the Tey folk. Its shaft goes down and down, to the heart of the Grandam."),
]

# The tracks and the paths of the colony. The other places have no way to
# them. Each road is (from, to, kind, era, via), as in
# content/dawnwatch/places.py. kind is "track" (a cart can use it) or
# "path" (feet only).
ROADS = [
    ("Wreckers' Bay", "The Saltpans", "path", "now", [(12, 13.5)]),
    ("The Saltpans", "Hythe", "track", "now", [(16, 12.5)]),
    ("Hythe", "Founders' Hill", "path", "now", [(17, 10.5)]),
    ("Hythe", "The Corrin Light", "track", "now", [(19, 11), (20.5, 9.5)]),
    ("Hythe", "The Kettles", "track", "now", [(15.5, 10), (14, 8), (12.5, 6.5)]),
    ("The Kettles", "The wreck of the Morning Star", "path", "now", [(10.5, 6), (9.5, 6.5)]),
    ("The Kettles", "The Boneyard", "track", "now", [(9, 4.5), (6, 4)]),
    ("Hythe", "The Saint's Hearth", "path", "now", [(14, 12), (10, 12), (7, 11.5)]),
]

KINDS = ("island", "town", "ruin", "wreck", "shrine", "bay", "hill", "hills", "rock",
         "shore", "works", "springs", "cave", "river")


def place(name):
    """Return the place with this name. Raise KeyError if there is none."""
    for p in PLACES:
        if p["name"] == name:
            return p
    raise KeyError(name)
