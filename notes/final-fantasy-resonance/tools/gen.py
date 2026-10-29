import json,re,collections
c=json.load(open('inv/catalog.json')); src=json.load(open('inv/src_all.json'))
for b in ('Mindflayer (Olderion world map, north)','Gogmagog (Zoldaad world map)','Pyroviper (Zoldaad world map)'):
    src['Mist Turbo Ether'].append('Boss drop: '+b)
cat={}
for r in c['items']: cat[r['name']]=r
for r in c['equip']: cat[r['name']]=r
ORDER=['Earth Shrine','Grandshelt world map, on the way','Town of Mitra','Grandshelt world map','Grandshelt Castle (Chapter 4)','Grandshelt Castle','Grandshelt Commercial District','Grandshelt','Village of Kol','Grandshelt world map (desert)','Grandport Harbor','Grandshelt world map (Felicitas island)','Town of Felicitas','Kolobos Ruins',"Siren's Tower",'Marauder Cave','Dilmagia','Mt. Thunderclap','Dirnado world map','Dwarven Forge','Shoggoth Cave','Mobliz Shipyard','Wind Shrine','Olderion world map (south)','Rukh Cave','Olderion jump rope: 1','Olderion','Cave of Waters','Old Town, Olderion','Lake Dorr','Waterfall Way','Town of Amore','Olderion world map (north)','Mindflayer','Water Shrine','Olderion jump rope','Mozul Station','Zoldaad world map','Gogmagog','Pyroviper','Capital Station','Colosseum','Zoldaad','Capital Market','Slums']
# fix: chapter-4 castle and jump rope 30+ placed late
def prank(label):
    l=re.sub(r'^(Shop|Drop|Steal|Boss drop): ','',label)
    if l.startswith('Grandshelt Castle (Chapter 4)') or l.startswith('Grandshelt (Chapter 4)'): return ORDER.index('Colosseum')
    if l.startswith('Olderion jump rope'):
        n=int(re.search(r'(\d+) jumps',l).group(1)); return ORDER.index('Olderion') if n<=20 else ORDER.index('Mozul Station')
    if l.startswith('Sub quest'):
        l=re.search(r'\((.*)\)',l).group(1)
    if l.startswith('Tablet Shard box'):
        n=int(re.search(r'(\d+) shards',l).group(1)); return SHARD[n]
    if label.startswith(('Drop','Steal','Boss drop')) and l.split(' (')[0] in ENEMY: return ENEMY[l.split(' (')[0]]
    for i,k in sorted(enumerate(ORDER),key=lambda x:-len(x[1])):
        if l.startswith(k): return i
    print('NORANK',label); return 99
# bestiary groups -> ORDER index
GMAP={'Grandshelt Castle':'Grandshelt Castle','Earth Shrine':'Earth Shrine','Grandshelt (World Map)':'Grandshelt world map','Grandport (World Map)':'Grandport Harbor','Kolobos (World Map)':'Grandshelt world map (Felicitas island)','Kolobos Ruins':'Kolobos Ruins',"Siren's Tower":"Siren's Tower",'Marauder Cave':'Marauder Cave','Dirnado (World Map)':'Dirnado world map','Mt. Thunderclap':'Mt. Thunderclap','Dwarven Forge':'Dwarven Forge','Shoggoth Cave':'Shoggoth Cave','Mobliz Shipyard':'Mobliz Shipyard','Wind Shrine':'Wind Shrine','Olderion (World Map)':'Olderion world map (south)','Rukh Cave':'Rukh Cave','Cave of Waters':'Cave of Waters','Old Town, Olderion':'Old Town, Olderion','Lake Dorr':'Lake Dorr','Waterfall Way':'Waterfall Way','Olderion (World Map, around Amore)':'Olderion world map (north)','Water Shrine':'Water Shrine','Zoldaad (World Map)':'Zoldaad world map','Colosseum (Fledgling League)':'Colosseum'}
ENEMY={}; g=None
for line in open('/home/spowell/git/heygoodbuddy.com/data/final-fantasy-resonance/bestiary.yaml'):
    m=re.match(r'  - area: (.*)',line)
    if m: g=m.group(1).strip().strip('"'); continue
    m=re.match(r'\s+- name: (.*)',line)
    if m:
        n=m.group(1).strip().strip('"'); ENEMY.setdefault(n,ORDER.index(GMAP[g]))
