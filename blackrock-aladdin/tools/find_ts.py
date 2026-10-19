import re,sys,html,json
def norm(s):
    s=html.unescape(s).lower().replace('’',"'").replace('‘',"'")
    s=re.sub(r'[^a-z0-9 ]+',' ',s)
    return s.split()
def load_vtt(p):
    cues=[]
    for block in open(p,encoding='utf-8').read().split('\n\n'):
        lines=[l for l in block.strip().split('\n')]
        tl=[l for l in lines if '-->' in l]
        if not tl: continue
        st=tl[0].split('-->')[0].strip()
        h,m,s=st.split(':'); sec=int(h)*3600+int(m)*60+float(s)
        txt=' '.join(re.sub(r'<[^>]+>','',l) for l in lines[lines.index(tl[0])+1:])
        cues.append((sec,html.unescape(txt)))
    # youtube auto-captions repeat lines; dedupe consecutive repeated text
    out=[];last=''
    for sec,t in cues:
        t=t.strip()
        if not t: continue
        if last and (t.startswith(last) ): t=t[len(last):].strip()
        elif last and last.endswith(t): continue
        # handle two-line cues where first line == last line of previous
        parts=t.split('\n')
        last=parts[-1].strip()
        out.append((sec,t.replace('\n',' ')))
    return out
def load_ts(p):
    out=[]
    for l in open(p,encoding='utf-8'):
        m=re.match(r'\[(\d+):(\d+)\]\s*(.*)',l)
        if m: out.append((int(m.group(1))*60+int(m.group(2)),m.group(3)))
    return out
def find(cues,quote):
    toks=[];pos=[]
    for sec,t in cues:
        for w in norm(t): toks.append(w); pos.append(sec)
    q=norm(quote)
    # try progressively shorter prefixes of the quote (first 8,6,5,4 words), also any 5-gram window
    best=None
    for n in (8,6,5,4,3):
        if len(q)<n: continue
        for start in range(0,min(len(q)-n+1,6)):
            g=q[start:start+n]
            for i in range(len(toks)-n+1):
                if toks[i:i+n]==g:
                    return pos[i], ' '.join(toks[i:i+14]), (n,start)
    return None
if __name__=='__main__':
    p=sys.argv[1]; cues=load_vtt(p) if p.endswith('.vtt') else load_ts(p)
    for qt in sys.argv[2:]:
        r=find(cues,qt)
        if r: print(f"{int(r[0])//60:02d}:{int(r[0])%60:02d}  [{r[2]}] {qt[:60]!r} -> {r[1]}")
        else: print(f"NOT FOUND {qt[:70]!r}")
