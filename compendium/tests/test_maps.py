"""Tests for the maps of The Dawnwatch. The interior prints in black and white, with no transparency."""
import os
import re
import xml.etree.ElementTree as ET

import pytest

import maps
from content.dawnwatch import places as places_module

NS = "{http://www.w3.org/2000/svg}"
REAL_MAP_DIR = maps.MAP_DIR


@pytest.fixture(autouse=True)
def previews_only(tmp_path_factory, monkeypatch):
    """Test the drawn previews. A final map in compendium/maps/ must not change these tests."""
    monkeypatch.setattr(maps, "MAP_DIR", str(tmp_path_factory.mktemp("no-final-maps")))


def labels(svg):
    """The text of each label in the SVG."""
    root = ET.fromstring(svg)
    return ["".join(t.itertext()) for t in root.iter(NS + "text")]


def has_name(svg, name):
    """True if a label holds the name as whole words, in any case."""
    pat = re.compile(r"(?<![\w'])" + re.escape(name) + r"(?![\w'])", re.IGNORECASE)
    return any(pat.search(t) for t in labels(svg))


def test_the_book_has_the_four_maps():
    assert maps.MAP_IDS == ["ostrey-then", "land-today", "act-1", "act-2"]


@pytest.mark.parametrize("map_id", maps.MAP_IDS)
def test_each_map_is_valid_svg(map_id):
    root = ET.fromstring(maps.map_svg(map_id))
    assert root.tag == NS + "svg"
    w, h = root.get("width"), root.get("height")
    assert w.endswith("mm") and h.endswith("mm")
    size = maps.SIZES[maps.MAPS[map_id]["size"]]
    assert (float(w[:-2]), float(h[:-2])) == size
    assert root.get("viewBox") == f"0 0 {size[0]:g} {size[1]:g}"


def test_the_sizes_are_those_of_the_map_tool():
    assert maps.SIZES == {"page": (167, 250), "half": (167, 120)}


@pytest.mark.parametrize("size", ["page", "half"])
def test_a_map_has_the_size_that_the_build_asks_for(size):
    root = ET.fromstring(maps.map_svg("act-2", size))
    assert (float(root.get("width")[:-2]), float(root.get("height")[:-2])) == maps.SIZES[size]


def test_an_unknown_map_or_size_raises():
    with pytest.raises(KeyError):
        maps.map_svg("nowhere")
    with pytest.raises(ValueError):
        maps.map_svg("act-1", "poster")


@pytest.mark.parametrize("map_id", maps.MAP_IDS)
def test_maps_use_only_black_and_white(map_id):
    svg = maps.map_svg(map_id)
    colours = set(re.findall(r'\b(?:fill|stroke)="([^"]+)"', svg))
    colours = {c for c in colours if not c.startswith("url(")}
    assert colours <= {"#000", "#fff", "none"}, colours
    for word in ("opacity", "rgba", "filter", "Gradient", "mask", " style="):
        assert word not in svg, word


@pytest.mark.parametrize("map_id", maps.MAP_IDS)
def test_labels_have_no_outline(map_id):
    # Chrome prints outlined text as a Type 3 font, and Lulu warns about Type 3 fonts.
    root = ET.fromstring(maps.map_svg(map_id))
    for t in root.iter(NS + "text"):
        assert t.get("stroke") is None
        assert t.get("font-family").split(",")[0] in ("Caladea", "Inter")


def test_maps_have_no_em_dash():
    for map_id in maps.MAP_IDS:
        assert "\u2014" not in maps.map_svg(map_id)


def test_a_new_place_appears_on_the_maps_of_its_era(monkeypatch):
    extra = [
        dict(name="Hollin", kind="town", x=60, y=120, era="now", chapters=(), summary="A test town."),
        dict(name="Old Marrow", kind="shrine", x=60, y=60, era="then", chapters=(), summary="A test shrine."),
        dict(name="Weir", kind="ruin", then_kind="town", x=90, y=280, era="both", chapters=(),
             summary="A test ruin."),
    ]
    monkeypatch.setattr(maps, "PLACES", list(places_module.PLACES) + extra)
    then, today = maps.map_svg("ostrey-then"), maps.map_svg("land-today")
    assert has_name(today, "Hollin") and not has_name(then, "Hollin")
    assert has_name(then, "Old Marrow") and not has_name(today, "Old Marrow")
    assert has_name(then, "Weir") and has_name(today, "Weir")


def test_a_place_off_a_regional_map_is_not_on_it(monkeypatch):
    extra = [dict(name="Farhold", kind="town", x=10, y=10, era="now", chapters=(), summary="A test town.")]
    monkeypatch.setattr(maps, "PLACES", list(places_module.PLACES) + extra)
    assert has_name(maps.map_svg("land-today"), "Farhold")
    assert not has_name(maps.map_svg("act-1"), "Farhold")


