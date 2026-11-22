---
tags:
  - Flesh and Blood
fg:
  subtabs: true
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Combat

The combat chain, step by step (CR 7). Click a card name to see the card and
its current text.

[Quiz this page](quiz.md?set=combat){ .md-button }

## Combat steps

The **combat chain** opens when an attack or attack-layer goes on the stack.
Each attack becomes a **chain link**. The steps are:

| Step | What happens | Priority? |
| --- | --- | --- |
| Layer | The attack is on the stack. When everyone passes, it goes to the **attack queue** | Yes |
| Attack | The next attack in the queue becomes a chain link. "When this attacks" triggers. Attacking and defending heroes are set | Yes |
| Defend | The defending hero declares defenders from hand and equipment, all at once. This isn't playing them | Yes |
| Reaction | The attacker plays **attack reactions**. The defender plays **defense reactions** | Yes |
| Damage | If power {{ sym("p") }} is **greater than** total defense {{ sym("d") }}, the attack hits for the difference | Yes |
| Resolution | Go again gives its action point. The turn-player may attack again | Yes |
| Close | Chain-close triggers, then permanents go home and everything else is cleared | **No** |

Card examples for the steps:

- **Attack:** {{ card("gravekeeping-1") }}'s "when this attacks a hero"
  triggers here.
- **Defend:** {{ card("bastion-of-unity") }} gets its Unity bonus because
  every declared defender joins as one event. The defender picks the order,
  which matters for {{ card("flic-flak-1") }} (CR 7.3.2c–d).
- **Reaction:** {{ card("lunging-press-3") }} is an attack reaction.
  {{ card("sink-below-1") }} is a defense reaction.
- **Close:** {{ card("pillar-of-unity") }} takes its Temper counter here.

## During combat

- While the chain is open, **action** cards and abilities can only be used
  as instants. The exception is new attacks during the resolution step
  (CR 7.0.1a).
- A **hit** is damage from the hit-event. If prevention brings that damage to
  0, it isn't a hit, and life loss is never a hit (CR 7.5.5). *Example:* if
  {{ card("feign-death-2") }} prevents all of an attack's damage, the attack
  didn't hit, so its "when this hits" effects don't trigger.

## Allies

- **Attacking an ally:** its controller is the defending hero, but can only
  declare defenders or play defense reactions if an effect allows it. Those
  are only allowed when a *hero* is the attack-target (CR 7.3.2a, 7.4.2b).
- **An ally attacking:** its controller is the attacking hero (CR 7.2.3a).
  *Example:*
  {{ card("cintari-sellsword") }} attacks through its own attack ability, and
  its controller is the attacking hero.

## Weapons and attack-layers

- **Weapons and other attack-proxies:** the proxy inherits its source's
  properties and any changes made to the source. Effects aimed only at the
  proxy end when that attack is over (CR 1.4.3). *Example:*
  {{ card("bone-basher") }} attacks through a proxy. If
  {{ card("ironsong-determination-2") }} gives the weapon +1 power and
  dominate, every attack it makes this turn has them.
- **Attack-layers:** "attack with" cards like
  {{ card("and-again-3", "And Again…") }} create a layer that isn't an attack.
  Effects on the layer don't carry over to the attack it makes (CR 1.4.4;
  May 19, 2026 rules update). *Example:* if {{ card("mage-master-boots") }}
  gives And Again… go again, the sword attack it makes doesn't have go again.
  {{ card("emperor-dracai-of-aesir") }}'s ability works the same way with
  Command and Conquer.

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
