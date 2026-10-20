# Builds X/preview_A.html and X/preview_B.html from the real HTML (read only), replacing Exhibit 3.
import re, sys, subprocess
S = "/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad"
X = S + "/ex23"
REAL = S + "/gtm/out/Aladdin_Studio_With_AI.html"

# Citations are written with logical keys and resolved by URL against the real file's register at build time,
# so the previews follow any renumbering of the real document.
URLS = {1: "youtube.com/watch?v=Me_H_-E6lSg", 6: "pypi.org/search/?q=asdk_plugin", 9: "youtube.com/watch?v=oyqeCHFM5U4",
        14: "products/aladdin-studio", 19: "tradingview.com/news/reuters.com,2025-12-05", 23: "products/aladdin-data-cloud",
        25: "youtube.com/watch?v=BahCi45_BTc", 27: "https://github.com/blackrock/aladdinsdk", 28: "products/apis",
        29: "products/aladdin-risk", 30: "products/aladdin-tools-for-excel", 31: "products/aladdin-data-exchange",
        32: "aladdin-data-cloud-powered-by-snowflake", 33: "microsoft-cloud/blog/2024/12/11", 34: "ir.theice.com",
        35: "sustainalytics.com/investor-solutions", 41: "apps/aladdin-developer-portal",
        "fivetran": "fivetran.com/blog/how-fivetran", "naik": "engineering.blackrock.com/open-sourcing", "job": "builtinbristol.uk/job/technical-writer",
        "goel": "data-as-a-strategic-assets-for-pensions", "snowpb": "snowflake.com/powered-by/aladdin", "builder": "github.com/blackrock/aladdinsdk-plugin-builder"}
_real = open(REAL, encoding="utf-8").read()
_reg = _real[_real.index('<div class="register">'):]
RES = {}
for k, u in URLS.items():
    hits = re.findall(r'<p id="s(\d+)"><b class="n">\d+</b>.*?<a href="([^"]+)"', _reg, flags=re.S)
    m = [n for n, href in hits if (href == u if u.startswith("http") else u in href)]
    assert len(m) == 1, (k, u, m)
    RES[k] = int(m[0])
def sup(*ns):
    ns = sorted(RES[n] for n in ns)
    return '<sup class="fnref">' + ', '.join(f'<a href="#s{n}">{n}</a>' for n in ns) + '</sup>'

TITLE = '<p class="ex-title"><span class="ex-num">Exhibit 3.</span> {}</p>'

# ---------------- Variant A: layered stack ----------------
CSS_A = """<style>
#stackA{display:grid;grid-template-columns:1fr 104pt;column-gap:8pt;font-size:9pt;line-height:10.8pt}
#stackA .ly{grid-column:1}
#stackA .lb{font-family:var(--font-cond);font-weight:700;font-size:8pt;line-height:9.6pt;letter-spacing:.06em;text-transform:uppercase;margin:0 0 2.5pt}
#stackA .ly + .ly{margin-top:5pt}
#stackA .row{display:grid;gap:4pt}
#stackA .c4{grid-template-columns:repeat(4,1fr)}
#stackA .c2{grid-template-columns:1fr 1fr}
#stackA .c3{grid-template-columns:repeat(3,1fr)}
#stackA .t{border:.75pt solid #000;background:#fff;padding:3pt 5pt;text-align:center}
#stackA .t b{display:block;font-weight:700}
#stackA .t span{display:block;font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt}
#stackA .c4 .t{display:flex;align-items:center;justify-content:center}
#stackA .t.cop{background:var(--tint-pink);border-color:var(--pink)}
#stackA .studio{border:1.5pt solid var(--yellow);background:var(--tint-yellow);padding:4pt}
#stackA .studio .t{text-align:left}
#stackA .core{background:#000;color:#fff;padding:5pt 8pt;text-align:center}
#stackA .core b{display:block;font-weight:700}
#stackA .core span{display:block;font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt;color:#fff}
#stackA .out{border:.75pt dashed #000;padding:3.5pt 8pt;text-align:center}
#stackA .side{grid-column:2;grid-row:2 / 5;background:var(--box);padding:6pt 7pt;align-self:stretch;margin-top:12.1pt}
#stackA .side .lb{margin-bottom:5pt}
#stackA .side p{margin:0 0 6pt;font-size:9pt;line-height:10.8pt}
#stackA .side p b{display:block}
#stackA .side p span{font-family:var(--font-cond);font-weight:300}
</style>"""

