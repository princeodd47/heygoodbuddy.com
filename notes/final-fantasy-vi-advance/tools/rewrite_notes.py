"""Replace the source sites' explanatory notes in data.json with our own wording.

Equipment keeps its first note (the in-game description, shown as a quote).
Everything after it is replaced by the lines below. Esper spell descriptions
are replaced too, and the Esper name origins are dropped.

    python3 notes/final-fantasy-vi-advance/tools/rewrite_notes.py
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data.json"

BACK = "Full damage from the back row."
JUMP = "Jump does double damage with it, instead of the usual 1.5×."
MPCRIT = "Spends 12–19 MP per hit to land a critical hit; no critical once MP runs out."
KILL = "25% chance to kill the target outright. It never tries on enemies immune to instant death, and it fully heals Undead targets."
EVA = "+10% Evade."
TOOLS = "Used with Edgar's Tools."


def cast(spell):
    return f"25% chance to cast {spell} when it hits."


def rod(spell):
    return [cast(spell), f"Use it as an item to cast {spell} that ignores defense and can't be blocked; the rod breaks."]


def shield(spell, teaches):
    return [f"Use it as an item to cast {spell} that ignores defense and can't be blocked; the shield breaks.", f"Teaches {teaches} (×5)."]


ITEMS = {
    # weapons
    "Angel Brush": [cast("Confuse")],
    "Burning Fist": [cast("Fire")],
    "Kaiser Knuckles": ["Holy-elemental attacks."],
    "Venom Claws": [cast("Poison")],
    "Assassin's Dagger": [KILL],
    "Ichigeki": [KILL],
    "Viper Darts": [KILL, BACK],
    "Wing Edge": [KILL, BACK],
    "Gladius": [],  # sources disagree on its element (Holy vs Lightning); see README
    "Kagenui": [cast("Stop")],
    "Main Gauche": [EVA],
    "Swordbreaker": [EVA],
    "Mutsunokami": [EVA],
    "Man-Eater": ["Double damage against human enemies."],
    "Sakura": ["Wind-elemental attacks."],
    "Thief's Knife": ["Each hit has a 50% chance to steal from the target too."],
    "Valiant Knife": ["Ignores defense, and adds the wielder's missing HP (max HP minus current HP) to each hit's damage."],
    "Zwill Crossblade": [cast("Sleep")],
    "Cards": [BACK], "Darts": [BACK], "Boomerang": [BACK], "Chain Flail": [BACK],
    "Moonring Blade": [BACK], "Morning Star": [BACK], "Rising Sun": [BACK],
    "Death Tarot": [cast("Doom"), BACK],
    "Dice": ["Damage is the two dice multiplied together, times 2, times the user's level."],
    "Fixed Dice": ["Damage is the three dice multiplied together, times 2, times the user's level. If all three match, it's multiplied by that number again."],
    "Final Trump": [MPCRIT, BACK],
    "Kazekiri": ["Half the time, the hit is replaced by a Wind Slash on every enemy (Wind element). Works with the Master's Scroll."],
    "Golden Spear": [JUMP], "Heavy Lance": [JUMP], "Mythril Spear": [JUMP],
    "Partisan": [JUMP], "Radiant Lance": [JUMP],
    "Gungnir": ["Doesn't get the usual lance bonus when Jumping."],
    "Holy Lance": [JUMP, cast("Holy"), "Holy-elemental attacks."],
    "Impartisan": ["Adds only 1 attack unless the wielder is an Imp.", JUMP],
    "Trident": [JUMP, "Water-elemental attacks."],
    "Flame Rod": rod("Fira"), "Ice Rod": rod("Blizzara"), "Thunder Rod": rod("Thundara"),
    "Poison Rod": rod("Poison"), "Holy Rod": rod("Holy"),
    "Gravity Rod": rod("Graviga") + ["Graviga has no effect on enemies immune to instant death."],
    "Healing Rod": ["Heals the target instead of hurting it. When thrown, it targets your own party."],
    "Punisher": [MPCRIT], "Rune Blade": [MPCRIT],
    "Apocalypse": ["Spends 12–19 MP per hit to land a critical hit."],
    "Stardust Rod": [cast("Meteor")],
    "Shuriken": [BACK, "Used with Shadow's Throw."],
    "Fuma Shuriken": [BACK, "Used with Shadow's Throw."],
    "Pinwheel": [BACK, "Used with Shadow's Throw."],
    "Hawkeye": ["Half the time it deals 3× damage to floating enemies and 1.5× to others.", BACK],
    "Sniper": ["Half the time it deals 3× damage to floating enemies and 1.5× to others.", BACK],
    "Scorpion Tail": [cast("Bio"), BACK],
    "Blood Sword": ["Heals the wielder by the damage dealt, but a hit can't do more damage than the HP it can restore."],
    "Soul Sabre": ["Restores the wielder's MP by the damage dealt, but a hit can't do more damage than the MP it can restore.",
                   "25% chance to cast Doom, except on enemies immune to instant death."],
    "Excalibur": ["Holy-elemental attacks."],
    "Flametongue": [cast("Fire")], "Icebrand": [cast("Blizzard")], "Thunder Blade": [cast("Thunder")],
    "Lightbringer": [MPCRIT, BACK, cast("Holy")],
    "Organyx": [MPCRIT, "Breaks on roughly 28% of hits, depending on the last digit of the wielder's current HP."],
    "Ragnarok": [MPCRIT, cast("Flare")],
    "Save the Queen": [],
    "Stoneblade": ["25% chance to cast Break, except on enemies immune to instant death."],
    "Ultima Weapon": ["Ignores defense. Damage depends on current HP compared with max HP, so it's strongest at full HP, and it's weaker below level 64. The blade looks longer on hits over 500 and over 1,000 damage."],
    "Zantetsuken": ["25% chance to cut the target down in one stroke. It never tries on enemies immune to instant death."],
    # tools
    "Air Anchor": ["The target dies the next time it acts.", TOOLS],
    "Auto Crossbow": ["Physical damage to every enemy.", TOOLS],
    "Bioblaster": ["Poison-elemental damage to every enemy, and may poison them.", TOOLS],
    "Chainsaw": ["Either a heavy hit that ignores defense, or an attempt to kill one enemy outright.", TOOLS],
    "Debilitator": ["Makes one enemy weak to a random element it isn't already weak to.", TOOLS],
    "Drill": ["Heavy damage to one enemy, ignoring defense.", TOOLS],
    "Flash": ["Damages every enemy and may Blind them.", TOOLS],
    "Noiseblaster": ["May Confuse every enemy.", TOOLS],
    # armor, helmets, shields
    "Minerva Bustier": ["+25% max MP. Doesn't stack with other MP bonuses."],
    "Mirage Vest": ["Starts each battle with Image, which wears off as usual."],
    "Moogle Suit": ["The wearer looks like a moogle in battle."],
    "Reed Cloak": ["Adds only 1 Defense unless the wearer is an Imp.", "Teaches Imp (×1)."],
    "Saucer": ["Adds only 1 Defense unless the wearer is an Imp."],
    "Beret": ["Makes Sketch more likely to work, by about 33–50% depending on levels."],
    "Hypno Crown": ["Makes Control more likely to work, by about 33–50% depending on levels."],
    "Cat-Ear Hood": ["Doubles the gil from battles."],
    "Dueling Mask": ["+25% max HP."],
    "Green Beret": ["+12.5% max HP. Doesn't stack with other HP bonuses."],
    "Priest's Miter": ["+12.5% max MP. Doesn't stack with other MP bonuses."],
    "Red Cap": ["+25% max HP. Doesn't stack with other HP bonuses."],
    "Thornlet": ["The wearer has Sap for the whole battle, and it can't be cured."],
    "Cursed Shield": ["The wearer is Confused, Berserk, Sapped, Silenced and under Doom.",
                      "After 256 battles equipped on anyone but Gogo, it turns into the Paladin's Shield."],
    "Flame Shield": shield("Firaga", "Fira"),
    "Ice Shield": shield("Blizzaga", "Blizzara"),
    "Thunder Shield": shield("Thundaga", "Thundara"),
    "Force Shield": ["The wearer has Shell.", "Teaches Shell (×5)."],
    "Paladin's Shield": ["Teaches Ultima (×1)."],
    "Tortoise Shield": ["Teaches Imp (×1)."],
    # relics
    "Alarm Earring": ["Prevents back and pincer attacks, except scripted ones."],
    "Amulet": ["Protects against Poison, Blind and Zombie."],
    "Angel Ring": ["The wearer has Regen, which also blocks Sap."],
    "Angel Wings": ["The wearer has Float."],
    "Barrier Ring": ["Casts Shell on the wearer when their HP gets low.", "Magic +2."],
    "Berserker Ring": ["Gives Umaro a Throw attack that ignores defense.", "Strength +5. Absorbs Fire, nullifies Lightning."],
    "Black Belt": ["75% chance to counter physical attacks with a normal attack."],
    "Blizzard Orb": ["Gives Umaro Snowstorm, an Ice attack on every enemy.", "Magic +5. Absorbs Ice, nullifies Fire."],
    "Bone Wrist": ["+50% max HP and Strength, +25% physical and magic damage, and attacks always hit.",
                   "Strength, Speed, Stamina and Magic +5; Defense and Magic Defense +10; Evade and Magic Evade +10%."],
    "Brigand's Glove": ["Steal becomes Mug: attack and steal in the same turn."],
    "Celestriad": ["Every spell costs 1 MP, including Lores and Esper summons."],
    "Crystal Orb": ["+50% max MP. Doesn't stack with other MP bonuses."],
    "Cursed Ring": ["Teaches X-Zone (×5).", "The wearer starts every battle under Doom."],
    "Dragon Horn": ["Jump lands several times instead of once."],
    "Dragoon Boots": ["Fight becomes Jump."],
    "Earring": ["+25% magic damage, or +50% with two."],
    "Fairy Ring": ["Protects against Poison and Blind."],
    "Fake Mustache": ["Sketch becomes Control."],
    "Gale Hairpin": ["More preemptive attacks."],
    "Gauntlet": ["Hold a one-handed weapon in both hands for double attack power.", "Defense +5."],
    "Genji Glove": ["Equip a weapon in each hand."],
    "Gigas Glove": ["+25% physical damage. Doesn't stack with another Gigas Glove or a Hero's Ring."],
    "Gold Hairpin": ["Halves the MP cost of spells, Lores and Esper summons."],
    "Growth Egg": ["Doubles the wearer's EXP."],
    "Guard Bracelet": ["The wearer has Protect and Shell."],
    "Heiji's Jitte": ["Slot becomes Gil Toss, which throws money at every enemy."],
    "Hermes Sandals": ["The wearer has Haste, which also blocks Slow."],
    "Hero's Ring": ["+25% physical and magic damage. The magic part stacks with another Hero's Ring and Earrings; the physical part doesn't stack with another Hero's Ring or a Gigas Glove."],
    "Hyper Wrist": ["+50% Strength. Doesn't stack with another Hyper Wrist."],
    "Jeweled Ring": ["Protects against Petrify."],
    "Knight's Code": ["The wearer takes physical hits for allies whose HP is low, unless the wearer is KO'd, Petrified, invisible, a Zombie, asleep, Confused or Stopped."],
    "Lich Ring": ["Makes the wearer Undead: most healing hurts them, and instant-death spells and weapons fully heal them."],
    "Master's Scroll": ["Fight hits four times per turn, at half damage each."],
    "Memento Ring": ["Protects against instant death, Petrify and Zombie."],
    "Merit Award": ["Equip almost anything, except women-only gear, the animal suits, the Ultima Weapon and the Bone Club."],
    "Miracle Shoes": ["The wearer has Safe, Shell, Regen and Haste, which also block Slow and Sap."],
    "Molulu's Charm": ["No random battles."],
    "Muscle Belt": ["+50% max HP. Doesn't stack with other HP bonuses."],
    "Mythril Glove": ["Casts Protect on the wearer when their HP gets low.", "Defense +6."],
    "Peace Ring": ["Protects against Berserk and Confuse."],
    "Prayer Beads": ["Evades half of the physical attacks that can be dodged.", "Evade +20%."],
    "Princess Ring": ["Casts Protect and Shell on the wearer when their HP gets low."],
    "Protect Ring": ["The wearer has Protect."],
    "Reflect Ring": ["The wearer has Reflect."],
    "Ribbon": ["Protects against Blind, Poison, Zombie, Petrify, Imp, Silence, Sleep, Berserk, Confuse and Sap."],
    "Safety Bit": ["Protects against instant death, Petrify and Zombie."],
    "Silver Spectacles": ["Protects against Blind."],
    "Sniper Eye": ["The wearer's Fight attacks can't be dodged."],
    "Soul of Thamasa": ["Magic becomes Dualcast: two spells in one turn. Equipped Espers can't be summoned."],
    "Sprint Shoes": ["Walk faster on the field."],
    "Star Pendant": ["Protects against Poison."],
    "Thief's Bracer": ["Doubles the chance to steal with Steal, Mug and the Thief's Knife. Two don't stack.", "Speed +5."],
    "Tintinnabulum": ["Restores HP with each step: the wearer's Stamina divided by 4."],
    "Ward Bangle": ["25% fewer random battles."],
    "White Cape": ["Protects against Imp and Silence.", "Defense and Magic Defense +5, Magic Evade +10%."],
    "Zephyr Cloak": ["The wearer sometimes shows a cape-twirl when dodging.", "Evade and Magic Evade +10%."],
}

SPELLS = {
    "Cure": "Restores HP.", "Cura": "Restores more HP.", "Curaga": "Restores a lot of HP.",
    "Raise": "Revives a KO'd ally with a little HP.", "Arise": "Revives a KO'd ally with full HP.",
    "Reraise": "Revives the target automatically, once, if they're KO'd.",
    "Esuna": "Cures status ailments, except Zombie.", "Poisona": "Cures Poison and Sap.",
    "Regen": "Restores HP little by little.", "Dispel": "Removes status effects from spells, good or bad.",
    "Protect": "Raises physical defense.", "Shell": "Raises magic defense.",
    "Reflect": "Bounces most spells back at their caster.", "Float": "Lifts the target off the ground, which dodges Earth attacks.",
    "Haste": "Fills one target's ATB gauge faster.", "Hastega": "Fills the whole party's ATB gauges faster.",
    "Slow": "Fills one target's ATB gauge slower.", "Slowga": "Fills several targets' ATB gauges slower.",
    "Stop": "Freezes the target's ATB gauge.", "Quick": "The caster takes two turns in a row.",
    "Vanish": "Makes the target invisible.", "Teleport": "Escapes from a dungeon or a battle.",
    "Libra": "Shows the target's HP, MP and weaknesses.",
    "Confuse": "Confuses the target.", "Sleep": "Puts the target to sleep.", "Silence": "Stops the target from casting spells.",
    "Berserk": "The target attacks on its own, uncontrolled.", "Imp": "Turns the target into an Imp.",
    "Fire": "Light Fire damage to one or more targets.", "Fira": "Fire damage, stronger than Fire.", "Firaga": "Heavy Fire damage.",
    "Blizzard": "Light Ice damage to one or more targets.", "Blizzara": "Ice damage, stronger than Blizzard.", "Blizzaga": "Heavy Ice damage.",
    "Thunder": "Light Lightning damage to one or more targets.", "Thundara": "Lightning damage, stronger than Thunder.", "Thundaga": "Heavy Lightning damage.",
    "Poison": "Poison damage, and poisons the target for the rest of the battle.",
    "Bio": "Poison damage, and poisons the targets for the rest of the battle.",
    "Drain": "Takes HP from the target and gives it to the caster.",
    "Osmose": "Takes MP from the target and gives it to the caster.", "Rasp": "Destroys the target's MP.",
    "Holy": "Holy damage to one target.", "Flare": "Heavy non-elemental damage to one target, ignoring defense.",
    "Meteor": "Heavy non-elemental damage to every enemy, ignoring defense.",
    "Ultima": "The strongest non-elemental damage to every enemy, ignoring defense.",
    "Quake": "Earth damage to everyone on the ground, allies included. Floating targets are safe.",
    "Tornado": "Cuts the HP of everyone in battle, allies included, to almost nothing.",
    "Meltdown": "Heavy Fire and Wind damage to everyone in battle, allies included, ignoring defense.",
    "Gravity": "Takes half of the target's HP. No effect on enemies immune to instant death.",
    "Graviga": "Takes three quarters of the targets' HP. No effect on enemies immune to instant death.",
    "Break": "Tries to Petrify one target. No effect on enemies immune to instant death.",
    "Death": "Tries to kill one target outright. No effect on enemies immune to instant death.",
    "Banish": "Tries to send every enemy away for good. No effect on enemies immune to instant death.",
}


def main():
    D = json.loads(DATA.read_text(encoding="utf-8"))
    missing = []
    for e in D["equipment"]:
        extra = e["notes"][1:]
        if e["name"] in ITEMS:
            e["notes"] = e["notes"][:1] + ITEMS[e["name"]]
        elif any(not n.startswith("Element:") for n in extra):
            missing.append(e["name"])
        # 'Element: X' lines become the structured 'elem' field, which the page shows.
        el = [n.split(":", 1)[1].strip() for n in extra if n.startswith("Element:")]
        if el and not e.get("elem"):
            e["elem"] = ", ".join(el)
        e["notes"] = [n for n in e["notes"] if not n.startswith("Element:")]
    for x in D["espers"]:
        x.pop("etym", None)
        for s in x["spells"]:
            if s["desc"] or s["name"] in SPELLS:
                s["desc"] = SPELLS.get(s["name"], "")
                if s["name"] not in SPELLS:
                    missing.append("spell " + s["name"])
    DATA.write_text(json.dumps(D, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("not rewritten:", missing or "none")


if __name__ == "__main__":
    main()
