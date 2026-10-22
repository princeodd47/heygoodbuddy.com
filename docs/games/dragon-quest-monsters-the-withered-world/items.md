---
game_version: Demo
platform: Switch
spoilers: none
status: draft
tags:
  - Dragon Quest Monsters The Withered World
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
