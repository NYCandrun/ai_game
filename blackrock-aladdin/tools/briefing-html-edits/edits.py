import re, sys, shutil
B='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
SRC=B+'/htmlrev/src/briefing_original.html'
OUT=B+'/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.html'
s=open(SRC,encoding='utf-8').read()
head_end=s.index('</head>')+len('</head>')
HEAD=s[:head_end]
log=[]
def rep(old,new,n=1,note=''):
    global s
    c=s.count(old)
    if c!=n:
        print('MISMATCH (%d found, %d expected): %s' % (c,n,old[:90])); sys.exit(1)
    s=s.replace(old,new)
    log.append(note or old[:60])

# ---------- URLs ----------
U_WOODHEAD='https://www.youtube.com/watch?v=Me_H_-E6lSg'
U_GOEL='https://www.blackrock.com/aladdin/discover/expertise/webinars/data-as-a-strategic-assets-for-pensions'
U_RL='https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management'
U_BNP='https://www.blackrock.com/aladdin/discover/podcast/bnp-paribas-asset-management-case-study'
U_KHARA='https://www.blackrock.com/aladdin/discover'
U_BVB='https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions'
U_MS2='https://www.blackrock.com/aladdin/discover/podcast/microsoft-part-2-podcast'
U_MS1='https://www.blackrock.com/aladdin/discover/podcast/microsoft-part-1-podcast'
U_SKINNER='https://www.blackrock.com/aladdin/discover/podcast/renovating-the-house-reimagining-operating-models-podcast-episode'
U_PEMM='https://www.blackrock.com/aladdin/discover/podcast/reducing-time-to-insight-how-ai-is-reshaping-risk-management'
U_SOMA='https://www.blackrock.com/aladdin/discover/podcast/trading-market-structure-and-anacott-steel-with-aviva-investors-podcast-episode'
U_LANG='https://www.youtube.com/watch?v=oyqeCHFM5U4'
U_MILLER='https://www.youtube.com/watch?v=3iXd7a7_F6g'
U_BLQ='https://www.blackrock.com/aladdin/discover/expertise/big-little-questions'
U_GIR='https://www.blackrock.com/aladdin/discover/podcast/global-insurance-report-podcast-episode'
U_ACF='https://www.blackrock.com/aladdin/discover/expertise/events/aladdin-client-forum-2026'
U_APAC='https://www.blackrock.com/aladdin/discover/expertise/events/apac-aladdin-client-forum-recap-2025'
U_NEWMAN='https://www.blackrock.com/aladdin/discover/podcast/snowflake-podcast-data-the-key-ingredient'
U_SLC='https://www.blackrock.com/aladdin/discover/podcast/slc-management-podcast-episode'
U_TCW='https://www.blackrock.com/aladdin/discover/podcast/built-to-scale-part-2-podcast-episode'
U_UPP='https://www.blackrock.com/aladdin/discover/podcast/where-trusted-data-meets-investment-innovation-upp'
U_INGKA='https://www.blackrock.com/aladdin/discover/podcast/ingka-podcast-episode'
U_HELV='https://www.blackrock.com/aladdin/discover/client-story/client-testimonials-helvetia'
U_INTESA='https://www.blackrock.com/aladdin/discover/podcast/intesa-sanpaolo-podcast-episode'
U_NORTH='https://www.blackrock.com/aladdin/discover/podcast/northstar-group-podcast-episode'
U_EFRONT='https://www.efront.com/en/resources/client-testimonial-videos'
U_POD='https://www.blackrock.com/aladdin/discover/podcast/engineering-story-podcast-episode'
U_WHOLE='https://www.blackrock.com/aladdin/discover/expertise/webinars/unifying-the-whole-portfolio-across-public-and-private-markets'
U_FIVETRAN='https://www.fivetran.com/blog/how-fivetran-helps-power-blackrocks-aladdin-data-cloud'
U_SDKREADME='https://github.com/blackrock/aladdinsdk'
U_PLUGINS='https://github.com/blackrock/aladdinsdk-plugin-builder'
U_STUDIO='https://www.blackrock.com/aladdin/platforms/products/aladdin-studio'
U_AIREPORT='https://www.blackrock.com/aladdin/discover/report/ai-in-investment-management'
U_WATERS2023='https://waterstechnology.com/node/7951367'
U_FINK='https://www.blackrock.com/corporate/investor-relations/larry-fink-annual-chairmans-letter'
U_PREQINPC='https://www.preqin.com/about/press-release/blackrock-aladdin-expands-private-credit-solutions-on-preqin-for-greater-transparency-and-insights-across-the-asset-class'

