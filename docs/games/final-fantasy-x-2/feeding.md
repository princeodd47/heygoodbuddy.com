---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy X-2
---

# Feeding

Creatures learn abilities and gain stats by eating items. Open the main
menu, pick **Creature**, choose the creature, then the feed option. The
Creature Creator's "Develop Creature" just sends you to the same menu.

- **Qty** is how many it eats at once. The whole stack goes in one
  feeding, and you get the ability and the stat gain once.
- Stat gains are base values. Each creature scales them by its own growth,
  so the same item can give one creature more than another.
- Everything you feed is used up. Don't feed an accessory you can't get
  back, like a Ribbon.
- The same menu can make a creature **forget** an ability. Creatures pick
  their own actions, so a short list of good moves beats a long one.
- Creatures also learn some abilities by being hit by them in battle.

Accessories can be fed too. Their **Feed** column is on the
[Accessories](accessories.md) page. For which abilities are worth it, see
[Building the Team](creature-team.md#step-3-equip-and-feed-them).

## Feeding gains

No guide documents the exact formula, but this much is known:

- **The gain goes into the creature's base stat.** Anything worn that
  raises the stat by a percentage then multiplies it. A creature wearing a
  Crystal Bangle (Max HP +100%) shows about twice the HP gain, but only
  the base amount is really added. Wearing the bangle while you feed
  doesn't make feeding more efficient.
- **The shown gain can be wrong until you leave the menu.** In our game a
  Crystal Bangle showed +120 HP on the feeding screen, and the number
  changed after we exited. Check the stat again after leaving.
- **Gains vary by creature and can shrink as HP rises.** One player reports
  +137 HP per Crystal Bangle on a Tonberry and +40 on a Coeurl. In our
  game, a level 60 Red Elemental at about 1,100 base HP got +120 from one
  Crystal Bangle (shown with one worn), and once it reached 9,999 HP
  wearing a bangle the same feed gave only +42.
- **HP feeding greys out at 9,999.** The cap (without Break HP Limit,
  1 Enterprise) is on the HP the creature shows, gear included. Once a
  creature shows 9,999 the HP items are greyed out and you can't feed
  them any more. Take the Crystal Bangle off to keep raising its base HP.

## Items

| Item | Qty | Teaches | Type | Stat gain |
|------|----:|---------|------|-----------|
{% for i in ffx2_feeding['items'] -%}
| **{{ i.name }}** | {{ i.qty }} | {{ i.teaches or "—" }} | {{ i.type or "—" }} | {{ i.gain or "—" }} |
{% endfor %}

## Sources

- Quantities, abilities and stat gains:
  [Jegged's Develop Creature page](https://jegged.com/Games/Final-Fantasy-X-2/Creature-Creator/Develop-Creature.html),
  checked against the
  [Gamer Guides item list](https://www.gamerguides.com/final-fantasy-x-2/guide/creature-create/creature-buildup/item-based-augmentation).
- How gains work: our own game, the
  [Steam Creature Creator effects guide](https://steamcommunity.com/sharedfiles/filedetails/?id=898744691)
  and its comments, and a
  [GameFAQs thread](https://gamefaqs.gamespot.com/boards/643146-final-fantasy-x-x-2-hd-remaster/69219900)
  on HP feeding.
