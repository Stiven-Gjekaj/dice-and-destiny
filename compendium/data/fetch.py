import json, subprocess, sys
def get(ep):
    url = f"https://api.open5e.com/v2/{ep}/?document__key=srd-2024&limit=100&format=json"
    out = []
    while url:
        raw = subprocess.run(["curl", "-sS", "-m", "90", url], capture_output=True, text=True).stdout
        d = json.loads(raw); out += d["results"]; url = d.get("next")
    return out
for ep in [a for a in sys.argv[1:] if not a.startswith("--")]:
    r = get(ep); json.dump(r, open(f"all_{ep}.json", "w")); print(ep, len(r), flush=True)

# Usage (from this folder):
#   python3 fetch.py spells creatures items feats species backgrounds rules rulesets weapons armor magicitems
#   python3 fetch.py --classes
if __name__ == "__main__" and "--classes" in sys.argv:
    for c in "barbarian bard cleric druid fighter monk paladin ranger rogue sorcerer warlock wizard".split():
        raw = subprocess.run(["curl", "-sS", "-m", "90", f"https://api.open5e.com/v2/classes/srd-2024_{c}/?format=json"], capture_output=True, text=True).stdout
        open(f"{c}.json", "w").write(raw); print(c)
    raw = subprocess.run(["curl", "-sS", "-m", "90", "https://api.open5e.com/v2/classes/?document__key=srd-2024&format=json&limit=100"], capture_output=True, text=True).stdout
    open("all.json", "w").write(raw)
