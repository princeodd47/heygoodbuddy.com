---
game_version: Demo
platform: PS5
spoilers: none
verified: 2026-10-19
status: draft
tags:
  - Final Fantasy Resonance
---

# Visions

Visions are the crystallized essence of legendary heroes. They take the place
of a job system: equipping a Vision decides which abilities a character can
learn.

## Where to get Visions

| Vision | Where to get it |
|--------|-----------------|
{% for v in ffr.visions -%}
| **{{ v.name }}** | {{ v.how_to_get }} |
{% endfor %}

Tronn and Leah are story rewards: you can't miss them. The others are found in
optional **sanctums** on the world map.

## Mastery

Mastery is how a Vision's base abilities are learned.

- A Vision earns Mastery Points every time its wielder fights.
- Each Mastery rank unlocks abilities and permanent stat boosts.
- Mastery is tracked **per character**. If two characters use the same
  Vision, each one levels it separately.
- Learned abilities have to be equipped, and each one costs AP. A character's
  AP total caps how many fit.
- Abilities stay learned, so you can equip them while using a different
  Vision, as long as the AP allows.

## Awakening

Each Vision has three greyed-out stars. Awakening a Vision fills in a star
and permanently unlocks another set of skills and passives on top of the base
set. Awakening is separate from Mastery: it only happens when you spend
magicite.

The costs below come from third-party guides and are *unverified*.

| Tier | Cost |
|------|------|
| ★ | Magicite Shard |
| ★★ | Magicite |
| ★★★ | Magicite Cryst |

### Where to awaken

After you defeat **Siren** in Siren's Tower, the **Moogle of Light** appears
in **Grandport**. It gives a tutorial on using magicite and gives you a
**Magicite Shard**. Talk to it to awaken your Visions.

### Where to get Magicite Shards

- **Siren's Tower:** one in a chest
- **Oblivion Palace (Area 2/5):** two in chests
- **Boss drops:** reportedly Siren, Marauder and Leviathan
- **Side quests:** some reward them

Tablet Shards are a separate item. See [Tablet Shards](tablet-shards.md)
for where to find them and what they're traded for.
