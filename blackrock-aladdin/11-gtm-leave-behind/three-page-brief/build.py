#!/usr/bin/env python3
"""Build the three-page executive brief from the Prep 2 source.

Reuses the Prep 2 <head> (embedded Barlow fonts, colour tokens, base print
styles) and adds a small stylesheet for the brief's own layout.
Sources keep the Prep 2 register's titles and URLs and are renumbered in
order of first use. ORIG maps each brief number to its Prep 2 number.
"""
import pathlib, re

ROOT = pathlib.Path('/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad')
SRC = ROOT / 'edits5/work.html'
OUT = ROOT / 'brief3/Aladdin_Studio_brief.html'

src = SRC.read_text()
head = src[:src.index('</head>')]
head = re.sub(r'<title>.*?</title>', '<title>Aladdin Studio from the outside</title>', head, flags=re.S)

# ---------------------------------------------------------------- sources
# key: (Prep 2 number, short label for the page source line, URL)
REG = {
    'woodhead': (1, 'Dave Woodhead, Head of Engineering for Aladdin Studio, Snowflake Data Cloud podcast, Nov. 11, 2025',
                 'https://www.youtube.com/watch?v=Me_H_-E6lSg'),
    'studio': (14, 'BlackRock, Aladdin Studio product page, as of Oct. 2026',
               'https://www.blackrock.com/aladdin/platforms/products/aladdin-studio'),
    'apis': (30, 'BlackRock, Aladdin APIs product page, as of Oct. 2026',
             'https://www.blackrock.com/aladdin/platforms/products/apis'),
    'specs': (6, 'asdk_plugin_* packages, version 2.0.0b3, 11 packages holding 54 Swagger 2.0 specifications, PyPI, unpacked Oct. 2026',
              'https://pypi.org/search/?q=asdk_plugin'),
    'adc': (20, 'BlackRock, Aladdin Data Cloud product page, as of Oct. 2026',
            'https://www.blackrock.com/aladdin/platforms/products/aladdin-data-cloud'),
    'sdk': (29, 'AladdinSDK README and source, github.com/blackrock/aladdinsdk, as of Oct. 19, 2026',
            'https://github.com/blackrock/aladdinsdk'),
    'portal': (44, 'Aladdin developer portal, checked Oct. 20, 2026 (redirects to the client login)',
               'https://www.blackrock.com/apps/aladdin-developer-portal/'),
    'atx': (32, 'BlackRock, ATX: Aladdin Tools for Excel product page, as of Oct. 20, 2026',
            'https://www.blackrock.com/aladdin/platforms/products/aladdin-tools-for-excel'),
    'webinar': (10, 'BlackRock, “Build vs. Buy: How Asset Managers Are Rethinking Key Decisions Today,” webinar replay dated June 2026, published captions',
                'https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions'),
    'simcorp': (7, 'SimCorp, “Introducing Agent Launchpad,” 2026',
                'https://www.simcorp.com/about-us/news/2026/introducing-agent-launchpad'),
    'arcesium': (75, 'Arcesium, “Arcesium unveils new suite of AI features in Aquata,” press release, 2025',
                 'https://www.arcesium.com/press-release/arcesium-unveils-new-suite-of-ai-features-in-aquata'),
    'bloomberg': (77, 'Bloomberg, “Bloomberg Launches Enterprise MCP…,” press release, Sept. 29, 2026',
                  'https://www.prnewswire.com/news-releases/bloomberg-launches-enterprise-mcp-to-seamlessly-connect-bloomberg-data-with-clients-enterprise-ai-applications-302891331.html'),
    'pr52': (56, 'Pull request 52, URL rewriting for enterprise API gateways, blackrock/aladdinsdk, Dec. 2025',
             'https://github.com/blackrock/aladdinsdk/pull/52'),
    'pr53': (57, 'Pull request 53, additional HTTP headers, blackrock/aladdinsdk, Dec. 2025',
             'https://github.com/blackrock/aladdinsdk/pull/53'),
    'jhg': (53, 'Janus Henderson Group, Form 10-K for fiscal 2025, SEC EDGAR',
            'https://www.sec.gov/Archives/edgar/data/1274173/000143774926005628/jhg20251231_10k.htm'),
    'edgar': (49, 'Full-text search of SEC EDGAR for “Aladdin Studio,” run Oct. 2026',
              'https://www.sec.gov/edgar/search/#/q=%22Aladdin%20Studio%22'),
    'rosales': (9, 'Brennan Rosales and Pedro Vicente Valdez, BlackRock, LangChain Interrupt 2025, machine transcription',
                'https://www.youtube.com/watch?v=oyqeCHFM5U4'),
}
NUM = {}            # key -> brief number
PAGE_USED = {}      # page -> ordered keys first used on that page
cur_page = [1]