def test_a_place_moves_when_the_list_changes(monkeypatch):
    def keep_x(svg):
        root = ET.fromstring(svg)
        return [float(t.get("x")) for t in root.iter(NS + "text") if "".join(t.itertext()) == "Pell"]

    one = [dict(name="Pell", kind="town", x=100, y=200, era="now", chapters=(), summary="A test town.")]
    two = [dict(one[0], x=200)]
    monkeypatch.setattr(maps, "PLACES", list(places_module.PLACES) + one)
    a = keep_x(maps.map_svg("land-today"))
    monkeypatch.setattr(maps, "PLACES", list(places_module.PLACES) + two)
    b = keep_x(maps.map_svg("land-today"))
    assert len(a) == len(b) == 1 and b[0] > a[0]


def test_ostrey_then_has_no_name_of_today():
    svg = maps.map_svg("ostrey-then")
    for p in places_module.PLACES:
        if p["era"] == "now":
            assert not has_name(svg, p["name"]), p["name"]


def test_land_today_has_no_old_name():
    svg = maps.map_svg("land-today")
    # The town Corrin and the river the Corrin share a name. The river is still there.
    kept = {p["name"].removeprefix("The ") for p in places_module.PLACES if p["era"] == "both"}
    for p in places_module.PLACES:
        if p["era"] == "then" and p["name"] not in kept:
            assert not has_name(svg, p["name"]), p["name"]


def test_old_names_are_on_ostrey_then():
    names = [p["name"] for p in places_module.PLACES if p["era"] == "then"]
    svg = maps.map_svg("ostrey-then")
    for name in names:
        shown = name[4:] if name.startswith("The ") else name
        assert has_name(svg, shown), name


def test_has_name_matches_whole_words_only():
    svg = '<svg xmlns="http://www.w3.org/2000/svg"><text>THE MARCH OF GAUNTRY</text></svg>'
    assert not has_name(svg, "Gaunt")
    assert has_name(svg, "March of Gauntry")


def test_write_previews_writes_each_map(tmp_path):
    maps.write_previews(str(tmp_path))
    for map_id in maps.MAP_IDS:
        svg = (tmp_path / f"{map_id}.svg").read_text()
        assert svg == maps.map_svg(map_id)
        assert (tmp_path / f"{map_id}.html").exists()
    assert (tmp_path / "index.html").read_text().count("<svg") == len(maps.MAP_IDS)


FINAL = ('<svg xmlns="http://www.w3.org/2000/svg" width="167mm" height="250mm" viewBox="0 0 167 250">'
         '<rect width="167" height="250" fill="white"/><path d="M0,0L10,10" stroke="#000000"/>'
         '<text x="5" y="5" font-family="Caladea" fill="black">Final map</text></svg>')


def test_a_file_in_the_map_folder_replaces_the_preview(tmp_path, monkeypatch):
    monkeypatch.setattr(maps, "MAP_DIR", str(tmp_path))
    (tmp_path / "act-1.svg").write_text(FINAL)
    assert maps.map_svg("act-1") == FINAL
    assert maps.map_svg("act-2") != FINAL
    assert "dw-map" in maps.map_svg("act-2")


def test_with_no_file_the_build_draws_the_preview(tmp_path, monkeypatch):
    monkeypatch.setattr(maps, "MAP_DIR", str(tmp_path))
    assert 'class="dw-map"' in maps.map_svg("act-1")


@pytest.mark.parametrize("bad", [
    '<rect fill="#888"/>',
    '<rect fill="grey"/>',
    '<rect style="fill:#cccccc"/>',
    '<rect fill="#000" opacity=".5"/>',
    '<rect fill="#000" fill-opacity=".5"/>',
    '<rect fill="rgba(0,0,0,.5)"/>',
    '<defs><linearGradient id="g"/></defs>',
    '<text stroke="#000">Outline</text>',
    '<g stroke="#fff"><text>Halo</text></g>',
    '<g stroke="#fff"><g><text><textPath href="#p">Halo</textPath></text></g></g>',
    '<g style="stroke:#fff"><text>Halo</text></g>',
])
def test_a_map_file_that_does_not_print_is_refused(tmp_path, monkeypatch, bad):
    monkeypatch.setattr(maps, "MAP_DIR", str(tmp_path))
    (tmp_path / "act-1.svg").write_text(FINAL.replace("</svg>", bad + "</svg>"))
    with pytest.raises(ValueError):
        maps.map_svg("act-1")


