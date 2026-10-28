# Flesh and Blood practice quiz research

Working notes behind `docs/games/flesh-and-blood/quiz.md`. This folder is outside `docs/`,
so it never gets published to the site.

Everything below is our own summary. Don't copy from sources.

**How to use:** this is a judge exam study guide, not a playthrough, so nothing
is held back by progress. When official documents conflict, the newest one
wins; note the date of every article used. Card text: cardvault.fabtcg.com.

Questions live in `data/flesh-and-blood/quiz.yaml`; the page script is
`docs/javascripts/fab-quiz.js`, which saves missed question ids in
localStorage under `fab-quiz-missed`.

The user's own rulings live in `data/flesh-and-blood/my-rulings.yaml`
(ids start with `m`). The "My rulings" set asks all of them in file order;
only the choices are shuffled. Those are the user's to write; don't add or
edit them unless asked.

Card images and text: a question can list card ids under `cards:` (ids are
the `card_id` column of `data/flesh-and-blood/cards.csv`, e.g.
`pillar-of-unity`, or `sink-below-1` for the red one of a pitch cycle). After
changing tags, run `.venv/bin/python scripts/fab_cards.py`. It copies the
tagged cards' images to `docs/assets/images/flesh-and-blood/cards/` and their
text to `cards.yaml`. `--refresh` re-downloads the official CSV (it's updated
daily) and rewrites `cards.csv`; the git diff then shows any errata.
`--mirror` keeps every English card image in the gitignored
`data/flesh-and-blood/card-cache/`, so the script works without the LSS site.

## Sources (researched 2026-10-27)

Every question cites the CR/PPG/TRP rule or release note it's based on;
see the rules, policy and interactions notes for those sources.

- Official card data CSV, linked as "Download Card Data" on
  cardvault.fabtcg.com (2026-10-28): every print in every language, about
  33 MB. The `true_*` columns are current text after errata. Card images are
  .webp files on LSS's S3, about 54 KB each. The site's search API isn't
  documented; we don't use it.

## Open questions

- Card text uses `{g}` (167 times) and `{x}` (8 times), which have no icon on
  rules.fabtcg.com, so the quiz shows them as plain text. Find the official
  icons if a tagged card needs them.

When a document changes, search the YAML for its rule numbers.

## Held back

Nothing.

## Already on the page

115 questions: rules 45, interactions 11, policy 37, tournament 22. Quote
bare Yes/No answers in the YAML, or they load as booleans.