def c(*keys):
    """Superscript citation. Each number links straight to the source."""
    out = []
    for k in keys:
        if k not in NUM:
            NUM[k] = len(NUM) + 1
        if k not in PAGE_USED.setdefault(cur_page[0], []):
            PAGE_USED[cur_page[0]].append(k)
        n = NUM[k]
        out.append(f'<a href="{REG[k][2]}">{n}</a>')
    return '<sup class="fnref">' + ', '.join(out) + '</sup>'


def srcline(page):
    keys = sorted(PAGE_USED.get(page, []), key=lambda k: NUM[k])
    items = [f'<span><b>{NUM[k]}</b> <a href="{REG[k][2]}">{REG[k][1]}</a></span>' for k in keys]
    return '<div class="srcs"><span class="lb">Sources</span> ' + ' '.join(items) + '</div>'


CSS = r"""
<style>
@page{
  size:612pt 792pt; margin:40pt 50pt 50pt 50pt;
  @bottom-left{content:"Independent analysis of public sources. Not produced, reviewed or endorsed by BlackRock.";
    font-family:"Barlow Condensed"; font-weight:300; font-size:7.5pt; color:#595959; vertical-align:top; padding-top:4pt}
  @bottom-right{content:counter(page); font-family:"Barlow"; font-weight:400; font-size:9pt; color:#000; vertical-align:top; padding-top:2pt}
}
body{font-size:10pt; line-height:13pt}
.pg{break-after:page; display:flex; flex-direction:column; height:702pt}
.pg:last-child{break-after:auto}
.pg .grow{flex:1}
p{margin:0 0 7pt}
.mast .accent-bar{margin:0 0 10pt}
.mast h1{font-weight:800; font-size:22pt; line-height:25pt; margin:0 0 3pt}
.mast .sub{font-size:12pt; line-height:15pt; margin:0 0 4pt}
.mast .by{font-family:var(--font-cond); font-weight:400; font-size:9pt; line-height:11pt; color:var(--ink-2); margin:0 0 8pt}
.intro{font-size:10.5pt; line-height:13.5pt; margin:0 0 6pt; padding:0 0 8pt; border-bottom:.75pt solid var(--series-gray)}
h2.hl{font-weight:800; font-size:15pt; line-height:18pt; margin:8pt 0 5pt}
h2.hl::before{content:""; display:block; width:40pt; height:5pt; background:var(--yellow); margin:0 0 8pt}
.pg.first h2.hl::before{display:none}
h3.sh{font-weight:800; font-size:10.5pt; line-height:13pt; margin:9pt 0 4pt}
.exhibit{margin:6pt 0 6pt; padding-top:5pt}
.exhibit > .ex-title{font-size:10pt; line-height:12pt; margin:0 0 5pt}
.notes{font-size:8pt; line-height:9.6pt; margin:4pt 0 0}
/* page 1 diagram */
.studio-dg .cap{font-family:var(--font-cond); font-weight:700; font-size:7.5pt; letter-spacing:.06em; text-transform:uppercase; margin:0 0 3pt}
.studio-dg .groups{display:grid; grid-template-columns:1fr 1fr 1fr; gap:5pt}
.studio-dg .g{background:var(--tint-yellow); border:1.2pt solid var(--yellow); padding:5pt 7pt 6pt}
.studio-dg .g h4{margin:0 0 3pt; font-size:9.5pt; line-height:11pt}
.studio-dg .g .gl{font-family:var(--font-cond); font-weight:700; font-size:7.5pt; letter-spacing:.06em; color:var(--ink-2); display:block; margin-bottom:1pt}
.studio-dg .g ul{margin:0; padding:0 0 0 9pt}
.studio-dg .g li{font-size:9pt; line-height:11pt; margin:0 0 2.5pt}
.studio-dg .g li::before{left:-8pt; top:3.8pt; width:3pt; height:3pt}
.studio-dg .g .q{font-family:var(--font-cond); font-weight:300; font-size:8pt; line-height:9.6pt; margin:2pt 0 0}
.studio-dg .band{margin-top:5pt; background:#000; color:#fff; padding:5pt 8pt; font-size:9pt; line-height:11pt}
.studio-dg .band b{color:#fff}
.studio-dg .band sup a{color:#fff}
/* page 1 API figures */
.figs{display:grid; grid-template-columns:repeat(3,1fr); background:var(--box); padding:5pt 9pt 4pt; margin:0 0 5pt}
.figs div{border-left:2.5pt solid var(--yellow); padding-left:7pt}
.figs div{display:flex; align-items:baseline; gap:6pt}
.figs b{font-weight:800; font-size:18pt; line-height:21pt}
.figs span{font-size:9pt; line-height:10.5pt}
.obs{display:grid; grid-template-columns:1fr 1fr; gap:12pt; margin:2pt 0 5pt}
.obs h4{margin:0 0 2pt; font-size:9.5pt; line-height:11.5pt}
.obs p{margin:0; font-size:9.5pt; line-height:12pt}
.lim{font-size:9.5pt; line-height:12pt; margin:4pt 0 4pt}
.method{background:var(--box); font-family:var(--font-cond); font-weight:300; font-size:8.5pt; line-height:10.5pt; padding:5pt 8pt; margin:0 0 4pt}
.method b{font-weight:700}
/* sources line at the foot of each page */
.srcs{border-top:.75pt solid var(--series-gray); padding-top:4pt; font-family:var(--font-cond); font-weight:300; font-size:7.2pt; line-height:8.8pt; color:#000}
.srcs .lb{font-weight:700; margin-right:2pt}
.srcs span{margin-right:5pt}
.srcs b{font-weight:700}
.srcs a{text-decoration:none}
/* page 2 */
.callouts{display:grid; grid-template-columns:1fr 1fr; gap:12pt; margin:2pt 0 3pt}
.callouts div{display:flex; gap:7pt; align-items:center; border-left:2.5pt solid var(--yellow); background:var(--box); padding:5pt 8pt}
.callouts b{font-weight:800; font-size:20pt; line-height:22pt; flex:none}
.callouts span{font-size:9pt; line-height:11pt}
.qual{font-family:var(--font-cond); font-weight:300; font-size:8.5pt; line-height:10.5pt; margin:0 0 6pt}
.impl{background:var(--tint-yellow); border-left:3pt solid var(--yellow); padding:5pt 9pt; font-size:9.5pt; line-height:12pt; margin:0 0 4pt}
.impl b{font-weight:800}
.take{font-size:9.5pt; line-height:12pt; margin:0}
table.comp{font-size:9.5pt; line-height:12pt; margin:0 0 5pt}
table.comp td.first{width:80pt}
.journey{display:grid; grid-template-columns:repeat(6,1fr); gap:0; margin:2pt 0 7pt}
.journey div{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 24' preserveAspectRatio='none'%3E%3Cpolygon fill='%23FFCE00' points='0,0 91,0 100,12 91,24 0,24 9,12'/%3E%3C/svg%3E"); background-size:100% 100%; padding:5pt 6pt 5pt 12pt; font-weight:700; font-size:9pt; line-height:11pt; display:flex; align-items:center; gap:4pt; min-height:24pt}
.journey div:first-child{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 24' preserveAspectRatio='none'%3E%3Cpolygon fill='%23FFCE00' points='0,0 91,0 100,12 91,24 0,24'/%3E%3C/svg%3E"); padding-left:6pt}
.journey .step{margin:0; flex:none; width:11pt; height:11pt; font-size:7pt}
.jf{display:grid; grid-template-columns:1fr 1fr 1fr; gap:10pt; margin:0 0 5pt}
.jf div{border-top:1.5pt solid #000; padding-top:4pt}
.jf h4{margin:0 0 2pt; font-size:9.5pt; line-height:11.5pt}
.jf p{margin:0; font-size:9.2pt; line-height:11.5pt}
.dq{border:1pt solid #000; padding:5pt 9pt; font-size:9.5pt; line-height:12pt; margin:2pt 0 5pt}
.dq b{font-weight:800}
/* page 3 */
table.ws{font-size:9.8pt; line-height:12.6pt; table-layout:fixed}
table.ws th{font-size:9pt; padding-bottom:4pt}
table.ws td{padding:6pt 9pt 7pt 0}
table.ws td.first{width:94pt; padding-right:8pt}
table.ws td.first .n{display:block; font-size:18pt; line-height:20pt; font-weight:800; margin-bottom:2pt}
table.ws tr.w td{border-bottom:1pt solid #000}
table.ws ul{margin:0; padding-left:9pt}
table.ws li{margin:0 0 2pt}
table.ws li::before{left:-8pt; top:4pt; width:3pt; height:3pt}
.ctl{background:var(--box); border-left:3pt solid #000; padding:5pt 9pt; font-size:9.5pt; line-height:12pt; margin:8pt 0 8pt}
.ctl b{font-weight:800}
.close{font-size:10.5pt; line-height:13.5pt; margin:0 0 6pt}
</style>
"""

