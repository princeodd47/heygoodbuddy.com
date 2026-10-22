// Recipe builder for the Withered World Synthesis page. Pick a monster to get
// a synthesis chart: the monster at the bottom, its parents branching above.
(function () {
  const root = document.getElementById("synth-builder");
  if (!root) return;

  const data = JSON.parse(document.getElementById("synth-data").textContent);
  const monsters = {};
  const byName = {};
  for (const m of data.monsters) {
    monsters[m.id] = m;
    byName[m.name.toLowerCase()] = m.id;
  }

  // Special recipes first, then the family table.
  const routes = {};
  const add = (id, route) => (routes[id] = routes[id] || []).push(route);
  for (const r of data.recipes) add(r.result, r);
  for (const r of data.family_recipes) {
    add(r.result, {
      parents: [{ family: r.lead }, { family: r.partner }],
      status: r.status,
      sources: r.sources || ["meowdb"],
      note: r.note,
      family: true,
    });
  }
  const hasSpecial = (id) => (routes[id] || []).some((r) => !r.family);

  const input = root.querySelector("#sb-input");
  const list = root.querySelector("#sb-list");
  const out = root.querySelector("#sb-result");

  for (const m of [...data.monsters].sort((a, b) => a.name.localeCompare(b.name))) {
    const opt = document.createElement("option");
    opt.value = m.name;
    list.append(opt);
  }

  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.textContent = text;
    return e;
  }

  function button(cls, text, action, path) {
    const b = el("button", cls, text);
    b.type = "button";
    b.dataset.action = action;
    b.dataset.path = path;
    return b;
  }

  // Open/closed and chosen recipe for each node, keyed by its path in the tree.
  // A path includes the recipe chosen above it, so switching recipes starts
  // that branch fresh.
  let target = null;
  let nodes = new Map();

  // Generations of parents shown before you start clicking. Deeper parents
  // start closed but can still be opened.
  const DEFAULT_DEPTH = 3;

  function nodeState(path, id, depth) {
    const open = depth === 0 || (depth < DEFAULT_DEPTH && hasSpecial(id));
    if (!nodes.has(path)) nodes.set(path, { open, route: 0 });
    return nodes.get(path);
  }

  function familyTile(family) {
    const li = el("li");
    const tile = el("div", "sb-tile sb-any dqm-fam-" + family.toLowerCase());
    tile.append(el("span", "sb-name", "Any " + family));
    li.append(tile);
    return li;
  }

  // `chain` holds the monsters below this one, so a parent that's already
  // being made further down isn't expanded again.
  function monsterNode(id, path, chain) {
    const m = monsters[id];
    const known = routes[id] || [];
    const looped = chain.includes(id);
    const s = nodeState(path, id, chain.length);
    const li = el("li");
    const tile = el("div", "sb-tile dqm-fam-" + m.family.toLowerCase());
    if (!chain.length) tile.classList.add("sb-target");

    if (known.length && !looped) {
      const name = button("sb-name sb-open", m.name, "toggle", path);
      name.setAttribute("aria-expanded", String(s.open));
      name.title = s.open ? "Hide parents" : "Show parents";
      tile.append(name);
    } else {
      tile.append(el("span", "sb-name", m.name));
    }
    tile.append(el("span", "sb-meta", `${m.family} · ${m.rank}`));

    const route = known[s.route];
    if (looped) {
      tile.append(el("span", "sb-meta", "Already in this chart"));
    } else if (!known.length) {
      tile.append(el("span", "sb-meta", "Scout"));
    } else if (s.open) {
      const label = known.length > 1 ? `Recipe ${s.route + 1} of ${known.length}` : "Recipe";
      const info = route.status === "verified" ? label + " ✓" : label;
      const sources = route.sources.map((x) => data.sources[x].name).join(", ");
      if (known.length > 1) {
        const next = button("sb-route", info + " ›", "route", path);
        next.title = "Next recipe";
        tile.append(next);
      } else if (route.status === "verified") {
        tile.append(el("span", "sb-meta", "Verified ✓"));
      }
      tile.title = `${route.status}, from ${sources}`;
      if (route.note) tile.title += `. ${route.note}`;
    }

    li.append(tile);
    if (s.open && route && !looped) {
      const ul = el("ul");
      route.parents.forEach((p, i) => {
        const childPath = `${path}.${s.route}.${i}`;
        ul.append(p.monster ? monsterNode(p.monster, childPath, chain.concat(id)) : familyTile(p.family));
      });
      li.append(ul);
    }
    return li;
  }

  // Summary card for the chosen monster. Skills come from an optional
  // `skills` list on the monster in monsters.yaml.
  function card(id) {
    const m = monsters[id];
    const c = el("section", "sb-card dqm-fam-" + m.family.toLowerCase());
    const name = el("a", "sb-card-name", m.name);
    name.href = "../monsters/#" + id;
    c.append(name);

    const facts = el("div", "sb-card-facts");
    facts.append(el("span", "sb-chip", m.family), el("span", "sb-chip", "Rank " + m.rank));
    const count = (routes[id] || []).length;
    facts.append(el("span", "sb-chip", count ? `${count} known recipe${count > 1 ? "s" : ""}` : "Scout only"));
    if (m.where) facts.append(el("span", "sb-chip", m.where));
    c.append(facts);

    c.append(el("div", "sb-card-label", "Skills"));
    if (m.skills && m.skills.length) {
      const ul = el("ul", "sb-skills");
      for (const s of m.skills) ul.append(el("li", "sb-chip", s));
      c.append(ul);
    } else {
      c.append(el("p", "sb-card-empty", "No skills recorded yet."));
    }
    return c;
  }

  function render() {
    out.replaceChildren();
    if (!target) return;
    const tree = el("ul", "sb-tree");
    tree.append(monsterNode(target, "0", []));
    const wrap = el("div", "sb-chart");
    wrap.append(tree);
    out.append(card(target), wrap);
    // Start scrolled to the bottom-centre, where the chosen monster sits.
    wrap.scrollLeft = (wrap.scrollWidth - wrap.clientWidth) / 2;
  }

  out.addEventListener("click", (e) => {
    const b = e.target.closest("button[data-action]");
    if (!b) return;
    const s = nodes.get(b.dataset.path);
    if (b.dataset.action === "toggle") s.open = !s.open;
    else s.route = (s.route + 1) % routes[idAt(b)].length;
    render();
    const again = out.querySelector(`button[data-path="${b.dataset.path}"][data-action="${b.dataset.action}"]`);
    if (again) again.focus();
  });

  function idAt(b) {
    return byName[b.closest(".sb-tile").querySelector(".sb-name").textContent.toLowerCase()];
  }

  function show(id) {
    target = id;
    nodes = new Map();
    render();
  }

  function pick() {
    const id = byName[input.value.trim().toLowerCase()];
    if (!id || id === target) return;
    show(id);
    const url = new URL(location.href);
    url.searchParams.set("monster", id);
    history.replaceState(null, "", url);
  }

  input.addEventListener("input", pick);
  input.addEventListener("change", pick);

  const start = new URLSearchParams(location.search).get("monster");
  if (start && monsters[start]) {
    input.value = monsters[start].name;
    show(start);
  }
})();
