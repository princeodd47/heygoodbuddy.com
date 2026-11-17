---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy X-2
---

# Garment Grids

All 64 Garment Grids, in Jegged's order, which keeps similar grids
together: stat grids first, then elemental, status, defensive, healing
and the rest.

- **Equipped** is what the grid gives just by wearing it.
- **Gates** light up when you change Dressphere *through* them in battle,
  and the bonus lasts for the rest of the fight. The colour is the gate's
  colour on the grid.
- **Creature** is what the grid gives a creature instead. Creatures don't
  use gates, so this is all they get from the grid.
- **Chapter** is when you can first get it. Some are missable; the
  [walkthrough](walkthrough.md) flags the Chapter 1 ones.

| Grid | Equipped | Gates | Creature | Chapter | Where |
|------|----------|-------|----------|---------|-------|
{% for g in ffx2_grids.grids -%}
| **{{ g.name }}** | {{ g.equip or "—" }} | {{ g.gates or "—" }} | {{ g.creature or "—" }} | {{ g.chapter or "—" }} | {{ g.where or "—" }} |
{% endfor %}

## Sources

- Abilities, gates, creature abilities and where to get each grid:
  [Jegged's Garment Grids list](https://jegged.com/Games/Final-Fantasy-X-2/Garment-Grids/),
  checked against the
  [Gamer Guides Garment Grid data](https://www.gamerguides.com/final-fantasy-x-2/guide/extras/garment-grid-data).
