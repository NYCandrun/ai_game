import sys
F = sys.argv[1]
html = open(F, encoding="utf-8").read()
def rep(old, new, count=1):
    global html
    n = html.count(old)
    assert n == count, f"expected {count}, found {n}: {old[:90]!r}"
    html = html.replace(old, new)
# Exhibit 4 APIs row: back to four lines after the wider superscripts
rep('Defined ways for a program to read and write Aladdin data.', 'Ways for a program to read and write Aladdin data.')
rep('The 54 public specs include', 'The 54 specs include')
# summary: one line out of each body paragraph, one out of the box, tighter list and source margins
rep('a Python SDK on GitHub and Aladdin Data Cloud on Snowflake, described the same way', 'a Python SDK and Aladdin Data Cloud on Snowflake, described the same way')
rep('Proof of use sits in public records: JPMorgan', 'Proof of use is public: JPMorgan')
rep('I assembled that picture with AI agents in about a day, from 54 public API specifications, 128 recordings, filings and code.</p>',
    'I assembled that with AI agents in about a day from 54 API specifications, 128 recordings, filings and code.</p>')
rep('<p>Four signals point the same way. API calls are the fastest-growing measure BlackRock showed investors, 17x by 2030, though the slide does not name the products behind the calls; reading them as Studio is my inference.',
    '<p>API calls are the fastest-growing measure BlackRock showed investors, 17x by 2030, though the slide does not name the products behind the calls, so Studio is my inference.')
rep('128 recordings (121 from BlackRock’s own channels and partner stages), SEC filings', '128 recordings, SEC filings')
rep('<li style="margin-bottom:2pt">', '<li style="margin-bottom:0">', 6)
rep('<p class="stats-src">', '<p class="stats-src" style="margin-bottom:12pt">')
open(F, 'w', encoding='utf-8').write(html)
print('ok')
