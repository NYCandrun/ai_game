import re,html as H,sys
S='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
old=open(S+'/v20check/v21_baseline.html',encoding='utf-8').read()
new=open(S+'/ex3back/preview_mapE.html',encoding='utf-8').read()
def reg(h):
    a=h.index('<div class="register">')
    return {int(n):H.unescape(re.sub('<[^>]+>','',t)).strip() for n,t in re.findall(r'<p id="s(\d+)">.*?<span class="t">(.*?)</span>',h[a:],flags=re.S)}
ro,rn=reg(old),reg(new); t2n={v:k for k,v in rn.items()}
def seg(h):
    a=h.index('<figure class="exhibit keep" id="exhibit-3">'); b=h.index('<figure class="exhibit keep" id="exhibit-4">')
    return a,b
a,b=seg(old); blk=old[a:b]
# remap citation numbers by title
def rm(m):
    n=int(m.group(1)); t=ro[n]; assert t in t2n,(n,t); return str(t2n[t])
blk=re.sub(r'(?<=href="#s)(\d+)(?=")',rm,blk)
blk=re.sub(r'(<a href="#s(\d+)">)\d+(</a>)',lambda m:m.group(1)+m.group(2)+m.group(3),blk)
def R(o,n):
    global blk; assert blk.count(o)==1,(o,blk.count(o)); blk=blk.replace(o,n)
R('<div class="row c2"><div class="t">Microsoft Azure today</div><div class="t hatch">AWS option, announced</div></div>',
  '<div class="row c2"><div class="t">Microsoft Azure</div><div class="t">Amazon Web Services</div></div>')
R('Hosting: Microsoft Azure today, and an AWS option that is announced, not live.','Hosting: Microsoft Azure and Amazon Web Services.')
R('<div class="studio"><b>Aladdin Studio:</b> the developer and data layer; its parts are in Exhibit 4</div>',
  '<div class="studio"><b>Aladdin Studio:</b> the developer and data layer, whose parts Exhibit 4 shows</div>')
R('<p class="cap">Controls built into the APIs</p>','<p class="cap">Controls in the API specifications</p>')
R('<span>Each API has its own access scope. A user sees only what their entitlements allow.</span>','<span>Each API has its own OAuth scopes.</span>')
R('<p><b>Compliance by default</b><span>The order API runs compliance by default and returns any violations.</span></p>\n<p style="margin:0"><b>A second approver</b><span>Dataset releases need a second check.</span></p></div>',
  '<p style="margin:0"><b>Compliance by default on orders</b><span>Posting an order runs compliance unless the caller turns it off, and returns any violations.</span></p></div>')
R('A side column lists the controls built into the APIs: access set per API, compliance by default on orders, and a second approver for dataset releases.',
  'A side column lists the controls in the API specifications: access set per API through OAuth scopes, and compliance by default when an order is posted, which the caller can turn off.')
R('Every box is named in the sources below; the AWS option is announced, not live. The 11 domains are the packages of BlackRock’s public SDK; the specifications also name Dashboard and Risk Radar.',
  'Every box is named in the sources below. The 11 domains are the packages of BlackRock’s public software development kit (SDK). The specifications also name Dashboard and Risk Radar.')
# hosting sources: replace "hosting, Azure and the AWS release[..]" with 10-K and Microsoft
m=re.search(r'hosting, Azure and the AWS release<sup class="fnref">(.*?)</sup>',blk); nums=re.findall(r'#s(\d+)',m.group(1))
print('old hosting cites (new numbering):',[(n,rn[int(n)]) for n in nums])
ms=[n for n in nums if n!='21']
assert len(ms)==1
k=t2n[[t for t in rn.values() if t.startswith('BlackRock, Inc., Form 10-K')][0]]
blk=blk.replace(m.group(0),f'the FY2025 10-K, for hosting<sup class="fnref"><a href="#s{k}">{k}</a></sup>; Microsoft, for Azure<sup class="fnref"><a href="#s{ms[0]}">{ms[0]}</a></sup>')
c,d=seg(new); out=new[:c]+blk+new[d:]
open(S+'/redraw34/preview.html','w',encoding='utf-8').write(out)
print(re.sub(r'\s+',' ',H.unescape(re.sub('<[^>]+>',' ',re.sub(r'<style>.*?</style>','',blk,flags=re.S)))))
