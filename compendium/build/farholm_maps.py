"""The maps of Beyond the Western Sea.

The final maps are SVG files in compendium/maps/western-sea/<id>.svg. This module does not
draw a preview. With no final file, map_svg raises KeyError, and the book shows a placeholder.
"""
import os

import maps

MAP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "maps", "western-sea")
MAP_IDS = ["farholm", "colony-town"]


def map_file(map_id):
    """The path of the final map of map_id. The file can be missing."""
    return os.path.join(MAP_DIR, f"{map_id}.svg")


def missing_maps(ids=None):
    """The map ids with no final map in compendium/maps/western-sea/."""
    return [i for i in (MAP_IDS if ids is None else ids) if not os.path.exists(map_file(i))]


def map_svg(map_id, size=None):
    """Return the SVG of the final map of map_id as a string.

    size is "page", "half", or None. The final map has its own size, so size only must be known.
    Raise KeyError for an unknown id or for a map with no final file.
    """
    if map_id not in MAP_IDS:
        raise KeyError(f"unknown map {map_id!r}; the maps are {', '.join(MAP_IDS)}")
    if size is not None and size not in maps.SIZES:
        raise ValueError(f"unknown map size {size!r}")
    path = map_file(map_id)
    if not os.path.exists(path):
        raise KeyError(f"the map {map_id!r} has no final file")
    with open(path, encoding="utf-8") as f:
        return maps.scope_ids(maps.check_print(f.read(), path), map_id)
