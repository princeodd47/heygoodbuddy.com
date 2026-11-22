# heygoodbuddy.com

## Public repo: Flesh and Blood and Articles only

This repo is **public**. It holds only Flesh and Blood
(`docs/games/flesh-and-blood/`, `data/`, `notes/`, images, `fab-*` scripts)
and the articles (`docs/blog/`). Every other game lives in the private repo
`princeodd47/heygoodbuddy-private` (local checkout `C:\git\heygoodbuddy-private`).

- Never add another game, its notes, data or images here. Work on them in the
  private repo.
- `scripts/public_check.py` holds the allowlist; the deploy stops on anything
  else. Add a path to it only when the user says that content is public.
- Shared theme files (`overrides/main.html`, `field-guide.css`, `fg-*.js`,
  `extra.css`) exist in both repos. A theme fix made here may need copying to
  the private repo too; ask.

## Parallel sessions

More than one Claude session often works on this repo at once. Keep them
apart:

- **One worktree per session.** Before editing, work in your own worktree
  and branch, not the main checkout:
  `git worktree add ../heygoodbuddy.com-<topic> -b <topic>` (or start the
  session with `claude --worktree`). The main checkout `C:\git\heygoodbuddy.com`
  stays on `main` for pulling and merging.
- **Stay in your lane.** Edit only the folders for your task. The shared files
  (`mkdocs.yml` nav, `docs/stylesheets/`, `docs/javascripts/`, `overrides/`)
  get small, targeted edits only.
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
