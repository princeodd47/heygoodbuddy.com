"""Build the FF6 Advance Field Guide page for the site.

Reads template.html and data.json from this folder and writes
docs/games/final-fantasy-vi-advance/index.html, the game's only page. It also
writes field-guide/index.html, a redirect from the guide's old address.

    python3 notes/final-fantasy-vi-advance/build.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "docs/games/final-fantasy-vi-advance/index.html"
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

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Final Fantasy VI Advance field guide: characters, abilities, bestiary, equipment, Espers, a chapter-by-chapter walkthrough, the Colosseum and tips, using the Game Boy Advance names and stats.">
"""

# The way back to the site: "heygoodbuddy.com › Games", small and dim above
# the title, in the guide's own colors.
CRUMB_CSS = (
    ".crumb{display:inline-block;font-size:13px;color:var(--ink-dim);margin-bottom:10px}"
    ".crumb a{color:inherit;text-decoration:none}"
    ".crumb a:hover{color:var(--gold);text-decoration:underline}"
    ".crumb .sep{margin:0 6px;opacity:.6}\n"
)


def replace_once(text, old, new):
    assert text.count(old) == 1, f"expected one match for {old[:40]!r}"
    return text.replace(old, new)


def main():
    page = (HERE / "template.html").read_text(encoding="utf-8")
    data = (HERE / "data.json").read_text(encoding="utf-8").replace("</", "<\\/")
    page = replace_once(page, "__DATA__", data)
    # The artifact host adds its own document skeleton; the site needs a full one.
    page = page.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    page = replace_once(page, "<style>", "<style>\n" + CRUMB_CSS)
    page = replace_once(
        page,
        '<h1><small>Final Fantasy VI Advance</small>Field Guide</h1>',
        '<div><nav class="crumb" aria-label="Breadcrumb"><a href="../../">heygoodbuddy.com</a>'
        '<span class="sep">›</span><a href="../">Games</a></nav>'
        '<h1><small>Final Fantasy VI Advance</small>Field Guide</h1></div>',
    )
    style_end = page.index("</style>") + len("</style>")
    page = HEAD + page[:style_end] + "\n</head>\n<body>\n" + page[style_end:] + "\n</body>\n</html>\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page):,} bytes)")
    OLD.parent.mkdir(parents=True, exist_ok=True)
    OLD.write_text(REDIRECT, encoding="utf-8")
    print(f"wrote {OLD.relative_to(ROOT)} (redirect)")


if __name__ == "__main__":
    main()
