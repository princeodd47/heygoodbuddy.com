---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy XII The Zodiac Age
---

# Bazaar

- Sell the listed loot to any shop. Once you've sold all of it, the bundle
  unlocks in the shop's **Bazaar** tab.
- Buying a bundle resets the sold count for every loot in it, even extra you
  sold. **If a loot is in more than one bundle, unlock them all before buying
  any.** You only need to sell the highest amount any one bundle needs.
- Standard bundles can be bought once. Repeatable bundles unlock again each
  time you sell their loot.
- For Monographs and the Canopic Jar, see [Monographs](monographs.md).

## Repeatable Bundles

| Bundle | Loot to sell | Contains | Gil |
|--------|--------------|----------|-----|
{% for b in ffxii_bazaar['repeatable'] -%}
| <a id="{{ b.id }}"></a>**{{ b.name }}** | {{ b.loot }} | {{ b.contains }} | {{ b.price }} |
{% endfor %}

## Bundles

| Bundle | Loot to sell | Contains | Gil |
|--------|--------------|----------|-----|
{% for b in ffxii_bazaar['bundles'] -%}
| <a id="{{ b.id }}"></a>**{{ b.name }}** | {{ b.loot }} | {{ b.contains }} | {{ b.price }} |
{% endfor %}