# ================= COVER / META =================
rep('Prepared for <strong>Jacob Nikolau</strong>&emsp;|&emsp;As of October 8, 2026</p>',
    'Prepared for <strong>Jacob Nikolau</strong>&emsp;|&emsp;As of October 8, 2026&emsp;|&emsp;Revised October 19, 2026</p>',
    note='cover meta revision line')
rep('<p class="indep">Independent interview preparation compiled from public sources and the candidate’s own notes. It was not produced, reviewed or endorsed by BlackRock.</p>\n</section><section class="contents"',
    '<p class="indep">Independent interview preparation compiled from public sources and the candidate’s own notes. It was not produced, reviewed or endorsed by BlackRock. Text as of October 8, 2026; revised October 19, 2026 after a fact-check against BlackRock’s public API specifications, product pages, press releases, job postings and about 120 transcripts of its talks and podcasts.</p>\n</section><section class="contents"',
    note='cover indep revision sentence')
# contents list: add verification notes chapter
rep('<li class=""><span class="n">B</span><span><a href="#appendix-b-key-sources">Key sources</a></span><span class="pg">72</span></li></ul>',
    '<li class=""><span class="n">B</span><span><a href="#appendix-b-key-sources">Key sources</a></span><span class="pg">72</span></li><li class=""><span class="n"></span><span><a href="#verification-notes-for-this-revision">Verification notes for this revision</a></span><span class="pg">75</span></li></ul>',
    note='toc: verification notes row')
rep('<li><span class="n">B</span><span><a href="#appendix-b-key-sources">Key sources</a></span><span class="pg">72</span></li></ul>\n</section><section class="chapter" id="appendix-a-evidence-notes-and-caveats">',
    '<li><span class="n">B</span><span><a href="#appendix-b-key-sources">Key sources</a></span><span class="pg">72</span></li><li><span class="n"></span><span><a href="#verification-notes-for-this-revision">Verification notes for this revision</a></span><span class="pg">75</span></li></ul>\n</section><section class="chapter" id="appendix-a-evidence-notes-and-caveats">',
    note='appendices divider: verification notes row')
# back page
rep('<p>Facts are as of October 8, 2026, unless a table gives another date. ',
    '<p>Facts are as of October 8, 2026, unless a table gives another date. The text was revised on October 19, 2026 after a fact-check against BlackRock’s public API specifications, product pages, press releases, job postings and about 120 transcripts of its talks and podcasts; the changes are listed in the verification notes at the end. ',
    note='back page revision sentence')

# ================= SUMMARY =================
rep('and BlackRock has never named a Studio reference client. BlackRock is hiring a full developer team to close these gaps, including this role.</p>',
    'and BlackRock has not named a client as building on Studio’s APIs or SDK. The nearest thing is <a href="'+U_RL+'">Royal London’s chief executive crediting the Snowflake implementation in its Aladdin programme</a>, in a BlackRock client video. BlackRock is hiring a full developer team to close these gaps, including this role.</p>',
    note='summary point 5')

# ================= 2. EXHIBIT 5: risk factors =================
rep('Aladdin Risk uses more than 5,000 risk factors across public and private markets.',
    'Aladdin Risk uses thousands of risk factors across public and private markets; the only public figure above 3,000 is <a href="'+U_FIVETRAN+'">a 2024 Fivetran write-up with BlackRock</a> that says Aladdin “monitors over 5,000 risk factors daily,” so cite that source if using the 5,000.',
    note='ex5 risk factors')
rep('<div class="notes" id="u68"><p>Source: BlackRock Aladdin product and Studio pages; client press releases, 2021 to 2026.</p></div>',
    '<div class="notes" id="u68"><p>Source: BlackRock Aladdin product and Studio pages; client press releases, 2021 to 2026; Fivetran customer write-up with BlackRock, August 2024 (risk factor count).</p></div>',
    note='ex5 notes')

