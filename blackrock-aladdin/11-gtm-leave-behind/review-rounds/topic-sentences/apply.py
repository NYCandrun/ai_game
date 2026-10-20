import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
# 1 exec summary
rep('<p style="margin-bottom:8pt">API calls are the fastest-growing measure',
    '<p style="margin-bottom:8pt">BlackRock’s investor story and its buyers’ own answers both point to Studio. API calls are the fastest-growing measure')
# 2 SDK paragraph
rep('<p>The SDK’s README documents three run modes',
    '<p>The SDK is the one piece of Studio a prospect can install before any conversation. Its README documents three run modes')
# 3 recordings + definition + Exhibit 3 lead-in merged
rep('<p>I pulled 128 recordings for this document<sup class="fnref"><a href="#s9">9</a>, <a href="#s10">10</a></sup>. Five BlackRock speakers define Studio in them.</p>\n<p>BlackRock’s own definition of Studio comes from the head of Studio engineering, on Snowflake’s podcast in November 2025.</p>',
    '<p>Five BlackRock speakers define Studio in the 128 recordings I pulled for this document<sup class="fnref"><a href="#s9">9</a>, <a href="#s10">10</a></sup>; Exhibit 3 lists each with the title the recording gives. BlackRock’s own definition comes from the head of Studio engineering, on Snowflake’s podcast in November 2025.</p>')
rep('<p>Exhibit 3 lists each speaker with the title the recording gives.</p>\n','')
# 4 specifications paragraph
rep('<p>Posting an order takes','<p>The specifications say more than Exhibit 9’s counts: they show how the APIs behave. Posting an order takes')
# 5 Janus paragraph
rep('<p>In December 2025 a Janus Henderson engineer','<p>A second kind of record is code written by a client’s engineers. In December 2025 a Janus Henderson engineer')
# 6 Finding 2 opener
rep('<p>BlackRock projected at its','<p>BlackRock tells investors growth will come from API calls, without naming the product behind them. It projected at its')
# 7 eFront paragraph
rep('<p>BlackRock bought eFront in 2019','<p>The private-markets data BlackRock has been adding reaches clients through Data Cloud and Explore. BlackRock bought eFront in 2019')
# 8 Finding 3 opener
rep('<p><a href="https://www.blackrock.com/aladdin/platforms/products/aladdin-copilot">Aladdin Copilot</a> draws on a registry',
    '<p><a href="https://www.blackrock.com/aladdin/platforms/products/aladdin-copilot">Aladdin Copilot</a>, the AI inside the login, is built on the same APIs Studio exposes. It draws on a registry')
# 9 providers paragraph
rep('<p>Six data and cloud providers that Studio buyers also use','<p>Exhibit 14 lists what the providers a Studio buyer compares have made public about AI access. Six data and cloud providers that Studio buyers also use')
# 10 About
rep('<p>Facts are as of October 19, 2026, unless an exhibit gives another date. Underlined text','<p>Underlined text')
rep('BlackRock did not produce, review or endorse it.</p>','BlackRock did not produce, review or endorse it. Facts are as of October 19, 2026, unless an exhibit gives another date.</p>')
open(p,'w',encoding='utf-8').write(s); print('ok')
