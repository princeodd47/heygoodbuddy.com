import json
D=json.load(open('data.json'))
R={r['name']:r for r in D['rages']}
top={
 'Guard Leader':('All enemies',"Wind Slash hits every enemy. The best multi-target Rage you can get this early."),
 'Stray Cat':('One enemy',"Cat Scratch hits four times for big single-target damage, and stays useful into the late game."),
 'Templar':('One or all',"Free Fira on one or all enemies, and Gau starts the fight with Protect."),
 'Bomb':('One or all',"Blaze: strong Fire damage on one or all enemies, with useful immunities."),
 'Aspiran':('One or all',"Gigavolt: very high Lightning damage, though it sometimes hits only one enemy."),
 'Satellite':('One enemy',"Sonic Boom chips away a big share of an enemy's HP, and the Rage blocks many statuses."),
 'Lesser Lopros':('All enemies',"Fireball: strong early multi-target Fire damage."),
 'Marchosias':('All enemies',"Aero: heavy Wind damage to every enemy, accurate, with strong immunities."),
 'Tyrannosaur':('All enemies',"Meteor hits every enemy and ignores Reflect."),
 'Io':('All enemies',"Flare Star: huge damage to every enemy that ignores Reflect and rarely misses."),
 'Yojimbo':('All enemies',"Shock: non-elemental damage to every enemy that never misses."),
 'Rafflesia':('All enemies',"Entice makes enemies attack each other, and it works on many bosses."),
 'Kamui':('All enemies',"Snowstorm: strong Ice damage to every enemy."),
 'Al Jabr':('One or all',"Thundaga for free."),
}
good="Cirpius Gorgias Trillium Mu Doberman Magitek Armor|Ghost Anguiform Darkside Eukaryote Heavy Armor Gold Bear Acrophies Hill Gigas Veil Dancer Joker|Litwor Chicken Wyvern Chaser Destroyer Grenade Ninja Chimera Behemoth Brainpan Gigantos|Black Dragon|Land Ray Peeper Fafnir Borghese Crawler|Greater Mantis Punisher|Behemoth King (2)|Death Warden Baalzephon Covert Devil Warlock|Holy Dragon|Magic Urn Cherry|Great Behemoth|Primeval Dragon|Vector Lythos Adamankary"
names=[]
for chunk in good.split('|'):
    names+=[chunk] if ' ' in chunk and chunk in R else []
# parse properly
pool=['Cirpius','Gorgias','Trillium','Mu','Doberman','Magitek Armor','Ghost','Anguiform','Darkside','Eukaryote','Heavy Armor','Gold Bear','Acrophies','Hill Gigas','Veil Dancer','Joker','Litwor Chicken','Wyvern','Chaser','Destroyer','Grenade','Ninja','Chimera','Behemoth','Brainpan','Gigantos','Black Dragon','Land Ray','Peeper','Fafnir','Borghese','Crawler','Greater Mantis','Punisher','Behemoth King (2)','Death Warden','Baalzephon','Covert','Devil','Warlock','Holy Dragon','Magic Urn','Cherry','Great Behemoth','Primeval Dragon','Vector Lythos','Adamankary']
best={}
for n,(tgt,why) in top.items():
    r=R[n]; best[str(r['n'])]={'tier':'top','target':tgt,'why':why}
for n in pool:
    r=R.get(n)
    if not r: print('missing',n); continue
    best.setdefault(str(r['n']),{'tier':'good'})
for v in best.values(): pass
for n,b in best.items():
    lv=next(r['level'] for r in D['rages'] if str(r['n'])==n) or 0
    b['stage']='Early' if lv<20 else 'Mid' if lv<36 else 'Late'
