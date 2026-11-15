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
