"""Downtime activities and the stronghold system.

STRONGHOLDS is the HTML of the stronghold system.
Each other file adds a list DOWNTIME of downtime activities.
"""
from content.collect import collect_list
from content.downtime.strongholds import STRONGHOLDS

DOWNTIME = collect_list(__name__, "DOWNTIME")
