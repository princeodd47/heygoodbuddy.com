---
tags:
  - Flesh and Blood
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Glossary

Short definitions, in our own words. The numbers point into the
Comprehensive Rules (CR), the Procedure and Penalty Guide (PPG), and the
Tournament Rules and Policy (TRP). Click a card name to see an example card
and its current text.

| Term | Meaning | Ref | Example |
| --- | --- | --- | --- |
| Action point | What you spend to play an action card or use an action ability. You get 1 at the start of your action phase, and you can only gain them on your own turn | CR 1.13.2 | {{ card("lead-the-charge-1") }} |
| Active chain link | The chain link that's currently resolving | CR 7.0.3b | {{ card("flittering-charge-1") }} |
| Allowance | A rule or effect saying something *may* happen. The weakest of the three | CR 1.0.2 | {{ card("ghostly-visit-1") }} |
| Arena | The hero, equipment, weapon and permanent zones plus the combat chain. It isn't a zone itself, and it doesn't include arsenal, hand, deck, graveyard, banished, pitch or stack | CR 3.0.5 |  |
| Arsenal | A private zone outside the arena. Each arsenal zone holds at most one of its owner's deck-cards, which can be played from there | CR 3.3 | {{ card("entangling-shot-1") }} |
| Arena-card | Any card that isn't a hero, token or deck-card, such as equipment and weapons. It can't start in the deck | CR 1.3.2d | {{ card("pillar-of-unity") }} |
| Assisted information | Card text, rules and policy. A judge provides it on request | TRP 5.1 |  |
| Attack-layer | A layer from an "attack with" effect. It isn't an attack, and it makes one when it resolves | CR 1.4.4 | {{ card("and-again-3") }} |
| Attack-proxy | The attack object a weapon or ally creates. It inherits its source's properties | CR 1.4.3 | {{ card("bone-basher") }} |
| Attack queue | Where an attack waits after leaving the stack, before it becomes a chain link | CR 7.1 |  |
| Card-pool | Every card a player brings for the format: deck-cards and arena-cards | CR 1.1.3 |  |
| Caution | Penalty level 0. Spoken only and not recorded | PPG 1.4 |  |
| Chain link | One attack and its defenders on the combat chain | CR 7.0.3 | {{ card("double-strike-1") }} |
| Chi {{ sym("c") }} | An asset that can pay resource costs. It has to be spent before resources | CR 1.13.5 | {{ card("sacred-art-undercurrent-desires-3--inner-chi-3", "Inner Chi") }} |
| Close step | The last combat step. No priority. Permanents go home and the rest is cleared | CR 7.7 | {{ card("pillar-of-unity") }} |
| Controller | Whoever controls an object. Only objects in the arena or on the stack have one | CR 1.2.1b | {{ card("sirens-of-safe-harbor-1") }} |
| Deadlock | Every player *refuses* to move the game toward an end. The game is a draw | CR 4.5.4e |  |
| Deviation | The Head Judge choosing a different fix or penalty from the PPG | PPG 1.2 |  |
| Discrete effect | A one-off effect that makes an event and is done | CR 6.1 | {{ card("sand-sketched-plan-3") }} |
| Effect-cost | A cost paid by doing something, such as destroying or discarding | CR 1.14.4 | {{ card("reckless-swing-3") }} |
| FtMGS | Failure to Maintain Game State. The opponent's side of a gameplay error | PPG 2.2 |  |
| Game state action | A check made before priority: losses, clearing 0-life cards and extra uniques, then triggers | CR 1.10.2 | {{ card("blasmophet-the-insatiable-hunger") }} |
| GRV | Game Rules Violation | PPG 2.1 |  |
| HCE | Hidden Card Error | PPG 2.5 |  |
| Historical information | Something that used to be public but no longer matters, like a card revealed and returned to hand | TRP 5.1 |  |
| Inventory | The cards from a card-pool that weren't chosen for the game. Private, and not a zone | CR 4.1.7 | {{ card("taylor") }} |
| IP2 | Intellect Penalty: -1 intellect {{ sym("i") }}, so you draw 1 fewer card for 2 end-of-turn draws | PPG 1.4 |  |
| Last known information | A frozen snapshot of an object just before it left. Used when a rule needs that object | CR 1.2.3 | {{ card("endless-arrow-1") }} |
| Layer | A card, activated ability or trigger on the stack that hasn't resolved yet | CR 1.6 | {{ card("energy-potion-3") }} |
| Layer-continuous effect | An ongoing effect made by a layer resolving. Ends at end of turn unless it says otherwise | CR 6.2.2 | {{ card("come-to-fight-1") }} |
| LEC | Looking at Extra Cards | PPG 2.4 |  |
| Macro | An object in the arena that isn't a card and is created by tournament rules. An IP is one | CR 1.5 | {{ card("sanctuary-of-aria") }} |
| Multi-event | Several similar events from one instruction, like "draw 3". Triggers fire once | CR 1.9.2 | {{ card("tome-of-harvests-3") }} |
| Out-of-order play | Doing legal actions slightly out of sequence when the result is the same | TRP 5.3 |  |
| Partial fix | Correcting the current game state instead of rewinding | PPG 1.3 |  |
| Permanent | A card that stays in the arena: hero, equipment, weapon, token, ally, aura, item and so on | CR 1.3.3 | {{ card("energy-potion-3") }} |
| Pitch | Moving a card from hand to the pitch zone to gain resources {{ sym("r") }}. Allowed only while a cost needs it | CR 1.14.3 | {{ card("sink-below-3", "Sink Below") }} |
| Priority | Permission to play or activate something. Only in the action phase | CR 1.11 | {{ card("predatory-plating") }} |
| Public information | Facts not shown on the table but known to everyone, such as floating resources and choices made | TRP 5.1 |  |
| REL | Rules Enforcement Level: Casual, Competitive or Professional | TRP 1.2 |  |
| Replacement effect | Changes an event before it happens ("instead", "prevent") | CR 6.4 | {{ card("drone-of-brutality-1") }} |
| Requirement | A rule or effect saying something *must* happen if possible | CR 1.0.2 |  |
| Restriction | A rule or effect saying something *can't* happen. The strongest of the three | CR 1.0.2 | {{ card("hypothermia-3") }} |
| Shortcut | Skipping obvious priority passes in a way everyone understands | TRP 5.2 |  |
| Simple rewind | Undoing the last action or two when the error is caught right away | PPG 1.3 |  |
| Stalemate | No player *can* move the game toward an end. The game is a draw | CR 4.5.4d |  |
| Static-continuous effect | An ongoing effect from a static ability that updates live | CR 6.2.3 | {{ card("luminaris") }} |
| Timestamp | When an effect was created. It breaks ties when applying effects | CR 6.3.4 |  |
| Triggered effect | "When / whenever / at / the next time" effects that put a layer on the stack | CR 6.6 | {{ card("gravekeeping-1") }} |
| Turn-player | The player whose turn it is. They break most ordering ties | CR 4.0.3b |  |
| Unverified information | A hidden fact that let a player do something, like a cloaked card. Shown on request at the end of the game | TRP 5.1 |  |
| Visible information | What's shown on the table: cards, zones, counters, life totals | TRP 5.1 |  |

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
