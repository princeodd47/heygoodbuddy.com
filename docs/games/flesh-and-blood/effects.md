---
tags:
  - Flesh and Blood
fg:
  subtabs: true
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Effects

What effects do, how long they last, the order they apply in, and when they
trigger. Click a card name to see the card and its current text.

[Quiz this page](quiz.md?set=effects){ .md-button }

## Optional, conditional and targeted

- **Optional ("may"):** you can't choose an optional effect you can't
  actually carry out, including one with a cost you can't pay. Heave needs
  both the resources and an open arsenal. "May **choose** to" is
  different: you can choose it anyway (CR 1.8.3b). *Example:*
  {{ card("rubble-raiser-1") }} has Heave 2: with less than 2 resources or a
  full arsenal, you can't heave it. {{ card("mark-of-the-huntsman") }} says
  "you may choose to destroy this and mark them", so you can choose it even
  if one part can't happen.
- **Conditional ("if"):** for a discrete effect, the condition is checked
  once, when it would happen (CR 6.1.3). "While" conditions are checked all
  the time (CR 1.8.4c). *Example:* {{ card("heart-of-fyendal-3") }} checks
  your life against your opponent's once, when it's pitched.
  {{ card("parable-of-humility-2") }}'s -1 power applies only while those
  attacks are attacking or defending.
- **Targeted** effects use the word "target". Only public objects in the
  arena or on the stack can be targeted, unless the effect names another zone
  (CR 1.8.5). Effects without the word "target" pick their objects on
  resolution. *Example:* {{ card("memorial-ground-1") }} targets a card in
  your graveyard because it names that zone. {{ card("remembrance-2") }}
  doesn't say "target", so it picks its cards as it resolves.
- An effect **fails** if all its targets are gone, if there are no legal
  parameters, or if every event it creates fails (CR 1.8.9). *Example:*
  {{ card("flick-knives") }} with its targeted dagger gone.

## Events

- **Doing nothing isn't an event.** Dealing 0 damage doesn't happen, so it
  can't be replaced or trigger anything (CR 1.9.1b). *Example:*
  {{ card("blazing-aether-1") }} deals X arcane damage, where X is the arcane
  damage you've already dealt that hero this turn. With X = 0, there's no
  damage event at all.
- **Searching a private zone:** you may "fail to find" a card the opponent
  can't verify (CR 1.9.1c). *Example:* when {{ card("moon-wish-1") }} hits,
  you can search for Sun Kiss and choose not to find it.
- **Multi-events** ("draw 3") trigger an effect once, not once per card.
  They're also replaced as a whole (CR 1.9.2). *Example:*
  {{ card("tome-of-harvests-3") }} draws 3 as one multi-event.
  {{ card("mordred-tide-1") }} replaces a whole group of Runechants with that
  many plus 1, not plus 1 for each.

## Continuous effects (CR 6.2–6.3)

- **From a resolved layer:** with no stated duration, it lasts **until end of
  turn**. Values like X are locked in when it's created. It keeps applying to
  an object even if the object's properties change. *Example:*
  {{ card("come-to-fight-1") }}'s bonus lasts until end of turn.
  {{ card("tear-limb-from-limb-3") }} is the twist: its X is the next Brute
  attack's base power, so X is locked in when that attack is played, not when
  Tear Limb resolves (CR 6.2.2b).
- **From a static ability:** it lasts while the ability works, values update
  live, and it applies only while the object still matches. *Example:*
  {{ card("luminaris") }}'s go again turns on and off as yellow cards enter and
  leave your pitch zone.
- **Order of application:** rules-changing effects come first, then 8
  **stages** (copy → controller → name/text → types → supertypes →
  abilities → base numbers → numbers). Inside the number stages, the
  **substages** are add/remove property → set → multiply → divide → add →
  subtract → dependent. Ties go by **timestamp**. *Example:*
  {{ card("hypothermia-3") }} changes the rules ("can't gain go again"), so it
  applies before any effect that would add go again. {{ card("minnowism-1") }}
  checks base power: if an earlier stage drops a 6-power attack's base to 3,
  Minnowism then applies to it (CR 6.3.5a).

!!! example "Set before add"
    An attack with base 3 power gets +2. Later, another effect sets its power
    to 1. "Set" goes before "add" whatever the timestamps, so the result is
    1 + 2 = **3**.

## Replacement effects (CR 6.4–6.5)

- A replacement has to exist **before** the event happens. They're never
  retroactive. *Example:* {{ card("drone-of-brutality-1") }} goes to the
  bottom of your deck instead of the graveyard, because its replacement is
  there before it would move.
- Each replacement modifies an event **once**. *Example:* with two
  {{ card("to-be-continued-3", "To Be Continued...") }} in play, 1 damage is
  prevented by the first one only. The second one is used on the next damage
  that turn (CR 6.4.2b).
- When several apply, the turn-player picks who goes first. Then they apply
  in this order: **self/identity → standard → prevention → event happens →
  outcome**. *Example:* {{ card("tome-of-divinity-2") }} draws 3 instead of
  2 if a card went into your soul this turn. That's a self-replacement, so it
  applies first.
- **Prevention:** *fixed* prevention is used up on one event. *Shielding*
  ("prevent the next N") carries over until it's used up. *Example:*
  {{ card("enchanting-melody-1") }} is fixed: destroy it to prevent 4 of one
  damage event. {{ card("steadfast-1") }} is shielding: it prevents the next 6
  damage from one source, spread over as many events as it takes.

## Triggered effects (CR 6.6)

- A trigger has to exist when its event happens. *Example:*
  {{ card("snatch-1") }}'s "when this hits, draw a card" works because Snatch
  is on the chain when it hits.
- *Inline* triggers ("when you do") are the exception: they trigger as long
  as the condition was met.
- Triggered layers go on the stack before anyone next gets priority. If
  several are waiting, the turn-player chooses a player to start, then each
  player in clockwise order adds theirs in any order.
- A trigger with targets and no legal target never reaches the stack.
- A triggered or activated layer still resolves after its source is gone
  (CR 1.7.1a). *Example:* {{ card("energy-potion-3") }} is destroyed to
  activate it, and you still gain the resources.
- A triggered-static ability still triggers when its source is destroyed by
  the same event (CR 5.4.6a). *Example:* {{ card("merciful-retribution-2") }}
  triggers when an aura you control is destroyed, including itself.

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
