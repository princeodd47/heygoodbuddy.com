---
platform: SFC
spoilers: none
status: draft
tags:
  - Lufia II
---

# Bestiary

Enemies grouped by area, in the order you reach each area. Within an area
they're sorted by level. **Overworld** means the fields around that town.
Bosses for each area are listed after its enemies.

**Drop** is the item and the chance it drops. **Weak** takes extra damage
from that element or weapon type, and **Strong** takes half. Hard, Flying,
Insect, Dragon and similar entries are weapon types: some weapons hit those
enemies harder. See the [Walkthrough](walkthrough.md) for boss strategy.

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
