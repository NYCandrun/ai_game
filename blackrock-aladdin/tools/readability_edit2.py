#!/usr/bin/env python3
"""Pass 2: fit pages (trim where pass 1 lengthened text; findings run on). Edits the pass-1 output in place."""
import sys
B = "/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad"
P = B + "/gtm/out/Aladdin_Studio_With_AI.html"
html = open(P, encoding="utf-8").read()
head, body = html.split("</head>", 1)
n = 0
def R(old, new, count=1):
    global body, n
    c = body.count(old)
    if c != count:
        print("MISMATCH (%d found, %d expected):\n  %s" % (c, count, old[:200])); sys.exit(1)
    body = body.replace(old, new); n += 1

# ---- page 2
R('Six likely initial directions, set out in Part 3, close both gaps, and none of them changes how Aladdin is sold.</p>',
  'Part 3 sets out six directions that close both gaps without changing how Aladdin is sold.</p>')
R('per its proxy statement, almost six times what it paid in 2017</p>',
  'per its proxy statement, almost six times its 2017 payments</p>')
R('<p class="stats-src" style="margin-bottom:12pt">Sources, left to right: <a href="https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf">BlackRock 2025 Investor Day</a><sup class="fnref"><a href="#s1">1</a></sup>, slide on keeping the cost of growth low. The slide projects API calls 17x, model portfolios 4x, portfolios 2x and trade allocations 1.3x. It does not say which products generate the API calls; attributing them to Studio is my inference.',
  '<p class="stats-src" style="margin-bottom:8pt">Sources, left to right: <a href="https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf">BlackRock 2025 Investor Day</a><sup class="fnref"><a href="#s1">1</a></sup>, slide on keeping the cost of growth low: API calls 17x, model portfolios 4x, portfolios 2x, trade allocations 1.3x. The slide does not say which products generate the API calls; attributing them to Studio is my inference.')
R('The other half of the growth story is the whole portfolio, public markets and private. The new private-markets data arrives through Data Cloud and Explore, which are Studio’s surfaces<sup class="fnref"><a href="#s6">6</a></sup>. Aladdin Copilot, BlackRock’s AI assistant, works only inside the Aladdin login. Data providers have gone the other way: they sell connectors that let outside AI tools pull their data<sup class="fnref"><a href="#s7">7</a></sup>. At BlackRock’s own webinar, buyers said they want a core platform plus tools they build themselves, and rival platforms are already selling to that demand<sup class="fnref"><a href="#s8">8</a></sup>.</p>',
  'The other half of the growth story is the whole portfolio, public markets and private; the new private-markets data arrives through Data Cloud and Explore, which are Studio’s surfaces<sup class="fnref"><a href="#s6">6</a></sup>. Aladdin Copilot, BlackRock’s AI assistant, works only inside the Aladdin login, while data providers sell connectors that let outside AI tools pull their data<sup class="fnref"><a href="#s7">7</a></sup>. At BlackRock’s own webinar, buyers said they want a core platform plus tools they build themselves, and rival platforms already sell to that demand<sup class="fnref"><a href="#s8">8</a></sup>.</p>')
R('<div class="method" style="margin-top:4pt; margin-bottom:6pt">', '<div class="method" style="margin-top:2pt; margin-bottom:4pt">')
R('<p><b>Public material only.</b> The sources are BlackRock web pages, the 54 API specifications inside 11 public <code>asdk_plugin</code> Python packages, 128 recordings, SEC filings, procurement notices, GitHub and PyPI. AI agents pulled them in about a day; I checked every fact against its document. Some recordings are machine-transcribed, so names and jargon can be misheard; the Sources section marks which quotes come from machine transcripts. Figures may be out of date. I have no internal product context, so some conclusions may be wrong for reasons I cannot see.</p>',
  '<p><b>Public material only.</b> BlackRock web pages, the 54 API specifications inside 11 public <code>asdk_plugin</code> Python packages, 128 recordings, SEC filings, procurement notices, GitHub and PyPI. AI agents pulled them in about a day; I checked every fact against its document. Some recordings are machine-transcribed, so names and jargon can be misheard; the Sources section marks which. Figures may be out of date, and I have no internal product context, so some conclusions may be wrong for reasons I cannot see.</p>')
R('<p>Underlined text links to the document behind the fact. Each superscript number points to an entry in the Sources section at the end of this document. The entry gives the source’s grade (P, S or T, below), its title, speaker and date. For recordings, it also gives the minute and second at which each quoted passage begins.</p>',
  '<p>Underlined text links to the document behind the fact. Each superscript number points to an entry in Sources, at the end of this document, giving the grade (P, S or T), title, speaker and date. For recordings it also gives the minute and second where each quoted passage begins.</p>')
R('<b>P</b> Primary document: an SEC filing, an API specification, a BlackRock web page, a procurement notice, or code on GitHub or PyPI</span>',
  '<b>P</b> Primary document: a filing, a specification, a BlackRock page, a procurement notice, or code on GitHub or PyPI</span>')
