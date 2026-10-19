import os,re,glob
BLQ='https://www.blackrock.com/aladdin/discover/expertise/big-little-questions'
META={
'BLQ_MSFT_2024':('Big Little Questions: What is the potential of AI in financial services? (Syril Garson, Aladdin, and Allison Nachtigal, Microsoft)',BLQ),
'BLQ_MigrationJourney':('Big Little Questions: In fintech, where does the platform end and the solution begin? (Randy Fradin, Aladdin, and Matthew Kerner, Microsoft, on the Azure migration)',BLQ),
'BLQ_Pensions':('Big Little Questions: Where is the light at the end of the tunnel for pensions? (Ultan Geraghty and Badr Bevaart)',BLQ),
'BLQ_AssetManagers':('Big Little Questions: Is efficiency a dirty word? (asset managers episode; title taken from the opening line)',BLQ),
'BLQ_ACX_2023':('Big Little Questions: In financial services, how have relationships evolved? (client service episode, 2023)',BLQ),
'BLQ_COO_CTO':('Big Little Questions: As tech evolves, how do you create better client solutions? (COO and CTO episode)',BLQ),
'BLQ_Data':('Big Little Questions: In the age of AI, what is data today?',BLQ),
'blq_accounting':('Big Little Questions: How can tech transform numbers into insightful narratives? (David Schneid and Daniel Shannon, Aladdin Accounting)',BLQ),
'BLQ_UX_2024':('Big Little Questions: How is emerging tech reshaping the user experience? (Sitija Sarkar and Yael Alpert)',BLQ),
'BLQ_SanayaKhanejaKunalKhara':('Big Little Questions: How do clients shape product development? (Kunal Khara, Global Head of Aladdin Product, and Sanaya Khaneja, Solutions Engineering)',BLQ),
'BLQ_Analytics_2024':('Big Little Questions: How are analytics reshaping how we manage risk? (Yulia Yudelevich and Michael Sternberg)',BLQ),
'BLQ_AskAladdin':('Big Little Questions: What is the role of emerging tech in financial services? (client-centric product building)',BLQ),
'whole_portfolio_promo':('View the whole portfolio: promo video','https://www.blackrock.com/aladdin/view-whole-portfolio'),
'eFrontInvestmentCafe':('eFront Investment Cafe explainer video (official)','https://www.efront.com/en/alternative-investment-software-video/efront-investment-cafe-explainer-video'),
'eFrontInsightLP':('eFront Insight LP explainer video (official)','https://www.efront.com/en/alternative-investment-software-video/efront-insight-lp-explainer-video'),
'Landscape_Ask_eFrontCopilot':('Ask eFront Copilot: product video (official)','https://www.efront.com/en/alternative-investment-software/efront-copilot'),
}
def para(t,n=110):
    w=t.split();out=[];cur=[]
    for x in w:
        cur.append(x)
        if len(cur)>=n and x.endswith(('.','?','!')): out.append(' '.join(cur));cur=[]
    if cur: out.append(' '.join(cur))
    return '\n\n'.join(out)
rows=[];n=20
for f in sorted(glob.glob('media/*.whisper.txt')):
    base=os.path.basename(f).split('.')[0]; key=next((k for k in META if base.startswith(k)),None)
    if not key: continue
    title,src=META[key]; txt=open(f).read().strip(); n+=1
    safe=re.sub(r'[^A-Za-z0-9]+','_',title.split('(')[0])[:60].strip('_')
    open(f'transcripts/{n:02d}_{safe}.md','w').write(f'# {title}\n\nSource page: {src}  \nMedia: {base}.mp4 (BlackRock CloudFront)  \nTranscript: local Whisper (base.en), machine-made; names may be mis-heard.\n\n---\n\n'+para(txt)+'\n')
    rows.append(f'| {n} | {title} | Aladdin / eFront site video | {len(txt.split()):,} words |')
idx=open('transcripts/00_INDEX.md').read().rstrip()
idx+='\n\n## Added from the link directory\n\n| # | Item | Type | Size |\n|---|---|---|---|\n'
idx+='| 11 | Never Done podcast: Data, the key ingredient (Richard Newman, Aladdin Studio, with Snowflake) | site transcript | 1,759 words |\n'
idx+='| 12 | Never Done podcast: Humans in the loop, robots on the team, part 1 (Microsoft) | site transcript | 3,025 words |\n'
idx+='| 13 | Never Done podcast: Humans in the loop, robots on the team, part 2 (Microsoft) | site transcript | 3,635 words |\n'
idx+='| 14 | eFront Copilot page with embedded video transcript | site transcript | 205 words |\n'
idx+='| 15 | Reference pages as plain text (Fivetran blog, Microsoft Ignite recap, Studio for Risk, Copilot, Wealth Auto Commentary, Whole Portfolio, BLQ descriptions) | notes | — |\n'
idx+='\n'.join(rows)+'\n'
idx+='\n## Not retrievable from this environment\n\n- YouTube: oyqeCHFM5U4 (LangChain talk on Aladdin Copilot), 3iXd7a7_F6g (Snowflake customer story), 0Bl_q4k65Vc (Tim Garbien talk), x5huBDiCLGc, BahCi45_BTc, U1FUBHYIkOU (no captions exist; audio download blocked). YouTube requires a signed-in session from this IP.\n- eFront Portfolio Monitoring video: the page loads its player from an internal app (vice01.efront.com) and exposes no media URL.\n- NVIDIA GTC session S72854: JavaScript-only page.\n- All Aladdin webinar replays: behind an Eloqua registration form.\n'
open('transcripts/00_INDEX.md','w').write(idx); print('\n'.join(rows))
