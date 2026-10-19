#!/usr/bin/env python3
"""Pass 3: meaning-check fixes (MEANING_CHECK_proposed.md) + further fitting."""
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

# ===== meaning fixes, report 01
R('<a href="#f1">Four findings on where BlackRock is heading and what buyers want</a>',
  '<a href="#f1">Four findings on where BlackRock is heading and what the market is doing</a>')
R('the new private-markets data arrives through Data Cloud and Explore, which are Studio’s surfaces<sup class="fnref"><a href="#s6">6</a></sup>. Aladdin Copilot, BlackRock’s AI assistant, works only inside the Aladdin login, while data providers sell connectors that let outside AI tools pull their data',
  'the new private-markets data arrives through Data Cloud and Explore<sup class="fnref"><a href="#s6">6</a></sup>. Aladdin Copilot, BlackRock’s AI assistant, works only inside the Aladdin login, while data providers offer connectors that let outside AI tools pull their data')
R('<li style="margin-bottom:0">Publish a description of how Copilot’s plugins map to Aladdin’s APIs.</li>',
  '<li style="margin-bottom:0">Publish a description of the Copilot plugin model: API mapping, governance, and how clients connect their own AI tools.</li>')
R('<li style="margin-bottom:0">Publish a prospect-facing “what is in the box” summary of the public API catalog.</li>',
  '<li style="margin-bottom:0">Write a prospect-facing “what is in the box” summary of the public API catalog.</li>')
R('the Sources section marks which. Figures may be out of date',
  'the Sources section marks which recordings. Figures may be out of date')
R('<b>P</b> Primary document: a filing, a specification, a BlackRock page, a procurement notice, or code on GitHub or PyPI</span>',
  '<b>P</b> Primary document: a filing, a specification, a web page or press release, a procurement notice, or code on GitHub or PyPI</span>')
R('<b>T</b> Third-party report: trade press, or a summary by someone other than BlackRock</span>',
  '<b>T</b> Third-party report: trade press, or a third party’s summary of a primary source</span>')
# page 2 fit
R('The public proof that clients use Aladdin never names Studio either. Part 3 sets out six directions that close both gaps without changing how Aladdin is sold.</p>',
  'Public proof that clients use Aladdin never names Studio either. Part 3 sets out six directions to close both gaps without changing how Aladdin is sold.</p>')
R('per its proxy statement, almost six times its 2017 payments</p>', 'per its proxy statement, almost 6x its 2017 level</p>')
R('At BlackRock’s own webinar, buyers said they want a core platform plus tools they build themselves, and rival platforms already sell to that demand',
  'Buyers at BlackRock’s own webinar want a core platform plus tools they build themselves, and rivals already sell to that demand')

# ===== report 02
R('The Aladdin organization is “around 7,000 people, with over 4,000 of those being engineers.”',
  'The organization is “around 7,000 people, with over 4,000 of those being engineers.”')
R('up 24 percent in the year it bought Preqin', 'up 24 percent with Preqin')
R('Aladdin is sold the way enterprise platforms are sold: the conversation comes first, and documentation, a sandbox and credentials come from the solutions team once a prospect is qualified. Part 1 covers what a prospect can see before that conversation.</p>',
  'Aladdin is sold the way enterprise platforms are sold: the conversation comes first, and documentation, a sandbox and credentials come from the solutions team once a prospect is qualified. Part 1 covers what a prospect can see before that conversation.</p>')
R('<span class="ex-num">Exhibit 2.</span> The public APIs cover a trade from order to NAV, but they name no order screen and hold no position or event API</p>',
  '<span class="ex-num">Exhibit 2.</span> The public APIs trace a trade from order to NAV, but they name no order screen and hold no position or event API</p>')
R('<figure class="exhibit keep" id="exhibit-2">', '<figure class="exhibit" id="exhibit-2">')
R('Alpha, beta, stable and sunset are the maturity labels in the specifications, alpha being the earliest. The specifications hold no position or event API, and they do not say in what sequence steps 4 to 6 happen; the sequence shown is mine.</p>',
  'Alpha, beta, stable and sunset are the stability labels each specification carries (its <code>x-aladdin-api-stability</code> field), alpha being the earliest. The specifications hold no position or event API, and they do not say in what sequence steps 4 to 6 happen.</p>')
R('<td>A domain of five APIs, all still labelled alpha, covering research notes,', '<td>A domain of five APIs, all labelled alpha, covering research notes,')
R('with Aladdin Data eXchange for bulk delivery, and gives little detail on either', 'with Aladdin Data eXchange for bulk delivery, and gives little detail on the add-in')
R('Risk exceptions and Data Cloud datasets carry bitemporal fields, which record both when something was true and when the system learned it. Rule assignments and dataset releases name a four-eyes approval, a second sign-off before a change takes effect<sup class="fnref"><a href="#s17">17</a></sup>.',
  'Risk exceptions and Data Cloud datasets carry bitemporal fields, which record two time dimensions. Rule assignments and dataset releases name a four-eyes approval, a second sign-off<sup class="fnref"><a href="#s17">17</a></sup>.')
