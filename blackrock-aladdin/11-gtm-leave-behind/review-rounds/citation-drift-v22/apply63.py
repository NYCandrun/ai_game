# Applies the 68 approved should-fix rewrites (plus the page-14 author edit) to preview_before63.html -> preview.html
import re, subprocess, sys
R = "/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/redraw34"
G = "/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm"
h = open(R + "/preview_before63.html", encoding="utf-8").read()
done = {}
def rep(n, old, new, cnt=1):
    global h
    c = h.count(old)
    assert c == cnt, (n, c, old[:100])
    h = h.replace(old, new)
    done.setdefault(n, 0); done[n] += 1
def S(*nums):
    return '<sup class="fnref">' + ', '.join(f'<a href="#s{x}">{x}</a>' for x in nums) + '</sup>'

# ---------------- Pages 1-4 ----------------
rep(1, 'Aladdin’s APIs also change the book.', 'Aladdin’s APIs can also write, not only read.')
rep(2, 'Posting an order runs compliance by default. The caller can turn it off' + S(6) + '.</p>\n<p style="margin-bottom:8pt">Letting AI tools act',
       'Posting an order runs compliance by default. The caller can turn it off' + S(6) + '. An AI tool calling these APIs would work under the same controls.</p>\n<p style="margin-bottom:8pt">Letting AI tools act')
rep(3, 'Letting AI tools act will not stay unique; SimCorp and Clearwater have announced AI agents' + S(7, 8) + '. What BlackRock can show is its own use.',
       'Aladdin will not be alone in letting AI tools act. SimCorp and Clearwater have announced AI agents' + S(7, 8) + '. BlackRock’s advantage is that it already runs its own business this way.')
done[4] = 1  # item 4 applied in the same replacement as item 3 (page 2 only)
rep(5, 'Buyers say AI is changing what they build, and BlackRock has told investors that API calls will grow 17x by 2030' + S(10, 11) + '.',
       'Buyers of investment software say AI is changing what they build' + S(10) + '. BlackRock has told investors that API calls will grow 17x by 2030' + S(11) + '.')
rep(6, 'the 54 API specifications inside 11 public <code>asdk_plugin</code> Python packages',
       'the 54 API specifications inside BlackRock’s 11 public Python plugin packages (named <code>asdk_plugin</code>)')
rep(7, '<p class="subtitle">What public sources show, and why clients’ AI tools could act on Aladdin under controls BlackRock’s own business runs on</p>',
       '<p class="subtitle">What public sources show. Clients’ AI tools could act on Aladdin under the same controls BlackRock uses for its own business.</p>')
rep(8, '<p class="indep">Independent analysis from public sources with AI agents. Not produced, reviewed or endorsed by BlackRock.</p>',
       '<p class="indep">Independent analysis of public sources, done with AI agents. Not produced, reviewed or endorsed by BlackRock.</p>')
rep(9, '$2.0 billion in 2025</a>, up 24 percent including Preqin, the private-markets data firm bought in 2025' + S(12) + '.',
       '$2.0 billion in 2025</a>' + S(12) + '. Its 24 percent rise includes Preqin, the private-markets data firm BlackRock bought in 2025' + S(12) + '.')
rep(10, 'available to all Aladdin clients</a> that gives no investment advice' + S(23) + '</td>',
        'available to all Aladdin clients</a>. It gives no investment advice' + S(23) + '</td>')
rep(11, 'Gives custodians and administrators access to Aladdin, and <a href="https://www.blackrock.com/uk/literature/prospectus/ishares-v-plc-prospectus-en.pdf">they pay BlackRock for it</a>',
        'Gives custodians and administrators access to Aladdin. <a href="https://www.blackrock.com/uk/literature/prospectus/ishares-v-plc-prospectus-en.pdf">These providers pay BlackRock for it</a>')
rep(13, '<div class="det">Posting takes <code>whatIf</code> and <code>runCompliance</code>' + S(6) + '</div>',
        '<div class="det">Test (<code>whatIf</code>) and compliance (<code>runCompliance</code>)' + S(6) + '</div>')
rep(14, '<span class="ex-num">Exhibit 3.</span> Where Studio sits in Aladdin</p>',
        '<span class="ex-num">Exhibit 3.</span> Clients reach Aladdin through Studio, and the APIs carry their own controls</p>')
