import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def cut(start,end_marker,inclusive=True):
    global s
    assert s.count(start)==1,(s.count(start),start[:60]); i=s.index(start); j=s.index(end_marker,i)
    if inclusive: j+=len(end_marker)
    b=s[i:j]; s=s[:i]+s[j:]; return b
# definition sentence + Woodhead quote (ends right before the trade lead-in)
B_def=cut('<p>BlackRock’s own definition of Studio comes from the head of Studio engineering','<p class="lead-in">Exhibit 4 follows one trade',inclusive=False)
assert B_def.rstrip().endswith('</div>'),B_def[-80:]
# speakers block: from the pulled paragraph to the end of Exhibit 9
i=s.index('<p>I pulled 128 recordings'); j=s.index('</figure>\n', s.index('id="exhibit-9"'))+len('</figure>\n')
B_speak=s[i:j]; s=s[:i]+s[j:]
assert 'id="exhibit-9"' in B_speak and 'id="exhibit-8"' in B_speak
old=' Exhibit 8 lists each speaker with the title the recording gives.</p>\n'
assert B_speak.count(old)==1
pulled_end=B_speak.index(old)+len(old)
pulled=B_speak[:pulled_end].replace(old,'</p>\n')
rest=B_speak[pulled_end:]
B_new=('<h3>What Studio is</h3>\n'+pulled+B_def+'<p>Exhibit 8 lists each speaker with the title the recording gives.</p>\n'+rest)
anchor='<h3>What BlackRock sells</h3>\n'; assert s.count(anchor)==1
s=s.replace(anchor,B_new+anchor,1)
a='Gives the three-part definition quoted at the start of Part 1.'; assert s.count(a)==1
s=s.replace(a,'Gives the three-part definition quoted above.')
m={8:3,9:4,3:5,4:6,5:7,6:8,7:9}
def f(mo):
    n=int(mo.group(2)); return mo.group(1)+str(m.get(n,n))
s=re.sub(r'(id="exhibit-|href="#exhibit-)(\d+)',f,s)
s=re.sub(r'(Exhibit )(\d+)\b',f,s)
open(p,'w',encoding='utf-8').write(s); print('moved')
t=re.sub(r'<[^>]+>','',s)
for ph in ['Exhibit 6 follows one trade','Exhibit 9 counts them','Exhibit 1 follows a prospect','Exhibit 2 puts Studio','as in Exhibit 9','Exhibit 3 lists each speaker','Exhibit 4. All four speakers','Exhibit 3. Five BlackRock','Exhibit 5. Of Aladdin','Exhibit 8. Six pieces','Exhibit 9. Two domains','Exhibit 7. Apps']:
    print(ph,t.count(ph))
# order of exhibit titles
print(re.findall(r'Exhibit (\d+)\.',t))
