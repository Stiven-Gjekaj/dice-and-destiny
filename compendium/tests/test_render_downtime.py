"""Tests for render_downtime. Each test builds its own activities."""
import pytest

from render_downtime import activities_html, activity_errors, activity_html


def make_activity(**changes):
    a = dict(name="Test Work", summary="You test & check.", time="1 workweek", cost="5 GP",
             check="Intelligence ([[Investigation]]).",
             results=[("9 or lower", "Nothing."), ("10–14", "Something."), ("15 or higher", "More.")],
             complications=["One", "Two", "Three", "Four", "Five", "Six"])
    a.update(changes)
    return a


def test_a_correct_activity_has_no_errors():
    assert activity_errors(make_activity()) == []


def test_activity_errors_find_a_missing_key_and_an_unknown_key():
    a = make_activity(colour="red")
    del a["cost"]
    errors = activity_errors(a)
    assert any("missing key 'cost'" in e for e in errors)
    assert any("unknown key 'colour'" in e for e in errors)


@pytest.mark.parametrize("changes", [
    {"results": [("10 or higher", "All.")]},
    {"results": [("1", "a"), ("2", "b"), ("3", "c"), ("4", "d"), ("5", "e"), ("6", "f"), ("7", "g")]},
    {"results": [("9 or lower", "Nothing."), ("10 or higher",)]},
    {"complications": ["One", "Two", "Three", "Four", "Five"]},
    {"complications": ["One", "Two", "Three", "Four", "Five", "One"]},
])
def test_activity_errors_find_bad_tables(changes):
    assert activity_errors(make_activity(**changes))


def test_activity_html_has_each_result_and_a_numbered_complication_and_escapes_text():
    out = activity_html(make_activity())
    assert "You test &amp; check." in out
    assert "<b>Investigation</b>" in out
    assert '<td class="c">10–14</td><td>Something.</td>' in out
    assert '<td class="c">6</td><td>Six</td>' in out


def test_activity_html_stops_on_a_bad_activity():
    with pytest.raises(ValueError):
        activity_html(make_activity(complications=[]))


def test_activities_html_sorts_by_name_and_is_empty_with_none():
    out = activities_html([make_activity(name="Zeta"), make_activity(name="Alpha")])
    assert out.index("Alpha") < out.index("Zeta")
    assert activities_html([]) == ""
