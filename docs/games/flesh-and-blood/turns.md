---
tags:
  - Flesh and Blood
fg:
  subtabs: true
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Turns & Priority

Who can act and when, from the start of the game to the end of a turn.
Click a card name to see the card and its current text.

[Quiz this page](quiz.md?set=turns){ .md-button }

## Priority

- Only one player has priority at a time. Players only get priority in the
  **action phase** (CR 1.11.3).
- **No one has priority** while a card is being played, an ability is being
  activated, a layer is resolving, or game state actions are happening
  (CR 1.11.5). This explains a lot of release-note rulings. You can't
  respond halfway through a card's resolution. You also can't activate an
  instant ability halfway through paying a cost. *Example:*
  {{ card("predatory-plating") }} can't be activated to help pay for the
  6-power card you're in the middle of playing (see
  [Card Interactions](interactions.md#compendium-of-rathe)).
- The **turn-player** gets priority at the start of the action phase, after
  each layer resolves, and at the start of most combat steps.
- If everyone passes in a row with something on the stack, the top layer
  resolves. With an empty stack, the step or phase ends (CR 1.11.4a).
- No priority in the **start phase**, the **end phase**, or the
  **close step** of combat (CR 4.2.1, 4.4.1, 7.7.1). *Example:* the Temper
  counter on {{ card("pillar-of-unity") }} goes on in the close step, so no
  one can respond to it.

## Start of game (CR 4.1)

1. Heroes go face up.
2. A randomly chosen player picks who goes first. In later games, the player
   who lost the previous game picks. After a draw, the same player picks
   again.
3. Each player secretly picks arena-cards: up to one each for head, chest,
   arms, legs and weapon zones. *Example:*
   {{ card("kayo-underhanded-cheat") }} starts the game with only one weapon
   zone, and doesn't get a second one back even if Kayo loses that ability
   (CR 4.1.2a).
4. Arena-cards are revealed, starting with the first player.
5. Each player picks the deck-cards for their deck. *Example:*
   {{ card("dash") }} may start with a cheap Mechanologist item in the arena.
   It's chosen from the deck, so a 40-card deck starts with 39 cards in the
   deck zone (CR 4.1.6b).
6. Everything left over becomes the player's **inventory**. It's private and
   isn't a zone.
7. Decks are shuffled and presented to an opponent to shuffle or cut.
8. "Start of the game" triggers resolve.
9. Everyone draws up to intellect.

!!! note "Arena-cards before the deck"
    Arena-cards are now chosen *before* the deck. This started as a trial in
    the September 17, 2026 rules update and is now in the CR and TRP.

## Start phase and action phase

- Start phase: "until start of turn" effects end, then start-of-turn
  triggers resolve. No priority (CR 4.2).
- Action phase: beginning-of-action-phase triggers, then the turn-player gets
  **1 action point** and priority. Gaining that point doesn't count as
  "gaining an action point" for triggers or replacements (CR 4.3.2).
- A player can only gain action points during **their own** action phase.
  An action card played as an instant on an opponent's turn gives no action
  point from go again (CR 1.13.2b). *Example:* if you play
  {{ card("lead-the-charge-1") }} as an instant on an opponent's turn, its go
  again gives you nothing. Neither does its own "gain 1 action point" when
  you play another action card that turn.

## End phase (CR 4.4)

Beginning-of-end-phase triggers resolve first. *Example:* the card banished
by {{ card("lay-down-the-challenge-2") }}'s intimidate comes back here, before
the arsenal step. Then the end-of-turn procedure runs in this order:

1. Allies' life resets to base (counters still count).
2. The turn-player may put a card from hand face down into an empty arsenal.
3. Every player puts their pitch zone on the bottom of their deck, in any
   order. The order is hidden information.
4. The turn-player untaps their permanents.
5. Everyone loses all action points and resource points.
6. The turn-player draws up to intellect. On the **first turn of the game,
   every player** draws up to intellect.

Then the turn ends. "This turn" effects end, and play passes clockwise.

## Ending a game (CR 4.5)

- A player loses at 0 life, with no hero, by an effect, or by conceding.
- If every remaining hero hits 0 at the same time, the game is a draw. A
  stalemate (no one *can* advance) or a deadlock (no one *will* advance) is
  also a draw.

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
