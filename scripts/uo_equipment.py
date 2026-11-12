"""Build the Unicorn Overlord equipment data from the Fandom and Miraheze wikis.

Run from the repo root (standard library only):

    python3 scripts/uo_equipment.py

It reads every item in the Equipment column of
docs/games/unicorn-overlord/post-game-teams.md and writes
data/unicorn-overlord/equipment.yaml: stats, effects, the skill it grants,
every place to get it and the cheapest shop price. The Equipment page and the
item previews on the Post-Game Teams page read that file.

Where an item comes from, in this order:

1. Shops: the armorer tables on every Fandom town page, plus the Black Market
   Dealer page. Towns are grouped by price and labelled with their continent.
2. Exchanges: the Divine Shard Exchange and Coliseum Prize Exchange pages.
3. Quest rewards: the reward columns on the Fandom Quests page.
4. Anything else on the item's own Fandom page (starting equipment, monuments,
   drops), plus its shop lines for towns the town pages missed.
5. The Miraheze weapon tables' "How to Obtain", only when nothing above did.

Item names follow the post-game page (GameFAQs spellings). ALIASES maps them to
Fandom page titles where they differ. OVERRIDES adds or replaces fields where
both wikis are missing something or wrong. In-game data wins: when the user
reports a difference, fix it here and rerun.
"""

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEAMS = ROOT / "docs/games/unicorn-overlord/post-game-teams.md"
OUT = ROOT / "data/unicorn-overlord/equipment.yaml"
FANDOM = "https://unicornoverlord.fandom.com/api.php"
MIRAHEZE = "https://unilord.miraheze.org/w/api.php"
CONTINENTS = ["Cornia", "Drakenhold", "Elheim", "Bastorias", "Albion"]
WEAPON_PAGES = ["Swords", "Axes", "Spears", "Bows", "Staves"]
QUEST_KINDS = {"Main Quests": "main quest", "Side Quests": "side quest", "Overworld Quests": "overworld quest",
               "Liberation Quests": "liberation quest", "Treasure Map Quests": "treasure map"}

# Post-game page name -> Fandom page title.
ALIASES = {
    "Apeliotes' Bow": "Apeliotes's Bow",
    "Black Iron Greatshield": "Black-Iron Greatshield",
    "Black Iron Spear": "Black-Iron Spear",
    "Blessed Round Shield": "Blessed Roundshield",
    "Boreas' Axe": "Boreas's Axe",
    "Chlorotic Wand": "Chlorotic",
    "Euros' Staff": "Euros's Staff",
    "Heaven Mirror Greatshield": "Heaven's Mirror Greatshield",
    "Labrys Axe": "Labrys",
    "Millennium Scepter": "Millenium Scepter",
    "Notos' Sword": "Notos's Sword",
    "Skiron's Shield": "Skiron's Greatshield",
    "Speedhex Staff": "Speed-Hex Staff",
    "Zephyros' Spear": "Zephyros's Spear",
}

# Fields to add or replace after parsing, by post-game page name.
OVERRIDES = {
    "Ring of the Maiden": {
        "kind": "accessory",
        "where": ["Quest reward: Unicorn and Maiden (main quest)"],
    },
    # From the user (in-game); the battle is the Forest of Thorns main quest per Fandom's Baltro and Quests pages.
    "Necromancer's Lantern": {"where": ["Dropped by Baltro in Vile Desecration (main quest, Forest of Thorns, Elheim)"]},
    # From the user (Discord tip): Jerome's city is Largion Citadel, in southeastern Albion.
    "Lamplight Ring": {"where": ["From a resident on Albion's southern coast, near Largion Citadel"]},
    # The Quests page lists the ring under quests that need it, not ones that give it.
    "Ring of the Unicorn": {"where": ["Alain's starting accessory"]},
    # From the user (in-game): only one Flame-Hex Staff exists.
    "Flame-Hex Staff": {"where": ["Shop, 8,000 G: Nestascheft Town (Drakenhold), stock 1"]},
    # From the user (in-game): only one Mirage Greatshield exists.
    "Mirage Greatshield": {"where": ["Shop, 10,000 G: Kiulkukka Town (Elheim), stock 1"]},
}

