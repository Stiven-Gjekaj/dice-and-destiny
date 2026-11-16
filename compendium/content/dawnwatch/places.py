"""The places of The Dawnwatch, Book One.

This list is the single source for the maps, the Places appendix, and the
index. The facts come from the world bible:
docs/superpowers/specs/2026-11-16-dawnwatch-world.md.

Each place is a dict with these keys:

- name: the name, as the book prints it.
- kind: city, town, ruin, shrine, fortress, region, mountains, river, or sea.
- x, y: the position in miles from the north-west corner. x goes east and
  y goes south. For an area, this is the centre of the area.
- summary: one line for the Places appendix.
- chapters: the chapters of Book One that use the place.
- era: "then" (only 300 years ago), "now" (only today), or "both".

Some places have more keys:

- area: (x0, y0, x1, y1) in miles, for a region, mountains, or the sea.
- course: a list of (x, y) points in miles from the source to the mouth, for
  a river.
- then_kind: the kind 300 years ago, when it is not the same as today.
- now_name: the name today of a place that has an old name.
"""

PLACES = [
    # ---- The north ----
    dict(name="Coldharrow", kind="fortress", x=120, y=20, era="now", chapters=(),
         summary="The fortress of Malgrath, behind the Grey Teeth. Its old name is Caer Dunholm."),
    dict(name="Caer Dunholm", kind="fortress", x=120, y=20, era="then", chapters=(),
         now_name="Coldharrow",
         summary="The old name of Coldharrow, the fortress in the north."),
    dict(name="The Grey Teeth", kind="mountains", x=130, y=50, area=(60, 40, 200, 60),
         era="both", chapters=(),
         summary="A wall of mountains across the north. Coldharrow is behind them."),

    # ---- The heart of old Ostrey ----
    dict(name="Ostrey", kind="region", x=128, y=165, area=(20, 60, 240, 320),
         era="then", chapters=(1, 7, 8, 10),
         summary="The old kingdom. It fell in the Grey Winter, 200 years ago."),
    dict(name="Kingsholm", kind="ruin", then_kind="city", x=125, y=120, era="both",
         chapters=(10,),
         summary="The old capital of Ostrey on the River Dunn, now ruins. Garrath slept under it."),
    dict(name="Dawnwatch Keep", kind="fortress", x=165, y=150, era="both", chapters=(1, 7),
         summary="The keep in the Wolds where the Dawnwatch slept for 300 years."),
    dict(name="The Wolds", kind="region", x=168, y=150, area=(145, 135, 190, 165),
         era="both", chapters=(1, 2, 7),
         summary="Low hills with sheep and old stones around Dawnwatch Keep."),
    dict(name="Brannock's Ford", kind="town", x=160, y=172, era="now", chapters=(2,),
         summary="A village at a ford of the River Brann, one day from the keep."),
    dict(name="Wenlow", kind="town", x=148, y=200, era="now", chapters=(9,),
         summary="A small village of the Church on the old road, one day north of Saint Ivo's. The Hush burned its chapel."),
    dict(name="Wendle", kind="town", x=144, y=256, era="now", chapters=(5, 9),
         summary="A village of farms on the border, in Gaunt by a mile, on the good road south."),

    # ---- The Church ----
    dict(name="Saint Ivo's", kind="town", x=150, y=220, era="now", chapters=(3, 9),
         summary="The town of the Church of the Five Sleepers. It grew around the shrine of Saint Ivo."),
    dict(name="The shrine of Saint Ivo", kind="shrine", x=150, y=220, era="then", chapters=(),
         now_name="Saint Ivo's",
         summary="A shrine of Ostrey. The town of Saint Ivo's grew around it."),
    dict(name="The shrine at Kell", kind="shrine", x=110, y=205, era="both", chapters=(4,),
         summary="An old shrine of Ostrey on a hill, three days west of Saint Ivo's."),

    # ---- The south ----
    dict(name="Gaunt", kind="region", x=128, y=290, area=(70, 255, 190, 320),
         era="now", chapters=(5, 9),
         summary="The state of soldiers in the south. The Gauntry family rules it from Stannard."),
    dict(name="The March of Gauntry", kind="region", x=128, y=290, area=(70, 255, 190, 320),
         era="then", chapters=(), now_name="Gaunt",
         summary="The southern border land of Ostrey, held by the Gauntry family."),
    dict(name="Stannard", kind="town", x=130, y=285, era="now", chapters=(5,),
         summary="The seat of the Gauntry family and the heart of Gaunt."),
    dict(name="Ashby Field", kind="region", x=140, y=250, area=(128, 244, 152, 256),
         era="now", chapters=(9,),
         summary="Open land on the border of Gaunt and Saint Ivo's."),

    # ---- The west coast ----
    dict(name="Corrantey", kind="city", x=35, y=200, era="now", chapters=(6,),
         summary="The city of free merchants on the west coast, at the mouths of the Corrin and the Tey."),
    dict(name="Corrin", kind="town", x=33, y=193, era="then", chapters=(), now_name="Corrantey",
         summary="A sea town of Ostrey at the mouth of the Corrin. Today it is part of Corrantey."),
    dict(name="Tey", kind="town", x=35, y=207, era="then", chapters=(), now_name="Corrantey",
         summary="A sea town of Ostrey at the mouth of the Tey. Today it is part of Corrantey."),
    dict(name="The Western Sea", kind="sea", x=8, y=160, area=(0, 0, 20, 320), era="both",
         chapters=(6,),
         summary="The sea on the west coast."),

    # ---- The south-east ----
    dict(name="Fennick", kind="ruin", then_kind="town", x=205, y=245, era="both", chapters=(8,),
         summary="A town of Ostrey. The flood of the Grey Winter drowned it in the Low Fen."),
    dict(name="The Low Fen", kind="region", x=210, y=250, area=(185, 225, 235, 275),
         era="now", chapters=(8,),
         summary="Marsh and black water in the south-east. It was the farmland of Fennick before the flood."),

    # ---- Rivers ----
    dict(name="The River Dunn", kind="river", x=125, y=120, era="both", chapters=(10,),
         course=[(172, 60), (178, 84), (172, 106), (160, 124), (142, 126), (125, 120),
                 (110, 132), (90, 150), (66, 166), (42, 178), (21, 183)],
         summary="It comes down from the Grey Teeth, passes Kingsholm, and reaches the sea north of Corrantey."),
    dict(name="The River Brann", kind="river", x=160, y=172, era="both", chapters=(2,),
         course=[(188, 138), (180, 150), (168, 162), (160, 172), (164, 190), (178, 208),
                 (192, 226), (203, 240)],
         summary="It comes from the Wolds, passes Brannock's Ford, and goes south into the Low Fen."),
    dict(name="The Corrin", kind="river", x=55, y=188, era="both", chapters=(6,),
         course=[(76, 180), (64, 184), (52, 189), (42, 192), (33, 194)],
         summary="A short river. It reaches the sea at Corrantey."),
    dict(name="The Tey", kind="river", x=58, y=214, era="both", chapters=(6,),
         course=[(82, 224), (68, 218), (55, 212), (44, 208), (35, 206)],
         summary="A short river. It reaches the sea at Corrantey."),
]

