#!/usr/bin/env python3
"""Build Aladdin_Studio_With_AI.html from the verified pieces of
Aladdin_Studio_From_The_Outside.html plus new prose. Receipts keep the old
register ids while writing; a final pass renumbers them in order of first
citation and renumbers exhibits in document order."""
import re, sys, html as H
from bs4 import BeautifulSoup

B = '/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
SRC = f'{B}/gtm/out/Aladdin_Studio_From_The_Outside.html'
OUT = f'{B}/gtm/out/Aladdin_Studio_With_AI.html'
old = open(SRC, encoding='utf-8').read()

# ---------------------------------------------------------------- head
head_end = old.index('<section class="fullpage cover">')
head = old[:head_end]
head = head.replace('<title>Aladdin Studio from the outside</title>', '<title>Aladdin Studio, learned with AI</title>')

# ---------------------------------------------------------------- reusable blocks
def block(tag_open, text, end):
    i = text.index(tag_open); j = text.index(end, i) + len(end); return text[i:j]

def figure(ex_id):
    return block(f'<figure class="exhibit', old[old.index(f'id="exhibit-{ex_id}"') - 40:], '</figure>')

def figure_by_id(ex_id):
    i = old.index(f'id="{ex_id}"'); i = old.rfind('<figure', 0, i); j = old.index('</figure>', i) + 9
    return old[i:j]

FIG = {n: figure_by_id(f'exhibit-{n}') for n in range(1, 18)}

def retitle(fig, title):
    return re.sub(r'(<span class="ex-num">Exhibit \d+\.</span>)[^<]*</p>', r'\1 ' + title + '</p>', fig, count=1)

# register entries from the old file, keyed by id
REG = {}
for m in re.finditer(r'<p id="(s\d+)">(.*?)</p>', old, flags=re.S):
    inner = m.group(2)
    grade = re.search(r'<span class="g">([PST])</span>', inner).group(1)
    body = re.sub(r'^<b class="n">\d+</b>', '', inner)
    REG[m.group(1)] = (grade, body)

def reg(key, grade, title, rest, url, extra=''):
    REG[key] = (grade, f'<span class="g">{grade}</span><span class="t">{title}</span>. {rest} <a href="{url}">{url}</a>{(" " + extra) if extra else ""}')

# new sources (ids renumbered later)
reg('n_ppf', 'P', 'Contract award notice 062522-2025, investment risk and analytics platform, Pension Protection Fund',
    'UK Find a Tender, 2025. Scoring weights and outcome as read in an earlier draft of this research (October 2026); not re-pulled.',
    'https://www.find-tender.service.gov.uk/Notice/062522-2025')
reg('n_nest', 'P', 'Contract award notice 035311-2023, Nest Corporation',
    'UK Find a Tender, 2023. Scoring weights and outcome as read in an earlier draft of this research (October 2026); not re-pulled.',
    'https://www.find-tender.service.gov.uk/Notice/035311-2023')
reg('n_pbgc', 'P', 'Award 16PBGC23C0006, Investment Risk Management System, Pension Benefit Guaranty Corporation to BlackRock Financial Management',
    'USAspending.gov, award record: full and open competition, four offers received, performance March 2023 to March 2027, re-read October 19, 2026. The 2017 award and the price comparison are as read in an earlier draft of this research.',
    'https://api.usaspending.gov/api/v2/awards/CONT_AWD_16PBGC23C0006_1665_-NONE-_-NONE-/')
reg('n_ms', 'P', 'How BlackRock is finding new alpha as AI transformation becomes a critical business driver',
    'Microsoft Cloud blog, by Judson Althoff, December 11, 2024.',
    'https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/11/how-blackrock-is-finding-new-alpha-as-ai-transformation-becomes-a-critical-business-driver/')
reg('n_wp', 'S', 'Unifying the whole portfolio across public and private markets (webinar replay; machine transcription)',
    'Melissa Faraz, Global Head of Business Development for Private Markets Analytics Platforms and Head of Preqin London; Paul McGaugh, Managing Director, Aladdin Private Markets Product; Cameron Skinner, Managing Director and Global Head of Solutions Engineering, BlackRock, September 2025.',
    'https://www.blackrock.com/aladdin/discover/expertise/webinars/unifying-the-whole-portfolio-across-public-and-private-markets',
    'Quoted at WP_TIMES.')
# Build vs. Buy: add the Sewdass passages quoted in this edition
g, b = REG['s63']
REG['s63'] = (g, b.replace('Quoted at 4:37, 4:40, 14:46, 24:34, 42:22, 47:41.',
                           'Quoted at 4:37, 4:40, 14:46, 24:34, 31:56, 32:01, 39:15, 39:42, 42:22, 47:41 (Sewdass at 31:56, 32:01, 39:15 and 39:42; Schafer at 42:22).'))

def r(*keys):
    return '<sup class="fnref">' + ', '.join(f'<a href="#{k}">{k}</a>' for k in keys) + '</sup>'

def a(url, text):
    return f'<a href="{url}">{text}</a>'

STUDIO = 'https://www.blackrock.com/aladdin/platforms/products/aladdin-studio'
APIS = 'https://www.blackrock.com/aladdin/platforms/products/apis'
SDK = 'https://github.com/blackrock/aladdinsdk'
WOOD = 'https://www.youtube.com/watch?v=Me_H_-E6lSg'
LANG = 'https://www.youtube.com/watch?v=oyqeCHFM5U4'
INV25 = 'https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf'
BVB = 'https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions'
WP = 'https://www.blackrock.com/aladdin/discover/expertise/webinars/unifying-the-whole-portfolio-across-public-and-private-markets'
MS = 'https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/11/how-blackrock-is-finding-new-alpha-as-ai-transformation-becomes-a-critical-business-driver/'
AWS = 'https://press.aboutamazon.com/aws/2025/12/blackrock-partners-with-aws-to-deliver-aladdin-on-secure-scalable-cloud-infrastructure'

