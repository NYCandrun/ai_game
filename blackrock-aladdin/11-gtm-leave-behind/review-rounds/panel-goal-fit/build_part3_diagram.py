import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
SUP=lambda *ns: '<sup class="fnref">'+', '.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'
# page 2 pointer
rep('Part 3 lists five directions to explore for marketing Studio, each resting on a finding.','Part 3 puts the findings together into one way of presenting Studio, and the marketing work that follows.')
# replace Part 3 body
i=s.index('<section class="chapter part" id="part-3">'); j=s.index('</section>',i)+len('</section>')
svg='''<div role="img" aria-label="Diagram. On the left, BlackRock's own use: about 100 BlackRock applications and Copilot's thousands of tools. On the right, a client's use: its engineering team behind its own gateway, its own applications built with the SDK, and, hatched, its own AI tools, on which BlackRock has published nothing beyond a job posting. All of them sit on the same band, Aladdin's APIs, 54 of them public. Under the band, four controls in the public record: every call checked against the user's permissions, a second person's approval for rule changes, Copilot tested to give no investment advice, and Data Cloud as a copy of the client's Aladdin data in a Snowflake account BlackRock runs for that client.">
<svg id="pos" viewBox="0 0 1280 560" xmlns="http://www.w3.org/2000/svg" style="display:block;width:504pt;height:auto;overflow:visible">
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

<!-- left group: BlackRock's own use -->
<rect x="10" y="10" width="600" height="210" rx="6" class="band"/>
<text x="24" y="34" class="cap">BLACKROCK’S OWN USE · IN THE PUBLIC RECORD</text>
<rect x="24" y="52" width="276" height="148" rx="4" class="tile"/>
<text x="38" y="80" class="tt">About 100 BlackRock applications</text>
<text x="38" y="104" class="s">Explore, Dashboard, Risk Radar and the rest</text>
<text x="38" y="126" class="s">all call these APIs. Users see what their</text>
<text x="38" y="148" class="s">permissions allow.</text>
<rect x="318" y="52" width="276" height="148" rx="4" class="cop"/>
<text x="332" y="80" class="tt">Copilot</text>
<text x="332" y="104" class="s">Thousands of tools, each one an</text>
<text x="332" y="126" class="s">Aladdin API, built by 50 to 60 BlackRock</text>
<text x="332" y="148" class="s">engineering teams. Answers go through</text>
<text x="332" y="170" class="s">the user’s own permissions.</text>

<!-- right group: a client's use -->
<rect x="670" y="10" width="600" height="210" rx="6" class="band"/>
<text x="684" y="34" class="cap">A CLIENT’S USE · THE SAME APIS</text>
<rect x="684" y="52" width="180" height="148" rx="4" class="studio"/>
<text x="696" y="80" class="tt">Its engineers</text>
<text x="696" y="104" class="s">Route Aladdin calls</text>
<text x="696" y="126" class="s">through the client’s</text>
<text x="696" y="148" class="s">own gateway. Two code</text>
<text x="696" y="170" class="s">changes to the SDK.</text>
<rect x="880" y="52" width="180" height="148" rx="4" class="studio"/>
<text x="892" y="80" class="tt">Its applications</text>
<text x="892" y="104" class="s">Built with the SDK,</text>
<text x="892" y="126" class="s">run in the client’s own</text>
<text x="892" y="148" class="s">environment, on the</text>
<text x="892" y="170" class="s">client’s credentials.</text>
<rect x="1076" y="52" width="180" height="148" rx="4" style="fill:#fff"/>
<rect x="1076" y="52" width="180" height="148" rx="4" class="tile hatch"/>
<text x="1088" y="80" class="tt">Its AI tools</text>
<text x="1088" y="104" class="s">How they would connect</text>
<text x="1088" y="126" class="s">is not published.</text>
<text x="1088" y="148" class="s">BlackRock’s only public</text>
<text x="1088" y="170" class="s">word is a job posting.</text>

<!-- arrows down to the API band -->
<path d="M162 200 V262" class="arr" marker-end="url(#pos-arrow)"/>
<path d="M456 200 V262" class="arr" marker-end="url(#pos-arrow)"/>
<path d="M774 200 V262" class="arr" marker-end="url(#pos-arrow)"/>
<path d="M970 200 V262" class="arr" marker-end="url(#pos-arrow)"/>
<path d="M1166 200 V262" class="arr" stroke-dasharray="6 5" marker-end="url(#pos-arrow)"/>

<!-- the API band -->
<rect x="10" y="266" width="1260" height="70" rx="6" class="api"/>
<text x="640" y="296" class="tt tc">Aladdin’s APIs: one set, 54 of them public</text>
<text x="640" y="322" class="s tc">BlackRock’s applications, Copilot and a client’s own code all call the same APIs. Every call is checked against the user’s permissions.</text>

<!-- controls -->
<text x="24" y="376" class="cap">THE CONTROLS, ALL IN THE PUBLIC RECORD</text>
<rect x="10" y="390" width="300" height="150" rx="4" class="tile"/>
<text x="24" y="418" class="tt">Permissions per user</text>
<text x="24" y="442" class="s">Each API has its own access scope,</text>
<text x="24" y="464" class="s">and a user sees only what their</text>
<text x="24" y="486" class="s">entitlements allow.</text>
<rect x="330" y="390" width="300" height="150" rx="4" class="tile"/>
<text x="344" y="418" class="tt">A second approver</text>
<text x="344" y="442" class="s">Changes to compliance rules and</text>
<text x="344" y="464" class="s">dataset releases record a second</text>
<text x="344" y="486" class="s">person’s approval.</text>
<rect x="650" y="390" width="300" height="150" rx="4" class="tile"/>
<text x="664" y="418" class="tt">No investment advice</text>
<text x="664" y="442" class="s">Copilot’s standing instructions are</text>
<text x="664" y="464" class="s">tested so it will not give advice;</text>
<text x="664" y="486" class="s">the product page says the same.</text>
<rect x="970" y="390" width="300" height="150" rx="4" class="tile"/>
<text x="984" y="418" class="tt">Data Cloud</text>
<text x="984" y="442" class="s">A copy of the client’s Aladdin data in</text>
<text x="984" y="464" class="s">a Snowflake account BlackRock runs</text>
<text x="984" y="486" class="s">for that client, now adding private-</text>
<text x="984" y="508" class="s">markets data.</text>
</svg></div>
'''
part3=('<section class="chapter part" id="part-3">\n'
'<h2><span class="pn">Part 3</span>Directions to explore</h2>\n'
'<p>Put the findings together and they say one thing about how to present Studio. Studio is the same set of APIs, data and controls that BlackRock’s own teams build on, and BlackRock could offer it to a client’s engineers as exactly that. The people who would buy it are the client’s engineering and data team. The proof that it works is BlackRock’s own use of it.</p>\n'
'<figure class="exhibit keep" id="exhibit-14"><p class="ex-title"><span class="ex-num">Exhibit 14.</span> BlackRock’s own applications and a client’s can run on the same APIs, data and controls</p>\n'
+svg+
'<div class="notes"><p><span class="lbl"></span>Solid boxes are in the public record. The hatched box is not: BlackRock has published nothing on it beyond a job posting'+SUP(60)+'. Sources: the 100 applications, Copilot’s tools and the no-advice tests from Rosales and Valdez'+SUP(3)+' and the Copilot page'+SUP(10)+'; the client’s gateway code from pull requests 52 and 53 and the SDK README'+SUP(32,33,17)+'; permissions and second approvals from the public specifications'+SUP(11)+'; Data Cloud from its product page, Woodhead and Fivetran'+SUP(13,1,16)+'.</p></div></figure>\n'
'<figure class="exhibit" id="exhibit-15"><p class="ex-title"><span class="ex-num">Exhibit 15.</span> Five pieces of marketing work that follow</p>\n'
'<table>\n<colgroup><col style="width:110pt"><col><col style="width:150pt"></colgroup>\n'
'<thead><tr><th>The work</th><th>What it is</th><th>How to know it worked</th></tr></thead>\n<tbody>\n'
'<tr><td class="first">An answer for RFPs</td><td>A ready answer to the question “what APIs do you have, and can we connect to them”: the list of APIs by area with the label each carries in the public packages, how permissions work, how a client routes calls through its own gateway, and whether Aladdin connects to Snowflake and Databricks</td><td>How long the API section of an RFP takes to answer; how many RFPs score Studio; how many of those are won</td></tr>\n'
'<tr><td class="first">A public explanation of how Copilot’s tools work</td><td>A page that says which APIs Copilot’s tools call, whose permissions apply, what stops it giving advice, and how a client’s own AI tools would connect</td><td>The page is published and dated; prospects stop asking about connectors in deal reviews</td></tr>\n'
'<tr><td class="first">One client willing to be named</td><td>One client story, approved for the Studio page and the RFP answer. Candidates: a public pension fund whose award is already public, or a client whose engineers have contributed code to the SDK</td><td>Named clients sales can cite; deals in which one is cited</td></tr>\n'
'<tr><td class="first">A worked example: compliance reporting</td><td>A page and a demo of compliance reporting built on Data Cloud and the compliance APIs. Attendees at BlackRock’s own webinar named it first among the things they would stop running in house</td><td>Meetings that open on this example; pipeline tagged to it</td></tr>\n'
'<tr><td class="first">A worked example: private-markets data</td><td>A page and a demo of a custom application using Preqin and eFront data from a client’s Data Cloud</td><td>Clients with Data Cloud who take the private-markets data; use of the example in client meetings</td></tr>\n'
'</tbody></table>\n<div class="notes"><p><span class="lbl"></span>Source: my proposals, built on Exhibit 14 and the findings in Part 2.</p></div></figure>\n'
'</section>')
s=s[:i]+part3+s[j:]
# Part 4 exhibits 15,16 -> 16,17
m={15:16,16:17}
def f(mo):
    n=int(mo.group(2)); return mo.group(1)+str(m.get(n,n))
k=s.index('<section class="chapter part" id="part-4">')
tail=re.sub(r'(id="exhibit-|href="#exhibit-)(\d+)',f,s[k:]); tail=re.sub(r'(Exhibit )(\d+)\b',f,tail)
s=s[:k]+tail
open(p,'w',encoding='utf-8').write(s); print('built')
t=re.sub(r'<[^>]+>','',s); print(re.findall(r'Exhibit (\d+)\.',t)[-5:], t.count('Exhibit 16 follows a prospect'), t.count('Exhibit 17 puts Studio'))
