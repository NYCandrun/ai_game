# Lost-citation check: GONE.md items against the v24 preview

Read-only check. I edited nothing. I extracted the v24 preview HTML with every superscript mapped back to its v23 register entry by exact title. I spot-checked against the PDF text (pdftotext), and the two match.

**How I matched sources.** I matched by register title. Two v24 entries were retitled but are the same document, with the same notice number or URL, so I count them as the SAME source:
- v24 53 "Contract award notice 062522-2025, order management, portfolio monitoring and risk analytics system, PPF" is v23 58 "Contract award notice 062522-2025, investment risk and analytics platform, PPF". Same notice and same URL.
- v24 58 "BlackRock earnings call transcripts, Q1 2020 to Q3 2026" is v23 64 "... Q1 2020 to Q2 2026". Same roic.ai URL, extended by one quarter.

**Not in the v24 register** (v23 numbers): 17 Wealth AI commentary release, 19 Preqin private credit release, 21 AWS release, 47 Jeff Miller Snowflake video, 59 PPF contract notice 001014-2025, 70 private markets webinar, 73 Forward Deploy Engineer posting, 80 AllianceBernstein, 82 Build vs buy insight page, 83 eFront acquisition release. Every fact that relied only on these is CUT below. No surviving fact still needs them.

Superscripts in the v24 wording column use **v24 numbers**, with the register title noted where it helps.

