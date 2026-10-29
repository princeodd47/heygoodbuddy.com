import re,html,sys,subprocess
for slug in sys.argv[1:]:
    t=subprocess.run(['curl','-sL','-A','Mozilla/5.0','https://meowdb.com/db/final-fantasy-resonance/enemies/'+slug],capture_output=True,text=True).stdout
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'<[^>]+>','\n',t); t=html.unescape(t)
    s='|'.join(l.strip() for l in t.splitlines() if l.strip())
    head=re.search(r'\|([^|]+)\|((?:Boss|Enemy)[^|]*Lv \d+)',s)
    def sect(a,b):
        i=s.find(a); j=s.find(b,i)
        return s[i:j] if i>=0 else ''
    el=sect('Elements|Element|Resistance','Status resistances')
    els=re.findall(r'\|(Fire|Ice|Wind|Earth|Thunder|Water|Light|Dark)\|([^|]+)',el)
    hp=re.search(r'\|HP\|([\d,]+)',s); ex=re.search(r'\|EXP\|([\d,]+)\|Gil\|([\d,]+)',s)
    mrp=re.search(r'MRP\|([\d,]+)',s)
    print('##',slug, head.groups() if head else '', 'HP',hp.group(1) if hp else '', 'EXP/Gil',ex.groups() if ex else '', 'MRP', mrp.group(1) if mrp else '')
    print('  elem:',[f'{e}:{r}' for e,r in els if r!='Normal'])
    print('  where:',sect('Where found|Place|Details','Drops and steals')[30:])
    print('  items:',sect('Drops and steals|Item|Method','Move list')[24:])
    tr=sect('Battle traits','Notes')
    if tr: print('  traits:',tr[:300])
