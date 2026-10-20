import re,html,json
V="/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/v20check"
cur=open("/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.html",encoding="utf-8").read()
curtxt=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',cur)))
norm=lambda s: re.sub(r'[^a-z0-9]+','',s.lower())
CN=norm(curtxt)
E=html.escape
items=[]
for f,rng in [("read_p01_04","Pages 1–4"),("read_p05_08","Pages 5–8"),("read_p09_12","Pages 9–12"),("read_p13_16","Pages 13–16")]:
    t=open(f"{V}/{f}.md").read()
    m=re.search(r'#+\s*SHOULD FIX.*?\n(.*?)(?=\n#+\s*OPTIONAL|\Z)',t,re.S)
    body=m.group(1)
    blocks=re.split(r'\n(?=(?:\*\*S\d+\.|###\s*S\d+\.))',body)
    for b in blocks:
        b=b.strip()
        if not re.match(r'(\*\*S\d+\.|###\s*S\d+\.)',b): continue
        head=re.sub(r'^(\*\*|###\s*)','',b.split('\n')[0]).strip().strip('*').strip()
        def field(name):
            mm=re.search(r'(?:^|\n)\s*-?\s*\*?\*?'+name+r'[^:\n]*:\*?\*?\s*(.*?)(?=\n\s*-?\s*\*?\*?(?:Current|Problem|Rewrite|Type|Why|Add)[^:\n]*:|\Z)',b,re.S)
            return re.sub(r'\s+',' ',mm.group(1)).strip() if mm else ""
        c=field("Current") or "(the whole paragraph)"; p=field("Problem") or field("Type"); r=field("Rewrite") or field("Add")
        quotes=re.findall(r'"([^"]{25,})"|“([^”]{25,})”',c)
        qs=[a or b2 for a,b2 in quotes] or [c]
        status=""
        probe=[norm(q)[:60] for q in qs if len(norm(q))>=25]
        if probe and not any(pp in CN for pp in probe): status="Wording has changed since this review (v21 or the pending preview). Check before applying."
        items.append(dict(src=rng,head=head,cur=c,prob=p,fix=r,status=status))
print(len(items), sum(1 for i in items if i["status"]))
json.dump(items,open(V+"/should_items.json","w"),indent=1)
rows=[]; last=None; n=0
for it in items:
    if it["src"]!=last:
        cnt=sum(1 for x in items if x["src"]==it["src"]); rows.append(f'<h2>{E(it["src"])} <span class="c">{cnt}</span></h2>'); last=it["src"]
    n+=1
    st=f'<div class="st">{E(it["status"])}</div>' if it["status"] else ''
    rows.append(f'<div class="it"><div class="hd"><b>{n}.</b> {E(it["head"])}</div>{st}<div class="g"><div class="l">Now</div><div class="cur">{E(it["cur"])}</div>{('<div class="l">Problem</div><div class="why">'+E(it["prob"])+'</div>') if it["prob"] else ''}<div class="l">Fix</div><div class="new">{E(it["fix"])}</div></div></div>')
nchg=sum(1 for i in items if i["status"])
doc=f'''<!doctype html><html><head><meta charset="utf-8"><title>Should-fix items</title><style>
@page{{size:612pt 792pt;margin:42pt 48pt}} body{{font:9.5pt/1.4 Helvetica,Arial,sans-serif;color:#111}}
h1{{font-size:17pt;margin:0 0 4pt}} h1:before{{content:"";display:block;width:50pt;height:5pt;background:#FFCE00;margin-bottom:10pt}}
.sub{{color:#555;margin:0 0 6pt}} h2{{font-size:12pt;border-top:2pt solid #111;padding-top:5pt;margin:14pt 0 4pt}} .c{{color:#777;font-weight:400}}
.it{{break-inside:avoid;border-bottom:.6pt solid #ccc;padding:5pt 0}} .hd{{font-size:10pt;margin-bottom:2pt}}
.g{{display:grid;grid-template-columns:44pt 1fr;row-gap:2pt}} .l{{font-size:7.5pt;text-transform:uppercase;letter-spacing:.4pt;color:#777;padding-top:1.5pt}}
.cur{{color:#555}} .new{{background:#FFF6CC;padding:1pt 4pt}} .why{{color:#333}} .st{{font-size:8.5pt;color:#8a5a00;margin:1pt 0 3pt}}
</style></head><body>
<h1>The {len(items)} should-fix items, with suggested fixes</h1>
<p class="sub">From the four readability reviews of v20. Each item shows the wording now, the problem and a suggested rewrite that keeps every fact and citation. {nchg} items are marked where the wording has changed since: the must-fix round in v21, the Exhibits 3 and 4 redraw or the seven factual fixes. Check those against the latest text. Nothing here has been applied.</p>
{''.join(rows)}</body></html>'''
open(V+"/Should_fix_items.html","w").write(doc)
