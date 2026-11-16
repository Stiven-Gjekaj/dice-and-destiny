"""Tests for the build of The Dawnwatch, Book One: Waking.

Each test makes its own sources in a temporary folder and its own content
in a small namespace. No test reads the book text that the writers edit.
"""
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


def test_a_map_uses_maps_py_when_it_exists(monkeypatch):
    fake = types.ModuleType("maps")
    fake.map_html = lambda map_id, screen=False: f"<svg data-id='{map_id}' data-screen='{screen}'></svg>"
    monkeypatch.setitem(sys.modules, "maps", fake)
    monkeypatch.setattr(W.importlib.util, "find_spec", lambda name: object())
    h = W.map_html("act1", screen=True)
    assert "data-id='act1'" in h and "data-screen='True'" in h and h.startswith('<figure class="map"')


def test_a_map_id_that_maps_py_does_not_know_is_a_placeholder(monkeypatch):
    fake = types.ModuleType("maps")

    def unknown(map_id):
        raise KeyError(map_id)
    fake.map_html = unknown
    monkeypatch.setitem(sys.modules, "maps", fake)
    monkeypatch.setattr(W.importlib.util, "find_spec", lambda name: object())
    assert 'class="map-placeholder"' in W.map_html("nowhere")
    assert W.WARNINGS == ["map not drawn: nowhere"]


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
    assert [W.place_text(p) for p in ("Ash", ("Kell", "A shrine."), {"name": "Gaunt", "desc": "A state."}, ("X", 3))] == [
        "", "A shrine.", "A state.", ""]


def test_the_appendices_list_each_entry_with_its_chapters():
    d = dw(mon=[creature("Zzyx Lurker")], npcs=[("A ferryman", "Old Bren"), ("A smith", person("Zzyx Smith"))],
           places=[("Brannock's Ford", "A village.")])
    h = W.appendices_html(d, CHS)
    assert [t[1] for t in B.TOC] == ["Appendix A: Creatures", "Appendix B: People", "Appendix C: Places"]
    assert 'id="c-zzyx-lurker"' in h and 'id="p-old-bren"' in h and 'id="l-brannocks-ford"' in h
    assert "A ferryman" in h and "A village." in h
    bren = h[h.index('id="p-old-bren"'):h.index('id="p-zzyx-smith"')]
    assert '<div class="named-in">Chapters 1, 3</div>' in bren and 'class="monster"' not in bren
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
