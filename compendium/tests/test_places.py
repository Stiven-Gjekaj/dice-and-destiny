"""Tests for the places of The Dawnwatch, Book One."""
import pytest
from content.dawnwatch.places import KINDS, PLACES, ROADS, place

W, H = 240, 320  # the size of the land in miles, from the world bible


def test_each_place_has_the_keys():
    for p in PLACES:
        for key in ("name", "kind", "x", "y", "summary", "chapters", "era"):
            assert key in p, (p.get("name"), key)


def test_each_kind_is_known():
    for p in PLACES:
        assert p["kind"] in KINDS, p["name"]
        assert p.get("then_kind", "city") in KINDS, p["name"]


def test_each_era_is_known():
    for p in PLACES:
        assert p["era"] in ("then", "now", "both"), p["name"]


def test_names_are_unique():
    names = [p["name"] for p in PLACES]
    assert len(names) == len(set(names))


def test_each_place_is_on_the_map():
    for p in PLACES:
        assert 0 <= p["x"] <= W and 0 <= p["y"] <= H, p["name"]
        for x, y in p.get("course", []):
            assert 0 <= x <= W and 0 <= y <= H, p["name"]


def test_an_area_holds_its_centre():
    for p in PLACES:
        if "area" in p:
            x0, y0, x1, y1 = p["area"]
            assert x0 <= p["x"] <= x1 and y0 <= p["y"] <= y1, p["name"]


def test_each_river_has_a_course():
    for p in PLACES:
        assert (p["kind"] == "river") == ("course" in p), p["name"]
        if "course" in p:
            assert len(p["course"]) >= 2


def test_an_old_name_points_to_a_name_of_today():
    for p in PLACES:
        if "now_name" in p:
            assert p["era"] == "then", p["name"]
            assert place(p["now_name"])["era"] in ("now", "both"), p["name"]


def test_each_road_joins_two_places():
    for a, b, kind, era, via in ROADS:
        place(a), place(b)
        assert era in ("then", "now", "both")


def test_place_raises_for_an_unknown_name():
    with pytest.raises(KeyError):
        place("Nowhere")


def test_summaries_have_no_em_dash():
    for p in PLACES:
        assert "\u2014" not in p["summary"], p["name"]
