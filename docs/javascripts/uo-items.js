// Unicorn Overlord equipment previews. Pages that include the uo-items-data
// tag (equipment.yaml as JSON) get every known item name in their text turned
// into a button that opens a small preview: type, stats, effects, skill, price
// and where to get it, with a link to the item's row on the Equipment page.
(function () {
  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.append(text);
    return e;
  }

  function catalog(data) {
    const items = {};
    for (const g of data.groups) {
      for (const e of g.entries) {
        items[e.name] = Object.assign({ type: g.type.replace(/ves$/, "ff").replace(/ies$/, "y").replace(/s$/, "") }, e);
      }
    }
    return items;
  }

  function setUp() {
    const dataTag = document.getElementById("uo-items-data");
    const article = document.querySelector("article.md-content__inner");
    if (!dataTag || !article) return;
    const items = catalog(JSON.parse(dataTag.textContent));

    // Longest names first, so "Black Iron Greatshield" wins over shorter names.
    const names = Object.keys(items).sort((a, b) => b.length - a.length);
    const escaped = names.map((n) => n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
    const source = "(?<![\\w'-])(" + escaped.join("|") + ")(?![\\w'-])";
    const pattern = new RegExp(source, "g");
    const test = new RegExp(source);

    const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT, {
      acceptNode: (node) =>
        node.parentElement.closest("a, button, .uo-itemref, code, pre, script, h1, h2, h3, h4, h5, h6, th") ||
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
          const ref = el("span", "uo-itemref", part);
          ref.setAttribute("role", "button");
          ref.tabIndex = 0;
          ref.dataset.item = part;
          ref.setAttribute("aria-haspopup", "dialog");
          frag.append(ref);
        } else if (part) {
          frag.append(part);
        }
      });
      node.replaceWith(frag);
    }

    const pop = el("div", "uo-itempop md-typeset");
    pop.hidden = true;
    pop.setAttribute("role", "dialog");
    document.body.append(pop);
    let openFor = null;

    function show(ref) {
      const name = ref.dataset.item;
      const item = items[name];
      pop.replaceChildren();
      const close = el("button", "uo-itempop-close", "✕");
      close.type = "button";
      close.setAttribute("aria-label", "Close");
      close.addEventListener("click", hide);
      pop.append(close, el("div", "uo-itempop-name", name), el("div", "uo-itempop-type", item.type));
      if (item.stats) pop.append(el("div", "uo-itempop-stats", item.stats));
      if (item.effects.length) pop.append(el("p", null, item.effects.join(" · ")));
      if (item.skill) {
        const skill = el("p");
        skill.append(el("strong", null, item.skill.name));
        if (item.skill.details) skill.append(" (" + item.skill.details + ")");
        if (item.skill.text) skill.append(": " + item.skill.text);
        pop.append(skill);
      }
      if (item.price) {
        const price = el("p");
        price.append(el("strong", null, "Price: "), item.price);
        pop.append(price);
      }
      if (item.where.length) {
        const where = el("div", "uo-itempop-where");
        where.append(el("strong", null, "Where"));
        for (const line of item.where) where.append(el("div", null, line));
        pop.append(where);
      }
      const link = el("a", null, "Full entry →");
      link.href = new URL("../equipment/#" + item.id, location.href).href;
      const linkLine = el("p", "uo-itempop-link");
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
      const ref = e.target.closest(".uo-itemref");
      if (!ref) return;
      if (openFor === ref) hide();
      else show(ref);
    });
    article.addEventListener("keydown", (e) => {
      const ref = e.target.closest(".uo-itemref");
      if (!ref || (e.key !== "Enter" && e.key !== " ")) return;
      e.preventDefault();
      if (openFor === ref) hide();
      else show(ref);
    });
    document.addEventListener("click", (e) => {
      if (openFor && !pop.contains(e.target) && !e.target.closest(".uo-itemref")) hide();
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
