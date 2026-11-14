# heygoodbuddy.com

## Local preview ports

This repo is worked on from levia, where port 8080 belongs to levia-web, the
always-on home-network site (see `hosts/levia/web` in network-config). Never
bind 8080 here.

- `zensical serve` uses `127.0.0.1:8000` (`dev_addr` in `mkdocs.yml`).
- For one-off static checks, use `python3 -m http.server 8765 --bind 127.0.0.1`.
- To preview from a phone, use `zensical serve -a 0.0.0.0:8000` and a ufw rule
  for 8000 from `192.168.0.0/24`, never 8080.
