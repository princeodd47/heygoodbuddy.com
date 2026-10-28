# Flesh and Blood rules research

Working notes behind `docs/games/flesh-and-blood/rules.md`. This folder is outside `docs/`,
so it never gets published to the site.

Everything below is our own summary. Don't copy from sources.

**How to use:** this is a judge exam study guide, not a playthrough, so nothing
is held back by progress. When official documents conflict, the newest one
wins; note the date of every article used. Card text: cardvault.fabtcg.com.

## Sources (researched 2026-10-27)

- Comprehensive Rules, Procedure and Penalty Guide, Tournament Rules and
  Policy: rules.fabtcg.com (MkDocs site; plain text at
  rules.fabtcg.com/txt/latest/en-fab-{cr,trp,ppg}.txt). The text files carry
  no version number; record the date checked instead. fabtcg.com returns 403
  to curl, so use the browser for it; rules.fabtcg.com works with curl.
- Read CR chapters 1 and 3–9 in full (glossary skipped). Rule numbers on
  the page were checked against the 2026-10-27 text.
- Rules Update 2026-09-17 (start-of-game: arena-cards before deck) is now in
  CR 4.1.4–4.1.6 and TRP 3.3.
- Rules Update 2026-01-30: ally attacking/defending heroes, targeted layers
  still resolve.
- Rules Update 2026-05-19: attack queue and attack-layers.

## Open questions

None.

## Held back

Nothing. Left out for length: split cards, double-faced cards, meld,
Living Legend points, macros in depth, hidden triggers, clash, the full
keyword list in CR 8.

## Already on the page

Precedence, ownership/LKI, priority, start/turn/end phases, ending a game,
costs and pitching, playing cards (9 steps), resolving layers, optional /
conditional / targeted effects, events, continuous-effect staging,
replacement order, triggers, combat steps, ally attacks, attack-proxies,
attack-layers, keyword table, number rules.

Card examples (added 2026-10-28): most points end with an *Example:* naming a
card through the `card()` macro, which opens a preview of the card's image and
current text. Most examples come from the CR's own examples; each was checked
against the card's current text in `data/flesh-and-blood/cards.csv`. The
keyword table has an Example column. Points with no natural card example
(priority basics, payment order, ending a game) have none. After adding or
changing a `card()` call, run `.venv/bin/python scripts/fab_cards.py`.

Usurp the Shadow Throne cards use set code IAR in the card data.