A = f"""<figure class="exhibit keep" id="exhibit-3">{TITLE.format('Apps, Copilot and Studio share the same Aladdin services and data')}
{CSS_A}
<div id="stackA" role="img" aria-label="A layered stack. Top: who builds, namely client engineers, code-curious portfolio managers, data analysts and Excel users building reports. Next: BlackRock’s own applications, about 100 of them such as Explore, Dashboard and Risk Radar, with Aladdin Copilot inside them; each Copilot tool matches an Aladdin API already in production. Next: Aladdin Studio, with APIs that read and write data, event-driven workflows, the Python SDK with Aladdin Compute and notebooks, Aladdin Data Cloud on Snowflake, Aladdin Tools for Excel and the Data eXchange, and the Data Dictionary and Developer Portal behind a client login. Next: Aladdin’s shared services and data for portfolio management, trading, risk, compliance, operations and accounting, reached through the 11 public API domains. Bottom: outside inputs, the client’s own and third-party data loaded into Data Cloud or through the Data eXchange, and vendor data such as prices and ESG research. A side column lists the controls built into the APIs: access set per API, compliance by default on orders, and a second approver for dataset releases.">
<div class="ly"><p class="lb">Who builds</p>
<div class="row c4"><div class="t">Client engineers</div><div class="t">Code-curious portfolio managers</div><div class="t">Data analysts</div><div class="t">Excel users building reports</div></div></div>
<div class="ly"><p class="lb">BlackRock’s own applications</p>
<div class="row c2"><div class="t"><b>About 100 applications</b><span>such as Explore, Dashboard and Risk Radar</span></div><div class="t cop"><b>Aladdin Copilot, inside them</b><span>each tool matches an Aladdin API already in production</span></div></div></div>
<div class="ly"><p class="lb">Aladdin Studio</p>
<div class="studio"><div class="row c3">
<div class="t"><b>APIs</b><span>that read and write Aladdin data</span></div>
<div class="t"><b>Event-driven workflows</b><span>Aladdin tells a program when something happens</span></div>
<div class="t"><b>Python SDK, Aladdin Compute</b><span>and notebooks</span></div>
<div class="t"><b>Aladdin Data Cloud</b><span>on Snowflake, each client’s own data store</span></div>
<div class="t"><b>Aladdin Tools for Excel</b><span>and the Aladdin Data eXchange</span></div>
<div class="t"><b>Data Dictionary, Developer Portal</b><span>behind a client login</span></div>
</div></div></div>
<div class="ly"><p class="lb">Aladdin’s shared services and data</p>
<div class="core"><b>Portfolio management, trading, risk, compliance, operations and accounting</b><span>The 11 public API domains: accounting, analytics, clients, compliance, data, investment-operations, investment-research, platform, portfolio, portfolio-management, trading</span></div></div>
<div class="ly"><p class="lb">Outside inputs</p>
<div class="out">The client’s own and third-party data, loaded into Data Cloud or through the Data eXchange, and vendor data such as prices and ESG research</div></div>
<div class="side"><p class="lb">Controls built into the APIs</p>
<p><b>Access set per API</b><span>Each API has its own access scope. A user sees only what their entitlements allow.</span></p>
<p><b>Compliance by default</b><span>The order API runs compliance by default and returns any violations.</span></p>
<p style="margin:0"><b>A second approver</b><span>Dataset releases need a second check.</span></p></div>
</div>
<div class="notes"><p><span class="lead">For illustrative purposes only.</span> The 11 domains are the packages of BlackRock’s public SDK, named as in its specifications, which also name Dashboard and Risk Radar. The controls are those in Exhibit 14. <span class="lbl"></span>Source: <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4&amp;t=155s">Rosales and Vicente Valdez at 2:35</a>, for the apps and Copilot{sup(9)}; a training recording, for Explore{sup(25)}; <a href="https://www.youtube.com/watch?v=Me_H_-E6lSg&amp;t=289s">Woodhead at 4:49</a>, for Studio, events and the Data Cloud{sup(1)}; the public specifications and SDK{sup(6, 27)}; BlackRock’s Studio, APIs, ATX, ADX, Data Cloud and Aladdin Risk pages{sup(14, 23, 28, 29, 30, 31)}; the developer portal{sup(41)}; the Data Cloud launch release{sup(32)}; data vendors, ICE and Sustainalytics{sup(34, 35)}. Aladdin is hosted on Microsoft Azure, with an AWS option announced for US-hosted Aladdin Enterprise clients{sup(19, 33)}.</p></div></figure>"""

