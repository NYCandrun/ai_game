import re, sys
F = sys.argv[1]
h = open(F, encoding='utf-8').read()

SVG = r'''<svg id="pmap" viewBox="0 18 1280 680" xmlns="http://www.w3.org/2000/svg" style="display:block;width:504pt;height:auto;overflow:visible">
<style>
#pmap text{font-family:"Barlow",sans-serif;font-weight:400;font-size:16px;fill:#000}
#pmap .tt{font-weight:700;font-size:17px}
#pmap .s{font-family:"Barlow Condensed",sans-serif;font-weight:300;font-size:16px}
#pmap .cap{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:14px;letter-spacing:.08em}
#pmap .domn{font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:18px}
#pmap .tc{text-anchor:middle}
#pmap .ic{fill:none;stroke:#000;stroke-width:1.5}
#pmap .ln{stroke:#000;stroke-width:1.2;fill:none}
#pmap .arr{stroke:#000;stroke-width:1.5;fill:none}
#pmap .hd{fill:#000}
#pmap .env{fill:#fff;stroke:#000;stroke-width:1.6}
#pmap .band{fill:#fff;stroke:#D6D5DD;stroke-width:1.2}
#pmap .tile{fill:#fff;stroke:#000;stroke-width:1.4}
#pmap .tile.hatch{fill:url(#pm-hatch)}
#pmap .cop{fill:#FEEBF0;stroke:#FC9BB3;stroke-width:1.6}
#pmap .api{fill:#F2F2F2;stroke:#000;stroke-width:1.2}
#pmap .eng{fill:#F2F2F2;stroke:#000;stroke-width:1.2}
#pmap .studio{fill:#FFF5CC;stroke:#FFCE00;stroke-width:1.6}
#pmap .dom{fill:#fff;stroke:#000;stroke-width:1.3}
#pmap .cyl{fill:#fff;stroke:#000;stroke-width:1.4}
</style>
<defs>
<marker id="pm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="hd"/></marker>
<pattern id="pm-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="2" height="6" style="fill:#BFBFBF"/></pattern>
<symbol id="pm-person" viewBox="0 0 20 20"><circle cx="10" cy="6" r="3.6" class="ic"/><path d="M3 18 C3 12.5 17 12.5 17 18" class="ic"/></symbol>
</defs>

<!-- the platform -->
<rect x="165" y="20" width="945" height="676" rx="8" class="env"/>
<text x="180" y="41" class="cap">THE ALADDIN PLATFORM · INSTITUTIONAL</text>

<!-- people -->
<text x="10" y="40" class="cap">PEOPLE</text>
<use href="#pm-person" x="8" y="52" width="22" height="22"/><text x="34" y="69">Portfolio manager</text>
<use href="#pm-person" x="8" y="84" width="22" height="22"/><text x="34" y="101">Trader</text>
<use href="#pm-person" x="8" y="116" width="22" height="22"/><text x="34" y="133">Compliance, risk</text>
<use href="#pm-person" x="8" y="148" width="22" height="22"/><text x="34" y="165">Operations</text>
<use href="#pm-person" x="8" y="180" width="22" height="22"/><text x="34" y="197">Accountant</text>
<use href="#pm-person" x="8" y="212" width="22" height="22"/><text x="34" y="223">Performance</text><text x="34" y="240">analyst</text>
<path d="M160 56 V 236" class="ln"/>
<path d="M160 102 H 377" class="arr" marker-end="url(#pm-arrow)"/>
<text x="268" y="94" class="s tc">use the apps</text>

<use href="#pm-person" x="8" y="262" width="22" height="22"/><text x="34" y="274">Client developers,</text><text x="34" y="291">quants</text>
<path d="M160 276 H 178" class="arr" marker-end="url(#pm-arrow)"/>

<rect x="8" y="318" width="146" height="48" rx="4" class="tile"/><text x="18" y="338" class="tt">Client systems</text><text x="18" y="356" class="s">the client’s own tools</text>

<!-- apps -->
<rect x="380" y="50" width="715" height="140" rx="6" class="band"/>
<text x="392" y="68" class="cap">APPS · ABOUT 100 FRONT-END APPLICATIONS</text>
<rect x="392" y="78" width="164" height="48" rx="4" class="tile"/><text x="474" y="98" class="tt tc">Explore</text><text x="474" y="116" class="s tc">analyse portfolios, test trades</text>
<rect x="568" y="78" width="164" height="48" rx="4" class="tile"/><text x="650" y="98" class="tt tc">Dashboard</text><text x="650" y="116" class="s tc">monitor orders and events</text>
<rect x="744" y="78" width="164" height="48" rx="4" class="tile"/><text x="826" y="98" class="tt tc">Risk Radar</text><text x="826" y="116" class="s tc">work through risk breaches</text>
<rect x="920" y="78" width="164" height="48" rx="4" class="tile"/><text x="1002" y="98" class="tc">about 95 more</text><text x="1002" y="116" class="s tc">cash, FX, collateral, data</text>
<rect x="392" y="136" width="692" height="42" rx="5" class="cop"/>
<text x="406" y="163"><tspan class="tt">Aladdin Copilot</tspan><tspan dx="10" class="s">a chat panel inside each app · reads what is on screen · answers through the same APIs</tspan></text>
<path d="M650 190 V 202" class="arr" marker-end="url(#pm-arrow)"/>

<!-- api -->
<rect x="380" y="204" width="715" height="38" rx="6" class="api"/>
<text x="392" y="229"><tspan class="tt">Shared API layer</tspan><tspan dx="10" class="s">every app, Copilot and Studio call it · access checked on every call</tspan></text>
<path d="M475 242 V 256" class="arr" marker-end="url(#pm-arrow)"/>
<path d="M649 242 V 256" class="arr" marker-end="url(#pm-arrow)"/>
<path d="M823 242 V 256" class="arr" marker-end="url(#pm-arrow)"/>
<path d="M997 242 V 256" class="arr" marker-end="url(#pm-arrow)"/>

<!-- domains: the 11 public API domains -->
<rect x="380" y="258" width="715" height="232" rx="6" class="band"/>
<text x="392" y="276" class="cap">DOMAIN SERVICES · THE 11 PUBLIC API DOMAINS</text>
<rect x="392" y="290" width="166" height="44" rx="4" class="dom"/><text x="400" y="309" class="domn">investment-research</text><text x="400" y="327" class="s">notes, coverage, watchlists</text>
<rect x="566" y="290" width="166" height="44" rx="4" class="dom"/><text x="574" y="309" class="domn">portfolio</text><text x="574" y="327" class="s">setup, groups, restrictions</text>
<rect x="740" y="290" width="166" height="44" rx="4" class="dom"/><text x="748" y="309" class="domn">portfolio-management</text><text x="748" y="327" class="s">cash ladder, strategy, data</text>
<rect x="914" y="290" width="166" height="44" rx="4" class="dom"/><text x="922" y="309" class="domn">investment-operations</text><text x="922" y="327" class="s">settlement, corp. actions</text>
<rect x="392" y="342" width="166" height="44" rx="4" class="dom"/><text x="400" y="361" class="domn">trading</text><text x="400" y="379" class="s">orders, trades</text>
<rect x="566" y="342" width="166" height="44" rx="4" class="dom"/><text x="574" y="361" class="domn">compliance</text><text x="574" y="379" class="s">rules, levels, violations</text>
<rect x="740" y="342" width="166" height="44" rx="4" class="dom"/><text x="748" y="361" class="domn">analytics</text><text x="748" y="379" class="s">risk limits, climate, ESG</text>
<rect x="914" y="342" width="166" height="44" rx="4" class="dom"/><text x="922" y="361" class="domn">accounting</text><text x="922" y="379" class="s">lots, valuations, NAV</text>
<rect x="392" y="394" width="166" height="44" rx="4" class="dom"/><text x="400" y="413" class="domn">data</text><text x="400" y="431" class="s">security master</text>
<rect x="566" y="394" width="166" height="44" rx="4" class="dom"/><text x="574" y="413" class="domn">platform</text><text x="574" y="431" class="s">users, permissions, datasets</text>
<rect x="740" y="394" width="166" height="44" rx="4" class="dom"/><text x="748" y="413" class="domn">clients</text><text x="748" y="431" class="s">fund flows in and out</text>
<rect x="392" y="446" width="688" height="36" rx="5" class="eng"/><text x="406" y="470"><tspan class="tt">Aladdin Analytics</tspan><tspan dx="10" class="s">the risk engine every domain uses · turns positions and market data into risk numbers</tspan></text>
<path d="M469 490 V 506" class="arr" marker-end="url(#pm-arrow)"/><path d="M481 506 V 490" class="arr" marker-end="url(#pm-arrow)"/>
<path d="M643 490 V 506" class="arr" marker-end="url(#pm-arrow)"/><path d="M655 506 V 490" class="arr" marker-end="url(#pm-arrow)"/>
<path d="M817 490 V 506" class="arr" marker-end="url(#pm-arrow)"/><path d="M829 506 V 490" class="arr" marker-end="url(#pm-arrow)"/>
<path d="M991 490 V 506" class="arr" marker-end="url(#pm-arrow)"/><path d="M1003 506 V 490" class="arr" marker-end="url(#pm-arrow)"/>

<!-- shared data -->
<rect x="380" y="508" width="715" height="120" rx="6" class="band"/>
<text x="392" y="526" class="cap">SHARED DATA · EVERY DOMAIN READS AND WRITES IT</text>
<g>
<ellipse cx="454" cy="546" rx="58" ry="8" class="cyl"/><path d="M396 546 v40 a58 8 0 0 0 116 0 v-40" class="cyl"/><text x="454" y="575" class="tt tc">Orders, trades</text>
<ellipse cx="596" cy="546" rx="58" ry="8" class="cyl"/><path d="M538 546 v40 a58 8 0 0 0 116 0 v-40" class="cyl"/><text x="596" y="570" class="tt tc">Positions</text><text x="596" y="587" class="s tc">IBOR, the live book</text>
<ellipse cx="738" cy="546" rx="58" ry="8" class="cyl"/><path d="M680 546 v40 a58 8 0 0 0 116 0 v-40" class="cyl"/><text x="738" y="570" class="tt tc">Accounting</text><text x="738" y="587" class="s tc">ABOR, NAV</text>
<ellipse cx="880" cy="546" rx="58" ry="8" class="cyl"/><path d="M822 546 v40 a58 8 0 0 0 116 0 v-40" class="cyl"/><text x="880" y="575" class="tt tc">Portfolios</text>
<ellipse cx="1022" cy="546" rx="58" ry="8" class="cyl"/><path d="M964 546 v40 a58 8 0 0 0 116 0 v-40" class="cyl"/><text x="1022" y="575" class="tt tc">Securities</text>
</g>

<!-- hosting -->
<rect x="380" y="640" width="715" height="42" rx="6" class="band"/>
<text x="392" y="666" class="cap">HOSTING</text>
<rect x="470" y="647" width="110" height="28" rx="4" class="tile"/><text x="525" y="667" class="tc">Azure today</text>
<rect x="592" y="647" width="160" height="28" rx="4" style="fill:#fff"/><rect x="592" y="647" width="160" height="28" rx="4" class="tile hatch"/><text x="672" y="667" class="tc">AWS option, H2 2026</text>

<!-- studio -->
<rect x="180" y="150" width="184" height="478" rx="6" class="studio"/>
<text x="192" y="170" class="cap">ALADDIN STUDIO</text><text x="192" y="188" class="s">for clients who build on Aladdin</text>
<rect x="190" y="204" width="168" height="38" rx="4" class="tile"/><text x="200" y="221" class="tt">AladdinSDK</text><text x="200" y="236" class="s">calls the shared APIs</text>
<path d="M358 223 H 378" class="arr" marker-end="url(#pm-arrow)"/>
<rect x="190" y="254" width="168" height="38" rx="4" class="tile"/><text x="198" y="271" class="tt">Research sandboxes</text><text x="198" y="286" class="s">hosted places to build</text>
<rect x="190" y="320" width="168" height="44" rx="4" class="tile"/><text x="200" y="338" class="tt">Excel tools, feeds</text><text x="200" y="356" class="s">events and files out</text>
<path d="M190 342 H 156" class="arr" marker-end="url(#pm-arrow)"/>
<text x="272" y="514" class="s tc">fed by Aladdin data</text><text x="272" y="530" class="s tc">and analytics</text>
<ellipse cx="272" cy="546" rx="80" ry="8" class="cyl"/><path d="M192 546 v42 a80 8 0 0 0 160 0 v-42" class="cyl"/>
<text x="272" y="570" class="tt tc">Aladdin Data Cloud</text><text x="272" y="587" class="s tc">Snowflake, this client’s own</text>
<path d="M380 566 H 354" class="arr" marker-end="url(#pm-arrow)"/>

<!-- outside -->
<text x="1140" y="290" class="cap">OUTSIDE ALADDIN</text>
<rect x="1140" y="300" width="136" height="44" rx="4" class="tile"/><text x="1150" y="319" class="tt">Brokers</text><text x="1150" y="336" class="s">orders, confirms</text>
<path d="M1080 312 H 1138" class="arr" marker-start="url(#pm-arrow)" marker-end="url(#pm-arrow)"/>
<rect x="1140" y="352" width="136" height="44" rx="4" class="tile"/><text x="1150" y="371" class="tt">Custodians</text><text x="1150" y="388" class="s">settle, reconcile</text>
<path d="M1080 324 L 1138 368" class="arr" marker-start="url(#pm-arrow)" marker-end="url(#pm-arrow)"/>
<rect x="1140" y="546" width="136" height="44" rx="4" class="tile"/><text x="1150" y="565" class="tt">Data vendors</text><text x="1150" y="582" class="s">prices, ESG, Preqin</text>
<path d="M1138 568 H 1097" class="arr" marker-end="url(#pm-arrow)"/>
</svg>'''

