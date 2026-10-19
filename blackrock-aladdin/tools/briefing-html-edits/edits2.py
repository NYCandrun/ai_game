# ================= 7. ALADDIN STUDIO IN DEPTH =================
# Woodhead three pillars after the script block
rep('Copilot sits on top and uses those same APIs as plugins.”</p></div><h3 id="7-aladdin-studio-in-depth--the-pieces">',
    'Copilot sits on top and uses those same APIs as plugins.”</p></div><p id="u347a">Dave Woodhead, Head of Aladdin Studio Engineering, gives the same picture in three pillars <a href="'+U_WOODHEAD+'">on Snowflake’s Data Cloud podcast</a>: Studio “exposes everything Aladdin knows how to do as a set of APIs, events. The Aladdin data cloud built on top of Snowflake takes all of that information that’s generated through our analytics factory and inside of Aladdin and pushes that into Snowflake. And increasingly we’re building a set of developer tools.”</p><h3 id="7-aladdin-studio-in-depth--the-pieces">',
    note='s7 Woodhead three pillars')
# Exhibit 24 APIs row
rep('Named examples include the Graph API for portfolio data and risk, an Investment Research API, and the trade, order and compliance-rule APIs that the SDK plugins call TradeAPI, OrderAPI and ComplianceRuleAPI.</td>',
    'Aladdin Graph is BlackRock’s name for the API layer as a whole: every public specification is an “agraph” API, and the specs refer to naming agreed with the Aladdin Graph team. Within it, named examples include an investment research domain of five APIs (research notes, engagement, analyst coverage, watchlists and criteria) and the trade, order and compliance-rule APIs that the SDK plugins call TradeAPI, OrderAPI and ComplianceRuleAPI.</td>',
    note='ex24 Graph row')
# 54 specs + spec facts + Miller
rep('contain 58 API specifications covering 301 operations. They span trading, compliance, risk, operations, research and portfolio setup. That is the fullest public view of Aladdin’s API surface, though it is only visible by unpacking the packages.</p><p id="u350">Studio APIs can change data in the system of record, not only read it. That is why governance and permissions run through everything Studio does. Bernadette Rivosecchi, a BlackRock Managing Director, described Data Cloud’s change in one line: rather than getting files, clients now get a database ready on day one.</p>',
    'contain 54 API specifications covering 301 operations. They span trading, compliance, risk, operations, research and portfolio setup. That is the fullest public view of Aladdin’s API surface, though it is only visible by unpacking the packages.</p>'
    '<p id="u349a">The specifications also show how the surface is run:</p><ul id="u349b">'
    '<li>Of the 54 specifications, 24 are marked alpha, 6 beta, 23 stable and 1 sunset.</li>'
    '<li>Every call carries an application-key header and OAuth scopes set per resource, so access is checked twice: once for the application and once for what the user may touch.</li>'
    '<li>Thirty-five operations are flagged as long-running, the kind that return a job to poll rather than an answer.</li>'
    '<li>A linter comment in the packages warns that a change “will break all citizen developers code,” which shows that backward compatibility is enforced in code review, not only promised.</li>'
    '<li>Every public specification is tagged Access.Internal.</li>'
    '<li>The Studio resources listed in <a href="'+U_SDKREADME+'">the SDK’s own files</a> include ADX, the Aladdin Data eXchange, which does not appear among the eight pieces above.</li>'
    '</ul><p id="u350">Studio APIs can change data in the system of record, not only read it. That is why governance and permissions run through everything Studio does. Jeff Miller, a BlackRock Managing Director and Global Head of Data Platform and Product Engineering, described Data Cloud’s change <a href="'+U_MILLER+'">in a Snowflake video</a>: “We sent flat files, we sent large schema definitions, FTP and related transfers, but the Aladdin Data Cloud and Snowflake makes it much simpler for us to get our clients’ data and market data from our third-party providers and Aladdin partners back to our clients and to do so in a way that is open and integrated to their bigger data estate.”</p>',
    note='s7 54 specs, spec facts, Miller quote')
# What clients build: three benefit headings
rep('<p id="u357">BlackRock’s examples fall into three groups:</p><ul id="u358">\n<li><strong>Create and automate.</strong>',
    '<p id="u357"><a href="'+U_STUDIO+'">The Studio page</a> groups its examples under three benefit headings: “Create &amp; automate,” “Make Aladdin your own” and “Align internally &amp; externally.”</p><ul id="u358">\n<li><strong>Create &amp; automate.</strong>',
    note='s7 what clients build intro')
rep('<li><strong>Align inside and outside the firm.</strong> Preparing regulatory data',
    '<li><strong>Align internally &amp; externally.</strong> Preparing regulatory data', note='s7 third benefit bullet')
# How big it is
rep('BlackRock gives few hard numbers. Sudhir Nair, Global Head of Aladdin, <a href="https://www.citisoft.com/insights/blog/solutions-market-perspective-series-sudhir-nair-blackrock">has said more than 2,000 citizen developers</a> actively use Studio. That figure is undated, likely from around 2024, and includes BlackRock’s own staff. <a href="https://careers.blackrock.com',
    'BlackRock gives few hard numbers. The one headcount it has given is internal. Dave Woodhead, Head of Aladdin Studio Engineering, said <a href="'+U_WOODHEAD+'">on Snowflake’s Data Cloud podcast</a>: “inside of BlackRock we have 3,000 citizen developers” and business engineers “that are interacting with all that in using Python or using R. I think that number has probably peaked,” because more complex work will be done through natural language. Diwakar Goel, Global Head of Data, gave the same figure <a href="'+U_GOEL+'">on a BlackRock pensions webinar</a>: “we have 3,000 people who qualify in this bracket today.” Neither figure counts Studio clients; both describe BlackRock’s own staff. Sudhir Nair’s podcast as Global Head of Aladdin gives no citizen-developer figure. <a href="https://careers.blackrock.com',
    note='s7 how big: 3,000 citizen developers')
rep('It still shows how central API use is to BlackRock’s plan. BlackRock has not named any outside client as a Studio or Data Cloud reference.</p><h3 id="7-aladdin-studio-in-depth--how-blackrock-talks-about-studio">',
    'It still shows how central API use is to BlackRock’s plan.</p><p id="u361a">Woodhead also gives a sense of Data Cloud’s scale: “we operate hundreds of Snowflake accounts. We share data to hundreds of Snowflake accounts and we’re managing hundreds of vendors, tens of thousands of pipelines.” He dates the Data Cloud conversation to “around 2019” and says BlackRock “several years ago crossed the threshold where more of our users are consuming data programmatically through R, through Python” than through Excel.</p><p id="u361b">BlackRock has not named any outside client as building on Studio’s APIs or the SDK. The nearest public statement is Royal London’s chief executive crediting “the implementation of Snowflake that we did as part of the overall programme” <a href="'+U_RL+'">in a BlackRock client video</a>; he does not say Data Cloud or Studio.</p><h3 id="7-aladdin-studio-in-depth--how-blackrock-talks-about-studio">',
    note='s7 Woodhead scale + no named Studio builder')
