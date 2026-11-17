---
platform: SFC
spoilers: none
status: draft
tags:
  - Lufia II
fg:
  chapters: true
---

{#- Each chapter ends with its treasure and enemies, from
    data/lufia-ii/walkthrough.yaml and the Bestiary's data. -#}
{%- macro extras(title) -%}
{%- set c = lufia2_walk.chapters[title] -%}
{%- set n = namespace(count=0) -%}
{%- for g in c.treasure or [] %}{% set n.count = n.count + g["items"]|length %}{% endfor -%}
{%- if n.count or c.also -%}
<div class="fg-wt-box fg-wt-chest"><span class="fg-wt-k">Treasure{% if n.count %} ({{ n.count }}){% endif %}</span>
{%- for g in c.treasure or [] -%}
{%- if (c.treasure|length) > 1 %}<div class="fg-wt-place">{{ g.place }}</div>{% endif -%}
<ul class="fg-wt-items">{% for x in g["items"] %}<li><span class="fg-wt-i">{{ x.i }}</span>{% if x.n %}<span class="fg-wt-n">{{ x.n }}</span>{% endif %}</li>{% endfor %}</ul>
{%- endfor -%}
{%- if c.also %}<p class="fg-wt-also"><b>Also here</b>{{ c.also|join(", ") }}</p>{% endif -%}
</div>
{%- endif -%}
{%- if c.areas -%}
<div class="fg-wt-enemies"><b>Enemies</b>
{%- for name in c.areas -%}
{%- for a in lufia2_bestiary.areas if a.area == name and a.monsters -%}
{%- set href = "bestiary.md#" ~ name|lower|replace(":", "")|replace("(", "")|replace(")", "")|replace("'", "")|replace(" ", "-") -%}
<p><a href="{{ href }}">{{ name|replace("Overworld: ", "Around ") }}</a>{{ a.monsters|sort(attribute="level")|map(attribute="name")|join(", ") }}</p>
{%- endfor -%}
{%- endfor -%}
</div>
{%- endif -%}
{%- endmacro %}

# Walkthrough

The story in order, with what to buy in each town and the bosses. Each
chapter ends with its treasure and the enemies you'll meet there. **Buy in X:** lines list what's worth buying there. **Missable:**
marks anything you can lose for good. See [Equipment](equipment.md) for
stats, the [Bestiary](bestiary.md) for drops, and
[Capsule Monsters](capsule-monsters.md) for where each one is and what to
feed it.

Shops sell at the same price everywhere. The inn price is per stay.

## Elcid and the Secret Skills Cave

- The elder sends Maxim to the cave south of town. Push the pots onto the
  switches. You learn **Restart**, which resets the room you're in if a
  puzzle goes wrong.
- **Buy in Elcid:** Rapier and Small Shield for Maxim, and the Strong spell.

{{ extras("Elcid and the Secret Skills Cave") }}

## Cave to Sundletan

- A **Dragon Egg** here needs the Hook. Come back for it later.

### Boss: Lizard Man

- **HP:** 80
- **Drops:** the key to Sundletan
- Level 5 or 6 is plenty.

{{ extras("Cave to Sundletan") }}

## Sundletan and the Lake Cave

- **Buy in Sundletan:** a Cap and spells. Skip the weapons, because the Lake
  Cave has an Insect Crush. Sundletan also sells **Apple Cider** (1,000),
  the best food for class 3 capsule monsters.

### Boss: Big Catfish

- **HP:** 200
- **Strong:** water
- **Drops:** sometimes the **Catfish Jewel**. It's rare, so save before the
  fight and reset until it drops if you want it.

Head back to Sundletan, then return to the Lake Cave to save Tia from a
Skeleton and Goblin. **Tia joins.**

- **Jelze**, the first capsule monster, is in Foomy Woods. Go through the
  portal north of the Lake Cave, then left and south.

{{ extras("Sundletan and the Lake Cave") }}

## Alunze and the Castle Basement

- **Buy in Alunze:** Short Sword (ice IP), Cloth Armor and Buckler for
  Maxim. Long Knife and Mini Shield for Tia. Cheap Alunze gear is also good
  capsule food to reach class 2.
- The inn has a small casino. The **Fire Charm** prize helps against the
  Tarantula later.
- Bart and Bertie steal the crown.
- The basement has the **Bomb** skill, a **Dragon Egg** and a **Secret
  Fruit**. Its **Water Jewel** needs the Hook, so come back for it later.
- Keep the Secret Fruit. It's what Jelze needs for its last form.
- When the king offers a reward, pick **Nothing**. It pays 3,000, more than
  any of the other answers.

{{ extras("Alunze and the Castle Basement") }}

## Northwest Cave

Abel's key gets you in.

- The **Eron Hat** and **Tuff Buckler** need the Hammer. Come back for them
  after Flower Mountain.

### Boss: Regal Goblin

- **HP:** 500
- Around level 13. Drowsy works on him. Use the Short Sword's ice IP.

{{ extras("Northwest Cave") }}

## Tanbel and the East Tower

- Climb the East Tower **before** talking to Guy in Tanbel. Camu isn't there
  yet, so you can grab the **Fire Dagger**, **Camu Armor** and **Pearl
  Brace** early. They're still there later, so this isn't missable.
- Two Followers attack in town (HP 150 each, weak to water). Guy helps.
- **Buy in Tanbel:** Kukris for their thunder IP, and the new spells.
- Set the tower's clock to 9:00 to open the door, and 12:00 for the Jute
  Helm.

### Boss: Camu

- **HP:** 1,500
- **Weak:** thunder · **Strong:** fire
- **Drops:** rarely the **Camu Jewel**. Save first if you want it.
- Use Tia's Flash and the Kukri IP. **Guy joins** afterward.

{{ extras("Tanbel and the East Tower") }}

## Clamento and the Ruby Cave

- **Buy in Clamento:** Bravery and Free spells, and **Mystery Pins** for the
  Tarantula's paralysis.
- **Blaze** is here. Go right at the first fork, bomb the wall, press the
  four switches, bomb the next wall and take the teleporter.
- Big Bees drop **Bee Rocks**, good class 4 capsule food.

### Boss: Tarantula

- **HP:** 2,000
- **Weak:** fire, insect · **Strong:** thunder
- **Drops:** rarely the **Spido Jewel**
- Around level 20. Use Brave on Tia, the Fire Dagger IP and the Insect
  Crush. Carry Mystery Pins.

Jaffy is behind the boss. Jaffy gives Tia jewelry, and the shrine north of
Clamento opens the way to Parcelyte.

{{ extras("Clamento and the Ruby Cave") }}

## Parcelyte and the Treasure Sword Shrine

- **Buy in Parcelyte:** Franshiska for Guy, a Rod for Selan, and Regains.
  The Red Cores near the castle give 2,222 EXP each.
- **Selan joins.**
- The **Undead Ring** blocks instant death. Keep one on someone from here on.

### Boss: Pierre and Danielle

- **HP:** 1,200 each
- **Pierre (blue):** **Weak:** water, ice · **Strong:** thunder
- **Danielle (red):** **Weak:** fire, thunder · **Strong:** ice
- In the second round they revive each other, so they have to go down on the
  same turn. Put Maxim and Tia on Pierre (Cold Rapier IP, Droplet), and Guy
  and Selan on Danielle (Fire Dagger IP, Spark, Flash).

On the way out, the king lets you take the **Holy Wings** from the castle
basement.

{{ extras("Parcelyte and the Treasure Sword Shrine") }}

## Gordovan West Tower

- The **Hook** skill is here.
- With the Hook, you can now get the Sundletan cave Dragon Egg and the Alunze
  basement Water Jewel.
- In the zombie room, hit the switches in this order: 1, 5, 6, 2, 7, 3, 4.

### Boss: Gades

- **HP:** 7,500
- **Weak:** light · **Strong:** dark
- You're meant to lose. **Missable:** if you win, he drops the **Gades
  Blade**, the only way to get it outside the Ancient Cave. It takes a high
  level, so save before the fight if you want to try.

Guy leaves for a while at Parcelyte.

{{ extras("Gordovan West Tower") }}

## Merix and the Cave to Bound

- **Buy in Merix:** the Fireball spell and a **Gladius**. Its Holy Energy IP
  hits hard, and much harder against anything weak to light.
- In the cave, break the crystal ball to stop enemies respawning.
- Bring the carpenter back to Merix. His daughter gives you a **Dragon
  Egg**.

{{ extras("Merix and the Cave to Bound") }}

## Bound Kingdom and the Northern Labyrinth

- **Talk to the King of Bound.** If you skip him, Idura won't be in the
  labyrinth and the story can't move on.
- **Buy in Bound:** Bronze Swords. They're good weapons and good class 4
  capsule food. Fire Balls for the bosses.
- The Deadly Sword is cursed. Have it uncursed, or sell it. Deadly Swords
  here drop more.
- **Flash** is here. From the moving platform room, take the lower-right
  door into a one-way mini maze.
- Light the bombs in order 1 to 5, and wait for each to go off before the
  next. Setting them off too fast can freeze the game.

### Boss: 4 Mummies and 3 Trolls

- **HP:** Mummies 150, Trolls 200
- **Weak:** fire. Fireball and Fire Balls clear them fast.

- **Missable:** **Tia leaves for good** when you get back to Bound. Unequip
  her first. If you forget, the Forfeit shop later sells everything you've
  ever owned.

{{ extras("Bound Kingdom and the Northern Labyrinth") }}

## Ancient Tower

- **Dekar and Guy join.** Give Dekar agility gear like the Speedy Ring.
- Teleporters send you the way you face. Hit the statue on the red carpet 3
  times and the one on the blue carpet 5 times. In the monster race, bet on
  the skeleton on the right.

### Boss: Gades

- **HP:** 3,000
- **Weak:** light
- Use the Thunder Ax IP, Trick and Brave on Maxim, and Strong to heal.

The tower sinks, Maxim and Selan marry, and the story skips a year.

{{ extras("Ancient Tower") }}

## Northern Lighthouse

Maxim and Selan go alone. Re-equip Selan.

- Push the blocks into an arrow pointing right. The box puzzle gives the
  Mystery Ring, Dragon Egg and Big Shield.

### Boss: Idura

- **HP:** 1,500
- **Weak:** ice · **Strong:** thunder
- Drowsy works on him. Use the Water Jewel's IP on Selan.
- His Groupies drop **Magic Fruit**, which fills 8 blocks on any capsule
  monster. Worth farming here and in his later fights.

Use the shrine right of the Ancient Tower to reach Aleyn. **Guy and Dekar
rejoin.**

{{ extras("Northern Lighthouse") }}

## Aleyn and Phantom Tree Mountain

- **Buy in Aleyn:** every spell and the new gear.
- The **Fire Arrow** skill is here.
- For the Fire Arrow bush puzzle, start lower left and go up, up, up, right,
  down, right, up, right, down, down, left, down, left.

### Boss: 2 Lions

- **HP:** 1,000 each
- **Weak:** ice · **Strong:** water
- They aren't immune to instant death. Trick and Brave on Maxim.

Jyad starts the ship. Visit Gruberik and Narcysus once each so you can warp
there.

### Gruberik: the Ancient Cave

The Ancient Cave is a random 99-floor dungeon under Gruberik. Everything you
find inside, except blue chests, is lost when you leave. Blue chests are
yours for good. *Check in game: exact rule.* The ten **Iris treasures** are deep inside. Bring all ten to
the woman in Gruberik's pub. Go in whenever you like, and see
[Missables](missables.md) for the party members who can only go while
they're with you.

{{ extras("Aleyn and Phantom Tree Mountain") }}

## Narcysus and the Tower of Sacrifice

- Evil Fish drop **Charm Fruit**, Blaze's last-form food.
- Specters can kill instantly. Wear the Holy Wings, Jute Helm and Undead
  Ring.
- **Gusto** is here: the middle door in the bomb-and-arrows room.

### Boss: Idura

- **HP:** 2,500, with Followers
- Ice spells and IPs. Drowsy still works. Trick on Maxim.

{{ extras("Narcysus and the Tower of Sacrifice") }}

## Karlloon and the North Shrine

- **Buy in Karlloon:** spells and gear. The **Multi Sword** attacks twice.
  Skip a weapon for Dekar, because the Dekar Blade is in the shrine.

### Boss: Idura

- **HP:** 3,500
- He confuses. Bring Shriek. Trick and IPs.

- **Missable:** **Dekar leaves for good** in this shrine, before the barrier
  room. Unequip him first. The Dekar Blade sells for 7,500.

The small shrine to the east leads to Treadool.

{{ extras("Karlloon and the North Shrine") }}

## Treadool and Flower Mountain

- Meet Lexis at his lab in the northeast of Treadool. Warp to Aleyn, where
  Jyad builds the ship.
- The **Hammer** skill is on Flower Mountain.
- **Sully** is here: the door between the second and third rows of spikes.
- With the Hammer, go back to the Alunze Northwest Cave for the **Eron Hat**
  and **Tuff Buckler**.

### Boss: Rogue Flower

- **HP:** 3,000
- **Weak:** fire · **Strong:** water
- Use the Burn Sword.

Back in Treadool, **Lexis joins** and you get the ship. Dankirk, Auralio and
Forfeit Island open up.

{{ extras("Treadool and Flower Mountain") }}

## Forfeit Island

- The shop here sells **every item you've ever had**, so gear lost with Tia
  or Dekar can be bought back.
- **Casino:** the Jewel Sonar beeps once per chest still unopened in a
  dungeon. The Dragon Blade is the top prize. You need the **VIP Card**
  from the Prince of Auralio for the back room.

{{ extras("Forfeit Island") }}

## Dankirk and the North Dungeon

- **Buy in Dankirk:** gear and the Shield, Courage, Mirror and Coma spells.
- Talk to the royal family and Prince Leon. Jaffy in Clamento makes a glass
  icon. Give it to the prince, then go after the butler James in the cave
  to the north.
- A hidden group of chests holds a **Dragon Egg**: cut the lone patch of
  grass, then walk down and left.
- Assassins are fast and can kill instantly.

### Boss: 4 Soldiers

- **HP:** 400 each

- At Auralio, **talk to the prince twice**. The second time he gives you the
  **VIP Card**.
- The sea is open. Ferim, Pico, Treble, Portravia, Barnan and Durale are all
  reachable by ship.
- **Darbi** is in the small tree shrine on the crescent-moon island west of
  the Shrine of Vengeance. *Check in game: this combines two guides'
  directions.*

{{ extras("Dankirk and the North Dungeon") }}

## Ferim and the Northeast Tower

- **Buy in Ferim:** the Champion, Firebird and Ice Valk spells.
- Floor tile path: up, left, up, up, right, up, left, up, right, right,
  right, down, down, left, down, down, right, right, up, up, up, up.

{{ extras("Ferim and the Northeast Tower") }}

## Agurio and Treble

Iris tells you to seek the Dual Blade. Head to Treble, then Portravia.

{{ extras("Agurio and Treble") }}

## Portravia and the Mountain of No Return

- **Buy in Portravia:** the Thunder, Dragon and Valor spells, and Launchers.

### Boss: 4 Gargoyles

- **HP:** 1,000 each
- **Weak:** flying, hard · **Strong:** earth
- They aren't immune to instant death. Use the Mysto Jewel's IP, Darbi, the
  Flying Ax and the Eagle Rock. Trick and Courage.

- **Missable:** **Lexis leaves for good** here. Unequip him first, or buy his
  gear back at Forfeit.

{{ extras("Portravia and the Mountain of No Return") }}

## Eserikto and the Divine Shrine

- **Artea joins.** **Buy in Eserikto:** Thunder, Firebird, Dragon, Ice Valk
  and Fry, plus new weapons.
- For the **Dragon Egg**, play the notes 3, 2, 4, 1, 5.
- Karyn's sacrifice fills Artea's IP and raises everyone's stats.
- Back in Portravia, the ship becomes a submarine.
- **Zeppy** is in the underwater cave south of Parcelyte. Its two chests have
  **Secret Fruit**.

### The Egg Dragon

Once you have all eight **Dragon Eggs**, take the sub to the island left of
Pico. The dragon grants a wish: 10 of each stat potion, 20 of each capsule
fruit, and more. After each wish the eggs are hidden again in random chests.
The Jewel Sonar helps you find them. After four wishes you can fight the Egg
Dragon (65,535 HP) for the Egg Sword and Egg Ring.

{{ extras("Eserikto and the Divine Shrine") }}

## Barnan and the Shrine of Vengeance

- **Buy in Barnan:** platinum armor and shields.
- **Buy in Chaed** (any time from now): the **Rune Rapier** and other strong
  gear.
- Enter by sub, from the south side of the temple.
- The **Cursed Bow** appears after the boss. Uncursed, it becomes **Arty's
  Bow**, which hits every enemy.

### Boss: Venge Ghost

- **HP:** 7,500
- **Weak:** light · **Strong:** ice, dark
- Instant-death attacks. Wear the Holy Robe, Undead Ring or Ruse Armor. Use
  the Rune Rapier and the Light Jewel's IP. Level 40 or so.

{{ extras("Barnan and the Shrine of Vengeance") }}

## Durale and the Tower of Truth

- **Buy in Durale:** the **Zap** spell (65,000), the best light spell.
- Note puzzles: 3, 2, 1, 4, then 3, 2, 4, 1 with the fifth note across the
  Hook gap. Stun the Siren rather than killing her.

### Boss: 3 White Dragons

- **HP:** 550 each
- **Weak:** fire, dragon
- They drop **Holy Fruit**, Darbi's last-form food.

{{ extras("Durale and the Tower of Truth") }}

## Chaed and Dragon Mountain

The biggest dungeon in the game.

- **Missable inside the run:** the sliding-block room the game calls the
  hardest trick in the world holds the **Lizard Blow**, **Mega Shield**,
  **Legend Helm** and **Holy Robe**. It's optional, but those are some of the
  best items in the game. Use Restart to reset it.
- Lure the Behemoth onto the weak floor.

### Boss: Fire Dragon

- **HP:** 7,500
- **Weak:** dragon, ice, flying · **Strong:** fire, earth
- There's a Miracle behind the teleporter on the way out.

The elder gives you the Mermaid Key. Dive by Darbi's crescent island to reach
Preamarl.

{{ extras("Chaed and Dragon Mountain") }}

## Preamarl, the Ghost Ship and the Dual Blade Shrine

### Boss: Ghost Ship

- **HP:** 10,000
- **Weak:** fire, light, healing
- It never attacks directly. Kill what it summons, or it uses Doomcry.
  Firebird works well.

In the Dual Blade shrine, the US version has a graphics bug. Walk up until
the wall, three steps left or right, up, three steps the other way, up.

Daos destroys Chaed. Go see Lexis in Portravia.

{{ extras("Preamarl, the Ghost Ship and the Dual Blade Shrine") }}

## Gratze

- Take the sub to the whirlpool north of Gratze. You're captured, and Bart
  and Bertie break you out.

### Boss: Tank

- **HP:** 10,000
- **Weak:** hard
- Huge magic resistance. Use weapons and IPs.

Lexis turns the motor into an airship. Fly to Narvick.

{{ extras("Gratze") }}

## Narvick and the Sealed Towers

- **Buy in Narvick:** the Zirco gear, the best you can buy.
- **Shuman (south):** **Boss: Gades** (7,500 HP).
- **Stradha (northeast):** **Boss: Amon** (10,000 HP). His Chaos Wave
  confuses, so bring Shriek.
- **Kamirno (northwest):** the Dual Blade chooses Maxim. **This is the last
  save point before the end.**
- Repair the Dual Blade in Portravia and equip it on Maxim.

{{ extras("Narvick and the Sealed Towers") }}

## Doom Island

Bring a dozen Miracles. Your IP fills before each Sinistral.

- **Gades:** 7,500 HP
- **Amon:** 10,000 HP
- **Erim:** 15,000 HP. Devastation Wave kills instantly, and you lose all IP
  if anyone dies. Wear the Undead Ring, Ruse Armor, Ghost Ring or an
  uncursed Dark Mirror.
- **Daos:** 20,000 HP. Cast Absorb when he raises his Dark Reflector.

{{ extras("Doom Island") }}

## Sources

- Story order, chests, puzzles and boss strategy: Iron Knuckle's
  [Lufia II walkthrough](https://gamefaqs.gamespot.com/snes/588451-lufia-ii-rise-of-the-sinistrals/faqs/11045)
  (GameFAQs).
- Shops, chests and boss data:
  [RPGClassics' Lufia 2 shrine](http://www.rpgclassics.com/shrines/snes/lufia2/).

<script type="application/json" id="fg-cards-data">{{ {"bestiary": lufia2_bestiary, "equipment": lufia2_equipment, "items": lufia2_items, "magic": lufia2_magic, "ip": lufia2_ip} | tojson }}</script>