# ---------------- Variant B: Studio parts named in the SDK files ----------------
CSS_B = """<style>
#partsB{font-size:9pt;line-height:10.8pt}
#partsB .studio{border:1.5pt solid var(--yellow);background:var(--tint-yellow);padding:5pt 6pt 6pt}
#partsB .hd{display:flex;justify-content:space-between;align-items:baseline;margin:0 0 5pt}
#partsB .hd b{font-weight:800;font-size:10pt}
#partsB .tag{font-family:var(--font-cond);font-weight:700;font-size:8pt;letter-spacing:.06em;background:var(--yellow);padding:.5pt 4pt;margin-right:5pt;text-transform:uppercase}
#partsB .rd{font-size:9pt}
#partsB .grid{display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr;gap:4pt}
#partsB .t{border:.75pt solid #000;background:#fff;padding:3.5pt 5pt}
#partsB .t b{display:block;font-weight:700}
#partsB .t span{display:block;font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt}
#partsB .proj{grid-row:1 / 3;padding:3.5pt 5pt}
#partsB .proj .t{background:var(--box);border:0;margin-top:4pt;padding:3pt 5pt}
#partsB .sdk{background:#000;color:#fff;text-align:center;padding:4pt 8pt;margin:5pt 0}
#partsB .sdk b{font-weight:700}
#partsB .base{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4pt}
#partsB .base .t{text-align:center;background:#fff}
</style>"""

