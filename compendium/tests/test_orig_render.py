"""Tests for the subclass feature text in orig_render."""
from orig_render import feature_text


def test_feature_text_without_marker_is_only_escaped():
    assert feature_text("Deal 2d6 <Fire> damage & push it.") == "Deal 2d6 &lt;Fire&gt; damage &amp; push it."


def test_feature_text_shows_each_label_in_bold():
    text = "Choose one: [[Smoke:]] it hides you. [[Flash (Cost: 1d6):]] it blinds a creature."
    assert feature_text(text) == (
        "Choose one: <b>Smoke:</b> it hides you. <b>Flash (Cost: 1d6):</b> it blinds a creature."
    )


def test_feature_text_escapes_the_label():
    assert feature_text("[[A & B:]] text") == "<b>A &amp; B:</b> text"


def test_feature_text_keeps_single_brackets():
    assert feature_text("[a] and [[b]") == "[a] and [[b]"


def test_subclass_order_adds_new_classes_that_have_subclasses():
    from orig_render import ORDER, subclass_order
    subs = {"barbarian": [], "captain": [("A", "", [])]}
    assert subclass_order(subs, ["captain", "shaper"]) == ORDER + ["captain"]


def test_subclass_order_is_the_srd_order_without_new_classes():
    from orig_render import ORDER, subclass_order
    assert subclass_order({"bard": []}, []) == ORDER


def test_species_are_in_alphabetical_order(monkeypatch):
    import content.species
    from orig_render import species_html
    monkeypatch.setattr(content.species, "SPECIES", [
        ("Zeta", "Medium", "30 feet", "z", []),
        ("Alpha", "Small", "30 feet", "a", []),
    ])
    html = species_html()
    assert html.index("<h3>Alpha</h3>") < html.index("<h3>Zeta</h3>")


def test_backgrounds_are_in_alphabetical_order(monkeypatch):
    import content.backgrounds
    from orig_render import backgrounds_html
    monkeypatch.setattr(content.backgrounds, "BACKGROUNDS", [
        ("Zeta", "Str", "Athletics", "none", "Hardy", "rope", "z"),
        ("Alpha", "Dex", "Stealth", "none", "Hardy", "rope", "a"),
    ])
    html = backgrounds_html()
    assert html.index("<h4>Alpha</h4>") < html.index("<h4>Zeta</h4>")
