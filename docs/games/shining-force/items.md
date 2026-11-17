---
platform: Genesis
spoilers: none
status: draft
tags:
  - Shining Force
---

# Items

Every item shop sells the same four items. Everything else comes from
chests, listed in the order you reach them.

{% for g in sf_items.groups %}
## {{ g.type }}

{% if g.note %}{{ g.note }}

{% endif -%}
| Item | Price | Effect | Where |
|------|------:|--------|-------|
{% for i in g['items'] -%}
| **{{ i.name }}** | {{ i.price }} | {{ i.effect }} | {{ i.where }} |
{% endfor %}
{% endfor %}

## Sources

- Prices, healing amounts and chest locations: Dark_Vortex's
  [Shining Force guide](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/51880)
  (GameFAQs).
- Stat item amounts and Shower of Cure: the GameFAQs
  [guide and walkthrough](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/14731)
  and GLSicherman's
  [FAQ](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/2837).
- Hidden costumes and joke items:
  [DvDTranslations' secrets guide](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/63031),
  checked against the US item list in a
  [save state hacking guide](https://gamefaqs.gamespot.com/genesis/563340-shining-force/faqs/7586)
  (GameFAQs).
