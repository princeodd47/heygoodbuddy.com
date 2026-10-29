# FFX-2 creature team research

Working notes behind `docs/games/final-fantasy-x-2/creature-team.md` and
`docs/games/final-fantasy-x-2/feeding.md` (`data/final-fantasy-x-2/feeding.yaml`).

Everything below is our own summary. Don't copy from sources.

**How to use:** the user has played FFX-2 many times and wants no spoiler
gating, so nothing is held back for progress. If the user reports something
different in-game, the in-game value wins. Fix the page and these notes.

Raw downloads (Jegged and Gamer Guides HTML) were saved to the session
scratchpad and parsed by `tools/build_data.py`; re-download to rebuild.

## Sources (researched 2026-10-29)

- Steam 2741975115069502725 (Hinnyuu, 2017): Chapter 1 Mascot run. Chocobo
  (Mi'ihen), Tonberry (Mushroom Rock), Red Elemental (Kilika); setups;
  grinding teams Black Chandelier (600+ EXP), Hellbreeders (2,500+ EXP, to
  ~50), No Mercy (Crystal Bangles); team at 52/54/52 after 6-8 hours;
  Shady Duo and Tonberry the Ripper warnings; Nooj hardest.
- Steam 3130541122074999501, 2971771480504122731, 1779388024827277065:
  triple Impale team, Agility is what matters, Iron Dukes from Major
  Numerus, Ray of Hope + Key to Success ~20 Iron Dukes per fight,
  Numerus drops Enterprise/Invincible without Ray of Hope.
- Jegged Tips > Best Creatures: Impale Machina catch table, Mushroom Cloud,
  Almighty Shinra, abilities worth teaching, avoid Auto-Wall with Vigor,
  Black Sky on one creature only.
- Jegged Creature Creator > Develop Creature: full feed table (data source).
- Gamer Guides Garment Grid data: creature abilities per grid (Vanguard,
  First Steps, Unerring Path, Helios Guard, Protection Halo, Ray of Hope,
  Higher Power).

## Open questions

- Steam's "Machina Scout" in the Impale trio: no such Impale creature;
  Jegged and the Fandom wiki summary say Leader, Hunter, Ranger. Scout
  Machina is a Medium creature without Impale.
- Steam claims (marked "players report" on the page): Chocobo Auto-Haste
  at 40, Tonberry innate Death Strike, Red Elemental learns MP1. Not
  checked against a second source.
- Steam says Minerva's Plate teaches Flare and Rabbit's Foot gives +100
  Luck. Both feed tables disagree (Minerva's Plate MDef +40; Rabite's Foot
  Luck +5). The +100 is probably the worn effect. Page follows the tables.
- Darkness ~9,000 per hit from a Tonberry is one Steam commenter.
- Stat caps for creatures (likely 255, 9,999 HP/999 MP without breaks)
  weren't confirmed, so the page doesn't state them.
- "Unerring Path comes with your first Special Dressphere" is Gamer
  Guides' wording ("get a Special Dressphere in Chapters 1 or 2").

## Feed table conflicts (Jegged vs Gamer Guides)

Page uses Jegged. Differences: Titanium Bangle HP +20 vs +30; Crystal
Bangle +50 vs +55; Red Ring, Snow Ring, Blue Ring, Icy Gleam, NulShock Ring
eat 1 (Jegged) vs 2; Gold Hairpin 3 vs 1; Wring Magic +30 vs +3; Key to
Success also Luck +10 (Jegged only); Heady Perfume Evasion +10 (Jegged
only). Gamer Guides lists Invincible (1, Break Damage Limit); Jegged's
develop table omits it but its accessory page has it.

## Ideas not on the page

- Fiend Tale bonus usage (Jegged): catch Flame Dragon in Ch. 1, Flan
  Blanco in Ch. 2, Mycotoxin in Ch. 3 so the free chapter-end levels go
  toward the Aeon Cup. Shiva (from Flan Blanco) is a good simulator EXP
  target.
- Stunlock build (Steam #5): Agility 200+, Quick Hit, Auto-Haste, First
  Strike, Mercurial Strike grid, Speed Bracers.
- Heavy Sallet (Large, Bikanel Ch. 5 after Cactuar Hollow) learns Quick
  Hit on its own; Logos (NG+) has Hail of Bullets.
