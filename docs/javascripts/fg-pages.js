// Field guide page tools, like the FF6 Advance guide. A page turns them on in
// its front matter, under "fg" (overrides/main.html passes it here as JSON):
//
//   fg:
//     subtabs: true      Each "##" section becomes a sub-tab; one shows at a
//                        time. "Sources" always shows, at the end.
//     chapters: true     Each "##" section becomes a numbered row that opens
//                        (walkthroughs), with a search box. "### Boss: X"
//                        headings show as tags.
//     list:              The page's tables become rows that open, under one
//                        window of controls.
//       merge: true      All tables make one list; each "##" heading is the
//                        row's group (an area), and identical rows are listed
//                        once with every group they appear in.
//       group: Area      What a group is called (a dropdown filters by it).
//       show: [Level, HP]  Columns shown on the row; the rest show when it
//                        opens. A table's first column is the row's name.
//       sort: [Level, -HP] Sort choices; "-" sorts highest first.
//       chips: Weak      A column whose comma-separated values become
//                        filter chips (any pressed chip matches).
//       chip_values: [..]  Chip order and set (default: every value found).
//       aliases: {All: [..]}  A cell value standing for several chips.
//       chips_label: ..  The chips' label (default: the column's name).
//       chips_style: elements  Show the column as element tags with dots.
//       elements: [Strong]  Other columns shown as element tags.
//       show_in: {Rings: [Use]}  Columns for one section's list instead of
//                        "show" (a list shows the "show" columns it has).
//       group_in: {Bosses: Chapter}  A section's own name for its groups.
//       drop: ["#"]      Columns left out (a per-battle count, so the same
//                        enemy in several battles merges into one row).
//       sections: [Items]  Only these "##" sections' tables become lists
//                        (default: every section with a table).
//
// Without merge, a section's tables that share the first one's columns make
// one list; a "###" heading above a table is its rows' group (a dropdown when
// "group" is set). A table before the first "##" makes a list of its own.
//
// With merge, a section's text (a battle's win condition) shows above the
// list when its group is picked.
//       placeholder: ..  The search box's hint.
//
// The tables and text stay in the page, so site search still finds them and
// the page reads fine without this script.
(function () {
  var spec = document.getElementById("fg-page-spec");
  if (!spec) return;
  var fg = JSON.parse(spec.textContent || "null");
  if (!fg) return;
  var article = document.querySelector("article.md-content__inner");
  if (!article) return;

  var ELEMENTS = {
    fire: "#ff6b4a", ice: "#7fdcff", thunder: "#ffe45c", lightning: "#ffe45c",
    water: "#4f9dff", wind: "#7cf0a2", earth: "#d9a066", poison: "#c78bff",
    holy: "#ffffff", light: "#fff3b0", shadow: "#9a7cff", dark: "#9a7cff",
    heal: "#7cf0a2"
  };

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function text(node) { return (node.textContent || "").replace(/\s+/g, " ").trim(); }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function plural(s) {
    if (/[^aeiou]y$/i.test(s)) return s.slice(0, -1) + "ies";
    if (/(s|x|ch|sh)$/i.test(s)) return s + "es";
    return s + "s";
  }
  function num(s) {
    var m = String(s).replace(/,/g, "").match(/-?\d+(\.\d+)?/);
    return m ? parseFloat(m[0]) : null;
  }
  function split(s) {
    return String(s).split(/\s*,\s*/).filter(function (v) { return v && v !== "—"; });
  }
  function elChip(v, cls) {
    var c = ELEMENTS[v.toLowerCase()];
    return '<span class="fg-el' + (cls ? " " + cls : "") + '"' + (c ? ' style="--c:' + c + '"' : "") + ">" +
      (c ? "<i></i>" : "") + esc(v) + "</span>";
  }

  // ---------- Sections: each h2 and what follows it, up to the next h2 ----------

  function sections() {
    var out = [], cur = null;
    Array.prototype.slice.call(article.children).forEach(function (n) {
      if (n.tagName === "H2") {
        cur = { h2: n, id: n.id, title: text(n).replace(/¶$/, "").trim(), nodes: [] };
        out.push(cur);
      } else if (cur) {
        cur.nodes.push(n);
      }
    });
    out.forEach(function (s) {
      var box = el("section", "fg-sec");
      box.dataset.id = s.id;
      s.h2.parentNode.insertBefore(box, s.h2);
      box.appendChild(s.h2);
      s.nodes.forEach(function (n) { box.appendChild(n); });
      s.box = box;
      s.sources = /^sources$/i.test(s.title);
    });
    return out;
  }

  // Where tools go: after the h1 and the intro text, before the first section.
  function insertTop(node, secs) {
    var first = secs.length ? secs[0].box : null;
    if (first) article.insertBefore(node, first); else article.appendChild(node);
  }

  function title(s) {
    var h = s.h2.cloneNode(true);
    var a = h.querySelector(".headerlink");
    if (a) a.remove();
    return text(h);
  }

  // ---------- Hash links: open whatever holds the linked element ----------

  var openers = [];
  function follow(scroll) {
    var id = decodeURIComponent((location.hash || "").slice(1));
    if (!id) return false;
    for (var i = 0; i < openers.length; i++) {
      if (openers[i](id, scroll)) return true;
    }
    return false;
  }
  window.addEventListener("hashchange", function () { follow(true); });

  // ---------- Lists: tables to rows that open ----------

  function buildList(cfg, secs) {
    cfg = cfg || {};
    var show = cfg.show || [];
    var sorts = (cfg.sort || []).map(function (s) {
      return { col: s.replace(/^-/, ""), desc: s.charAt(0) === "-" };
    });
    var aliases = cfg.aliases || {};
    var drop = cfg.drop || [];
    var lists = [];
    var labels = {};
    function label(col) { return labels[col] || col; }

    function rowsOf(table, group) {
      var heads = [];
      // Two columns with the same name ("Parent", "Parent") stay apart.
      Array.prototype.forEach.call(table.querySelectorAll("thead th"), function (th) {
        var h = text(th) || "—", n = 2, k = h;
        while (heads.indexOf(k) >= 0) k = h + " " + n++;
        if (k !== h) {
          // Named after the column it follows: "MP (earlier on)".
          var ctx = null;
          for (var j = heads.length - 1; j > heads.indexOf(h); j--) {
            if (!labels[heads[j]]) { ctx = heads[j]; break; }
          }
          labels[k] = ctx ? h + " (" + ctx.toLowerCase() + ")" : h;
        }
        heads.push(k);
      });
      var kind = heads[0];
      return Array.prototype.map.call(table.querySelectorAll("tbody tr"), function (tr) {
        var cells = {};
        var tds = tr.children;
        heads.forEach(function (h, i) {
          if (i && tds[i] && drop.indexOf(h) < 0) cells[h] = { html: tds[i].innerHTML, text: text(tds[i]) };
        });
        return {
          kind: kind, heads: heads.filter(function (h) { return drop.indexOf(h) < 0; }),
          // Anchors in the name cell stay in the (hidden) table; the row
          // remembers them so links to them open it.
          name: tds[0] ? tds[0].innerHTML.replace(/<(a|span)\b[^>]*\sid="[^"]*"[^>]*><\/\1>/g, "") : "", nameText: tds[0] ? text(tds[0]) : "",
          anchors: tds[0] ? Array.prototype.map.call(tds[0].querySelectorAll("[id]"), function (a) { return a.id; }) : [],
          // The bold name alone, without a note in the same cell.
          key: tds[0] ? text(tds[0].querySelector("strong") || tds[0]).toLowerCase() : "",
          cells: cells, groups: group ? [group] : []
        };
      });
    }

    // One list per section (with sub-tabs), or one for the page (merge).
    if (cfg.merge) {
      var all = [], seen = {}, groups = [];
      secs.forEach(function (s) {
        if (s.sources) return;
        var tables = s.box.querySelectorAll("table");
        if (!tables.length) return;
        var note = Array.prototype.filter.call(s.box.children, function (n) {
          return n !== s.h2 && !n.querySelector("table") && n.tagName !== "TABLE";
        }).map(function (n) { return n.outerHTML; }).join("");
        groups.push({ id: s.id, title: title(s), note: note });
        Array.prototype.forEach.call(tables, function (t) {
          rowsOf(t, title(s)).forEach(function (r) {
            var key = r.kind + "|" + r.nameText + "|" + r.heads.slice(1).map(function (h) {
              return r.cells[h] ? r.cells[h].text : "";
            }).join("|");
            if (seen[key]) seen[key].groups.push(r.groups[0]);
            else { seen[key] = r; all.push(r); }
          });
        });
        s.box.hidden = true;
        s.box.classList.add("fg-gone");
      });
      var box = el("div", "fg-listbox");
      var src = secs.filter(function (s) { return s.sources; })[0];
      if (src) article.insertBefore(box, src.box); else article.appendChild(box);
      lists.push({ rows: all, box: box, groups: groups });
    } else {
      var only = cfg.sections ? cfg.sections.map(function (x) { return x.toLowerCase(); }) : null;
      var headsOf = function (t) {
        return Array.prototype.map.call(t.querySelectorAll("thead th"), text).join("|");
      };
      // The "###" heading a table sits under, if any (and whether only the
      // table follows it, so the heading can go with the table).
      // The "###" heading a table sits under, and the text around the table
      // up to the next heading or table (it moves into the list with it).
      var isTable = function (n) { return n.tagName === "TABLE" || (n.classList && n.classList.contains("md-typeset__scrollwrap")); };
      var h3Of = function (wrap) {
        var n = wrap.previousElementSibling, text = [];
        while (n && n.tagName !== "H3" && n.tagName !== "H2" && !isTable(n)) { text.unshift(n); n = n.previousElementSibling; }
        if (!n || n.tagName !== "H3") return null;
        n2 = wrap.nextElementSibling;
        while (n2 && !/^H[1-3]$/.test(n2.tagName) && !isTable(n2)) { text.push(n2); n2 = n2.nextElementSibling; }
        return { h3: n, text: text };
      };
      var n2;
      var addList = function (tables, sec) {
        // The theme wraps tables for scrolling; hide the outermost wrapper.
        var wraps = tables.map(function (t) { return t.closest(".md-typeset__scrollwrap") || t; });
        // Each table's heading, found before the list box goes in.
        var heads = wraps.map(function (w) { return tables.length > 1 ? h3Of(w) : null; });
        var box = el("div", "fg-listbox");
        wraps[0].parentNode.insertBefore(box, wraps[0]);
        var rows = [], groups = [];
        tables.forEach(function (t, ti) {
          var wrap = wraps[ti];
          var h = heads[ti];
          var g = h ? title({ h2: h.h3 }) : null;
          if (g && !groups.some(function (x) { return x.title === g; })) {
            groups.push({ id: h.h3.id, title: g, text: h.text.map(function (n) { return n.outerHTML; }).join("") });
          }
          rows = rows.concat(rowsOf(t, g));
          wrap.classList.add("fg-gone");
          if (h) {
            h.h3.classList.add("fg-gone");
            h.text.forEach(function (n) { n.classList.add("fg-gone"); });
          }
        });
        lists.push({ rows: rows, box: box, sec: sec, groups: groups });
      };
      secs.forEach(function (s) {
        if (s.sources) return;
        if (only && only.indexOf(title(s).toLowerCase()) < 0) return;
        var tables = Array.prototype.slice.call(s.box.querySelectorAll("table"));
        if (!tables.length) return;
        var k = headsOf(tables[0]);
        addList(tables.filter(function (t) { return headsOf(t) === k; }), s);
      });
      // A table before the first section (a page that's one big table).
      if (!only) {
        var loose = Array.prototype.filter.call(article.querySelectorAll("table"), function (t) {
          return !t.closest(".fg-sec") && !t.closest(".fg-gone");
        });
        if (loose.length) addList([loose[0]], null);
      }
    }
    if (!lists.length) return null;

    // A column is a number column if every value in it is a number or "—".
    var numCols = {};
    lists.forEach(function (L) {
      var heads = L.rows.length ? L.rows[0].heads : [];
      var own = L.sec && cfg.show_in && cfg.show_in[title(L.sec)];
      L.show = (own || show).filter(function (col) { return heads.indexOf(col) >= 0; });
      // Nothing to show from the list: its next two columns.
      if (!L.show.length && !own) L.show = heads.slice(1, 3);
    });
    var allShown = [];
    lists.forEach(function (L) { L.show.forEach(function (c) { if (allShown.indexOf(c) < 0) allShown.push(c); }); });
    allShown.forEach(function (col) {
      var any = false, all = true;
      lists.forEach(function (L) {
        L.rows.forEach(function (r) {
          var c = r.cells[col];
          if (!c || c.text === "—" || c.text === "") return;
          // A number, optionally with a note: "2,000 (casino)".
          if (/^[\d,.\s%()+–-]+$/.test(c.text) || /^[\d,.]+\s*\([^)]{1,20}\)$/.test(c.text)) any = true; else all = false;
        });
      });
      numCols[col] = any && all;
    });

    lists.forEach(function (L) {
      L.rows.forEach(function (r, i) { r.order = i; });
      L.kinds = [];
      L.rows.forEach(function (r) { if (L.kinds.indexOf(r.kind) < 0) L.kinds.push(r.kind); });
    });

    // Chip values, in the given order or as found.
    var chipVals = cfg.chip_values ? cfg.chip_values.slice() : [];
    if (cfg.chips && !cfg.chip_values) {
      lists.forEach(function (L) {
        L.rows.forEach(function (r) {
          var c = r.cells[cfg.chips];
          if (c) split(c.text).forEach(function (v) {
            if (!aliases[v] && chipVals.indexOf(v) < 0) chipVals.push(v);
          });
        });
      });
    }
    function chipsOf(r) {
      var c = r.cells[cfg.chips];
      var out = [];
      if (c) split(c.text).forEach(function (v) {
        (aliases[v] || [v]).forEach(function (x) { if (out.indexOf(x) < 0) out.push(x); });
      });
      return out;
    }

    // ---- The controls window ----
    var state = { q: "", sort: "", kind: "", group: "", chips: [] };
    var ctl = el("div", "fg-ctl");
    var html = '<div class="fg-grp fg-grow"><label class="fg-lbl">Search</label>' +
      '<input type="search" placeholder="' + esc(cfg.placeholder || "Name") + '" aria-label="Search this list"></div>';
    if (sorts.length) {
      html += '<div class="fg-grp"><label class="fg-lbl">Sort</label><select data-k="sort">' +
        '<option value="">Story order</option>' +
        sorts.map(function (s, i) {
          return '<option value="' + i + '">' + esc(s.col) + (s.desc ? ", highest" : ", lowest") + "</option>";
        }).join("") + "</select></div>";
    }
    var kinds = lists[0].kinds;
    if (cfg.merge && kinds.length > 1) {
      html += '<div class="fg-grp"><label class="fg-lbl">Show</label><select data-k="kind">' +
        '<option value="">All</option>' +
        kinds.map(function (k) { return '<option value="' + esc(k) + '">' + esc(plural(k)) + "</option>"; }).join("") +
        "</select></div>";
    }
    if (cfg.group) {
      // Filled in by draw() with the groups of the list on show.
      html += '<div class="fg-grp" data-groups><label class="fg-lbl">' + esc(cfg.group) + '</label><select data-k="group">' +
        "</select></div>";
    }
    if (cfg.chips) {
      html += '<div class="fg-chips-row"><span class="fg-lbl">' + esc(cfg.chips_label || cfg.chips) + '</span><div class="fg-chips">' +
        chipVals.map(function (v) {
          var c = ELEMENTS[v.toLowerCase()];
          return '<button type="button" class="fg-chip" aria-pressed="false" data-v="' + esc(v) + '">' +
            (c ? '<i style="background:' + c + '"></i>' : "") + esc(v) + "</button>";
        }).join("") + "</div></div>";
    }
    ctl.innerHTML = html;
    ctl.className = "fg-ctl fg-win";
    var count = el("p", "fg-count");

    var top = el("div", "fg-tools");
    top.appendChild(ctl);
    top.appendChild(count);
    // A page that's one big table: the controls go right above its list.
    if (!lists[0].sec && !cfg.merge) article.insertBefore(top, lists[0].box);
    else insertTop(top, secs);

    ctl.addEventListener("input", function (e) {
      if (e.target.type === "search") { state.q = e.target.value.trim().toLowerCase(); draw(); }
    });
    ctl.addEventListener("change", function (e) {
      var k = e.target.dataset.k;
      if (k) { state[k] = e.target.value; draw(); }
    });
    ctl.addEventListener("click", function (e) {
      var b = e.target.closest(".fg-chip");
      if (!b) return;
      var on = b.getAttribute("aria-pressed") !== "true";
      b.setAttribute("aria-pressed", on);
      var v = b.dataset.v;
      state.chips = state.chips.filter(function (x) { return x !== v; });
      if (on) state.chips.push(v);
      draw();
    });

    // ---- Rows ----
    function cellHtml(col, r) {
      var c = r.cells[col];
      if (!c) return "";
      if ((col === cfg.chips && cfg.chips_style === "elements") || (cfg.elements || []).indexOf(col) >= 0) {
        var vs = split(c.text);
        return vs.length ? vs.map(function (v) { return elChip(v, "fg-weak"); }).join("") : "—";
      }
      return c.html;
    }

    function rowEl(r, L) {
      var row = el("div", "fg-row");
      var head = el("button", "fg-head");
      head.type = "button";
      head.setAttribute("aria-expanded", "false");
      var h = '<span class="fg-name"><span class="fg-cursor"></span><span>' + r.name + "</span>" +
        (L.kinds.length > 1 && r.kind !== L.kinds[0] ? '<span class="fg-tag">' + esc(r.kind) + "</span>" : "") + "</span>";
      L.show.forEach(function (col) {
        var v = cellHtml(col, r);
        h += '<span class="fg-c' + (numCols[col] ? " fg-num" : "") + '" data-k="' + esc(col) + '">' + (v === "" ? "—" : v) + "</span>";
      });
      head.innerHTML = h;
      row.appendChild(head);
      head.addEventListener("click", function () {
        var open = !row.classList.contains("open");
        row.classList.toggle("open", open);
        head.setAttribute("aria-expanded", open);
        var d = row.querySelector(".fg-detail");
        if (open && !d) row.appendChild(detail(r, L));
        else if (d) d.hidden = !open;
      });
      return row;
    }

    function detail(r, L) {
      var d = el("div", "fg-detail");
      var h = "<dl>";
      r.heads.slice(1).forEach(function (col) {
        if (L.show.indexOf(col) >= 0) return;
        var v = cellHtml(col, r);
        h += "<dt>" + esc(label(col)) + "</dt><dd>" + (v || "—") + "</dd>";
      });
      if (r.groups.length) {
        h += "<dt>" + esc(cfg.group_label || (cfg.merge ? "Found in" : (L.sec && cfg.group_in && cfg.group_in[title(L.sec)]) || cfg.group || "Found in")) + "</dt><dd>" + r.groups.map(esc).join(", ") + "</dd>";
      }
      d.innerHTML = h + "</dl>";
      // Item and enemy names in it open cards (fg-cards.js), if the page has them.
      if (window.fgCards) window.fgCards.link(d);
      return d;
    }

    function colhead(L) {
      var c = el("div", "fg-colhead");
      var h = "<span>" + esc(L.kinds.length > 1 ? "Name" : L.kinds[0]) + "</span>";
      L.show.forEach(function (col) {
        h += '<span class="' + (numCols[col] ? "fg-num" : "") + '">' + esc(label(col)) + "</span>";
      });
      c.innerHTML = h;
      return c;
    }

    lists.forEach(function (L) {
      if (cfg.merge) {
        L.note = el("div", "fg-groupnote");
        L.note.hidden = true;
        L.box.appendChild(L.note);
      }
      L.box.appendChild(colhead(L));
      L.list = el("div", "fg-list");
      L.box.appendChild(L.list);
      L.empty = el("p", "fg-empty", "Nothing matches.");
      L.empty.hidden = true;
      L.box.appendChild(L.empty);
      L.els = L.rows.map(function (r) { return rowEl(r, L); });
      // Every row, shown or not, so fg-cards.js can link names in them.
      (window.fgPageRows = window.fgPageRows || []).push.apply(window.fgPageRows, L.els);
      L.box.style.setProperty("--fg-cols", "minmax(0,1.6fr)" + L.show.map(function (col) {
        return numCols[col] ? " minmax(0,.55fr)" : " minmax(0,1.2fr)";
      }).join(""));
    });

    function match(r) {
      if (state.kind && r.kind !== state.kind) return false;
      if (state.group && r.groups.indexOf(state.group) < 0) return false;
      if (state.chips.length) {
        var have = chipsOf(r);
        if (!state.chips.some(function (c) { return have.indexOf(c) >= 0; })) return false;
      }
      if (state.q) {
        var hay = (r.nameText + " " + r.kind + " " + Object.keys(r.cells).map(function (k) { return r.cells[k].text; }).join(" ") +
          " " + r.groups.join(" ")).toLowerCase();
        if (hay.indexOf(state.q) < 0) return false;
      }
      return true;
    }

    function draw() {
      var s = state.sort === "" ? null : sorts[+state.sort];
      lists.forEach(function (L) {
        var idx = L.rows.map(function (r, i) { return i; }).filter(function (i) { return match(L.rows[i]); });
        if (s) {
          idx.sort(function (a, b) {
            var x = L.rows[a].cells[s.col] ? num(L.rows[a].cells[s.col].text) : null;
            var y = L.rows[b].cells[s.col] ? num(L.rows[b].cells[s.col].text) : null;
            if (x === null && y === null) return a - b;
            if (x === null) return 1;
            if (y === null) return -1;
            return (s.desc ? y - x : x - y) || a - b;
          });
        }
        L.list.textContent = "";
        // In story order, a "###" group's rows start with its heading.
        var heads = !cfg.merge && !s && L.groups && L.groups.length > 1, last = null;
        idx.forEach(function (i) {
          var g = L.rows[i].groups[0];
          if (heads && g && g !== last) {
            L.list.appendChild(el("div", "fg-grouphead", esc(g)));
            var gt = L.groups.filter(function (x) { return x.title === g; })[0];
            if (gt && gt.text) {
              if (!gt.el) { gt.el = el("div", "fg-grouptext", gt.text); if (window.fgCards) window.fgCards.link(gt.el); }
              L.list.appendChild(gt.el);
            }
          }
          last = g;
          L.list.appendChild(L.els[i]);
        });
        L.empty.hidden = idx.length > 0;
        L.shown = idx.length;
        if (L.note) {
          var g = state.group && (L.groups || []).filter(function (x) { return x.title === state.group; })[0];
          L.note.innerHTML = g && g.note ? g.note : "";
          L.note.hidden = !(g && g.note);
          if (g && g.note && window.fgCards) window.fgCards.link(L.note);
        }
      });
      // The lists on show (all of them, or the current sub-tab's).
      var vis = lists.filter(function (L) { return !L.sec || !L.sec.box.hidden; });
      top.hidden = !vis.length;
      if (!vis.length) { if (onDraw) onDraw(); return; }
      var shown = 0, total = 0;
      vis.forEach(function (L) { shown += L.shown; total += L.rows.length; });
      count.textContent = shown + " of " + total;
      fillGroups(vis);
      if (onDraw) onDraw();
    }
    // The group dropdown lists the groups of the lists on show.
    var groupsKey = null;
    function fillGroups(vis) {
      var box = ctl.querySelector("[data-groups]");
      if (!box) return;
      var gs = [];
      vis.forEach(function (L) { (L.groups || []).forEach(function (g) { if (gs.indexOf(g.title) < 0) gs.push(g.title); }); });
      box.hidden = gs.length < 2;
      // A section can call its groups something else (Bosses: Chapter).
      var own = cfg.group_in && vis.length === 1 && vis[0].sec && cfg.group_in[title(vis[0].sec)];
      box.querySelector("label").textContent = own || cfg.group;
      var key = gs.join("|");
      if (key === groupsKey) return;
      groupsKey = key;
      var sel = box.querySelector("select");
      sel.innerHTML = '<option value="">All</option>' + gs.map(function (g) {
        return '<option value="' + esc(g) + '">' + esc(g) + "</option>";
      }).join("");
      if (gs.indexOf(state.group) < 0 && state.group) { state.group = ""; draw(); return; }
      sel.value = state.group;
    }
    var onDraw = null;

    if (cfg.group) {
      // A link to a group's old heading (an area) filters to that group.
      openers.push(function (id, scroll) {
        var hit = null;
        lists.forEach(function (L) {
          (L.groups || []).forEach(function (g) { if (!hit && g.id === id) hit = { L: L, g: g }; });
        });
        if (!hit) return false;
        if (hit.L.sec && api.selectSec) api.selectSec(hit.L.sec.id);
        state.group = hit.g.title;
        draw();
        ctl.querySelector('select[data-k="group"]').value = hit.g.title;
        if (scroll) top.scrollIntoView({ block: "start" });
        return true;
      });
    }

    // "#find=Name" (a card's "Full entry" link) opens that name's row: its
    // sub-tab, a search for it, and the row itself.
    openers.push(function (id, scroll) {
      if (id.indexOf("find=") !== 0) return false;
      var name = id.slice(5).toLowerCase(), hit = null;
      lists.forEach(function (L) {
        L.rows.forEach(function (r, i) {
          var n = r.key;
          if (!hit && (n === name || n.indexOf(name + " (") === 0)) hit = { L: L, i: i };
        });
      });
      if (!hit) return false;
      state.q = name; state.kind = ""; state.group = ""; state.chips = [];
      ctl.querySelector("input[type=search]").value = id.slice(5);
      Array.prototype.forEach.call(ctl.querySelectorAll("select"), function (x) { x.value = ""; });
      Array.prototype.forEach.call(ctl.querySelectorAll(".fg-chip"), function (x) { x.setAttribute("aria-pressed", "false"); });
      if (hit.L.sec && api.selectSec) api.selectSec(hit.L.sec.id);
      draw();
      var row = hit.L.els[hit.i];
      if (!row.classList.contains("open")) row.querySelector(".fg-head").click();
      if (scroll) row.scrollIntoView({ block: "center" });
      return true;
    });

    // A link to an anchor in a row's name cell (bazaar.md#chronos-tear-pack)
    // opens that row, with every filter cleared.
    openers.push(function (id, scroll) {
      var hit = null;
      lists.forEach(function (L) {
        L.rows.forEach(function (r, i) { if (!hit && r.anchors.indexOf(id) >= 0) hit = { L: L, i: i }; });
      });
      if (!hit) return false;
      state.q = ""; state.kind = ""; state.group = ""; state.chips = [];
      ctl.querySelector("input[type=search]").value = "";
      Array.prototype.forEach.call(ctl.querySelectorAll("select"), function (x) { x.value = ""; });
      Array.prototype.forEach.call(ctl.querySelectorAll(".fg-chip"), function (x) { x.setAttribute("aria-pressed", "false"); });
      if (hit.L.sec && api.selectSec) api.selectSec(hit.L.sec.id);
      draw();
      var row = hit.L.els[hit.i];
      if (!row.classList.contains("open")) row.querySelector(".fg-head").click();
      if (scroll) row.scrollIntoView({ block: "center" });
      return true;
    });

    var api = {
      lists: lists, draw: draw,
      counts: function (sec) {
        var L = lists.filter(function (x) { return x.sec === sec; })[0];
        return L ? L.rows.length : null;
      },
      setOnDraw: function (f) { onDraw = f; }
    };
    return api;
  }

  // ---------- Sub-tabs ----------

  function buildSubtabs(secs, list) {
    var tabs = secs.filter(function (s) { return !s.sources; });
    if (tabs.length < 2) return;
    var nav = el("nav", "fg-subtabs");
    nav.setAttribute("aria-label", "Sections");
    tabs.forEach(function (s) {
      var n = list ? list.counts(s) : null;
      var a = el("a", null, "<b>" + esc(title(s)) + "</b>" + (n != null ? '<span class="fg-cnt">' + n + "</span>" : ""));
      a.href = "#" + s.id;
      a.dataset.id = s.id;
      nav.appendChild(a);
      s.box.classList.add("fg-tab-sec");
    });
    // Directly under the game's tab window, as in the field guide: the
    // page title moves out of sight (the lit tab already names the page).
    var h1 = article.querySelector("h1");
    if (h1 && h1.nextSibling) article.insertBefore(nav, h1.nextSibling); else insertTop(nav, secs);
    article.classList.add("fg-tabbed-page");
    document.documentElement.classList.add("fg-subtabbed");

    function select(id) {
      tabs.forEach(function (s) { s.box.hidden = s.id !== id; });
      Array.prototype.forEach.call(nav.children, function (a) {
        if (a.dataset.id === id) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
      });
      if (list) list.draw();
    }
    nav.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (!a) return;
      e.preventDefault();
      history.replaceState(null, "", "#" + a.dataset.id);
      select(a.dataset.id);
    });
    openers.push(function (id, scroll) {
      var s = tabs.filter(function (x) { return x.id === id || x.box.querySelector('[id="' + CSS.escape(id) + '"]'); })[0];
      if (!s) return false;
      select(s.id);
      if (scroll) {
        var t = s.id === id ? nav : document.getElementById(id);
        if (t) t.scrollIntoView({ block: "start" });
      }
      return true;
    });
    if (list) list.selectSec = select;
    select(tabs[0].id);
  }

  // ---------- Chapters: sections as numbered rows that open ----------

  function buildChapters(secs) {
    var chs = secs.filter(function (s) { return !s.sources; });
    if (!chs.length) return;
    var tools = el("div", "fg-tools");
    var ctl = el("div", "fg-ctl fg-win",
      '<div class="fg-grp fg-grow"><label class="fg-lbl">Search</label>' +
      '<input type="search" placeholder="Place, boss, item" aria-label="Search the walkthrough"></div>' +
      '<div class="fg-grp"><label class="fg-lbl">&nbsp;</label><button type="button" class="fg-btn" data-all>Open all</button></div>');
    var count = el("p", "fg-count");
    tools.appendChild(ctl);
    tools.appendChild(count);
    insertTop(tools, secs);
    var list = el("div", "fg-list fg-chapters");
    article.insertBefore(list, chs[0].box);

    chs.forEach(function (s, i) {
      var row = el("div", "fg-row fg-ch");
      // "### Boss: X", "### Final Boss: X", a "Boss: X" callout's title, or
      // a boss in an Enemies line (class fg-wt-boss).
      var names = [];
      Array.prototype.forEach.call(s.box.querySelectorAll("h3, .admonition-title, summary, .fg-wt-boss"), function (n) {
        var t = text(n).replace(/¶$/, "").trim();
        if (n.classList.contains("fg-wt-boss")) names.push(t);
        else if (/^(final )?boss(es)?:/i.test(t)) names.push(t.replace(/^(final )?boss(es)?:\s*/i, ""));
      });
      var tags = names.filter(function (t, j) { return names.indexOf(t) === j; })
        .map(function (t) { return '<span class="fg-tag fg-boss">' + esc(t) + "</span>"; });
      var head = el("button", "fg-head",
        '<span class="fg-chnum">' + (i + 1 < 10 ? "0" : "") + (i + 1) + "</span>" +
        '<span class="fg-name"><span class="fg-cursor"></span><span>' + esc(title(s)) + "</span></span>" +
        '<span class="fg-tags">' + tags.join("") + "</span>");
      head.type = "button";
      head.setAttribute("aria-expanded", "false");
      var body = el("div", "fg-detail fg-chbody");
      s.box.removeChild(s.h2);
      while (s.box.firstChild) body.appendChild(s.box.firstChild);
      s.box.remove();
      // Keep the heading's id so links to the chapter still land on it.
      row.id = s.id;
      s.h2.removeAttribute("id");
      row.appendChild(head);
      row.appendChild(body);
      body.hidden = true;
      list.appendChild(row);
      s.row = row; s.head = head; s.body = body;
      s.hay = text(body).toLowerCase() + " " + title(s).toLowerCase();
      head.addEventListener("click", function () { toggle(s, !row.classList.contains("open")); });
    });

    function toggle(s, open) {
      s.row.classList.toggle("open", open);
      s.head.setAttribute("aria-expanded", open);
      s.body.hidden = !open;
    }
    var allBtn = ctl.querySelector("[data-all]");
    allBtn.addEventListener("click", function () {
      var open = allBtn.textContent === "Open all";
      chs.forEach(function (s) { if (!s.row.hidden) toggle(s, open); });
      allBtn.textContent = open ? "Close all" : "Open all";
    });
    function draw(q) {
      var n = 0;
      chs.forEach(function (s) {
        var hit = !q || s.hay.indexOf(q) >= 0;
        s.row.hidden = !hit;
        if (hit) n++;
      });
      count.textContent = q ? n + " of " + chs.length + " chapters" : chs.length + " chapters";
    }
    ctl.querySelector("input").addEventListener("input", function (e) { draw(e.target.value.trim().toLowerCase()); });
    draw("");
    openers.push(function (id, scroll) {
      var s = chs.filter(function (x) { return x.id === id || x.body.querySelector('[id="' + CSS.escape(id) + '"]'); })[0];
      if (!s) return false;
      toggle(s, true);
      if (scroll) {
        var t = s.id === id ? s.row : document.getElementById(id);
        if (t) t.scrollIntoView({ block: "start" });
      }
      return true;
    });
  }

  // ---------- Weak and strong as element tags ----------

  // "**Weak:** fire, insect · **Strong:** thunder" in the text becomes element
  // tags, like the Bestiary's. The names match the Bestiary's spelling.
  var EL_NAMES = { dark: "Shadow", healing: "Heal", lightning: "Thunder" };
  function elementTags() {
    Array.prototype.forEach.call(article.querySelectorAll("li, p"), function (n) {
      if (!/<strong>(Weak|Strong):<\/strong>/.test(n.innerHTML)) return;
      n.innerHTML = n.innerHTML.replace(/(<strong>(?:Weak|Strong):<\/strong>)\s*([a-z][a-z ,]*?)(?=\s*(?:·|\.|<|$))/g, function (all, label, list) {
        var tags = list.split(/\s*,\s*|\s+and\s+/).filter(Boolean).map(function (v) {
          v = EL_NAMES[v] || v.charAt(0).toUpperCase() + v.slice(1);
          return elChip(v, "fg-weak");
        });
        return label + ' <span class="fg-els">' + tags.join("") + "</span>";
      });
    });
  }

  // ---------- Start ----------

  elementTags();
  var secs = sections();
  var list = fg.list ? buildList(fg.list, secs) : null;
  if (fg.subtabs) buildSubtabs(secs, list);
  else if (list) list.draw();
  if (fg.chapters) buildChapters(secs);
  document.documentElement.classList.add("fg-ready");
  if (location.hash) follow(true);
})();
