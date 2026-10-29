// Final Fantasy Resonance item previews. Pages that include the
// ffr-items-data tag (equipment.yaml and items.yaml as JSON) get every known
// item name in their text turned into a button that opens a small preview:
// type, stats, effect and where to get it, with a link to the full entry.
(function () {
  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.append(text);
    return e;
  }

  // Heading ids as the Markdown toc extension writes them.
  function slug(text) {
    return text.toLowerCase().replace(/[^\w\s-]/g, "").trim().replace(/\s+/g, "-");
  }

  // Where-text uses <br> between sources and *...* for quest names.
  function appendWhere(parent, text) {
    text.split("<br>").forEach((line) => {
      const div = el("div");
      line.split(/(\*[^*]+\*)/).forEach((part) => {
        const m = /^\*(.+)\*$/.exec(part);
        if (m) div.append(el("em", null, m[1]));
        else if (part) div.append(part);
      });
      parent.append(div);
    });
  }

  function catalog(data) {
    const items = {};
    for (const g of data.equipment.weapons) {
      for (const e of g.entries) {
        const stats = ["Atk " + e.atk, "Mag " + e.mag].concat(e.other ? [e.other] : []).join(" · ");
        const who = g.who ? g.who : "No one in your party yet";
        items[e.name] = { type: g.type.replace(/s$/, "") + " · " + who, stats, effect: e.effect, where: e.where,
          page: "equipment", anchor: slug(g.type) };
      }
    }
    for (const g of data.equipment.armor) {
      for (const e of g.entries) {
        const stats = ["Def " + e.def, "M.Def " + e.mdef].concat(e.other ? [e.other] : []).join(" · ");
        items[e.name] = { type: g.type + " · " + g.who, stats, effect: e.effect, where: e.where,
          page: "equipment", anchor: slug(g.type) };
      }
    }
    for (const e of data.equipment.accessories) {
      items[e.name] = { type: "Accessory", stats: e.other, effect: e.effect, where: e.where, page: "accessories" };
    }
    for (const g of data.items.groups) {
      for (const e of g.entries) {
        const where = [e.buy && "Buy: " + e.buy.split("<br>").join("; "), e.found].filter(Boolean).join("<br>");
        items[e.name] = { type: "Item · " + g.group, effect: e.effect, where, page: "items", anchor: slug(g.group) };
      }
    }
    return items;
  }

  function setUp() {
    const dataTag = document.getElementById("ffr-items-data");
    const article = document.querySelector("article.md-content__inner");
    if (!dataTag || !article) return;
    const items = catalog(JSON.parse(dataTag.textContent));

    // Longest names first, so "Mist Ether" wins over "Ether".
    const names = Object.keys(items).sort((a, b) => b.length - a.length);
    const escaped = names.map((n) => n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
    const source = "(?<![\\w'-])(" + escaped.join("|") + ")(?![\\w'-])";
    const pattern = new RegExp(source, "g");
    const test = new RegExp(source);

    const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT, {
      acceptNode: (node) =>
        node.parentElement.closest("a, button, .ffr-itemref, code, pre, script, h1, h2, h3, h4, h5, h6, th") ||
        !test.test(node.nodeValue)
          ? NodeFilter.FILTER_REJECT
          : NodeFilter.FILTER_ACCEPT,
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const node of nodes) {
      const frag = document.createDocumentFragment();
      node.nodeValue.split(pattern).forEach((part, i) => {
        if (i % 2) {
          // A span rather than a <button>, so long names wrap like text.
          const btn = el("span", "ffr-itemref", part);
          btn.setAttribute("role", "button");
          btn.tabIndex = 0;
          btn.dataset.item = part;
          btn.setAttribute("aria-haspopup", "dialog");
          frag.append(btn);
        } else if (part) {
          frag.append(part);
        }
      });
      node.replaceWith(frag);
    }

    const pop = el("div", "ffr-itempop md-typeset");
    pop.hidden = true;
    pop.setAttribute("role", "dialog");
    document.body.append(pop);
    let openFor = null;

    function show(ref) {
      const name = ref.dataset.item;
      const item = items[name];
      pop.replaceChildren();
      const close = el("button", "ffr-itempop-close", "✕");
      close.type = "button";
      close.setAttribute("aria-label", "Close");
      close.addEventListener("click", hide);
      pop.append(close, el("div", "ffr-itempop-name", name), el("div", "ffr-itempop-type", item.type));
      if (item.stats) pop.append(el("div", "ffr-itempop-stats", item.stats));
      if (item.effect) pop.append(el("p", null, item.effect));
      if (item.where) {
        const where = el("div", "ffr-itempop-where");
        where.append(el("strong", null, "Where"));
        appendWhere(where, item.where);
        pop.append(where);
      }
      const link = el("a", null, "Full entry →");
      link.href = new URL("../" + item.page + "/" + (item.anchor ? "#" + item.anchor : ""), location.href).href;
      const linkLine = el("p", "ffr-itempop-link");
      linkLine.append(link);
      pop.append(linkLine);
      pop.hidden = false;
      openFor = ref;

      const r = ref.getBoundingClientRect();
      const width = pop.offsetWidth;
      const left = Math.max(8, Math.min(r.left + window.scrollX, window.scrollX + document.documentElement.clientWidth - width - 8));
      pop.style.left = left + "px";
      pop.style.top = r.bottom + window.scrollY + 6 + "px";
    }

    function hide() {
      const ref = openFor;
      pop.hidden = true;
      openFor = null;
      return ref;
    }

    article.addEventListener("click", (e) => {
      const ref = e.target.closest(".ffr-itemref");
      if (!ref) return;
      if (openFor === ref) hide();
      else show(ref);
    });
    article.addEventListener("keydown", (e) => {
      const ref = e.target.closest(".ffr-itemref");
      if (!ref || (e.key !== "Enter" && e.key !== " ")) return;
      e.preventDefault();
      if (openFor === ref) hide();
      else show(ref);
    });
    document.addEventListener("click", (e) => {
      if (openFor && !pop.contains(e.target) && !e.target.closest(".ffr-itemref")) hide();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && openFor) hide().focus();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setUp);
  } else {
    setUp();
  }
})();
