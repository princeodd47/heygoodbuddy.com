import re, json, sys
w=open(sys.argv[1]).read()
w=w[w.find('==List of Rages=='):w.find('==Other appearances')]
w=w[w.find('{|'):]
def link(s):
    s=re.sub(r'\{\{note\|.*?\}\}','',s)
    s=re.sub(r'\{\{icon\|FFVI\|element\|(\w+)\}\}',lambda m:m.group(1).title(),s)
    s=re.sub(r'\{\{(?:LA|A)\|(?:[^|}]*\|)?([^|}]*)\}\}',r'\1',s)
    s=re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]',r'\1',s)
    s=re.sub(r"'''",'',s)
    return s.strip()
rows=w.split('\n|-\n')[2:]
out=[]
for i,r in enumerate(rows):
    lines=[l for l in r.split('\n') if l.startswith(('!','|')) and not l.startswith('|}')]
    if len(lines)<5: print('skip',r[:80]); continue
    namecell=lines[0][1:]
    note=re.search(r'\{\{note\|(.*?)\}\}',namecell)
    parts=namecell.split('<br>')
    gba=link(parts[0]); snes=link(parts[1]).strip('()') if len(parts)>1 else gba
    innate=link(lines[3][1:])
    d={'n':i+1,'name':gba,'snes':snes,'attack':link(lines[1][1:]),'ability':link(lines[2][1:]),
       'immune':[x.strip() for x in link(lines[4][1:]).split(',') if x.strip() and x.strip()!='None'],'footnote':link(note.group(1)) if note else ''}
    for key in ['Immune','Weak','Absorb','Grants','Note']:
        m=re.search(key+r':\s*(.*?)(?:<br/?>|$)',innate)
        d[key.lower() if key!='Immune' else 'nullify']=[x.strip() for x in m.group(1).split(',')] if m else []
    out.append(d)
json.dump(out,open(sys.argv[2],'w'),indent=0)
print(len(out)); print(out[0]); print(out[3]); print(out[-1])
