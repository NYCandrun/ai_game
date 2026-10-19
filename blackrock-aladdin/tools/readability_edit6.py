#!/usr/bin/env python3
"""Pass 6: white-space pass (Finding 3 box onto its page; Exhibit 17 column widths; cover page numbers)."""
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

# Exhibit 14: wider middle column, two-line note
R('<colgroup><col style="width:80pt"><col><col style="width:150pt"></colgroup>\n<thead><tr><th>Provider</th><th>What is public</th><th>Receipt</th></tr></thead>',
  '<colgroup><col style="width:70pt"><col><col style="width:140pt"></colgroup>\n<thead><tr><th>Provider</th><th>What is public</th><th>Receipt</th></tr></thead>')
R('Of the system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources; State Street Alpha, Charles River and Bloomberg are not listed because my sources hold none for them.</p>',
  'Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources; State Street Alpha, Charles River and Bloomberg are not listed because my sources hold none.</p>')
# Exhibit 15: the For/inside cell back to four lines
R('enterprise trust; a rollout BlackRock controls, one engineering team at a time<sup', 'enterprise trust; a rollout BlackRock controls, team by team<sup')
# Finding 3 direction box: same sentences, fewer words
R('Said in BlackRock’s own words, that description answers the RFP question about connectors better than an MCP server with a partial catalog would. It also lets BlackRock, not FactSet and LSEG, set the terms on which buyers compare. I would hold any outside connector for now. The inside model already answers three governance questions: who can call what, with which permissions, and under which guardrails. An outside connector should wait until those are answered for outside callers too. Exhibit 15 is the evidence for that view; this is the fifth direction in Part 3.</p>',
  'In BlackRock’s own words, that description answers the RFP connector question better than an MCP server with a partial catalog would. It also lets BlackRock, not FactSet and LSEG, set the terms on which buyers compare. I would hold any outside connector for now. The inside model already answers three governance questions: who can call what, with which permissions, and under which guardrails. An outside connector should wait until those are answered for outside callers. Exhibit 15 is the evidence; this is the fifth direction in Part 3.</p>')
# Exhibit 17: give "What it involves" more width
R('<colgroup><col style="width:92pt"><col style="width:62pt"><col><col style="width:78pt"><col style="width:96pt"></colgroup>\n<thead><tr><th>Direction</th>',
  '<colgroup><col style="width:92pt"><col style="width:48pt"><col><col style="width:68pt"><col style="width:84pt"></colgroup>\n<thead><tr><th>Direction</th>')
# Cover page numbers (Finding 1 now starts on page 10, Part 3 on page 15)
R('<p class="pt"><a href="#f1">Four findings on where BlackRock is heading and what the market is doing</a></p><p class="pc">Page 9</p>',
  '<p class="pt"><a href="#f1">Four findings on where BlackRock is heading and what the market is doing</a></p><p class="pc">Page 10</p>')
R('<p class="pt"><a href="#part-3">Where the research points this role’s first six months</a></p><p class="pc">Page 14</p>',
  '<p class="pt"><a href="#part-3">Where the research points this role’s first six months</a></p><p class="pc">Page 15</p>')

open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("pass 6 applied", n, "edits")
