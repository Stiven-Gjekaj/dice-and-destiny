# Review request: traps format and traps batch 1 (handover to GM tools)

From: the treasure session. I started this batch before the split in
`5caee92`. It is complete, and `compendium/build.sh` passes on `c2bc317`
(102 tests, the content checks, the page check, and the font check). The
batch is not committed. The full diff is at the end of this file, so the
GM tools session can apply it with `git apply`.

Please tell me one of these:

- **A.** You approve the batch. I commit it in three commits and push.
  The GM tools session continues from there.
- **B.** The GM tools session applies the diff and continues it. I do no
  more work on traps.

## The format (new)

`compendium/content/traps/*.py`: each file adds a list `TRAPS` of dicts.
`build/render_traps.py` checks each entry and stops the build on an error.

| Key | Value |
|---|---|
| `name` | Unique name. |
| `kind` | `Trap` (a creature made it) or `Hazard` (part of the place). |
| `where` | The kind of place, free text. |
| `severity` | `Setback`, `Dangerous`, or `Deadly`. |
| `summary` | One line of description (italic). |
| `trigger`, `effect`, `find`, `stop` | Rules text. `[[Label:]]` shows in bold. |
| `bands` | A list of `(first level, DC, damage)`. The first level is 1, 5, 11, or 17. The damage is dice such as `4d10`, or `""` for no damage. |

The renderer checks these rules:

- The bands are in order, each band one time.
- Each DC is from 10 to 20, and the DC does not go down in a higher band.
- The average damage is not above the Improvised Damage table in GM
  Chapter 10 for the severity and the band. For example, the limit for
  Dangerous at levels 5 to 10 is 4d10 (22).

The book shows a small table (Levels, DC, Damage) for each entry. The DC
is the save DC, and also the DC to find and to stop the entry, unless the
text gives a different DC.

## Commits (when approved)

1. `feat: add the renderer and the checks for traps and hazards`:
   `build/render_traps.py`, `tests/test_render_traps.py` (18 tests),
   `content/traps/__init__.py`, and one `REGISTRY` line in
   `check_content.py`.
