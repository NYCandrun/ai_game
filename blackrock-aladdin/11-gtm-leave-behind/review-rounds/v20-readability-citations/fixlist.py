import html
E=html.escape
items=[
("A. Garbled or contradicts something nearby",[
("2","Executive summary, end of paragraph 2","Part 3 sets out this direction, what would have to be true for it to hold, and four pieces of marketing work that would follow.","Part 3 sets out this direction: clients’ AI tools acting on Aladdin under BlackRock’s own controls. It covers what would have to be true, and four pieces of marketing work that would follow.","“This direction” points back to nothing. The sentence before it is about API calls."),
("3","Part 1 opening","The organization is “around 7,000 people, with over 4,000 of those being engineers.” They maintain “around 100 Aladdin front-end applications” [9].","The Aladdin organization is “around 7,000 people, with over 4,000 of those being engineers.” It maintains “around 100 Aladdin front-end applications” [9].","Reads as BlackRock’s whole headcount. Rosales says “The Aladdin organization is made up of around 7,000 people” (1:44)."),
("3","Part 1 opening, against Exhibit 1","BlackRock sells Aladdin as four platforms … They are the Aladdin platform, eFront, Aladdin Wealth and Preqin [13]. (Exhibit 1 below: eight products, no Preqin row, eFront “holding Preqin”.)","Add after it: “Exhibit 1 lists eight products sold across them.” eFront row: “A private-fund platform that now includes Preqin [18] …”","The text says four platforms including Preqin. The exhibit right below says eight products and puts Preqin inside eFront."),
("3","Exhibit 2 title","The public APIs follow a trade from order to NAV","The public APIs cover a trade from order to NAV, except the position step","The exhibit’s own step 4 says no public API covers positions."),
("5–6","Woodhead quote, block quote and Exhibit 7","“… as a set of APIs events.”","“… as a set of APIs [and] events.”","The captions’ wording reads as your typo. Brackets mark the added word."),
("6","Exhibit 6 versus Exhibit 7, Woodhead","Exhibit 6: “the three-part definition”. Exhibit 7: “APIs, events, Data Cloud, developer tools” (four).","Exhibit 7: “APIs and events, Data Cloud, developer tools”.","Two exhibits on facing pages count Woodhead’s parts differently."),
("6","Goel, body and Exhibit 7","He also describes a near-real-time data store [40]. Exhibit 7: “APIs, events, a near-real-time data store”.","He also describes Data Cloud as a near-real-time data store [40]. Exhibit 7: “APIs, events, Data Cloud”.","Exhibit 6 says Goel speaks about Data Cloud. Exhibit 7 seems to say he doesn’t. Goel says “ADC”, which is Aladdin Data Cloud."),
("7","Kinds of record, paragraphs around Exhibit 8","A second kind of record is code … Janus Henderson’s 10-K says … Public buyers add a third kind of record.","Move the Janus Henderson sentence up beside JPMorgan and say: “Company filings are the first kind of record.”","The list announces a second and third kind but never names the first, and puts a filing under “code”."),
("7","Exhibit 8 note","In 2016 it said it was connecting to Aladdin for custody clients [51]. That 2016 report is trade press, not a JPMorgan or BlackRock document.","A 2016 trade press report says JPMorgan was connecting to Aladdin for its custody clients [51]. The report is not a JPMorgan or BlackRock document.","“That 2016 report” points back to nothing, and “it said” reads as JPMorgan speaking."),
("12","Part 3, paragraph 1","I have not found it describe Studio this way.","I have not seen BlackRock describe Studio this way.","Broken grammar, and “it” is unclear."),
("12","Part 3, paragraph 4","It projects API calls to grow 17x by 2030, and AI tools acting for clients could become a large source of them [11]. Linking that figure to Studio is my inference.","It projects API calls to grow 17x by 2030 [11]. My inference is that clients’ AI tools, acting through Studio, could become a large source of those calls.","The source sits on your inference, so it reads as if BlackRock said AI tools would drive the calls."),
("12","Exhibit 14 hatched box and note","Box: “Nearest public sign: an internal job posting.” Note: “a September 2026 posting for an internal data role”.","Box: “Nearest public sign: a BlackRock job posting that names MCP.” Note: “a September 2026 Forward Deploy Engineer posting for Aladdin Data that names MCP and AI agents [77].”","A public posting called “internal”. Exhibit 12 describes the same posting differently."),
("13","Exhibit 15, row 4","Aladdin runs what-if and compliance on every order and returns any violations, and a portfolio manager approves before anything trades [6].","Aladdin runs a compliance check on every order by default and returns any violations. An order can also be posted as a what-if test [6]. In the demo, a portfolio manager approves before anything trades.","The source lands on the approval, which is the demo’s design. What-if is an option, not on every order."),
("15","About this document","Facts are as of October 19, 2026, unless an exhibit gives another date.","Facts are as of October 19, 2026, unless an exhibit or a source entry gives another date.","Several sources are dated October 20."),
]),
("B. Hints at a point instead of saying it",[
("8","Top of page, Finding 1","None of this proof names Studio, which matters less than it seems.","None of this proof names Studio. It still backs a Studio pitch, because a buyer wants to know another institution built on Aladdin and stayed.","The reader has to work out why it matters less."),
("10","Finding 3 box","A public account of the Copilot plugin model would cover … That account answers three governance questions …","BlackRock could publish how Copilot’s plugin model works: which production APIs each tool calls, which user groups may use each tool, and the tested guardrails that block investment advice [9, 23].","Never says what to do. The tense slips, and the three items don’t match the three questions."),
("11","Finding 4 box","Studio is the right kind of answer.","Studio is BlackRock’s answer to the RFP’s API question, so it could lead the API section of a response.","“The right kind of answer” gestures instead of saying why."),
]),
("C. Citation in the wrong place or missing",[
("3","Exhibit 2, Order step, “Where”","Explore [27]","Explore what-if, then the order [27]","The recording shows Explore’s what-if tool, never an order."),
("3","Exhibit 2, Trade step","Broker confirms via BrokerConfirm RoutingAPI [6]","Confirmed with the broker. BrokerConfirm RoutingAPI sets where confirms go [6]","The spec doesn’t say the broker confirms through the API."),
("3","Exhibit 2, Position step, “Who”","Investment team [22]","Investment team. (Move [22] to the “Where” cell: Data Cloud [22, 28].)","Newman backs IBOR data going into Data Cloud, not an “investment team”."),
("3","Exhibit 1, Aladdin Provider","Links custodians and administrators to a client’s Aladdin, and they pay BlackRock for it [25]","Gives custodians and administrators access to Aladdin, and they pay BlackRock for it [25]","The prospectus doesn’t say “a client’s Aladdin”."),
("4","Exhibit 3 note","Rosales and Vicente Valdez at 2:35, for the apps and Copilot [9]","Rosales at 2:35 and 4:31, for the apps and Copilot [9]","The “each tool matches a production API” line is at 4:31, and only Rosales speaks at 2:35."),
]),
]
rows=[]
n=0
for sec,its in items:
    rows.append(f'<h2>{E(sec)} <span class="c">{len(its)}</span></h2>')
    for pg,where,cur,new,why in its:
        n+=1
        rows.append(f'<div class="it"><div class="hd"><b>{n}.</b> Page {E(pg)} · {E(where)}</div><div class="g"><div class="l">Now</div><div class="cur">{E(cur)}</div><div class="l">Fix</div><div class="new">{E(new)}</div><div class="l">Why</div><div class="why">{E(why)}</div></div></div>')
