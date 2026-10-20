import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:90]); s=s.replace(a,b)
def cut_block(start,end,keep_end=False):
    global s
    assert s.count(start)==1,(s.count(start),start[:80]); i=s.index(start)
    j=s.index(end,i); assert j>i
    s=s[:i]+(s[j:] if keep_end else s[j+len(end):])
SUP=lambda n: f'<sup class="fnref"><a href="#s{n}">{n}</a></sup>'
# ---- page 2
rep('<p class="lede">Studio is the product behind the growth story BlackRock tells investors, but the story never names it. Public proof that clients use Aladdin never names Studio either. Part 3 sets out six directions to close both gaps.</p>',
    '<p class="lede">Studio is the product behind the growth story BlackRock tells investors.</p>')
rep('since 2024'+SUP(5)+'. Public documents prove named clients use Aladdin (none names Studio): JPMorgan Chase’s proxy statements, Janus Henderson’s code commits and 10-K, Royal London’s CEO on video, and three pension tenders.</p>',
    'since 2024'+SUP(5)+'.</p>')
rep('17x by 2030. The other half is the whole portfolio, public and private; new private-markets data arrives via Data Cloud and Explore, Aladdin’s portfolio app'+SUP(6)+'. Aladdin Copilot, BlackRock’s AI assistant, works only inside the login, via plugins on Aladdin’s APIs, while data providers’ connectors let outside AI tools pull their data'+SUP(7)+'. Buyers',
    '17x by 2030. Buyers')
rep('<p style="margin-bottom:4pt">Six likely initial directions:</p>','<p style="margin-bottom:4pt">Five likely initial directions:</p>')
rep('<li style="margin-bottom:0">Put Studio’s name beside the 17x API-call projection in investor and client materials.</li>\n','')
rep('can be misheard; the Sources section marks which recordings. Figures may be out of date, and I have no internal product context,',
    'can be misheard. I have no internal product context,')
rep(' For recordings it also gives the minute and second where each quoted passage begins.</p>','</p>')
# ---- page 3 / 4
rep(' Aladdin is sold the way enterprise platforms are sold: the conversation comes first, and documentation, a sandbox and credentials come from the solutions team once a prospect is qualified. Part 1 covers what a prospect can see before that conversation.</p>','</p>')
rep('on Snowflake’s podcast in November 2025. It has three parts.</p>','on Snowflake’s podcast in November 2025.</p>')
rep('<p class="lead-in">The three parts are APIs and events, the Aladdin Data Cloud on Snowflake, and developer tools. Exhibit 2 follows','<p class="lead-in">Exhibit 2 follows')
rep('The public APIs follow a trade from order to NAV, except positions and events</p>','The public APIs follow a trade from order to NAV</p>')
# ---- page 6
rep('<p>Only 23 of the 54 specifications are stable, and the specifications say more than their count. Every one is tagged <code>Access.Internal</code>, a label BlackRock does not explain in public'+SUP(17)+'. Posting an order','<p>Posting an order')
rep('<p>The SDK is the one piece that installs before any conversation. It has had <a href="https://pypi.org/project/aladdinsdk/#history">14 releases since May 2024</a>, all alpha or beta. The core is at 2.0.0b10 as of July 2026 and the add-ons at 2.0.0b3<sup class="fnref"><a href="#s28">28</a>, <a href="#s17">17</a></sup>. Each release pins an old Snowflake library, so none installs on Python 3.13. The SDK’s dependencies also <a',
    '<p>The SDK’s dependencies <a')
rep(' (MCP, the Model Context Protocol, is the standard AI assistants use to pull data from other systems.) An outside',' An outside')
rep('Azure API Management”'+SUP(23)+'. Run modes, credential storage and API-gateway settings are the needs of a client’s engineering team.</p>','Azure API Management”'+SUP(23)+'.</p>')
# ---- page 8 / 9
rep('can reach, from 0 to 2. The total','can reach. The total')
rep('transcribed from recordings. Nothing can be run.</p>','transcribed from recordings.</p>')
# ---- Exhibit 11
rep('Aladdin won every bid that three public pension bodies scored, 2017 to 2025</p>','Aladdin won the tenders of three public pension bodies</p>')
rep('<colgroup><col style="width:126pt"><col style="width:44pt"><col><col style="width:150pt"></colgroup>\n<thead><tr><th>Buyer</th><th>Year</th><th>Weights or process</th><th>Outcome</th></tr></thead>',
    '<colgroup><col style="width:126pt"><col style="width:44pt"><col></colgroup>\n<thead><tr><th>Buyer</th><th>Year</th><th>Outcome</th></tr></thead>')
