import sys, re
F = sys.argv[1]
html = open(F, encoding="utf-8").read()
def rep(old, new, count=1):
    global html
    n = html.count(old)
    assert n == count, f"expected {count}, found {n}: {old[:90]!r}"
    html = html.replace(old, new)

# --- executive summary: compact ---
rep('<p class="lede">Studio is the product behind the growth story BlackRock tells investors, but the story never names it, and the public proof that clients build on Aladdin is real but not Studio-specific. The quick wins close both gaps inside the enterprise selling model, without changing what a prospect can access.</p>',
    '<p class="lede">Studio is the product behind the growth story BlackRock tells investors, but the story never names it, and the public proof that clients build on Aladdin is not Studio-specific. The quick wins close both gaps inside the enterprise selling model.</p>')
rep('<p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, on the 2025 Investor Day slide on keeping the cost of growth low, against 4x for model portfolios, 2x for portfolios and 1.3x for trade allocations</p>',
    '<p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, the fastest-growing measure on the 2025 Investor Day slide on keeping the cost of growth low</p>')
rep('<p class="cap">JPMorgan Chase’s payments to BlackRock for Aladdin in 2025, reported in its own proxy statement; almost six times the 2017 figure</p>',
    '<p class="cap">JPMorgan Chase’s payments to BlackRock for Aladdin in 2025, in its own proxy statement; almost six times the 2017 figure</p>')
rep('<p class="cap">Mentions of Studio by a BlackRock executive on 26 earnings calls since 2020, Q1 2020 to Q2 2026</p>',
    '<p class="cap">Mentions of Studio by a BlackRock executive on 26 earnings calls, Q1 2020 to Q2 2026</p>')
rep('BlackRock 2025 Investor Day</a><sup class="fnref"><a href="#s1">1</a></sup>; the slide does not say which products generate the API calls, so reading them as Studio is my inference. <a href=',
    'BlackRock 2025 Investor Day</a><sup class="fnref"><a href="#s1">1</a></sup>, slide on keeping the cost of growth low: API calls 17x, model portfolios 4x, portfolios 2x, trade allocations 1.3x; the slide does not say which products generate the API calls, so reading them as Studio is my inference. <a href=')
rep(' I assembled that picture with AI agents in about a day, from 54 public API specifications, 128 recordings, filings and code; Part 1 is what it shows.</p>',
    ' I assembled that picture with AI agents in about a day, from 54 public API specifications, 128 recordings, filings and code.</p>')
rep('<p>Six quick wins, in the order I would do them:</p>\n<ol>\n', '<p style="margin-bottom:4pt">Six quick wins, in the order I would do them:</p>\n<ol style="margin-bottom:8pt">\n')
for item in ['Named proof from clients', 'Studio’s name beside the API-call', 'A written one-page version of the definition', 'An RFP-ready answer', 'A published description', 'A prospect-facing “what is in the box” summary of the public catalog']:
    rep('<li>' + item, '<li style="margin-bottom:2pt">' + item)

# --- Exhibit 7 paragraph: back below the exhibit (it does not fit above with Exhibit 6) ---
m = re.search(r'<p>Exhibit 7 puts Studio beside 10 platforms.*?</p>\n', html, flags=re.S)
para = m.group(0)
html = html.replace(para, '', 1)
rep('</div></figure>\n<figure class="exhibit keep" id="exhibit-7">', '</div></figure>\n\n<figure class="exhibit keep" id="exhibit-7">')
rep('</div></figure>\n<p>Five BlackRock speakers define Studio', '</div></figure>\n' + para + '\n<p>Five BlackRock speakers define Studio')

# --- Finding 1: pull the orphaned last line of paragraph 1 back ---
rep('names no client as building on Studio<sup', 'names no client building on Studio<sup')
rep('finds no filing that mentions it<sup', 'finds no filing mentioning it<sup')
rep('On BlackRock’s own client video, Royal London’s', 'On BlackRock’s client video, Royal London’s')
rep('proxy statement</a> every year: $4.4 million', 'proxy statement</a> each year: $4.4 million')

# --- Finding 2: drop the two hedge sentences to pay for the 17x clause ---
rep('describes<sup class="fnref"><a href="#s13">13</a></sup>. The investor story is told without the product’s name. Across',
    'describes<sup class="fnref"><a href="#s13">13</a></sup>. Across')
rep('API calls appear in none of those terms<sup class="fnref"><a href="#s10">10</a>, <a href="#s1">1</a></sup>. Exhibit 12 is an observation about how the story is told.</p>',
    'API calls appear in none of those terms<sup class="fnref"><a href="#s10">10</a>, <a href="#s1">1</a></sup>.</p>')

open(F, 'w', encoding='utf-8').write(html)
print('ok')
