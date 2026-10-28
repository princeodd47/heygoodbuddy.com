# heygoodbuddy.com

Source for [heygoodbuddy.com](https://heygoodbuddy.com/): game guides, notes
and articles, built with [Zensical](https://zensical.org/). Site settings live in
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

## Layout

```
docs/
  index.md                 # home page
  games/
    index.md               # games hub, one card per game
    <game>/                # one folder per game
  blog/posts/              # articles (need a date in frontmatter)
  tags.md                  # auto-generated tag index
  CNAME                    # custom domain for GitHub Pages
data/<game>/               # YAML data used to build tables
scripts/                   # helper scripts, e.g. fab_cards.py (Flesh and Blood card data)
```

## Adding things

- **New game:** add a folder under `docs/games/`, a card on
  `docs/games/index.md`, and its pages to `nav` in `mkdocs.yml`.
- **New article:** add a Markdown file to `docs/blog/posts/` with a `date`
  in its frontmatter. It's listed automatically.
- **New data table:** add a YAML file under `data/` and register it under
  `include_yaml` in `mkdocs.yml`. The file's top level must be a mapping
  (e.g. `visions:` followed by the list), not a bare list. A wrong path is
  skipped silently, so an empty table usually means a typo in the path.

## Deploying

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site
and publishes it with GitHub Pages. In the repo's **Settings → Pages**, the
source must be set to **GitHub Actions**.

Zensical is pre-1.0 and pinned in `requirements.txt`. Before upgrading,
build and check the site locally.