doc=f'''<!doctype html><html><head><meta charset="utf-8"><title>v20 fix list</title><style>
@page{{size:612pt 792pt;margin:44pt 50pt}}
body{{font:10pt/1.4 "Barlow",Helvetica,Arial,sans-serif;color:#111}}
h1{{font-size:18pt;margin:0 0 4pt}} h1:before{{content:"";display:block;width:50pt;height:5pt;background:#FFCE00;margin-bottom:10pt}}
.sub{{color:#555;margin:0 0 6pt}} h2{{font-size:12.5pt;border-top:2pt solid #111;padding-top:6pt;margin:16pt 0 6pt}} .c{{color:#777;font-weight:400}}
.it{{break-inside:avoid;border-bottom:0.6pt solid #ccc;padding:6pt 0}} .hd{{font-size:10.5pt;margin-bottom:3pt}}
.g{{display:grid;grid-template-columns:34pt 1fr;row-gap:2pt}} .l{{font-size:8pt;text-transform:uppercase;letter-spacing:.5pt;color:#777;padding-top:1.5pt}}
.cur{{color:#555}} .new{{background:#FFF6CC;padding:1pt 4pt}} .why{{font-size:9pt;color:#333}} ul{{margin:4pt 0 0 14pt;padding:0}} li{{margin:2pt 0}}
</style></head><body>
<h1>v20: what reads badly, and citations in the wrong place</h1>
<p class="sub">Four agents read every page for clarity. Two re-checked the 54 citations that changed since the last check, and 49 of them are right. These are the must-fix items, each with its exact wording now and a proposed fix. The document is unchanged.</p>
<ul><li>Citation order and numbering are correct throughout.</li><li>One reviewer item was dropped. It said “Letting AI tools act is unlikely to stay unique” contradicts the next sentence, but that sentence is the evidence for it.</li><li>About 70 smaller “should fix” items are in the review files, not listed here.</li></ul>
{''.join(rows)}
</body></html>'''
open("/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/v20check/v20_fix_list.html","w").write(doc); print(n,"items")
