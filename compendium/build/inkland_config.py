"""Make the inkland config of the Dawnwatch maps from compendium/maps/places.json.

inkland (github.com/Stiven-Gjekaj/inkland) draws the final maps. This module
turns the places, areas, rivers, and roads of places.json into its config:

    python3 build/inkland_config.py           writes compendium/maps/dawnwatch.inkland.json
    inkland generate --config maps/dawnwatch.inkland.json --out-dir <dir>

Then copy <dir>/<id>.svg to compendium/maps/<id>.svg for each map id.
"""
import json
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAP_DIR = os.path.join(HERE, "..", "maps")
PLACES_JSON = os.path.join(MAP_DIR, "places.json")
CONFIG_JSON = os.path.join(MAP_DIR, "dawnwatch.inkland.json")

SEED = 300  # the year of the waking

# The kinds of places.json, as inkland place kinds.
# The areas that are terrain regions. The other areas that are not seas are features.
REGION_AREAS = ("The Wolds", "The Low Fen")

PLACE_KIND = {"city": "city", "town": "town", "village": "village", "ruin": "ruin", "fortress": "fortress"}

# Target lengths of the roads of today, in miles, from the travel section of the world bible.
ROAD_TARGETS = {
    ("Dawnwatch Keep", "Brannock's Ford"): 22,
    ("Brannock's Ford", "Saint Ivo's"): 72,
    ("Saint Ivo's", "Stannard"): 72,
    ("Saint Ivo's", "Corrantey"): 120,
}
ROAD_TOLERANCE = 0.1

RIVER_LIMIT = 8
MAIN_RIVERS = ("The River Dunn",)  # drawn at least as wide as the largest other river
COAST_ROUGHNESS = 14  # miles; inkland keeps the coast towns on the coast
COAST_WANDER = 12  # miles of long, slow bends in the coast line
HILL_LOW = 42  # the lowest height with a hill symbol on a print map (inkland docs/TERRAIN.md)
LOWLAND_TOP = 76  # miles: the lowland starts south of the soft edge of the Grey Teeth

# The character of the land outside the named regions. An area steers the heights,
# the biomes, and the relief symbols, and its edge is loose. The world bible gives
# the foothills, the rolling land around the Wolds, the forest around Kingsholm,
# and the farmland of Gaunt. The other woods are free.
CHARACTER_AREAS = [
    {"id": "foothills", "character": "rough", "box": [50, 28, 210, 78], "strength": 0.7},
    {"id": "wolds-country", "character": "rolling", "box": [125, 115, 215, 185]},
    {"id": "dunn-wood", "character": "wooded", "circle": {"at": [70, 140], "r": 26}, "strength": 0.8},
    {"id": "gaunt-farmland", "character": "flat", "box": [40, 235, 185, 320], "strength": 0.7},
]  # the generated rivers with the most water that the maps keep
# The print maps keep this part of the relief symbols. The marsh symbols stand only
# in the Low Fen, not on the wet strips of the coast. The fields stand only in the
# lowland, not in the mountains around Coldharrow.
RELIEF = {"density": 0.6, "only_in": {"marsh": ["low-fen"], "field": ["lowland"]}}
# The regions that did not exist 300 years ago. The old map shows no symbols in them.
THEN_HIDE_RELIEF = ["low-fen", "kingsholm-wood"]

# A road that passes a place of the map passes it by id. The bible puts Wenlow on the old road.
ROAD_VIA_PLACES = {("Brannock's Ford", "Saint Ivo's"): ["Wenlow"]}


def ident(name):
    """An inkland id: lower-case letters and digits, words joined by '-'."""
    s = re.sub(r"[^a-z0-9]+", "-", name.lower().replace("'", "")).strip("-")
    return re.sub(r"^the-", "", s)


def river_id(name):
    """The id of a river. It cannot be the id of a place, so it starts with 'river-'."""
    return "river-" + re.sub(r"^river-", "", ident(name))


def _inside(xy, crop):
    x0, y0, x1, y1 = crop
    return x0 <= xy[0] <= x1 and y0 <= xy[1] <= y1


def _hidden_labels(places, mid, era, crop):
    """The labels that a map of the era does not show: the areas that it does not
    list, and the rivers with less than half of their course in its view."""
    keys = []
    for a in places["areas"]:
        if a["kind"] == "sea" or mid in a["maps"]:
            continue
        if a["kind"] == "mountains" or a["name"] in REGION_AREAS:
            keys.append("region:" + ident(a["name"]))
        elif era in _era_of(a):
            keys.append("feature:" + ident(a["name"]))
    for r in places["rivers"]:
        if 2 * sum(_inside(p, crop) for p in r["points"]) < len(r["points"]):
            keys.append("river:" + river_id(r["name"]))
    return keys


def _point_pin(p, era):
    kind = p.get("then_kind", p["kind"]) if era == "then" else p["kind"]
    pin = {"id": ident(p["name"]), "at": [p["x"], p["y"]], "name": p["name"]}
    if kind in PLACE_KIND:
        pin["kind"] = PLACE_KIND[kind]
    else:
        pin["kind"], pin["custom_kind"] = "custom", kind
    return pin


