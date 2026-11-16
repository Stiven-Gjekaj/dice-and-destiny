"""Tests for the Markdown renderer of The Dawnwatch. Each test builds its own small text."""
import waking_md as wm


def test_a_plain_block_quote_is_read_aloud():
    h = wm.render("> The road bends, and you see the river.\n", {})
    assert '<blockquote class="read-aloud">' in h
    assert "gm-box" not in h


def test_each_label_makes_its_own_gm_box():
    cases = {"GM tip": "gm-tip", "Teach": "gm-teach", "Thread (the Shadow)": "gm-thread", "Scaling": "gm-scaling",
             "Secret (chapter 7)": "gm-secret"}
    for label, cls in cases.items():
        h = wm.render(f"> **{label}:** Some text.\n", {})
        assert f'<blockquote class="gm-box {cls}">' in h, label
        assert "read-aloud" not in h


def test_a_bold_word_that_is_not_a_label_stays_read_aloud():
    h = wm.render("> **Run!** the guard shouts.\n", {})
    assert '<blockquote class="read-aloud">' in h


def test_two_quotes_get_their_own_classes():
    h = wm.render("> You see a door.\n\nText.\n\n> **Teach: Doors.** Open it.\n", {})
    assert h.index("read-aloud") < h.index("gm-teach")


def test_a_directive_calls_its_handler_with_the_argument():
    calls = []

    def sb(arg):
        calls.append(arg)
        return f'<div class="sb">{arg}</div>'
    h = wm.render("Before.\n{{statblock: Giant Rat}}\nAfter.\n", {"statblock": sb})
    assert calls == ["Giant Rat"]
    assert '<div class="sb">Giant Rat</div>' in h
    assert "<p><div" not in h
    assert h.index("Before.") < h.index('class="sb"') < h.index("After.")


def test_all_four_directive_kinds_are_found_with_spaces():
    text = "{{statblock: A}}\n{{ treasure : B b }}\n{{map:act1}}\n  {{handout: 03-letter}}  \n"
    assert wm.directives(text) == [("statblock", "A"), ("treasure", "B b"), ("map", "act1"), ("handout", "03-letter")]


def test_a_directive_inside_a_sentence_is_not_a_directive():
    assert wm.directives("Use {{map: x}} here.\n") == []


def test_a_kind_with_no_handler_stays_as_text():
    h = wm.render("{{map: world}}\n", {})
    assert "{{map: world}}" in h


def test_a_link_to_a_markdown_file_keeps_only_its_text():
    h = wm.render("See the [statblocks](../../statblocks.md#giant-rat) and [site](https://example.org).\n", {})
    assert "statblocks.md" not in h and ">statblocks<" not in h and "the statblocks" in h
    assert 'href="https://example.org"' in h


def test_headings_get_ids_with_the_prefix_and_no_repeats():
    h = wm.render("## Scene 1: The Hall\n\n### Rewards\n\n## Rewards\n", {}, prefix="ch2")
    assert 'id="ch2-scene-1-the-hall"' in h
    assert 'id="ch2-rewards"' in h and 'id="ch2-rewards-2"' in h


def test_a_table_becomes_html():
    assert "<table>" in wm.render("| A | B |\n|---|---|\n| 1 | 2 |\n", {})


def test_demote_moves_each_heading_down():
    assert wm.demote("# A\n## B\ntext #1\n") == "## A\n### B\ntext #1\n"


def test_title_and_drop_title():
    text = "Intro\n# The Title\nBody\n# Second\n"
    assert wm.title_of(text) == "The Title"
    assert wm.drop_title(text) == "Intro\nBody\n# Second\n"
    assert wm.title_of("no heading", "x") == "x"


def test_drop_section_removes_only_that_section():
    text = "## Keep\na\n## Files\n- one\n- two\n## Also\nb\n"
    assert wm.drop_section(text, "Files") == "## Keep\na\n## Also\nb\n"
    assert wm.drop_section("## Files\nlast\n", "Files") == ""


def test_slug():
    assert wm.slug("Brannock's Ford") == "brannocks-ford"
    assert wm.slug("<b>Saint</b> Ivo&#39;s") == "saint-ivos"


def test_the_word_secret_with_no_chapter_is_not_a_secret_box():
    assert '<blockquote class="read-aloud">' in wm.render("> **Secret** door!\n", {})


def test_struck_out_text_in_both_forms():
    for line in ("> ~~The chapel of the keep.~~ Done.\n", "> <del>The chapel of the keep.</del> Done.\n"):
        h = wm.render(line, {})
        assert "<del>The chapel of the keep.</del> Done." in h and "~~" not in h, line


def test_a_single_tilde_stays():
    assert "about ~5 miles" in wm.render("about ~5 miles\n", {})
