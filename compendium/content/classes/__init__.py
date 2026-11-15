"""Original classes. Each file adds a list CLASSES of class entries.

A class entry is a dict with these keys:
  key, name, tagline, role, difficulty, icon: short text
  primary, saves, skills, weapons, tools, armor, equipment: text for the traits box
  hit_die: the number of sides of the Hit Die, for example 10
  subclass_levels: the levels that give a subclass feature, for example [3, 7, 11, 15]
  columns: a list of (heading, [20 values, one for each level])
  features: a list of (level, name, text). In the text, [[label]] shows the label in bold.
  guide: a dict with "play" and "build" text
  lists (optional): a list of (title, [(name, text), ...]). Each list shows as
    its own block after the features, for example the options of a feature.

The subclasses of a class go in content/subclasses under the key of the class.
"""
from content.collect import collect_list

CLASSES = collect_list(__name__, "CLASSES")
CLASS_KEYS = [c["key"] for c in CLASSES]