# Khara major unlock after Exhibit 25
rep('Zero counts are reliable. Other counts are approximate, because transcripts can contain errors.</p></div></figure><figure class="exhibit" id="exhibit-26">',
    'Zero counts are reliable. Other counts are approximate, because transcripts can contain errors.</p></div></figure><p id="u363a">Studio is not absent from product leadership’s story, though. In <a href="'+U_KHARA+'">BlackRock’s own winner interview</a> after the 2023 Buy-Side Technology Awards, Kunal Khara, Global Head of Aladdin Product, named Studio as a focus for the year ahead: “What we call the Aladdin studio estate, we think is going to this year be a major, major unlock, because we’re finding that more users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis at machine scale, over and above what they get through our front end applications as well.”</p><figure class="exhibit" id="exhibit-26">',
    note='s7 Khara major unlock')
# Exhibit 26 citizen developer row
rep('<td class="first">Citizen developer</td>\n<td>May 2024</td>\n<td><a href="https://engineering.blackrock.com/open-sourcing-the-aladdinsdk-empower-python-developers-with-a-quantitative-edge-7f63376061e6">SDK launch blog</a>. Replaced on the 2026 Studio page by “code-curious portfolio manager.”</td>',
    '<td class="first">Citizen developer</td>\n<td>November 2023</td>\n<td>A BlackRock speaker on <a href="'+U_GIR+'">the Global Insurance Report podcast</a>: “citizen developers are what are driving these organizations today.” Used again on a March 2024 BlackRock podcast and in <a href="'+U_SDKREADME+'">the SDK README</a> (May 2024). Replaced on the 2026 Studio page by “code-curious portfolio manager.”</td>',
    note='ex26 citizen developer first use')
# Exhibit 27 rows
rep('<td>Data Cloud “is part of Studio.” Analytics once reached only through screens are becoming APIs. “Clients have been requesting more access, more openness to Aladdin content.”</td>',
    '<td>Data Cloud “is part of Studio.” Analytics once reached only through screens are becoming APIs. “Clients have been requesting more access, more openness to Aladdin content.” Also: “speed to market doesn’t necessarily imply better data. You still have to have the data governance.”</td>',
    note='ex27 Newman')
rep('<td class="first"><a href="https://www.blackrock.com/aladdin/discover/insights/behind-the-code-data-frameworks-interview">Dave Woodhead</a></td>\n<td>Head of Aladdin Studio Engineering (about July 2026)</td>\n<td>“Snowflake is central to our strategy of delivering a whole-portfolio data solution.”</td>',
    '<td class="first"><a href="'+U_WOODHEAD+'">Dave Woodhead</a></td>\n<td>Managing Director and Head of Engineering for Aladdin Studio (Snowflake Data Cloud podcast, undated; Fivetran write-up, August 2024)</td>\n<td>Studio “exposes everything Aladdin knows how to do as a set of APIs, events.” “We are very much on a journey to what we call a whole portfolio view.” On Snowflake: “So we love the partnership with Snowflake. It’s a key part of our platform, but it’s a part of a platform.”</td>',
    note='ex27 Woodhead')
rep('<td>Global Head of Solutions Engineering, Aladdin (February 2026)</td>\n<td>Clients have more choice “because there are APIs, because we’ve opened up systems over the last five years.”</td>',
    '<td>Global Head of Solutions Engineering, Aladdin (BlackRock podcast, January 2026)</td>\n<td>Clients have more choice “because there are APIs, because we’ve opened up systems over the last five years.” On agents: “There are guardrails that we can put in place. There are constraints that we can apply. There’s business logic now that we can code. We can’t replace the judgment of the trader.”</td>',
    note='ex27 Skinner')
rep('<td class="first"><a href="https://www.blackrock.com/aladdin/discover/whitepaper/the-intelligence-of-investing">Diwakar Goel</a></td>\n<td>Global Head of Aladdin Data (October 2026)</td>\n<td>“The context that today implicitly resides in people and applications must be codified” so models and agents can use it</td>\n</tr>',
    '<td class="first"><a href="'+U_GOEL+'">Diwakar Goel</a></td>\n<td>Global Head of Data, Aladdin (BlackRock pensions webinar)</td>\n<td>“Every single transaction that happens should be available and accessible to you via an event, via an API.” Data Cloud is “a data integration hub” with “15 minutes of latency.” Citizen developers’ code must go “into GitHub in the same governance level that we check code from our software engineer,” with “survivorship” when they leave.</td>\n</tr>\n<tr>\n<td class="first"><a href="'+U_PEMM+'">Pavan Pemmaraju</a></td>\n<td>Head of AI Product and Engineering (Never Done podcast, July 2026)</td>\n<td>“The data model itself is structured for agentic use cases and we’re even changing the way that we refactor the way that our products are built in order to achieve that.”</td>\n</tr>',
    note='ex27 Goel + Pemmaraju')
rep('<td>Head of Product for AI (November 2024)</td>\n<td>Described “a set of common services and capabilities that underpin all of these different copilot experiences”</td>\n</tr>',
    '<td>Head of Product for AI (Never Done podcast with Microsoft, “Humans in the loop”)</td>\n<td>“Getting to trust is going to be predominantly about transparency in the short term. So, making sure that we’ve got human in the loop on the vast majority of operations, particularly in regulated industries, is going to be really, really critical.”</td>\n</tr>\n<tr>\n<td class="first"><a href="'+U_SOMA+'">Kamya Somasundaram</a></td>\n<td>Global Head of Aladdin Partnerships and Trading Product Marketing (BlackRock podcast, December 2025)</td>\n<td>“There is a burgeoning community of individuals saying ‘I need that in the form of an API.’”</td>\n</tr>',
    note='ex27 Garson + Somasundaram')
rep('<td class="first"><a href="https://www.zenml.io/llmops-database/agentic-ai-architecture-for-investment-management-platform">Brennan Rosales and Pedro Vicente Valdez</a></td>\n<td>AI engineering leads (2025 talk)</td>\n<td>50 to 60 teams register existing Aladdin APIs as Copilot tools. They were evaluating agent-to-agent protocols.</td>',
    '<td class="first"><a href="'+U_LANG+'">Brennan Rosales and Pedro Vicente Valdez</a></td>\n<td>AI engineering lead and Principal AI Engineer (LangChain Interrupt 2025 talk)</td>\n<td>50 to 60 teams register existing Aladdin APIs as Copilot tools. They were evaluating agent-to-agent protocols. On Copilot: “build an evaluation pipeline and make sure that we are never going to give investment advice.”</td>',
    note='ex27 Rosales and Valdez')
