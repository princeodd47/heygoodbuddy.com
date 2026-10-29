---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy X-2
---

# Dresspheres

All 19 Dresspheres in the order you can first get them, with how to get
each one and its abilities. **AP** is the AP needed to learn it (0 means
it's known from the start), and **Needs** is the ability you must learn
first.

- Yuna, Rikku and Paine share one set of Dresspheres. Each can change
  into any Dressphere on her Garment Grid mid-battle (see
  [Garment Grids](garment-grids.md)).
- **Special Dresspheres** (Full Throttle, Floral Fallal, Machina Maw)
  belong to one character and don't go on a grid. In battle, change into
  every Dressphere on her grid once, then open the grid again to
  transform. She fights alone with two support units.
- Festivalist, Trainer and Mascot have a different moveset for each of
  the three.
- **Creatures** need a Dressphere too. It changes their stats but not
  their abilities; Mascot gives the biggest boost (see
  [Building the Team](creature-team.md)).

{% for d in ffx2_dresspheres.dresspheres %}
## {{ d.name }}

**How to get it:** {{ d.how }}

{% for g in d.groups %}
{% if g.who %}
### {{ d.name }}: {{ g.who }}
{% endif %}

| Ability | AP | Needs |
|---------|---:|-------|
{% for a in g.abilities -%}
| {{ a.name }} | {{ a.ap }} | {{ a.needs or "—" }} |
{% endfor %}
{% endfor %}
{% endfor %}

## Sources

- Ability lists, AP and prerequisites:
  [Jegged's Dressphere pages](https://jegged.com/Games/Final-Fantasy-X-2/Dresspheres/).
- Where to get each one: Jegged, checked against the
  [Gamer Guides Dressphere section](https://www.gamerguides.com/final-fantasy-x-2/guide/extras/dresspheres).
