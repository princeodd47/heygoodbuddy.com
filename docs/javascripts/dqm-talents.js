// Search and pick on the Withered World Talents page. Every Talent is rendered
// as a <section class="tal"> with a lowercase data-search string; this shows
// one at a time and filters the Talent buttons as you type.
(function () {
  const root = document.getElementById("dqm-talents");
  if (!root) return;

  const input = document.getElementById("tal-search");
  const list = document.getElementById("tal-list");
  const hint = document.getElementById("tal-hint");
  const sections = [...root.querySelectorAll("section.tal")];
  let current = null;

  const buttons = sections.map((s) => {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "tal-pick";
    b.textContent = s.dataset.name;
    b.dataset.id = s.id;
    list.append(b);
    return b;
  });

  function select(id) {
    current = sections.find((s) => s.id === id) ? id : null;
    for (const s of sections) s.hidden = s.id !== current;
    for (const b of buttons) b.setAttribute("aria-pressed", String(b.dataset.id === current));
    hint.hidden = Boolean(current);
    highlight();

    const url = new URL(location.href);
    if (current) url.searchParams.set("talent", current);
    else url.searchParams.delete("talent");
    history.replaceState(null, "", url);
  }

  // Mark tree rows whose skill matches the search.
  function highlight() {
    const q = input.value.trim().toLowerCase();
    for (const row of root.querySelectorAll(".tal-tree tbody tr")) {
      row.classList.toggle("tal-match", Boolean(q) && row.dataset.name.includes(q));
    }
  }

  function filter() {
    const q = input.value.trim().toLowerCase();
    let shown = 0;
    sections.forEach((s, i) => {
      const match = !q || s.dataset.search.includes(q);
      buttons[i].hidden = !match;
      if (match) shown++;
    });
    hint.textContent = shown ? "Pick a Talent to see its tree." : "No Talent, skill or monster matches that.";
    // One match: show it straight away.
    const visible = buttons.filter((b) => !b.hidden);
    if (visible.length === 1) select(visible[0].dataset.id);
    else highlight();
  }

  list.addEventListener("click", (e) => {
    const b = e.target.closest("button.tal-pick");
    if (b) select(b.dataset.id);
  });
  input.addEventListener("input", filter);
  input.addEventListener("keydown", (e) => {
    if (e.key !== "Enter") return;
    const first = buttons.find((b) => !b.hidden);
    if (first) select(first.dataset.id);
  });

  select(new URLSearchParams(location.search).get("talent"));
})();
