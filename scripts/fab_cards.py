"""Keep the Flesh and Blood card data and images the quiz uses.

Run from the repo root with the site's virtualenv:

    .venv/bin/python scripts/fab_cards.py             # sync cards tagged in questions
    .venv/bin/python scripts/fab_cards.py --refresh   # fetch today's card data first
    .venv/bin/python scripts/fab_cards.py --mirror    # also save every card image locally

What it does:

1. With --refresh (or when there is no local copy yet), downloads the official
   card data CSV from cardvault.fabtcg.com into data/flesh-and-blood/card-cache/
   (gitignored), then writes data/flesh-and-blood/cards.csv: one row per
   English card with its current text, stats and image link. That trimmed file
   is committed, so the script works from the repo alone when LSS is offline.
2. Reads the `cards:` lists in quiz.yaml and my-rulings.yaml, copies those cards'
   images into docs/assets/images/flesh-and-blood/cards/ and writes their
   details to data/flesh-and-blood/cards.yaml for the quiz page. Images come
   from the local cache, and are downloaded only when the cache lacks them.
3. With --mirror, downloads every English card image into the cache (about
   300 MB the first time, then only new cards), so any card can be tagged later
   without the LSS site.

Card data and images © Legend Story Studios.
"""

import argparse
import csv
import difflib
import shutil
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "flesh-and-blood"
CACHE = DATA / "card-cache"
RAW_CSV = CACHE / "public_card_data.csv"
CACHE_IMAGES = CACHE / "images"
TRIMMED_CSV = DATA / "cards.csv"
USED_YAML = DATA / "cards.yaml"
QUESTION_FILES = [DATA / "quiz.yaml", DATA / "my-rulings.yaml"]
SITE_IMAGES = ROOT / "docs" / "assets" / "images" / "flesh-and-blood" / "cards"

CSV_URL = "https://d1pn9y8e99aays.cloudfront.net/public_card_data.csv"

FACE_FIELDS = {
    "name": "name",
    "image_url": "thumbnail_large",
    "pitch": "true_pitch",
    "color": "true_color",
    "cost": "true_cost",
    "power": "true_power",
    "defense": "true_defense",
    "life": "true_life",
    "intellect": "true_intellect",
    "typebox": "true_typebox",
    "text": "true_textbox",
}
COLUMNS = ["card_id", "print_id", "set_code", "rarity"] + [
    f"{side}_{field}" for side in ("front", "back") for field in FACE_FIELDS
]


def download(url, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "heygoodbuddy.com card sync"})
    with urllib.request.urlopen(req, timeout=60) as resp, open(tmp, "wb") as out:
        shutil.copyfileobj(resp, out)
    tmp.replace(dest)


def refresh_raw_csv():
    print("Downloading card data...")
    try:
        download(CSV_URL, RAW_CSV)
    except OSError as e:
        print(f"  couldn't download ({e}); using the copy already saved")


def write_trimmed_csv():
    """One row per English card, preferring its regular (non-foil) print."""
    best = {}
    with open(RAW_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["print_language"] != "en":
                continue
            seen = best.get(row["card_id"])
            if seen is None or (
                row["face_1_finish_type"] == "regular" and seen["face_1_finish_type"] != "regular"
            ):
                best[row["card_id"]] = row

    with open(TRIMMED_CSV, "w", newline="", encoding="utf-8") as f:
        out = csv.writer(f)
        out.writerow(COLUMNS)
        for card_id in sorted(best):
            row = best[card_id]
            line = [card_id, row["print_id"], row["set_code"], row["rarity"]]
            for face in ("face_1", "face_2"):
                line += [row[f"{face}_{col}"] for col in FACE_FIELDS.values()]
            out.writerow(line)
    print(f"Wrote {len(best)} cards to {TRIMMED_CSV.relative_to(ROOT)}")


def load_cards():
    with open(TRIMMED_CSV, newline="", encoding="utf-8") as f:
        return {row["card_id"]: row for row in csv.DictReader(f)}


def cached_image(url):
    return CACHE_IMAGES / url.rsplit("/", 1)[-1]


def fetch_image(url):
    path = cached_image(url)
    if not path.exists():
        download(url, path)
    return path


def image_urls(card):
    return [card[f"{side}_image_url"] for side in ("front", "back") if card[f"{side}_image_url"]]


def mirror_images(cards):
    urls = [u for card in cards.values() for u in image_urls(card) if not cached_image(u).exists()]
    print(f"Mirroring {len(urls)} missing images into {CACHE_IMAGES.relative_to(ROOT)}...")
    failed = []

    def get(url):
        try:
            fetch_image(url)
        except OSError as e:
            failed.append(f"{url} ({e})")

    with ThreadPoolExecutor(max_workers=4) as pool:
        for i, _ in enumerate(pool.map(get, urls), 1):
            if i % 250 == 0:
                print(f"  {i}/{len(urls)}")
    for line in failed:
        print("  failed:", line)


def tagged_card_ids():
    ids = set()
    for path in QUESTION_FILES:
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for q in doc.get("questions") or []:
            ids.update(q.get("cards") or [])
    return ids


def face_details(card, side, image):
    details = {}
    for field in FACE_FIELDS:
        value = card[f"{side}_{field}"]
        if field != "image_url" and value != "":
            details[field] = value
    details["image"] = image
    return details


def sync_used_cards(cards):
    wanted = sorted(tagged_card_ids())
    unknown = [c for c in wanted if c not in cards]
    for card_id in unknown:
        close = difflib.get_close_matches(card_id, cards, n=3, cutoff=0.6)
        print(f"Unknown card id {card_id!r}" + (f"; did you mean {', '.join(close)}?" if close else ""))
    if unknown:
        sys.exit(1)

    SITE_IMAGES.mkdir(parents=True, exist_ok=True)
    used, keep = {}, set()
    for card_id in wanted:
        card = cards[card_id]
        entry = {}
        for side, suffix in (("front", ""), ("back", "-back")):
            url = card[f"{side}_image_url"]
            if not url:
                continue
            name = f"{card_id}{suffix}.webp"
            shutil.copyfile(fetch_image(url), SITE_IMAGES / name)
            keep.add(name)
            entry[side] = face_details(card, side, name)
        used[card_id] = entry

    for old in SITE_IMAGES.glob("*.webp"):
        if old.name not in keep:
            old.unlink()

    header = (
        "# Generated by scripts/fab_cards.py from the official card data; don't edit by hand.\n"
        "# The cards tagged in quiz.yaml and my-rulings.yaml. © Legend Story Studios.\n\n"
    )
    body = yaml.safe_dump({"cards": used}, sort_keys=False, allow_unicode=True, width=1000)
    USED_YAML.write_text(header + body, encoding="utf-8")
    print(f"{len(used)} tagged cards written to {USED_YAML.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--refresh", action="store_true", help="download today's card data first")
    parser.add_argument("--mirror", action="store_true", help="save every card image in the local cache")
    args = parser.parse_args()

    if args.refresh or not RAW_CSV.exists():
        refresh_raw_csv()
    if RAW_CSV.exists():
        write_trimmed_csv()
    cards = load_cards()
    if args.mirror:
        mirror_images(cards)
    sync_used_cards(cards)


if __name__ == "__main__":
    main()
