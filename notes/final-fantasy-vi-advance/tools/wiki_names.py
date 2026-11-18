"""Match the FF6 guide's monsters to the FF Wiki's names per version.

usage: python3 -I build.py <data.json>   (reads pages.json, bestiary.wiki)
writes names.json: {guide name: {page, snes, ps, ios, pr, wgba}}
"""
import json, re, sys

W = open('bestiary.wiki').read()
P = json.load(open('pages.json'))
D = json.load(open(sys.argv[1]))


def norm(t):
    t = t.replace('_', ' ').strip()
    return t[:1].upper() + t[1:]


P = {norm(k): v for k, v in P.items()}


def boxes(c):
    out = []
    for m in re.finditer(r'\{\{\s*infobox enemy stats FFVI', c, flags=re.I):
        i, depth = m.end(), 1
        while depth and i < len(c):
            if c.startswith('{{', i):
                depth += 1; i += 2
            elif c.startswith('}}', i):
                depth -= 1; i += 2
            else:
                i += 1
        f = {}
        for line in re.split(r'\n\s*\|', c[m.end():i - 2]):
            if '=' in line:
                k, v = line.split('=', 1)
                f[k.strip().lower()] = v.strip()
        out.append(f)
    return out


def variants(page):
    vs = []
    for f in boxes(P.get(page, '')):
        if 'gba' in f or 'snes' in f:
            vs.append({k: f.get(k) for k in ('snes', 'ps', 'gba', 'ios')})
        for n in range(1, 9):
            if f'{n} gba' in f or f'{n} snes' in f:
                vs.append({k: f.get(f'{n} {k}') for k in ('snes', 'ps', 'gba', 'ios')})
    return vs


def section(h):
    i = W.find(h)
    j = W.find('\n== ', i + 5)
    return W[i:j if j > 0 else None]


def links(s):
    out = []
    for line in s.split('\n'):
        m = re.match(r'\s*(?:#|<li>)\s*\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', line)
        if m:
            out.append((norm(m.group(1)), (m.group(2) or m.group(1)).strip()))
    return out


def clean(s):
    if not s:
        return None
    s = re.sub(r'<br\s*/?>', ' / ', s)
    s = re.sub(r'\[\[[^\]|]+\|([^\]]+)\]\]', r'\1', s)
    s = re.sub(r'\[\[([^\]|]+?)(?: \([^)]*\))?\]\]', r'\1', s)
    s = re.sub(r"''+", '', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\{\{[^}]*\}\}', '', s).strip()
    return s or None


base = lambda s: re.sub(r'\s*\(.*?\)\s*', '', s or '').strip().lower()

gba = links(section('== Bestiary (Game Boy Advance) =='))
pr = links(section("== Bestiary (''Pixel Remaster'') =="))
prBy = {}
for p, n in pr:
    prBy.setdefault(p, []).append(n)
gbaPage = {}
for p, n in gba:
    gbaPage.setdefault(base(n), p)

# GBA entries per page, in bestiary order, to line up with PR entries.
order = {}
for m in sorted((m for m in D['monsters'] if m.get('bestiary')), key=lambda m: m['bestiary']):
    if m['bestiary'] <= len(gba):
        order.setdefault(gba[m['bestiary'] - 1][0], []).append(m['name'])

out, miss = {}, []
for m in D['monsters']:
    page = None
    if m.get('bestiary') and m['bestiary'] <= len(gba):
        page = gba[m['bestiary'] - 1][0]
    if not page:
        page = gbaPage.get(base(m['name']))
    if not page:
        for t in P:
            if any(base(clean(v.get('gba'))) == base(m['name']) for v in variants(t)):
                page = t
                break
    if not page:
        miss.append((m['name'], 'no page'))
        continue
    src = page
    vs = variants(page)
    for alt in (f"{page}/{m.get('bestiary')}", f'{page} (Final Fantasy VI)', f'{page} (Final Fantasy VI boss)'):
        if not vs and alt in P:
            src, vs = alt, variants(alt)
    if not vs:
        miss.append((m['name'], page))
        continue
    v = next((v for v in vs if base(clean(v.get('gba'))) == base(m['name'])), None)
    if v is None:
        sib = order.get(page, [])
        k = sib.index(m['name']) if m['name'] in sib else 0
        v = vs[min(k, len(vs) - 1)]
    prs = prBy.get(page) or prBy.get(src) or []
    sib = order.get(page, [m['name']])
    k = sib.index(m['name']) if m['name'] in sib else 0
    prn = prs[k] if k < len(prs) else (prs[0] if prs else None)
    out[m['name']] = {'page': src, 'snes': clean(v.get('snes')), 'ps': clean(v.get('ps')),
                      'wgba': clean(v.get('gba')), 'ios': clean(v.get('ios')), 'pr': prn}
json.dump(out, open('names.json', 'w'), ensure_ascii=False, indent=0)
print('matched', len(out), 'missing', len(miss), miss)
