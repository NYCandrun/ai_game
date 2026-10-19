#!/usr/bin/env python3
"""Pass 7: free ~20pt on the Exhibit 14/15 page so Finding 3's direction box joins its exhibits."""
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
R('Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources; State Street Alpha, Charles River and Bloomberg are not listed because my sources hold none.</p>',
  'Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources; State Street Alpha, Charles River and Bloomberg have none there, so they are not listed.</p>')
R('<td>Governance in one place; each user keeps their Aladdin permissions (“permission-dependent access”); guardrails against giving advice, tested in the system prompt; enterprise trust; a rollout BlackRock controls, team by team<sup class="fnref"><a href="#s16">16</a>, <a href="#s9">9</a></sup></td><td>Prospects can find it; developers adopt it on their own; it signals an ecosystem; it gives a ready answer to the RFP question about connectors; and it matches what FactSet, LSEG and MSCI now offer, which is the comparison buyers make<sup',
  '<td>Governance in one place; users keep their Aladdin permissions (“permission-dependent access”); guardrails against advice, tested in the system prompt; enterprise trust; a rollout BlackRock controls, team by team<sup class="fnref"><a href="#s16">16</a>, <a href="#s9">9</a></sup></td><td>Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors; and it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make<sup')
R('In BlackRock’s own words, that description answers the RFP connector question better than an MCP server with a partial catalog would. It also lets BlackRock, not FactSet and LSEG, set the terms on which buyers compare.',
  'In BlackRock’s own words, that answers the RFP connector question better than an MCP server with a partial catalog would. It also lets BlackRock, not FactSet and LSEG, set the terms of comparison.')
open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("pass 7 applied", n, "edits")
