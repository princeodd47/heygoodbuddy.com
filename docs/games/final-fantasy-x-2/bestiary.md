---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy X-2
---

# Bestiary

Every enemy, alphabetical. **Weak** lists elements that do extra damage;
**Other** lists elements it resists, is immune to or absorbs. **Steal**
and **Drop** give the common item first, then the rare one. **Bribe**
needs Lady Luck's Bribe ability. **Where** gives each place and the
chapters it appears there; Fiend Arena enemies are on the
[Fiend Arena](fiend-arena.md) page.

Drops aren't guaranteed, and one enemy can drop more than one thing:
an item listed after "also" was dropped in our game but isn't in the
guides.

Butterfingers (a creature on the Ray of Hope Garment Grid) makes every
drop the rare one, and Master Thief always steals the rare one.

| Enemy | Lv | HP | Weak | Other | Steal | Drop | Bribe | Where |
|-------|---:|---:|------|-------|-------|------|-------|-------|
{% for e in ffx2_bestiary.enemies -%}
| **{{ e.name }}** | {{ e.level or "—" }} | {{ e.hp or "—" }} | {{ e.weak or "—" }} | {{ e.other or "—" }} | {{ e.steal or "—" }} | {{ e.drop or "—" }} | {{ e.bribe or "—" }} | {{ e.where or "—" }} |
{% endfor %}

## Sources

- Stats, elements, steals, drops, bribes and locations:
  [Jegged's FFX-2 bestiary](https://jegged.com/Games/Final-Fantasy-X-2/Bestiary/).
