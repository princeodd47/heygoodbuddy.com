"""Second wording pass on data.json: Lores, Dance moves, Esper locations,
equipment elemental properties and Rage footnotes, all in our own words.

Dance moves also get a `kinds` list (used by the page's move filter), worked
out from the old descriptions before they're replaced.

    python3 notes/final-fantasy-vi-advance/tools/rewrite_more.py
"""
import json
import re
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data.json"

LORES = {
    "1000 Needles": "Always deals exactly 1,000 damage to one enemy.",
    "Aero": "Wind damage to every enemy.",
    "Aqua Breath": "Water and Wind damage to every enemy.",
    "Bad Breath": "Inflicts Blind, Poison, Imp, Silence, Confuse and Sleep on one enemy.",
    "Dischord": "Halves one enemy's level.",
    "Doom": "Puts a countdown on one enemy; it's KO'd when the count runs out.",
    "Force Field": "Each cast makes the party immune to one random element for the rest of the battle.",
    "Grand Delta": "Heavy damage to every enemy.",
    "Lv. 3 Confuse": "Confuses every enemy whose level is a multiple of 3.",
    "Lv. 4 Flare": "Casts Flare on every enemy whose level is a multiple of 4.",
    "Lv. 5 Death": "KOs every enemy whose level is a multiple of 5.",
    "Lv. ? Holy": "Casts Holy on every enemy whose level is a multiple of the last digit of your gil (the game hides the number).",
    "Mighty Guard": "Protect and Shell on the whole party.",
    "Quasar": "Heavy damage to every enemy.",
    "Reflect ???": "Hits every enemy that has Reflect with Blind, Silence or Slow, at random.",
    "Revenge Blast": "Damage to one enemy equal to the HP the caster has lost.",
    "Rippler": "Swaps status effects between the caster and one target.",
    "Roulette": "A wheel picks one fighter, enemy or ally, and KOs it.",
    "Self-Destruct": "The caster is KO'd to deal heavy damage to one enemy.",
    "Stone": "Damages and Confuses one enemy; 7.5× damage when the caster's level matches the target's.",
    "Transfusion": "The caster gives up their life and all their MP to fully heal one ally.",
    "Traveler": "Damage to one enemy equal to the party's total steps divided by 32.",
    "Tsunami": "Heavy Water damage to every enemy.",
    "White Wind": "Heals the whole party by the caster's current HP.",
}

NOSPLIT = "isn't weakened by hitting several targets"
NODEATH = "fails on enemies immune to instant death"
MOVES = {
    "Wind Slash": f"Wind damage to every enemy. Can't be blocked and {NOSPLIT}.",
    "Sunbath": "Heals the whole party.",
    "Plasma": "Lightning damage to one enemy. Can't be blocked.",
    "Cockatrice": f"Magic damage that ignores defense and Petrifies one enemy; {NODEATH}.",
    "Leaf Swirl": f"Non-elemental magic damage to every enemy. Can't be blocked and {NOSPLIT}.",
    "Forest Healing": "Cures Blind, Poison, Petrify, Silence, Confuse, Sap, Sleep, Slow and Stop.",
    "Will o' the Wisp": "Fire damage to one enemy. Can't be blocked.",
    "Wombat": "Strong magic damage to one enemy, ignoring defense. Misses flying enemies.",
    "Sandstorm": f"Wind damage to every enemy; {NOSPLIT}.",
    "Antlion": f"KOs one enemy; {NODEATH}.",
    "Meerkat": "Haste on the whole party.",
    "Apparition": "Confuses one enemy.",
    "Snare": f"KOs one enemy, Undead included; {NODEATH}. It also holds off a dying enemy's final attack for a turn.",
    "Tapir": "Cures almost every status ailment. Anyone asleep also gets their HP and MP fully restored.",
    "Rock Slide": "Magic damage to one enemy, ignoring defense.",
    "Sonic Boom": f"Cuts one enemy's HP by 5/8 of its maximum and Saps it; {NODEATH}.",
    "Boar Brigade": "Magic damage to one enemy, ignoring defense. Misses flying enemies.",
    "El Niño": f"Water damage to every enemy. Can't be blocked and {NOSPLIT}.",
    "Raccoon": "Heals the whole party and cures almost every status ailment, Frozen included.",
    "Cave In": f"Cuts one enemy's current HP by three quarters and Saps it; {NODEATH}.",
    "Poisonous Frog": "Poison damage to one enemy, and poisons it.",
    "Snowball": f"Halves one enemy's HP; {NODEATH}.",
    "Avalanche": f"Ice damage to every enemy. Can't be blocked and {NOSPLIT}.",
    "Arctic Hare": "Heals the whole party.",
}

