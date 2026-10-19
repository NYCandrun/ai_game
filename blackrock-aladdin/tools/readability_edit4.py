#!/usr/bin/env python3
"""Pass 4: page fitting (exec summary, Exhibits 4/5, Finding 1) and flow (Part 2 findings and Part 3 run on)."""
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

# ---- executive summary
R('Public proof that clients use Aladdin never names Studio either. Part 3 sets out six directions to close both gaps without changing how Aladdin is sold.</p>',
  'Public proof that clients use Aladdin never names Studio either. Part 3 sets out six directions to close both gaps.</p>')
R('<p>Studio is Aladdin’s developer and data layer. It has three parts: APIs and events, a Python SDK, and Aladdin Data Cloud, a managed data service on Snowflake. Five BlackRock speakers have defined it on the record since 2024<sup class="fnref"><a href="#s5">5</a></sup>. Public documents prove that named clients use Aladdin, though not Studio by name: JPMorgan Chase’s proxy statements, Janus Henderson’s code commits and 10-K, Royal London’s chief executive on BlackRock’s client video, and three public pension bodies’ tender notices.</p>',
  '<p>Studio is Aladdin’s developer and data layer, with three parts: APIs and events, a Python SDK, and Aladdin Data Cloud on Snowflake. Five BlackRock speakers have defined it on the record since 2024<sup class="fnref"><a href="#s5">5</a></sup>. Public documents prove named clients use Aladdin, though none names Studio: JPMorgan Chase’s proxy statements, Janus Henderson’s code commits and 10-K, Royal London’s chief executive on BlackRock’s video, and three pension bodies’ tender notices.</p>')
R('<p style="margin-bottom:4pt">Six likely initial directions, in the order I would take them:</p>',
  '<p style="margin-bottom:4pt">Six likely initial directions, in the order I would take them; none changes how Aladdin is sold:</p>')
R('<li style="margin-bottom:0">Publish a description of the Copilot plugin model: API mapping, governance, and how clients connect their own AI tools.</li>',
  '<li style="margin-bottom:0">Describe the Copilot plugin model publicly: API mapping, governance, client AI-tool connections.</li>')

# ---- Exhibit 4 trims
R('Woodhead names “APIs events” as one of the three parts<sup class="fnref"><a href="#s5">5</a></sup>;',
  'Woodhead names “APIs events” as one part<sup class="fnref"><a href="#s5">5</a></sup>;')
R('Eleven add-on packages, one per API domain (Exhibit 5), are generated from the specifications by BlackRock’s <a href="https://github.com/blackrock/aladdinsdk-plugin-builder">plugin builder</a> tool',
  'Eleven add-on packages, one per API domain, are generated from the specifications by BlackRock’s <a href="https://github.com/blackrock/aladdinsdk-plugin-builder">plugin builder</a>')
R('<td>A domain of five APIs, all labelled alpha, covering research notes, engagements, analyst coverage, watchlists and screening criteria',
  '<td>A domain of five APIs, all alpha: research notes, engagements, analyst coverage, watchlists and screening criteria')
# ---- Exhibit 5 trims
R('<span class="ex-num">Exhibit 5.</span> Investment operations and analytics hold 127 of the 301 public operations, and only 23 of the 54 specifications are stable</p>\n<table>\n<colgroup><col style="width:92pt"><col style="width:34pt"><col style="width:96pt"><col style="width:30pt"><col style="width:30pt"><col style="width:32pt"><col style="width:34pt"><col></colgroup>',
  '<span class="ex-num">Exhibit 5.</span> Operations and analytics hold 127 of the 301 public operations; only 23 of 54 specifications are stable</p>\n<table>\n<colgroup><col style="width:80pt"><col style="width:32pt"><col style="width:84pt"><col style="width:28pt"><col style="width:28pt"><col style="width:30pt"><col style="width:32pt"><col></colgroup>')
R('Counts are mine, recomputed from the files. The core <code>aladdinsdk</code> package adds four utility APIs (token, subscription, notification and a demo), which are not counted here.</p>',
  'Counts are mine, recomputed from the files. The core <code>aladdinsdk</code> package adds four utility APIs (token, subscription, notification and a demo), not counted here.</p>')

# ---- Finding 1 trims
R('On BlackRock’s client video, Royal London’s chief executive credits', 'On BlackRock’s video, Royal London’s chief executive credits')
R('to serve custody clients on the platform<sup class="fnref"><a href="#s45">45</a></sup>. That 2016 report is trade press, not a JPMorgan or BlackRock document.</p>',
  'for custody clients<sup class="fnref"><a href="#s45">45</a></sup>; that 2016 report is trade press, not a JPMorgan or BlackRock document.</p>')
R('Adoption is growing among client types whose records are public. Between 2023 and 2025, a bank’s proxy statement,',
  'Adoption is growing among client types whose records are public: between 2023 and 2025, a bank’s proxy statement,')

# ---- flow: Part 2 findings run on; Part 3 runs on after "What would change my view"
R('<section class="chapter finding" id="f2">', '<section class="chapter finding runon" id="f2">')
R('<section class="chapter finding" id="f3">', '<section class="chapter finding runon" id="f3">')
R('<section class="chapter part" id="part-3">', '<section class="chapter part runon" id="part-3">')

open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("pass 4 applied", n, "edits")