R(' Each of these is a feature of a controlled production system for an existing client, not of a product a stranger can try.</p>', '</p>')
R('conflict with the official toolkit for MCP</a>, the Model Context Protocol, the standard that lets outside AI tools call a vendor’s APIs.',
  'conflict with the official toolkit for MCP</a>, the Model Context Protocol, the common standard AI assistants use to pull data from other systems.')
R('Run modes, credential storage and API-gateway settings are the needs of a client’s engineering team, not of a prospect.</p>',
  'Run modes, credential storage and API-gateway settings are the needs of a client’s engineering team.</p>')
R('<th class="ctr">Developer call to action</th>', '<th class="ctr">Call to action</th>')
R('The message is the same across speakers and years, so BlackRock already has a positioning for Studio. What it lacks is reach. Learning about Studio from outside takes effort.',
  'The message is consistent across speakers and years, so BlackRock already has a positioning for Studio. Learning about it from outside takes effort.')
R('<span class="ex-num">Exhibit 8.</span> Five BlackRock executives have defined Studio on the record since early 2024, and the head of Studio engineering gave the fullest definition in November 2025</p>',
  '<span class="ex-num">Exhibit 8.</span> Five BlackRock executives have defined Studio on the record, and the head of Studio engineering gave the three-part definition in November 2025</p>')
R('<td>The three-part definition quoted in Part 1; 3,000 internal citizen developers</td>',
  '<td>The three-part definition quoted in Part 1; 3,000 internal citizen developers (a figure Goel also gives)</td>')
R('Quoted at 25:22, 28:52, 29:28, 29:37; the 3,000 figure is given at 35:23.</p>',
  'Quoted at 25:22, 28:52, 29:28, 29:37. Goel also gives the 3,000 citizen-developer figure, at 35:23; Exhibit 8 credits it to Woodhead, who gives it at 9:39 in entry 5.</p>')

# ===== report 03
R('<h2>1. Public proof that clients use Aladdin already exists, and it works as Studio proof even though none of it names Studio</h2>',
  '<h2>1. Public proof that clients use Aladdin already exists, and it can serve as Studio proof even though none of it names Studio</h2>')
R('Royal London’s chief executive credits <a href="https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management">the Snowflake implementation</a> in its Aladdin programme<sup class="fnref"><a href="#s44">44</a></sup>. JPMorgan Chase’s <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A">proxy statements</a> report payments for Aladdin of',
  'Royal London’s chief executive credits Aladdin’s <a href="https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management">Snowflake implementation</a><sup class="fnref"><a href="#s44">44</a></sup>. JPMorgan Chase’s <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A">proxy statements</a> report Aladdin payments of')
R('The grey 2016 bar is for integration services, not Aladdin, and is left out of the text. The payments may cover more than a client license: JPMorgan is also a custodian, and',
  'The grey 2016 bar is a payment for integration services; the figures in the text start with 2017. The payments may cover more than a client license: JPMorgan is also a custodian, and')
R('<span class="ex-num">Exhibit 10.</span> JPMorgan Chase paid under $8 million a year for Aladdin until 2023, then $25.6 million in 2025</p>',
  '<span class="ex-num">Exhibit 10.</span> JPMorgan paid under $8 million a year for Aladdin until 2023, then $25.6 million in 2025</p>')
R('procurement notices that show how each bid for Aladdin was scored.</p>', 'procurement notices that show how the bids for Aladdin were scored.</p>')
R('<span class="ex-num">Exhibit 11.</span> Three public pension bodies scored Aladdin bids between 2017 and 2025, and Aladdin won every one</p>',
  '<span class="ex-num">Exhibit 11.</span> Three public pension bodies scored Aladdin bids, 2017 to 2025, and Aladdin won each time</p>')
R('<p>None of this proof names Studio, and that matters less than it seems. Studio is sold for building custom applications on Aladdin, so a buyer wants to know that another institution built on the platform and stayed. For custom applications, proof from one firm counts even when the buyer is a different kind of firm. Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public, so they are the natural first candidates for a named Studio story.</p>',
  '<p>None of this proof names Studio, which matters less than it seems. Studio is sold for building custom applications on Aladdin, so a buyer wants to know that another institution built on the platform and stayed; proof from one firm counts even when the buyer is a different kind of firm. Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public, so they are the natural first candidates for a named Studio story.</p>')
R('an asset manager’s 10-K and three public pension buyers’ procurement notices all record Aladdin.',
  'an asset manager’s 10-K and three public pension buyers’ notices all record Aladdin.')

