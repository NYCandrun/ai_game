#!/usr/bin/env python3
"""Builds Aladdin_Studio_From_The_Outside.html from the Key Findings head plus a new body.
Receipts: {{r:key}} -> superscript reference, numbered in order of first citation.
          {{u:key}} -> the source URL (for href).
"""
import re, json, html, os
B = "/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad"
HEAD = open(f"{B}/gtm/key_findings_v52.html", encoding="utf-8").read().split("\n")[:531]
OUT = f"{B}/gtm/out/Aladdin_Studio_From_The_Outside.html"

# ---------------------------------------------------------------- sources
# key: (grade, title, who/publisher, date, url)
S = {
 # P: primary documents
 "studio":   ("P","Aladdin Studio product page","BlackRock","page as captured October 2026","https://www.blackrock.com/aladdin/platforms/products/aladdin-studio"),
 "apis":     ("P","Aladdin APIs product page","BlackRock","page as captured October 2026","https://www.blackrock.com/aladdin/platforms/products/apis"),
 "adc":      ("P","Aladdin Data Cloud product page","BlackRock","page as captured October 2026","https://www.blackrock.com/aladdin/products/aladdin-data-cloud"),
 "copilot":  ("P","Aladdin Copilot product page","BlackRock","page as captured October 2026","https://www.blackrock.com/aladdin/platforms/products/aladdin-copilot"),
 "pypi":     ("P","aladdinsdk, release history","PyPI","releases May 2024 to July 2026","https://pypi.org/project/aladdinsdk/#history"),
 "plugins":  ("P","asdk_plugin_* add-on packages, version 2.0.0b3 (11 packages holding 54 Swagger 2.0 specifications)","PyPI","version 2.0.0b3, unpacked October 2026","https://pypi.org/search/?q=asdk_plugin"),
 "readme":   ("P","AladdinSDK README and source, blackrock/aladdinsdk","GitHub","as of October 19, 2026","https://github.com/blackrock/aladdinsdk"),
 "builder":  ("P","aladdinsdk-plugin-builder","GitHub, blackrock","as of October 19, 2026","https://github.com/blackrock/aladdinsdk-plugin-builder"),
 "pr52":     ("P","Pull request 52, URL rewriting for enterprise API gateways, blackrock/aladdinsdk","GitHub","December 2025","https://github.com/blackrock/aladdinsdk/pull/52"),
 "pr53":     ("P","Pull request 53, additional HTTP headers, blackrock/aladdinsdk","GitHub","December 2025","https://github.com/blackrock/aladdinsdk/pull/53"),
 "pr57":     ("P","Pull request 57, dependency conflict with the MCP toolkit, blackrock/aladdinsdk","GitHub","merged August 2026","https://github.com/blackrock/aladdinsdk/pull/57"),
 "patch":    ("P","Commit 1c1bd25, raw patch, blackrock/aladdinsdk","GitHub","December 1, 2025","https://github.com/blackrock/aladdinsdk/commit/1c1bd2559e4e4da2591f13dccfd7db6c2f9dc68c.patch"),
 "contrib":  ("P","Contributors graph, blackrock/aladdinsdk","GitHub","as of October 19, 2026","https://github.com/blackrock/aladdinsdk/graphs/contributors"),
 "clientpy": ("P","aladdinsdk/api/client.py, main branch","GitHub, blackrock/aladdinsdk","as of October 19, 2026","https://github.com/blackrock/aladdinsdk/blob/main/aladdinsdk/api/client.py"),
 "engblog":  ("P","Open-sourcing the AladdinSDK: empower Python developers with a quantitative edge","BlackRock Engineering, on Medium","2024","https://engineering.blackrock.com/open-sourcing-the-aladdinsdk-empower-python-developers-with-a-quantitative-edge-7f63376061e6"),
 "jhg10k":   ("P","Janus Henderson Group, Form 10-K for fiscal year 2025","SEC EDGAR","filed 2026","https://www.sec.gov/Archives/edgar/data/1274173/000143774926005628/jhg20251231_10k.htm"),
 "jpmproxy": ("P","JPMorgan Chase proxy statements (DEF 14A), filed 2017 to 2026, related-party payments to BlackRock for Aladdin","SEC EDGAR","2017 to 2026","https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000019617&type=DEF+14A"),
 "jpm2026":  ("P","JPMorgan Chase proxy statement (DEF 14A), payments for 2025","SEC EDGAR","filed April 2, 2026","https://www.sec.gov/Archives/edgar/data/19617/000001961726000096/jpm-20260402.htm"),
 "blk10k":   ("P","BlackRock, Inc., Form 10-K for fiscal year 2025","SEC EDGAR","filed 2026","https://www.sec.gov/Archives/edgar/data/2012383/000119312526071966/blk-20251231.htm"),
 "id2025":   ("P","BlackRock 2025 Investor Day presentation","BlackRock","June 2025","https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf"),
 "id2023":   ("P","BlackRock 2023 Investor Day presentation","BlackRock","June 2023","https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BlackRock-2023-Investor-Day.pdf"),
 "edgar":    ("P","Full-text search of SEC EDGAR for “Aladdin Studio”","SEC EDGAR","run October 2026","https://www.sec.gov/edgar/search/#/q=%22Aladdin%20Studio%22"),
 "ghblk":    ("P","BlackRock organization page","GitHub","as of October 19, 2026","https://github.com/blackrock"),
 "fde":      ("P","Job posting: Forward Deploy Engineer, Aladdin Data, Associate (Mumbai)","BlackRock Careers","seen October 2026","https://careers.blackrock.com/job/mumbai/forward-deploy-engineer-aladdin-data-associate/45831/97466309856"),
 "spd":      ("P","Job posting: Senior Product Director, Aladdin Studio Developer (New York)","BlackRock Careers","seen October 2026","https://careers.blackrock.com/job/new-york/senior-product-director-aladdin-studio-developer/45831/96232273856"),
 "aws":      ("P","BlackRock partners with AWS to deliver Aladdin on secure, scalable cloud infrastructure","Amazon press release","December 2025","https://press.aboutamazon.com/aws/2025/12/blackrock-partners-with-aws-to-deliver-aladdin-on-secure-scalable-cloud-infrastructure"),
 "preqinpr": ("P","BlackRock Aladdin expands private credit solutions on Preqin","Preqin press release","May 2026","https://www.preqin.com/about/press-release/blackrock-aladdin-expands-private-credit-solutions-on-preqin-for-greater-transparency-and-insights-across-the-asset-class"),
 "wealthpr": ("P","Aladdin Wealth launches AI-enabled commentary tool at Morgan Stanley","BlackRock press release","October 2, 2025","https://www.blackrock.com/aladdin/discover/press-release/aladdin-wealth-launches-ai-enabled-commentary-tool-at-morgan-stanley"),
 "ishares":  ("P","iShares V plc prospectus (Aladdin Provider fees paid by service providers)","BlackRock","2026","https://www.blackrock.com/uk/literature/prospectus/ishares-v-plc-prospectus-en.pdf"),
 "factset":  ("P","FactSet meets demand for AI-ready data, first to announce MCP","FactSet press release","2025","https://www.factset.com/newsroom/press-release/factset-meets-demand-for-ai-ready-data-first-to-announce-mcp-sans-intermediary"),
 "lseg":     ("P","LSEG announces collaboration with Anthropic","LSEG press release","2025","https://www.lseg.com/en/media-centre/press-releases/2025/lseg-announces-collaboration-with-anthropic"),
 "msci":     ("P","MSCI unveils new AI connectors","MSCI press release","2025","https://www.msci.com/discover-msci/media-room/msci-unveils-new-ai-connectors-transforming-access-to-proprietary-data"),
 "arcesium": ("P","Arcesium unveils new suite of AI features in Aquata","Arcesium press release","2025","https://www.arcesium.com/press-release/arcesium-unveils-new-suite-of-ai-features-in-aquata"),
 "spg":      ("P","S&P Global brings Credit Ratings to the S&P Global AI Data Portal","S&P Global press release","September 28, 2026","https://press.spglobal.com/2026-09-28-S-P-Global-brings-Credit-Ratings-to-the-S-P-Global-AI-Data-Portal"),
 "snowmcp":  ("P","Cortex Agents MCP server, product documentation","Snowflake","as of October 2026","https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp"),
 "dbxmcp":   ("P","Managed MCP servers, product documentation","Databricks","as of October 2026","https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp"),
 "mcp":      ("P","Model Context Protocol specification site","modelcontextprotocol.io","as of October 2026","https://modelcontextprotocol.io/"),
 "fsdev":    ("P","FactSet developer portal","FactSet","as of October 8, 2026","https://developer.factset.com"),
 "ssdev":    ("P","State Street developer portal","State Street","as of October 8, 2026","https://developer.statestreet.com"),
 "lsegdev":  ("P","LSEG developer portal","LSEG","as of October 8, 2026","https://developers.lseg.com/en"),
 "snowdev":  ("P","Snowflake developers page","Snowflake","as of October 8, 2026","https://www.snowflake.com/en/developers/"),
 "dbxtry":   ("P","Try Databricks","Databricks","as of October 8, 2026","https://www.databricks.com/try-databricks"),
 "arcai":    ("P","Arcesium launches comprehensive AI platform","Arcesium press release","2026","https://www.arcesium.com/press-release/arcesium-launches-comprehensive-ai-platform"),
 "simagent": ("P","Introducing Agent Launchpad","SimCorp news","2026","https://www.simcorp.com/about-us/news/2026/introducing-agent-launchpad"),
 "ab":       ("P","AllianceBernstein selects SimCorp One technology platform","AllianceBernstein press release","February 2026","https://alliancebernsteinholdinglp.gcs-web.com/news-releases/news-release-details/alliancebernstein-selects-simcorp-one-technology-platform"),
 "pictet":   ("P","Pictet Asset Management selects SimCorp One","SimCorp news","May 2026","https://www.simcorp.com/about-us/news/2026/pictet-asset-management-selects-simcorp-one"),
 "bvbpage":  ("P","Build vs buy: a decision framework (insight page)","BlackRock Aladdin","August 2026","https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework"),
 "nd":       ("P","Never Done, the Aladdin podcast series page","BlackRock Aladdin","as of October 2026","https://www.blackrock.com/aladdin/discover/expertise/never-done-podcast-by-aladdin"),
 "blq":      ("P","Big Little Questions, video series page","BlackRock Aladdin","as of October 2026","https://www.blackrock.com/aladdin/discover/expertise/big-little-questions"),
 "acf":      ("P","Aladdin Client Forum 2026 event page","BlackRock Aladdin","fall 2026","https://www.blackrock.com/aladdin/discover/expertise/events/aladdin-client-forum-2026"),
 # S: BlackRock speakers on the record
 "woodhead": ("S","From Analytics To Intelligence: BlackRock’s Journey To Data Productization (Snowflake Data Cloud podcast; auto-captions)","Dave Woodhead, Managing Director and Head of Engineering for Aladdin Studio, BlackRock","published November 11, 2025","https://www.youtube.com/watch?v=Me_H_-E6lSg"),
 "newman":   ("S","Data: the key ingredient (Never Done podcast, with Snowflake; published transcript)","Richard Newman, General Manager, Aladdin Studio, BlackRock","January 8, 2025","https://www.blackrock.com/aladdin/discover/podcast/snowflake-podcast-data-the-key-ingredient"),
 "goel":     ("S","Data as a strategic asset for pensions (webinar replay; machine transcription)","Diwakar Goel, Global Head of Data, Aladdin, BlackRock","2025, page undated","https://www.blackrock.com/aladdin/discover/expertise/webinars/data-as-a-strategic-assets-for-pensions"),
 "khara":    ("S","Best Overall Technology Provider for 2023, Buy-Side Technology Awards winner interview (machine transcription)","Kunal Khara, Managing Director and Global Head of Aladdin Product, BlackRock","early 2024","https://www.blackrock.com/aladdin/discover"),
 "miller":   ("S","BlackRock transforms client data delivery with Snowflake’s Aladdin Data Cloud (Snowflake video; machine transcription)","Jeff Miller, Managing Director, Global Head of Data Platform and Product Engineering, BlackRock","undated","https://www.youtube.com/watch?v=3iXd7a7_F6g"),
 "rlam":     ("S","Shaping tomorrow with technology (Aladdin client story video; machine transcription)","Hans Georgeson, Chief Executive, Royal London Asset Management, with Tarek Chouman, Global Head of the Aladdin Client Business","recorded November 2024","https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management"),
 "langchain":("S","How BlackRock built production AI agents for asset management with LangGraph (LangChain Interrupt 2025; machine transcription)","Brennan Rosales, AI Engineering Lead, and Pedro Vicente Valdez, Principal AI Engineer, BlackRock","2025","https://www.youtube.com/watch?v=oyqeCHFM5U4"),
 "crockett": ("S","Humans in the loop, robots on the team, part 2 (Never Done podcast; published transcript)","Adrian Crockett, General Manager, Microsoft Cloud for Financial Services, with Syril Smith Garson, Head of Product for AI, BlackRock","November 6, 2024","https://www.blackrock.com/aladdin/discover/podcast/microsoft-part-2-podcast"),
 "bvb":      ("S","Build vs. buy: how asset managers are rethinking key decisions (webinar replay; published captions)","Michael Campos, US asset manager coverage, and Alisha Sewdass, Head of Aladdin Solutions Engineering, Americas, BlackRock, with Clark Schafer, Partner, Alpha FMC","replay page undated","https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions"),
 "braun":    ("S","Microsoft and Aladdin partner story (Aladdin Client Stories podcast; published transcript)","Lance Braunstein, Managing Director, Aladdin, BlackRock","March 7, 2023","https://www.blackrock.com/aladdin/discover/podcast/microsoft-podcast-episode"),
 "kharains": ("S","Bringing to life the Global Insurance Report (Aladdin Client Stories podcast; published transcript)","Kunal Khara, Global Head of Aladdin Product, BlackRock","November 3, 2023","https://www.blackrock.com/aladdin/discover/podcast/global-insurance-report-podcast-episode"),
 "kamya":    ("S","How data architecture shapes modern trading (Aladdin Client Stories podcast; published transcript)","Kamya Somasundaram, Global Head of Aladdin Partnerships and Trading Product Marketing, BlackRock","December 25, 2025","https://www.blackrock.com/aladdin/discover/podcast/trading-market-structure-and-anacott-steel-with-aviva-investors-podcast-episode"),
 "pemm":     ("S","Reducing time to insight: how AI reshapes risk management (Never Done podcast; machine transcription)","Pavan Pemmaraju, Head of AI Product and Engineering, BlackRock","July 16, 2026","https://www.blackrock.com/aladdin/discover/podcast/reducing-time-to-insight-how-ai-is-reshaping-risk-management"),
 # T: third-party reports
 "roic":     ("T","BlackRock earnings call transcripts, Q1 2020 to Q2 2026","roic.ai","2020 to 2026","https://www.roic.ai/quote/BLK/transcripts"),
 "roic4q21": ("T","BlackRock Q4 2021 earnings call transcript","roic.ai","January 2022","https://www.roic.ai/quote/BLK/transcripts/2021-year/4-quarter"),
 "roic3q22": ("T","BlackRock Q3 2022 earnings call transcript","roic.ai","October 2022","https://www.roic.ai/quote/BLK/transcripts/2022-year/3-quarter"),
 "roic4q23": ("T","BlackRock Q4 2023 earnings call transcript","roic.ai","January 2024","https://www.roic.ai/quote/BLK/transcripts/2023-year/4-quarter"),
 "roic4q24": ("T","BlackRock Q4 2024 earnings call transcript","roic.ai","January 2025","https://www.roic.ai/quote/BLK/transcripts/2024-year/4-quarter"),
 "trade":    ("T","JP Morgan to connect to BlackRock’s Aladdin","The TRADE","2016","https://www.thetradenews.com/jp-morgan-to-connect-to-blackrocks-aladdin/"),
 "investing":("T","LSEG Q1 2026 slides: record growth, AI adoption accelerates (summary of LSEG results slides)","Investing.com","April 2026","https://www.investing.com/news/company-news/lseg-q1-2026-slides-record-growth-ai-adoption-accelerates-93CH-4631412"),
}

