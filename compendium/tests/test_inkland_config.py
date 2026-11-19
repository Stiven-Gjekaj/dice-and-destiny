"""Tests for the inkland config of the Dawnwatch maps."""
import json
import os

import inkland_config


def small_land():
    """A small land: a coast, a sea, one river, two places, one road, and one map."""
    return {
        "land_miles": [100, 100],
        "coast": [[10, 0], [12, 50], [10, 100]],
        "places": [
            dict(name="Hollin", kind="town", x=40, y=40, era="both", old_names=[], maps=["land-today"]),
            dict(name="Mere", kind="village", x=60, y=70, era="now", old_names=[], maps=["land-today"]),
        ],
        "areas": [
            dict(name="The Grey Sea", kind="sea", era="both", old_names=[], maps=["land-today"],
                 x=5, y=50, box=[0, 0, 10, 100]),
            dict(name="Far March", kind="region", era="now", old_names=[], maps=[],
                 x=80, y=90, box=[70, 80, 90, 100]),
        ],
        "rivers": [dict(name="The River Rill", era="both",
                        points=[[90, 10], [92, 20], [94, 30]])],
        "roads": [dict(start="Hollin", end="Mere", kind="road", era="now",
                       points=[[40, 40], [60, 70]])],
        "maps": {"land-today": dict(era="now", size_mm=[167, 120], bounds_miles=[0, 0, 50, 100],
                                    title="The Land")},
    }


def test_a_river_id_has_one_prefix():
    cfg = inkland_config.build(small_land())
    assert [r["id"] for r in cfg["pins"]["rivers"]] == ["river-rill"]


def test_a_map_hides_the_labels_of_items_outside_it():
    cfg = inkland_config.build(small_land())
    labels = cfg["overlays"]["land-today"]["labels"]
    # The river is outside the view, and the map does not list the march.
    assert labels["river:river-rill"] == {"hide": True}
    assert labels["feature:far-march"] == {"hide": True}
    assert cfg["variants"][0]["overlay"] == "land-today"


def test_the_maps_show_no_generated_names_or_places():
    cfg = inkland_config.build(small_land())
    assert cfg["render"]["labels"] == {"generated": False, "check_generated": True}
    assert (cfg["world"]["states"], cfg["world"]["towns"]) == (0, 0)
    assert cfg["world"]["fill_land"] is True


def test_each_place_is_in_the_overlay_of_its_map():
    # A place of the base world would get roads that inkland makes.
    cfg = inkland_config.build(small_land())
    assert cfg["pins"]["points"] == []
    added = [p["id"] for p in cfg["overlays"]["land-today"]["add"]["places"]]
    assert added == ["hollin", "mere"]


def test_the_committed_config_matches_places_json(tmp_path):
    # Run "python3 build/inkland_config.py" after a change to places.json.
    out = inkland_config.write(str(tmp_path / "config.json"))
    with open(out, encoding="utf-8") as f, open(inkland_config.CONFIG_JSON, encoding="utf-8") as g:
        assert json.load(f) == json.load(g)


def test_an_organic_outline_is_not_a_box_and_stays_in_the_frame():
    box = [70, 255, 190, 320]
    pts = inkland_config.organic_outline("gaunt", box, (240, 320))
    assert pts == inkland_config.organic_outline("gaunt", box, (240, 320))
    assert len(pts) > 40
    assert all(0 <= x <= 240 and 0 <= y <= 320 for x, y in pts)
    # The outline keeps near the box, but goes in and out of it.
    xs = [x for x, _ in pts]
    assert 60 < min(xs) < 80 and 180 < max(xs) < 200
    assert len({round(x) for x, y in pts if y < 270}) > 10


def test_the_dunn_is_the_main_river():
    land = small_land()
    land["rivers"].append(dict(name="The River Dunn", era="both", points=[[30, 10], [30, 50], [12, 60]]))
    rivers = {r["id"]: r for r in inkland_config.build(land)["pins"]["rivers"]}
    assert rivers["river-dunn"]["main"] is True
    assert "main" not in rivers["river-rill"]


def test_only_the_old_map_hides_the_relief_of_the_new_age():
    land = small_land()
    land["maps"]["ostrey-then"] = dict(era="then", size_mm=[167, 250], bounds_miles=[0, 0, 100, 100],
                                       title="Ostrey")
    variants = {v["name"]: v for v in inkland_config.build(land)["variants"]}
    assert variants["ostrey-then"]["relief"] == {"hide_in": inkland_config.THEN_HIDE_RELIEF}
    assert "relief" not in variants["land-today"]

