import sys, re
F = sys.argv[1]
html = open(F, encoding="utf-8").read()
orig = html

def rep(old, new, count=1):
    global html
    n = html.count(old)
    assert n == count, f"expected {count}, found {n}: {old[:90]!r}"
    html = html.replace(old, new)

def sup(*nums):
    return '<sup class="fnref">' + ', '.join(f'<a href="#s{n}">{n}</a>' for n in nums) + '</sup>'

# ---------- Item 1: executive summary ----------
rep('<p class="lede">An outsider with AI agents and about a day can assemble a detailed, sourced picture of Aladdin Studio from BlackRock’s own specifications, pages and recordings, plus filings and code. This is what it looks like, what it says about direction, and the quick wins for marketing Studio.</p>',
    '<p class="lede">Studio is the product behind the growth story BlackRock tells investors, but the story never names it, and the public proof that clients build on Aladdin is real but not Studio-specific. The quick wins close both gaps inside the enterprise selling model, without changing what a prospect can access.</p>')

rep('''  <div><span class="accent-bar"></span><p class="num">54</p><p class="cap">Public API specifications read, in 11 PyPI packages covering 301 operations</p></div>
  <div><span class="accent-bar"></span><p class="num">128</p><p class="cap">Recordings transcribed and checked, 121 of them from BlackRock’s own channels and partner stages</p></div>
  <div><span class="accent-bar"></span><p class="num">17x</p><p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, from the 2025 Investor Day</p></div>
</div>
<p class="stats-src">Source: <a href="https://pypi.org/search/?q=asdk_plugin">asdk_plugin packages on PyPI</a><sup class="fnref"><a href="#s1">1</a></sup>; the recordings listed under S in the Source register; <a href="https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf">BlackRock 2025 Investor Day</a><sup class="fnref"><a href="#s2">2</a></sup>.</p>''',
    '''  <div><span class="accent-bar"></span><p class="num">17x</p><p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, on the 2025 Investor Day slide on keeping the cost of growth low, against 4x for model portfolios, 2x for portfolios and 1.3x for trade allocations</p></div>
  <div><span class="accent-bar"></span><p class="num">$25.6M</p><p class="cap">JPMorgan Chase’s payments to BlackRock for Aladdin in 2025, reported in its own proxy statement; almost six times the 2017 figure</p></div>
  <div><span class="accent-bar"></span><p class="num">0</p><p class="cap">Mentions of Studio by a BlackRock executive on 26 earnings calls since 2020, Q1 2020 to Q2 2026</p></div>
</div>
<p class="stats-src">Source: <a href="https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf">BlackRock 2025 Investor Day</a>''' + sup(2) + '''; the slide does not say which products generate the API calls, so reading them as Studio is my inference. <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A">JPMorgan Chase proxy statements</a>''' + sup(45, 7) + '''; <a href="https://www.roic.ai/quote/BLK/transcripts">third-party earnings call transcripts</a>''' + sup(52) + '''.</p>''')

