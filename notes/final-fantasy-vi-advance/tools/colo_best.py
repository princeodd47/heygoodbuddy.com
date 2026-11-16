import json
L=json.load(open('raw/colo/list.json'))
ALL=[r for r in L if len(r)==3 and r[0]!='Wager']
ALL=[[w,'Siegfried (2)' if o=='Siegfried' else o,p] for w,o,p in ALL]
# stage, wager, win, why (prize), how (strategy), tag: top|good|chain
B=[
('Early','Elixir','Rename Card','Easy win, and the Rename Card is the next link in a chain: bet it again for Miracle Shoes.',"Setzer with plain Dice, no relics. His Dice beat the Cactuar on his first turn.",'easy'),
('Early','Phoenix Down','Magicite Shard','Turns a cheap item into a random Esper summon.',"Same as above: Setzer with Dice wins every time.",'easy'),
('Early','Flametongue','Organyx','A strong sword that uses MP for critical hits. It can break when it lands a hit, except on a Black Belt counter, so it suits Celes or Edgar swinging only in self-defense.',"Sabin with two Burning Fists and a Ribbon. If Great Malboro sneezes you out you keep the Flametongue.",''),
('Early','Murasame','Masamune','Cyan\'s better katana, and the first step of the katana chain.',"Sabin with two Venom Claws and a Black Belt. Save first; it's over in a couple of turns either way.",''),
('Early','Tintinnabulum','Growth Egg','Doubles the wearer\'s EXP.',"Dark Force is weak to instant death. Setzer with Viper Darts (two with a Genji Glove) or a Soul Sabre.",''),
('Early','Gold Hairpin','Dragon Horn','Jump lands 2 to 4 times. One of the best relics for a Dragoon (Edgar, Mog or anyone with Dragoon Boots).',"Same fight as the Organyx: Sabin with two Burning Fists and a Ribbon. If you picked the Gold Hairpin over Mog, this is the trade to make.",'top'),
('Early','Ribbon','Gold Hairpin','Only if you have a spare Ribbon. Lets you then trade the Gold Hairpin for a Dragon Horn.',"Dark Force: instant-death weapons, as for the Growth Egg.",'chain'),
('Mid','Regal Gown','Minerva Bustier','The best armor for Terra, Celes and Relm: nullifies Fire, Ice, Lightning and Wind, halves the rest, and adds 25% MP.',"Equip a Reflect Ring and just run. Death Machine casts Death, which bounces back and kills it. Don't attack: hurting it triggers up to four Blaster counters. The Regal Gown is in Daryl's Tomb.",'top'),
('Mid','Rename Card','Miracle Shoes','Permanent Safe, Shell, Haste and Regen.',"Fiend Dragon. Dragoon Edgar with a Flame Shield. Fallen One drops you to 1 HP, so it's a gamble, but it's the payoff of the Elixir chain.",'top'),
('Mid','Murasame','Masamune','',"",'skip'),
('Mid','Masamune','Murakumo','Stronger katana for Cyan.',"Gorgimera. Dragoon Edgar with a Flame Shield, which blocks its Surge and Flare Star. An Ice Shield doubles Aero damage, so don't use one.",''),
('Mid','Murakumo','Holy Lance','The best lance for Edgar or Mog: Holy element, +3 Magic, and casts Holy one time in four.',"Galypdes. Instant death doesn't work; send Dragoon Edgar and hope.",'top'),
('Mid','Falchion','Flame Shield','Absorbs Fire, nullifies Ice. Bet it again for an Ice Shield.',"Outsider is weak to instant death: Setzer with two Viper Darts and a Black Belt.",''),
('Mid','Flame Shield','Ice Shield','Absorbs Ice, nullifies Fire, +10% magic block. Bet it back for another Flame Shield to get a set of each.',"Metal Hitman has little HP. Sabin with two Dragon Claws and a Black Belt.",''),
('Mid','Fuma Shuriken','Pinwheel','The strongest throwing star for Shadow, and hard to get anywhere else.',"Chaos Dragon can kill in one hit. Dragoon Edgar and hope; expect to retry.",''),
('Mid','Bone Club','Red Jacket','Sabin\'s best armor; nullifies Fire.',"Test Rider. Wear an Ice Shield to absorb its Flash Rain.",''),
('Mid','Behemoth Suit','Snow Scarf','Great armor for Mog and Gau, and the start of the Ward Bangle chain. Behemoth Suits come from the Veldt.',"Outsider: Setzer with two Viper Darts and a Black Belt.",''),
('Mid','Ichigeki','Ichigeki','Recruits Shadow, if he survived the Floating Continent. He shows up as the opponent and joins you whether you win, lose or Teleport out.',"Win or lose, Shadow joins.",'top'),
('Late','Megalixir','Tintinnabulum','A relic that heals HP as you walk.',"Siegfried's Hyperdrive kills in one hit. Shadow with the Kagenui (random Stop), Dragoon Boots, Dragon Horn and high magic block.",''),
('Late','Healing Rod','Magus Rod','Relm\'s best rod.',"Tonberry counters any damage with Cleaver plus Traveler, so you must kill it in one hit. Protect against Break (Reflect Ring, Ribbon, Safety Bit), raise HP (Muscle Belt, Red Cap) and use a Master's Scroll with Fixed Dice or the Valiant Knife.",''),
('Late','Cat-Ear Hood','Merit Award','Lets anyone equip any weapon or armor.',"Slagworm is weak to instant death. Wear Angel Wings (against Quake) and a Thunder Shield (against Sand Storm). Mog with 255 Defense can't lose.",'top'),
('Late','Snow Scarf','Ward Bangle','Fewer random battles. Handy for the Dragons\' Den.',"Yojimbo. Max magic block (Force Shield, Force Armor, Priest's Miter, White Cape) on Setzer with Fixed Dice and a Master's Scroll.",''),
('Late','Ward Bangle','Dragon Horn','A second Dragon Horn.',"Yojimbo again, same setup.",''),
('Late','Thornlet','Mirage Vest','',"Aspidochelon is easy: weak to Holy, low HP. Sabin with two Dragon Claws, a Black Belt and Gaia Gear.",''),
('Late','Nutkin Suit','Genji Armor','A strong armor from a suit few can wear.',"Aspidochelon, as above.",''),
('Late','Thief\'s Bracer','Brigand\'s Glove','Steal becomes Mug (attack and steal in one turn).',"Amduscias. 255 Defense and a Ribbon or Peace Ring against its Confuse.",''),
('Late','Genji Glove','Thunder Shield','Turn spare Genji Gloves into Thunder Shields, which absorb Lightning and are very useful in Kefka\'s Tower.',"Demon Knight. Equip a Reflect Ring to bounce its Holy.",''),
('Late','Gauntlet','Thunder Shield','Same idea with spare Gauntlets.',"Vector Chimera. Thunder Shield plus Red Jacket blocks all its strong attacks; Edgar works well.",''),
('Post','Ragnarok','Lightbringer','The Lightbringer is a stronger sword than the Ragnarok. Each time you fight the final battle you can steal another Ragnarok from Lady, so you can turn every one into a Lightbringer for Terra, Celes and Locke.',"Daedalus.",'top'),
('Post','Soul of Thamasa','Celestriad','A GBA-only relic. Bet it again for a Dragon Horn.',"Behemoth King.",''),
('Post','Celestriad','Dragon Horn','Another Dragon Horn.',"Vector Chimera. Thunder Shield plus Red Jacket.",''),
('Post','Safety Bit','Dragon Horn','',"Tonberry, as for the Magus Rod.",''),
]
best=[dict(st=a,w=b,p=c,why=d,how=e,tag=f) for a,b,c,d,e,f in B if f!='skip']
opp={r[0]+'|'+r[2]:r[1] for r in ALL}
for x in best:
    x['o']=opp.get(x['w']+'|'+x['p'])
    if x['w']=='Ichigeki': x['o']='Shadow *'
    assert x['o'], x
D=json.load(open('build/data.json'))
D['colo']={'all':ALL,'best':best}
json.dump(D,open('build/data.json','w'),separators=(',',':'))
E={e['name'] for e in D['equipment']};M={m['name'] for m in D['monsters']}
print(len(ALL),len(best))
print('unknown items',sorted({n for r in ALL for n in (r[0],r[2]) if n not in E}))
print('unknown opp',sorted({r[1] for r in ALL if r[1] not in M}))
