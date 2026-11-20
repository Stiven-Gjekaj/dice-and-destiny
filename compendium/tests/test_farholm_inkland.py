"""Tests for the inkland config of the map of Farholm."""
import json

import farholm_inkland


def two_places():
    """A stub list of two places of the island, with no area and no course."""
    return [
        dict(name="Hythe", kind="town", x=17.5, y=11.5, era="now", ring="outer", chapters=(1,),
             summary="A town."),
        dict(name="The Kettles", kind="springs", x=12, y=5.5, era="now", ring="inner",
             chapters=(2,), summary="Hot pools."),
    ]


def test_every_place_is_an_overlay_place():
    cfg = farholm_inkland.config(two_places(), roads=[])
    # A place of the base world gets roads that inkland makes.
    assert cfg["pins"]["points"] == []
    overlay = cfg["overlays"][cfg["variants"][0]["overlay"]]
    added = {p["id"]: p for p in overlay["add"]["places"]}
    assert sorted(added) == ["hythe", "kettles"]
    assert added["hythe"]["kind"] == "town"
    assert (added["kettles"]["kind"], added["kettles"]["custom_kind"]) == ("custom", "springs")
    assert added["kettles"]["at"] == [12, 5.5]
    assert added["kettles"]["name"] == "The Kettles"


def test_the_map_shows_no_generated_names_towns_or_roads():
    cfg = farholm_inkland.config(two_places(), roads=[])
    assert cfg["render"]["labels"]["generated"] is False
    assert cfg["render"]["labels"]["check_generated"] is True
    assert (cfg["world"]["states"], cfg["world"]["towns"]) == (0, 0)
    assert cfg["world"]["generated_roads"] is False
    assert cfg["pins"]["roads"] == []


def test_a_road_joins_two_overlay_places():
    roads = [("Hythe", "The Kettles", "path", "now", [(15, 9)])]
    cfg = farholm_inkland.config(two_places(), roads=roads)
    overlay = cfg["overlays"][cfg["variants"][0]["overlay"]]
    (road,) = overlay["add"]["roads"]
    assert (road["from"], road["to"], road["via"]) == ("hythe", "kettles", [[15, 9]])
    assert road["kind"] == "trail"


def test_an_area_is_a_region_and_a_course_is_a_river():
    places = two_places() + [
        dict(name="The Ribs", kind="hills", x=8, y=8, area=(5, 6, 11, 10), era="now", ring="inner",
             chapters=(2,), summary="Ridges."),
        dict(name="The Fleet", kind="river", x=15, y=9, era="now", ring=None, chapters=(1,),
             course=[(12, 6), (14, 8), (17.5, 12)], summary="A stream."),
    ]
    cfg = farholm_inkland.config(places, roads=[])
    regions = {r["id"]: r for r in cfg["pins"]["regions"]}
    assert regions["ribs"]["name"] == "The Ribs"
    assert regions["ribs"]["kind"] == "hills"
    # A region with the outline of a box looks drawn by a machine.
    assert "box" not in regions["ribs"] and len(regions["ribs"]["polygon"]) > 40
    (river,) = cfg["pins"]["rivers"]
    assert (river["id"], river["name"], river["source"]) == ("river-fleet", "The Fleet", [12, 6])
    added = [p["id"] for p in cfg["overlays"][cfg["variants"][0]["overlay"]]["add"]["places"]]
    assert "ribs" not in added and "river-fleet" not in added


def test_the_island_is_land_in_a_sea_and_its_coast_is_not_a_polygon_of_lines():
    cfg = farholm_inkland.config(two_places(), roads=[])
    regions = {r["id"]: r for r in cfg["pins"]["regions"]}
    sea, land = regions["western-sea"], regions["farholm"]
    assert (sea["kind"], land["kind"]) == ("sea", "land")
    assert land["priority"] > sea.get("priority", 0)
    assert land["roughness"] > 0 and land["wander"] > 0
    assert cfg["render"]["hand_drawn"] is True
    assert cfg["render"]["mode"] == "print-safe"


def test_the_committed_config_matches_places_py(tmp_path):
    # Run "python3 build/farholm_inkland.py" after a change to places.py.
    out = farholm_inkland.write(str(tmp_path / "config.json"))
    with open(out, encoding="utf-8") as f, open(farholm_inkland.CONFIG_JSON, encoding="utf-8") as g:
        assert json.load(f) == json.load(g)


def test_a_place_in_the_sea_is_on_the_shore_if_a_road_ends_there():
    places = two_places() + [
        dict(name="Grey Bay", kind="bay", x=10.5, y=13.5, era="now", ring=None, chapters=(1,),
             summary="A bay."),
        dict(name="The wreck", kind="wreck", x=10, y=15, era="now", ring=None, chapters=(1,),
             summary="A wreck."),
    ]
    cfg = farholm_inkland.config(places, roads=[("Grey Bay", "Hythe", "path", "now", [])])
    overlay = cfg["overlays"][cfg["variants"][0]["overlay"]]
    added = {p["id"]: p for p in overlay["add"]["places"]}
    # inkland puts no place in a sea. The road needs a place, so the bay is on its shore.
    bay = added["grey-bay"]
    assert farholm_inkland._inside(bay["at"], farholm_inkland.COAST)
    assert abs(bay["at"][0] - 10.5) < 1 and abs(bay["at"][1] - 13.5) < 1
    # The wreck has no road. It stays in the sea as a named feature.
    assert "wreck" not in added
    assert overlay["add"]["features"] == [
        {"id": "wreck", "kind": "custom", "name": "The wreck", "at": [10, 15]}]
