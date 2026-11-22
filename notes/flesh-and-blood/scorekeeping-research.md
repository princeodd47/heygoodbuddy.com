# Flesh and Blood scorekeeping research

Working notes behind `docs/games/flesh-and-blood/scorekeeping.md`. This folder is outside `docs/`,
so it never gets published to the site.

Everything below is our own summary. Don't copy from sources.

**How to use:** this is a judge exam study guide, not a playthrough, so nothing
is held back by progress. When official documents conflict, the newest one
wins; note the date of every article used. Card text: cardvault.fabtcg.com.

Quiz questions for this page are `s01`–`s20` in `data/flesh-and-blood/quiz.yaml`
(topic `scorekeeping`; the quiz menu shows it as "Scorekeeping only").

## Sources (researched 2026-11-21)

- Judge Blog, "World Championship 2026 Updates" (Klaus Lassacher,
  2026-11-05): Scorekeeper Basic certification launched on JudgeHub that day.
  It tests understanding of GEM and readiness to be joint Scorekeeper + Head
  Judge, or to scorekeep side events at a World Tour stop. Nothing else: no
  syllabus, question count, pass mark or study material.
- JudgeHub exams guide (judge.fabtcg.com/guides/exams-intro/, via search
  snippet): exams available to Level 0 judges are L1A, L1B, Learn To Play
  Test, Scorekeeper - Basic.
- Judge Blog Scorekeeping category
  (blog.judge.fabtcg.com/blog/category/specializations/scorekeeping/): the
  only scorekeeping article is "Scorekeeping and Coverage Tips for Mixed
  Format Events" (Sebastian Bednarski, 2024-10-28). GEM steps for moving to
  new draft pods: Accept All Reports → Back to Tournament → cog under
  Tournament Rounds → format Booster Draft + New Draft Pods, untick Cut to
  Top 8 for more Swiss, or tick Cut to Top 8 + Elimination Rounds for a top 8
  draft. Hide pairings before the draft. Print Draft Pods. Also covers Purple
  Fox (third-party) for build-table seating, top 8 brackets and metagame
  images; left off the page as not exam material. Its "17+ players means 6
  draft rounds" was a 2024 Pro Quest structure; TRP A.2 now says 5 for
  17–32, so that claim isn't on the page. Button names are from 2024.
- TRP and PPG plain text (rules.fabtcg.com/txt/latest/en-fab-{trp,ppg}.txt),
  checked 2026-11-21. Sections used: TRP 1.1, 1.5, 2.1, 2.4, 2.7, 3.1–3.7,
  3.11, 9.2, 9.3, A.2–A.5; PPG 1.4, 3.1, 4.4, 4.9.
- CMP and MLP formulas are SVG images in the TRP appendix
  (rules.fabtcg.com/en/assets/images/trp_{cmp,mlp}_equation.svg), missing
  from the .txt. Rendered with headless Chrome:
  CMP = Σ m_r(2^R − 2^(r−1)) / Σ (2^R − 2^(r−1)); MLP = Σ l_r / R_p.
  So round 1 is worth the most. 3-round weights are 7, 6, 4 (total 17).

## Source quirks

- TRP A.2 single-day 9–16 row reads "5/4*" rounds and "Top 4/8*", with
  "* Limited tournament with booster draft play-off". Read positionally:
  5 rounds + top 4 normally; 4 rounds + top 8 (one draft pod) for Limited
  with a draft play-off.
- TRP A.2 team table has "64 -- 128" after "33 -- 64"; page says 65–128.
- legacy.fabtcg.com (old Pairings and Tiebreaker Policy, Play Anywhere guide)
  didn't respond 2026-11-21. Both are superseded by TRP A.4 anyway.

## Open questions

- Whether a bye counts as a win (m_r = 1) for CMP. TRP says m_r is 1 "if the
  player had a win in round r". Page doesn't claim either way.
- How Swiss pairing handles odd players, pair-downs and bye assignment. TRP
  doesn't say; GEM does it. Worth adding if LSS publishes it.
- Exam content itself. If the user takes it, ask what topics came up.

## Held back

Nothing.

## Already on the page

Quick reference, scorekeeper duties, official roles and tiers, GEM profiles
and ID, Swiss vs elimination, round counts (single-day, team, multi-day),
round times and Limited step times, round clock and extensions, reporting,
result-recording table, byes, tiebreaker order with CMP and MLP worked
examples, drops/no-shows/DQ, decklists, GEM draft-pod steps, team events,
UPF placement.
