import sys
F = sys.argv[1]
h = open(F, encoding='utf-8').read()
head, body = h.split('</head>', 1)
def R(a, b):
    global body
    assert body.count(a) == 1, (body.count(a), a[:70])
    body = body.replace(a, b)
# 1 Finding 3 paragraph 2
R('Seven providers that Studio buyers also use offer a connector or an MCP server.',
  'Six data and cloud providers that Studio buyers also use offer a connector or an MCP server, and two system-of-record rivals have announced AI features.')
# 2 four speakers
R('Write the one-page definition of Studio that five speakers so far give only in recordings.',
  'Write the one-page definition of Studio that four speakers so far give only in recordings.')
R('Turn the definition five speakers already give<sup class="fnref"><a href="#s5">5</a>, <a href="#s15">15</a>, <a href="#s25">25</a>, <a href="#s40">40</a>, <a href="#s41">41</a></sup> into one written page.',
  'Turn the definition four speakers already give<sup class="fnref"><a href="#s5">5</a>, <a href="#s15">15</a>, <a href="#s25">25</a>, <a href="#s40">40</a></sup> into one written page.')
# 3 Exhibit 17 row 5
R('and how clients will connect their own AI tools. Publish it when the work described in the Forward Deploy Engineer posting<sup class="fnref"><a href="#s65">65</a></sup> is ready</td>',
  'and how clients will connect their own AI tools. Publish the plugin-model and governance parts now; add the client AI-tool section when the work described in the Forward Deploy Engineer posting<sup class="fnref"><a href="#s65">65</a></sup> is ready</td>')
# 4 Exhibit 14 source note
R('State Street Alpha, Charles River and Bloomberg have none there, so they are not listed.',
  'State Street, Clearwater and Bloomberg have none in my sources, so they are not listed.')
# 5 Finding 2 fee sentence (merged with the preceding sentence so the fact is stated once, with its receipts)
R('API calls appear in none of those fee terms<sup class="fnref"><a href="#s10">10</a>, <a href="#s1">1</a></sup>. So the measure BlackRock projects to grow fastest is not one it says it charges for.</p>',
  'The 10-K does not list API calls among the fee terms it names<sup class="fnref"><a href="#s10">10</a>, <a href="#s1">1</a></sup>.</p>')
# 6 Exhibit 11 weights
R('<td>Technical 85%, price 6%, price sensitivity 6%, contract terms 3%</td>', '<td>Technical 85, price 6, price sensitivity 6, contract terms 3</td>')
R('<td>Quality 70%, cost 20%, social value 10%</td>', '<td>Quality 70, cost 20, social value 10</td>')
# 7 minor
R('<p class="indep">Independent analysis from public sources. Not produced, reviewed or endorsed by BlackRock.</p>',
  '<p class="indep">Independent analysis from public sources with AI agents. Not produced, reviewed or endorsed by BlackRock.</p>')
R('said a platform transformation runs', 'said a transformation runs')
R('BlackRock’s own marketing agrees: its <a href="https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework">August 2026 insight</a> piece says',
  'BlackRock’s own <a href="https://www.blackrock.com/aladdin/discover/insights/build-vs-buy-decision-framework">August 2026 insight</a> page says the same:')
R('AI features in Aquata, its data platform, and an AI platform announcement', 'AI features in Aquata, and an AI platform announcement')
R('Data Cloud, API and Copilot came up four times in total', 'Data Cloud, API and Copilot came up about four times in total')
# 8 residual readability
R('The SDK’s dependencies also <a href="https://github.com/blackrock/aladdinsdk/pull/57">conflict with the official toolkit for MCP</a>, the Model Context Protocol, the common standard AI assistants use to pull data from other systems. An outside',
  'The SDK’s dependencies also <a href="https://github.com/blackrock/aladdinsdk/pull/57">conflict with the official MCP toolkit</a>. (MCP, the Model Context Protocol, is the standard AI assistants use to pull data from other systems.) An outside')
R('For the AI connector, 2 means a connector that outside AI tools can use, such as an MCP server; 1 means one announced or in limited release; 0 means none, or an assistant that works only inside the vendor’s own platform.',
  'For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform.')
R('JPMorgan is also a custodian, and <a href="https://www.thetradenews.com/jp-morgan-to-connect-to-blackrocks-aladdin/">in 2016 it said it was connecting to Aladdin</a> for custody clients<sup class="fnref"><a href="#s45">45</a></sup>; that 2016 report is trade press',
  'JPMorgan is also a custodian. <a href="https://www.thetradenews.com/jp-morgan-to-connect-to-blackrocks-aladdin/">In 2016 it said it was connecting to Aladdin</a> for custody clients<sup class="fnref"><a href="#s45">45</a></sup>. That 2016 report is trade press')
R('built on the platform and stayed; proof from one firm counts', 'built on the platform and stayed. Proof from one firm counts')
R('I make it because API use is the activity', 'I make that inference because API use is the activity')
R('In BlackRock’s own words, that answers the RFP connector question better than', 'Said in BlackRock’s own words, that description answers the RFP connector question better than')
R('Shortlist clients whose Aladdin relationship is already on the record: the public funds whose tenders BlackRock won (the Pension Protection Fund, Nest, PBGC), the SEC filers that disclose Aladdin (JPMorgan Chase, Janus Henderson), and Royal London, which is already on video<sup',
  'Shortlist clients already on the record. Public funds whose tenders BlackRock won: the Pension Protection Fund, Nest, PBGC. SEC filers that disclose Aladdin: JPMorgan Chase, Janus Henderson. And Royal London, already on video<sup')
R('A document that answers the question Schafer says buyers now ask<sup class="fnref"><a href="#s8">8</a></sup>: which API domains exist, how many specifications and operations each has and at what status, what connectors exist for Snowflake and Databricks, and how clients build on top. The solutions team',
  'A document that answers the question Schafer says buyers now ask<sup class="fnref"><a href="#s8">8</a></sup>. It lists the API domains, the specification and operation counts and status for each, the Snowflake and Databricks connectors, and how clients build on top. The solutions team')
R('<span class="ex-num">Exhibit 14.</span> Two system-of-record rivals have announced AI features and the data vendors have shipped or announced AI access to their data; Aladdin has only a job advert that mentions MCP</p>',
  '<span class="ex-num">Exhibit 14.</span> Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data; Aladdin has only a job advert that mentions MCP</p>')
open(F, 'w', encoding='utf-8').write(head + '</head>' + body)
print('meaning edits applied: 22')
