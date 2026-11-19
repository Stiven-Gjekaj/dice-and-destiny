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

RIVER_LIMIT = 12  # the generated rivers with the most water that the maps keep
RELIEF_DENSITY = 0.35  # the part of the relief symbols that the print maps keep

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


def _land_polygon(coast, width, y0, y1, height, amp=4):
    """The land east of the coast line, from y0 to y1. An edge inside the frame is wavy."""
    pts = [[x, y] for x, y in coast if y0 < y < y1]
    first, last = _coast_x(coast, y0), _coast_x(coast, y1)
    top = [[first, y0], [width, y0]] if y0 <= 0 else _wavy_y(f"land-{y0}", first, width, y0, amp)
    bottom = [[width, y1], [last, y1]] if y1 >= height else _wavy_y(f"land-{y1}", width, last, y1, amp)
    return top + bottom + pts[::-1]


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


def _wavy_y(key, x0, x1, y, amp, step=4):
    """Points from x0 to x1 near the line y, with a wave of up to amp.

    The wave is 0 at the two ends, so the line still meets the coast and the frame.
    """
    noise = _noise(_rng(key))
    n = max(2, int(abs(x1 - x0) / step))
    return [[round(x0 + (x1 - x0) * i / n, 2),
             round(y + amp * math.sin(math.pi * i / n) * noise(math.pi * i / n), 2)]
            for i in range(n + 1)]


def _coast_x(coast, y):
    """The x of the coast line at y, by straight lines between its points."""
    for (xa, ya), (xb, yb) in zip(coast, coast[1:]):
        if ya <= y <= yb:
            return xa + (xb - xa) * (y - ya) / (yb - ya) if yb != ya else xa
    raise ValueError(f"the coast line does not reach y = {y}")


def build(places):
    width, height = places["land_miles"]
    # Each place is in the overlay of its era. inkland joins the places of the base
    # world with roads of its own, and the book has no such roads.
    overlays = {"then": {"add": {"places": [], "roads": [], "features": []}, "labels": {}},
                "today": {"add": {"places": [], "roads": [], "features": []}, "labels": {}}}
    for p in places["places"]:
        for era in _era_of(p):
            overlays[era]["add"]["places"].append(_point_pin(p, era))

    # The land is low east of the coast. The Wolds lie on it with a higher
    # priority, so that they set the height where they overlap. The lowland
    # stops at the Grey Teeth (y 40 to 60, with a soft edge), so that the
    # rivers can come down from the mountains.
    regions = [{"id": "lowland-north", "kind": "plains", "height": [24, 40],
                "polygon": _land_polygon(places["coast"], width, 0, 32, height)},
               {"id": "lowland", "kind": "plains", "height": [21, 42],
                "polygon": _land_polygon(places["coast"], width, 70, height, height)}]
    for a in places["areas"]:
        rid = ident(a["name"])
        if a["kind"] == "sea":
            regions.append({"id": rid, "kind": "sea", "name": a["name"],
                            "polygon": _sea_polygon(places["coast"], height)})
        elif a["kind"] == "mountains":
            regions.append({"id": rid, "kind": "mountains", "name": a["name"], "edge": 8,
                            "polygon": organic_outline(rid, a["box"], (width, height))})
        elif a["name"] == "The Wolds":
            regions.append({"id": rid, "kind": "hills", "name": a["name"],
                            "polygon": organic_outline(rid, a["box"], (width, height)),
                            "height": [38, 50], "edge": 6, "priority": 1})
        elif a["name"] == "The Low Fen":
            # The fen is terrain, so it is in both eras. Before the flood it was farmland,
            # so the old map hides its name.
            regions.append({"id": rid, "kind": "marsh", "name": a["name"],
                            "polygon": organic_outline(rid, a["box"], (width, height))})
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
        rivers.append({"id": river_id(r["name"]), "name": r["name"], "source": pts[0],
                       "through": pts[1:-1], "mouth": mouth})

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
        variants.append({"name": mid, "overlay": mid,
                         "crop": crop, "page": {"w_mm": w_mm, "h_mm": h_mm},
                         "extras": {"cartouche": {"title": m["title"]}}})

    return {
        "version": 1,
        "seed": SEED,
        "units": {"name": "mile"},
        "frame": {"origin": "top-left", "x_axis": "east", "y_axis": "south", "width": width, "height": height},
        # Only the pins are places, and only the pinned seas are water.
        "world": {"cells": 20000, "template": "pangea", "states": 0, "towns": 0,
                  "fill_land": True, "river_limit": RIVER_LIMIT, "jitter": 0.9,
                  "climate": {"latitude_range": [48, 54]}},
        "pins": {"points": [], "regions": regions,
                 "rivers": rivers, "roads": []},
        "overlays": map_overlays,
        "variants": variants,
        "render": {"mode": "print-safe",
                   "fonts": {"title": "IM Fell English", "labels": "IM Fell English",
                             "labels_sc": "IM Fell English SC", "other": "Caladea"},
                   "min_line_width_pt": 0.5,
                   # The map shows no name that the config does not give, and the report checks it.
                   "labels": {"generated": False, "check_generated": True},
                   # No trees: they fill the land. No marsh: the Low Fen was farmland
                   # before the flood, and the relief is the same on each map.
                   "relief": {"density": RELIEF_DENSITY, "hide": ["tree", "marsh"]},
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
