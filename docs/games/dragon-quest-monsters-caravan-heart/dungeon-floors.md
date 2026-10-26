---
platform: GBC
spoilers: none
status: draft
tags:
  - Dragon Quest Monsters Caravan Heart
---

# Dungeon Floors

Floor-by-floor notes from orb dungeons. The number of floors depends on how
many orbs you use. With 4 orbs there are 14 floors, and the boss is on 15F.
Enemies and events change each run, so treat these as what one run turned
up. For how the dungeons work, see
[Orb Dungeons](orb-dungeons.md).

{% for d in dqmch_dungeons['dungeons'] %}
## {{ d.name }}

**Orbs:** {{ d.orbs }}{% if d.family %} · **Family:** {{ d.family }}{% endif %}

| Floor | Enemies | Chests | Event |
|-------|---------|--------|-------|
{% for f in d.floors -%}
| {{ f.floor }} | {{ f.enemies | default([]) | join(', ') }} | {{ f.chests | default([]) | join(', ') }} | {{ f.event | default('') }} |
{% endfor %}
{% endfor %}