order = []
def r(keys):
    nums = []
    for k in keys.split(","):
        k = k.strip()
        if k not in S: raise KeyError(k)
        if k not in order: order.append(k)
        nums.append(order.index(k) + 1)
    inner = ", ".join(f'<a href="#s{n}">{n}</a>' for n in nums)
    return f'<sup class="fnref">{inner}</sup>'
def u(k): return html.escape(S[k][4], quote=True)

# ---------------------------------------------------------------- API catalog
apis = json.load(open(f"{B}/apis.json"))
from collections import defaultdict
agg = defaultdict(lambda: {"specs":0,"ops":0,"alpha":0,"beta":0,"stable":0,"sunset":0,"names":[]})
for a in apis:
    g = agg[a["d"]]; g["specs"] += 1; g["ops"] += a["o"]; g[a["s"]] += 1; g["names"].append((a["o"], a["n"]))
tot = {"specs":0,"ops":0,"alpha":0,"beta":0,"stable":0,"sunset":0}
rows = []
label = {"investment_operations":"Investment operations","analytics":"Analytics","investment_research":"Investment research",
         "platform":"Platform","portfolio_management":"Portfolio management","portfolio":"Portfolio","data":"Data",
         "trading":"Trading","compliance":"Compliance","accounting":"Accounting","clients":"Clients"}
maxops = max(g["ops"] for g in agg.values())
for d, g in sorted(agg.items(), key=lambda kv: -kv[1]["ops"]):
    for t in tot: tot[t] += g[t]
    names = ", ".join(n for _, n in sorted(g["names"], key=lambda x: -x[0])[:4])
    if g["specs"] > 4: names += f" and {g['specs']-4} more"
    w = 60 * g["ops"] / maxops
    def c(v): return f'<td class="num">{v if v else "–"}</td>'
    rows.append(f'<tr><td class="first">{label[d]}</td><td class="num">{g["specs"]}</td>'
                f'<td class="opbar"><span class="bar" style="width:{w:.1f}pt"></span><b>{g["ops"]}</b></td>'
                f'{c(g["alpha"])}{c(g["beta"])}{c(g["stable"])}{c(g["sunset"])}<td class="ex">{names}</td></tr>')
assert (tot["specs"],tot["ops"],tot["alpha"],tot["beta"],tot["stable"],tot["sunset"]) == (54,301,24,6,23,1), tot
rows.append(f'<tr class="total"><td class="first">Total</td><td class="num">{tot["specs"]}</td><td class="opbar"><b>{tot["ops"]}</b></td>'
            f'<td class="num">{tot["alpha"]}</td><td class="num">{tot["beta"]}</td><td class="num">{tot["stable"]}</td><td class="num">{tot["sunset"]}</td><td class="ex">11 domains, 11 PyPI packages</td></tr>')
CATALOG_ROWS = "\n".join(rows)

# ---------------------------------------------------------------- charts
def hbar_chart(title_label, items, width=240, unit="%", maxv=None, aria=""):
    """Horizontal bars, yellow, bold value labels, in the sample's typography."""
    lw = 118; top = 6; rh = 17; bh = 10.5
    maxv = maxv or max(v for _, v in items)
    plot_w = width - lw - 30
    h = top + rh * len(items) + 16
    parts = [f'<svg aria-label="{html.escape(aria)}" class="chart" role="img" width="{width}pt" height="{h:.1f}pt" viewBox="0 0 {width} {h:.1f}" xmlns="http://www.w3.org/2000/svg">']
    y = top
    for name, v in items:
        bw = plot_w * v / maxv
        parts.append(f'<text font-size="9" text-anchor="end" x="{lw-6}" y="{y+bh-2:.1f}">{html.escape(name)}</text>')
        parts.append(f'<rect fill="#FFCE00" x="{lw}" y="{y:.1f}" width="{bw:.1f}" height="{bh}"></rect>')
        parts.append(f'<text font-size="9" font-weight="700" x="{lw+bw+4:.1f}" y="{y+bh-2:.1f}">{v}{unit}</text>')
        y += rh
    parts.append(f'<path d="M{lw} {top-2} V{y-rh+bh+2:.1f}" fill="none" stroke="#000" stroke-width="0.75"></path>')
    parts.append(f'<text font-size="9" x="{lw}" y="{h-3:.1f}" fill="#595959">{html.escape(title_label)}</text>')
    parts.append('</svg>')
    return "\n".join(parts)

