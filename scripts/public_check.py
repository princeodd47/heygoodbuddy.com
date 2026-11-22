"""Stop the deploy if anything outside the public allowlist is in the repo.

This repo is the public half of heygoodbuddy.com: Flesh and Blood and the
articles. Every other game lives in the private repo (heygoodbuddy-private).
A new top-level folder or game has to be added here on purpose before it can
be published. Run: python scripts/public_check.py
"""
import subprocess
import sys

# Exact files, and folders (ending in "/") whose contents are all allowed.
ALLOWED = [
    ".gitignore", "CLAUDE.md", "README.md", "requirements.txt", "mkdocs.yml",
    ".github/",
    "docs/CNAME", "docs/index.md", "docs/tags.md", "docs/blog/",
    "docs/games/flesh-and-blood/", "docs/assets/images/flesh-and-blood/",
    "data/flesh-and-blood/", "notes/flesh-and-blood/", "notes/README.md",
    "docs/stylesheets/extra.css", "docs/stylesheets/field-guide.css",
    "docs/stylesheets/fab.css",
    "docs/javascripts/fab-cards.js", "docs/javascripts/fab-quiz.js",
    "docs/javascripts/fg-pages.js", "docs/javascripts/fg-tables.js",
    "docs/javascripts/fg-search.js",
    "overrides/main.html",
    "scripts/fab_cards.py", "scripts/public_check.py",
]


def allowed(path):
    return any(path == a or (a.endswith("/") and path.startswith(a)) for a in ALLOWED)


files = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.split()
bad = [f for f in files if not allowed(f)]
if bad:
    print("Not on the public allowlist (move it to the private repo, or add it")
    print("to ALLOWED in scripts/public_check.py if it really is public):")
    for f in bad:
        print("  " + f)
    sys.exit(1)
print(f"public_check: {len(files)} files, all on the allowlist")
