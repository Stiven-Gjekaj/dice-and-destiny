"""The maps of The Dawnwatch, drawn as SVG in code.

The style is a line-drawn atlas in black ink on white paper. Hatching shows
the sea, small peaks show the mountains, and the labels use the book fonts.
The maps have no grey fill and no transparency, because Lulu prints the
interior in black and white. The labels are plain text with no outline,
because Chrome prints outlined text as a Type 3 font.

The places come from content/dawnwatch/places.py. A map changes when a
place in that list changes.

To look at the maps, write them to a folder:

    python3 build/maps.py /tmp/maps

The command writes one SVG for each map and an HTML page with all of them.
Open the HTML page in Chrome, or add --png to write a PNG of each map.
"""
import math
import os
import random
import re
import subprocess
import sys
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from content.dawnwatch.places import PLACES, ROADS, place  # noqa: E402

INK, PAPER = "#000", "#fff"
SERIF, SANS = "Caladea, serif", "Inter, sans-serif"

# The size of a map in mm. The final maps from the map tool have the same
# sizes, so a final map can replace a preview with no change to the layout.
SIZES = {"page": (167.0, 250.0), "half": (167.0, 120.0)}
MARGIN = 3.0  # mm from the edge of the SVG to the inner frame

# The coast of the Western Sea, from north to south, in miles.
COAST = [(14, -60), (15, -30), (14, -5), (16, 20), (13, 45), (17, 70), (15, 95), (19, 120), (17, 145), (20, 163),
         (22, 180), (25, 188), (30, 192), (32, 198), (33, 203), (31, 209), (26, 214), (21, 224),
         (19, 245), (16, 270), (18, 295), (15, 325), (17, 350), (15, 380)]

MAPS = {
    "ostrey-then": dict(
        era="then", size="page", bounds=(0, 0, 240, 320), scale_miles=50, ticks=20,
        title="Ostrey", sub="The kingdom, three hundred years ago",
        title_at="ne", tools_at="se", capital="Kingsholm",
        label_at={"Ostrey": (100, 92)}),
    "land-today": dict(
        era="now", size="page", bounds=(0, 0, 240, 320), scale_miles=50, ticks=20,
        title="The Land", sub="As it is today, three hundred years later",
        title_at="ne", tools_at="se", capital=None, label_at={}, legend_at=(30, 258)),
    "act-1": dict(
        era="now", size="half", bounds=(60, 114, 234, 228), scale_miles=20, ticks=10,
        title="The Wolds and Saint Ivo's", sub="Book One, chapters 2 to 5",
        title_at="ne", tools_at="se", capital=None, label_at={}),
    "act-2": dict(
        era="now", size="page", bounds=(0, 104, 240, 312), scale_miles=50, ticks=20,
        title="The South", sub="Book One, chapters 5 to 10",
        title_at="ne", tools_at="se", capital=None, label_at={}, legend_at=(30, 262)),
}

MAP_IDS = list(MAPS)


# ---------------------------------------------------------------- helpers

def _n(v):
    """Format a number for SVG with at most two decimals."""
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def _pts(points):
    return " ".join(f"{_n(x)},{_n(y)}" for x, y in points)


def _seed(text):
    """A stable seed from a text. The hash() of Python changes in each run."""
    return sum((i + 1) * ord(c) for i, c in enumerate(text))


def _smooth(points):
    """A path through the points with Catmull-Rom curves."""
    if len(points) < 3:
        return "M" + " L".join(f"{_n(x)},{_n(y)}" for x, y in points)
    p = [points[0]] + list(points) + [points[-1]]
    d = [f"M{_n(p[1][0])},{_n(p[1][1])}"]
    for i in range(1, len(p) - 2):
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p[i - 1], p[i], p[i + 1], p[i + 2]
        c1 = (x1 + (x2 - x0) / 6, y1 + (y2 - y0) / 6)
        c2 = (x2 - (x3 - x1) / 6, y2 - (y3 - y1) / 6)
        d.append(f"C{_n(c1[0])},{_n(c1[1])} {_n(c2[0])},{_n(c2[1])} {_n(x2)},{_n(y2)}")
    return " ".join(d)


def _wobble(points, rng, step, amount):
    """Cut each segment into short pieces and move the inner points a little to the side."""
    out = [points[0]]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        length = math.hypot(x1 - x0, y1 - y0)
        n = max(1, int(length / step))
        nx, ny = (-(y1 - y0) / length, (x1 - x0) / length) if length else (0, 0)
        for i in range(1, n + 1):
            t = i / n
            off = rng.uniform(-amount, amount) if i < n else 0
            out.append((x0 + (x1 - x0) * t + nx * off, y0 + (y1 - y0) * t + ny * off))
    return out


def _text_width(text, size, caps=False, spacing=0.0, bold=False):
    """An estimate of the width of a label in mm. It is a little too large on purpose."""
    em = 0.7 if caps else (0.58 if bold else 0.52)
    return len(text) * size * em + max(0, len(text) - 1) * spacing


def _sample(points, step=.8):
    """Points along a polyline, at most `step` mm apart."""
    out = [points[0]]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        out += [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n) for i in range(1, n + 1)]
    return out


