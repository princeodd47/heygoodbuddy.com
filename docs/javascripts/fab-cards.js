// Flesh and Blood card display, shared by the study pages and the practice
// quiz. Card details come from data/flesh-and-blood/cards.yaml (written by
// scripts/fab_cards.py). On the study pages, card names written with the
// card() macro open a preview of the card's image and current text.
window.FabCards = (function () {
  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.append(text);
    return e;
  }

  // Card symbols written as {p}, {r} and so on. iconFor(key) returns an <img>
  // for the symbol, or null to leave the text as it is (as with {g} and {x}).
  function appendSymbols(parent, text, iconFor) {
    text.split(/(\{[a-z]\})/).forEach((part) => {
      const icon = /^\{([a-z])\}$/.test(part) && iconFor(part[1]);
      if (icon) parent.append(icon);
      else if (part) parent.append(part);
    });
  }

  // Card text marks bold with **, italics with _ and line breaks with {br}.
  function appendCardText(parent, text, iconFor) {
    text.split("{br}").forEach((line) => {
      const div = el("div");
      line.split(/(\*\*[^*]+\*\*|_[^_]+_)/).forEach((part) => {
        const bold = /^\*\*(.+)\*\*$/.exec(part);
        const italic = /^_(.+)_$/.exec(part);
        if (bold || italic) {
          const span = el(bold ? "strong" : "em");
          appendSymbols(span, (bold || italic)[1], iconFor);
          div.append(span);
        } else if (part) {
          appendSymbols(div, part, iconFor);
        }
      });
      parent.append(div);
    });
  }

  // Name, type line and text of one face of a card.
  function faceText(face, iconFor) {
    const box = el("div", "fab-cardtext");
    const title = el("div", "fab-cardname", face.name + (face.color ? " (" + face.color + ")" : ""));
    title.append(el("span", "fab-typebox", face.typebox));
    box.append(title);
    if (face.text) appendCardText(box, face.text, iconFor);
    return box;
  }

  function faces(card) {
    return [card.front, card.back].filter(Boolean);
  }

  // Previews for card names on the study pages.
  function setUpPreviews() {
    const dataTag = document.getElementById("fab-cards-data");
    const refs = document.querySelectorAll("a.fab-cardref[data-card]");
    if (!dataTag || !refs.length) return;
    const { cards, icons } = JSON.parse(dataTag.textContent);

    const pop = el("div", "fab-cardpop md-typeset");
    pop.hidden = true;
    pop.setAttribute("role", "dialog");
    document.body.append(pop);
    let openFor = null;

    function show(ref) {
      const card = cards[ref.dataset.card];
      if (!card) return;
      // The card images sit in cards/ next to the symbol icons.
      const iconFor = (key) => {
        if (!icons[key]) return null;
        const img = el("img", "fab-icon");
        img.src = new URL("../icon_" + key + ".png", ref.href).href;
        img.alt = img.title = icons[key];
        return img;
      };
      pop.replaceChildren();
      const images = el("div", "fab-cardpop-images");
      for (const face of faces(card)) {
        const img = el("img");
        img.src = new URL(face.image, ref.href).href;
        img.alt = face.name;
        images.append(img);
      }
      pop.append(images, ...faces(card).map((face) => faceText(face, iconFor)));
      pop.hidden = false;
      openFor = ref;

      const r = ref.getBoundingClientRect();
      const width = pop.offsetWidth;
      const left = Math.max(8, Math.min(r.left + window.scrollX, window.scrollX + document.documentElement.clientWidth - width - 8));
      pop.style.left = left + "px";
      pop.style.top = r.bottom + window.scrollY + 6 + "px";
    }

    function hide() {
      pop.hidden = true;
      openFor = null;
    }

    for (const ref of refs) {
      ref.setAttribute("aria-haspopup", "dialog");
      ref.addEventListener("click", (e) => {
        e.preventDefault();
        if (openFor === ref) hide();
        else show(ref);
      });
    }
    document.addEventListener("click", (e) => {
      if (openFor && !pop.contains(e.target) && !e.target.closest("a.fab-cardref")) hide();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && openFor) {
        const ref = openFor;
        hide();
        ref.focus();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setUpPreviews);
  } else {
    setUpPreviews();
  }

  return { appendSymbols, appendCardText, faceText, faces };
})();
