# Citation ledger: CUTS24 second pass

One row per affected superscript, in document order. The first column gives the v23 source number and title, then the number it has now (after renumbering). Source-line entries under exhibits are included. Superscripts in unchanged sentences are not listed.

Checks after the pass: mech.py shows first-citation order ok, no uncited register entries, sequential IDs and a sorted register. Every superscript in the body was then printed with the 110 characters before it (scratchpad/cuts24work/ctx_final.txt) and read against this ledger.

| v23 source number and title | Action | Exact words it now sits on (or "fact cut") | Why |
|---|---|---|---|
| **Executive summary (p2)** | | | |
| 1 Woodhead, Snowflake podcast (now 1) | kept in place | "Studio is Aladdin’s developer and data layer: APIs and events, Aladdin Data Cloud, and developer tools" | "on Snowflake" cut. Woodhead names all three parts. |
| 6 asdk_plugin specifications (now 6) | moved | "Posting an order runs a compliance check by default" | The off-switch sentence it sat on is cut. The specifications show runCompliance on by default. |
| 7 SimCorp, Introducing Agent Launchpad (now 65) | removed (fact cut) | fact cut | SimCorp dropped from the p2 rivals list. Still cited in Exhibit 11, Part 3 and Exhibit 16. |
| 9 Rosales and Valdez, LangChain talk (now 9) | kept in place | "No public source shows Copilot posting orders" | Registry-rules sentence before it cut. It had no superscript of its own. |
| **Part 1 text (p3)** | | | |
| 9 Rosales and Valdez (now 9) | kept in place | "It maintains “around 100 Aladdin front-end applications”" | Headcount quote before it cut. |
| 13 BlackRock private markets press release (now 13) | kept in place | "BlackRock sells Aladdin as four platforms: the Aladdin platform, eFront, Aladdin Wealth and Preqin" | "that share one data language" cut and two sentences merged. The release names the four platforms. |
| **Exhibit 1** | | | |
| 17 Aladdin Wealth AI commentary tool release | removed (fact cut) | fact cut | AI commentary tool clause cut. No other use. Register entry removed. |
| 17 (source line entry "Aladdin Wealth commentary tool release, October 2025") | removed (fact cut) | fact cut | Source-line entry removed with the fact. |
| 19 Preqin private credit release | removed (fact cut) | fact cut | Private credit analytics clause cut. Its p8 use was cut too. Register entry removed. |
| 19 (source line entry "Preqin private credit release, May 2026") | removed (fact cut) | fact cut | Source-line entry removed. |
| 21 BlackRock AWS release | removed (fact cut) | fact cut | "sold as an add-on to Aladdin Enterprise" cut. No other use. Register entry removed. |
| 21 (source line entry "BlackRock AWS release, December 2025") | removed (fact cut) | fact cut | Source-line entry removed. |
| 23 Aladdin Copilot product page (now 20) | moved | "A chat assistant available to all Aladdin clients" | "It gives no investment advice" cut. The same page backs "available to all Aladdin clients" (that phrase links to it). |
| 25 iShares V plc prospectus (now 22) | moved | "Gives custodians and administrators access to Aladdin" | "These providers pay BlackRock for it" cut. The citation check (citecheck/cb03.json) shows the prospectus was the only support for the whole cell, so it stays on the surviving words. Kept in the source line and the register. |
| 23 Aladdin Copilot product page (Exhibit 1 note) | removed (fact cut) | the "four platforms and nine solutions" fact now cites 14 | Additional item 7: the Copilot page is the wrong source for the platforms and solutions list. |
| 14 Aladdin Studio product page (now 14) | added | "BlackRock lists nine solutions" | Additional item 7: the Studio page’s site navigation lists them. The audit trimmed "four platforms and" because the p3 text states it with source 13. |
| **Exhibit 2** | | | |
| 6 and 26 (lead-in) (now 6, 23) | kept in place | "Exhibit 2 follows one trade through Aladdin as far as the 54 public specifications describe it" | Only "step by step," cut. |
| 6 (Trade detail cell) | removed (fact cut) | fact cut | "BrokerConfirmRoutingAPI holds where confirms go" cut. The cell is blank. |
| 6 (Lot detail cell) | removed (fact cut) | fact cut | "Retrieved from the ledger_a_summary table" cut. |
| 6 (NAV detail cell) | removed (fact cut) | fact cut | "Each valuation counts its exceptions. Another call lists them" cut. |
| **Exhibit 3** (only the timestamps changed) | | | |
| 9 Rosales and Valdez (now 9) | kept in place | "Rosales, for the apps and Copilot" | "at 2:35 and 4:31" cut from the link text, and &t=155s from the link address. 2:35 is not among the times register 9 lists. |
| 1 Woodhead (now 1) | kept in place | "Woodhead, for Studio" | "at 4:49" cut from the text, and &t=289s from the address. |
| 20 Data Cloud page and 33 ADX page, Exhibit 3 source line (now 18, 30) | kept in place | "BlackRock’s Studio, APIs, ATX, ADX, Data Cloud and Aladdin Risk pages" | Author: Exhibit 3 inputs. The outside-inputs row now says data is "stored with Aladdin data in Data Cloud or loaded into the Aladdin platform through the Data eXchange". Both pages were already in the source line and back the two halves. No superscript added. |
| **Exhibit 4** | | | |
| 6 specifications (source line) (now 6) | kept in place | "the 54 public specifications, for the portal link and the Admin Center" | "the ids" left the label because the agraph evidence moved to the Exhibit 5 note, which cites 6. |
| 29 AladdinSDK README (source line) (now 26) | kept in place | "the public SDK’s README, for the SDK and the other workspace items" | Label reworded for the author’s SDK emphasis. It still backs the SDK tile and the workspace items. |
| 40 aladdinsdk-plugin-builder (source line) | removed (fact cut) | fact cut | SDK-tile sentence on the plugin builder cut. Still cited in Exhibit 15 (now 79). |
| 28 Fivetran blog (source line) | removed (fact cut) | fact cut | "with Fivetran moving the data" cut. Still cited in Exhibits 2 and 13 (now 24). |
| 20 Aladdin Data Cloud product page (now 18) | added | "the Data Cloud page, for Data Cloud" (Exhibit 4 source line) | The tile still says "A managed data store on Snowflake". Fivetran was its only labelled source in this exhibit, and the Data Cloud page backs the same words in Exhibit 1. |
| **Exhibit 4, Developer guides tile (author: portal tile)** | | | |
| 30 Aladdin APIs product page (now 27) | added | "Developer guides, Jupyter notebooks, code samples, and a Data Dictionary of Aladdin field definitions, as listed on the APIs page" | Author’s portal tile text. The APIs page lists these resources. |
| 44 Aladdin developer portal (now 35) | added | "The developer portal sits behind a client login" | Author’s portal tile text. The register entry records that the address redirects to the client login. Its first citation moved earlier, so sources 35 to 40 were renumbered. |
| **Exhibit 5 and p5 text** | | | |
| 6 (Exhibit 5 source line) (now 6) | kept in place | "Source: the 54 public specifications on PyPI" | Package name and version cut. |
| 6 (long-running sentence) | removed (fact cut) | fact cut | "Ten specifications offer a way to track them, and 35 operations are marked long-running" cut. |
| 29 README (long-running sentence) | removed (fact cut) | fact cut | "SDK checks back on these operations at set intervals" cut. Still cited elsewhere. |
| 6 (bitemporal sentence) | removed (fact cut) | fact cut | Bitemporal sentences cut. |
| 6 (credential sentence) (now 6) | kept in place | "…an application key and a credential, which is an OAuth 2.0 token, a client key, or a user name and password" | Two sentences merged. One source for both. |
| 6 (scope string) (now 6) | moved | "With OAuth, access is granted per API" | The raw scope string it sat on is cut. The per-API fact had no superscript of its own and would otherwise lose its only citation. |
| 29 README (now 26) | kept in place | "The public SDK’s README says developers get their OAuth client ID and secret from Studio’s screens" | Author’s SDK emphasis. The words it backs are unchanged. |
| 1, 22, 41, 46 (speakers sentence) (now 1, 19, 38, 42) | kept in place | "Four BlackRock speakers describe Studio or its parts in recordings" | "I pulled about 125 recordings" cut. Five became four. |
| 47 Miller, Snowflake video (speakers sentence) | removed (fact cut) | fact cut | Miller row cut. No other use. Register entry removed. |
| 1 Woodhead (quote attribution) (now 1) | kept in place | "Dave Woodhead, Head of Engineering for Aladdin Studio, Snowflake Data Cloud podcast, November 2025" | Title and exact date trimmed. Both stay in Exhibit 6 and register 1. |
| **Exhibits 6 and 7 merged (new Exhibit 6)** | | | |
| 46 Khara interview (now 42) | moved | "Named “the Aladdin studio estate” a 2024 focus. “More users are craving this ability … on a programmatic basis”" | The Exhibit 6 Recording-column copy and the Exhibit 7 quote copy became one superscript at the end of Khara’s cell. It backs both statements. |
| 22 Newman podcast (now 19) | moved | "“Aladdin data cloud specifically comes in, which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella”" | The two copies (Exhibit 6 and 7) became one after the quotes. |
| 41 Goel webinar (now 38) | moved | "“Every single transaction ... via an event, via an API”; “a near real time data store”" | The two copies merged. The latency quote and the third fragment were cut. |
| 1 Woodhead (now 1) | moved | "“It exposes everything Aladdin knows how to do … developer tools”" | The two copies merged. |
| 47 Miller (Exhibit 6 row) | removed (fact cut) | fact cut | Row cut. |
| 1, 22, 41, 46 (Exhibit 7 source line) (now 1, 19, 38, 42) | kept in place | "Source: the four recordings cited" | Became the merged exhibit’s source line. |
| **p6 paragraph** | | | |
| 22 Newman | removed (fact cut) | fact cut | Per-speaker sentence cut. The fact stays in Exhibit 6 with 22. |
| 41 Goel | removed (fact cut) | fact cut | Per-speaker sentences cut. The fact stays in Exhibit 6 with 41. |
| 46 Khara | removed (fact cut) | fact cut | Per-speaker sentence cut. The fact stays in Exhibit 6 with 46. |
| 1 and 48 (now 1, 43) | kept in place | "Only Woodhead lists all three parts in one definition" / "calls Studio Developer “Aladdin’s extensibility layer”" | The sentences after them were cut. |
| **Finding 1 (p7 text, Exhibits 8 and 9)** | | | |
| 50 Royal London client video (now 45) | kept in place | "…then chief executive of Royal London Asset Management, praises the Snowflake implementation in Royal London’s Aladdin program" | The title sentence merged in. The video gives his title. |
| 51, 52 JPMorgan proxies (now 46, 47) | kept in place | "…report payments to BlackRock for Aladdin in every year since 2017, reaching $25.6 million in 2025" | Year-by-year figures cut. The proxies give every year and the 2025 figure. |
| 53 Janus Henderson 10-K (now 48) | kept in place | "…says the firm chose in 2025 to move its investment management system to Aladdin" | Quarter and quote cut. |
| 51, 52 and 54 (Exhibit 8 note) (now 46, 47, 49) | kept in place | "…proxy statements (DEF 14A) filed 2017 to 2026" / "…JPMorgan was connecting to Aladdin for its custody clients" | The grey-bar, ownership and "not a JPMorgan document" sentences were cut. They had no superscripts. |
| 38, 56, 57 (now 36, 51, 52) | kept in place | "A BlackRock Aladdin Studio engineer accepted both into the SDK" | "who co-wrote the SDK’s launch post" cut. 38 (Naik and Kalish) gives the engineer’s Aladdin Studio role. 56 and 57 show the merges. The links on "rewrites web addresses" and "adds custom headers" went with that cut sentence. |
| 58 PPF award notice (now 53) | kept in place | "BlackRock won both parts of the tender" | Price and estimate cut. |
| 59 PPF contract notice (cell) | removed (fact cut) | fact cut | The fund’s estimate is cut. No other use. Register entry removed. |
| 59 (Exhibit 9 source line) | removed (fact cut) | fact cut | Removed from "UK Find a Tender". |
| 58 (note, supplier web address) | removed (fact cut) | fact moved into register entry 58 | The note sentence is cut. Its fact now sits in the register entry, as the audit asked. |
| 62, 63 PBGC awards (now 56, 57) | kept in place | "BlackRock won an investment risk system contract both times" | "at the same yearly price" cut. |
| **Finding 2 (p8)** | | | |
| 11 2025 Investor Day (now 11) | kept in place | "At its 2025 Investor Day, BlackRock estimated that API calls across BlackRock and Aladdin would grow 17x by 2030" | Topic sentence and "four volume estimates" cut. Slide 23. |
| 12 BlackRock 10-K FY2025 (now 12) | moved | "BlackRock also tells investors it is “empowering clients with data and APIs”" | Moved from direction box 2 into the body with its quote. Checked in audit/D/blk10k.txt. The audit’s draft gave 11, which is wrong for this quote. |
| 11 2025 Investor Day (now 11) | kept in place | "…and lists “Aladdin as a platform” among Aladdin’s growth drivers" | "Another slide lists" became part of the merged sentence. Slide 35. |
| 12 10-K (now 12) | kept in place | "It does not list API calls among its fee terms" | The fee-list sentence before it was cut. The 10-K fee sentence before that has no superscript of its own and is covered by this one in the same paragraph, as in v24. |
| 65 2023 Investor Day (Exhibit 10 Studio cell) | removed (fact cut) | fact cut | Cell trimmed to "Never". The same fact is cited in the body (now 59). |
| 66, 67 earnings calls (now 61, 62) | kept in place | "Q3 2022" / "Q4 2024" | Trailing clause cut. |
| 70 private-markets webinar (two superscripts) | removed (fact cut) | fact cut | Whole private-markets paragraph cut. No other use. Register entry removed. |
| 12 10-K (HPS sentence) | removed (fact cut) | fact cut | Paragraph cut. |
| 19 Preqin credit release (p8) | removed (fact cut) | fact cut | Paragraph cut. |
| 22 Newman (p8 paragraph) | removed (fact cut) | fact cut | Paragraph cut. |
| 12 10-K (box 2) | moved | see body row above | Quote moved to the body. |
| 11 Investor Day (box 2) (now 11) | kept in place | "BlackRock could name Studio as the product behind “Aladdin as a platform”" | Box rewritten as a direction. The superscript stays on the quoted phrase. |
| 14 Studio page (box 2) | removed (fact cut) | fact cut | "Studio is the product clients use to build on Aladdin" cut. 14 is cited widely. |
| 22 Newman (box 2) | removed (fact cut) | fact cut | eFront and Preqin data sentence cut. |
| **Finding 3 (p9 text)** | | | |
| 9 (now 9) | kept in place | "It draws on a registry of about two thousand tools and agents built by Aladdin’s engineering teams" | The quote "couple of thousands agents and tools" became a plain number. The quote stays in Exhibit 10 with 9. |
| 9 (now 9) | kept in place | "A team can define a tool “mapping one-to-one to an existing Aladdin API already out in production”" | "Teams add to the registry in two ways" cut. |
| 9 (agent route) | removed (fact cut) | fact cut | "The second is to register an agent of their own" cut. |
| 6 and 39 Aladdin Graph job posting | removed (fact cut) | fact cut | "The public APIs are Aladdin Graph APIs" cut as a repeat of Exhibit 4. 39 is still in the Exhibit 4 source line (now 37). |
| 6 (now 6) | kept in place | "Some public APIs back BlackRock’s own screens, such as Risk Radar" | Clause became a sentence. |
| 9 ("Copilot’s tools map to Aladdin APIs already in production") | removed (fact cut) | fact cut | Repeat of the mapping sentence two sentences earlier, which keeps 9. |
| 1 Woodhead (now 1) | kept in place | "Woodhead describes Studio as exposing “everything Aladdin knows how to do” as APIs and events" | Additional item 4 wording. |
| 6 (now 6) | moved | "The public specifications hold 301 operations" | The combined sentence carried [6, 9] at its end. Split so each clause has its own source. |
| 9 (now 9) | moved | "Copilot draws on about two thousand tools and agents" | Same split. The inference after it ("so many of its tools likely sit on APIs clients cannot call") carries no superscript. |
| 71 Never Done, Microsoft part 2 (Crockett quote) | removed (fact cut) | fact cut | Crockett quote cut. |
| 71 Never Done, Microsoft part 2 (now 64) | moved | "…BlackRock’s Head of Product for AI said, “we are hearing that from our clients”" | Moved from the Exhibit 14 note to p9 so the quote appears once. Register 71 now lists 8:00 only. |
| 72 Reducing time to insight podcast (p9) | removed (fact cut) | fact cut | "the data model itself is structured for agentic use cases" cut on p9. Still cited in Part 3 P1 (now 74). |
| **Exhibit 11 (new Exhibit 10)** | | | |
| 9 (box 1) (now 9) | kept in place | "…The talk’s example is “what is my exposure to aerospace in Portfolio 1?”" | "the open app, portfolio and widgets" cut. |
| 9 (box 3) (now 9) | kept in place | "…a plugin registry holding “couple of thousands agents and tools”" | "from “50, 60 Aladdin engineering teams”" cut. |
| 9 (box 4) (now 9) | moved | "…leaving “say, 20 to 30 tools and agents”" | The "40, 50 tools" sentence it sat on is cut. |
| 9 (box 5, loop quote) (now 9) | moved | "as of the May 2025 talk, Copilot planned which tools to call, called them, and repeated" | GPT-4 and the loop quote cut. The talk backs the plan, call and repeat steps. |
| 9 (box 5, output guardrails) (now 9) | kept in place | "Output guardrails then check the answer for hallucinations" | Unchanged. |
| 9 (box 6, "tests every rule") | removed (fact cut) | fact cut | Sentence cut. |
| **p9 to p10 text, Exhibit 12 (new Exhibit 11)** | | | |
| 29 README (now 26) | kept in place | "According to the public SDK’s README, a licensed client’s own programs call the APIs with credentials registered in Studio" | Author’s SDK emphasis. "AI tools included" became the separate, unsourced inference "That would include a client’s own AI tools." The README says nothing about AI tools. |
| 73 Forward Deploy Engineer job posting | removed (fact cut) | fact cut | The last job-posting sentence is cut. No other use. Register entry removed. |
| 74 LSEG Q1 2026 trading update (p9) | removed (fact cut) | fact cut | Repeat cut. Still in the Exhibit 11 LSEG row (now 70). |
| 3 FactSet release (now 3) | kept in place | "FactSet has offered an MCP server for its data since December 2025" (Source column) | "and calls it the industry’s first production-grade MCP server" cut. |
| **Finding 4 (p10, p11)** | | | |
| 10 Build vs. Buy webinar (now 10) | moved | "The first poll asked where firms sit today. Exhibit 12 shows the answers" | The percentages it sat on were cut. The exhibit shows them from the same webinar. |
| 10 (now 10) | moved | "“AI and data demands” led at 42 percent" | The cut "tied for second" sentence carried it. |
| 10 (third poll) | removed (fact cut) | fact cut | Third-poll sentence cut. |
| 10 (Exhibit 13 note) (now 10) | kept in place | "Source: Build vs. Buy webinar, poll 1" | Note trimmed. The poll 3 panel was cut. |
| 10 ("backbone foundational data") | removed (fact cut) | fact cut | Sentence cut. |
| 10 (two "system of work" sentences) (now 10) | moved | "She called a “really defined system of work”, with workflows governed by operational controls, the other layer that is “almost equally important”" | Two sentences, both from source 10, merged into one. One superscript at the end covers both clauses. |
| 80 AllianceBernstein release | removed (fact cut) | fact cut | AllianceBernstein cut. No other use. Register entry removed. |
| 81 Pictet, SimCorp news (now 73) | kept in place | "Pictet chose SimCorp One in May 2026 and connects its own tools to it by API" | Shared superscript [80, 81] became [81]. |
| 82 BlackRock build vs buy insight page | removed (fact cut) | fact cut | Sentence cut. No other use. Register entry removed. |
| **Part 3 (p12 in v23, now p13)** | | | |
| 9 (P1, "It sells Aladdin as the system it runs internally") | removed (fact cut) | fact cut | Sentence cut. |
| NEW Aquata MCP page (P2) | removed (fact cut) | fact cut | Arcesium MCP detail cut from P2. Still on p2 and in Exhibit 11 (now 7). |
| 7 SimCorp (P2) (now 65) | moved | "SimCorp" in "SimCorp, Clearwater and Arcesium have announced AI agents or AI platforms" | Merged sentence. Each rival carries its own source. |
| 8 Clearwater release (P2) (now 8) | moved | "Clearwater" in the same sentence | Same. |
| 76 Arcesium AI platform and NEW ABF Journal reprint (P2) (now 67, 68) | moved | "Arcesium" in the same sentence | Same. The reprint backs the Arcesium platform. |
| 9 (P2) (now 9) | kept in place | "…Copilot runs across about 100 applications on about two thousand registered tools and agents" | Unchanged. |
| 6 (P3) (now 6) | kept in place | "…and the public order API has no call to authorize one" | The time-limit sentence was cut and the permission sentence reworded. 6 still covers the paragraph’s specification facts. |
| 29 README (P4) (now 26) | kept in place | "According to the public SDK’s README, a licensed client’s own programs call the APIs with credentials registered in Studio" | Same rewording as on p10. |
| 9 (P5) (now 9) | moved | "Copilot’s own guardrails, planning and AI-graded tests run inside Copilot" | "Its system prompts are tested daily by AI judges" cut. The first sentence had no superscript of its own. |
| 10 (P6) (now 10) | moved | "…buyers named AI and data demands as the top reason to rethink what to build and what to buy" | P6 and P7 replaced by the merged paragraph. The RFP clause and 42 percent cut. |
| 9 (P7, "hundreds of Aladdin clients in 70 countries") | removed (fact cut) | fact cut | Sentence cut (repeat of p3). |
| 12 10-K (P7, "$2.0 billion in 2025") | removed (fact cut) | fact cut | Same. |
| 11 Investor Day ($20 billion) and 11 (17x) (now 11) | moved | "BlackRock sizes Aladdin’s addressable market at more than $20 billion and projects API calls across BlackRock and Aladdin to grow 17x by 2030" | Two sentences with the same source merged. One superscript at the end covers both clauses (slides 35 and 23). |
| **Exhibit 14 (new Exhibit 13)** | | | |
| 71 (note) | moved | moved to p9, see above | Smith Garson quote now on p9. |
| 29 README (source line) (now 26) | kept in place | "the public SDK’s README" | Label reworded for the SDK emphasis. Sources 34, 20, 28 and 1 kept because the Data Cloud line stays (author’s Exhibit 14 decision). |
| **Exhibit 15 (new Exhibit 14)** | | | |
| 10 (row 2) (now 10) | kept in place | "Clients already build rebalancing tools on Aladdin’s APIs" | "Sewdass names rebalancing tools as what clients build" reworded. Sewdass said the APIs let clients build "their secret sauce rebalancing tools". |
| **Exhibit 16 (new Exhibit 15)** | | | |
| 50 Royal London video (Hear receipts) | removed (fact cut) | fact cut | Receipt cut. "client videos" left the Public cell with it. |
| 1 Woodhead (Hear receipts) | removed (fact cut) | fact cut | Receipt cut. "partner channels" left the Public cell. |
| 9 Rosales and Valdez (Hear receipts) | removed (fact cut) | fact cut | Receipt cut. "conference talks" left the Public cell. The cell now reads "Podcasts, video series and webinar replays on BlackRock’s site", which the remaining receipts (84, 85, 10) back. |
| 29 README (Try and Build receipts) (now 26) | kept in place | "SDK README" receipts beside "Per the public SDK’s README: Studio Compute (hosted Python), API credentials registered in Studio, and the client’s Aladdin address" and "which the public SDK needs for every call" | Wording trimmed and SDK emphasis added. |
| 6 and 44 developer portal (note) | removed (fact cut) | fact cut | Note sentence cut. Both are still cited in the Read and See rows, and 44 in the Exhibit 4 tile. |
| **p14 text** | | | |
| 29 README (SDK paragraph) (now 26) | moved | "The SDK is the one piece of Studio a prospect can install before any conversation" | Author’s SDK emphasis. The gateway-setting sentence it sat on is cut. The new hedge "The public version may not match the one clients use." carries no source. |
| 96 Aquata Demo Center (now 88) | kept in place | "Arcesium is the exception, with a 30-day trial of its Aquata data platform" | Sentence reworded. Same fact. |
| 89 FactSet developer portal and 98 MSCI API user guide | removed (fact cut) | fact cut | "LSEG and FactSet come next ..." cut. Both stay in the Exhibit 16 source line (now 81, 90). |

