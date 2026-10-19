import re, sys, html as H, difflib
from html.parser import HTMLParser
B='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
htmlpath=sys.argv[1] if len(sys.argv)>1 else B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.html'
mdpath=B+'/pdfcheck/out/Aladdin_Briefing_and_Interview_Guide_REVISED.md'

def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    s=s.replace('—',' - ').replace('–','-').replace(' ',' ').replace('…','...')
    s=s.replace('&','&')
    s=re.sub(r'\s+',' ',s).strip()
    return s

# ---- HTML text blocks
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.blocks=[]; s.cur=[]; s.skip=0; s.line=1
    def flush(s):
        t=norm(''.join(s.cur))
        if t: s.blocks.append((s.bline,t))
        s.cur=[]
    def handle_starttag(s,tag,attrs):
        if tag in('style','head','nav','script'): s.skip+=1
        if tag=='sup' and ('class','fnref') in attrs: s.skip+=1
        if tag in ('p','li','td','th','h1','h2','h3','h4','div','section','tr','table','figure','ul','ol','br'):
            s.flush(); s.bline=s.getpos()[0]
    def handle_endtag(s,tag):
        if tag in('style','head','nav','script'): s.skip-=1
        if tag=='sup' and s.skip>0: s.skip-=1
        if tag in ('p','li','td','th','h1','h2','h3','h4','div','section','tr','table','figure','ul','ol'):
            s.flush()
    def handle_data(s,d):
        if s.skip<=0:
            if not s.cur: s.bline=s.getpos()[0]
            s.cur.append(d)
p=P(); p.bline=1
p.feed(open(htmlpath,encoding='utf-8').read())
hblocks=p.blocks

# ---- MD blocks
md=open(mdpath,encoding='utf-8').read().split('\n')
mblocks=[]
for i,l in enumerate(md,1):
    l=l.strip()
    if not l or l.startswith('---') or re.match(r'^\|[-| ]+\|$',l): continue
    l=re.sub(r'^#+\s*','',l); l=re.sub(r'^[-*]\s+','',l); l=re.sub(r'^\d+\.\s+','',l)
    if l.startswith('|'):
        cells=[c.strip() for c in l.strip('|').split('|')]
    else: cells=[l]
    for c in cells:
        c=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',c)
        c=c.replace('**','').replace('\\&','&').replace('\\$','$').replace('\\_','_').replace('\\*','*').replace('\\"','"')
        c=re.sub(r'(?<!\w)\*([^*]+)\*(?!\w)',r'\1',c)
        c=re.sub(r'\[\^[^\]]+\]','',c)
        c=norm(c)
        if c: mblocks.append((i,c))

def sents(t):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-Z"\'(\[])',t) if x.strip()]
hs=set(); 
for ln,t in hblocks:
    hs.add(t)
    for x in sents(t): hs.add(x)
ms=set()
for ln,t in mblocks:
    ms.add(t)
    for x in sents(t): ms.add(x)
mode=sys.argv[2] if len(sys.argv)>2 else 'md'
if mode=='md':
    hl=[x for x in hs if len(x)>12]
    hw={h:set(re.findall(r'\w+',h.lower())) for h in hl}
    out=[]
    for ln,t in mblocks:
        for x in sents(t):
            if x not in hs and len(x)>12:
                xw=set(re.findall(r'\w+',x.lower()))
                cands=sorted(hl,key=lambda h:-len(xw&hw[h])/(len(xw|hw[h]) or 1))[:12]
                best=(0,'')
                for c in cands:
                    if difflib.SequenceMatcher(None,x,c).quick_ratio()<=best[0]: continue
                    r=difflib.SequenceMatcher(None,x,c).ratio()
                    if r>best[0]: best=(r,c)
                out.append((best[0],ln,x,best[1]))
    for r,ln,x,m in out:
        print(f'MD{ln} [{r:.2f}]: {x}')
        if r<0.995: print(f'   HTML: {m}')
else:
    for ln,t in hblocks:
        for x in sents(t):
            if x not in ms and len(x)>12:
                print(f'H{ln}: {x}')
