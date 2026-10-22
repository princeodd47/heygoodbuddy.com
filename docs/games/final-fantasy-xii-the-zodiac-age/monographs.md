---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy XII The Zodiac Age
---

# Monographs

A Monograph raises the chance of rare loot from its enemy types, and lets
those enemies drop two items instead of one. It works as long as it's in your
inventory.

Monographs are sold in the Bazaar as **Forgotten Grimoire** once unlocked. The
talk and read counts work at any shop or notice board in any town. Notice board
reads may only count after you finish the Rogue Tomato hunt.

| Monograph | Enemies | Price (gil) | How to unlock |
|-----------|---------|-------------|---------------|
{% for m in ffxii_monographs['monographs'] -%}
| <a id="{{ m.id }}"></a>**{{ m.name }}** | {{ m.enemies }} | {{ m.price }} | {{ m.unlock }} |
{% endfor %}

## Canopic Jar

Not a Monograph, but it works the same way. With the **Canopic Jar** in your
inventory, any enemy can drop **Arcana**. It's sold in the Bazaar as **Morbid Urn** for 250,000 gil,
after you sell **Horakhty's Flame**, **Phobos Glaze** and **Deimos Clay**.
All three are hunt rewards.