parts = []
P = parts.append

# ================================================================ cover
P(f'''
<section class="fullpage cover">
  <p class="prepared-for">Prepared for BlackRock</p>
  <div class="inner">
    <span class="accent-bar"></span>
    <h1>Aladdin Studio, learned with AI</h1>
    <p class="subtitle">What public sources show about the product, where BlackRock is heading, and the quick wins for marketing Studio</p>
    <p class="meta">Prepared by <strong>Jacob Nikolau</strong>&emsp;|&emsp;As of October 19, 2026</p>
  </div>
  <div class="parts">
    <div><span class="accent-bar"></span><p class="pn">Part 1</p><p class="pt"><a href="#part-1">What the public record shows</a></p><p class="pc">Page PG1</p></div>
    <div><span class="accent-bar"></span><p class="pn">Part 2</p><p class="pt"><a href="#f1">Four findings about BlackRock’s direction and market</a></p><p class="pc">Page PG2</p></div>
    <div><span class="accent-bar"></span><p class="pn">Part 3</p><p class="pt"><a href="#part-3">Quick wins for marketing Studio</a></p><p class="pc">Page PG3</p></div>
  </div>
  <p class="indep">Independent analysis compiled from public sources with AI agents. It was not produced, reviewed or endorsed by BlackRock.</p>
</section>
''')

# ================================================================ executive summary
P(f'''
<section class="chapter first" id="executive-summary">
<h2>Executive summary</h2>
<p class="lede">An outsider with AI agents and about a day can assemble a detailed, sourced picture of Aladdin Studio from BlackRock’s own specifications, pages and recordings, plus filings and code. This is what it looks like, what it says about direction, and the quick wins for marketing Studio.</p>
<div class="stats three">
  <div><span class="accent-bar"></span><p class="num">54</p><p class="cap">Public API specifications read, in 11 PyPI packages covering 301 operations</p></div>
  <div><span class="accent-bar"></span><p class="num">128</p><p class="cap">Recordings transcribed and checked, 121 of them from BlackRock’s own channels and partner stages</p></div>
  <div><span class="accent-bar"></span><p class="num">17x</p><p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, from the 2025 Investor Day</p></div>
</div>
<p class="stats-src">Source: {a("https://pypi.org/search/?q=asdk_plugin", "asdk_plugin packages on PyPI")}{r("s1")}; the recordings listed under S in the Source register; {a(INV25, "BlackRock 2025 Investor Day")}{r("s11")}.</p>
<p><b>What was found.</b> Studio is Aladdin’s developer and data layer: APIs and events, a Python SDK on GitHub, and Aladdin Data Cloud on Snowflake, described the same way by five BlackRock speakers since 2024{r("s12","s13","s14","s2")}. Proof of use sits in public records: JPMorgan Chase’s proxy statements, Janus Henderson’s commits and 10-K, Royal London’s chief executive on video, and three pension funds’ tender notices{r("s3","s5","s45","s7","n_ppf")}.</p>
<p><b>What it says about direction.</b> APIs and data access are the growth engine: the fastest-growing measure BlackRock showed investors is API calls{r("s11")}. The product is the whole portfolio, public and private, fed through Data Cloud and Explore{r("n_wp")}. AI stays inside the platform while data providers market connectors outside{r("s23","s15")}. Buyers tell BlackRock’s own webinar they want a core platform plus their own builds{r("s63")}.</p>
<p><b>The quick wins.</b> Named proof from clients whose Aladdin relationship is already public; Studio’s name on the API growth story; a written one-page version of the spoken message; an RFP-ready API answer; a decision on describing the Copilot plugin model; a “what is in the box” summary. None opens the gate.</p>
<div class="method" style="margin-top:4pt">
<h3>What this method can and cannot do</h3>
<p><b>Public material only.</b> BlackRock pages, the 54 specifications inside 11 public <code>asdk_plugin</code> packages, 128 recordings (121 from BlackRock’s own channels and partner stages), SEC filings, procurement notices, GitHub and PyPI. Part is machine-transcribed, and names and jargon can be mis-heard; the register marks which. Figures may be outdated, and there is no internal product context, so conclusions may be wrong for reasons the author cannot see.</p>
<p><b>Enterprise gating is expected.</b> Aladdin is enterprise software sold to large institutions, and gating documentation, sandboxes and credentials behind qualification is the normal model for that market; a qualified prospect gets them from BlackRock’s solutions team. The right-hand column of Exhibit 6 describes the sequence after qualification, not an absence.</p>
<p><b>Three corrections already made.</b> 58 specifications became 54 once the SDK’s four utility APIs were set aside; a widely repeated “68 percent” survey figure was dropped because it could not be found in the report it is attributed to; “more than 2,000 citizen developers” became 3,000, counted inside BlackRock rather than among clients.</p>
</div>
<div class="label-key">
<h3>How to read the receipts</h3>
<p>Underlined text links to the document behind the fact. Each superscript points to the Source register, which gives the grade, title, speaker and date and, for recordings, the minute and second of each quoted passage.</p>
<div class="key-grid">
<div><span class="lbl"><b>P</b> Primary document: a filing, a specification, a page, a notice, GitHub or PyPI</span></div>
<div><span class="lbl e"><b>S</b> BlackRock speaker on the record, with the name and title as given</span></div>
<div><span class="lbl n"><b>T</b> Third-party report: trade press or a secondary summary</span></div>
</div>
</div>
</section>
''')

