import re, sys, subprocess, html as H
import pdfplumber
B='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
OUT=B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.html'
PDF=B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.pdf'
TMPH=B+'/htmlrev/work/_zero.html'; TMPP=B+'/htmlrev/work/_zero.pdf'
BOTTOM=733.4   # measured glyph bottom of the last text line on a full page (reference render)

def norm(t):
    t=H.unescape(t)
    t=t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace(' ',' ').replace('—','-').replace('–','-').replace('…','...')
    return re.sub(r'\s+',' ',t).strip()
def strip(t): return norm(re.sub(r'<[^>]+>','',t))

def render(src,dst):
    r=subprocess.run(['node',B+'/htmlrev/tools/render_chromium.js',src,dst],cwd='/home/user/ai_game',capture_output=True,text=True)
    if r.returncode: print(r.stderr); sys.exit(1)

def blocks(s):
    out=[]
    for m in re.finditer(r'<div class="footnotes" id="([^"]+)" style="margin-top:([\d.]+)pt">(.*?)</div>',s,re.S):
        bid,mt,body=m.group(1),float(m.group(2)),m.group(3)
        notes=re.findall(r'<span id="fn-([^"]+)"><b>(\d+)</b>(.*?)</span>',body,re.S)
        out.append(dict(id=bid,mt=mt,span=m.span(),notes=[(f,int(n),strip(t)) for f,n,t in notes]))
    return out

def marker_phrase(s,fid):
    i=s.index('<sup class="fnref" id="fr-%s">'%fid)
    pre=strip(s[max(0,i-1500):i])
    w=pre.split()
    return ' '.join(w[-7:])

def load_pages(pdf):
    pages=[]
    with pdfplumber.open(pdf) as doc:
        for p in doc.pages:
            words=p.extract_words(use_text_flow=True,keep_blank_chars=False)
            txt=norm(' '.join(w['text'] for w in words))
            # char offset -> word index map
            offs=[];pos=0
            for i,w in enumerate(words):
                t=norm(w['text']); offs.append(pos); pos+=len(t)+1
            pages.append(dict(words=words,txt=txt,offs=offs))
    return pages

def find(pages,phrase,first=True):
    """return list of (pageno, top, bottom) for phrase occurrences"""
    ph=norm(phrase); res=[]
    if len(ph)<6: return res
    for pn,p in enumerate(pages,1):
        start=0
        while True:
            k=p['txt'].find(ph,start)
            if k<0: break
            # words covering k..k+len
            wi=[i for i,o in enumerate(p['offs']) if k<=o<k+len(ph)]
            if wi:
                ws=[p['words'][i] for i in wi]
                res.append((pn,min(w['top'] for w in ws),max(w['bottom'] for w in ws)))
            start=k+1
    return res

def measure(pdf,s,verbose=True):
    pages=load_pages(pdf)
    rows=[]
    for b in blocks(s):
        f0,n0,t0=b['notes'][0]; fl,nl,tl=b['notes'][-1]
        head=find(pages,(str(n0)+t0)[:60]) or find(pages,t0[:50])
        tail=find(pages,tl[-50:])
        if head: tail=[t for t in tail if t[0]==head[0][0]] or tail
        mk=[]
        for f,n,t in b['notes']:
            ph=marker_phrase(s,f)
            hits=find(pages,ph) or find(pages,' '.join(ph.split()[-4:]))
            mk.append((n,[h[0] for h in hits]))
        rows.append(dict(b=b,head=head,tail=tail,mk=mk))
        if verbose:
            hp=head[0] if head else None; tp=tail[-1] if tail else None
            mp=sorted(set(p for n,ps in mk for p in ps))
            flag=''
            bad=[n for n,ps in mk if ps and (hp and hp[0] not in ps)]
            if bad: flag='  <-- block not on marker page for notes %s'%bad
            if hp and tp and tp[0]!=hp[0]: flag+='  <-- block split across pages'
            if hp and tp and hp[0]==tp[0] and BOTTOM-tp[2]>14: flag+='  <-- gap %.0fpt'%(BOTTOM-tp[2])
            print('%-18s mt=%7.2f block p%s top=%s bottom=%s markers=%s %s'%(b['id'],b['mt'],hp[0] if hp else '?', ('%.1f'%hp[1]) if hp else '?', ('%.1f'%tp[2]) if tp else '?', [(n,ps) for n,ps in mk], flag))
    return rows,len(pages)

mode=sys.argv[1] if len(sys.argv)>1 else 'check'
s=open(OUT,encoding='utf-8').read()
if mode=='ref':
    s=open(B+'/htmlrev/src/briefing_original.html',encoding='utf-8').read()
    rows,n=measure(B+'/htmlrev/ref/br_chromium.pdf',s); print('pages',n)
elif mode=='check':
    rows,n=measure(PDF,s); print('pages',n)
elif mode=='fit':
    z=re.sub(r'(<div class="footnotes" id="[^"]+" style="margin-top:)[\d.]+pt',r'\g<1>0pt',s)
    open(TMPH,'w',encoding='utf-8').write(z)
    render(TMPH,TMPP)
    print('--- zero-margin measurement')
    rows,n=measure(TMPP,z); print('pages',n)
    news={}
    for r in rows:
        b=r['b']; hp=r['head'][0] if r['head'] else None; tp=r['tail'][-1] if r['tail'] else None
        mp=sorted(set(p for n_,ps in r['mk'] for p in ps))
        bad=[n for n,ps in r['mk'] if ps and hp and hp[0] not in ps]
        if hp and tp and hp[0]==tp[0] and not bad:
            news[b['id']]=max(0.0,b['mt']+BOTTOM-tp[2])
        else:
            print('CANNOT FIT',b['id'],'block page',hp and hp[0],tp and tp[0],'markers',mp)
    def sub(m):
        return '%s%.2fpt'%(m.group(1),news.get(m.group(2),float(m.group(3))))
    s2=re.sub(r'(<div class="footnotes" id="([^"]+)" style="margin-top:)([\d.]+)pt',lambda m:'%s%.2fpt'%(m.group(1),news.get(m.group(2),0.0 if m.group(2) not in news else 0)),s)
    # keep unfit blocks at 0 so they are visible
    open(OUT,'w',encoding='utf-8').write(s2)
    render(OUT,PDF)
    print('--- after fit')
    rows,n=measure(PDF,s2); print('pages',n)
elif mode=='where':
    pdf=sys.argv[2]; pages=load_pages(pdf)
    for ph in sys.argv[3:]:
        print(repr(ph[:40]), find(pages,ph))
elif mode=='refit':
    rows,n=measure(PDF,s,verbose=False)
    news={}
    for r in rows:
        b=r['b']; hp=r['head'][0] if r['head'] else None; tp=r['tail'][-1] if r['tail'] else None
        bad=[n_ for n_,ps in r['mk'] if ps and hp and hp[0] not in ps]
        if hp and tp and hp[0]==tp[0] and not bad:
            news[b['id']]=max(0.0,b['mt']+BOTTOM-tp[2])
        else: print('NOT FITTED',b['id'])
    s2=re.sub(r'(<div class="footnotes" id="([^"]+)" style="margin-top:)([\d.]+)pt',lambda m:'%s%.2fpt'%(m.group(1),news.get(m.group(2),float(m.group(3)))),s)
    open(OUT,'w',encoding='utf-8').write(s2); render(OUT,PDF)
    rows,n=measure(PDF,s2); print('pages',n)
