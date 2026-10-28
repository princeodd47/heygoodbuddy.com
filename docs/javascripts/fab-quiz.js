// Practice quiz on the Flesh and Blood judge study pages. Questions come from
// data/flesh-and-blood/quiz.yaml; answers are shuffled each time, and missed
// questions are remembered in this browser so they can be reviewed later.
(function () {
  const root = document.getElementById("fab-quiz");
  if (!root) return;

  const data = JSON.parse(document.getElementById("fab-quiz-data").textContent);
  // Rulings from data/flesh-and-blood/my-rulings.yaml: always asked in full,
  // in file order.
  const mineTag = document.getElementById("fab-quiz-mine");
  const mine = mineTag ? JSON.parse(mineTag.textContent) : [];
  mine.forEach((q) => (q.mine = true));
  const everyQuestion = data.questions.concat(mine);
  // Card details for questions with a `cards:` list, from
  // data/flesh-and-blood/cards.yaml (written by scripts/fab_cards.py).
  const cardsTag = document.getElementById("fab-quiz-cards");
  const cards = cardsTag ? JSON.parse(cardsTag.textContent) : {};
  const PASS = 0.85;
  const STORE = "fab-quiz-missed";
  const EXAMS = {
    all: { label: "Everything", topics: Object.keys(data.topics) },
    l1a: { label: "L1A practice (rules)", topics: ["rules", "interactions"] },
    l1b: { label: "L1B practice (policy)", topics: ["policy", "tournament"] },
  };
  for (const [key, label] of Object.entries(data.topics)) {
    EXAMS[key] = { label: label + " only", topics: [key] };
  }
  if (mine.length) {
    EXAMS.mine = { label: "My rulings (" + mine.length + ", in order)", fixed: true };
  }

  // Browser storage can be missing or blocked; the quiz still works without it.
  function loadMissed() {
    try {
      return new Set(JSON.parse(localStorage.getItem(STORE) || "[]"));
    } catch (e) {
      return new Set();
    }
  }
  function saveMissed() {
    try {
      localStorage.setItem(STORE, JSON.stringify([...missed]));
    } catch (e) {
      // Nothing to do; the list just won't survive a reload.
    }
  }
  const missed = loadMissed();

  // Card symbols written as {p}, {r} and so on in the question text are shown
  // as the icons the page renders in #fab-quiz-icons.
  const icons = {};
  for (const img of document.querySelectorAll("#fab-quiz-icons img[data-key]")) {
    icons[img.dataset.key] = img;
  }

  // Card images sit in a cards/ folder next to the icons, so the icons' URL
  // gives the right path from whatever page this runs on.
  const anyIcon = Object.values(icons)[0];
  const cardImageBase = anyIcon ? new URL("cards/", anyIcon.src) : null;

  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) appendText(e, text);
    return e;
  }

  function iconFor(key) {
    if (!icons[key]) return null;
    const img = icons[key].cloneNode();
    img.className = "fab-icon";
    img.title = img.alt;
    return img;
  }

  function appendText(parent, text) {
    FabCards.appendSymbols(parent, text, iconFor);
  }

  // Like appendText, but rule numbers ("TRP 5.9") link to the official rules.
  function appendRuleText(parent, text) {
    FabCards.appendRuleLinks(parent, text, appendText);
    return parent;
  }

  function cardFaces(q) {
    return (q.cards || []).filter((id) => cards[id]).flatMap((id) => FabCards.faces(cards[id]));
  }

  // Thumbnails above the question; click one to see it full size.
  function cardImages(q) {
    const faces = cardFaces(q);
    if (!faces.length || !cardImageBase) return null;
    const row = el("div", "fq-cards");
    for (const face of faces) {
      const b = el("button", "fq-cardimg");
      b.type = "button";
      b.title = "Click to enlarge";
      const img = el("img");
      img.src = new URL(face.image, cardImageBase).href;
      img.alt = face.name;
      img.loading = "lazy";
      b.append(img);
      b.addEventListener("click", () => b.classList.toggle("fq-zoom"));
      row.append(b);
    }
    return row;
  }

  // The current official text of each card, shown with the explanation.
  function cardTexts(q) {
    return cardFaces(q).map((face) => FabCards.faceText(face, iconFor));
  }

  function button(cls, text, onClick) {
    const b = el("button", "md-button " + cls, text);
    b.type = "button";
    b.addEventListener("click", onClick);
    return b;
  }

  function shuffle(list) {
    const a = [...list];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  let run = null;

  function showSetup() {
    root.replaceChildren();
    const form = el("div", "fq-setup");

    const examLabel = el("label", null, "Questions from ");
    const exam = el("select");
    for (const [key, e] of Object.entries(EXAMS)) {
      const opt = el("option", null, e.label);
      opt.value = key;
      exam.append(opt);
    }
    examLabel.append(exam);

    const countLabel = el("label", null, "How many ");
    const count = el("select");
    for (const n of [10, 20, 40, "all"]) {
      const opt = el("option", null, String(n));
      opt.value = String(n);
      count.append(opt);
    }
    count.value = "20";
    countLabel.append(count);

    const pool = () => data.questions.filter((q) => EXAMS[exam.value].topics.includes(q.topic));
    const syncCount = () => (count.disabled = !!EXAMS[exam.value].fixed);
    exam.addEventListener("change", syncCount);
    const start = button("md-button--primary", "Start", () => {
      if (EXAMS[exam.value].fixed) {
        begin(mine, EXAMS[exam.value].label);
        return;
      }
      const all = shuffle(pool());
      const n = count.value === "all" ? all.length : Number(count.value);
      begin(all.slice(0, n), EXAMS[exam.value].label, true);
    });

    form.append(examLabel, countLabel, start);
    root.append(form);

    const missedQs = everyQuestion.filter((q) => missed.has(q.id));
    const review = el("p", "fq-review");
    if (missedQs.length) {
      review.append(
        button("", "Review missed (" + missedQs.length + ")", () =>
          begin(shuffle(missedQs), "Missed questions")
        ),
        " ",
        button("fq-clear", "Clear missed list", () => {
          missed.clear();
          saveMissed();
          showSetup();
        })
      );
    } else {
      review.textContent = "No missed questions saved yet.";
    }
    root.append(review);
  }

  // Only fresh practice runs are compared with the 85% pass mark. Reviews,
  // retries and My rulings repeat questions you've already seen.
  function begin(questions, label, graded = false) {
    run = { questions, label, graded, index: 0, right: 0, wrong: [] };
    showQuestion();
  }

  function showQuestion() {
    const q = run.questions[run.index];
    root.replaceChildren();

    const head = el("div", "fq-head");
    head.append(
      el("span", null, run.label),
      el("span", null, "Question " + (run.index + 1) + " of " + run.questions.length),
      el("span", null, "Score " + run.right + "/" + run.index)
    );
    root.append(head);

    const card = el("div", "fq-card");
    card.append(el("div", "fq-topic", q.mine ? "My ruling" : data.topics[q.topic]));
    const images = cardImages(q);
    if (images) card.append(images);
    card.append(el("p", "fq-q", q.q));

    const choices = el("div", "fq-choices");
    const order = shuffle(q.choices.map((text, i) => ({ text, right: i === q.answer })));
    const buttons = order.map((c) => {
      const b = el("button", "fq-choice", c.text);
      b.type = "button";
      b.addEventListener("click", () => answer(c.right, b, buttons, order, card));
      choices.append(b);
      return b;
    });
    card.append(choices);
    root.append(card);
    buttons[0].focus({ preventScroll: true });
  }

  function answer(right, picked, buttons, order, card) {
    const q = run.questions[run.index];
    buttons.forEach((b, i) => {
      b.disabled = true;
      if (order[i].right) b.classList.add("fq-right");
    });
    if (right) {
      run.right++;
      missed.delete(q.id);
    } else {
      picked.classList.add("fq-wrong");
      run.wrong.push(q);
      missed.add(q.id);
    }
    saveMissed();

    const result = el("div", "fq-why " + (right ? "fq-why-right" : "fq-why-wrong"));
    // A blank line in "why" starts a new paragraph.
    String(q.why || "")
      .trim()
      .split(/\n\s*\n/)
      .forEach((text, i) => {
        const p = el("p", "fq-why-text");
        if (i === 0) p.append(el("strong", null, right ? "Correct. " : "Not quite. "));
        appendRuleText(p, text.replace(/\s*\n\s*/g, " "));
        result.append(p);
      });
    const source = [q.cite, q.when].filter(Boolean).join(" · ");
    if (source) result.append(appendRuleText(el("div", "fq-cite"), source));
    result.append(...cardTexts(q));
    card.append(result);

    const last = run.index + 1 >= run.questions.length;
    const next = button("md-button--primary fq-next", last ? "See results" : "Next", () => {
      run.index++;
      if (last) showResults();
      else showQuestion();
    });
    card.append(next);
    next.focus({ preventScroll: true });
  }

  function showResults() {
    root.replaceChildren();
    const total = run.questions.length;
    const pct = total ? run.right / total : 0;
    const pass = pct >= PASS;

    const box = el("div", "fq-card fq-results");
    box.append(el("p", "fq-score", run.right + " / " + total + " (" + Math.round(pct * 100) + "%)"));
    if (run.graded) {
      box.append(
        el(
          "p",
          pass ? "fq-pass" : "fq-fail",
          pass ? "At or above the 85% the real exams need." : "Below the 85% the real exams need."
        )
      );
    } else {
      const left = run.questions.filter((q) => missed.has(q.id)).length;
      box.append(
        el(
          "p",
          "fq-review-note",
          "Review round, so it isn't scored against the 85% pass mark. " +
            (left
              ? left + " of these " + (left === 1 ? "is" : "are") + " still on your missed list."
              : "None of these are on your missed list now.")
        )
      );
    }

    if (run.wrong.length) {
      box.append(el("p", null, "Missed this time:"));
      const list = el("ul");
      for (const q of run.wrong) {
        const li = el("li", null, q.q + " ");
        if (q.cite) li.append(appendRuleText(el("span", "fq-cite"), "(" + q.cite + ")"));
        list.append(li);
      }
      box.append(list);
    }

    const again = el("p");
    again.append(button("md-button--primary", "New quiz", showSetup));
    if (run.wrong.length) {
      again.append(" ", button("", "Retry these misses", () => begin(shuffle(run.wrong), "Retry")));
    }
    box.append(again);
    root.append(box);
  }

  showSetup();
})();
