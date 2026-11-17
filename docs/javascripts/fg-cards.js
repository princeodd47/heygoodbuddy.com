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
    dark: "#9a7cff", heal: "#7cf0a2", lightning: "#ffe45c", holy: "#ffffff", poison: "#c78bff"
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
    return cards[name] || (cards[name] = { name: name, enemy: null, areas: [], bosses: [], gear: null, item: null, spell: null, ip: null, extra: [] });
  }
  // A plural ("Goblins", "Dark Elves") opens the one-name card.
  function plurals(name) {
    aliases[plural(name)] = name;
    if (/f$/.test(name)) aliases[name.slice(0, -1) + "ves"] = name;
  }

  // Other games' data, turned into generic card sections:
  //   {type, page, find, stats: [[label, value]], rows: [[label, value]],
  //    blocks: [{where: [{label, title, count}], stats, rows}], note}
  // A row value is text, or {el: "Fire, Ice"} for element tags.
  var ADAPTERS = {};
  ADAPTERS["shining-force"] = function (d) {
    (d.bestiary && d.bestiary.battles || []).forEach(function (b) {
      var title = "Battle " + b.number + ": " + b.name;
      [["Enemy", b.enemies || []], ["Boss", b.bosses || []]].forEach(function (p) {
        p[1].forEach(function (e) {
          // "Colossus x3", "Skeleton (stronger)", "Dark Dragon (3 heads)".
          var m = e.name.match(/^(.*?)(?: x(\d+))?(?: \((.*)\))?$/);
          var c = card(m[1]);
          plurals(m[1]);
          var sec = c.extra.filter(function (x) { return x.type === p[0]; })[0];
          if (!sec) c.extra.push(sec = { type: p[0], page: "bestiary", find: e.name, blocks: [] });
          var stats = [["HP", e.hp], ["ATT", e.atk], ["DEF", e.def], ["AGI", e.agi], ["MOV", e.mov]];
          var rows = [["Wields", e.weapon], ["Spells", e.spells], ["Note", (m[3] ? m[3] + ". " : "") + (e.note || "")]];
          var sig = JSON.stringify([stats, rows]);
          var blk = sec.blocks.filter(function (x) { return x.sig === sig; })[0];
          if (!blk) sec.blocks.push(blk = { sig: sig, where: [], stats: stats, rows: rows });
          blk.where.push({ label: "Battle " + b.number, title: title, count: m[2] ? +m[2] : e.count });
        });
      });
    });
    var eq = d.equipment || {};
    (eq.weapons || []).forEach(function (g) {
      g.items.forEach(function (e) {
        card(e.name).extra.push({ type: "Weapon · " + g.type, page: "equipment",
          stats: [["ATT", "+" + e.atk]], rows: [["Price", e.price], ["Who", e.who], ["Where", e.where]] });
      });
    });
    (eq.rings || []).forEach(function (e) {
      card(e.name).extra.push({ type: "Ring", page: "equipment",
        rows: [["Equipped", e.effect], ["Use", e.use], ["Who", e.who], ["Where", e.where]] });
    });
    (d.items && d.items.groups || []).forEach(function (g) {
      g.items.forEach(function (it) {
        card(it.name).extra.push({ type: g.type, page: "items", note: g.note,
          rows: [["Effect", it.effect], ["Price", it.price], ["Where", it.where]] });
      });
    });
  };
  ADAPTERS["treasure-of-the-rudras"] = function (d) {
    // A block per set of stats; "where" lists every place with those stats.
    function add(name, type, title, label, stats, rows) {
      var m = name.match(/^(.*?)(?: \((.*)\))?$/);
      var c = card(m[1]);
      if (/[^s]$/.test(m[1])) plurals(m[1]);
      var sec = c.extra.filter(function (x) { return x.type === type; })[0];
      if (!sec) c.extra.push(sec = { type: type, page: "bestiary", find: name, blocks: [] });
      if (m[2]) rows = [["Form", m[2]]].concat(rows);
      var sig = JSON.stringify([stats, rows]);
      var blk = sec.blocks.filter(function (x) { return x.sig === sig; })[0];
      if (!blk) sec.blocks.push(blk = { sig: sig, where: [], stats: stats, rows: rows });
      blk.where.push({ label: label, title: title });
    }
    (d.monsters && d.monsters.areas || []).forEach(function (a) {
      a.monsters.forEach(function (m) {
        add(m.name, "Enemy", a.area, a.area,
          [["Level", m.level], ["HP", m.hp], ["EXP", m.exp], ["Ragu", m.ragu]],
          [["Weak", m.weak ? { el: m.weak } : ""], ["Drops", m.drops], ["Note", m.note]]);
      });
    });
    (d.bosses && d.bosses.chapters || []).forEach(function (ch) {
      ch.bosses.forEach(function (b) {
        add(b.name, "Boss", ch.name, ch.name + (b.day != null ? " · Day " + b.day : "") + " · " + b.where,
          [["HP", b.hp]],
          [["Weak", b.weak ? { el: b.weak } : ""], ["Drops", b.drops], ["Note", b.note]]);
      });
    });
    var eq = d.equipment || {};
    (eq.weapons || []).forEach(function (g) {
      g.items.forEach(function (e) {
        card(e.name).extra.push({ type: "Weapon · " + g.type, page: "equipment",
          stats: [["Attack", e.atk], ["MDef", e.mdef]],
          rows: [["Element", e.elem ? { el: e.elem } : ""], ["Notes", e.notes], ["Sells", e.sell], ["Where", e.where]] });
      });
    });
    (eq.armor || []).forEach(function (g) {
      g.items.forEach(function (e) {
        card(e.name).extra.push({ type: "Armor · " + g.type, page: "equipment",
          stats: [["Def", e.def], ["MDef", e.mdef || 0]],
          rows: [["Element", e.elem ? { el: e.elem } : ""], ["Notes", e.notes], ["Buys", e.buy], ["Sells", e.sell], ["Where", e.where]] });
      });
    });
  };
  ADAPTERS["final-fantasy-x-2"] = function (d) {
    function txt(v) { return v ? { md: v } : ""; }
    (d.bestiary && d.bestiary.enemies || []).forEach(function (e) {
      card(e.name).extra.push({ type: "Enemy", page: "bestiary",
        stats: [["Lv", e.level], ["HP", e.hp]],
        rows: [["Weak", e.weak ? { el: e.weak } : ""], ["Other", e.other], ["Steal", e.steal], ["Drop", e.drop],
          ["Bribe", e.bribe], ["Where", txt(e.where)]] });
    });
    (d.creatures && d.creatures.creatures || []).forEach(function (c) {
      card(c.name).extra.push({ type: "Creature · Size " + c.size, page: "creatures", rows: [["Trap it", txt(c.where)]] });
    });
    (d.accessories && d.accessories.categories || []).forEach(function (g) {
      g.accessories.forEach(function (a) {
        card(a.name).extra.push({ type: "Accessory · " + g.name, page: "accessories",
          rows: [["Effect", a.effect], ["Feed", a.feed], ["Sell", a.sell], ["Where", txt(a.where)]] });
      });
    });
    (d.grids && d.grids.grids || []).forEach(function (g) {
      card(g.name).extra.push({ type: "Garment Grid", page: "garment grids",
        rows: [["Equipped", g.equip], ["Gates", txt(g.gates)], ["Creature", g.creature], ["Chapter", g.chapter], ["Where", txt(g.where)]] });
    });
    (d.dresspheres && d.dresspheres.dresspheres || []).forEach(function (x) {
      card(x.name).extra.push({ type: "Dressphere", page: "dresspheres", hash: slug(x.name), rows: [["How", txt(x.how)]] });
    });
    (d.feeding && d.feeding.items || []).forEach(function (i) {
      card(i.name).extra.push({ type: "Item", page: "feeding",
        rows: [["Feed", i.qty ? i.qty + " to teach " + (i.teaches || "—") : ""], ["Type", i.type], ["Stat gain", i.gain]] });
    });
  };
  ADAPTERS["final-fantasy-xii-the-zodiac-age"] = function (d) {
    var bz = d.bazaar || {};
    [["Repeatable bundle", bz.repeatable || []], ["Bazaar bundle", bz.bundles || []]].forEach(function (p) {
      p[1].forEach(function (b) {
        card(b.name).extra.push({ type: p[0], page: "bazaar", hash: b.id,
          rows: [["Loot to sell", b.loot], ["Contains", b.contains], ["Gil", b.price]] });
      });
    });
    (d.monographs && d.monographs.monographs || []).forEach(function (m) {
      card(m.name).extra.push({ type: "Monograph", page: "monographs", hash: m.id,
        rows: [["Enemies", m.enemies], ["Price", m.price], ["Unlock", m.unlock]] });
    });
  };
  // "[Visions](visions.md)" links in data text read as their words.
  function unlink(t) { return t ? String(t).replace(/\[([^\]]+)\]\([^)]+\)/g, "$1") : t; }
  ADAPTERS["final-fantasy-resonance"] = function (d) {
    function txt(v) { return v ? { md: unlink(v) } : ""; }
    function el(v) { return v ? { el: v } : ""; }
    (d.bestiary && d.bestiary.bestiary || []).forEach(function (a) {
      a.enemies.forEach(function (e) {
        var c = card(e.name);
        var sec = c.extra.filter(function (x) { return x.type === "Enemy"; })[0];
        if (!sec) c.extra.push(sec = { type: "Enemy", page: "bestiary", blocks: [] });
        var stats = [["Level", e.level]];
        var rows = [["Weak", el(e.weak)], ["Resists", el(e.resist)], ["Drops", e.drops], ["Steals", e.steals]];
        var sig = JSON.stringify([stats, rows]);
        var blk = sec.blocks.filter(function (x) { return x.sig === sig; })[0];
        if (!blk) sec.blocks.push(blk = { sig: sig, where: [], stats: stats, rows: rows });
        blk.where.push({ label: e.where && e.where !== a.area ? a.area + " · " + e.where : a.area, title: a.area });
      });
    });
    var eq = d.equipment || {};
    (eq.weapons || []).forEach(function (g) {
      g.entries.forEach(function (e) {
        card(e.name).extra.push({ type: g.type + (g.who ? " · " + g.who : ""), page: "equipment",
          stats: [["Atk", e.atk], ["Mag", e.mag]],
          rows: [["Other", e.other], ["Effect", e.effect], ["Where", txt(e.where)]] });
      });
    });
    (eq.armor || []).forEach(function (g) {
      g.entries.forEach(function (e) {
        card(e.name).extra.push({ type: g.type + (g.who ? " · " + g.who : ""), page: "equipment",
          stats: [["Def", e.def], ["M.Def", e.mdef]],
          rows: [["Other", e.other], ["Effect", e.effect], ["Where", txt(e.where)]] });
      });
    });
    (eq.accessories || []).forEach(function (e) {
      card(e.name).extra.push({ type: "Accessory", page: "accessories",
        rows: [["Stats", e.other], ["Effect", e.effect], ["Where", txt(e.where)]] });
    });
    (d.items && d.items.groups || []).forEach(function (g) {
      g.entries.forEach(function (e) {
        card(e.name).extra.push({ type: "Item · " + g.group, page: "items",
          rows: [["Effect", e.effect], ["Buy", txt(e.buy)], ["Found", txt(e.found)]] });
      });
    });
    var ki = d.key_items || {};
    [["Key item", ki.key_items || []], ["Artifact", ki.artifacts || []]].forEach(function (p) {
      p[1].forEach(function (e) {
        card(e.name).extra.push({ type: p[0], page: "key items",
          rows: [["What", unlink(e.what)], ["Where", txt(e.where)]] });
      });
    });
    (d.visions && d.visions.visions || []).forEach(function (v) {
      card(v.name).extra.push({ type: "Vision", page: "visions", hash: "where-to-get-visions",
        rows: [["How to get", txt(v.how_to_get)]] });
    });
  };
  ADAPTERS["unicorn-overlord"] = function (d) {
    (d.equipment && d.equipment.groups || []).forEach(function (g) {
      g.entries.forEach(function (e) {
        var rows = [["Effects", (e.effects || []).join(" · ")]];
        if (e.skill) rows.push(["Skill", e.skill.name + (e.skill.details ? " (" + e.skill.details + ")" : "") + (e.skill.text ? ": " + e.skill.text : "")]);
        rows.push(["Price", e.price], ["Where", (e.where || []).join(" · ")]);
        card(e.name).extra.push({ type: g.type.replace(/ves$/, "ff").replace(/ies$/, "y").replace(/s$/, ""),
          page: "equipment", stats: (e.stats || "").split(/\s*·\s*/).filter(Boolean).map(function (x) {
            var m = x.match(/^(.*?)\s+(\S+)$/);
            return m ? [m[1], m[2]] : [x, ""];
          }), rows: rows });
      });
    });
  };
  ADAPTERS["dragon-quest-monsters-the-withered-world"] = function (d) {
    var talents = {};
    (d.talents && d.talents.talents || []).forEach(function (t) {
      talents[t.id] = t.name;
      card(t.name).extra.push({ type: "Talent", page: "talents", hash: t.id,
        rows: t.tree.map(function (r) { return [r.points + " pts", r.name]; }) });
    });
    (d.monsters && d.monsters.monsters || []).forEach(function (m) {
      card(m.name).extra.push({ type: "Monster · " + m.family + " · Rank " + m.rank, page: "monsters", hash: m.id,
        rows: [["Talents", (m.talents || []).map(function (t) { return talents[t] || t; }).join(", ")], ["Where", m.where]] });
    });
    (d.items && d.items.items || []).forEach(function (i) {
      card(i.name).extra.push({ type: "Item · " + i.type, page: "items", hash: i.id,
        rows: [["Effect", i.description], ["Where", i.where]] });
    });
  };
  if (data.game && ADAPTERS[data.game]) ADAPTERS[data.game](data);

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
    .filter(function (n) {
      // A plural of a stopped name ("Rudras") is stopped too.
      var stop = STOP.concat(data.stop || []);
      return stop.indexOf(n) < 0 && stop.indexOf(aliases[n]) < 0;
    })
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

  // Data text with <br> line breaks and *italic* labels ("*Chest:* Luca").
  function md(t) {
    return esc(t).replace(/&lt;br&gt;/g, "<br>").replace(/\*([^*]+)\*/g, "<em>$1</em>");
  }
  function statLine(list) {
    list = (list || []).filter(function (s) { return s[1] != null && s[1] !== ""; });
    return list.length ? '<div class="fg-cardpop-stats">' + list.map(function (s) {
      return "<span><b>" + esc(s[0]) + "</b>" + esc(fmt(s[1])) + "</span>";
    }).join("") + "</div>" : "";
  }
  function rowList(list) {
    var h = (list || []).map(function (r) {
      var v = r[1];
      if (v == null || v === "" || v === "—") return "";
      return row(r[0], typeof v === "object" ? (v.el ? els(v.el) : md(v.md)) : esc(v));
    }).join("");
    return h ? "<dl>" + h + "</dl>" : "";
  }
  function section(c, x) {
    var h = '<div class="fg-cardpop-type">' + esc(x.type) + "</div>" + statLine(x.stats);
    (x.blocks || []).forEach(function (b) {
      h += '<div class="fg-cardpop-fight"><div class="fg-cardpop-where">' + b.where.map(function (w) {
        var href = pageLink(x.page, slug(w.title));
        var t = esc(w.label) + (w.count > 1 ? " ×" + w.count : "");
        return href ? '<a href="' + esc(href) + '" title="' + esc(w.title) + '">' + t + "</a>" : t;
      }).join(", ") + "</div>" + statLine(b.stats) + rowList(b.rows) + "</div>";
    });
    h += rowList(x.rows);
    if (x.note) h += '<p class="fg-cardpop-note">' + esc(x.note) + "</p>";
    if (x.hash) {
      var hh = pageLink(x.page, x.hash);
      return h + (hh ? '<p class="fg-cardpop-link"><a href="' + esc(hh) + '">Full entry →</a></p>' : "");
    }
    return h + full(x.page, x.find || c.name);
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
    c.extra.forEach(function (x) { parts.push(section(c, x)); });
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
