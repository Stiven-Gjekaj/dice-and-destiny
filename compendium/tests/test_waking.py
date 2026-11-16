"""Tests for the build of The Dawnwatch, Book One: Waking.

Each test makes its own sources in a temporary folder and its own content
in a small namespace. No test reads the book text that the writers edit.
"""
import re
import sys
import types

import pytest

import build as B
import waking as W
from monster_engine import M


def creature(name, cr=1):
    return M(name, "M", "Monstrosity", "Unaligned", cr, "14 12 13 3 10 5", attacks=[("Bite", "m", "1d8", "Piercing")])


def person(name):
    return M(name, "M", "Humanoid", "Neutral", 0.5, "14 10 12 10 10 10", attacks=[("Club", "m", "1d6", "Bludgeoning")])


def dw(mon=(), npcs=(), items=(), places=()):
    return types.SimpleNamespace(MON=list(mon), NPCS=list(npcs), ITEMS=list(items), PLACES=list(places))


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


@pytest.fixture
def tutorial(tmp_path):
    root = tmp_path / "tutorial"
    write(root / "README.md", "# The Tutorial\n\nOverview text.\n\n## Premise\n\nA king.\n\n## Files\n\n- [Statblocks](statblocks.md): the rats.\n")
    write(root / "sessions/01-the-last-watch/README.md",
          "# Session 1: The Last Watch\n\nRead it first.\n\n- [Statblocks](../../statblocks.md)\n\n## Scene 1: The Hall\n\n> You wake.\n")
    write(root / "statblocks.md", "# Statblocks\n\n## Giant Rat\n\nA rat.\n")
    write(root / "pregens.md", "# Pregenerated characters\n\n## 1. The Shield\n\n### Numbers\n")
    write(root / "cheat-sheet.md", "# Player cheat sheet\n\n## The one rule\n")
    return root


@pytest.fixture(autouse=True)
def clean():
    B.TOC.clear()
    W.WARNINGS.clear()
    W.ANCHOR_MARK.clear()
    W.IDX.clear()
    yield


# ------------------------------------------------------------------ sources

def test_chapter_one_is_the_tutorial_in_one_text(tutorial):
    t = W.tutorial_text(str(tutorial))
    assert t.startswith("# The Last Watch\n")
    assert t.count("\n# ") == 0  # the other files move down one level
    assert "## Premise" in t and "## Scene 1: The Hall" in t
    assert "## Statblocks" in t and "### Giant Rat" in t and "#### Numbers" in t and "## Player cheat sheet" in t
    assert "## Files" not in t and "statblocks.md" not in t
    assert "# Session 1" not in t
    assert t.index("Premise") < t.index("Scene 1") < t.index("Giant Rat") < t.index("The Shield") < t.index("The one rule")


def test_the_chapters_come_in_order_with_the_number_of_the_file(tmp_path, tutorial):
    book = tmp_path / "book"
    write(book / "chapters/03-saint-ivos.md", "# Saint Ivo's\n")
    write(book / "chapters/02-brannocks-ford.md", "# Brannock's Ford\n")
    write(book / "chapters/01-old.md", "# Not the tutorial\n")
    write(book / "chapters/notes.md", "# Not a chapter\n")
    chs = W.chapters(str(book), str(tutorial))
    assert [(n, k) for n, k, _ in chs] == [(1, "ch1"), (2, "ch2"), (3, "ch3")]
    assert chs[0][2].startswith("# The Last Watch")


def test_with_no_tutorial_folder_there_is_no_chapter_one(tmp_path):
    book = tmp_path / "book"
    write(book / "chapters/02-a.md", "# A\n")
    assert [n for n, _, _ in W.chapters(str(book), str(tmp_path / "none"))] == [2]


def test_handouts_have_their_ids_and_titles(tmp_path):
    book = tmp_path / "book"
    write(book / "handouts/02-map.md", "# The Old Map\n")
    write(book / "handouts/01-letter.md", "No heading here.\n")
    assert [(i, t) for i, t, _ in W.handouts(str(book))] == [("01-letter", "01-letter"), ("02-map", "The Old Map")]


# ------------------------------------------------------------------ directives

def test_a_statblock_comes_from_the_dawnwatch_content_first():
    h = W.statblock_html("zzyx lurker", dw(mon=[creature("Zzyx Lurker")]))
    assert "Zzyx Lurker" in h and 'class="inline-stat"' in h and not W.WARNINGS


