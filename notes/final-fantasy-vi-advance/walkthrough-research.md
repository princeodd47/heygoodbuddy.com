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