# The roads of the Travel table in the world bible, and the old roads of
# Ostrey to Kingsholm. The off-road journeys have no line. Each road is
# (from, to, kind, era, via), where via is a list of (x, y) points in miles
# between the two places. A road uses the position of each end, also when
# the place at that end has another era.
ROADS = [
    ("Dawnwatch Keep", "Brannock's Ford", "track", "now", [(160, 161)]),
    ("Brannock's Ford", "Saint Ivo's", "old road", "both", [(156, 196)]),
    ("Saint Ivo's", "Stannard", "road", "now", [(138, 252)]),
    ("Saint Ivo's", "Corrantey", "road", "now", [(110, 222), (72, 202), (50, 200)]),
    ("Kingsholm", "Brannock's Ford", "old road", "then", [(140, 140), (152, 158)]),
    ("Kingsholm", "Corrin", "old road", "then", [(105, 142), (80, 162), (55, 182), (40, 190)]),
    ("Kingsholm", "The shrine at Kell", "old road", "then", [(118, 165)]),
]

KINDS = ("city", "town", "ruin", "shrine", "fortress", "region", "mountains", "river", "sea")


def place(name):
    """Return the place with this name. Raise KeyError if there is none."""
    for p in PLACES:
        if p["name"] == name:
            return p
    raise KeyError(name)
