import re
p='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/review24/Proposed_v24_changes.html'
h=open(p,encoding='utf-8').read()
h=h.replace('</style>','.tag{display:inline-block;color:#fff;font-weight:bold;padding:1pt 4pt;margin-right:3pt;font-size:7.6pt}.keep{background:#1a7f37}.cut{background:#c62828}\n</style>',1)
h=h.replace("Your decision: keep. ","<span class='tag keep'>YOUR DECISION: KEEP</span> ")
h=h.replace("Your decision: cut. No change to v23. ","<span class='tag cut'>YOUR DECISION: CUT</span> No change to v23. ")
box=("<div class='box'><b>Your decisions on the extra-detail items:</b> "
     "<span class='tag keep'>KEEP</span> fix 50 (growth without Preqin), fix 58 (Studio Compute naming), fix 60 (internal-only operations), fix 61 (Spaces), N6 (Exhibit 15 owners line). "
     "<span class='tag cut'>CUT</span> fix 43 (long-running operations) and N9 (sector-exposure example). Each is tagged in the tables below.</div>")
h=h.replace("<h2>Six decisions for you first</h2>", box+"<h2>Six decisions for you first</h2>",1)
h=h.replace("<li>Optional: one line on who owns each row (N6).</li>","<li>One line on who owns each row (N6).</li>")
open(p,'w',encoding='utf-8').write(h)
print(h.count("class='tag keep'"), h.count("class='tag cut'"))