H = []  # body parts

# ================================================================ PAGE 1
cur_page[0] = 1
p1 = f"""
<section class="pg first">
<div class="mast"><span class="accent-bar"></span>
<h1>Aladdin Studio from the outside</h1>
<p class="sub">What the public record shows about the product, the market, and questions for GTM discovery</p>
<p class="by">Prepared by Jacob Nikolau &nbsp;|&nbsp; Research conducted October 2026</p></div>
<p class="intro">This brief distills public-source research into Aladdin Studio’s technical capabilities, the buyer and competitive evidence surrounding extensible investment platforms, and three questions for internal GTM discovery. I examined BlackRock product material, the public Python SDK and API specifications, recordings featuring BlackRock leaders, and competitors’ published materials, without access to internal product, customer, roadmap, or commercial information.</p>

<h2 class="hl">Studio exposes Aladdin through APIs, data, and developer tools</h2>
<p>Aladdin Studio gives developers programmatic access to Aladdin through APIs and events, Aladdin Data Cloud on Snowflake, and developer tools{c('woodhead')}. BlackRock describes Studio as the experience that allows clients to treat Aladdin as a platform and build applications and workflows around its capabilities{c('woodhead', 'studio')}.</p>

<figure class="exhibit keep studio-dg"><p class="ex-title"><span class="ex-num">Exhibit 1.</span> What Studio offers, in three groups</p>
<p class="cap">Aladdin Studio</p>
<div class="groups">
<div class="g"><h4>APIs and events</h4><ul>
<li><b>APIs:</b> read and write access to documented Aladdin capabilities{c('apis')}</li>
<li><b>Events:</b> event-driven integration capabilities described by BlackRock{c('woodhead')}</li></ul>
<p class="q">No public event specification was available in the reviewed packages{c('specs')}.</p></div>
<div class="g"><h4>Aladdin Data Cloud</h4><ul>
<li>Managed data on Snowflake{c('adc')}</li>
<li>Supports access to Aladdin data for downstream analysis and integration{c('adc')}</li></ul></div>
<div class="g"><h4>Developer tools</h4><ul>
<li>Aladdin SDK{c('sdk')}</li>
<li>Aladdin Compute{c('apis')}</li>
<li>Developer Portal and Data Dictionary{c('apis', 'portal')}</li>
<li>Aladdin Tools for Excel{c('atx')}</li></ul></div>
</div>
<div class="band"><b>Aladdin services and data:</b> portfolio management, trading, risk, compliance, investment operations, and accounting{c('apis', 'specs')}</div>
<p class="notes">Simplified from Exhibit 4 of the full research. Grouping is conceptual. Individual products and data services have their own access requirements.</p>
</figure>

<h3 class="sh">Evidence from the public API specifications</h3>
<div class="figs"><div><b>54</b><span>public API specifications</span></div><div><b>301</b><span>operations</span></div><div><b>11</b><span>domains</span></div></div>
<p style="font-size:9.5pt;line-height:12pt">I counted 301 operations in 54 Swagger specifications across the 11 public asdk_plugin packages, version 2.0.0b3. The specifications cover areas including investment operations, analytics, portfolio management, trading, compliance, and accounting. These counts describe the public packages examined, not necessarily Studio’s full API surface{c('specs')}.</p>
<div class="obs">
<div><h4>Read and write</h4><p>The documented APIs extend beyond data retrieval. For example, the Order API includes a what-if setting and an option to run compliance checks{c('specs')}.</p></div>
<div><h4>Access and integration</h4><p>The specifications document API-specific OAuth scopes{c('specs')}, while the SDK supports authenticated calls and enterprise API gateway configurations{c('sdk')}.</p></div>
</div>
<div class="grow"></div>
<p class="method"><b>Limitation.</b> This analysis examines public product material, SDK code, and API specifications. I could not authenticate to a client environment or verify the full developer experience. <b>Method.</b> Public-source review, October 2026. AI tools assisted with collection, transcription, package analysis, and drafting. Claims were checked against cited materials. No internal or authenticated client access.</p>
{srcline(1)}
</section>
"""
H.append(p1)

