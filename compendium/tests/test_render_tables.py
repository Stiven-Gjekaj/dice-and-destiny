"""Tests for render_tables. Each test builds its own table sets."""
import pytest

from render_tables import is_compact, set_errors, set_html, sets_html, table_html


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


def test_a_long_table_of_short_entries_is_compact_and_a_short_or_wordy_one_is_not():
    short = [f"Name {i}" for i in range(1, 11)]
    assert is_compact(short)
    assert not is_compact(short[:9])
    assert not is_compact(short[:9] + ["A name of more than three words"])


def test_a_compact_table_has_two_results_in_each_row_and_reads_down_each_column():
    entries = [f"N{i}" for i in range(1, 12)]
    out = table_html("d12", "Names", entries + ["N12"])
    assert "two-col" in out
    assert out.count("<tr><td") == 6
    assert '<tr><td class="c">1</td><td>N1</td><td class="c">7</td><td>N7</td></tr>' in out
    assert '<tr><td class="c">6</td><td>N6</td><td class="c">12</td><td>N12</td></tr>' in out


def test_a_compact_table_with_an_odd_count_leaves_the_last_cell_empty():
    out = table_html("d12", "Names", [f"N{i}" for i in range(1, 12)])
    assert '<td class="c">6</td><td>N6</td><td></td><td></td></tr>' in out
