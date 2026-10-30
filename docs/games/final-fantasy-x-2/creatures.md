---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy X-2
---

# Creatures

How trapping works, what releasing a creature unlocks, and where every
creature can be trapped.

## Trap Pods

| Pod | Catches |
|-----|---------|
| **Trap Pod S** | A random Small creature from that location |
| **Trap Pod M** | A random Medium creature |
| **Trap Pod L** | A random Large creature |
| **Trap Pod SP** | A random creature of the family you pick (Machina, Elemental, Humanoid and so on). The only pod that can catch people. |

- Shinra's Creature Creator tutorial on your first Celsius visit gives a
  Trap Pod S, M and L. You can hold eight.
- **Getting more:** play any Fiend Arena tournament (win or lose), release
  a creature whose story is finished, or finish Chapters 1 to 4 (three SP
  pods each).
- **Free pods:** with none left, back out of Trap Creature and the game
  gives you a Trap Pod S or M.
- One pod per location at a time. Round it up before setting another
  there.
- You can hold eight creatures. Release one to make room.

## Sizes and the party

A party is worth three slots. Yuna, Rikku, Paine and Small creatures take
one, Medium creatures take two, and Large creatures take all three.
Creatures act on their own. The 1 to 5 star cheer gauge in battle nudges
how aggressive they are, but young creatures mostly ignore it.

Every creature needs a **Garment Grid** and a **Dressphere** before it can
fight. The Dressphere can't be changed in battle. It changes the
creature's stats and adds that Dressphere's abilities (Thief adds Mug,
Psychic adds Telekinesis) without removing any it already has. The
Garment Grid gives
the creature its own set of abilities, which are different from what the
grid gives Yuna, Rikku and Paine.

## Fiend Tales and releasing

- A creature joins at about your party's average level, and its Fiend Tale
  gains a Story Level each time it gains a level. A tale has 3 to 5 Story
  Levels.
- The end of each of the first four chapters, and every cup you win,
  gives all your creatures a free Story Level.
- A creature that joins at level 99 can never level, so its tale can never
  finish. Catch tale creatures early, or in New Game Plus, where creatures
  carry over at level 1 with their abilities.
- **Releasing** a creature with a finished tale plays its ending and gives
  you a Trap Pod. Some releases unlock more:

| Release | Unlocks |
|---------|---------|
| **Flame Dragon** | Ifrit in the arena |
| **Flan Blanco** | Shiva in the arena |
| **Mycotoxin** | Valefor in the arena |
| **Machina Striker** | Ixion in the arena |
| **Azi Dahaka** | Bahamut in the arena |
| **Critical Bug** | Yojimbo in the arena |
| **Aranea** | Anima in the arena |
| **Jumbo Cactuar** | The Magus Sisters in the arena |
| **Daeva** | Becomes Aka Manah |
| **Aka Manah** | Becomes Aeshma |
| **Aeshma** | Becomes Jahi |
| **Jahi** | Starts Shinra's "Capture the Fiend Traitor!" mission; Tomb can now be trapped |
| **Tomb** | Dolmen can now be trapped |
| **Dolmen** | Monolith can now be trapped |
| **Monolith** | Becomes Ultima Weapon |
| **Ultima Weapon** | Starts the "Fiend Deathmatch!" mission and opens the Fiend Portal |
| **Omega Weapon** | Opens the Almighty Shinra Cup |
| **Almighty Shinra** | Gives the Last Resort Garment Grid |
| **Haizhe** | Deep Haizhe can now be trapped |
| **Killer Hound** | YSLS-Zero can now be trapped |
| **YSLS-Zero** | Machina Panzer can now be trapped |
| **Spine Drake** | Balivarha can now be trapped |

The first eight have a **Fayth fragment** instead of a story. Release all
eight to open the Aeon Cup. Releasing other creatures adds their teams to
the arena; see the "Appears after" column on the
[Fiend Arena](fiend-arena.md) page.

## Easy to miss

- **Flame Dragon** (for the Aeon Cup): Trap Pod L in Besaid, Chapters 1 to
  4. In Chapter 5 it's only a rare Large catch in Luca.
- **Bevelle in Chapter 2 only:** Kukulcan, YAC-13, YAU-28 and YSLS-99.
- **Gone once a Chapter 5 area opens:** Zalamander (Thunder Plains, before
  the New Cave), Lich (Djose, before the Farplane), Pop Fry and Aculeate
  (Bikanel, before Cactuar Hollow), and Yaibal and Elma (Mushroom Rock,
  before the Den of Woe).
- **Youth League only:** Lucil, Elma and Yaibal (Chapters 2 to 4) need the
  Awesome Sphere to have gone to the Youth League.
- **New Game Plus only:** Leblanc, Logos and Ormi (Guadosalam), Lulu
  (Besaid) and Kimahri (Mt. Gagazet), all with a Trap Pod SP.

## Where to trap them

**Size** is the pod to use. Each line under **Where** is a location, the
pods that work there (SP shows the family to pick), and the chapters. A
creature listed under Luca can also be caught there, but Luca's list is so
long that the odds are poor.

| Creature | Size | Where |
|----------|------|-------|
{% for c in ffx2_creatures.creatures -%}
| **{{ c.name }}** | {{ c.size }} | {{ c.where }} |
{% endfor %}

Not trapped at all: Seymour, Auron and Tidus (Farplane Cup), Omega Weapon
(Fiend Portal), Almighty Shinra (his own cup), and Aka Manah, Aeshma, Jahi
and Ultima Weapon (from releases).

## Sources

- Trap Pods, locations, releases and Fiend Tales:
  [Jegged's Creature Creator section](https://jegged.com/Games/Final-Fantasy-X-2/Creature-Creator/Overview.html),
  checked against the
  [Gamer Guides creature lists](https://www.gamerguides.com/final-fantasy-x-2/guide/creature-create/the-basics/small-creatures).