rep('''<p><b>What was found.</b> Studio is Aladdin’s developer and data layer: APIs and events, a Python SDK on GitHub, and Aladdin Data Cloud on Snowflake, described the same way by five BlackRock speakers since 2024<sup class="fnref"><a href="#s3">3</a>, <a href="#s4">4</a>, <a href="#s5">5</a>, <a href="#s6">6</a></sup>. Proof of use sits in public records: JPMorgan Chase’s proxy statements, Janus Henderson’s commits and 10-K, Royal London’s chief executive on video, and three pension funds’ tender notices<sup class="fnref"><a href="#s7">7</a>, <a href="#s8">8</a>, <a href="#s9">9</a>, <a href="#s10">10</a>, <a href="#s11">11</a></sup>.</p>
<p><b>What it says about direction.</b> APIs and data access are the growth engine: the fastest-growing measure BlackRock showed investors is API calls<sup class="fnref"><a href="#s2">2</a></sup>. The product is the whole portfolio, public and private, fed through Data Cloud and Explore<sup class="fnref"><a href="#s12">12</a></sup>. AI stays inside the platform while data providers market connectors outside<sup class="fnref"><a href="#s13">13</a>, <a href="#s14">14</a></sup>. Buyers tell BlackRock’s own webinar they want a core platform plus their own builds<sup class="fnref"><a href="#s15">15</a></sup>.</p>
<p><b>The quick wins.</b> Named proof from clients whose Aladdin relationship is already public; Studio’s name on the API growth story; a written one-page version of the spoken message; an RFP-ready API answer; a decision on describing the Copilot plugin model; a “what is in the box” summary. None opens the gate.</p>''',
    '''<p>Studio is Aladdin’s developer and data layer: APIs and events, a Python SDK on GitHub and Aladdin Data Cloud on Snowflake, described the same way by five BlackRock speakers since 2024''' + sup(6) + '''. Proof of use sits in public records: JPMorgan Chase’s proxy statements, Janus Henderson’s commits and 10-K, Royal London’s chief executive on video and three pension funds’ tender notices. I assembled that picture with AI agents in about a day, from 54 public API specifications, 128 recordings, filings and code; Part 1 is what it shows.</p>
<p>Four signals point the same way. The fastest-growing measure BlackRock showed investors is API calls, 17x by 2030 against 4x for model portfolios, though the slide does not say which products generate the calls, so reading them as Studio is my inference. The product is the whole portfolio, public and private, fed through Data Cloud and Explore''' + sup(12) + '''. Copilot, BlackRock’s AI front door, stays inside the platform while data providers market connectors outside''' + sup(14) + '''. Buyers at BlackRock’s own webinar said they want a core platform plus their own builds, and rivals are selling to that''' + sup(15) + '''.</p>
<p>Six quick wins, in the order I would do them:</p>
<ol>
<li>Named proof from clients whose Aladdin relationship is already public.</li>
<li>Studio’s name beside the API-call projection, in investor and client materials.</li>
<li>A written one-page version of the definition five speakers give only in recordings.</li>
<li>An RFP-ready answer to the API question buyers now ask.</li>
<li>A published description of the Copilot plugin model.</li>
<li>A prospect-facing “what is in the box” summary of the public catalog.</li>
</ol>''')

# ---------- Items 1, 2, 3: method box ----------
rep('''<p><b>Public material only.</b> BlackRock pages, the 54 specifications inside 11 public <code>asdk_plugin</code> packages, 128 recordings (121 from BlackRock’s own channels and partner stages), SEC filings, procurement notices, GitHub and PyPI. Part is machine-transcribed, and names and jargon can be mis-heard; the register marks which. Figures may be outdated, and there is no internal product context, so conclusions may be wrong for reasons the author cannot see.</p>
<p><b>Enterprise gating is expected.</b> Aladdin is enterprise software sold to large institutions, and gating documentation, sandboxes and credentials behind qualification is the normal model for that market; a qualified prospect gets them from BlackRock’s solutions team. The right-hand column of Exhibit 6 describes the sequence after qualification, not an absence.</p>
<p><b>Three corrections already made.</b> 58 specifications became 54 once the SDK’s four utility APIs were set aside; a widely repeated “68 percent” survey figure was dropped because it could not be found in the report it is attributed to; “more than 2,000 citizen developers” became 3,000, counted inside BlackRock rather than among clients.</p>''',
    '''<p><b>Public material only.</b> BlackRock pages, the 54 specifications inside 11 public <code>asdk_plugin</code> packages, 128 recordings (121 from BlackRock’s own channels and partner stages), SEC filings, procurement notices, GitHub and PyPI, pulled by AI agents and checked by me against each document. Part is machine-transcribed, and names and jargon can be misheard; the register marks which. Figures may be outdated, and I have no internal product context, so conclusions may be wrong for reasons I cannot see.</p>''')

# ---------- Item 2 and 7: Part 1 opening ----------
rep('Its AI engineering lead put the scale this way at a LangChain conference in 2025:',
    'Brennan Rosales, its AI Engineering Lead, put the scale this way at a LangChain conference in 2025:')