| # | v23 item (short) | v23 source (title) | Class | v24 wording / note |
|---|---|---|---|---|
| 1 | Studio is the developer and data layer | Woodhead, Snowflake podcast | KEPT-CITED | "Studio is Aladdin’s developer and data layer: APIs and events, Aladdin Data Cloud, and developer tools ⟦1⟧." ("on Snowflake" trimmed) |
| 2 | Data providers offer AI tools a way to read data | LSEG/Anthropic, FactSet MCP, MSCI connectors, Snowflake Cortex MCP | KEPT-CITED | "Many data providers now let outside AI tools read their data ⟦2, 3, 4, 5⟧." |
| 3 | Caller can turn compliance off (exec summary) | asdk_plugin specs | KEPT-CITED (moved) | Dropped from the exec summary. Part 3: "The caller can skip that check with the same Order:write scope it uses to post." The paragraph closes on specs ⟦6⟧. Also in the Exhibit 3 controls box ("The caller can turn it off with the scope it uses to post"), whose caption cites specs ⟦6⟧. |
| 4 | SimCorp and Clearwater announced agents (exec summary) | Agent Launchpad; CWAN 800+ agents | KEPT-CITED (moved) | Part 3: "SimCorp ⟦65⟧ , Clearwater ⟦8⟧ and Arcesium ⟦67, 68⟧ have announced AI agents or AI platforms." 65 is "Introducing Agent Launchpad". |
| 5 | Each Copilot tool matches a production API | Rosales and Valdez, LangChain | KEPT-CITED | Exec summary: "each tool maps to an Aladdin API already in production. No public source shows Copilot posting orders ⟦9⟧." Also Part 2 §3 with ⟦9⟧. |
| 6 | API calls 17x by 2030 (exec summary) | 2025 Investor Day | KEPT-CITED | "BlackRock estimated that API calls across BlackRock and Aladdin would grow 17x by 2030 ⟦11⟧." |
| 7 | Four platforms named | Private Markets Transparency release | KEPT-CITED | "BlackRock sells Aladdin as four platforms: the Aladdin platform, eFront, Aladdin Wealth and Preqin ⟦13⟧." ("share one data language" cut) |
| 8 | Wealth: advisors; AI commentary since Oct 2025 | Wealth page; Wealth AI commentary release | First half KEPT-CITED, second half CUT | "Risk analysis and proposals for advisors ⟦16⟧". The commentary tool and source 17 are gone. |
| 9 | eFront includes Preqin; private credit May 2026 | eFront Insight page; Preqin private credit release | First half KEPT-CITED, second half CUT | "A private-fund platform that now includes Preqin ⟦17⟧" (17 is the eFront Insight page). The private credit fact and source 19 are gone. |
| 10 | Data Cloud: Snowflake; add-on to Enterprise; part of Studio | Data Cloud page; AWS release; Newman | Add-on CUT, rest KEPT-CITED | "Managed data on Snowflake ⟦18⟧ , and part of Studio ⟦19⟧". The add-on claim and the AWS release are gone. |
| 11 | Copilot gives no investment advice (Exhibit 1) | Copilot page | KEPT-CITED (moved) | Exhibit 10: "One answer . The product page says Copilot “will not give investment advice” ⟦20⟧". |
| 12 | Providers pay BlackRock for Aladdin Provider | iShares V prospectus | CUT | Row now reads "Gives custodians and administrators access to Aladdin ⟦22⟧". Only the register title still mentions fees. |
| 13 | Exhibit 1 source line | product pages, AWS, Woodhead, prospectus, specs | KEPT-CITED | "Source: BlackRock product pages ⟦14, 15, 16, 17, 18, 20, 21⟧ ; Rosales and Valdez ⟦9⟧ ; Newman ⟦19⟧ ; Woodhead ⟦1⟧ ; iShares prospectus ⟦22⟧ ; the public specifications ⟦6⟧ ." The AWS release was dropped along with the add-on fact (item 10). |
| 14 | Exhibit 2 intro | specs; Aladdin Accounting episode | KEPT-CITED | "Exhibit 2 follows one trade through Aladdin as far as the 54 public specifications describe it ⟦6, 23⟧." |
| 15 | Explore what-if (step 1, Where) | Explore training recording | CUT | Step 1 Where is now "Order Monitor in Aladdin Dashboard ⟦6⟧". Explore survives only in Exhibit 3, with its own cite ⟦25⟧. |
| 16 | runCompliance on by default (step 2) | specs | KEPT-CITED | Detail cell: "runCompliance is on by default ⟦6⟧". "Runs automatically" moved to the Who cell, in the same row. |
| 17 | BrokerConfirmRoutingAPI (step 3) | specs | CUT | Step 3 Detail is now empty. |
| 18 | Positions appear only as fields in other APIs (step 4) | specs | CUT (replaced) | Now "No holdings API ⟦6⟧". The "fields in other APIs" claim is gone. |
| 19 | ledger_a_summary table (step 5) | specs | CUT | |
| 20 | Each valuation carries an exception list (step 6) | specs | CUT | |
| 21 | Exhibit 2 source line | specs, Newman, Explore recording, Accounting episode, Fivetran | KEPT-CITED | "Source: the specifications named in each step ⟦6⟧ ; Newman ⟦19⟧ ; the Aladdin Accounting episode ⟦23⟧ ; Fivetran ⟦24⟧ ." The Explore recording was dropped along with item 15. |
| 22 | Exhibit 3 source line | Rosales, Explore, Woodhead, specs, SDK, pages, release, 10-K, Microsoft, ICE, Sustainalytics | KEPT-CITED | Same line with the timestamps removed: "Rosales , for the apps and Copilot ⟦9⟧ ; a training recording, for Explore ⟦25⟧ ; Woodhead , for Studio ⟦1⟧ ; ... ⟦33, 34⟧ ." |
| 23 | Exhibit 4 source line | Studio page ... Studio for Aladdin Risk | KEPT-CITED | Kept except for three changes. "For the ids" moved to the Exhibit 5 caption ("taken from each specification’s id, which begins agraph.<domain>", Source ⟦6⟧). The plugin builder sentence was cut from the SDK box (plugin builder is still cited in Exhibit 15 ⟦79⟧). "With Fivetran moving the data" was cut from the Data Cloud box. Data Cloud page ⟦18⟧ was added. |
| 24 | Exhibit 5 source: 54 Swagger specs | specs | KEPT-CITED | "Source: the 54 public specifications on PyPI ⟦6⟧ ." |
| 25 | Ten specs track; 35 long-running ops | specs | CUT | |
| 26 | SDK checks back at set intervals | SDK README | CUT | |
| 27 | Data Cloud dataset bitemporal flag | specs | CUT | |
| 28 | Compliance rule assignments review states | specs | KEPT-CITED | "Compliance rule assignments carry a review state, such as draft, review required or approved ⟦6⟧." |
| 29 | Second credential types | specs | KEPT-CITED | "Every request carries an application key and a credential, which is an OAuth 2.0 token, a client key, or a user name and password ⟦6⟧." |
| 30 | Example scope ...Order:read | specs | CUT | Only "With OAuth, access is granted per API ⟦6⟧" remains. |
| 31 | OAuth client ID and secret from Studio screens | SDK README | KEPT-CITED | "The public SDK’s README says developers get their OAuth client ID and secret from Studio’s screens ⟦26⟧." |
| 32 | Five speakers describe Studio | Woodhead, Newman, Goel, Khara, Miller | KEPT-CITED (Miller cut) | "Four BlackRock speakers describe Studio or its parts in recordings ⟦1, 19, 38, 42⟧." |
| 33 | Woodhead quote attribution | Woodhead | KEPT-CITED | "Dave Woodhead, Head of Engineering for Aladdin Studio , Snowflake Data Cloud podcast, November 2025 ⟦1⟧" |
| 34 | Miller row, Snowflake video May 2026 | Miller Snowflake video | CUT | The row and the source are both gone. |
| 35 | Only Woodhead names every part | Woodhead | KEPT-CITED | "Only Woodhead lists all three parts in one definition ⟦1⟧." |
| 36 | Newman: Data Cloud and analytics APIs part of Studio | Newman, Never Done | KEPT-CITED (moved to Exhibit 6) | Newman row: "“Aladdin data cloud specifically comes in, which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella” ⟦19⟧" |
| 37 | Goel: near-real-time data store | Goel webinar | KEPT-CITED | Goel row: "... “a near real time data store” ⟦38⟧" |
| 38 | Khara: programmatic access | Khara awards interview | KEPT-CITED | Khara row: "“More users are craving this ability to interact with our data ... on a programmatic basis” ⟦42⟧" |
| 39 | Goel row quotes | Goel webinar | KEPT-CITED | "“Every single transaction ... via an event, via an API”; “a near real time data store” ⟦38⟧". The third quote was cut. |
| 40 | Georgeson praises Snowflake implementation | Royal London client video | KEPT-CITED | "In a BlackRock client video, Hans Georgeson, then chief executive of Royal London Asset Management, praises the Snowflake implementation in Royal London’s Aladdin program ⟦45⟧." |
| 41 | JPM payments by year | JPM proxies; JPM 2026 proxy | KEPT-CITED | "JPMorgan Chase’s proxy statements report payments to BlackRock for Aladdin in every year since 2017, reaching $25.6 million in 2025 ⟦46, 47⟧." The yearly figures (4.4, 7.6, 14.7) are now chart labels in Exhibit 7, and the caption cites ⟦46, 47⟧. |
| 42 | Janus Henderson move to Aladdin | Janus Henderson 10-K | KEPT-CITED | "Janus Henderson’s 10-K says the firm chose in 2025 to move its investment management system to Aladdin ⟦48⟧." The quote and "third quarter" were cut. |
| 43 | BlackRock engineer accepted both changes | Naik and Kalish; PR 52; PR 53 | KEPT-CITED | "A BlackRock Aladdin Studio engineer accepted both into the SDK ⟦36, 51, 52⟧." |
| 44 | PPF: won both parts, £74.0m vs £55m | PPF award 062522-2025; PPF notice 001014-2025 | KEPT-CITED (values CUT) | "BlackRock won both parts of the tender ⟦53⟧". 53 is the retitled 062522-2025. Notice 001014-2025 was dropped along with the values. |
| 45 | PBGC won both times, same yearly price | PBGC awards 2023, 2017 | KEPT-CITED | "BlackRock won an investment risk system contract both times ⟦56, 57⟧ ." "At about the same yearly price" was cut. |
| 46 | PPF notice gives Aladdin page as supplier address | PPF award 062522-2025 | KEPT-CITED (moved into the source entry) | Gone from the body. Source entry 53 now ends: "The notice gives BlackRock’s Aladdin web page as the supplier web address." |
| 47 | API calls fastest forecast growth, 17x | 2025 Investor Day | 17x KEPT-CITED, "fastest" CUT | "At its 2025 Investor Day , BlackRock estimated that API calls across BlackRock and Aladdin would grow 17x by 2030 ⟦11⟧." |
| 48 | I attribute those calls to Studio | Studio page | CUT | Replaced by "The slide ... does not say who makes them." |
| 49 | No "Studio" on 26 earnings calls | earnings call transcripts | KEPT-CITED (same source, retitled) | "No executive said “Studio” on any of the 27 earnings calls from the first quarter of 2020 to the third quarter of 2026 ⟦58⟧." |
| 50 | 10-K does not list API calls in fee terms | FY2025 10-K | KEPT-CITED | "It does not list API calls among its fee terms ⟦12⟧." |
| 51 | Only investor-facing mention: 2023 slide | 2023 Investor Day | KEPT-CITED | "Outside the calls, the only investor-facing mention I found is a single line on a 2023 Investor Day slide ⟦59⟧." |
| 52 | Data Cloud on Q3 2022 and Q4 2024 calls, add-on | Q3 2022 and Q4 2024 transcripts | KEPT-CITED (add-on gloss CUT) | "Q3 2022 ⟦60⟧ and Q4 2024 ⟦61⟧" |
| 53 | Exhibit 9 source line | earnings call transcripts | KEPT-CITED (same source, retitled) | "Source: third-party transcripts of BlackRock earnings calls , Q1 2020 to Q3 2026 ⟦58⟧ ." |
| 54 | Sept 2025 private markets webinar | Unifying the whole portfolio webinar | CUT | The whole private-markets paragraph is gone. |
| 55 | Private credit model with "colleagues from HPS" | same webinar | CUT | |
| 56 | HPS bought July 2025 | FY2025 10-K | CUT | |
| 57 | Private credit analytics on Preqin May 2026 | Preqin private credit release | CUT | |
| 58 | Newman: eFront and Preqin data into Data Cloud | Newman | CUT | |
| 59 | 17x by 2030 (finding 2 implications) | 2025 Investor Day | KEPT-CITED (moved to Part 3) | "BlackRock sizes Aladdin’s addressable market at more than $20 billion and projects API calls across BlackRock and Aladdin to grow 17x by 2030 ⟦11⟧." |
| 60 | Fastest of four forecasts | 2025 Investor Day | CUT | |
| 61 | eFront and Preqin data into Data Cloud, part of Studio | Newman | CUT | |
| 62 | "couple of thousands agents and tools" | Rosales and Valdez | KEPT-CITED | "It draws on a registry of about two thousand tools and agents built by Aladdin’s engineering teams ⟦9⟧." The quote is in Exhibit 10 with ⟦9⟧. |
| 63 | Tool maps one-to-one to production API | Rosales and Valdez | KEPT-CITED | "A team can define a tool “mapping one-to-one to an existing Aladdin API already out in production” ⟦9⟧." |
| 64 | Second way: register an agent | Rosales and Valdez | KEPT-CITED (merged) | Covered by "a registry of about two thousand tools and agents built by Aladdin’s engineering teams ⟦9⟧". The "two ways" framing is gone. |
| 65 | Studio exposes everything Aladdin knows how to do | Woodhead | KEPT-CITED | "Woodhead describes Studio as exposing “everything Aladdin knows how to do” as APIs and events ⟦1⟧." |
| 66 | Crockett: "no copilot without plug-ins" | Humans in the loop, part 2 | CUT (replaced) | Crockett's quote is gone. The same source now backs a different fact: "...BlackRock’s Head of Product for AI said, “we are hearing that from our clients” ⟦64⟧." |
| 67 | Data model structured for agentic use | Reducing time to insight (Pemmaraju) | KEPT-CITED | Part 3: "and that the data model is being structured for agentic use ⟦74⟧." |
| 68 | Exhibit 10 registry box, "50, 60 teams" | Rosales and Valdez | KEPT-CITED | "About two thousand registered tools and agents : a plugin registry holding “couple of thousands agents and tools” ⟦9⟧". The "50, 60 teams" quote was cut. |
| 69 | More than "40, 50 tools" hurts performance | Rosales and Valdez | CUT | Exhibit 10 now gives only the 20 to 30 shortlist. |
| 70 | Loop over planning and action node | Rosales and Valdez | KEPT-CITED | "as of the May 2025 talk, Copilot planned which tools to call, called them, and repeated ⟦9⟧" |
| 71 | One answer, no investment advice | Copilot page | KEPT-CITED | "One answer . The product page says Copilot “will not give investment advice” ⟦20⟧" |
| 72 | Team tests every rule in system prompts | Rosales and Valdez | KEPT-CITED (moved) | Part 3: "Copilot’s own guardrails, planning and AI-graded tests run inside Copilot ⟦9⟧." Exhibit 13: "AI models test every system prompt daily and on every change", with caption source ⟦9⟧. |
| 73 | Only MCP mention is a job posting | Forward Deploy Engineer posting | CUT | The source is gone too. |
| 74 | LSEG 90 MCP customers | LSEG Q1 2026 trading update | KEPT-CITED | Exhibit 11 LSEG row: "It had 90 customers connected to its MCP server by April 2026", with source cell "LSEG press releases ⟦2, 70⟧". |
| 75 | Arcesium press releases (Exhibit 11) | Aquata AI features; Arcesium AI platform | KEPT-CITED | "Arcesium press releases , Aquata MCP page and a reprint ⟦7, 66, 67, 68⟧" |
| 76 | Aladdin row: BlackRock job posting | Forward Deploy Engineer posting | CUT | The row now says "No published connector for outside AI tools", with source "Copilot page ⟦20⟧". |
| 77 | Aladdin has only a job posting on MCP | Forward Deploy Engineer posting | CUT | |
| 78 | Could publish how plugin model works | Rosales and Valdez; Copilot page | KEPT-CITED | "BlackRock could describe how Copilot’s tools are registered, permissioned and tested ⟦9⟧." The investment-advice clause was cut along with the Copilot page cite. |
| 79 | Poll 1 percentages | Build vs. Buy webinar | KEPT-CITED | "Exhibit 12 shows the answers ⟦10⟧". The figures 37/30/18/15 are in the chart, with source "Build vs. Buy webinar , poll 1 ⟦10⟧". |
| 80 | AI and data demands 42%; tie for second | Build vs. Buy webinar | KEPT-CITED | "“AI and data demands” led at 42 percent ⟦10⟧." The tie for second was cut. |
| 81 | Third poll, 53% compliance reporting | Build vs. Buy webinar | CUT | |
| 82 | Exhibit 12 source | Build vs. Buy webinar | KEPT-CITED | "Source: Build vs. Buy webinar , poll 1 ⟦10⟧ ." |
| 83 | "backbone foundational data" quote | Build vs. Buy webinar | CUT | |
| 84 | "really defined system of work" | Build vs. Buy webinar | KEPT-CITED | "She called a “really defined system of work”, with workflows governed by operational controls, the other layer that is “almost equally important” ⟦10⟧." |
| 85 | Integrated workflows governed by controls | Build vs. Buy webinar | KEPT-CITED (merged into 84) | Same sentence as item 84. The PM/trading/ops/compliance list and "same data" were cut. |
| 86 | AllianceBernstein in-house tech; Pictet via API | AllianceBernstein release; Pictet release | AB CUT, Pictet KEPT-CITED | "Pictet chose SimCorp One in May 2026 and connects its own tools to it by API ⟦73⟧." |
| 87 | BlackRock insight page: not binary | Build vs buy insight page | CUT | The source is gone too. |
| 88 | Sells Aladdin as the system it runs internally | Rosales and Valdez; eFront acquisition | KEPT-CITED (moved) | Exhibit 1: "the same one BlackRock runs internally ⟦9⟧". Part 1 also has the Rosales quote with ⟦9⟧. The eFront acquisition release was dropped, and ⟦9⟧ alone carries the fact. |
| 89 | SimCorp, Clearwater agents, Arcesium platform | Agent Launchpad; CWAN; Arcesium AI platform | KEPT-CITED | "SimCorp ⟦65⟧ , Clearwater ⟦8⟧ and Arcesium ⟦67, 68⟧ have announced AI agents or AI platforms." "Others will likely follow" was cut. |
| 90 | Owning team sets user groups per tool | Rosales and Valdez | KEPT-CITED (reworded) | "Copilot applies its registry rules by environment, user group and app as it picks tools ⟦9⟧." The "owning team sets" detail was dropped. |
| 91 | Caller can turn it off (Part 3) | specs | KEPT-CITED | "The caller can skip that check with the same Order:write scope it uses to post." The paragraph closes with ⟦6⟧. |
| 92 | Guardrails tested daily | Rosales and Valdez | KEPT-CITED | Part 3: "Copilot’s own guardrails, planning and AI-graded tests run inside Copilot ⟦9⟧". "Daily" survives in Exhibit 13, with caption ⟦9⟧. |
| 93 | 42% AI and data; RFPs ask about APIs | Build vs. Buy webinar | KEPT-CITED | Part 3: "At BlackRock’s webinar, buyers named AI and data demands as the top reason to rethink what to build and what to buy ⟦10⟧." The RFP half survives in the Schafer quote ("that part of the RFP has become much more prominent"), attributed with ⟦10⟧. |
| 94 | Hundreds of clients, 70 countries; $2.0bn | Rosales and Valdez; FY2025 10-K | KEPT-CITED (moved to Part 1) | "“...hundreds of clients globally across 70 countries.” ... ⟦9⟧ . BlackRock’s technology services and subscription revenue was $2.0 billion in 2025 ⟦12⟧ ." |
| 95 | Aladdin Graph posting: 200+ institutions | Aladdin Graph job posting | CUT | That posting is still cited, but only for Aladdin Graph in Exhibit 4. |
| 96 | Addressable market over $20bn | 2025 Investor Day | KEPT-CITED | Part 3 sentence quoted under item 59, with ⟦11⟧. |
| 97 | API calls 17x by 2030 (Part 3) | 2025 Investor Day | KEPT-CITED | Same Part 3 sentence, with ⟦11⟧. |
| 98 | Forward Deploy Engineer posting names MCP | Forward Deploy Engineer posting | CUT | |
| 99 | Exhibit 13 sources line | Rosales ... Fivetran | KEPT-CITED | Same list: "Sources: Rosales and Valdez ⟦9⟧ , ... the public SDK’s README ⟦26⟧ , ... Woodhead ⟦1⟧ and Fivetran ⟦24⟧ ." |
| 100 | Order can be posted as a what-if test (marketing row) | specs | KEPT-CITED | Exhibit 14 row 2: "posts it as what-if orders with compliance on. A portfolio manager authorizes them before a trader works them ⟦6⟧ ." Also Part 1 "An order can be posted as a test (the whatIf setting)... ⟦6⟧". |
| 101 | Sewdass: clients build rebalancing tools | Build vs. Buy webinar | KEPT-CITED | "Clients already build rebalancing tools on Aladdin’s APIs ⟦10⟧ ." Also "“their secret sauce rebalancing tools” on top ⟦10⟧". |
| 102 | Hear row receipts | Never Done, BLQ, client video, webinar, Woodhead, Rosales, Forum, SE posting | KEPT-CITED | "the Never Done podcast ⟦75⟧ , the Big Little Questions video series ⟦76⟧ , webinar replay ⟦10⟧ , Client Forum page ⟦77⟧ , Solutions Engineering job posting ⟦78⟧". Three receipts were dropped with their facts. The public cell no longer claims "client videos and conference talks ... and partner channels". |
| 103 | Build row receipts | SDK README; PyPI history; plugin builder | KEPT-CITED | "SDK README ⟦26⟧ , PyPI history ⟦80⟧ , plugin builder ⟦79⟧ , ..." |
| 104 | Get help row receipts | PR 52; PR 53; Studio page; APIs page | KEPT-CITED (split) | The PRs moved to the Build row with "Merged code changes from outside developers": "SDK change for enterprise gateways ⟦51⟧ , SDK change for extra HTTP headers ⟦52⟧". The Studio and APIs pages stay in Get help: "Studio page ⟦14⟧ , APIs page ⟦27⟧". "Book a meeting / brochure" was cut. |
| 105 | Could not test, portal opens only after login | specs; developer portal | KEPT-CITED (moved) | Exhibit 4: "The developer portal sits behind a client login ⟦35⟧ ." Exhibit 15 Read row: "developer portal ⟦6, 35⟧". The Part 4 intro sentence "I could not run anything, test what a client receives..." was uncited in v23 as well. |
| 106 | SDK settings for enterprise API management (Azure APIM) | SDK README | KEPT-WRONG-SOURCE (benign) | The README sentence was cut. The capability survives as "Both help firms that send Aladdin calls through their own enterprise gateway." It is backed by the PRs: "Pull request 52, URL rewriting for enterprise API gateways" and "Pull request 53" (⟦36, 51, 52⟧, next sentence) plus commit ⟦50⟧, not the README. PR 52's title supports it. |
| 107 | Exhibit 16 source line | the full platform list | KEPT-CITED | Same set of sources by title: "Source: my test of each platform’s public pages ⟦2, 4, 5, 6, 8, 14, 26, 27, 65, 66, 67, 69, 72, 81 to 96⟧ , no accounts or payments, October 8 to 20, 2026." |
| 108 | FactSet and MSCI: first call only for licensed clients | FactSet developer portal; MSCI API User Guide | KEPT-CITED (as table scores) | The sentence was cut. The fact survives as FactSet 0 and MSCI 0 under "First API call without a contract" (0 = "Not reachable without a client relationship"). The Exhibit 16 source line cites ⟦81⟧ (FactSet developer portal) and ⟦90⟧ (MSCI API User Guide). |

