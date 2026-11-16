"""Tests for render_pantheons. Each test builds its own pantheons."""
import pytest

from render_pantheons import domains_text, full_name, god_errors, pantheon_errors, pantheon_html, pantheons_html

DOMAINS = {"Life Domain", "Test Domain"}


def make_god(**changes):
    g = dict(name="Testa", title="the Tester", portfolio="Tests & checks", alignment="Neutral",
             symbol="A [[red]] tick", domains=["Test Domain"], wants="Green builds.", worshippers="Coders.")
    g.update(changes)
    return g


def make_pantheon(**changes):
    p = dict(name="The Test Court", summary="Gods for the tests.", gods=[make_god(), make_god(name="Other", title="")])
    p.update(changes)
    return p


def test_a_correct_pantheon_has_no_errors():
    assert pantheon_errors(make_pantheon(), DOMAINS) == []


def test_errors_find_missing_and_unknown_keys_of_a_god_and_a_pantheon():
    g = make_god(colour="red")
    del g["symbol"]
    p = make_pantheon(gods=[g], era="old")
    del p["summary"]
    assert any("missing key 'summary'" in e for e in pantheon_errors(p, DOMAINS))
    assert any("unknown key 'era'" in e for e in pantheon_errors(p, DOMAINS))
    errors = god_errors(g, DOMAINS)
    assert any("missing key 'symbol'" in e for e in errors)
    assert any("unknown key 'colour'" in e for e in errors)


@pytest.mark.parametrize("changes", [
    {"alignment": "Good"},
    {"domains": ["War Domain"]},
    {"domains": ["Life Domain", "Life Domain"]},
])
def test_god_errors_find_bad_values(changes):
    assert god_errors(make_god(**changes), DOMAINS)


def test_a_pantheon_needs_a_god():
    assert pantheon_errors(make_pantheon(gods=[]), DOMAINS)


def test_names_and_domains_read_well():
    assert full_name(make_god()) == "Testa, the Tester"
    assert full_name(make_god(title="")) == "Testa"
    assert domains_text(make_god(domains=["Life Domain", "Test Domain"])) == "Life, Test"
    assert domains_text(make_god(domains=[])) == "Any"


def test_pantheon_html_has_a_row_and_an_entry_for_each_god_and_escapes_text():
    out = pantheon_html(make_pantheon(), DOMAINS)
    assert out.count('<div class="entry god">') == 2
    assert out.count("<tr><td><b>") == 2
    assert "Tests &amp; checks" in out
    assert "A <b>red</b> tick" in out


def test_pantheons_html_stops_on_a_bad_god_and_is_empty_with_none():
    with pytest.raises(ValueError):
        pantheons_html([make_pantheon(gods=[make_god(alignment="Good")])], DOMAINS)
    assert pantheons_html([], DOMAINS) == ""
