---
platform: SFC
spoilers: none
status: draft
tags:
  - Lufia II
fg:
  list:
    merge: true
    group: Type
    group_label: Type
    show: [Element, MP, Price, Effect]
    sort: [MP, -MP, Price, -Price]
    chips: Element
    chips_label: Element
    chips_style: elements
    placeholder: Name, effect, town, character
---

# Magic

Every spell, in the order shops first sell them. Spells are bought in town
magic shops, and each one is learned only by the characters listed. Guy and
Dekar can't learn magic. Open a spell for who can learn it and where it's
sold. Gear can also cast some spells as an IP: see [IP Attacks](ip-attacks.md).

{% for g in lufia2_magic.groups %}
## {{ g.type }}

| Spell | Element | MP | Price | Effect | Who | Where |
|-------|---------|---:|------:|--------|-----|-------|
{% for s in g.spells -%}
| **{{ s.name }}** | {{ s.element or "—" }} | {{ s.mp }} | {{ s.price }} | {{ s.effect }} | {{ s.who }} | {{ s.where }} |
{% endfor %}
{% endfor %}

## Sources

- Spells, MP, prices, who learns them and where they're sold:
  [RPGClassics' Lufia 2 shrine](http://www.rpgclassics.com/shrines/snes/lufia2/).
- Spell elements:
  [Almar's Guides](https://www.almarsguides.com/retro/walkthroughs/snes/games/lufiaii/misc/lists/spells/).

<script type="application/json" id="fg-cards-data">{{ {"bestiary": lufia2_bestiary, "equipment": lufia2_equipment, "items": lufia2_items, "magic": lufia2_magic, "ip": lufia2_ip} | tojson }}</script>