rep(15, '<div class="wl">Who builds</div>', '<div class="wl">Who builds on Studio</div>')
rep(16, 'The 11 domains are the packages of BlackRock’s public SDK. <span class="lbl">',
        'The 11 domains are the packages of BlackRock’s public software development kit (SDK). <span class="lbl">')
rep(19, 'Every public specification’s id starts <code>agraph.&lt;domain&gt;</code></span>',
        'Every public specification’s ID begins <code>agraph.&lt;domain&gt;</code>, for Aladdin Graph</span>')
rep(19, 'every public specification id starts agraph.domain.', 'every public specification ID begins agraph.domain, for Aladdin Graph.')

# ---------------- Pages 5-8 ----------------
rep(20, '<p>The specifications say more than Exhibit 5’s counts: they show how the APIs behave. ',
        '<p>The specifications also show how the APIs behave. They set out several controls. ')
rep(21, 'Posting an order takes <code>whatIf</code> and <code>runCompliance</code>, which defaults to true, and the response returns any compliance violations inline' + S(6) + '. ',
        'An order can be posted as a test (the <code>whatIf</code> setting). A compliance check runs by default (<code>runCompliance</code>). The response lists any compliance breaches with the order' + S(6) + '. ')
rep(22, 'Ten specifications expose an endpoint for long-running operations, and 35 operations are flagged as long-running' + S(6) + '. The <a href="https://github.com/blackrock/aladdinsdk">SDK polls them</a>' + S(33) + '.',
        'Some operations take time to finish. Ten specifications offer a way to track them, and 35 operations are marked long-running' + S(6) + '. The <a href="https://github.com/blackrock/aladdinsdk">SDK checks back on these operations at set intervals</a>' + S(33) + '.')
rep(24, 'Every request carries an application key and a second credential. That is an OAuth 2.0 token, a client key, or a user name and password' + S(6) + '. OAuth scopes look like <code>trading.order_management.order.v1.Order:read</code>' + S(6) + '. The <a href="https://github.com/blackrock/aladdinsdk">client ID and secret come from the Studio UI</a>' + S(33) + '.',
        'Every request carries an application key and a second credential. The second credential is an OAuth 2.0 token, a client key, or a user name and password' + S(6) + '. With OAuth, access is granted per API and per action. A typical OAuth scope reads <code>trading.order_management.order.v1.Order:read</code>' + S(6) + '. Developers get their <a href="https://github.com/blackrock/aladdinsdk">OAuth client ID and secret from Studio’s screens</a>' + S(33) + '.')
rep(25, 'Alpha, beta, stable and sunset are the stability labels each specification carries (its <code>x-aladdin-api-stability</code> field). The four columns count specs by label.</p>',
        'Each specification carries one stability label: alpha, beta, stable or sunset. The four columns count specifications by label. The 54 specifications span 11 domains and 11 PyPI packages. Domain names are BlackRock’s own, taken from each specification’s id.</p>')
done[26] = 1  # note sentences added with item 25; Total row cell emptied below
rep(26, '<td class="ex">11 domains, 11 PyPI packages</td>', '<td class="ex"></td>')
rep(27, 'Named “the Aladdin studio estate” as a 2024 focus, meaning programmatic access “at machine scale”',
        'Named “the Aladdin studio estate” a 2024 focus. Described it as programmatic access “at machine scale”')
rep(28, 'Quotations are verbatim from the transcripts; three of the five are machine transcriptions, marked as such in the Sources section at the end of this document.',
        'Quotations are verbatim from the transcripts. Three of the five transcripts are machine-made, as marked in the Sources section.')
rep(28, 'Quotations are verbatim. Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. Goel does not use the name Studio.',
        'Quotations are verbatim. Three of the four transcripts (Khara, Goel and Woodhead) are machine-made, as marked in the Sources section. Goel does not use the name Studio. Miller, in Exhibit 6, speaks only about Data Cloud replacing file transfers, so he is not shown.')
