# Builds data/final-fantasy-x-2/*.yaml from saved Jegged pages.
# usage: python3 -I build_data.py <download dir> <repo data dir>
# The download dir holds jeg_Accessories.html, jeg_Creature-Creator_*.html.
# YAML is written as JSON flow mappings, which YAML reads fine.
import html, json, os, re, sys

src, out = sys.argv[1], sys.argv[2]


def read(name):
    return open(os.path.join(src, name), encoding='utf-8').read()


def txt(s, br='; '):
    s = re.sub(r'<br\s*/?>', br, s)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip().replace(' ,', ',').replace(' .', '.').replace(' ;', ';').replace('( ', '(').replace(' )', ')').replace(' \u2019s', '\u2019s')


def rows(fragment):
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', fragment, flags=re.S):
        c = [txt(re.sub(r'</a>\s*<a', '</a><br><a', x)) for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, flags=re.S)]
        if c:
            yield c


def dump(path, header, key, items):
    with open(os.path.join(out, path), 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(f'{key}:\n')
        for i in items:
            f.write('  - ' + json.dumps(i, ensure_ascii=False) + '\n')


# Feeding table: items and accessories a creature can eat.
dev = read('jeg_Creature-Creator_Develop-Creature.html')
feed_items, feed_acc = [], {}
section = None
for c in rows(dev):
    if c[0] in ('Item', 'Accessory'):
        section = c[0]
        continue
    name, qty, teaches, typ, gain = (c + [''] * 5)[:5]
    e = {'name': name, 'qty': int(qty), 'teaches': teaches, 'type': typ, 'gain': gain}
    if section == 'Item':
        feed_items.append(e)
    else:
        feed_acc[name] = e
dump('feeding.yaml',
     '# Items a creature can eat in Develop Creature, from Jegged\'s Develop Creature page.\n'
     '# qty is how many it eats at once. See notes/final-fantasy-x-2/creature-team-research.md.\n',
     'items', feed_items)

# Accessories.
acc_html = read('jeg_Accessories.html')
labels = {'Treasure': 'Chest', 'Buy': 'Buy', 'Steal': 'Steal', 'Drop': 'Drop', 'Bribe': 'Bribe',
          'Prize': 'Prize', 'Gift': 'Gift', 'Other': 'Other'}
accs, seen, cat = [], set(), None
for m in re.finditer(r'<h3 id="[^"]+">(.*?)</h3>|<div[^>]*class="alert-heading">(.*?)</div>(.*?)</dl>', acc_html, flags=re.S):
    if m.group(1):
        cat = txt(m.group(1))
        continue
    name = txt(m.group(2))
    if name in seen:
        continue
    seen.add(name)
    d = {}
    where = []
    for k, v in re.findall(r'<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>', m.group(3), flags=re.S):
        k = txt(k).rstrip(':')
        if k == 'Acquisition':
            for typ, ul in re.findall(r'<strong>([^<]+):</strong>\s*<ul>(.*?)</ul>', v, flags=re.S):
                lis = [txt(li) for li in re.findall(r'<li>(.*?)</li>', ul, flags=re.S)]
                if lis:
                    where.append(f"*{labels.get(typ, typ)}:* " + '; '.join(lis))
        else:
            d[k] = txt(v)
    f = feed_acc.get(name)
    feed = ''
    cc = d.get('Creature Creator', '')
    mm = re.match(r'Consume (\d+) to teach a creature (.+?)\.?$', cc)
    if not f and mm:
        feed = f"{mm.group(1)}: {mm.group(2)}"
    if f:
        bits = [b for b in (f['teaches'], f['gain']) if b]
        feed = f"{f['qty']}: " + ', '.join(bits)
    accs.append({'name': name, 'category': cat, 'effect': d.get('Effect', ''),
                 'feed': feed, 'sell': d.get('Sell Price', '').replace(' Gil', ''),
                 'where': '<br>'.join(where).replace('|', '/')})
cats = ['Attribute', 'Elemental', 'Status effect', 'Ability', 'Special']
with open(os.path.join(out, 'accessories.yaml'), 'w', encoding='utf-8') as fh:
    fh.write('# Accessories by Jegged category. Effects, sell prices and sources from Jegged\'s\n'
             '# accessory list; feed from its Develop Creature table.\n'
             '# See notes/final-fantasy-x-2/accessories-research.md.\n')
    fh.write('categories:\n')
    for c in cats:
        fh.write(f'  - name: {json.dumps(c)}\n    accessories:\n')
        for a in accs:
            if a['category'] == c:
                a = {k: v for k, v in a.items() if k != 'category'}
                fh.write('      - ' + json.dumps(a, ensure_ascii=False) + '\n')

def chap(c):
    n = [int(x) for x in c.split()]
    if len(n) > 1 and n == list(range(n[0], n[-1] + 1)):
        return f"Ch. {n[0]}\u2013{n[-1]}"
    return 'Ch. ' + ', '.join(map(str, n))


def tidy(note):
    # "S Ch. 5, Before X" means that pod only works in Ch. 5 before X.
    m = re.match(r'^((?:S|M|L|SP)(?: (?:S|M|L|SP))*) (Ch\. [\d-]+)(?:, (.+))?$', note)
    if m:
        rest = f", {m.group(3)[0].lower()}{m.group(3)[1:]}" if m.group(3) else ''
        rest = rest.replace('Hollow Starts', 'Hollow starts').replace('Starting', 'starting').replace('Complete', 'complete')
        rest = rest.replace('; Before', '; before').replace('; After', '; after')
        return f"{m.group(1).replace(' ', '/')} only in {m.group(2).replace('-', chr(8211))}{rest}"
    m = re.match(r'^((?:S|M|L|SP)(?: (?:S|M|L|SP))*) (Before|After) (.+)$', note)
    if m:
        return f"{m.group(1).replace(' ', '/')} only {m.group(2).lower()} {m.group(3)}"
    note = note.replace('Hollow Starts', 'Hollow starts').replace('Starting', 'starting').replace('Complete', 'complete')
    note = note.replace('; Before', '; before').replace('; After', '; after')
    return note[0].lower() + note[1:] if note[:6] in ('Before', 'After ') else note


# Creatures: where each can be trapped.
trap = read('jeg_Creature-Creator_Trap-Creature.html')
panes = re.split(r'<div[^>]*id="([A-Za-z-]+)-Pane"', trap)
pretty = {'Miihen-Highroad': 'Mi’ihen Highroad', 'Mt-Gagazet': 'Mt. Gagazet'}
order = []
by = {}
size_of = {}
for i in range(1, len(panes), 2):
    loc, body = panes[i], panes[i + 1]
    for c in rows(body):
        if c[0] == 'Creature':
            continue
        name, pods, sp, chapters, notes = (c + [''] * 5)[:5]
        if loc == 'Full-Alphabetical-List':
            size_of[name] = pods
            continue
        place = pretty.get(loc, loc.replace('-', ' '))
        if name not in by:
            by[name] = []
            order.append(name)
        pod = pods.replace(' ', '/')
        if sp:
            pod = pod.replace('SP', f'SP ({sp})')
        s = f"{place}: {pod}, {chap(chapters)}"
        if notes:
            s += f" ({tidy(notes)})"
        by[name].append(s)
creatures = []
for name in sorted(order, key=str.lower):
    pods = size_of.get(name, '')
    size = next((p for p in ('S', 'M', 'L') if p in pods.split()), 'SP')
    creatures.append({'name': name, 'size': size, 'where': '<br>'.join(by[name])})
dump('creatures.yaml',
     '# Where each creature can be trapped, by location, from Jegged\'s Trap Creature page.\n'
     '# size is the Trap Pod size; SP-only creatures (mostly people) say SP.\n',
     'creatures', creatures)

def team_unlock(u):
    for w, n in (('once', '1 win'), ('twice', '2 wins'), ('three times', '3 wins'), ('four times', '4 wins')):
        u = u.replace(f'Win this cup {w}', n)
    return u.replace('; Release', ', and release').replace('Release', 'release')


# Our own wording for each cup's unlock.
UNLOCK = {
    'Standard Cup': 'Open from the start.',
    'Standard Cup: Hard': 'Win the Standard Cup 3 times.',
    'Grand Cup': 'Win Standard Cup: Hard once.',
    'Grand Cup: Hard': 'Win the Grand Cup 3 times.',
    'Chocobo Cup': 'Win Grand Cup: Hard once. A Chocobo must be in your party to enter.',
    'Cactuar Cup': 'Win Grand Cup: Hard 4 times. A Cactuar must be in your party to enter.',
    'Youth League Tournament': 'Win Grand Cup: Hard 6 times.',
    'Aeon Cup': 'Finish and release all eight fiends with a Fayth fragment (see Creatures).',
    'Fiend World Cup': 'Finish the Daeva and Tomb chains, win the Fiend Portal and recruit Omega Weapon (see the team guide).',
    'Farplane Cup': 'Win every other cup.',
}


# Fiend Arena cups.
arena = read('jeg_Creature-Creator_Fiend-Arena.html')
start = arena.find('Fiend Arena Tournaments')
end = arena.find('Recruiting Characters')
parts = re.split(r'<h3[^>]*>(.*?)</h3>', arena[start:end], flags=re.S)
cups = []
for i in range(1, len(parts), 2):
    name = txt(parts[i])
    body = parts[i + 1]
    info = {}
    teams = []
    for c in rows(body):
        if c[0] in ('Unlock Requirements', 'Prizes'):
            info[c[0]] = c[1]
        elif c[0] != 'Team':
            teams.append({'team': c[0], 'members': c[1].replace('; ', ', '), 'unlock': team_unlock(c[2] if len(c) > 2 else '')})
    prizes = re.sub(r'(\d+) (st|nd|rd|th) win:', r'\1\2 win:', info.get('Prizes', ''))
    prizes = prizes[prizes.find('1st win') if '1st win' in prizes else 0:]
    prizes = [x.strip() for x in prizes.split('; ') if x.strip()]
    cups.append({'name': name, 'unlock': UNLOCK.get(name, info.get('Unlock Requirements', '')),
                 'prizes': prizes, 'teams': teams})
dump('arena.yaml',
     '# Fiend Arena cups, prizes and opponent teams, from Jegged\'s Fiend Arena page.\n'
     '# See notes/final-fantasy-x-2/fiend-arena-research.md.\n',
     'cups', cups)
print(len(feed_items), len(accs), len(creatures), len(cups))
