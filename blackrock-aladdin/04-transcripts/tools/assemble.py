import os,re,json,subprocess,glob
META={
'Me_H_-E6lSg':('From Analytics To Intelligence: BlackRock\'s Journey To Data Productization','Snowflake Inc.','27:21'),
'GVa1iGck9ew':('Blackrock Aladdin Tutorial For Beginners - Portfolio Management Software Overview','Shax Finance','8:07'),
'l6jSUZ6sskc':('BlackRock Interview Q&A - Aladdin Operations, Portfolio Services & Fund Accounting Roles','CandiMentor','14:40'),
'x5huBDiCLGc':('BlackRock Aladdin Demo, Tutorial & Review | How to Use BlackRock Aladdin (2026)','James And Jenna\'s Tutorials','8:25'),
'BahCi45_BTc':('Blackrock Aladdin Explore - Intro','jas jas','14:21'),
'nFwJlw0Ut9k':('Blackrock Aladdin - Fixed Income Performance Analyst','Ryderr the cat','8:57'),
'hvjaxY-nPbA':('Bringing transparency to private markets | Preqin | BlackRock','Aladdin by BlackRock','3:29'),
'Qcc8Y6M10Xw':('Why Private Markets Are Becoming Practical for Advisors | Aladdin Wealth | iCapital','iCapital','9:11'),
'U1FUBHYIkOU':('Aladdin Asset Management Software','Aladdin SGE','1:40:28'),
'7FsKtcaaEdw':('BlackRock Spotlight: Enhanced Directory in BlackRock Aladdin | Symphony Innovate 2026','Symphony','8:24')}
ORDER=['Me_H_-E6lSg','GVa1iGck9ew','l6jSUZ6sskc','x5huBDiCLGc','BahCi45_BTc','nFwJlw0Ut9k','hvjaxY-nPbA','Qcc8Y6M10Xw','U1FUBHYIkOU','7FsKtcaaEdw']
def para(t,n=110):
    w=t.split();out=[];cur=[]
    for x in w:
        cur.append(x)
        if len(cur)>=n and x.endswith(('.','?','!')): out.append(' '.join(cur));cur=[]
    if cur: out.append(' '.join(cur))
    return '\n\n'.join(out)
idx=['# Transcripts: Aladdin videos\n','Auto-generated YouTube captions, cleaned of duplicate cue lines. Speaker changes in auto-captions appear as ">>". Captions are machine-made, so names and jargon can be mis-heard (e.g. "Black Rockck" = BlackRock, "frequence/prequin" = Preqin).\n','| # | Video | Channel | Length | Status |','|---|---|---|---|---|']
for i,vid in enumerate(ORDER,1):
    title,ch,dur=META[vid]; vtt=f'subs/{vid}.en.vtt'; status='captions unavailable (YouTube bot check / rate limit from this environment)'
    if os.path.exists(vtt):
        subprocess.run(['python3','-I','vtt2txt.py',vtt],capture_output=True)
        txt=open(f'subs/{vid}.txt').read(); status=f'transcribed, {len(txt.split()):,} words'
        safe=re.sub(r'[^A-Za-z0-9]+','_',title)[:60].strip('_')
        with open(f'transcripts/{i:02d}_{safe}.md','w') as f:
            f.write(f'# {title}\n\nChannel: {ch}  \nLength: {dur}  \nSource: https://www.youtube.com/watch?v={vid}  \nTranscript: YouTube auto-captions, cleaned.\n\n---\n\n'+para(txt)+'\n')
    idx.append(f'| {i} | {title} | {ch} | {dur} | {status} |')
open('transcripts/00_INDEX.md','w').write('\n'.join(idx)+'\n')
print('\n'.join(idx[4:]))
