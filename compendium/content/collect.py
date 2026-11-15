"""Collect the entries of all modules in a content package.

A new file in a content folder is found with no other change.
The modules are read in the order of their file names.
"""
import importlib
import pkgutil


def _modules(package):
    pkg = importlib.import_module(package)
    names = sorted(m.name for m in pkgutil.iter_modules(pkg.__path__) if not m.ispkg)
    return [importlib.import_module(f"{package}.{n}") for n in names]


def collect_list(package, attr):
    """Join the list `attr` of each module in `package`."""
    out = []
    for mod in _modules(package):
        out.extend(getattr(mod, attr, []))
    return out


def collect_dict_of_lists(package, attr):
    """Join the dict `attr` of each module. Lists under the same key are joined, not replaced."""
    out = {}
    for mod in _modules(package):
        for key, items in getattr(mod, attr, {}).items():
            out.setdefault(key, []).extend(items)
    return out
