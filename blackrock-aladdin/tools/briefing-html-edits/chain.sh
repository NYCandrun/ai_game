set -e
B=/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad
cd $B/htmlrev/work
python3 -I edits.py
python3 -I fnfit.py fit 2>&1 | grep 'CANNOT\|pages\|---'
python3 -I fnfit.py refit 2>&1 | grep 'NOT FITTED\|<--\|pages'
python3 -I fnfit.py refit 2>&1 | grep 'NOT FITTED\|<--\|pages'
python3 -I pagenums.py | tail -3
cd /home/user/ai_game && node $B/htmlrev/tools/render_chromium.js $B/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.html $B/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.pdf >/dev/null
cd $B/htmlrev/work && echo "flags after final render: $(python3 -I fnfit.py check 2>&1 | grep -c '<--')"
python3 - <<'PY'
import pdfplumber
B='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
with pdfplumber.open(B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.pdf') as d:
    print('pages',len(d.pages))
    for i,p in enumerate(d.pages,1):
        ws=p.extract_words(); n=len(ws); bot=max([w['bottom'] for w in ws if w['bottom']<740] or [0])
        if n<120 or bot<500: print('page',i,'words',n,'last text bottom %.0f'%bot)
PY
echo CHAIN DONE
