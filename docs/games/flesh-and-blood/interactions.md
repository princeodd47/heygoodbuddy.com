---
tags:
  - Flesh and Blood
---

{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Card Interactions

Release notes, Rules Reprise articles and rules updates, **newest first**.
When two of them conflict, the newer one wins. Check the date before you
trust an older article. Release notes are rarely updated after a set
releases. Click a card name to see the card and its current text.

## Themes that keep coming up

These six ideas explain most release-note rulings. Learn the rule behind
each one, and new cards get much easier to rule.

1. **No priority while something is resolving** (CR 1.11.5). You can't step
   in partway through a card's effects, partway through playing a card, or
   in the start phase, end phase or close step. *Example:*
   {{ card("starflow-robes") }} can't be used between the two damage
   instructions of one card.
2. **Nothing is retroactive.** If a condition is met *after* a trigger
   moment, the trigger doesn't go back and fire. The static bonus still
   applies, though (CR 6.6.5a). *Example:* {{ card("tempestuous-kiss-1") }}
   given go again after it's attacking gets +1 power, but not its "when this
   attacks a hero" damage. {{ card("pillar-of-unity") }} misses its Unity
   bonus if the card from hand is a defense reaction played later.
3. **Last known information.** If a card leaves, its chain link or effect
   uses its last known state, and that state can't change (CR 1.2.3).
   *Example:* {{ card("endless-arrow-1") }} returns to hand on hit, and its
   chain link still gives the action point if it had go again.
4. **Triggers wait for the next priority window.** A trigger caused while
   applying prevention, like destroying a Ward card, goes on the stack
   afterward. It can't affect the damage event that caused it. *Example:*
   {{ card("flicker-reality-3") }}.
5. **Optional means you have to be able to do all of it** (CR 1.8.3b). An
   optional targeted trigger can also be put on the stack with no target,
   and then none of it happens. *Example:* {{ card("magmatic-carapace") }}
   needs you to be able to tap it *and* pay. {{ card("sigil-of-silphidae-3") }}'s
   trigger can go on the stack with no target.
6. **"When this defends" triggers however the card became a defender.**
   That includes an opponent's effect adding it. *Example:*
   {{ card("scowling-flesh-bag") }}'s "when this defends, intimidate" still
   triggers if an opponent's effect made it a defender.

## Rules updates and articles

??? abstract "September 21, 2026 — Rules Reprise: Usurp the Shadow Throne (Constructed)"
    Rulings for the newest set in Constructed. The new keywords are in
    [Usurp the Shadow Throne](#usurp-the-shadow-throne) below.

??? abstract "September 17, 2026 — Rules Update"
    - **Start of game:** arena-cards are now chosen and revealed *before*
      the deck is chosen. It started as a trial and is now in CR 4.1 and
      TRP 3.3.
    - **Randomization aides:** when picking a random card from the
      graveyard by shuffling face down, a player can use a placeholder card
      that shows only the real card's English name and pitch (TRP 5.12).

??? abstract "June 11, 2026 — Draft Procedure Rules Guide"
    Covers zone drafts and called drafts, and what counts as a minor or
    major Draft Procedure Violation (PPG 3.6).

??? abstract "May 28, 2026 — Rules Reprise: Omens of the Third Age (Constructed)"
    Rulings for quickstrike, starfall, fragment and Lightning Flow
    interactions. See [Omens of the Third Age](#omens-of-the-third-age).

??? abstract "May 19, 2026 — Rules Update"
    - **Attack queue:** when an attack would resolve, it goes into a queue
      and enters the combat chain from there (CR 5.3.1a, 7.1).
    - **Attack-layers:** "attack with" effects (Beckon Steel, And Again…)
      make a layer that isn't an attack. Effects on that layer don't carry
      over to the attack it creates (CR 1.4.4b). If
      {{ card("mage-master-boots") }} gives
      {{ card("and-again-3", "And Again…") }} go again, the sword attack
      doesn't get it. {{ card("beckon-steel-3") }} works the same way.

??? abstract "February 5, 2026 — Rules Reprise: Compendium of Rathe"
    Rulings for the set's Brute, Guardian and returning cards, including
    **sharpen**. {{ card("predatory-plating") }} is the one most often
    brought up. See
    [Compendium of Rathe](#compendium-of-rathe).

??? abstract "January 30, 2026 — Rules Update"
    - **An attacking ally's controller is the attacking hero.**
    - **An attacked ally's controller is the defending hero**, but still
      can't declare defenders or play defense reactions for the ally unless
      an effect allows it (CR 7.3.2a, 7.4.2b).
    - **Targeted layers still resolve.** If all of a layer's targets are
      gone, only the targeted effect fails, and the rest still happens. An
      attack that has lost its target is still removed (CR 7.2.2c).
    - **{{ card("pummel-1", "Pummel") }}** got a functional erratum. Click it
      for the current text.

??? abstract "May 29, 2025 — Back Alley Oracle #17"
    - Basic rarity was added.
    - Choosing objects is limited to the arena and the stack unless the
      effect says otherwise.
    - Spectra no longer closes the combat chain.
    - Attack reactions can be played for ally attacks.
    - Continuous effects with no stated duration last until end of turn.
    - Players may reorder their own graveyards.

??? abstract "January 24, 2025 — Back Alley Oracle #16"
    - Combat steps were merged into the current seven.
    - Rules for naming any card.
    - The play-off tiebreaker procedure (TRP 3.4).

??? abstract "October 25, 2024 — Back Alley Oracle #15"
    The note-taking philosophy. Ask yourself: *would I be penalized if I
    forgot this?* If yes, you may keep a marker for it, like life or
    floating resources. If no, you can't, like a turn count or pitch order.

## Set release notes

### Usurp the Shadow Throne

Legal **September 25, 2026**.

- **New keywords:** bind, decay, incarnate, Shadow Resist, traverse, unique,
  usurp. See the [Rules](rules.md#keywords-to-know) keyword table.
- **{{ card("soul-of-existence-4") }}** is the first **purple** card, with
  pitch 4.
- **Unique** is a game state action. If you control two permanents with the
  same name and one has unique, you clear down to one (CR 8.3.48a).
  *Example:* {{ card("blasmophet-the-insatiable-hunger") }}.
- **Incarnate** cards can't start in your deck. Removing one this way isn't
  "dying" (CR 8.3.46). *Example:* {{ card("corrupted-corpse") }}.
- **Bind:** a binding card that loses its bound card is cleared as a game
  state action (CR 8.3.44b).
- **{{ card("chains-of-consecration-2") }} on
  {{ card("corrupted-corpse") }}:** go again still applies through last known
  information.

### Mastery Pack: Warrior

Legal **August 7, 2026**. Reprints only, with no new rulings.

### Omens of the Third Age

Legal **June 5, 2026**. Keywords: **fragment**, **quickstrike**,
**starfall**.

- **Quickstrike isn't retroactive.** An attack that gains go again after it
  becomes attacking gets the static bonus, like +1 power. Its "when this
  attacks a hero" trigger doesn't fire, because that moment has passed
  ({{ card("tempestuous-kiss-1") }}, {{ card("dashing-flashfoot-2") }} and
  others).
- **{{ card("quick-succession-1") }}:** if an attack gets go again from an
  on-hit trigger,
  the +1 only applies after that trigger resolves. That's too late for the
  damage already dealt.
- **Starfall** is checked when the card resolves.
  {{ card("astral-bridge-1") }} can turn on its own starfall by milling an
  instant first.
- **Prevention between effects:** {{ card("starflow-robes") }},
  {{ card("glide-through-starlight-1") }} and the Astral Sanctuary set can't
  be used between two damage instructions on the same card. The card resolves completely before anyone gets
  priority.
- **Prevention doesn't stop life loss.** {{ card("constella-tiara") }} and
  the others
  prevent physical, arcane and untyped damage, but not loss of life.
- **Ward destroyed, holo counter too late:** destroying
  {{ card("flicker-reality-3") }} for
  its Ward creates a trigger. That trigger can't power up another card's
  Ward in time for the same damage event.
- **The "Duality" cards** ({{ card("cosmic-duality-1") }} and others):
  discarding one to pay for its ability is
  activating an instant ability, *not* playing an instant. If the target
  hero is gone, you still create the Lightning Flow token.
- **{{ card("oscilio") }}:** discarding a card with an instant *ability*
  isn't discarding an instant *card*.
- **Tokens that leave the arena cease to exist.** A banished Lightning aura
  token never comes back ({{ card("blink-of-an-eye-1") }},
  {{ card("flicker-reality-3") }}).

### Compendium of Rathe

Legal **February 13, 2026**. Keyword: **sharpen**: put a +1 power counter
on it, then remove them at the beginning of the end phase (CR 8.5.58).
*Example:* {{ card("sharpening-sparks-1") }}.

!!! example "Predatory Plating"
    {{ card("predatory-plating") }}: *Instant — Destroy this: gain resources.
    Activate this only if you control a card with 6 or more power.*

    You **can't** activate it to help pay for the 6-power card you're in
    the middle of playing. During the nine steps of playing a card no one
    has priority (CR 1.11.5). Activating an instant ability needs priority
    (CR 5.2.2). "Control" means a card in the arena or on the stack. A
    6-power card in your hand doesn't count. A 6-power attack already on
    the stack or chain does count, so you can activate Plating *after*
    it's played, to pay for something else.

- **{{ card("touch-of-reality") }}** with X = 0 gets Ward 0. Using it to prevent damage
  still destroys it.
- **{{ card("graven-gaslight") }} / Spellvoid:** you can't use Spellvoid 1, then re-equip
  and use Spellvoid again on the **same** arcane damage event. There's no
  priority in the middle of an event.
- **{{ card("magmatic-carapace") }}:** its optional effect needs you to be able to both
  tap it *and* pay. If you can't do both, you can't choose it.
- **{{ card("sigil-of-silphidae-3") }}, {{ card("runic-fellingsong-1") }},
  {{ card("weeping-battleground-1") }}:** you can
  put the trigger or card on the stack without a target. If you do, none of
  it happens.
- **Bond (Earth/Lightning/Ice):** you have to pitch a matching card *while
  paying for this card*. Resources from an earlier pitch don't count.
  *Example:* {{ card("strong-wood-1") }}.
- **Contract ({{ card("mist-hunter-1") }},
  {{ card("excessive-bloodloss-1") }}):** **you** have to be the
  one banishing the opponent's card. If the opponent banishes their own
  card, it doesn't count.
- **{{ card("lay-down-the-challenge-2") }}:** you can intimidate yourself, but then you
  won't draw.
- **{{ card("rip-off-the-top-2") }}:** pitching a random card still gives you resources and
  still triggers pitch effects.
- **{{ card("scuttle-toes") }}:** untapping an ally that's already untapped fails. The
  ally is still destroyed at the end phase.

### Super Slam

Legal **September 26, 2025**. Introduced **suspense** (CR 8.3.42) and the
crowd **cheers** / **boos** mechanics. *Examples:*
{{ card("to-be-continued-3", "To Be Continued...") }} (suspense),
{{ card("overturn-the-results-3") }} (boos).

### High Seas

Legal **June 6, 2025**. Introduced **tap/untap**, **give**, **steal**,
**companion**, **perched**, **unlimited**, **watery grave**, **high tide**
and **go fish**. Tapping a permanent that's already tapped fails
(CR 8.5.55a). Give and steal both change who controls the object.
*Examples:* {{ card("entangling-shot-1") }} (tap),
{{ card("money-or-your-life-1") }} (give).

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