# ================= 3. WHO THE CUSTOMERS ARE =================
# insurers row: add Anderson scale quote
old=re.search(r'(<tr id="u74">\n<td class="first">Insurers</td>\n<td>.*?)(</td>\n</tr>)',s,re.S)
assert old
ins=old.group(1)
assert 'bought in 2021' in ins
rep(ins+old.group(2),
    ins+' On scale, BlackRock’s Georgette Anderson said <a href="'+U_BLQ+'">in a Big Little Questions video</a>: “we have roughly about 500 billion of insurance asset management on the system and 6 trillion of insurance assets that are actually processed through Aladdin.”'+old.group(2),
    note='s3 insurer scale quote')

# Exhibit 6: citizen developers row
rep('''<tr id="u93">
<td class="first">About 2024</td>
<td><a href="https://www.citisoft.com/insights/blog/solutions-market-perspective-series-sudhir-nair-blackrock">“Over 2,000 citizen developers”</a><sup class="fnref" id="fr-ex6-2000"><a href="#fn-ex6-2000">12</a></sup></td>
<td>Studio users, including BlackRock’s own staff</td>
</tr>''',
'''<tr id="u93">
<td class="first">2024 to 2026</td>
<td>3,000 citizen developers</td>
<td>BlackRock-internal headcount, not a count of Studio clients. Dave Woodhead, Head of Aladdin Studio Engineering, <a href="'''+U_WOODHEAD+'''">on Snowflake’s Data Cloud podcast</a>: “inside of BlackRock we have 3,000 citizen developers” and business engineers, adding “I think that number has probably peaked.” Diwakar Goel, Global Head of Data, <a href="'''+U_GOEL+'''">on a BlackRock pensions webinar</a>: “we have 3,000 people who qualify in this bracket today.”</td>
</tr>''', note='ex6 citizen developer row')
rep('<p><span id="fn-ex6-2000"><b>12</b>From an undated Citisoft interview with Sudhir Nair, Global Head of Aladdin, likely from around 2024. The figure includes BlackRock’s own staff.</span><span id="fn-ex6-faq">',
    '<p><span id="fn-ex6-faq">', note='drop fn 12 (Nair citisoft)')
rep('<p id="m13-3-who-the-customers-are">Source: BlackRock annual reports, investor days, earnings calls and job postings. The higher counts',
    '<p id="m13-3-who-the-customers-are">Source: BlackRock annual reports, investor days, earnings calls and job postings; Snowflake Data Cloud podcast with Dave Woodhead; BlackRock webinar “Data as a strategic asset for pensions.” The higher counts',
    note='ex6 notes')

