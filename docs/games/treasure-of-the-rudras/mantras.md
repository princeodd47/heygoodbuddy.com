---
platform: SFC
spoilers: none
status: draft
tags:
  - Treasure of the Rudras
---

# Mantras

A mantra is a word you type in, made of smaller words strung together. The
game reads it from the end:

1. The **last word** sets the mantra's effect, targets, MP cost and power.
2. **Every word before it** changes the MP cost and power, and some change
   the element or effect.

Each word works differently depending on where it is, so the tables below
show both.

For example, PECOABITNA is **PE** + **COA** + **BIT** + **NA**. NA at the end:
2 MP, hits all enemies. BIT makes it fire damage and adds 1 MP. COA and PE
each take off 1 MP, so it ends up costing 1 MP.

Power is hidden in-game. It runs from 0 to 255, and higher power means more
damage, healing or a bigger stat change. The MP cost never goes below 1.

- **Elements fight each other.** Fire and water are opposites, and so are
  wind and lightning, and holy and dark. An earlier word of the opposite
  element halves an elemental mantra's power. One of any other element only
  adds half its power.
- **Don't repeat a word.** Using the same word twice halves the power.

## Words

### Cost and Power

These mostly go at the front, to make a mantra cheaper or stronger.

| Word | At the end | MP | Power | Earlier on | MP | Power |
|------|------------|---:|------:|------------|---:|------:|
| PE | Weak damage, all | 7 | 40 | | -1 | +10 |
| COA | Defense up | 8 | 16 | | -1 | +10 |
| BE | Weak damage | 1 | 5 | | -1 | +10 |
| KI | Instant death | 8 | 10 | | +5 | +38 |
| KUE | Damage | 8 | 80 | | +6 | +48 |
| NANI | Weak damage | 1 | 10 | | +8 | +56 |
| NA | Weak damage, all | 2 | 9 | Hits all | +3 | +8 |
| T | Lightning damage | 1 | 10 | Lightning damage | +1 | 0 |

NA is the word to end on when you want something to hit everyone. Put an
element or effect word in front of it, like BIT in PECOABITNA or FAST in
PECOAFASTNA.

### Attack

| Word | At the end | MP | Power | Earlier on | MP | Power |
|------|------------|---:|------:|------------|---:|------:|
| BIT | Fire damage | 11 | 110 | Fire damage | +1 | +13 |
| MINU | Water damage | 11 | 110 | Water damage | +1 | +8 |
| US | Lightning damage | 11 | 110 | Lightning damage | +1 | +13 |
| JIN | Wind damage | 11 | 110 | Wind damage | +1 | +8 |
| SUN | Holy damage | 8 | 80 | | +1 | +8 |
| HILI | Holy damage | 8 | 80 | Holy damage | +3 | +26 |
| MUNY | Dark damage | 11 | 110 | Dark damage | +1 | +13 |
| GOD | Dark damage | 11 | 110 | | +1 | +6 |
| RAT | Earth damage | 3 | 30 | Earth damage | +1 | +10 |

### Healing

| Word | At the end | MP | Power | Earlier on | MP | Power |
|------|------------|---:|------:|------------|---:|------:|
| LEF | Restores HP | 2 | 20 | Restores HP | +2 | +8 |
| LEFNA | Restores HP, all | 4 | 40 | Restores HP, all | +2 | +8 |
| MEGAMI | Restores HP, all | 8 | 100 | | +1 | +8 |
| SOUL | Revives | 8 | 40 | | +20 | +8 |
| CLEAN | Blocks abnormal status | 6 | 30 | Blocks abnormal status | +2 | +19 |

LEFNA is one word, not LEF + NA.

### Status Up

| Word | At the end | MP | Power | Earlier on | MP | Power |
|------|------------|---:|------:|------------|---:|------:|
| SU | Spirit up | 8 | 16 | Spirit up | +8 | +19 |
| POWERUP | Strength up, all | 13 | 32 | | 0 | 0 |
| FAST | Speed up | 8 | 16 | Speed up | +8 | +19 |
| GAIA | Defense up, all | 9 | 16 | Defense up, all | +9 | +19 |
| BARRIER | Magic defense up | 8 | 16 | Magic defense up | +8 | +19 |
| REFLEC | Magic evasion | 24 | 0 | Magic evasion | +36 | +38 |

COAREFLECTNA reads as COA + REFLEC + T + NA, not REFLECT.

### Status Down

| Word | At the end | MP | Power | Earlier on | MP | Power |
|------|------------|---:|------:|------------|---:|------:|
| VIRUS | Spirit down | 7 | 16 | Spirit down | +9 | +19 |
| WEAK | Strength down | 7 | 16 | | +1 | +6 |
| ZERO | Magic defense down | 7 | 16 | Magic defense down | +9 | +19 |
| SOFT | Defense down | 7 | 16 | | -2 | -8 |
| SLOW | Speed down | 7 | 16 | Speed down | +8 | +19 |
| STEAL | Absorbs MP | 1 | 16 | | +1 | +4 |

## Common Combinations

These groups show up at the front of a lot of mantras.

| Combination | Made of | MP | Power | Used in |
|-------------|---------|---:|------:|---------|
| PECOA | PE + COA | -2 | +20 | PECOABITNA, PECOAMINUNA, PECOAUSNA, PECOAJINNA, PECOAHILINA, PECOAMUNYNA, PECOARATNA, PECOASUNA, PECOAPOWERUP, PECOAFASTNA, PECOAGAIA, PECOAGODWEAK, PECOAGODZERO, PECOAGODSOFT, PECOAGODSLOW, PECOAGODSOUL, PECOACLEANNA |
| BEPE | BE + PE | -2 | +20 | BEPEGODSTEAL, BEPEGODLEFNA |
| KIPECOA | KI + PE + COA | +3 | +58 | KIPECOAVIRUS |
| KIBEPE | KI + BE + PE | +3 | +58 | KIBEPELEFNA |
| BEKUE | BE + KUE | +5 | +58 | BEKUEGODSOUL |
| KIKUE | KI + KUE | +11 | +86 | KIKUEGODMINU |
| NANIKUE | NANI + KUE | +14 | +104 | NANIKUEGODUS |
| NANIKIKUE | NANI + KI + KUE | +19 | +142 | NANIKIKUEBIT, NANIKIKUEJIN, NANIKIKUESUN, NANIKIKUEGOD |

## Standalone Mantras

These work on their own, as a single word.

| Mantra | MP | Target | Effect |
|--------|---:|--------|--------|
| CRITICAL | 12 | One | Attacks can't miss |
| INFINITY | 24 | One | Attacks can't miss |
| PHOENIX | 16 | One | Auto-revive |
| MIRACLE | 20 | All | Restores the party; the caster dies |
| FLOAT | 3 | One | Wind; adds Float |
| PEACE | 3 | All | Escape from battle |

## Sources

- How mantras are built, and each word's MP and power: Rushlight's
  [Mantra Mechanics Guide](https://gamefaqs.gamespot.com/snes/564407-rudra-no-hihou/faqs/81319).