rep('<div class="notes"><p id="m52-7-aladdin-studio-in-depth">Source: BlackRock podcasts, interviews, white papers and engineering blog; conference summary (Rosales and Valdez).<sup class="fnref" id="fr-ex27-zenml"><a href="#fn-ex27-zenml">53</a></sup></p></div></figure><div class="footnotes" id="fnb-exhibit-27" style="margin-top:305.08pt"><p><span id="fn-ex27-zenml"><b>53</b>The Rosales and Valdez points come from ZenML’s summary of their 2025 conference talk, not from a BlackRock recording or transcript.</span></p></div>',
    '<div class="notes"><p id="m52-7-aladdin-studio-in-depth">Source: BlackRock podcasts, webinars, interviews, white papers and engineering blog; Snowflake Data Cloud podcast; LangChain Interrupt 2025 talk recording. Quotations are verbatim from published transcripts or captions.</p></div></figure>',
    note='ex27 notes; drop fn53 and its block')
# Where it is heading: Skinner + plugins paragraph
rep('<p id="u385">In September 2026, Cameron Skinner, global head of solutions engineering for Aladdin, told WatersTechnology the team is spending “a lot of time thinking about” semantics, meaning how data is defined, before rolling out AI agents.<sup class="fnref" id="fr-skinner"><a href="#fn-skinner">54</a></sup> A speaker on a BlackRock podcast with Microsoft said there is no copilot without plug-ins.<sup class="fnref" id="fr-plugins"><a href="#fn-plugins">55</a></sup></p><div class="footnotes" id="fnb-u385" style="margin-top:76.66pt"><p><span id="fn-skinner"><b>54</b>From WatersTechnology’s report of September 24, 2026, not from a BlackRock source. The article is paywalled.</span><span id="fn-plugins"><b>55</b>Taken from a secondhand summary of a BlackRock podcast episode with Microsoft. It was not checked against the recording.</span></p></div>',
    '<p id="u385">How data is defined, its semantics, is the groundwork for any of this; an agent that calls an API needs the fields to mean one thing. Cameron Skinner, Global Head of Solutions Engineering for Aladdin, put the limits of agents this way <a href="'+U_SKINNER+'">on a BlackRock podcast in January 2026</a>: “There are guardrails that we can put in place. There are constraints that we can apply. There’s business logic now that we can code. We can’t replace the judgment of the trader.” On BlackRock’s own Never Done podcast, Adrian Crockett, General Manager of Microsoft Cloud for Financial Services, said: <a href="'+U_MS2+'">“There’s no copilot without plugins”</a> (Microsoft Copilot episode, part 2, November 2024).</p>',
    note='s7 heading: Skinner Jan 2026 + Crockett; drop fn54, fn55 block')
rep('<a href="https://www.blackrock.com/aladdin/discover/report/ai-in-investment-management">Its September 2026 AI adoption report</a> found that 68% of the organizations surveyed, through 303 senior decision-makers, favor core platforms plus their own builds. It advises firms to standardize the basics and spend engineering effort where it sets them apart.</p>',
    '<a href="'+U_AIREPORT+'">Its September 2026 AI adoption report</a> is based on a survey of 303 investment firms; the figure of 68% favoring core platforms plus their own builds, cited in the earlier draft, could not be verified against the report and is unconfirmed. The better-sourced numbers are in Exhibit 20A. The report advises firms to standardize the basics and spend engineering effort where it sets them apart.</p>',
    note='s7 68% unconfirmed')

# ================= 8. DEVELOPER MARKETING =================
rep('<p id="u416">BlackRock has never named a Studio reference client. Public code and hiring ads',
    '<p id="u416">BlackRock has not named a client as building on Studio’s APIs or SDK. Public code and hiring ads', note='s8 not named')
rep('<td class="first">SLC Management (Sun Life)</td>\n<td>Featured in a podcast on <a href="https://www.blackrock.com/aladdin/products/aladdin-data-cloud">BlackRock’s own Data Cloud page</a></td>\n<td>Live October 2026</td>',
    '<td class="first">SLC Management (Sun Life)</td>\n<td><a href="'+U_SLC+'">Two BlackRock podcast episodes with SLC</a> are placed on <a href="https://www.blackrock.com/aladdin/products/aladdin-data-cloud">BlackRock’s own Data Cloud page</a>, but neither episode mentions Data Cloud, Snowflake, Studio or APIs. The placement is BlackRock’s editorial choice, not client evidence.</td>\n<td>Live October 2026; placement only</td>',
    note='ex33 SLC downgraded')
rep('<div class="notes"><p>Source: GitHub; job boards and staffing firm pages; Strata FSC website.</p></div>',
    '<div class="notes"><p>Source: GitHub; job boards and staffing firm pages; Strata FSC website; BlackRock Data Cloud page and podcast transcripts.</p></div>', note='ex33 notes')
rep('<p id="u419">Client quotes from Royal London, BNP Paribas and others talk about adopting Aladdin in general, not about what they built on Studio. The proof exists inside BlackRock, through its own citizen developers, but has not been turned into outside customer evidence. That is the most fixable credibility gap.</p>',
    '<p id="u419">Client quotes from BNP Paribas and others talk about adopting Aladdin in general, not about what they built on Studio. Royal London’s chief executive goes one step further, crediting “the implementation of Snowflake that we did as part of the overall programme” <a href="'+U_RL+'">in a BlackRock client video</a>, but without naming Data Cloud or Studio or describing what was built. The proof exists inside BlackRock, through its own citizen developers, but has not been turned into outside customer evidence. BlackRock says so itself. Kunal Khara, Global Head of Aladdin Product, <a href="'+U_KHARA+'">in BlackRock’s winner interview</a>: “Ultimately, we eat our own cooking at BlackRock. We use Aladdin to manage the managed portfolios across the firm.” That is the most fixable credibility gap.</p>',
    note='s8 client quotes + Khara eat our own cooking')
rep('<p id="u422">The main event is the Aladdin Client Forum, held regionally every two years. The job description',
    '<p id="u422">The main event is the Aladdin Client Forum, held regionally; <a href="'+U_ACF+'">the 2026 forum is in New York</a> and <a href="'+U_APAC+'">an APAC forum was held in 2025</a>, but BlackRock does not publish a cadence. The job description', note='s8 Client Forum cadence')
