import sys,re
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
SUP=r'<sup class="fnref">(?:<a href="#s\d+">\d+</a>(?:, )?)+</sup>'
def sub(pat,repl,flags=0):
    global s
    n=len(re.findall(pat,s,flags)); assert n==1,(n,pat[:80]); s=re.sub(pat,repl,s,flags=flags)
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
# [1] cover Part 3 card
sub(r'\n    <div><span class="accent-bar"></span><p class="pn">Part 3</p>.*?</div>','',re.S)
# subtitle
rep('What public sources show about Studio and the likely initial directions for marketing it','What public sources show about Studio')
# [2] page 2 list
sub(r'<p style="margin-bottom:4pt">Five likely initial directions:</p>\n<ol[^>]*>.*?</ol>\n','',re.S)
# [3][4][5] framing paragraph
rep('Everything here was read from outside the login, which limits','Everything here was read from outside, which limits')
rep('it relies on what the sources say. Some gaps are gaps in the public record: no event specification, no position API, no public connector for AI tools. Gating is one selling model, not the only one, and Exhibit 2 shows how differently providers draw the line.</p>','it relies on what sources say.</p>')
# [6] SDK paragraph
sub(r'<p>The SDK’s dependencies <a href="[^"]+">conflict with the official MCP toolkit</a>\. An outside contributor’s fix for the conflict was merged in August 2026 and has not shipped'+SUP+r'\. The README documents','<p>The SDK’s README documents')
# [7]
sub(r' Among the investment platforms, only Studio offers an <a href="[^"]+">open-source SDK</a>'+SUP+r'\.</p>','</p>')
# [8]
rep('Gives the three-part definition quoted above. Puts BlackRock’s internal citizen developers at 3,000, a figure Goel also gives</td>','Gives the three-part definition quoted above</td>')
# [9]
sub(r' Woodhead names them outright'+SUP+r'\.','.')
s=s.replace('with the same three parts..','with the same three parts.')
# [10] Exhibit 5 Studio row + note
sub(r', and developer tools, of which the open-source Python SDK and Aladdin Compute are the public ones'+SUP+r'\. BlackRock calls it',', and developer tools. BlackRock calls it')
sub(r'; the SDK README'+SUP+r'\.</p></div></figure>','.</p></div></figure>')
# [11]
rep('<th>Public API that covers it</th>','<th>API that covers it</th>')
# [12][13][14][15] Exhibit 8 cells
sub(r' The <a href="[^"]+">APIs page</a> says there are “dozens,” with more added regularly'+SUP+r'\. The 54 specifications include orders, trades, compliance rules, risk rules, security creation and Data Cloud datasets'+SUP+r'\.</td>','</td>')
sub(r' No event specification is in the public packages'+SUP+r'\.</td>','</td>')
sub(r' Woodhead: (?:<a href="[^"]+">)?“hundreds of Snowflake accounts \S+ tens of thousands of pipelines”(?:</a>)?'+SUP+r'\.</td>','</td>')
sub(r' All sit behind a client login'+SUP+r'\.</td>','</td>')
# [16][17] Finding 2
rep('<p>BlackRock tells investors growth will come from two things: API calls, and the whole portfolio, public and private markets together. It projected at its','<p>BlackRock projected at its')
sub(r' That was the fastest-growing measure on the slide, which was about keeping the cost of growth low\. Model portfolios were projected at 4x, portfolios at 2x and trade allocations at 1\.3x\. The slide gives no starting number and does not say which products generate the API calls\. Attributing',' Attributing')
# [18] page 12
sub(r' One public hint is a job advert: a <a href="[^"]+">Forward Deploy Engineer posting</a> for Aladdin Data names “Model Context Protocol \(MCP\), AI agents, and Copilot extensions”'+SUP+r'\. Exhibit 14 lists both comparisons a Studio buyer makes: the system-of-record rivals and the data vendors\.</p>','</p>')
# [19]
rep('<td>None found. A Forward Deploy Engineer posting','<td>A Forward Deploy Engineer posting')
# [20] Part 3
sub(r'<section class="chapter part" id="part-3">.*?</section>\n','',re.S)
# About
rep('    <p>The directions in Part 3 are my proposals, based on Part 1 and the findings in Part 2.</p>\n','')
open(p,'w',encoding='utf-8').write(s); print('cuts2 ok')
t=re.sub(r'<[^>]+>','',s)
for ph in ['Part 3','direction','Exhibit 16','Five likely','None found','citizen developers at 3,000','only Studio offers','MCP toolkit','sources say']:
    print(ph,t.count(ph))