D['rageBest']=best
json.dump(D,open('data.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(best),sum(b['tier']=='top' for b in best.values()))
p='template.html';s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
rep("rages:{q:'',el:'',elMode:'weak',sort:'n'}","rages:{q:'',el:'',elMode:'weak',sort:'n',best:''}")
rep('''    <div class="grp"><label class="lbl" for="relm">Element</label>''','''    <div class="grp"><label class="lbl" for="rbest">Show</label><select id="rbest"><option value="">All Rages</option><option value="top">Top picks only</option><option value="any">Top picks and worth learning</option></select></div>
    <div class="grp"><label class="lbl" for="relm">Element</label>''')
rep("  ${legend('lg-rages',[\n","  ${legend('lg-rages',[\n    ['<span class=\"badge best\">★ Top pick</span>','One of the strongest Rages, recommended by fan guides. The gold bar marks it in the list; open it to see why.'],\n    ['<span class=\"badge good\">Worth learning</span>','Recommended by a walkthrough as a Rage worth picking up.'],\n    ['<b>Early · Mid · Late</b>','Roughly when you can get it, by the monster\\'s level.'],\n")
rep("  const q=document.getElementById('rq'),so=document.getElementById('rsort'),em=document.getElementById('relm');\n  so.value=s.sort;em.value=s.elMode;",
    "  const q=document.getElementById('rq'),so=document.getElementById('rsort'),em=document.getElementById('relm'),rb=document.getElementById('rbest');\n  so.value=s.sort;em.value=s.elMode;rb.value=s.best;rb.onchange=()=>{s.best=rb.value;draw()};")
rep("      if(s.el){if(s.elMode==='weak'","      const B=D.rageBest[r.n];if(s.best==='top'&&!(B&&B.tier==='top'))return false;if(s.best==='any'&&!B)return false;\n      if(s.el){if(s.elMode==='weak'")
rep("    L.innerHTML=a.length?a.map(r=>rowHTML('rage',r.n,`","    L.innerHTML=a.length?a.map(r=>{const B=D.rageBest[r.n];return rowHTML('rage'+(B?' '+B.tier:''),r.n,`")
rep("<span>${esc(r.name)}${r.footnote?' <span class=\"badge\">Can\\'t select</span>':''}</span></span>",
    "<span>${esc(r.name)}${r.footnote?' <span class=\"badge\">Can\\'t select</span>':''}${B?(B.tier==='top'?' <span class=\"badge best\">★ Top pick</span>':' <span class=\"badge good\">Worth learning</span>'):''}</span></span>")
rep("'<span class=\"faint\">—</span>':''}</span>`,()=>rageDetail(r),String(r.n)===pendingOpen)).join('')","'<span class=\"faint\">—</span>':''}</span>`,()=>rageDetail(r),String(r.n)===pendingOpen)}).join('')")
rep("  return `<section><h3>In battle</h3><dl class=\"kv\">","  const B=D.rageBest[r.n];\n  return `${B?`<section class=\"why\"><h3>${B.tier==='top'?'★ Why it\\'s a top pick':'Worth learning'}</h3><p class=\"prose\">${B.why?esc(B.why):'Recommended by a walkthrough as a Rage worth picking up.'}</p><p class=\"prose dim\" style=\"margin-top:6px\">${B.target?esc(B.target)+' · ':''}${B.stage} game</p></section>`:''}<section><h3>In battle</h3><dl class=\"kv\">")
rep(".lore{--cols:",""".badge.best{background:var(--gold);color:#1a1440;border-color:var(--gold);font-weight:600}
.badge.good{border-color:rgba(255,213,107,.5);color:var(--gold);background:none}
.row.rage.top{box-shadow:inset 4px 0 0 var(--gold);background:linear-gradient(90deg,rgba(255,213,107,.13),transparent 55%)}
.row.rage.good{box-shadow:inset 3px 0 0 rgba(255,213,107,.45)}
.lore{--cols:""")
s=s.replace("\\\\'","\\'")
open(p,'w').write(s)
d=open('data.json').read()
open('ff6-field-guide.html','w').write(s.replace('__DATA__',d.replace('</','<\\/')))
