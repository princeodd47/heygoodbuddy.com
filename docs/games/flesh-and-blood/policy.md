---
tags:
  - Flesh and Blood
---

{% macro sym(k) %}![{{ fab_icons[k] }}](../../assets/images/flesh-and-blood/icon_{{ k }}.png){ .fab-icon title="{{ fab_icons[k] }}" }{% endmacro %}

# Policy & Penalties

This page covers the Procedure and Penalty Guide (PPG), plus the parts of the
Tournament Rules and Policy (TRP) that come up at the table. The PPG is
written for **Competitive and Professional** REL. Casual events use the
separate Casual Procedure Guide.

## Quick reference

| Infraction | Penalty | Main change |
| --- | --- | --- |
| **Gameplay** | | *Upgrade on the 3rd of the same type in a day* |
| Game Rules Violation | Warning | IP2 if it can't be fixed and gave a significant advantage |
| Failure to Maintain Game State | Warning | Never upgraded for repeats |
| Missed Trigger | Caution | Warning if missing your own trigger helped you |
| Looking at Extra Cards | Warning | IP2 and a shuffle at 5+ cards from a non-random deck |
| Hidden Card Error | Warning | IP2 if the mixed cards can't all be recovered |
| Shuffling Error | IP2 | — |
| Presenting Cards Error | Warning | Caution for a flip-card face. IP2 at Pro. Game Loss if off by 2+ |
| **Tournament** | | *Upgrade on the 2nd of the same type in a day* |
| Tardiness | IP2 | Warning under 1 minute, Game Loss over 10 |
| Note Taking / Outside Assistance | Warning | Game Loss if it gave a strategic advantage |
| Slow Play | Caution | Then Warning. Game Loss after 2 Warnings |
| Decklist Error | IP2 | Warning in some cases. Game Loss for big or illegal errors |
| Card-Pool Contents Error | IP2 | Caution if cards are only missing |
| Draft Procedure Violation | Warning (minor) / Game Loss (major) | A major Game Loss is given after the draft |
| Marked Cards | Warning | Game Loss if the HJ sees a significant advantage |
| Insufficient Shuffling | Warning | — |
| Communicating Incorrect Game Information | Warning | Caution for a stale marker at Competitive |
| **Conduct** | | |
| Unsporting Conduct – Minor | Warning | Repeats: IP2, then Game Loss |
| Unsporting Conduct – Major | Disqualification | — |
| Cheating | Disqualification | — |
| Aggressive Behavior | Disqualification | — |
| Improperly Determining a Winner | Game Loss | — |
| Bribery | Disqualification | Game Loss if from ignorance |
| Betting | Disqualification | Game Loss if from ignorance |
| Theft | Disqualification | The HJ may lower it to a Warning |
| Stalling | Disqualification | — |
| Improper Concession | Game Loss | Warning if from ignorance. DQ for asking again |
| Rules Sharking | Warning | Caution if only suspected. Game Loss for a pattern |
| Fraud | Disqualification | — |

!!! warning "The PPG's own table disagrees with itself"
    The quick-reference table at the end of the PPG lists **Outside
    Assistance as a Game Loss**. The infraction's own section (PPG 3.2) says
    **Warning**, upgraded to a Game Loss if the player gained a strategic
    advantage. Go with the section. A spectator who gives assistance always
    gets a Game Loss for their next game.

## How penalties work

### The ladder (PPG 1.4)

| Severity | Penalty | What it does |
| --- | --- | --- |
| 0 | **Caution** | A spoken warning. Not recorded |
| 1 | **Warning** | Recorded. Repeats can upgrade |
| 2 | **Intellect Penalty (IP2)** | -1 intellect {{ sym("i") }} for the next 2 end-of-turn draws |
| 3 | **Game Loss** | The game ends as a loss |
| 4 | **Disqualification** | Removed from the tournament |

- **IP details:** the player draws 1 fewer card at the end of the next two
  turns (including the first-turn draw). An IP given before a game starts
  lowers the opening hand too. A second IP adds turns to the one already
  running. Any upgrade or downgrade that lands on an IP is an IP2.
