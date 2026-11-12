# Equipment page research

The page and data come from `scripts/uo_equipment.py`. Rerun it after adding
items to the Post-Game Teams page: it reads that page's Equipment column and
writes `data/unicorn-overlord/equipment.yaml`. The page and the item previews
on Post-Game Teams (`docs/javascripts/uo-items.js`) read that file.

## Sources (2026-11-11)

- unicornoverlord.fandom.com via its API (curl works; WebFetch gets 402):
  item pages (stats, effects, skill, obtention), every page in
  Category:Towns and Cities (armorer stock and prices), the "<Continent>
  (Locations)" pages for each town's continent, Black Market Dealer, Divine
  Shard Exchange, Coliseum Prize Exchange, Quests (reward columns), Star Iron
  (Meteorite weapons).
- unilord.miraheze.org via its API: weapon tables' "How to Obtain", used only
  when Fandom gives nothing (e.g. Juggernaut, General's Pike, Icestorm Staff).
- GameFAQs Merqurial item tables and Game8 shield list (read via Chrome): stats
  only, no locations.

## Known gaps and quirks

- No source found for: Blue Rose Shield, Drakestone Iceshield, Golden Ram
  Shield, Heavenswing Shield, Nameless Guard's Shield,
  Vengeful Caligae, Watchman's Lantern, White Rider's
  Shield. Likely character starting gear (Heavenswing = Ochlys? Golden Ram =
  Gloucester? Watchman's Lantern = Mandrin? Drakestone Iceshield is on Amalia
  in the Miraheze Coliseum data). Ask the user to check in-game.
- **From the user:** Necromancer's Lantern drops from Baltro the first time
  you fight him in Elheim. Fandom's Baltro page puts that fight in the Forest
  of Thorns, which is the main quest Vile Desecration (Quests page).
- **From the user (Discord tip):** Lamplight Ring comes from a person on
  Albion's southern coast, possibly in Jerome's city. Jerome's city is
  Largion Citadel (Fandom), in southeastern Albion. Not confirmed in-game.
- Fandom's Quests page lists Ring of the Unicorn under quests that need it;
  overridden to "Alain's starting accessory".
- Fandom's Celestial Talisman skill box says "Hastened Cast"; the script takes
  the skill name from the item's Effect #1 (Hastened Charge) instead.
- Names follow the post-game page's GameFAQs spellings; ALIASES maps them to
  Fandom titles (Boreas' Axe -> Boreas's Axe, Speedhex -> Speed-Hex, etc.).
- Divine Shard Exchange stock is shared across every church.
