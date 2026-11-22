---
tags:
  - Flesh and Blood
fg:
  subtabs: true
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Rules

The Comprehensive Rules (CR), arranged by concept over six pages. Most card
examples come from the CR itself. Click a card name to see the card and its
current text.

Read one page, then take its quiz.

| Page | Covers |
| --- | --- |
| **Rules** (this page) | What wins a conflict, players and objects, last known information, numbers and symbols |
| [Turns & Priority](turns.md) | Priority, the start of the game, each phase of a turn, how a game ends |
| [Playing Cards](playing-cards.md) | Costs and assets, the steps for playing a card, resolving a layer |
| [Effects](effects.md) | Optional, conditional and targeted effects, events, continuous, replacement and triggered effects |
| [Combat](combat.md) | The combat chain and its steps, hits, allies, weapons and attack-layers |
| [Keywords](keywords.md) | What each keyword does, with a card for each |

[Quiz this page](quiz.md?set=basics){ .md-button }

## What wins a conflict

- **Tournament rules beat card text, and card text beats the CR**
  (CR 1.0.1a–b). *Example:* the CR says you play cards from hand or arsenal,
  but {{ card("ghostly-visit-1") }} says you may play it from your banished
  zone. The card wins. *Example:* {{ card("taylor") }} lets you put equipment
  of any class into your inventory, but the Card Legality Policy (TRP 7) says
  a banned card can't be in a card-pool at all. The tournament rule wins, so
  Taylor still can't bring a banned piece of equipment.
- **A restriction beats a requirement, and a requirement beats an allowance**
  (CR 1.0.2). A "can't" beats a "must", and a "must" beats a "may". If one
  effect says you can't play cards from your banished zone and another says
  you may, you can't. *Example:* {{ card("hypothermia-3") }} says your
  attacks can't gain go again. If {{ card("torrent-of-tempo-1") }} hits while
  you have Hypothermia, it doesn't get the go again it gives itself on hit.
- **"Only" is a restriction.** "You may only play cards from arsenal" means
  you can't play from anywhere else, even if another effect lets you
  (CR 1.0.2a). *Example:* after {{ card("three-of-a-kind-1") }}, you can't
  play {{ card("ghostly-visit-1") }} from your banished zone for the rest of
  the turn.
- **Restrictions aren't retroactive.** An attack that gains overpower after
  two action cards defend it keeps both defenders (CR 1.0.2b). *Example:*
  {{ card("over-the-top-1") }} gets overpower once its power is above its
  base. If {{ card("lunging-press-3") }} pumps it in the reaction step, it
  gains overpower, but both defenders stay.

## Players, objects and ownership

- **"You"** means the controller of the object. If nothing controls it, "you"
  means the owner. A card revealed in a clash has no controller, so its
  "you" is its owner (CR 1.1.2b). *Example:* {{ card("the-golden-son-2") }}
  says "when you win a clash revealing this, create a Gold token". Revealed
  from the deck, it has no controller, so its owner is the one who has to win
  the clash.
- **Card-pool:** every card's supertypes have to be a subset of the hero's
  supertypes. Cards with no supertypes are generic and fit any hero
  (CR 1.1.3). *Example:* {{ card("ironsong-determination-2") }} is a Warrior
  card, so only a Warrior hero can use it. {{ card("sink-below-1") }} is
  Generic and fits any deck.
- **Owner and controller:** a card only has a controller while it's in the
  arena or on the stack. A layer is controlled by the player who put it on
  the stack (CR 1.2.1, 1.3.1b, 1.6.1b). *Example:*
  {{ card("sirens-of-safe-harbor-1") }} triggers when it's put into "your"
  graveyard. If you play your opponent's copy, you control it, so when it goes
  to *their* graveyard it doesn't trigger for anyone (CR 3.0.7a).
- **Distinct cards:** cards with a different name *or pitch* are different
  cards. A red {{ card("sink-below-1", "Sink Below") }} and a yellow
  {{ card("sink-below-2", "Sink Below") }} are separate cards for copy limits
  (CR 1.3.4).
- **Permanents:** heroes, arena-cards and tokens in the arena. A deck-card
  becomes a permanent only with a permanent subtype, such as Ally, Aura,
  Item, Landmark or Affliction (CR 1.3.3). *Example:*
  {{ card("energy-potion-3") }} is an Item, so it stays in the arena after it
  resolves. {{ card("sink-below-1") }} has no permanent subtype and goes to
  the graveyard.

## Last known information

If a rule or effect needs information about an object that no longer
exists, it uses a snapshot from just before the object left (CR 1.2.3).

- LKI includes counters and the effects on the object.
- LKI **can't be changed**. *Example:* {{ card("luminaris") }} gives your
  Illusionist attacks go again while a yellow card is in your pitch zone. If
  an Illusionist attack has already left the chain, pitching a yellow card
  afterwards doesn't give its chain link go again.
- LKI **isn't an object**, so it can't be targeted. *Example:*
  {{ card("midas-touch-2") }} destroys an ally, then its controller creates
  Gold equal to its cost. The ally is gone by then, so LKI supplies both the
  controller and the cost.
- *Example:* {{ card("endless-arrow-1") }} hits and returns to hand. Its
  chain link still uses the arrow's LKI, so if it had go again, the player
  still gains the action point.

## Numbers and symbols

Card text uses these symbols (CR 1.12.4). In the text-only rules documents
they appear as the letter in braces, like `{p}`.

| Symbol | Text | Meaning |
| --- | --- | --- |
| {{ sym("p") }} | `{p}` | Power. Also used for physical damage |
| {{ sym("d") }} | `{d}` | Defense |
| {{ sym("r") }} | `{r}` | Resource. Each one is 1 resource point |
| {{ sym("c") }} | `{c}` | Chi. Pays resource costs too, and is spent first |
| {{ sym("h") }} | `{h}` | Life |
| {{ sym("h") }} | `{g}` | Also life. Newer cards' text usually writes it this way; the icon is the same |
| {{ sym("i") }} | `{i}` | Intellect: how many cards you draw up to |
| {{ sym("t") }} | `{t}` | Tap a permanent |
| {{ sym("u") }} | `{u}` | Untap a permanent |

- Fractions round **toward zero**: 3.5 becomes 3, and -3.5 becomes -3
  (CR 1.12.1a).
- An undefined X or * counts as 0 (CR 1.12.2–3).
- If an effect asks for a property the object doesn't have (cost on Heart
  of Fyendal, for example), the object doesn't meet the condition. A number
  it needs from that missing property is 0 (CR 1.8.7).
- Opposing counters (+1 and -1) both stay on the object (CR 1.15.4).

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