def test_a_statblock_of_a_person_with_a_statblock():
    h = W.statblock_html("Zzyx Smith", dw(npcs=[("A smith", person("Zzyx Smith")), ("A child", "Zzyx Child")]))
    assert "Zzyx Smith" in h
    W.statblock_html("Zzyx Child", dw(npcs=[("A child", "Zzyx Child")]))
    assert W.WARNINGS == ["statblock not found: Zzyx Child"]


def test_a_statblock_can_come_from_the_compendiums():
    from content.monsters import MON
    assert MON[0].name in W.statblock_html(MON[0].name, dw())
    assert "Giant Rat" in W.statblock_html("Giant Rat", dw())
    assert not W.WARNINGS


def test_an_unknown_statblock_shows_a_note_and_a_warning():
    h = W.statblock_html("Nobody At All", dw())
    assert 'class="missing"' in h and W.WARNINGS == ["statblock not found: Nobody At All"]


def test_a_treasure_from_each_source():
    from content.items import ITEMS
    d = dw(items=[("Zzyx Lamp", "Wondrous Item", "Rare", "requires attunement", "A lamp.")])
    h = W.treasure_html("Zzyx Lamp", d)
    assert "Zzyx Lamp" in h and "Wondrous Item, Rare (requires attunement)" in h
    assert ITEMS[0][0] in W.treasure_html(ITEMS[0][0], d)
    assert "Bag of Holding" in W.treasure_html("Bag of Holding", d)
    assert not W.WARNINGS
    W.treasure_html("No Such Thing", d)
    assert W.WARNINGS == ["treasure not found: No Such Thing"]


def fake_maps(monkeypatch, ids, final=()):
    fake = types.ModuleType("maps")
    fake.MAP_IDS = list(ids)

    def map_svg(map_id):
        if map_id not in ids:
            raise KeyError(map_id)
        return f"<svg data-id='{map_id}'></svg>"
    fake.map_svg = map_svg
    fake.missing_maps = lambda only=None: [i for i in (only or ids) if i not in final]
    monkeypatch.setitem(sys.modules, "maps", fake)
    monkeypatch.setattr(W.importlib.util, "find_spec", lambda name: object())


def test_a_map_uses_maps_py_when_it_exists(monkeypatch):
    fake_maps(monkeypatch, ["act-1"])
    h = W.map_html(" act-1")
    assert "data-id='act-1'" in h and h.startswith('<figure class="map" id="map-act-1">') and not W.WARNINGS


def test_a_map_id_that_maps_py_does_not_know_is_a_placeholder(monkeypatch):
    fake_maps(monkeypatch, ["act-1"])
    assert 'class="map-placeholder"' in W.map_html("nowhere")
    assert W.WARNINGS == ["map not drawn: nowhere"]


def test_missing_maps_lists_the_maps_with_no_final_file_and_unknown_ids(monkeypatch, tmp_path):
    book = tmp_path / "book"
    write(book / "chapters/02-a.md", "# A\n\n{{map: act-1}}\n\n{{map: old-map}}\n")
    write(book / "gazetteer.md", "# G\n\n{{map: land-today}}\n")
    fake_maps(monkeypatch, ["act-1", "land-today", "act-2"], final=["act-1", "land-today"])
    monkeypatch.setattr(W, "TUTORIAL", str(tmp_path / "none"))
    assert W.missing_maps(str(book)) == ["act-2", "old-map"]


def test_with_no_maps_py_a_map_is_a_placeholder(monkeypatch):
    monkeypatch.setattr(W.importlib.util, "find_spec", lambda name: None)
    assert "Map: world" in W.map_html("world")


def test_a_handout_reference_has_a_page_placeholder():
    h = W.handout_ref_html("03-letter", {"03-letter": "A Letter"})
    assert "A Letter" in h and "@@PAGE:handout-03-letter@@" in h and "<a " not in h
    assert 'href="#handout-03-letter"' in W.handout_ref_html("03-letter", {"03-letter": "A Letter"}, screen=True)
    W.handout_ref_html("99-none", {})
    assert W.WARNINGS == ["handout not found: 99-none"]


# ------------------------------------------------------------------ sections

