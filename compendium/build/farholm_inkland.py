"""Make the inkland config of the map of Farholm from content/western_sea/places.py.

inkland (github.com/Stiven-Gjekaj/inkland) draws the final map. This module
turns the places, the areas, the river, and the roads of places.py into its
config, as build/inkland_config.py does for the Dawnwatch maps:

    python3 build/farholm_inkland.py     writes compendium/maps/western-sea/farholm.inkland.json
    inkland generate --config maps/western-sea/farholm.inkland.json --out-dir <dir>

Then copy <dir>/farholm.svg to compendium/maps/western-sea/farholm.svg.
"""
import json
import math
import os
import sys

from inkland_config import _noise, _rng, ident, organic_outline, river_id

HERE = os.path.dirname(os.path.abspath(__file__))
MAP_DIR = os.path.join(HERE, "..", "maps", "western-sea")
CONFIG_JSON = os.path.join(MAP_DIR, "farholm.inkland.json")

SEED = 60  # the fleet sailed west in the year -60
MAP_ID = "farholm"
PAGE_MM = (167, 120)  # the "half" size of maps.SIZES

# The coast of the island, clockwise from the tip of the tail in the west, in
# miles. The island is the long back of the Grandam: a hump from west to east,
# with coves in the north and in the south. The coast passes the
# places on the shore: the Boneyard, the Corrin Light on the east point, Hythe
# at the mouth of the Fleet, the Saltpans, and Wreckers' Bay. inkland moves this
# line with its roughness and its bends, but not near a place.
COAST = [
    (1.0, 8.7), (1.8, 8.2), (2.6, 7.6), (3.0, 6.6), (3.1, 5.8), (3.5, 5.1), (4.0, 4.6),
    (4.9, 4.1), (5.8, 3.5), (6.9, 3.4), (7.8, 2.9), (8.9, 3.0), (9.8, 2.6), (10.8, 2.7),
    (11.2, 3.4), (11.8, 3.6), (12.3, 2.9), (12.9, 2.6), (13.7, 2.4), (14.6, 2.7), (15.6, 2.6),
    (16.4, 3.2), (17.3, 3.3), (18.1, 4.0), (19.0, 4.3), (19.6, 5.0), (20.0, 5.9), (20.6, 5.9),
    (20.9, 6.5), (21.7, 7.1), (22.2, 7.9), (21.9, 8.6), (21.6, 9.3), (21.5, 10.1), (20.8, 10.7),
    (20.3, 11.6), (19.4, 11.9), (18.5, 12.1), (17.8, 12.4), (17.0, 12.6), (16.2, 13.1),
    (15.3, 13.2), (14.5, 13.6), (13.6, 13.7), (12.6, 14.3), (11.6, 13.8), (10.9, 12.9),
    (10.1, 12.9), (9.3, 13.6), (8.7, 14.4), (7.9, 14.0), (7.0, 13.6), (6.5, 13.4), (6.1, 12.8),
    (5.5, 12.9), (5.0, 12.5), (4.4, 12.4), (3.9, 11.8), (3.3, 11.2), (2.9, 10.3), (2.5, 9.6),
    (1.8, 9.1),
]
COAST_ROUGHNESS = 0.2  # miles; the bays and the capes of the coast
COAST_WANDER = 0.25  # miles of long, slow bends in the coast line
ISLAND_HEIGHT = [22, 40]  # low land, with the Ribs above it

# The kinds of places.py that are a region of the map, and their inkland kind.
REGION_KIND = {"hills": "hills"}
HILLS_HEIGHT = [32, 42]  # the land between the ridges
# The kinds of places.py that are an inkland place kind. The other kinds are custom.
PLACE_KIND = {"town": "town", "ruin": "ruin"}
# A road of places.py, as an inkland road. A track is for a cart, a path is for feet.
ROAD_KIND = {"track": "road", "path": "trail"}

# The character of the land that places.py does not give. The back of the
# island is rolling land, with a loose edge.
CHARACTER_AREAS = [
    {"id": "back", "character": "rolling", "box": [3, 4, 21, 12], "strength": 0.6},
]
# The woods have no name. A wood grows in the shelter of the valley of the
# Fleet, one on the north slope, and one around the Saint's Hearth. Each is
# (id, box) in miles. The outline of a wood is organic, not a box.
WOODS = [
    ("fleet-wood", (13.2, 8.6, 15.2, 10.8)),
    ("north-wood", (16.0, 4.6, 19.4, 7.4)),
    ("west-wood", (3.4, 8.6, 6.0, 10.4)),
]
# The Ribs are ridges that run north to south across the back of the island,
# as the ribs of an animal run from its spine. The named region of the Ribs
# holds RIB_COUNT narrow ridges. All of them bend a little to the east, as ribs do.
RIB_COUNT = 4
RIB_HEIGHT = [66, 80]
RIB_HALF_WIDTH = 0.4  # miles
RIB_BEND = 0.35  # miles
# The unnamed terrain under a named place: the hill of Founders' Hill and the
# stack of Gull Rock off the north coast. The hill is a little north-east of
# the place, so that the Fleet can flow past it.
EXTRA_REGIONS = [
    {"id": "founders-rise", "kind": "hills", "height": [42, 48], "edge": 0.6, "priority": 2,
     "circle": {"at": [16.4, 9.1], "r": 0.45}},
    {"id": "gull-stack", "kind": "land", "height": [30, 40], "priority": 3, "roughness": 0,
     "circle": {"at": [14, 1.5], "r": 0.22}},
]
RELIEF = {"density": 1.0, "hide": ["field", "marsh", "dune"],
          "only_in": {"tree": [w for w, _ in WOODS]}}


