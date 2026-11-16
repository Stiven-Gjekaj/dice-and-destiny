"""The Injuries and scars optional system. Each file adds a list INJURIES.

An injury entry is a dict with these keys:
  name: the name of the injury
  roll: the result on the d20 Injury table, from 1 to 20. Each result is used one time.
  severity: "Minor" (roll 1 to 10), "Serious" (11 to 17), or "Lasting" (18 to 20)
  effect: what the injury does while it stays
  treatment: how the injury heals, with rest and care or with magic
  scar: (name, benefit) of the scar that the injury leaves when it heals without magic

In all text, [[label]] shows the label in bold.
"""
from content.collect import collect_list

INJURIES = collect_list(__name__, "INJURIES")