ESPER_LOC = {
    "Alexander": "Doma Castle throne room, after Cyan's dream (World of Ruin).",
    "Bahamut": "Beat Doom Gaze in the sky (World of Ruin). Using X-Zone on it loses the Esper.",
    "Bismarck": "Magitek Research Facility lab (World of Balance).",
    "Cactuar": "Maranda desert.",
    "Cait Sith": "Zozo, after you find Terra (World of Balance).",
    "Carbuncle": "Magitek Research Facility lab (World of Balance).",
    "Catoblepas": "Magitek Research Facility lab (World of Balance).",
    "Crusader": "Where you beat the last of the eight dragons (World of Ruin).",
    "Diabolos": "Dragons' Den.",
    "Fenrir": "Mobliz, after beating Humbaba (World of Ruin).",
    "Gilgamesh": "Colosseum.",
    "Golem": "Jidoor auction house.",
    "Ifrit": "Magitek Research Facility (World of Balance).",
    "Kirin": "Zozo, after you find Terra (World of Balance).",
    "Lakshmi": "Owzer's Mansion, after beating Chadarnook (World of Ruin).",
    "Leviathan": "The ferry between Nikeah and South Figaro.",
    "Maduin": "Magitek Research Facility lab (World of Balance).",
    "Midgardsormr": "Umaro's Cave (World of Ruin).",
    "Odin": "Ancient Castle (World of Ruin).",
    "Phantom": "Magitek Research Facility lab (World of Balance).",
    "Phoenix": "Phoenix Cave, in the star-shaped mountains (World of Ruin).",
    "Quetzalli": "Cid's island, once you have the airship (World of Ruin).",
    "Ragnarok": "Narshe weapon shop (World of Ruin), instead of the Ragnarok sword.",
    "Raiden": "Ancient Castle basement (World of Ruin): stand five steps below the queen's throne and press the action button.",
    "Ramuh": "Zozo, after you find Terra (World of Balance).",
    "Seraph": "Bought in Tzen: 3,000 gil in the World of Balance, 10 gil in the World of Ruin.",
    "Shiva": "Magitek Research Facility (World of Balance).",
    "Siren": "Zozo, after you find Terra (World of Balance).",
    "Unicorn": "Magitek Research Facility lab (World of Balance).",
    "Valigarmanda": "The cliffs above Narshe (World of Ruin).",
    "Zona Seeker": "Jidoor auction house.",
}

FOOTNOTES = {
    "Siegfried (2)": "Left unused in the game; only reachable with a cheat device.",
    "Typhon (Colosseum)": "Left unused in the game; only reachable with a cheat device.",
    "Death Warden": "Unused on SNES and PlayStation without cheats, but Gau can learn it normally on GBA.",
    "Tonberries": "Unused on SNES and PlayStation. On GBA Gau can learn it, but it can't be picked in battle.",
}

ELEM_NAMES = {"pearl": "Holy", "bolt": "Lightning"}


def old_kinds(desc):
    d, k = desc.lower(), []
    if re.search(r"all opponents", d):
        k.append("all")
    elif re.search(r"(one|an?) (opponent|enemy|target)|enemy's hp|target's hp|one target", d) and not re.search(r"causes death|reduces", d):
        k.append("one")
    if re.search(r"restores? hp", d):
        k.append("heal")
    if re.search(r"recovers from", d):
        k.append("cure")
    if re.search(r"causes death|reduces .*hp", d):
        k.append("death")
    if re.search(r"haste on all allies", d):
        k.append("buff")
    return k


def and_list(items):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def elem_text(s):
    if ":" not in s:
        return s
    verbs = {"Absorbs Damage": "Absorbs", "Nullifies Damage": "Nullifies", "Halves Damage": "Halves", "Double Damage": "Weak to"}
    out = []
    for part in s.split(";"):
        k, v = part.split(":", 1)
        names = [ELEM_NAMES.get(n.strip().lower(), n.strip().capitalize()) for n in v.split(",") if n.strip()]
        out.append(f"{verbs[k.strip()]} {and_list(names)}")
    return ". ".join(out) + "."


def main():
    D = json.loads(DATA.read_text(encoding="utf-8"))
    missing = []
    for l in D["lores"]:
        if l["name"] in LORES:
            l["desc"] = LORES[l["name"]]
        else:
            missing.append("lore " + l["name"])
    for d in D["dances"]:
        for m in d["moves"]:
            if "kinds" not in m:
                m["kinds"] = old_kinds(m["desc"])
                power = re.search(r"spell power is (\d+)", m["desc"])
                m["power"] = int(power.group(1)) if power else None
            if m["name"] in MOVES:
                m["desc"] = MOVES[m["name"]] + (f" Power {m['power']}." if m.get("power") else "")
            else:
                missing.append("move " + m["name"])
    for e in D["espers"]:
        if e["name"] in ESPER_LOC:
            e["loc"] = ESPER_LOC[e["name"]]
        else:
            missing.append("esper " + e["name"])
    for e in D["equipment"]:
        if e.get("elem"):
            e["elem"] = elem_text(e["elem"])
    for r in D["rages"]:
        if r.get("footnote"):
            if r["name"] in FOOTNOTES:
                r["footnote"] = FOOTNOTES[r["name"]]
            else:
                missing.append("footnote " + r["name"])
    DATA.write_text(json.dumps(D, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("not rewritten:", missing or "none")


if __name__ == "__main__":
    main()
