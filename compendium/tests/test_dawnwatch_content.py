"""Tests for the content package of The Dawnwatch.

Each test writes its own content files into a temporary folder or into
content/dawnwatch, and removes them at the end.
"""
import hashlib
import importlib
import os
import sys

import pytest

import check_content
from content.collect import collect_list

DW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "dawnwatch")

CREATURE = '''from monster_engine import M
MON = [M("Zzyx Test Lurker", "M", "Monstrosity", "Unaligned", 1, "14 12 13 3 10 5",
         attacks=[("Bite", "m", "1d8", "Piercing")])]
'''
PERSON = '''from monster_engine import M
NPCS = [("A test smith", M("Zzyx Test Smith", "M", "Humanoid", "Neutral", 0.5, "14 10 12 10 10 10",
                            attacks=[("Hammer", "m", "1d6", "Bludgeoning")])),
        ("A test child", "Zzyx Test Child")]
'''
TREASURE = '''ITEMS = [("Zzyx Test Lamp", "Wondrous Item", "Rare", None, "A lamp for the test.")]
'''
FILES = {"creatures_zzyx.py": CREATURE, "people_zzyx.py": PERSON, "treasures_zzyx.py": TREASURE}


def _forget():
    """Drop the loaded content and build modules, so the next import reads the files again."""
    for key in [k for k in sys.modules if k == "content" or k.startswith("content.")
                or k in ("orig_render", "build", "classes", "compendium", "cover")
                or k.startswith("render_")]:
        del sys.modules[key]
    importlib.invalidate_caches()


@pytest.fixture
def dawnwatch_files():
    made = []
    for name, body in FILES.items():
        path = os.path.join(DW, name)
        assert not os.path.exists(path)
        with open(path, "w") as f:
            f.write(body)
        made.append(path)
    _forget()
    yield
    for path in made:
        os.remove(path)
    _forget()


def _books():
    import build
    return {n: hashlib.sha256(build.expand(n).encode()).hexdigest() for n in ("player", "gm")}


def _cover_counts():
    import cover
    return cover.content_counts()


def test_the_package_collects_each_list_from_its_own_files(dawnwatch_files):
    import content.dawnwatch as dw
    # The real content of the book is also in the package. Look only at the entries of the test files.
    assert [m.name for m in dw.MON if m.name.startswith("Zzyx")] == ["Zzyx Test Lurker"]
    assert [e[0] for e in dw.NPCS if e[0].startswith("A test")] == ["A test smith", "A test child"]
    assert [i[0] for i in dw.ITEMS if i[0].startswith("Zzyx")] == ["Zzyx Test Lamp"]


def test_the_compendiums_do_not_change_when_dawnwatch_content_exists():
    _forget()
    before, counts = _books(), _cover_counts()
    for name, body in FILES.items():
        with open(os.path.join(DW, name), "w") as f:
            f.write(body)
    try:
        _forget()
        import content.dawnwatch as dw
        assert dw.MON and dw.NPCS and dw.ITEMS  # the files are really there and loaded
        after, counts_after = _books(), _cover_counts()
    finally:
        for name in FILES:
            os.remove(os.path.join(DW, name))
        _forget()
    assert after == before
    assert counts_after == counts


def test_the_compendium_packages_do_not_list_dawnwatch_content(dawnwatch_files):
    from content.items import ITEMS
    from content.monsters import MON
    from content.npcs import NPCS
    names = {m.name for m in MON} | {e[1].name for e in NPCS} | {i[0] for i in ITEMS}
    assert not any(n.startswith("Zzyx") for n in names)


def test_the_content_check_reads_the_dawnwatch_package(dawnwatch_files):
    assert check_content.check_all_content() == []
    import content.dawnwatch as dw
    names = check_content.REGISTRY["dawnwatch"](dw)
    assert {"Zzyx Test Lurker", "Zzyx Test Smith", "Zzyx Test Child", "Zzyx Test Lamp"} <= set(names)


def test_a_campaign_name_that_is_also_a_compendium_name_is_an_error():
    assert check_content.campaign_clashes(["Ghoul", "New Thing"], ["ghoul ", "Old Thing"]) == [
        "dawnwatch: 'Ghoul' is also the name of a Compendium entry"]


def test_a_prefix_reads_only_the_matching_files(tmp_path, monkeypatch):
    pkg = tmp_path / "zzyxpkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("")
    (pkg / "creatures_a.py").write_text("MON = [1]\n")
    (pkg / "people_a.py").write_text("MON = [2]\n")
    monkeypatch.syspath_prepend(str(tmp_path))
    importlib.invalidate_caches()
    try:
        assert collect_list("zzyxpkg", "MON", "creatures_") == [1]
        assert collect_list("zzyxpkg", "MON") == [1, 2]
    finally:
        for key in [k for k in sys.modules if k.startswith("zzyxpkg")]:
            del sys.modules[key]
