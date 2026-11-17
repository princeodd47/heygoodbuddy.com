// Field guide look: on phones, wide tables (4+ columns) become one card per
// row. This copies each column header onto its cells as data-label so the
// CSS can label the fields. Runs only on pages with `skin: field-guide`.
(function () {
  function label() {
    if (!document.documentElement.classList.contains("fg")) return;
    document.querySelectorAll(".md-typeset table:not([class])").forEach(function (t) {
      if (t.closest(".uo-equip")) return;
      var heads = Array.prototype.map.call(t.querySelectorAll("thead th"), function (th) {
        return th.textContent.trim();
      });
      if (heads.length < 4) return;
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