rep('and Eli Kalish, and podcasts featuring executives such as Sudhir Nair, Lance Braunstein and Tarek Chouman rather than developers.</p>',
    'and Eli Kalish, and podcasts that mostly feature executives such as Sudhir Nair, Lance Braunstein and Tarek Chouman. Engineer-led public content does exist, and he should know it: a Snowflake Summit 2024 talk, <a href="'+U_LANG+'">the LangChain Interrupt 2025 talk</a> on Copilot’s agent design by Brennan Rosales and Pedro Vicente Valdez, <a href="'+U_WOODHEAD+'">Dave Woodhead’s Snowflake podcast</a>, and <a href="'+U_POD+'">a 2023 “Principles of Design” engineering podcast</a> with Afwa Kandawire, Global Head of Aladdin Platforms, and Sue Zheng, Tech Fellow. It is thin next to what rivals publish, but it is not absent.</p>',
    note='s8 engineer-led content')

# ================= 11. CUSTOMERS =================
rep('One gap matters here: BlackRock has not named any Studio reference client. Asking the PMs',
    'One gap matters here: BlackRock has not named any client as building on Studio’s APIs or SDK. Asking the PMs', note='s11 gap')
rep('These match Studio’s three stated benefits: create and automate, make Aladdin your own, and align inside and outside the firm.</p>',
    'These match the three benefit headings on <a href="'+U_STUDIO+'">the Studio page</a>: “Create &amp; automate,” “Make Aladdin your own” and “Align internally &amp; externally.”</p>', note='s11 three benefits')

# ================= 12. REGULATED COMPANY =================
rep('<p id="u541">One BlackRock example to point to: in March 2026, Ted Stratigos described the Aladdin Wealth Auto Commentary rollout. He said its guardrails were built with risk, legal, information security and model governance teams, and that the real impact came from adoption.</p>',
    '<p id="u541">One BlackRock example to point to: the Aladdin Wealth Auto Commentary rollout, <a href="https://www.blackrock.com/aladdin/discover/press-release/aladdin-wealth-launches-ai-enabled-commentary-tool-at-morgan-stanley">announced in October 2025</a> with Morgan Stanley as the first user. An AI feature that writes client-facing text is the kind of launch that has to satisfy risk, legal, information security and model governance reviewers before it ships, and whose impact shows up only when advisors adopt it. He should describe it in those terms, as his own reading of the launch, rather than attributing the point to a BlackRock executive.</p>',
    note='s12 Stratigos quote replaced')
# Exhibit 38 titles
rep('<td>Senior Managing Director, Global Head of Aladdin</td>\n<td>Aladdin overall</td>',
    '<td>Global Head of Aladdin</td>\n<td>Aladdin overall</td>', note='ex38 Nair title')
rep('<td>Head of Aladdin Studio Engineering</td>\n<td>Studio engineering</td>\n<td>About July 2026</td>',
    '<td>Head of Aladdin Studio Engineering (BlackRock interview and Fivetran write-up); “managing director and head of engineering for Aladdin Studio” (<a href="'+U_WOODHEAD+'">Snowflake Data Cloud podcast</a>)</td>\n<td>Studio engineering</td>\n<td>About July 2026; August 2024; podcast undated</td>', note='ex38 Woodhead titles')
rep('<td>Global Head of Aladdin Data</td>\n<td>Data, next to Data Cloud</td>',
    '<td>Global Head of Data, Aladdin</td>\n<td>Data, next to Data Cloud</td>', note='ex38 Goel title')
rep('<td>Head of AI Product and Engineering</td>\n<td>Copilot and agents</td>\n<td>October 2026</td>',
    '<td>Head of AI Product and Engineering</td>\n<td>Copilot and agents</td>\n<td>July 2026 (<a href="'+U_PEMM+'">podcast</a>); October 2026</td>', note='ex38 Pemmaraju date')
rep('<td>Global Head of Solutions Engineering, Aladdin</td>\n<td>Solutions engineering</td>\n<td>February 2026</td>',
    '<td>Global Head of Solutions Engineering, Aladdin</td>\n<td>Solutions engineering</td>\n<td>January to February 2026</td>', note='ex38 Skinner date')
rep('<td>Global Head of Aladdin Partnerships and Trading Product Marketing</td>\n<td>Product marketing; a likely peer</td>\n<td>January 2026</td>',
    '<td>Global Head of Aladdin Partnerships and Trading Product Marketing</td>\n<td>Product marketing; a likely peer</td>\n<td>December 2025 to January 2026</td>', note='ex38 Somasundaram date')
rep('<td class="first">Pia Schäfer</td>\n<td>Head of Value Engineering for Aladdin</td>\n<td>Value and ROI</td>\n<td>Undated</td>',
    '<td class="first"><a href="https://www.blackrock.com/aladdin/discover/podcast/capturing-change-alpha-podcast">Pia Schaefer</a></td>\n<td>Global Head of Value Engineering for the Aladdin Client Business</td>\n<td>Value and ROI</td>\n<td>July 2025 (BlackRock podcast)</td>', note='ex38 Schaefer')
rep('<td class="first">Ted Stratigos</td>\n<td>Global Head of Aladdin Wealth</td>\n<td>Wealth</td>\n<td>March 2026</td>',
    '<td class="first"><a href="https://www.blackrock.com/aladdin/discover/press-release/aladdin-wealth-launches-ai-enabled-commentary-tool-at-morgan-stanley">Ted Stratigos</a></td>\n<td>Global Head of Aladdin Wealth Tech</td>\n<td>Wealth</td>\n<td>October 2025 (press release)</td>', note='ex38 Stratigos')

# ================= 13. QUESTIONS =================
rep('<li>“I couldn’t find a client publicly named as a Studio user. Which clients',
    '<li>“I couldn’t find a client publicly named as building on Studio’s APIs or SDK. Which clients', note='s13 question')

# ================= 14. EXHIBIT 40 =================
rep('<td><a href="https://www.blackrock.com/corporate/investor-relations/larry-fink-annual-chairmans-letter">Larry Fink’s 2026 letter: Aladdin sits at the core of how BlackRock scales and is “the language of portfolios”; Preqin tripled Aladdin’s desktop reach</a></td>\n</tr>',
    '<td><a href="'+U_FINK+'">Larry Fink’s 2026 letter: Aladdin sits at the core of how BlackRock scales; Preqin tripled Aladdin’s desktop reach</a>. The “language of the portfolio” phrase is Dave Woodhead’s, <a href="'+U_WOODHEAD+'">on Snowflake’s podcast</a> (“a single symbology, a single language, the language of the portfolio”), and <a href="'+U_ACF+'">the Aladdin Client Forum 2026 opener</a> says “we built a common language for portfolios.” Cite those, not the letter, for the phrase.</td>\n</tr>\n<tr>\n<td class="first">Studio as a leadership priority</td>\n<td>Kunal Khara, Global Head of Aladdin Product, <a href="'+U_KHARA+'">in BlackRock’s winner interview</a> after the 2023 awards: “the Aladdin studio estate, we think is going to this year be a major, major unlock” because users want to work “on a programmatic basis at machine scale”</td>\n</tr>',
    note='ex40 Fink letter phrase + Khara priority row')
