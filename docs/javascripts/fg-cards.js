// Popup cards for a game's enemies, bosses, equipment and items. A page that
// includes a "fg-cards-data" tag (the game's data as JSON) gets every known
// name in its text turned into a button that opens a small card, in the
// field guide's window style, with a link to the full entry ("#find=Name",
// which fg-pages.js opens).
//
// The data tag holds {bestiary, equipment, items, magic, ip} in Lufia II's
// shapes (data/lufia-ii/*.yaml), and optionally "plain": names that stay
// plain text even though they contain a known name ("Winged Lion", a capsule
// monster form, isn't the Lion enemy). Names in bold stay plain when they're
// a label ("**Strong:**") or in BOLD_PLAIN ("**Flash**" is the capsule
// monster, not the spell). Rows that fg-pages.js builds later (an opened
// row's details) are linked through window.fgCards.link(node).
(function () {
  var tag = document.getElementById("fg-cards-data");
  var article = document.querySelector("article.md-content__inner");
  if (!tag || !article) return;
  var data = JSON.parse(tag.textContent);

  var ELEMENTS = {
    fire: "#ff6b4a", ice: "#7fdcff", thunder: "#ffe45c", water: "#4f9dff",
    wind: "#7cf0a2", earth: "#d9a066", light: "#fff3b0", shadow: "#9a7cff",
    dark: "#9a7cff", heal: "#7cf0a2"
  };
  // Names that read as ordinary words in the text; never linked.
  var STOP = ["Shadow", "Current", "Pot", "Statue", "Brave", "Master", "Cloth", "Shield"];
  // Longer phrases that contain a name but aren't it.
  var PLAIN = ["Flash, capsule monster", "Dragon Egg", "Dragon Eggs", "Dragon Egg Shrine", "Dragon Mountain", "Water Dragon", "Thunder Monster", "Ice Queen"];
  var BOLD_PLAIN = ["Flash", "Strong"];

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function fmt(n) { return typeof n === "number" ? n.toLocaleString("en-US") : n; }
  function plural(s) {
    if (/[^aeiou]y$/.test(s)) return s.slice(0, -1) + "ies";
    if (/(s|x|ch|sh)$/.test(s)) return s + "es";
    return s + "s";
  }
  function slug(s) {
    return s.toLowerCase().replace(/[:()'’]/g, "").trim().replace(/\s+/g, "-");
  }

  // Where each page lives: the game's tab window links to them.
  var pages = {};
  Array.prototype.forEach.call(document.querySelectorAll(".fg-tabs a"), function (a) {
    pages[a.textContent.trim().toLowerCase()] = a.getAttribute("href");
  });
  function pageLink(page, hash) {
    var href = pages[page];
    return href ? href.replace(/#.*$/, "") + "#" + hash : null;
  }

  // ---------- The catalog: name -> cards ----------

  var cards = {};
  var aliases = {};
  function card(name) {
    return cards[name] || (cards[name] = { name: name, enemy: null, areas: [], bosses: [], gear: null, item: null, spell: null, ip: null });
  }

  (data.bestiary && data.bestiary.areas || []).forEach(function (a) {
    (a.monsters || []).forEach(function (m) {
      var c = card(m.name);
      if (!c.enemy) c.enemy = m;
      if (c.areas.indexOf(a.area) < 0) c.areas.push(a.area);
    });
    (a.bosses || []).forEach(function (b) {
      // "Mummy x4", "Gades (Shuman)", "Goblin and Skeleton".
      var m = b.name.match(/^(.*?)(?: x(\d+))?(?: \((.*)\))?$/);
      m[1].split(" and ").forEach(function (base) {
        var c = card(base);
        c.bosses.push({ area: a.area, b: b, count: m[2], where: m[3] });
        if (m[2]) aliases[plural(base)] = base;
      });
    });
  });
  // The page spells her Danielle.
  if (cards.Daniele) aliases.Danielle = "Daniele";

  var GEAR = { weapons: "Weapon", armor: "Armor", shields: "Shield", helmets: "Helmet", rings: "Ring", jewels: "Rock or jewel" };
  Object.keys(data.equipment || {}).forEach(function (k) {
    (data.equipment[k] || []).forEach(function (e) {
      card(e.name).gear = { type: GEAR[k] || k, e: e };
    });
  });
  (data.items && data.items.groups || []).forEach(function (g) {
    g.items.forEach(function (it) { card(it.name).item = { type: g.type, note: g.note, it: it }; });
  });

  (data.magic && data.magic.groups || []).forEach(function (g) {
    g.spells.forEach(function (sp) { card(sp.name).spell = { type: g.type, s: sp }; });
  });
  var ipGear = {};
  Object.keys(data.equipment || {}).forEach(function (k) {
    (data.equipment[k] || []).forEach(function (e) {
      if (e.ip) (ipGear[e.ip] = ipGear[e.ip] || []).push(e.name);
    });
  });
  (data.ip && data.ip.groups || []).forEach(function (g) {
    g.ips.forEach(function (x) { card(x.name).ip = { type: g.type, x: x, gear: ipGear[x.name] || x.gear || [] }; });
  });

  // ---------- Finding names in the text ----------

  var plain = (data.plain || []).concat(PLAIN);
  var names = Object.keys(cards).concat(Object.keys(aliases), plain)
    .filter(function (n) { return STOP.indexOf(n) < 0; })
    .sort(function (a, b) { return b.length - a.length; });
  var source = "(?<![\\w'’-])(" + names.map(function (n) {
    // A space in a name matches a line break in the text too.
    return n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/ /g, "\\s+");
  }).join("|") + ")(?![\\w'’-])";
  var pattern = new RegExp(source, "g");
  var test = new RegExp(source);
  // Row heads are buttons; only their cells (an IP on an Equipment row) link.
  var SKIP = "a, code, pre, script, style, h1, h2, h4, h5, h6, th, dt, select, .fg-ctl, .fg-subtabs, .fg-tabs, " +
    ".fg-cardref, .fg-cardpop, .fg-gone, .fg-name, .fg-el, .fg-colhead, .fg-chnum";
  // Inside a card, its own name and headings stay plain; the rest links.
  var SKIP_IN_CARD = "a, button, dt, .fg-el, .fg-cardref, .fg-cardpop-name, .fg-cardpop-type, .fg-cardpop-where";
  function skip(node) {
    var p = node.parentElement;
    var inCard = p.closest(".fg-cardpop");
    if (inCard) return !!p.closest(SKIP_IN_CARD);
    if (p.closest(SKIP)) return true;
    if (p.closest("button") && !p.closest(".fg-head .fg-c")) return true;
    var b = p.closest("strong, b");
    if (b) {
      var t = b.textContent.trim();
      if (/:$/.test(t) || BOLD_PLAIN.indexOf(t) >= 0) return true;
    }
    return false;
  }

  function link(root, self) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        return skip(node) || !test.test(node.nodeValue)
          ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      var frag = document.createDocumentFragment();
      node.nodeValue.split(pattern).forEach(function (part, i) {
        var key = part.replace(/\s+/g, " ");
        if (i % 2 && plain.indexOf(key) >= 0) {
          frag.appendChild(document.createTextNode(part));
        } else if (i % 2) {
          // A span rather than a <button>, so long names wrap like text.
          var ref = document.createElement("span");
          ref.className = "fg-cardref";
          ref.textContent = part;
          ref.setAttribute("role", "button");
          ref.setAttribute("aria-haspopup", "dialog");
          ref.tabIndex = 0;
          ref.dataset.card = aliases[key] || key;
          // A card's own name in its text (Fireball's IP "casts Fireball").
          if (self && ref.dataset.card === self) { frag.appendChild(document.createTextNode(part)); return; }
          frag.appendChild(ref);
        } else if (part) {
          frag.appendChild(document.createTextNode(part));
        }
      });
      node.parentNode.replaceChild(frag, node);
    });
  }

  // ---------- The card ----------

  function els(list) {
    if (!list) return "—";
    return String(list).split(/\s*,\s*/).map(function (v) {
      var c = ELEMENTS[v.toLowerCase()];
      return '<span class="fg-el"' + (c ? ' style="--c:' + c + '"' : "") + ">" + (c ? "<i></i>" : "") + esc(v) + "</span>";
    }).join("");
  }
  function row(label, value) {
    return value == null || value === "" ? "" : "<dt>" + esc(label) + "</dt><dd>" + value + "</dd>";
  }
  function areaLink(area) {
    var href = pageLink("bestiary", slug(area));
    return href ? '<a href="' + esc(href) + '">' + esc(area) + "</a>" : esc(area);
  }
  function full(page, name) {
    var href = pageLink(page, "find=" + encodeURIComponent(name));
    return href ? '<p class="fg-cardpop-link"><a href="' + esc(href) + '">Full entry →</a></p>' : "";
  }

  function render(c) {
    var h = '<button type="button" class="fg-cardpop-close" aria-label="Close">✕</button>' +
      '<div class="fg-cardpop-name">' + esc(c.name) + "</div>";
    var parts = [];
    if (c.enemy) {
      var m = c.enemy;
      parts.push('<div class="fg-cardpop-type">Enemy</div>' +
        '<div class="fg-cardpop-stats">' +
        [["Level", m.level], ["HP", m.hp], ["EXP", m.exp], ["Gold", m.gold]].map(function (s) {
          return "<span><b>" + s[0] + "</b>" + esc(fmt(s[1])) + "</span>";
        }).join("") + "</div><dl>" +
        row("Drop", m.drop ? esc(m.drop) : "—") + row("Weak", els(m.weak)) + row("Strong", els(m.strong)) +
        row("Found in", c.areas.map(areaLink).join(", ")) + "</dl>" + full("bestiary", c.name));
    }
    if (c.bosses.length) {
      parts.push('<div class="fg-cardpop-type">Boss</div>' + c.bosses.map(function (x) {
        var b = x.b;
        return '<div class="fg-cardpop-fight"><div class="fg-cardpop-where">' + areaLink(x.area) +
          (x.where ? " · " + esc(x.where) : "") + (x.count ? " · " + x.count + " of them" : "") + "</div><dl>" +
          row("HP", esc(fmt(b.hp)) + (x.count ? " each" : "")) +
          (b.weak ? row("Weak", els(b.weak)) : "") + (b.strong ? row("Strong", els(b.strong)) : "") +
          (b.drop ? row("Drop", esc(b.drop)) : "") + (b.note ? row("Note", esc(b.note)) : "") + "</dl></div>";
      }).join("") + (c.enemy ? "" : full("bestiary", c.name)));
    }
    if (c.gear) {
      var e = c.gear.e;
      parts.push('<div class="fg-cardpop-type">' + esc(c.gear.type) + "</div>" +
        (e.stats ? '<div class="fg-cardpop-stats"><span>' + esc(e.stats) + "</span></div>" : "") + "<dl>" +
        row("IP", e.ip ? esc(e.ip) : "") + row("Price", e.price ? esc(e.price) : "") +
        row("Who", e.who ? esc(e.who) : "") + row("Where", e.where ? esc(e.where) : "") + "</dl>" +
        full("equipment", c.name));
    }
    if (c.spell) {
      var sp = c.spell.s;
      parts.push('<div class="fg-cardpop-type">Spell · ' + esc(c.spell.type) + "</div>" +
        '<div class="fg-cardpop-stats"><span><b>MP</b>' + esc(sp.mp) + "</span><span><b>Price</b>" + esc(sp.price) + "</span></div><dl>" +
        (sp.element ? row("Element", els(sp.element)) : "") + row("Effect", esc(sp.effect)) +
        row("Who", esc(sp.who)) + row("Where", esc(sp.where)) + "</dl>" + full("magic", c.name));
    }
    if (c.ip) {
      var x = c.ip.x;
      parts.push('<div class="fg-cardpop-type">IP attack · ' + esc(c.ip.type) + "</div><dl>" +
        (x.element ? row("Element", els(x.element)) : "") + row("Effect", esc(x.effect)) +
        row("Gear", esc(c.ip.gear.join(", ") || "—")) + "</dl>" + full("ip attacks", c.name));
    }
    if (c.item) {
      var it = c.item.it;
      parts.push('<div class="fg-cardpop-type">' + esc(c.item.type) + "</div><dl>" +
        row("Effect", esc(it.effect)) + row("Price", esc(it.price)) + row("First", esc(it.first)) + "</dl>" +
        (c.item.note ? '<p class="fg-cardpop-note">' + esc(c.item.note) + "</p>" : "") +
        full("items", c.name));
    }
    return h + parts.join('<hr class="fg-cardpop-sep">');
  }

  var pop = document.createElement("div");
  pop.className = "fg-cardpop md-typeset";
  pop.hidden = true;
  pop.setAttribute("role", "dialog");
  document.body.appendChild(pop);
  var openFor = null;

  // The names shown in the window, in order; "Back" returns to the last.
  var trail = [];
  function fill(name) {
    var c = cards[name];
    pop.innerHTML = (trail.length > 1 ? '<button type="button" class="fg-cardpop-back">← ' + esc(trail[trail.length - 2]) + "</button>" : "") +
      render(c);
    pop.setAttribute("aria-label", c.name);
    pop.querySelector(".fg-cardpop-close").addEventListener("click", function () { hide().focus(); });
    var back = pop.querySelector(".fg-cardpop-back");
    if (back) back.addEventListener("click", function (e) {
      e.stopPropagation();
      trail.pop();
      fill(trail[trail.length - 1]);
    });
    // Names in the card open their own card in this window.
    link(pop, c.name);
    pop.scrollTop = 0;
  }

  function show(ref) {
    if (!cards[ref.dataset.card]) return;
    if (pop.contains(ref)) {
      trail.push(ref.dataset.card);
      fill(ref.dataset.card);
      return;
    }
    trail = [ref.dataset.card];
    fill(ref.dataset.card);
    pop.hidden = false;
    openFor = ref;
    var r = ref.getBoundingClientRect();
    var vw = document.documentElement.clientWidth;
    var left = Math.max(8, Math.min(r.left, vw - pop.offsetWidth - 8));
    var top = r.bottom + 6;
    // Above the name if it doesn't fit below.
    if (top + pop.offsetHeight > window.innerHeight - 8 && r.top - pop.offsetHeight - 6 > 8) top = r.top - pop.offsetHeight - 6;
    pop.style.left = left + window.scrollX + "px";
    pop.style.top = top + window.scrollY + "px";
  }
  function hide() {
    var ref = openFor;
    pop.hidden = true;
    openFor = null;
    return ref;
  }

  // Capture, so a name inside a row's head opens its card without also
  // opening the row.
  document.addEventListener("click", function (e) {
    var ref = e.target.closest(".fg-cardref");
    if (!ref) return;
    e.stopPropagation();
    e.preventDefault();
    if (openFor === ref) hide(); else show(ref);
  }, true);
  // Clicks inside the window (Back, a link) don't count as clicking away.
  document.addEventListener("click", function (e) {
    if (openFor && !pop.contains(e.target)) hide();
    // Following a link inside the card closes it.
    if (openFor && e.target.closest(".fg-cardpop a")) hide();
  });
  document.addEventListener("keydown", function (e) {
    var ref = e.target.closest && e.target.closest(".fg-cardref");
    if (ref && (e.key === "Enter" || e.key === " ")) {
      e.preventDefault();
      if (openFor === ref) hide(); else show(ref);
    } else if (e.key === "Escape" && openFor) {
      hide().focus();
    }
  });

  window.fgCards = { link: link };
  link(article);
  // List rows not on the page right now (filtered out, or on another sub-tab).
  (window.fgPageRows || []).forEach(function (r) { if (!article.contains(r)) link(r); });
})();