CHART_POLL1 = hbar_chart("Share of attendees, poll 1", [("Mostly vendor platforms",37),("Hybrid",30),("Actively re-evaluating",18),("Mostly built in house",15)],
                         aria="Bar chart, where firms sit today: mostly vendor platforms 37 percent, hybrid 30, actively re-evaluating 18, mostly built in house 15.")
CHART_POLL3 = hbar_chart("Share of attendees, poll 3", [("Compliance reporting",53),("Position and cash management",22),("Trade lifecycle",17),("Risk infrastructure",9)],
                         aria="Bar chart, what firms would stop maintaining internally: compliance reporting 53 percent, position and cash management 22, trade lifecycle 17, risk infrastructure 9.")

# JPMorgan chart: markup reused from Key Findings Exhibit 1
kf = "\n".join(open(f"{B}/gtm/key_findings_v52.html", encoding="utf-8").read().split("\n")[531:])
m = re.search(r'<svg aria-label="Column chart of JPMorgan Chase payments.*?</svg>', kf, re.S)
JPM_SVG = m.group(0).replace('height="211.70pt"', 'height="186.3pt"').replace('width="504pt"', 'width="443.5pt"')
m = re.search(r'<table class="heat">.*?</table>', kf, re.S)
HEAT_TABLE = m.group(0)
m = re.search(r'<div class="code" data-lang="text" id="blk-15">.*?</div>', kf, re.S)
CODE_BLOCK = m.group(0).replace(' id="blk-15"', '')
m = re.search(r'<p class="code-link" id="blk-16">.*?</p>', kf, re.S)
CODE_LINK = m.group(0).replace(' id="blk-16"', '')

