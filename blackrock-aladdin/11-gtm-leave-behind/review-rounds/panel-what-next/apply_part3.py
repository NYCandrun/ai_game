import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
# cover subtitle and card
rep('<p class="subtitle">What public sources show about Studio</p>','<p class="subtitle">What public sources show about Studio, and directions to explore for marketing it</p>')
rep('<p class="pt"><a href="#f1">Four findings on BlackRock’s direction and the market</a></p><p class="pc">Page 10</p></div>',
    '<p class="pt"><a href="#f1">Four findings on BlackRock’s direction and the market</a></p><p class="pc">Page 10</p></div>\n    <div><span class="accent-bar"></span><p class="pn">Part 3</p><p class="pt"><a href="#part-3">Directions to explore</a></p><p class="pc">Page 15</p></div>')
# executive summary
rep('and rivals already sell to that demand<sup class="fnref"><a href="#s6">6</a></sup>.</p>',
    'and rivals already sell to that demand<sup class="fnref"><a href="#s6">6</a></sup>. Part 3 lists five directions to explore for marketing Studio, each resting on a finding.</p>')
# Part 3 section before the About page
part3='''<section class="chapter part" id="part-3">
<h2><span class="pn">Part 3</span>Directions to explore</h2>
<p>Each of these follows from a finding and rests only on what is public. I would want to test each inside BlackRock before sizing it.</p>
<figure class="exhibit" id="exhibit-16"><p class="ex-title"><span class="ex-num">Exhibit 16.</span> Five directions to explore for marketing Studio</p>
<table>
<colgroup><col style="width:88pt"><col><col style="width:134pt"><col style="width:118pt"></colgroup>
<thead><tr><th>Direction</th><th>What marketing would produce</th><th>Why</th><th>How to measure it</th></tr></thead>
<tbody>
<tr><td class="first">An RFP answer on the API suite</td><td>A sales-ready answer: the API catalog by domain with the labels the public packages carry, the permission model Copilot runs on, the gateway pattern a client has built, and a straight answer on Snowflake and Databricks connectivity</td><td>Buyers now put the question in RFPs (Finding 4); solutions engineers answer it from scratch today</td><td>Time to answer the API section of an RFP; share of RFPs where Studio is scored; win rate where it is</td></tr>
<tr><td class="first">A named client on the record</td><td>One client story, cleared for the Studio page and the RFP answer; Janus Henderson first, a public pension award as fallback</td><td>Filings, code and tenders already show who builds on Aladdin (Finding 1), and the Studio page names no one</td><td>Named references in use by sales; deals in which one is cited</td></tr>
<tr><td class="first">A public account of the Copilot plugin model</td><td>A page on who can call what, with which permissions, under which guardrails, plus one sentence on outside AI tools</td><td>Eight of nine comparable providers have announced AI access; BlackRock has the deepest implementation and a job advert (Finding 3)</td><td>Page published and dated; prospects stop raising connectors in deal reviews</td></tr>
<tr><td class="first">Compliance reporting as a worked example</td><td>A use-case page and a demo on Data Cloud plus the compliance APIs</td><td>Attendees at BlackRock’s own webinar named it first among things they would stop running in house (Finding 4)</td><td>Meetings that open on the use case; pipeline tagged to it</td></tr>
<tr><td class="first">Private-markets data as a worked example</td><td>One flagship piece showing Preqin and eFront data reaching a client’s Snowflake through Data Cloud</td><td>A story no system-of-record rival can tell (Finding 2); answers the buyers who cited AI and data demands</td><td>Clients with a Data Cloud instance who take the private-markets data; the piece’s use in client meetings</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: my proposals, built on the findings in Part 2.</p></div></figure>
</section>

'''
rep('</section>\n\n\n\n<section class="fullpage back">','</section>\n\n'+part3+'<section class="fullpage back">')
open(p,'w',encoding='utf-8').write(s); print('ok')