## Tally

- CUT in full: 28 items (15, 17, 18, 19, 20, 25, 26, 27, 30, 34, 48, 54, 55, 56, 57, 58, 60, 61, 66, 69, 73, 76, 77, 81, 83, 87, 95, 98).
- Partly cut, with the surviving part KEPT-CITED: 7 items (8, 9, 10, 44, 45, 47, 86).
- KEPT-CITED: 79 items, counting the 7 partial ones.
- KEPT-UNCITED: none.
- KEPT-WRONG-SOURCE: 1 (item 106, benign).

## KEPT-UNCITED and KEPT-WRONG-SOURCE items, with the smallest fix

**KEPT-UNCITED: none.** Every fact that survives still has a superscript to the same register source somewhere: in its own sentence, at the end of its paragraph, in the same table row, or in its exhibit's source line.

**KEPT-WRONG-SOURCE**

1. **Item 106: SDK support for enterprise API gateways.**
   - v23 said: "It has settings for firms that call ‘the Aladdin APIs via an enterprise API management platform such as Azure API Management’ ⟦SDK README⟧."
   - v24 says: "Both help firms that send Aladdin calls through their own enterprise gateway." It is cited to commit 1c1bd25 ⟦50⟧ and to PR 52 and PR 53 ⟦51, 52⟧, with Naik and Kalish ⟦36⟧ in the next sentence. The README is not cited.
   - The new sources support the claim. PR 52 is titled "URL rewriting for enterprise API gateways", and README line 633 says the same thing.
   - Smallest fix: none needed. To restore the README backing, add ⟦26⟧ after "through their own enterprise gateway".

## Minor notes (no fix required)

- **Item 46:** the PPF supplier-address fact now appears only inside source entry 53, not in the body. Put it back in the Exhibit 8 note only if a reader should see it there.
- **Item 16:** "Runs automatically" now sits in the Who cell of step 2 with no superscript. The Detail cell in the same row carries the cited fact ("runCompliance is on by default ⟦6⟧").
- **Item 3:** in the Exhibit 3 controls box and the Exhibit 13 controls box, "The caller can turn it off with the scope it uses to post" has no superscript of its own. It relies on each exhibit's source line, which cites the specs ⟦6⟧. That is consistent with how the other exhibit boxes are cited.
