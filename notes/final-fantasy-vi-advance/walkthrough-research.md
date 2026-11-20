# FF6 Advance walkthrough: research notes

Notes behind hand-written walkthrough text in `wt_content.py`. Reworded from
the sources; nothing here is quoted.

## 1.9 Lethe River: raft forks (2026-11-18)

- Caves of Narshe, chapter 1-9
  (<https://www.cavesofnarshe.com/ff6/walkthrough.php?chapter=1-9>), is the
  most detailed source. It maps every branch and the encounters on each:
  - A fight, then fork 1: Straight / Left / Right. All three end at a small
    cave with a save point.
    - Straight: most fights; best route for meeting a Lesser Lopros.
    - Left: fewest fights, can be none.
    - Right: in between.
  - After the save point, a fight, then fork 2: Up / Left.
    - Up: a run of fights that loops back to the same fork.
    - Left: one possible fight, then a cave with a second save point, then a
      short stretch to Ultros.
  - No chests on the river. Ultros gives no EXP or Gil.
- GamerGuides' Lethe River page agrees on fork 2 (Up loops, Left goes on)
  and says fork 1's choice doesn't matter beyond the number of fights; no
  chests.
- Thonky: "take a left whenever you're asked"; two save points; no chests.
- The user asked for the forks to show which lead to chests. No source lists
  a chest on the river, so the box says there's no treasure. If the user
  sees one in game, in-game data wins.

## 1.17 South Figaro Cave: Thunder Rod or Hero's Ring (2026-11-18)

From this guide's own data (data.json equipment and chest lists):

- Hero's Ring sources: Dragon's Neck cabin pot (1.21, World of Balance);
  the South Figaro Cave north-east chest in the World of Ruin, only if it
  wasn't opened for the Thunder Rod in Locke's scenario; the Jidoor auction
  in the World of Ruin (50,000 Gil, once); Zone Eater's Belly; Kefka's Tower
  (party 3). Colosseum: a Guard Bracelet bet fights a Demon Knight for a
  Hero's Ring, and a Hero's Ring bet wins a Guard Bracelet back, so it's a
  swap, not a farm. Guard Bracelets: one World of Ruin Narshe chest,
  Wrexsoul's drop, Fiend Dragon steal, Metamorph.
- Thunder Rod: also sold in Thamasa (World of Balance) and stolen from
  Wizards.
- Stacking (equipment notes): Hero's Ring is +25% physical and magic; the
  magic part stacks with Earrings and other Hero's Rings, the physical part
  doesn't stack with a Gigas Glove or a second Hero's Ring. Earring is +25%
  magic, +50% with two. The user confirmed Earring x2 and Earring + Hero's
  Ring stack in game, and Gigas Glove doesn't stack with itself or a Hero's
  Ring.
- Blitzes: Raging Fist and Meteor Strike are physical; Aura Cannon and
  Rising Phoenix are magic (data.json blitzes).

## Scenario order and the first Veldt trip (2026-11-18)

Question: play Sabin's scenario first (fewer groups in the Veldt pool) or
last (more Rages on the first trip)?

- Veldt rules (Gamer Corner Veldt Tool,
  <https://guides.gamercorner.net/ffvi/veldt>, and the FF6T Veldt
  Encounter Guide): 64 groups, visited in order, one fight per group;
  groups with no formation you've seen are skipped. Within a group a
  random formation is picked; an unseen one passes to the next in the group.
  Fighting off the Veldt rerolls the pick; loading a save shifts the group.
- Guard Leader (SNES "Marshal") is only in group 1, as "2 Lobos, Marshal",
  1 of 8 formations. All 8 are already seen by 1.9 (Narshe, 1.3's
  Leafers/Dark Winds), so Terra's Leaf Bunnies don't dilute it.
- Seen monsters per chapter from data.json `en` lists, mapped to SNES names
  through the Rage list's `snes` field; a formation counts as seen if all
  its monsters were met (an approximation).
- Groups in the cycle at the first Veldt trip: 15 with Sabin first, 18 with
  Sabin last (Locke adds Commanders/Vector Pups/Gold Bear groups, Terra the
  Wild Rat/Dark Side group). Expected Veldt fights per Guard Leader: about
  15 × 8 = 120 vs 18 × 8 = 144. Every other Rage slows by the same 20%.
- The extra Rages from Terra and Locke include no top picks (good: Eukaryote,
  Darkside, Heavy Armor, Acrophies, Gold Bear).

## Sabin's scenario first (2026-11-18)

The user chose to play Sabin's scenario first (see the Veldt analysis
above). Chapters were renumbered to read in that order: Caves of Narshe's
1-11..1-15 (Sabin) are 1.10–1.14 here, and its 1-10 (Terra) is 1.15. Locke
keeps 1.16–1.17. No Rage or Lore moves between chapters: the only enemy
Terra's and Sabin's chapters share is Apparition, which has no Rage.
`tools/walkbuild.py` still uses Caves of Narshe's ids, so a rebuild with it
would need the same remap.
- Veldt boxes (`veldt` in data.json, built by walkbuild.py from chapter
  order): with Sabin first, Darkside and Eukaryote (Terra, 1.15) moved from
  1.13's list to 1.36's. 1.13 now lists 12 Rages: Guard Leader, Lesser
  Lopros, Stray Cat, Templar, Bomb (top picks) and Magitek Armor, Mu,
  Trillium, Gorgias, Cirpius, Doberman, Ghost (worth learning).
