import re, html, json, sys, glob, os
raw=sys.argv[1]
def clean(s):
    s=re.sub(r'<img[^>]*alt="([^"]*)"[^>]*>',r'\1, ',s)
    s=re.sub(r"<img[^>]*alt='([^']*)'[^>]*>",r'\1, ',s)
    s=re.sub(r'<br\s*/?>','\n',s); s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s); s=re.sub(r'[ \t]+',' ',s)
    return '\n'.join(l.strip().strip(',').strip() for l in s.split('\n') if l.strip())
out=[]
def parse(f,cat,sub):
    t=open(f,encoding='utf-8',errors='replace').read()
    parts=t.split('<div class="tabletitletext">')[1:]
    for p in parts:
        name=clean(p[:p.find('</div>')])
        if name in ('Classes','Pages'): continue
        p=p.split('<div id="footer"')[0]
        L=[clean(x) for x in re.findall(r'<div class="tabletoptext">(.*?)</div>',p,re.S)]
        V=[clean(x) for x in re.findall(r'<div class="tablemaintext">(.*?)</div>\s*</td>',p,re.S)]
        if len(L)!=len(V): print('MISMATCH',name,L,V[:3]); continue
        d={'name':name,'cat':cat,'sub':sub}
        d.update(dict(zip(L,V)))
        out.append(d)
for f in sorted(glob.glob(raw+'/w_*.html')): parse(f,'Weapon',os.path.basename(f)[2:-5])
for f in sorted(glob.glob(raw+'/a_*.html')): parse(f,{'armor':'Armor','helmet':'Helmet','shield':'Shield'}[os.path.basename(f)[2:-5]],'')
parse(raw+'/relics.html','Relic','')
json.dump(out,open(sys.argv[2],'w'),indent=0)
import collections
print(len(out), collections.Counter(d['cat'] for d in out))
print(collections.Counter(k for d in out for k in d))
for n in ('Flametongue','Behemoth Suit','Genji Glove','Ribbon','Excalipoor'):
    print([d for d in out if d['name']==n])
