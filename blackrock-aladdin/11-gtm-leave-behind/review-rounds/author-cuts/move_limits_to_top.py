import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
# 1. extract block
start='<h3>What is public before a conversation starts</h3>\n'
i=s.index(start); assert s.count(start)==1
pm='<p>Exhibit 7 puts Studio beside 10 platforms'
j=s.index(pm,i); k=s.index('</p>\n',j)+len('</p>\n')
block=s[i:k]; s=s[:i]+s[k:]
# 2. modify block
old_intro=re.search(r'<p>Exhibit 6 follows a prospect’s engineer.*?</p>\n',block).group(0)
new_intro=('<p>Everything here was read from outside the login, which limits what this document can be sure of. '
 'Exhibit 1 follows a prospect’s engineer through six steps, from first hearing about Studio to getting help. '
 'For each step it records what is public today and what a client receives after qualification. '
 'I could read the pages, unpack the specifications and read the SDK’s code. I could not run anything, open the catalog, guides, notebooks or samples, or test what a client receives; where this document describes those, it relies on what the sources say. '
 'Some gaps are gaps in the public record: no event specification, no position API, no public connector for AI tools. '
 'Gating is one selling model, not the only one, and Exhibit 2 shows how differently providers draw the line.</p>\n')
block=block.replace(start,'<h3>What I could not see</h3>\n',1).replace(old_intro,new_intro,1)
# 3. insert after Part 1 intro paragraph
anchor='<figure class="exhibit" id="exhibit-1">'; assert s.count(anchor)==1
s=s.replace(anchor, block+'<h3>What BlackRock sells</h3>\n'+anchor,1)
# 4. renumber exhibits
m={6:1,7:2,1:3,2:4,3:5,4:6,5:7}
def f(mo):
    n=int(mo.group(2)); return mo.group(1)+str(m.get(n,n))
s=re.sub(r'(id="exhibit-|href="#exhibit-)(\d+)',f,s)
s=re.sub(r'(Exhibit )(\d+)\b',f,s)
open(p,'w',encoding='utf-8').write(s); print('moved')
t=re.sub(r'<[^>]+>','',s)
print(sorted(set(re.findall(r'Exhibit \d+',t)),key=lambda x:int(x.split()[1])))
for ph in ['Exhibit 4 follows one trade','Exhibit 7 counts them','Exhibit 1 follows a prospect','Exhibit 2 puts Studio','as in Exhibit 7']:
    print(ph,t.count(ph))
