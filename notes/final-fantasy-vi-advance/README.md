# Final Fantasy VI Advance Field Guide

The guide is one self-contained page, not Markdown. It's published at
`docs/games/final-fantasy-vi-advance/field-guide/index.html`, which is built
from the files here.

## Rebuilding the page

```bash
python3 notes/final-fantasy-vi-advance/build.py
```

This puts `data.json` into `template.html`, adds the full document skeleton
and the "← heygoodbuddy.com" link, and writes the page under `docs/`. Run it
after any change to `template.html` or `data.json`, then commit both the
source and the built page.

## Files

- `template.html`: the page (styles, markup and script). `__DATA__` marks
  where `data.json` goes.
- `data.json`: everything the page shows, compiled from the sources below.
- `wt_content.py`: the walkthrough's steps, highlighted boxes and boss
  strategies, written for this guide.
- `wt_titles.py`: the walkthrough chapter titles, written for this guide.
- `tools/`: the scripts that compiled `data.json`. The parsers and
  `walkbuild.py`, `chestmap.py` and `colo_best.py` read pages downloaded
  from the source sites into a `raw/` folder. Those downloads are **not
  committed**, so these scripts won't run as-is; they're kept as a record of
  how the data was put together. Edit `data.json` directly for small fixes.

## Sources

- [Caves of Narshe](https://www.cavesofnarshe.com/ff6/), GBA mode: stats,
  items, equipment, Espers, Lores, the Colosseum wager list and guide.
- Djibriel's [Caves of Narshe walkthrough](https://www.cavesofnarshe.com/ff6/walkthrough.php):
  chapter order, enemies and treasure per chapter.
- [Gamer Corner](https://guides.gamercorner.net/ffvi/): treasure locations
  (SNES names, mapped to GBA names in `tools/chestmap.py`).
- [Final Fantasy Wiki](https://finalfantasy.fandom.com/): Rage and Dance
  lists, and the level reset glitch.
- Master ZED's monster guide: locations and special-attack formulas (SNES).

Write in our own words; don't copy text from the sources.

## Open questions

- Five SNES → GBA item names in `tools/chestmap.py` are guesses: Tempest →
  Kazekiri, Coin Toss → Heiji's Jitte, Stunner → Kagenui, Regal Cutlass →
  Great Sword, Blizzard → Icebrand.
- The Doma Castle banquet-reward treasure is placed in chapter 1.40.
- The Dragons' Den chapters and a few small stops only have a plain item
  list, with no locations.
- 23 of the 256 Rages aren't tied to a walkthrough chapter.
- Where the post-game clear save puts you (outside Kefka's Tower, or at the
  last save point) isn't confirmed.
- Kefka's Megalixir steal comes from the walkthrough; the bestiary data
  doesn't list it.
- Gladius: the source data lists it as Lightning, but its old note called it
  Holy (and its in-game text says it smites evil). The page shows Lightning.
- Gravija, Valor and Flood have no spell description yet.
- Minerva Bustier: the data says it absorbs Fire, Ice, Lightning and Wind;
  some guides say it nullifies them. Check in-game.

## Wording

In-game text is kept word for word and shown as a quote: equipment
descriptions, Blitz and Bushido descriptions, and Esper summon descriptions.
Everything else that explains something is in our own words. Two scripts
replaced the source sites' wording in `data.json`, and they're kept as a
record (running them again does no harm):

- `tools/rewrite_notes.py`: equipment notes and spell descriptions; drops
  the Esper name origins.
- `tools/rewrite_more.py`: Lores, Dance moves (and their `kinds` filter
  tags), Esper locations, equipment elemental text and Rage footnotes.

Bestiary and Rage locations are short place lists, kept as data.
