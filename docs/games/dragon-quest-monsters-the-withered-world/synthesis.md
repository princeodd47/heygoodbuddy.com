---
game_version: Demo
platform: Switch
spoilers: none
status: draft
tags:
  - Dragon Quest Monsters The Withered World
---

# Synthesis

Recipes reported online for the demo. **Unverified** means it hasn't been
tested here yet. Parents need to be level 10.

{% set names = {} -%}
{% for m in dqm.monsters %}{% set _ = names.update({m.id: m.name}) %}{% endfor -%}
{% macro mon(id) -%}
{% if id in names %}{{ "[" ~ names[id] ~ "](monsters.md#" ~ id ~ ")" }}{% else %}**missing: {{ id }}**{% endif %}
{%- endmacro %}
{% macro parent(p) -%}
{% if p.monster %}{{ mon(p.monster) }}{% else %}Any {{ p.family }}{% endif %}
{%- endmacro %}

## Special recipes

"Any Demon" means any Demon-family monster.

| Result | Parent | Parent | Status | Sources |
|--------|--------|--------|--------|---------|
{% for r in dqm_synth.recipes -%}
| **{{ mon(r.result) }}** | {{ parent(r.parents[0]) }} | {{ parent(r.parents[1]) }} | {{ r.status | capitalize }} | {% for s in r.sources %}[{{ dqm_synth.sources[s].name }}]({{ dqm_synth.sources[s].url }}){{ ", " if not loop.last }}{% endfor %}{% if r.note %}<br>*{{ r.note }}*{% endif %} |
{% endfor %}

## Family recipes

Pick the row for the family you want, then the column for the other parent's
family. All unverified. Source: [MeowDB]({{ dqm_synth.sources.meowdb.url }}).

{% for rank in ["G", "F"] %}
=== "Rank {{ rank }}"

    | Want ↓ / With → | {{ dqm_synth.families | join(" | ") }} |
    |---|{% for f in dqm_synth.families %}---|{% endfor %}
    {% for lead in dqm_synth.families -%}
    | **{{ lead }}** |{% for partner in dqm_synth.families %} {% for r in dqm_synth.family_recipes if r.rank == rank and r.lead == lead and r.partner == partner %}{{ mon(r.result) }}{% else %}—{% endfor %} |{% endfor %}
    {% endfor %}
{% endfor %}