B = f"""<figure class="exhibit keep" id="exhibit-3">{TITLE.format('The Studio parts named in BlackRock’s public SDK files')}
{CSS_B}
<div id="partsB" role="img" aria-label="Aladdin Studio drawn as one box. Inside it: a Project, which holds login apps for code and a storage bucket; Compute sessions, where SDK code can run instead of on a laptop; API tokens registered in the Studio screens; Spaces, named only as an alert target; the Data Cloud Admin Center, where dataset owners edit datasets before a second check; and alerts by email or push to a user, project or space. My reading is that these parts form one hosted place to build. Below Studio, the AladdinSDK runs on a developer’s machine or in Studio Compute sessions. Below that: the Aladdin APIs, 54 public specifications with 301 operations in 11 packages; Aladdin Data Cloud on Snowflake; and Aladdin Tools for Excel and the Data eXchange.">
<div class="studio">
<div class="hd"><b>Aladdin Studio</b><span class="rd"><span class="tag">My reading</span>These parts form one hosted place to build</span></div>
<div class="grid">
<div class="t proj"><b>Project</b>
<div class="t"><b>Login apps for code</b><span>OAuth apps are made “under a Project in Studio”</span></div>
<div class="t"><b>Storage bucket</b><span>keys come from “S3 Storage Integration in a Studio Project”</span></div></div>
<div class="t"><b>Compute sessions</b><span>where SDK code can run instead of on a developer’s own machine</span></div>
<div class="t"><b>Spaces</b><span>named as an alert target; their role is not described</span></div>
<div class="t"><b>Alerts</b><span>email or push, sent to a user, a project or a space</span></div>
<div class="t"><b>API tokens</b><span>“registered via Studio UI”</span></div>
<div class="t"><b>ADC Admin Center</b><span>where dataset owners edit Data Cloud datasets before a second check</span></div>
<div></div>
</div></div>
<div class="sdk"><b>AladdinSDK</b>, the Python toolkit, “can run on a developer’s local machine or in Aladdin Studio Compute sessions”</div>
<div class="base">
<div class="t"><b>Aladdin APIs</b><span>54 public specifications, 301 operations, in 11 packages</span></div>
<div class="t"><b>Aladdin Data Cloud</b><span>on Snowflake, each client’s own data store</span></div>
<div class="t"><b>Aladdin Tools for Excel</b><span>and the Aladdin Data eXchange, linked from the APIs page</span></div>
</div></div>
<div class="notes"><p><span class="lead">For illustrative purposes only.</span> Every part inside the Studio box is named in the SDK README’s settings for login, storage, API tokens, run mode and notifications, or in the Data Cloud dataset specification. The files do not say what a Space is. Around these parts sit BlackRock’s own applications and Copilot, which draw on the same Aladdin services and data{sup(9)}, among them Explore{sup(25)} and the risk engine{sup(29)}; Aladdin is hosted on Microsoft Azure, with an AWS option announced for US-hosted Aladdin Enterprise clients{sup(19, 33)}, and takes in vendor data such as ICE prices and Sustainalytics ESG research{sup(34, 35)}. <span class="lbl"></span>Source: the SDK README{sup(27)}; the public specifications{sup(6)}; <a href="https://www.youtube.com/watch?v=Me_H_-E6lSg&amp;t=289s">Woodhead at 4:49</a>, for Studio and the Data Cloud{sup(1)}; BlackRock’s Studio, APIs, ATX, ADX and Data Cloud pages{sup(14, 23, 28, 30, 31)}; the Data Cloud launch release{sup(32)}.</p></div></figure>"""


# ---------------- Variant C: one stack replaces Exhibits 3 and 4 ----------------
C_STUDIO = """<div class="studio"><div class="row c3">
<div class="t"><b>APIs (Aladdin Graph)</b><span>read and write Aladdin data</span></div>
<div class="t"><b>Event-driven workflows</b><span>Aladdin tells a program when something happens</span></div>
<div class="t"><b>Aladdin Data Cloud</b><span>a managed data store on Snowflake, Fivetran moving the data</span></div>
<div class="t"><b>Aladdin Compute</b><span>hosted Python environments</span></div>
<div class="t"><b>Aladdin SDK</b><span>open-source Python library for login, retries, rate limits</span></div>
<div class="t"><b>Developer Portal and Data Dictionary</b><span>behind a client login</span></div>
</div><p class="also">The APIs page also links Aladdin Tools for Excel and the Aladdin Data eXchange</p></div>"""
a0 = A.index('<div class="studio">'); a1 = A.index('</div></div></div>', a0) + len('</div></div>')
C = A[:a0] + C_STUDIO + A[a1:]
C = C.replace('#stackA .side{', '#stackA .also{margin:4pt 0 0;font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt;text-align:center}\n#stackA .side{')
C = C.replace('Next: Aladdin Studio, with APIs that read and write data, event-driven workflows, the Python SDK with Aladdin Compute and notebooks, Aladdin Data Cloud on Snowflake, Aladdin Tools for Excel and the Data eXchange, and the Data Dictionary and Developer Portal behind a client login.',
  'Next: Aladdin Studio in six pieces: APIs (Aladdin Graph) that read and write Aladdin data; event-driven workflows, where Aladdin tells a program when something happens; Aladdin Data Cloud, a managed data store on Snowflake with Fivetran moving the data; Aladdin Compute, hosted Python environments; the Aladdin SDK, an open-source Python library for login, retries and rate limits; and the Developer Portal and Data Dictionary behind a client login. The APIs page also links Aladdin Tools for Excel and the Aladdin Data eXchange.')
