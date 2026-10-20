import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
i=s.index('<svg id="pos"'); j=s.index('</svg>',i)+len('</svg>')
def tile(x,y,w,h,cls,title,lines,extra=''):
    out=[]
    if extra: out.append(extra)
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" class="{cls}"/>')
    out.append(f'<text x="{x+13}" y="{y+27}" class="tt">{title}</text>')
    for k,l in enumerate(lines): out.append(f'<text x="{x+13}" y="{y+49+20*k}" class="s">{l}</text>')
    return '\n'.join(out)
TY=48; TH=124; BAND_Y=226; CAP_Y=324; CY=338; CH=118
svg='''<svg id="pos" viewBox="0 0 1280 468" xmlns="http://www.w3.org/2000/svg" style="display:block;width:490pt;height:auto;overflow:visible">
<style>
#pos text{font-family:"Barlow",sans-serif;font-weight:400;font-size:16px;fill:#000}
#pos .tt{font-weight:700;font-size:17px}
#pos .s{font-family:"Barlow Condensed",sans-serif;font-weight:300;font-size:16px}
#pos .cap{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:14px;letter-spacing:.08em}
#pos .tc{text-anchor:middle}
#pos .arr{stroke:#000;stroke-width:1.5;fill:none}
#pos .hd{fill:#000}
#pos .band{fill:#fff;stroke:#D6D5DD;stroke-width:1.2}
#pos .tile{fill:#fff;stroke:#000;stroke-width:1.4}
#pos .tile.hatch{fill:url(#pos-hatch)}
#pos .cop{fill:#FEEBF0;stroke:#FC9BB3;stroke-width:1.6}
#pos .api{fill:#F2F2F2;stroke:#000;stroke-width:1.2}
#pos .studio{fill:#FFF5CC;stroke:#FFCE00;stroke-width:1.6}
</style>
<defs>
<marker id="pos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="hd"/></marker>
<pattern id="pos-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="2" height="6" style="fill:#BFBFBF"/></pattern>
</defs>
'''
svg+=f'<rect x="10" y="8" width="600" height="{TY+TH+10}" rx="6" class="band"/>\n<text x="24" y="31" class="cap">BLACKROCK’S OWN USE · IN THE PUBLIC RECORD</text>\n'
svg+=tile(24,TY,276,TH,'tile','About 100 BlackRock applications',['Explore, Dashboard, Risk Radar and the rest','all call these APIs. Users see what their','permissions allow.'])+'\n'
svg+=tile(318,TY,276,TH,'cop','Copilot',['Thousands of tools, each one an Aladdin','API, built by 50 to 60 BlackRock teams.','Answers go through the user’s permissions.'])+'\n'
svg+=f'<rect x="670" y="8" width="600" height="{TY+TH+10}" rx="6" class="band"/>\n<text x="684" y="31" class="cap">A CLIENT’S USE · THE SAME APIS</text>\n'
svg+=tile(684,TY,180,TH,'studio','Its engineers',['Route Aladdin calls','through the client’s own','gateway. Two code','changes to the SDK.'])+'\n'
svg+=tile(880,TY,180,TH,'studio','Its applications',['Built with the SDK, run','in the client’s own','environment, on the','client’s credentials.'])+'\n'
svg+=tile(1076,TY,180,TH,'tile hatch','Its AI tools',['How they would connect','is not published.','BlackRock’s only public','word is a job posting.'],extra=f'<rect x="1076" y="{TY}" width="180" height="{TH}" rx="4" style="fill:#fff"/>')+'\n'
ay=TY+TH
for x in (162,456,774,970): svg+=f'<path d="M{x} {ay} V{BAND_Y-4}" class="arr" marker-end="url(#pos-arrow)"/>\n'
svg+=f'<path d="M1166 {ay} V{BAND_Y-4}" class="arr" stroke-dasharray="6 5" marker-end="url(#pos-arrow)"/>\n'
svg+=f'<rect x="10" y="{BAND_Y}" width="1260" height="64" rx="6" class="api"/>\n<text x="640" y="{BAND_Y+27}" class="tt tc">Aladdin’s APIs: one set, 54 of them public</text>\n<text x="640" y="{BAND_Y+51}" class="s tc">BlackRock’s applications, Copilot and a client’s own code all call the same APIs. Every call is checked against the user’s permissions.</text>\n'
svg+=f'<text x="24" y="{CAP_Y}" class="cap">THE CONTROLS, ALL IN THE PUBLIC RECORD</text>\n'
svg+=tile(10,CY,300,CH,'tile','Permissions per user',['Each API has its own access scope,','and a user sees only what their','entitlements allow.'])+'\n'
svg+=tile(330,CY,300,CH,'tile','A second approver',['Changes to compliance rules and','dataset releases record a second','person’s approval.'])+'\n'
svg+=tile(650,CY,300,CH,'tile','No investment advice',['Copilot’s standing instructions are','tested so it will not give advice;','the product page says the same.'])+'\n'
svg+=tile(970,CY,300,CH,'tile','Data Cloud',['A copy of the client’s Aladdin data in','a Snowflake account BlackRock runs for','that client, now adding private markets.'])+'\n'
svg+='</svg>'
s=s[:i]+svg+s[j:]
open(p,'w',encoding='utf-8').write(s); print('compacted')
