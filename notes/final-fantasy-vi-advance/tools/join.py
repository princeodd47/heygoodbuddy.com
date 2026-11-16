import json, re, sys
B=sys.argv[1]
E=json.load(open(B+'/enemies.json')); Z=json.load(open(B+'/zed.json')); R=json.load(open(B+'/rages.json')); Q=json.load(open(B+'/equip.json'))
gba_add=set(sys.argv[2].split(';'))
norm=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
key=lambda x:(x['level'],x['hp'],x['exp'],x['gil'])
zk={}
for z in Z: zk.setdefault(key(z),[]).append(z)
zi={z['idx']:z for z in Z}
ek={}
for e in E: ek.setdefault(key(e),[]).append(e)
en={norm(e['name']):e for e in E}
def strip(s): return re.sub(r'^\[[^\]]*\]','',s)
def loc_fix(z):
    l=z['loc']
    l=l.replace('WOB','World of Balance').replace('WOR','World of Ruin')
    return l
mons=[]
for e in E:
    zs=zk.get(key(e),[])
    if not zs: zs=[z for z in Z if norm(z['name'])==norm(e['name'])][:1]
    loc='; '.join(dict.fromkeys(loc_fix(z) for z in zs if z['loc']))
    m=dict(e)
    m['steal']={k:strip(v) for k,v in e['steal'].items()}
    m['drop']={k:strip(v) for k,v in e['drop'].items()}
    m['morph']={'items':[strip(x) for x in e['morph']['items']],'rate':e['morph']['rate']}
    m['loc']=loc
    m['gba']=e['name'] in gba_add
    m['speed']=zs[0]['speed'] if zs else None
    m['info']=zs[0]['info'] if zs else ''
    m['cmdImmune']='' if e['cmdImmune']=='None' else re.sub(r'\s+',' ',e['cmdImmune'])
    m['type']='' if e['type']=='None' else e['type']
    mons.append(m)
rages=[]; unmatched=[]
for r in R:
    z=zi.get(r['n']-1)
    cands=ek.get(key(z),[]) if z else []
    e=None
    if len(cands)==1: e=cands[0]
    else:
        e=en.get(norm(r['name'])) or (cands[0] if cands else None)
    if not e: unmatched.append(r['name'])
    eff=''
    if z and z['rage'] and 'Special' in z['rage'] and z['special']:
        mm=re.search(r'\((.*)\)\s*$',z['special']); eff=mm.group(1) if mm else ''
    rages.append({'n':r['n'],'name':e['name'] if e else r['name'],'snes':r['snes'],'attack':r['attack'],'ability':r['ability'],
        'abilityKind':'Special attack' if (z and 'Special' in z['rage']) else 'Spell / skill','effect':eff,
        'weak':r['weak'],'absorb':r['absorb'],'nullify':r['nullify'],'grants':r['grants'],'traits':r['note'],'immune':r['immune'],
        'loc':loc_fix(z) if z else '','level':e['level'] if e else None,'monster':e['name'] if e else None,'footnote':r['footnote']})
print('rage unmatched',unmatched)
def locparse(s):
    out=[];cur=None
    for line in s.split('\n'):
        m=re.match(r'^(Found|Buy From|Win from|Steal From|Metamorph From|Colosseum|[A-Z][A-Za-z ]+):\s*(.*)$',line)
        if m: cur=[m.group(1).replace('Win from','Dropped by').replace('Steal From','Stolen from').replace('Buy From','Sold in').replace('Metamorph From','Metamorph from'),[]]; out.append(cur); 
        if m and m.group(2): cur[1].append(m.group(2))
        elif not m and cur: cur[1].append(line)
        elif not m: out.append(['',[line]])
    return [[a,', '.join(b)] for a,b in out]
eq=[]
for d in Q:
    x={'name':d['name'],'cat':d['cat'],'sub':d['sub']}
    num=lambda k: int(d[k]) if d.get(k,'').lstrip('-').isdigit() else (d.get(k) or None)
    for k,nk in [('Attack','atk'),('Defense','def'),('Mag. Def.','mdef'),('Evade','evade'),('Magic Evade','mevade'),('Mag. Block','mevade'),('Strength','str'),('Stamina','sta'),('Magic','mag'),('Mag. Power','mag'),('Speed','spd')]:
        if k in d: x[nk]=num(k)
    for k,nk in [('Two-Hand Capable','twohand'),('Runic Capable','runic'),('Bushido Capable','bushido')]:
        if k in d: x[nk]=d[k]=='Yes'
    x['who']=', '.join(w.strip() for w in re.split(r'[,\n]+',d.get('Equippers','All Characters')) if w.strip())
    sa=d.get('Special Attributes','None')
    desc=d.get('Description','')
    x['notes']=[l for l in (desc+'\n'+sa).split('\n') if l.strip() and l.strip()!='None']
    if d.get('Elemental Attributes') and d['Elemental Attributes']!='None': x['elem']=d['Elemental Attributes'].replace('\n','; ')
    if 'Cost' in d: x['cost']=d['Cost']
    x['loc']=locparse(d['Location'])
    eq.append(x)
json.dump({'monsters':mons,'rages':rages,'equipment':eq},open(B+'/data.json','w'),separators=(',',':'))
print(len(mons),len(rages),len(eq), sum(1 for m in mons if not m['loc']), [m['name'] for m in mons if not m['loc'] and not m['gba']][:60])
print(rages[22]); print(eq[0]); print([e for e in eq if e['name']=='Behemoth Suit'])
