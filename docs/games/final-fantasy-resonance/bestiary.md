---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy Resonance
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

<script id="ffr-items-data" type="application/json">{{ {"equipment": ffr_equipment, "items": ffr_items} | tojson }}</script>
