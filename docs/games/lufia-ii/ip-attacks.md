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
    show: [Element, Effect]
    chips: Element
    chips_label: Element
    chips_style: elements
    placeholder: Name, effect, gear
---

# IP Attacks

Every IP attack and the gear that has it. The IP gauge under each
character's HP fills as they take damage. Once it's full enough, they can use
an IP from any gear they're wearing. Open an IP for its gear; see
[Equipment](equipment.md) for the stats.

{% for g in lufia2_ip.groups %}
## {{ g.type }}

| IP | Element | Effect | Gear |
|----|---------|--------|------|
{% for x in g.ips -%}
{%- set ns = namespace(gear=[]) -%}
{%- for k, items in lufia2_equipment.items() -%}{%- for e in items if e.ip == x.name -%}{%- set ns.gear = ns.gear + [e.name] -%}{%- endfor -%}{%- endfor -%}
| **{{ x.name }}** | {{ x.element or "—" }} | {{ x.effect }} | {{ (ns.gear or x.gear or ["—"]) | join(", ") }} |
{% endfor %}
{% endfor %}

## Sources

- What each IP does and which gear has it:
  [RPGClassics' Lufia 2 shrine](http://www.rpgclassics.com/shrines/snes/lufia2/),
  checked against the gear on [Equipment](equipment.md).

<script type="application/json" id="fg-cards-data">{{ {"bestiary": lufia2_bestiary, "equipment": lufia2_equipment, "items": lufia2_items, "magic": lufia2_magic, "ip": lufia2_ip} | tojson }}</script>
