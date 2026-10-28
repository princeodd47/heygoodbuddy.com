---
tags:
  - Flesh and Blood
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Rules

The Comprehensive Rules (CR), arranged by concept. Each section ends with the
rule numbers to read in full. Most card examples come from the CR itself.
Click a card name to see the card and its current text.

## What wins a conflict

- **Tournament rules beat card text, and card text beats the CR**
  (CR 1.0.1a–b). *Example:* the CR says you play cards from hand or arsenal,
  but {{ card("ghostly-visit-1") }} says you may play it from your banished
  zone. The card wins.
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

### Last known information (LKI)

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

## Turn structure

### Start of game (CR 4.1)

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

### Start phase and action phase

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

### End phase (CR 4.4)

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

### Ending a game (CR 4.5)

- A player loses at 0 life, with no hero, by an effect, or by conceding.
- If every remaining hero hits 0 at the same time, the game is a draw. A
  stalemate (no one *can* advance) or a deadlock (no one *will* advance) is
  also a draw.

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

### Resolving a layer (CR 5.3)

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

## Effects

### Optional, conditional and targeted

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

### Events

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

### Continuous effects (CR 6.2–6.3)

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

### Replacement effects (CR 6.4–6.5)

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

### Triggered effects (CR 6.6)

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

## Combat (CR 7)

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

- While the chain is open, **action** cards and abilities can only be used
  as instants. The exception is new attacks during the resolution step
  (CR 7.0.1a).
- A **hit** is damage from the hit-event. If prevention brings that damage to
  0, it isn't a hit, and life loss is never a hit (CR 7.5.5). *Example:* if
  {{ card("feign-death-2") }} prevents all of an attack's damage, the attack
  didn't hit, so its "when this hits" effects don't trigger.
- **Attacking an ally:** its controller is the defending hero, but can only
  declare defenders or play defense reactions if an effect allows it. Those
  are only allowed when a *hero* is the attack-target (CR 7.3.2a, 7.4.2b).
- **An ally attacking:** its controller is the attacking hero (CR 7.2.3a).
  This was clarified in the January 30, 2026 rules update. *Example:*
  {{ card("cintari-sellsword") }} attacks through its own attack ability, and
  its controller is the attacking hero.
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

## Keywords to know

| Keyword | Meaning | CR | Example |
| --- | --- | --- | --- |
| Go again | Gain 1 action point when this resolves (or at the resolution step, for an attack). An object can't have go again twice | 8.3.5 | {{ card("head-jab-1") }} |
| Dominate | Can't be defended by more than 1 card **from hand**. Equipment and an arsenal defense reaction can still be added | 8.3.4 | {{ card("macho-grande-1") }} |
| Overpower | Can't be defended by more than 1 **action card** | 8.3.22 | {{ card("over-the-top-1") }} |
| Blade Break | When the chain closes, if this defended, destroy it | 8.3.3 | {{ card("ironrot-helm") }} |
| Battleworn | When the chain closes, if this defended, -1 defense counter | 8.3.2 | {{ card("seasoned-saviour") }} |
| Temper | Like battleworn, then destroy it at 0 defense | 8.3.10 | {{ card("pillar-of-unity") }} |
| Guardwell | When the chain closes, if this defended, -1 defense counters equal to its defense | 8.3.34 | {{ card("predatory-plating") }} |
| Ward N | If you'd be dealt damage, destroy this to prevent N | 8.3.20 | {{ card("spectral-shield") }} |
| Spellvoid N | If you'd be dealt arcane damage, you may destroy this to prevent N. If it can't be destroyed, you can't use it | 8.3.15 | {{ card("spell-fray-tiara") }} |
| Arcane Barrier N | If you'd be dealt arcane damage, you may pay N resources to prevent N | 8.3.8 | {{ card("nullrune-boots") }} |
| Legendary | Only 1 copy in a constructed deck | 8.3.6 | {{ card("heart-of-fyendal-3") }} |
| Specialization | Only allowed if your hero is the named hero | 8.3.7 | {{ card("blazing-aether-1") }} |
| Essence | Lets the deck include the listed supertypes | 8.3.16 | {{ card("oscilio") }} |
| Unique | Two or more permanents with the same name and one has unique: clear down to one (game state action) | 8.3.48 | {{ card("blasmophet-the-insatiable-hunger") }} |
| Intimidate | Banish a random card from hand face down, and return it at the beginning of the end phase. It counts even with an empty hand | 8.5.10 | {{ card("pack-hunt-1") }} |
| Opt N | Look at the top N cards and put them on the top or bottom in any order | 8.5.22 | {{ card("fate-foreseen-1") }} |
| Negate | Clear a layer from the stack. Only layers can be targeted | 8.5.26 | {{ card("rewind-3") }} |
| Combo | If the named card was the last attack this chain, get the bonus | 8.4.1 | {{ card("qi-unleashed-1") }} |
| Crush | Triggers when this **deals** 4 or more damage, not just on a hit | 8.4.2 | {{ card("knock-em-off-their-feet-1") }} |
| Sharpen | +1 power counter, removed at the beginning of the end phase | 8.5.58 | {{ card("sharpening-sparks-1") }} |
| Quickstrike | "If this has go again, …" | 8.4.20 | {{ card("rush-of-power-1") }} |
| Starfall | "If an instant has been put into your graveyard this turn, …" | 8.4.21 | {{ card("comet-collision-1") }} |
| Fragment | Whenever a card with 2+ defense defends this, -2 power | 8.3.43 | {{ card("erode-authority-1") }} |
| Decay | At the beginning of your end phase, -1 life counter | 8.3.45 | {{ card("restless-shieldmaiden-1") }} |
| Bind | Has to bind to another card when it enters. Cleared if it becomes unbound | 8.3.44 | {{ card("mark-of-pathstone-3") }} |
| Incarnate | Can't start in the deck. If it would die, it's removed from the game instead and doesn't count as dying | 8.3.46 | {{ card("corrupted-corpse") }} |
| Usurp | Additional cost: destroy a Runechant if able. If you do, +2 power | 8.3.49 | {{ card("runic-reaving-1") }} |
| Traverse | Flip a double-faced card to its other face | 8.5.60 | {{ card("viserai-between-worlds--viserai-usurper") }} |
| Suspense | Enters with 2 suspense counters, loses one each start of turn, and is destroyed at 0 | 8.3.42 | {{ card("to-be-continued-3", "To Be Continued...") }} |
| Give / Steal | The player gains control of the object | 8.5.53–54 | {{ card("patient-zero-1") }}, {{ card("undercover-acquisition-1") }} |
| Tap | Turn a permanent sideways. Tapping a tapped permanent fails | 8.5.55 | {{ card("entangling-shot-1") }} |

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
