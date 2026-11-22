# heygoodbuddy.com

## Parallel sessions

More than one Claude session often works on this repo at once. Keep them
apart:

- **One worktree per session.** Before editing, work in your own worktree
  and branch, not the main checkout:
  `git worktree add ../heygoodbuddy.com-<topic> -b <topic>` (or start the
  session with `claude --worktree`). The main checkout `C:\git\heygoodbuddy.com`
  stays on `main` for pulling and merging.
- **Stay in your lane.** Edit only your game's folders: `docs/games/<slug>/`,
  `data/<slug>/`, `notes/<slug>/`. The shared files (`mkdocs.yml` nav,
  `docs/games/index.md`, `docs/stylesheets/`, `docs/javascripts/`,
  `overrides/`) get small, targeted edits only.
- **In the main checkout, never** switch branches, stash, reset, clean or
  `git add -A`/`git add .`. Stage files by path.
- **Finishing:** commit on your branch, `git rebase main`, then from the main
  checkout `git merge --ff-only <topic>`, and `git worktree remove` the folder.
- **Preview ports:** a second session previewing at the same time uses
  `zensical serve -a 127.0.0.1:8001` (8002, ...), never 8080.

## Local preview ports

This repo is worked on from levia, where port 8080 belongs to levia-web, the
always-on home-network site (see `hosts/levia/web` in network-config). Never
bind 8080 here.

- `zensical serve` uses `127.0.0.1:8000` (`dev_addr` in `mkdocs.yml`).
- For one-off static checks, use `python3 -m http.server 8765 --bind 127.0.0.1`.
- To preview from a phone, use `zensical serve -a 0.0.0.0:8000` and a ufw rule
  for 8000 from `192.168.0.0/24`, never 8080.