# Exhibit 8: featured clients sub-table
rep('''<td>First user of Aladdin on AWS</td>
<td>Dec 2025</td>
<td>AWS joint release</td>
</tr>
</tbody>
</table><div class="notes" id="u158"><p>Source: Company filings on SEC EDGAR; pension board materials; UK Find a Tender notices; GPIF procurement disclosure; BlackRock and client press releases; trade press.</p></div></figure>''',
'''<td>First user of Aladdin on AWS</td>
<td>Dec 2025</td>
<td>AWS joint release</td>
</tr>
</tbody>
</table><p class="ex-sub" id="u157a">Featured in BlackRock-published podcasts or videos</p><p class="ex-legend">These clients appear in BlackRock’s own podcasts, client-story videos and eFront testimonial videos. A client speaking on the vendor’s channel is weaker evidence than a filing but stronger than a job posting. None of them describes building on Studio’s APIs or SDK.</p><table>
<thead>
<tr>
<th>Client</th>
<th>What it uses</th>
<th class="col-date">When</th>
<th>Evidence</th>
</tr>
</thead>
<tbody>
<tr>
<td class="first"><a href="'''+U_INTESA+'''">Intesa Sanpaolo</a> (bank)</td>
<td>Aladdin</td>
<td>Mar 2024</td>
<td>BlackRock client podcast</td>
</tr>
<tr>
<td class="first"><a href="'''+U_SLC+'''">SLC Management</a> (Sun Life; insurer-owned asset manager)</td>
<td>Aladdin; the episodes are about data transformation and do not mention Data Cloud, Snowflake, Studio or APIs</td>
<td>Feb 2024; Mar 2026</td>
<td>BlackRock podcasts</td>
</tr>
<tr>
<td class="first"><a href="'''+U_SOMA+'''">Aviva Investors</a></td>
<td>Aladdin; its global head of trading on trading data architecture</td>
<td>Dec 2025</td>
<td>BlackRock podcast</td>
</tr>
<tr>
<td class="first"><a href="'''+U_TCW+'''">TCW</a></td>
<td>Aladdin; its global COO on AI and time to insight</td>
<td>Jul 2026</td>
<td>Never Done podcast</td>
</tr>
<tr>
<td class="first"><a href="'''+U_UPP+'''">University Pension Plan Ontario (UPP)</a></td>
<td>Aladdin; its CIO on the Canadian pension model</td>
<td>Sep 2026</td>
<td>BlackRock podcast</td>
</tr>
<tr>
<td class="first"><a href="'''+U_INGKA+'''">Ingka Investments</a> (IKEA)</td>
<td>Aladdin for its financial markets portfolio</td>
<td>Dec 2024</td>
<td>BlackRock podcast</td>
</tr>
<tr>
<td class="first"><a href="'''+U_HELV+'''">Helvetia</a> (Swiss insurer)</td>
<td>Aladdin; its asset management CTO on portfolio management</td>
<td>Undated</td>
<td>BlackRock client-story video</td>
</tr>
<tr>
<td class="first"><a href="'''+U_NORTH+'''">Northstar</a></td>
<td>Aladdin</td>
<td>May 2024</td>
<td>BlackRock client podcast</td>
</tr>
<tr>
<td class="first"><a href="'''+U_EFRONT+'''">APG, Allianz Capital Partners, Velliv, Mizuho, Bouwinvest, Meridiam, Brown Brothers Harriman, Alter Domus</a></td>
<td>eFront</td>
<td>Undated</td>
<td>eFront client testimonial videos</td>
</tr>
</tbody>
</table><div class="notes" id="u158"><p>Source: Company filings on SEC EDGAR; pension board materials; UK Find a Tender notices; GPIF procurement disclosure; BlackRock and client press releases; trade press; BlackRock’s Aladdin Client Stories and Never Done podcasts, client-story videos and eFront videos.</p></div></figure>''',
    note='ex8 featured clients sub-table')

# Royal London, section 3
rep('<li><strong><a href="https://www.blackrock.com/aladdin/discover/press-release/royal-london-asset-management-press-release">Royal London Asset Management (March 2024).</a></strong> Its chief operating officer described Aladdin as its new investment platform and Snowflake as the base of its new cloud data platform. He called the program the largest and most complicated the firm had ever run.</li>',
    '<li><strong><a href="'+U_RL+'">Royal London Asset Management (BlackRock client video, November 2024).</a></strong> Its chief executive, Hans Georgeson, said the programme was delivered by three organisations, Royal London, Aladdin and HSBC, and that “we are genuinely in a minority of organisations that achieved it largely on time, if not ahead of plan, and we came in under budget.” He said the client experience “in the past was multiple order management systems” and that the move allows “a single client statement,” and he credited the data side: “the implementation of Snowflake that we did as part of the overall programme has been really successful.” He gave no duration and did not call it the firm’s largest programme.</li>',
    note='s3 Royal London CEO remarks')

# ================= 4. COSTS: CalPERS note =================
rep('The two documents may describe different contracts. Read both before citing either.</p></div></figure>',
    'The two documents may describe different contracts. Read both before citing either. Revision note: the two CalPERS figures come from different sources (board materials of November 2021 and a finance item of November 2025) and need reconciling before either is used in an interview.</p></div></figure>',
    note='ex11 CalPERS revision note')

# ================= 5. REPLACES =================
rep('BNP Paribas Asset Management retired more than 60 applications when it moved to Aladdin. <a href="https://www.sec.gov',
    'BNP Paribas Asset Management decommissioned <a href="'+U_BNP+'">“more than 60 applications”</a> in its 2016 to 2020 “Back in the Race” programme, which put Aladdin in the front-to-back chain alongside Salesforce for CRM and a DataHub, so the 60 belong to the whole programme rather than to Aladdin alone. <a href="https://www.sec.gov',
    note='s5 BNP lede')
