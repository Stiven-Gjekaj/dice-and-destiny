"""Tests for render_systems. Each test builds its own entries."""
import pytest

from render_systems import (bond_errors, bond_html, bonds_html, mark_errors, mark_html,
                            marks_html, track_html)


def make_mark(**changes):
    m = dict(
        name="Test Mark", kind="Taint", hidden=True, summary="A mark for the tests.",
        benefit="You gain [[Edge:]] a bonus.", cost="You lose & suffer.", grows="When you use it.",
        thresholds=[(1, "First change."), (3, "Second change.")],
        give_in="Full power.", scar="A small trace.", ends="A quest.", ends_after="A harder quest.",
        secret="The GM knows this.", blocks_bonds=False,
    )
    m.update(changes)
    return m


def make_bond(**changes):
    b = dict(name="Friend", summary="Two friends.", special=("Shield", "Take the hit."),
             strain="Leave the friend.", example="Ana takes the hit.")
    b.update(changes)
    return b


def test_a_correct_mark_has_no_errors():
    assert mark_errors(make_mark()) == []


def test_mark_errors_find_a_missing_key_and_an_unknown_key():
    m = make_mark(colour="red")
    del m["scar"]
    errors = mark_errors(m)
    assert any("missing key 'scar'" in e for e in errors)
    assert any("unknown key 'colour'" in e for e in errors)


def test_mark_errors_find_an_unknown_kind():
    assert any("kind 'Boon'" in e for e in mark_errors(make_mark(kind="Boon")))


def test_only_a_curse_can_have_no_benefit():
    assert mark_errors(make_mark(kind="Curse", secret="", benefit="")) == []
    assert any("no benefit" in e for e in mark_errors(make_mark(benefit="")))


def test_only_a_taint_can_have_a_secret():
    assert any("secret" in e for e in mark_errors(make_mark(kind="Blessing")))
    assert mark_errors(make_mark(kind="Blessing", secret="")) == []


@pytest.mark.parametrize("values", [[], [0], [5], [3, 1], [2, 2]])
def test_mark_errors_find_bad_thresholds(values):
    assert mark_errors(make_mark(thresholds=[(v, "x") for v in values]))


def test_track_has_six_cells_and_bold_thresholds():
    out = track_html(make_mark())
    assert out.count("<td") == 6
    assert '<td class="c"><b>1</b></td>' in out
    assert '<td class="c">2</td>' in out
    assert '<td class="c"><b>3</b></td>' in out
    assert "<b>5 Crisis</b>" in out


def test_mark_html_escapes_text_and_shows_bold_labels():
    out = mark_html(make_mark())
    assert "You lose &amp; suffer." in out
    assert "<b>Edge:</b> a bonus." in out


def test_mark_html_shows_the_secret_only_in_the_gm_book():
    assert "The GM knows this." not in mark_html(make_mark())
    assert "The GM knows this." in mark_html(make_mark(), gm=True)


def test_mark_html_shows_none_for_a_curse_with_no_benefit():
    out = mark_html(make_mark(kind="Curse", secret="", benefit=""))
    assert "<dt>Benefit</dt><dd>None.</dd>" in out


def test_mark_html_tells_visibility_and_bond_block():
    out = mark_html(make_mark(kind="Curse", hidden=False, secret="", blocks_bonds=True))
    assert "Curse · open by default · blocks bond help" in out
    assert "hidden by default" in mark_html(make_mark())


def test_mark_html_stops_on_a_bad_mark():
    with pytest.raises(ValueError):
        mark_html(make_mark(kind="Boon"))


def test_marks_html_puts_each_kind_in_its_book_in_name_order():
    marks = [make_mark(name="Zeal", kind="Blessing", secret=""),
             make_mark(name="Awe", kind="Blessing", secret=""),
             make_mark(name="Bane", kind="Curse", secret=""),
             make_mark(name="Rot", kind="Taint")]
    player = marks_html(marks, "player")
    assert player.index("<h2>Blessings</h2>") < player.index("Awe") < player.index("Zeal")
    assert player.index("Zeal") < player.index("<h2>Curses</h2>") < player.index("Bane")
    assert "Rot" not in player and "Taints" not in player
    gm = marks_html(marks, "gm")
    assert "<h2>Taints</h2>" in gm and "Rot" in gm and "Awe" not in gm


def test_marks_html_is_empty_when_the_book_has_no_marks():
    assert marks_html([], "player") == ""
    assert marks_html([make_mark()], "player") == ""


def test_marks_html_stops_on_a_bad_mark_of_the_other_book():
    with pytest.raises(ValueError):
        marks_html([make_mark(benefit="")], "player")


def test_bond_errors():
    assert bond_errors(make_bond()) == []
    assert bond_errors(make_bond(special=("Only a name",)))
    b = make_bond()
    del b["strain"]
    assert any("missing key 'strain'" in e for e in bond_errors(b))


def test_bond_html_shows_the_special_the_strain_and_the_example():
    out = bond_html(make_bond())
    assert "<dt>Special: Shield</dt><dd>Take the hit.</dd>" in out
    assert "Leave the friend." in out
    assert '<div class="example"><p>Ana takes the hit.</p></div>' in out


def test_bonds_html_keeps_the_order_and_is_empty_with_no_bonds():
    assert bonds_html([]) == ""
    out = bonds_html([make_bond(name="Rival"), make_bond(name="Debt")])
    assert out.index("Rival") < out.index("Debt")


def test_entries_do_not_use_the_class_of_the_page_markers():
    # The build hides each element with the class "mark" (the page markers of the contents).
    import re
    out = mark_html(make_mark(), gm=True) + bond_html(make_bond())
    classes = [c for attr in re.findall(r'class="([^"]*)"', out) for c in attr.split()]
    assert "mark" not in classes
