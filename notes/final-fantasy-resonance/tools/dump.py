import re,html,sys
t=open(sys.argv[1]).read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=re.sub(r'<[^>]+>','\n',t); t=html.unescape(t)
s='\n'.join(l.strip() for l in t.splitlines() if l.strip())
i=s.find('Random Dad Joke'); j=s.find('Editorial note')
print(s[i:j] if i>0 else s)
