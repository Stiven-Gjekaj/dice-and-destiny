"""Tests for render_crafting. Each test builds its own materials, recipes, and items."""
import pytest

from render_crafting import all_errors, base_cost, material_errors, recipe_errors, recipes_html, materials_html

ITEMS = {"Test Potion": "Uncommon", "Test Boots": "Uncommon", "Test Shield": "Rare"}


def mat(**changes):
    m = dict(name="Glow Moss", source="Biome", origin="Cave", rarity="Uncommon", check="Intelligence (Nature)",
             text="It glows & hums.")
    m.update(changes)
    return m


def rec(**changes):
    r = dict(item="Test Potion", rarity="Uncommon", consumable=True, tool="Alchemist's Supplies",
             materials=["Glow Moss"], gold=50, days=5, note="")
    r.update(changes)
    return r


MATS = {"Glow Moss": mat(), "Dust": mat(name="Dust", rarity="Common"), "Scale": mat(name="Scale", rarity="Rare")}


def test_a_consumable_takes_half_of_the_base():
    assert base_cost("Uncommon", False) == (200, 10)
    assert base_cost("Uncommon", True) == (100, 5)


def test_correct_entries_have_no_problem():
    assert material_errors(mat()) == []
    assert recipe_errors(rec(), MATS, ITEMS) == []


def test_a_material_needs_a_known_source_and_rarity():
    errors = material_errors(mat(source="Shop", rarity="Epic"))
    assert any("source 'Shop'" in e for e in errors)
    assert any("rarity 'Epic'" in e for e in errors)


def test_a_recipe_below_the_cost_floor_is_reported():
    errors = recipe_errors(rec(gold=10), MATS, ITEMS)
    assert errors == ["Recipe 'Test Potion': costs 60 GP in all; the floor is 80 GP (80% of 100)"]


def test_a_recipe_below_the_time_floor_is_reported():
    errors = recipe_errors(rec(item="Test Boots", consumable=False, gold=150, days=7), MATS, ITEMS)
    assert errors == ["Recipe 'Test Boots': takes 7 days; the floor is 8 (80% of 10)"]


def test_a_recipe_at_the_floor_passes():
    assert recipe_errors(rec(gold=30, days=4), MATS, ITEMS) == []


def test_the_item_must_exist_with_the_same_rarity():
    assert recipe_errors(rec(item="No Such Thing"), MATS, ITEMS) == [
        "Recipe 'No Such Thing': the item is not an SRD magic item or an original magic item of this book"]
    assert recipe_errors(rec(item="Test Shield"), MATS, ITEMS) == ["Recipe 'Test Shield': the item is Rare, not Uncommon"]


def test_unknown_materials_are_reported():
    assert recipe_errors(rec(materials=["Glow Moss", "Ghost Ink"]), MATS, ITEMS) == [
        "Recipe 'Test Potion': unknown material 'Ghost Ink'"]


def test_a_recipe_needs_a_material_of_its_rarity_and_none_above():
    low = recipe_errors(rec(materials=["Dust"], gold=90), MATS, ITEMS)
    high = recipe_errors(rec(materials=["Scale"]), MATS, ITEMS)
    rule = "Recipe 'Test Potion': needs at least one material of its own rarity, and none above it"
    assert low == [rule] and high == [rule]


def test_a_material_name_used_two_times_is_reported():
    assert all_errors([mat(), mat()], [], ITEMS) == ["Material 'Glow Moss': the name is used two times"]


def test_the_html_shows_the_totals_and_the_groups():
    out = recipes_html([mat()], [rec(), rec(item="Test Boots", consumable=False, gold=150, days=10)], ITEMS)
    assert "<h2>Uncommon Recipes</h2>" in out
    assert "Glow Moss (50 GP)" in out
    assert "50 GP and the materials (100 GP in all), 5 workdays" in out
    assert out.index("Test Boots") < out.index("Test Potion")


def test_materials_are_grouped_by_source():
    out = materials_html([mat(name="Fang", source="Monster", origin="Wolf"), mat()])
    assert out.index("<h2>Monster Materials</h2>") < out.index("<h2>Biome Materials</h2>")
    assert "It glows &amp; hums." in out
    assert "Intelligence (Nature) DC 13 · 50 GP" in out


def test_a_bad_recipe_stops_the_build():
    with pytest.raises(ValueError):
        recipes_html([mat()], [rec(gold=0)], ITEMS)
