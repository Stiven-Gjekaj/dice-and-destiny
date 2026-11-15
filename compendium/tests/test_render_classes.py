"""Tests for render_classes. Each test builds its own class entry."""
import pytest

from render_classes import class_html, level_table, prof


def make_class(**changes):
    c = dict(
        key="tester", name="Tester", tagline="A class for the tests.", role="Test role",
        difficulty="Easy", icon="flag", primary="Intelligence", hit_die=8,
        saves="Wisdom and Intelligence", skills="Choose 2: History or Insight",
        weapons="Simple weapons", tools="None", armor="Light armor", equipment="50 GP",
        subclass_levels=[3, 6],
        columns=[("Points", list(range(1, 21)))],
        features=[(1, "First Trick", "Pick one: [[Up:]] go up. [[Down:]] go down."),
                  (3, "Tester Subclass", "Choose a subclass.")],
        guide=dict(play="Play & win.", build="Intelligence 15."),
    )
    c.update(changes)
    return c


def test_prof_follows_the_srd_steps():
    assert [prof(lv) for lv in (1, 4, 5, 9, 13, 17, 20)] == ["+2", "+2", "+3", "+4", "+5", "+6", "+6"]


def test_level_table_puts_each_feature_on_its_level():
    rows = level_table(make_class())
    assert len(rows) == 20
    assert rows[0] == ["First Trick"]
    assert rows[2] == ["Tester Subclass"]
    assert rows[5] == ["Subclass feature"]
    assert rows[19] == []


def test_class_html_has_twenty_rows_and_the_column_values():
    out = class_html(make_class())
    body = out.split("<tbody>")[1].split("</tbody>")[0]
    assert body.count("<tr>") == 20
    assert '<td class="c">20</td></tr>' in body


def test_class_html_escapes_text_and_shows_bold_labels():
    out = class_html(make_class())
    assert "Play &amp; win." in out
    assert "<b>Up:</b> go up." in out


def test_class_html_lists_the_subclasses_only_when_given():
    assert "Subclasses in this book" not in class_html(make_class())
    assert "Alpha, Beta" in class_html(make_class(), ["Alpha", "Beta"])


def test_class_html_needs_a_known_icon():
    with pytest.raises(KeyError):
        class_html(make_class(icon="no-such-icon"))


def test_class_html_starts_a_new_page_only_when_asked():
    assert 'class="class-banner newpage"' in class_html(make_class())
    assert 'class="class-banner"' in class_html(make_class(), newpage=False)
