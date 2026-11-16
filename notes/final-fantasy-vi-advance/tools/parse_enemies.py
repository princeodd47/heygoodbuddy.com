import re, html, glob, json, sys
raw = sys.argv[1]
def clean(s):
    s = re.sub(r'<img[^>]*alt=.([^\'"]*).[^>]*>', r'[\1]', s)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).strip()
def imgs(s): return [a.title() for a in re.findall(r"<img[^>]*alt='([^']*)'", s)]
mons=[]
for f in sorted(glob.glob(raw+'/all_*.html'), key=lambda x:int(re.findall(r'\d+',x.split('/')[-1])[0])):
    t=open(f,encoding='utf-8',errors='replace').read()
    blocks=t.split('<td class="titlecolumn"')[1:]
    for b in blocks:
        b=b.split('<tr><td>&nbsp;</td><td colspan="6" height="20">')[0]
        name=clean(re.search(r'tabletitletext">([^<]+)',b).group(1))
        bn=re.search(r'Bestiary #(\d+)',b); 
        cells=re.findall(r'<div class="tablemaintext">(.*?)</div></td>',b,re.S)
        m={'name':name,'bestiary':int(bn.group(1)) if bn else None}
        g=re.search(r'Bestiary #\d+',b)
        vals=cells
        keys=['type','level','hp','mp','gil','exp','str','mag','evade','def','mdef','mevade']
        for k,v in zip(keys,vals[:12]): 
            v=clean(v); m[k]=int(v) if v.lstrip('-').isdigit() else v
        def items(s):
            out={}
            for part in re.split(r'<br\s*/?>',s):
                c=clean(part)
                mm=re.match(r'(Common|Rare):\s*(.*)',c)
                if mm: out[mm.group(1).lower()]=mm.group(2)
            return out
        m['steal']=items(vals[12]); m['drop']=items(vals[13])
        m['statusImmune']=imgs(vals[14]); m['elemImmune']=imgs(vals[15])
        m['elemAbsorb']=imgs(vals[16]); m['elemWeak']=imgs(vals[17])
        m['lores']=[x for x in re.findall(r'>([^<>]+)</a>',vals[18])]
        m['cmdImmune']=clean(vals[19]); 
        mp=clean(vals[20]) if len(vals)>20 else ''
        lines=[x for x in mp.split('\n') if x]
        m['morph']={'items':[clean(x) for x in re.findall(r'<a[^>]*>(.*?)</a>',vals[20])] if len(vals)>20 else [], 'rate':lines[-1].replace(' Success Rate','') if lines else ''}
        mons.append(m)
json.dump(mons,open(sys.argv[2],'w'),indent=0)
print(len(mons)); print(json.dumps(mons[0])); 
import collections
print(collections.Counter(len(re.findall('x','')) for _ in [0]))