R('<b>T</b> Third-party report: trade press, or a summary written by someone other than BlackRock</span>',
  '<b>T</b> Third-party report: trade press, or a summary by someone other than BlackRock</span>')

# ---- page 3 (Part 1 opening)
R('Aladdin is sold the way enterprise platforms are sold. The conversation comes first. Documentation, a sandbox and credentials come from the solutions team once a prospect is qualified. Part 1 covers what a prospect can see before that conversation.</p>',
  'Aladdin is sold the way enterprise platforms are sold: the conversation comes first, and documentation, a sandbox and credentials come from the solutions team once a prospect is qualified. Part 1 covers what a prospect can see before that conversation.</p>')
R('<span class="ex-num">Exhibit 1.</span> BlackRock sells one engine through eight named products, and Studio is the entry point for people who write code</p>\n<table>\n<colgroup><col style="width:92pt"><col><col style="width:132pt"></colgroup>',
  '<span class="ex-num">Exhibit 1.</span> One engine, eight named products; Studio is the entry point for people who write code</p>\n<table>\n<colgroup><col style="width:84pt"><col><col style="width:108pt"></colgroup>')
R('Alpha, beta, stable and sunset are the maturity labels each specification carries, from alpha, the earliest, to stable.',
  'Alpha, beta, stable and sunset are the maturity labels in the specifications, alpha being the earliest.')

# ---- page 5 (Exhibits 3 and 4)
R('<span class="ex-num">Exhibit 3.</span> Studio is the layer between the people who build on Aladdin and the one record of holdings underneath, with Copilot above it and governance across every layer</p>',
  '<span class="ex-num">Exhibit 3.</span> Studio sits between the people who build and the one record of holdings, with Copilot above it</p>')
R('<span class="ex-num">Exhibit 4.</span> Studio has eight pieces, and the catalog, guides, notebooks and samples all sit behind a client login</p>',
  '<span class="ex-num">Exhibit 4.</span> Studio has eight pieces; the catalog, guides, notebooks and samples sit behind a client login</p>')
R('security creation and Aladdin Data Cloud datasets<sup class="fnref"><a href="#s17">17</a></sup>.',
  'security creation and Data Cloud datasets<sup class="fnref"><a href="#s17">17</a></sup>.')
R('are generated from the specifications by a tool BlackRock publishes called the <a href="https://github.com/blackrock/aladdinsdk-plugin-builder">plugin builder</a>',
  'are generated from the specifications by BlackRock’s <a href="https://github.com/blackrock/aladdinsdk-plugin-builder">plugin builder</a> tool')
R('<td>A domain of five APIs, all still labelled alpha. They cover research notes, engagements, analyst coverage, watchlists and screening criteria<sup class="fnref"><a href="#s17">17</a></sup>.</td>',
  '<td>A domain of five APIs, all still labelled alpha, covering research notes, engagements, analyst coverage, watchlists and screening criteria<sup class="fnref"><a href="#s17">17</a></sup>.</td>')
R('lists it as a Studio resource, alongside Aladdin Data eXchange for bulk delivery, and gives little detail on either',
  'lists it as a Studio resource, with Aladdin Data eXchange for bulk delivery, and gives little detail on either')

# ---- Finding 1
R('credits <a href="https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management">the Snowflake implementation</a> done as part of its Aladdin programme<sup class="fnref"><a href="#s44">44</a></sup>. JPMorgan Chase’s <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A">proxy statements</a> report payments for Aladdin of $4.4 million to $7.6 million a year from 2017 to 2023. The figure then jumped to $14.7 million in 2024 and',
  'credits <a href="https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management">the Snowflake implementation</a> in its Aladdin programme<sup class="fnref"><a href="#s44">44</a></sup>. JPMorgan Chase’s <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A">proxy statements</a> report payments for Aladdin of $4.4 million to $7.6 million a year from 2017 to 2023, then $14.7 million in 2024 and')
R('<span class="ex-num">Exhibit 10.</span> JPMorgan Chase paid BlackRock under $8 million a year for Aladdin from 2017 to 2023, then $14.7 million in 2024 and $25.6 million in 2025</p>',
  '<span class="ex-num">Exhibit 10.</span> JPMorgan Chase paid under $8 million a year for Aladdin until 2023, then $25.6 million in 2025</p>')
R('The grey 2016 bar is a payment for integration services, not a payment for Aladdin, and is excluded from the figures in the text. The payments may cover more than a client license. JPMorgan is also a custodian, and',
  'The grey 2016 bar is for integration services, not Aladdin, and is left out of the text. The payments may cover more than a client license: JPMorgan is also a custodian, and')
R('Public buyers add a third kind of record. Their procurement notices show how each bid for Aladdin was scored.</p>',
  'Public buyers add a third kind of record: procurement notices that show how each bid for Aladdin was scored.</p>')
R('<span class="ex-num">Exhibit 11.</span> Three public pension bodies scored Aladdin bids in open competitions between 2017 and 2025, and Aladdin won every one</p>\n<table>\n<colgroup><col style="width:150pt"><col style="width:60pt"><col><col style="width:160pt"></colgroup>',
  '<span class="ex-num">Exhibit 11.</span> Three public pension bodies scored Aladdin bids between 2017 and 2025, and Aladdin won every one</p>\n<table>\n<colgroup><col style="width:126pt"><col style="width:44pt"><col><col style="width:150pt"></colgroup>')
