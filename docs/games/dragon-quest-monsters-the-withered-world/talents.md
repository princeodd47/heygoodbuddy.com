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

# Talents

Talents are skill trees. A monster puts points into a Talent to unlock its
skills and traits. Search for a Talent, a skill or a monster, then pick a
Talent to see its full tree. Talents and point costs come from
[Soshage]({{ dqm_synth.sources.soshage.url }}) (Japanese); the notes on what each one does are our own
shorthand. **(Wis)** means higher wisdom makes it more likely to work.

{% set names = {} -%}
{% for m in dqm.monsters %}{% set _ = names.update({m.id: m.name}) %}{% endfor -%}
{% set notes = {} -%}
{% for a in dqm_abilities.abilities %}{% set _ = notes.update({a.name: a.note}) %}{% endfor -%}

<div id="dqm-talents" markdown="0">
<label for="tal-search">Search</label>
<input id="tal-search" type="search" placeholder="Talent, skill or monster" autocomplete="off">
{% for t in dqm_talents.talents %}
{% set words = [t.name] + (t.tree | map(attribute="name") | list) + (t.others or []) -%}
{% for id in t.monsters %}{% set _ = words.append(names[id]) %}{% endfor -%}
<section class="tal" id="{{ t.id }}" data-name="{{ t.name }}" data-search="{{ words | join('|') | lower }}">
<h2 class="tal-name">{{ t.name }}</h2>
<table class="tal-tree">
<thead><tr><th>Points</th><th>Unlocks</th><th>Type</th><th>What it does</th></tr></thead>
<tbody>
{% for row in t.tree %}<tr data-name="{{ row.name | lower }}"><td>{{ row.points }}</td><td>{{ row.name }}</td><td>{{ row.type | capitalize }}</td><td class="tal-note">{{ notes[row.name] or "" }}</td></tr>
{% endfor %}</tbody>
</table>
<p class="tal-mons"><strong>Monsters:</strong>
{% for id in t.monsters %}{{ '<a href="monsters.md' ~ '#' ~ id ~ '">' ~ names[id] ~ '</a>' }}{{ ", " if not loop.last or t.others }}{% endfor %}{% for o in t.others or [] %}{{ o }}{{ ", " if not loop.last }}{% endfor %}{% if not t.monsters and not t.others %}None listed{% endif %}
</p>
</section>
{% endfor %}
<p id="tal-hint" class="tal-hint" hidden>Pick a Talent to see its tree.</p>
<div id="tal-list" class="tal-list"></div>
</div>
