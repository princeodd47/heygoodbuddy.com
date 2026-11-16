import csv,json,re
R=list(csv.DictReader(open('raw/gc_treasures.csv')))
D=json.load(open('build/data.json'));E={x['name'] for x in D['equipment']}
NM={'Aegis Shld':'Aegis Shield','Air Lancet':'Air Knife','Assassin':"Assassin's Dagger",'Atlas Armlet':'Gigas Glove','Atma Weapon':'Ultima Weapon','AutoCrossbow':'Auto Crossbow','Back Guard':'Alarm Earring','Beads':'Prayer Beads','Break Blade':'Stoneblade','Chain Saw':'Chainsaw','Charm Bangle':'Ward Bangle','Cherub Down':'Angel Wings','Coin Toss':"Heiji's Jitte",'Coronet':'Circlet','Cure Ring':'Angel Ring','Cursed Shld':'Cursed Shield','Czarina Gown':'Regal Gown','Doom Darts':'Viper Darts','DragoonBoots':'Dragoon Boots','Drainer':'Blood Sword','Earrings':'Earring','Exp. Egg':'Growth Egg','FakeMustache':'Fake Mustache','Fire Knuckle':'Burning Fist','Fire Rod':'Flame Rod','Flame Sabre':'Flametongue','Blizzard':'Icebrand','Flame Shld':'Flame Shield','Force Shld':'Force Shield','Gem Box':'Soul of Thamasa','Genji Helmet':'Genji Helm','Genji Shld':'Genji Shield','Gold Armor':'Golden Armor','Gold Helmet':'Golden Helm','Gold Shld':'Golden Shield','Heal Rod':'Healing Rod','Heavy Shld':'Heavy Shield','Hero Ring':"Hero's Ring",'Ice Shld':'Ice Shield','Inviz Edge':'Invisibility Scroll','Magical Brsh':'Magical Brush','Man Eater':'Man-Eater','Minerva':'Minerva Bustier','MithrilGlove':'Mythril Glove','Moogle Charm':"Molulu's Charm",'Pearl Lance':'Holy Lance','Pearl Rod':'Holy Rod','Pod Bracelet':'Guard Bracelet','Rage Ring':'Berserker Ring','Rainbow Brsh':'Rainbow Brush','Regal Crown':'Royal Crown','RegalCutlass':'Great Sword','Relic Ring':'Cursed Ring','Rune Edge':'Rune Blade','RunningShoes':'Hermes Sandals','Sneak Ring':"Thief's Bracer",'Sniper Sight':'Sniper Eye','Striker':'Ichigeki','Stunner':'Kagenui','Tack Star':'Pinwheel','Tempest':'Kazekiri','Thief Glove':"Brigand's Glove",'ThiefKnife':"Thief's Knife",'Thunder Shld':'Thunder Shield','ThunderBlade':'Thunder Blade','Tintinabar':'Tintinnabulum','True Knight':"Knight's Code",'ValiantKnife':'Valiant Knife','Wall Ring':'Reflect Ring','Water Edge':'Water Scroll','Zephyr Cape':'Zephyr Cloak',
'Tonic':'Potion','Potion':'Hi-Potion','Tincture':'Ether','Ether':'Hi-Ether','Fenix Down':'Phoenix Down','Soft':'Gold Needle','Eyedrop':'Eye Drops','Revivify':'Holy Water','Warp Stone':'Teleport Stone','Magicite':'Magicite Shard','Lump of Metal':'Lump of Metal',
'Tiger Fangs':'Tigerfang','Dragon Claw':'Dragon Claws','Offering':"Master's Scroll",'Graedus':'Gladius'}
MB={'Presenter':'Angler Whelk','Telstar':'Satellite','Specter':'Apparition','Siegfried':'Siegfried','Allo Ver':'Death Warden','KatanaSoul':'Samurai Soul','Master Pug':'Master Tonberry'}
KEEP={'X-Potion','X-Ether','Elixir','Megalixir','Remedy','Green Cherry','Sleeping Bag','Tent','Antidote','Echo Screen','Green Beret','Hyper Wrist'}
def gba(n):
    n=n.strip()
    m=re.match(r'^(.+?) \((.+)\)$',n)
    if m: return (gba(m.group(2))[0], 'monster-in-a-box: '+MB.get(m.group(1),m.group(1))) if gba(m.group(2))[0] else (None,None)
    if re.match(r'^[\d,]+ GP$',n): return (n.replace(' GP',' Gil'),None)
    g=NM.get(n,n)
    return (g,None) if (g in E or g in KEEP or g in NM.values()) else (None,None)
