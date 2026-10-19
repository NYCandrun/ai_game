import sys,re
B='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
H=B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.html'
s=open(H,encoding='utf-8').read()
n=int(sys.argv[1]); 
for pat in sys.argv[2:]:
    for m in re.finditer(re.escape(pat),s):
        ln=s.count('\n',0,m.start())+1
        a=max(0,m.start()-n); b=min(len(s),m.end()+n)
        print(f'--- L{ln} [{pat}]\n{s[a:b]}\n')
