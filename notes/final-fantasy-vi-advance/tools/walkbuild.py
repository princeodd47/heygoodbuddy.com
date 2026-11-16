import json,re,sys
sys.path.insert(0,'build')
from wt_content import W
exec(open('build/wt_titles.py').read())
D=json.load(open('build/data.json'))
CHESTS=json.load(open('build/chests.json'))
C=json.load(open('raw/wt/chapters.json'))
mons=D['monsters']; mnames={m['name'] for m in mons}
eq={x['name'] for x in D['equipment']}; es={e['name'] for e in D['espers']}
byname={}
for i,m in enumerate(mons): byname.setdefault(m['name'],[]).append(i)
rageByMon={}
for r in D['rages']: rageByMon.setdefault(r['monster'],[]).append(r['n'])
bad=[]
def chk(t):
    for k,v in re.findall(r'\{([mest]):([^}]+)\}',t):
        if k=='m' and v not in mnames: bad.append(('m',v))
        if k=='e' and v not in eq: bad.append(('e',v))
        if k=='s' and v not in es: bad.append(('s',v))
seenR=set(); seenL=set(); out=[]; pendL=[]; joined=False
key=lambda i:tuple(int(x) for x in i.split('-'))
avail=lambda i:(1,42)<=key(i)<=(1,50) or key(i)>=(2,29)
loreFrom={l['name']:l['from'] for l in D['lores']}
for c in C:
    w=W.get(c['id'],{})
    en=[e for e in c['enemies'] if e in mnames]
    rg=[]
    for e in en:
        for n in rageByMon.get(e,[]):
            if n not in seenR: seenR.add(n); rg.append(n)
    lo=[]
    for e in en:
        for i in byname[e]:
            for l in mons[i]['lores']:
                if l not in seenL:
                    seenL.add(l)
                    (lo if avail(c['id']) else pendL).append(l)
    old=[]
    if c['id'] in ('1-42','2-29'):
        old=[[l,loreFrom.get(l,[])] for l in pendL]; pendL=[]
    bosses=[]
    for nm,ix,st in w.get('boss',[]):
        if nm not in byname: bad.append(('boss',nm)); continue
        bosses.append([byname[nm][ix],st]); chk(st)
    for t in w.get('s',[]): chk(t)
    for _,t in w.get('b',[]): chk(t)
    tr=re.sub(r'\s+,',',',c['treasures']).strip()
    CH=CHESTS.get(c['id'],[])
    have={x['i'] for x in CH}
    extra=[t for t in re.split(r',\s*',tr) if t and re.sub(r' x\d+$','',t) not in have] if CH else []
    out.append(dict(chests=CH,trx=extra,id=c['id'],t=T.get(c['id'],c['title']),s=w.get('s',[]),b=w.get('b',[]),boss=bosses,rages=rg,lores=lo,loresOld=old,tr=tr,en=en))
firstCh={}
for k,o in enumerate(out):
    for n in o['rages']: firstCh[n]=k
bestN=[int(n) for n in D['rageBest']]
prev=-1
for k,o in enumerate(out):
    if W.get(o['id'],{}).get('veldt'):
        o['veldt']={'new':[n for n in bestN if n in firstCh and prev<firstCh[n]<=k],'old':[n for n in bestN if n in firstCh and firstCh[n]<=prev]}
        print('veldt',o['id'],len(o['veldt']['new']),len(o['veldt']['old']))
        prev=k
last=[o for o in out if o.get('veldt')][-1]
last['veldt']['later']=[n for n in bestN if n in firstCh and firstCh[n]>prev]
print('later',len(last['veldt']['later']))
print('bad',bad); print('chapters',len(out),'with notes',sum(1 for o in out if o['s']))
print('rages assigned',len(seenR),'of',len(D['rages']))
D['walk']=out
json.dump(D,open('build/data.json','w'),separators=(',',':'))