# ---------------------------------------------------------------- body
BODY = r'''
<style>
/* additions for this edition */
.cover .parts .pt a{text-decoration:none}
.method{background:var(--box); padding:9pt 12pt 6pt; margin:0 0 12pt; break-inside:avoid}
.method h3{margin:0 0 5pt; font-size:11pt; line-height:13.2pt}
#executive-summary .method p{font-family:var(--font-cond); font-weight:300; font-size:8.5pt; line-height:10pt; margin:0 0 3pt}
#executive-summary .method p b{font-weight:700}
.method{padding:7pt 10pt 5pt}
#executive-summary .stats{margin-bottom:2pt}
#executive-summary p{margin-bottom:10pt}
#executive-summary .label-key p{font-size:9pt; line-height:11pt; margin-bottom:6pt}
#executive-summary .key-grid{font-size:9pt; line-height:11pt}
#executive-summary p.stats-src{margin-bottom:12pt}
.key-grid{grid-template-columns:1fr 1fr 1fr}
.key-grid > div{grid-template-columns:1fr}
table td.opbar{white-space:nowrap}
table td.opbar .bar{display:inline-block; height:8pt; background:var(--yellow); vertical-align:-.5pt; margin-right:5pt}
table td.ex{font-family:var(--font-cond); font-weight:300; font-size:8.5pt; line-height:10pt}
.chapter.finding > h2{font-size:17pt; line-height:21pt}
.chapter.finding > h2::before{margin-bottom:16pt}
.gtm{border-left:3pt solid var(--yellow); padding:4pt 0 4pt 10pt; margin:4pt 0 12pt}
.gtm p{margin:0}
.gtm .lead{font-weight:700}
.notes .lbl::before{vertical-align:0}
.register{column-count:2; column-gap:20pt; font-size:7.6pt; line-height:9.2pt}
.register h3{column-span:none; font-size:9pt; line-height:10.5pt; margin:7pt 0 4pt; break-after:avoid}
.register h3:first-child{margin-top:0}
.register p{margin:0 0 3.6pt; break-inside:avoid; padding-left:16pt; text-indent:-16pt}
.register p b.n{display:inline-block; width:16pt; text-indent:0; font-weight:700}
.register p .g{font-family:var(--font-cond); font-weight:700; margin-right:3pt}
.register a{text-decoration:none; color:#595959; overflow-wrap:anywhere}
.register .t{font-weight:700}
.chk{font-weight:700}
.chapter.part > h2 .pn{display:block; font-size:10pt; line-height:12pt; font-weight:400; color:#595959; margin-bottom:3pt}
td.num.dim{color:#595959}
.chart-row .side{flex:1}
.chart-row .side .side-head{margin-top:8pt}
.exhibit .script{margin-top:4pt}
.arch .node{min-height:28pt; padding:4pt 5pt}
.arch .studio div{min-height:24pt; padding:4pt 5pt}
.arch{row-gap:6pt}
.exhibit > .ex-title{break-after:avoid}
.exhibit > .tbl-wrap, .exhibit > table{break-before:avoid}
.notes{break-before:avoid}
#executive-summary ul li{font-size:11pt; line-height:14.5pt}
</style>

<section class="fullpage cover">
  <p class="prepared-for">Prepared for BlackRock</p>
  <div class="inner">
    <span class="accent-bar"></span>
    <h1>Aladdin Studio from the outside</h1>
    <p class="subtitle">What a prospect can see today, with receipts</p>
    <p class="meta">Prepared by <strong>Jacob Nikolau</strong>&emsp;|&emsp;As of October 19, 2026</p>
  </div>
  <div class="parts">
    <div><span class="accent-bar"></span><p class="pn">Parts 1 and 2</p><p class="pt"><a href="#part-1">What Studio is, and the public surface, mapped</a></p><p class="pc">Page 3</p></div>
    <div><span class="accent-bar"></span><p class="pn">Part 3</p><p class="pt"><a href="#f1">Six findings, one page each</a></p><p class="pc">Page 8</p></div>
    <div><span class="accent-bar"></span><p class="pn">Part 4</p><p class="pt"><a href="#part-4">What I would do, and what I would need</a></p><p class="pc">Page 14</p></div>
  </div>
  <p class="indep">Independent analysis compiled from public sources. It was not produced, reviewed or endorsed by BlackRock.</p>
</section>

<section class="chapter first" id="executive-summary">
<h2>Executive summary</h2>
<p class="lede">Aladdin Studio is in use, and BlackRock has described it the same way for three years. Almost everything a developer would want, though, sits behind a client login. The gap is distribution, not positioning.</p>
<div class="stats three">
  <div><span class="accent-bar"></span><p class="num">54</p><p class="cap">Public API specifications in 11 PyPI packages, covering 301 operations</p></div>
  <div><span class="accent-bar"></span><p class="num">3,000</p><p class="cap">Citizen developers inside BlackRock writing Python or R against Aladdin, per its head of Studio engineering, 2025</p></div>
  <div><span class="accent-bar"></span><p class="num">4 of 16</p><p class="cap">Studio’s score on an eight-criterion test of what an outside developer can reach</p></div>
</div>
<p class="stats-src">Source: <a href="{{u:plugins}}">asdk_plugin packages on PyPI</a>{{r:plugins}}; <a href="{{u:woodhead}}">Dave Woodhead on the Snowflake Data Cloud podcast</a>{{r:woodhead}}; the author’s hands-on test, Exhibit 6.</p>
<p>The proof of use is outside BlackRock’s channels. JPMorgan Chase <a href="{{u:jpm2026}}">paid $25.6 million for Aladdin in 2025</a>, almost six times its 2017 level{{r:jpm2026,jpmproxy}}. A Janus Henderson engineer <a href="{{u:pr52}}">adapted the open-source SDK</a> to the firm’s API gateway, and BlackRock merged the changes{{r:pr52,pr53}}. Royal London’s chief executive credits <a href="{{u:rlam}}">the Snowflake implementation</a>{{r:rlam}}. Inside BlackRock, Woodhead counts <a href="{{u:woodhead}}">“3,000 citizen developers”</a>{{r:woodhead}}.</p>
<p>From outside, a prospect can read one <a href="{{u:studio}}">product page</a> whose calls to action are “Book a meeting” and “Download the brochure”{{r:studio}}, install an <a href="{{u:readme}}">SDK</a> that needs a client host and a Studio token before any call succeeds{{r:readme}}, and unpack <a href="{{u:plugins}}">54 specifications</a>, every one tagged <code>Access.Internal</code>{{r:plugins}}. No executive has said “Studio” on <a href="{{u:roic}}">26 earnings calls</a> since 2020{{r:roic}}, while BlackRock projects <a href="{{u:id2025}}">API calls to grow 17 times by 2030</a>{{r:id2025}}.</p>
<p>Four BlackRock speakers, from early 2024 to late 2025, describe Studio with the same three parts: APIs and events, Aladdin Data Cloud on Snowflake, and developer tools{{r:khara,newman,goel,woodhead}}. That message reaches podcasts, webinars and one page, not investors, a public developer portal, or the AI tools that seven data providers already connect to{{r:factset,lseg,msci}}. Part 4 sets out five moves for the first 90 days and the eight internal numbers needed first.</p>
<div class="label-key">
<h3>How to read the receipts</h3>
<p>Underlined text links to the document behind the fact. Each superscript points to the Source register at the back, which gives the grade, title, speaker and date. Each exhibit’s source line starts with the grade of its main source.</p>
<div class="key-grid">
<div><span class="lbl"><b>P</b> Primary document: an SEC filing, an API specification, a product page, GitHub or PyPI</span></div>
<div><span class="lbl e"><b>S</b> BlackRock speaker on the record: a recording, with the name and title as given</span></div>
<div><span class="lbl n"><b>T</b> Third-party report: trade press or a secondary summary</span></div>
</div>
</div>
<div class="method" style="margin-top:8pt">
<h3>Method</h3>
<p><b>Pulled.</b> The 54 Swagger specifications inside BlackRock’s 11 public <code>asdk_plugin</code> packages; 15 BlackRock product pages; 126 transcripts of recordings, 121 from BlackRock’s own channels and partner stages (podcasts, Big Little Questions, webinar replays, client videos, conference talks) and five third-party tutorials; SEC filings for BlackRock, JPMorgan Chase and Janus Henderson; BlackRock’s GitHub and PyPI pages.</p>
<p><b>Checked.</b> Every number was recomputed from the files or read in the cited document. Every quotation was matched to its transcript; machine transcriptions are marked in the register.</p>
<p><b>Corrected.</b> 58 specifications is 54 once the SDK’s four utility APIs are set aside. A widely repeated “68 percent” survey figure was dropped because it could not be found in the report it is attributed to. “More than 2,000 citizen developers” is 3,000, and the figure counts BlackRock staff, not clients.</p>
</div>
</section>

<section class="chapter part" id="part-1">
<h2><span class="pn">Part 1</span>What Studio is</h2>
<p>Aladdin is the investment platform BlackRock built for itself and sells to other institutions. Its AI engineering lead put the scale this way at a LangChain conference in 2025: <a href="{{u:langchain}}">“BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries”</a>; the organization is “around 7,000 people, with over 4,000 of those being engineers,” who maintain “around 100 Aladdin front-end applications”{{r:langchain}}. BlackRock’s technology services and subscription revenue was <a href="{{u:blk10k}}">$2.0 billion in 2025</a>, up 24 percent with Preqin{{r:blk10k}}. BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code.</p>

<figure class="exhibit" id="exhibit-1"><p class="ex-title"><span class="ex-num">Exhibit 1.</span> One core engine with separate entry points for each kind of buyer</p>
<table>
<colgroup><col style="width:92pt"><col><col style="width:132pt"></colgroup>
<thead><tr><th>Product</th><th>What it does</th><th>Main users</th></tr></thead>
<tbody>
<tr><td class="first">Aladdin</td><td>The front-to-back system for public markets, the same system BlackRock runs internally{{r:langchain}}</td><td>Asset managers, insurers, pension funds, banks</td></tr>
<tr><td class="first">Aladdin Wealth</td><td>Portfolio risk analysis and proposals for advisors; its AI “auto commentary” tool <a href="{{u:wealthpr}}">launched in October 2025 with Morgan Stanley first</a>{{r:wealthpr}}</td><td>Wealth managers and private banks</td></tr>
<tr><td class="first">eFront</td><td>A private fund investment from due diligence through cash flows and reporting; folded Preqin into eFront Insight, with <a href="{{u:preqinpr}}">private credit analytics added in May 2026</a>{{r:preqinpr}}</td><td>Investors in funds and fund managers</td></tr>
<tr class="focus"><td class="first">Aladdin Studio</td><td>The developer and data layer: APIs and events, a Python SDK, Aladdin Compute and Aladdin Data Cloud; <a href="{{u:studio}}">“API-first”</a>, for “a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting”{{r:studio}}</td><td>Client engineers, data analysts, code-curious portfolio managers</td></tr>
<tr><td class="first">Aladdin Data Cloud</td><td>A managed data service on Snowflake that puts Aladdin and outside data in one place; <a href="{{u:aws}}">sold as an add-on to Aladdin Enterprise</a>{{r:aws}}; Newman places it <a href="{{u:newman}}">“part of Studio”</a>{{r:newman}}</td><td>Data teams</td></tr>
<tr><td class="first">Aladdin Copilot</td><td>A chat assistant <a href="{{u:copilot}}">“now available to all Aladdin clients”</a> that “will not give investment advice”{{r:copilot}}</td><td>All platform users</td></tr>
<tr><td class="first">Aladdin Accounting</td><td>Investment accounting and performance; the public accounting APIs cover configuration, valuations, lots and composites{{r:plugins}}</td><td>Asset managers and asset owners</td></tr>
<tr><td class="first">Aladdin Provider</td><td>Connects custodians and administrators into a client’s Aladdin; <a href="{{u:ishares}}">service providers pay BlackRock for its use</a>{{r:ishares}}</td><td>Custodians and administrators</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: BlackRock product pages{{r:studio,copilot,adc}}; Amazon press release, December 2025{{r:aws}}; iShares prospectus{{r:ishares}}; the public specifications{{r:plugins}}.</p></div></figure>

<p>BlackRock’s own definition comes from the head of Studio engineering, on Snowflake’s podcast in November 2025. It has three parts.</p>
<div class="script"><p>“So we think about Aladdin today as a platform and Aladdin Studio is essentially the user experience that allows people to think of Aladdin as a platform. It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake takes all of that information that’s generated through our analytics factory and inside of Aladdin and pushes that into Snowflake. And increasingly we’re building a set of developer tools.”</p><p>— <a href="{{u:woodhead}}">Dave Woodhead, Managing Director and Head of Engineering for Aladdin Studio</a>, Snowflake Data Cloud podcast, published November 11, 2025{{r:woodhead}}</p></div>

<figure class="exhibit" id="exhibit-2"><p class="ex-title"><span class="ex-num">Exhibit 2.</span> Studio sits between the people who build and the system of record</p>
<div aria-label="Layer diagram: builders, the AI layer, Aladdin Studio, the system of record and outside inputs, with governance across all layers" class="arch" role="img">
<div class="rl" style="grid-row:1">Who builds</div>
<div class="row" style="grid-column:2;grid-row:1">
<div class="node">Engineers building workflow apps</div>
<div class="node">Code-curious portfolio managers</div>
<div class="node">Data analysts automating reports</div>
<div class="node">Business users working in Excel</div>
</div>
<div class="gov"><b>Governance across all layers</b>Permissions, OAuth scopes and one data model, so what people build stays on the platform</div>
<div class="rl" style="grid-row:2">AI layer</div>
<div class="ai" style="grid-column:2;grid-row:2"><b>Aladdin Copilot</b>, which answers plain-English questions and calls production Aladdin APIs as plugins</div>
<div class="rl" style="grid-row:3">Aladdin Studio</div>
<div class="studio" style="grid-column:2;grid-row:3">
<div>APIs and events: 54 public specifications, all “Aladdin Graph”</div>
<div>The Python SDK, Aladdin Compute and notebooks</div>
<div>Aladdin Data Cloud on Snowflake, fed by Fivetran</div>
<div>Aladdin Tools for Excel and Aladdin Data eXchange</div>
<div>The Developer Portal and Data Dictionary, behind a client login</div>
</div>
<div class="rl" style="grid-row:4">System of record</div>
<div class="core" style="grid-column:2;grid-row:4">The Aladdin core: one shared record of holdings for portfolio management, trading, risk, compliance, operations and accounting</div>
<div class="rl" style="grid-row:5">Outside inputs</div>
<div class="inputs" style="grid-column:2 / span 2;grid-row:5">The client’s own models and data, plus vendor and third-party data, flowing into Data Cloud</div>
</div>
<div class="notes"><p><span class="lead">For illustrative purposes only.</span> <span class="lbl"></span>Source: BlackRock Studio, APIs and Data Cloud pages{{r:studio,apis,adc}}; the public specifications and SDK README{{r:plugins,readme}}; Woodhead{{r:woodhead}}; Rosales and Valdez on the Copilot plugin registry{{r:langchain}}.</p></div></figure>

<figure class="exhibit" id="exhibit-3"><p class="ex-title"><span class="ex-num">Exhibit 3.</span> Eight pieces, from read-and-write APIs to an Excel add-in</p>
<table>
<colgroup><col style="width:110pt"><col></colgroup>
<thead><tr><th>Piece</th><th>What it is, in plain words</th></tr></thead>
<tbody>
<tr><td class="first">APIs (Aladdin Graph)</td><td>Defined ways for a program to read and write Aladdin data. Every public specification carries an id of the form <code>agraph.&lt;domain&gt;.&lt;segment&gt;.&lt;group&gt;.v1.&lt;API&gt;</code>, so Aladdin Graph is the whole API layer, not one API{{r:plugins}}. The <a href="{{u:apis}}">APIs page</a> says there are “dozens,” with more added regularly{{r:apis}}. The 54 public specs include orders, trades, compliance rules, risk rules, security creation and ADC datasets{{r:plugins}}.</td></tr>
<tr><td class="first">Event-driven APIs</td><td>Aladdin tells a program when something happens instead of the program asking. Woodhead names “APIs events” as one pillar{{r:woodhead}}; Goel’s target is <a href="{{u:goel}}">“every single transaction ... via an event, via an API”</a>{{r:goel}}. No event specification is in the public packages{{r:plugins}}.</td></tr>
<tr><td class="first">Aladdin Data Cloud</td><td>A managed data store on Snowflake, with Fivetran moving the data; Goel gives the latency as <a href="{{u:goel}}">“within 15 minutes”</a>{{r:goel}}. Woodhead: “hundreds of Snowflake accounts ... tens of thousands of pipelines”{{r:woodhead}}.</td></tr>
<tr><td class="first">Aladdin Compute</td><td>A hosted space where developers run Python next to their Aladdin data; the SDK has a run mode for <a href="{{u:readme}}">“Aladdin Studio Compute sessions”</a>{{r:readme}}.</td></tr>
<tr><td class="first">Aladdin SDK</td><td>An <a href="{{u:readme}}">open-source Python library</a> that handles login, retries, rate limits, pagination and long-running operations{{r:readme}}. Eleven add-on packages, one per domain, are generated from the specifications by the <a href="{{u:builder}}">plugin builder</a>{{r:builder}}.</td></tr>
<tr><td class="first">Investment research</td><td>A domain of five alpha APIs: research notes, engagements, analyst coverage, watchlists and screening criteria{{r:plugins}}.</td></tr>
<tr><td class="first">Aladdin Tools for Excel</td><td>An Excel add-in listed on the <a href="{{u:apis}}">APIs page</a> as a Studio resource, with Aladdin Data eXchange for bulk delivery; little public detail{{r:apis}}.</td></tr>
<tr><td class="first">Developer Portal and Data Dictionary</td><td>The API catalog, framework guides, field dictionary, notebooks and code samples the <a href="{{u:apis}}">APIs page</a> describes. All sit behind a client login{{r:apis}}.</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: BlackRock Studio and APIs pages{{r:studio,apis}}; the 54 public specifications and SDK README{{r:plugins,readme}}; Woodhead{{r:woodhead}} and Goel{{r:goel}}.</p></div></figure>

<figure class="exhibit keep" id="exhibit-4"><p class="ex-title"><span class="ex-num">Exhibit 4.</span> The public catalog: 54 specifications across 11 domains</p>
<table>
<colgroup><col style="width:92pt"><col style="width:34pt"><col style="width:96pt"><col style="width:30pt"><col style="width:30pt"><col style="width:32pt"><col style="width:34pt"><col></colgroup>
<thead><tr><th>Domain</th><th class="num">Specs</th><th>Operations</th><th class="num">Alpha</th><th class="num">Beta</th><th class="num">Stable</th><th class="num">Sunset</th><th>Largest APIs by operations</th></tr></thead>
<tbody>
''' + CATALOG_ROWS + r'''
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the 54 Swagger 2.0 specifications inside the 11 <code>asdk_plugin</code> packages, version 2.0.0b3, on PyPI{{r:plugins}}. Counts recomputed by the author from the files. The core <code>aladdinsdk</code> package adds four utility APIs (token, subscription, notification and a demo), which are not counted here.</p></div></figure>
<p>The specifications say more than their count. Every one is tagged <code>Access.Internal</code>, a label BlackRock does not explain in public{{r:plugins}}. Posting an order takes <code>whatIf</code> and <code>runCompliance</code>, which defaults to true, and returns compliance violations inline{{r:plugins}}. Ten specifications expose a long-running-operations endpoint and 35 operations are flagged for it; the <a href="{{u:readme}}">SDK polls them</a>{{r:readme}}. Risk exceptions and ADC datasets carry bitemporal fields; rule assignments and dataset releases name a four-eyes approval{{r:plugins}}. Every request carries an application key plus OAuth 2.0 scopes such as <code>trading.order_management.order.v1.Order:read</code>, and the <a href="{{u:readme}}">client ID and secret come from the Studio UI</a>{{r:readme}}.</p>
</section>

<section class="chapter part" id="part-2">
<h2><span class="pn">Part 2</span>The public surface, mapped</h2>
<p>Exhibit 5 follows a prospect’s engineer through six steps, from first hearing about Studio to getting help, and records what is open at each step and what needs a client login. The pattern is the same at every step after the first two.</p>
<figure class="exhibit" id="exhibit-5"><p class="ex-title"><span class="ex-num">Exhibit 5.</span> Six steps a prospect’s developer takes, and where each one stops</p>
<table>
<colgroup><col style="width:58pt"><col style="width:170pt"><col style="width:150pt"><col></colgroup>
<thead><tr><th>Step</th><th>Open today</th><th>Behind a client login</th><th>Receipt</th></tr></thead>
<tbody>
<tr><td class="first">Hear</td><td>Podcasts, webinar replays, client videos and conference talks on BlackRock’s site and partner channels; a Fivetran write-up and a Microsoft recap</td><td>Nothing</td><td><a href="{{u:nd}}">Never Done</a>{{r:nd}}, <a href="{{u:blq}}">Big Little Questions</a>{{r:blq}}, <a href="{{u:woodhead}}">Woodhead</a>{{r:woodhead}}, <a href="{{u:langchain}}">Rosales and Valdez</a>{{r:langchain}}</td></tr>
<tr><td class="first">Read</td><td>The Studio page: three benefit headings, “Create &amp; automate,” “Make Aladdin your own,” “Align internally &amp; externally,” and three named users; the APIs page says “dozens of APIs”</td><td>The Developer Portal and the API framework guides</td><td><a href="{{u:studio}}">Studio page</a>{{r:studio}}, <a href="{{u:apis}}">APIs page</a>{{r:apis}}</td></tr>
<tr><td class="first">See the catalog</td><td>54 specifications, visible only by unpacking the 11 PyPI add-on packages</td><td>The API catalog and the Data Dictionary</td><td><a href="{{u:plugins}}">asdk_plugin packages</a>{{r:plugins}}, <a href="{{u:apis}}">APIs page</a>{{r:apis}}</td></tr>
<tr><td class="first">Try</td><td>Nothing: no sandbox, trial or public test environment was found</td><td>Studio Compute, an API token or OAuth application “registered via Studio UI,” the client’s Aladdin host</td><td><a href="{{u:readme}}">SDK README</a>{{r:readme}}</td></tr>
<tr><td class="first">Build</td><td>The open-source SDK on GitHub and PyPI, with a detailed README; the plugin builder</td><td>Every call: the SDK needs a client host and credentials before any request succeeds</td><td><a href="{{u:readme}}">SDK README</a>{{r:readme}}, <a href="{{u:pypi}}">PyPI history</a>{{r:pypi}}, <a href="{{u:builder}}">plugin builder</a>{{r:builder}}</td></tr>
<tr><td class="first">Get help</td><td>GitHub issues and pull requests on the SDK, which BlackRock engineers answer; the calls to action are “Book a meeting” and “Download the brochure”</td><td>Notebooks, code samples, support</td><td><a href="{{u:pr52}}">Pull request 52</a>{{r:pr52}}, <a href="{{u:pr57}}">pull request 57</a>{{r:pr57}}, <a href="{{u:studio}}">Studio page</a>{{r:studio}}</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the pages and repositories in the Receipt column, read with no account, login or payment, October 2026.</p></div></figure>

<p>The same gating shows in a scored comparison. On October 8, 2026, I tested how far a developer with no client relationship could get on 11 platforms, scoring eight criteria from 0 to 2{{r:fsdev,ssdev,lsegdev}}. Studio scored 4 of 16. Its <a href="{{u:readme}}">open-source SDK</a> is unique among the incumbent investment platforms tested{{r:readme}}, but documentation, a sandbox and a first call all require a login. The data and cloud platforms score higher because they sell to developers directly, so their rows are a reference point, not a like-for-like comparison.</p>
<figure class="exhibit keep" id="exhibit-6"><p class="ex-title"><span class="ex-num">Exhibit 6.</span> Outside developer access, scored on eight criteria</p>
<div class="heat-key"><span class="k2">2: Fully public or self-serve</span><span class="k1">1: Partial or after signup or approval</span><span class="k0">0: None or blocked</span></div>
''' + HEAT_TABLE + r'''
<div class="notes"><p>Scoring: on each criterion, 2 means fully public or self-serve, 1 means partial, limited, or open only after a free signup or an approval, and 0 means none or blocked. For the AI connector, 2 means an MCP server or connector that outside AI tools can use, 1 means one that is announced or in limited release, and 0 means none, or an assistant that works only inside the vendor’s own platform.</p><p><span class="lbl"></span>Source: the author’s hands-on test of each platform’s public pages{{r:studio,fsdev,ssdev,lsegdev,snowdev,dbxtry,simagent,arcai,msci}}, with no accounts, logins or payments, October 8, 2026. Bloomberg, Clearwater and MSCI may be underrated because some of their pages blocked automated access.</p></div></figure>

<p>The richest public source on Studio is spoken, not written. The 126 recordings pulled for this document hold 39 podcast episodes, 12 webinar replays, 15 Big Little Questions episodes, three client-story videos, two Uncharted episodes, 32 eFront videos and a handful of conference talks and partner videos{{r:nd,blq}}. Five BlackRock speakers define Studio on the record, and their titles are the ones the recordings give.</p>
<figure class="exhibit" id="exhibit-7"><p class="ex-title"><span class="ex-num">Exhibit 7.</span> The five BlackRock speakers who define Studio on the record</p>
<table>
<colgroup><col style="width:92pt"><col style="width:150pt"><col><col style="width:84pt"></colgroup>
<thead><tr><th>Speaker</th><th>Title, as given</th><th>What they add</th><th>Where</th></tr></thead>
<tbody>
<tr><td class="first">Dave Woodhead</td><td>Managing Director and Head of Engineering for Aladdin Studio</td><td>The three-pillar definition; 3,000 internal citizen developers; “hundreds of Snowflake accounts”</td><td><a href="{{u:woodhead}}">Snowflake podcast, Nov 2025</a>{{r:woodhead}}</td></tr>
<tr><td class="first">Richard Newman</td><td>General Manager, Aladdin Studio</td><td>Data Cloud is “part of Studio”; analytics APIs “releasing soon ... all part of the Studio umbrella”</td><td><a href="{{u:newman}}">Never Done, Jan 2025</a>{{r:newman}}</td></tr>
<tr><td class="first">Diwakar Goel</td><td>Global Head of Data, Aladdin</td><td>Every transaction “via an event, via an API”; Data Cloud “within 15 minutes of latency”; 3,000 people in the citizen-developer bracket</td><td><a href="{{u:goel}}">Pensions webinar, 2025</a>{{r:goel}}</td></tr>
<tr><td class="first">Kunal Khara</td><td>Managing Director and Global Head of Aladdin Product</td><td>“The Aladdin studio estate” as a 2024 focus: programmatic access “at machine scale”</td><td><a href="{{u:khara}}">Awards interview, early 2024</a>{{r:khara}}</td></tr>
<tr><td class="first">Jeff Miller</td><td>Managing Director, Global Head of Data Platform and Product Engineering</td><td>Data Cloud replaced “flat files ... FTP and related transfers”</td><td><a href="{{u:miller}}">Snowflake video, undated</a>{{r:miller}}</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl e"></span>Source: the recordings cited in the Where column. Quotations are verbatim from the transcripts; three of the five are machine transcriptions, marked in the register.</p></div></figure>
</section>

<!-- ================= PART 3 ================= -->
<section class="chapter finding" id="f1">
<h2>1. Studio is in use, and the proof sits in other firms’ filings and code</h2>
<p>BlackRock’s <a href="{{u:studio}}">Studio page</a> names no client as building on Studio’s APIs or SDK{{r:studio}}; its own client video has Royal London’s chief executive crediting <a href="{{u:rlam}}">the Snowflake implementation</a>{{r:rlam}}. A <a href="{{u:edgar}}">full-text search of SEC EDGAR</a> finds no company filing that mentions “Aladdin Studio”{{r:edgar}}. The evidence of use is in what other firms pay, file and commit. JPMorgan Chase reports its Aladdin payments in its <a href="{{u:jpmproxy}}">proxy statement</a> every year, the only client found that does so over this many years{{r:jpmproxy}}. Payments stayed between $4.4 million and $7.6 million from 2017 to 2023, then rose to $14.7 million in 2024 and <a href="{{u:jpm2026}}">$25.6 million in 2025</a>{{r:jpm2026}}.</p>
<figure class="exhibit chart keep" id="exhibit-8"><p class="ex-title"><span class="ex-num">Exhibit 8.</span> JPMorgan Chase payments to BlackRock for Aladdin, US$ millions</p>
''' + JPM_SVG + r'''
<div class="notes"><p><span class="lbl"></span>Source: JPMorgan Chase proxy statements (DEF 14A), filed 2017 to 2026, by year of payment{{r:jpmproxy,jpm2026}}. The payments may include more than a client license: JPMorgan is also a custodian, and <a href="{{u:trade}}">in 2016 it said it was connecting to Aladdin</a> to serve custody clients on the platform{{r:trade}}; that report is trade press, not a JPMorgan or BlackRock document.</p></div></figure>
<p>In December 2025 a Janus Henderson engineer submitted two changes to the <a href="{{u:readme}}">open-source SDK</a>: one <a href="{{u:pr52}}">lets it send API calls to a different address</a>, the other <a href="{{u:pr53}}">adds custom headers</a> such as a subscription key, both for firms that route Aladdin calls through an enterprise gateway like Azure API Management{{r:pr52,pr53}}. The BlackRock engineer who co-wrote the SDK’s <a href="{{u:engblog}}">launch post</a> merged them, and the code is <a href="{{u:clientpy}}">on the main branch</a>{{r:engblog,clientpy}}. All six commits carry the same author line:</p>
''' + CODE_BLOCK + CODE_LINK.replace("</a></p>", "</a>{{r:patch}}</p>") + r'''
<p>The timing fits Janus Henderson’s <a href="{{u:jhg10k}}">10-K</a>, which says the firm chose in the third quarter of 2025 to move its investment management system to Aladdin, a “complex, multi-year initiative”{{r:jhg10k}}. The SDK’s <a href="{{u:contrib}}">contributor history</a> shows no code from any other company{{r:contrib}}. Inside BlackRock, Woodhead counts <a href="{{u:woodhead}}">“3,000 citizen developers in business engineers that are interacting with Aladdin using Python or using R”</a> and adds “I think that number has probably peaked”{{r:woodhead}}; Goel gives the same figure{{r:goel}}.</p>
<div class="gtm"><p><span class="lead">What it means for go-to-market.</span> The references exist, but none is BlackRock’s to use: a proxy statement, a 10-K and a commit are facts a prospect can find, not stories a seller can tell. The first job is to turn one migration into a named build story with the client’s consent.</p></div>
</section>

<section class="chapter finding" id="f2">
<h2>2. BlackRock’s own growth story is APIs, yet Studio is never named to investors</h2>
<p>At its <a href="{{u:id2025}}">2025 Investor Day</a>, BlackRock projected that API calls across BlackRock and Aladdin would grow 17 times by 2030, against four times for model portfolios, two times for portfolios and 1.3 times for trade allocations; the slide gave no starting number{{r:id2025}}. API use is the activity the <a href="{{u:studio}}">Studio page</a> describes{{r:studio}}. Yet across <a href="{{u:roic}}">26 earnings calls</a> from the first quarter of 2020 to the second quarter of 2026, no executive said “Studio”{{r:roic}}, and a single line on a <a href="{{u:id2023}}">2023 Investor Day slide</a> is the only other investor mention found{{r:id2023}}. BlackRock’s <a href="{{u:blk10k}}">10-K</a> reports technology services revenue and annual contract value, with nothing on Studio{{r:blk10k}}.</p>
<figure class="exhibit" id="exhibit-9"><p class="ex-title"><span class="ex-num">Exhibit 9.</span> Mentions of Studio terms on 26 BlackRock earnings calls, Q1 2020 to Q2 2026</p>
<table>
<colgroup><col style="width:110pt"><col style="width:60pt"><col></colgroup>
<thead><tr><th>Term</th><th class="num">Mentions</th><th>Context</th></tr></thead>
<tbody>
<tr class="focus"><td class="first">Studio</td><td class="num">0</td><td>One line on a <a href="{{u:id2023}}">2023 Investor Day slide</a> is the only other investor mention found{{r:id2023}}</td></tr>
<tr><td class="first">Data Cloud</td><td class="num">2</td><td><a href="{{u:roic3q22}}">Q3 2022</a>{{r:roic3q22}} and <a href="{{u:roic4q24}}">Q4 2024</a>{{r:roic4q24}}, as an add-on sold with Aladdin Enterprise</td></tr>
<tr><td class="first">API</td><td class="num">1</td><td><a href="{{u:roic4q21}}">Q4 2021</a>: “clients are really looking to use both data and APIs”{{r:roic4q21}}</td></tr>
<tr><td class="first">Copilot</td><td class="num">1</td><td><a href="{{u:roic4q23}}">Q4 2023</a>: “investments in Aladdin AI copilots”{{r:roic4q23}}</td></tr>
<tr><td class="first">Citizen developer</td><td class="num">0</td><td>Never</td></tr>
<tr><td class="first">Agent</td><td class="num">0</td><td>Never</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl n"></span>Source: <a href="{{u:roic}}">third-party transcripts of BlackRock earnings calls</a>, Q1 2020 to Q2 2026{{r:roic}}. Counts are the author’s tally. Zero counts are reliable; other counts are approximate.</p></div></figure>
<p>The 10-K describes the economics without the product. <a href="https://www.sec.gov/Archives/edgar/data/2012383/000119312526071966/R41.htm">BlackRock’s FY2025 10-K</a> says technology services fees are generally set by the value of positions on the platform or at a fixed rate, and can also depend on the number of subscriptions, implementation go-lives, and delivery and support{{r:blk10k}}. API calls, the measure BlackRock projects to grow fastest, appear in none of those terms{{r:id2025}}.</p>
<p>The silence is not for lack of material. BlackRock’s product head told an awards interviewer in early 2024 that <a href="{{u:khara}}">“the Aladdin studio estate ... is going to this year be a major, major unlock,”</a> because users want to work with data “on a programmatic basis at machine scale”{{r:khara}}. Its trading product marketing head describes <a href="{{u:kamya}}">“a burgeoning community of individuals saying ‘I need that in the form of an API’”</a>{{r:kamya}}. Those lines live on podcasts and award videos, not in the materials an analyst or a chief technology officer reads.</p>
<div class="gtm"><p><span class="lead">What it means for go-to-market.</span> The 17-times projection is Studio’s number without Studio’s name. A reportable measure, agreed with investor relations and product, would let the investor story and the product story point at the same thing.</p></div>
</section>

<section class="chapter finding" id="f3">
<h2>3. The developer front door is a sales conversation, not a signup</h2>
<p>The <a href="{{u:studio}}">public Studio page</a> works like a brochure: its calls to action are “Book a meeting” and “Download the brochure”{{r:studio}}. The <a href="{{u:apis}}">APIs page</a> mentions developer guides, notebooks and code samples but links to none{{r:apis}}. The one open artifact is the SDK, and the SDK is a key without a door: the README says the <a href="{{u:readme}}">client ID and secret “can be sourced from Studio UI by creating a OAuth application under a Project,”</a> and an API token is “registered via Studio UI”{{r:readme}}. A developer at a prospect firm can install it and read its code, and cannot make a call.</p>
<figure class="exhibit" id="exhibit-10"><p class="ex-title"><span class="ex-num">Exhibit 10.</span> The top of Studio’s developer funnel is a sales conversation, not a signup</p>
<table>
<colgroup><col style="width:252pt"><col></colgroup>
<thead><tr><th>Public</th><th>Behind a client login</th></tr></thead>
<tbody>
<tr><td>Marketing pages on blackrock.com/aladdin{{r:studio,apis}}</td><td>The Studio Developer Portal{{r:apis}}</td></tr>
<tr><td>The BlackRock Engineering blog on Medium{{r:engblog}}</td><td>Full API documentation and the API framework guides{{r:apis}}</td></tr>
<tr><td>The open-source SDK on GitHub and PyPI, with a detailed README{{r:readme,pypi}}</td><td>The Data Dictionary and downloadable notebooks{{r:apis}}</td></tr>
<tr><td>The 54 specifications, by unpacking the add-on packages{{r:plugins}}</td><td>API tokens, OAuth applications, Compute sessions and Data Cloud{{r:readme}}</td></tr>
<tr><td>Podcasts, webinar replays and conference talks{{r:nd,woodhead}}</td><td>Rate limits, SLAs, pricing and the Studio UI itself</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: BlackRock’s Studio and APIs pages{{r:studio,apis}}; the SDK README and PyPI history{{r:readme,pypi}}; the engineering blog{{r:engblog}}.</p></div></figure>
<p>The README shows who the SDK is built for. It documents three run modes, “a developer’s local machine,” <a href="{{u:readme}}">“Aladdin Studio Compute sessions”</a> and a test mode; it stores a prompted password in the operating system’s credential manager; and it already carries settings for firms that consume “the Aladdin APIs via an enterprise API management platform such as Azure API Management,” the case the Janus Henderson pull requests extended{{r:readme,pr52}}. These are the needs of a client’s engineering team, not of a prospect reading the page.</p>
<p>The SDK itself is a beta. It has had <a href="{{u:pypi}}">14 releases since May 2024</a>, all alpha or beta, with the core at 2.0.0b10 in July 2026 and the add-ons at 2.0.0b3{{r:pypi,plugins}}. None installs on Python 3.13, because each pins an old Snowflake library, and the SDK <a href="{{u:pr57}}">conflicts with the official MCP toolkit</a>; an outside fix was merged in August 2026 and has not shipped{{r:pr57}}. The scored test in Exhibit 6 puts Studio at 4 of 16, level with State Street and one point behind Bloomberg{{r:ssdev}}. Gating is a reasonable choice for a platform sold to large institutions on long contracts. It does mean the curious engineer at a prospect, the person Khara describes as wanting access “at machine scale,” reads nothing until a meeting is booked{{r:khara}}.</p>
<div class="gtm"><p><span class="lead">What it means for go-to-market.</span> The first public API reference, even a read-only one for a few stable domains, would move the developer’s first hour from a sales call to a page. A stable SDK release would give that page something that installs.</p></div>
</section>

<section class="chapter finding" id="f4">
<h2>4. AI tools are the new front door, and seven data providers already have one</h2>
<p><a href="{{u:mcp}}">MCP</a> is the common standard AI assistants use to pull data from other systems{{r:mcp}}. Seven providers a Studio buyer also talks to now offer a connector or an MCP server. LSEG had <a href="{{u:investing}}">90 customers connected to its MCP server</a> by April 2026, according to a secondary summary of its results slides{{r:investing,lseg}}. No public connector for Aladdin was found on BlackRock’s <a href="{{u:studio}}">product pages</a> or <a href="{{u:ghblk}}">GitHub</a>{{r:studio,ghblk}}.</p>
<figure class="exhibit" id="exhibit-11"><p class="ex-title"><span class="ex-num">Exhibit 11.</span> Seven data and platform providers let outside AI tools pull their data; no public Aladdin equivalent was found</p>
<table>
<colgroup><col style="width:80pt"><col><col style="width:150pt"></colgroup>
<thead><tr><th>Provider</th><th>What is public</th><th>Receipt</th></tr></thead>
<tbody>
<tr><td class="first">FactSet</td><td>An MCP server for its data, which FactSet calls the first in its market</td><td><a href="{{u:factset}}">FactSet press release</a>{{r:factset}}</td></tr>
<tr><td class="first">LSEG</td><td>A collaboration with Anthropic and an MCP server; 90 customers connected by April 2026</td><td><a href="{{u:lseg}}">LSEG press release</a>{{r:lseg}}; <a href="{{u:investing}}">Investing.com summary</a>{{r:investing}}</td></tr>
<tr><td class="first">MSCI</td><td>“AI connectors” to its proprietary data</td><td><a href="{{u:msci}}">MSCI press release</a>{{r:msci}}</td></tr>
<tr><td class="first">Arcesium</td><td>AI features in Aquata, and an AI platform announcement</td><td><a href="{{u:arcesium}}">Arcesium press releases</a>{{r:arcesium,arcai}}</td></tr>
<tr><td class="first">S&amp;P Global</td><td>Credit Ratings added to its AI Data Portal, September 2026</td><td><a href="{{u:spg}}">S&amp;P Global press release</a>{{r:spg}}</td></tr>
<tr><td class="first">Snowflake</td><td>A documented MCP server for Cortex Agents</td><td><a href="{{u:snowmcp}}">Snowflake documentation</a>{{r:snowmcp}}</td></tr>
<tr><td class="first">Databricks</td><td>Managed MCP servers, documented</td><td><a href="{{u:dbxmcp}}">Databricks documentation</a>{{r:dbxmcp}}</td></tr>
<tr class="focus"><td class="first">Aladdin</td><td>None found. A Forward Deploy Engineer posting for Aladdin Data names “Model Context Protocol (MCP), AI agents, and Copilot extensions”</td><td><a href="{{u:fde}}">BlackRock Careers</a>{{r:fde}}</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the press releases, documentation and job posting in the Receipt column, as of October 2026. The LSEG customer count is from a secondary summary{{r:investing}}.</p></div></figure>
<p>Inside the platform, the connector already exists in a different form. <a href="{{u:copilot}}">Aladdin Copilot</a> is “now available to all Aladdin clients” and “will not give investment advice or respond to questions outside Aladdin platform boundaries”{{r:copilot}}. Its engineers describe a plugin registry with <a href="{{u:langchain}}">“couple of thousands agents and tools”</a>, where the first way a team onboards is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production”{{r:langchain}}. Copilot’s tools are Studio’s APIs. Microsoft’s Adrian Crockett put the dependency in one line on BlackRock’s podcast: <a href="{{u:crockett}}">“There’s no copilot without plug-ins”</a>{{r:crockett}}. BlackRock’s AI product head says the team is making sure <a href="{{u:pemm}}">“the data model itself is structured for agentic use cases”</a>{{r:pemm}}.</p>
<div class="gtm"><p><span class="lead">What it means for go-to-market.</span> The next prospect’s first API call may come from an AI assistant rather than a notebook. A connector that exposes a governed subset of the same APIs Copilot already calls would meet that buyer where FactSet, LSEG and MSCI already stand.</p></div>
</section>

<section class="chapter finding" id="f5">
<h2>5. Buyers say they want a core platform plus their own builds</h2>
<p>BlackRock’s own Build vs. Buy webinar polled its attendees. In the first poll, 37 percent said they run “mostly vendor platforms,” 30 percent “hybrid,” 18 percent were “actively reevaluating” and 15 percent were “mostly built in house”{{r:bvb}}. Asked what is driving the decision, “AI and data demands” led at 42 percent, with cost and speed to market tied behind it{{r:bvb}}. Asked what they would stop maintaining internally, 53 percent chose compliance reporting{{r:bvb}}. The slide put 60 to 70 percent of technology cost in “maintenance of current systems,” and the Alpha FMC panellist said a transformation runs “roughly 12 to 18 months”{{r:bvb}}.</p>
<figure class="exhibit chart keep" id="exhibit-12"><p class="ex-title"><span class="ex-num">Exhibit 12.</span> What attendees of BlackRock’s Build vs. Buy webinar said</p>
<div class="chart-row">
<div class="side"><p class="side-head">Where firms sit today</p>''' + CHART_POLL1 + r'''</div>
<div class="side"><p class="side-head">What they would stop maintaining internally</p>''' + CHART_POLL3 + r'''</div>
</div>
<div class="notes"><p><span class="lbl e"></span>Source: poll results as read out on the <a href="{{u:bvb}}">Build vs. Buy webinar replay</a>, published captions{{r:bvb}}. Attendee counts were not stated. Poll 2, on what is driving the decision, put “AI and data demands” at 42 percent, with cost and speed to market tied.</p></div></figure>
<div class="script"><p>“What’s the API suite that you have? Are you using connectors to Snowflake or to Databricks? And I think that that part of the RFP has become much more prominent.”</p><p>— <a href="{{u:bvb}}">Clark Schafer, Partner, Alpha FMC</a>, on the Build vs. Buy webinar{{r:bvb}}</p></div>
<p>The market is moving the same way. SimCorp announced wins at <a href="{{u:ab}}">AllianceBernstein</a> in February 2026 and <a href="{{u:pictet}}">Pictet</a> in May 2026; AllianceBernstein keeps its “specialized in-house technology,” and Pictet connects its own tools to SimCorp One by API{{r:ab,pictet}}. BlackRock’s <a href="{{u:bvbpage}}">August 2026 insight</a> says “Build vs buy is no longer a binary question”{{r:bvbpage}}. Studio is the product that answers that question for Aladdin, and the webinar did not name it.</p>
<div class="gtm"><p><span class="lead">What it means for go-to-market.</span> The buyer is asking for the API suite in the RFP. The answer should be a document a prospect can read before the RFP, with the catalog, the connectors and a named client who built on it.</p></div>
</section>

<section class="chapter finding" id="f6">
<h2>6. The public message is consistent; the distribution is not</h2>
<p>Four BlackRock speakers, across two years and four venues, describe Studio with the same three parts. Woodhead names them outright{{r:woodhead}}. Newman places Data Cloud “part of Studio” and analytics APIs “all part of the Studio umbrella”{{r:newman}}. Goel describes events, APIs and a near-real-time data store, and adds that BlackRock wants “to start exposing some of the software and application that we’re building”{{r:goel}}. Khara calls it programmatic access to data, reporting and dashboards{{r:khara}}. The 2026 <a href="{{u:spd}}">Studio Developer posting</a> calls Studio “Aladdin’s extensibility layer”{{r:spd}}, and the <a href="{{u:studio}}">product page</a> says “Make Aladdin your own”{{r:studio}}.</p>
<figure class="exhibit" id="exhibit-13"><p class="ex-title"><span class="ex-num">Exhibit 13.</span> Four BlackRock speakers, 2024 to 2025, and the three pillars each names</p>
<table>
<colgroup><col style="width:84pt"><col><col style="width:36pt"><col style="width:36pt"><col style="width:36pt"></colgroup>
<thead><tr><th>Speaker, date</th><th>What they said</th><th class="ctr">APIs and events</th><th class="ctr">Data Cloud</th><th class="ctr">Developer tools</th></tr></thead>
<tbody>
<tr><td class="first">Kunal Khara, early 2024</td><td><a href="{{u:khara}}">“More users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis at machine scale, over and above what they get through our front end applications”</a>{{r:khara}}</td><td class="ctr chk">Yes</td><td class="ctr chk">Yes</td><td class="ctr dim">–</td></tr>
<tr><td class="first">Richard Newman, Jan 2025</td><td><a href="{{u:newman}}">“The Aladdin data cloud specifically ... which is part of Studio”; “we’re releasing soon the ability to actually access those analytic APIs ... That’s all part of the Studio umbrella”</a>{{r:newman}}</td><td class="ctr chk">Yes</td><td class="ctr chk">Yes</td><td class="ctr dim">–</td></tr>
<tr><td class="first">Diwakar Goel, 2025</td><td><a href="{{u:goel}}">“Every single transaction that happens should be available and accessible to you via an event, via an API”; ADC as “a near real time data store ... within 15 minutes of latency”; exposing “the software and application that we’re building”</a>{{r:goel}}</td><td class="ctr chk">Yes</td><td class="ctr chk">Yes</td><td class="ctr chk">Yes</td></tr>
<tr><td class="first">Dave Woodhead, Nov 2025</td><td><a href="{{u:woodhead}}">“It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... And increasingly we’re building a set of developer tools”</a>{{r:woodhead}}</td><td class="ctr chk">Yes</td><td class="ctr chk">Yes</td><td class="ctr chk">Yes</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl e"></span>Source: the four recordings cited{{r:khara,newman,goel,woodhead}}. Quotations are verbatim from the transcripts; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked in the register.</p></div></figure>
<p>Where the message appears is the problem. It appears on podcasts, in webinar replays and on one product page{{r:nd,bvb,studio}}. It does not appear on an earnings call{{r:roic}}, in a public developer portal{{r:apis}}, in an SDK release that installs on current Python{{r:pypi}}, or in a connector an outside AI tool can use{{r:ghblk}}. The <a href="{{u:acf}}">fall 2026 Aladdin Client Forum</a> promised a first look at “where Aladdin goes next,” to an audience of clients{{r:acf}}. The positioning has held for three years. The channels have not changed with it.</p>
<div class="gtm"><p><span class="lead">What it means for go-to-market.</span> Marketing does not need a new message. It needs the existing one in four places it is missing: investor materials, a public reference, a stable release and an AI connector, in that order of cost.</p></div>
</section>

<section class="chapter part" id="part-4">
<h2><span class="pn">Part 4</span>What I would do, and what I would need</h2>
<p>Each move answers one finding. Product owns what gets built and when; marketing owns positioning, launches, client stories and sales enablement. Every capability would be labeled live or roadmap, with a quarter, before sales hears it; the product manager checks each message for accuracy, engineering checks technical claims and compliance checks the final version.</p>
<figure class="exhibit" id="exhibit-14"><p class="ex-title"><span class="ex-num">Exhibit 14.</span> Five moves over 90 days and the two quarters after</p>
<table>
<colgroup><col style="width:66pt"><col style="width:96pt"><col style="width:90pt"><col style="width:82pt"><col style="width:82pt"><col></colgroup>
<thead><tr><th>Move</th><th>First 90 days</th><th>Following two quarters</th><th>Marketing owns</th><th>Product owns</th><th>Measure</th></tr></thead>
<tbody>
<tr><td class="first">Client build stories (Finding 1)</td><td>Shortlist clients moving onto Aladdin; secure one consent; draft the first story</td><td>Three named stories, one per persona on the Studio page</td><td>Finding, writing, legal review, placement</td><td>Client introductions; the engineering detail</td><td>Named references; deals where one was used</td></tr>
<tr><td class="first">A reportable Studio measure (Finding 2)</td><td>Propose two candidate measures with investor relations, built on the API-call projection</td><td>One measure in earnings materials and in sales decks</td><td>The story around the number</td><td>A number that can be reported</td><td>Studio cited in earnings materials</td></tr>
<tr><td class="first">A public API reference (Finding 3)</td><td>Decide with product what can be public; publish a getting-started guide for two stable domains</td><td>A public reference for the stable specifications; a first-call tutorial</td><td>The guide, the pages around it, the launch</td><td>The scope decision; technical review of every page</td><td>Developer access score; prospects who reach a first call</td></tr>
<tr><td class="first">A stable SDK release (Finding 3)</td><td>Agree a release date; plan the launch</td><td>Ship 2.0; tell clients, partners and sales</td><td>Launch plan, release notes, partner briefing</td><td>The merged dependency fix; current Python support</td><td>Clean installs; a first stable release</td></tr>
<tr><td class="first">An Aladdin AI connector (Finding 4)</td><td>Size the launch; position against FactSet, LSEG and MSCI; brief sales on what exists today</td><td>Launch a governed connector on the APIs Copilot already calls</td><td>Positioning, launch tiering, enablement</td><td>Scope and timing, on the Forward Deploy Engineer work{{r:fde}}</td><td>Connector available; clients connected</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the author’s proposals, built on Findings 1 to 6. The connector move builds on BlackRock’s <a href="{{u:fde}}">Forward Deploy Engineer posting</a>, which names MCP{{r:fde}}, and on the plugin registry its engineers describe{{r:langchain}}.</p></div></figure>
<p>Launches would be sized in three tiers agreed with product, from a full campaign to release notes. Before any of this, eight questions need internal data that no public source holds.</p>
<figure class="exhibit" id="exhibit-15"><p class="ex-title"><span class="ex-num">Exhibit 15.</span> Eight questions for internal data</p>
<table>
<colgroup><col style="width:300pt"><col></colgroup>
<thead><tr><th>Question</th><th>What the answer would decide</th></tr></thead>
<tbody>
<tr><td class="first">How many clients have active API credentials or a Data Cloud instance, and how has that changed since 2024?</td><td>The baseline for every measure in Exhibit 14</td></tr>
<tr><td class="first">Is a migration the main moment clients start building on Studio?</td><td>Whether to lead with clients moving onto Aladdin</td></tr>
<tr><td class="first">Which clients would agree to be named, and what usually stops them?</td><td>How soon client stories can start</td></tr>
<tr><td class="first">What could a non-client be allowed to see without a login?</td><td>How much of an API reference can be public</td></tr>
<tr><td class="first">What does the <code>Access.Internal</code> tag on every public specification mean, and does it limit what can be documented?</td><td>Whether the public catalog is the public reference</td></tr>
<tr><td class="first">Which builds by BlackRock’s own 3,000 citizen developers could become client stories, and what approvals would they need?</td><td>Whether internal builds can serve as early proof</td></tr>
<tr><td class="first">How will clients connect their own AI tools to Aladdin, and is the Forward Deploy Engineer work the path?</td><td>The scope and timing of a connector launch</td></tr>
<tr><td class="first">Where does adoption stall most: awareness, the first API call, or getting a build into production?</td><td>Where marketing spends first: public content, self-serve help or client success</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the author’s questions, to test this document’s findings against BlackRock’s internal data. Question 5 refers to the tag on the public specifications{{r:plugins}}.</p></div></figure>
<p>On method: every claim in this document was checked against the document or recording it cites, and every number carries a date. Generative AI tools were used to pull pages, unpack packages and transcribe recordings. The reading, the scoring and the judgement were done by hand.</p>
</section>

<section class="chapter runon" id="sources">
<h2>Source register</h2>
<p class="front-note">Numbered in order of first citation and grouped by grade. P is a primary document; S is a BlackRock speaker on the record, with the name and title as the recording gives them; T is a third-party report. “Machine transcription” means a local transcription of the downloaded audio; “auto-captions” means YouTube’s captions. In both, names and jargon can be mis-heard, and only caption misspellings of proper names were corrected inside quotations.</p>
<div class="register">
{{REGISTER}}
</div>
</section>

<section class="fullpage back">
  <div class="inner">
    <span class="accent-bar"></span>
    <h2>About this document</h2>
    <p>Independent analysis compiled from public sources: BlackRock product pages, SEC filings, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings. It was not produced, reviewed or endorsed by BlackRock.</p>
    <p>Facts are as of October 19, 2026, unless an exhibit gives another date. Underlined text links to the document behind each fact. Superscripts point to the Source register, which gives the grade, the title, the speaker and the date of every source.</p>
    <p>Three corrections were made against earlier drafts of this research: 58 API specifications became 54 once the SDK’s four utility APIs were set aside; a widely repeated “68 percent” survey figure was dropped because it could not be found in the report it is attributed to; and “more than 2,000 citizen developers” became 3,000, counted inside BlackRock rather than among clients.</p>
    <p>The moves and questions in Part 4 are the author’s proposals, based on the findings in Part 3.</p>
    <p>BlackRock and Aladdin are registered trademarks of BlackRock, Inc. Other company and product names are the property of their owners.</p>
    <p>Set in Barlow and Barlow Condensed, open-license stand-ins for BlackRock’s licensed BLK Fort typeface. Code is set in IBM Plex Mono.</p>
  </div>
</section>
'''

