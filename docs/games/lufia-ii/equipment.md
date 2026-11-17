---
platform: SFC
spoilers: none
status: draft
tags:
  - Lufia II
fg:
  subtabs: true
  list:
    show: [Stats, IP, Price]
    sort: [-Stats, Price]
    chips: Who
    chips_label: Who can equip
    chip_values: [Maxim, Tia, Guy, Selan, Dekar, Lexis, Artea]
    aliases:
      All: [Maxim, Tia, Guy, Selan, Dekar, Lexis, Artea]
      Women: [Tia, Selan]
    placeholder: Name, stat, IP attack, place
---

# Equipment

Every table is in the order you can first get each item. **Price** is the
shop price; anything sells for half. **IP** is the IP attack the item gives
when equipped. **Where** names a shop town, a dungeon for a chest, or
**Drop:** for an enemy drop. The Forfeit Island shop sells everything you've
ever owned, so lost gear can be bought back there.

Characters are Maxim, Tia, Guy, Selan, Dekar, Lexis and Artea.

{% for key, title in [('weapons', 'Weapons'), ('armor', 'Armor'), ('shields', 'Shields'), ('helmets', 'Helmets'), ('rings', 'Rings'), ('jewels', 'Rocks and Jewels')] %}
## {{ title }}

| Item | Stats | IP | Price | Who | Where |
|------|-------|----|------:|-----|-------|
{% for i in lufia2_equipment[key] -%}
| **{{ i.name }}** | {{ i.stats or "—" }} | {{ i.ip or "—" }} | {{ i.price or "—" }} | {{ i.who or "All" }} | {{ i.where or "—" }} |
{% endfor %}
{% endfor %}

## Sources

- Stats, IP attacks, prices, who can equip and where:
  [RPGClassics' Lufia 2 shrine](http://www.rpgclassics.com/shrines/snes/lufia2/),
  checked against Iron Knuckle's
  [Lufia II walkthrough](https://gamefaqs.gamespot.com/snes/588451-lufia-ii-rise-of-the-sinistrals/faqs/11045)
  (GameFAQs).

<script type="application/json" id="fg-cards-data">{{ {"bestiary": lufia2_bestiary, "equipment": lufia2_equipment, "items": lufia2_items, "magic": lufia2_magic, "ip": lufia2_ip} | tojson }}</script>
