import re, sys, html as H, pdfplumber
B='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
OUT=B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.html'
PDF=B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.pdf'
s=open(OUT,encoding='utf-8').read()
def norm(t): return re.sub(r'\s+',' ',H.unescape(t).replace('’',"'").replace('’',"'")).strip()
# headings: (anchor id, text)
heads=[]
for m in re.finditer(r'<section class="chapter[^"]*" id="([^"]+)"><h2[^>]*>(.*?)</h2>',s): heads.append((m.group(1),norm(re.sub(r'<[^>]+>','',m.group(2))),'h2'))
for m in re.finditer(r'<section class="fullpage divider" id="([^"]+)">.*?<h1>(.*?)</h1>',s,re.S): heads.append((m.group(1),norm(re.sub(r'<[^>]+>','',m.group(2))),'h1'))
big={}
with pdfplumber.open(PDF) as doc:
    for pn,p in enumerate(doc.pages,1):
        ws=p.extract_words(extra_attrs=['size'])
        big[pn]=(norm(' '.join(w['text'] for w in ws if w['size']>=19.5 and w['top']<700)), norm(' '.join(w['text'] for w in ws if w['size']>=39)))
pages={}
for aid,txt,kind in heads:
    hits=[pn for pn,(t20,t40) in big.items() if (txt in t20 if kind=='h2' else txt in t40)]
    if kind=='h2': hits=[pn for pn in hits if pn>2]
    pages[aid]=hits
    print(aid,txt,hits)
# patch toc and divider page numbers
def patch(m):
    aid=m.group(2); hits=pages.get(aid)
    if not hits: print('NO PAGE FOR',aid); return m.group(0)
    return '%s%d%s'%(m.group(1),hits[0],m.group(4))
s2=re.sub(r'(<a href="#([^"]+)">[^<]*</a></span><span class="pg">)(\d+)(</span>)',patch,s)
if s2!=s:
    open(OUT,'w',encoding='utf-8').write(s2); print('patched page numbers')
else: print('page numbers unchanged')