# ---------------------------------------------------------------- resolve placeholders
def sub(m):
    kind, arg = m.group(1), m.group(2)
    return r(arg) if kind == "r" else u(arg)
body = re.sub(r"\{\{(r|u):([a-z0-9_,]+)\}\}", sub, BODY)

# register, grouped by grade in citation order
groups = {"P":[], "S":[], "T":[]}
for i, k in enumerate(order, 1):
    groups[S[k][0]].append((i, k))
names = {"P":"P. Primary documents", "S":"S. BlackRock speakers on the record", "T":"T. Third-party reports"}
reg = []
for g in ("P","S","T"):
    reg.append(f"<h3>{names[g]}</h3>")
    for i, k in groups[g]:
        grade, title, who, date, url = S[k]
        reg.append(f'<p id="s{i}"><b class="n">{i}</b><span class="g">{grade}</span><span class="t">{html.escape(title)}</span>. {html.escape(who)}, {html.escape(date)}. <a href="{html.escape(url, quote=True)}">{html.escape(url)}</a></p>')
body = body.replace("{{REGISTER}}", "\n".join(reg))

unused = [k for k in S if k not in order]
print("sources cited:", len(order), "unused:", unused)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(HEAD) + "\n" + body + "\n</body></html>\n")
print("wrote", OUT)