def _inside(xy, polygon):
    """True if the point is inside the polygon (the even-odd rule)."""
    x, y = xy
    inside = False
    for (x0, y0), (x1, y1) in zip(polygon, polygon[1:] + polygon[:1]):
        if (y0 > y) != (y1 > y) and x < x0 + (y - y0) * (x1 - x0) / (y1 - y0):
            inside = not inside
    return inside


def _on_land(xy):
    """True if the point is on the island or on a stack of rock off its coast."""
    stacks = [r["circle"] for r in EXTRA_REGIONS if r["kind"] == "land"]
    return _inside(xy, COAST) or any(
        (xy[0] - c["at"][0]) ** 2 + (xy[1] - c["at"][1]) ** 2 <= c["r"] ** 2 for c in stacks)


def _feature(p):
    """A place in the sea, as a named feature. inkland puts no place in a sea."""
    return {"id": ident(p["name"]), "kind": "custom", "name": p["name"], "at": [p["x"], p["y"]]}


def _shore(p):
    """A point on the shore near a place in the sea.

    The point is on the line from the place to the middle of the island, a
    short distance inside the coast.
    """
    cx = sum(x for x, _ in COAST) / len(COAST)
    cy = sum(y for _, y in COAST) / len(COAST)
    x, y = p["x"], p["y"]
    dx, dy = cx - x, cy - y
    step = 0.1 / (dx * dx + dy * dy) ** 0.5
    t = 0.0
    while not _inside((x + t * dx, y + t * dy), COAST):
        t += step
    t += 2 * step
    return round(x + t * dx, 2), round(y + t * dy, 2)


def _rib(key, x, y0, y1, bend):
    """The outline of one narrow ridge from y0 to y1 near x.

    The ridge bends to the side by up to bend miles in the middle. It tapers
    at the two ends, and its edges are not straight.
    """
    noise = _noise(_rng(key))
    left, right = [], []
    n = 24
    for i in range(n + 1):
        t = i / n
        y = y0 + t * (y1 - y0)
        cx = x + bend * math.sin(math.pi * t) + 0.15 * noise(2 * math.pi * t)
        w = RIB_HALF_WIDTH * math.sin(math.pi * (0.08 + 0.84 * t)) * (1 + 0.3 * noise(4 + 7 * t))
        left.append([round(cx - w, 2), round(y, 2)])
        right.append([round(cx + w, 2), round(y, 2)])
    return left + right[::-1]


def _ribs(rid, area):
    """The ridges of the Ribs in the area (x0, y0, x1, y1)."""
    x0, y0, x1, y1 = area
    rng = _rng(rid + ":ribs")
    out = []
    for k in range(RIB_COUNT):
        x = x0 + (k + 0.5) * (x1 - x0) / RIB_COUNT
        top = y0 + rng.uniform(-0.3, 0.6)
        bottom = y1 + rng.uniform(-0.6, 0.3)
        out.append({"id": f"{rid}-ridge-{k + 1}", "kind": "mountains", "height": RIB_HEIGHT,
                    "priority": 3, "edge": 0.4, "peaks": True, "roughness": 0,
                    "polygon": _rib(f"{rid}:{k}", x, top, bottom, RIB_BEND + rng.uniform(-0.1, 0.1))})
    return out


def _overlay_place(p):
    place = {"id": ident(p["name"]), "at": [p["x"], p["y"]], "name": p["name"]}
    if p["kind"] in PLACE_KIND:
        place["kind"] = PLACE_KIND[p["kind"]]
    else:
        place["kind"], place["custom_kind"] = "custom", p["kind"]
    return place


