# Applies FIX_PLAN.json to a PREVIEW copy only. DECIDE items use the recommended option (proposed_html).
import json,re,sys,subprocess,shutil
F="/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix"
G="/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm"
plan=json.load(open(F+"/FIX_PLAN.json"))
h=open(F+"/current.html",encoding="utf-8").read()
applied=[];skipped=[];newsrc={}
for o in plan:
    if o["action"]=="NO CHANGE" or not o.get("proposed_html"): continue
    pairs=[(o["current_html"],o["proposed_html"])]+[(a.get("current_html") or a.get("current",""),a.get("proposed_html") or a.get("proposed","")) for a in (o.get("also_change") or []) if isinstance(a,dict) and "alternative only" not in (a.get("where") or "").lower()]
    for cur,new in pairs:
        if not cur or not new: continue
        n=h.count(cur)
        if n!=1: skipped.append((o["id"],n,cur[:80])); continue
        h=h.replace(cur,new); applied.append(o["id"])
    for e in o.get("new_sources") or []:
        m=re.match(r'<p id="(s[^"]+)">',e)
        if m and m.group(1) not in newsrc: newsrc[m.group(1)]=e
# give NEW sources temporary numbers
for k,(nid,e) in enumerate(newsrc.items()):
    num=900+k
    e=re.sub(r'<p id="[^"]+"><b class="n">[^<]*</b>',f'<p id="s{num}"><b class="n">{num}</b>',e,count=1)
    h=re.sub(r'<a href="#'+re.escape(nid)+r'">[^<]*</a>',f'<a href="#s{num}">{num}</a>',h)
    i=h.index('<div class="register">')+len('<div class="register">\n'); h=h[:i]+e.strip()+"\n"+h[i:]
left=re.findall(r'href="#sNEW[^"]*"',h)
# sort numbers inside each superscript
def fix(m):
    links=re.findall(r'<a href="#s\d+">\d+</a>',m.group(1))
    links=sorted(dict.fromkeys(links),key=lambda a:int(re.search(r'>(\d+)<',a).group(1)))
    return '<sup class="fnref">'+', '.join(links)+'</sup>'
h=re.sub(r'<sup class="fnref">(.*?)</sup>',fix,h)
# drop register entries no longer cited
body=h[:h.index('<div class="register">')]+h[h.index('</div>\n</section>',h.index('<div class="register">')):]
cited=set(re.findall(r'<a href="#(s\d+)">',body))
orph=[]
def drop(m):
    if m.group(1) not in cited: orph.append(m.group(1)); return ""
    return m.group(0)
a=h.index('<div class="register">'); b=h.index('</div>\n</section>',a)
reg=re.sub(r'<p id="(s\d+)">.*?</p>\n',drop,h[a:b],flags=re.S); h=h[:a]+reg+h[b:]
P=F+"/preview.html"; open(P,"w",encoding="utf-8").write(h)
r=subprocess.run(["python3","-I",G+"/renumber.py",P],capture_output=True,text=True); print(r.stdout[-300:],r.stderr[-800:])
h=open(P,encoding="utf-8").read(); a=h.index('<div class="register">'); b=h.index('</div>\n</section>',a)
ents=re.findall(r'<p id="s\d+">.*?</p>\n',h[a:b],flags=re.S); ents.sort(key=lambda e:int(re.match(r'<p id="s(\d+)"',e).group(1)))
h=h[:a]+'<div class="register">\n'+''.join(ents)+h[b:]; h=re.sub(r'<sup class="fnref">(.*?)</sup>',fix,h); open(P,"w",encoding="utf-8").write(h)
print("applied",len(applied),"skipped",skipped,"new sources",len(newsrc),"unresolved NEW refs",left,"dropped orphans",orph)
