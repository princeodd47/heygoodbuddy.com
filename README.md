# heygoodbuddy.com

Source for [heygoodbuddy.com](https://heygoodbuddy.com/): Flesh and Blood
rules study and articles, built with [Zensical](https://zensical.org/). Site settings live in
`mkdocs.yml`, which Zensical reads directly.

## Local preview

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/zensical serve
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\zensical serve
```

Then open http://127.0.0.1:8000. The page reloads as you edit.

To check the site builds without serving it, run `.venv/bin/zensical build`.
It should end with "No issues found".

GitHub Pages lets browsers cache scripts and stylesheets for 10 minutes, so a
page can load new HTML with an old script. The scripts and stylesheets in
`mkdocs.yml` carry a `?v=` tag for that reason: change it (e.g. to today's
date) whenever the file changes.

## Layout

```
docs/
  index.md                 # home page
  games/flesh-and-blood/   # Flesh and Blood (top-level tab; URLs kept from
                           # when it sat under Games)
  blog/posts/              # articles (need a date in frontmatter)
  tags.md                  # auto-generated tag index
  CNAME                    # custom domain for GitHub Pages
data/flesh-and-blood/      # YAML data used to build tables
scripts/                   # fab_cards.py (card data), public_check.py (allowlist)
```

## Public and private

This repo is public and holds only Flesh and Blood and the articles. Every
other game's guide lives in the private repo `heygoodbuddy-private`.

`scripts/public_check.py` lists every path allowed here. The deploy runs it
first and stops if anything else is in the repo, so a new game or folder can
only be published by adding it to that list on purpose.

## Adding things

- **New article:** add a Markdown file to `docs/blog/posts/` with a `date`
  in its frontmatter. It's listed automatically.
- **New data table:** add a YAML file under `data/flesh-and-blood/` and
  register it under `include_yaml` in `mkdocs.yml`. The file's top level must
  be a mapping (e.g. `quiz:` followed by the list), not a bare list. A wrong
  path is skipped silently, so an empty table usually means a typo in the path.

## Deploying

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site
and publishes it with GitHub Pages. In the repo's **Settings → Pages**, the
source must be set to **GitHub Actions**.

Zensical is pre-1.0 and pinned in `requirements.txt`. Before upgrading,
build and check the site locally.