n0 = C.index('<div class="notes">')
C = C[:n0] + f"""<div class="notes"><p><span class="lead">For illustrative purposes only.</span> The six Studio pieces are my grouping; BlackRock gives no count. The 11 domains are the packages of BlackRock’s public SDK, named as in its specifications, which also name Dashboard and Risk Radar. No event specification is public, and the specifications link the guides to a portal behind a client login. The controls are those in Exhibit 14. <span class="lbl"></span>Source: <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4&amp;t=155s">Rosales and Vicente Valdez at 2:35</a>, for the apps and Copilot{sup(9)}; a training recording, for Explore{sup(25)}; <a href="https://www.youtube.com/watch?v=Me_H_-E6lSg&amp;t=289s">Woodhead at 4:49</a>, for Studio, events and the Data Cloud{sup(1)}; the 54 public specifications and the SDK README{sup(6, 27)}; Naik and Kalish, for Aladdin Graph{sup("naik")}; the plugin builder{sup("builder")}; Snowflake’s partner page, for Compute{sup("snowpb")}; Fivetran{sup("fivetran")}; Goel, for events{sup("goel")}; a BlackRock job posting{sup("job")}; BlackRock’s Studio, APIs, ATX, ADX, Data Cloud and Aladdin Risk pages{sup(14, 23, 28, 29, 30, 31)}; the developer portal{sup(41)}; the Data Cloud launch release{sup(32)}; data vendors, ICE and Sustainalytics{sup(34, 35)}. Aladdin is hosted on Microsoft Azure, with an AWS option announced for US-hosted Aladdin Enterprise clients{sup(19, 33)}.</p></div></figure>"""

def renumber_exhibits(h):
    # Exhibit 4 is gone: every exhibit numbered 5 or above moves down by one, in the body only.
    i = h.index('<body')
    head, body = h[:i], h[i:]
    def dec(m):
        n = int(m.group(2))
        return m.group(1) + str(n - 1 if n >= 5 else n)
    body = re.sub(r'(Exhibits?(?:\s|&nbsp;)+)(\d+)', dec, body)
    body = re.sub(r'(id="exhibit-)(\d+)', dec, body)
    body = re.sub(r'(href="#exhibit-)(\d+)', dec, body)
    return head + body

# ---------------- Variant D: skinny platform view (Exhibit 3) + Studio components (Exhibit 4), no renumbering ----------------
CSS_D3 = """<style>
#stackD{display:grid;grid-template-columns:60pt 1fr 116pt;column-gap:6pt;row-gap:4pt;font-size:9pt;line-height:10.8pt;align-items:stretch}
#stackD .lb{grid-column:1;font-weight:700;font-size:9pt;line-height:10.8pt;align-self:center}
#stackD .row{grid-column:2;display:grid;gap:4pt}
#stackD .c4{grid-template-columns:repeat(4,1fr)}
#stackD .c2{grid-template-columns:1fr 1fr}
#stackD .t{border:.75pt solid #000;background:#fff;padding:2.5pt 5pt;text-align:center;display:flex;flex-direction:column;justify-content:center}
#stackD .t b{font-weight:700}
#stackD .t span{font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt}
#stackD .t.cop{background:var(--tint-pink);border-color:var(--pink)}
#stackD .t.hatch{background:repeating-linear-gradient(135deg,#fff 0 3pt,#D6D5DD 3pt 4pt);border-style:dashed}
#stackD .studio{grid-column:2;border:1.5pt solid var(--yellow);background:var(--tint-yellow);padding:4pt 8pt;text-align:center}
#stackD .studio b{font-weight:700}
#stackD .core{grid-column:2;background:#000;color:#fff;padding:4pt 8pt;text-align:center}
#stackD .core b{display:block;font-weight:700}
#stackD .core span{display:block;font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt;color:#fff}
#stackD .out{grid-column:2;border:.75pt dashed #000;padding:3pt 8pt;text-align:center}
#stackD .side{grid-column:3;grid-row:2 / 6;background:var(--box);padding:5pt 7pt}
#stackD .side .cap{font-family:var(--font-cond);font-weight:700;font-size:8pt;line-height:9.6pt;letter-spacing:.06em;text-transform:uppercase;margin:0 0 4pt}
#stackD .side p{margin:0 0 3pt}
#stackD .side p b{display:block}
#stackD .side p span{font-family:var(--font-cond);font-weight:300}
</style>"""