def _add_crossing(overlay, name, xy):
    """An unnamed point that a road of the old map ends at."""
    pid = ident(name)
    overlay["add"]["places"].append({"id": pid, "kind": "custom", "custom_kind": "crossing",
                                     "at": list(xy)})
    overlay["labels"]["place:" + pid] = {"hide": True}


def _era_of(item):
    return {"then": ("then",), "now": ("today",), "both": ("then", "today")}[item["era"]]


def _sea_polygon(coast, height):
    """The sea west of the coast line, clipped to the frame."""
    pts = [[x, y] for x, y in coast if 0 <= y <= height]
    return [[0, 0], [pts[0][0], 0]] + pts + [[pts[-1][0], height], [0, height]]




def _noise(rng, terms=7):
    """A smooth periodic noise of t in [0, 2 pi): a sum of sines with random phases."""
    waves = [(k, rng.uniform(0, 2 * math.pi), rng.uniform(0.3, 1) / k ** 0.8) for k in range(2, 2 + terms)]
    scale = sum(a for _, _, a in waves)
    return lambda t: sum(a * math.sin(k * t + ph) for k, ph, a in waves) / scale


def _rng(key):
    """A random source for one shape. The same seed and key give the same shape."""
    return random.Random(f"{SEED}:{key}")


def organic_outline(key, box, frame, wobble=0.22, points=96):
    """An irregular outline that fills the box: a rounded box with a wavy edge.

    A shape on a map that is a box looks drawn by a machine. The outline keeps
    the size and the place of the box. It goes out of the box and into it by up
    to wobble of its half size, and it stops at the frame.
    """
    x0, y0, x1, y1 = box
    cx, cy, ax, ay = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2
    width, height = frame
    noise = _noise(_rng(key))
    out = []
    for i in range(points):
        t = 2 * math.pi * i / points
        c, s = math.cos(t), math.sin(t)
        # A superellipse (exponent 4): nearly the box, with round corners.
        r = 1 + wobble * noise(t)
        x = cx + ax * r * math.copysign(abs(c) ** 0.5, c)
        y = cy + ay * r * math.copysign(abs(s) ** 0.5, s)
        out.append([round(min(max(x, 0), width), 2), round(min(max(y, 0), height), 2)])
    return [p for i, p in enumerate(out) if p != out[i - 1]]






