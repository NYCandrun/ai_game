import sys, re
F = sys.argv[1]
html = open(F, encoding="utf-8").read()
def rep(old, new, count=1):
    global html
    n = html.count(old)
    assert n == count, f"expected {count}, found {n}: {old[:90]!r}"
    html = html.replace(old, new)

# summary: lede to three lines, captions to three lines, two-column ranked list
rep('<p class="lede">Studio is the product behind the growth story BlackRock tells investors, but the story never names it, and the public proof that clients build on Aladdin is not Studio-specific. The quick wins close both gaps inside the enterprise selling model.</p>',
    '<p class="lede">Studio is the product behind the growth story BlackRock tells investors, but the story never names it, and the public proof of adoption is not Studio-specific. The quick wins close both gaps inside the enterprise selling model.</p>')
rep('<p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, the fastest-growing measure on the 2025 Investor Day slide on keeping the cost of growth low</p>',
    '<p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, the fastest-growing measure on a 2025 Investor Day slide</p>')
rep('<p class="cap">JPMorgan Chase’s payments to BlackRock for Aladdin in 2025, in its own proxy statement; almost six times the 2017 figure</p>',
    '<p class="cap">JPMorgan Chase’s 2025 payments to BlackRock for Aladdin, per its proxy statement; almost six times 2017</p>')
rep('The fastest-growing measure BlackRock showed investors is API calls, 17x by 2030 against 4x for model portfolios, though the slide does not say which products generate the calls, so reading them as Studio is my inference.',
    'API calls are the fastest-growing measure BlackRock showed investors, 17x by 2030, though the slide does not name the products behind the calls; reading them as Studio is my inference.')
rep('<ol style="margin-bottom:8pt">', '<ol style="margin-bottom:8pt; columns:2; column-gap:18pt">')

# Exhibit 4: Goel row back to two lines
rep('Aladdin tells a program when something happens instead of the program asking. Woodhead names “APIs events” as one pillar<sup class="fnref"><a href="#s5">5</a></sup>; Diwakar Goel, Global Head of Data, Aladdin, sets the target as <a',
    'Aladdin tells a program when something happens. Woodhead names “APIs events” as one pillar<sup class="fnref"><a href="#s5">5</a></sup>; Diwakar Goel, Global Head of Data, Aladdin, wants <a')

# Finding 1: JPMorgan sentence shorter
rep('JPMorgan Chase reports its Aladdin payments in its <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A">proxy statement</a> each year: $4.4 million to $7.6 million from 2017 to 2023, then $14.7 million in 2024 and',
    'JPMorgan Chase’s <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0000019617&amp;type=DEF+14A">proxy statement</a> reports Aladdin payments of $4.4 million to $7.6 million a year from 2017 to 2023, then $14.7 million in 2024 and')

open(F, 'w', encoding='utf-8').write(html)
print('ok')