D3 = f"""<figure class="exhibit keep" id="exhibit-3">{TITLE.format('Apps, Copilot and Studio share the same Aladdin services and data')}
{CSS_D3}
<div id="stackD" role="img" aria-label="A layered stack in six rows. Who builds: client engineers, code-curious portfolio managers, data analysts and Excel users building reports. BlackRock’s own applications: about 100, such as Explore, Dashboard and Risk Radar, with Aladdin Copilot inside them; each Copilot tool matches an Aladdin API already in production. Aladdin Studio: the developer and data layer, whose parts Exhibit 4 shows. Aladdin’s shared services and data: portfolio management, trading, risk, compliance, operations and accounting, reached through the 11 public API domains. Hosting: Microsoft Azure today, and an AWS option that is announced, not live. Outside inputs: the client’s own and third-party data, loaded into Data Cloud or through the Data eXchange, and vendor data such as prices and ESG research. A side column lists the controls built into the APIs: access set per API, compliance by default on orders, and a second approver for dataset releases.">
<div class="lb">Who builds</div>
<div class="row c4"><div class="t">Client engineers</div><div class="t">Code-curious portfolio managers</div><div class="t">Data analysts</div><div class="t">Excel users building reports</div></div>
<div class="lb">BlackRock’s applications</div>
<div class="row c2"><div class="t"><b>About 100 applications</b><span>such as Explore, Dashboard and Risk Radar</span></div><div class="t cop"><b>Aladdin Copilot, inside them</b><span>each tool matches an Aladdin API already in production</span></div></div>
<div class="lb">Aladdin Studio</div>
<div class="studio"><b>Aladdin Studio:</b> the developer and data layer; its parts are in Exhibit 4</div>
<div class="lb">Shared services and data</div>
<div class="core"><b>Portfolio management, trading, risk, compliance, operations, accounting</b><span>reached through the 11 public API domains</span></div>
<div class="lb">Hosting</div>
<div class="row c2"><div class="t">Microsoft Azure today</div><div class="t hatch">AWS option, announced</div></div>
<div class="lb">Outside inputs</div>
<div class="out">The client’s own and third-party data, loaded into Data Cloud or through the Data eXchange, and vendor data such as prices and ESG research</div>
<div class="side"><p class="cap">Controls built into the APIs</p>
<p><b>Access set per API</b><span>Each API has its own access scope. A user sees only what their entitlements allow.</span></p>
<p><b>Compliance by default</b><span>The order API runs compliance by default and returns any violations.</span></p>
<p style="margin:0"><b>A second approver</b><span>Dataset releases need a second check.</span></p></div>
</div>
<div class="notes"><p><span class="lead">For illustrative purposes only.</span> Every box is named in the sources below; the AWS option is announced, not live. The 11 domains are the packages of BlackRock’s public SDK; the specifications also name Dashboard and Risk Radar. Controls as in Exhibit 14. <span class="lbl"></span>Source: <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4&amp;t=155s">Rosales and Vicente Valdez at 2:35</a>, for the apps and Copilot{sup(9)}; a training recording, for Explore{sup(25)}; <a href="https://www.youtube.com/watch?v=Me_H_-E6lSg&amp;t=289s">Woodhead at 4:49</a>, for Studio{sup(1)}; the public specifications and SDK{sup(6, 27)}; BlackRock’s Studio, APIs, ATX, ADX, Data Cloud and Aladdin Risk pages{sup(14, 23, 28, 29, 30, 31)}; the Data Cloud launch release{sup(32)}; hosting, Azure and the AWS release{sup(19, 33)}; data vendors, ICE and Sustainalytics{sup(34, 35)}.</p></div></figure>"""