- **Game Loss between games, or after time is up:** it applies to the
  player's **next** game. Game Losses for both players at once are recorded
  as a double match loss.
- **DQ:** the player loses the current match and is dropped. They keep
  prizes already received and get no more. Players below them move up one
  place, unless it happens after the cut. Both the player and the HJ fill
  out DQ forms.

### Rules for every ruling (PPG 1.2)

- Don't step into a game unless there's an infraction or you're
  investigating. **Don't step in** for a Missed Trigger that would only be a
  Caution, or for a Caution or Warning the players fix quickly between
  themselves.
- Explain the infraction, the fix and the penalty to **everyone involved**.
- **Check with the Head Judge before giving an IP2 or higher.** The
  exceptions are **Tardiness** and **Decklist Error**.
- **Several related infractions:** apply each fix, but give only the
  **single highest** penalty.
- **Time extension:** if a ruling takes more than 1 minute, add that much
  time to the match, rounded **up** to the minute.
- **Repeat upgrades:**
    - Gameplay: the 3rd infraction of the same type in a day goes up one
      level. Failure to Maintain Game State never upgrades this way.
    - Tournament: the 2nd of the same type in a day goes up one level.
      Tardiness and Slow Play are excluded.
    - Repeat upgrades never go past a Game Loss, and the count resets each
      day.
- **Deviations:** only the **Head Judge** can depart from the PPG. They have
  to explain the normal ruling and why they're deviating. Floor judges can
  suggest a deviation.
- **Judge mistakes:** admit it, apologize, and fix it if you can. A judge's
  mistake can be a reason for the HJ to deviate.
