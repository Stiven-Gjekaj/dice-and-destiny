"""Tests for the general book engine in campaign.py.

Each test makes its own book in a temporary folder and its own content
in a small module. No test reads the book text that the writers edit.
"""
import dataclasses
import os
import types

import pytest

import build as B
import campaign


def stub_content():
    mod = types.ModuleType("stub_content")
    mod.MON, mod.NPCS, mod.ITEMS, mod.PLACES = [], [], [], []
    return mod


def one_chapter_book(tmp_path, **kw):
    book = tmp_path / "book"
    (book / "chapters").mkdir(parents=True)
    text = "# x\n\nThe x marks the spot.\n"
    (book / "chapters" / "01-x.md").write_text(text)
    mod = stub_content()
    fields = dict(
        name="box", book=str(book), content=lambda: mod,
        front=dict(title="The Box", sub_title="Book Six: Wax", sub="Six boxes.", compat="A test book."),
        css="box.css",
        parts=dict(run="Run text.", story="Story text.", world="World text.", reference="Reference text."),
        chapters=lambda b: [(1, "ch1", text)] if os.path.isdir(b) else [],
    )
    fields.update(kw)
    return campaign.Campaign(**fields)


@pytest.fixture(autouse=True)
def clean():
    B.TOC.clear()
    campaign.WARNINGS.clear()
    campaign.ANCHOR_MARK.clear()
    campaign.IDX.clear()
    yield


def front_of(h):
    return h[:h.index("{{TOC}}")]


def test_post_filter_runs_on_the_body(tmp_path):
    plain = one_chapter_book(tmp_path)
    filtered = dataclasses.replace(plain, post=lambda h: h.replace("x", "y"))
    before, _ = campaign.expand(plain)
    after, _ = campaign.expand(filtered)
    assert "The x marks the spot." in before
    assert "The y marks the spot." in after and "The x marks the spot." not in after
    assert "y" in after
    assert front_of(after) == front_of(before)
    assert "The Box<br>Book Six: Wax" in front_of(after)


def test_the_campaign_fields_go_into_the_page(tmp_path):
    c = one_chapter_book(tmp_path)
    h, _ = campaign.expand(c, screen=True)
    assert '<link rel="stylesheet" href="box.css">' in h and "screen.css" in h
    assert "<title>The Box, Book Six: Wax</title>" in h
    assert "{{PART:II|The Adventure|Story text.}}" not in h  # the parts become HTML
    assert "Story text." in h and "Reference text." in h and "Run text." not in h
    hp, _ = campaign.expand(c, inside_mm=20)
    assert "bw.css" in hp and "margin-left: 20mm" in hp


def test_the_extra_forms_and_the_index_terms_come_from_the_campaign(tmp_path):
    c = one_chapter_book(tmp_path, index_terms=[("The Spot", ["spot"])])
    _, es = campaign.expand(c)
    assert [e["name"] for e in es if e["kind"] == "term"] == ["The Spot"]
    assert [n for n, _, _ in campaign.IDX] == ["The Spot"]
    es = [dict(kind="treasure", name="The Lamp", anchor="t-the-lamp", obj=None)]
    campaign.IDX.clear()
    campaign.mark_mentions("<p>A lamp and the Lamp.</p>", es, extra_forms={"The Lamp": ["lamp"]})
    assert [n for n, _, _ in campaign.IDX] == ["The Lamp", "The Lamp"]