R('<p>None of this proof names Studio. That matters less than it seems. Studio is sold for building custom applications on Aladdin, so a buyer wants to know that another institution built on the platform and stayed. For custom applications, proof from one firm counts even when the buyer is a different kind of firm. Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public. They are the natural first candidates for a named Studio story.</p>',
  '<p>None of this proof names Studio, and that matters less than it seems. Studio is sold for building custom applications on Aladdin, so a buyer wants to know that another institution built on the platform and stayed. For custom applications, proof from one firm counts even when the buyer is a different kind of firm. Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public, so they are the natural first candidates for a named Studio story.</p>')

# ---- findings 2 to 4 run on instead of each forcing a new page
R('<section class="chapter finding" id="f2">', '<section class="chapter finding runon" id="f2">')
R('<section class="chapter finding" id="f3">', '<section class="chapter finding runon" id="f3">')
R('<section class="chapter finding" id="f4">', '<section class="chapter finding runon" id="f4">')

# ---- Finding 3
R(' Exhibit 14 lists the data vendors, which are one comparison a Studio buyer makes, and the system-of-record rivals, which are the other.</p>',
  ' Exhibit 14 lists both comparisons a Studio buyer makes: the data vendors and the system-of-record rivals.</p>')
R('<span class="ex-num">Exhibit 14.</span> Six data and cloud providers have shipped AI connectors to their data and two system-of-record rivals have announced AI agents; Aladdin has no public equivalent, only a job advert that mentions MCP</p>',
  '<span class="ex-num">Exhibit 14.</span> Data vendors have shipped AI connectors and two system-of-record rivals have announced AI agents; Aladdin has only a job advert that mentions MCP</p>')
R('Of the system-of-record rivals, SimCorp and Arcesium are the only ones with an AI announcement in my sources; State Street Alpha, Charles River and Bloomberg are not listed because my sources hold no such announcement for them.</p>',
  'Of the system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources; State Street Alpha, Charles River and Bloomberg are not listed because my sources hold none for them.</p>')
R('<span class="ex-num">Exhibit 15.</span> Keeping the AI front door inside the login gives BlackRock governance and trust; opening it outside gives discoverability on rivals’ terms, with more to secure and more to explain to regulators</p>',
  '<span class="ex-num">Exhibit 15.</span> Inside the login buys governance and trust; outside the login buys discoverability on rivals’ terms, with more to secure and to explain to regulators</p>')
R('I would describe the Copilot plugin model publicly, now. The description is short. Copilot’s tools are production Aladdin APIs,',
  'I would describe the Copilot plugin model publicly, now. Copilot’s tools are production Aladdin APIs,')
R('Exhibit 15 is the evidence for that view, and this is the fifth direction in Part 3.</p>',
  'Exhibit 15 is the evidence for that view; this is the fifth direction in Part 3.</p>')

# ---- Finding 4
R('<p>BlackRock ran a Build vs. Buy webinar for asset managers and polled the attendees. The replay does not say how many attended. The first poll asked where firms sit today.',
  '<p>BlackRock ran a Build vs. Buy webinar for asset managers and polled the attendees. The first poll asked where firms sit today.')
R('The shift of the last two years, she said, is “to more of a modular approach',
  'The shift of the last two years is “to more of a modular approach')
R('On AI, she said, “you need that system of record that underpins anything that AI is built upon.” She added that “the other layer that is almost equally important is a really defined system of work”',
  'On AI, she said, “you need that system of record that underpins anything that AI is built upon,” and “the other layer that is almost equally important is a really defined system of work”')
R('Rivals are selling to the same buyer, the one who wants a core platform and their own builds on it. SimCorp announced a win at <a href="https://alliancebernsteinholdinglp.gcs-web.com/news-releases/news-release-details/alliancebernstein-selects-simcorp-one-technology-platform">AllianceBernstein</a> in February 2026 and another at',
  'Rivals are selling to the same buyer, the one who wants a core platform plus their own builds. SimCorp announced wins at <a href="https://alliancebernsteinholdinglp.gcs-web.com/news-releases/news-release-details/alliancebernstein-selects-simcorp-one-technology-platform">AllianceBernstein</a> in February 2026 and')
R('BlackRock itself says so. Its <a href="https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework">August 2026 insight</a> piece says',
  'BlackRock itself says so: its <a href="https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework">August 2026 insight</a> piece says')
R('It is not yet a finished answer. The public catalog in Part 1 is mostly alpha, and the SDK is beta. The directions in Part 3 put Studio into the RFP, where the buyer is asking the question.</p>',
  'It is not yet a finished answer: the public catalog in Part 1 is mostly alpha, and the SDK is beta. The directions in Part 3 put Studio into the RFP, where the buyer is asking.</p>')

open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("pass 2 applied", n, "edits")
