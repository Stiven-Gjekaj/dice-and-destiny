"""Tests for render_tables. Each test builds its own table sets."""
import pytest

from render_tables import set_errors, set_html, sets_html, table_html


def make_set(**changes):
    t = dict(name="Test Set", theme="Settlements", summary="A set for the tests.",
             tables=[("d4", "Trouble", ["Fire & smoke", "[[Wolves]] at night", "A missing child", "Bad water"]),
                     ("d6", "Trade", ["Wool", "Salt", "Fish", "Timber", "Iron", "Wine"])])
    t.update(changes)
    return t


def test_a_correct_set_has_no_errors():
    assert set_errors(make_set()) == []


def test_set_errors_find_a_missing_key_and_an_unknown_key():
    t = make_set(colour="red")
    del t["summary"]
    errors = set_errors(t)
    assert any("missing key 'summary'" in e for e in errors)
    assert any("unknown key 'colour'" in e for e in errors)


def test_set_errors_find_an_unknown_theme():
    assert any("theme 'Weather'" in e for e in set_errors(make_set(theme="Weather")))


@pytest.mark.parametrize("tables", [
    [],
    [("d7", "Odd", ["a"] * 7)],
    [("d4", "Short", ["a", "b", "c"])],
    [("d4", "Long", ["a", "b", "c", "d", "e"])],
    [("d4", "Repeat", ["a", "b", "c", "a"])],
    [("d4", "Same", ["a", "b", "c", "d"]), ("d4", "Same", ["e", "f", "g", "h"])],
    [("d4", ["a", "b", "c", "d"])],
])
def test_set_errors_find_bad_tables(tables):
    assert set_errors(make_set(tables=tables))


def test_table_html_numbers_each_row_and_shows_the_die():
    out = table_html("d4", "Trouble", ["a", "b", "c", "d"])
    assert "<caption>d4 Trouble</caption>" in out
    assert out.count("<tr><td") == 4
    assert '<td class="c">4</td><td>d</td>' in out


def test_set_html_escapes_text_and_shows_bold_labels():
    out = set_html(make_set())
    assert "Fire &amp; smoke" in out
    assert "<b>Wolves</b> at night" in out


def test_set_html_keeps_the_name_and_the_summary_with_the_first_table_only():
    out = set_html(make_set())
    head = out[out.index('<div class="ts-head">'):out.index("</div>")]
    assert "Test Set" in head and "A set for the tests." in head and "d4 Trouble" in head
    assert "d6 Trade" not in head


def test_set_html_stops_on_a_bad_set():
    with pytest.raises(ValueError):
        set_html(make_set(theme="Weather"))


def test_sets_html_groups_by_theme_in_order_and_sorts_by_name():
    out = sets_html([make_set(name="Zeta"), make_set(name="Dark Hall", theme="Dungeons"), make_set(name="Alpha")])
    assert out.index("<h2>Settlements</h2>") < out.index("Alpha") < out.index("Zeta") < out.index("<h2>Dungeons</h2>")
    assert out.index("<h2>Dungeons</h2>") < out.index("Dark Hall")


def test_sets_html_is_empty_with_no_sets():
    assert sets_html([]) == ""
