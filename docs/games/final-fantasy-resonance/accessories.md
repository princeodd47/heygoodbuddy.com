---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy Resonance
fg:
  list:
    show: [Stats, Effect]
    placeholder: Name, effect, where
---

# Accessories

Every accessory you can get so far, in the order you can first get it.

**Where** says how to get it. A place name on its own means a chest or a
pickup there. *Drop* and *Steal* name the enemy; see the
[Bestiary](bestiary.md) for where it lives.

| Accessory | Effect | Stats | Where |
|-----------|--------|-------|-------|
{% for e in ffr_equipment.accessories -%}
| **{{ e.name }}** | {{ e.effect or "—" }} | {{ e.other or "—" }} | {{ e.where }} |
{% endfor %}

Effects come from
[NiaDB](https://meowdb.com/db/final-fantasy-resonance/equipment). Locations
come from NiaDB and the
[RPG Site walkthrough](https://www.rpgsite.net/guide/21486-final-fantasy-resonance-walkthrough-100-items-all-achievements-tablet-shards-step-by-step-guide).

<script type="application/json" id="fg-cards-data">{{ {"game": "final-fantasy-resonance", "bestiary": ffr_bestiary, "equipment": ffr_equipment, "items": ffr_items, "key_items": ffr_key_items, "visions": ffr, "stop": ["Cloud", "Shadow"]} | tojson }}</script>
