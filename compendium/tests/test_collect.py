"""Tests for content.collect. Each test makes its own package in a temporary folder."""
import importlib
import sys

import pytest

from content.collect import collect_dict_of_lists, collect_list


@pytest.fixture
def make_pkg(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(tmp_path))
    made = []

    def make(name, files):
        pkg = tmp_path / name
        pkg.mkdir(exist_ok=True)
        (pkg / "__init__.py").write_text("")
        for fname, body in files.items():
            (pkg / fname).write_text(body)
        made.append(name)
        importlib.invalidate_caches()
        return name

    yield make
    for name in made:
        for key in [k for k in sys.modules if k == name or k.startswith(name + ".")]:
            del sys.modules[key]


def test_collect_list_joins_files_in_name_order(make_pkg):
    pkg = make_pkg("pkg_order", {"b.py": "X = [3]\n", "a.py": "X = [1, 2]\n"})
    assert collect_list(pkg, "X") == [1, 2, 3]


def test_collect_list_skips_module_without_attr(make_pkg):
    pkg = make_pkg("pkg_skip", {"a.py": "X = [1]\n", "b.py": "Y = [2]\n"})
    assert collect_list(pkg, "X") == [1]


def test_collect_dict_of_lists_extends_same_key(make_pkg):
    pkg = make_pkg("pkg_dict", {"a.py": 'S = {"bard": [1]}\n', "b.py": 'S = {"bard": [2], "monk": [3]}\n'})
    assert collect_dict_of_lists(pkg, "S") == {"bard": [1, 2], "monk": [3]}


def test_new_file_is_found_without_other_change(make_pkg, tmp_path):
    pkg = make_pkg("pkg_new", {"a.py": "X = [1]\n"})
    assert collect_list(pkg, "X") == [1]
    (tmp_path / pkg / "c.py").write_text("X = [9]\n")
    importlib.invalidate_caches()
    assert 9 in collect_list(pkg, "X")
