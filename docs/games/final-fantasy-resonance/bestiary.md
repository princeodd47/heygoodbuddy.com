---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy Resonance
fg:
  list:
    merge: true
    group: Area
    show: [Level, Weaknesses, Resists]
    sort: [Level, -Level]
    chips: Weaknesses
    chips_label: Weak to
    chips_style: elements
    chip_values: [Fire, Ice, Water, Lightning, Wind, Earth, Light, Dark]
    elements: [Resists]
    placeholder: Name, drop, steal, area
---

# Bestiary

The game has no bestiary of its own, so here's one. Enemies are grouped by
the area where you first meet them, in the order you reach those areas.
**Where** lists every place an enemy shows up. **Resists** means it takes
half damage from that element, or none where it says *(immune)*. *(rare)*
marks a rare drop or rare steal.

{% for g in ffr_bestiary.bestiary %}
## {{ g.area }}

| Enemy | Level | Where | Weaknesses | Resists | Drops | Steals |
|-------|-------|-------|------------|---------|-------|--------|
{% for e in g.enemies -%}
| **{{ e.name }}**{% if e.boss %} (boss){% endif %} | {{ e.level }} | {{ e.where }} | {{ e.weak or "—" }} | {{ e.resist or "—" }} | {{ e.drops or "—" }} | {{ e.steals or "—" }} |
{% endfor %}
{% endfor %}

<script type="application/json" id="fg-cards-data">{{ {"game": "final-fantasy-resonance", "bestiary": ffr_bestiary, "equipment": ffr_equipment, "items": ffr_items, "key_items": ffr_key_items, "visions": ffr, "stop": ["Cloud", "Shadow"]} | tojson }}</script>