def _overlap(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


# ---------------------------------------------------------------- the map class

class _Map:
    def __init__(self, map_id, size):
        self.id = map_id
        self.cfg = MAPS[map_id]
        self.era = self.cfg["era"]
        bx0, by0, bx1, by1 = self.cfg["bounds"]
        self.w, self.h = SIZES[size or self.cfg["size"]]
        iw, ih = self.w - 2 * MARGIN, self.h - 2 * MARGIN
        self.s = min(iw / (bx1 - bx0), ih / (by1 - by0))
        # Show more land on the long side, so that the map fills its size.
        ex = (iw / self.s - (bx1 - bx0)) / 2
        ey = (ih / self.s - (by1 - by0)) / 2
        self.bounds = (bx0 - ex, by0 - ey, bx1 + ex, by1 + ey)
        self.k = 1.15 if self.s > 0.9 else 1.0  # larger symbols on a regional map
        self.inner = (MARGIN, MARGIN, self.w - MARGIN, self.h - MARGIN)
        self.boxes = []    # the areas that labels and symbols use
        self.lines = []    # small boxes along the rivers and the roads
        self.out = []

    # ---- coordinates
    def X(self, x):
        return MARGIN + (x - self.bounds[0]) * self.s

    def Y(self, y):
        return MARGIN + (y - self.bounds[1]) * self.s

    def P(self, pt):
        return (self.X(pt[0]), self.Y(pt[1]))

    def inside(self, x, y, pad=0.0):
        x0, y0, x1, y1 = self.inner
        return x0 + pad <= x <= x1 - pad and y0 + pad <= y <= y1 - pad

    # ---- which places this map shows
    def shows(self, p):
        if p["era"] not in ("both", self.era):
            return False
        if p["kind"] in ("river", "sea", "region", "mountains"):
            return True
        return self.inside(self.X(p["x"]), self.Y(p["y"]), 1.0)

    def kind(self, p):
        if self.era == "then":
            return p.get("then_kind", p["kind"])
        return p["kind"]

    def places(self):
        return [p for p in PLACES if self.shows(p)]

    # ---- output
    def keep_off(self, pts, r=.5):
        """Keep the labels and the land art off a line."""
        self.lines += [(x - r, y - r, x + r, y + r) for x, y in _sample(pts)]

    def coast_x(self, y):
        """The x of the coast in mm at the height y."""
        pts = self.coast_mm
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if y0 <= y <= y1:
                return x0 + (x1 - x0) * ((y - y0) / (y1 - y0) if y1 != y0 else 0)
        return pts[0][0]

    def free(self, box, lines=True):
        """True if no symbol, label, line, or sea uses the box."""
        if box[0] < max(self.coast_x(box[1]), self.coast_x(box[3])) + .6:
            return False
        if any(_overlap(box, b) for b in self.boxes):
            return False
        return not (lines and any(_overlap(box, b) for b in self.lines))

    def add(self, s):
        self.out.append(s)

    def text(self, x, y, s, size, family=SERIF, anchor="start", italic=False, weight=None,
             spacing=0.0, rotate=0.0):
        a = [f'x="{_n(x)}" y="{_n(y)}" font-family="{family}" font-size="{_n(size)}"',
             f'fill="{INK}"']
        if anchor != "start":
            a.append(f'text-anchor="{anchor}"')
        if italic:
            a.append('font-style="italic"')
        if weight:
            a.append(f'font-weight="{weight}"')
        if spacing:
            a.append(f'letter-spacing="{_n(spacing)}"')
        if rotate:
            a.append(f'transform="rotate({_n(rotate)} {_n(x)} {_n(y)})"')
        self.add(f'<text {" ".join(a)}>{escape(s)}</text>')

    # ---------------------------------------------------------------- layers
    def sea(self):
        rng = random.Random(11)
        coast = [self.P(p) for p in _wobble(COAST, rng, 2.5, 0.8)]
        # The hatching stops a little before the coast, as on an engraved map.
        gap = 0.9
        hatch_edge = [(x - gap, y) for x, y in coast] + [(-50, coast[-1][1]), (-50, coast[0][1])]
        cid = f"dw-sea-{self.id}"
        self.add(f'<clipPath id="{cid}"><polygon points="{_pts(hatch_edge)}"/></clipPath>')
        lines = []
        y = self.inner[1] + 0.6
        while y < self.inner[3]:
            lines.append(f"M{_n(self.inner[0])},{_n(y)}H{_n(self.inner[2])}")
            y += 1.1
        self.add(f'<path clip-path="url(#{cid})" d="{"".join(lines)}" fill="none" stroke="{INK}" '
                 f'stroke-width=".18"/>')
        self.add(f'<path d="{_smooth(coast)}" fill="none" stroke="{INK}" stroke-width=".5" '
                 f'stroke-linejoin="round"/>')
        self.coast_mm = coast

    def scatter(self, area, step_mm, seed, size_mm):
        """Points inside the ellipse of an area, on a loose grid, from north to south."""
        x0, y0, x1, y1 = (self.X(area[0]), self.Y(area[1]), self.X(area[2]), self.Y(area[3]))
        cx, cy, rx, ry = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2
        rng = random.Random(seed)
        pts = []
        row = 0
        y = y0 + step_mm * 0.5
        while y < y1:
            x = x0 + (step_mm * 0.5 if row % 2 else 0) + step_mm * 0.25
            while x < x1:
                px, py = x + rng.uniform(-.3, .3) * step_mm, y + rng.uniform(-.25, .25) * step_mm
                e = ((px - cx) / rx) ** 2 + ((py - cy) / ry) ** 2
                if e <= 1 + rng.uniform(-.25, .1) and self.inside(px, py, 1.5):
                    box = (px - size_mm / 2, py - size_mm, px + size_mm / 2, py + .3)
                    if self.free(box):
                        pts.append((px, py))
                x += step_mm
            y += step_mm * 0.75
            row += 1
        return sorted(pts, key=lambda p: p[1])

    def mountains(self, p):
        rng = random.Random(_seed(p["name"]))
        w0 = 4.2 * self.k
        for x, y in self.scatter(p["area"], w0 * 0.8, _seed(p["name"]) + 1, w0):
            w = w0 * rng.uniform(.8, 1.15)
            h = w * rng.uniform(.6, .85)
            px = x + rng.uniform(-.12, .12) * w
            left, peak, right = (x - w / 2, y), (px, y - h), (x + w / 2, y)
            self.add(f'<polygon points="{_pts([left, peak, right])}" fill="{PAPER}" stroke="none"/>')
            self.add(f'<polyline points="{_pts([left, peak, right])}" fill="none" stroke="{INK}" '
                     f'stroke-width=".35" stroke-linejoin="round"/>')
            # Shade the east side with short lines from the slope to the foot.
            d = []
            for t in (.3, .5, .7, .88):
                sx = peak[0] + (right[0] - peak[0]) * t
                sy = peak[1] + (right[1] - peak[1]) * t
                d.append(f"M{_n(sx)},{_n(sy + .35)}V{_n(y)}")
            self.add(f'<path d="{"".join(d)}" stroke="{INK}" stroke-width=".18"/>')

    def hills(self, p):
        rng = random.Random(_seed(p["name"]))
        w0 = 3.0 * self.k
        d = []
        for x, y in self.scatter(p["area"], w0 * 1.15, _seed(p["name"]) + 2, w0):
            w = w0 * rng.uniform(.8, 1.1)
            h = w * .38
            d.append(f"M{_n(x - w / 2)},{_n(y)}Q{_n(x)},{_n(y - 2 * h)} {_n(x + w / 2)},{_n(y)}")
            d.append(f"M{_n(x + w * .05)},{_n(y - h * .55)}l{_n(w * .18)},{_n(h * .45)}")
        self.add(f'<path d="{"".join(d)}" fill="none" stroke="{INK}" stroke-width=".28" '
                 f'stroke-linecap="round"/>')

    def marsh(self, p):
        w0 = 2.6 * self.k
        d = []
        for x, y in self.scatter(p["area"], w0 * 1.25, _seed(p["name"]) + 3, w0):
            d.append(f"M{_n(x - w0 / 2)},{_n(y)}h{_n(w0)}")
            d.append(f"M{_n(x - w0 * .3)},{_n(y + .7)}h{_n(w0 * .6)}")
            for dx, hh in ((-.22, .75), (0, 1.05), (.22, .75)):
                d.append(f"M{_n(x + dx * w0)},{_n(y - .15)}v{_n(-hh)}")
        self.add(f'<path d="{"".join(d)}" fill="none" stroke="{INK}" stroke-width=".22" '
                 f'stroke-linecap="round"/>')

    def river(self, p):
        rng = random.Random(_seed(p["name"]))
        pts = _wobble([self.P(q) for q in p["course"]], rng, 2.2, .45)
        n = len(pts) - 1
        w0, w1 = .25 * self.k, .7 * self.k
        # One piece for each segment, so the river becomes wider to the mouth.
        ext = [pts[0]] + pts + [pts[-1]]
        for i in range(1, n + 1):
            (x0, y0), (x1, y1), (x2, y2), (x3, y3) = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
            c1 = (x1 + (x2 - x0) / 6, y1 + (y2 - y0) / 6)
            c2 = (x2 - (x3 - x1) / 6, y2 - (y3 - y1) / 6)
            w = w0 + (w1 - w0) * (i - 1) / max(1, n - 1)
            self.add(f'<path d="M{_n(x1)},{_n(y1)}C{_n(c1[0])},{_n(c1[1])} {_n(c2[0])},'
                     f'{_n(c2[1])} {_n(x2)},{_n(y2)}" fill="none" stroke="{INK}" '
                     f'stroke-width="{_n(w)}" stroke-linecap="round"/>')
        self.river_mm[p["name"]] = pts
        self.keep_off(pts)

    def roads(self):
        for a, b, kind, era, via in ROADS:
            ends = (place(a)["era"], place(b)["era"])
            if era not in ("both", self.era) or any(e not in ("both", self.era) for e in ends):
                continue
            pa, pb = self.road_end(a), self.road_end(b)
            pts = [self.P(pa)] + [self.P(v) for v in via] + [self.P(pb)]
            dash = ".5 .75" if kind == "track" else "1.8 .9"
            width = .3 if kind == "track" else .38
            self.add(f'<path d="{_smooth(pts)}" fill="none" stroke="{INK}" stroke-width="{width}" '
                     f'stroke-dasharray="{dash}" stroke-linecap="round"/>')
            self.road_mm.append((a, b, pts))
            self.keep_off(pts, .4)

    def road_end(self, name):
        p = place(name)
        return (p["x"], p["y"])

    # ---------------------------------------------------------------- symbols
    def radius(self, p):
        """The radius of the symbol of a place, in mm."""
        if p["name"] == self.cfg.get("capital"):
            return 2.5 * self.k
        return {"city": 2.0, "town": 1.45, "ruin": 1.6, "shrine": 1.7,
                "fortress": 1.65}[self.kind(p)] * self.k

    def symbol(self, p):
        x, y = self.P((p["x"], p["y"]))
        return self.draw_symbol(x, y, self.kind(p), p["name"] == self.cfg.get("capital"))

    def draw_symbol(self, x, y, kind, capital=False):
        k = self.k
        a = self.add
        if capital:
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(2.5 * k)}" fill="{PAPER}" stroke="{INK}" stroke-width=".45"/>')
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(1.6 * k)}" fill="none" stroke="{INK}" stroke-width=".3"/>')
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(.8 * k)}" fill="{INK}"/>')
            r = 2.5 * k
        elif kind == "city":
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(2 * k)}" fill="{PAPER}" stroke="{INK}" stroke-width=".42"/>')
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(.9 * k)}" fill="{INK}"/>')
            r = 2 * k
        elif kind == "town":
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(1.45 * k)}" fill="{PAPER}"/>')
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(1.0 * k)}" fill="{INK}"/>')
            r = 1.45 * k
        elif kind == "ruin":
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(1.6 * k)}" fill="{PAPER}" stroke="{INK}" '
              f'stroke-width=".38" stroke-dasharray=".75 .55"/>')
            e = .65 * k
            a(f'<path d="M{_n(x - e)},{_n(y - e)}L{_n(x + e)},{_n(y + e)}M{_n(x + e)},{_n(y - e)}'
              f'L{_n(x - e)},{_n(y + e)}" stroke="{INK}" stroke-width=".35"/>')
            r = 1.6 * k
        elif kind == "shrine":
            a(f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(1.7 * k)}" fill="{PAPER}"/>')
            a(f'<path d="M{_n(x)},{_n(y - 1.6 * k)}V{_n(y + 1.3 * k)}M{_n(x - .9 * k)},{_n(y - .6 * k)}'
              f'H{_n(x + .9 * k)}M{_n(x - .9 * k)},{_n(y + 1.3 * k)}H{_n(x + .9 * k)}" '
              f'stroke="{INK}" stroke-width=".45"/>')
            r = 1.7 * k
        elif kind == "fortress":
            u = .55 * k
            pts = [(-3, 2.5), (-3, -2.6), (-1.7, -2.6), (-1.7, -1.6), (-.65, -1.6), (-.65, -2.6),
                   (.65, -2.6), (.65, -1.6), (1.7, -1.6), (1.7, -2.6), (3, -2.6), (3, 2.5)]
            shape = _pts([(x + px * u, y + py * u) for px, py in pts])
            # A white edge keeps the black keep clear of the art under it.
            a(f'<polygon points="{shape}" fill="{PAPER}" stroke="{PAPER}" stroke-width=".8"/>')
            a(f'<polygon points="{shape}" fill="{INK}"/>')
            r = 3 * u
        else:
            return None
        return (x, y, r, kind)

    # ---------------------------------------------------------------- labels
    def label_text(self, p):
        name = p["name"]
        kind = self.kind(p)
        if kind in ("region", "mountains", "sea"):
            return name
        if name.startswith("The "):
            name = name[4:]
            name = name[0].upper() + name[1:]
        return name

    def label_style(self, p):
        kind = self.kind(p)
        if p["name"] == self.cfg.get("capital"):
            return dict(size=3.5, caps=True, spacing=.5, italic=False, weight=None)
        return {
            "city": dict(size=3.4, caps=False, spacing=.1, italic=False, weight="bold"),
            "town": dict(size=2.9, caps=False, spacing=0, italic=False, weight=None),
            "ruin": dict(size=2.9, caps=False, spacing=0, italic=True, weight=None),
            "shrine": dict(size=2.7, caps=False, spacing=0, italic=True, weight=None),
            "fortress": dict(size=3.0, caps=False, spacing=0, italic=False, weight="bold"),
        }[kind]

    def point_label(self, p, sym):
        x, y, r, kind = sym
        st = self.label_style(p)
        s = st["size"] * (1.08 if self.k > 1 else 1)
        txt = self.label_text(p)
        shown = txt.upper() if st["caps"] else txt
        w = _text_width(shown, s, st["caps"], st["spacing"], bool(st["weight"]))
        g = r + .9
        cands = [  # (anchor x, baseline y, text-anchor, box)
            (x + g, y + s * .34, "start", (x + g - .4, y - s * .45, x + g + w + .4, y + s * .45)),
            (x - g, y + s * .34, "end", (x - g - w - .4, y - s * .45, x - g + .4, y + s * .45)),
            (x, y - g - s * .25, "middle", (x - w / 2 - .4, y - g - s * 1.0, x + w / 2 + .4, y - g + .2)),
            (x, y + g + s * .8, "middle", (x - w / 2 - .4, y + g - .2, x + w / 2 + .4, y + g + s * 1.0)),
            (x + g * .6, y - g - s * .1, "start", (x + g * .6 - .4, y - g - s * .85, x + g * .6 + w + .4, y - g + .2)),
            (x + g * .6, y + g + s * .75, "start", (x + g * .6 - .4, y + g - .2, x + g * .6 + w + .4, y + g + s * .95)),
        ]
        prefer = self.cfg.get("label_side", {}).get(p["name"])
        if prefer is not None:
            cands = [cands[prefer]] + cands
        backed = None
        for lx, ly, anchor, box in cands:
            if self.inside(box[0], box[1], .5) and self.inside(box[2], box[3], .5) and self.free(box):
                break
        else:
            # No place is free of lines. Use the first place that is free of labels and
            # symbols, and put white paper under the text so that a line stops at it.
            ok = [c for c in cands if self.inside(c[3][0], c[3][1], .5) and
                  self.inside(c[3][2], c[3][3], .5) and self.free(c[3], lines=False)]
            lx, ly, anchor, box = (ok or cands)[0]
            backed = box
        self.boxes.append(box)
        self.labels.append((backed, lambda lx=lx, ly=ly, anchor=anchor: self.text(
            lx, ly, shown, s, anchor=anchor, italic=st["italic"], weight=st["weight"],
            spacing=st["spacing"])))

    def area_label(self, p):
        kind = self.kind(p)
        at = self.cfg["label_at"].get(p["name"], (p["x"], p["y"]))
        x, y = self.P(at)
        big = p["name"] in ("Ostrey", "Gaunt", "The March of Gauntry")
        if kind == "sea":
            s, caps, sp, italic = 3.4, False, .9, True
        elif big:
            s, caps, sp, italic = 4.6 if p["name"] != "The March of Gauntry" else 3.6, True, 1.4, False
        elif kind == "mountains":
            s, caps, sp, italic = 2.9, True, .9, False
        else:
            s, caps, sp, italic = 2.6, True, .6, False
        s *= 1.08 if self.k > 1 else 1
        shown = p["name"].upper() if caps else p["name"]
        w = _text_width(shown, s, caps, sp)
        if kind == "sea":
            # The sea is a narrow strip, so its name runs from south to north.
            x = self.X(p["x"])
            if not self.inside(x, y, 1):
                return
            ys = [q[1] for q in self.coast_mm]
            y = (max(self.inner[1], min(ys)) + min(self.inner[3], max(ys))) / 2
            box = (x - s * .7, y - w / 2 - .5, x + s * .5, y + w / 2 + .5)
            self.boxes.append(box)
            self.labels.append((None, lambda: self.text(x + s * .35, y, shown, s, anchor="middle",
                                                       italic=True, spacing=sp, rotate=-90)))
            return
        if kind == "mountains":
            y = self.Y(p["area"][3]) + s * 1.1
        # Try the centre first, then move up and down in steps of one line.
        tries = [(0, dy) for dy in (0, -1.5, 1.5, -3, 3, -4.5, 4.5)]
        tries += [(sx * (w / 2 + 2), dy) for dy in (0, -1.5, 1.5) for sx in (1, -1)]
        for dx, dy in tries:
            xx, yy = x + dx, y + dy * s
            box = (xx - w / 2 - .5, yy - s * .8, xx + w / 2 + .5, yy + s * .3)
            if self.inside(box[0], box[1], 1) and self.inside(box[2], box[3], 1) and self.free(box):
                x, y = xx, yy
                break
        else:
            return
        self.boxes.append(box)
        self.labels.append((None, lambda: self.text(x, y, shown, s, anchor="middle", italic=italic,
                                                    spacing=sp)))

    def river_label(self, p):
        pts = [q for q in self.river_mm[p["name"]] if self.inside(q[0], q[1], 4)]
        if len(pts) < 4:
            return
        name = self.label_text(p)
        s = 2.4 * (1.08 if self.k > 1 else 1)
        w = _text_width(name, s, False, .3)
        best = None
        # Choose a straight part of the river with no other label on it.
        for i in range(1, len(pts) - 1):
            (ax, ay), (bx, by) = pts[i - 1], pts[i + 1]
            ang = math.degrees(math.atan2(by - ay, bx - ax))
            if ang > 90:
                ang -= 180
            elif ang < -90:
                ang += 180
            cx, cy = pts[i]
            rad = math.radians(ang)
            ox, oy = -math.sin(rad) * 1.4, math.cos(rad) * 1.4  # below the river line
            lx, ly = cx + ox, cy + oy + s * .3
            half = w / 2
            dx, dy = math.cos(rad) * half, math.sin(rad) * half
            box = (min(lx - dx, lx + dx) - .6, min(ly - dy, ly + dy) - s * .8,
                   max(lx - dx, lx + dx) + .6, max(ly - dy, ly + dy) + .4)
            if not self.free(box, lines=False) or not (
                    self.inside(box[0], box[1], 1) and self.inside(box[2], box[3], 1)):
                continue
            # Prefer a gentle angle and a place near the middle of the shown course.
            score = abs(ang) + 40 * abs(i / len(pts) - .5)
            if best is None or score < best[0]:
                best = (score, lx, ly, ang, box)
        if best is None:
            return
        _, lx, ly, ang, box = best
        self.boxes.append(box)
        self.labels.append((None, lambda: self.text(lx, ly, name, s, anchor="middle", italic=True,
                                                    spacing=.3, rotate=ang)))

    def road_notes(self):
        """On a regional map, say where a road goes when it leaves the map."""
        if self.cfg["size"] != "half":
            return
        for a, b, pts in self.road_mm:
            ins = [self.inside(x, y, 0) for x, y in pts]
            for far, (i0, i1) in ((b, (0, -1)), (a, (-1, 0))):
                if ins[i0] and not ins[i1]:
                    # Walk along the road to the last point inside the frame.
                    seq = _sample(pts if i0 == 0 else pts[::-1], .5)
                    j = next((i for i, q in enumerate(seq) if not self.inside(q[0], q[1], .5)),
                             len(seq) - 1)
                    last = seq[max(0, j - 12)]  # 6 mm back along the road
                    s = 2.3
                    txt = f"to {far}"
                    w = _text_width(txt, s)
                    x, y = last
                    box = (x - w / 2 - .4, y - s * 1.6, x + w / 2 + .4, y - s * .4)
                    # Put the note beside the road, on the side with room.
                    tries = [(dx, dy) for dy in (-1, 1) for dx in (1, -1)]
                    for dx, dy in tries + tries[:1]:
                        anchor = "start" if dx > 0 else "end"
                        bx0 = x + 1 if dx > 0 else x - 1 - w
                        ty = y - s * .5 if dy < 0 else y + s * 1.2
                        box = (bx0 - .4, ty - s * .85, bx0 + w + .4, ty + s * .3)
                        if self.free(box) and self.inside(box[0], box[1]) and self.inside(box[2], box[3]):
                            break
                    dx = 1 if dx > 0 else -1
                    self.boxes.append(box)
                    self.labels.append((None, lambda x=x + dx, ty=ty, txt=txt, s=s, an=anchor: self.text(
                        x, ty, txt, s, family=SANS, anchor=an, italic=True)))

    # ---------------------------------------------------------------- frame and furniture
    def corner(self, where, w, h, pad=2.2):
        x0, y0, x1, y1 = self.inner
        x = x0 + pad if "w" in where else x1 - pad - w
        y = y0 + pad if "n" in where else y1 - pad - h
        return x, y

    def cartouche_box(self):
        t, sub = self.cfg["title"].upper(), self.cfg["sub"]
        ts, ss = (5.6, 2.8) if self.cfg["size"] == "page" else (4.2, 2.5)
        w = max(_text_width(t, ts, True, 1.2), _text_width(sub, ss)) + 8
        h = ts + ss + 7.6
        x, y = self.corner(self.cfg["title_at"], w, h)
        return (x, y, x + w, y + h), t, sub, ts, ss

    def cartouche(self, box, t, sub, ts, ss):
        x0, y0, x1, y1 = box
        a = self.add
        a(f'<rect x="{_n(x0)}" y="{_n(y0)}" width="{_n(x1 - x0)}" height="{_n(y1 - y0)}" '
          f'fill="{PAPER}" stroke="{INK}" stroke-width=".5"/>')
        a(f'<rect x="{_n(x0 + 1)}" y="{_n(y0 + 1)}" width="{_n(x1 - x0 - 2)}" '
          f'height="{_n(y1 - y0 - 2)}" fill="none" stroke="{INK}" stroke-width=".2"/>')
        cx = (x0 + x1) / 2
        self.text(cx, y0 + 3.2 + ts * .8, t, ts, anchor="middle", spacing=1.2)
        self.text(cx, y1 - 3.4, sub, ss, anchor="middle", italic=True)

    def tools_box(self):
        miles = self.cfg["scale_miles"]
        bar = miles * self.s
        w = max(bar + 12, 22)
        h = 24
        x, y = self.corner(self.cfg["tools_at"], w, h)
        return (x, y, x + w, y + h)

    def tools(self, box):
        """A north arrow and a scale bar in miles."""
        x0, y0, x1, y1 = box
        a = self.add
        a(f'<rect x="{_n(x0)}" y="{_n(y0)}" width="{_n(x1 - x0)}" height="{_n(y1 - y0)}" '
          f'fill="{PAPER}" stroke="none"/>')
        cx = (x0 + x1) / 2
        # North arrow: one half black, one half white.
        top, bot = y0 + 5.2, y0 + 14
        a(f'<polygon points="{_pts([(cx, top), (cx, bot - 2), (cx - 2, bot)])}" fill="{INK}"/>')
        a(f'<polygon points="{_pts([(cx, top), (cx + 2, bot), (cx, bot - 2)])}" fill="{PAPER}" '
          f'stroke="{INK}" stroke-width=".3" stroke-linejoin="round"/>')
        a(f'<path d="M{_n(cx - 2)},{_n(bot)}L{_n(cx)},{_n(top)}" stroke="{INK}" stroke-width=".3"/>')
        self.text(cx, y0 + 4.2, "N", 3.2, family=SANS, anchor="middle", weight="600")
        # Scale bar.
        miles = self.cfg["scale_miles"]
        n = 5 if miles % 5 == 0 else 4
        seg = miles * self.s / n
        bx = cx - miles * self.s / 2
        by = y1 - 6
        for i in range(n):
            fill = INK if i % 2 == 0 else PAPER
            a(f'<rect x="{_n(bx + i * seg)}" y="{_n(by)}" width="{_n(seg)}" height="1.2" '
              f'fill="{fill}" stroke="{INK}" stroke-width=".25"/>')
        self.text(bx, by + 4.1, "0", 2.3, family=SANS, anchor="middle")
        self.text(bx + miles * self.s, by + 4.1, f"{miles} miles", 2.3, family=SANS,
                  anchor="middle")

    LEGEND = [("city", "City"), ("town", "Town or village"), ("ruin", "Ruin"), ("shrine", "Shrine"),
              ("fortress", "Fortress"), ("road", "Road"), ("track", "Track")]

    def legend_box(self):
        if "legend_at" not in self.cfg:
            return None
        x, y = self.P(self.cfg["legend_at"])
        return (x, y, x + 33, y + 4 + 4.2 * len(self.LEGEND))

    def legend(self, box):
        """A key to the symbols and the lines."""
        x0, y0, x1, y1 = box
        self.add(f'<rect x="{_n(x0)}" y="{_n(y0)}" width="{_n(x1 - x0)}" height="{_n(y1 - y0)}" '
                 f'fill="{PAPER}" stroke="{INK}" stroke-width=".3"/>')
        for i, (kind, name) in enumerate(self.LEGEND):
            cx, cy = x0 + 5, y0 + 4.3 + 4.2 * i
            if kind in ("road", "track"):
                dash = ".5 .75" if kind == "track" else "1.8 .9"
                self.add(f'<path d="M{_n(cx - 3)},{_n(cy)}H{_n(cx + 3)}" stroke="{INK}" '
                         f'stroke-width=".38" stroke-dasharray="{dash}"/>')
            else:
                self.draw_symbol(cx, cy, kind)
            self.text(cx + 5, cy + .85, name, 2.5, family=SANS)

    def frame(self):
        x0, y0, x1, y1 = self.inner
        a = self.add
        a(f'<rect x="{_n(x0)}" y="{_n(y0)}" width="{_n(x1 - x0)}" height="{_n(y1 - y0)}" '
          f'fill="none" stroke="{INK}" stroke-width=".3"/>')
        a(f'<rect x=".6" y=".6" width="{_n(self.w - 1.2)}" height="{_n(self.h - 1.2)}" '
          f'fill="none" stroke="{INK}" stroke-width=".7"/>')
        # Ticks along the frame, each `ticks` miles, black and white as on an old atlas.
        step = self.cfg["ticks"]
        bx0, by0, bx1, by1 = self.bounds
        d = []
        m = bx0 - bx0 % step + step
        while m < bx1:
            X = self.X(m)
            d.append(f"M{_n(X)},{_n(.6)}V{_n(y0)}M{_n(X)},{_n(y1)}V{_n(self.h - .6)}")
            m += step
        m = by0 - by0 % step + step
        while m < by1:
            Y = self.Y(m)
            d.append(f"M{_n(.6)},{_n(Y)}H{_n(x0)}M{_n(x1)},{_n(Y)}H{_n(self.w - .6)}")
            m += step
        a(f'<path d="{"".join(d)}" stroke="{INK}" stroke-width=".3"/>')

    # ---------------------------------------------------------------- the whole map
    def render(self):
        places = self.places()
        self.labels, self.river_mm, self.road_mm = [], {}, []
        cart = self.cartouche_box()
        tools = self.tools_box()
        cx0, cy0, cx1, cy1 = cart[0]
        self.boxes += [(cx0 - 1, cy0 - 1, cx1 + 1, cy1 + 1), tools]
        legend = self.legend_box()
        if legend:
            self.boxes.append(legend)
        # The symbols take their room first, then the labels, then the land art.
        body = []
        self.out, saved = body, self.out
        syms = []
        for p in places:
            if self.kind(p) in ("city", "town", "ruin", "shrine", "fortress"):
                x, y = self.P((p["x"], p["y"]))
                r = self.radius(p) + .3
                self.boxes.append((x - r, y - r, x + r, y + r))
                syms.append(p)
        self.out = []
        self.sea()
        sea_layer = self.out
        self.out = []
        for p in places:
            if p["kind"] == "river":
                self.river(p)
        self.roads()
        line_layer = self.out
        # Labels: points first, then areas, then rivers, then notes on the roads.
        self.out = []
        sym_layer = []
        for p in syms:
            self.out = sym_layer
            sym = self.symbol(p)
            self.point_label(p, sym)
        for p in places:
            if self.kind(p) in ("region", "mountains", "sea"):
                self.area_label(p)
        for p in places:
            if p["kind"] == "river":
                self.river_label(p)
        self.road_notes()
        # The land art goes around the labels.
        self.out = []
        for p in places:
            kind = self.kind(p)
            if kind == "mountains":
                self.mountains(p)
            elif p["name"] == "The Wolds":
                self.hills(p)
            elif p["name"] == "The Low Fen":
                self.marsh(p)
        art_layer = self.out
        self.out = []
        for box, draw in self.labels:
            if box is not None:
                self.add(f'<rect x="{_n(box[0])}" y="{_n(box[1])}" width="{_n(box[2] - box[0])}" '
                         f'height="{_n(box[3] - box[1])}" fill="{PAPER}"/>')
            draw()
        label_layer = self.out
        self.out = saved

        cid = f"dw-frame-{self.id}"
        x0, y0, x1, y1 = self.inner
        title = escape(f'{self.cfg["title"]}: {self.cfg["sub"]}')
        a = self.add
        a(f'<svg xmlns="http://www.w3.org/2000/svg" class="dw-map" width="{_n(self.w)}mm" '
          f'height="{_n(self.h)}mm" viewBox="0 0 {_n(self.w)} {_n(self.h)}" role="img" '
          f'aria-label="{title}">')
        a(f"<title>{title}</title>")
        a(f'<rect width="{_n(self.w)}" height="{_n(self.h)}" fill="{PAPER}"/>')
        a(f'<clipPath id="{cid}"><rect x="{_n(x0)}" y="{_n(y0)}" width="{_n(x1 - x0)}" '
          f'height="{_n(y1 - y0)}"/></clipPath>')
        a(f'<g clip-path="url(#{cid})">')
        self.out += sea_layer + art_layer + line_layer + sym_layer + label_layer
        a("</g>")
        self.frame()
        self.cartouche(*cart)
        self.tools(tools)
        if legend:
            self.legend(legend)
        a("</svg>")
        return "\n".join(self.out)