rep('<td><a href="https://www.preqin.com/about/press-release/blackrock-aladdin-expands-private-credit-solutions-on-preqin-for-greater-transparency-and-insights-across-the-asset-class">Kunal Khara, May 2026: private credit is becoming a core part of portfolios, but its data remains fragmented</a></td>',
    '<td>Private credit is becoming a core part of portfolios while its data remains fragmented; this is the author’s framing. BlackRock’s product response: <a href="'+U_PREQINPC+'">private credit analytics added in May 2026</a>, and “Preqin indices are also available today in Aladdin Explore and our Aladdin data cloud” (<a href="'+U_WHOLE+'">BlackRock webinar, September 2025</a>)</td>',
    note='ex40 private credit row')
rep('<td><a href="https://www.blackrock.com/aladdin/discover/report/ai-in-investment-management">68% of organizations favor core platforms plus their own builds, in a survey of 303 senior decision-makers (September 2026)</a></td>\n</tr>',
    '<td><a href="'+U_AIREPORT+'">AI Adoption Report 2026, a global survey of 303 investment firms (September 2026)</a>. The figure “68% favor core platforms plus their own builds” could not be verified against the report and should not be quoted until checked; treat it as unconfirmed</td>\n</tr>\n<tr>\n<td class="first">Build vs buy evidence</td>\n<td><a href="'+U_BVB+'">BlackRock’s Build vs Buy webinar poll</a>: mostly vendor 37%, hybrid 30%, actively re-evaluating 18%, mostly in-house 15%; “60 to 70%” of a tech organisation “keeping the lights on”; firms most want to stop maintaining compliance reporting (53%). See Exhibit 20A</td>\n</tr>',
    note='ex40 68% unconfirmed + build vs buy row')

# ================= 15. MOTIVATION =================
rep('Diwakar Goel’s October 2026 point that business context “must be codified” supports this, as does Cameron Skinner’s comment that the team is thinking hard about how data is defined before rolling out AI agents.</li>',
    'Two BlackRock leaders support this on the record. Pavan Pemmaraju, Head of AI Product and Engineering, <a href="'+U_PEMM+'">on the Never Done podcast in July 2026</a>: “the data model itself is structured for agentic use cases.” Diwakar Goel, Global Head of Data, <a href="'+U_GOEL+'">on a BlackRock pensions webinar</a>: “every single transaction that happens should be available and accessible to you via an event, via an API.” BlackRock’s October 2026 <a href="https://www.blackrock.com/aladdin/discover/whitepaper/the-intelligence-of-investing">white paper</a> makes the same argument in its own words, that business context must be codified for models and agents.</li>',
    note='s15 Pemmaraju + Goel')

# ================= 16. STRATEGY =================
rep('Useful facts: Rivosecchi’s line about clients getting a database ready on day one, and the goal to “reduce off-platform development risk.”',
    'Useful facts: Jeff Miller’s line that before Data Cloud BlackRock <a href="'+U_MILLER+'">“sent flat files, we sent large schema definitions, FTP and related transfers,”</a> and the goal to “reduce off-platform development risk.”', note='s16 Miller line')

# ================= 18. CLOSING =================
rep('<li>“Your own survey found 68% of firms want a core platform plus their own builds. Preqin already sells data',
    '<li>“Your Build vs Buy webinar poll put most firms in the hybrid or vendor camp, and the firms most wanted to stop maintaining compliance reporting themselves. Preqin already sells data', note='s18 closing question')

# ================= APPENDIX A =================
rep('shows $9.3 million to $15.0 million a year for a fixed income platform. They may be different contracts.</td>',
    'shows $9.3 million to $15.0 million a year for a fixed income platform. They may be different contracts. The two figures are from different sources and need reconciling before either is cited.</td>', note='appA CalPERS')
rep('<td>Reported by WatersTechnology on September 24, 2026; the article is paywalled</td>',
    '<td>Reported by WatersTechnology on September 24, 2026; the article is paywalled. The remark does not appear in any of his five BlackRock-published transcripts, so this revision states the semantics point in the author’s own voice and quotes his January 2026 podcast line on guardrails instead</td>', note='appA Skinner semantics')
rep('<td>Cameron Skinner’s September 2026 comment on semantics</td>',
    '<td>Cameron Skinner’s September 2026 comment on semantics</td>', note='appA skinner row (unchanged anchor)')
old_tail=re.search(r'(<td>Cameron Skinner’s September 2026 comment on semantics</td>\n<td>.*?</td>\n<td>WatersTechnology</td>\n</tr>\n)',s,re.S).group(1)
rep(old_tail, old_tail+'<tr id="u743a">\n<td>The “68% of 303 firms” statistic</td>\n<td>The 303-firm sample is the AI Adoption Report 2026; the 68% could not be found in that report and may come from a separate BlackRock webinar on whole-portfolio views</td>\n<td>BlackRock AI adoption report, September 2026</td>\n</tr>\n', note='appA 68% row')
rep('<li><strong>“Over 2,000 citizen developers”</strong> comes from an undated interview, likely from around 2024, and includes BlackRock’s own staff.</li>',
    '<li><strong>The 3,000 citizen developers figure</strong> is BlackRock-internal headcount, given by Dave Woodhead on Snowflake’s podcast (who adds that it “has probably peaked”) and by Diwakar Goel on a BlackRock webinar. It is not a count of Studio clients, and Sudhir Nair’s podcast gives no such figure.</li>', note='appA citizen developers')
rep('<li><strong>Revenue growth in 2025 and early 2026 includes Preqin.</strong> Organic ACV growth, 16% for 2025 and 14% to 15% in 2026, is the cleaner measure.</li>\n</ul>',
    '<li><strong>Revenue growth in 2025 and early 2026 includes Preqin.</strong> Organic ACV growth, 16% for 2025 and 14% to 15% in 2026, is the cleaner measure.</li>\n<li><strong>The risk factor count.</strong> BlackRock’s own materials give 2,000-plus private markets factors, a 3,000-factor model for Aladdin Wealth and “2500 plus” in a stress-test demo. “Over 5,000 … daily” appears only in a Fivetran write-up; say “thousands” unless citing Fivetran.</li>\n</ul>', note='appA risk factor count')
rep('<li>BlackRock has not named any outside client as a Studio or Data Cloud reference.</li>',
    '<li>BlackRock has not named any outside client as building on Studio’s APIs or the SDK. Royal London’s chief executive credits the Snowflake implementation in its programme, without naming Data Cloud or Studio.</li>', note='appA not found')
rep('<li>The fall 2026 Client Forum announcements were not public as of October 8.</li>\n</ul>',
    '<li>The fall 2026 Client Forum announcements were not public as of October 8.</li>\n<li>The cadence of the Aladdin Client Forum is not published; the 2026 forum is in New York and an APAC forum was held in 2025.</li>\n</ul>', note='appA forum cadence')