ARIA = ("Platform map of institutional Aladdin. People use about 100 apps such as Explore, Dashboard and Risk Radar, with Aladdin Copilot as a chat panel inside each app. "
        "Apps, Copilot and Aladdin Studio call one shared API layer, which reaches the 11 public API domains, all using Aladdin Analytics, the risk engine. "
        "Every domain reads and writes shared data: orders and trades, positions, accounting, portfolios and securities. Aladdin Studio holds the AladdinSDK, research sandboxes, "
        "Excel tools and feeds, and Aladdin Data Cloud, fed by Aladdin data and analytics. Outside, brokers and custodians exchange orders and settlements, and data vendors feed prices in. "
        "Hosting is Azure today, with an AWS option announced for the second half of 2026.")

TITLE = "Every app, Copilot and Studio call one API layer, and the 11 public domains sit behind it"

NOTES = ('<div class="notes"><p><span class="lead">For illustrative purposes only.</span> <span class="lbl"></span>Source: about 100 apps, with Copilot in all of them, '
         '<a href="https://www.youtube.com/watch?v=oyqeCHFM5U4&amp;t=155s">Rosales and Vicente Valdez at 2:35</a><sup class="fnref"><a href="#s9">9</a></sup>. '
         'The 11 domains are the packages of BlackRock’s public SDK, named as in its specifications<sup class="fnref"><a href="#s17">17</a>, <a href="#s24">24</a></sup>. '
         'App names other than Explore come from field descriptions in those specifications, so their screens are not drawn<sup class="fnref"><a href="#s17">17</a>, <a href="#s21">21</a></sup>. '
         'Aladdin Analytics is the name the risk specifications give the engine<sup class="fnref"><a href="#s17">17</a></sup>. '
         'Studio, <a href="https://www.youtube.com/watch?v=Me_H_-E6lSg&amp;t=289s">Woodhead at 4:49</a><sup class="fnref"><a href="#s5">5</a></sup>; '
         'Excel tools and feeds, the APIs page<sup class="fnref"><a href="#s23">23</a></sup>; '
         'Data Cloud fed by Aladdin data and analytics<sup class="fnref"><a href="#s5">5</a>, <a href="#s19">19</a></sup>; '
         'hosting<sup class="fnref"><a href="#s58">58</a>, <a href="#s14">14</a></sup>. '
         'Solid outline = shown in sources; hatched = announced, not live.</p></div>')

