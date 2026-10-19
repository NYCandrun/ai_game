#!/usr/bin/env python3
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
R('<figure class="exhibit" id="exhibit-15">', '<figure class="exhibit" id="exhibit-15" style="margin-bottom:8pt">')
R('I would describe the Copilot plugin model publicly, now. Copilot’s tools are production Aladdin APIs, the same governed APIs Studio exposes. Copilot inherits each user’s permissions. Its guardrails against giving advice are tested in the system prompt, and it never gives investment advice<sup class="fnref"><a href="#s9">9</a>, <a href="#s16">16</a></sup>. In BlackRock’s own words, that answers the RFP connector question better than an MCP server with a partial catalog would.',
  'I would describe the Copilot plugin model publicly now. Copilot’s tools are production Aladdin APIs, the same governed APIs Studio exposes. Copilot inherits each user’s permissions. Its no-advice guardrails are tested in the system prompt, and it never gives investment advice<sup class="fnref"><a href="#s9">9</a>, <a href="#s16">16</a></sup>. In BlackRock’s own words, that answers the RFP connector question better than an MCP server with a partial catalog.')
open(P, "w", encoding="utf-8").write(head + "</head>" + body)
print("pass 8 applied", n, "edits")
