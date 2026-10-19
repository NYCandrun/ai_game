#!/usr/bin/env python3
"""Pass 5: fill page-bottom gaps (split two long paragraphs, let Exhibit 5 split) and fit the executive summary."""
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

# ---- executive summary: paragraph 1 to three lines, slightly tighter paragraph margins
R('<p>Studio is Aladdin’s developer and data layer, with three parts: APIs and events, a Python SDK, and Aladdin Data Cloud on Snowflake. Five BlackRock speakers have defined it on the record since 2024<sup class="fnref"><a href="#s5">5</a></sup>. Public documents prove named clients use Aladdin, though none names Studio: JPMorgan Chase’s proxy statements, Janus Henderson’s code commits and 10-K, Royal London’s chief executive on BlackRock’s video, and three pension bodies’ tender notices.</p>',
  '<p style="margin-bottom:8pt">Studio is Aladdin’s developer and data layer, with three parts: APIs and events, a Python SDK and Aladdin Data Cloud on Snowflake. Five BlackRock speakers have defined it on the record since 2024<sup class="fnref"><a href="#s5">5</a></sup>. Public documents prove named clients use Aladdin (none names Studio): JPMorgan Chase’s proxy statements, Janus Henderson’s commits and 10-K, Royal London’s chief executive on video, and three pension tenders.</p>')
R('<p>API calls are the fastest-growing measure BlackRock showed investors: 17x by 2030.',
  '<p style="margin-bottom:8pt">API calls are the fastest-growing measure BlackRock showed investors: 17x by 2030.')

# ---- Exhibit 5 may split across pages (thead repeats; last two rows stay together)
R('<figure class="exhibit keep" id="exhibit-5">', '<figure class="exhibit" id="exhibit-5">')

# ---- Finding 3: split the connector paragraph; tighten two funnel boxes
R('according to a secondary summary of its results slides<sup class="fnref"><a href="#s62">62</a>, <a href="#s63">63</a></sup>. I found no public connector for Aladdin',
  'according to a secondary summary of its results slides<sup class="fnref"><a href="#s62">62</a>, <a href="#s63">63</a></sup>.</p>\n<p>I found no public connector for Aladdin')
R('leaving <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“say, 20 to 30 tools and agents,”</a> because giving the model more than “40, 50 tools” would hurt performance',
  'leaving <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“say, 20 to 30 tools and agents,”</a> because more than “40, 50 tools” would hurt performance')
R('with GPT-4 function calling; output guardrails then check for hallucinations', 'with GPT-4 function calling, then output guardrails check for hallucinations')

# ---- Finding 4: split the Sewdass paragraph before the rivals
R('is a really defined system of work”<sup class="fnref"><a href="#s8">8</a></sup>. Rivals are selling to the same buyer,',
  'is a really defined system of work”<sup class="fnref"><a href="#s8">8</a></sup>.</p>\n<p>Rivals are selling to the same buyer,')

open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("pass 5 applied", n, "edits")

# ---- length is no longer a constraint: restore the fuller finding-style titles shortened only for space
html = open(P, encoding="utf-8").read(); head, body = html.split("</head>", 1)
R('<span class="ex-num">Exhibit 1.</span> One engine, eight named products; Studio is the entry point for people who write code</p>',
  '<span class="ex-num">Exhibit 1.</span> BlackRock sells one engine through eight named products, and Studio is the entry point for people who write code</p>')
R('<span class="ex-num">Exhibit 3.</span> Studio sits between the people who build and the one record of holdings, with Copilot above it</p>',
  '<span class="ex-num">Exhibit 3.</span> Studio is the layer between the people who build on Aladdin and the one record of holdings underneath, with Copilot above it and governance across every layer</p>')
R('<span class="ex-num">Exhibit 4.</span> Studio has eight pieces; the catalog, guides, notebooks and samples sit behind a client login</p>',
  '<span class="ex-num">Exhibit 4.</span> Studio has eight pieces, and the catalog, guides, notebooks and samples all sit behind a client login</p>')
R('<span class="ex-num">Exhibit 5.</span> Operations and analytics hold 127 of the 301 public operations; only 23 of 54 specifications are stable</p>',
  '<span class="ex-num">Exhibit 5.</span> Investment operations and analytics hold 127 of the 301 public operations, and only 23 of the 54 specifications are stable</p>')
R('<span class="ex-num">Exhibit 10.</span> JPMorgan paid under $8 million a year for Aladdin until 2023, then $25.6 million in 2025</p>',
  '<span class="ex-num">Exhibit 10.</span> JPMorgan Chase paid BlackRock under $8 million a year for Aladdin from 2017 to 2023, then $14.7 million in 2024 and $25.6 million in 2025</p>')
R('<span class="ex-num">Exhibit 11.</span> Three public pension bodies scored Aladdin bids, 2017 to 2025, and Aladdin won each time</p>',
  '<span class="ex-num">Exhibit 11.</span> Three public pension bodies scored Aladdin bids between 2017 and 2025, and Aladdin won every one</p>')
open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("titles restored; total", n)