def test_a_chapter_gets_its_number_and_a_toc_entry():
    h = W.section_html("# Chapter 2: Brannock's Ford\n\n## Scene\n\n# A Second Head\n", {}, "ch2", num=2)
    assert 'class="ch-num">Chapter 2</div>' in h and ">Brannock's Ford</h1>" in h
    assert 'id="ch2"' in h and h.count('class="ch-num"') == 1
    assert [t[1] for t in B.TOC] == ["2. Brannock's Ford", "A Second Head"]
    assert W.ANCHOR_MARK == {"ch2": B.TOC[0][2]}


def test_the_book_order_and_the_parts(tmp_path, tutorial):
    book = tmp_path / "book"
    write(book / "how-to-run.md", "# How to Run This Book\n")
    write(book / "players-guide.md", "# The Player's Guide\n")
    write(book / "gazetteer.md", "# The Gazetteer\n")
    write(book / "chapters/02-a.md", "# Brannock's Ford\n")
    write(book / "handouts/01-map.md", "# The Map\n")
    out, _, _ = W.body_parts(dw(mon=[creature("Zzyx Lurker")]), str(book), str(tutorial))
    s = "".join(out)
    order = ["titlepage", "{{TOC}}", "{{PART:I|", "How to Run This Book", "The Player's Guide", "{{PART:II|",
             "The Last Watch", "Brannock's Ford", "{{PART:III|", "The Gazetteer", "{{PART:IV|",
             "Appendix A: Creatures", "Handouts", "The Map", ">Index<", "{{INDEX}}"]
    pos = [s.index(x) for x in order]
    assert pos == sorted(pos)


def test_a_missing_source_leaves_out_its_part(tmp_path):
    out, _, _ = W.body_parts(dw(), str(tmp_path / "book"), str(tmp_path / "none"))
    s = "".join(out)
    assert "{{TOC}}" in s and "{{INDEX}}" in s
    assert "{{PART:I|" not in s and "{{PART:II|" not in s and "{{PART:III|" not in s
    assert "{{PART:IV|" in s and "Appendix" not in s and "Handouts" not in s


# ------------------------------------------------------------------ appendices

CHS = [(1, "ch1", "The Zzyx Lurker hides. Old Bren waits at Brannock's Ford."),
       (2, "ch2", "Brannock's Fordham is a different place. Zzyx Lurkers swarm."),
       (3, "ch3", "Old Bren's Lamp glows. Old Bren smiles.")]


def test_named_in_finds_whole_names_only():
    assert W.named_in("Brannock's Ford", CHS) == [1]
    assert W.named_in("Zzyx Lurker", CHS) == [1]
    assert W.named_in("Old Bren", CHS) == [1, 3]
    assert W.named_in("Nobody", CHS) == []


def test_a_longer_name_wins_in_the_pattern():
    pat = W.mention_pattern(["Old Bren", "Old Bren's Lamp"])
    assert pat.findall(CHS[2][2]) == ["Old Bren's Lamp", "Old Bren"]
    assert W.mention_pattern([]) is None


def test_entries_are_a_to_z_in_each_kind_and_a_shared_name_keeps_one_kind():
    d = dw(mon=[creature("Zzyx B"), creature("Zzyx A")], npcs=[("A guard", "Bren"), ("A cook", person("Zzyx A"))],
           items=[("Lamp", "Wondrous Item", "Rare", None, "x")], places=[{"name": "Kell", "text": "A shrine."}, "Ash"])
    es = W.entries(d)
    assert [(e["kind"], e["name"]) for e in es] == [
        ("creature", "Zzyx A"), ("creature", "Zzyx B"), ("person", "Bren"), ("treasure", "Lamp"),
        ("place", "Ash"), ("place", "Kell")]
    assert es[0]["anchor"] == "c-zzyx-a" and es[-1]["anchor"] == "l-kell"


def test_the_place_formats():
    assert [W.place_name(p) for p in ("Ash", ("Kell", "A shrine."), {"name": "Gaunt"})] == ["Ash", "Kell", "Gaunt"]
    assert [W.place_text(p) for p in ("Ash", ("Kell", "A shrine."), {"name": "Gaunt", "desc": "A state."}, ("X", 3),
                                      {"name": "Kell", "summary": "An old shrine."})] == [
        "", "A shrine.", "A state.", "", "An old shrine."]


