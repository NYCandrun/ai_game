import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def SUP(*ns): return '<sup class="fnref">'+', '.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'
def tile(x,y,w,h,cls,title,lines,fs=None,extra=''):
    out=[]
    if extra: out.append(extra)
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" class="{cls}"/>')
    out.append(f'<text x="{x+12}" y="{y+26}" class="tt">{title}</text>')
    step=20 if fs is None else fs
    for k,l in enumerate(lines): out.append(f'<text x="{x+12}" y="{y+48+step*k}" class="s">{l}</text>')
    return '\n'.join(out)
TY=46; TH=116; BAND_Y=218; CAP_Y=316; CY=328; CH=108
svg='''<div role="img" aria-label="Diagram. On the left, BlackRock's own use: about 100 BlackRock applications and Copilot's thousands of tools. On the right, a client's use: its engineers behind its own gateway, its applications, and, hatched, its AI tools, on which BlackRock has published nothing beyond a job posting. All sit on one band, Aladdin's APIs, which all of them call and whose Data Cloud they read. Below, two groups: controls on every call (permissions per user, a second approver, compliance on every order) and what Copilot adds for AI (input guardrails, output guardrails, LLM judges).">
<svg id="pos" viewBox="0 0 1280 444" xmlns="http://www.w3.org/2000/svg" style="display:block;width:504pt;height:auto;overflow:visible">
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
#pos .ai{fill:#EEF1F5;stroke:#000;stroke-width:1.2}
</style>
<defs>
<marker id="pos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="hd"/></marker>
<pattern id="pos-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="2" height="6" style="fill:#BFBFBF"/></pattern>
</defs>
'''
svg+=f'<rect x="10" y="8" width="600" height="{TY+TH+10-8}" rx="6" class="band"/>\n<text x="24" y="30" class="cap">BLACKROCK’S OWN USE · IN THE PUBLIC RECORD</text>\n'
svg+=tile(24,TY,276,TH,'cop','About 100 BlackRock applications',['Explore, Dashboard, Risk Radar and the rest','all call these APIs.'])+'\n'
svg+=tile(318,TY,276,TH,'cop','Copilot',['Thousands of tools, each one an Aladdin','API, built by 50 to 60 BlackRock teams.'])+'\n'
svg+=f'<rect x="670" y="8" width="600" height="{TY+TH+10-8}" rx="6" class="band"/>\n<text x="684" y="30" class="cap">A CLIENT’S USE · THE SAME APIS</text>\n'
svg+=tile(684,TY,180,TH,'studio','Its engineers',['Route Aladdin calls','through the client’s own','gateway.'])+'\n'
svg+=tile(880,TY,180,TH,'studio','Its applications',['Run in the client’s own','environment, on the','client’s credentials.'])+'\n'
svg+=tile(1076,TY,180,TH,'tile hatch','Its AI tools',['How they would connect','is not published.','BlackRock’s only public','word is a job posting.'],extra=f'<rect x="1076" y="{TY}" width="180" height="{TH}" rx="4" style="fill:#fff"/>')+'\n'
ay=TY+TH
for x in (162,456,774,970): svg+=f'<path d="M{x} {ay} V{BAND_Y-4}" class="arr" marker-end="url(#pos-arrow)"/>\n'
svg+=f'<path d="M1166 {ay} V{BAND_Y-4}" class="arr" stroke-dasharray="6 5" marker-end="url(#pos-arrow)"/>\n'
svg+=f'<rect x="10" y="{BAND_Y}" width="1260" height="64" rx="6" class="api"/>\n<text x="640" y="{BAND_Y+27}" class="tt tc">Aladdin’s APIs</text>\n<text x="640" y="{BAND_Y+51}" class="s tc">BlackRock’s applications, Copilot and a client’s own code call the same APIs and read the same Data Cloud, the client’s Aladdin data in a Snowflake account BlackRock runs for it.</text>\n'
svg+=f'<rect x="10" y="{CAP_Y-16}" width="610" height="{CH+40}" rx="6" class="band"/>\n<text x="24" y="{CAP_Y+2}" class="cap">CONTROLS ON EVERY CALL</text>\n'
svg+=tile(24,CY+8,190,CH,'tile','Permissions per user',['Each API has its own access','scope. A user sees only what','their entitlements allow.'])+'\n'
svg+=tile(224,CY+8,190,CH,'tile','A second approver',['Rule assignments and dataset','releases record a second','sign-off.'])+'\n'
svg+=tile(424,CY+8,180,CH,'tile','Compliance on every order',['The order API runs compliance','by default and returns any','violations.'])+'\n'
svg+=f'<rect x="660" y="{CAP_Y-16}" width="610" height="{CH+40}" rx="6" class="band"/>\n<text x="674" y="{CAP_Y+2}" class="cap">WHAT COPILOT ADDS FOR AI · FROM BLACKROCK’S OWN ACCOUNT</text>\n'
svg+=tile(674,CY+8,190,CH,'ai','Input guardrails',['Off-topic content is caught','and personal data handled','before any plan.'])+'\n'
svg+=tile(874,CY+8,190,CH,'ai','Output guardrails',['Answers are checked for','hallucinations and against','domain rules.'])+'\n'
svg+=tile(1074,CY+8,186,CH,'ai','LLM judges',['Every system prompt is tested','daily and on every change.'])+'\n'
svg+='</svg></div>\n'
part3=('<section class="chapter part" id="part-3">\n'
'<h2><span class="pn">Part 3</span>Directions to explore</h2>\n'
'<p>The findings suggest that Studio could be presented as a way for a client to read its Aladdin data anywhere and act on it through the same APIs and controls BlackRock’s own applications use. Data Cloud puts the data in the client’s Snowflake account for analysis. Anything that changes the book, such as an order or a compliance rule, goes through the APIs, where user permissions apply and orders are checked for compliance by default. This is my reading of the specifications; BlackRock has not described Studio this way'+SUP(11,13)+'.</p>\n'
'<p>Buyers now ask about APIs and data connectors in RFPs. SimCorp also invites clients to build on its platform. BlackRock may be able to show something SimCorp cannot: a large investment business that runs on these APIs every day'+SUP(2,3,61,62)+'.</p>\n'
'<p>BlackRock told investors that API calls would grow 17x by 2030. If that growth comes from Studio, it likely depends on analysts and portfolio managers who write code using it daily, not only on the engineers who evaluate it. Linking that figure to Studio is my inference'+SUP(7,40)+'.</p>\n'
'<p>Clients will expect their own AI tools to reach Aladdin, as they already reach FactSet, LSEG and Snowflake'+SUP(55,51,58)+'. Copilot shows how that can work under each user’s permissions and with guardrails'+SUP(3,10)+'. How a client’s own tools would connect is not public'+SUP(60)+'.</p>\n'
'<p>Proof that clients use Aladdin is already public: JPMorgan Chase’s payment records, pension tenders, and client engineers contributing to the SDK. A named Studio story could start with one of them'+SUP(29,32,33,37,38,39)+'.</p>\n'
'<figure class="exhibit keep" id="exhibit-14"><p class="ex-title"><span class="ex-num">Exhibit 14.</span> BlackRock’s applications and a client’s code call the same APIs under the same permissions</p>\n'
+svg+
'<div class="notes"><p><span class="lbl"></span>Solid boxes are in the public record. The hatched box is not: on a client’s AI tools BlackRock has published nothing beyond a job posting'+SUP(60)+'. The right-hand controls show how BlackRock governs AI on these APIs today, which is the model a client’s own AI tools could follow. Sources: Rosales and Valdez'+SUP(3)+', the Copilot page'+SUP(10)+', pull requests 52 and 53'+SUP(32,33)+', the SDK README'+SUP(17)+', the public specifications'+SUP(11)+', the Data Cloud page'+SUP(13)+', Woodhead'+SUP(1)+' and Fivetran'+SUP(16)+'.</p></div></figure>\n'
'<figure class="exhibit" id="exhibit-15"><p class="ex-title"><span class="ex-num">Exhibit 15.</span> Five pieces of marketing work to explore, in the order I would start them</p>\n'
'<table>\n<colgroup><col style="width:16pt"><col style="width:96pt"><col><col style="width:132pt"></colgroup>\n'
'<thead><tr><th></th><th>The work</th><th>What it is</th><th>How to know it worked</th></tr></thead>\n<tbody>\n'
'<tr><td class="first">1</td><td class="first">An answer for RFPs</td><td>A ready answer to “what APIs do you have, and can we connect to them”: the APIs by area with their package labels, how permissions work, how a client routes calls through its own gateway, and the Snowflake and Databricks answer.</td><td>Time to answer the API section of an RFP; RFPs that score Studio; how many of those are won</td></tr>\n'
'<tr><td class="first">2</td><td class="first">How a client’s AI tools reach Aladdin</td><td>A page on how a client’s own AI tools could call Aladdin’s APIs under the same permissions and guardrails Copilot uses.</td><td>The page is published; RFPs and deal reviews get a clear answer on AI connections; API calls from client AI tools</td></tr>\n'
'<tr><td class="first">3</td><td class="first">One client willing to be named</td><td>One client story, cleared for the Studio page and the RFP answer: a public pension fund already on record, or a client whose engineers have contributed to the SDK.</td><td>Named clients sales can cite; deals in which one is cited</td></tr>\n'
'<tr><td class="first">4</td><td class="first">A worked example: a rebalancing tool</td><td>A page and a demo of a rebalancing tool a client builds on the order API. It tests trades with what-if, runs compliance on every order, and returns any violations before anything trades. Sewdass names rebalancing tools as what clients build on Aladdin’s APIs'+SUP(2)+'.</td><td>Meetings that open on this example; pipeline tagged to it; API calls from clients who build it</td></tr>\n'
'<tr><td class="first">5</td><td class="first">A worked example: private-markets data</td><td>A page and a demo of a custom application using Preqin and eFront data from a client’s Data Cloud.</td><td>Clients with Data Cloud who take the private-markets data; API calls on private-markets data; use in client meetings</td></tr>\n'
'</tbody></table>\n</figure>\n'
'</section>')
i=s.index('<section class="chapter part" id="part-3">'); j=s.index('</section>',i)+len('</section>')
s=s[:i]+part3+s[j:]
open(p,'w',encoding='utf-8').write(s); print('built')
