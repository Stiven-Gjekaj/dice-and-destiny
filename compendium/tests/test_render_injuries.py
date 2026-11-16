"""Tests for render_injuries. Each test builds its own injury entries."""
import pytest

from render_injuries import injuries_html, injury_errors, roll_ranges, table_errors


def make(**changes):
    i = dict(name="Sore Arm", roll=3, severity="Minor", effect="It hurts & aches.",
             treatment="Rest.", scar=("Tough Arm", "You are [[tough:]] now."))
    i.update(changes)
    return i


def test_a_correct_entry_has_no_problem():
    assert injury_errors(make()) == []


def test_missing_and_unknown_keys_are_reported():
    i = make(color="red")
    del i["scar"]
    errors = injury_errors(i)
    assert "Injury 'Sore Arm': missing key 'scar'" in errors
    assert "Injury 'Sore Arm': unknown key 'color'" in errors


def test_the_roll_must_match_the_severity():
    assert injury_errors(make(roll=12)) == ["Injury 'Sore Arm': a Minor injury needs a roll from 1 to 10"]
    assert injury_errors(make(severity="Lasting", roll=18)) == []


def test_an_unknown_severity_is_reported():
    assert "is not one of" in injury_errors(make(severity="Mild"))[0]


def test_a_d20_result_used_two_times_is_reported():
    errors = table_errors([make(), make(name="Bad Back")])
    assert errors == ["Injury 'Bad Back': roll 3 is also used by 'Sore Arm'"]


def test_each_entry_covers_the_results_up_to_the_next_entry():
    rows = roll_ranges([make(roll=4, name="B"), make(roll=1, name="A"), make(roll=18, severity="Lasting", name="C")])
    assert [(r, i["name"]) for r, i in rows] == [("1–3", "A"), ("4–17", "B"), ("18–20", "C")]


def test_a_single_result_shows_one_number():
    rows = roll_ranges([make(roll=19, severity="Lasting"), make(roll=20, severity="Lasting", name="Last")])
    assert [r for r, _ in rows] == ["19", "20"]


def test_the_html_has_the_table_the_groups_and_the_scar():
    out = injuries_html([make(roll=1), make(name="Mid", roll=11, severity="Serious"),
                         make(name="Big One", roll=18, severity="Lasting")])
    assert "<caption>Injury Table</caption>" in out
    assert out.index("<h2>Minor Injuries</h2>") < out.index("<h2>Lasting Injuries</h2>")
    assert "It hurts &amp; aches." in out
    assert "<dt>Scar: Tough Arm</dt><dd>You are <b>tough:</b> now.</dd>" in out


def test_no_injuries_give_no_html():
    assert injuries_html([]) == ""


def test_a_bad_entry_stops_the_build():
    with pytest.raises(ValueError):
        injuries_html([make(roll=15)])


def test_a_range_that_goes_into_the_next_severity_is_reported():
    errors = table_errors([make(roll=1), make(name="Big", roll=18, severity="Lasting")])
    assert errors == ["Injury 'Sore Arm': its range 1–17 goes past the Minor results; "
                      "add an entry at the first result of the next severity"]


def test_a_table_that_does_not_start_at_1_is_reported():
    errors = table_errors([make(roll=2), make(name="Mid", roll=11, severity="Serious"),
                           make(name="Big", roll=18, severity="Lasting")])
    assert errors == ["Injury table: the lowest roll must be 1, so that each d20 result has an injury"]