def test_the_appendices_list_each_entry_with_its_chapters():
    d = dw(mon=[creature("Zzyx Lurker")], npcs=[("A ferryman", "Old Bren"), ("A smith", person("Zzyx Smith"))],
           places=[("Brannock's Ford", "A village.")])
    h = W.appendices_html(d, CHS)
    assert [t[1] for t in B.TOC] == ["Appendix A: Creatures", "Appendix B: People", "Appendix C: Places"]
    assert 'id="c-zzyx-lurker"' in h and 'id="p-old-bren"' in h and 'id="l-brannocks-ford"' in h
    assert "A ferryman" in h and "A village." in h
    bren = h[h.index('id="p-old-bren"'):h.index('id="p-zzyx-smith"')]
    assert '<div class="named-in">Named in chapters 1 and 3</div>' in bren and 'class="monster"' not in bren
    smith = h[h.index('id="p-zzyx-smith"'):]
    assert 'class="monster"' in smith and "named-in" not in smith.split("</div></div>")[0]
    assert [(n, main) for n, _, main in W.IDX] == [("Zzyx Lurker", True), ("Old Bren", True), ("Zzyx Smith", True), ("Brannock's Ford", True)]


def test_with_no_content_there_are_no_appendices():
    assert W.appendices_html(dw(), CHS) == "" and B.TOC == []


def test_each_handout_starts_a_right_hand_chunk_with_its_marker():
    h = W.handouts_html([("01-map", "The Map", "# The Map\n\nA map."), ("02-note", "A Note", "# A Note\n")], {})
    chunks = h.split("<!--PARTSTART-->")
    assert len(chunks) == 3 and 'id="handout-01-map"' in chunks[1] and 'id="handout-02-note"' in chunks[2]
    assert W.ANCHOR_MARK["handout-01-map"] in chunks[1] and W.ANCHOR_MARK["handout-02-note"] in chunks[2]
    assert W.handouts_html([], {}) == ""


# ------------------------------------------------------------------ index

ES = [dict(kind="person", name="Old Bren", anchor="p-old-bren", obj=None),
      dict(kind="place", name="Kell", anchor="l-kell", obj=None)]


def test_a_mention_in_the_text_gets_a_marker():
    h = W.mark_mentions("<p>Old Bren goes to Kell. Kelly stays.</p>", ES)
    assert h.count('<span class="mark">@@I') == 2
    assert "Kelly stays" in h
    assert [n for n, _, _ in W.IDX] == ["Old Bren", "Kell"]


def test_headings_links_markers_and_svg_keep_their_text():
    src = ('<h2>Old Bren</h2><p><a href="#x">Kell</a> <span class="mark">Kell</span> <svg><text>Kell</text></svg> '
           '<span class="other">Kell</span></p>')
    h = W.mark_mentions(src, ES)
    assert len(W.IDX) == 1  # only the plain span
    assert h.startswith("<h2>Old Bren</h2>")


def test_on_the_screen_a_mention_links_to_its_entry():
    h = W.mark_mentions("<p>Old Bren</p>", ES, screen=True)
    assert '<a class="xref" href="#p-old-bren">Old Bren</a><span class="mark">@@I0@@</span>' in h


def test_a_name_with_an_ampersand_matches_the_escaped_text():
    es = [dict(kind="place", name="Salt & Ash", anchor="l-salt-ash", obj=None)]
    assert len(W.IDX) == 0
    W.mark_mentions("<p>At Salt &amp; Ash.</p>", es)
    assert [n for n, _, _ in W.IDX] == ["Salt & Ash"]


def test_the_index_lists_each_name_with_its_pages_and_the_entry_page_in_bold():
    W.IDX[:] = [("Old Bren", "@@I0@@", True), ("Old Bren", "@@I1@@", False), ("Old Bren", "@@I2@@", False),
                ("Kell", "@@I3@@", False)]
    pages = {"@@I0@@": 40, "@@I1@@": 7, "@@I2@@": 7, "@@I3@@": 12}
    h = W.index_html(pages, ES)
    assert '<p>Kell <span class="pg">12</span></p>' in h
    assert '<p>Old Bren <span class="pg">7, <b>40</b></span></p>' in h
    assert h.index("Kell") < h.index("Old Bren")
    assert '<a href="#p-old-bren">Old Bren</a>' in W.index_html(pages, ES, screen=True)


