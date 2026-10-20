import json,html,collections
S="/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc"
d=json.load(open(S+"/compiled.json")); fin=d["fin"]; cl=d["claims"]
E=lambda s: html.escape(s or "")
OBS=["about a day","reasons I cannot see","How many clients use the APIs today","Learning about it from outside"]
def obsolete(c): return any(k in c for k in OBS)
pg=lambda i:int(cl[i]["page"])
order=lambda i:(pg(i),i)
cnt1=collections.Counter(v["first"] for v in fin.values()); cnt2=collections.Counter(v["final"] for v in fin.values())
V=["CONFIRMED","CONFIRMED (note)","CORPUS-ONLY","PARTLY","UNVERIFIED","WRONG"]
def row(i):
    f=fin[i]; c=cl[i]
    ob=' <span class="ob">text since changed</span>' if obsolete(f["claim"]) else ""
    moved="" if f["first"]==f["final"] else f' <span class="mv">first check: {E(f["first"])}</span>'
    return (f'<article class="f"><header><span class="id">{E(i)}</span> <span class="pg">Page {pg(i)}</span> '
            f'<span class="loc">{E(c["loc"])}</span>{moved}{ob}</header>'
            f'<p class="cl">{E(f["claim"])}</p><p class="fx"><b>Finding.</b> {E(f["correction"])}</p>'
            f'<p class="rc"><b>Receipt.</b> {E(f["receipt"])}</p></article>')
sec=[]
for v,title,blurb in [("WRONG","Wrong","A source contradicts the claim. Both checkers agree unless noted."),
                      ("PARTLY","Partly wrong","Part of the claim holds. The finding names the words that do not, or a citation that does not support the sentence."),
                      ("UNVERIFIED","Unverified","Not contradicted, but neither checker found a source."),
                      ("CORPUS-ONLY","Supported only by our own transcripts","True in our transcripts or crawled pages, but the checkers could not reach the words on the open web.")]:
    ids=sorted([i for i in fin if fin[i]["final"]==v],key=order)
    sec.append(f'<section><h2>{title} <span class="n">{len(ids)}</span></h2><p class="blurb">{blurb}</p>'+"".join(row(i) for i in ids)+'</section>')
tbl="".join(f'<tr><td>{v}</td><td>{cnt1.get(v,0)}</td><td>{cnt2.get(v,0)}</td></tr>' for v in V)
doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fact Check Findings</title><style>
:root{{--bg:#fff;--fg:#111;--mut:#555;--line:#ddd;--box:#f5f5f2;--acc:#FFCE00;--red:#b3261e;--amb:#8a5a00}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151515;--fg:#eee;--mut:#aaa;--line:#333;--box:#1f1f1f;--red:#ff8a80;--amb:#ffcc66}}}}
:root[data-theme="dark"]{{--bg:#151515;--fg:#eee;--mut:#aaa;--line:#333;--box:#1f1f1f;--red:#ff8a80;--amb:#ffcc66}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif;max-width:900px;margin:0 auto;padding:24px 16px}}
h1{{font-size:26px;margin:0 0 4px}} h1:before{{content:"";display:block;width:56px;height:6px;background:var(--acc);margin-bottom:14px}}
h2{{font-size:19px;border-top:2px solid var(--fg);padding-top:10px;margin-top:36px}} .n{{color:var(--mut);font-weight:400}}
.blurb,.mut{{color:var(--mut)}} table{{border-collapse:collapse;margin:8px 0 16px}} td,th{{border-bottom:1px solid var(--line);padding:4px 14px 4px 0;text-align:left}}
.f{{border-bottom:1px solid var(--line);padding:10px 0}} .f header{{font-size:13px;color:var(--mut)}} .id{{font-family:ui-monospace,monospace;color:var(--fg)}}
.pg{{font-weight:600;color:var(--fg)}} .mv{{color:var(--amb)}} .ob{{background:var(--box);padding:0 6px;border-radius:3px}}
.cl{{font-weight:600;margin:4px 0}} .fx{{margin:4px 0}} .rc{{margin:4px 0;font-size:13px;color:var(--mut);overflow-wrap:anywhere}}
ul{{padding-left:20px}} li{{margin:4px 0}}
</style></head><body>
<h1>Fact check findings</h1>
<p class="mut">"Aladdin Studio from the outside", checked October 20, 2026. Report only: nothing in the document was changed.</p>
<h2>How it was checked</h2>
<ul><li>Nine agents listed every factual claim: 796 claims, including every exhibit cell and all 70 Sources entries.</li>
<li>133 agents each checked six claims, on the open web first, and had to quote the words that support or contradict each one.</li>
<li>A second, independent agent re-checked all 199 claims the first pass did not confirm, and tried to overturn the first verdict.</li>
<li>Claims were taken from the version with the page 7 cut (v7). Text changed since then is marked "text since changed". Sources numbered 64 to 70 here are 65 to 71 in the current document, because the Aladdin Graph posting became source 64.</li>
<li>Part way through, the shared web-search allowance ran out. Later checkers fetched pages directly instead, and some say so in their receipts.</li></ul>
<table><tr><th>Verdict</th><th>First check</th><th>After re-check</th></tr>{tbl}</table>
{"".join(sec)}
</body></html>'''
open(S+"/FACT_CHECK_FINDINGS.html","w").write(doc); print("written", len(doc))