done[29] = 1  # Miller sentence added to the Exhibit 7 note above
rep(30, 'A 2026 <a href="https://careers.blackrock.com/job/new-york/senior-product-director-aladdin-studio-developer/45831/96232273856">job posting</a> for a product director of Aladdin Studio Developer calls it “Aladdin’s extensibility layer”' + S(50) + '.',
        'A 2026 <a href="https://careers.blackrock.com/job/new-york/senior-product-director-aladdin-studio-developer/45831/96232273856">job posting</a> calls Studio “Aladdin’s extensibility layer”' + S(50) + '. The role is a product director for Aladdin Studio Developer.')
rep(31, 'APIs and data access recur across speakers and years, so BlackRock already has the core of a positioning for Studio.</p>',
        'Speakers since 2024 describe Studio as APIs and data access. BlackRock can build Studio’s positioning on that shared description.</p>')
rep(32, 'On BlackRock’s video, Hans Georgeson, then chief executive of Royal London Asset Management, credits Aladdin’s <a href="https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management">Snowflake implementation</a>' + S(52) + '.',
        'In a BlackRock client video, Hans Georgeson praises the <a href="https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london-asset-management">Snowflake implementation</a> in Royal London’s Aladdin program' + S(52) + '. He was then chief executive of Royal London Asset Management.')
rep(33, 'submitted two changes to the <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a>: <a href="https://github.com/blackrock/aladdinsdk/pull/52">URL rewriting</a> and <a href="https://github.com/blackrock/aladdinsdk/pull/53">custom headers</a>. Both are for firms that route Aladdin calls through an enterprise gateway. The BlackRock engineer who co-wrote the SDK’s <a href="https://engineering.blackrock.com/open-sourcing-the-aladdinsdk-empower-python-developers-with-a-quantitative-edge-7f63376061e6">launch post</a> merged them' + S(34, 35, 40, 57) + '.',
        'submitted two changes to the <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a>. Both help firms that send Aladdin calls through their own enterprise gateway. One <a href="https://github.com/blackrock/aladdinsdk/pull/52">rewrites web addresses</a> and one <a href="https://github.com/blackrock/aladdinsdk/pull/53">adds custom headers</a>. The BlackRock engineer who co-wrote the SDK’s <a href="https://engineering.blackrock.com/open-sourcing-the-aladdinsdk-empower-python-developers-with-a-quantitative-edge-7f63376061e6">launch post</a> accepted both into the SDK' + S(34, 35, 40, 57) + '.')
rep(34, 'Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public. So they are the natural first candidates for a named Studio story.</p>',
        'Some clients are easier to name in public: public pension funds, and firms whose filings or tenders already name BlackRock. They are the natural first subjects for a Studio case study that names the client.</p>')
rep(34, 'A named Studio story can start with clients whose Aladdin use is already on the record.</p>',
        'A Studio case study that names the client can start with clients whose Aladdin use is already on the record.</p>')
rep(35, '2. BlackRock’s growth story to investors runs through Studio, though it rarely says the name</h2>',
        '2. BlackRock’s growth story to investors runs through Studio, but BlackRock rarely names Studio to investors</h2>')
rep(36, '2025 Investor Day</a> it forecast four volumes to 2030. API calls across BlackRock and Aladdin led, with 17x growth' + S(11) + '. Attributing them to Studio is my inference. I make that inference because API use is the activity the <a href="https://www.blackrock.com/aladdin/platforms/products/aladdin-studio">Studio page</a> describes' + S(14) + '.',
        '2025 Investor Day</a>, BlackRock forecast four usage measures to 2030. API calls across BlackRock and Aladdin had the fastest forecast growth, 17 times' + S(11) + '. I attribute those API calls to Studio, because the <a href="https://www.blackrock.com/aladdin/platforms/products/aladdin-studio">Studio page</a> describes API use' + S(14) + '.')
rep(37, 'They can also depend on subscriptions, go-lives and support. The 10-K does not list API calls among the fee terms it names' + S(12) + '.',
        'Fees can also depend on subscriptions, client launches (go-lives) and support. The 10-K does not list API calls among its fee terms' + S(12) + '. So, under the terms it names, more API calls do not by themselves raise fees.')
rep(38, 'My tally. The non-zero counts add up to about four mentions in six and a half years. A zero means the term appears in no transcript; the non-zero counts are approximate.',
        'The tally is mine. The non-zero counts total four mentions in six and a half years, and are approximate. A zero means the term appears in no transcript.')
