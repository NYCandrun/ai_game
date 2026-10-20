import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
# 1. extract the limits block: from the h3 through the Exhibit 2 commentary paragraph
i=s.index('<h3>What I could not see</h3>\n'); j=s.index('<p>Exhibit 2 puts Studio beside'); j=s.index('</p>\n',j)+len('</p>\n')
limits=s[i:j]; s=s[:i]+s[j:]
limits=limits.replace('<h3>What I could not see</h3>\n','',1)
# 2. extract the "What Studio is" block: from its h3 to just before "What BlackRock sells"
i=s.index('<h3 style="break-before:page">What Studio is</h3>\n'); j=s.index('<h3>What BlackRock sells</h3>\n')
studio=s[i:j]; s=s[:i]+s[j:]
studio=studio.replace('<h3 style="break-before:page">What Studio is</h3>\n','<h3>What Studio is</h3>\n',1)
# 3. insert "What Studio is" after the "What BlackRock sells" block, i.e. at the end of Part 1 (before its </section>)
k=s.index('<section class="chapter finding" id="f1">'); k=s.rindex('</section>',0,k)
s=s[:k]+studio+s[k:]
# 4. Part 4 after Part 3
part4='<section class="chapter part" id="part-4">\n<h2><span class="pn">Part 4</span>What I could not see</h2>\n'+limits+'</section>\n\n'
rep('</section>\n\n<section class="fullpage back">','</section>\n\n'+part4+'<section class="fullpage back">')
# 5. cover card and grid
rep('<p class="pt"><a href="#part-3">Directions to explore</a></p><p class="pc">Page 15</p></div>',
    '<p class="pt"><a href="#part-3">Directions to explore</a></p><p class="pc">Page 15</p></div>\n    <div><span class="accent-bar"></span><p class="pn">Part 4</p><p class="pt"><a href="#part-4">What I could not see</a></p><p class="pc">Page 16</p></div>')
rep('.cover .parts{position:absolute; left:82pt; right:82pt; top:520pt; display:grid;\n  grid-template-columns:repeat(3,1fr); column-gap:22pt}',
    '.cover .parts{position:absolute; left:82pt; right:82pt; top:520pt; display:grid;\n  grid-template-columns:repeat(4,1fr); column-gap:16pt}')
rep('  .cover .parts{grid-template-columns:repeat(3,1fr); column-gap:22px}','  .cover .parts{grid-template-columns:repeat(4,1fr); column-gap:16px}')
# 6. renumber exhibits
m={5:1,6:2,7:3,8:4,9:5,3:6,4:7,10:8,11:9,12:10,13:11,14:12,15:13,16:14,1:15,2:16}
def f(mo):
    n=int(mo.group(2)); return mo.group(1)+str(m.get(n,n))
s=re.sub(r'(id="exhibit-|href="#exhibit-)(\d+)',f,s)
s=re.sub(r'(Exhibit )(\d+)\b',f,s)
open(p,'w',encoding='utf-8').write(s); print('reordered')
t=re.sub(r'<[^>]+>','',s)
print(re.findall(r'Exhibit (\d+)\.',t))
for ph in ['Exhibit 15 follows a prospect','Exhibit 16 puts Studio','Exhibit 6 lists each','Exhibit 2 follows one trade','Exhibit 5 counts them','as in Exhibit 5','Exhibit 12 lists what the providers']:
    print(ph,t.count(ph))
