// Rank and family toggles for the Withered World Monsters page. Each group of
// monsters is a .dqm-grid tagged with data-rank and data-family; its heading
// has the id rank-<rank>-<family> and its rank heading the id rank-<rank>.
(function () {
  const box = document.getElementById("dqm-filters");
  if (!box) return;

  const grids = [...document.querySelectorAll(".dqm-grid[data-rank]")];
  const unique = (key) => [...new Set(grids.map((g) => g.dataset[key]))];
  const ranks = unique("rank");
  const families = unique("family");
  const label = (s) => s.charAt(0).toUpperCase() + s.slice(1);

  // Start from the address, e.g. ?rank=f&family=dragon,slime ("none" hides
  // the whole row).
  const params = new URLSearchParams(location.search);
  const fromUrl = (key, all) => {
    if (params.get(key) === "none") return new Set();
    const picked = (params.get(key) || "").split(",").filter((x) => all.includes(x));
    return new Set(picked.length ? picked : all);
  };
  let shownRanks = fromUrl("rank", ranks);
  let shownFamilies = fromUrl("family", families);

  function apply() {
    for (const g of grids) {
      const show = shownRanks.has(g.dataset.rank) && shownFamilies.has(g.dataset.family);
      g.hidden = !show;
      document.getElementById(`rank-${g.dataset.rank}-${g.dataset.family}`).hidden = !show;
    }
    for (const r of ranks) {
      const any = grids.some((g) => g.dataset.rank === r && !g.hidden);
      document.getElementById(`rank-${r}`).hidden = !any;
    }
    empty.hidden = grids.some((g) => !g.hidden);
    for (const b of box.querySelectorAll("button[data-value]")) {
      const set = b.dataset.kind === "rank" ? shownRanks : shownFamilies;
      b.setAttribute("aria-pressed", String(set.has(b.dataset.value)));
    }

    const url = new URL(location.href);
    for (const [key, set, all] of [["rank", shownRanks, ranks], ["family", shownFamilies, families]]) {
      if (set.size === all.length) url.searchParams.delete(key);
      else if (!set.size) url.searchParams.set(key, "none");
      else url.searchParams.set(key, all.filter((x) => set.has(x)).join(","));
    }
    history.replaceState(null, "", url);
  }

  function row(title, kind, values, cls) {
    const div = document.createElement("div");
    div.className = "dqm-filter-row";
    div.setAttribute("role", "group");
    div.setAttribute("aria-label", title);
    const span = document.createElement("span");
    span.className = "dqm-filter-label";
    span.textContent = title;
    div.append(span);
    for (const v of values) {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "dqm-toggle " + cls(v);
      b.dataset.kind = kind;
      b.dataset.value = v;
      b.textContent = kind === "rank" ? "Rank " + v.toUpperCase() : label(v);
      div.append(b);
    }
    for (const [text, action] of [["Show all", "all"], ["Hide all", "none"]]) {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "dqm-toggle dqm-bulk";
      b.dataset.kind = kind;
      b.dataset.action = action;
      b.textContent = text;
      div.append(b);
    }
    return div;
  }

  const empty = document.createElement("p");
  empty.className = "dqm-empty";
  empty.textContent = "Nothing selected. Turn on at least one rank and one family.";

  box.append(
    row("Ranks", "rank", ranks, () => "dqm-toggle-rank"),
    row("Families", "family", families, (f) => "dqm-fam-" + f),
    empty,
  );

  box.addEventListener("click", (e) => {
    const b = e.target.closest("button");
    if (!b) return;
    const isRank = b.dataset.kind === "rank";
    if (b.dataset.action) {
      const set = b.dataset.action === "all" ? new Set(isRank ? ranks : families) : new Set();
      if (isRank) shownRanks = set;
      else shownFamilies = set;
    } else {
      const set = isRank ? shownRanks : shownFamilies;
      if (set.has(b.dataset.value)) set.delete(b.dataset.value);
      else set.add(b.dataset.value);
    }
    apply();
  });

  // A link to a monster that's filtered out (e.g. from the Synthesis page)
  // shows everything rather than landing on nothing.
  const target = location.hash && document.getElementById(location.hash.slice(1));
  if (target && target.classList.contains("dqm-tile")) {
    const g = target.closest(".dqm-grid");
    if (!shownRanks.has(g.dataset.rank) || !shownFamilies.has(g.dataset.family)) {
      shownRanks = new Set(ranks);
      shownFamilies = new Set(families);
    }
  }
  apply();
})();
