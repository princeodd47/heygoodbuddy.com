# FF Resonance Bestiary research

Notes behind `docs/games/final-fantasy-resonance/bestiary.md` and
`data/final-fantasy-resonance/bestiary.yaml`.

## Sources

- ffresonance.wiki enemy pages (level, where, weaknesses, drops, steals).
- meowdb.com/db/final-fantasy-resonance/areas/<slug> and /enemies/<slug>
  (datamined: encounter tables per area, drop vs rare drop vs steal, chests).
  Used for Old Town, Lake Dorr and Waterfall Way (2026-10-28).
  Variant drops are filtered to the levels in progress.
- RPG Site walkthrough, to confirm which enemies appear where.
- The user's in-game Libra checks win over both.

## Open questions

- **Resistances** (added 2026-10-29) are all from meowdb enemy pages:
  "Halved" → listed plain, "Immune" → "(immune)". No enemy so far absorbs.
  Pots nullify all damage; Metal Minituar halves every element.
- **Weakness mismatches with meowdb:** Soul (page: Fire, Earth; meowdb: Fire
  only, resists Ice) and Sergeant (page: Fire, Earth, Water, Light; meowdb:
  Fire, Light). Page left as is; Libra them if the user revisits.

- **Uncertain placements:** Minituar, Imp, Killer Mantis. (Medusa and Dhorme
  Chimera were confirmed by the walkthrough.)
- **Southern Olderion cluster:** only Basilisk, Mini Gil Snapper, Mu, Sea
  Scorpion, Sorcerer, Diresaur and Green Soul (lv 18–19) were added. A
  YouTube video saw a **Destroyer** in the south Olderion Gil Snapper spot,
  which suggests the north/south split may be off.
- **Rukh:** is it optional?
- **Old Town "Defeat the monsters" fights:** no source names the regular
  enemies. Only Water Dragon is on the page.
- **Alluvion lv 26** (meowdb, ch. 3, 48,000 HP, weak Lightning, immune Water,
  drops Azure Amulet, "special skill grows with each prism core"). Listed
  under the Water Shrine as its boss. The story also has a battle with
  Alluvion in flooded Old Town; unknown whether that's the same fight data.
- **Olderion world map fields 5–8:** Destroyer, Gigas, Gigas Worm and
  Maelspike also appear there (field 5, 6, 7, 8). Not added to a world-map
  group; which fields the user has crossed is unknown.
- **Metal Minituar HP:** sources say 3, 4, 6 or 9 depending on difficulty.
  The bestiary doesn't list HP.

## Held back (deliberately excluded)

- **Chapter 4 after "Gather information in Zoldaad":** Underground Tunnel
  (Fire Lizard in area 2, Crimson Pot), Weapons Factory (Ignis lv 27, 56,000
  HP, weak Water, halves Fire, enrages when hit), Zoldaad Castle, Emperor of
  Zoldaad (lv 30, 52,000 HP, weak Water, Poison), Lazarov (lv 30, 45,000 HP,
  weak Earth, Sleep). Optional: Gogmagog Cave and Pyroviper Cave bosses.
  Not researched in detail.
- **Anet and Adamantoise on the world map:** the wiki also lists them on the
  Olderion world map. They're only under Cave of Waters on the page until
  the user confirms where else they appear.

- **Kolobos Ruins / Cavern of Swords, high level:** Former Knight (lv 40,
  weak Fire, Light), Magitek Weapon (lv 41, weak Lightning, Water). Later
  revisit content.
- **Tonberry** (lv 42, Gronoa Shrine). Chapter 6.
- **Gilgamesh:** Siren's Tower to the Genji Armor chain (see wiki
  gilgamesh-genji-gloves). Later.
- **Titan:** sealed desert Esper; needs Colosseum Fledgling Battle 5.
- **Cactuar:** now listed under Zoldaad (World Map). Also Dirnado field 6
  and Grandshelt field 9 (meowdb); those aren't in its Where.
- **Northern Olderion cluster** (lv 24+): Anet, Adamantoise, Destroyer,
  Dragon Junior, Drosera, Gigas, Golden Eagle, Thug, Vulture, Twinscythe,
  Amoebozoa, Zuu.
- **Olderion city / Old Town enemies:** from later events; the first visit
  has no fights.
- **Umbra:** later boss.

## Already on the page

Areas, in order: Grandshelt Castle, Earth Shrine, Grandshelt (World Map),
Grandport (World Map), Kolobos (World Map), Kolobos Ruins, Siren's Tower,
Marauder Cave, Dirnado (World Map), Mt. Thunderclap, Dwarven Forge, Shoggoth
Cave, Mobliz Shipyard, Wind Shrine, Olderion (World Map, south), Rukh Cave,
Cave of Waters (regular enemies, Wave Lopros and its two Snappers; areas
3–7 have no new regular enemies), Old Town, Olderion (Water Dragon), Lake
Dorr (Leviathan, Orbs of Light), Waterfall Way (Merman, Xiphactinus, Gigas
Worm, Maelspike, Black Shark, Gigas, Destroyer), Olderion (World Map,
around Amore) = meowdb "Olderion field 6" (Hivesguard, Drosera, Dragon
Junior, Destroyer, Vulture, Amoebozoa, Zuu), Water Shrine (Objet d'Art,
Skadi, Pit Fiend, Red Marshmallow, Ribosome, Megalodon, Monster Effigy,
boss Alluvion). Warden's Cape has no area page of its own on meowdb.

Leviathan details not on the page: 40,000 HP, 4,500 EXP, 2,400 gil; resists
Water; enrages if the fight drags on. Orbs of Light: one weak Fire (resists
Ice), one weak Water (resists Fire), one weak Earth (resists Wind); breaking
one weakens Leviathan. Water Dragon: 24,000 HP, resists Water.

## Zoldaad (added 2026-10-29)

From meowdb's encounter map (`/db/final-fantasy-resonance/tools/encounter-map`,
JSON embedded in the page). Fields: 1 near Mozul Station, 2 near the capital,
3 and 4 near Capital Station, 5 and 6 "near Rebel Hideout" (east), 7 near the
Weapons Factory (far east), 8 near Infernal Hollow (far south, plus a small
northern patch). All eight are one "Zoldaad (World Map)" group; Where gives
rough directions. Field 8 is only Cactuar, Sandworm, Sandworm + 2 Treants
(a third each). Sandworm is typed "Boss" on meowdb but is a random encounter;
not marked boss.

Colosseum (Fledgling League) group: Balaur, Simurgh, Blood Worm, Gray Bomb,
Ice Lizard, Lieutenant, Allosaur, Ice Sculpture, Ahriman. Most also roam
Mysidia (ch. 5); that's left out of Where. Wyvern, Magma Tortoise, Coeurl
and Chimera are in the Zoldaad group with "Colosseum" added to Where.
