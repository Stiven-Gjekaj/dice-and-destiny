"""Optional rules systems. Each file adds lists of entries.

MARKS is a list of Mark entries. A Mark entry is a dict with these keys:
  name: the name of the Mark
  kind: "Blessing", "Curse", or "Taint"
  hidden: True if the GM tracks the Mark in secret by default
  summary: one or two sentences that tell what the Mark is
  benefit: the benefit before the crisis, or "" (a Curse can have no benefit)
  cost: the cost that the character pays while the Mark stays
  grows: what makes the track grow
  thresholds: a list of (track value from 1 to 4, what changes at that value)
  give_in: the full power after the crisis, and the moments that the GM steers
  scar: the small permanent trace when the character breaks free
  ends: how the Mark ends before the crisis
  ends_after: how the Mark ends after the character gives in (a higher price)
  secret: the hidden part of the price, or "". Only a Taint can have one.
  blocks_bonds: True if the Mark blocks the bond die and the damage reduction

BONDS is a list of Bond kinds. A Bond entry is a dict with these keys:
  name: the name of the kind, for example "Friend"
  summary: one or two sentences that tell what the Bond is
  special: (name, text) of the special use of the kind
  strain: what strains a Bond of this kind
  example: a short example of play

TECHNIQUES is a list of Technique entries. A Technique entry is a dict with these keys:
  name: the name of the technique
  type: "Stance", "Maneuver", or "Shaping"
  cost: the technique points that it costs, from 1 to 3
  level: the lowest character level to learn it (1, 5, 11, or 17)
  timing: when you use it, for example "Bonus Action" or "Reaction"
  text: what it does

LEGENDS is a list of Legend path entries. A Legend entry is a dict with these keys:
  name: the name of the path, for example "Dragonslayer"
  summary: one or two sentences that tell what the path is
  deeds: the deeds that give legend points on this path
  fall: what makes the character lose legend points on this path
  tiers: a list of 5 (title, benefit), one for each tier from I to V

In all text, [[label]] shows the label in bold.
"""
from content.collect import collect_list

MARKS = collect_list(__name__, "MARKS")
BONDS = collect_list(__name__, "BONDS")
TECHNIQUES = collect_list(__name__, "TECHNIQUES")
LEGENDS = collect_list(__name__, "LEGENDS")