# chapter assignment by row index ranges; (start,end,chapter[,which]) which: 0 first option, -1 last option
A=[(1,2,'1-2'),(3,4,'1-2',0),(5,8,'1-3'),(9,13,'1-4'),(14,16,'1-5',0),(17,24,'1-6',0),(25,25,'1-6'),(27,29,'1-7'),(30,38,'1-8'),(40,49,'1-6'),(50,56,'1-16'),(57,57,'1-10',0),(58,62,'1-11'),(63,71,'1-12'),(72,73,'1-14'),(74,78,'1-15'),(79,86,'1-19'),(87,89,'1-21'),(90,90,'1-22'),(91,98,'1-23'),(103,103,'1-23'),(104,110,'1-27'),(111,122,'1-30'),(125,125,'1-32'),(139,156,'1-38'),(157,163,'1-39'),(164,177,'1-40'),(178,183,'1-41'),(184,185,'1-42'),(186,189,'1-43'),(190,194,'1-40'),(195,200,'1-48'),(205,212,'2-3'),(213,213,'2-4'),(215,220,'2-8'),(221,224,'2-10'),(225,226,'2-11'),(228,228,'2-20'),(229,229,'2-16'),(231,233,'2-18'),(236,236,'2-12'),(237,243,'2-22'),(244,246,'2-25'),(250,255,'2-28'),(258,262,'2-33'),(264,272,'2-36'),(273,281,'2-37'),(283,288,'2-37'),(289,294,'2-34'),(295,300,'2-35'),(302,306,'2-40'),(307,308,'2-41'),(311,311,'2-16'),(312,313,'2-42'),(314,318,'2-43'),(319,326,'2-44'),(328,328,'2-45'),
   (3,4,'2-16',-1),(14,16,'2-7',-1),(17,23,'2-6',-1),(57,57,'2-16',-1),(1,1,'1-17',1),(16,16,'1-17',1)]
OUT={}
skipped=[]
for a in A:
    s,e,ch=a[:3]; which=a[3] if len(a)>3 else None
    for i in range(s,e+1):
        r=R[i]; opts=[o.strip() for o in re.split(r'\s+or,?\s+',r['Treasure'].replace('or,','or')) if o.strip()]
        if not opts: continue
        if (s,e,ch)==(1,1,'1-17'): r=R[14]; opts=[o.strip() for o in re.split(r'\s+or,?\s+',r['Treasure'].replace('or,','or'))]
        if which is not None and len(opts)>1: pick=opts[which] if which in (0,-1) else opts[which]
        elif which==1: pick=opts[0]
        else: pick=opts[0]
        if ch=='1-17': pick=opts[1] if len(opts)>2 else opts[-1]
        n,mb=gba(pick)
        if not n: skipped.append((i,ch,pick)); continue
        where=r['Map'].strip()
        area=r['Area'].strip()
        note=re.sub(r'\s+',' ',r['Notes']).strip().rstrip('.')
        cond=r['Conditions'].strip()
        if len(opts)>1: cond=''
        changes=len(opts)>1
        OUT.setdefault(ch,[]).append(dict(i=n,a=area,w=where,n=note,c=cond,mb=mb,ch=changes))
# de-dup exact
for ch in OUT:
    seen=set();L=[]
    for x in OUT[ch]:
        k=(x['i'],x['a'],x['w'],x['n'])
        if k in seen: continue
        seen.add(k);L.append(x)
    OUT[ch]=L
json.dump(OUT,open('build/chests.json','w'))
print('skipped:',skipped)
for ch in sorted(OUT,key=lambda k:[int(x) for x in k.split('-')]): print(ch,len(OUT[ch]),', '.join(x['i'] for x in OUT[ch]))
