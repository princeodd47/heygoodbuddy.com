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

!!! info "Page status"
    Last checked **{{ page.meta.verified }}** on the **{{ page.meta.game_version }}**.
    Anything marked *unverified* comes from third-party guides and hasn't
    been checked in-game yet.

Visions are the crystallized essence of legendary heroes. They take the place
of a job system: equipping a Vision decides which abilities a character can
learn.

## Visions in the demo

| Vision | How to get it | Status |
|--------|---------------|--------|
{% for v in ffr.visions -%}
| **{{ v.name }}** | {{ v.how_to_get }} | {{ v.status }} |
{% endfor %}

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

=== "Demo"
    - Mastery rank cap: **5**
    - Character level cap: **15**

=== "Full game"
    - TBD after launch.

## Awakening

Each Vision has three greyed-out stars. Awakening a Vision fills in a star
and permanently unlocks another set of skills and passives on top of the base
set. Awakening is separate from Mastery: it only happens when you spend
magicite.

| Tier | Cost | Status |
|------|------|--------|
| ★ | Magicite Shard | unverified |
| ★★ | Magicite | unverified |
| ★★★ | Magicite Cryst | unverified |

!!! quote "Magicite Shard (key item)"
    *"A shard imbued with the power of the Farplane. Has the power to awaken
    visions."*

### Where to awaken

!!! warning "Unverified"
    Guides say a **Moogle in Grandport** awakens Visions in exchange for
    magicite, and that it becomes available near the end of the demo, after
    an awakening tutorial.

### Where to get Magicite Shards in the demo

- **Siren's Tower:** one in a chest
- **Oblivion Palace (Area 2/5):** two in chests
- **Boss drops:** reportedly Siren, Marauder and Leviathan
- **Side quests:** some reward them

??? note "Tablet Shards and the princess (unverified)"
    Tablet Shards are found in treasure chests. Guides say you can hand them
    to a princess at **Oblivion Palace** in exchange for magicite. Guides
    disagree on how many Tablet Shards the demo has, so trust your in-game
    hand-in count.