- **The three principles:** *education* (the player understands what went
  wrong), *equity* (any advantage is removed), and *mission* ("playing
  great games").
- **The four kinds of advantage:** information, state, strategic and
  tournament.

### Fixes (PPG 1.3)

| Fix | When to use it |
| --- | --- |
| **Simple rewind** | Caught right away. Undo the last action(s). Never undo randomness, such as putting a drawn card back |
| **Full rewind** | Actions have been taken since. Only when every step can be accounted for. Any unknown card that goes back is chosen at random |
| **Partial fix** | Correct the current state: life totals, zones, counters, a missed choice, a loss that should have happened. Not if a strategic decision was made off the error |
| **Top/bottom of deck** | The **opponent** picks the order and top or bottom for each card |
| **Shuffle into the random part** | Only as part of a deviation, because FaB decks are rarely random during a game |

## Gameplay infractions

Assumed to be **accidental**. If it was deliberate, it's Cheating.

### Game Rules Violation — Warning (PPG 2.1)

A player gets the rules wrong in a way no other infraction covers: not
paying a full cost, defending from arsenal, playing an action on the
opponent's turn without instant speed, or forgetting to draw.

- **Fix:** caught right away, do a simple rewind. Otherwise do a partial fix,
  then a full rewind. If neither works, leave it.
- **Upgrade to IP2:** if it can't be fixed *and* the player gained a
  significant advantage.
- **The opponent:** if they had a fair chance to notice and didn't, they get
  a Warning for Failure to Maintain Game State. If they share
  responsibility (it was their card that made the play illegal), they get a
  GRV Warning instead.

### Failure to Maintain Game State — Warning (PPG 2.2)

The opponent's side of someone else's gameplay infraction. It can't happen
on its own, it doesn't apply to Missed Triggers, and it's **never**
upgraded for repeats.

### Missed Trigger — Caution (PPG 2.3)

The controller doesn't acknowledge their own trigger by the time it matters.
Acknowledging means a visible change or confirming it out loud, and **any**
player can do it.

**When a trigger is missed:**

- Triggers with choices (targets, modes): before the controller next passes
  priority.
- Triggers that change the rules: before the action they'd make illegal.
- Triggers with visible results: before anyone does something that could
  only happen after the trigger resolved.
- Triggers with hidden results: before they first show up visibly.

**Not a missed trigger:**

- A trigger that wouldn't have done anything.
- One whose only effect is optional. The player is assumed to have said no.
- One that partly resolved. The missing part is a GRV instead.

Other points:

- A missed trigger still counts toward its "once per turn" type limits.
- Triggers that depended on the missed one are missed too.
- Nobody has to point out an opponent's trigger. Deliberately rushing the
  game so an opponent misses theirs is Rules Sharking.
- **Fix:** caught right away, simple rewind. Otherwise a partial fix that
  resolves it now, then a full rewind. If neither works, the trigger fails.
- **Upgrade to Warning:** if missing it helped the player and it was the
  player's own trigger, not one the opponent created.

### Looking at Extra Cards — Warning (PPG 2.4)

The player sees cards they shouldn't have, but the cards haven't moved
zones.

- Seen while drawing for the end of turn, before the opponent has accepted
  the phase change: leave them on top.
- From a fully randomized deck: shuffle them back in.
- From a non-random deck, and the player already knew them (through opt and
  the like): leave them. If they didn't, the opponent sees them and picks
  top or bottom.
- From other zones, or the opponent's cards: show them to the opponent and
  leave them.
- **Upgrade:** 5 or more cards from a non-random deck is an IP2, and the deck
  is shuffled.

### Hidden Card Error — Warning (PPG 2.5)

Private cards get mixed in a way public information can't untangle. Drawing
5 when intellect is 4, opt cards mixed into the hand, an arsenal card picked
up into the hand, or equipment put face down without an effect allowing it.

- **Fix:** show the whole mixed group to the opponent. The opponent decides
  which cards go back where, keeping each zone's count right. Cards going to
  the deck go top or bottom, as the opponent chooses. Face-down equipment
  that wasn't allowed is removed from the game.
- **Upgrade to IP2:** if cards are already gone from the mixed group and it
  can't be fully fixed.
- If the cards can be separated cleanly, it's Looking at Extra Cards
  instead.

### Shuffling Error — IP2 (PPG 2.6)

Randomizing an ordered set by mistake, like shuffling pitched cards into the
deck. Make sure the deck ends up properly randomized.

### Presenting Cards Error — Warning (PPG 2.7)

The decklist and card-pool are legal, but the player starts the game with
an illegal set of cards: the wrong deck size, equipment in the deck, two
weapons that can't go together, or a double-faced card showing its back.

- Take out cards that can't be in the deck. Cards that can't start outside
  the deck go back in the deck, or into inventory.
- Before the game starts: add cards (Cracked Baubles if needed) or remove
  cards to fix the size. Once the game has started, the size stays as is.
- An unclear set of starting arena-cards: lay out the legal options, and
  the **opponent** picks.
- **Downgrade:** a flip-card on the wrong face is a Caution at every REL.
- **Upgrade:**
    - At Pro REL, an IP2 for everything except double-sided cards on the
      wrong face.
    - An IP2 for transcend cards that can't be corrected.
    - A **Game Loss** if the deck is still 2+ cards off after the fix.

## Tournament infractions

### Tardiness — IP2 (PPG 3.1)

Not seated when the round starts, or late with a required procedure such as
the decklist.

- Extend the match by the time lost.
- Under 1 minute is a **Warning**. Over 10 minutes is a **Game Loss**, and
  the player is dropped unless they check in before the next pairings.
- If the round started early, lateness counts from the scheduled start.

### Note Taking and Outside Assistance — Warning (PPG 3.2)

- Illegal notes get destroyed.
- A spectator who helps gets a **Game Loss in their next game** and is sent
  away.
- **Upgrade to Game Loss** if the player gained a strategic advantage.
- Getting advice you didn't ask for isn't the player's fault.

### Slow Play — Caution (PPG 3.3)

Taking too long without meaning to gain from it.

- Caution and educate the player.
- If they stay slow, a Warning.
- After **two Warnings** in the tournament, a Game Loss.
- Only penalize what a **judge sees**, not what players or spectators
  report.
- No extra time is given for accusations alone.
- Slow play done on purpose is **Stalling**.

### Decklist Error — IP2 (PPG 3.4)

The list doesn't match what the player meant to play, or it's illegal. That
covers missing equipment, a missing pitch, an ambiguous hero name, or a
banned hero. Fix the list to match what they meant. The player can finish
the current game, but can't start a new one until it's fixed.

- **Warning** if it's minor and caught before round 1, or the player
  reports it. Also a Warning if the hero is missing but only one hero
  makes sense.
- **Game Loss** if it's a big difference or gave a strategic advantage.
  Also a Game Loss if the list has illegal cards the player meant to play.
  Those get swapped for Cracked Baubles.

### Card-Pool Contents Error — IP2 (PPG 3.5)

The cards don't match a correct decklist. The card-pool includes anything
stored nearby, like the same deck box compartment. Remove the extras, note
any missing cards, and let the player find replacements.

- **Caution** if cards are only missing.
- **Warning** if the extras couldn't have helped.
- **Warning** for extra copies the player reports right away that didn't
  affect the game. If one was drawn or revealed, use the next card instead.
- **Game Loss** for a big difference or a strategic advantage.

### Draft Procedure Violation (PPG 3.6)

- **Minor — Warning:** a pack passed the wrong way and caught before the next
  pick, a late pick, looking around, or reviewing picks outside the review
  time. Pause the draft only when it won't disrupt anyone.
- **Major — Game Loss:** two cards taken from a pack, a pack mixed with your
  picks, announcing what you're drafting, or showing your picks. The Game
  Loss is given **after the draft ends**, so it doesn't affect the rest of
  the draft.

### Marked Cards — Warning (PPG 3.7)

The player re-sleeves or replaces the cards before their next match. A proxy
is possible in rare cases, and Cracked Baubles if no replacement can be
found. Fix it mid-game only if that's quick. Otherwise wait for the match
to end. **Game Loss** if the HJ thinks the marking gave a significant
advantage.

### Insufficient Shuffling — Warning (PPG 3.8)

Watch the player shuffle and teach them. Pile counting alone isn't
shuffling.

### Communicating Incorrect Game Information — Warning (PPG 3.9)

Wrong or incomplete information about non-private facts that the opponent
**acted on**. "Attack for four" when it's three is an example. Rewind to
before the opponent's affected action, if it's not too late. If the
opponent assumed something without asking, it's not this infraction. At
Competitive REL, a stale marker can be lowered to a Caution.

## Conduct infractions

| Infraction | Key test |
| --- | --- |
| Unsporting Conduct – Minor (Warning) | Rude, messy or disruptive, but it ends when you tell them to stop. Demanding the HJ before the first judge rules, or demanding a penalty for the opponent, counts |
| Unsporting Conduct – Major (DQ) | Harassment, slurs, making someone feel unsafe, or refusing a tournament official over and over |
| Cheating (DQ) | **Both** an intent to gain an advantage **and** knowing it's against the rules. Lying to a judge is cheating. So is staying quiet about an opponent's error for your own gain |
| Aggressive Behavior (DQ) | Threats or physical intimidation. Safety comes first |
| Improperly Determining a Winner (Game Loss) | A coin flip, highest life, or anything other than playing it out. Both players can get one. With an incentive, it's Bribery. If they knew it was illegal, it's Cheating |
| Bribery (DQ) | An incentive to concede or change a result. Prize splits are fine if they don't affect the result |
| Betting (DQ) | Any bet on any part of the event, even with no money |
| Theft (DQ) | The HJ may lower it to a Warning for a misunderstanding when the item is returned |
| Stalling (DQ) | Slow play **on purpose** to run out the clock |
| Improper Concession (Game Loss) | Asking for a concession (pressure counts) or conceding after taking an action once time is called |
| Rules Sharking (Warning) | Rushing or tricking the opponent into an infraction or a missed window |
| Fraud (DQ) | Lying about identity or results, or letting someone else play as you |

## Tournament rules that come up

### Event tiers and REL (TRP A.1)

| Tier | Events | REL |
| --- | --- | --- |
| 1 | Armory, Skirmish, Pre-Release, World Premiere, On-demand | Casual |
| 2 | Road to Nationals, ProQuest, Battlegrounds, Sunday Showdown | Competitive |
| 3 | Calling | Day 1 Competitive, day 2+ Professional |
| 3 | National Championship | Competitive (Professional in the USA) |
| 4 | Pro Tour, World Championship | Professional |

- The TO may also **judge** only at Tier 1.
- Officials may also **play** at Tier 1, except Skirmish.

### Formats (TRP 7–9)

| Format | Deck | Card-pool | Copies |
| --- | --- | --- | --- |
| Classic Constructed | 60+ | 80 + hero | 3 |
| Living Legend | Like CC, with its own banned list. Living legend heroes are allowed | | |
| Blitz | Exactly 40 | 52 + young hero | 1 |
| Silver Age | Exactly 40 | 55 + young hero. Common and rare only | 2 |
| Sealed / Booster Draft | Exactly 30 | Opened cards plus any basics | Any |
| Ultimate Pit Fight | Exactly 40 | 52 + young hero | 2 |

### Match logistics (TRP 3)

- **Start-of-game time:** 5 minutes for game 1 and 3 minutes for later
  games. Going over is slow play.
- **Who goes first:**
    - Random for game 1.
    - In a play-off, the higher seed chooses.
    - After that, the loser of the last game chooses. After a draw, the same
      player chooses again.
    - A player who looks at their hand without choosing goes first.
- **Time called in Swiss:** the turn-player finishes their turn, then **one
  more turn** is played. If there's still no winner, it's a draw.
- **Play-offs have no draws:**
    1. Warn the players.
    2. Highest life total wins.
    3. Otherwise, more game wins takes it. If tied, play a 4-turn tiebreaker
       game.
    4. Keep going until one life total is higher.
    5. If still tied, the higher seed wins.
- **Concessions** are allowed until time is called, and only before an
  action is taken after that. **Intentional draws** are allowed, except in
  elimination rounds. **Never ask** for a concession.
- **Deck checks:**
    - Decklists are required at Competitive and Professional.
    - Regular deck checks are required at Pro and recommended at
      Competitive, on at least 10% of players.
    - The match gets the time the check took **plus 3 minutes**.
- **Judge calls:**
    - At Competitive and Pro, spectators can't call a judge, but may quietly
      tell one.
    - Players can't ask for a particular judge.
    - Appeals go to the Head Judge and must come **before** the fix is
      applied.
- **Feature matches:** players can turn them down in Swiss at Casual and
  Competitive. At Pro, or in any play-off, saying no is a match loss.

### Information (TRP 5.1)

| Type | Examples | Must a player tell the truth? |
| --- | --- | --- |
| Visible | Cards in play, zones, counters, life totals | Yes, completely |
| Public | Choices made, effects in play, floating resources, phase/step, match score | Yes, completely |
| Unverified | Face-down cloaked equipment allowed by an ability | Yes. It's revealed at the end of the game on request |
| Assisted | Card text, rules, policy | A judge provides it |
| Historical | A card revealed earlier that's private again | No one is responsible for it, but no lying |
| Private | Your hand and deck | No |

### Note-taking, shortcuts and play (TRP 5)

- **Allowed notes:**
    - Life totals and their sources, and the game result.
    - Dice for floating resources and action points, power, or X.
    - Counting cards in a *public* zone.
    - A card named by an effect.
- **Not allowed:**
    - A turn counter.
    - Tracking pitch order or cards played or revealed.
    - Counting cards in a deck.
    - Doing math on paper.
    - Sorting your graveyard to work out what's left in your deck.
    - A marker that's out of date.
- Players may use notes and devices **during the start-of-game procedure**,
  for things like sideboard guides.
- **Shortcuts** need everyone to understand them. Anyone can interrupt one
  before its result is accepted.
- **Out-of-order play** is fine if every action is legal and the end result
  is the same. It can't be used to go back and do something that was
  missed.
- **Reversing an action:** generally not allowed. A judge may allow it only
  if no information was gained, like "No blocks — wait, I'll block with
  these."
- **Default decisions:** no target declared means the opposing hero. An
  optional trigger that isn't acknowledged means "no".
- **Random cards:** say which die numbers match which cards *before*
  rolling. If the cards aren't marked face down, you can shuffle them face
  down and have the opponent pick.
- **Card text:** the official text is on cardvault.fabtcg.com. The Head
  Judge is the final authority.

---

<small>heygoodbuddy.com is in no way affiliated with Legend Story Studios.
Flesh and Blood™ and set names are trademarks of Legend Story Studios®.
© Legend Story Studios.</small>
