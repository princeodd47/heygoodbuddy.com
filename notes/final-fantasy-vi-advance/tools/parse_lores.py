import re, html, json, sys
def clean(s):
    s=re.sub(r'<br\s*/?>',' ',s); s=re.sub(r'<[^>]+>','',s); return re.sub(r'\s+',' ',html.unescape(s)).strip()
t=open(sys.argv[1]+'/lore.html',encoding='utf-8',errors='replace').read()
av=open(sys.argv[1]+'/lorecoll.html',encoding='utf-8',errors='replace').read()
avt=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',av)))
out=[]
for b in t.split('<div class="tabletitletext">')[1:]:
    b=b.split('height="30"')[0]
    name=clean(b[:b.find('</div>')])
    V=re.findall(r'<div class="tablemaintext">(.*?)</div></td>',b,re.S)
    d={'name':name,'mp':(int(clean(V[0])) if clean(V[0]).isdigit() else clean(V[0])),'reflect':clean(V[1]),'runic':clean(V[2]),'elem':[a.title() for a in re.findall(r"alt='(\w+)'",V[3])],
       'target':clean(V[4]),'from':[clean(x) for x in re.findall(r'<a[^>]*>(.*?)</a>',V[5])],'desc':clean(V[6])}
    m=re.search(re.escape(name)+r' (World of (?:Balance|Ruin)), Chapter (\d+)',avt)
    d['first']=m.group(1) if m else ''; d['chapter']=int(m.group(2)) if m else None
    out.append(d)
json.dump(out,open(sys.argv[2],'w'),indent=0)
for d in out: print(d['name'],d['mp'],d['elem'],d['target'],d['first'],d['chapter'],'|',', '.join(d['from']))
