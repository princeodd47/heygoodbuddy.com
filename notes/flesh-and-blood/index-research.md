# Flesh and Blood study guide research

Working notes behind `docs/games/flesh-and-blood/index.md`. This folder is outside `docs/`,
so it never gets published to the site.

Everything below is our own summary. Don't copy from sources.

**How to use:** this is a judge exam study guide, not a playthrough, so nothing
is held back by progress. When official documents conflict, the newest one
wins; note the date of every article used. Card text: cardvault.fabtcg.com.

## Sources (researched 2026-10-27)

- fabtcg.com/judges/become-a-judge/: levels L0/L1/L2; L1 needs L1A (rules)
  and L1B (policy) at 85%+ within the last 120 days, then the Level 1
  checklist in JudgeHub (auto-approved). L2 needs 120 days at L1, an L2
  recommendation review, 2+ competitive events in 365 days, L2A/L2B at 85%.
  Update quizzes each major set. Free; no events needed for L0/L1.
- fabtcg.com/resources/terms-use-licensed-assets/ (page dated 2025-07-14):
  "Assets" (art, design, visual assets) and card images are allowed for
  content creation (written content, indirect monetization OK) and fair use
  (teaching). Requires "© Legend Story Studios" and no passing off /
  implied endorsement. FAB logos for content creation need the statement
  "[name] is in no way affiliated with Legend Story Studios. Flesh and
  Blood™, and set names are trademarks of Legend Story Studios®." The
  footer on every page carries both lines.
- Comprehensive Rules, Procedure and Penalty Guide, Tournament Rules and
  Policy: rules.fabtcg.com (MkDocs site; plain text at
  rules.fabtcg.com/txt/latest/en-fab-{cr,trp,ppg}.txt). The text files carry
  no version number; record the date checked instead. fabtcg.com returns 403
  to curl, so use the browser for it; rules.fabtcg.com works with curl.

## Open questions

- Casual Procedure Guide PDF (cdn.fabtcg.com/uploads/2025/08/FaB_Casual_Procedure_Guide_2023_10_13-2.pdf)
  and the Judges of Rathe Code of Conduct (fabtcg.com/judges-of-rathe-code-of-conduct/,
  2026-08-08) not read yet. Probably not on L1 exams, but worth a skim.

## Resolved 2026-10-27

- Symbol images: downloaded the 8 icons (c, d, h, i, p, r, t, u) from
  rules.fabtcg.com/en/assets/images/icon_<key>.png into
  docs/assets/images/flesh-and-blood/. Allowed as "Assets" for written
  content / teaching under the terms above; every page carries the
  "© Legend Story Studios" line. Names are in data/flesh-and-blood/icons.yaml;
  pages use a `sym()` Jinja macro, and the quiz turns {p}-style tokens
  into icons.

## Held back

Nothing.

## Already on the page

L1 steps table, L1/L2 requirements, study plan, document links, disclaimer.
