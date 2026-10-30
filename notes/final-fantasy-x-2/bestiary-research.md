# Bestiary research

## Sources (researched 2026-10-29)

- Jegged FFX-2 bestiary, one page per enemy (235 pages): level, HP,
  elemental weak/resist/immune/absorb, common and rare steal and drop,
  bribe item, locations with chapters.
- Built by `tools/build_data.py` into `data/final-fantasy-x-2/bestiary.yaml`.

## Decisions

- When the common and rare item are the same, the page shows it once.
- Fiend Arena-only teams live on the Fiend Arena page, not here.
- Ability lists and flavour descriptions left out (copy concerns, and
  too wide for the table).

## Open questions

- None checked in game yet. In-game Scan data wins if it differs.

## In-game drops (2026-10-29)

- Boris (Floating Ruins, Chapter 1) dropped both Star Pendant and Faerie
  Earrings in one fight. Jegged lists only Star Pendant (87.5% common,
  12.5% rare, same item); its accessory list doesn't name Boris for Faerie
  Earrings. Added via `IN_GAME_DROPS` in `tools/build_data.py`, which also
  adds Boris to Faerie Earrings on the Accessories page.
- The guides' percentages are the common/rare split, not the chance of a
  drop, and they don't cover a second item. Treat drops as not
  guaranteed.
