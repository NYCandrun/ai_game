import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
def sub(pat,repl,n=1,flags=0):
    global s
    k=len(re.findall(pat,s,flags)); assert k==n,(k,pat[:80]); s=re.sub(pat,repl,s,flags=flags)
# 1 cover line
rep('<p class="prepared-for">Prepared for BlackRock</p>','<p class="prepared-for">Notes made to prepare for interviews, October 2026</p>')
# 2 stat tiles + their source note
sub(r'<div class="stats three">.*?</div>\n<p class="stats-src"[^>]*>.*?</p>\n','',flags=re.S)
# 3 lede and speakers
rep('<p class="lede">Studio is the layer of Aladdin that clients build on, and the layer Copilot runs on.</p>','<p class="lede">Studio is the layer of Aladdin that clients build on.</p>')
rep('Four BlackRock speakers have defined it the same way since 2024','Five BlackRock speakers have defined it on the record, and four give these same three parts')
# 4 Janus Henderson paragraph
rep('In December 2025 a Janus Henderson engineer submitted two changes','In December 2025 an engineer at a client firm submitted two changes')
sub(r' merged them\. The <a href="[^"]+">commits</a> name a janushenderson\.com address as the author(<sup class="fnref">)',r' merged them\1')
# 5 Exhibit 16 reference row
rep('Janus Henderson first, a public pension award as fallback','a public pension award, or a client whose engineers have contributed to the SDK')
# 6 typeface sentence
sub(r'\s*<p>The text is set in Barlow and Barlow Condensed[^<]*</p>','')
# 7 stale source note
rep(' Goel also gives the 3,000 citizen-developer figure, at 35:23. Exhibit 3 credits it to Woodhead, who gives it at 9:39 in entry 5.','')
# 8 Exhibit 2 total column
i=s.index('<figure class="exhibit keep" id="exhibit-2">'); j=s.index('</figure>',i)
blk=s[i:j]
blk2=blk.replace('<th>Total</th>\n','',1)
blk2,n=re.subn(r'<td class="score"><span class="bar" style="width:[\d.]+pt"></span><b>\d+</b></td>\n','',blk2); assert n==11,n
blk2=blk2.replace('<td colspan="10">','<td colspan="9">'); assert blk2.count('colspan="9"')==2
s=s[:i]+blk2+s[j:]
rep('It scores each on eight things a developer with no client relationship can reach. The total sums the eight scores, so it runs from 0 to 16. A high total means the vendor opens to developers before any sale; a low total means access follows a relationship. So the total measures each vendor’s selling model. Investment platforms cluster low',
    'It scores each on eight things a developer with no client relationship can reach: 2 where the vendor opens it before any sale, 0 where access follows a relationship. The pattern is each vendor’s selling model. Investment platforms cluster low')
# 9 Part 3 first move
rep('I would want to test each inside BlackRock before sizing it.</p>','I would want to test each inside BlackRock before sizing it. I would start with the RFP answer: it reuses what Part 1 already assembled and has the clearest measure.</p>')
# 10 Finding 3 headline
rep('<h2>3. Aladdin’s AI works only inside the login; data providers let outside AI tools reach their data</h2>','<h2>3. Aladdin’s AI answers inside the login; data providers let outside AI tools reach their data</h2>')
# 11 Finding 3 callout
rep('I would describe the Copilot plugin model publicly now: production Aladdin APIs, the same ones Studio exposes, each user’s own permissions, and tested no-advice guardrails','A public account of the Copilot plugin model would cover production Aladdin APIs, the same ones Studio exposes, each user’s own permissions, and tested no-advice guardrails')
rep('That description answers three governance questions','That account answers three governance questions')
# 12 Exhibit 16 Copilot row
rep('BlackRock has the deepest implementation and a job posting (Finding 3)','BlackRock has a working implementation behind the login and a job posting (Finding 3)')
open(p,'w',encoding='utf-8').write(s); print('applied')
