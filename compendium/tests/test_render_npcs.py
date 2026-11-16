"""Tests for render_npcs. Each test builds its own entries."""
import pytest

from monster_engine import M
from render_npcs import npc_errors, npcs_html, npcs_index_html


def make_npc(name="Test Guard", typ="Humanoid", cr=1):
    return M(name, "M", typ, "Any Alignment", cr, "14 12 12 10 10 10",
             attacks=[("Spear", "m", "1d8", "Piercing")])


def test_a_correct_npc_has_no_errors():
    assert npc_errors(("Guards and Soldiers", make_npc())) == []


def test_npc_errors_find_an_unknown_role():
    errors = npc_errors(("Bakers", make_npc()))
    assert any("role 'Bakers'" in e for e in errors)


def test_npc_errors_find_a_type_that_is_not_humanoid():
    errors = npc_errors(("Guards and Soldiers", make_npc(typ="Beast")))
    assert any("not a Humanoid" in e for e in errors)


@pytest.mark.parametrize("cr", [0, 16])
def test_npc_errors_find_a_cr_out_of_range(cr):
    errors = npc_errors(("Guards and Soldiers", make_npc(cr=cr)))
    assert any("outside 1/8 to 15" in e for e in errors)


def test_npc_errors_find_an_entry_that_is_not_a_pair():
    assert npc_errors(make_npc())
    assert npc_errors(("Guards and Soldiers", "not a monster"))


def test_npcs_html_groups_by_role_in_role_order_and_sorts_by_cr():
    npcs = [("Cultists", make_npc("Zealot", cr=3)),
            ("Guards and Soldiers", make_npc("Captain", cr=4)),
            ("Guards and Soldiers", make_npc("Recruit", cr=0.125))]
    text = npcs_html(npcs)
    assert text.index("Guards and Soldiers") < text.index("Cultists")
    assert text.index("Recruit") < text.index("Captain")
    assert text.count('class="monster"') == 3


def test_npcs_html_stops_on_a_bad_entry():
    with pytest.raises(ValueError):
        npcs_html([("Bakers", make_npc())])


def test_npcs_html_and_index_are_empty_with_no_entries():
    assert npcs_html([]) == ""
    assert npcs_index_html([]) == ""


def test_npcs_index_html_shows_the_cr_and_the_xp():
    text = npcs_index_html([("Guards and Soldiers", make_npc("Recruit", cr=0.125))])
    assert "Recruit" in text
    assert "CR 1/8" in text
    assert "25 XP" in text