rep('<li><strong>Royal London Asset Management</strong> <a href="https://www.blackrock.com/aladdin/discover/press-release/royal-london-asset-management-press-release">said its move took over two years</a> and was the largest and most complicated program the firm had ever run.</li>',
    '<li><strong>Royal London Asset Management’s</strong> chief executive <a href="'+U_RL+'">said in a BlackRock client video</a> that the programme came in “largely on time, if not ahead of plan, and we came in under budget,” replacing “multiple order management systems” with one platform run with HSBC. No duration has been published, and the video does not call it the firm’s largest programme.</li>',
    note='s5 switching costs Royal London')
# Exhibit 16 rows
rep('''<td class="first"><a href="https://www.blackrock.com/aladdin/discover/press-release/royal-london-asset-management-press-release">Royal London AM</a></td>
<td>Moved two order systems, reportedly thinkFolio and Murex, onto Aladdin in December 2023<sup class="fnref" id="fr-ex16-rl"><a href="#fn-ex16-rl">42</a></sup></td>''',
'''<td class="first"><a href="'''+U_RL+'''">Royal London AM</a></td>
<td>Replaced “multiple order management systems” with Aladdin, live by December 2023; its chief executive says the programme came in largely on time and under budget. Trade press named the old systems as thinkFolio and Murex; BlackRock’s own video does not name them<sup class="fnref" id="fr-ex16-rl"><a href="#fn-ex16-rl">42</a></sup></td>''',
    note='ex16 Royal London row')
rep('<span id="fn-ex16-rl"><b>42</b>BlackRock’s March 2024 release confirms the move but names neither system. The TRADE reported in July 2024',
    '<span id="fn-ex16-rl"><b>42</b>BlackRock’s November 2024 client video and its March 2024 release confirm the move but name neither system. The TRADE reported in July 2024',
    note='fn42 reword')
rep('<td class="first">BNP Paribas AM</td>\n<td>Retired more than 60 applications<sup class="fnref" id="fr-ex16-bnp">',
    '<td class="first"><a href="'+U_BNP+'">BNP Paribas AM</a></td>\n<td>Decommissioned more than 60 applications across its 2016 to 2020 programme, which covered Aladdin front to back, Salesforce for CRM and a DataHub<sup class="fnref" id="fr-ex16-bnp">',
    note='ex16 BNP row')
rep('<span id="fn-ex16-bnp"><b>43</b>From interviews, not a filing or release. The firm’s chief technology officer said “more than 60” on a BlackRock client podcast in February 2023. A 2019 DigFin interview with another executive gave 57.</span>',
    '<span id="fn-ex16-bnp"><b>43</b>The firm’s chief technology officer said “more than 60” on BlackRock’s own client podcast in February 2023, for the whole 2016 to 2020 programme. A 2019 DigFin interview with another executive gave 57.</span>',
    note='fn43 reword')

