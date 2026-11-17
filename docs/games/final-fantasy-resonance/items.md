---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy Resonance
---

# Items

Every consumable you can get so far.

**Buy** lists where it's sold. "Most item shops" means six or more of the
shops you've reached. The **Capital Market** in Zoldaad charges far more
than other shops.

**Also found** lists chests and pickups, where a place name on its own means
a chest or a pickup there. For items you can't buy, it also lists the
enemies that drop it or carry it to steal. See the [Bestiary](bestiary.md)
for where they live.

Scrolls, knives and shuriken get stronger when thrown, and a thrown scroll
hits every enemy.

{% for g in ffr_items.groups %}
## {{ g.group }}

| Item | Effect | Buy | Also found |
|------|--------|-----|------------|
{% for e in g.entries -%}
| **{{ e.name }}** | {{ e.effect }} | {{ e.buy or "—" }} | {{ e.found or "—" }} |
{% endfor %}
{% endfor %}

Effects and shop stock come from
[NiaDB](https://meowdb.com/db/final-fantasy-resonance/items). Chest
locations come from NiaDB and the
[RPG Site walkthrough](https://www.rpgsite.net/guide/21486-final-fantasy-resonance-walkthrough-100-items-all-achievements-tablet-shards-step-by-step-guide).
