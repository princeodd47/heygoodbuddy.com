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
# Drops the user saw in game that the guides don't list. In-game data wins.
IN_GAME_DROPS = {'Boris': ['Faerie Earrings']}
for a in accs:
    found = [e for e, items in IN_GAME_DROPS.items() if a['name'] in items]
    if found:
        parts = a['where'].split('<br>') if a['where'] else []
        for i, w in enumerate(parts):
            if w.startswith('*Drop:* '):
                parts[i] = w + '; ' + '; '.join(found)
                break
        else:
            parts.append('*Drop:* ' + '; '.join(found))
        a['where'] = '<br>'.join(parts)
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

# Garment Grids, in Jegged's game order.
gg = read('jeg_Garment-Grids_idx.html')
grids, seen = [], set()
for m in re.finditer(r'<div[^>]*class="alert-heading">((?:(?!alert-heading).)*?)</div>((?:(?!alert-heading).)*?)</dl>', gg, flags=re.S):
    name = txt(m.group(1))
    if name in seen:
        continue
    seen.add(name)
    d = {}
    gates = []
    for k, v in re.findall(r'<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>', m.group(2), flags=re.S):
        k = txt(k).rstrip(':')
        if k == 'Gates':
            for colour, ab in re.findall(r'alt="(\w+) Gate Icon"[^>]*>(.*?)</span>', v, flags=re.S):
                gates.append(f"{colour}: {txt(ab)}")
            if not gates:
                gates.append(txt(v))
        else:
            d[k] = txt(v)
    grids.append({'name': name, 'equip': d.get('Equip Ability', ''), 'gates': '<br>'.join(gates),
                  'creature': d.get('Creature Ability', ''), 'chapter': d.get('Chapter', ''),
                  'where': d.get('Acquisition', '').replace('|', '/')})
dump('garment-grids.yaml',
     '# Garment Grids in the order you can first get them, from Jegged\'s Garment Grids list.\n'
     '# See notes/final-fantasy-x-2/garment-grids-research.md.\n',
     'grids', grids)

# Dresspheres: ability lists from Jegged; how to get them is our own wording.
DRESS = [
    ('Warrior', 'Starting Dressphere (Paine).'),
    ('Thief', 'Starting Dressphere (Rikku).'),
    ('Gunner', 'Starting Dressphere (Yuna).'),
    ('Songstress', 'Chapter 1, Luca: Yuna gets it in the opening fight with Leblanc.'),
    ('Festivalist', 'Chapter 1, Celsius: Brother gives it to you on your first visit. HD Remaster and International only.'),
    ('Black Mage', 'Chapter 1, Celsius: Shinra gives it to you after the Mt. Gagazet Floating Ruins.'),
    ('White Mage', 'Chapter 1, Besaid: beat the Flame Dragon in the cave.'),
    ('Gun Mage', 'Chapter 1, Moonflow: finish "Shave the Hypello?" for Tobli. Missed it? Sell at least six of Tobli\'s ten tickets without a loss in Chapter 2.'),
    ('Psychic', 'Fiend Arena: first Standard Cup win. HD Remaster and International only.'),
    ('Alchemist', 'Chapter 2, Calm Lands: the "Clean Sweep" mission at the Chocobo Ranch. Clasko has to reach the Calm Lands first.'),
    ('Dark Knight', 'Chapter 2, Bevelle Underground: a chest at the end of the lift and switch puzzle. It stays there if you miss it.'),
    ('Samurai', 'Chapter 3, Kilika Temple: on the floor after the two Daevas. If you miss it, it\'s in a chest there in Chapter 5.'),
    ('Lady Luck', 'Chapter 3, Luca: win the Sphere Break tournament and beat Shinra. Or beat him in the stadium basement in Chapter 5.'),
    ('Berserker', 'Chapter 3, Lake Macalania: defend the Travel Agency and win six battles in a row. Chapter 3 only.'),
    ('Trainer', 'Chapter 3, Mt. Gagazet: Kimahri gives it if you answered him right in Chapter 2.'),
    ('Mascot', 'Episode Complete in all 15 locations (scene on the Celsius in Chapter 5), or the first Youth League Tournament win in the Fiend Arena.'),
    ('Full Throttle', 'Paine\'s Special. Chapter 1, Macalania Woods: talk to Tromell at the Spring four times. Last chance: the same in Chapter 2.'),
    ('Floral Fallal', 'Yuna\'s Special. Chapter 2, Djose Highroad, during that chapter\'s mission.'),
    ('Machina Maw', 'Rikku\'s Special. Chapter 2, Bikanel Desert: comes in the Oasis mission cutscene.'),
]
dresses = []
for name, how in DRESS:
    page = read(os.path.join('dress', name.replace(' ', '-') + '.html'))
    la = page[page.find('List of Abilities'):]
    la = la[:la.find('<h2')] if '<h2' in la else la
    tabs = [txt(b) for b in re.findall(r'<button[^>]*role="tab"[^>]*>(.*?)</button>', la, flags=re.S)]
    groups = []
    for i, table in enumerate(re.findall(r'<table.*?</table>', la, flags=re.S)):
        abil = []
        for c in rows(table):
            if c[0] == 'Ability':
                continue
            abil.append({'name': c[0], 'ap': c[1], 'needs': c[2] if len(c) > 2 else ''})
        if not tabs and len(re.findall(r'<table', la)) == 3:
            tabs = ['Yuna', 'Rikku', 'Paine']
        groups.append({'who': tabs[i] if i < len(tabs) else '', 'abilities': abil})
    dresses.append({'name': name, 'how': how, 'groups': groups})