rep('<td>2025</td><td>Weights: technical 85, price 6, price sensitivity 6, contract terms 3</td>','<td>2025</td>')
rep('<td>2023</td><td>Weights: quality 70, cost 20, social value 10</td>','<td>2023</td>')
rep('<td>2017 and 2023</td><td>Run as a full and open competition; four bids were received each time</td>','<td>2017 and 2023</td>')
# ---- Finding 1 callout
rep('about direction.</span> Aladdin adoption is growing among clients whose records are public. Between 2023 and 2025, a bank’s proxy statement, an asset manager’s 10-K and three public pension buyers’ notices all record Aladdin. A named Studio story','about direction.</span> A named Studio story')
# ---- Finding 2
rep('<p>The other half of the growth story is the whole portfolio, public and private markets together. BlackRock bought eFront','<p>BlackRock bought eFront')
cut_block(' Hosting has moved to the public cloud as well. Microsoft wrote','second half of 2026</a>'+SUP(14)+'.')
rep('about direction.</span> BlackRock itself says growth will come from API calls and from the whole portfolio. The fastest-growing measure it showed investors is API calls. The data it is adding, private markets and Preqin, arrives through Data Cloud and Explore. Both are Studio surfaces. So Studio carries the growth story, whether or not BlackRock says its name.</p>',
    'about direction.</span> BlackRock itself says growth will come from API calls, the fastest-growing measure it showed investors. The data it is adding, private markets and Preqin, arrives through Data Cloud and Explore. Both are Studio surfaces.</p>')
# ---- Finding 3
rep('>Aladdin Copilot</a> is “now available to all Aladdin clients” and “will not give investment advice or respond to questions outside Aladdin platform boundaries”'+SUP(16)+'. Two of its engineers, Brennan Rosales, AI Engineering Lead, and Pedro Vicente Valdez, Principal AI Engineer, describe how it works. Copilot draws on','>Aladdin Copilot</a> draws on')
rep('<p>Outside the login, data providers have chosen the opposite design: they let the buyer’s own AI tools reach their data. <a href="https://modelcontextprotocol.io/">MCP</a> is the common standard AI assistants use to pull data from other systems'+SUP(61)+'. Six data','<p>Six data')
rep('AI access to their data; Aladdin has a job advert</p>','AI access to their data</p>')
cut_block('<figure class="exhibit" id="exhibit-15" style="margin-bottom:8pt">','</figure>\n')
rep('That description, in BlackRock’s own words, answers the connector question buyers now put in RFPs (Finding 4) better than an MCP server with a partial catalog would. It also lets BlackRock, not FactSet and LSEG, set the terms of comparison. I would hold any outside connector for now. The inside model already answers three governance questions: who can call what, with which permissions, and under which guardrails. An outside connector should wait until those are answered for outside callers. Exhibit 15 is the evidence. This is the Copilot direction in Part 3.</p>',
    'That description answers three governance questions: who can call what, with which permissions, and under which guardrails.</p>')
# ---- Finding 4
rep(' The host read out a slide saying that 60 to 70 percent of technology cost sits in “maintenance of current systems”'+SUP(8)+'. Clark Schafer of Alpha FMC, the panelist, said a transformation runs “roughly 12 to 18 months”'+SUP(8)+'.</p>','</p>')
rep('published captions'+SUP(8)+'. The webinar did not state attendee counts. Poll 2, which is not charted, asked what is driving the decision: “AI and data demands” led at 42 percent, and cost and speed to market tied for second.</p>','published captions'+SUP(8)+'.</p>')
rep('on the same webinar. <a href="https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions">“That word monolith is definitely being challenged in the market,”</a> she said. She described','on the same webinar. She described')
rep('Studio is the right kind of answer. The APIs, events and Data Cloud that Sewdass describes are the Studio pieces listed in Exhibit 4. It is not yet a finished answer, because the public catalog in Part 1 is mostly alpha and the SDK is beta. The directions in Part 3 put Studio into the RFP, where the buyer is asking.</p>','Studio is the right kind of answer.</p>')
cut_block('<h3>What would change my view</h3>','</ul>\n')
# ---- Part 3
rep('<p>Part 1 and the four findings point to six likely initial directions. They are not a plan. Exhibit 18 lists what I would need from inside BlackRock before sizing any of them. Each direction uses only what is already public, or already true inside BlackRock. Product owns what is built and when; marketing owns positioning, stories and sales material; compliance checks the final version.</p>\n','')
rep('Six likely initial directions, with an owner and a measure for each</p>','Five likely initial directions</p>')
rep('<colgroup><col style="width:92pt"><col style="width:48pt"><col><col style="width:68pt"><col style="width:84pt"></colgroup>\n<thead><tr><th>Direction</th><th>Rests on</th><th>What it involves</th>',
    '<colgroup><col style="width:96pt"><col><col style="width:72pt"><col style="width:88pt"></colgroup>\n<thead><tr><th>Direction</th><th>What it involves</th>')