# ================================================================ PAGE 2
cur_page[0] = 2
p2 = f"""
<section class="pg">
<h2 class="hl">Buyers are asking how they can build on their investment platforms</h2>
<h3 class="sh" style="margin-top:2pt">Buyer evidence</h3>
<p>In BlackRock’s June 2026 Build vs. Buy webinar, Clark Schafer of Alpha FMC said that questions about API suites and connections to Snowflake or Databricks have become more prominent in RFPs. BlackRock’s Alisha Sewdass described clients moving toward modular approaches, with foundational data, robust APIs, and room to build proprietary tools on top{c('webinar')}.</p>
<div class="callouts">
<div><b>67%</b><span>of webinar participants use mostly vendor or hybrid platforms{c('webinar')}</span></div>
<div><b>42%</b><span>named AI and data demands as a leading build-versus-buy consideration{c('webinar')}</span></div>
</div>
<p class="qual">Directional webinar-attendee responses. Sample size not disclosed. Not a representative industry survey.</p>
<p class="impl"><b>PMM implication:</b> Studio’s documented capabilities are directly relevant to the API, integration, and extensibility questions surfaced in this discussion. The frequency and commercial importance of those questions in BlackRock’s own pipeline remain to be validated.</p>

<figure class="exhibit keep"><p class="ex-title"><span class="ex-num">Exhibit 2.</span> Selective competitive observations</p>
<table class="comp"><thead><tr><th>Provider</th><th>Public development</th></tr></thead><tbody>
<tr><td class="first">SimCorp</td><td>SimCorp announced Agent Launchpad in 2026, including plans for prebuilt agents and client-built agents on SimCorp One’s data layer{c('simcorp')}.</td></tr>
<tr><td class="first">Arcesium</td><td>Arcesium added AI features to Aquata, including an MCP server that connects external AI tools to client data{c('arcesium')}.</td></tr>
<tr><td class="first">Bloomberg</td><td>Bloomberg launched an MCP server for licensed data in September 2026{c('bloomberg')}.</td></tr>
</tbody></table>
<p class="take">These examples indicate that competitors are publicly emphasizing extensibility or AI access, but the offerings differ substantially. They do not establish feature parity, a competitive ranking, or customer demand for a specific Studio integration.</p>
</figure>

<figure class="exhibit keep"><p class="ex-title"><span class="ex-num">Exhibit 3.</span> The public developer journey, from first hearing about Studio to getting help</p>
<div class="journey">
<div><span class="step">1</span>Hear</div><div><span class="step">2</span>Read</div><div><span class="step">3</span>See the catalog</div><div><span class="step">4</span>Try</div><div><span class="step">5</span>Build</div><div><span class="step">6</span>Get help</div>
</div>
<div class="jf">
<div><h4>Public discovery</h4><p>BlackRock product pages, recordings, public Python SDK packages, specifications, and sample material provide a starting point for understanding Studio{c('studio', 'apis', 'specs', 'sdk')}.</p></div>
<div><h4>Authenticated evaluation</h4><p>The complete developer portal, API catalog, credentials, and working Aladdin calls depend on additional access{c('portal', 'sdk')}. I could not test the authenticated journey.</p></div>
<div><h4>Enterprise integration signal</h4><p>The public SDK includes configuration for calls routed through enterprise API management infrastructure{c('sdk')}. Externally contributed changes for gateways and custom headers were accepted into the SDK{c('pr52', 'pr53')}.</p></div>
</div>
<p class="notes">Stages as in Exhibit 16 of the full research. Read with no account or login, October 2026.</p>
</figure>
<p class="dq"><b>Discovery question:</b> Where, if anywhere, do developers or buying teams encounter friction during Studio evaluation? Public visibility alone cannot establish the answer.</p>
<div class="grow"></div>
{srcline(2)}
</section>
"""
H.append(p2)