rep(''' It is enterprise software, sold to large institutions through a solutions team; documentation, sandboxes and credentials follow qualification, which is the normal model in that market. BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code.</p>''',
    ''' BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code. Aladdin is sold the way enterprise platforms are sold: a conversation first, then documentation, a sandbox and credentials from the solutions team once a prospect is qualified. What follows is what is out there before that conversation.</p>''')

# ---------- Item 7: Exhibit 1 ----------
rep('A private fund investment from due diligence through cash flows and reporting; folded Preqin into eFront Insight, with ',
    'A private-fund investment platform covering due diligence through cash flows and reporting; Preqin was folded into eFront Insight, with ')
rep('“API-first”</a>, for “a professional engineer', '“API-first,”</a> for “a professional engineer')
rep('; Newman places it <a href="https://www.blackrock.com/aladdin/discover/podcast/snowflake-podcast-data-the-key-ingredient">“part of Studio”</a>',
    '; Richard Newman, General Manager, Aladdin Studio, calls it <a href="https://www.blackrock.com/aladdin/discover/podcast/snowflake-podcast-data-the-key-ingredient">“part of Studio”</a>')

# Exhibit 3 source, Exhibit 4 Goel
rep('Rosales and Valdez on the Copilot plugin registry', 'Brennan Rosales and Pedro Vicente Valdez on the Copilot plugin registry')
rep('Goel’s target is <a href="https://www.blackrock.com/aladdin/discover/expertise/webinars/data-as-a-strategic-assets-for-pensions">“every single transaction ... via an event, via an API”</a>',
    'Diwakar Goel, Global Head of Data, Aladdin, sets the target as <a href="https://www.blackrock.com/aladdin/discover/expertise/webinars/data-as-a-strategic-assets-for-pensions">“every single transaction ... via an event, via an API”</a>')

# ---------- Item 6: first person in exhibit notes ----------
rep('Counts recomputed by the author from the files.', 'Counts are mine, recomputed from the files.')
rep('Source: the author’s test of each platform’s public pages', 'Source: my test of each platform’s public pages')
rep('Counts are the author’s tally. Zero counts are reliable', 'My tally. Zero counts are reliable')
rep('Source: the author’s reading of the Copilot page', 'Source: my reading of the Copilot page')
rep('Source: the author’s proposals, built on Part 1 and Findings 1 to 4.', 'Source: my proposals, built on Part 1 and Findings 1 to 4.')
rep('Source: the author’s questions. Question 3 refers', 'Source: my questions. Question 3 refers')

# ---------- Item 2: page 6 ----------
rep(' and records what is out there at each step and what follows qualification. A qualified prospect gets documentation, a sandbox and credentials through BlackRock’s solutions team; the right-hand column is that sequence, not a gap.</p>',
    ' and records what is out there at each step and what follows qualification.</p>')

# ---------- Items 4 and 7: Exhibit 7 ----------
rep('1: Partial or after signup or approval', '1: Partial or after sign-up or approval')
rep('For the AI connector, 2 means an MCP server or connector that outside AI tools can use, 1 one announced or in limited release, and 0 none, or an assistant that works only inside the vendor’s own platform.',
    'For the AI connector, 2 means an MCP server or connector that outside AI tools can use; 1 means one announced or in limited release; 0 means none, or an assistant that works only inside the vendor’s own platform.')
