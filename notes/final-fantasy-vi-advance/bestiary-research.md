# FF6 Advance Bestiary: research notes

## Other versions' names (2026-11-18)

Each Bestiary entry has `aka` in data.json: `snes` and `ps` when they differ
from the GBA name, and `spell` for a different spelling of the GBA name.
The page shows them under the name and in the popup card, and the search
matches them.

- Source: Final Fantasy Wiki. Every FF6 enemy page's
  "infobox enemy stats FFVI" has `snes`, `ps`, `gba` and `ios` names (and
  `1 snes`, `2 snes`... for multi-part bosses). "Bestiary (Final Fantasy
  VI)" lists the GBA bestiary (384 entries) and the Pixel Remaster bestiary
  (346), each linking to the enemy pages.
- Matching: guide monster → GBA bestiary number → wiki page → names
  (`tools/wiki_names.py`; it reads downloaded wikitext that isn't
  committed). Unnumbered entries match by name. All 399 matched.
- Pixel Remaster: in every case the wiki's PR list name equals its GBA
  name, and `gba` equals `ios` (2014 mobile) on every page. So the page says
  the guide's GBA names are also the PR names, and shows no PR line.
  Enemies missing from the PR bestiary list (Darkside, Kefka, Specter...)
  were checked against the `ios` name instead.
- PS1: the wiki's `ps` names are often shortened (Rhintaur, MagRoadr1–4).
  When `ps` equals `snes` the page shows one "SNES / PS1" name; otherwise
  both. Magna Roader's numbered PS1 names (MagRoadr1–4) are shown as
  "MagRoadr" since the colour each number belongs to isn't given.
- GBA-only enemies (Dragons' Den, Soul Shrine, the Redux dragons) get no
  other names.
- Fixes: the wiki's Erebus pages have a broken template value
  ("Hidon (Final Fantasy VI)ite"); the page text says the SNES name is
  Hidonite. The guide spells two names differently from the wiki's GBA
  list: Caladruis (wiki: Caladrius) and Tzakmagiel (wiki: Tzakmaqiel); the
  wiki spellings are stored as `spell` so search finds either.

## Elemental audit (2026-11-19)

Re-downloaded Caves of Narshe's enemy list in GBA mode (`ff6mode=gba`, 21
pages) and re-ran `tools/parse_enemies.py`: all 399 enemies match data.json
(stats, elements, statuses, steals, drops, Lores). So the data is a faithful
copy of CoN; the errors below are CoN's own.

Cross-checked elements against Gamer Corner's monster pages (SNES data, 364
pages from its sitemap): 341 of 350 matched enemies agree. The 40 GBA-only
enemies (Dragons' Den, Soul Shrine, etc.) have no second source. Where the
two disagreed, the Final Fantasy Wiki (api.php wikitext) settled it:

- Guardian: weak to Lightning and Water, no absorbs (CoN lists them as
  absorbs; its own strategy text says weak). Steal: common Force Armor, rare
  Ribbon (CoN has them reversed; the wiki's slot 1 is common, checked
  against Dadaluma).
- Goddess: absorbs Lightning and Holy (CoN: none).
- Level 20 Magic: absorbs Poison (CoN: weak to Poison).
- Mousse: immune to Poison, Wind, Holy, Earth and Water (CoN had Fire, not
  Water).
- Visage: immune to Earth (CoN: none).
- Left as CoN has them: Erebus (2)-(4), which CoN lists as separate variants
  and Gamer Corner as one enemy; Master Tonberry (Gamer Corner: absorbs
  Water; the wiki says its elements vary).
- Not checked: Hornet and Naude (no elemental table on their Gamer Corner
  pages); steals and drops beyond the Guardian.
