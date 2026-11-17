---
platform: SFC
spoilers: none
status: draft
tags:
  - Lufia II
fg:
  list:
    merge: true
    group: Area
    show: [Level, HP, EXP, Gold, Weak]
    sort: [Level, -HP, -EXP, -Gold]
    chips: Weak
    chips_label: Weak to
    chips_style: elements
    elements: [Strong]
    placeholder: Name, drop, area
---

# Bestiary

Every enemy and boss, each listed once. Search by name, drop or area, pick an
area to see only what's there, or sort by level, HP, EXP or gold. Open a row
for its drop, what it resists and every area it's found in. **Overworld**
means the fields around that town.

**Drop** is the item and the chance it drops. **Weak** takes extra damage
from that element or weapon type, and **Strong** takes half. Hard, Flying,
Insect, Dragon and similar entries are weapon types: some weapons hit those
enemies harder. See the [Walkthrough](walkthrough.md) for boss strategy.

*Check in game: drop chances come from one guide, and another gives
different numbers for some monsters.*

{% for a in lufia2_bestiary.areas %}
## {{ a.area }}

{% if a.monsters %}
| Enemy | Level | HP | EXP | Gold | Drop | Weak | Strong |
|-------|------:|---:|----:|-----:|------|------|--------|
{% for m in a.monsters|sort(attribute='level') -%}
| **{{ m.name }}** | {{ m.level }} | {{ m.hp }} | {{ m.exp }} | {{ m.gold }} | {{ m.drop or "—" }} | {{ m.weak or "—" }} | {{ m.strong or "—" }} |
{% endfor %}
{% endif %}
{% if a.bosses %}
| Boss | HP | Drop | Weak | Strong |
|------|---:|------|------|--------|
{% for b in a.bosses -%}
| **{{ b.name }}**{% if b.note %}<br>*{{ b.note }}*{% endif %} | {{ b.hp }} | {{ b.drop or "—" }} | {{ b.weak or "—" }} | {{ b.strong or "—" }} |
{% endfor %}
{% endif %}
{% endfor %}

## Sources

- Levels, HP, EXP, gold, drop chances and weaknesses: Iron Knuckle's
  [Lufia II walkthrough](https://gamefaqs.gamespot.com/snes/588451-lufia-ii-rise-of-the-sinistrals/faqs/11045)
  (GameFAQs).
- Which enemies appear where: the monster list on
  [RPGClassics' Lufia 2 shrine](http://www.rpgclassics.com/shrines/snes/lufia2/).

<script type="application/json" id="fg-cards-data">{{ {"bestiary": lufia2_bestiary, "equipment": lufia2_equipment, "items": lufia2_items, "magic": lufia2_magic, "ip": lufia2_ip} | tojson }}</script>
