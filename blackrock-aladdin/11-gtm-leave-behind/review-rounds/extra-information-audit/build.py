import re, html
S='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/asides/'
files=[('Cover, executive summary and Part 1 (pages 1 to 6)','out_p1_6.md'),('Part 2 (pages 7 to 11)','out_p7_11.md'),('Parts 3 and 4, and About this document (pages 12 to 15)','out_p12_15.md')]
def md(t):
    t=html.escape(t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    return t

def cite(t):
    pat=re.compile(r'(\S+) (\d{1,3}(?:(?:, | and | \.\.\. )\d{1,3})*)(?=[\.,;:\)\]]|$| and | \.\.\.)(?!\.\d)')
    def f(m):
        prev=m.group(1)
        if re.match(r"(?i)(exhibit|part|register|oauth|fix|fixes|source|sources|entry|p|page|about|the|over|of|than|at|in|by|to|and)$", prev.strip('"(')) : return m.group(0)
        if re.search(r'\d', prev): return m.group(0)
        nums=[int(x) for x in re.findall(r'\d+',m.group(2))]
        if any(n>105 for n in nums): return m.group(0)
        return prev+' [source '+', '.join(str(n) for n in nums)+']'
    t=pat.sub(f, t)
    for a,b in [('Drop [source 34, 20] and 28 from','Drop sources 34, 20 and 28 from'),('Interrupt 2025 9;','Interrupt 2025 [source 9];'),
                ('poll 1 10.','poll 1 [source 10].'),('Client Forum page 86,','Client Forum page [source 86],'),('tender 58"','tender [source 58]"'),('hallucinations 9"','hallucinations [source 9]"'),('tools\\" 9"','tools\\" [source 9]"'),('agents\\" 9"','agents\\" [source 9]"'),('Portfolio 1?\\" 9"','Portfolio 1?\\" [source 9]"'),('Copilot page 23.','Copilot page [source 23].'),('job posting 87"','job posting [source 87]"')]:
        t=t.replace(a,b)
    return t
sections=[]; counts={'CUT':0,'TRIM':0,'KEEP':0}; keeps=[]
for title,f in files:
    rows=[]
    for line in open(S+f,encoding='utf-8'):
        if not line.startswith('|') or line.startswith('|---') or line.startswith('| p |') : continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)<7: continue
        p,txt,point,why,verdict,repl,dep=cells[:7]
        v='CUT' if 'CUT' in verdict else ('TRIM' if 'TRIM' in verdict else ('KEEP' if 'KEEP' in verdict else verdict))
        if v in counts: counts[v]+=1
        if v=='KEEP': keeps.append((p,txt,why)); continue
        rows.append(f"<tr class='{v.lower()}'><td class='pg'>{md(p)}</td><td class='v v{v}'>{v}</td><td class='tx'>{md(txt)}</td><td>{md(why)}</td><td class='rep'>{md(cite(repl))}</td><td class='dep'>{md(dep)}</td></tr>")
    sections.append((title,rows))
