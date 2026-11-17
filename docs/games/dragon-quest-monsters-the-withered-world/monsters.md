---
hide:
  - toc
game_version: Demo
platform: Switch
spoilers: none
status: draft
tags:
  - Dragon Quest Monsters The Withered World
---

# Monsters

Grouped by rank, then family. The top color shows the family. Click a name
to chart how to make it in the [Recipe Builder](recipe-builder.md).

<div id="dqm-filters"></div>

{% set talent_names = {} -%}
{% for tt in dqm_talents.talents %}{% set _ = talent_names.update({tt.id: tt.name}) %}{% endfor -%}
{% for rank in dqm.monsters | map(attribute="rank") | unique | sort(reverse=true) %}
## Rank {{ rank }} {: #rank-{{ rank | lower }} }

{% for family in dqm_synth.families %}
{% set group = dqm.monsters | selectattr("rank", "eq", rank) | selectattr("family", "eq", family) | list %}
{% if group %}
### {{ family }} <span class="dqm-count">{{ group | length }}</span> {: #rank-{{ rank | lower }}-{{ family | lower }} .dqm-fam-heading .dqm-fam-{{ family | lower }} }

<div class="dqm-grid dqm-fam-{{ family | lower }}" data-rank="{{ rank | lower }}" data-family="{{ family | lower }}" markdown="0">
{% for m in group %}<div class="dqm-tile" id="{{ m.id }}"><a class="dqm-name" href="recipe-builder.md?monster={{ m.id }}">{{ m.name }}</a>{% if m.where %}<span class="dqm-where">{{ m.where }}</span>{% endif %}{% for tid in m.talents or [] %}<a class="dqm-talent" href="talents.md?talent={{ tid }}">{{ talent_names[tid] }}</a>{% endfor %}</div>
{% endfor %}</div>
{% endif %}
{% endfor %}
{% endfor %}
