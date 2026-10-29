---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy Resonance
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

<script id="ffr-items-data" type="application/json">{{ {"equipment": ffr_equipment, "items": ffr_items} | tojson }}</script>
