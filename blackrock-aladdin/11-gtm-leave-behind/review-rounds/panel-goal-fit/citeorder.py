import re,sys,subprocess
S="/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad"
p=sys.argv[1]
def sort_sups(h):
    def fix(m):
        inner=m.group(1)
        links=re.findall(r'<a href="#s\d+">\d+</a>',inner)
        assert ', '.join(links)==inner, inner
        links.sort(key=lambda a:int(re.search(r'>(\d+)<',a).group(1)))
        return '<sup class="fnref">'+', '.join(links)+'</sup>'
    return re.sub(r'<sup class="fnref">(.*?)</sup>',fix,h)
for it in range(5):
    h=open(p,encoding="utf-8").read(); h2=sort_sups(h); open(p,"w",encoding="utf-8").write(h2)
    out=subprocess.run(["python3","-I",S+"/gtm/renumber.py",p],capture_output=True,text=True)
    assert out.returncode==0,out.stderr
    n=int(re.search(r'entries renumbered: (\d+)',out.stdout).group(1)); print("pass",it,"renumbered",n)
    h=open(p,encoding="utf-8").read()
    if n==0 and sort_sups(h)==h: break
# flatten register into one list in numeric order
h=open(p,encoding="utf-8").read()
a=h.index('<div class="register">'); b=h.index('</div>\n</section>',a)
reg=h[a:b]
entries=re.findall(r'<p id="s\d+">.*?</p>\n',reg,flags=re.S)
assert len(entries)==71,len(entries)
entries.sort(key=lambda e:int(re.match(r'<p id="s(\d+)"',e).group(1)))
assert [int(re.match(r'<p id="s(\d+)"',e).group(1)) for e in entries]==list(range(1,72))
h=h[:a]+'<div class="register">\n'+''.join(entries)+h[b:]
old="Sources are numbered in the order they are first cited, then grouped into three grades, so the numbers within a group are not consecutive. P is a primary document."
assert h.count(old)==1
h=h.replace(old,"Sources are numbered in the order they are first cited. The letter after each number gives its grade. P is a primary document.")
open(p,"w",encoding="utf-8").write(h)
sups=re.findall(r'<sup class="fnref">(.*?)</sup>',h)
bad=[s for s in sups if [int(x) for x in re.findall(r'>(\d+)</a>',s)]!=sorted(int(x) for x in re.findall(r'>(\d+)</a>',s))]
print("unsorted superscripts:",len(bad)); print("h3 left in register:",h[a:a+len(reg)].count('<h3>'))