dump('dresspheres.yaml',
     '# Dresspheres in the order you can first get them. Ability lists from Jegged\'s\n'
     '# Dressphere pages; "how" is our own wording. See notes/final-fantasy-x-2/dresspheres-research.md.\n',
     'dresspheres', dresses)
print(len(grids), len(dresses))

# Bestiary, from Jegged's enemy pages (saved under enemies/).
ENEMY_DIR = os.path.join(src, 'enemies')
if os.path.isdir(ENEMY_DIR):
    enemies = []
    for fn in sorted(os.listdir(ENEMY_DIR), key=str.lower):
        page = open(os.path.join(ENEMY_DIR, fn), encoding='utf-8').read()
        name = txt(re.search(r'<h1[^>]*>(.*?)</h1>', page, flags=re.S).group(1))
        secs = re.split(r'<h2[^>]*>(.*?)</h2>', page)
        stats_html = secs[0]
        sec = {txt(secs[i]): secs[i + 1] for i in range(1, len(secs), 2)}
        stats = {}
        for c in rows(stats_html):
            if len(c) == 2:
                stats[c[0]] = c[1]
        where = [txt(li) for li in re.findall(r'<li[^>]*>(.*?)</li>', sec.get('Where to Find It', ''), flags=re.S)]
        if not where:
            where = [x for x in txt(re.sub(r'</p>|<br\s*/?>', '\n', sec.get('Where to Find It', ''))).split('\n') if x]
        loot = {'Steal': [], 'Drop': [], 'Bribe': []}
        cur = None
        for c in rows(sec.get('Steals, Drops, and Bribes', '')):
            if c[0] in loot:
                cur = c[0]
                c = c[1:]
            elif c[0] == 'Source':
                continue
            if cur and c and c[0] and c[0] != '—':
                loot[cur].append(c[0])
        el = {}
        for c in rows(sec.get('Elemental Affinities', '')):
            if len(c) == 2 and c[0] != 'Element' and c[1] != 'Normal':
                el.setdefault(c[1], []).append(c[0])

        def pair(lst):
            if not lst:
                return ''
            if len(lst) == 1 or lst[0] == lst[1]:
                return lst[0]
            return f"{lst[0]}; rare: {lst[1]}"

        affin = '; '.join(f"{k}: {', '.join(v)}" for k, v in sorted(el.items()) if k != 'Weak')
        enemies.append({'name': name, 'level': stats.get('Level', ''), 'hp': stats.get('HP', ''),
                        'weak': ', '.join(el.get('Weak', [])), 'other': affin,
                        'steal': pair(loot['Steal']), 'drop': '; also: '.join([pair(loot['Drop'])] + IN_GAME_DROPS.get(name, [])), 'bribe': pair(loot['Bribe']),
                        'where': '<br>'.join(where).replace('|', '/')})
    dump('bestiary.yaml',
         '# Every enemy, alphabetical, from Jegged\'s bestiary pages. Steal and drop give the\n'
         '# common item first, then the rare one. See notes/final-fantasy-x-2/bestiary-research.md.\n',
         'enemies', enemies)
    print(len(enemies))
