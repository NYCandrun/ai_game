import sys,re
p=sys.argv[1]; h=open(p,encoding="utf-8").read()
def rep(a,b,n=1):
    global h; c=h.count(a); assert c==n,(c,a[:80]); h=h.replace(a,b)
sup=lambda *x:'<sup class="fnref">'+', '.join(f'<a href="#s{i}">{i}</a>' for i in x)+'</sup>'
# 1 exec summary
rep('Part 3 sets out this direction, what would have to be true for it to hold, and four pieces of marketing work that would follow.',
    'Part 3 sets out this direction: clients’ AI tools acting on Aladdin under BlackRock’s own controls. It covers what would have to be true, and four pieces of marketing work that would follow.')
# 2 Aladdin organization
rep('The organization is “around 7,000 people, with over 4,000 of those being engineers.” They maintain','The Aladdin organization is “around 7,000 people, with over 4,000 of those being engineers.” It maintains')
# 3 four platforms vs eight products
rep('Aladdin Wealth and Preqin'+sup(13)+'.','Aladdin Wealth and Preqin'+sup(13)+'. Exhibit 1 lists eight products sold across them.')
rep('A private-fund platform holding Preqin'+sup(18),'A private-fund platform that now includes Preqin'+sup(18))
# 4 Exhibit 2 title
rep('The public APIs follow a trade from order to NAV</p>','The public APIs cover a trade from order to NAV, except positions</p>')
# 5 APIs [and] events (block quote + Exhibit 7)
rep('as a set of APIs events.','as a set of APIs [and] events.',2)
# 6 Woodhead parts
rep('<td>APIs, events, Data Cloud, developer tools</td>','<td>APIs and events, Data Cloud, developer tools</td>')
# 7 Goel
rep('He also describes a near-real-time data store'+sup(40),'He also describes Data Cloud as a near-real-time data store'+sup(40))
rep('<td>APIs, events, a near-real-time data store</td>','<td>APIs, events, Data Cloud</td>')
# 8 kinds of record
rep('On BlackRock’s video, Hans Georgeson','The first kind of record is what clients say and file. On BlackRock’s video, Hans Georgeson')
jh=re.search(r' Janus Henderson’s <a href="[^"]+">10-K</a> says that in the third quarter of 2025 the firm chose to move its investment management system to Aladdin, “a complex, multi-year initiative”'+re.escape(sup(55))+r'\.',h).group(0)
rep(jh,'')
rep('$25.6 million in 2025</a>'+sup(49,50)+'.','$25.6 million in 2025</a>'+sup(49,50)+'.'+jh)
# 9 Exhibit 8 note
rep('<a href="https://www.thetradenews.com/jp-morgan-to-connect-to-blackrocks-aladdin/">In 2016 it said it was connecting to Aladdin</a> for custody clients'+sup(51)+'. That 2016 report is trade press, not a JPMorgan or BlackRock document.',
    'A <a href="https://www.thetradenews.com/jp-morgan-to-connect-to-blackrocks-aladdin/">2016 trade press report</a> says JPMorgan was connecting to Aladdin for its custody clients'+sup(51)+'. The report is not a JPMorgan or BlackRock document.')
# 10 page 12 para 1
rep('I have not found it describe Studio this way.','I have not seen BlackRock describe Studio this way.')
# 11 17x
rep('It projects API calls to grow 17x by 2030, and AI tools acting for clients could become a large source of them'+sup(11)+'. Linking that figure to Studio is my inference.',
    'It projects API calls to grow 17x by 2030'+sup(11)+'. My inference is that clients’ AI tools, acting through Studio, could become a large source of those calls.')
# 12 Exhibit 14 hatched box + note + aria
rep('<text x="1088" y="154" class="s">an internal job posting.</text>','<text x="1088" y="154" class="s">a job posting naming MCP.</text>')
rep('the nearest public sign is an internal job posting.','the nearest public sign is a job posting that names MCP.')
rep('The nearest public sign is a September 2026 posting for an internal data role that names MCP and AI agents'+sup(77),
    'The nearest public sign is a September 2026 Forward Deploy Engineer posting for Aladdin Data that names MCP and AI agents'+sup(77))
# 13 Exhibit 15 row 4
rep('Aladdin runs what-if and compliance on every order and returns any violations, and a portfolio manager approves before anything trades'+sup(6)+'.',
    'Aladdin runs a compliance check on every order by default and returns any violations. An order can also be posted as a what-if test'+sup(6)+'. In the demo, a portfolio manager approves before anything trades.')
# 14 About
rep('unless an exhibit gives another date.','unless an exhibit or a source entry gives another date.')
# 15 p8 top
rep('None of this proof names Studio, which matters less than it seems. Studio is sold for building custom applications on Aladdin, so a buyer wants to know that another institution built on the platform and stayed.',
    'None of this proof names Studio. It still backs a Studio pitch, because Studio is sold for building custom applications on Aladdin, and a buyer wants to know that another institution built on the platform and stayed.')
# 16 Finding 3 box
rep('A public account of the Copilot plugin model would cover the production Aladdin APIs its tools call, which user groups may use each tool, and tested no-advice guardrails'+sup(9,23)+'. That account answers three governance questions: who can call what, with which permissions, and under which guardrails.',
    'BlackRock could publish how Copilot’s plugin model works: which production APIs each tool calls, which user groups may use each tool, and the tested guardrails that block investment advice'+sup(9,23)+'.')
# 17 Finding 4 box
rep('Buyers now ask in RFPs whether they can build on the platform. Studio is the right kind of answer.',
    'Buyers now ask in RFPs whether they can build on the platform. Studio is BlackRock’s answer to that question, so it could lead the API section of a response.')
# 18 Explore
rep('">Explore</a>'+sup(27)+'</div>','">Explore what-if</a>'+sup(27)+'</div>')
# 19 Trade
rep('<div class="det">Broker confirms via <a','<div class="det"><a')
rep('<code>BrokerConfirm<wbr>RoutingAPI</code></a>'+sup(6)+'</div>','<code>BrokerConfirm<wbr>RoutingAPI</code></a> holds where confirms go'+sup(6)+'</div>')
# 20 Position
rep('<div class="who">Investment team'+sup(22)+'</div>','<div class="who">Investment team</div>')
rep('">Data Cloud</a>'+sup(28)+'</div>','">Data Cloud</a>'+sup(22,28)+'</div>')
# 21 Provider
rep('Links custodians and administrators to a client’s Aladdin, and <a','Gives custodians and administrators access to Aladdin, and <a')
# 22 Exhibit 3 note
rep('>Rosales and Vicente Valdez at 2:35</a>, for the apps and Copilot','>Rosales at 2:35 and 4:31</a>, for the apps and Copilot')
open(p,"w",encoding="utf-8").write(h); print("all applied")