rep('BNP Paribas’s count is 57 in one interview and more than 60 in another.</li>',
    'BNP Paribas’s count is 57 in one interview and more than 60 in another; BlackRock’s own podcast with BNP’s chief technology officer says “more than 60,” for the whole 2016 to 2020 programme.</li>', note='appA BNP')

# ================= APPENDIX B =================
rep('<li><a href="https://www.blackrock.com/aladdin/institutions/industry-segments/banks-and-brokers">Aladdin for banks and brokers</a></li>\n</ul><h3 id="appendix-b-key-sources--blackrock-job-postings">',
    '<li><a href="https://www.blackrock.com/aladdin/institutions/industry-segments/banks-and-brokers">Aladdin for banks and brokers</a></li>\n</ul><h3 id="appendix-b-key-sources--blackrock-podcasts-webinars-and-videos">BlackRock podcasts, webinars and videos used for this revision</h3><ul>\n'
    '<li><a href="'+U_WOODHEAD+'">Snowflake Data Cloud podcast with Dave Woodhead, “From Analytics to Intelligence”</a></li>\n'
    '<li><a href="'+U_NEWMAN+'">Never Done podcast: “Data, the key ingredient” (Richard Newman with Snowflake, January 2025)</a></li>\n'
    '<li>Never Done podcast with Microsoft: <a href="'+U_MS1+'">“Humans in the loop; robots on the team”</a> (Syril Smith Garson and Adrian Crockett) and <a href="'+U_MS2+'">“Microsoft Copilot episode, part 2”</a> (November 2024)</li>\n'
    '<li><a href="'+U_PEMM+'">Never Done podcast: “Reducing time to insight” (Pavan Pemmaraju, July 2026)</a></li>\n'
    '<li>Aladdin Client Stories: <a href="'+U_BNP+'">BNP Paribas Asset Management</a> (February 2023); <a href="https://www.blackrock.com/aladdin/discover/podcast/capturing-change-alpha-podcast">“Capturing change alpha”</a> (Pia Schaefer, July 2025); <a href="'+U_SKINNER+'">“How asset managers rethink operating models”</a> (Cameron Skinner, January 2026); <a href="'+U_SOMA+'">“How data architecture shapes modern trading”</a> (Kamya Somasundaram and Aviva Investors, December 2025); <a href="'+U_GIR+'">Global Insurance Report episode</a> (November 2023); <a href="'+U_SLC+'">SLC Management episodes</a> (February 2024 and March 2026); <a href="'+U_INTESA+'">Intesa</a>, <a href="'+U_NORTH+'">Northstar</a>, <a href="'+U_TCW+'">TCW</a>, <a href="'+U_UPP+'">UPP</a> and <a href="'+U_INGKA+'">Ingka Investments</a> episodes</li>\n'
    '<li>Client-story videos: <a href="'+U_RL+'">Royal London Asset Management, “Shaping tomorrow with technology”</a> (Hans Georgeson with Tarek Chouman, November 2024); <a href="'+U_HELV+'">Helvetia</a></li>\n'
    '<li>Webinar replays: <a href="'+U_BVB+'">Build vs Buy</a>; <a href="'+U_GOEL+'">“Data as a strategic asset for pensions”</a> (Diwakar Goel with Snowflake); <a href="'+U_WHOLE+'">“Unifying the whole portfolio across public and private markets”</a> (September 2025); <a href="https://www.blackrock.com/aladdin/discover/expertise/webinars/navigating-private-markets">“Navigating private markets”</a></li>\n'
    '<li><a href="'+U_BLQ+'">Big Little Questions</a>: “Are insurers disruptive or disrupted?” (Georgette Anderson and Brett Sadler); Kunal Khara on how clients shape product development; Randy Fradin and Microsoft on the Azure migration</li>\n'
    '<li><a href="'+U_KHARA+'">WatersTechnology Buy-Side Technology Awards 2023 winner interview with Kunal Khara, published by BlackRock</a></li>\n'
    '<li><a href="'+U_ACF+'">Aladdin Client Forum 2026 opener video</a></li>\n'
    '<li><a href="'+U_LANG+'">LangChain Interrupt 2025 talk by Brennan Rosales and Pedro Vicente Valdez</a></li>\n'
    '<li><a href="'+U_MILLER+'">Snowflake video with Jeff Miller on Aladdin Data Cloud</a></li>\n'
    '<li><a href="'+U_FIVETRAN+'">Fivetran customer write-up with BlackRock, August 2024</a></li>\n'
    '<li><a href="'+U_EFRONT+'">eFront client testimonial videos</a>: APG, Allianz Capital Partners, Velliv, Mizuho, Bouwinvest, Meridiam, Brown Brothers Harriman, Alter Domus</li>\n'
    '</ul><h3 id="appendix-b-key-sources--blackrock-job-postings">',
    note='appB new podcasts/videos list')
rep('<li><a href="https://github.com/blackrock/aladdinsdk-plugin-builder">SDK plugin builder</a></li>',
    '<li><a href="https://github.com/blackrock/aladdinsdk-plugin-builder">SDK plugin builder</a> (the 11 public plugin packages hold 54 API specifications)</li>', note='appB plugin builder 54')
rep('<li><a href="https://www.zenml.io/llmops-database/agentic-ai-architecture-for-investment-management-platform">Aladdin Copilot conference talk summary (ZenML)</a></li>',
    '<li><a href="'+U_LANG+'">Aladdin Copilot talk at LangChain Interrupt 2025 (recording)</a>; <a href="https://www.zenml.io/llmops-database/agentic-ai-architecture-for-investment-management-platform">ZenML summary of the same talk</a></li>', note='appB langchain')