old_ex7_para = '''<p>Exhibit 7 puts Studio beside ten platforms a Studio buyer also deals with, on eight things a developer with no client relationship can reach<sup class="fnref"><a href="#s34">34</a>, <a href="#s35">35</a>, <a href="#s36">36</a></sup>. Investment platforms mostly gate: documentation, a sandbox and a first call follow a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium. Data and cloud platforms, which sell to developers directly, mostly self-serve. Only Studio, among the investment platforms, offers an <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a><sup class="fnref"><a href="#s28">28</a></sup>. The exhibit shows each vendor’s model, not a score against Aladdin.</p>

'''
new_ex7_para = '''<p>Exhibit 7 puts Studio beside 10 platforms that a Studio buyer also deals with, on eight things a developer with no client relationship can reach<sup class="fnref"><a href="#s34">34</a>, <a href="#s35">35</a>, <a href="#s36">36</a></sup>. The total counts how many of the eight criteria a developer can meet before any client relationship exists, so it measures each vendor’s selling model. Investment platforms cluster low because they gate: documentation, a sandbox and a first call follow a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium. Data and cloud platforms, which sell to developers directly, cluster high. Only Studio, among the investment platforms, offers an <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a><sup class="fnref"><a href="#s28">28</a></sup>.</p>
'''
rep(old_ex7_para, '')
rep('''</div></figure>




<figure class="exhibit keep" id="exhibit-7">''', '''</div></figure>
''' + new_ex7_para + '''<figure class="exhibit keep" id="exhibit-7">''')

# ---------- Items 2 and 7: page 8 ----------
rep('Newman places Data Cloud “part of Studio”', 'Newman calls Data Cloud “part of Studio”')
rep('and nothing can be run; that fits how Aladdin is sold, through a solutions team to qualified institutions, after a conversation.</p>',
    'and nothing can be run.</p>')
rep('Snowflake podcast, Nov 2025', 'Snowflake podcast, November 2025')
rep('Never Done, Jan 2025', 'Never Done, January 2025')
rep('Richard Newman, Jan 2025', 'Richard Newman, January 2025')
rep('Dave Woodhead, Nov 2025', 'Dave Woodhead, November 2025')

# ---------- Item 7: Finding 1 and Exhibit 10 ----------
rep('can go public more easily', 'can be named publicly more easily')
rep('JPMorgan Chase payments to BlackRock for Aladdin, US$ millions</p>', 'JPMorgan Chase payments to BlackRock for Aladdin, $ millions</p>')
rep('rotate(-90)">US $ millions</text>', 'rotate(-90)">$ millions</text>')

# ---------- Item 5: Exhibit 11 note ----------
rep('Source: UK Find a Tender<sup class="fnref"><a href="#s11">11</a>, <a href="#s50">50</a></sup>; USAspending.gov<sup class="fnref"><a href="#s51">51</a></sup>. Weights and outcomes are from an earlier draft of this research (October 2026) and its reading of the notices, not re-pulled; the 2023 PBGC record was re-read on October 19, 2026.</p>',
    'Source: UK Find a Tender<sup class="fnref"><a href="#s11">11</a>, <a href="#s50">50</a></sup>; USAspending.gov<sup class="fnref"><a href="#s51">51</a></sup>.</p>')

# ---------- Items 7 and 10: Finding 2 ----------
rep('2025 Investor Day</a>, BlackRock projected that API calls across BlackRock and Aladdin would grow 17 times by 2030, against four times for model portfolios, two times for portfolios and 1.3 times for trade allocations; the slide gave no starting number<sup class="fnref"><a href="#s2">2</a></sup>.',
    '2025 Investor Day</a>, on a slide about keeping the cost of growth low, BlackRock projected that API calls across BlackRock and Aladdin would grow 17x by 2030, against 4x for model portfolios, 2x for portfolios and 1.3x for trade allocations. The slide gave no starting number and does not say which products generate the API calls, so attributing them to Studio is my inference<sup class="fnref"><a href="#s2">2</a></sup>.')
rep('commitments, fundings, pay-downs and PIK', 'commitments, fundings, paydowns and PIK')

# ---------- Items 7 and 8: Finding 3 ----------
rep('Its engineers describe a plugin registry with <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“couple of thousands agents and tools”</a>, where',
    'Two of its engineers, Brennan Rosales, AI Engineering Lead, and Pedro Vicente Valdez, Principal AI Engineer, describe a plugin registry with <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“couple of thousands agents and tools,”</a> where')
rep('Seven providers a Studio buyer also talks to offer a connector or an MCP server',
    'Seven providers that a Studio buyer also deals with offer a connector or an MCP server')
