# FF Resonance Equipment, Accessories and Items research

Notes behind `equipment.md`, `accessories.md` and `items.md` in
`docs/games/final-fantasy-resonance/`. The data is generated into
`data/final-fantasy-resonance/equipment.yaml` and `items.yaml`. Don't
hand-edit those; regenerate them (see Regenerating below).

## Scope

Everything the user *could* have obtained up to their progress (2026-10-29:
Ch. 4, "Gather information in Zoldaad"), including reachable optional
content: the Colosseum Fledgling League and its shop, Grandshelt Castle's
Chapter 4 jail chests, Olderion jump rope up to 60, the Mechabo Evolved
Sandworms, and the optional bosses Mindflayer, Gogmagog and Pyroviper
(Magicite and Mist Turbo Ether only).

Left out: Titan (Esper rule; it drops Magicite) and Ruby Fragments/Ruby
Cave (Esper rule). Everything from "Meet up in the alley" onward is out
(Underground Tunnel, Rebel Hideout and its shop, Weapons Factory, etc.).
Capital Market stock marked "from partway through Chapter 4" is out; its
current stock is the inflated "until partway" list. Colosseum stock behind
the Brawler's and Gladiator's Proofs is out.

## Sources

- meowdb (NiaDB): `/db/final-fantasy-resonance/equipment`, `/items` and
  `/areas` lists (JSON is embedded in each page), plus area pages for
  chests and shops. The area pages list town and dungeon chests only, not
  world-map pickups.
- RPG Site 100% walkthrough (rpgsite.net/guide/21486-...): chests,
  world-map pickups, NPC gifts and quest rewards, in story order.
- `bestiary.yaml`: drops and steals for every enemy on the Bestiary page.
- Tablet Shard boxes up to 48. Colosseum first-win rewards.

## Method

1. `catalog.py` parses the embedded catalog JSON (areas, items, equipment).
2. `area.py` parses each area page's chests, shops (name, shop, price/notes)
   and quests.
3. `build.py` adds shop sources for the reached towns. The Colosseum's
   no-Proof consumables (Hi-Potion, Mist Hi-Potion, Turbo Ether, Mist Turbo
   Ether, Phoenix Down) aren't parsed from the HTML and are added by hand.
4. `build2.py` matches catalog names in the RPG Site text from Chapter 1 to
   "Meet up with your party at Imperial Hotel alley", labels each match with
   a place, adds meowdb chests for visited areas, quest/NPC rewards, box
   rewards and bestiary drops/steals.
5. `gen.py` sorts by first availability (a fixed story order of places;
   enemies take their Bestiary group's place; boxes take the area where that
   shard total is reached) and writes the YAML. Consumables are grouped by
   kind. For buyable consumables, enemy drops/steals are left out.

## Regenerating

The scripts live in `notes/final-fantasy-resonance/tools/` and expect a
working directory containing `inv/` (downloads) and `bin/` (the scripts):
`inv/catalog.json` (from `areas.html`, `list-items.html`,
`list-equipment.html`), `inv/areas/*.html`, `inv/areas.json`,
`inv/rpgsite.txt` and `inv/rpg_hits.json` (the RPG Site matcher was an inline
script: it scans lines between "### Chapter 1" and a cutoff line for catalog
names, longest first). On a progress update: move the cutoff line, add the
new towns to `shopareas` (build.py) and areas to `VIS`/`PLACE`/`ORDER`, drop
the "until partway" filter if the Capital Market has changed, then rerun.

## Character weapon and armor types (meowdb character pages)

Rain: greatsword, heavy and light armor. Lasswell: katana, heavy and light.
Fina: bow, robe and light. Archwitch Fina: whip, robe and light. Lid:
hammer, light and heavy. Nichol: grimoire, robe and light. Guns and rods
have no user in the party yet ("Nobody in your party uses these yet").

## Open questions

- Lordly Robes: meowdb says a "Grandshelt Castle (Prologue)" chest, RPG
  Site gets it in ch. 8. Left out.
- Transporter artifact: meowdb says "Grandshelt Castle, story event", with
  no chapter. Left out.
- Bandit Cuff Links, Sorcerer's Cape, Tome of Sages: meowdb says "New game,
  starting item". Listed. Verify with the user.
- Remedy at the Colosseum: listed twice on meowdb; treated as Fledgling.
- Hasaito: RPG Site only mentions it in passing ("near the Hasaito"),
  west of Ruby Cave. Listed as a world-map pickup there.
- Ancient Greatsword: Atk 1, Mag 1, no description.
- Some starting gear and NPC-only items may be missing: RPG Site doesn't
  list starting equipment.

## Item popups

`docs/javascripts/ffr-items.js` turns every known item name on a page into
a clickable span that opens a preview (type, stats, effect, where, and a
"Full entry" link to the Equipment/Accessories/Items section). It only runs
on pages that end with the `ffr-items-data` script tag (equipment.yaml and
items.yaml as JSON): bestiary, colosseum, tablet-shards, tips, visions,
espers, key-items. A new FFR page that mentions items needs that tag.
Names are matched longest-first ("Mist Ether" before "Ether"), skipping
links, headings, table headers and code. Key items aren't matched. YAML
groups use `entries`, not `items` (Jinja reads `g.items` as dict.items).
Styles are in `docs/stylesheets/extra.css`. Tested in headless Chrome
2026-10-29: 307 names on the Bestiary, popup opens and closes.

## Already on the pages

108 weapons and armor, 37 accessories, 46 consumables (2026-10-29).