SA=['Grandshelt Commercial District','Village of Kol','Grandport Harbor','Grandport Harbor','Grandshelt world map (desert)','Town of Felicitas','Town of Felicitas','Kolobos Ruins','Kolobos Ruins',"Siren's Tower","Siren's Tower","Siren's Tower",'Dilmagia','Dilmagia','Dilmagia','Dilmagia','Mt. Thunderclap','Mt. Thunderclap','Mt. Thunderclap','Dwarven Forge','Dwarven Forge','Mobliz Shipyard','Mobliz Shipyard','Mobliz Shipyard','Wind Shrine','Wind Shrine','Wind Shrine','Olderion','Olderion','Olderion','Olderion','Cave of Waters','Cave of Waters','Cave of Waters','Waterfall Way','Waterfall Way','Waterfall Way','Town of Amore','Town of Amore','Water Shrine','Water Shrine','Water Shrine','Mozul Station','Capital Station','Zoldaad','Zoldaad','Zoldaad','Colosseum']
SHARD={i+1:ORDER.index(a) for i,a in enumerate(SA)}
def rank(n): return min(prank(s) for s in src[n])

def clean(d): return re.sub(r'\s*\n\s*',' ',d or '').strip()
def esc(s): return json.dumps(s,ensure_ascii=False)
def where_equip(n):
    out=[]
    for s in sorted(src[n],key=prank):
        out.append(s)
    return out
def fmt_where_item(n):
    S=src[n]; shops=[s for s in S if s.startswith('Shop: ')]
    found=[s for s in S if not s.startswith(('Shop: ','Drop: ','Steal: ','Boss drop: '))]
    fights=[s for s in S if s.startswith(('Drop: ','Steal: ','Boss drop: '))]
    buy=''
    if shops:
        prices=collections.defaultdict(list)
        for s in shops:
            m=re.match(r'Shop: (.*?)(?: \(([^)]*)\))?( after the Fledgling League)?$',s)
            place,pr,after=m.group(1),m.group(2) or '',m.group(3) or ''
            prices[pr].append(place+after)
        buy=' · '.join(f"{pr}: {', '.join(sorted(set(p),key=lambda x:prank(x)))}" for pr,p in sorted(prices.items(),key=lambda kv:int(re.sub(r'\D','',kv[0].split(';')[0]) or 0)))
    other=sorted(set(found),key=prank)
    if not shops or len(fights)<=4:
        other+= sorted(fights,key=prank)
    return buy,other
STATS=[('Physical attack','Atk'),('Magic attack','Mag'),('Physical defense','Def'),('Magic defense','M.Def'),('HP','HP'),('MP','MP'),('Speed','Speed'),('Sanctity','Sanctity'),('Stamina','Stamina')]
def statstr(r,skip=()):
    return ' · '.join(f"{lab} {v:+d}" if lab in ('Speed',) and v<0 else f"{lab} {v}" for k,lab in STATS if k not in skip for v in [r['stats'].get(k)] if v)
eq=collections.defaultdict(list); acc=[]; cons=[]
for n in src:
    r=cat[n]; k=r['category']
    if k=='Weapon' or k=='Armor':
        eq[(k,r['attributes'].get('Type'))].append(n)
    elif k=='Accessory': acc.append(n)
    elif k=='Consumable': cons.append(n)
WT=[('Greatsword','Greatswords','Rain'),('Katana','Katanas','Lasswell'),('Bow','Bows','Fina'),('Whip','Whips','Archwitch Fina'),('Hammer','Hammers','Lid'),('Grimoire','Grimoires','Nichol'),('Gun','Guns',''),('Rod','Rods','')]
AT=[('Heavy Armor','Heavy armor','Rain, Lasswell, Lid'),('Light Armor','Light armor','everyone'),('Robe','Robes','Fina, Archwitch Fina, Nichol')]
L=['# Generated from NiaDB (meowdb.com) data; see notes/final-fantasy-resonance/equipment-research.md','weapons:']
def item_lines(n,ind,kind):
    r=cat[n]; o=[f"{ind}- name: {esc(n)}"]
    if kind=='weapon':
        o.append(f"{ind}  atk: {r['stats'].get('Physical attack',0)}"); o.append(f"{ind}  mag: {r['stats'].get('Magic attack',0)}")
        o.append(f"{ind}  other: {esc(statstr(r,('Physical attack','Magic attack')))}")
    elif kind=='armor':
        o.append(f"{ind}  def: {r['stats'].get('Physical defense',0)}"); o.append(f"{ind}  mdef: {r['stats'].get('Magic defense',0)}")
        o.append(f"{ind}  other: {esc(statstr(r,('Physical defense','Magic defense')))}")
    elif kind=='acc':
        o.append(f"{ind}  other: {esc(statstr(r))}")
    o.append(f"{ind}  effect: {esc(clean(r['description']))}")
    o.append(f"{ind}  where: {esc('<br>'.join(where_equip(n)))}")
    return o