def build(places):
    width, height = places["land_miles"]
    # Each place is in the overlay of its era. inkland joins the places of the base
    # world with roads of its own, and the book has no such roads.
    overlays = {"then": {"add": {"places": [], "roads": [], "features": []}, "labels": {}},
                "today": {"add": {"places": [], "roads": [], "features": []}, "labels": {}}}
    for p in places["places"]:
        for era in _era_of(p):
            overlays[era]["add"]["places"].append(_point_pin(p, era))

    # The regions fix what the book names: the sea, the mountains, the hills, and
    # the fen. inkland gives their outlines a natural roughness.
    # The land south of the mountains is low. The named regions and the character
    # areas rule over this lowland, because it has the lowest priority. It has no
    # peaks: the only mountains of the land are the Grey Teeth.
    regions = [{"id": "lowland", "kind": "plains", "height": [21, 38], "priority": -1, "peaks": False,
                "edge": 12, "roughness": 0, "box": [0, LOWLAND_TOP, width, height]},
               # The world bible puts the shrine at Kell on a hill. The hill has no name.
               {"id": "kell-hill", "kind": "hills", "height": [HILL_LOW, HILL_LOW + 6], "edge": 4,
                "circle": {"at": [110, 205], "r": 6}},
               # The forest grew around Kingsholm after it burned. It is a region, so
               # that the map of the old age can leave out its trees.
               # An old wood east of the Brann. It is a forest region, because a
               # wooded area does not turn grassland into forest.
               {"id": "east-wood", "kind": "forest", "height": [24, 34],
                "circle": {"at": [215, 183], "r": 24}, "roughness": 6},
               {"id": "kingsholm-wood", "kind": "forest", "height": [24, 34],
                "circle": {"at": [120, 112], "r": 20},
                "roughness": 6}]
    for a in places["areas"]:
        rid = ident(a["name"])
        if a["kind"] == "sea":
            regions.append({"id": rid, "kind": "sea", "name": a["name"], "roughness": COAST_ROUGHNESS, "wander": COAST_WANDER,
                            "coast_detail": 8, "polygon": _sea_polygon(places["coast"], height)})
        elif a["kind"] == "mountains":
            regions.append({"id": rid, "kind": "mountains", "name": a["name"], "box": a["box"],
                            "edge": 10, "roughness": 8})
        elif a["name"] == "The Wolds":
            regions.append({"id": rid, "kind": "hills", "name": a["name"], "box": a["box"], "height": [HILL_LOW, HILL_LOW + 10],
                            "edge": 10, "roughness": 6})
        elif a["name"] == "The Low Fen":
            # The fen is terrain, so it is in both eras. Before the flood it was farmland,
            # so the old map hides its name.
            regions.append({"id": rid, "kind": "marsh", "name": a["name"], "box": a["box"],
                            "roughness": 6})
            overlays["then"]["labels"]["region:" + rid] = {"hide": True}
        else:
            # A political area or a field: a named feature of its era only.
            feature = {"id": rid, "name": a["name"]}
            if a["name"] == "Ashby Field":
                feature.update(kind="battle-site", at=[a["x"], a["y"]])
            else:
                feature.update(kind="border", polygon=organic_outline(rid, a["box"], (width, height)))
            for era in _era_of(a):
                overlays[era]["add"]["features"].append(dict(feature))

    rivers = []
    for r in places["rivers"]:
        pts = r["points"]
        mouth = {"region": "low-fen"} if r["name"] == "The River Brann" else {"region": "western-sea"}
        river = {"id": river_id(r["name"]), "name": r["name"], "source": pts[0],
                 "through": pts[1:-1], "mouth": mouth}
        if r["name"] in MAIN_RIVERS:
            river["main"] = True
        rivers.append(river)

    # On the old map, a road ends at the old name of a place. The ford was a crossing
    # with no village, so the old map gets an unnamed point there.
    then_name = {p["now_name"]: p["name"] for p in places["places"] if p.get("now_name")}
    then_ids = {ident(p["name"]) for p in places["places"] if p["era"] in ("then", "both")}
    for w in places["roads"]:
        key = (w["start"], w["end"])
        points = [list(p) for p in w["points"][1:-1]]
        for era in _era_of(w):
            start, end = w["start"], w["end"]
            if era == "then":
                start, end = then_name.get(start, start), then_name.get(end, end)
                for name, xy in ((start, w["points"][0]), (end, w["points"][-1])):
                    if ident(name) not in then_ids:
                        _add_crossing(overlays["then"], name, xy)
                        then_ids.add(ident(name))
                via = points
            else:
                via = [ident(v) for v in ROAD_VIA_PLACES.get(key, [])] or points
            road = {"id": ident(start + " to " + end), "from": ident(start), "to": ident(end),
                    "via": via, "kind": "trail" if w["kind"] == "track" else "road"}
            if era == "today" and key in ROAD_TARGETS:
                road.update(target_length=ROAD_TARGETS[key], tolerance=ROAD_TOLERANCE)
            overlays[era]["add"]["roads"].append(road)

    variants, map_overlays = [], {}
    for mid, m in places["maps"].items():
        x0, y0, x1, y1 = m["bounds_miles"]
        crop = [max(0, x0), max(0, y0), min(width, x1), min(height, y1)]
        w_mm, h_mm = m["size_mm"]
        # Each map has its own overlay: the overlay of its era, and the labels that it hides.
        era = "then" if m["era"] == "then" else "today"
        overlay = json.loads(json.dumps(overlays[era]))
        for key in _hidden_labels(places, mid, era, crop):
            overlay["labels"].setdefault(key, {})["hide"] = True
        map_overlays[mid] = overlay
        variant = {"name": mid, "overlay": mid,
                   "crop": crop, "page": {"w_mm": w_mm, "h_mm": h_mm},
                   "extras": {"cartouche": {"title": m["title"]}}}
        if era == "then":
            # The fen and the wood came after the Grey Winter. The variant keeps the
            # other relief options of the render.
            variant["relief"] = {"hide_in": THEN_HIDE_RELIEF}
        variants.append(variant)

    return {
        "version": 1,
        "seed": SEED,
        "units": {"name": "mile"},
        "frame": {"origin": "top-left", "x_axis": "east", "y_axis": "south", "width": width, "height": height},
        # Only the pins are places, and only the pinned seas are water.
        "world": {"cells": 20000, "template": "pangea", "states": 0, "towns": 0,
                  "fill_land": True, "river_limit": RIVER_LIMIT, "jitter": 0.9,
                  "climate": {"latitude_range": [48, 54], "preset": "temperate"}},
        "pins": {"points": [], "regions": regions,
                 "areas": CHARACTER_AREAS,
                 "rivers": rivers, "roads": []},
        "overlays": map_overlays,
        "variants": variants,
        "render": {"mode": "print-safe",
                   "fonts": {"title": "IM Fell English", "labels": "IM Fell English",
                             "labels_sc": "IM Fell English SC", "other": "Caladea"},
                   "min_line_width_pt": 0.5,
                   # The map shows no name that the config does not give, and the report checks it.
                   "labels": {"generated": False, "check_generated": True},
                   "relief": RELIEF,
                   "hand_drawn": True,
                   "river_contrast": 0.8,
                   "extras": {"scale_bar": True, "compass": True},
                   "layers": ["ocean", "coast", "relief", "rivers", "regions", "roads",
                              "features", "places", "labels"]},
    }


def write(path=CONFIG_JSON):
    with open(PLACES_JSON) as f:
        cfg = build(json.load(f))
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return path


if __name__ == "__main__":
    print(write(sys.argv[1] if len(sys.argv) > 1 else CONFIG_JSON))