# ================================================================ Part 1
P(f'''
<section class="chapter part" id="part-1">
<h2><span class="pn">Part 1</span>What the public record shows</h2>
<p>Aladdin is the investment platform BlackRock built for itself and sells to other institutions. Its AI engineering lead put the scale this way at a LangChain conference in 2025: {a(LANG, "“BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries”")}; the organization is “around 7,000 people, with over 4,000 of those being engineers,” who maintain “around 100 Aladdin front-end applications”{r("s18")}. BlackRock’s technology services and subscription revenue was {a("https://www.sec.gov/Archives/edgar/data/2012383/000119312526071966/blk-20251231.htm", "$2.0 billion in 2025")}, up 24 percent with Preqin{r("s19")}. It is enterprise software, sold to large institutions through a solutions team; documentation, sandboxes and credentials follow qualification, which is the normal model in that market. BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code.</p>
''')
P(FIG[1])
P(f'''
<p>BlackRock’s own definition comes from the head of Studio engineering, on Snowflake’s podcast in November 2025. It has three parts.</p>
<div class="script"><p>“So we think about Aladdin today as a platform and Aladdin Studio is essentially the user experience that allows people to think of Aladdin as a platform. It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake takes all of that information that’s generated through our analytics factory and inside of Aladdin and pushes that into Snowflake. And increasingly we’re building a set of developer tools.”</p><p>— {a(WOOD, "Dave Woodhead, Managing Director and Head of Engineering for Aladdin Studio")}, Snowflake Data Cloud podcast, published November 11, 2025{r("s2")}</p></div>
<p class="lead-in">Exhibit 2 follows one trade through that platform, as far as the public specifications describe it: who acts, where BlackRock names a product or application, and which of the 54 APIs covers each step{r("s1","s70")}.</p>
''')
P(FIG[2])
P(FIG[3])
P(FIG[4])
P(FIG[5])
P(f'''
<p>The specifications say more than their count. Every one is tagged <code>Access.Internal</code>, a label BlackRock does not explain in public{r("s1")}. Posting an order takes <code>whatIf</code> and <code>runCompliance</code>, which defaults to true, and returns compliance violations inline{r("s1")}. Ten specifications expose a long-running-operations endpoint and 35 operations are flagged for it; the {a(SDK, "SDK polls them")}{r("s9")}. Risk exceptions and ADC datasets carry bitemporal fields; rule assignments and dataset releases name a four-eyes approval{r("s1")}. Every request carries an application key plus OAuth 2.0 scopes such as <code>trading.order_management.order.v1.Order:read</code>, and the {a(SDK, "client ID and secret come from the Studio UI")}{r("s9")}.</p>

<h3>What is out there before a conversation starts</h3>
<p>Exhibit 6 follows a prospect’s engineer through six steps, from first hearing about Studio to getting help, and records what is out there at each step and what follows qualification. A qualified prospect gets documentation, a sandbox and credentials through BlackRock’s solutions team; the right-hand column is that sequence, not a gap.</p>
<p>The SDK is the one piece that installs before any conversation. It has had {a("https://pypi.org/project/aladdinsdk/#history", "14 releases since May 2024")}, all alpha or beta, with the core at 2.0.0b10 in July 2026 and the add-ons at 2.0.0b3{r("s30","s1")}. Each release pins an old Snowflake library, so none installs on Python 3.13, and the SDK’s dependencies {a("https://github.com/blackrock/aladdinsdk/pull/57", "conflict with the official MCP toolkit")}; an outside fix was merged in August 2026 and has not shipped{r("s31")}. The README documents three run modes, “a developer’s local machine,” {a(SDK, "“Aladdin Studio Compute sessions”")} and a test mode, stores a prompted password in the operating system’s credential manager, and carries settings for firms that consume “the Aladdin APIs via an enterprise API management platform such as Azure API Management”{r("s9")}. These are the needs of a client’s engineering team.</p>
<figure class="exhibit" id="exhibit-106"><p class="ex-title"><span class="ex-num">Exhibit 6.</span> Six steps a prospect’s developer takes, before and after qualification</p>
<table>
<colgroup><col style="width:52pt"><col style="width:160pt"><col style="width:126pt"><col></colgroup>
<thead><tr><th>Step</th><th>Out there today</th><th>After qualification</th><th>Receipt</th></tr></thead>
<tbody>
<tr><td class="first">Hear</td><td>Podcasts, webinar replays, client videos and conference talks on BlackRock’s site and partner channels</td><td>Client forums and the solutions team</td><td>{a("https://www.blackrock.com/aladdin/discover/expertise/never-done-podcast-by-aladdin", "Never Done")}{r("s28")}, {a("https://www.blackrock.com/aladdin/discover/expertise/big-little-questions", "Big Little Questions")}{r("s29")}, {a(WOOD, "Woodhead")}{r("s2")}, {a(LANG, "Rosales and Valdez")}{r("s18")}</td></tr>
<tr><td class="first">Read</td><td>The Studio page: “Create &amp; automate,” “Make Aladdin your own,” “Align internally &amp; externally”; the APIs page: “dozens of APIs”</td><td>The Developer Portal and the API framework guides</td><td>{a(STUDIO, "Studio page")}{r("s8")}, {a(APIS, "APIs page")}{r("s26")}</td></tr>
<tr><td class="first">See the catalog</td><td>54 specifications, by unpacking the 11 PyPI add-on packages</td><td>The API catalog and the Data Dictionary</td><td>{a("https://pypi.org/search/?q=asdk_plugin", "asdk_plugin packages")}{r("s1")}, {a(APIS, "APIs page")}{r("s26")}</td></tr>
<tr><td class="first">Try</td><td>Nothing to run: no public sandbox or trial is offered</td><td>Studio Compute, an API token or OAuth application “registered via Studio UI,” the client’s Aladdin host</td><td>{a(SDK, "SDK README")}{r("s9")}</td></tr>
<tr><td class="first">Build</td><td>The open-source SDK on GitHub and PyPI, with a detailed README; the plugin builder</td><td>Every call: the SDK needs a client host and credentials</td><td>{a(SDK, "SDK README")}{r("s9")}, {a("https://pypi.org/project/aladdinsdk/#history", "PyPI history")}{r("s30")}, {a("https://github.com/blackrock/aladdinsdk-plugin-builder", "plugin builder")}{r("s27")}</td></tr>
<tr><td class="first">Get help</td><td>GitHub issues and pull requests on the SDK, answered by BlackRock engineers; “Book a meeting” and “Download the brochure”</td><td>Notebooks, code samples, support</td><td>{a("https://github.com/blackrock/aladdinsdk/pull/52", "Pull request 52")}{r("s5")}, {a("https://github.com/blackrock/aladdinsdk/pull/57", "pull request 57")}{r("s31")}, {a(STUDIO, "Studio page")}{r("s8")}</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the pages and repositories in the Receipt column, read with no account or login, October 2026; the right-hand column is what they say a client receives, not tested.</p></div></figure>




''')
heat = retitle(FIG[7], 'Several access models coexist in this market: what a developer with no client relationship can reach, on eight criteria')
heat = heat.replace('<th>Score</th>', '<th>Total</th>').replace('Source: the author’s hands-on test of each platform’s public pages', 'Source: the author’s test of each platform’s public pages').replace(', with no accounts, logins or payments, October 8, 2026. Bloomberg, Clearwater and MSCI may be underrated because some of their pages blocked automated access.', ', no accounts or payments, October 8, 2026. Bloomberg, Clearwater and MSCI may be underrated: some pages blocked automated access.')
heat = heat.replace('Scoring: on each criterion, 2 means fully public or self-serve, 1 means partial, limited, or open only after a free signup or an approval, and 0 means none or blocked. For the AI connector, 2 means an MCP server or connector that outside AI tools can use, 1 means one that is announced or in limited release, and 0 means none, or an assistant that works only inside the vendor’s own platform.', 'For the AI connector, 2 means an MCP server or connector that outside AI tools can use, 1 one announced or in limited release, and 0 none, or an assistant that works only inside the vendor’s own platform.')
P(heat)
P(f'''
<p>Exhibit 7 puts Studio beside ten platforms a Studio buyer also deals with, on eight things a developer with no client relationship can reach{r("s32","s33","s34")}. Investment platforms mostly gate: documentation, a sandbox and a first call follow a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium. Data and cloud platforms, which sell to developers directly, mostly self-serve. Only Studio, among the investment platforms, offers an {a(SDK, "open-source SDK")}{r("s9")}. The exhibit shows each vendor’s model, not a score against Aladdin.</p>
''')
P(f'''
<p>Five BlackRock speakers define Studio on the record in the 128 recordings pulled for this document, with the titles the recordings give{r("s28","s29")}.</p>
''')
P(FIG[8].replace('The three-pillar definition; 3,000 internal citizen developers; “hundreds of Snowflake accounts”', 'The three-pillar definition; 3,000 internal citizen developers').replace('Data Cloud “within 15 minutes of latency”; 3,000 people in the citizen-developer bracket', 'Data Cloud “within 15 minutes of latency”'))
P(f'''
<p>Four of them describe Studio with the same three parts: Woodhead names them outright{r("s2")}; Newman places Data Cloud “part of Studio”{r("s13")}; Goel describes events, APIs and a near-real-time data store{r("s14")}; Khara calls it programmatic access to data and reporting{r("s12")}. A 2026 {a("https://careers.blackrock.com/job/new-york/senior-product-director-aladdin-studio-developer/45831/96232273856", "job posting")} calls Studio “Aladdin’s extensibility layer”{r("s67")}. The message is consistent across speakers and years, so the positioning exists. Learning about Studio from outside takes effort: the catalog is unpacked from packages, the definitions transcribed from recordings, and nothing can be run; that fits how Aladdin is sold, through a solutions team to qualified institutions, after a conversation.</p>
''')
P(FIG[15].replace(' on a programmatic basis at machine scale, over and above what they get through our front end applications”', ' on a programmatic basis”').replace('“The Aladdin data cloud specifically ... which is part of Studio”; “we’re releasing soon the ability to actually access those analytic APIs ... That’s all part of the Studio umbrella”', '“The Aladdin data cloud ... which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella”').replace('“Every single transaction that happens should be available and accessible to you via an event, via an API”; ADC as “a near real time data store ... within 15 minutes of latency”; exposing “the software and application that we’re building”', '“Every single transaction ... via an event, via an API”; “a near real time data store”; exposing “the software and application that we’re building”').replace('“It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... And increasingly we’re building a set of developer tools”', '“It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... developer tools”').replace('Quotations are verbatim from the transcripts; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked in the register.', 'Quotations are verbatim; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked in the register.'))
P('''
</section>
''')