def test_fill_puts_in_the_contents_the_index_and_the_page_references():
    B.TOC[:] = [("ch", "Handouts", "@@T0@@")]
    W.ANCHOR_MARK["handout-01-map"] = "@@T0@@"
    body = "{{TOC}}|page @@PAGE:handout-01-map@@ and @@PAGE:handout-99@@|{{INDEX}}"
    s = W.fill(body, {"@@T0@@": 9}, ES)
    assert "page 9 and ?" in s and "{{TOC}}" not in s and "{{INDEX}}" not in s
    assert '<span class="p">9</span>' in s and 'class="index"' in s


def test_recto_marks_and_blank_pages():
    body = "a @@T0@@ <!--PARTSTART-->x @@T1@@ @@T2@@<!--PARTSTART-->y @@T3@@"
    assert W.recto_marks(body) == ["@@T1@@", "@@T3@@"]
    s = W.insert_blanks(body, {1})
    assert s.count('class="blankpage"') == 1 and s.index("blankpage") < s.index("y @@T3@@") and s.index("@@T2@@") < s.index("blankpage")


def fake_press(base):
    """A fake render: the page of a marker is its base page plus one page for each blank page before it."""
    seen = {}

    def render(out, s):
        seen["s"] = s

    def find(out):
        s = seen["s"]
        return {mk: p + s[:s.index(mk)].count('class="blankpage"') for mk, p in base.items() if mk in s}
    return render, find, seen


def test_the_passes_put_each_recto_chunk_on_a_right_hand_page():
    B.TOC[:] = [("ch", "One", "@@T0@@"), ("part", "Two", "@@T1@@"), ("sub", "Three", "@@T2@@")]
    body = ('{{TOC}}<span class="mark" id="t0">@@T0@@</span><!--PARTSTART--><span class="mark" id="t1">@@T1@@</span>'
            '<!--PARTSTART--><span class="mark" id="t2">@@T2@@</span>{{INDEX}}')
    render, find, seen = fake_press({"@@T0@@": 1, "@@T1@@": 2, "@@T2@@": 3})
    pages, toc = W.passes("x", body, [], render=render, find=find)
    assert pages == {"@@T0@@": 1, "@@T1@@": 3, "@@T2@@": 5}
    assert seen["s"].count('class="blankpage"') == 2
    assert "@@T1@@" in seen["s"] and W.HIDE_MARKS in seen["s"]  # the last render hides the markers
    assert [t[2] for t in toc] == ["@@T0@@", "@@T1@@", "@@T2@@"]


def test_on_the_screen_the_passes_add_no_blank_pages():
    B.TOC[:] = [("part", "Two", "@@T1@@")]
    body = '{{TOC}}<!--PARTSTART--><span class="mark" id="t1">@@T1@@</span>'
    render, find, seen = fake_press({"@@T1@@": 2})
    pages, _ = W.passes("x", body, [], screen=True, render=render, find=find)
    assert pages == {"@@T1@@": 2} and "blankpage" not in seen["s"]


def test_expand_makes_one_page_of_html_with_links_on_the_screen(tmp_path, tutorial):
    book = tmp_path / "book"
    write(book / "chapters/02-ford.md", "# The Ford\n\nOld Bren waits at Kell — alone.\n\n{{handout: 01-map}}\n")
    write(book / "handouts/01-map.md", "# The Map\n")
    d = dw(npcs=[("A ferryman", "Old Bren")], places=["Kell"])
    h, es = W.expand(screen=True, book=str(book), tutorial=str(tutorial), dw=d)
    assert h.startswith("<!DOCTYPE html>") and "waking.css" in h and "screen.css" in h
    assert '<a class="xref" href="#p-old-bren">Old Bren</a>' in h
    assert "—" not in h
    assert "{{TOC}}" in h and "{{INDEX}}" in h and "@@PAGE:handout-01-map@@" in h
    assert {e["name"] for e in es} == {"Old Bren", "Kell"}
    labels = [t[1] for t in B.TOC]
    assert labels.index("1. The Last Watch") < labels.index("2. The Ford") < labels.index("Index")
    hp, _ = W.expand(screen=False, inside_mm=25, book=str(book), tutorial=str(tutorial), dw=d)
    assert "bw.css" in hp and "margin-left: 25mm" in hp and 'class="xref"' not in hp


def test_the_passes_stop_if_the_last_render_has_another_page_count():
    B.TOC[:] = [("ch", "One", "@@T0@@")]
    body = '{{TOC}}<span class="mark" id="t0">@@T0@@</span>'
    render, find, seen = fake_press({"@@T0@@": 1})
    count = lambda out: 11 if W.HIDE_MARKS in seen["s"] else 10
    with pytest.raises(SystemExit, match="11 pages, not 10"):
        W.passes("x", body, [], render=render, find=find, count=count)