rep(39, 'In September 2025 its private markets team described the result on a <a',
        'In September 2025 its private markets team described what the two deals brought clients, on a <a')
rep(39, 'And “over 10 different transaction types” were added to Aladdin, covering commitments, fundings, paydowns and PIK, so private credit loans are captured natively. The team said those were designed with BlackRock’s own professionals and “our new colleagues from HPS”' + S(70) + '.',
        'More than 10 new transaction types were added to Aladdin (“over 10 different transaction types”). They cover commitments, fundings, paydowns and payment in kind (PIK). So Aladdin now records private credit loans directly. The team said it designed the new types with BlackRock’s own professionals and “our new colleagues from HPS”' + S(70) + '. HPS is the credit investment manager BlackRock bought in July 2025' + S(12) + '.')

# ---------------- Pages 9-12 ----------------
rep(40, 'BlackRock projects API calls across BlackRock and Aladdin to grow 17x by 2030, the fastest of the four volumes it showed investors' + S(11) + '. The private-markets data it is adding from eFront and Preqin is going into Data Cloud, which is part of Studio' + S(22) + '.</p>',
        'BlackRock’s two growth bets both run through Studio. It projects API calls across BlackRock and Aladdin to grow 17x by 2030' + S(11) + '. That is the fastest of the four forecasts it showed investors' + S(11) + '. Its new eFront and Preqin private-markets data is going into Data Cloud, which is part of Studio' + S(22) + '. BlackRock could name Studio when it tells investors this growth story.</p>')
rep(41, 'It draws on a registry of plugins, <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“couple of thousands agents and tools,”</a> built by Aladdin’s engineering teams. The first way a team adds a tool is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production”' + S(9) + '. Teams can also register agents of their own' + S(9) + '.',
        'It draws on a registry of plugins built by Aladdin’s engineering teams. The speakers put it at a <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“couple of thousands agents and tools”</a>' + S(9) + '. Teams add to the registry in two ways. The first is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production”' + S(9) + '. The second is to register an agent of their own' + S(9) + '.')
rep(42, 'Microsoft’s Adrian Crockett made the dependence plain on BlackRock’s podcast: <a',
        'On BlackRock’s podcast, Microsoft’s Adrian Crockett said Copilot depends on its plugins: <a')
rep(43, '3. Aladdin’s AI answers inside the login; data providers let outside AI tools reach their data</h2>',
        '3. Aladdin’s AI works only for logged-in users. Data providers let outside AI tools reach their data.</h2>')
rep(43, 'Four system-of-record rivals have announced AI features or AI access to their data. LSEG had <a href="https://www.investing.com/news/company-news/lseg-q1-2026-slides-record-growth-ai-adoption-accelerates-93CH-4631412">90 customers connected</a> by April 2026, according to a secondary summary of its results slides' + S(73) + '.',
        'Four system-of-record rivals have announced AI features or AI access to their data. Many of the 11 offer an MCP (Model Context Protocol) server, a standard way for outside AI tools to connect. Aladdin has published no such route. Its only public mention of MCP is a job posting' + S(79) + '. LSEG had <a href="https://www.investing.com/news/company-news/lseg-q1-2026-slides-record-growth-ai-adoption-accelerates-93CH-4631412">90 customers connected to its MCP server</a> by April 2026' + S(73) + '. The figure comes from a secondary summary of its results slides.')
done[44] = 1  # body sentence rewritten in the replacement above
rep(44, 'It had 90 customers connected by April 2026</td>', 'It had 90 customers connected to its MCP server by April 2026</td>')
rep(45, 'Of the 11 providers I compared, ten have announced AI features or AI access to their data</p>',
        'Ten of the 11 providers I compared have announced AI features or AI access. Aladdin has not.</p>')
rep(46, '<thead><tr><th>Provider</th><th>What is public</th><th>Receipt</th></tr></thead>',
        '<thead><tr><th>Provider</th><th>What is public</th><th>Source</th></tr></thead>')
rep(46, 'job posting in the Receipt column, as of October 2026.', 'job posting in the Source column, as of October 2026.')
rep(47, 'The tool counts are the speakers’ own approximations; the talk is a machine transcription, marked as such in the Sources section.',
        'The tool counts are the speakers’ own estimates. Quotes come from a machine transcript of the talk, marked as such in Sources.')