# ================= 6. COMPETITORS =================
rep('<a href="https://www.blackrock.com/aladdin/discover/report/ai-in-investment-management">BlackRock’s own 2026 survey with Forrester of 303 senior decision-makers</a> found that 68% of their organizations favor core platforms plus their own builds.</p>',
    '<a href="'+U_AIREPORT+'">BlackRock’s own 2026 AI adoption report</a> is based on a survey of 303 investment firms. The figure of “68% favor core platforms plus their own builds,” used in the earlier draft of this guide, could not be verified against the report; it appears to fuse the report’s sample size with <a href="'+U_WHOLE+'">a separate BlackRock webinar finding</a> that 68% of surveyed investors call a single view across public and private holdings crucial. Treat it as unconfirmed until checked against the report itself. BlackRock’s own Build vs Buy webinar gives a better-sourced reading of the same question.</p>'
    '<figure class="exhibit" id="exhibit-20a"><p class="ex-title"><span class="ex-num">Exhibit 20A.</span> Webinar attendees said maintenance eats 60 to 70% of their technology budgets and most want a core platform plus their own builds</p><table>\n<thead>\n<tr>\n<th>Finding</th>\n<th>What was said</th>\n</tr>\n</thead>\n<tbody>\n'
    '<tr>\n<td class="first">Where firms sit today (live audience poll)</td>\n<td><a href="'+U_BVB+'">“mostly built in house at about 15%,” “actively reevaluating at 18%,” “hybrid second most at 30 and then mostly vendor platforms at 37%”</a></td>\n</tr>\n'
    '<tr>\n<td class="first">Cost of maintenance</td>\n<td>“if you have 60 to 70% of your tech organisation focused on keeping the lights on, well, then you can’t deploy that engineering capacity to go build that differentiation”</td>\n</tr>\n'
    '<tr>\n<td class="first">Top driver for re-evaluating (poll)</td>\n<td>“AI and data demands at 42%, an exact tie between cost and speed to market. And last place was regulatory complexity”</td>\n</tr>\n'
    '<tr>\n<td class="first">What firms most want to stop maintaining (poll)</td>\n<td>“compliance reporting is number one at 53% followed by position and cash management 22%, trade life cycle at 17 and finally risk infrastructure at 9%”</td>\n</tr>\n'
    '<tr>\n<td class="first">Migration timing</td>\n<td>“12 to 18 months is what we see most regularly,” with return on investment arriving some months after go-live as roles settle</td>\n</tr>\n'
    '<tr>\n<td class="first">What RFPs now ask</td>\n<td>“what’s the API suite that you have? Are you using connectors to Snowflake or to Databricks? And I think that part of the RFP has become much more prominent”</td>\n</tr>\n'
    '<tr>\n<td class="first">Closing argument</td>\n<td>“maintaining plumbing or functions that are solved or commoditized may not be the best source of generating alpha, generating differentiation”</td>\n</tr>\n'
    '</tbody>\n</table><div class="notes"><p>Source: <a href="'+U_BVB+'">BlackRock Build vs Buy webinar replay</a>, with Michael Campos and Alisha Sewdass of Aladdin and Clark Schafer of Alpha FMC. Quotations are verbatim from the replay. The poll is of the webinar’s audience, not a representative survey.</p></div></figure>',
    note='s6 68% unconfirmed + Exhibit 20A')
rep('<td><a href="https://waterstechnology.com/node/7951367">Best overall buy-side provider and best IBOR in 2023</a>; <a href="https://waterstechnology.com/node/7952071">in 2024 Bloomberg won best overall</a> and SimCorp won best IBOR</td>',
    '<td><a href="'+U_KHARA+'">Three Buy-Side Technology Awards in 2023: Best Overall Technology Provider, Best IBOR and Best Portfolio Analysis Tool</a>, confirmed in BlackRock’s own winner interview video; <a href="https://waterstechnology.com/node/7952071">in 2024 Bloomberg won best overall</a> and SimCorp won best IBOR</td>',
    note='ex21 awards row')

exec(open(B+'/htmlrev/work/edits2.py',encoding='utf-8').read())

# ---------- footnote renumbering ----------
refs=re.findall(r'<sup class="fnref" id="fr-([^"]+)"><a href="#fn-([^"]+)">(\d+)</a></sup>',s)
ids=[]
for a,b,n in refs:
    assert a==b,(a,b)
    if b not in ids: ids.append(b)
num={fid:i+1 for i,fid in enumerate(ids)}
def r1(m): return '<sup class="fnref" id="fr-%s"><a href="#fn-%s">%d</a></sup>'%(m.group(1),m.group(1),num[m.group(1)])
s=re.sub(r'<sup class="fnref" id="fr-([^"]+)"><a href="#fn-[^"]+">\d+</a></sup>',r1,s)
def r2(m):
    fid=m.group(1)
    if fid not in num: print('ORPHAN NOTE',fid); sys.exit(1)
    return '<span id="fn-%s"><b>%d</b>'%(fid,num[fid])
s=re.sub(r'<span id="fn-([^"]+)"><b>\d+</b>',r2,s)
notes=set(re.findall(r'<span id="fn-([^"]+)"><b>',s))
missing=[i for i in ids if i not in notes]
assert not missing, missing
assert s[:head_end]==HEAD
open(OUT,'w',encoding='utf-8').write(s)
print('ok, %d edits, %d footnotes'%(len(log),len(ids)))
