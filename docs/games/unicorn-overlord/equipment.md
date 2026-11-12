---
platform: Switch
spoilers: none
status: draft
tags:
  - Unicorn Overlord
---

# Equipment

Every item the [Post-Game Teams](post-game-teams.md) squads use. **P.Atk**
and **M.Atk** are physical and magic attack, **P.Def** and **M.Def** physical
and magic defense, and **Guard** is guard rate.

**Price** is the cheapest gold price in a shop. **Where** lists every way to
get the item:

- **Shop:** armorers that sell it, grouped by price, with the continent in
  brackets. **Black Market Dealer** is the night-time merchant on that
  continent.
- **Divine Shard Exchange:** any church that trades Divine Shards; they share
  one stock.
- **Coliseum Prize Exchange:** the coliseum in Baumratte.
- **Quest reward:** the quest that gives it.

{% for g in uo_equipment.groups %}
## {{ g.type }}

| Item | Stats | Effects | Price | Where |
|------|-------|---------|-------|-------|
{% for e in g.entries -%}
| <span class="uo-anchor" id="{{ e.id }}"></span>**{{ e.name }}** | {{ e.stats or "—" }} | {% if e.skill %}**{{ e.skill.name }}** ({{ e.skill.details }}): {{ e.skill.text }}{% if e.effects %}<br>{% endif %}{% endif %}{{ e.effects | join("<br>") }}{% if not e.skill and not e.effects %}—{% endif %} | {{ e.price or "—" }} | {{ e.where | join("<br>") if e.where else "—" }} |
{% endfor %}
{% endfor %}
