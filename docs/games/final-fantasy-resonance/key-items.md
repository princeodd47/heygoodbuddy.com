---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy Resonance
fg:
  subtabs: true
  list:
    show: [What it is, Effect]
    placeholder: Name, where
---

# Key Items

Valuable items and artifacts you can have so far.

## Valuable items

| Item | What it is | Where |
|------|------------|-------|
{% for e in ffr_key_items.key_items -%}
| **{{ e.name }}** | {{ e.what }} | {{ e.where }} |
{% endfor %}

## Artifacts

| Artifact | Effect | Where |
|----------|--------|-------|
{% for e in ffr_key_items.artifacts -%}
| **{{ e.name }}** | {{ e.what }} | {{ e.where }} |
{% endfor %}

Item details come from
[NiaDB](https://meowdb.com/db/final-fantasy-resonance/items).

<script type="application/json" id="fg-cards-data">{{ {"game": "final-fantasy-resonance", "bestiary": ffr_bestiary, "equipment": ffr_equipment, "items": ffr_items, "key_items": ffr_key_items, "visions": ffr, "stop": ["Cloud", "Shadow"]} | tojson }}</script>
