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

## Primalliquid Chapter 1 video (added 2026-10-29)

### Source (researched 2026-10-29)

- Primalliquid, "Final Fantasy X-2 How OVERPOWERED! Can You Get In
  Chapter 1", https://www.youtube.com/watch?v=hcxPXGfBwdk (20:12,
  uploaded 2020-11-06). Auto captions (en-orig) via yt-dlp; the user asked
  for a write-up of this video.
- Recorded on the PC version with the speed-up on. Total grind 174 h 13 m.

### Caption fixes (checked against our data files)

tom berry/tomboy = Tonberry; dive beak = Divebeak; flag/flak python = Flak
Python; hal breeders = Hellbreeders (Gug, Tindalos ×2); black chandelier =
Black Chandelier (Dark Elemental); megatonbury = Mega Tonberry (Tonberry the
Ripper); humbaba behemoth = Humbaba (Elephant Eater team); mocking a panzer
= Machina Panzer (No Mercy); alma = Elma; monotonics = Mana Tonics (Shady
Duo drop); smooth shavings = Shmooth Shailing; rabbit's foot = Rabite's
Foot; black law = Black Lore; ys alzad zero = YSLS-Zero; xanax = Zanarkand;
beaconell = Bikanel; fifa drastic = Psychic.

### Checks

- Matches our data: Psychic is the first Standard Cup prize; Abominable
  has a Ribbon gate; Chocobo Cup prizes; Youth League opens after 6 Grand
  Cup: Hard wins and its prizes (Mascot, Tetra Bracelet, Defense Bracer,
  Speed Bracer, Shmooth Shailing); Adamantite from the Machina Panzer tale;
  Crystal Bangle from Machina Panzer; Mana Tonic from Mushroom Cloud and
  Black Elemental; Black Tome from Yaibal and Black Lore from Lulu in the
  arena; 60 Supreme Gems teach Ultima; Regal Crown teaches Darkness; Dark
  Matter teaches Meteor.
- Video says "these eight monsters" but names seven (Killer Hound is later
  released). Page says seven.
- Conflict: video uses Telekinesis from creatures in Psychic; Jegged's
  Equipping Creatures page says a creature's Dressphere doesn't change its
  abilities. Flagged on the page as something to test.
- Conflict: video says Adamantite gives +100 Def/MDef; Jegged data says
  +120. Page uses the data.
- EXP figures (670, 852 Oversoul) and level-12 Telekinesis note are the
  video's own numbers.

### What went where

The user decided not to build the video's Divebeak / Flak Python / Recoil
team (they're doing the Impale Machina later), so the standalone page was
deleted. Kept on Building the Team: Meteor /
Full-Life / Turbo Black Magic / Ultima / Flare sources in What to teach,
Simulator tips and the Psychic shortcut flag (Stage 2), Adamantite chain,
and saving Speed Bracers and Shmooth Shailing for the Machina.
- 2026-10-29: user asked to drop the Luca EXP farm from the page. Added a
  tip at the top: every tournament gives a Trap Pod, win or lose.
- 2026-10-29: page restructured into 19 numbered steps in play order at
  the user's request. Team unlock counts per cup checked against
  arena.yaml: Black Chandelier and No Mercy join Standard Cup: Hard at 3
  wins, Hellbreeders at 4; Grand Cup: Hard adds Elephant Eater,
  Hellbreeders, Shady Duo and Tonberry the Ripper at 3 wins; Lulu joins
  the Youth League after 1 win. Unerring Path source corrected to Tromell
  ×4 in Macalania (was "first Special Dressphere").
- 2026-10-30: user pointed out trapping doesn't depend on where you are.
  Confirmed by Jegged's Trap Creature page (pick a location and a pod
  from the menu). Flame Dragon isn't special. Reworded step 1, removed
  the "before you leave Besaid" step, and fixed two walkthrough lines.
- 2026-10-30: Moonflow and Macalania steal/levelling tips added to step 2,
  built from bestiary.yaml (Chapter 1 enemies) and feeding.yaml counts.
- 2026-10-30: Mushroom Rock and Kilika level/steal tips added under step 4,
  from bestiary.yaml Chapter 1 entries and walkthrough chest lists. Kilika's
  Chapter 1 enemies all belong to the end-of-chapter heist.
- 2026-10-30: user confirmed in game that a creature's Dressphere ADDS
  its abilities (Thief: Mug, Psychic: Telekinesis) without removing
  existing ones. Jegged's "doesn't change their abilities" is wrong (or
  means it doesn't remove them). Fixed Creatures page and step 3/step 7.
  Psychic recommendation for the starter team: Chocobo (most turns, Magic
  and MP), all three for the Black Chandelier farm.
- 2026-10-30: user says the step 6 note was wrong: teams open in the
  Simulator once you've battled them in a tournament. Dropped the
  per-win-count unlock wording (from Jegged's "Unlock Conditions") in
  step 6.
- 2026-10-30: same rewording in step 9 (Grand Cup: Hard teams), at the user's request.
- 2026-10-30: added Fayth fragments subsection (step 17) with all eight, trap windows from creatures.yaml, and how to release (5 Story Levels, Creature History message) from Jegged's Creature History page.