def test_two_final_maps_with_the_same_ids_do_not_share_them(tmp_path, monkeypatch):
    monkeypatch.setattr(maps, "MAP_DIR", str(tmp_path))
    body = ('<defs><clipPath id="clip"><rect width="1" height="1"/></clipPath></defs>'
            '<path id="river" d="M0 0L1 1" clip-path="url(#clip)"/>'
            '<text><textPath href="#river">River</textPath></text>'
            '<text><textPath xlink:href="#river">River</textPath></text>')
    svg = FINAL.replace("</svg>", body + "</svg>").replace(
        "<svg ", '<svg xmlns:xlink="http://www.w3.org/1999/xlink" ', 1)
    (tmp_path / "act-1.svg").write_text(svg)
    (tmp_path / "act-2.svg").write_text(svg)
    one, two = maps.map_svg("act-1"), maps.map_svg("act-2")
    ids_one = set(re.findall(r'\bid="([^"]+)"', one))
    ids_two = set(re.findall(r'\bid="([^"]+)"', two))
    assert not ids_one & ids_two
    for svg_text, ids in ((one, ids_one), (two, ids_two)):
        refs = re.findall(r'href="#([^"]+)"', svg_text) + re.findall(r"url\(#([^)]+)\)", svg_text)
        assert len(refs) == 3 and set(refs) <= ids


def test_a_text_can_turn_off_the_stroke_of_its_group(tmp_path, monkeypatch):
    monkeypatch.setattr(maps, "MAP_DIR", str(tmp_path))
    good = '<g stroke="#000"><path d="M0 0L1 1"/><text stroke="none">Plain</text></g>'
    (tmp_path / "act-1.svg").write_text(FINAL.replace("</svg>", good + "</svg>"))
    assert "Plain" in maps.map_svg("act-1")


@pytest.mark.parametrize("map_id", maps.MAP_IDS)
def test_each_final_map_in_the_repository_prints(map_id, monkeypatch):
    monkeypatch.setattr(maps, "MAP_DIR", REAL_MAP_DIR)
    if not os.path.exists(maps.map_file(map_id)):
        pytest.skip("no final map yet")
    ET.fromstring(maps.map_svg(map_id))


def test_missing_maps_lists_each_map_with_no_final_file(tmp_path, monkeypatch):
    monkeypatch.setattr(maps, "MAP_DIR", str(tmp_path))
    assert maps.missing_maps() == maps.MAP_IDS
    (tmp_path / "act-1.svg").write_text(FINAL)
    (tmp_path / "act-2.svg").write_text(FINAL)
    assert maps.missing_maps() == ["ostrey-then", "land-today"]
    assert maps.missing_maps(["act-1", "land-today"]) == ["land-today"]
    for map_id in maps.MAP_IDS:
        (tmp_path / f"{map_id}.svg").write_text(FINAL)
    assert maps.missing_maps() == []


def test_the_committed_places_json_matches_places_py():
    # Run "python3 build/maps.py --places-json" after a change to places.py.
    path = os.path.join(REAL_MAP_DIR, "places.json")
    with open(path, encoding="utf-8") as f:
        assert f.read() == maps.places_json()


def test_places_json_follows_the_list(monkeypatch):
    import json
    extra = [
        dict(name="Hollin", kind="town", x=4, y=60, era="now", chapters=(), summary="A test town."),
        dict(name="Old Hollin", kind="town", x=4, y=60, era="then", chapters=(), now_name="Hollin",
             summary="A test town."),
        dict(name="Mire", kind="region", x=100, y=150, area=(90, 140, 110, 160), era="now",
             chapters=(), summary="A test marsh."),
        dict(name="The Rill", kind="river", x=100, y=210, era="both", chapters=(),
             course=[(100, 200), (100, 220)], summary="A test river."),
    ]
    monkeypatch.setattr(maps, "PLACES", extra)
    monkeypatch.setattr(maps, "ROADS", [])
    data = json.loads(maps.places_json())
    town = next(p for p in data["places"] if p["name"] == "Hollin")
    assert (town["x"], town["y"], town["old_names"]) == (4, 60, ["Old Hollin"])
    assert town["maps"] == ["land-today"]
    old = next(p for p in data["places"] if p["name"] == "Old Hollin")
    assert old["maps"] == ["ostrey-then"] and old["now_name"] == "Hollin"
    assert data["areas"] == [dict(name="Mire", kind="region", era="now", old_names=[],
                                  maps=["land-today", "act-1", "act-2"], x=100, y=150,
                                  box=[90, 140, 110, 160])]
    assert data["rivers"][0]["points"] == [[100, 200], [100, 220]]
    assert data["maps"]["act-1"]["size_mm"] == [167, 120]


def test_each_map_draws_only_the_roads_of_its_era(monkeypatch):
    def roads(svg):
        return len(re.findall(r'<path d="[^"]*" fill="none" stroke="#000" stroke-width="[\d.]+" '
                              r'stroke-dasharray', svg))

    monkeypatch.setattr(maps, "ROADS", [])
    base_then, base_now = roads(maps.map_svg("ostrey-then")), roads(maps.map_svg("land-today"))
    monkeypatch.setattr(maps, "ROADS", [
        ("Kingsholm", "Dawnwatch Keep", "old road", "then", []),
        ("Kingsholm", "Fennick", "old road", "both", []),
        ("Kingsholm", "The shrine at Kell", "road", "now", []),
        ("Kingsholm", "Stannard", "road", "now", []),
    ])
    assert roads(maps.map_svg("ostrey-then")) - base_then == 2
    assert roads(maps.map_svg("land-today")) - base_now == 3
