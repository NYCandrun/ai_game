import re,sys
S='/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad'
h=open(S+'/redraw34/preview.html',encoding='utf-8').read()
def R(o,n,c=1):
    global h; assert h.count(o)==c,(o[:80],h.count(o)); h=h.replace(o,n)
sup=lambda *ns:'<sup class="fnref">'+', '.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'
LSEG='https://www.lseg.com/en/media-centre/press-releases/2026/london-stock-exchange-group-plc-q1-2026-trading-update'
# 1 LSEG: primary source replaces the Investing.com summary as entry 74
R(re.search(r'<p id="s74">.*?</p>',h).group(0),
  f'<p id="s74"><b class="n">74</b><span class="g">P</span><span class="t">London Stock Exchange Group plc: Q1 2026 Trading Update</span>. LSEG press release, April 23, 2026. <a href="{LSEG}">{LSEG}</a></p>')
R(sup(74)+'. The figure comes from a secondary summary of its results slides.</p>', sup(74)+'.</p>')
R(' The LSEG customer count is from a secondary summary'+sup(74)+'.','')
inv=re.search(r'; <a href="https://www.investing.com[^>]*>[^<]*</a>'+re.escape(sup(74)),h).group(0)
R('LSEG press release</a>'+sup(2)+inv, 'LSEG press releases</a>'+sup(2,74))
# 2 Get help row: PR 53 (client engineer) replaces PR 57 (BlackRock engineer)
R('<a href="https://github.com/blackrock/aladdinsdk/pull/57">SDK change for Pydantic v2</a>'+sup(89),
  '<a href="https://github.com/blackrock/aladdinsdk/pull/53">SDK change for extra HTTP headers</a>'+sup(56))
h=re.sub(r'<p id="s89">.*?</p>\n','',h,flags=re.S)
# 3 Crockett
R('Microsoft’s Adrian Crockett said Copilot depends on its plugins:','Microsoft’s Adrian Crockett said firms building their own copilots need plugins:')
# 4 Sewdass
R('She said clients have moved over the last two years “to more of a modular approach”','She said clients are making a “move to more of a modular approach”')
# 5 HPS
R('The team said it designed the new types with BlackRock’s own professionals','The team said it designed its private credit data model with BlackRock’s own professionals')
# 6 Exhibit 4 source note
R('Source: BlackRock’s Studio, APIs, ATX and ADX pages, which list Data Cloud, ADX, Aladdin Compute and ATX as “Additional Aladdin Studio resources”'+sup(14,30,32,33),
  'Source: BlackRock’s Studio page'+sup(14)+'; its APIs, ATX and ADX pages, which list Data Cloud, ADX, Aladdin Compute and ATX as “Additional Aladdin Studio resources”'+sup(30,32,33))
# 7 job posting
R('</a> calls Studio “Aladdin’s extensibility layer”'+sup(48),'</a> calls Studio Developer “Aladdin’s extensibility layer”'+sup(48))
# 8 commit patch moves to the sentence it supports
R('submitted two changes to the <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a>.','submitted two changes to the <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a>'+sup(57)+'.')
R('accepted both into the SDK'+sup(38,55,56,57),'accepted both into the SDK'+sup(38,55,56))
open(S+'/fix8/preview_fix8.html','w',encoding='utf-8').write(h)
print('ok')