rep('''<div class="gtm"><p><span class="lead">What it suggests about direction.</span> The choice is deliberate and consistent with the governance message: permission-dependent access, content filtering, no investment advice. The open question is timing and description, not access: when BlackRock describes how clients’ own AI tools will reach Aladdin, and in what words, while rivals set the terms of that comparison.</p></div>''',
    '''<div class="gtm"><p><span class="lead">What it suggests about direction.</span> I would describe the Copilot plugin model publicly now: Copilot’s tools are production Aladdin APIs, the same governed APIs Studio exposes, with inherited permissions and no-advice guardrails tested in the system prompt, and it never gives investment advice''' + sup(16, 13) + '''. Said in BlackRock’s own words, that is a stronger answer to the RFP connector question than an MCP server with a partial catalog, and it takes the terms of comparison back from FactSet and LSEG. I would hold any outside connector until the governance questions the inside model already answers, who can call what, with which permissions and under which guardrails, are solved for outside callers. Exhibit 15 is the evidence for that view.</p></div>''')

# ---------- Items 7 and 9: Finding 4 ----------
rep('<h2>4. Buyers say they want a core platform plus their own builds, and rivals are selling to that</h2>',
    '<h2>4. Buyers at BlackRock’s own webinar said they want a core platform plus their own builds, and rivals are selling to that</h2>')
rep('<p>BlackRock’s own Build vs. Buy webinar polled its attendees. In the first poll,',
    '<p>BlackRock’s own Build vs. Buy webinar polled its attendees; the attendee count was not given. In the first poll,')
rep('the Alpha FMC panellist said', 'the Alpha FMC panelist said')
rep('actively re-evaluating 18, mostly built in house 15.', 'actively reevaluating 18, mostly built in house 15.')
rep('y="48.5">Actively re-evaluating</text>', 'y="48.5">Actively reevaluating</text>')
rep('<p>BlackRock’s head of solutions engineering for the Americas answered on the same webinar.',
    '<p>Alisha Sewdass, BlackRock’s Head of Aladdin Solutions Engineering, Americas, answered on the same webinar.')
rep('''<div class="gtm"><p><span class="lead">What it suggests about direction.</span> Extensibility is now an RFP question, asked in those words, and Studio is BlackRock’s answer: the APIs, events and Data Cloud that Sewdass describes are the pieces in Exhibit 4. The buyer’s question and the product already match. The quick wins put the answer where the buyer is asking.</p></div>''',
    '''<div class="gtm"><p><span class="lead">What it suggests about direction.</span> Extensibility is now an RFP question, and Studio is BlackRock’s answer in direction: the APIs, events and Data Cloud that Sewdass describes are the pieces in Exhibit 4. The match is in direction, not yet in finish; the public catalog in Part 1 is mostly alpha and the SDK is beta. The quick wins put the answer where the buyer is asking.</p></div>''')

# ---------- Items 2, 6, 7, 8: Part 3 ----------
rep(' None opens the gate: documentation, sandboxes and credentials stay with the solutions team, after qualification. Product owns',
    ' Product owns')
rep('<td class="first">A named-proof programme, starting where the relationship is already public</td>',
    '<td class="first">A named-proof program, starting where the relationship is already public</td>')
rep('<td>Agree one measure with investor relations and product,', '<td>Agree on one measure with investor relations and product,')
rep('''<tr><td class="first">A decision on when and how to describe the Copilot plugin model publicly</td><td>Finding 3</td><td>A description, not access: how Copilot’s tools map to production APIs<sup class="fnref"><a href="#s16">16</a></sup>, what governance applies<sup class="fnref"><a href="#s13">13</a></sup>, and how clients will connect their own AI tools, timed with the Forward Deploy Engineer work<sup class="fnref"><a href="#s65">65</a></sup></td><td>Product with marketing; compliance review</td><td>A public description exists; prospects stop asking the question in rivals’ words</td></tr>''',
    '''<tr><td class="first">Publish a description of the Copilot plugin model</td><td>Finding 3</td><td>One page, in BlackRock’s words, with no new access: how Copilot’s tools map to production APIs<sup class="fnref"><a href="#s16">16</a></sup>, what governance applies<sup class="fnref"><a href="#s13">13</a></sup>, and how clients will connect their own AI tools, timed with the work described in the Forward Deploy Engineer posting<sup class="fnref"><a href="#s65">65</a></sup></td><td>Product with marketing; compliance review</td><td>The description exists, dated and public; prospects stop asking the question in deal reviews</td></tr>''')
