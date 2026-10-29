---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy Resonance
---

# Equipment

Every weapon and armor you can get so far, in the order you can first get
it. **Atk** and **Mag** are physical and magic attack. **Def** and **M.Def**
are physical and magic defense.

**Where** says how to get it. A place name on its own means a chest or a
pickup there. *Drop* and *Steal* name the enemy; see the
[Bestiary](bestiary.md) for where it lives. The **Capital Market** in
Zoldaad charges far more than other shops.

## Weapons

{% for g in ffr_equipment.weapons %}
### {{ g.type }}

{% if g.who %}{{ g.who }} uses these.{% else %}Nobody in your party uses these yet.{% endif %}

| Weapon | Atk | Mag | Other stats | Effect | Where |
|--------|----:|----:|-------------|--------|-------|
{% for e in g.entries -%}
| **{{ e.name }}** | {{ e.atk }} | {{ e.mag }} | {{ e.other or "—" }} | {{ e.effect or "—" }} | {{ e.where }} |
{% endfor %}
{% endfor %}

## Armor

{% for g in ffr_equipment.armor %}
### {{ g.type }}

Worn by {{ g.who }}.

| Armor | Def | M.Def | Other stats | Effect | Where |
|-------|----:|------:|-------------|--------|-------|
{% for e in g.entries -%}
| **{{ e.name }}** | {{ e.def }} | {{ e.mdef }} | {{ e.other or "—" }} | {{ e.effect or "—" }} | {{ e.where }} |
{% endfor %}
{% endfor %}

Stats and effects come from
[NiaDB](https://meowdb.com/db/final-fantasy-resonance/equipment). Locations
come from NiaDB and the
[RPG Site walkthrough](https://www.rpgsite.net/guide/21486-final-fantasy-resonance-walkthrough-100-items-all-achievements-tablet-shards-step-by-step-guide).
