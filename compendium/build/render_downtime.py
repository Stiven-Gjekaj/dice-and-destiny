"""Render the downtime activities (content/downtime, the list DOWNTIME) into HTML for the Game Master's Compendium.

An activity has a time, a cost, one ability check, a table of results by the total of the
check, and a d6 table of complications.
"""
import html

from orig_render import feature_text

E = html.escape

ACTIVITY_KEYS = {"name", "summary", "time", "cost", "check", "results", "complications"}
COMPLICATIONS = 6
RESULTS = (2, 6)


def activity_errors(a):
    """Return a list of the problems of one activity. An empty list means no problem."""
    name = a.get("name", "?")
    errors = [f"Downtime '{name}': missing key '{k}'" for k in sorted(ACTIVITY_KEYS - set(a))]
    errors += [f"Downtime '{name}': unknown key '{k}'" for k in sorted(set(a) - ACTIVITY_KEYS)]
    if errors:
        return errors
    if not RESULTS[0] <= len(a["results"]) <= RESULTS[1]:
        errors.append(f"Downtime '{name}': needs {RESULTS[0]} to {RESULTS[1]} results")
    if any(len(r) != 2 for r in a["results"]):
        errors.append(f"Downtime '{name}': each result must be (check total, text)")
    if len(a["complications"]) != COMPLICATIONS:
        errors.append(f"Downtime '{name}': needs {COMPLICATIONS} complications for a d6")
    if len(set(a["complications"])) != len(a["complications"]):
        errors.append(f"Downtime '{name}': has the same complication two times")
    return errors


def _stop_on(errors):
    if errors:
        raise ValueError("; ".join(errors))


def activity_html(a):
    """One activity: the summary, the time, the cost, the check, the results, and the complications."""
    _stop_on(activity_errors(a))
    results = "".join(f'<tr><td class="c">{E(total)}</td><td>{feature_text(text)}</td></tr>' for total, text in a["results"])
    comps = "".join(f'<tr><td class="c">{i}</td><td>{feature_text(c)}</td></tr>' for i, c in enumerate(a["complications"], 1))
    return (f'<div class="entry downtime"><h4 class="sp-name">{E(a["name"])}</h4>'
            f'<p><i>{feature_text(a["summary"])}</i></p><dl class="feat">'
            f'<dt>Time</dt><dd>{feature_text(a["time"])}</dd>'
            f'<dt>Cost</dt><dd>{feature_text(a["cost"])}</dd>'
            f'<dt>Check</dt><dd>{feature_text(a["check"])}</dd></dl>'
            f'<table class="compact downtime-table"><thead><tr><th class="c">Total</th><th>Result</th></tr></thead>'
            f'<tbody>{results}</tbody></table>'
            f'<table class="compact downtime-table"><caption>d6 Complications</caption>'
            f'<thead><tr><th class="c">d6</th><th>Complication</th></tr></thead><tbody>{comps}</tbody></table></div>')


def activities_html(activities):
    """All activities, in the order of the names. Return "" if there are none. Stop on a problem."""
    _stop_on([e for a in activities for e in activity_errors(a)])
    if not activities:
        return ""
    return ('<div class="cols2 compendium">'
            + "\n".join(activity_html(a) for a in sorted(activities, key=lambda a: a["name"])) + "</div>")


def all_downtime_html():
    from content.downtime import DOWNTIME
    return activities_html(DOWNTIME)
