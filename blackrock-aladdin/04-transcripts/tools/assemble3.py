import csv,re,os,glob,collections,json
rows=list(csv.DictReader(open('media2/MANIFEST.tsv'),delimiter='\t'))
media=[r for r in rows if re.search(r'\.(mp3|mp4)$',r['filename'])]
has_tx={}
for t in glob.glob('media2/*.transcript.txt'):
    m=re.search(r'# audio: (\S+)',open(t).read(1000))
    if m: has_tx[m.group(1)]=t
def base(fn): return re.sub(r'\.(720p|1080p|480p)\.wide\.mp4$|\.mp3$|\.mp4$','',fn)
def key(title):
    t=title.split(' / feed:')[0]; t=re.sub(r'\s*\[.*?\]\s*$','',t); t=re.sub(r'[^a-z0-9 ]','',t.lower()); return ' '.join(t.split()[:7])
def para(t,n=110):
    w=t.split();out=[];cur=[]
    for x in w:
        cur.append(x)
        if len(cur)>=n and x.endswith(('.','?','!')): out.append(' '.join(cur));cur=[]
    if cur: out.append(' '.join(cur))
    return '\n\n'.join(out)
parent={}
def find(x):
    while parent.setdefault(x,x)!=x: x=parent[x]
    return x
def union(a,b): parent[find(a)]=find(b)
bykey={}
for r in media:
    fn=r['filename']; find(fn); k=key(r['title'])
    if k in bykey: union(fn,bykey[k])
    else: bykey[k]=fn
    s=(r.get('same_audio_as') or '').strip()
    if s: union(fn,s)
groups=collections.OrderedDict()
for r in media: groups.setdefault(find(r['filename']),[]).append(r)
def source_text(fn):
    b=base(fn)
    if fn in has_tx:
        body=open(has_tx[fn]).read(); return re.sub(r'^(# .*\n)+','',body).strip(),'published transcript (BlackRock page)'
    cap='media2/'+b+'.captions.txt'
    if os.path.exists(cap): return para(open(cap).read().strip()),'published captions (CloudFront .vtt)'
    wf='media2/'+fn.rsplit('.',1)[0]+'.whisper.txt'
    if os.path.exists(wf): return para(open(wf).read().strip()),'Whisper from audio'
    return None,None
os.makedirs('transcripts2',exist_ok=True)
for f in glob.glob('transcripts2/*.md'): os.remove(f)
def cat_of(page,fn):
    if 'never-done' in page or 'rss.art19' in page or '/podcast/' in page or fn.endswith('.mp3'): return 'Podcast'
    if 'big-little' in page: return 'Big Little Questions'
    if 'uncharted' in page: return 'Uncharted'
    if 'webinar' in page: return 'Webinar replay'
    if 'efront.com' in page: return 'eFront video'
    if 'client-story' in page or 'testimonial' in page.lower() or 'implementations' in page: return 'Client story'
    return 'Other site video'
items=[];missing=[]
for g,rs in groups.items():
    rs2=sorted(rs,key=lambda r:(source_text(r['filename'])[0] is None, r['source_page_url'].startswith('feed:')))
    pick=rs2[0]; fn=pick['filename']; body,typ=source_text(fn)
    title=pick['title'].split(' / feed:')[0].strip(); title=re.sub(r'\s*\[.*?\]\s*$','',title)
    feedinfo=next((r['title'] for r in rs if re.search(r'\[.*\]\s*$',r['title'])),'')
    m=re.search(r'\[(.*?)\]\s*$',feedinfo); series=m.group(1) if m else ''
    page=next((r['source_page_url'] for r in rs if not r['source_page_url'].startswith('feed:')),pick['source_page_url'].replace('feed:',''))
    desc=(pick.get('description') or '').strip()
    if body is None: missing.append((title,page)); continue
    words=len(body.split())
    if words<15: missing.append((title+' (no speech)',page)); continue
    items.append((cat_of(page,fn),series,title,page,fn,typ,desc,body,words))
order={'Podcast':0,'Big Little Questions':1,'Uncharted':2,'Webinar replay':3,'Client story':4,'Other site video':5,'eFront video':6}
items.sort(key=lambda x:(order[x[0]],x[2].lower()))
idx=['# Transcripts part 2: audio and video hosted on the Aladdin and eFront sites\n','Published transcripts and captions are BlackRock\'s own text. Everything marked Whisper is a local machine transcription of the downloaded audio, so names and jargon can be mis-heard.\n','| # | Category | Title | Series / date | Source page | Transcript type | Size |','|---|---|---|---|---|---|---|']
for n,(cat,series,title,page,fn,typ,desc,body,words) in enumerate(items,1):
    safe=re.sub(r'[^A-Za-z0-9]+','_',title)[:64].strip('_')
    with open(f'transcripts2/{n:03d}_{safe}.md','w') as f:
        f.write(f'# {title}\n\nCategory: {cat}  \n'+(f'Series: {series}  \n' if series else '')+f'Source page: {page}  \nMedia file: {fn}  \nTranscript: {typ}.\n\n'+(f'Description: {desc}\n\n' if desc else '')+'---\n\n'+body+'\n')
    idx.append(f'| {n} | {cat} | {title} | {series} | {page} | {typ} | {words:,} words |')
if missing: idx.append('\n## Not transcribed\n'+'\n'.join(f'- {t} ({p})' for t,p in missing))
open('transcripts2/00_INDEX.md','w').write('\n'.join(idx)+'\n')
print(len(items),'written;',len(missing),'missing');print(collections.Counter(i[0] for i in items));print(collections.Counter(i[5] for i in items))
