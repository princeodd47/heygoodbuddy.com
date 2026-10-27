---
platform: Genesis
spoilers: none
status: draft
tags:
  - Shining Force
---

# Bestiary

Enemies battle by battle, in story order. **Wields** is what the enemy
fights with. Enemies don't drop items at random. The only items you can get
from them are the ones named under a battle, and only if the unit that
lands the kill has a free item slot. See the [Walkthrough](walkthrough.md)
for strategy.

{% for b in sf_bestiary.battles %}
## Battle {{ b.number }}: {{ b.name }}

**Win:** {{ b.win }}.{% if b.note %} **{{ b.note }}.**{% endif %}

| Enemy | # | HP | ATT | DEF | AGI | MOV | Wields | Spells | Notes |
|-------|--:|---:|----:|----:|----:|----:|--------|--------|-------|
{% for e in b.enemies -%}
| **{{ e.name }}** | {{ e.count }} | {{ e.hp }} | {{ e.atk }} | {{ e.def }} | {{ e.agi }} | {{ e.mov }} | {{ e.weapon or "—" }} | {{ e.spells or "—" }} | {{ e.note or "" }} |
{% endfor -%}
{% for e in b.bosses or [] -%}
| **{{ e.name }}** (boss) | 1 | {{ e.hp }} | {{ e.atk }} | {{ e.def }} | {{ e.agi }} | {{ e.mov }} | {{ e.weapon or "—" }} | {{ e.spells or "—" }} | {{ e.note or "" }} |
{% endfor %}
{% endfor %}

## Sources

- Rosters, win conditions and enemy stats: Dark_Vortex's
  [Shining Force guide](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/51880)
  (GameFAQs).