def test_the_marker_of_a_handout_is_in_the_box_with_the_page_break():
    h = W.handouts_html([("01-map", "The Map", "# The Map\n\nA map.")], {})
    assert '<div class="handout-top" id="handout-01-map"><span class="mark" id="t1">@@T1@@</span></div>' in h


def test_a_marker_on_two_pages_belongs_to_the_last_one():
    assert W.marks_in_pages(["a @@T1@@ @@I2@@", "@@T1@@ b", "@@I3@@"]) == {"@@T1@@": 2, "@@I2@@": 1, "@@I3@@": 3}


def test_the_chapters_line_reads_as_a_sentence():
    assert W.chapters_line([]) == ""
    assert ">Named in chapter 9<" in W.chapters_line([9])
    assert ">Named in chapters 2 and 3<" in W.chapters_line([2, 3])
    assert ">Named in chapters 2, 3, 5, and 9<" in W.chapters_line([2, 3, 5, 9])


def test_an_authored_chapter_sentence_goes_out_when_the_build_shows_the_chapters():
    assert W.without_chapters('A pedlar who sells bones. Chapters 2 and 3.') == "A pedlar who sells bones."
    assert W.without_chapters("A priest. Chapters 3, 4, and 9.") == "A priest."
    assert W.without_chapters("The ferry woman. Chapter 2.") == "The ferry woman."
    assert W.without_chapters("The keep of Chapter House Ward.") == "The keep of Chapter House Ward."
    d = dw(npcs=[("A ferryman. Chapters 1 and 3.", "Old Bren"), ("A ghost. Chapter 8.", "Zzyx Nobody")],
           places=[{"name": "Kell", "summary": "A shrine. Chapter 4."}])
    h = W.appendices_html(d, CHS + [(4, "ch4", "Kell is far.")])
    assert ">A ferryman.</div>" in h and "Chapters 1 and 3." not in h
    assert ">A ghost. Chapter 8.</div>" in h  # no chapter names it, so the authored sentence stays
    assert "<p>A shrine.</p>" in h and "Named in chapter 4" in h


def test_hide_marks_puts_the_rule_into_the_head():
    assert W.hide_marks("<head><title>x</title></head><body>@@T0@@</body>") == (
        "<head><title>x</title>" + W.HIDE_MARKS + "</head><body>@@T0@@</body>")
    assert W.hide_marks("<p>x</p>").startswith(W.HIDE_MARKS)


def test_a_name_with_the_also_matches_a_lowercase_the():
    chs = [(10, "ch10", "They lift the Fennick Candle."), (11, "ch11", "Other text. Then the end.")]
    assert W.named_in("The Fennick Candle", chs) == [10]
    es = [dict(kind="treasure", name="The Fennick Candle", anchor="t-the-fennick-candle", obj=None)]
    h = W.mark_mentions("<p>They lift the Fennick Candle. The Fennick Candle glows.</p>", es, screen=True)
    assert [n for n, _, _ in W.IDX] == ["The Fennick Candle", "The Fennick Candle"]
    assert '<a class="xref" href="#t-the-fennick-candle">the Fennick Candle</a>' in h
    assert W.mention_pattern(["The Wolds"]).search("THE Wolds") is None


def test_names_sort_without_the_first_article():
    assert sorted(["The Black Stone", "Ash", "The Corrin", "Brannock", "A Ledger"], key=W.sort_key) == [
        "Ash", "The Black Stone", "Brannock", "The Corrin", "A Ledger"]
    assert W.letter_of("The Black Stone") == "B" and W.letter_of("Theo") == "T" and W.letter_of("The") == "T"
    d = dw(items=[("The Black Stone", "Wondrous Item", "Rare", None, "x"), ("Candle", "Wondrous Item", "Rare", None, "y"),
                  ("Amulet", "Wondrous Item", "Rare", None, "z")])
    h = W.appendices_html(d, [])
    letters = re.findall(r'<div class="letter">(\w)</div>', h)
    assert letters == ["A", "B", "C"]
    es = W.entries(d)
    assert [e["name"] for e in es] == ["Amulet", "The Black Stone", "Candle"]
    ih = W.index_html({}, es)
    assert re.findall(r'<div class="letter">(\w)</div>', ih) == ["A", "B", "C"]
