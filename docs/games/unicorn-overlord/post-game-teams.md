---
skin: field-guide
platform: Switch
spoilers: none
status: draft
tags:
  - Unicorn Overlord
---

{#- One squad: heading, description, unit cards by row, start-of-battle
    notes and tactics notes. Squads live in data/unicorn-overlord/teams.yaml. -#}
{% macro squad(q) -%}
### {{ q.title }}

{{ q.about }}

<div class="uo-squad">
{%- for row in ["front", "back"] %}{% set us = q.units | selectattr("row", "equalto", row) | list %}{% if us %}
<div class="uo-row"><div class="uo-row-name">{{ row | title }} row</div><div class="uo-cards">
{%- for u in us %}{% set k = q.start.keep %}
<section class="uo-unit{% if k and k.unit == u.name %} uo-keep{% endif %}">
<div class="uo-unit-head"><span class="uo-unit-name">{{ u.name }}</span><span class="uo-unit-class">{{ u["class"] }}</span></div>
{%- if k and k.unit == u.name %}
<p class="uo-start uo-start-keep"><span class="uo-flag">Keep on</span>{{ k.skill }}{% if k.via %} ({{ k.via }}){% endif %}</p>
{%- endif %}{% for o in q.start.get("off", []) if o.unit == u.name %}
<p class="uo-start uo-start-off"><span class="uo-flag">Turn off</span>{{ o.skill }}</p>
{%- endfor %}
<ul class="uo-gear">{% for e in u.equipment %}<li>{{ e }}</li>{% endfor %}</ul>
<details class="uo-tactics"><summary>Tactics <span class="uo-count">{{ u.tactics | length }}</span></summary>
{%- for kind in ["active", "passive"] %}{% set ts = u.tactics | selectattr("type", "equalto", kind) | list %}{% if ts %}
<div class="uo-tac-kind">{{ kind | title }}</div><ol class="uo-tac">{% for t in ts %}<li><span class="uo-skill">{{ t.skill }}</span><span class="uo-when{% if t.when == "None" %} uo-none{% endif %}">{{ t.when }}</span></li>{% endfor %}</ol>
{%- endif %}{% endfor %}
</details>
</section>
{%- endfor %}
</div></div>
{%- endif %}{% endfor %}
</div>

{% if not q.start.keep %}**Start-of-battle skill:** none needed.{% if q.start.note %} {{ q.start.note }}{% endif %}
{% elif q.start.note %}**Start of battle:** {{ q.start.note }}
{% endif %}
{%- if q.notes %}
??? note "Tactics notes"

{{ q.notes | indent(4, true) }}
{% endif %}
{%- endmacro %}

# Post-Game Teams

Ten full squads to field together for post-game content on the hardest
difficulty. No two squads share an item you only have one of. Every unit
listed is in exactly one squad.

- **Squads:** your army caps at 10 units (squads), with 5 characters each.
- **Class-change items:** none of these squads uses one. Everyone stays in
  their default class.
- **One start-of-battle skill per unit.** Only one *Limited* skill that
  activates at the start of battle fires per squad side. If two units have
  one (Alain's Rapid Order, a Swordmaster's Hastened Strike, a Divine
  Blessing), the one you want may not go off. Each squad's unit cards mark
  the one to **Keep on** and the ones to **Turn off** in Tactics.
- **Quick Impetus** comes from the White Cat-Ear Hood and the Black Cat-Ear
  Hood. They do the same thing and you have one of each. It fires when an
  ally uses an active skill and lets that ally act again right away. On a
  charge skill, the ally starts charging, Quick Impetus fires, and they
  immediately use the big skill (Trinity Rain, Glacial Rain, Dragoon Dive)
  instead of waiting a turn.
- **Ring of the Maiden** goes on Alain's bonded partner, Berengaria.
- **Unit cards** are grouped by front and back row and show each unit's
  class and four items. Open **Tactics** on a card for its active and passive
  skills in priority order, top to bottom, the way they appear in the Tactics
  menu. Skills not listed are off.
- **Item names:** click one to see its stats, skill, price and where to get
  it. The [Equipment](equipment.md) page lists them all.
- Test every squad in a mock battle before a hard fight. The forecast tells
  you whether the combo kills before the enemy acts.

## The Ten Squads

{% for q in uo_teams.squads %}
{{ squad(q) }}
{% endfor %}
## Bench

Everyone else: Jeremy, Mordon, Nina, Gammel, Fodoquia, Mandrin, Aubin, Rolf,
Kitra, Melisandre, Colm, Leah, Liza, Ridiel, Umerus, Millé, Gailey, Hermann,
Beaumont, Laurent, Govil and Bertrand.

Good swaps:

- **Liza** (Shieldshooter) with Skiron's Shield for Lex in squad 2. Hastened
  Cover makes the ally she covers act right away, so a covered Hilda dives
  immediately.
- **Aubin** (Viking) in squad 4 or 8. His defense shred counts as a debuff,
  which powers up Dark Flame and Death Spin.

## Unique Items

Items you only have one of, and who holds them.

| Item | Holder | Squad |
| --- | --- | --- |
{% for q in uo_teams.squads %}{% set n = loop.index %}{% for u in q.units %}{% for e in u.equipment if uo_teams.limited.get(e) == 1 and e not in uo_teams.pendants -%}
| {{ e }} | {{ u.name }} | {{ n }} |
{% endfor %}{% endfor %}{% endfor %}

### Pendants and Medallions

| Item | Used | Holders |
| --- | --- | --- |
{% for p in uo_teams.pendants %}{% set hs = [] %}{% for q in uo_teams.squads %}{% for u in q.units if p in u.equipment %}{% set _ = hs.append(u.name) %}{% endfor %}{% endfor -%}
| {{ p }}{% if uo_teams.limited.get(p) %} ({{ uo_teams.limited[p] }}){% endif %} | {{ hs | length }} | {{ hs | join(", ") }} |
{% endfor %}

Other repeated items (Sage's Hood, Royal Scarf, Elite Beret, Blue
Spectacles, Meteorite weapons, Citadel Guard's Sabatons and so on) can be
bought in late-game shops, so you can hold more than one.

## Other Strong Post-Game Teams

Full builds of well-known community squads. These are alternatives, not
extra slots: most share characters and unique items with the ten squads
above, so swap one in by breaking up the squad it borrows from. Where a
source used a generic unit, the build below uses one of your named
characters of the same class.


{% for q in uo_teams.others %}
{{ squad(q) }}
{% endfor %}
## Sources

YouTube:

- TitaniumLegman, [Steal These Squads compilation](https://www.youtube.com/watch?v=ErIEkfFZa90): Super Tax Brothers, Bruno burn squad, Freezer Burn, Affliction Angels, Ajax Doom Knight squad, Bruno and the Braves, Alain and Berengaria, Josette dodge team
- TitaniumLegman, [squad builds](https://www.youtube.com/watch?v=U1ZJD6utcoI)
- TitaniumLegman, [Trinity Rain build](https://www.youtube.com/watch?v=dSZiq_eBsyA)
- Corvie Indo, [full squads and tactics](https://www.youtube.com/watch?v=axnNcvONdE4): squad 4, Hilda Lightning Shaker
- Varsona, [five team comps](https://www.youtube.com/watch?v=ZmGuY6UPUa4): Alain multi-nuke, Rosalinde counter squad, Yunifi crit, Berengaria and the Doom Knight, Amalia and Berenice
- Varsona, [three more team comps](https://www.youtube.com/watch?v=wkBlTK2UCis): Hilda and Primm, Nina and Gilbert, Yunifi Triple Counter
- 89 Games, [board nuke units](https://www.youtube.com/watch?v=B2DZ0OjjAUE): Hilda Dragoon Dive, Glacial Rain, Trinity Rain
- 89 Games, [mid to late game units](https://www.youtube.com/watch?v=uqC6_WU9jT4): Alain's cavalry, Monica's affliction squad, Fran's flyers
- Iced Coffee Gaming, [Amalia guide](https://www.youtube.com/watch?v=HmvWvZ51MGQ)
- Iced Coffee Gaming, [Yunifi guide](https://www.youtube.com/watch?v=z3tNPdXOI44)
- Iced Coffee Gaming, [Feathersword guide](https://www.youtube.com/watch?v=75raLIAlRH0)
- Iced Coffee Gaming, [Berengaria guide](https://www.youtube.com/watch?v=ZeIv8sLvtBY)

Written:

- Merqurial, [Unicorn Overlord guide on GameFAQs](https://gamefaqs.gamespot.com/switch/426397-unicorn-overlord/faqs/81216): items, class skills, sample units
- GameFAQs board, [Amalia thread](https://gamefaqs.gamespot.com/boards/426397-unicorn-overlord/80732519): squad 6's Leaping Slash loop
- [Game8 Unicorn Overlord wiki](https://game8.co/games/Unicorn-Overlord): character builds and weapon types
- [Unicorn Overlord Fandom wiki](https://unicornoverlord.fandom.com/wiki/Characters): classes, Black Cat-Ear Hood
- [Unicorn Overlord Miraheze wiki](https://unilord.miraheze.org/wiki/Main_Page): item sources and counts

<script id="uo-items-data" type="application/json">{{ uo_equipment | tojson }}</script>