rep(48, '<b>Plan and call the API</b>: an orchestrator loops <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a> using GPT-4 function calling. Output guardrails then check the answer for hallucinations' + S(9) + '</div>',
        '<b>Plan and call the APIs</b>: Copilot uses GPT-4 function calling to plan which tools to call, calls them, and repeats. The talk describes a loop <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a>' + S(9) + '. Output guardrails then check the answer for hallucinations' + S(9) + '</div>')
rep(49, 'She described the shift of the last two years. It is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows.” That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction.” Those APIs',
        'She said clients have moved over the last two years “to more of a modular approach”' + S(10) + '. They want “that backbone foundational data that supports both publics and privates workflows”' + S(10) + '. They also want “very, very robust APIs that manage the end to end life cycle of a transaction”' + S(10) + '. Those APIs')
rep(50, 'She also said “the other layer that is almost equally important is a really defined system of work”' + S(10) + '.</p>',
        'She called a “really defined system of work” the other layer that is “almost equally important”' + S(10) + '. By that she meant integrated workflows across portfolio management, trading, operations and compliance, governed by operational controls and run on the same data' + S(10) + '.</p>')
rep(51, '<p>The findings suggest that Studio could be presented as the place where a client’s own AI tools act on investment data under the same controls BlackRock’s own business runs on. ',
        '<p>BlackRock could present Studio as the place where a client’s own AI tools act on investment data. Those tools would run under the same controls as BlackRock’s own business. ')
rep(52, '<span class="ex-num">Exhibit 14.</span> BlackRock’s applications and a client’s code draw on Aladdin’s shared services and APIs</p>',
        '<span class="ex-num">Exhibit 14.</span> BlackRock’s apps, Copilot and client code share Aladdin’s APIs and controls. How a client’s AI tools would connect is not public.</p>')
rep(52, '<text x="640" y="269" class="s tc">BlackRock’s applications, Copilot and a client’s code draw on Aladdin’s shared services and APIs. Each client reads its own Data Cloud, which BlackRock runs on Snowflake.</text>',
        '<text x="640" y="269" class="s tc">Each client reads its own Data Cloud, which BlackRock runs on Snowflake.</text>')
rep(53, '''<text x="686" y="384" class="s">Off-topic content is caught</text>
<text x="686" y="404" class="s">and personal data handled</text>
<text x="686" y="424" class="s">before any plan.</text>''',
'''<text x="686" y="384" class="s">Copilot catches off-topic</text>
<text x="686" y="404" class="s">requests and handles personal</text>
<text x="686" y="424" class="s">data before it plans any</text>
<text x="686" y="444" class="s">API calls.</text>''')
rep(53, '''<text x="1086" y="362" class="tt">LLM judges</text>
<text x="1086" y="384" class="s">Every system prompt is tested</text>
<text x="1086" y="404" class="s">daily and on every change.</text>''',
'''<text x="1086" y="362" class="tt">AI-graded tests</text>
<text x="1086" y="384" class="s">AI models (“LLM judges”) test</text>
<text x="1086" y="404" class="s">every system prompt daily</text>
<text x="1086" y="424" class="s">and on every change.</text>''')
rep(54, ', the Copilot page' + S(23) + ', pull requests 52 and 53' + S(34, 35) + ', the SDK README' + S(33) + ', the public specifications' + S(6) + ',',
        ', the Copilot page' + S(23) + ', two SDK pull requests' + S(34, 35) + ', the SDK README' + S(33) + ', Aladdin’s public API specifications' + S(6) + ',')

# ---------------- Pages 13-16 ----------------
rep(55, '<span class="ex-num">Exhibit 16.</span> What I was not able to see from outside, and what opens after qualification</p>',
        '<span class="ex-num">Exhibit 16.</span> At each step, what is public today and what opens only after qualification</p>')
rep(56, '<p>Everything here was read from outside, which limits what this document can be sure of. ',
        '<p>I read everything here from outside, with no client login. So this document cannot confirm what clients see. ')
rep(57, 'Where this document describes those, it relies on what sources say.</p>',
        'Where this document describes the catalog, the guides or what a client receives, it relies on what sources say.</p>')
