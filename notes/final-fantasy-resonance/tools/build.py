import json,re,sys,collections
sys.path.insert(0,'bin')
c=json.load(open('inv/catalog.json')); A=json.load(open('inv/areas.json')); H=json.load(open('inv/rpg_hits.json'))
cat={r['name']:r for r in c['items']+c['equip']}
src=collections.defaultdict(list)
def add(n,s):
    if n not in cat: print('UNKNOWN',n,file=sys.stderr); return
    if s not in src[n]: src[n].append(s)
# shops
shopareas={'town-of-mitra-2000':'Town of Mitra','grandshelt-the-royal-capital-2010':'Grandshelt','commercial-district-2015':'Grandshelt Commercial District','earth-shrine-3001':'Earth Shrine','village-of-kol-2020':'Village of Kol','grandport-harbor-2030':'Grandport Harbor','town-of-felicitas-2040':'Town of Felicitas','dwarven-forge-2050':'Dwarven Forge','dilmagia-the-machinopolis-2060':'Dilmagia','olderion-the-aquapolis-2070':'Olderion','town-of-amore-2090':'Town of Amore','mozul-station-2100':'Mozul Station','capital-station-2102':'Capital Station','capital-market-2112':'Capital Market (Zoldaad)','slums-2114':'Slums (Zoldaad)','colosseum-2016':'Colosseum'}
for k,place in shopareas.items():
    for n,s,p in A[k]['shops']:
        parts=p.split('; ')
        if any(x.startswith('from partway') or "Brawler" in x or "Gladiator" in x for x in parts): continue
        price=parts[0]
        if price=='Not listed' or price.startswith('limit') or price.startswith('needs'): price=f"{cat[n]['stats']['Buy price']:,} gil"
        lim=[x for x in parts if x.startswith('limit')]
        if lim: price+='; '+lim[0]
        extra=[x for x in parts[1:] if x.startswith('needs Fledgling')]
        label=f"Shop: {place}"+(f" ({price})" if price else "")+(" after the Fledgling League" if extra else "")
        add(n,('shop',label))
for n in ['Hi-Potion','Mist Hi-Potion','Turbo Ether','Mist Turbo Ether','Phoenix Down']:
    add(n,('shop',f"Shop: Colosseum ({cat[n]['stats']['Buy price']:,} gil)"))
json.dump({k:v for k,v in src.items()},open('inv/src_shops.json','w'),indent=0)
print(len(src))