for t,h,who in WT:
    ns=sorted(eq.get(('Weapon',t),[]),key=lambda n:(rank(n),n))
    if not ns: continue
    L+= [f"  - type: {esc(h)}",f"    who: {esc(who)}","    entries:"]
    for n in ns: L+=item_lines(n,'      ','weapon')
L.append('armor:')
for t,h,who in AT:
    ns=sorted(eq.get(('Armor',t),[]),key=lambda n:(rank(n),n))
    L+= [f"  - type: {esc(h)}",f"    who: {esc(who)}","    entries:"]
    for n in ns: L+=item_lines(n,'      ','armor')
L.append('accessories:')
for n in sorted(acc,key=lambda n:(rank(n),n)): L+=item_lines(n,'  ','acc')
open('inv/equipment.yaml','w').write('\n'.join(L)+'\n')
# items
GROUPS=[('Healing',['Potion','Mist Potion','Hi-Potion','Mist Hi-Potion','X-Potion','Mist X-Potion','Healing Spring','Ether','Mist Ether','Turbo Ether','Mist Turbo Ether','X-Ether','Elixir','Tent']),
('Revival',['Phoenix Down','Phoenix Pinion']),
('Status cures',['Antidote Herb','Eye Drops','Echo Herb','Herb of Awakening','Unicorn Horn','Smelling Salts','Gold Needle','Remedy']),
('Scrolls',['Flame Scroll I','Flame Scroll II','Ice Scroll I','Ice Scroll II','Wind Scroll I','Wind Scroll II','Earth Scroll I','Earth Scroll II','Lightning Scroll I','Lightning Scroll II','Water Scroll I','Water Scroll II']),
('Knives and shuriken',['Knife of Poison','Knife of Blind','Knife of Silence','Knife of Sleep','Knife of Paralysis','Knife of Confuse','Shuriken','Fuma Shuriken']),
('Other',['Smoke Bomb','Small Golden Shell'])]
allg=sum((g for _,g in GROUPS),[])
miss=[n for n in cons if n not in allg]; assert not miss,miss
def fights_str(fights):
    d=collections.OrderedDict([('Boss drop',[]),('Drop',[]),('Steal',[])])
    for s in sorted(fights,key=prank):
        k,v=s.split(': ',1); d[k].append(v)
    lab={'Boss drop':'Boss drops','Drop':'Drops','Steal':'Steals'}
    return [f"{lab[k]}: {', '.join(v)}" for k,v in d.items() if v]
def fmt_where_item(n):
    S=src[n]; shops=[s for s in S if s.startswith('Shop: ')]
    found=sorted(set(s for s in S if not s.startswith(('Shop: ','Drop: ','Steal: ','Boss drop: '))),key=prank)
    fights=[s for s in S if s.startswith(('Drop: ','Steal: ','Boss drop: '))]
    prices=collections.defaultdict(list)
    for s in shops:
        m=re.match(r'Shop: (.*?)(?: \(([^)]*)\))?( after the Fledgling League)?$',s)
        prices[m.group(2) or ''].append(m.group(1)+(m.group(3) or ''))
    parts=[]
    for pr,pl in sorted(prices.items(),key=lambda kv:int(re.sub(r'\D','',kv[0].split(';')[0]) or 0)):
        pl=sorted(set(pl),key=prank)
        txt='most item shops' if len(pl)>=6 else ', '.join(pl)
        parts.append(f"{txt} ({pr})")
    buy='<br>'.join(parts)
    other=found+([] if shops else fights_str(fights))
    return buy,other
I=['# Generated from NiaDB (meowdb.com) data; see notes/final-fantasy-resonance/items-research.md','groups:']
for g,ns in GROUPS:
    ns=[n for n in ns if n in cons]
    I+=[f"  - group: {esc(g)}","    entries:"]
    for n in ns:
        r=cat[n]; buy,other=fmt_where_item(n)
        I+=[f"      - name: {esc(n)}",f"        effect: {esc(clean(r['description']))}",f"        buy: {esc(buy)}",f"        found: {esc('<br>'.join(other))}"]
open('inv/items.yaml','w').write('\n'.join(I)+'\n')
print(sum(len(v) for v in eq.values()),len(acc),len(cons))
