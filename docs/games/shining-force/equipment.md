---
platform: Genesis
spoilers: none
status: draft
tags:
  - Shining Force
---

# Equipment

Shining Force has no armor. Each unit equips one weapon and one ring. Every
table is in the order you can first get each item. **Where** names a shop
town, a chest, or an enemy that carries it. Shops charge the same in every
town.

**Promoted** means the unit has to be promoted first. Knights are Ken, Mae,
Arthur, Pelle, Vankar and Earnest. Healers are Lowe, Khris and Torasu. Mages
are Tao, Anri and Alef. Gong, Domingo, Bleu, Zylo, Adam and Jogurt don't use
weapons.

## Weapons

{% for g in sf_equipment.weapons %}
### {{ g.type }}

| Weapon | ATT | Price | Who | Where |
|--------|----:|------:|-----|-------|
{% for i in g['items'] -%}
| **{{ i.name }}** | +{{ i.atk }} | {{ i.price }} | {{ i.who }} | {{ i.where }} |
{% endfor %}
{% endfor %}

## Rings

**USE** a ring in battle to cast its spell. It works from the inventory
without equipping it, which is the safe way to get spells out of the cursed
rings.

| Ring | Equipped | Use | Who | Where |
|------|----------|-----|-----|-------|
{% for i in sf_equipment.rings -%}
| **{{ i.name }}** | {{ i.effect }} | {{ i.use }} | {{ i.who }} | {{ i.where }} |
{% endfor %}

## What to buy

| Town | Buy |
|------|-----|
| Guardiana | Spears, Hand Axe |
| Rindo | Bronze Lances, Middle Swords, Power Staff |
| Bustoke | Power Spears, Middle Axes, Steel Arrows |
| Pao | Long Sword |
| Waral | Steel Lances, Steel Swords, Battle Axes, Elven Arrows |
| Rudo | Chrome Lances, Guardian Staffs |
| Prompt | Assault Shells, Broad Swords, Great Axe |
| Runefaust | Buster Shots |

## Sources

- Attack values and who can equip: Dark_Vortex's
  [Shining Force guide](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/51880)
  (GameFAQs).
- Shop prices: the same guide, and Dinob0t's
  [shop FAQ](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/40809)
  (GameFAQs).
- Ring spells and the Jogurt Ring: GLSicherman's
  [Shining Force FAQ](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/2837)
  (GameFAQs). Cursed gear: the GameFAQs
  [guide and walkthrough](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/2838).
- Musashi's Katana:
  [character guide](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/63598)
  (GameFAQs).