# ================================================================ Part 2: findings
# ---- Finding 1
P(f'''
<section class="chapter finding" id="f1">
<h2>1. Public customer proof already exists, and it is viable even though it is not Studio-specific</h2>
<p>BlackRock’s {a(STUDIO, "Studio page")} names no client as building on Studio{r("s8")}, and a {a("https://www.sec.gov/edgar/search/#/q=%22Aladdin%20Studio%22", "full-text search of SEC EDGAR")} finds no filing that mentions it{r("s40")}. Proof of Aladdin in use is public all the same. On BlackRock’s own client video, Royal London’s chief executive credits {a("https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management", "the Snowflake implementation")}{r("s7")}. JPMorgan Chase reports its Aladdin payments in its {a("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A", "proxy statement")} every year: $4.4 million to $7.6 million from 2017 to 2023, then $14.7 million in 2024 and {a("https://www.sec.gov/Archives/edgar/data/19617/000001961726000096/jpm-20260402.htm", "$25.6 million in 2025")}{r("s4","s3")}.</p>
''')
P(FIG[9].replace('height="186.3pt"', 'height="111.8pt"').replace('width="443.5pt"', 'width="266.1pt"'))
P(f'''
<p>In December 2025 a Janus Henderson engineer submitted two changes to the {a(SDK, "open-source SDK")}, {a("https://github.com/blackrock/aladdinsdk/pull/52", "URL rewriting")} and {a("https://github.com/blackrock/aladdinsdk/pull/53", "custom headers")}, for firms that route Aladdin calls through an enterprise gateway; the BlackRock engineer who co-wrote the SDK’s {a("https://engineering.blackrock.com/open-sourcing-the-aladdinsdk-empower-python-developers-with-a-quantitative-edge-7f63376061e6", "launch post")} merged them, and the {a("https://github.com/blackrock/aladdinsdk/commit/1c1bd2559e4e4da2591f13dccfd7db6c2f9dc68c.patch", "commits")} carry a janushenderson.com author line{r("s5","s6","s42","s44")}. Janus Henderson’s {a("https://www.sec.gov/Archives/edgar/data/1274173/000143774926005628/jhg20251231_10k.htm", "10-K")} says the firm chose in the third quarter of 2025 to move its investment management system to Aladdin, “a complex, multi-year initiative”{r("s45")}. Public buyers add a third record: procurement notices that score the bids.</p>
<figure class="exhibit" id="exhibit-111"><p class="ex-title"><span class="ex-num">Exhibit 11.</span> Public buyers that scored Aladdin bids</p>
<table>
<colgroup><col style="width:150pt"><col style="width:60pt"><col><col style="width:160pt"></colgroup>
<thead><tr><th>Buyer</th><th>Year</th><th>Scoring</th><th>Outcome</th></tr></thead>
<tbody>
<tr><td class="first">{a("https://www.find-tender.service.gov.uk/Notice/062522-2025", "UK Pension Protection Fund")}{r("n_ppf")}</td><td>2025</td><td>Technical 85, price 6, price sensitivity 6, contract terms 3</td><td>Aladdin won both lots, above the fund’s own price estimate</td></tr>
<tr><td class="first">{a("https://www.find-tender.service.gov.uk/Notice/035311-2023", "Nest (UK)")}{r("n_nest")}</td><td>2023</td><td>Quality 70, cost 20, social value 10</td><td>Aladdin won against six other bids</td></tr>
<tr><td class="first">{a("https://api.usaspending.gov/api/v2/awards/CONT_AWD_16PBGC23C0006_1665_-NONE-_-NONE-/", "US Pension Benefit Guaranty Corporation")}{r("n_pbgc")}</td><td>2017 and 2023</td><td>Full and open competition, four bids each time</td><td>BlackRock won both; the 2023 rebid kept the same price</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: UK Find a Tender{r("n_ppf","n_nest")}; USAspending.gov{r("n_pbgc")}. Weights and outcomes are from an earlier draft of this research (October 2026) and its reading of the notices, not re-pulled; the 2023 PBGC record was re-read on October 19, 2026.</p></div></figure>
<p>None of this is Studio-specific, and that matters less than it looks. Studio is sold for custom applications on Aladdin, and a buyer wants to know that another institution built on the platform and stayed; in custom-application land, proof from one firm counts even for a dissimilar buyer. Public pension funds, and firms whose filings or tenders already name BlackRock, can go public more easily, and are the natural first candidates for a named Studio story.</p>
<div class="gtm"><p><span class="lead">What it suggests about direction.</span> Adoption is growing in client types whose records are public: a bank’s proxy statement, an asset manager’s 10-K and three pension funds’ notices all record Aladdin between 2023 and 2025. Named proof for Studio can start where the relationship is already on the record.</p></div>
</section>
''')