rep(58, 'For each step it records what is public today and what a client receives after qualification.',
        'For each step it records what is public today and what opens only to qualified prospects and clients.')
rep(59, 'A ready answer to “what APIs do you have, and can we connect to them”: the APIs by area with their stability labels, how permissions work, how a client routes calls through its own gateway, and an answer on Snowflake and Databricks connectors, plus how a client’s own AI tools would connect.</td>',
        'A ready answer to “what APIs do you have, and can we connect to them”. It lists the APIs by area, with stability labels. It explains permissions and how a client routes calls through its own gateway. It covers Snowflake and Databricks connectors, and how a client’s own AI tools would connect.</td>')
rep(60, '<td>Time to answer the API section of an RFP; RFPs that score Studio; how many of those are won</td>',
        '<td>Time to answer the API section of an RFP. Number of RFPs in which buyers score Studio. How many of those are won.</td>')
rep(61, '<td>Studio Compute; an API token or an OAuth application “registered via Studio UI”; and the client’s own Aladdin host to call</td>',
        '<td>Studio Compute (hosted Python), an API token or OAuth app “registered via Studio UI”, the client’s Aladdin address</td>')
rep(62, '<td>Pull requests on the SDK, reviewed and merged by a BlackRock engineer; on the Studio page, “Book a meeting” and “Download the brochure”</td>',
        '<td>SDK changes from outside developers, reviewed and merged by a BlackRock engineer. On the Studio page, “Book a meeting” and “Download the brochure”.</td>')
rep(63, '<a href="https://github.com/blackrock/aladdinsdk/pull/52">Pull request 52</a>' + S(34) + ', <a href="https://github.com/blackrock/aladdinsdk/pull/57">pull request 57</a>' + S(89),
        '<a href="https://github.com/blackrock/aladdinsdk/pull/52">SDK change for enterprise gateways</a>' + S(34) + ', <a href="https://github.com/blackrock/aladdinsdk/pull/57">SDK change for Pydantic v2</a>' + S(89))
rep(64, 'Its README documents three run modes: “a developer’s local machine,” <a href="https://github.com/blackrock/aladdinsdk">“Aladdin Studio Compute sessions”</a> and a test mode. It stores a prompted password in the operating system’s credential manager. It carries settings for firms that consume “the Aladdin APIs',
        'Its README shows it is built for firms with strict IT controls. It runs in three modes: “a developer’s local machine,” <a href="https://github.com/blackrock/aladdinsdk">“Aladdin Studio Compute sessions”</a> and a test mode. It keeps a password it asks for in the operating system’s credential manager. It has settings for firms that call “the Aladdin APIs')
rep(65, '<span class="ex-num">Exhibit 17.</span> Investment platforms, Studio among them, open to developers mostly after a relationship</p>',
        '<span class="ex-num">Exhibit 17.</span> Data platforms open to any developer, investment platforms like Studio mostly to clients</p>')
rep(66, '<span class="k0">0: None or blocked</span>', '<span class="k0">0: None, or closed to non-clients</span>')
rep(67, 'The pattern is each vendor’s selling model. Investment platforms cluster low because they gate. At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, a first API call needs a contract or a relationship. ',
        'The scores follow how each vendor sells. Investment platforms score low because a first API call needs a contract or a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium. Studio scores in line with them, but trails Bloomberg and Arcesium on AI connectors (0 against 2). ')
done[68] = 1  # added in the same replacement as item 67
rep('author', 'Exhibit 17 puts Studio beside 10 platforms that a Studio buyer also deals with.',
              'Exhibit 17 puts Studio beside 10 platforms that may compete with Aladdin for certain uses.')
rep(69, 'The sources are BlackRock product pages, investor presentations, SEC filings, a fund prospectus, procurement notices, press releases and job postings. They also include public code and packages on GitHub and PyPI, other vendors’ product and developer pages, blogs and trade press. The rest are transcripts of recordings and earnings calls with BlackRock speakers.',
        'The sources include BlackRock product pages, investor presentations, SEC filings, a fund prospectus, procurement notices, press releases and job postings. They also include public code and packages on GitHub and PyPI, other vendors’ product and developer pages, blogs and trade press. Finally, they include transcripts of recordings and earnings calls in which BlackRock speakers take part.')