# ===== report 04
R('So the measure BlackRock is growing fastest is not one it says it charges for.</p>',
  'So the measure BlackRock projects to grow fastest is not one it says it charges for.</p>')
R('<a href="#s55">55</a></sup>, both times described as an add-on sold with Aladdin Enterprise</td>',
  '<a href="#s55">55</a></sup>, described as an add-on sold with Aladdin Enterprise</td>')
R('arrives through Data Cloud and Explore, and both of those are part of Studio. So Studio carries the growth story',
  'arrives through Data Cloud and Explore, the surfaces Studio provides. So Studio carries the growth story')

# ===== report 05
R('The data layer is being shaped the same way: BlackRock’s AI product head says', 'On the data side, BlackRock’s AI product head says')
R('<b>Plan and call the API</b>: an orchestrator, the component that decides which tool to call, loops <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a> using GPT-4’s function calling; a final check, the output guardrails, screens the answer for hallucinations',
  '<b>Plan and call the API</b>: the orchestrator (the component that runs the loop) iterates <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a> with GPT-4 function calling; output guardrails then check for hallucinations')
R('The one public hint is a job advert:', 'One public hint is a job advert:')
R('<td>One place to govern access; each user keeps their Aladdin permissions (“permission-dependent access”); guardrails against giving advice, tested in the system prompt; the trust of an enterprise login; a rollout BlackRock controls, one engineering team at a time',
  '<td>Governance in one place; each user keeps their Aladdin permissions (“permission-dependent access”); guardrails against giving advice, tested in the system prompt; enterprise trust; a rollout BlackRock controls, one engineering team at a time')
R('<td>More to secure and more to support; buyers would read a partial catalog as the whole catalog; and a platform that will not give advice<sup class="fnref"><a href="#s16">16</a></sup> would have to explain to regulators what outside AI tools do with its data</td>',
  '<td>More to secure and more to support; buyers would read a partial catalog as the whole catalog; and the regulatory optics of outside AI tools drawing on a platform that will not give advice<sup class="fnref"><a href="#s16">16</a></sup></td>')
R('<span class="ex-num">Exhibit 13.</span> Every Copilot answer is a call to a production Aladdin API: thousands of registered tools are filtered to 20 or 30, the call is planned and checked, and advice is refused</p>',
  '<span class="ex-num">Exhibit 13.</span> Copilot answers a question by choosing from thousands of registered tools and calling production Aladdin APIs, never giving investment advice</p>')
R('<span class="ex-num">Exhibit 14.</span> Data vendors have shipped AI connectors and two system-of-record rivals have announced AI agents; Aladdin has only a job advert that mentions MCP</p>',
  '<span class="ex-num">Exhibit 14.</span> Data vendors have shipped or announced AI access to their data and two system-of-record rivals have announced AI features; Aladdin has only a job advert that mentions MCP</p>')
R('<span class="ex-num">Exhibit 15.</span> Inside the login buys governance and trust; outside the login buys discoverability on rivals’ terms, with more to secure and to explain to regulators</p>',
  '<span class="ex-num">Exhibit 15.</span> Inside the login buys governance; outside the login buys discoverability on rivals’ terms</p>')

# ===== report 06
R('Source: poll results as the host read them out on the <a href="https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions">Build vs. Buy webinar replay</a>, taken from the published captions',
  'Source: poll results as read out on the <a href="https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions">Build vs. Buy webinar replay</a>, taken from the published captions')
R('On top of that data sit “very, very robust APIs that manage the end to end life cycle of a transaction,” so that clients',
  'That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction,” so that clients')
R('BlackRock itself says so: its <a href="https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework">August 2026 insight</a> piece says',
  'BlackRock’s own marketing agrees: its <a href="https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework">August 2026 insight</a> piece says')
R('<td>Number of named references the sales team can use; number of deals in which one was cited</td>',
  '<td>Number of named references in use by sales; number of deals in which one was cited</td>')
R('which API domains exist, how many specifications each has and at what status,', 'which API domains exist, how many specifications and operations each has and at what status,')
R('prospects stop asking in deal reviews how Copilot connects</td>', 'prospects stop asking about connectors in deal reviews</td>')
R('<td>Where marketing spends first: content for awareness, sales enablement for the first call, or client success for production builds</td>',
  '<td>Where marketing spends first: content, sales enablement or client success</td>')

# ===== layout: findings 2 and 3 on fresh pages, finding 4 runs on after finding 3
R('<section class="chapter finding runon" id="f2">', '<section class="chapter finding" id="f2">')
R('<section class="chapter finding runon" id="f3">', '<section class="chapter finding" id="f3">')

open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("pass 3 applied", n, "edits")
