"""Check the Unicorn Overlord post-game squads against the game's rules.

Run from the repo root (needs PyYAML, which the site's requirements install):

    python scripts/uo_teams_check.py

It reads data/unicorn-overlord/teams.yaml and data/unicorn-overlord/equipment.yaml
and exits with an error, listing every problem, if:

- a row (front or back) has more than 3 units, or a squad more than 5;
- a unit doesn't have exactly 4 items, or has the same item twice;
- an item isn't in equipment.yaml (so its preview and Equipment row are missing);
- a tactic isn't active or passive;
- a start-of-battle skill names a unit that isn't in the squad;
- in the ten squads: a unit is in two squads, or the squads together use more
  of a limited item than you have.

The community builds (others) share units and items with the ten squads, so
only the per-squad rules apply to them. Missing items there are warnings for
now, not errors.
"""

import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TEAMS = ROOT / "data/unicorn-overlord/teams.yaml"
EQUIPMENT = ROOT / "data/unicorn-overlord/equipment.yaml"


def main():
    data = yaml.safe_load(TEAMS.read_text())
    equipment = yaml.safe_load(EQUIPMENT.read_text())
    known = {e["name"] for g in equipment["groups"] for e in g["entries"]}
    errors, warnings = [], []

    def check_squad(q, strict):
        where = q["title"]
        names = [u["name"] for u in q["units"]]
        if len(names) > 5:
            errors.append(f"{where}: {len(names)} units (at most 5)")
        if len(set(names)) != len(names):
            errors.append(f"{where}: a unit is listed twice")
        for row in ("front", "back"):
            n = sum(u["row"] == row for u in q["units"])
            if n > 3:
                errors.append(f"{where}: {n} units in the {row} row (at most 3)")
        for u in q["units"]:
            who = f"{where}, {u['name']}"
            if u["row"] not in ("front", "back"):
                errors.append(f"{who}: row is '{u['row']}' (front or back)")
            items = u["equipment"]
            if len(items) != 4:
                (errors if strict else warnings).append(f"{who}: {len(items)} items (every unit has 4 slots)")
            if len(set(items)) != len(items):
                errors.append(f"{who}: the same item twice ({', '.join(items)})")
            for item in items:
                if item not in known:
                    (errors if strict else warnings).append(f"{who}: '{item}' isn't in equipment.yaml")
            for t in u["tactics"]:
                if t["type"] not in ("active", "passive"):
                    errors.append(f"{who}: tactic type '{t['type']}' (active or passive)")
        start = q.get("start") or {}
        named = ([start["keep"]] if start.get("keep") else []) + start.get("off", [])
        for s in named:
            if s["unit"] not in names:
                errors.append(f"{where}: start-of-battle skill for {s['unit']}, who isn't in the squad")

    squad_of = {}
    used = defaultdict(list)
    for q in data["squads"]:
        check_squad(q, strict=True)
        for u in q["units"]:
            if u["name"] in squad_of:
                errors.append(f"{u['name']} is in '{squad_of[u['name']]}' and '{q['title']}'")
            squad_of[u["name"]] = q["title"]
            for item in u["equipment"]:
                used[item].append(u["name"])
    for item, have in data["limited"].items():
        if len(used[item]) > have:
            errors.append(f"{item}: you have {have}, the ten squads use {len(used[item])} ({', '.join(used[item])})")
    for item in data["pendants"]:
        if item not in known:
            errors.append(f"pendants: '{item}' isn't in equipment.yaml")

    for q in data["others"]:
        check_squad(q, strict=False)

    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    squads = len(data["squads"]) + len(data["others"])
    print(f"{squads} squads checked: {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