css="""@page{size:Letter landscape;margin:0.42in 0.45in}
body{font-family:Helvetica,Arial,sans-serif;font-size:8.2pt;color:#111;line-height:1.3}
h1{font-size:15pt;margin:0 0 3pt}h2{font-size:11pt;margin:12pt 0 4pt;padding:3pt 6pt;background:#111;color:#fff}
h3{font-size:9.6pt;margin:8pt 0 3pt}p{margin:0 0 5pt}ul,ol{margin:0 0 5pt 14pt;padding:0}li{margin:0 0 2pt}
.lead{font-size:9pt;color:#333}.box{background:#fff3c4;padding:6pt 8pt;margin:4pt 0 8pt}
.dec{border:1.5px solid #111;padding:6pt 8pt;margin:0 0 8pt;break-inside:avoid}
table{width:100%;border-collapse:collapse;margin:0 0 6pt}th,td{border:1px solid #bbb;padding:3pt 4pt;vertical-align:top;text-align:left}
th{background:#eee;font-size:7.8pt}tr{break-inside:avoid}
td.pg{width:16pt;text-align:center}td.v{width:30pt;font-weight:bold;font-size:7.4pt}
td.vCUT{color:#fff;background:#c62828}td.vTRIM{color:#111;background:#ffcf33}
td.tx{width:24%}td.rep{background:#fff3c4;width:22%}td.dep{width:15%;color:#444;font-size:7.6pt}
.k td{font-size:7.6pt;color:#333}"""
out=[f"<!doctype html><html><head><meta charset='utf-8'><title>Extra information audit</title><style>{css}</style></head><body>"]
out.append(f"""<h1>Extra information in v23: what to cut</h1>
<p class='lead'>Nothing in the document has changed. This is for you to mark up.</p>
<p class='lead'>Three reviewers read every sentence, table cell and exhibit label on pages 1 to 15. The source list was not audited. The test was your test: does this serve the point of its paragraph, its section and the whole argument, not just its own sentence? Each item is marked CUT, TRIM (with clean replacement wording) or KEEP.</p>
<p class='lead'>Where a sentence is already being changed in the v24 review, they judged the proposed wording. Replacements follow your six writing rules. A "dependency" says when a cut would leave a source cited nowhere, or touch a v24 fix.</p>
<div class='box'><b>Totals:</b> {counts['CUT']} cut, {counts['TRIM']} trim and {counts['KEEP']} keep. The kept items are listed at the end, with the reason each one only looks extra.</div>
<h2>Read these first</h2>
<div class='dec'><h3>1. Errors found while auditing, which I checked myself</h3><ul>
<li><b>Source 83 does not support its sentence.</b> Page 12 cites it for "It sells Aladdin as the system it runs internally 9, 83". Source 83 is the 2019 eFront acquisition release, and it says nothing of the kind. Source 9 (Rosales: "BlackRock is the biggest user of Aladdin") supports the claim on its own. The reviewer recommends cutting the sentence anyway. If you keep it, cite only 9 and remove 83 from the source list.</li>
<li><b>Exhibit 6's note says "Three of the five transcripts are machine-made".</b> By the source list it is four: Woodhead's auto-captions, Goel, Khara and Miller. Only Newman's is a published transcript.</li>
<li><b>Exhibit 1's source line leaves out six sources its table cites:</b> 9, 16, 17, 19, 22 and 24.</li>
<li><b>Exhibit 3's source line cites Rosales "at 2:35",</b> but source 9's list of quoted times does not include it. The quote ("embedded across all of those hundred front-end applications") is at about 2:34 in the recording. Add the time to source 9, or drop the timestamps as the reviewer recommends.</li></ul></div>
<div class='dec'><h3>2. Where the audit conflicts with something you already decided</h3><ul>
<li><b>Exhibit 3's Hosting row.</b> The reviewer would cut it as off-point, which would also remove sources 35, 36 and 37. You asked for AWS to be shown as live, so I recommend <b>keeping</b> it. Your call.</li>
<li><b>Fix 50 (contract value growth without Preqin), which you chose to keep.</b> The reviewer would cut the whole "24 percent rise includes Preqin" sentence instead. Either keep it with your addition or cut both.</li>
<li><b>Fix 58 (Studio Compute naming) and fix 61 (Spaces), which you chose to keep.</b> The reviewer would trim Exhibit 4's workspace panel to the credentials line only. That would remove both, along with five other workspace items. Your call.</li>
<li><b>Fix 43, which you chose to cut.</b> The reviewer goes further and cuts the long-running-operations sentences from v23 altogether, along with the bitemporal sentences. That fits your decision.</li></ul></div>
<div class='dec'><h3>3. Larger structural cuts</h3>
<p>These change exhibits or whole paragraphs, not just words.</p><ol>
<li><b>Page 6: merge Exhibits 6 and 7 into one exhibit and drop the Miller row.</b> The same speakers are described three times on one page, and Woodhead's definition four times. This renumbers Exhibits 8 to 17 and every cross-reference to them. It also leaves source 47 cited nowhere, and fix 21 is no longer needed.</li>
<li><b>Page 8: cut the private-markets paragraph</b> from about ten sentences to two, or remove it entirely once the new Finding 2 box (fix 7) is adopted. The material that goes is the purchase dates, the 15,000 fund investments, the transaction types and HPS.</li>
<li><b>Exhibit 13: drop the third poll</b> (compliance reporting, 53 percent) and its chart panel. Nothing in the argument uses it, and fix 55's title change becomes moot.</li>
<li><b>Exhibit 4's workspace panel:</b> cut it to one line on API tokens and OAuth applications (see the conflict above).</li>
<li><b>Exhibit 8:</b> keep the chart, drop the grey 2016 integration bar, and cut the year-by-year figures from the text.</li>
<li><b>Page 12, paragraphs 3 and 4:</b> merge them into one five-sentence paragraph. They mostly repeat Parts 1 and 2: the poll, 42 percent, 70 countries, $2.0 billion, the job posting.</li>
<li><b>Page 14:</b> trim the SDK paragraph to two sentences. Cut the text under Exhibit 17 that reads the table aloud.</li>
<li><b>Page 15, About this document:</b> remove the half that repeats page 2. Keep one copy of the source-type list and one of the receipts explainer.</li>
<li><b>Direction box 2:</b> it gives no direction. Make it: "BlackRock could name Studio as the product behind 'Aladdin as a platform' when it speaks to investors." Move the investor quotes into the body.</li></ol></div>
<div class='dec'><h3>4. Effect on pending v24 fixes</h3><ul>
<li><b>No longer needed if the cuts are taken:</b> fixes 19, 21, 46, 47 and 48, and the title change in fix 55, because the text they correct is cut. Fix 55's note about respondents stays.</li>
<li><b>Fix 6:</b> two reviewers would drop the time-limit and "Compl Pending" sentence on page 12, because nothing else uses it. They would keep the "turn it off" point only on page 2, in the page 12 text and in Exhibit 14.</li>
<li><b>Fixes 8 and 14</b> add near-identical "no published connector" sentences on page 9. Keep one.</li>
<li><b>Fix 9:</b> use the Smith Garson quote once, on page 9, not in Exhibit 14 as well.</li>
<li><b>Fix 27:</b> the reviewers and your reader would drop "Disclosed because BlackRock owns more than 5 percent of JPMorgan."</li>
<li><b>Fix 52:</b> cut "Copilot's guardrails are tested daily" rather than moving it.</li>
<li><b>Sources that would be cited nowhere if every cut is taken:</b> 17, 21, 25, 27, 35, 36, 37, 47, 59, 73, 80, 82 and 83. They come out of the source list, and the rest renumber.</li></ul></div>""")
for title,rows in sections:
    out.append(f"<h2>{title}</h2><table><tr><th>p</th><th>Verdict</th><th>Text to cut or trim</th><th>Why it is extra for the overall point</th><th>Clean replacement</th><th>Dependencies</th></tr>{''.join(rows)}</table>")
out.append("<h2>Kept: items that look extra but serve the argument</h2><table class='k'><tr><th>p</th><th>Text</th><th>Why it stays</th></tr>"+"".join(f"<tr><td class='pg'>{md(p)}</td><td>{md(t)}</td><td>{md(w)}</td></tr>" for p,t,w in keeps)+"</table></body></html>")
open(S+'final/Extra_information_audit.html','w',encoding='utf-8').write(''.join(out))
print(counts, [len(r) for _,r in sections], len(keeps))