2. `feat: add the traps and hazards chapter to the GM book`: a new Part
   VII "The GM's Workshop" at the end of `gm.src.html`, with Chapter 23
   "Traps & Hazards" (an intro, "Reading an Entry", "Running Traps
   Fairly", and the placeholders `{{O_TRAPS_IDX}}` and `{{O_TRAPS}}`).
   Two lines in `build.py` for the placeholders, and one line in
   `CH_ICONS`. One line in `book.css` keeps each band table in one piece.
   I added a new part at the end, so no chapter number of another session
   changes.
3. `feat: add 26 traps and hazards`: `content/traps/dungeon.py` (14
   traps) and `content/traps/wilds.py` (12 hazards).

## The entries

26 entries: 14 traps and 12 hazards. Severity: Setback 8, Dangerous 14,
Deadly 4. Levels 1 to 4: 19 entries, 5 to 10: 26, 11 to 16: 15, 17 to
20: 6. In the GM book, the part and the chapter are pages 233 to 240. I
looked at the pages: no text goes out of a box, and no band table breaks.

The strongest entries:

- Acid Sluice (Deadly): 20d10 (110) at levels 17 to 20. The limit is 24d10
  (132). Nonmagical armor also gets a permanent -1 to AC on a failed save.
- Grinding Ceiling (Deadly): 4d10, 8d10, or 12d10 **each round** until
  the creatures stop it. Each round is below the limit. Over several
  rounds, the total is above it.
- Flooding Chamber (Deadly): no damage, but it can drown a creature.
- Arrow Gallery (Dangerous): 3 rounds of damage. Each round is below the
  limit.
- Storm Ridge (Dangerous): 16d10 at levels 17 to 20. It strikes on a 1 on
  a d6 each minute.
- Thinning Veil (Dangerous): 16d10 Force and a teleport of 60 feet, at
  levels 17 to 20.

## Things that I am not sure of

1. The limit applies to one trigger or one round. Do you want a limit on
   the total for traps that repeat (Grinding Ceiling, Arrow Gallery, Storm
   Ridge)?
2. Part VII "The GM's Workshop" is at the end of the book, after "Cheat
   Sheets & Templates". A different place would change the chapter
   numbers of other sessions.
3. Some roles are common (a pit, a poison needle, a swinging blade, a
   glyph). The names, the rules, and the text are new.

## The diff

```diff
diff --git a/compendium/books/book.css b/compendium/books/book.css
index 38b1088..079ca6c 100644
--- a/compendium/books/book.css
+++ b/compendium/books/book.css
@@ -142,3 +142,5 @@ table.trinkets { font-size: 7.4pt; }
 .compendium > *, .cols2.compendium > * { break-inside: auto; }
 .compendium .entry, .compendium .mitem { break-inside: auto; }
 .compendium .sp-name, .compendium .mon-name, .compendium .ft h4 { break-after: avoid; }
+/* Traps and hazards: keep the table of level bands in one piece. */
+.trap-bands { break-inside: avoid; }
diff --git a/compendium/books/gm.src.html b/compendium/books/gm.src.html
index 8aba007..68bff9b 100644
--- a/compendium/books/gm.src.html
+++ b/compendium/books/gm.src.html
@@ -941,5 +941,30 @@
   </tbody>
 </table>
 
+{{PART:VII|The GM's Workshop|Original tools for building a world and filling it with danger: traps and hazards, and more to come.}}
+<h1 class="chapter">23 · Traps &amp; Hazards</h1>
+<p class="chapter-intro">A trap is built by someone who wants you hurt. A hazard is the world being the world. Both reward careful players, and both should feel fair when they go off.</p>
+
+<h2 data-i="eye">Reading an Entry</h2>
+<ul>
+  <li><b>Kind:</b> a <b>trap</b> is made by a creature; a <b>hazard</b> is part of the place.</li>
+  <li><b>Where:</b> the kind of place where the entry fits best. Move it anywhere it makes sense.</li>
+  <li><b>Severity:</b> <b>Setback</b>, <b>Dangerous</b> or <b>Deadly</b>, matching the Improvised Damage table in Chapter 10. The damage in an entry never goes above that table.</li>
+  <li><b>Levels, DC and Damage:</b> pick the row for the party's level. The DC is the save DC, and also the DC to find the entry and to stop it, unless the text says otherwise. An entry with no row for the party's level doesn't fit them; pick another.</li>
+  <li><b>Trigger, Effect, Find it, Stop it:</b> what sets it off, what happens, how a careful character notices it, and how they make it safe.</li>
+</ul>
+
+<h2 data-i="tip">Running Traps Fairly</h2>
+<ul>
+  <li><b>Leave a clue.</b> A scorched wall, a missing flagstone, a skeleton in an odd place. Players who look for clues should find them.</li>
+  <li><b>Let a passive check do the work.</b> Compare the DC with each character's Passive Perception before you ask for a roll.</li>
+  <li><b>Reward a plan.</b> A good idea (a 10-foot pole, a thrown sack, a rope tied to a door) can stop a trap with no roll at all.</li>
+  <li><b>Use Deadly entries rarely.</b> Put them where the story says "this place is guarded", and let the warning signs be loud.</li>
+</ul>
+
+<h2 data-i="warn">Traps &amp; Hazards by Level</h2>
+{{O_TRAPS_IDX}}
+{{O_TRAPS}}
+
 </body>
 </html>
diff --git a/compendium/build/build.py b/compendium/build/build.py
index 35bd5ab..3290f25 100644
--- a/compendium/build/build.py
+++ b/compendium/build/build.py
@@ -12,6 +12,7 @@ CH_ICONS = {
     "Treasure &amp; Magic Items": "chest", "Session Prep": "scroll", "Cheat Sheets &amp; Templates": "d20",
     "Using the Bestiary": "eye", "Monsters A–Z": "dragon", "Magic Items by Rarity": "spark",
     "Magic Items A–Z": "chest", "Poisons": "skull",
+    "Traps &amp; Hazards": "warn",
     # Player
     "Welcome to the Table": "d20", "The Six Abilities": "sheet", "Skills, Proficiency &amp; Rolling": "dice",
     "Creating a Character": "quill", "Reading a Character Sheet": "eye", "Your Turn in Combat": "swords",
@@ -148,6 +149,8 @@ def expand(name):
         "{{O_CLASSES}}": lambda: __import__("render_classes").classes_html(),
         "{{SYS_MARKS}}": lambda: __import__("render_systems").player_marks_html(),
         "{{SYS_TAINTS}}": lambda: __import__("render_systems").gm_marks_html(),
+        "{{O_TRAPS_IDX}}": lambda: __import__("render_traps").all_traps_index_html(),
+        "{{O_TRAPS}}": lambda: __import__("render_traps").all_traps_html(),
     }
     for k, f in reps.items():
         if k in s:
diff --git a/compendium/build/check_content.py b/compendium/build/check_content.py
index 0eb05a9..1212854 100644
--- a/compendium/build/check_content.py
+++ b/compendium/build/check_content.py
@@ -182,6 +182,7 @@ REGISTRY = {
     "downtime": lambda m: [],
     "classes": lambda m: [e["name"] for e in m.CLASSES],
     "systems": lambda m: [e["name"] for e in m.MARKS + m.BONDS],
+    "traps": lambda m: [e["name"] for e in m.TRAPS],
 }
 
 
diff --git a/compendium/build/render_traps.py b/compendium/build/render_traps.py
new file mode 100644
index 0000000..24345ce
--- /dev/null
+++ b/compendium/build/render_traps.py
@@ -0,0 +1,139 @@
+"""Render the original traps and hazards (content/traps) into HTML for the GM's book.
+
+Each entry is a dict with the keys in KEYS. The "bands" key holds one row for
+each level band in which the entry is used: (first level of the band, DC, damage).
+The damage of a band must not be above the improvised damage of the entry's
+severity for that band (the table in Chapter 10 of the GM's book).
+"""
+import html
+import re
+
+from monster_engine import avg
+from orig_render import feature_text
+
+E = html.escape
+
+KEYS = {"name", "kind", "where", "severity", "summary", "trigger", "effect", "find", "stop", "bands"}
+KINDS = {"Trap": "Traps", "Hazard": "Hazards"}
+SEVERITIES = ("Setback", "Dangerous", "Deadly")
+# First level of a band: (label, improvised damage for Setback, Dangerous, Deadly).
+BANDS = {
+    1: ("1–4", ("1d10", "2d10", "4d10")),
+    5: ("5–10", ("2d10", "4d10", "10d10")),
+    11: ("11–16", ("4d10", "10d10", "18d10")),
+    17: ("17–20", ("10d10", "18d10", "24d10")),
+}
+DC_RANGE = (10, 20)
+DICE = re.compile(r"^\d+d\d+(\s*\+\s*\d+)?$")
+
+
+def band_label(first):
+    return BANDS[first][0]
+
+
+def damage_cap(first, severity):
+    """The highest average damage for a band and a severity."""
+    return avg(BANDS[first][1][SEVERITIES.index(severity)])
+
+
+def trap_errors(t):
+    """Return a list of the problems of one entry. An empty list means no problem."""
+    name = t.get("name", "?")
+    errors = [f"Trap '{name}': missing key '{k}'" for k in sorted(KEYS - set(t))]
+    errors += [f"Trap '{name}': unknown key '{k}'" for k in sorted(set(t) - KEYS)]
+    if errors:
+        return errors
+    if t["kind"] not in KINDS:
+        errors.append(f"Trap '{name}': kind '{t['kind']}' is not one of {list(KINDS)}")
+    if t["severity"] not in SEVERITIES:
+        errors.append(f"Trap '{name}': severity '{t['severity']}' is not one of {list(SEVERITIES)}")
+    rows = t["bands"]
+    if not rows:
+        return errors + [f"Trap '{name}': needs at least one band"]
+    firsts = [r[0] for r in rows]
+    if any(f not in BANDS for f in firsts):
+        return errors + [f"Trap '{name}': a band must start at one of {list(BANDS)}"]
+    if firsts != sorted(set(firsts)):
+        errors.append(f"Trap '{name}': the bands must be in order, each band one time")
+    dcs = [r[1] for r in rows]
+    if any(not DC_RANGE[0] <= dc <= DC_RANGE[1] for dc in dcs):
+        errors.append(f"Trap '{name}': a DC must be from {DC_RANGE[0]} to {DC_RANGE[1]}")
+    if dcs != sorted(dcs):
+        errors.append(f"Trap '{name}': the DC must not go down in a higher band")
+    for first, _, dmg in rows:
+        if not dmg:
+            continue
+        if not DICE.match(dmg):
+            errors.append(f"Trap '{name}': damage '{dmg}' is not a dice expression such as '2d10'")
+        elif t["severity"] in SEVERITIES and avg(dmg) > damage_cap(first, t["severity"]):
+            errors.append(f"Trap '{name}': damage {dmg} for levels {band_label(first)} is above "
+                          f"{damage_cap(first, t['severity'])}, the {t['severity']} limit")
+    return errors
+
+
+def _stop_on(errors):
+    if errors:
+        raise ValueError("; ".join(errors))
+
+
+def bands_html(t):
+    """A small table with the DC and the damage for each level band."""
+    has_damage = any(r[2] for r in t["bands"])
+    head = "<th>Levels</th><th class=\"c\">DC</th>" + ('<th class="c">Damage</th>' if has_damage else "")
+    rows = []
+    for first, dc, dmg in t["bands"]:
+        cells = f'<td>{band_label(first)}</td><td class="c">{dc}</td>'
+        if has_damage:
+            cells += f'<td class="c">{E(dmg) if dmg else "None"}</td>'
+        rows.append(f"<tr>{cells}</tr>")
+    return f'<table class="compact trap-bands"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>'
+
+
+def trap_html(t):
+    """One trap or hazard."""
+    _stop_on(trap_errors(t))
+    meta = f'{t["kind"]} · {E(t["where"])} · {t["severity"]}'
+    rows = [("Trigger", t["trigger"]), ("Effect", t["effect"]), ("Find it", t["find"]), ("Stop it", t["stop"])]
+    return "\n".join([
+        f'<div class="entry trap"><h4 class="sp-name">{E(t["name"])}</h4><div class="sp-meta"><i>{meta}</i></div>',
+        f'<p><i>{feature_text(t["summary"])}</i></p>',
+        bands_html(t),
+        '<dl class="feat">' + "".join(f"<dt>{k}</dt><dd>{feature_text(v)}</dd>" for k, v in rows) + "</dl>",
+        "</div>",
+    ])
+
+
+def traps_html(traps):
+    """All entries, grouped by kind, each group in the order of the names. Return "" if there are none."""
+    _stop_on([e for t in traps for e in trap_errors(t)])
+    out = []
+    for kind, plural in KINDS.items():
+        group = sorted((t for t in traps if t["kind"] == kind), key=lambda t: t["name"])
+        if group:
+            out.append(f'<h2>{plural}</h2><div class="cols2 compendium">')
+            out += [trap_html(t) for t in group]
+            out.append("</div>")
+    return "\n".join(out)
+
+
+def traps_index_html(traps):
+    """The names of the entries for each level band. An entry shows in each band that it has."""
+    if not traps:
+        return ""
+    out = ['<div class="cols2 cr-index">']
+    for first, (label, _) in BANDS.items():
+        names = sorted(t["name"] for t in traps if first in [r[0] for r in t["bands"]])
+        out.append(f"<p><b>Levels {label}</b> <span class=muted>({len(names)})</span><br>"
+                   f"{', '.join(E(n) for n in names) or 'None yet.'}</p>")
+    out.append("</div>")
+    return "\n".join(out)
+
+
+def all_traps_html():
+    from content.traps import TRAPS
+    return traps_html(TRAPS)
+
+
+def all_traps_index_html():
+    from content.traps import TRAPS
+    return traps_index_html(TRAPS)
diff --git a/compendium/content/traps/__init__.py b/compendium/content/traps/__init__.py
new file mode 100644
index 0000000..a0e6f92
--- /dev/null
+++ b/compendium/content/traps/__init__.py
@@ -0,0 +1,7 @@
+"""Original traps and hazards. Each file adds a list TRAPS of entries.
+
+The format of an entry is in build/render_traps.py.
+"""
+from content.collect import collect_list
+
+TRAPS = collect_list(__name__, "TRAPS")
diff --git a/compendium/content/traps/dungeon.py b/compendium/content/traps/dungeon.py
new file mode 100644
index 0000000..183f619
--- /dev/null
+++ b/compendium/content/traps/dungeon.py
@@ -0,0 +1,129 @@
+# Edition 2, traps batch 1: traps that creatures build. The format is in build/render_traps.py.
+TRAPS = [
+dict(
+    name="Hinged Flagstone Pit", kind="Trap", where="Dungeon", severity="Dangerous",
+    summary="A flagstone on a greased hinge, over a shaft that someone dug with care.",
+    trigger="A creature of 50 pounds or more steps on the flagstone.",
+    effect="The flagstone swings down. The creature makes a Dexterity save against the DC. On a failed save, it falls to the bottom of the pit and takes the damage as Bludgeoning damage. At levels 5 and up, the pit is deeper and wooden stakes line the bottom. On a successful save, it catches the edge and hangs on. The flagstone swings shut 1 round later.",
+    find="A Wisdom (Perception) check against the DC spots the thin gap around the stone and the shine of grease.",
+    stop="A wedge of iron or wood driven into the gap holds the stone shut (an Intelligence check with Thieves' Tools against the DC, or no check with an iron spike and 1 minute of work).",
+    bands=[(1, 12, "2d10"), (5, 13, "4d10")],
+),
+dict(
+    name="Needle Lock", kind="Trap", where="Dungeon, vault or noble house", severity="Setback",
+    summary="A lock that bites the hand that picks it.",
+    trigger="A creature tries to pick the lock or turns a key that is not the right one.",
+    effect="A needle jabs out of the keyhole. The creature makes a Constitution save against the DC. On a failed save, it takes the damage as Poison damage and has the Poisoned condition for 1 hour. On a successful save, it takes half as much damage only.",
+    find="An Intelligence (Investigation) check against the DC finds the tiny hole beside the keyhole.",
+    stop="A Dexterity check with Thieves' Tools against the DC bends the needle out of the way. A failure by 5 or more triggers the needle.",
+    bands=[(1, 11, "1d10"), (5, 13, "2d10"), (11, 15, "4d10")],
+),
+dict(
+    name="Scything Hall Blade", kind="Trap", where="Dungeon or tomb", severity="Dangerous",
+    summary="A curved blade on a long arm, hidden in a slot in the wall.",
+    trigger="A creature walks over a pressure plate in the middle of a 10-foot-wide hall.",
+    effect="The blade sweeps across the hall at waist height. Each creature in a 10-foot-square area by the plate makes a Dexterity save against the DC. On a failed save, a creature takes the damage as Slashing damage. On a successful save, it takes half as much damage. The blade resets after 1 minute.",
+    find="A Wisdom (Perception) check against the DC spots the slot in the wall and old scratches on the stones.",
+    stop="A creature can jam the slot with a weapon or a bar (a Strength check against the DC). The weapon is destroyed if the trap triggers later. A Dexterity check with Thieves' Tools against the DC disconnects the plate.",
+    bands=[(1, 12, "2d10"), (5, 14, "4d10"), (11, 16, "9d10")],
+),
+dict(
+    name="Grinding Ceiling", kind="Trap", where="Dungeon or vault", severity="Deadly",
+    summary="A room with one exit, a fine layer of dust on the floor, and a ceiling that is lower than it looks.",
+    trigger="A creature lifts the bait (often a chest or an idol) off its stand, or the door closes behind the last creature to enter.",
+    effect="The door locks, and the stone ceiling begins to drop. At the end of each round, it drops 2 feet. After it reaches the height of a Medium creature, each creature in the room makes a Constitution save against the DC at the end of each round, taking the damage as Bludgeoning damage on a failed save or half as much on a successful one. A typical room is 10 feet high, so the saves begin in round 2.",
+    find="A Wisdom (Perception) check against the DC notices that the walls have no dust above a line, and fresh scrapes in the corners.",
+    stop="[[Wedge it:]] a strong object, such as a 10-foot pole of iron or a heavy chest, stops the ceiling for 1d4 rounds. [[Open the door:]] a Dexterity check with Thieves' Tools against the DC, or a Strength check against the DC + 2 to force it. [[The mechanism:]] behind a loose stone near the floor, an Intelligence check with Thieves' Tools against the DC stops the ceiling.",
+    bands=[(5, 15, "4d10"), (11, 17, "8d10"), (17, 18, "12d10")],
+),
+dict(
+    name="Bellows of Cinders", kind="Trap", where="Dungeon, forge or temple", severity="Dangerous",
+    summary="A pair of carved dragon heads on the walls, still warm to the touch.",
+    trigger="A creature opens the door between the heads without first turning a hidden catch.",
+    effect="Hidden bellows blow burning coal dust from the heads in a 30-foot Cone. Each creature in the Cone makes a Dexterity save against the DC, taking the damage as Fire damage on a failed save or half as much on a successful one. Flammable objects in the Cone that aren't worn or carried catch fire.",
+    find="A Wisdom (Perception) check against the DC notices black soot in the mouths of the heads. An Intelligence (Investigation) check against the DC finds the catch under the door handle.",
+    stop="Turning the catch makes the door safe. Stuffing both mouths with wet cloth or mud reduces the damage by half.",
+    bands=[(1, 12, "2d10"), (5, 14, "4d10"), (11, 16, "8d10")],
+),
+dict(
+    name="Sleep-Spore Censer", kind="Trap", where="Dungeon, temple or wizard's tower", severity="Setback",
+    summary="A brass censer on a chain, full of grey dust that smells of lavender.",
+    trigger="A creature enters the room carrying an open flame, or a guard pulls a rope.",
+    effect="The censer releases a cloud of spores that fills a 20-foot-radius Sphere for 1 minute. A creature that starts its turn in the cloud makes a Constitution save against the DC. On a failed save, it has the Poisoned condition until the end of its next turn, and while Poisoned in this way its Speed is halved and it can't take Reactions. Creatures that don't breathe are unaffected.",
+    find="A Wisdom (Perception) check against the DC notices the dust on the floor below the censer and the faint smell.",
+    stop="A creature can close the lid of the censer (no check) if it can reach it before the trigger. A strong wind, such as from the Gust of Wind spell, clears the cloud.",
+    bands=[(1, 11, ""), (5, 13, ""), (11, 15, "")],
+),
+dict(
+    name="Tripwire Bell Net", kind="Trap", where="Camp, ruin or bandit hideout", severity="Setback",
+    summary="A cheap trap that guards a camp better than a sleepy sentry does.",
+    trigger="A creature walks into a thin wire stretched at ankle height across a path.",
+    effect="A weighted net drops over a 10-foot square, and a row of bells rings loudly enough to be heard 300 feet away. Each creature under the net makes a Dexterity save against the DC or has the Restrained condition. A Restrained creature can take an action to make a Strength (Athletics) check against the DC, freeing itself on a success. The net has AC 10 and 20 Hit Points.",
+    find="A Wisdom (Perception) check against the DC spots the wire.",
+    stop="Cutting the wire while holding it taut (a Dexterity check against the DC) stops the trap. Cutting it carelessly drops the net.",
+    bands=[(1, 11, ""), (5, 13, "")],
+),
+dict(
+    name="Rune of Binding Frost", kind="Trap", where="Any guarded place", severity="Dangerous",
+    summary="A silver rune, so faint that it looks like a crack in the floor, that a spellcaster drew to guard a door or a path.",
+    trigger="A creature that doesn't speak the rune's password moves within 5 feet of it.",
+    effect="Frost bursts from the rune in a 15-foot-radius Sphere. Each creature in the Sphere makes a Constitution save against the DC. On a failed save, a creature takes the damage as Cold damage, and its Speed is 0 until the end of its next turn. On a successful save, it takes half as much damage only. The rune then fades.",
+    find="A Detect Magic spell reveals the rune. Otherwise, an Intelligence (Investigation) check against the DC finds it.",
+    stop="An Intelligence (Arcana) check against the DC lets a creature trace the rune and fade it. A failure by 5 or more triggers it. A Dispel Magic spell also ends it.",
+    bands=[(1, 13, "2d10"), (5, 14, "4d10"), (11, 16, "9d10"), (17, 18, "16d10")],
+),
+dict(
+    name="Collapsing Stair", kind="Trap", where="Dungeon or tower", severity="Dangerous",
+    summary="A long stair whose steps fold flat on a hidden lever, turning it into a slide.",
+    trigger="A guard pulls the lever at the top or bottom, or a creature steps on a false step halfway down.",
+    effect="The steps fold flat and the stair becomes a steep stone slide. Each creature on it makes a Dexterity save against the DC. On a failed save, a creature slides to the bottom, taking the damage as Bludgeoning damage, and lands Prone. On a successful save, it grabs a handhold and can climb off the slide. At the bottom there is often a pit, a cage or a waiting guard.",
+    find="A Wisdom (Perception) check against the DC notices that every step has a thin hinge line along its front edge.",
+    stop="Iron spikes driven into the hinge lines of three steps stop the stair from folding (1 minute of work). A Dexterity check with Thieves' Tools against the DC disables the lever.",
+    bands=[(1, 12, "2d10"), (5, 13, "4d10")],
+),
+dict(
+    name="Flooding Chamber", kind="Trap", where="Dungeon, sewer or sunken temple", severity="Deadly",
+    summary="A room with drains in the ceiling instead of the floor.",
+    trigger="A creature lifts the bait from a stand, or the last creature passes a pressure plate in the doorway.",
+    effect="The doors slam shut and lock, and water pours from the ceiling. The room fills in 10 rounds. When the water is deeper than a creature is tall, the creature must swim and begins to suffocate when it can no longer hold its breath. Each creature in the water makes a Strength (Athletics) check against the DC at the start of each of its turns to keep its head above the water until the room is full.",
+    find="A Wisdom (Perception) check against the DC notices the drains in the ceiling and a waterline on the walls.",
+    stop="[[Open a door:]] a Dexterity check with Thieves' Tools against the DC, or a Strength check against the DC + 2. [[Plug the drains:]] each of the four drains needs a creature to plug it with cloth or a shield, and each plugged drain adds 2 rounds to the time to fill the room.",
+    bands=[(5, 15, ""), (11, 17, "")],
+),
+dict(
+    name="Arrow Gallery", kind="Trap", where="Fortress, gatehouse or tomb", severity="Dangerous",
+    summary="A narrow hall with dozens of small holes in both walls.",
+    trigger="A creature crosses the middle of the hall without first pressing a hidden switch at the entrance.",
+    effect="Crossbows behind the walls fire at the start of each round for 3 rounds. Each creature in the 30-foot hall makes a Dexterity save against the DC, taking the damage as Piercing damage on a failed save or half as much on a successful one. A creature with total cover from both walls, such as one under an upturned table, is safe.",
+    find="A Wisdom (Perception) check against the DC notices the holes. An Intelligence (Investigation) check against the DC finds the switch.",
+    stop="Pressing the switch makes the hall safe for 1 minute. Stuffing the holes on one side (2 minutes of work) halves the damage.",
+    bands=[(1, 12, "2d6"), (5, 14, "3d10"), (11, 16, "6d10")],
+),
+dict(
+    name="Whispering Idol", kind="Trap", where="Temple or ruin", severity="Dangerous",
+    summary="A smiling statue with a jewel in its open hand and a voice that sounds like an old friend.",
+    trigger="A creature that can hear moves within 30 feet of the idol.",
+    effect="The idol speaks softly in the voice of someone the creature trusts. The creature makes a Wisdom save against the DC. On a failed save, it takes the damage as Psychic damage and has the Charmed condition for 1 minute. While Charmed in this way, it uses its movement on each of its turns to move toward the idol by the safest route, and it tries to take the jewel. A Charmed creature repeats the save at the end of each of its turns, ending the effect on itself on a success. The idol usually stands at the edge of a pit or over another trap.",
+    find="A Detect Magic spell reveals an aura of Enchantment. An Intelligence (Religion) check against the DC tells a creature that no god is shown with that smile.",
+    stop="Covering the idol's face with cloth silences it. Breaking it (AC 17, 30 Hit Points) also works. A Dispel Magic spell ends it for 24 hours.",
+    bands=[(5, 14, "3d10"), (11, 16, "8d10"), (17, 18, "14d10")],
+),
+dict(
+    name="Lodestone Floor", kind="Trap", where="Dwarven hall, mine or vault", severity="Setback",
+    summary="A floor of dark, smooth stone that tugs at belt buckles.",
+    trigger="A guard turns a crank that brings the hidden lodestones up under the floor.",
+    effect="The floor becomes strongly magnetic for 1 minute. A creature that wears metal armor and starts its turn on the floor makes a Strength save against the DC. On a failed save, its Speed is 0 until the start of its next turn. A creature holding a metal weapon makes the same save or drops it. A dropped weapon sticks to the floor until the effect ends.",
+    find="A compass or a needle behaves strangely in the room. A Wisdom (Perception) check against the DC notices the iron filings in the cracks.",
+    stop="The crank is in a guard room. A Dexterity check with Thieves' Tools against the DC jams it.",
+    bands=[(1, 12, ""), (5, 14, "")],
+),
+dict(
+    name="Acid Sluice", kind="Trap", where="Alchemist's vault or deep dungeon", severity="Deadly",
+    summary="A short hall with a smooth, scorched trough in the floor and a sharp smell.",
+    trigger="A creature opens the vault door at the end of the hall without the right key.",
+    effect="Gates at both ends of the hall slam shut, and acid floods the trough from vents in the walls. Each creature in the hall makes a Dexterity save against the DC, taking the damage as Acid damage on a failed save or half as much on a successful one. Nonmagical armor worn by a creature that fails the save takes a permanent and cumulative -1 penalty to the AC it offers. The acid drains after 1 round and the gates open.",
+    find="A Wisdom (Perception) check against the DC notices the scorch marks and the vents. A creature that tastes the air knows it at once.",
+    stop="A Dexterity check with Thieves' Tools against the DC on the vault lock opens it safely. Sealing the vents with wax or clay (1 minute) stops the acid.",
+    bands=[(5, 15, "6d10"), (11, 17, "12d10"), (17, 19, "20d10")],
+),
+]
diff --git a/compendium/content/traps/wilds.py b/compendium/content/traps/wilds.py
new file mode 100644
index 0000000..2d9700f
--- /dev/null
+++ b/compendium/content/traps/wilds.py
@@ -0,0 +1,111 @@
+# Edition 2, traps batch 1: natural hazards. The format is in build/render_traps.py.
+TRAPS = [
+dict(
+    name="Thin Ice", kind="Hazard", where="Arctic, frozen lake or river", severity="Dangerous",
+    summary="Ice that looks solid until it isn't.",
+    trigger="A creature of 100 pounds or more, or a group that weighs 300 pounds or more, moves onto a 10-foot square of thin ice.",
+    effect="The ice breaks. Each creature on the square makes a Dexterity save against the DC. On a failed save, it falls into the freezing water, takes the damage as Cold damage, and gains 1 Exhaustion level unless it has Resistance or Immunity to Cold damage. On a successful save, it moves to the nearest safe ice. Climbing out of the hole takes an action and a Strength (Athletics) check against the DC.",
+    find="A Wisdom (Survival) check against the DC tells safe ice from thin ice, by its color and the sound it makes when tapped.",
+    stop="Spreading the weight (crawling, or walking 10 feet apart) lets a group cross 10-foot squares of thin ice safely. A rope tied to someone on safe ice gives Advantage on the save and on the check to climb out.",
+    bands=[(1, 12, "1d10"), (5, 13, "2d10")],
+),
+dict(
+    name="Quickmud", kind="Hazard", where="Swamp, river delta or rainy forest", severity="Dangerous",
+    summary="A patch of wet ground that drinks a traveler slowly.",
+    trigger="A creature enters a patch of quickmud, usually 10 to 20 feet across.",
+    effect="The creature sinks 1d4 + 1 feet and has the Restrained condition. At the start of each of its turns, it sinks another 1d4 feet. While it isn't fully under the mud, it can take an action to make a Strength (Athletics) check against the DC. On a success, it pulls itself out of the mud. A creature that is fully under the mud can't breathe. Another creature can take an action to pull a creature out, with a Strength check against the DC, if it can reach it.",
+    find="A Wisdom (Survival) check against the DC notices that the surface is too smooth and that nothing grows on it.",
+    stop="Lying flat and moving slowly lets a creature cross with a Strength (Athletics) check against the DC - 5. A rope or a long pole gives Advantage on each check to get out.",
+    bands=[(1, 12, ""), (5, 14, "")],
+),
+dict(
+    name="Rockslide", kind="Hazard", where="Mountain, cliff or canyon", severity="Dangerous",
+    summary="A slope of loose stone that needs only a push to come down.",
+    trigger="A loud noise, a creature that climbs the slope, or a creature above that pushes a boulder.",
+    effect="Rocks pour down in a Line 60 feet long and 20 feet wide. Each creature in the Line makes a Dexterity save against the DC. On a failed save, a creature takes the damage as Bludgeoning damage and has the Prone condition. On a successful save, it takes half as much damage only. The area becomes Difficult Terrain.",
+    find="A Wisdom (Survival) check against the DC notices fresh scars on the slope and stones that are balanced on others.",
+    stop="A party that moves quietly and below the slope's shoulder doesn't trigger it. A careful creature can start the slide on purpose from a safe place.",
+    bands=[(1, 12, "2d10"), (5, 14, "4d10"), (11, 16, "10d10")],
+),
+dict(
+    name="Choking Bloom", kind="Hazard", where="Forest, jungle or swamp", severity="Setback",
+    summary="A meadow of pale yellow flowers that burst into clouds of pollen when touched.",
+    trigger="A creature moves through the meadow faster than half its Speed, or a fight breaks out in it.",
+    effect="A cloud of pollen fills a 20-foot-radius Sphere around the creature for 1 minute. A creature that starts its turn in the cloud makes a Constitution save against the DC. On a failed save, it has the Poisoned condition until the start of its next turn and can't speak because it is coughing. Spells with a Verbal component fail for a creature that can't speak.",
+    find="A Wisdom (Survival) or Intelligence (Nature) check against the DC identifies the flowers.",
+    stop="Moving slowly through the meadow doesn't trigger it. A wet cloth over the mouth and nose gives Advantage on the save.",
+    bands=[(1, 11, ""), (5, 13, "")],
+),
+dict(
+    name="Sun-Glass Flats", kind="Hazard", where="Desert or salt plain", severity="Dangerous",
+    summary="A plain of white salt as bright as a mirror under the midday sun.",
+    trigger="A creature travels across the flats for 1 hour in daylight.",
+    effect="The creature makes a Constitution save against the DC. On a failed save, it gains 1 Exhaustion level, and if it has no protection for its eyes it has the Blinded condition for 1 hour. Water drunk during the hour gives Advantage on the save.",
+    find="A Wisdom (Survival) check against the DC tells a creature that the flats can be crossed safely only at night or at dawn.",
+    stop="Traveling at night avoids the hazard completely. A cloth or a mask over the eyes with a thin slit prevents the Blinded condition.",
+    bands=[(1, 12, ""), (5, 14, "")],
+),
+dict(
+    name="Storm Ridge", kind="Hazard", where="Mountain or high plain", severity="Dangerous",
+    summary="A bare ridge where the hair on your arms stands up just before the lightning comes.",
+    trigger="A thunderstorm, while a creature is on the high ground of the ridge.",
+    effect="Each minute, roll a d6. On a 1, lightning strikes the tallest creature on the ridge, or the creature holding the most metal. That creature and each creature within 10 feet of it make a Dexterity save against the DC, taking the damage as Lightning damage on a failed save or half as much on a successful one.",
+    find="A Wisdom (Survival) check against the DC reads the storm early, so that the party has 10 minutes to get off the ridge before the first strike.",
+    stop="Moving off the high ground, or lying flat with no metal held high, ends the danger.",
+    bands=[(5, 14, "4d10"), (11, 16, "9d10"), (17, 18, "16d10")],
+),
+dict(
+    name="Riptide", kind="Hazard", where="Coast or river mouth", severity="Dangerous",
+    summary="A calm stretch of water between the waves where the sea runs back out.",
+    trigger="A creature swims or wades into the current.",
+    effect="The creature makes a Strength (Athletics) check against the DC. On a failure, the current pulls it 60 feet out to sea, and it gains 1 Exhaustion level from the struggle. It repeats the check at the end of each of its turns while it is in the current. A creature that swims along the shore instead of toward it has Advantage on the check.",
+    find="A Wisdom (Survival) or Wisdom (Perception) check against the DC spots the gap in the waves and the foam that moves out to sea.",
+    stop="A creature with a Swim Speed ignores the current. A rope tied to the shore lets others pull a creature back with a Strength check against the DC.",
+    bands=[(1, 12, ""), (5, 14, "")],
+),
+dict(
+    name="Firedamp Pocket", kind="Hazard", where="Mine, cave or deep tunnel", severity="Deadly",
+    summary="An invisible gas that gathers in low tunnels and waits for a spark.",
+    trigger="An open flame, a Fire spell, or a spark from steel on stone in the pocket.",
+    effect="The gas explodes in a 30-foot-radius Sphere. Each creature in the Sphere makes a Dexterity save against the DC, taking the damage as Fire damage on a failed save or half as much on a successful one. The blast can bring down part of the tunnel (see Rockslide).",
+    find="A Wisdom (Perception) check against the DC notices dead insects, a faint sweet smell, or a candle flame that turns blue. A caged bird stops singing.",
+    stop="Traveling with no open flame avoids the explosion. Opening a path for fresh air clears the gas in 1 hour.",
+    bands=[(1, 14, "4d10"), (5, 15, "8d10"), (11, 17, "14d10")],
+),
+dict(
+    name="Rotten Floorboards", kind="Hazard", where="Abandoned house, ship or mill", severity="Setback",
+    summary="Old wood that looks fine until it isn't.",
+    trigger="A creature of 100 pounds or more moves onto a rotten board.",
+    effect="The board breaks. The creature makes a Dexterity save against the DC. On a failed save, its leg goes through the floor, it takes the damage as Piercing damage from splinters, and its Speed is 0 until it takes an action to pull free. On a failed save by 5 or more, it falls through to the floor below instead and takes falling damage.",
+    find="A Wisdom (Perception) check against the DC notices dark, soft wood and a sagging line in the floor.",
+    stop="Walking close to the walls avoids the weak boards.",
+    bands=[(1, 10, "1d10"), (5, 12, "2d10")],
+),
+dict(
+    name="Whiteout", kind="Hazard", where="Arctic or high mountain", severity="Setback",
+    summary="A blizzard so thick that the ground and the sky become the same white.",
+    trigger="A blizzard, which lasts for 2d4 hours.",
+    effect="Everything more than 10 feet away is Heavily Obscured. A group that travels in the whiteout makes a Wisdom (Survival) check against the DC each hour. On a failure, it becomes lost (it travels in a random direction for that hour). A creature without cold weather gear makes a Constitution save against the DC each hour, gaining 1 Exhaustion level on a failed save.",
+    find="A Wisdom (Survival) check against the DC predicts the blizzard 1 hour before it arrives.",
+    stop="Making camp and waiting avoids getting lost. A shelter, such as a tent or a snow cave, gives Advantage on the saves.",
+    bands=[(1, 12, ""), (5, 14, ""), (11, 16, "")],
+),
+dict(
+    name="Thinning Veil", kind="Hazard", where="Ancient battlefield, ley line or ruined tower", severity="Dangerous",
+    summary="A place where the world is worn thin, and things from elsewhere press against it.",
+    trigger="A creature casts a spell of level 1 or higher in the area, or the area is under a full moon.",
+    effect="The veil tears for an instant. Each creature within 20 feet of the caster, or each creature in the area under the full moon, makes a Charisma save against the DC. On a failed save, a creature takes the damage as Force damage and is teleported to an unoccupied space the GM chooses within 60 feet. On a successful save, it takes half as much damage only.",
+    find="A Detect Magic spell shows the whole area glowing with a weak aura of Conjuration. An Intelligence (Arcana) check against the DC recognizes the signs: shadows that point the wrong way, and echoes that come back changed.",
+    stop="Casting no spells avoids the hazard on most nights. A Dispel Magic spell cast at level 5 or higher closes the thin place for 24 hours.",
+    bands=[(5, 14, "4d10"), (11, 16, "9d10"), (17, 18, "16d10")],
+),
+dict(
+    name="Falling Icicles", kind="Hazard", where="Ice cave or frozen ruin", severity="Setback",
+    summary="A ceiling of long, sharp icicles that hang like spears.",
+    trigger="A loud noise, such as a shout or a Thunder spell, or a creature that climbs on the walls.",
+    effect="Icicles fall on a 20-foot square. Each creature in it makes a Dexterity save against the DC, taking the damage as Piercing damage on a failed save or half as much on a successful one.",
+    find="A Wisdom (Perception) check against the DC notices the cracks around the icicles and the broken ice on the floor.",
+    stop="Moving quietly doesn't trigger the icicles. A creature can knock the icicles down on purpose from a safe distance.",
+    bands=[(1, 11, "1d10"), (5, 13, "2d10"), (11, 15, "4d10")],
+),
+]
diff --git a/compendium/tests/test_render_traps.py b/compendium/tests/test_render_traps.py
new file mode 100644
index 0000000..ad7e31f
--- /dev/null
+++ b/compendium/tests/test_render_traps.py
@@ -0,0 +1,108 @@
+"""Tests for render_traps. Each test builds its own entries."""
+import pytest
+
+from render_traps import damage_cap, trap_errors, trap_html, traps_html, traps_index_html
+
+
+def make_trap(**changes):
+    t = dict(
+        name="Test Trap", kind="Trap", where="Dungeon", severity="Dangerous",
+        summary="A trap for the tests.", trigger="A creature steps on it.",
+        effect="[[Hit:]] it takes the damage & falls.", find="Look down.", stop="Jam it.",
+        bands=[(1, 12, "2d10"), (5, 14, "4d10")],
+    )
+    t.update(changes)
+    return t
+
+
+def test_a_correct_trap_has_no_errors():
+    assert trap_errors(make_trap()) == []
+
+
+def test_trap_errors_find_a_missing_key_and_an_unknown_key():
+    t = make_trap(colour="red")
+    del t["stop"]
+    errors = trap_errors(t)
+    assert any("missing key 'stop'" in e for e in errors)
+    assert any("unknown key 'colour'" in e for e in errors)
+
+
+def test_trap_errors_find_an_unknown_kind_and_severity():
+    errors = trap_errors(make_trap(kind="Puzzle", severity="Mild"))
+    assert any("kind 'Puzzle'" in e for e in errors)
+    assert any("severity 'Mild'" in e for e in errors)
+
+
+@pytest.mark.parametrize("bands", [[], [(2, 12, "1d10")], [(5, 12, "1d10"), (1, 12, "1d10")],
+                                   [(1, 12, "1d10"), (1, 12, "1d10")]])
+def test_trap_errors_find_bad_bands(bands):
+    assert trap_errors(make_trap(bands=bands))
+
+
+@pytest.mark.parametrize("dc", [9, 21])
+def test_trap_errors_find_a_dc_out_of_range(dc):
+    assert any("DC must be from" in e for e in trap_errors(make_trap(bands=[(1, dc, "1d10")])))
+
+
+def test_trap_errors_find_a_dc_that_goes_down():
+    assert any("go down" in e for e in trap_errors(make_trap(bands=[(1, 15, "1d10"), (5, 13, "2d10")])))
+
+
+def test_damage_cap_follows_the_improvised_damage_table():
+    assert damage_cap(1, "Setback") == 5
+    assert damage_cap(5, "Dangerous") == 22
+    assert damage_cap(17, "Deadly") == 132
+
+
+def test_damage_at_the_cap_is_correct_and_above_the_cap_is_an_error():
+    assert trap_errors(make_trap(severity="Setback", bands=[(1, 10, "1d10")])) == []
+    errors = trap_errors(make_trap(severity="Setback", bands=[(1, 10, "2d6")]))
+    assert any("above 5, the Setback limit" in e for e in errors)
+
+
+def test_a_flat_bonus_counts_toward_the_cap():
+    assert trap_errors(make_trap(severity="Setback", bands=[(1, 10, "1d8 + 1")])) == []
+    assert trap_errors(make_trap(severity="Setback", bands=[(1, 10, "1d8 + 2")]))
+
+
+def test_trap_errors_find_damage_that_is_not_dice():
+    assert any("not a dice expression" in e for e in trap_errors(make_trap(bands=[(1, 12, "lots")])))
+
+
+def test_a_hazard_with_no_damage_shows_no_damage_column():
+    out = trap_html(make_trap(kind="Hazard", bands=[(1, 12, ""), (5, 15, "")]))
+    assert "Damage" not in out
+    assert out.count("<tr>") == 3
+
+
+def test_a_band_with_no_damage_shows_none_when_others_have_damage():
+    out = trap_html(make_trap(bands=[(1, 12, ""), (5, 14, "4d10")]))
+    assert ">None</td>" in out
+
+
+def test_trap_html_escapes_the_text_and_bolds_labels():
+    out = trap_html(make_trap(name="A & B"))
+    assert "A &amp; B" in out
+    assert "<b>Hit:</b> it takes the damage &amp; falls." in out
+    assert "<dt>Find it</dt>" in out and "<dt>Stop it</dt>" in out
+
+
+def test_trap_html_stops_on_an_error():
+    with pytest.raises(ValueError, match="severity"):
+        trap_html(make_trap(severity="Mild"))
+
+
+def test_traps_html_groups_by_kind_and_sorts_by_name():
+    out = traps_html([make_trap(name="Zed"), make_trap(name="Alpha"), make_trap(name="Fog", kind="Hazard")])
+    assert out.index("<h2>Traps</h2>") < out.index("Alpha") < out.index("Zed") < out.index("<h2>Hazards</h2>") < out.index("Fog")
+
+
+def test_traps_html_is_empty_with_no_entries():
+    assert traps_html([]) == ""
+    assert traps_index_html([]) == ""
+
+
+def test_traps_index_lists_an_entry_in_each_of_its_bands():
+    out = traps_index_html([make_trap(name="Pit", bands=[(1, 12, "1d10"), (11, 15, "4d10")])])
+    assert out.count("Pit") == 2
+    assert "None yet." in out
```
