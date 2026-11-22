---
tags:
  - Flesh and Blood
fg:
  subtabs: true
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Playing Cards

Paying for cards, the steps for playing a card or activating an ability, and
what happens when a layer resolves. Click a card name to see the card and
its current text.

[Quiz this page](quiz.md?set=playing){ .md-button }

## Costs and assets

- There are four kinds of assets: **action points, resource points
  {{ sym("r") }}, life points {{ sym("h") }} and chi points {{ sym("c") }}**
  (CR 1.13). *Example:* {{ card("energy-potion-3") }} gives resource points,
  and {{ card("sigil-of-solace-1") }} gives life points.
- **Payment order** for mixed costs: chi, then resources, then life, then
  action points (CR 1.14.2a).
- **Pitching:** you pitch one card at a time, only while you still owe a
  cost that card would help pay, or when an effect tells you to. You can't
  pitch "extra" (CR 1.14.3b). Pay 3 with 1 resource floating, pitch a blue
  {{ card("sink-below-3", "Sink Below") }} (worth 3), and you have 1 left over
  and can't pitch again.
- **Chi** can pay resource costs, and has to be spent *before* resource
  points (CR 1.14.2d).
- **Cost calculation** for playing a card (CR 5.1.6a): start at the printed
  cost, apply "set" effects, then increases, then reductions. A cost can't go
  below 0. Increases come before reductions whatever their timestamps.
  *Example:* {{ card("bleed-out-1") }} costs less for each point of dagger
  damage this chain. Any cost increase is applied first, then Bleed Out's
  reduction, and it never drops below 0.
- An action card costs 1 action point, unless it's played as an instant, in
  which case it costs 0 (CR 5.1.6b).
- A zero cost is still a cost. You pay it by acknowledging it (CR 1.14.5).
  *Example:* {{ card("sink-below-1") }} costs 0, and playing it still goes
  through the payment steps.

## Playing cards and activating abilities

Playing a card goes through nine steps (CR 5.1). Nobody has priority in
between them.

1. **Announce:** the card moves to the stack. "Next card you play" effects
   that match it start to apply. *Example:* {{ card("come-to-fight-1") }}'s
   +3 power attaches to the next attack action card as soon as it's announced.
   {{ card("become-the-cup-1") }} picks its color here too (CR 5.1.2a).
2. **Declare costs:** X, optional extra costs, alternative costs. *Example:*
   {{ card("reckless-swing-3") }} has an extra cost of discarding a random
   card.
3. **Declare modes and targets.** Attacks declare their attack-target here.
   *Example:* {{ card("lunging-press-3") }} picks its target attack here.
4. **Check legal play.** If it's illegal, everything is reversed.
5. **Calculate asset-costs.**
6. **Pay asset-costs** (pitching happens here).
7. **Calculate effect-costs.**
8. **Pay effect-costs.**
9. **Play:** the card is played, and the player gets priority again.

- You play cards from **hand or arsenal** unless an effect says otherwise
  (CR 5.1.1a). *Example:* {{ card("ghostly-visit-1") }} also allows the
  banished zone.
- Activated abilities are written as *limit, type — cost: ability, condition*.
  Activating needs priority, a functional ability, and control of its source.
  Otherwise it follows the same steps as playing a card (CR 5.2). *Example:*
  {{ card("energy-potion-3") }}: the type is Instant, the cost is "destroy
  this", and the ability is "gain 2 resources".
- **Modes** are chosen as the layer goes on the stack, and the number of
  modes is fixed at that point (CR 1.7.5). *Example:*
  {{ card("art-of-war-2") }} says "choose 2", so you pick two different modes.
  {{ card("sacred-art-undercurrent-desires-3--inner-chi-3") }} lets you choose
  3 if you've played another blue card. That's checked when you choose, and
  doesn't change later.

## Resolving a layer (CR 5.3)

1. **Check:** a defense reaction that can't become a defending card fails
   here.
2. **Static abilities** of the layer turn on.
3. **Effects** happen in order, except go again. If one fails, the rest
   still happen.
4. **Go again:** the controller gains 1 action point, using LKI if needed.
   *Example:* {{ card("head-jab-1") }} has go again, so you get the action
   point back when it resolves.
5. **Leave the stack:** permanents go to the arena, and defense reactions
   become defending cards.
6. **Clear** whatever is left. The turn-player gets priority.

!!! tip "Targets"
    If *every* target of a targeted effect is gone or illegal, **that effect**
    fails. The layer still resolves and does everything else (CR 1.8.9,
    5.3.4b; January 30, 2026 rules update). An attack with no legal target
    left when it would hit the chain is the exception: it's removed from
    the queue (CR 7.2.2c).

    *Example:* {{ card("flick-knives") }} targets a dagger and a hero. If the
    dagger is gone before it resolves, the damage effect fails and no damage
    is dealt.

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