NEW3 = ('<figure class="exhibit keep" id="exhibit-3"><p class="ex-title"><span class="ex-num">Exhibit 3.</span> ' + TITLE + '</p>\n'
        '<div role="img" aria-label="' + ARIA + '">\n' + SVG + '\n</div>\n' + NOTES + '</figure>')

# ---- replace Exhibit 3
a = h.index('<figure class="exhibit" id="exhibit-3">')
b = h.index('</figure>', a) + len('</figure>')
old3 = h[a:b]
assert 'class="arch"' in old3 and 'Exhibit 3.' in old3
h = h[:a] + NEW3 + h[b:]

# ---- Exhibit 4: retitle and drop two rows
old_t = '<span class="ex-num">Exhibit 4.</span> Studio has eight pieces, and the catalog, guides, notebooks and samples all sit behind a client login</p>'
new_t = '<span class="ex-num">Exhibit 4.</span> Six pieces make up Studio, no event specification is public, and the catalog, guides, notebooks and samples all sit behind a client login</p>'
assert h.count(old_t) == 1; h = h.replace(old_t, new_t)
for first in ['Investment research', 'Aladdin Tools for Excel']:
    m = re.search(r'<tr><td class="first">' + re.escape(first) + r'</td>.*?</tr>\n', h, re.S)
    assert m and m.start() > a and m.start() < h.index('id="exhibit-5"'), first
    h = h[:m.start()] + h[m.end():]
assert 'eight pieces' not in h and 'class="arch"' not in h
open(F, 'w', encoding='utf-8').write(h)
print('ok; exhibit-3 replaced, exhibit-4 trimmed')
