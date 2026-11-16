"""Downtime activities and the stronghold system.

STRONGHOLDS is the HTML of the stronghold system.
Each other file adds a list DOWNTIME of downtime activities.

A DOWNTIME entry is a dict with these keys:
  name: the name of the activity
  summary: one or two sentences that tell what the character does
  time: how long it takes, in workweeks of 5 days
  cost: what it costs, and the tools that it needs
  check: the ability check at the end, and what changes it
  results: a list of 2 to 6 (check total, result), from the lowest total to the highest
  complications: a list of 6 complications, for a d6

In all text, [[label]] shows the label in bold.
"""
from content.collect import collect_list
from content.downtime.strongholds import STRONGHOLDS

DOWNTIME = collect_list(__name__, "DOWNTIME")
