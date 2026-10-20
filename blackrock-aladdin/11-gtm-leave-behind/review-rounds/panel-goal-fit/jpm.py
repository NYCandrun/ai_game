import sys
p=sys.argv[1]; w=float(sys.argv[2]); h=open(p,encoding="utf-8").read()
def rep(old,new):
    global h
    assert h.count(old)==1,(h.count(old),old[:60]); h=h.replace(old,new)
rep('class="chart" height="111.8pt" role="img" viewbox="0 0 504 211.70" width="266.1pt"',
    f'class="chart" height="{w*211.70/504:.1f}pt" role="img" viewbox="0 0 504 211.70" width="{w:.1f}pt"')
rep('<p>None of this proof names Studio,','<p style="break-before:page">None of this proof names Studio,')
open(p,"w",encoding="utf-8").write(h); print("ok")
