import json,re,sys,collections
c=json.load(open('inv/catalog.json')); A=json.load(open('inv/areas.json')); H=json.load(open('inv/rpg_hits.json'))
cat={}
for r in c['items']: cat[r['name']]=r
for r in c['equip']: cat[r['name']]=r   # equipment wins (Cursed Ring accessory)
src=collections.defaultdict(list)
def add(n,s):
    if n not in cat: print('UNKNOWN',repr(n),file=sys.stderr); return
    if s not in src[n]: src[n].append(s)

# 1. shops
for n,v in json.load(open('inv/src_shops.json')).items():
    for kind,label in v: add(n,label)

# 2. RPG Site hits
PLACE={'Earth Shrine':'Earth Shrine','World Map - Kingdom of Grandshelt':'Grandshelt world map','Mitra':'Town of Mitra',
'Grandshelt (Event)':'Grandshelt Castle','Grandshelt (Town)':'Grandshelt','World Map':'Grandshelt world map (desert)',
'Kol':'Village of Kol','World Map - Kingdom of Grandshelt (Desert)':'Grandshelt world map (desert)',
'Grandport Harbor':'Grandport Harbor','World Map - Kingdom of Grandshelt (SE section)':'Grandshelt world map (Felicitas island)',
'Felicitas':'Town of Felicitas','Kolobos Ruins':'Kolobos Ruins','Grandport':'Grandport Harbor','Siren’s Tower':"Siren's Tower",
'Dilmagia':'Dilmagia','Mt. Thunderclap':'Mt. Thunderclap','World Map - Dirnado, the Continent of Wind':'Dirnado world map',
'Dwarven Forge':'Dwarven Forge','Mobliz Shipyard':'Mobliz Shipyard','Wind Shrine':'Wind Shrine',
'World Map - Olderion Federation (South)':'Olderion world map (south)','Olderion - The Aquapolis':'Olderion','Cave of Waters':'Cave of Waters',
'Olderion - Old Town':'Old Town, Olderion','Lake Dorr':'Lake Dorr','Waterfall Way':'Waterfall Way','Town of Amore':'Town of Amore',
'World Map - Olderion Federation (North)':'Olderion world map (north)','Water Shrine':'Water Shrine','Mozul Station':'Mozul Station',
'World Map - Zoldaad Empire Territory':'Zoldaad world map','Grandshelt':'Grandshelt Castle (Chapter 4)',
'Grandshelt Colosseum -- Fledgling League':'Colosseum','Zoldaad, the Imperial Capital':'Zoldaad, the Imperial Capital'}
SKIP=re.compile(r'man east of the colosseum|Female Researcher|sells|Drops|Can steal|steal|dropping|Tablet Shard Note|Throughout|separate page|Oblivion Palace|give it|Give him|Hold onto|Gaia Hammer from|Ruby Fragment|Ruby Cave|Active Time Chat|Return to Ruby|also adds|Battle \d|After clearing|have Arcana|have Astral|has Guardian|Rewards are|Rewards:|reward of|earn|Jump|gives you|give you|Return to Verun|Super Salubrious|Blood Dragon|Rushroom|Tablet Shard \(|white sparkle',re.I)
for n,s,l in H:
    if n in ('Tablet Shard','Magicite Shard','Magicite','Ruby Fragment','Adamantite','Fledgling\'s Proof of Victory','Gaia Hammer','Dew of Reprieve'): continue
    if SKIP.search(l) and not (n in ('Phoenix Down',) and 'Event battle' in l): 
        if 'white sparkle' in l: add(n,'Grandshelt world map, on the way to Mitra')
        continue
    p=PLACE[s]
    if l.strip('- ') in ('Moon Saber','Power Wristbands'): p='Mt. Thunderclap'
    if 'dead end E of the Cave of Waters' in l: p='Olderion world map (south)'
    if 'Event battle' in l: add(n,f'{p}: event battle'); continue
    if re.search(r'knight in the NE room|Man in the shop|Woman to NE|Female Researcher',l): add(n,f'{p}: from an NPC'); continue
    add(n,p)
