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

- **Town of Felicitas:** Sub Quest *Secrets Unearthed*
- **Oblivion Palace:** 1-Star Chamber box at 9 Tablet Shards
- **Siren's Tower:** chest, down the hidden path to the northwest
- **Siren's Tower:** Boss Siren drops
- **Grandport:** the Moogle of Light's awakening tutorial
- **Grandport Harbor:** Sub Quest *Rear Support, Ahoy!*
- **Marauder's Cave:** Boss Marauder drops
- **Mt. Thunderclap:** Boss Ramuh drops
- **Dwarven Forge:** Sub Quest *Elven Maven*. Start it with the blue-haired
  woman on the east side of Dilmagia, then finish it by talking to Silvia on
  the bridge at the Dwarven Forge.
- **Shoggoth Cave** (Dirnado world map, near Mt. Thunderclap): Boss Shoggoth drops
- **Oblivion Palace:** 1-Star Chamber box at 24 Tablet Shards
- **Dwarven Forge:** Sub Quest *Arise, Mechabo!*. Win two random battles
  against Ipoohs outside the Dwarven Forge, then return to Verun.
- **Dwarven Forge:** Sub Quest *Lyrical Riddles*. Look at the large Cid
  portrait in Mobliz Shipyard, talk to the marked person at the Dilmagia
  shipyard, then return to Roy at the Dwarven Forge.
- **Wind Shrine:** chest on the lower level, down a ladder
- **Rukh Cave** (southern Olderion Federation world map): Boss Rukh drops
- **Olderion:** jump rope with the Spirited Girl on the west side. Reach 10 jumps.
- **Cave of Waters:** chest on the west side of the first area

Tablet Shards are a separate item. See [Tablet Shards](tablet-shards.md)
for where to find them and what they're traded for.
