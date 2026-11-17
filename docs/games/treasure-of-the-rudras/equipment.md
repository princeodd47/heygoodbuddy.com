---
platform: SFC
spoilers: none
status: draft
tags:
  - Treasure of the Rudras
---

# Equipment

Each table is sorted from weakest to strongest. Elements come in opposing
pairs: fire and water, wind and lightning, holy and dark.

- **Armor with an element** halves damage of that element and **doubles
  damage of the opposite element**. Dark armor also blocks Pollution, and
  wind armor stops Float from working.
- **Weapons with an element** do double damage to an enemy weak to it, and
  half to an enemy of the same element.

The item descriptions in the game call holy "Light" and lightning "Thunder".

**Where** gives the chapter and day: **S** Sion, **Su** Surlent, **R** Riza,
**D** Dune. S4 means Sion's Day 4. A town means its shop, anywhere else means
a chest, and "Drop" means an enemy drops it. See the [Bestiary](bestiary.md)
for drops.

## Weapons

{% for g in rudras_equipment.weapons %}
### {{ g.type }}

| Weapon | Attack | Element | Notes | Sells | Where |
|--------|-------:|---------|-------|------:|-------|
{% for i in g['items'] -%}
| **{{ i.name }}** | {{ i.atk }} | {{ i.elem or "—" }} | {{ i.notes or "" }}{% if i.mdef %}{{ ", " if i.notes }}MDef {{ i.mdef }}{% endif %} | {{ i.sell or "—" }} | {{ i.where or "—" }} |
{% endfor %}
{% endfor %}

## Armor

Buy prices are only known for gear with an element.

{% for g in rudras_equipment.armor %}
### {{ g.type }}

| Item | Def | MDef | Element | Notes | Buys | Sells | Where |
|------|----:|-----:|---------|-------|-----:|------:|-------|
{% for i in g['items'] -%}
| **{{ i.name }}** | {{ i.def }} | {{ i.mdef or 0 }} | {{ i.elem or "—" }} | {{ i.notes or "" }} | {{ i.buy or "—" }} | {{ i.sell or "—" }} | {{ i.where or "—" }} |
{% endfor %}
{% endfor %}

## Sources

- Stats and sell prices: Kurt Reonis's
  [Item List](https://gamefaqs.gamespot.com/snes/564407-rudra-no-hihou/faqs/31921).
- Buy prices and where elemental gear turns up in each chapter:
  [God Bird's elemental armor list](https://god-bird.net/data/rudra/armor.html)
  (Japanese).
- Hidden items and rare drops:
  [God Bird's rare items](https://god-bird.net/data/rudra/item.html) (Japanese).
- How elements work: [God Bird's strategy hints](https://god-bird.net/data/rudra/rudraguide.html)
  (Japanese).
- Other locations: [Kurt's walkthroughs](http://www.reonis.com/rudra/), based
  on Trunkz0r's guide.
