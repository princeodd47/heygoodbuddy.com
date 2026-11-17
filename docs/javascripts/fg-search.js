// Field guide look for the search dialog. The theme draws the dialog inside a
// shadow root, which the site's stylesheets can't reach, so this adds a style
// element to it. Colors and the body font come in through the variables set in
// field-guide.css; this adds what variables can't: an opaque window frame,
// pixel-font titles and the gold menu cursor on the selected result.
//
// The class names are the theme's minified ones (Zensical 0.0.71, pinned in
// requirements.txt). If the dialog looks plain after a Zensical upgrade, read
// the dialog's CSS in the theme bundle and update them.
(function () {
  var CSS = [
    // Pixelify Sans joins "fi" into a glyph that reads as "A" (Lufia), so no
    // ligatures, as on the rest of the site.
    ".r,.r *{font-feature-settings:'kern','liga' 0;font-variant-ligatures:no-common-ligatures}",
    // The panel: the field guide window, opaque instead of frosted glass.
    ".e{background:linear-gradient(180deg,#2a3f9e,#0f1a5c);backdrop-filter:none;-webkit-backdrop-filter:none;",
    "border:2px solid #e8ecff;border-radius:8px;",
    "box-shadow:0 0 0 2px #5d6fd0 inset,0 6px 0 rgba(0,0,0,.35),0 18px 48px rgba(0,0,0,.55)}",
    // Filters column: a darker band inside the window.
    ".t{background:rgba(11,16,36,.35)}",
    ".R{font-family:'Pixelify Sans',monospace;font-weight:500;color:#ffd66b}",
    ".X{font-family:'Pixelify Sans',monospace;font-weight:500;font-size:13px;letter-spacing:0;color:#aab3e6;opacity:1}",
    // Tag filters: names in the pixel face, counts in mono like the site's numbers.
    ".i .q{font-family:'Pixelify Sans',monospace;font-weight:500;letter-spacing:0}",
    ".i .A{font-family:'IBM Plex Mono',monospace}",
    // The search box: what you type, and its "Search" placeholder.
    ".s input{font-family:'Pixelify Sans',monospace;font-weight:500;letter-spacing:0}",
    // Result titles: pixel face in gold (matched words are underlined).
    ".x{font-family:'Pixelify Sans',monospace;font-weight:500;font-size:15px;color:#ffd66b;letter-spacing:0}",
    // Selected or hovered result: a row with the gold cursor bar.
    ".o:before{background-color:#1d2c84;box-shadow:inset 4px 0 0 #ffd66b}",
    ".f{font-family:'IBM Plex Mono',monospace}"
  ].join("");

  function style(host) {
    if (!host.shadowRoot || host.shadowRoot.querySelector("style[data-fg]")) return;
    var s = document.createElement("style");
    s.setAttribute("data-fg", "");
    s.textContent = CSS;
    host.shadowRoot.appendChild(s);
  }

  function find() {
    Array.prototype.forEach.call(document.body.children, function (el) {
      if (el.shadowRoot && el.shadowRoot.querySelector("dialog")) style(el);
    });
  }

  function start() {
    find();
    // The theme may build the dialog after this runs, or rebuild it.
    new MutationObserver(find).observe(document.body, { childList: true });
    document.addEventListener("click", function (e) {
      if (e.target.closest && e.target.closest(".md-search__button")) setTimeout(find, 0);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
