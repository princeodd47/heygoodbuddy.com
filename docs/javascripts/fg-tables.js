// Field guide look: on phones, a table with 4+ columns that is too wide for
// the screen (by its text) becomes one card per row. This copies each column header onto
// its cells as data-label so the CSS can label the fields.
(function () {
  // Estimate the table's width in characters: each column's longest entry
  // (or its header), plus room for padding. About 50 fit across a phone, so a
  // short table (Yes/No answers, small numbers) stays a table.
  var PHONE_CHARS = 50;

  function tooWide(t, heads) {
    var widest = heads.map(function (h) { return h.length; });
    t.querySelectorAll("tbody tr").forEach(function (tr) {
      Array.prototype.forEach.call(tr.children, function (td, i) {
        widest[i] = Math.max(widest[i] || 0, td.textContent.trim().length);
      });
    });
    var total = widest.reduce(function (sum, w) { return sum + w + 3; }, 0);
    return total > PHONE_CHARS;
  }

  // A header used twice gets told apart: after the nearest one-off header
  // before it that names a group ("MP · Earlier on" on a Mantras table), or
  // else by number ("Parent 2"). The first column is the row's name, not a
  // group, so it never counts.
  function distinct(heads) {
    var count = {};
    heads.forEach(function (h) { count[h] = (count[h] || 0) + 1; });
    var seen = {};
    return heads.map(function (h, i) {
      seen[h] = (seen[h] || 0) + 1;
      if (seen[h] === 1) return h;
      for (var j = i - 1; j > 0; j--) {
        if (count[heads[j]] === 1) return h + " · " + heads[j];
      }
      return h + " " + seen[h];
    });
  }

  function label() {
    if (!document.documentElement.classList.contains("fg")) return;
    document.querySelectorAll(".md-typeset table:not([class])").forEach(function (t) {
      if (t.closest(".uo-equip")) return;
      var heads = Array.prototype.map.call(t.querySelectorAll("thead th"), function (th) {
        return th.textContent.trim();
      });
      if (heads.length < 4 || !tooWide(t, heads)) return;
      heads = distinct(heads);
      t.setAttribute("data-fg-stack", "");
      t.querySelectorAll("tbody tr").forEach(function (tr) {
        Array.prototype.forEach.call(tr.children, function (td, i) {
          if (heads[i]) td.setAttribute("data-label", heads[i]);
          if (i > 0 && td.textContent.trim().length <= 20) td.classList.add("fg-short");
          // A bare number as the card title: show its header with it ("Battle 1").
          if (i === 0 && /^\d+$/.test(td.textContent.trim())) td.classList.add("fg-numhead");
        });
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", label);
  } else {
    label();
  }
})();