# The final maps from the map tool. A file <id>.svg here replaces the preview.
MAP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "maps")

_BLACK_WHITE = {"#000", "#000000", "black", "#fff", "#ffffff", "white", "none"}
_NOT_FOR_PRINT = ("opacity", "rgba(", "hsla(", "<filter", "filter:", "<mask", "mask=",
                  "Gradient", "<image")


def check_print(svg, source):
    """Raise ValueError if the SVG has transparency, a grey or colour fill, or outlined text.

    Lulu prints the interior in black and white and warns about transparency.
    Chrome prints outlined text as a Type 3 font.
    """
    for word in _NOT_FOR_PRINT:
        if word in svg:
            raise ValueError(f"{source}: {word.strip('<(:=')!r} is not allowed in a printed map")
    colours = re.findall(r'\b(?:fill|stroke|color)\s*[=:]\s*"?\s*([^";>]+)', svg)
    for c in colours:
        c = c.strip().lower()
        if c not in _BLACK_WHITE and not c.startswith("url("):
            raise ValueError(f"{source}: the colour {c!r} is not black or white")
    for tag in re.findall(r"<text\b[^>]*>", svg):
        if re.search(r'\bstroke\s*[=:]\s*"?\s*(?!none)[#\w]', tag):
            raise ValueError(f"{source}: a text has an outline")
    return svg