# RPG Site lines skipped by SKIP but that matter
add('Potion','Earth Shrine'); add('Ether','Earth Shrine')
add('Tent','Town of Felicitas')
# manual quest / NPC / special sources
Q=[('Flamberge','Sub quest *Dream of an Idealist* (Grandshelt → Village of Kol)'),
('Monk\'s Prayer Beads','Sub quest *Secrets Unearthed* (Town of Felicitas)'),
('Iwakirimaru','Sub quest *The Weight of Mercy* (Grandport Harbor)'),
('Mist Potion','Town of Felicitas: from the Female Researcher'),
('Mist Hi-Potion','Olderion jump rope: 15 jumps'),('Mist Ether','Olderion jump rope: 20 jumps'),
('Mist X-Potion','Olderion jump rope: 30 jumps'),('Swift Badge','Olderion jump rope: 40 jumps'),
('Lunar Sword','Grandshelt (Chapter 4): the man east of the Colosseum entrance'),('Brigandine','Grandshelt (Chapter 4): the man east of the Colosseum entrance'),
('Ancient Greatsword','Colosseum: first win of Fledgling Battle 3'),('Gaia Hammer','Colosseum: first win of Fledgling Battle 5'),
('Hi-Potion','Colosseum: repeat wins in the Fledgling League'),
('Aquatic Veil','Waterfall Way'),
('Hasaito','Olderion world map (south), west of Ruby Cave'),
('Potion','Grandshelt: from an NPC'),
]
for n,s in Q: add(n,s)
# meowdb chests in visited areas
VIS={'town-of-mitra-2000':'Town of Mitra','earth-shrine-3000':'Earth Shrine','earth-shrine-3001':'Earth Shrine','grandshelt-the-royal-capital-2010':'Grandshelt','commercial-district-2015':'Grandshelt','village-of-kol-2020':'Village of Kol','grandport-harbor-2030':'Grandport Harbor','town-of-felicitas-2040':'Town of Felicitas','kolobos-ruins-3040':'Kolobos Ruins','sirens-tower-3030':"Siren's Tower",'dilmagia-the-machinopolis-2060':'Dilmagia','shipyard-2061':'Dilmagia','mt-thunderclap-3050':'Mt. Thunderclap','dwarven-forge-2050':'Dwarven Forge','mobliz-shipyard-3060':'Mobliz Shipyard','wind-shrine-3070':'Wind Shrine','olderion-the-aquapolis-2070':'Olderion','cave-of-waters-3080':'Cave of Waters','old-town-olderion-3090':'Old Town, Olderion','waterfall-way-3100':'Waterfall Way','town-of-amore-2090':'Town of Amore','water-shrine-3110':'Water Shrine','zoldaad-the-imperial-capital-2110':'Zoldaad, the Imperial Capital','imperial-residences-2113':'Zoldaad, the Imperial Capital'}
for k,place in VIS.items():
    for ch in A[k]['chests']:
        m=re.match(r'(.*?) x [\d,]+$',ch)
        if not m or m.group(1) in ('Gil','Magicite Shard','Magicite'): continue
        add(m.group(1),place)
# Tablet Shard boxes
for k,n in [(3,'Vitality Charm'),(6,'Earrings'),(12,'Stagger Ring'),(16,'Dreadwing Mallet'),(20,'Compound Bow'),(28,'Astral Jacket'),(32,'Cure Drop'),(36,'Celaeno Fragments'),(44,'Phantom Robe'),(48,'Repeater Rifle')]:
    add(n,f'Tablet Shard box: {k} shards')

# 3. bestiary drops/steals (simple parser)
cur=None; ents=[]
for line in open('/home/spowell/git/heygoodbuddy.com/data/final-fantasy-resonance/bestiary.yaml'):
    m=re.match(r'\s+- name: (.*)',line)
    if m: cur={'name':m.group(1).strip().strip('"')}; ents.append(cur); continue
    m=re.match(r'\s+(boss|drops|steals): (.*)',line)
    if m and cur is not None: cur[m.group(1)]=m.group(2).strip().strip('"')
for e in ents:
    for kind in ('drops','steals'):
        v=e.get(kind,'')
        if not v: continue
        for it in v.split(' · '):
            rare='(rare)' in it; it=it.replace('(rare)','').strip()
            it=re.sub(r' x\d+$','',it)
            if it in ('Gil',): continue
            verb={'drops':'Drop','steals':'Steal'}[kind]
            if e.get('boss')=='true' and kind=='drops': verb='Boss drop'
            add(it,f"{verb}: {e['name']}"+(' (rare)' if rare else ''))
json.dump(src,open('inv/src_all.json','w'),indent=0)
print(len(src))
