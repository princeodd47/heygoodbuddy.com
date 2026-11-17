---
platform: SFC
spoilers: none
status: draft
tags:
  - Treasure of the Rudras
---

# Bestiary

Bosses are listed by chapter in the order you fight them. Other enemies are
grouped by area, roughly in the order you reach them. Mantras that hit each
element are on [Mantras](mantras.md).

## Bosses

{% for c in rudras_bosses.chapters %}
### {{ c.name }}

| Boss | Day | Where | HP | Weak | Drops |
|------|----:|-------|---:|------|-------|
{% for b in c.bosses -%}
| **{{ b.name }}**{% if b.note %}<br>*{{ b.note }}*{% endif %} | {{ b.day or "—" }} | {{ b.where }} | {{ b.hp }} | {{ b.weak or "—" }} | {{ b.drops or "—" }} |
{% endfor %}
{% endfor %}

## Enemies

{% for a in rudras_monsters.areas %}
### {{ a.area }}

| Enemy | Level | HP | EXP | Ragu | Weak | Drops |
|-------|------:|---:|----:|-----:|------|-------|
{% for m in a.monsters -%}
| **{{ m.name }}**{% if m.note %}<br>*{{ m.note }}*{% endif %} | {{ m.level }} | {{ m.hp }} | {{ m.exp }} | {{ m.ragu }} | {{ m.weak or "—" }} | {{ m.drops or "—" }} |
{% endfor %}
{% endfor %}

## Sources

- Boss HP, weaknesses and drops:
  [God Bird's boss data](https://god-bird.net/data/rudra/bossdata_sion.html)
  (Japanese).
- Enemy levels, HP, EXP and Ragu: Kurt Reonis's
  [Monster List](https://gamefaqs.gamespot.com/snes/564407-rudra-no-hihou/faqs/32313).
- Enemy drops and weaknesses: Trunkz0r's guide, in
  [Kurt's unedited walkthrough](http://www.reonis.com/rudra/Rudra_No_Hihou_Walkthrough.txt),
  [God Bird's rare items](https://god-bird.net/data/rudra/item.html)
  (Japanese) and [Bluewing's Dune chapter](https://bluewing.usamimi.info/gamecap/rudora/c_dune.html)
  (Japanese).
