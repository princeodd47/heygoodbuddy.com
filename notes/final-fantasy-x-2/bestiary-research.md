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
