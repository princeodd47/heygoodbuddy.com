---
hide:
  - toc
game_version: Demo
platform: Switch
spoilers: none
status: draft
tags:
  - Dragon Quest Monsters The Withered World
---

# Recipe Builder

Pick a monster to chart how to make it. Parents branch upward. Click a name
to show or hide its parents. Where there's more than one recipe, **Recipe 1 of
2 ›** switches between them. The top color shows the family. Recipes come from
the [Synthesis](synthesis.md) page.

<div id="synth-builder">
  <label for="sb-input">Monster</label><br>
  <input id="sb-input" list="sb-list" placeholder="Start typing a name" autocomplete="off">
  <datalist id="sb-list"></datalist>
  <div id="sb-result"></div>
</div>

<script id="synth-data" type="application/json">{{ {"monsters": dqm.monsters, "recipes": dqm_synth.recipes, "family_recipes": dqm_synth.family_recipes, "sources": dqm_synth.sources} | tojson }}</script>