# ================================================================ PAGE 3
cur_page[0] = 3
p3 = f"""
<section class="pg">
<h2 class="hl">Three GTM questions worth investigating inside Studio</h2>
<figure class="exhibit keep" style="margin-top:2pt"><p class="ex-title"><span class="ex-num">Exhibit 4.</span> Three workstreams to validate, in no order of priority</p>
<table class="ws"><colgroup><col style="width:96pt"><col><col style="width:118pt"><col></colgroup>
<thead><tr><th>Workstream</th><th>Evidence from outside</th><th>Possible PMM output</th><th>What I’d validate internally</th></tr></thead><tbody>
<tr class="w"><td class="first"><span class="n">1</span>API and integration positioning</td>
<td>BlackRock’s webinar indicates that questions about API suites and data-platform connectivity have become more prominent in RFPs{c('webinar')}. The public SDK provides a concrete basis for describing Studio’s documented API domains and integration patterns{c('specs', 'sdk')}.</td>
<td>A technically validated API and integration narrative for RFPs, sales conversations, or developer-oriented materials.</td>
<td><ul><li>Which questions and partner integrations, such as Snowflake and Databricks, recur in deals?</li><li>What collateral already exists?</li><li>Where does stronger enablement have the greatest potential value?</li></ul></td></tr>
<tr class="w"><td class="first"><span class="n">2</span>Studio-specific customer proof</td>
<td>Public sources document institutions using Aladdin{c('jhg')}, but this review found limited named examples specifically describing applications those institutions built with Studio{c('studio', 'edgar')}.</td>
<td>A permissioned Studio customer story explaining what the client built, why it mattered, and what outcomes can be substantiated.</td>
<td><ul><li>Which clients actively build with Studio?</li><li>What outcomes can be verified?</li><li>Which customers are willing and permitted to be named?</li></ul></td></tr>
<tr class="w"><td class="first"><span class="n">3</span>Client-built AI integration use cases</td>
<td>Studio exposes documented Aladdin APIs that external applications can call with appropriate credentials{c('specs', 'sdk')}. Competitors have announced AI integrations and agent capabilities{c('simcorp', 'arcesium', 'bloomberg')}. This suggests a possible area for client-built AI use cases, but does not establish demand, supported workflows, or product readiness.</td>
<td>If customer demand and technical readiness justify it, a validated use-case narrative or demonstration showing how a client-built AI application could interact with supported Aladdin capabilities.</td>
<td><ul><li>Which client use cases are requested?</li><li>What can the product safely support, and under which permissions and safeguards?</li><li>Is this commercially important relative to other Studio priorities?</li></ul></td></tr>
</tbody></table>
</figure>
<p class="ctl"><b>Technical note on workstream 3:</b> API permissions and service controls do not automatically give external AI tools Copilot’s tool-registry rules or AI-specific guardrails{c('specs', 'rosales')}.</p>
<p class="close">These are starting points for internal discovery, not ranked recommendations. Establishing priorities would require customer evidence, product and engineering input, visibility into the current GTM materials and roadmap, and an understanding of Studio’s commercial objectives.</p>
<div class="grow"></div>
{srcline(3)}
</section>
"""
H.append(p3)

OUT.write_text(head + CSS + '</head><body>\n' + '\n'.join(H) + '\n</body></html>\n')
ORIG = {NUM[k]: REG[k][0] for k in NUM}
(OUT.parent / 'source_map.txt').write_text(
    'Brief number -> Prep 2 source number\n' +
    '\n'.join(f'{n} -> {ORIG[n]}  {REG[k][1]}' for k, n in sorted(NUM.items(), key=lambda x: x[1])) + '\n')
print('sources', len(NUM))
