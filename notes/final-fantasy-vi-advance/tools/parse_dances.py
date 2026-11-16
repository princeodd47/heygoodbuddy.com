import re, json, sys
w=open(sys.argv[1]).read()
def link(s):
    s=re.sub(r'\{\{icon\|FFVI\|element\|(\w+)\}\}',lambda m:m.group(1).title(),s)
    s=re.sub(r'\{\{(?:LA|A)\|(?:[^|}]*\|)?([^|}]*)\}\}',r'\1',s)
    s=re.sub(r'\[\[File:[^\]]*\]\]','',s)
    s=re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]',r'\1',s)
    s=re.sub(r"'''?",'',s); return s.strip()
def table(after):
    t=w[w.find(after):]; t=t[t.find('{|'):t.find('\n|}')]
    return [r for r in t.split('\n|-\n')[2:]]
dances=[]
for r in table('== Dances =='):
    L=r.split('\n'); nm=L[0][1:].split('<br>')
    name=link(nm[0]); snes=link(nm[1]).strip('()') if len(nm)>1 else name
    moves=[]
    for m in L[3][1:].split('<br>'):
        a,b=link(m).rsplit(' - ',1); moves.append({'name':a.strip(),'odds':int(b.split(' in ')[0])})
    dances.append({'name':name,'snes':snes,'moves':moves})
abil={}
for r in table('== Abilities =='):
    L=[x for x in r.split('\n') if x.startswith(('!','|'))]
    nm=L[0][1:].split('<br>'); name=link(nm[0]); snes=link(nm[1]).strip('()') if len(nm)>1 else name
    desc=link(L[2][1:])
    elems=[e.title() for e in re.findall(r'element\|(\w+)',L[2])]
    abil[name]={'snes':snes,'desc':desc,'elem':elems}
bg={}
for r in table('== Battle backgrounds =='):
    L=[x for x in r.split('\n') if x.startswith(('!','|'))]
    name=link(L[0][1:].split('<br>')[0])
    bg[name]=[link(x) for x in re.split(r'<br\s*/?>',L[2][1:]) if link(x)]
for d in dances:
    d['learn']=bg.get(d['name'],[])
    for m in d['moves']:
        a=abil.get(m['name']) or abil.get(m['name'].replace(' o ',"-o'-"))
        if not a: print('NO ABIL',m['name']); continue
        m.update(a)
json.dump(dances,open(sys.argv[2],'w'),indent=0)
for d in dances: print(d['name'],d['snes'],d['learn'],[(m['name'],m['odds'],m.get('elem')) for m in d['moves']])