## Register entries removed (v23 numbers)
- 17 Aladdin Wealth launches AI-enabled commentary tool at Morgan Stanley
- 19 BlackRock Aladdin expands private credit solutions on Preqin
- 21 BlackRock partners with AWS to deliver Aladdin on secure, scalable cloud infrastructure
- 47 BlackRock transforms client data delivery with Snowflake’s Aladdin Data Cloud (Miller)
- 59 Contract notice 001014-2025 (PPF estimate)
- 70 Unifying the whole portfolio across public and private markets (webinar)
- 73 Job posting: Forward Deploy Engineer, Aladdin Data (R264906, Mumbai)
- 80 AllianceBernstein selects SimCorp One technology platform
- 82 Build vs buy: a decision framework (BlackRock insight page)

(83 was already removed in v24.) The register now has 96 entries.

## Register entries edited
- 58 PPF award notice: adds "The notice gives BlackRock’s Aladdin web page as the supplier web address."
- 71 Never Done, Microsoft part 2: "Quoted at 8:00 (Smith Garson)." Crockett is no longer quoted.

## Not changed, for the author to check
- Registers 9 and 10 still list the quote times of all passages quoted in v24. Some of those passages are now cut (for example the headcount quote, "40, 50 tools", "over a planning and action node", the "backbone" quote and the poll 3 result). The times cannot be matched to quotes without the transcripts, so I left the lists unchanged.