CSS_D4 = """<style>
#partsD{font-size:9pt;line-height:10.8pt}
#partsD .gh{font-family:var(--font-cond);font-weight:700;font-size:8pt;line-height:9.6pt;letter-spacing:.06em;text-transform:uppercase;margin:0 0 3pt}
#partsD .grid{display:grid;gap:4pt}
#partsD .g3{grid-template-columns:repeat(3,1fr)}
#partsD .g4{grid-template-columns:repeat(4,1fr)}
#partsD .t{border:.75pt solid #000;background:#fff;padding:3pt 5pt}
#partsD .t b{display:block;font-weight:700}
#partsD .t span{display:block;font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt}
#partsD .offer{border:1.5pt solid var(--yellow);background:var(--tint-yellow);padding:4pt}
#partsD .also{margin:3pt 0 0;font-family:var(--font-cond);font-weight:300;font-size:9pt;line-height:10.4pt;text-align:center}
#partsD .ws{margin-top:6pt;background:var(--box);padding:4pt 6pt}
#partsD .ws .grid{grid-template-columns:1fr 1fr;column-gap:12pt;row-gap:0}
#partsD .ws .grid div{padding:2pt 0;border-top:.5pt solid #BFBFBF}
#partsD .ws .grid b{font-weight:700}
#partsD .ws .grid span{font-family:var(--font-cond);font-weight:300}
#partsD code{font-size:8.5pt}
</style>"""

