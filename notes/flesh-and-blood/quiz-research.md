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

## Sources (researched 2026-10-27)

Every question cites the CR/PPG/TRP rule or release note it's based on;
see the rules, policy and interactions notes for those sources.

## Open questions

None. When a document changes, search the YAML for its rule numbers.

## Held back

Nothing.

## Already on the page

115 questions: rules 45, interactions 11, policy 37, tournament 22. Quote
bare Yes/No answers in the YAML, or they load as booleans.
