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
[Building the Team](creature-team.md#what-to-teach).

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
