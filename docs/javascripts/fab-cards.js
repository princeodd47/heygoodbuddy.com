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

  // Rule numbers such as "CR 1.0.2b", "PPG 3.2" or "TRP 5.9, A.1" link to that
  // rule on the official rules site. Each chapter is its own page there.
  const RULE_PAGES = {
    CR: ["01-game-concepts", "02-object-properties", "03-zones", "04-game-structure",
      "05-layers-cards-abilities", "06-effects", "07-combat", "08-keywords", "09-additional-rules"],
    PPG: ["01-general", "02-gameplay-infractions", "03-tournament-infractions",
      "04-conduct-infractions"],
    TRP: ["01-tournament-information", "02-roles-and-responsibilities", "03-tournament-logistics",
      "04-tournament-materials", "05-gameplay-logistics", "06-behavior-and-conduct",
      "07-constructed-formats", "08-limited-formats", "09-special-formats"],
  };

  function ruleUrl(doc, number) {
    const chapter = number.split(".")[0];
    const page = chapter === "A" ? "appendix" : RULE_PAGES[doc][Number(chapter) - 1];
    if (!page) return null;
    const d = doc.toLowerCase();
    return "https://rules.fabtcg.com/en/" + d + "/" + page + "/#" + d + number;
  }

  // A number is linked when it follows CR, PPG or TRP directly or through a
  // list of other numbers ("CR 8.4.10, 7.3.2d" or "CR 4.1.4–4.1.6").
  // startDoc treats the text as if it began with that document's name, for
  // table columns headed "CR". appendPlain(parent, text) adds everything else.
  function appendRuleLinks(parent, text, appendPlain, startDoc) {
    const re = /\b(CR|PPG|TRP)\b|\b(A\.\d+|\d+(?:\.\d+)*[a-z]?)(?!\w|\.\d)/g;
    let doc = startDoc || null;
    let done = 0;
    let lastEnd = 0;
    let m;
    while ((m = re.exec(text))) {
      const gap = text.slice(lastEnd, m.index);
      lastEnd = re.lastIndex;
      if (m[1]) {
        doc = m[1];
        continue;
      }
      if (!doc || !/^[\s,–-]*[a-z]?[\s,–-]*$/.test(gap)) {
        doc = null;
        continue;
      }
      const url = ruleUrl(doc, m[2]);
      if (!url) continue;
      if (m.index > done) appendPlain(parent, text.slice(done, m.index));
      const a = el("a", "fab-rulelink", m[2]);
      a.href = url;
      a.target = "_blank";
      a.rel = "noopener";
      a.title = "Open " + doc + " " + m[2] + " on rules.fabtcg.com";
      parent.append(a);
      done = re.lastIndex;
    }
    if (done < text.length) appendPlain(parent, text.slice(done));
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

  // Rule numbers in the text of the Flesh and Blood pages become links too.
  function linkRuleNumbers() {
    const article = document.querySelector("article.md-content__inner");
    if (!article || !location.pathname.includes("/games/flesh-and-blood/")) return;
    const replace = (node, startDoc) => {
      const frag = document.createDocumentFragment();
      appendRuleLinks(frag, node.nodeValue, (parent, text) => parent.append(text), startDoc);
      node.replaceWith(frag);
    };

    // Table columns headed CR, PPG or TRP hold bare numbers like "8.3.5".
    for (const table of article.querySelectorAll("table")) {
      const heads = [...table.querySelectorAll("thead th")].map((th) => th.textContent.trim());
      heads.forEach((doc, col) => {
        if (!RULE_PAGES[doc]) return;
        for (const row of table.querySelectorAll("tbody tr")) {
          const cell = row.children[col];
          if (cell && cell.firstChild && cell.firstChild.nodeType === Node.TEXT_NODE) {
            replace(cell.firstChild, doc);
          }
        }
      });
    }

    const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT, {
      acceptNode: (node) =>
        node.parentElement.closest("a, code, pre, script, #fab-quiz") ||
        !/\b(CR|PPG|TRP)\s+[\dA]/.test(node.nodeValue)
          ? NodeFilter.FILTER_REJECT
          : NodeFilter.FILTER_ACCEPT,
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const node of nodes) replace(node);
  }

  function setUp() {
    linkRuleNumbers();
    setUpPreviews();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setUp);
  } else {
    setUp();
  }

  return { appendSymbols, appendCardText, appendRuleLinks, faceText, faces };
})();
