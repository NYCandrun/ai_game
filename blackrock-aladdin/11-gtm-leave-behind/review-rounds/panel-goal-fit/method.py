import sys
p=sys.argv[1]; h=open(p,encoding="utf-8").read()
def rep(old,new):
    global h
    assert h.count(old)==1,(h.count(old),old); h=h.replace(old,new)
rep('<h3>What this method can and cannot do</h3>','<h3>Limitations of methodology</h3>')
rep('#executive-summary .method p{font-family:var(--font-cond); font-weight:300; font-size:8.5pt; line-height:10pt; margin:0 0 3pt}',
    '#executive-summary .method p{font-weight:400; font-size:10pt; line-height:12.5pt; margin:0 0 3pt}')
open(p,"w",encoding="utf-8").write(h); print("ok")