# ================= VERIFICATION NOTES CHAPTER =================
VN='''<section class="chapter" id="verification-notes-for-this-revision"><h2 id="u752">Verification notes for this revision</h2><p class="lede" id="u753">This revision applies a fact-check of the October 8, 2026 draft against a primary-source corpus: BlackRock’s 54 public Aladdin API specifications and the SDK README, its product pages, press releases and job postings, the Fivetran and Microsoft write-ups, and about 120 transcripts of BlackRock talks, podcasts, webinar replays and client videos. The author’s prose, structure, exhibit numbers and sourcing conventions are kept. The changes are listed below.</p><h3 id="verification-notes-for-this-revision--what-was-corrected-and-why">What was corrected and why</h3><ul id="u754">
<li><strong>API count (section 7).</strong> “58 API specifications” became 54. The 11 public plugin packages hold exactly 54 swagger files; the 301 operations stand.</li>
<li><strong>Aladdin Graph (Exhibit 24).</strong> The draft treated Graph as one API and named an “Investment Research API.” Every public specification is an “agraph” API, so Graph is the layer; investment research is a domain of five alpha APIs. The row now says so, consistent with Exhibit 28.</li>
<li><strong>Citizen developers (section 7, Exhibit 6, Appendix A).</strong> “More than 2,000,” attributed to Sudhir Nair, became 3,000, BlackRock-internal, quoted verbatim from Dave Woodhead (with his “has probably peaked” caveat) and Diwakar Goel. Nair’s podcast gives no figure.</li>
<li><strong>First use of “citizen developer” (Exhibit 26).</strong> May 2024 became November 2023, on a BlackRock podcast, with later uses in March 2024 and the SDK README.</li>
<li><strong>SLC Management (Exhibit 33).</strong> Downgraded from a featured Data Cloud reference to placement only: neither SLC episode mentions Data Cloud, Snowflake, Studio or APIs.</li>
<li><strong>“Never named a Studio reference client” (Summary, sections 7, 8, 11, 13, Appendix A).</strong> Softened to “not named a client as building on Studio’s APIs or SDK,” because Royal London’s chief executive credits the Snowflake implementation in BlackRock’s own video.</li>
<li><strong>Royal London (sections 3 and 5, Exhibit 16).</strong> The COO attribution, “largest and most complicated programme,” “over two years” and the system names were replaced with the CEO’s published remarks: on time, under budget, “multiple order management systems,” HSBC as partner, Snowflake in scope. The trade-press system names are kept, marked as such in the note.</li>
<li><strong>BNP Paribas (section 5, Exhibit 16, Appendix A).</strong> Now sourced to BlackRock’s own podcast, and the 60 applications attributed to the whole 2016 to 2020 programme (Aladdin, Salesforce, DataHub), not to Aladdin alone.</li>
<li><strong>2023 awards (Exhibit 21).</strong> Sourced to BlackRock’s own winner interview and completed: Best Overall Technology Provider, Best IBOR and Best Portfolio Analysis Tool.</li>
<li><strong>Titles (Exhibits 27 and 38).</strong> Pia Schaefer to Global Head of Value Engineering for the Aladdin Client Business; Ted Stratigos to Global Head of Aladdin Wealth Tech; Sudhir Nair to Global Head of Aladdin; Rosales and Valdez to AI engineering lead and Principal AI Engineer; Woodhead’s published titles shown.</li>
<li><strong>Three benefits (sections 7 and 11).</strong> Presented as the Studio page’s headings, “Create &amp; automate,” “Make Aladdin your own,” “Align internally &amp; externally,” rather than as a BlackRock sentence.</li>
<li><strong>“68% of 303 firms” (sections 6 and 7, Exhibit 40, section 18, Appendix A).</strong> Flagged unconfirmed: the 303 is the AI Adoption Report’s sample, the 68% was not found in it and resembles a separate webinar statistic. Replaced in the closing question with the Build vs Buy poll.</li>
<li><strong>Woodhead on Snowflake (Exhibit 27).</strong> The unsupported “central to our strategy” quote was replaced with his verbatim podcast lines.</li>
<li><strong>Risk factors (Exhibit 5, Appendix A).</strong> “More than 5,000” is now “thousands,” with the 5,000 tied to its only source, the Fivetran write-up.</li>
<li><strong>Unsupported attributed quotes removed or re-sourced.</strong> Stratigos on Auto Commentary guardrails (section 12), Skinner on semantics (sections 7 and 15), Goel “must be codified” (Exhibit 27, section 15), Khara on private credit (Exhibit 40), Garson on common copilot services (Exhibit 27) and Rivosecchi on “database ready on day one” (sections 7 and 16) were each replaced with a verbatim line from a BlackRock-published transcript, with speaker, title and source, or restated in the author’s voice without attribution. Jeff Miller’s flat-files-and-FTP line replaces Rivosecchi. “The language of portfolios” is attributed to Woodhead and the Client Forum 2026 opener, not to the Fink letter.</li>
<li><strong>Client Forum cadence and podcast content (section 8).</strong> “Every two years” removed; “executives rather than developers” qualified with the engineer-led talks and podcast that exist.</li>
<li><strong>“No copilot without plugins” (section 7).</strong> Now sourced to the recording and attributed to Microsoft’s Adrian Crockett on BlackRock’s Never Done podcast; the secondhand-summary note was dropped.</li>
<li><strong>CalPERS (Exhibit 11, Appendix A).</strong> A one-line note added that the two figures come from different sources and need reconciling. Neither figure was changed.</li>
<li><strong>Additions from the corpus.</strong> Exhibit 20A (Build vs Buy webinar poll and cost figures); the insurer scale figure in section 3; the clients featured in BlackRock-published podcasts and videos in Exhibit 8; Khara’s “major unlock” and “eat our own cooking” lines in sections 7, 8 and Exhibit 40; the specification facts in section 7 (24 alpha, 6 beta, 23 stable, 1 sunset; application-key header plus OAuth scopes; 35 long-running operations; the linter comment; Access.Internal; ADX); Woodhead’s three-pillar definition and Data Cloud scale; Pemmaraju, Somasundaram and Goel lines in Exhibit 27 and section 15; a list of the BlackRock podcasts, webinars and videos used, in Appendix B.</li>
<li><strong>Notes and numbering.</strong> Three numbered notes that pointed to secondhand summaries (the Citisoft interview, the ZenML talk summary and the podcast summary) were removed with the claims they supported, and the remaining notes were renumbered. New claims link to the BlackRock-published page or recording instead.</li>
</ul><h3 id="verification-notes-for-this-revision--what-this-revision-could-not-check">What this revision could not check</h3><p id="u755">The pricing, contract, named-deal, competitor-financial and regulatory figures in this guide, including all of section 4 and Exhibits 10 to 13, the named decisions in Exhibits 9, 16 and 19, the competitor figures in Exhibits 18, 21 and 22, the SDK repository statistics in Exhibit 32, the job-posting details in Exhibit 28, the financial and partnership facts in Exhibit 40, and the fund-finance and regulatory material in Exhibit 37, were not checkable against the primary-source corpus used for this revision (BlackRock’s public API specifications, product pages, press releases, job postings and about 120 transcripts of its talks and podcasts). They rest on the author’s cited external sources, listed in Appendix B and in the numbered notes. Their sourcing is the author’s and was neither added to nor strengthened here. Several of the dated decisions sit within weeks of the draft date and rest entirely on press releases; the author should be ready to name the public record behind each figure if challenged.</p></section>'''
rep('</ul></div></section><section class="fullpage back">', '</ul></div></section>'+VN+'<section class="fullpage back">', note='verification notes chapter')

