import re
p='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/review24/Proposed_v24_changes.html'
h=open(p,encoding='utf-8').read()
h=h.replace('</style>','.skip{display:inline-block;background:#c62828;color:#fff;font-weight:bold;padding:1pt 4pt;margin-right:3pt;font-size:7.6pt}\n</style>',1)
# tag inside table cells only
h=re.sub(r"(<td class='rec'>)(Optional\. |)Consider skipping\.?", r"\1<span class='skip'>CONSIDER SKIPPING</span>", h)
h=re.sub(r"(<td class='rec'>Reorder to 1, 4, 3, 2\. )Consider skipping the owners line\.", r"\1<span class='skip'>CONSIDER SKIPPING</span> the owners line.", h)
h=h.replace("<td class='rec'>Optional. &quot;Copilot","<td class='rec'><span class='skip'>CONSIDER SKIPPING</span> &quot;Copilot")
box=("<div class='box'><b>Marked <span class='skip'>CONSIDER SKIPPING</span></b> (extra detail that does not change the argument): "
     "fix 43 long-running operations, fix 50 growth without Preqin, fix 58 Studio Compute naming, fix 60 internal-only operations, "
     "fix 61 Spaces, N6 the Exhibit 15 owners line, and N9 the sector-exposure example. Each is tagged in red in the tables below.</div>")
h=h.replace("<h2>Six decisions for you first</h2>", box+"<h2>Six decisions for you first</h2>",1)
open(p,'w',encoding='utf-8').write(h)
print(h.count("class='skip'"))
