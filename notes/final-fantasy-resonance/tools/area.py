import re,html,json,sys,os
def parse(path):
    t=open(path).read()
    i=t.find('<script'); body=t
    name=re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S)
    name=html.unescape(re.sub('<[^>]+>','',name.group(1))).strip() if name else ''
    chests=[html.unescape(d) for l,d in re.findall(r'ffr-trk-cl-name">([^<]*)</span><small>([^<]*)</small>',t)]
    shops=[]
    for m in re.finditer(r'<tr><td><span><a class="[^"]*" href="/db/final-fantasy-resonance/(equipment|items)/([a-z0-9-]+)">([^<]*)</a></span></td><td>([^<]*)</td><td>([^<]*)</td></tr>',t):
        shops.append((html.unescape(m.group(3)),m.group(4),html.unescape(m.group(5))))
    quests=sorted(set(re.findall(r'href="/db/final-fantasy-resonance/quests/([a-z0-9-]+)"',t)))
    return dict(name=name,chests=chests,shops=list(dict.fromkeys(shops)),quests=quests)
if __name__=='__main__':
    out={}
    for f in sorted(os.listdir(sys.argv[1])):
        out[f[:-5]]=parse(os.path.join(sys.argv[1],f))
    json.dump(out,open(sys.argv[2],'w'),indent=1)
