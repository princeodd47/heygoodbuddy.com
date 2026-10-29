---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy X-2
---

# Accessories

All 128 accessories, grouped by type. **Effect** is what it does when Yuna,
Rikku or Paine wears it. **Feed** is how many a creature has to eat and
what it gets: an ability, a stat gain or both (see [Feeding](feeding.md)).
**Sell** is in gil. **Where** lists chests, shops, steals, drops, bribes and
prizes; *Fiend Arena* means the enemy or prize is in the
[Fiend Arena](fiend-arena.md).

Accessories work differently on a creature that wears one rather than eats
it, so check the in-game description before relying on one.

{% for c in ffx2_accessories.categories %}
## {{ c.name }}

| Accessory | Effect | Feed | Sell | Where |
|-----------|--------|------|-----:|-------|
{% for a in c.accessories -%}
| **{{ a.name }}** | {{ a.effect | replace("; ", "<br>") }} | {{ a.feed or "—" }} | {{ a.sell or "—" }} | {{ a.where or "—" }} |
{% endfor %}
{% endfor %}

## Sources

- Effects, sell prices and where to get each one:
  [Jegged's accessory list](https://jegged.com/Games/Final-Fantasy-X-2/Accessories/).
- Feed amounts:
  [Jegged's Develop Creature page](https://jegged.com/Games/Final-Fantasy-X-2/Creature-Creator/Develop-Creature.html),
  checked against the
  [Gamer Guides accessory list](https://www.gamerguides.com/final-fantasy-x-2/guide/creature-create/creature-buildup/accessory-based-augmentation).