# ---- Finding 2
P(f'''
<section class="chapter finding" id="f2">
<h2>2. BlackRock’s growth story is API consumption and the whole portfolio, and Studio is the vehicle even when it is not named</h2>
<p>At its {a(INV25, "2025 Investor Day")}, BlackRock projected that API calls across BlackRock and Aladdin would grow 17 times by 2030, against four times for model portfolios, two times for portfolios and 1.3 times for trade allocations; the slide gave no starting number{r("s11")}. API use is the activity the {a(STUDIO, "Studio page")} describes{r("s8")}. The investor story is told without the product’s name. Across {a("https://www.roic.ai/quote/BLK/transcripts", "26 earnings calls")} from the first quarter of 2020 to the second quarter of 2026, no executive said “Studio”{r("s10")}; a single line on a {a("https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BlackRock-2023-Investor-Day.pdf", "2023 Investor Day slide")} is the only other investor mention found{r("s47")}. BlackRock’s {a("https://www.sec.gov/Archives/edgar/data/2012383/000119312526071966/R41.htm", "10-K")} says technology services fees are generally set by the value of positions on the platform or at a fixed rate, and can depend on subscriptions, go-lives and support; API calls appear in none of those terms{r("s19","s11")}. Exhibit 12 is an observation about how the story is told.</p>
''')
P(FIG[10])
P(f'''
<p>The other half of the growth story is the whole portfolio. BlackRock bought eFront in 2019 and Preqin in 2025, and in September 2025 its private markets team described the result on a {a(WP, "client webinar")}: investors “now have access to over 15,000 fund investments within eFront Insight” for benchmarking; Preqin indices “are also available today in Aladdin Explore and our Aladdin Data Cloud capabilities”; and “over 10 different transaction types” were added to Aladdin, across commitments, fundings, pay-downs and PIK, so private credit loans are captured natively, designed with BlackRock’s own professionals and “our new colleagues from HPS”{r("n_wp")}. {a("https://www.preqin.com/about/press-release/blackrock-aladdin-expands-private-credit-solutions-on-preqin-for-greater-transparency-and-insights-across-the-asset-class", "Private credit analytics on Preqin")} followed in May 2026{r("s21")}. Newman lists eFront data and Preqin among what is joining Data Cloud{r("s13")}. Hosting moved the same way: Microsoft wrote in December 2024 that {a(MS, "all BlackRock’s technology platform clients and services are hosted in the Azure cloud")}, with new rollouts taking “weeks instead of quarters”{r("n_ms")}, and in December 2025 BlackRock and AWS announced a second option, with {a(AWS, "general availability for US-hosted Aladdin Enterprise clients expected in the second half of 2026")}{r("s22")}.</p>
<div class="gtm"><p><span class="lead">What it suggests about direction.</span> Extensibility and data access are where BlackRock itself says growth is. The fastest-growing measure it showed investors is API calls, and the data it is adding, private markets and Preqin, arrives through Data Cloud and Explore, which are Studio’s surfaces. Studio is the vehicle for that story whether or not the name appears.</p></div>
</section>
''')

