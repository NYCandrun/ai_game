import re,sys,html
def clean(path):
    cues=[];last=''
    for block in open(path,encoding='utf-8').read().split('\n\n'):
        lines=[l for l in block.strip().split('\n') if l and '-->' not in l and not l.startswith(('WEBVTT','Kind:','Language:'))]
        for l in lines:
            t=re.sub(r'<[^>]+>','',l); t=html.unescape(t).strip()
            if not t or t==last: continue
            # auto captions repeat the previous line as the first line of the next cue
            if cues and (cues[-1].endswith(t) or t.endswith(cues[-1])):
                if len(t)>len(cues[-1]): cues[-1]=t
                continue
            cues.append(t); last=t
    text=' '.join(cues); text=re.sub(r'\s+',' ',text)
    return text
for p in sys.argv[1:]:
    out=p.replace('.en.vtt','.txt'); txt=clean(p); open(out,'w').write(txt); print(out,len(txt.split()),'words')