def map_file(map_id):
    """The path of the final map of map_id. The file can be missing."""
    return os.path.join(MAP_DIR, f"{map_id}.svg")


def map_svg(map_id, size=None):
    """Return the SVG of a map as a string.

    map_id is one of MAP_IDS. size is "page" or "half". With no size, the
    map uses its own size from MAPS.

    If compendium/maps/<map_id>.svg exists, return that file. Else return the
    drawn preview. Both must pass check_print().
    """
    if map_id not in MAPS:
        raise KeyError(f"unknown map {map_id!r}; the maps are {', '.join(MAP_IDS)}")
    if size is not None and size not in SIZES:
        raise ValueError(f"unknown map size {size!r}")
    path = map_file(map_id)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return check_print(f.read(), path)
    return check_print(_Map(map_id, size).render(), f"the preview of {map_id}")


def write_previews(folder, png=False):
    """Write each map as an SVG, and an HTML page with all maps, into the folder."""
    os.makedirs(folder, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    fonts = os.path.join(here, "..", "books", "fonts")
    face = "".join(
        f'@font-face {{ font-family: "Inter"; src: url("file://{os.path.abspath(fonts)}/Inter-{n}.ttf"); '
        f"font-weight: {wt}; }}\n" for n, wt in (("Regular", 400), ("SemiBold", 600)))
    pages = []
    for map_id in MAP_IDS:
        svg = map_svg(map_id)
        path = os.path.join(folder, f"{map_id}.svg")
        with open(path, "w") as f:
            f.write(svg)
        html = (f"<!doctype html><meta charset='utf-8'><style>{face} body {{ margin: 0; "
                f"background: #fff; }} svg {{ display: block; }}</style>{svg}")
        hpath = os.path.join(folder, f"{map_id}.html")
        with open(hpath, "w") as f:
            f.write(html)
        pages.append(f"<h2>{map_id}</h2>{svg}")
        if png:
            w, h = (round(float(v.split('"')[1].rstrip("m")) * 96 / 25.4) for v in
                    (svg.split('width=', 2)[1], svg.split('height=', 2)[1]))
            subprocess.run([_chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=2", f"--window-size={w},{h}",
                            f"--screenshot={os.path.join(folder, map_id + '.png')}",
                            f"file://{os.path.abspath(hpath)}"],
                           check=True, capture_output=True)
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(f"<!doctype html><meta charset='utf-8'><style>{face} body {{ font-family: Inter; "
                f"background: #fff; }} svg {{ display: block; margin: 0 0 12mm; }}</style>"
                + "".join(pages))


def _chrome():
    for c in ("google-chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if os.path.exists(c) or subprocess.run(["which", c], capture_output=True).returncode == 0:
            return c
    raise SystemExit("Chrome is not installed")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write_previews(args[0] if args else "maps-preview", png="--png" in sys.argv)