# ================= FOOTNOTE BLOCK MOVES (layout after the content changes) =================
def take_block(bid):
    global s
    m=re.search(r'<div class="footnotes" id="%s" style="margin-top:[\d.]+pt">.*?</div>'%re.escape(bid),s,re.S)
    assert m, bid
    blk=m.group(0); s=s[:m.start()]+s[m.end():]
    return blk
# fnb-u106: join the cut Exhibit 8 table and put the block after the 'Named clients' paragraph
blk=take_block('fnb-u106')
rep('<figure class="exhibit" id="exhibit-8"><p class="ex-title" id="u102">', blk+'<figure class="exhibit" id="exhibit-8"><p class="ex-title" id="u102">', note='move fnb-u106 before Exhibit 8')
m=re.search(r'(<td>Deutsche Bank filings</td>\n</tr>)\n+</tbody>\n</table><table><thead>\n<tr>\n<th>Client</th>\n<th>What it uses</th>\n<th class="col-date">When</th>\n<th>Evidence</th>\n</tr>\n</thead><tbody>(<tr id="u107">)',s)
assert m, 'ex8 join'
rep(m.group(0), m.group(1)+'\n'+m.group(2), note='join Exhibit 8 asset manager table')
rep('<p class="ex-sub" id="u103">Asset managers</p><table class="pre-fn">', '<p class="ex-sub" id="u103">Asset managers</p><table>', note='ex8 table class')
# fnb-u159: after the banks table, before the new featured-clients sub-table
blk=take_block('fnb-u159')
rep('</table><p class="ex-sub" id="u157a">', '</table>'+blk+'<p class="ex-sub" id="u157a">', note='move fnb-u159 before featured sub-table')
# fnb-u338: cut Exhibit 22 before its BlackRock row
blk=take_block('fnb-u338')
m=re.search(r'(<tr id="u332">.*?</tr>\n)(<tr id="u333">)',s,re.S)
assert m, 'ex22 cut'
rep(m.group(0), m.group(1)+'</tbody>\n</table>'+blk+'<table><thead>\n<tr>\n<th>Rival</th>\n<th>Recent move</th>\n</tr>\n</thead><tbody>'+m.group(2), note='move fnb-u338 into Exhibit 22 cut')
rep('<span class="ex-num">Exhibit 22.</span> Rivals now sell some version of “build on our data with AI”</p><table>',
    '<span class="ex-num">Exhibit 22.</span> Rivals now sell some version of “build on our data with AI”</p><table class="pre-fn">', note='ex22 pre-fn class')
# fnb-u422: after paragraph u420, before the Community h3
blk=take_block('fnb-u422')
rep('<h3 id="8-studio-s-developer-marketing-and-adoption--community-events-and-content">', blk+'<h3 id="8-studio-s-developer-marketing-and-adoption--community-events-and-content">', note='move fnb-u422 before Community h3')
# hidden nav: drop anchors to removed blocks
rep('<a href="#fnb-exhibit-27">.</a>','', note='nav: drop fnb-exhibit-27')
rep('<a href="#fnb-u385">.</a>','', note='nav: drop fnb-u385')
# fnb-u125: after the asset managers table, before the Insurers sub-table
blk=take_block('fnb-u125')
rep('</tr></tbody></table><p class="ex-sub" id="u120">Insurers</p>', '</tr></tbody></table>'+blk+'<p class="ex-sub" id="u120">Insurers</p>', note='move fnb-u125 before Insurers sub-table')
# fnb-u377: cut Exhibit 26 after the Citizen developer row
blk=take_block('fnb-u377')
m=re.search(r'(<tr id="u371">.*?</tr>\n)(<tr id="u372">)',s,re.S)
assert m, 'ex26 cut'
rep(m.group(0), m.group(1)+'</tbody>\n</table>'+blk+'<table><thead>\n<tr>\n<th>Term</th>\n<th>First seen</th>\n<th>Where</th>\n</tr>\n</thead><tbody>'+m.group(2), note='move fnb-u377 into Exhibit 26 cut')
rep('<span class="ex-num">Exhibit 26.</span> When key terms first appeared in BlackRock’s materials</p><table>',
    '<span class="ex-num">Exhibit 26.</span> When key terms first appeared in BlackRock’s materials</p><table class="pre-fn">', note='ex26 pre-fn class')

# fnb-u143: split into two blocks; notes 16-17 after the Nest row, the rest after the table
blk=take_block('fnb-u143')
m=re.match(r'(<div class="footnotes" id="fnb-u143" style="margin-top:)[\d.]+(pt"><p>)(<span id="fn-ex8-gpif">.*?</span><span id="fn-ex8-btc">.*?</span>)(<span id="fn-ex8-omers">.*?</span><span id="fn-ex8-aware">.*?</span><span id="fn-ex8-ausuper">.*?</span>)(</p></div>)$',blk,re.S)
assert m, 'split u143'
blkA='<div class="footnotes" id="fnb-u139" style="margin-top:0pt"><p>'+m.group(3)+'</p></div>'
blkB='<div class="footnotes" id="fnb-u143" style="margin-top:0pt"><p>'+m.group(4)+'</p></div>'
m2=re.search(r'(<tr id="u139">.*?</tr>\n)(<tr id="u140">)',s,re.S)
assert m2, 'ex8 pensions cut'
rep(m2.group(0), m2.group(1)+'</tbody>\n</table>'+blkA+'<table><thead>\n<tr>\n<th>Client</th>\n<th>What it uses</th>\n<th class="col-date">When</th>\n<th>Evidence</th>\n</tr>\n</thead><tbody>'+m2.group(2), note='split fnb-u143: first part after Nest row')
# the remaining pensions notes join the block after the banks table (which now shares page 15)
m3=re.search(r'(<div class="footnotes" id="fnb-u159" style="margin-top:[\d.]+pt"><p>)',s)
assert m3, 'fnb-u159 block'
rep(m3.group(1), m3.group(1)+m.group(4), note='merge pensions notes 18-20 into fnb-u159')
rep('<a href="#fnb-u143">.</a>','', note='nav: drop fnb-u143')
rep('<figure class="exhibit keep" id="exhibit-27">','<figure class="exhibit" id="exhibit-27">', note='ex27: let the longer table flow across pages')
rep('<p class="ex-sub" id="u126">Pensions and other asset owners</p><table>', '<p class="ex-sub" id="u126">Pensions and other asset owners</p><table class="pre-fn">', note='ex8 pensions pre-fn')
# fnb-u394: its marker is at the end of chapter 7; park the block after chapter 8's lede, before the first h3
blk=take_block('fnb-u394')
rep('<h3 id="8-studio-s-developer-marketing-and-adoption--what-is-public-and-what-is-gated">', blk+'<h3 id="8-studio-s-developer-marketing-and-adoption--what-is-public-and-what-is-gated">', note='move fnb-u394 after chapter 8 lede')
