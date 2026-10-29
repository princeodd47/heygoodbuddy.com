---
platform: Switch
spoilers: none
status: draft
tags:
  - Final Fantasy X-2
---

# Fiend Arena

The Fiend Arena is the tournament half of Shinra's Creature Creator. Open
it from the Creature Creator menu on the Celsius. It has two parts:
**Enter Tournament**, where you fight through a cup for prizes, and the
**Battle Simulator**, where you replay any team you've already met.

See [Building the Team](creature-team.md) for the order to take the cups
in, and [Creatures](creatures.md) for catching what you'll need.

## How tournaments work

- Your party is whatever is in **Party Members**: any mix of Yuna, Rikku,
  Paine and creatures. Small creatures take one slot, Medium two and Large
  all three.
- HP and MP refill and ailments clear after every round. The exceptions
  are the Fiend Portal, the Fiend World Cup and the Almighty Shinra Cup.
- Losing a round just ends the tournament. The exception is the Fiend
  Portal, where a loss is a Game Over.
- Every tournament gives you a Trap Pod, even one you lose.
- Each cup's prizes come in a fixed order. Once you've had them all, each
  win gives one of the earlier prizes at random.
- Winning a cup also gives every creature you hold a Fiend Tale level.
- Unlocked cups and win counts carry over to New Game Plus.

## Battle Simulator

- Fight any team you've already met in a tournament, as often as you like.
  You only have to have met the team, not beaten it.
- You keep the EXP, AP and items from every win, and losing costs nothing.
  Trap Pods only come from tournaments, though.
- Releasing a creature with a Fayth fragment adds its Aeon to the list.
- This is where you grind levels and farm drops. Simulator teams don't
  carry over to New Game Plus.

## Recruiting from the arena

Some fighters only join through the arena. After you beat them in a won
cup, the game asks "Allow into Gullwings?"; say yes and they join.

- **Seymour, Auron and Tidus (????):** Farplane Cup opponents after 1, 2
  and 3 wins. Think twice before releasing one: you have to win the cup
  again to get them back, and there's a known bug where a released one
  won't rejoin.
- **Omega Weapon:** win the Fiend Portal.
- **Almighty Shinra:** win the Almighty Shinra Cup.

## Cups

{% for cup in ffx2_arena.cups %}
### {{ cup.name }}

**Unlock:** {{ cup.unlock }}

**Prizes:** {{ cup.prizes | join(", ") }}
{% if cup.name == "Grand Cup" %}
Jegged lists nothing new for the first win. Gamer Guides lists the
Festivalist Dressphere, but in the HD Remaster Brother gives you that on
the Celsius at the start of Chapter 1.
{% endif %}
{% if cup.name == "Fiend World Cup" %}
This cup starts life as the **Fiend Portal**. Win the Fiend Portal and
recruit Omega Weapon to turn it into the Fiend World Cup. Finish Omega
Weapon's Fiend Tale and Shinra becomes **Almighty Shinra**: the cup turns
into the **Almighty Shinra Cup** until you beat and recruit him. Releasing
Almighty Shinra gives the **Last Resort Garment Grid**.
{% endif %}

| Team | Creatures | Appears after |
|------|-----------|---------------|
{% for t in cup.teams -%}
| **{{ t.team }}** | {{ t.members }} | {{ t.unlock or "—" }} |
{% endfor %}
{% endfor %}

## Sources

- Cup unlocks, prizes, opponent teams and the Battle Simulator:
  [Jegged's Fiend Arena page](https://jegged.com/Games/Final-Fantasy-X-2/Creature-Creator/Fiend-Arena.html),
  checked against the
  [Gamer Guides Colosseum section](https://www.gamerguides.com/final-fantasy-x-2/guide/creature-create/the-colosseum/what-is-the-colosseum).
