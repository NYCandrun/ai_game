import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def SUP(*ns): return '<sup class="fnref">'+', '.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:70]); s=s.replace(a,b)
# page 2: replace the two paragraphs under the lede
i=s.index('<p class="lede">'); i=s.index('</p>\n',i)+len('</p>\n')
j=s.index('<div class="method"',i)
new2=('<p style="margin-bottom:8pt">Studio is Aladdin’s developer and data layer: APIs and events, Aladdin Data Cloud on Snowflake, and developer tools'+SUP(1)+'. Many data providers now offer AI tools a way to read their data'+SUP(51,55,56,58)+'. Aladdin’s APIs also change the book. They post orders and set compliance rules, under each user’s permissions and with a compliance check on every order'+SUP(11)+'.</p>\n'
'<p style="margin-bottom:8pt">Letting AI tools act will not stay unique; SimCorp has announced AI agents'+SUP(52)+'. What BlackRock can show is its own use. About 100 of its applications and thousands of Copilot tools already call these APIs every day'+SUP(3)+'. Buyers say AI is changing what they build, and BlackRock has told investors that API calls will grow 17x by 2030'+SUP(2,40)+'. Part 3 sets out this direction, what would have to be true for it to hold, and four pieces of marketing work that would follow.</p>\n')
s=s[:i]+new2+s[j:]
# page 13: replace everything above Exhibit 14
i=s.index('<h2><span class="pn">Part 3</span>Directions to explore</h2>\n')+len('<h2><span class="pn">Part 3</span>Directions to explore</h2>\n')
j=s.index('<figure class="exhibit keep" id="exhibit-14">')
new13=('<p>The findings suggest that Studio could be presented as the place where a client’s own AI tools act on investment data under the same controls BlackRock’s own business runs on. BlackRock has said parts of this. It sells Aladdin as the system it runs internally'+SUP(7,10,13,3)+'. Its speakers have said that the system of record underpins anything built with AI'+SUP(2)+', and that the data model is being structured for agentic use'+SUP(49)+'. I have not found it describe Studio this way.</p>\n'
'<p>Letting AI tools act is unlikely to stay unique. SimCorp has announced AI agents, Arcesium an AI platform, and other systems of record will likely follow'+SUP(52,53,54)+'. What BlackRock can show is its own use. About 100 of its applications and thousands of Copilot tools, built by 50 to 60 of its teams, call these APIs every day under each user’s permissions'+SUP(3)+'. Every order is checked for compliance by default, and Copilot’s guardrails are tested daily'+SUP(11,3)+'. A client’s AI tools would work under controls BlackRock already relies on for its own business. How those tools would connect is not public'+SUP(60)+'.</p>\n'
'<p>Buyers say AI is changing what they build. “AI and data demands” led BlackRock’s webinar poll at 42 percent as the reason firms are rethinking what to build and what to buy, and buyers now ask about APIs and connectors in RFPs'+SUP(2)+'. The poll did not ask whether clients want AI tools that act on Aladdin, and it gives no sample size.</p>\n'
'<p>The client base is large. BlackRock serves hundreds of Aladdin clients in 70 countries, and its technology services revenue was $2.0 billion in 2025'+SUP(3,4)+'. It projects API calls to grow 17x by 2030, and AI tools acting for clients could become a large source of them'+SUP(40)+'. Linking that figure to Studio is my inference. How many clients use the APIs today, or run their own AI tools, is not public.</p>\n'
'<p>Three things would have to be true for this direction to hold. Clients would have to want AI tools that act, not only ones that answer questions. Their risk teams and regulators would have to accept it, which likely means a person approves each action. And BlackRock would have to open its controls to tools it did not build.</p>\n')
s=s[:i]+new13+s[j:]
# Exhibit 15
rep('Five pieces of marketing work to explore, in the order I would start them</p>','Four pieces of marketing work to explore, in the order I would start them</p>')
rep('and the Snowflake and Databricks answer.</td>','and the Snowflake and Databricks answer, plus how a client’s own AI tools would connect.</td>')
m=re.search(r'<tr><td class="first">4</td>.*?</tr>\n',s,flags=re.S); assert m
row4=('<tr><td class="first">4</td><td class="first">A worked example: an AI-proposed rebalance</td><td>A page and a demo in which a client’s AI tool proposes a rebalance through the order API. Aladdin runs what-if and compliance on every order and returns any violations, and a portfolio manager approves before anything trades. Sewdass names rebalancing tools as what clients build on Aladdin’s APIs'+SUP(2)+'.</td><td>Meetings that open on this example; pipeline tagged to it; API calls from clients who build it</td></tr>\n')
s=s.replace(m.group(0),row4,1)
m=re.search(r'<tr><td class="first">5</td>.*?</tr>\n',s,flags=re.S); assert m; s=s.replace(m.group(0),'',1)
open(p,'w',encoding='utf-8').write(s); print('ok')