# ---- Finding 3
funnel = FIG[13]
funnel = funnel[:funnel.index('<p class="ex-sub">')] + funnel[funnel.index('<div class="notes">'):]
funnel = re.sub(r'<div class="notes">.*?</div></figure>',
    '<div class="notes"><p><span class="lbl e"></span>Source: Rosales and Valdez at LangChain Interrupt 2025' + r("s18") + '; the Copilot page' + r("s23") + '. The tool counts are the speakers’ own approximations; the talk is a machine transcription, marked in the register.</p></div></figure>', funnel, flags=re.S)
P(f'''
<section class="chapter finding" id="f3">
<h2>3. BlackRock has built an AI front door and keeps it inside the platform, while data providers market theirs outside</h2>
<p>{a("https://www.blackrock.com/aladdin/platforms/products/aladdin-copilot", "Aladdin Copilot")} is “now available to all Aladdin clients” and “will not give investment advice or respond to questions outside Aladdin platform boundaries”{r("s23")}. Its engineers describe a plugin registry with {a(LANG, "“couple of thousands agents and tools”")}, where the first way a team onboards is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production”{r("s18")}. Copilot’s tools are Studio’s APIs; Microsoft’s Adrian Crockett put it in one line on BlackRock’s podcast: {a("https://www.blackrock.com/aladdin/discover/podcast/microsoft-part-2-podcast", "“There’s no copilot without plug-ins”")}{r("s61")}. BlackRock’s AI product head says the team is making sure {a("https://www.blackrock.com/aladdin/discover/podcast/reducing-time-to-insight-how-ai-is-reshaping-risk-management", "“the data model itself is structured for agentic use cases”")}{r("s62")}.</p>
''')
P(funnel)
P(f'''
<p>Outside the login, the data market has chosen the other model. {a("https://modelcontextprotocol.io/", "MCP")} is the common standard AI assistants use to pull data from other systems{r("s53")}. Seven providers a Studio buyer also talks to offer a connector or an MCP server; LSEG had {a("https://www.investing.com/news/company-news/lseg-q1-2026-slides-record-growth-ai-adoption-accelerates-93CH-4631412", "90 customers connected")} by April 2026, according to a secondary summary of its results slides{r("s54","s16")}. No public connector for Aladdin was found on BlackRock’s pages or GitHub{r("s8","s55")}; a {a("https://careers.blackrock.com/job/mumbai/forward-deploy-engineer-aladdin-data-associate/45831/97466309856", "Forward Deploy Engineer posting")} for Aladdin Data names “Model Context Protocol (MCP), AI agents, and Copilot extensions”{r("s60")}.</p>
''')
P(FIG[12])
P(f'''
<figure class="exhibit" id="exhibit-115"><p class="ex-title"><span class="ex-num">Exhibit 15.</span> Two sides of the AI front door</p>
<table>
<colgroup><col style="width:44pt"><col><col></colgroup>
<thead><tr><th></th><th>Inside the login: Copilot plugins on production APIs</th><th>Outside the login: a connector or MCP server for the buyer’s own AI tools</th></tr></thead>
<tbody>
<tr><td class="first">For</td><td>Governance in one place; inherited permissions (“permission-dependent access”); no-advice guardrails tested in the system prompt; enterprise trust; a controlled rollout team by team{r("s23","s18")}</td><td>Discoverability; developer pull; an ecosystem signal; a ready answer to the RFP question about connectors; the terms FactSet, LSEG and MSCI now set{r("s15","s16","s17","s63")}</td></tr>
<tr><td class="first">Against</td><td>Invisible to prospects and to the AI tools buyers already use; rivals set the terms of comparison; the plugin model is described only in a conference talk{r("s18")}</td><td>A larger security surface; support cost; a partial catalog exposed and read as the whole; regulatory optics for a platform that will not give advice{r("s23")}</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the author’s reading of the Copilot page{r("s23")}, the LangChain talk{r("s18")}, the provider announcements in Exhibit 14 and the Build vs. Buy webinar{r("s63")}.</p></div></figure>
<div class="gtm"><p><span class="lead">What it suggests about direction.</span> The choice is deliberate and consistent with the governance message: permission-dependent access, content filtering, no investment advice. The open question is timing and description, not access: when BlackRock describes how clients’ own AI tools will reach Aladdin, and in what words, while rivals set the terms of that comparison.</p></div>
</section>
''')