D4 = f"""<figure class="exhibit keep" id="exhibit-4">{TITLE.format('Studio, grouped here into six pieces, and the parts of a client’s Studio named in the SDK files').replace('Exhibit 3.', 'Exhibit 4.')}
{CSS_D4}
<div id="partsD" role="img" aria-label="Two groups. What Studio offers, in six pieces: APIs (Aladdin Graph), whose public specification ids all start agraph.domain; event-driven workflows; Aladdin Data Cloud on Snowflake with Fivetran moving the data; Aladdin Compute, hosted Python environments; the Aladdin SDK, whose 11 plugin packages are generated from the specifications by BlackRock’s plugin builder; and the Developer Portal and Data Dictionary behind a client login. The APIs page also links Aladdin Tools for Excel and the Aladdin Data eXchange. Inside a client’s Studio workspace, as the public SDK files name them: Projects, Studio Compute, S3 storage integration, API tokens and API applications, Studio notifications, Studio UI and the ADC Admin Center.">
<p class="gh">What Studio offers</p>
<div class="offer"><div class="grid g3">
<div class="t"><b>APIs (Aladdin Graph)</b><span>Read and write Aladdin data. Every public specification’s id starts <code>agraph.&lt;domain&gt;</code></span></div>
<div class="t"><b>Event-driven workflows</b><span>Aladdin tells a program when something happens. No event specification is public</span></div>
<div class="t"><b>Aladdin Data Cloud</b><span>A managed data store on Snowflake, with Fivetran moving the data</span></div>
<div class="t"><b>Aladdin Compute</b><span>Hosted, ready-to-use Python environments</span></div>
<div class="t"><b>Aladdin SDK</b><span>Open-source Python library for login, retries and rate limits. BlackRock’s plugin builder generates its 11 plugin packages from the specifications</span></div>
<div class="t"><b>Developer Portal and Data Dictionary</b><span>Catalog, guides, field dictionary, notebooks and samples, behind a client login</span></div>
</div><p class="also">The APIs page also links Aladdin Tools for Excel and the Aladdin Data eXchange</p></div>
<div class="ws"><p class="gh">Inside a client’s Studio workspace, as the public SDK files name it</p>
<div class="grid">
<div><b>Projects</b> <span>Personal or shared. OAuth applications and storage are set up under one</span></div>
<div><b>Studio Compute</b> <span>Sessions where SDK code can run, as an alternative to a developer’s local machine</span></div>
<div><b>S3 storage integration</b> <span>File storage set up in a Studio Project, its bucket assigned to a user or project</span></div>
<div><b>API tokens and API applications</b> <span>Sign-in details for programs: a token, or an OAuth client ID and secret</span></div>
<div><b>Studio notifications</b> <span>Email or push alerts to a user, a Project or a Space</span></div>
<div><b>Studio UI</b> <span>Studio’s screens, where tokens, applications and storage are set up</span></div>
<div><b>ADC Admin Center</b> <span>Studio’s screen for managing Data Cloud datasets</span></div>
</div></div>
</div>
<div class="notes"><p><span class="lbl"></span>Source: BlackRock Studio and APIs pages{sup(14, 28)}; the 54 public specifications{sup(6)}, for the ids, the portal link and the Admin Center; the SDK README{sup(27)}, for the SDK and the lower group; Naik and Kalish, for Aladdin Graph{sup("naik")}; the plugin builder{sup("builder")}; Woodhead{sup(1)}, Goel{sup("goel")}, the Aladdin Risk page{sup(29)} and a BlackRock job posting{sup("job")}, for events and the portal; Fivetran{sup("fivetran")}; Snowflake’s partner page, for Compute{sup("snowpb")}; the developer portal{sup(41)}. BlackRock gives no count of pieces. The APIs page describes the catalog, guides, notebooks and samples but does not link them; the specifications link the guides to a portal behind a client login.</p></div></figure>"""
D = D3 + D4

def build(var, block):
    h = open(REAL, encoding="utf-8").read()
    a = h.index('<figure class="exhibit keep" id="exhibit-3">')
    b = h.index('</figure>', a) + len('</figure>')
    if var in ("C", "D"):
        assert h[b:].startswith('<figure class="exhibit" id="exhibit-4">')
        b = h.index('</figure>', b) + len('</figure>')
    h = h[:a] + block + h[b:]
    if var == "C":
        h = renumber_exhibits(h)
    P = f"{X}/preview_{var}.html"
    open(P, "w", encoding="utf-8").write(h)
    r = subprocess.run(["python3", "-I", S + "/gtm/renumber.py", P], capture_output=True, text=True)
    print(var, r.stdout.strip()[-300:], r.stderr[-800:])
    if r.returncode: sys.exit(1)
    h = open(P, encoding="utf-8").read()
    a = h.index('<div class="register">'); b = h.index('</div>\n</section>', a)
    ents = re.findall(r'<p id="s\d+">.*?</p>\n', h[a:b], flags=re.S)
    assert ''.join(ents) == h[a + len('<div class="register">\n'):b], 'register not flat'
    ents.sort(key=lambda e: int(re.match(r'<p id="s(\d+)"', e).group(1)))
    h = h[:a] + '<div class="register">\n' + ''.join(ents) + h[b:]
    def fix(m):
        links = re.findall(r'<a href="#s\d+">\d+</a>', m.group(1))
        links = sorted(dict.fromkeys(links), key=lambda x: int(re.search(r'>(\d+)<', x).group(1)))
        return '<sup class="fnref">' + ', '.join(links) + '</sup>'
    h = re.sub(r'<sup class="fnref">(.*?)</sup>', fix, h)
    open(P, "w", encoding="utf-8").write(h)

for v in (sys.argv[1:] or ["A", "B", "C", "D"]):
    build(v, {"A": A, "B": B, "C": C, "D": D}[v])
