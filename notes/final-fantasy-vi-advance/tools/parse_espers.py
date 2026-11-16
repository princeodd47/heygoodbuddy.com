import re, html, json, sys, glob
def clean(s):
    s=re.sub(r'<img[^>]*>','',s); s=re.sub(r'<br\s*/?>',' ',s); s=re.sub(r'<[^>]+>','',s)
    return re.sub(r'\s+',' ',html.unescape(s)).strip()
out=[]
for f in sorted(glob.glob(sys.argv[1]+'/esp_*.html'),key=lambda x:int(re.findall(r'\d+',x.split('/')[-1])[0])):
    t=open(f,encoding='utf-8',errors='replace').read()
    for b in t.split('<div class="tabletitletext">')[1:]:
        b=b.split('</table>')[0]
        name=clean(b[:b.find('</div>')])
        V=re.findall(r'<div class="tablemaintext">(.*?)</div></td>',b,re.S)
        if len(V)<6: continue
        e={'name':name,'bonus':clean(V[0]),'loc':clean(V[1]),'mp':clean(V[2]),
           'summon':clean(V[3]),'summonElem':[a.title() for a in re.findall(r"alt=\"?'?(\w+)['\"] title",V[3]) if a.lower()!='o'],
           'summonDesc':clean(V[4]),'etym':clean(V[5]),'spells':[]}
        rest=V[6:]
        for i in range(0,len(rest)-3,4):
            e['spells'].append({'name':clean(rest[i]),'elem':[a.title() for a in re.findall(r"alt='(\w+)'",rest[i])],'mp':clean(rest[i+1]),'rate':clean(rest[i+2]),'desc':clean(rest[i+3])})
        out.append(e)
json.dump(out,open(sys.argv[2],'w'),indent=0)
print(len(out)); 
for e in out: print(e['name'],'|',e['bonus'],'|',e['mp'],'|',e['summon'],e['summonElem'],'|',', '.join(s['name']+' '+s['rate'] for s in e['spells']),'|',e['loc'][:60])