# ---- Finding 4
P(f'''
<section class="chapter finding" id="f4">
<h2>4. Buyers say they want a core platform plus their own builds, and rivals are selling to that</h2>
<p>BlackRock’s own Build vs. Buy webinar polled its attendees. In the first poll, 37 percent said they run “mostly vendor platforms,” 30 percent “hybrid,” 18 percent were “actively reevaluating” and 15 percent were “mostly built in house”{r("s63")}. Asked what is driving the decision, “AI and data demands” led at 42 percent, with cost and speed to market tied behind it{r("s63")}. Asked what they would stop maintaining internally, 53 percent chose compliance reporting{r("s63")}. The host read from the slide that 60 to 70 percent of technology cost sits in “maintenance of current systems,” and the Alpha FMC panellist said a transformation runs “roughly 12 to 18 months”{r("s63")}.</p>
''')
P(FIG[14])
P(f'''
<div class="script"><p>“What’s the API suite that you have? Are you using connectors to Snowflake or to Databricks? And I think that that part of the RFP has become much more prominent.”</p><p>— {a(BVB, "Clark Schafer, Partner, Alpha FMC")}, on the Build vs. Buy webinar{r("s63")}</p></div>
<p>BlackRock’s head of solutions engineering for the Americas answered on the same webinar. {a(BVB, "“That word monolith is definitely being challenged in the market,”")} she said; the shift of the last two years is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows,” with “very, very robust APIs that manage the end to end life cycle of a transaction” so that clients can build “their secret sauce rebalancing tools” on top{r("s63")}. On AI, “you need that system of record that underpins anything that AI is built upon,” and “the other layer that is almost equally important is a really defined system of work”{r("s63")}. Rivals are selling to the same buyer. SimCorp announced wins at {a("https://alliancebernsteinholdinglp.gcs-web.com/news-releases/news-release-details/alliancebernstein-selects-simcorp-one-technology-platform", "AllianceBernstein")} in February 2026 and {a("https://www.simcorp.com/about-us/news/2026/pictet-asset-management-selects-simcorp-one", "Pictet")} in May 2026; AllianceBernstein keeps its “specialized in-house technology,” and Pictet connects its own tools to SimCorp One by API{r("s64","s65")}. BlackRock’s {a("https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework", "August 2026 insight")} says “Build vs buy is no longer a binary question”{r("s66")}.</p>
<div class="gtm"><p><span class="lead">What it suggests about direction.</span> Extensibility is now an RFP question, asked in those words, and Studio is BlackRock’s answer: the APIs, events and Data Cloud that Sewdass describes are the pieces in Exhibit 4. The buyer’s question and the product already match. The quick wins put the answer where the buyer is asking.</p></div>
</section>
''')

# ================================================================ Part 3
P(f'''
<section class="chapter part" id="part-3">
<h2><span class="pn">Part 3</span>Based on this, the quick wins in marketing Studio</h2>
<p>Each quick win uses what is already public or already true inside BlackRock, works inside the enterprise selling model, and changes nothing about what a prospect can access. None opens the gate: documentation, sandboxes and credentials stay with the solutions team, after qualification. Product owns what is built and when; marketing owns positioning, stories and sales material; compliance checks the final version.</p>
<figure class="exhibit" id="exhibit-117"><p class="ex-title"><span class="ex-num">Exhibit 17.</span> Quick wins</p>
<table>
<colgroup><col style="width:92pt"><col style="width:62pt"><col><col style="width:78pt"><col style="width:96pt"></colgroup>
<thead><tr><th>Quick win</th><th>Why</th><th>What it takes</th><th>Owner</th><th>Measure</th></tr></thead>
<tbody>
<tr><td class="first">A named-proof programme, starting where the relationship is already public</td><td>Finding 1</td><td>Shortlist clients whose Aladdin relationship is on the record: tender winners (the Pension Protection Fund, Nest, PBGC), filers (JPMorgan Chase, Janus Henderson) and Royal London, which is already on video{r("n_ppf","s3","s45","s7")}. Ask each for one Studio-specific sentence or one build. Accept proof from a dissimilar firm; a pension fund’s story serves an insurer</td><td>Marketing, with the client business for introductions</td><td>Named references in use; deals in which one was cited</td></tr>
<tr><td class="first">Studio’s name on the API growth story</td><td>Finding 2</td><td>Agree one measure with investor relations and product, built on the API-call projection{r("s11")}, and put Studio’s name beside it in investor and client materials</td><td>Product with investor relations; marketing writes the story</td><td>Studio named beside the measure in the next investor and client decks</td></tr>
<tr><td class="first">A written one-page version of the spoken message</td><td>Part 1</td><td>Turn the three-part definition four speakers already give{r("s2","s13","s14","s12")} into one written page, reviewed by product and compliance, used in every deck and page</td><td>Marketing</td><td>One page adopted; no deck or page that contradicts it</td></tr>
<tr><td class="first">An RFP-ready “API suite” answer for qualified buyers</td><td>Finding 4</td><td>A document that answers the question Schafer says buyers now ask{r("s63")}: the domains, counts and status of the catalog, connectors to Snowflake and Databricks, how clients build on top. Delivered by the solutions team after qualification</td><td>Solutions engineering, with marketing</td><td>Time to answer the API question in an RFP; RFPs in which it is used</td></tr>
<tr><td class="first">A decision on when and how to describe the Copilot plugin model publicly</td><td>Finding 3</td><td>A description, not access: how Copilot’s tools map to production APIs{r("s18")}, what governance applies{r("s23")}, and how clients will connect their own AI tools, timed with the Forward Deploy Engineer work{r("s60")}</td><td>Product with marketing; compliance review</td><td>A public description exists; prospects stop asking the question in rivals’ words</td></tr>
<tr><td class="first">A prospect-facing “what is in the box” summary</td><td>Part 1</td><td>One page listing the 11 domains with counts and status, as in Exhibit 5{r("s1")}, with no specifications; shared before the first meeting or on the Studio page</td><td>Marketing, with product</td><td>First meetings that start past scope; prospects who arrive with the list</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the author’s proposals, built on Part 1 and Findings 1 to 4. Receipts in the table point to the public facts each win rests on.</p></div></figure>

<h3>What I would need from inside</h3>
<p>Five questions need internal data that no public source holds. The answers would confirm or correct the findings before any of the wins is sized.</p>
<figure class="exhibit" id="exhibit-118"><p class="ex-title"><span class="ex-num">Exhibit 18.</span> Five questions for internal data</p>
<table>
<colgroup><col style="width:300pt"><col></colgroup>
<thead><tr><th>Question</th><th>What the answer would decide</th></tr></thead>
<tbody>
<tr><td class="first">How many clients have active API credentials or a Data Cloud instance, and how has that changed since 2024?</td><td>The baseline for every measure in Exhibit 17</td></tr>
<tr><td class="first">Which clients would agree to be named, and what usually stops them?</td><td>How soon the named-proof programme can start</td></tr>
<tr><td class="first">What does the <code>Access.Internal</code> tag on every public specification mean, and does it limit what can be described without a login?</td><td>What the “what is in the box” summary may say</td></tr>
<tr><td class="first">How will clients connect their own AI tools to Aladdin, and is the Forward Deploy Engineer work the path?</td><td>The timing of the Copilot description</td></tr>
<tr><td class="first">Where does adoption stall most: awareness, the first API call, or getting a build into production?</td><td>Where marketing spends first: content, enablement or client success</td></tr>
</tbody></table>
<div class="notes"><p><span class="lbl"></span>Source: the author’s questions. Question 3 refers to the tag on the public specifications{r("s1")}; question 4 to the job posting that names MCP{r("s60")}.</p></div></figure>
<p>On method: AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted; the author checked each claim against the document or recording it cites and takes responsibility for the reading. Public sources are limited, can be out of date and carry no internal product context, and machine transcription and synthesis are imperfect. The conclusions may be wrong for reasons the author cannot see, and the five questions above are where that would show first.</p>
</section>
''')