GROUPS = {"sword": "Swords", "greatsword": "Swords", "axe": "Axes", "spear": "Spears", "lance": "Spears",
          "bow": "Bows", "staff": "Staves", "tome": "Tomes", "shield": "Shields", "greatshield": "Greatshields",
          "accessory": "Accessories"}
GROUP_ORDER = list(dict.fromkeys(GROUPS.values()))

FIXES = [
    ("Mausoleaum", "Mausoleum"), ("Echange", "Exchange"), ("Elfheim", "Elheim"), ("Drakenheim", "Drakenhold"),
    ("Overlord battle", "Overworld battle"), ("maniscript", "manuscript"), (" ath the ", " at the "),
    ("’", "'"), ("Overwolrd", "Overworld"), ("(Questname)", ""), (" in Bastoria", " in Bastorias"),
]


def tidy(line):
    """Shared clean-up for location lines from either wiki."""
    for a, b in FIXES:
        line = line.replace(a, b)
    line = re.sub(r'\s*"([^"]+)"', r" \1", line)
    line = re.sub(r"[Qq]uest\s*:\s*", "quest ", line)
    line = re.sub(r"^(?:Complete|Completing) the quest ", "Quest reward: ", line)
    line = re.sub(r"^(\w+)(?: starts with this weapon)$", r"\1's starting weapon", line)
    line = re.sub(r"^Starting (?:equipment|accessory) of (.+)$", r"Starting equipment of \1", line)
    line = re.sub(r"\s+in (" + "|".join(CONTINENTS) + r")$", r" (\1)", line)
    line = re.sub(r",? boss of\s*$", "", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line[:1].upper() + line[1:]


# ---------------------------------------------------------------- fetching

def api(base, **params):
    params.update(format="json", formatversion=2)
    req = urllib.request.Request(base + "?" + urllib.parse.urlencode(params),
                                 headers={"User-Agent": "Mozilla/5.0 guide-research"})
    return json.load(urllib.request.urlopen(req))


def fetch(titles):
    """Fandom title -> wikitext, following redirects (keyed by the requested title)."""
    pages = {}
    titles = sorted(set(titles))
    for i in range(0, len(titles), 40):
        data = api(FANDOM, action="query", prop="revisions", rvprop="content", rvslots="main",
                   titles="|".join(titles[i:i + 40]), redirects=1)["query"]
        back = {r["to"]: r["from"] for r in data.get("redirects", []) + data.get("normalized", [])}
        for page in data["pages"]:
            title = page["title"]
            while title in back:
                title = back[title]
            if "revisions" in page:
                pages[title] = page["revisions"][0]["slots"]["main"]["content"]
        time.sleep(1)
    return pages


def category(name):
    data = api(FANDOM, action="query", list="categorymembers", cmtitle="Category:" + name, cmlimit=500)
    return [m["title"] for m in data["query"]["categorymembers"]]


# ---------------------------------------------------------------- wikitext helpers

def norm(name):
    return re.sub(r"[^a-z0-9]", "", name.lower().replace("'s ", " ").replace("' ", " "))


def clean(text):
    text = re.sub(r"\[\[File:[^\]]*\]\]", "", text)
    text = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"<br\s*\\?/?\s*>", " ", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("'''", "").replace("''", "").replace("💎", "")
    text = re.sub(r"\s+", " ", text).strip()
    return "" if text in ("-", "—") else text


def link_target(text):
    m = re.search(r"\[\[([^|\]]+)", text)
    return m.group(1).strip() if m else clean(text)


def cell(line):
    """Value of a wikitable cell line, without style attributes."""
    line = line.lstrip("|!").strip()
    if re.match(r"^(style|colspan|class)=", line) and "|" in line:
        line = line.split("|", 1)[1]
    return clean(line)


def section(text, name):
    m = re.search(r"==\s*" + name + r"[^=]*==(.*?)(?=\n==[^=]|\Z)", text, re.S)
    return m.group(1) if m else ""


def table_rows(text):
    """Rows of every wikitable in text, as lists of raw cell strings."""
    rows = []
    for table in re.findall(r"\{\|.*?\n\|\}", text, re.S):
        for row in table.split("\n|-")[1:]:
            cells = []
            for line in row.strip().splitlines():
                if line.startswith("|}") or line.startswith("!"):
                    continue
                if line.startswith("|"):
                    cells += [c.strip() for c in line[1:].split("||")]
                elif cells:
                    cells[-1] += " " + line.strip()
            if cells:
                rows.append(cells)
    return rows


def number(text):
    digits = re.sub(r"[^\d]", "", clean(text))
    return int(digits) if digits else None


def slug(name):
    """Row id on the Equipment page; the preview script links to it."""
    return re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", name.lower()).strip())


def gold(n):
    return f"{n:,} G"


# ---------------------------------------------------------------- source indexes

def continent_of():
    pages = fetch([f"{c} (Locations)" for c in CONTINENTS])
    found = {}
    for c in CONTINENTS:
        for name in re.findall(r"\[\[([^|\]]+)", pages.get(f"{c} (Locations)", "")):
            found.setdefault(name.strip(), c)
    found.setdefault("Baumratte", "Drakenhold")
    return found


def shop_index(wanted, continents):
    """norm(item) -> [(price, place, continent)] from every town's armorer table."""
    towns = [t for t in category("Towns and Cities") if "(Locations)" not in t and t not in ("Towns and Cities", "All Fevrith Archives")]
    pages = fetch(towns + ["Baumratte"])
    found = {}
    for town, text in pages.items():
        for heading in re.findall(r"==\s*([^=]*[Ss]hop[^=]*)==", text):
            if "provision" in heading.lower():
                continue
            for cells in table_rows(section(text, re.escape(heading.strip()))):
                key = norm(link_target(cells[0]))
                price = number(cells[-1]) if len(cells) >= 3 else None
                if key in wanted and price:
                    found.setdefault(key, []).append((price, town, continents.get(town, "")))
    return found


def black_market(wanted):
    text = fetch(["Black Market Dealer"]).get("Black Market Dealer", "")
    found = {}
    for part in re.split(r"\n==\s*\[*", text)[1:]:
        continent = re.match(r"([A-Za-z]+)", part).group(1)
        for cells in table_rows(part):
            key = norm(link_target(cells[0]))
            price = number(cells[-1])
            if key in wanted and price:
                found.setdefault(key, []).append((price, continent))
    return found


def exchanges(wanted):
    pages = fetch(["Divine Shard Exchange", "Coliseum Prize Exchange"])
    shards, coins = {}, {}
    for cells in table_rows(section(pages.get("Divine Shard Exchange", ""), "Shop Content")):
        key = norm(link_target(cells[0]))
        if key in wanted and len(cells) >= 3 and number(cells[2]):
            shards[key] = number(cells[2])
    for cells in table_rows(pages.get("Coliseum Prize Exchange", "")):
        key = norm(link_target(cells[0]))
        if key in wanted and number(cells[-1]):
            coins.setdefault(key, number(cells[-1]))
    return shards, coins


def quest_rewards(wanted):
    text = fetch(["Quests"]).get("Quests", "")
    found = {}
    for heading, kind in QUEST_KINDS.items():
        for cells in table_rows(section(text, heading)):
            if len(cells) < 4:
                continue
            quest = clean(cells[1])
            for reward in cells[3:]:
                key = norm(link_target(reward))
                if key in wanted:
                    found.setdefault(key, []).append(f"Quest reward: {quest} ({kind})")
    return found


def star_iron(wanted):
    text = fetch(["Star Iron"]).get("Star Iron", "")
    found = {}
    for cells in table_rows(text):
        key = norm(link_target(cells[0]))
        if key in wanted and len(cells) >= 3:
            found[key] = [f"Trade {clean(cells[1])} Star Iron at the {clean(cells[2])} (Bastorias)"]
    return found


def miraheze_weapons():
    """norm(name) -> (price, [how to obtain lines]) from the Miraheze weapon tables."""
    found = {}
    for page in WEAPON_PAGES:
        text = api(MIRAHEZE, action="parse", page=page, prop="wikitext")["parse"]["wikitext"]
        for row in text.split("\n|-")[1:]:
            row = row.split("\n|}")[0].replace("\n", " ").strip().lstrip("|")
            cells = [re.sub(r'^\s*style="[^|]*\|', "", c).strip() for c in row.split("||")]
            if len(cells) < 6:
                continue
            how = [clean(x).rstrip(".") for x in re.split(r"<br\s*\\?/?>", cells[-1])]
            how = [re.sub(r"\s*in the quest\s*$", "", x) for x in how if x]
            found[norm(clean(cells[1]))] = (number(cells[-2]), how)
        time.sleep(1)
    return found


# ---------------------------------------------------------------- item pages

def item_lines(text):
    """Obtention lines from an item page that the indexes don't cover."""
    lines = []
    for raw in section(text, "Obtention").splitlines():
        if not raw.startswith("*"):
            continue
        line = clean(raw.lstrip("* ")).rstrip(".")
        line = re.sub(r"^Can be (?:obtained|found) ", "", line)
        lines.append(tidy(line))
    if any("onument" in l for l in lines):
        lines = [". ".join(lines)]
    return lines


def is_covered(line):
    """True for item-page lines about shops, exchanges or quest rewards (the indexes cover those)."""
    return bool(re.search(r"\bG\b|Armorer|armorer|shops?\b|Black Market|[Dd]ivine [Ss]hard|Coliseum Prize|\bCC\b|"
                          r"^(?:For|When|By) (?:completing|doing)|^Complete|^As a reward|^Reward for", line))


def parse(text):
    first = re.search(r"is an? \[\[(?:[^|\]]*\|)?([^\]]+)\]\]", text)
    kind = first.group(1).lower().rstrip("s") if first else ""
    kind = "staff" if kind.startswith("stav") else kind

    stats, effects = {}, []
    rows = section(text, "Stats").splitlines()
    for i, line in enumerate(rows):
        if line.startswith("!") and "colspan" not in line:
            label = clean(line[1:])
            value = cell(rows[i + 1]) if i + 1 < len(rows) else ""
            if label.startswith("Effect"):
                if value:
                    effects.append(value)
            elif value:
                stats[label] = value

    skill = None
    block = section(text, "Skill while equipped")
    if block:
        rows = block.splitlines()
        info = {}
        for i, line in enumerate(rows):
            label = clean(line.lstrip("|"))
            if label in ("AP Cost", "PP Cost", "Type", "Trait", "Phys. Potency", "Mag. Potency", "Hit Rate"):
                info[label] = cell(rows[i + 1])
        desc = [cell(l) for l in rows if l.startswith("|") and "colspan" in l]
        cost = f"{info['AP Cost']} AP" if info.get("AP Cost") else f"{info['PP Cost']} PP" if info.get("PP Cost") else ""
        details = [cost, info.get("Type", "")]
        for key, short in (("Phys. Potency", "Phys. potency"), ("Mag. Potency", "Mag. potency"), ("Hit Rate", "Hit rate")):
            if info.get(key):
                details.append(f"{short} {info[key]}")
        if info.get("Trait"):
            details.append(info["Trait"].replace("(", "").replace(")", ""))
        # The skill is effect #1 on the item; the skill table's own header is sometimes wrong.
        skill = {"name": effects[0] if effects else "", "details": " · ".join(d for d in details if d),
                 "text": desc[0] if desc else ""}
        effects = effects[1:]

    short = {"Phys. ATK": "P.Atk", "Mag. ATK": "M.Atk", "Phys. DEF": "P.Def", "Mag. DEF": "M.Def", "Guard Rate": "Guard"}
    stat_text = " · ".join(f"{short[k]} {stats[k]}" for k in short if k in stats and stats[k] not in ("0", "0%"))
    return {"kind": kind, "stats": stat_text, "effects": effects, "skill": skill, "lines": item_lines(text)}


# ---------------------------------------------------------------- assembling

def shop_lines(shops):
    by_price = {}
    for price, town, continent in shops:
        by_price.setdefault(price, {}).setdefault(continent, set()).add(town)
    lines = []
    for price in sorted(by_price):
        groups = by_price[price]
        parts = [", ".join(sorted(towns)) + (f" ({c})" if c else "")
                 for c, towns in sorted(groups.items(), key=lambda kv: CONTINENTS.index(kv[0]) if kv[0] in CONTINENTS else 9)]
        lines.append(f"Shop, {gold(price)}: " + "; ".join(parts))
    return lines


def team_items():
    names = set()
    for line in TEAMS.read_text().splitlines():
        if line.startswith(("| Front ", "| Back ")):
            for item in line.split("|")[4].split(","):
                names.add(item.strip())
    names.discard("Starting weapon")
    return sorted(names)


def q(value):
    return json.dumps(value, ensure_ascii=False)


def write(groups):
    out = ["# Generated by scripts/uo_equipment.py from the Unicorn Overlord Fandom and Miraheze wikis.",
           "# Don't edit by hand: fix data through OVERRIDES in the script, then rerun it.", "groups:"]
    for group in GROUP_ORDER:
        entries = groups.get(group)
        if not entries:
            continue
        out += [f"  - type: {q(group)}", "    entries:"]
        for e in sorted(entries, key=lambda e: e["name"]):
            out.append(f"      - name: {q(e['name'])}")
            out.append(f"        id: {q(slug(e['name']))}")
            out.append(f"        stats: {q(e['stats'])}")
            out.append(f"        effects: {q(e['effects'])}")
            if e.get("skill"):
                out.append("        skill:")
                for k in ("name", "details", "text"):
                    out.append(f"          {k}: {q(e['skill'][k])}")
            out.append(f"        price: {q(e['price'])}")
            out.append(f"        where: {q(e['where'])}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out) + "\n")


def main():
    names = team_items()
    titles = {n: ALIASES.get(n, n) for n in names}
    wanted = {}
    for name in names:
        wanted[norm(name)] = name
        wanted[norm(titles[name])] = name
    keys = {name: {norm(name), norm(titles[name])} for name in names}

    item_pages = fetch(list(titles.values()))
    continents = continent_of()
    shops = shop_index(wanted, continents)
    market = black_market(wanted)
    shards, coins = exchanges(wanted)
    quests = quest_rewards(wanted)
    meteor = star_iron(wanted)
    weapons = miraheze_weapons()

    def gather(index, name):
        out = []
        for k in keys[name]:
            v = index.get(k)
            if isinstance(v, list):
                out += [x for x in v if x not in out]
            elif v is not None and not out:
                out = v
        return out

    groups, problems = {}, []
    for name in names:
        text = item_pages.get(titles[name], "")
        item = parse(text) if text else {"kind": "", "stats": "", "effects": [], "skill": None, "lines": []}
        item["name"] = name

        shop = gather(shops, name)
        towns = {t for _, t, _ in shop}
        where = shop_lines(shop)
        prices = [p for p, _, _ in shop]
        bm = gather(market, name)
        for price in sorted({p for p, _ in bm}):
            where.append(f"Black Market Dealer, {gold(price)}: " + ", ".join(c for p, c in bm if p == price))
            prices.append(price)
        if gather(shards, name):
            where.append(f"Divine Shard Exchange (any church): {gather(shards, name)} Divine Shards")
        if gather(coins, name):
            where.append(f"Coliseum Prize Exchange (Baumratte): {gather(coins, name):,} Coliseum Coins")
        where += gather(quests, name) + gather(meteor, name)
        for line in item["lines"]:
            covered = is_covered(line) and (where or "???" in line)
            new_town = any(t in line for t in re.findall(r"[A-Z][\w'-]+(?: [A-Z][\w'-]+)* (?:Town|Harbor|Citadel|Hamlet|Village|Palace)", line)
                           if t not in towns) and not where
            if "???" in line or (covered and not new_town):
                continue
            where.append(line)
        extra = weapons.get(norm(name)) or weapons.get(norm(titles[name]))
        if extra and not where:
            price, how = extra
            for line in how:
                m = re.match(r"(?:Can be )?[Pp]urchased (?:from|at) (?:the )?(.+)$", line)
                where.append(tidy(f"Shop, {gold(price)}: {m.group(1)}" if m and price else line))
            if price:
                prices.append(price)

        item["where"] = [tidy(w) for w in where]
        item["price"] = gold(min(prices)) if prices else ""
        item.update(OVERRIDES.get(name, {}))
        group = GROUPS.get(item["kind"])
        if not group:
            problems.append(f"No type: {name} ({item['kind']!r})")
            continue
        if not item["where"]:
            problems.append(f"No location: {name}")
        groups.setdefault(group, []).append(item)

    write(groups)
    print(f"Wrote {sum(map(len, groups.values()))} items to {OUT.relative_to(ROOT)}")
    for p in problems:
        print(p)


if __name__ == "__main__":
    main()
