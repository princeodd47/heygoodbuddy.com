import re,json,sys
def recs(path):
    t=open(path).read().replace('\\"','"').replace('\\\\','\\')
    out=[]
    for m in re.finditer(r'\{"attributes":',t):
        s=m.start(); d=0; ins=False; i=s
        while i<len(t):
            c=t[i]
            if ins:
                if c=='\\': i+=1
                elif c=='"': ins=False
            else:
                if c=='"': ins=True
                elif c=='{': d+=1
                elif c=='}':
                    d-=1
                    if d==0: break
            i+=1
        try: out.append(json.loads(t[s:i+1]))
        except Exception as e: pass
    return out
