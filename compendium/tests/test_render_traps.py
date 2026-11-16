"""Tests for render_traps. Each test builds its own entries."""
import pytest

from render_traps import damage_cap, trap_errors, trap_html, traps_html, traps_index_html


def make_trap(**changes):
    t = dict(
        name="Test Trap", kind="Trap", where="Dungeon", severity="Dangerous",
        summary="A trap for the tests.", trigger="A creature steps on it.",
        effect="[[Hit:]] it takes the damage & falls.", find="Look down.", stop="Jam it.",
        bands=[(1, 12, "2d10"), (5, 14, "4d10")],
    )
    t.update(changes)
    return t


def test_a_correct_trap_has_no_errors():
    assert trap_errors(make_trap()) == []


def test_trap_errors_find_a_missing_key_and_an_unknown_key():
    t = make_trap(colour="red")
    del t["stop"]
    errors = trap_errors(t)
    assert any("missing key 'stop'" in e for e in errors)
    assert any("unknown key 'colour'" in e for e in errors)


def test_trap_errors_find_an_unknown_kind_and_severity():
    errors = trap_errors(make_trap(kind="Puzzle", severity="Mild"))
    assert any("kind 'Puzzle'" in e for e in errors)
    assert any("severity 'Mild'" in e for e in errors)


@pytest.mark.parametrize("bands", [[], [(2, 12, "1d10")], [(5, 12, "1d10"), (1, 12, "1d10")],
                                   [(1, 12, "1d10"), (1, 12, "1d10")]])
def test_trap_errors_find_bad_bands(bands):
    assert trap_errors(make_trap(bands=bands))


@pytest.mark.parametrize("dc", [9, 21])
def test_trap_errors_find_a_dc_out_of_range(dc):
    assert any("DC must be from" in e for e in trap_errors(make_trap(bands=[(1, dc, "1d10")])))


def test_trap_errors_find_a_dc_that_goes_down():
    assert any("go down" in e for e in trap_errors(make_trap(bands=[(1, 15, "1d10"), (5, 13, "2d10")])))


def test_damage_cap_follows_the_improvised_damage_table():
    assert damage_cap(1, "Setback") == 5
    assert damage_cap(5, "Dangerous") == 22
    assert damage_cap(17, "Deadly") == 132


def test_damage_at_the_cap_is_correct_and_above_the_cap_is_an_error():
    assert trap_errors(make_trap(severity="Setback", bands=[(1, 10, "1d10")])) == []
    errors = trap_errors(make_trap(severity="Setback", bands=[(1, 10, "2d6")]))
    assert any("above 5, the Setback limit" in e for e in errors)


def test_a_flat_bonus_counts_toward_the_cap():
    assert trap_errors(make_trap(severity="Setback", bands=[(1, 10, "1d8 + 1")])) == []
    assert trap_errors(make_trap(severity="Setback", bands=[(1, 10, "1d8 + 2")]))


def test_trap_errors_find_damage_that_is_not_dice():
    assert any("not a dice expression" in e for e in trap_errors(make_trap(bands=[(1, 12, "lots")])))


def test_a_hazard_with_no_damage_shows_no_damage_column():
    out = trap_html(make_trap(kind="Hazard", bands=[(1, 12, ""), (5, 15, "")]))
    assert "Damage" not in out
    assert out.count("<tr>") == 3


def test_a_band_with_no_damage_shows_none_when_others_have_damage():
    out = trap_html(make_trap(bands=[(1, 12, ""), (5, 14, "4d10")]))
    assert ">None</td>" in out


def test_trap_html_escapes_the_text_and_bolds_labels():
    out = trap_html(make_trap(name="A & B"))
    assert "A &amp; B" in out
    assert "<b>Hit:</b> it takes the damage &amp; falls." in out
    assert "<dt>Find it</dt>" in out and "<dt>Stop it</dt>" in out


def test_trap_html_stops_on_an_error():
    with pytest.raises(ValueError, match="severity"):
        trap_html(make_trap(severity="Mild"))


def test_traps_html_groups_by_kind_and_sorts_by_name():
    out = traps_html([make_trap(name="Zed"), make_trap(name="Alpha"), make_trap(name="Fog", kind="Hazard")])
    assert out.index("<h2>Traps</h2>") < out.index("Alpha") < out.index("Zed") < out.index("<h2>Hazards</h2>") < out.index("Fog")


def test_traps_html_is_empty_with_no_entries():
    assert traps_html([]) == ""
    assert traps_index_html([]) == ""


def test_traps_index_lists_an_entry_in_each_of_its_bands():
    out = traps_index_html([make_trap(name="Pit", bands=[(1, 12, "1d10"), (11, 15, "4d10")])])
    assert out.count("Pit") == 2
    assert "None yet." in out