- "Most turn up within 20 to 40 battles": the per-Rage expectations from the
  analysis above with 15 groups (Templar ~22, Stray Cat ~22, Lesser Lopros
  ~30); Bomb ~6.
- 1.20's optional Veldt trip got its own Veldt box (2026-11-18): the top
  picks and worth-learning Rages first met in 1.14–1.20 (Aspiran, Anguiform,
  Darkside, Eukaryote, Heavy Armor, Gold Bear, Acrophies), with 1.13's list
  as "earlier ones". 1.36 now lists those seven among its earlier ones.
  None of the Battle for Narshe Rages are rated.

## Aspiran's Gigavolt (2026-11-18)

The user thought Gigavolt helps against Ifrit and Shiva (1.31). The guide's
data says both nullify Lightning (and Poison, Wind, Holy, Earth, Water), so
it doesn't; Ifrit is weak to Ice and Shiva to Fire. Lightning-weak enemies
after 1.20, from data.json: Ultros (1.25, 1.43); Sergeant, Proto Armor,
Mega Armor, Belzecue, Onion Knight, Trapper and Crane (Right) in Vector and
the Magitek Research Facility (1.28–1.34); Joker, Devourer, Ninja elsewhere.
The tip in 1.20 says where it pays off, and 1.31's strategy says to save
Lightning for the soldiers and armor on the way in.
- Follow-up: the user pointed out Gau's Rages pick their own target, so in
  the Ifrit + Shiva fight he must avoid Fire and Ice too (each absorbs one).
  Both nullify every other element (data.json and the wiki agree: Lightning,
  Wind, Earth, Water, Poison, Holy). Physical Rages available by 1.31:
  Stray Cat's Cat Scratch (×4, top pick), Gold Bear's Gouge (×2.5),
  Doberman's Bite (×1.5). Shiva had no boss card in 1.31; added.

## Magic AP (2026-11-18)

The points that teach Esper spells are "Magic AP" in the GBA version: the
user confirmed the battle results say "Earned 5 magic AP." The SNES called
them Magic Points (FF Wiki, "Ability Points"), which clashes with MP. The
guide now says Magic AP everywhere (1.36 Intangir tip, the Esper spell tip,
Terra's Trance note, the Espers and Bestiary intros), and the Espers intro
mentions the SNES name. Per the wiki, Magic AP is set per enemy formation,
not per monster.

## Back-row tips (2026-11-19)

The user asked for a back-row tip where each character joins for good in the
World of Balance (not the World of Ruin; by then the player knows it), linking
to the Tips tab's Rows section with `{t:See Tips|rows}` (the `|id` part
scrolls the Tips tab to that heading).

- Added: Edgar (1.4, Tools), Sabin (1.7, Blitz), Cyan (1.10, Bushido Fang,
  which ignores defense, per the user), Setzer (1.26, his weapons), Strago
  (1.42, Lores/magic), Relm (1.43, magic).
- Skipped: Locke, Celes and Terra rely on Fight. Gau: unconfirmed whether
  Rage attacks are halved in the back row. Mog: the walkthrough doesn't mark
  where he joins for good in the World of Balance. Shadow only joins for good
  in the World of Ruin.
- walkbuild.py needs the uncommitted raw/ downloads, so the six chapters'
  boxes were copied from wt_content.py into data.json's walk entries directly.

## Notable steals (2026-11-19)

The user asked for a note on Galypdes' rare Celestriad steal in Phoenix Cave
(the easiest source), and a steal note in each chapter with notable steals:
rare or unique relics, and equipment that's an upgrade or rare. Picked from
data.json (walk `en` lists, monster steal slots, equipment `loc`), first
chapter each enemy appears:

- Added: Harvester Dragoon Boots (1.23), Don Tiger Mask (1.27), Chimera
  Hyper Wrist (1.36), Ninja Angel Wings (1.38), Flame Eater Flametongue
  (1.42 boss), Dragon Genji Glove / Misfit Alarm Earring (1.48), Glasya
  Labolas Muscle Belt / Devil Fist Brigand's Glove (2.22), Baalzephon
  Sasuke / Shambling Corpse Soul Sabre (2.36), Galypdes Celestriad (2.37),
  Magic Master Crystal Orb (2.41 boss), Great Behemoth Tigerfang / Fiend
  Dragon Guard Bracelet (2.42), Dark Behemoth Behemoth Suit (3.2).
- Already in the text: Dadaluma Thief's Bracer, Hill Gigas Gigas Glove,
  Tunnel Armor Air Knife, Number 024, Number 128 Kazekiri, Guardian Ribbon,
  Hidon, Wrexsoul, Samurai Soul, Holy Dragon, Fiend.
- Left out: steals sold in shops at that point (Mythril gear, Twist
  Headband, Amulet, Earring, Diamond gear, Golden Spear), Tonberries'
  Minerva Bustier (also its drop), Punisher's Bone Club (Umaro can't change
  weapons), Masamune (Murakumo is stronger and already noted).
- Rare slot odds (1 in 8 successful steals) are from the Steal tab's text.
- In the World of Ruin nobody can Steal until Gogo (2.36) or Locke (2.37)
  joins, so the 2.22 note says to come back.

## Boss card text (2026-11-19)

The boss cards already show Weak, Absorbs, Steal and Drop, so the user asked
that strategies stop repeating them. Removed those mentions from every boss
strategy (wt_content.py and data.json); kept what the card doesn't show:
nullified elements (Ifrit/Shiva), other enemies' weaknesses (Ipooh, the right
Crane), and the Vargas steal timing. Bosses left with no text (Nelapa, Death
Warden, Samurai Soul) render no paragraph.

Guardian (2.45): data.json had Lightning and Water as absorbs, copied from
Caves of Narshe's stat table. Gamer Corner and the Final Fantasy Wiki both
list them as weaknesses (as does CoN's own strategy text). Fixed in
data.json; see bestiary-research.md.

## World of Ruin order for stealing (2026-11-19)

The user wants as few missed steals as possible in the World of Ruin, so
Gogo comes before any boss with a one-time steal. Nobody can Steal until
Gogo or Locke joins; Dullahan (Genji Glove) comes before the airship, so
that steal can't be had.

- New order after the airship (2.12): Gau on the Veldt (2.13), Narshe
  (2.14), the Narshe mines for Mog and Molulu's Charm (2.15), Umaro's Cave
  (2.16, Yeti is level 33), the Zone Eater for Gogo (2.17), then the rest in
  the old order. Old → new: 2-24→2-13, 2-16→2-14, 2-19→2-15, 2-18→2-16,
  2-36→2-17, 2-13..2-15→2-18..2-20, 2-17→2-21, 2-20..2-23→2-22..2-25,
  2-25..2-35→2-26..2-36. 2.37 onward unchanged.
- Rages, Lores and the Veldt box were recomputed for the new order with
  walkbuild.py's rules (lore availability keyed to Strago rejoining, now
  2.30). Every Rage and Lore is still assigned once; World of Balance
  chapters are unchanged. Self-Destruct (Zone Eater) now shows under
  Strago's chapter as an earlier Lore.
- Zone Eater enemies are level 43-44 (Daryl's Tomb: 29-30); Covert can't
  be run from (Gamer Corner) and is immune to Death, so Banish fails. Mog
  wearing Molulu's Charm avoids every random battle there; the dungeon has
  no boss.
- Gogo's commands: per the Final Fantasy Wiki, Gogo loses a command only if
  its owner never joined (Throw if Shadow was left behind, Dance until Mog
  joins), so Steal is available before Locke rejoins.
- Lone Wolf is in the World of Balance (user confirmed; the wiki says after
  the Magitek Research Facility, back in Narshe), so the choice moved from
  the old 2-19 to 1.37 with a recommendation to save Mog (the Gold Hairpin
  is also found at Mt. Zozo and the Ancient Castle). In the World of Ruin
  Mog is in the moogles' lair in the Narshe mines; Molulu's Charm is in the
  wall behind him, with nothing marking it (user).
- Added Mog's back-row tip to 1.37 (Dance ignores row).
- Shopping advice needs a reason. Cut as unexplained (user): Smoke Bombs at
  Nikeah (1.14; L+R already runs), Potions and Tents in Narshe (1.3), and
  Flame Scrolls in Kohlingen (1.21). The Nikeah Silk Robes stay: they're
  gear for the Narshe battle (1.18) (user).