body = ''.join(parts)

# ================================================================ exhibit renumbering (document order)
ex_ids = re.findall(r'id="(exhibit-\d+)"', body)
assert len(ex_ids) == len(set(ex_ids)), ex_ids
ex_map = {old_id: i + 1 for i, old_id in enumerate(ex_ids)}
def ex_sub(m):
    return f'id="EXTMP{ex_map[m.group(1)]}"'
body = re.sub(r'id="(exhibit-\d+)"', ex_sub, body)
# renumber the visible "Exhibit N." in order of appearance
counter = iter(range(1, 100))
body = re.sub(r'<span class="ex-num">Exhibit \d+\.</span>', lambda m: f'<span class="ex-num">Exhibit {next(counter)}.</span>', body)
body = body.replace('EXTMP', 'exhibit-')
# cross references in prose: map old exhibit numbers mentioned in text to new ones
# (new text was written against the new numbering already; the reused exhibit notes do not cross-refer)

# ================================================================ source renumbering (order of first citation)
order = []
for m in re.finditer(r'<sup class="fnref">(.*?)</sup>', body, flags=re.S):
    for k in re.findall(r'href="#([a-z_0-9]+)"', m.group(1)):
        if k not in order: order.append(k)
missing = [k for k in order if k not in REG]
assert not missing, missing
num = {k: i + 1 for i, k in enumerate(order)}
def sup_sub(m):
    inner = m.group(1)
    inner = re.sub(r'<a href="#([a-z_0-9]+)">[^<]*</a>', lambda mm: f'<a href="#s{num[mm.group(1)]}">{num[mm.group(1)]}</a>', inner)
    return f'<sup class="fnref">{inner}</sup>'
body = re.sub(r'<sup class="fnref">(.*?)</sup>', sup_sub, body, flags=re.S)
unused = [k for k in REG if k not in num]

groups = {'P': 'P. Primary documents', 'S': 'S. BlackRock speakers on the record', 'T': 'T. Third-party reports'}
reg_html = []
for g in 'PST':
    reg_html.append(f'<h3>{groups[g]}</h3>')
    for k in sorted([k for k in order if REG[k][0] == g], key=lambda k: num[k]):
        reg_html.append(f'<p id="s{num[k]}"><b class="n">{num[k]}</b>{REG[k][1]}</p>')

register = f'''
<section class="chapter runon" id="sources">
<h2>Source register</h2>
<p class="front-note">Numbered in order of first citation and grouped by grade. P is a primary document; S is a BlackRock speaker on the record, with the name and title as the recording gives them; T is a third-party report. “Machine transcription” means a local transcription of the downloaded audio; “auto-captions” means YouTube’s captions. In both, names and jargon can be mis-heard, and only caption misspellings of proper names were corrected inside quotations. For recordings, the entry gives the minute and second at which each quoted passage begins.</p>
<div class="register">
{chr(10).join(reg_html)}
</div>
</section>

<section class="fullpage back">
  <div class="inner">
    <span class="accent-bar"></span>
    <h2>About this document</h2>
    <p>Independent analysis compiled from public sources: BlackRock product pages, SEC filings, procurement notices, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings. It was not produced, reviewed or endorsed by BlackRock.</p>
    <p>AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted the text. The author checked each claim against the document or recording it cites. Public material is limited, can be out of date and carries no internal product context; machine transcription and synthesis are imperfect; the conclusions may be wrong for reasons the author cannot see.</p>
    <p>Facts are as of October 19, 2026, unless an exhibit gives another date. Underlined text links to the document behind each fact. Superscripts point to the Source register, which gives the grade, the title, the speaker and the date of every source.</p>
    <p>Three corrections were made against earlier drafts of this research: 58 API specifications became 54 once the SDK’s four utility APIs were set aside; a widely repeated “68 percent” survey figure was dropped because it could not be found in the report it is attributed to; and “more than 2,000 citizen developers” became 3,000, counted inside BlackRock rather than among clients.</p>
    <p>The quick wins and questions in Part 3 are the author’s proposals, based on Part 1 and the findings in Part 2.</p>
    <p>BlackRock and Aladdin are registered trademarks of BlackRock, Inc. Other company and product names are the property of their owners.</p>
    <p>Set in Barlow and Barlow Condensed, open-license stand-ins for BlackRock’s licensed BLK Fort typeface. Code is set in IBM Plex Mono.</p>
  </div>
</section>

</body></html>
'''

# page numbers on the cover, passed in as arguments
pg = dict(zip(['PG1', 'PG2', 'PG3'], sys.argv[1:4])) if len(sys.argv) >= 4 else {'PG1': '3', 'PG2': '10', 'PG3': '15'}
for k, v in pg.items(): body = body.replace(k, v)

wp_times = sys.argv[4] if len(sys.argv) >= 5 else 'WP_TIMES'
register = register.replace('WP_TIMES', wp_times)

open(OUT, 'w', encoding='utf-8').write(head + body + register)
print('exhibits:', len(ex_ids), ' sources cited:', len(order), ' unused old entries:', unused)