rep('<p>Five questions need internal data that no public source holds. The answers would confirm or correct the findings before any of the wins is sized.</p>',
    '<p>Five questions need internal data that no public source holds. The answers would confirm or correct the findings before any of the wins is sized, and they are where any error in my reading would show first.</p>')
rep('<td>How soon the named-proof programme can start</td>', '<td>How soon the named-proof program can start</td>')
rep('''<p>On method: AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted; the author checked each claim against the document or recording it cites and takes responsibility for the reading. Public sources are limited, can be out of date and carry no internal product context, and machine transcription and synthesis are imperfect. The conclusions may be wrong for reasons the author cannot see, and the five questions above are where that would show first.</p>
''', '')

# ---------- Items 3, 5, 7: register ----------
rep('''<p class="front-note">Numbered in order of first citation and grouped by grade. P is a primary document; S is a BlackRock speaker on the record, with the name and title as the recording gives them; T is a third-party report. “Machine transcription” means a local transcription of the downloaded audio; “auto-captions” means YouTube’s captions. In both, names and jargon can be mis-heard, and only caption misspellings of proper names were corrected inside quotations. For recordings, the entry gives the minute and second at which each quoted passage begins.</p>''',
    '''<p class="front-note">Numbered in order of first citation and grouped by grade: P is a primary document, S a BlackRock speaker on the record with the name and title as the recording gives them, T a third-party report; for recordings, the entry gives the minute and second at which each quoted passage begins. “Machine transcription” means a local transcription of the downloaded audio and “auto-captions” means YouTube’s captions; in both, names and jargon can be misheard, and only caption misspellings of proper names were corrected inside quotations.</p>''')
rep('UK Find a Tender, 2025. Scoring weights and outcome as read in an earlier draft of this research (October 2026); not re-pulled. <a',
    'UK Find a Tender, 2025. <a')
rep('UK Find a Tender, 2023. Scoring weights and outcome as read in an earlier draft of this research (October 2026); not re-pulled. <a',
    'UK Find a Tender, 2023. <a')
rep('performance March 2023 to March 2027, re-read October 19, 2026. The 2017 award and the price comparison are as read in an earlier draft of this research. <a',
    'performance March 2023 to March 2027. <a')
rep('Full-text search of SEC EDGAR for “Aladdin Studio”</span>. SEC EDGAR, run October 2026.',
    'Full-text search of SEC EDGAR for “Aladdin Studio.”</span> SEC EDGAR, run October 2026.')

# ---------- Items 3 and 6: back page ----------
rep('''    <p>AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted the text. The author checked each claim against the document or recording it cites. Public material is limited, can be out of date and carries no internal product context; machine transcription and synthesis are imperfect; the conclusions may be wrong for reasons the author cannot see.</p>''',
    '''    <p>AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted the text. I checked each claim against the document or recording it cites.</p>''')
rep('''    <p>Three corrections were made against earlier drafts of this research: 58 API specifications became 54 once the SDK’s four utility APIs were set aside; a widely repeated “68 percent” survey figure was dropped because it could not be found in the report it is attributed to; and “more than 2,000 citizen developers” became 3,000, counted inside BlackRock rather than among clients.</p>
''', '')
rep('The quick wins and questions in Part 3 are the author’s proposals, based on Part 1 and the findings in Part 2.',
    'The quick wins and questions in Part 3 are my proposals, based on Part 1 and the findings in Part 2.')

assert 'the author' not in html.split('</head>')[1], [m.start() for m in re.finditer('the author', html)]
open(F, 'w', encoding='utf-8').write(html)
print('ok, delta chars', len(html) - len(orig))
