---
tags:
  - Flesh and Blood
fg:
  list:
    show: [Meaning]
    placeholder: Keyword, meaning
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}
{% macro card(id, label=None) %}[{{ label or fab_cards.cards[id].front.name }}](../../assets/images/flesh-and-blood/cards/{{ id }}.webp){ .fab-cardref data-card="{{ id }}" }{% endmacro %}

# Keywords

What each keyword does, with a card that has it. The CR column is the rule
to read in full. Click a card name to see the card and its current text.

[Quiz this page](quiz.md?set=keywords){ .md-button }

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

<script id="fab-cards-data" type="application/json">{{ {"cards": fab_cards.cards, "icons": fab_icons} | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