def config(places=None, roads=None):
    """The inkland config of the map of Farholm from a list of places and roads."""
    if places is None or roads is None:
        from content.western_sea import places as source
        places = source.PLACES if places is None else places
        roads = source.ROADS if roads is None else roads
        width, height = source.W, source.H
    else:
        width, height = 24, 16
    island = next((p for p in places if p["kind"] == "island"), None)

    # Only the overlay has places. inkland joins the places of the base world
    # with roads of its own, and the book has no such roads.
    overlay = {"add": {"places": [], "roads": [], "features": []}, "labels": {}}
    regions = [
        # The sea fills the frame. The island is land with a higher priority.
        {"id": "western-sea", "kind": "sea", "box": [0, 0, width, height], "shelf": 0.8,
         # The sea is the ocean, but a cove of the rough coast can close.
         "landlocked": True},
        {"id": "farholm", "kind": "land", "polygon": [list(p) for p in COAST],
         "height": ISLAND_HEIGHT, "priority": 1, "roughness": COAST_ROUGHNESS,
         "wander": COAST_WANDER, "coast_detail": 5, "islets": 0, "peaks": False},
    ]
    extras = {}
    if island:
        # The name of the island is the title of the map, not a label across the Ribs.
        regions[1]["name"] = island["name"]
        overlay["labels"]["region:farholm"] = {"hide": True}
        extras["cartouche"] = {"title": island["name"]}
    rivers = []
    road_ends = {name for r in roads for name in r[:2]}
    for p in places:
        if p["kind"] == "island":
            continue
        if "course" in p:
            pts = [list(xy) for xy in p["course"]]
            rivers.append({"id": river_id(p["name"]), "name": p["name"], "source": pts[0],
                           "through": pts[1:-1], "mouth": {"region": "western-sea"}, "main": True})
        elif "area" in p and p["kind"] in REGION_KIND:
            rid = ident(p["name"])
            regions.append({"id": rid, "kind": REGION_KIND[p["kind"]], "name": p["name"],
                            "height": HILLS_HEIGHT, "priority": 2, "edge": 1.0, "peaks": False,
                            "roughness": 0,
                            "polygon": organic_outline(rid, p["area"], (width, height), wobble=0.3)})
            regions += _ribs(rid, p["area"])
        elif _on_land((p["x"], p["y"])):
            overlay["add"]["places"].append(_overlay_place(p))
        elif p["name"] in road_ends:
            # A road ends at a place, and inkland puts no place in a sea. A
            # bay with a road has its place on its shore, where the road ends.
            x, y = _shore(p)
            overlay["add"]["places"].append(_overlay_place(dict(p, x=x, y=y)))
        else:
            overlay["add"]["features"].append(_feature(p))
    regions += EXTRA_REGIONS
    for wid, box in WOODS:
        regions.append({"id": wid, "kind": "forest", "height": [24, 36], "priority": 2,
                        "roughness": 0, "polygon": organic_outline(wid, box, (width, height), wobble=0.35)})

    for start, end, kind, _era, via in roads:
        overlay["add"]["roads"].append({
            "id": ident(start + " to " + end), "from": ident(start), "to": ident(end),
            "via": [list(xy) for xy in via], "kind": ROAD_KIND[kind]})

    return {
        "version": 1,
        "seed": SEED,
        "units": {"name": "mile"},
        "frame": {"origin": "top-left", "x_axis": "east", "y_axis": "south",
                  "width": width, "height": height},
        # Only the overlay places are places, only the pinned sea is water, and
        # only the pinned roads are roads.
        "world": {"cells": 20000, "template": "low-island", "states": 0, "towns": 0,
                  "generated_roads": False, "river_limit": 0, "jitter": 0.9,
                  "deep_sea": True, "edges": {"north": "sea", "east": "sea", "south": "sea",
                                              "west": "sea"},
                  "climate": {"latitude_range": [56, 58], "preset": "temperate"}},
        "pins": {"points": [], "regions": regions, "areas": CHARACTER_AREAS,
                 "rivers": rivers, "roads": []},
        "overlays": {MAP_ID: overlay},
        "variants": [{"name": MAP_ID, "overlay": MAP_ID, "crop": [0, 0, width, height],
                      "page": {"w_mm": PAGE_MM[0], "h_mm": PAGE_MM[1]}, "extras": extras}],
        "render": {"mode": "print-safe",
                   "fonts": {"title": "IM Fell English", "labels": "IM Fell English",
                             "labels_sc": "IM Fell English SC", "other": "Caladea"},
                   "min_line_width_pt": 0.5,
                   # The map shows no name that places.py does not give, and the report checks it.
                   "labels": {"generated": False, "check_generated": True},
                   "relief": RELIEF,
                   "hand_drawn": True,
                   "river_contrast": 0.8,
                   "extras": {"scale_bar": True, "compass": True},
                   "layers": ["ocean", "coast", "relief", "rivers", "regions", "roads",
                              "features", "places", "labels"]},
    }


def write(path=CONFIG_JSON):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config(), f, indent=2, ensure_ascii=False)
        f.write("\n")
    return path


if __name__ == "__main__":
    print(write(sys.argv[1] if len(sys.argv) > 1 else CONFIG_JSON))
