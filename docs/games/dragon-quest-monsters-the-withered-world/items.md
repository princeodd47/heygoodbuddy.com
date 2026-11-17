---
game_version: Demo
platform: Switch
spoilers: none
status: draft
tags:
  - Dragon Quest Monsters The Withered World
fg:
  list:
    show: [Type, Description]
    placeholder: Name, effect, where
---

# Items

Items, gold and story progress don't carry over from the demo. Finishing the
demo unlocks the **Wrangler's Bundle** in the full game. The **Hearty Meat Set**
comes with digital purchases.

| Item | Type | Description | Where |
|------|------|-------------|-------|
{% for i in dqm_items['items'] -%}
| <a id="{{ i.id }}"></a>**{{ i.name }}** | {{ i.type }} | {{ i.description }} | {{ i.where | default("") }} |
{% endfor %}

<script type="application/json" id="fg-cards-data">{{ {"game": "dragon-quest-monsters-the-withered-world", "monsters": dqm, "talents": dqm_talents, "items": dqm_items} | tojson }}</script>