rep('<td class="first">A named proof program</td><td>Finding 1</td>','<td class="first">A named proof program</td>')
rep('already on video'+SUP(45)+'. Ask each for one sentence about Studio, or one thing they built on it. A pension fund’s story still serves an insurer, so accept proof from a firm unlike the prospect</td><td>Marketing, with the client business for introductions</td>',
    'already on video'+SUP(45)+'</td><td>Marketing</td>')
cut_block('<tr><td class="first">Studio’s name beside one measure of API use</td>','</tr>\n')
rep('<td class="first">A one-page written definition of Studio</td><td>Part 1</td>','<td class="first">A one-page written definition of Studio</td>')
rep('into one written page. Have product and compliance review it. Use it in every deck and page</td>','into one written page</td>')
rep('<td class="first">An RFP-ready answer on the API suite</td><td>Finding 4</td><td>A document that answers the question Schafer says buyers now ask','<td class="first">An RFP-ready answer on the API suite</td><td>A document that answers the question buyers now ask')
rep('how clients build on top. The solutions team delivers it once a prospect is qualified</td>','how clients build on top</td>')
rep('<td class="first">A public description of the Copilot plugin model</td><td>Finding 3</td><td>One page, in BlackRock’s words, that says','<td class="first">A public description of the Copilot plugin model</td><td>One page that says')
rep('connect their own AI tools. Publish the plugin-model and governance parts now. Add the client','connect their own AI tools. Add the client')
rep('<td>Product, with marketing. Compliance reviews it</td>','<td>Product, with marketing</td>')
rep('<td class="first">A prospect-facing summary of the public API catalog</td><td>Part 1</td>','<td class="first">A prospect-facing summary of the public API catalog</td>')
rep('but without the specifications themselves. Share it before the first meeting, or put it on the Studio page</td>','but without the specifications themselves</td>')
rep('<td>Number of first meetings that skip the what-is-included discussion; prospects who arrive already holding the list</td>','<td>Number of meetings that skip the what-is-included discussion</td>')
rep('<div class="notes"><p><span class="lbl"></span>Source: my proposals, built on Part 1 and Findings 1 to 4. Receipts in the table point to the public facts each direction rests on.</p></div></figure>','</figure>')
cut_block('\n<h3>What I would need from inside BlackRock</h3>','</figure>\n')
# ---- About
rep('<p>The directions and questions in Part 3 are my proposals','<p>The directions in Part 3 are my proposals')
# ---- renumber exhibits 16->15, 17->16
rep('<figure class="exhibit chart keep" id="exhibit-16"><p class="ex-title"><span class="ex-num">Exhibit 16.</span>','<figure class="exhibit chart keep" id="exhibit-15"><p class="ex-title"><span class="ex-num">Exhibit 15.</span>')
rep('<figure class="exhibit" id="exhibit-17"><p class="ex-title"><span class="ex-num">Exhibit 17.</span>','<figure class="exhibit" id="exhibit-16"><p class="ex-title"><span class="ex-num">Exhibit 16.</span>')
open(p,'w',encoding='utf-8').write(s); print('cuts ok')
t=re.sub(r'<[^>]+>','',s)
for ph in ['Exhibit 17','Exhibit 18','Exhibit 15','Exhibit 16','six likely','Six likely','six directions','What would change','Rests on','Access.Internal','MCP']:
    print(ph, t.count(ph))
