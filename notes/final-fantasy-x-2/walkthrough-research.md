# FFX-2 walkthrough research

Working notes behind `docs/games/final-fantasy-x-2/walkthrough.md`.

Everything below is our own summary. Don't copy from sources.

**How to use:** the user has played FFX-2 many times and wants no spoiler
gating, so nothing is held back for progress. If the user reports something
different in-game, the in-game value wins. Fix the page and these notes.

Raw downloads (Jegged and Gamer Guides HTML) were saved to the session
scratchpad and parsed by `tools/build_data.py`; re-download to rebuild.

## Sources (researched 2026-10-29)

- Jegged FFX-2 walkthrough, Chapter 1 pages 01 (Luca) and 02 (Mt. Gagazet
  Floating Ruins): chests, boss HP and steals, Celsius interlude, Black Mage
  from Shinra, Creature Creator opens on first Celsius visit.
- Gamer Guides FFX-2 walkthrough (Prologue, Aboard the Celsius, Gagazet,
  Return to the Celsius): cross-check.

## Scope

First pass ran Luca to the end of the Gagazet mission. Extended
2026-10-29 to all of Chapter 1 (Besaid through YSLS-Zero) with 100%
markers, checkpoints, notable steals/drops and creature catches.

Chapter 1 sources: Jegged Chapter 1 pages 01 to 20 (one per area), with
Gamer Guides Chapter 1 pages as the cross-check.

## Checkpoint semantics

Jegged's "Expected" completion figure after each box is the running total
once everything above it is done. Page uses 3%, 4%, 9%, 12%, 20%, and 25%
at chapter end; Gamer Guides also gives 25% at the end of Chapter 1.

## Conflicts and decisions

- Creature Creator tutorial pods: Jegged says the tutorial hands over one
  Trap Pod S. The user checked in game: it gives a Trap Pod S, M and L.
  In-game wins; walkthrough, Creatures page updated. The L pod is the one
  to use on Flame Dragon in Besaid.
- Gagazet Ronso answers: Jegged's marked answers were checked against the
  Gamer Guides list and the page uses the 100% set (Leave it to the
  Gullwings / never forget their sacrifice / I'm sure you're right / I can
  imagine how you must feel / I wouldn't forgive them either / a change
  for the better; Kimahri: learn to deal with these things; Garik: we'll
  take care of Lian and Ayde).
- Steals differ between guides: Gamer Guides gives Ormi (Gagazet) Iron
  Bangle and Logos (Luca) nothing specific; Jegged gives Gauntlets and
  Silver Glasses. Page uses Jegged.
- Gamer Guides lists Boris weak to fire and ice; Jegged doesn't list
  weaknesses. Page keeps fire/ice.

## "Creatures scenes"

Read as creature-related events in Chapter 1: what to trap where
(**Creatures:** lines), the Flame Dragon L-pod catch, and the chapter-end
Fiend Tale Story Level plus 3 Trap Pod SP. Fiend Tale text itself is not
copied; summaries could be a later page if wanted.

## Next if extended

Chapter 2: Bevelle (Kukulcan, YAC-13, YAU-28, YSLS-99 are Chapter 2 only),
Youth League vs New Yevon choice, Besaid/Kilika/Luca missions.

- Boris drop: user got Star Pendant and Faerie Earrings from one fight;
  guides list only Star Pendant. Page shows both.
- 2026-10-30: Besaid opening reworded. Jegged's Besaid page describes the
  Promontory walk as a scene, not something you walk to; Gamer Guides
  doesn't mention it. Added the Besaid Key shop note (900,000 gil, skip).
- 2026-10-30: user asked where the Waterfall Way cipher is. There isn't
  one: Jegged and Gamer Guides both put ciphers at the Promontory, the
  next (ruins) area, and two on the beach. Waterfall Way only has the
  Chocobo Wings. Cipher bullets now numbered on both pages.
- 2026-10-30: Moonflow escort third wave checked in game by the user: one
  bandit from the front and one from the back (we had "two from front and
  back"). In-game wins; both pages updated.
- 2026-10-30: full Chapter 1 100% audit against every Jegged Story
  Completion checkbox (pages 01 to 15; 01 Luca re-downloaded). All
  checkbox items were already on the page. Added: "visit every Hotspot"
  note, 100% markers for automatic scenes (Djose, Guadosalam arrival,
  Thunder Plains, Bikanel, Bevelle, Calm Lands, Mt. Gagazet, Zanarkand,
  chapter end), Shave the Hypello? completion as its own 100% item,
  checkpoints 18% (after Thunder Plains) and 21% (after Bikanel), Cid's
  answer doesn't count now, chapter end is 25.2%. Page-end expected totals:
  3.4, 6.6, 8.8, 9.4, 11.2, 15.8, 16.8, 17.4, 18.0, 20.2, 21.0, 21.8, 22.2,
  24.2, 25.2.
- 2026-10-30: user checked in game that random battles aren't reduced on
  the sparkling path during the O'aka chase. Removed the "skip most
  fights / forced Amorphous Gel" claim (from Jegged); kept the directions.
- 2026-10-30: added a Making gil tip box (Moonflow section): Pilfer Gil targets ranked by Gil and Gil (stolen) from Jegged enemy pages, sell prices from accessories.yaml. Pilfer amounts not checked in game.
- 2026-10-30: Shell Shocker location conflict. Jegged bestiary and FF Wiki
  infobox say Moonflow Chapters 1-5; Gamer Guides' Chapter 1 Moonflow
  bestiary lists it; but FF Wiki's Moonflow encounter lists (fandom API,
  Moonflow_(Final_Fantasy_X)) have no Shell Shocker formation in Chapter 1,
  only a lone Shell Shocker from Chapter 2. Jegged's Chapter 1 South Bank
  Road list doesn't include it. No source names a sub-area. Gil tip now
  points Chapter 1 players at Amorphous Gel. FF Wiki: its normal attack is
  a fraction of current HP, so it can't KO.