# ---------------- Author edits, Exhibit 3 ----------------
rep('ex3-1', '<span class="c">Portfolio management, trading, risk, compliance, operations, accounting. BlackRock calls it “a common data language”.</span>',
             '<span class="c">Portfolio management, trading, risk, compliance, operations, accounting.</span>')
rep('ex3-2', 'BlackRock Aladdin also includes eFront, Aladdin Wealth and Preqin, as in Exhibit 1</span>',
             'BlackRock Aladdin also includes eFront, Aladdin Wealth and Preqin</span>')
rep('ex3-3', '<span class="c">Each API has its own OAuth scopes. Other sign-in methods carry none.</span></p>',
             '<span class="c">Each API has its own OAuth scopes.</span></p>')
rep('ex3-4', '<div><b>Data Cloud: data out</b> <span class="c">Aladdin data is pushed into Snowflake, read by SQL and shared to the client’s own Snowflake account</span></div>',
             '<div><b>Data Cloud: data out</b></div>')
rep('ex3-5', '<span class="c">Microsoft Azure and Amazon Web Services. General availability on AWS for US Aladdin Enterprise clients was set for the second half of 2026.</span>',
             '<span class="c">Microsoft Azure and Amazon Web Services.</span>')
rep('ex3-aria', 'operations and accounting, which BlackRock calls a common data language. BlackRock Aladdin',
                'operations and accounting. BlackRock Aladdin')
rep('ex3-note', 'the AWS release, for the platforms, “a common data language” and AWS timing' + S(21),
                'the AWS release, for the platforms' + S(21))

rep('ex3-6', '\n<p><span class="c">Data Cloud, storage and the Data eXchange have their own access controls: Snowflake roles and keys, S3 keys and SFTP.</span></p></div></div>',
             '</div></div>')
rep('ex3-6aria', ' which the caller can turn off. Data Cloud, storage and the Data eXchange have their own access controls. Below,',
                 ' which the caller can turn off. Below,')
_i = h.index('<div id="mapE"'); _j = h.index('</figure>', _i)
assert 'SQL' not in re.sub(r'for the domains, apps, controls and SQL access', '', h[_i:_j]), 'SQL still in Exhibit 3'
rep('ex3-7', 'the specifications and SDK, for the domains, apps, controls and SQL access' + S(6, 33),
             'the specifications and SDK, for the domains, apps and controls' + S(6, 33))

# ---------------- Author edit, Exhibit 14 ----------------
rep('ex14', '''<text x="36" y="384" class="s">Each API has its own OAuth</text>
<text x="36" y="404" class="s">scopes. Other sign-in</text>
<text x="36" y="424" class="s">methods carry none.</text>''',
'''<text x="36" y="384" class="s">Each API has its own OAuth</text>
<text x="36" y="404" class="s">scopes.</text>''')

# extra patches from command line hook (layout tightening), if any
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("tight", R + "/a63/tight.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    h = m.apply(h, rep.__globals__)
except FileNotFoundError:
    pass

P = R + "/preview.html"; open(P, "w", encoding="utf-8").write(h)
r = subprocess.run(["python3", "-I", G + "/renumber.py", P], capture_output=True, text=True); print(r.stdout[-400:], r.stderr[-1500:])
if r.returncode: sys.exit(1)
def fix(m):
    links = re.findall(r'<a href="#s\d+">\d+</a>', m.group(1))
    links = sorted(dict.fromkeys(links), key=lambda a: int(re.search(r'>(\d+)<', a).group(1)))
    return '<sup class="fnref">' + ', '.join(links) + '</sup>'
h = open(P, encoding="utf-8").read(); a = h.index('<div class="register">'); b = h.index('</div>\n</section>', a)
ents = re.findall(r'<p id="s\d+">.*?</p>\n', h[a:b], flags=re.S); ents.sort(key=lambda e: int(re.match(r'<p id="s(\d+)"', e).group(1)))
h = h[:a] + '<div class="register">\n' + ''.join(ents) + h[b:]; h = re.sub(r'<sup class="fnref">(.*?)</sup>', fix, h)
open(P, "w", encoding="utf-8").write(h)
print("items touched", len(done), sorted(done, key=str), "register entries", len(ents))
