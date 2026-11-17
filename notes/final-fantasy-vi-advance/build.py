"""Build the FF6 Advance Field Guide for the site.

The guide is the game's page, /games/final-fantasy-vi-advance/, rendered by
the site like any other page so it gets the site header, search and Tags:

- docs/games/final-fantasy-vi-advance/index.md (written by hand) is the page:
  its front matter picks the ff6.html template, and its text is what search
  indexes. The template shows the guide instead of the text.
- This script reads template.html and data.json from this folder and writes
  overrides/partials/ff6-guide.html, the guide that template includes: its
  styles, markup and script, unchanged except that every style rule is scoped
  to the guide (.ff6) so it can't restyle the site's header or footer.
- It also writes field-guide/index.html, a redirect from the guide's old
  address.

    python3 notes/final-fantasy-vi-advance/build.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "overrides/partials/ff6-guide.html"
OLD = ROOT / "docs/games/final-fantasy-vi-advance/field-guide/index.html"

REDIRECT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Final Fantasy VI Advance Field Guide</title>
<link rel="canonical" href="../">
<meta http-equiv="refresh" content="0; url=../">
</head>
<body>
<p>The field guide has moved to <a href="../">Final Fantasy VI Advance</a>.</p>
</body>
</html>
"""

# Fits the guide into a site page like the other games': it starts where
# their content does and takes the page's width (there's no left nav or table
# of contents here), the game's name matches theirs, and the sticky tab window
# sits below the site's sticky header.
SITE_CSS = """
.ff6{flex:1 1 auto;min-width:0;background:none}
.ff6 nav.tabs{top:calc(2.4rem + 2px)}
.ff6 .wrap{max-width:none;margin:0 .8rem;padding:1.1rem 0 48px}
@media screen and (min-width:76.25em){.ff6 .wrap{margin:0 1.2rem}}
.ff6 header.top{padding:0}
.ff6 h1{font-size:.7rem;line-height:1.45;text-shadow:none}
.ff6 h1 small{font-size:inherit;margin:0 0 .5rem}
"""


def replace_once(text, old, new):
    assert text.count(old) == 1, f"expected one match for {old[:40]!r}"
    return text.replace(old, new)


def scope_selector(sel):
    """Put one selector inside .ff6; the page-level ones become .ff6 itself."""
    sel = sel.strip()
    m = re.match(r"^(:root|html|body)(?![\w-])(.*)$", sel)
    if m:
        return ".ff6" + m.group(2)
    return ".ff6 " + sel


def scope_css(css):
    """Scope every rule in css to .ff6, including those inside @media.

    @keyframes bodies are left alone. Rules only the standalone page needed
    (html's background, body::before's safe-area bar) are dropped.
    """
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            out.append(css[i:])
            break
        head = css[i:j]
        # Find the matching close brace.
        depth, k = 1, j + 1
        while depth:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        body = css[j + 1:k - 1]
        lead = head[: len(head) - len(head.lstrip())]
        h = head.strip()
        if h.startswith("@keyframes"):
            out.append(lead + h + "{" + body + "}")
        elif h.startswith("@"):
            out.append(lead + h + "{" + scope_css(body) + "}")
        elif h in ("html", "body::before"):
            pass
        else:
            sels = ",".join(scope_selector(s) for s in h.split(","))
            out.append(lead + sels + "{" + body + "}")
        i = k
    return "".join(out)


def main():
    page = (HERE / "template.html").read_text(encoding="utf-8")
    data = (HERE / "data.json").read_text(encoding="utf-8").replace("</", "<\\/")
    page = replace_once(page, "__DATA__", data)

    # The site's head already has the title and fonts; keep the guide's
    # styles, markup and script.
    start, end = page.index("<style>"), page.index("</style>")
    css = page[start + len("<style>"):end]
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    rest = page[end + len("</style>"):]

    guide = (
        "<style>\n" + scope_css(css) + SITE_CSS + "</style>\n"
        '<div class="ff6">' + rest.strip() + "\n</div>\n"
    )
    assert "{% endraw %}" not in guide
    out = (
        "{#- Built by notes/final-fantasy-vi-advance/build.py; edit the files"
        " there, not this one. -#}\n"
        "{% raw %}" + guide + "{% endraw %}\n"
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(out, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(out):,} bytes)")
    OLD.parent.mkdir(parents=True, exist_ok=True)
    OLD.write_text(REDIRECT, encoding="utf-8")
    print(f"wrote {OLD.relative_to(ROOT)} (redirect)")


if __name__ == "__main__":
    main()
