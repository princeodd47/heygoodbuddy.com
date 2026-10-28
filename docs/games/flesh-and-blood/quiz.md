---
hide:
  - toc
tags:
  - Flesh and Blood
---

# Practice Quiz

Pick a question set and start. Answers are shuffled every time. After each
answer you get the reason and the rule number to look up. Questions you
miss are saved in this browser, and **Review missed** brings them back
until you get them right. The real exams need **85%**. Only fresh practice
runs are checked against that; reviews and My rulings just show your score.

- **L1A practice** draws from the [Rules](rules.md) and
  [Card Interactions](interactions.md) pages.
- **L1B practice** draws from [Policy & Penalties](policy.md).
- **My rulings** asks every ruling from `data/flesh-and-blood/my-rulings.yaml`,
  in the order they're written there.

<div id="fab-quiz"></div>

<noscript>The quiz needs JavaScript.</noscript>

<div id="fab-quiz-icons" hidden markdown>
{% for k, name in fab_icons.items() %}![{{ name }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ data-key="{{ k }}" }
{% endfor %}
</div>

<script id="fab-quiz-data" type="application/json">{{ fab_quiz | tojson }}</script>
<script id="fab-quiz-mine" type="application/json">{{ (fab_my_rulings.questions or []) | tojson }}</script>
<script id="fab-quiz-cards" type="application/json">{{ (fab_cards.cards or {}) | tojson }}</script>

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
