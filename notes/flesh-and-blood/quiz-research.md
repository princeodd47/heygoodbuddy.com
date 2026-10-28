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

Rule numbers in `cite` and `why` ("CR 1.0.2b", "PPG 3.2", "TRP 5.9, A.1")
link to that rule on rules.fabtcg.com, opening in a new tab. The links are
built in `docs/javascripts/fab-cards.js` (`appendRuleLinks`): each chapter is
its own page there, e.g. `/en/trp/05-gameplay-logistics/#trp5.9`. Checked
2026-10-28: all 135 links in the quiz hit an anchor that exists. If LSS renames
a chapter page, update `RULE_PAGES` in that file. The same script links rule
numbers in the text of every Flesh and Blood page, including table columns
headed CR, PPG or TRP.

Only fresh practice runs (a preset from the menu) are compared with the 85%
pass mark. Review missed, Retry these misses and My rulings show the score
and how many are still on the missed list instead.

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

- `{g}` is life, the same as `{h}`: they appear in the same phrases ("gain
  1{g}", "less {g} than"), and Rampant Growth // Life uses both for one
  thing. Mostly newer sets use `{g}` (checked 2026-10-28). It's shown with
  the `{h}` icon (`SYMBOL_ALIASES` in fab-cards.js) and has its own row in
  the Rules symbols table. `{x}` (X resources, as in "costs {x} less") has
  no icon and stays plain text, as the user asked.

When a document changes, search the YAML for its rule numbers.

## Held back

Nothing.

## Already on the page

115 questions: rules 45, interactions 11, policy 37, tournament 22.
14 are tagged with cards (r17, r36, r43, r44, i01, i03-i05, i07-i11), plus
m01. Not tagged on purpose: r03 (overpower the keyword), p24 (Marked Cards
infraction), p25 (rewind), t19 (Silver Age format). Quote
bare Yes/No answers in the YAML, or they load as booleans.
