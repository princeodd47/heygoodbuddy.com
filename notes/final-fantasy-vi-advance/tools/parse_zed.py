import re, json, sys
t=open(sys.argv[1],encoding='latin-1').read()
t=t[t.find('6. Monster list',t.find('6. Monster list')+20):]
recs=re.split(r'\n-{40,}\n',t)
out=[]
for r in recs:
    m=re.match(r'\s*(\d+) (.+)',r)
    if not m: continue
    d={'idx':int(m.group(1)),'name':m.group(2).strip()}
    def g(p):
        x=re.search(p,r); return x.group(1).strip() if x else ''
    d['loc']=g(r'Found at:\s*(.*?)\n\n') .replace('\n',' ')
    for k,p in [('level',r'Level:\s*(\d+)'),('hp',r'HP:\s*(\d+)'),('mp',r'MP:\s*(\d+)'),('exp',r'Exp:\s*(\d+)'),('gil',r'GP:\s*(\d+)'),('def',r'Defense\s*:\s*(\d+)'),('mdef',r'Mag.Def\s*:\s*(\d+)'),('speed',r'Speed\s*:\s*(\d+)')]:
        v=g(p); d[k]=int(v) if v else None
    d['morph']=g(r'\nMorph:(.*)')
    d['rage']=g(r'\nRage\s*:(.*)')
    d['status']=g(r'\nStatus:(.*)'); d['immune']=g(r'\nImmune:(.*)')
    d['special']=g(r'Special attack:(.*)'); d['info']=g(r'Special Info:(.*)')
    d['weapon']=g(r'Regular weapon graphic:(.*)')
    out.append(d)
json.dump(out,open(sys.argv[2],'w'),indent=0)
print(len(out)); print(out[22]); print(out[0])
