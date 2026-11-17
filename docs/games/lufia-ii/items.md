---
platform: SFC
spoilers: none
status: draft
tags:
  - Lufia II
fg:
  subtabs: true
  list:
    show: [Price, Effect]
    sort: [Price, -Price]
    placeholder: Name, effect, shop
---

# Items

Grouped by type, in the order you can first buy or find each item. **First**
is the first shop that stocks it. Shops charge the same everywhere. Fruit
use is on [Capsule Monsters](capsule-monsters.md).

{% for g in lufia2_items.groups %}
## {{ g.type }}

{% if g.note %}{{ g.note }}

{% endif -%}
| Item | Price | Effect | First |
|------|------:|--------|-------|
{% for i in g['items'] -%}
| **{{ i.name }}** | {{ i.price }} | {{ i.effect or "—" }} | {{ i.first }} |
{% endfor %}
{% endfor %}

## Sources

- Prices, shops and effects:
  [RPGClassics' Lufia 2 shrine](http://www.rpgclassics.com/shrines/snes/lufia2/).
- Fruit drops: Iron Knuckle's
  [Lufia II walkthrough](https://gamefaqs.gamespot.com/snes/588451-lufia-ii-rise-of-the-sinistrals/faqs/11045)
  (GameFAQs).
- Cider effects: the same walkthrough and the GameFAQs
  [shop guide](https://gamefaqs.gamespot.com/snes/588451-lufia-ii-rise-of-the-sinistrals/faqs/21868)
  and [FAQ](https://gamefaqs.gamespot.com/snes/588451-lufia-ii-rise-of-the-sinistrals/faqs/5547).

<script type="application/json" id="fg-cards-data">{{ {"bestiary": lufia2_bestiary, "equipment": lufia2_equipment, "items": lufia2_items, "magic": lufia2_magic, "ip": lufia2_ip} | tojson }}</script>
