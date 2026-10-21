# CUTS24 log: second pass, accepted cuts and trims

File: scratchpad/v24/preview.html (backup before this pass: scratchpad/v24/preview_after_fixes.html, left untouched). Edit script: scratchpad/cuts24work/cuts24.py. Rendered to scratchpad/v24/preview.pdf, 21 pages.

"p" is the v23 page the audit row names. "now" is the page in the new PDF. Source numbers are v23 numbers. Exhibit numbers are v23 numbers unless marked "new".

Status words: **applied**; **applied with change** (reason given); **superseded** (a v24 fix or a later author decision already replaced the target); **exception** (an author exception in CUTS24 keeps it); **KEEP** (audit verdict KEEP, left as is); **not applied** (reason given).

## out_p1_6.md (103 rows)

### Page 1 (cover)
- p1 "October 2026" in "Notes made to prepare for interviews": applied (now p1).
- p1 "What public sources show.": KEEP (N1 wording in place).
- p1 thesis line: KEEP (fix 1 wording in place).
- p1 "done with AI agents" disclosure: KEEP.

### Page 2
- p2 "Aladdin Data Cloud on Snowflake": applied. Now "Aladdin Data Cloud" (now p2).
- p2 "Many data providers now ...": KEEP.
- p2 "Access is granted per API ...": KEEP (now the fix 5 wording on OAuth scopes).
- p2 compliance off-switch and hedge: applied. Now "Posting an order runs a compliance check by default[6]."
- p2 "An AI tool calling these APIs would work under the same controls": KEEP (fix 1 wording in place).
- p2 SimCorp sentence in the rivals list: applied. Sentence cut.
- p2 registry-rules sentence ("The team that owns each tool sets ..."): applied. Sentence cut.
- p2 "Buyers of investment software say AI is changing what they build": KEEP.
- p2 17x sentence: KEEP.
- p2 "Part 3 sets out this direction ...": applied. Now "Part 3 sets out this direction, what would have to be true for it to hold, and four pieces of marketing work that would follow."
- p2 method box "inside BlackRock's 11 public Python plugin packages (named asdk_plugin)": applied. Now "its 54 public API specifications".
- p2 method box "AI agents gathered them ...": KEEP (already two sentences in v24).
- p2 method box hedges: KEEP.
- p2 "How to read the receipts" box: applied. Whole box cut. See the About row below for how the duplicate was resolved.

### Page 3
- p3 "built for itself and sells to other institutions": KEEP.
- p3 "at a LangChain conference": applied. Now "put the scale this way in 2025."
- p3 Rosales client-count quote: KEEP.
- p3 headcount quote ("around 7,000 people ..."): applied. Cut.
- p3 "around 100 Aladdin front-end applications": KEEP.
- p3 $2.0 billion revenue: KEEP.
- p3 "Its 24 percent rise includes Preqin ...": exception (fix 50 stays, with the 16 percent line).
- p3 "four platforms that share one data language": applied. Now "BlackRock sells Aladdin as four platforms: the Aladdin platform, eFront, Aladdin Wealth and Preqin[13]." The Exhibit 1 note became "BlackRock lists nine solutions[14]" (audit dependency plus additional item 7, see below).
- p3 "Exhibit 1 lists eight products ...": KEEP.
- p3 Ex 1 Aladdin "the same one BlackRock runs internally": KEEP.
- p3 Ex 1 Wealth AI commentary tool: applied. Cut, with source 17 and its source-line entry. Source 17 removed from the register.
- p3 Ex 1 eFront private credit analytics: applied. Cut, with source 19 and its source-line entry. Source 19 removed from the register (its p8 use was also cut).
- p3 Ex 1 Studio "For engineers ...": KEEP.
- p3 Ex 1 Data Cloud "sold as an add-on to Aladdin Enterprise": applied. Cut, with source 21 and its source-line entry. Source 21 removed from the register.
- p3 Ex 1 Copilot "It gives no investment advice": applied. Now "A chat assistant available to all Aladdin clients[23]".
- p3 Ex 1 Accounting public APIs: KEEP.
- p3 Ex 1 Provider "These providers pay BlackRock for it": applied with change. The sentence is cut, but source 25 stays on "Gives custodians and administrators access to Aladdin" and in the source line. The citation check (citecheck/cb03.json) shows source 25 was the only support for the whole cell, so removing it would leave that fact uncited (citation rule 3). Source 25 stays in the register.
- p3 lead-in "step by step,": applied (now p3).
- p3 Ex 2 Order detail: KEEP.
- p3 Ex 2 Trade detail BrokerConfirmRoutingAPI: applied. Cell left blank.
- p3 Ex 2 Lot detail ledger_a_summary: applied. Cell left blank.
- p3 Ex 2 NAV detail (exceptions): applied. Cell left blank (fix 19's wording is gone with it).
- p3 Ex 2 Compliance "Who": KEEP (fix 23 wording).
- p3 Ex 2 stability labels: KEEP.
- p3 Ex 2 note label list: applied. Now "The labels in brackets are stability labels. Exhibit 5 counts them."
- p3 Ex 2 note "do not say in what sequence ...": KEEP.
- p3 Ex 2 source "Explore training recording": superseded (fix 13 removed it in v24).

### Page 4
- p4 Ex 3 "Who builds" row: KEEP.
- p4 Ex 3 Explore box, note sentence and Explore source: exception (Exhibit 3 stays complete).
- p4 Ex 3 Copilot box wording: exception.
- p4 Ex 3 Hosting row and sources 12, 35: exception.
- p4 Ex 3 Outside inputs vendor-data examples and sources 36, 37: exception.
- p4 Ex 3 controls panel text: exception.
- p4 Ex 3 note "For illustrative purposes only ...": KEEP.
- p4 Ex 3 note "The 11 domains ...": KEEP.
- p4 Ex 3 source-line timestamps: applied. Now "Rosales, for the apps and Copilot[9]" and "Woodhead, for Studio[1]". The timestamps were also taken out of the two link addresses (&t=155s and &t=289s) (now p4).
- p4 Ex 4 APIs tile agraph evidence: applied. Moved to the Exhibit 5 note (now p5).
- p4 Ex 4 Events tile "Events run on the same Aladdin Graph runtime.": applied. Cut.
- p4 Ex 4 SDK tile login, retries and plugin builder: applied. The plugin builder (source 40) left the Exhibit 4 source line. Fix 20's Snowflake connection is kept. Author: SDK emphasis also applies (see below).
- p4 Ex 4 Data Cloud tile "with Fivetran moving the data": applied. Fivetran (28) left the Exhibit 4 source line. "On Snowflake" stays, so the Data Cloud page (20) was added to the source line ("the Data Cloud page, for Data Cloud"), the page Exhibit 1 already cites for "Managed data on Snowflake".
- p4 Ex 4 ADX "with standard extracts and loaders": applied.
- p4 Ex 4 Compute and ATX tiles: KEEP.
- p4 Ex 4 Developer Portal tile: KEEP, then replaced (author: portal tile, below).
- p4 Ex 4 Governance tile: KEEP.
- p4 Ex 4 workspace panel trim to one line: exception (panel stays with Spaces and the Studio Compute note). Item wording kept. The panel heading now names the public SDK's README (author: SDK emphasis).
- p4 Ex 4 Studio Compute note cut: exception (fix 58 stays). Now reads "The public SDK uses both names ..." (author: SDK emphasis).
- p4 Ex 4 source line "Additional Aladdin Studio resources": KEEP. The source line also lost "the ids" from the label for source 6.

### Page 5
- p5 Ex 5 title: applied. Now "The 54 public specifications hold 301 operations, including orders, trades and compliance rules".
- p5 Ex 5 "Largest APIs" column: KEEP.
- p5 Ex 5 source "version 2.0.0b3" and package name: applied. Now "Source: the 54 public specifications on PyPI[6]."
- p5 Ex 5 "Counts are mine": KEEP.
- p5 Ex 5 utility API list in brackets: applied.
- p5 Ex 5 stability-label note: KEEP.
- p5 Ex 5 "The 54 specifications span 11 domains and 11 PyPI packages.": applied. Cut.
- p5 Ex 5 domain-name note: applied. Now ends "which begins agraph.<domain> for Aladdin Graph."
- p5 controls sentences (whatIf, runCompliance, breaches): KEEP (now p6).
- p5 long-running sentences: applied. Cut, with sources 6 and 29 there. Note for the author: APPLY24 had left this v23 sentence as is (fix 43 not applied). CUTS24 accepts every CUT and lists no exception for it, so it is now cut.
- p5 bitemporal sentences: applied. Cut.
- p5 review-state sentence: KEEP.
- p5 "second credential" sentences: applied. Now one sentence.
- p5 "With OAuth, access is granted per API": KEEP. It now carries source 6, moved from the cut scope string.
- p5 raw scope string: applied. Cut.
- p5 "Developers get their OAuth client ID ...": KEEP. Now opens "The public SDK's README says" (author: SDK emphasis).
- p5 "I pulled about 125 recordings.": applied. Cut.
- p5 "Five BlackRock speakers ...": applied. Now "Four BlackRock speakers describe Studio or its parts in recordings[1, 22, 41, 46]."
- p5 "Exhibit 6 lists each with the title ...": applied. Now "Exhibit 6 lists them."
- p5 "on Snowflake's podcast in November 2025": applied. Cut.

### Page 6
- p6 Woodhead quote: KEEP.
- p6 Woodhead attribution: applied. Now "Dave Woodhead, Head of Engineering for Aladdin Studio, Snowflake Data Cloud podcast, November 2025[1]".
- p6 Ex 6 Miller row: applied. Cut. Source 47 removed from the register.
- p6 Ex 6 Woodhead "Gives the three-part definition": applied (absorbed into the merged exhibit, which shows his quote).
- p6 Ex 6 Goel latency quote: applied. Cut.
- p6 Ex 6 titles column: KEEP (titles kept in the merged exhibit's first column).
- p6 Ex 6 note count: applied. Now "Three of the four transcripts (Khara, Goel and Woodhead) are machine-made".
- p6 topic sentence "Khara, Newman, Goel and Woodhead ...": KEEP.
- p6 "Only Woodhead lists all three parts ...": KEEP.
- p6 per-speaker sentences (Newman, Goel, Khara): applied. Cut.
- p6 job posting "extensibility layer": KEEP.
- p6 "The role is a product director ...": applied. Cut.
- p6 conclusion sentences: KEEP.
- p6 Ex 7 as a separate exhibit: applied. Merged into Exhibit 6, titled "Four BlackRock executives describe Studio or its parts in recordings, and only Woodhead lists all three parts in one definition". Columns: speaker, title and date | what they said | parts they name. Exhibits 8 to 17 became 7 to 16 (now p7).
- p6 Ex 7 Goel third fragment: applied. Cut.
- p6 Ex 7 Khara "None by name ...": KEEP. Applied with change in the merged row: Khara's "Named 'the Aladdin studio estate' a 2024 focus" from Exhibit 6 is kept beside his quote, because it is the only place he names Studio.
- p6 Ex 7 note "Goel does not use the name Studio.": KEEP.
- p6 Ex 7 note Miller sentence: applied. Cut.

## out_p7_11.md (84 rows)

### Page 7
- p7 EDGAR search: KEEP.
- p7 Georgeson title sentence: applied. Merged into one sentence (now p8).
- p7 JPMorgan year-by-year figures: applied. Now "report payments to BlackRock for Aladdin in every year since 2017, reaching $25.6 million in 2025[51, 52]".
- p7 Janus Henderson quarter and quote: applied. Now "says the firm chose in 2025 to move its investment management system to Aladdin[53]".
- p7 Ex 8 grey 2016 bar and legend: applied. The chart now runs 2017 to 2025 with no legend. Bars respaced. aria-label updated (new Exhibit 7).
- p7 Ex 8 "The chart plots each payment in the year it was made.": KEEP.
- p7 Ex 8 grey-bar note: applied. Cut (both sentences).
- p7 Ex 8 custodian hedge: KEEP (fix 27 wording).
- p7 Ex 8 2016 trade press report: KEEP.
- p7 Ex 8 "The report is not a JPMorgan or BlackRock document.": applied. Cut.
- p7 Ex 8 "Disclosed because BlackRock owns more than 5 percent of JPMorgan": applied (also additional item 2). Cut.
- p7 "One rewrites web addresses and one adds custom headers.": applied. Cut.
- p7 "who co-wrote the SDK's launch post": applied. Now "A BlackRock Aladdin Studio engineer accepted both into the SDK[38, 56, 57]."
- p7 December 2025 SDK changes: KEEP.
- p7 Ex 9 PPF price against estimate: applied. Cut. Source 59 removed from the cell and the source line, and from the register.
- p7 Ex 9 Nest "over six other bids": KEEP.
- p7 Ex 9 PBGC "at the same yearly price": applied. Cut. "The records name BlackRock, not Aladdin" (fix 48) stays.
- p7 Ex 9 note supplier web address: applied. Moved into register entry 58. Source line now "UK Find a Tender[58, 60]; Nest[61]; USAspending.gov[62, 63]."

### Page 8
- p8 "None of this proof names Studio.": KEEP.
- p8 buyer sentence (fix 25): KEEP.
- p8 "Proof from one firm counts ...": applied. Cut.
- p8 "Some clients are easier to name ..." (now the fix 26 sentence "Firms whose filings or tenders already name BlackRock may be easier to name in public as Aladdin references."): superseded. The cut depended on moving the reason into the box. Additional item 5 sets the box to a different sentence, so the fix 26 sentence no longer repeats the box and it stays. Author's judgment flagged.
- p8 direction box 1: superseded by additional item 5. Now "A Studio case study that names the client can start with a client that builds with Studio." (now p9).
- p8 Finding 2 heading: KEEP (fix 7 wording).
- p8 topic sentence repeating the heading (v24: "BlackRock tells investors that Aladdin is growing as a platform."): applied. Cut.
- p8 "four usage measures ... fastest ... 17 times": applied. Now "At its 2025 Investor Day, BlackRock estimated that API calls across BlackRock and Aladdin would grow 17x by 2030[11]."
- p8 "I attribute those API calls to Studio": KEEP (fix 7's hedge in its place).
- p8 "Outside the calls ... 2023 Investor Day slide": KEEP.
- p8 fee list "subscriptions, client launches (go-lives) and support": applied. Last sentence now "It does not list API calls among its fee terms[12]."
- p8 Ex 10 Studio cell: applied. Now "Never".
- p8 Ex 10 Data Cloud cell: applied. Now "Q3 2022[66] and Q4 2024[67]".
- p8 Ex 10 Citizen developer row: applied. Cut.
- p8 Ex 10 API and Copilot quotes: KEEP.
- p8 Ex 10 note: applied. Now "The tally is mine. Zeros mean the term appears in no transcript. The other counts are approximate."
- p8 private-markets paragraph, opening sentence (trim): applied by the whole-paragraph cut (CUTS24: fix 7's box is in).
- p8 "BlackRock bought eFront in 2019 and Preqin in 2025.": applied (paragraph cut).
- p8 "In September 2025 its private markets team ...": applied (paragraph cut).
- p8 "15,000 fund investments": applied (paragraph cut).
- p8 transaction types and PIK: applied (paragraph cut).
- p8 HPS sentences: applied (paragraph cut).
- p8 "Private credit analytics on Preqin followed in May 2026": applied (paragraph cut).
- p8 Newman eFront and Preqin sentence (KEEP, folded into the two-sentence version): not applied as KEEP. The whole paragraph is cut per CUTS24 ("cut the p8 private-markets paragraph entirely"). Source 70 was cited only in this paragraph and is removed from the register.

### Page 9
- p9 direction box 2 (v23 wording): superseded (v24 fix 7 box replaced it).
- p9 fix 7 box: applied. The two investor quotes moved into the Finding 2 body: "BlackRock also tells investors it is "empowering clients with data and APIs"[12] and lists "Aladdin as a platform" among Aladdin's growth drivers[11]." Box now: "BlackRock could name Studio as the product behind "Aladdin as a platform"[11] when it speaks to investors." Applied with change: the "empowering" quote keeps source 12 (the 10-K, checked in audit/D/blk10k.txt), not 11 as the audit wrote.
- p9 Finding 3 heading: KEEP.
- p9 "registry of plugins ... couple of thousands": applied. Now "It draws on a registry of about two thousand tools and agents built by Aladdin's engineering teams[9]."
- p9 "Teams add to the registry in two ways ...": applied. Now "A team can define a tool "mapping one-to-one to an existing Aladdin API already out in production"[9]."
- p9 Woodhead "exposes everything" sentence: KEEP, reworded by additional item 4.
- p9 fix 33 conclusion: applied with change, per additional item 4. The four sentences are verbatim: "Woodhead describes Studio as exposing "everything Aladdin knows how to do" as APIs and events[1]. The public specifications hold 301 operations[6]. Whether Copilot's tools include the public APIs is not public. Copilot draws on about two thousand tools and agents[9], so many of its tools likely sit on APIs clients cannot call." The audit's kept sentence "Some public APIs back BlackRock's own screens, such as Risk Radar[6]." sits just before them. "The public APIs are Aladdin Graph APIs" and "Copilot's tools map to Aladdin APIs already in production" are cut as repeats.
- p9 Crockett quote: applied. Replaced by the Smith Garson quote: "On BlackRock's podcast in November 2024, asked about clients using BlackRock's plug-ins in their own copilots, BlackRock's Head of Product for AI said, "we are hearing that from our clients"[71]." The quote was removed from the Exhibit 14 note, so it appears once. This reverses APPLY24's instruction to keep Crockett on p9. Flagged for the author. Register 71 now lists only 8:00 (Smith Garson).
- p9 "On the data side ... agentic use cases": applied. Cut (source 72 stays on p12).
- p9 Ex 11 box 1 "open app, portfolio and widgets": applied. Now "One question, with the user's screen as context."
- p9 Ex 11 box 2 "50, 60 Aladdin engineering teams": applied. Cut.
- p9 Ex 11 box 3 "40, 50 tools would hurt performance": applied. Cut.
- p9 Ex 11 box 4 GPT-4 and loop quote: applied with change. Now "as of the May 2025 talk, Copilot planned which tools to call, called them, and repeated[9]. Output guardrails then check the answer for hallucinations[9]". Fix 31's heading "Plan and call the tools and agents" and its date hedge are kept. The audit's "until it can answer" was not added, because the transcript wording it would rest on is not quoted anywhere I could check.
- p9 Ex 11 box 5 "The team tests every rule in its system prompts": applied. Cut.
- p9 Ex 11 note machine-transcript sentence: applied. Cut.
- p9 Ex 11 "The tool counts are the speakers' own estimates.": KEEP.
- p9 provider counts paragraph: superseded (fix 16 already gave the 11-provider and eight-of-11 wording).
- p9 "Aladdin has published no such route.": KEEP (APPLY24 wording "BlackRock has published no guide, MCP server or AI connector for them.").
- p9 job posting sentence (v24: "The one BlackRock job posting that names MCP is for its internal data platform[73]."): applied. Cut. Source 73 removed from the register. This removes one of APPLY24's verbatim p9 sentences. Flagged.
- p9 "LSEG had 90 customers ...": applied. Cut (source 74 stays in the Exhibit 12 LSEG row).

### Page 10
- p10 Ex 12 title: KEEP.
- p10 Ex 12 FactSet "first in its market": applied to the analyst wording. Now "FactSet has offered an MCP server for its data since December 2025".
- p10 Ex 12 Clearwater "800 agents": KEEP.
- p10 Ex 12 LSEG 90 customers: KEEP.
- p10 Ex 12 Aladdin row: KEEP.
- p10 Ex 12 note job-posting sentence (v24: "BlackRock has published no MCP server or AI connector for Aladdin."): applied. Cut.
- p10 Ex 12 State Street note: KEEP.
- p10 direction box 3: KEEP.
- p10 poll 1 percentages: applied. Now "The first poll asked where firms sit today. Exhibit 12 shows the answers[10]." (new numbering).
- p10 "Cost and speed to market tied for second": applied. Cut.
- p10 third poll sentence: applied. Cut.

### Page 11
- p11 Ex 13 right panel (poll 3) and title words: applied. Panel cut. Title now "Two thirds of webinar attendees run mostly vendor or hybrid platforms" (new Exhibit 12).
- p11 Ex 13 note: applied. Now "Source: Build vs. Buy webinar, poll 1[10]. Respondents to a BlackRock webinar. Number not given."
- p11 Schafer quote: KEEP.
- p11 Sewdass title: KEEP.
- p11 "backbone foundational data ...": applied. Cut.
- p11 "secret sauce rebalancing tools": KEEP.
- p11 system of record quote: KEEP.
- p11 "system of work" sentences: applied. Now one sentence.
- p11 AllianceBernstein and Pictet: applied. Now "Pictet chose SimCorp One in May 2026 and connects its own tools to it by API[81]." Source 80 removed from the register.
- p11 August 2026 insight page: applied. Cut. Source 82 removed from the register.
- p11 direction box 4: KEEP.

## out_p12_15.md (62 rows)

### Page 12, Part 3 text
- p12 "It sells Aladdin as the system it runs internally": applied. Cut (source 83 was already gone in v24) (now p13).
- p12 speakers sentence (10, 72): KEEP.
- p12 "I have not seen BlackRock describe Studio this way.": KEEP.
- p12 rivals (fix 3): applied per the CUTS24 reconciliation. P2 now opens "SimCorp[7], Clearwater[8] and Arcesium[76, ABF reprint] have announced AI agents or AI platforms." Each name carries its own source.
- p12 "What BlackRock can show ...": KEEP (N3 wording).
- p12 Copilot registry rules: KEEP.
- p12 fix 6 time limit and "either option": applied per reconciliation. Compl Pending sentence cut. Now "Whether an Aladdin permission restricts skipping the check is not public."
- p12 "Copilot's guardrails are tested daily": applied (P5 "Its system prompts are tested daily by AI judges" cut).
- p12 "A client's AI tools would work under controls BlackRock already relies on ...": superseded (fix 1 removed it).
- p12 "How those tools would connect is not public.": superseded (fix 8 and APPLY24 P4 replaced it).
- p12 "Buyers say AI is changing ..." trim: applied (merged paragraph).
- p12 "and it gives no sample size": applied (merged paragraph).
- p12 "The client base is large ..." trim: applied (merged paragraph).
- p12 Aladdin Graph job posting sentence: superseded (fix 51 removed it).
- p12 $20 billion addressable market: KEEP (in the merged paragraph).
- p12 17x with "across BlackRock and Aladdin": KEEP (in the merged paragraph).
- p12 inference sentence: KEEP.
- p12 "How many of those institutions ...": superseded (v24 already reads "How many clients run their own AI tools is not public.").
- p12 conditions paragraph: KEEP (three conditions, per the author's N2 decision).

### Page 12, Exhibit 14 (new Exhibit 13)
- p12 Ex 14 title "not public" clause: applied with change. v24 title second sentence ("Whether Copilot's tools use the APIs clients can call is not public.") cut, as the author's Exhibit 14 decision allows. Title now "BlackRock's apps, Copilot and client code run on Aladdin's APIs". The audit's "share Aladdin's APIs and controls" was not used, because the right-hand controls are Copilot's own and stay inside Copilot.
- p12 Ex 14 app names: applied. Cut.
- p12 Ex 14 "from 50 to 60 BlackRock teams": applied. Cut.
- p12 Ex 14 "Nearest public sign: a job posting naming MCP.": superseded (v24 tile replaced it).
- p12 Ex 14 Data Cloud line in the APIs bar: not applied (author: Exhibit 14 Studio content). Kept as a Studio part, with its sources.
- p12 Ex 14 gateway: KEEP.
- p12 Ex 14 capital flows: KEEP (fix 29 wording).
- p12 Ex 14 "Any violations are returned.": KEEP (not present in the v24 compliance box wording, which APPLY24 set).
- p12 Ex 14 "(LLM judges)": applied. Now "AI models test every system prompt daily and on every change." aria-label updated.
- p12 Ex 14 note job posting: superseded (removed in v24).
- p12 Ex 14 note "Data Cloud, storage and the Data eXchange have their own access controls.": not applied (author: Exhibit 14 Studio content). It goes with the Data Cloud line, which stays.
- p12 Ex 14 note "right-hand controls": superseded (v24 already has the trimmed wording).
- p12 Ex 14 note sources 34, 20 and 28: not applied (author: Exhibit 14 Studio content). They back the Data Cloud line, which stays.

### Page 13, Exhibit 15 (new Exhibit 14)
- p13 row 1 stability labels and connectors: KEEP (fix 56).
- p13 row 1 gateway: KEEP.
- p13 row 3 examples: superseded (fix 26 wording in place).
- p13 row 4 off-switch: superseded (N5 wording in place, now row 2).
- p13 row 4 "Sewdass names rebalancing tools ...": applied (now row 2). Now "Clients already build rebalancing tools on Aladdin's APIs[10]."

### Page 13, Part 4 text
- p13 "I read everything here from outside ...": KEEP (now p14).
- p13 "from first hearing about Studio ... qualified prospects and clients": applied. Now "Exhibit 15 follows a prospect's engineer through six steps." (new numbering).
- p13 "I could read the pages ...": KEEP.
- p13 "with their notebooks and code samples": applied. Cut.
- p13 "Where this document describes the catalog ...": KEEP.

### Pages 13 and 14, Exhibit 16 (new Exhibit 15)
- p13 Hear row receipts (client story video 50, Woodhead 1, Rosales and Valdez 9): applied. Applied with change: the Public cell said "client videos and conference talks on BlackRock's site and partner channels", which those three receipts backed. To keep the cell to what the remaining receipts show, it now reads "Podcasts, video series and webinar replays on BlackRock's site" (now p15).
- p13 Read row taglines: applied. Cut.
- p14 Try row quotation: applied. Now "Per the public SDK's README: Studio Compute (hosted Python), API credentials registered in Studio, and the client's Aladdin address" (also author: SDK emphasis).
- p14 Get help and Build rows: applied. Get help public is "No public support channel." Build public ends "Merged code changes from outside developers." The receipts for the code changes (56, 57) were already in the Build row.
- p14 note "After qualification column ... login 6, 44": applied. Cut.

### Page 14, SDK paragraph, Exhibit 17 (new Exhibit 16) and text
- p14 "The SDK is the one piece of Studio a prospect can install ...": KEEP (now carries source 29).
- p14 three modes and credential manager: applied. Cut.
- p14 README gateway quotation: superseded (author: SDK emphasis). The paragraph is now two sentences: "The SDK is the one piece of Studio a prospect can install before any conversation[29]. The public version may not match the one clients use." The gateway setting is cut.
- p14 Ex 17 Community or marketplace column: KEEP.
- p14 Ex 17 Bloomberg and Clearwater hedge: KEEP.
- p14 "Exhibit 17 puts Studio beside 10 platforms ...": KEEP (fix 36 wording, now "Exhibit 16 puts ...").
- p14 list of investment platform names: applied. Now "Investment platforms score low because a first API call needs a client relationship. Arcesium is the exception, with a 30-day trial of its Aquata data platform[96]."
- p14 "Studio scores in line with them ...": KEEP.
- p14 "LSEG and FactSet come next. FactSet and MSCI ...": applied. Cut (89 and 98 stay in the source line).

### Page 15, About this document
- p15 source-type sentences: applied. Now "This is an independent analysis compiled from public sources: BlackRock's pages, filings, job postings and recordings, public code on GitHub and PyPI, and other vendors' pages and trade press." (now p17).
- p15 "BlackRock did not produce, review or endorse this analysis.": KEEP.
- p15 as-of date: KEEP.
- p15 AI agents disclosure: KEEP.
- p15 receipts paragraph ("Underlined text links ..."): not applied. The p1 to 6 audit cuts the p2 receipts box and says About keeps this text. This audit cuts this text and says to keep the p2 box, "but not both". Cutting both would leave no reading aid. I cut the p2 box and kept this paragraph, which is the alternative this audit itself names ("cut p2, but not both"). Author's judgment flagged.
- p15 trademark notice: KEEP.

## Additional items in CUTS24
1. Exhibit 1 trims and cuts: applied as written (see p3 rows). The Provider row keeps source 25 on the surviving words (citation rule 3).
2. Fix 27 "The proxies disclose the payments because BlackRock owns more than 5 percent of JPMorgan.": applied. Cut.
3. Exhibit 14 note: applied. "The hatched box marks a use no public source shows yet: a client's AI tool calling the APIs."
4. Page 9 Woodhead and fix 33: applied verbatim (see p9 rows).
5. Finding 1 direction box: applied verbatim.
6. Exhibit 17 legend: applied in the note: "Except in the AI connector column, 0 means not reachable without a client relationship." The AI connector definitions are unchanged. The colour key above the table still reads "0: Not reachable without a client relationship" and is qualified by the note.
7. Fix 40: applied. The note now cites the Studio product page (14), not the Copilot page. Wording follows the audit's p3 trim: "BlackRock lists nine solutions[14]." The four platforms are stated, with source 13, in the p3 text just above.

## Author: SDK emphasis (coordinator message)
1. p14 SDK paragraph: applied. Two sentences, source 29 on the first only: "The SDK is the one piece of Studio a prospect can install before any conversation[29]. The public version may not match the one clients use."
2. "The public SDK" wording, citations unchanged:
   - Exhibit 4 SDK tile: "Open-source Python library. The public SDK has typed clients for the APIs and a Snowflake connection for Data Cloud".
   - Exhibit 4 workspace panel heading: "Inside a client's Studio workspace, as the public SDK's README and the specifications name it".
   - Exhibit 4 note: "The public SDK uses both names ...".
   - Exhibit 4 source line: "the public SDK's README[29], for the SDK and the other workspace items".
   - Exhibit 4 aria-label: updated to match.
   - p6 controls paragraph: "The public SDK's README says developers get their OAuth client ID and secret from Studio's screens[29]."
   - p10 and p13 (Part 3 P4): "According to the public SDK's README, a licensed client's own programs call the APIs with credentials registered in Studio[29]. That would include a client's own AI tools." (this replaces "A licensed client's own programs, AI tools included, can already call ...", so the AI-tools step is marked as my inference and not attributed to the README).
   - Exhibit 13 (old 14) AI tools tile: "Can call the APIs with Studio credentials, per the public SDK's README. No published guide or connector." The two top bands and the client tiles were made taller to fit the extra line. Note adds: "The client tiles rest on the public SDK and its README, which may not match the version clients use." Source label: "the public SDK's README[29]". aria-label updated.
   - Exhibit 15 (old 16) Try row: "Per the public SDK's README: ...". Build row: "The public, open-source SDK ..." and "which the public SDK needs for every call".
3. No new SDK detail added.
4. Exhibit 3 unchanged apart from the timestamp fix. Its source label "the public specifications and SDK" was left as is.
- Not changed: Exhibit 14 (old 15) row 1 says the RFP answer would cover "how a client's own AI tools can call the APIs today". It describes planned marketing content, so I left it. Flagged.

## Author: Exhibit 14 Studio content (coordinator message)
- Kept: the "A CLIENT'S USE · THROUGH STUDIO" column, the three client tiles, Studio credentials, the gateway tile, the Data Cloud line in the APIs bar and its note caveat, and sources 34, 20, 28 and 1 in the source line.
- Cut, as the audit allows: app names, "from 50 to 60 BlackRock teams", "(LLM judges)", the title's "not public" sentence. The job-posting box and note were already gone in v24.
- The Smith Garson quote left the note (moved to p9 per the p7 to 11 audit).

## Author: portal tile (coordinator message)
- Exhibit 4 tile retitled "Developer guides and Data Dictionary". Text: "Developer guides, Jupyter notebooks, code samples, and a Data Dictionary of Aladdin field definitions, as listed on the APIs page[30]. The developer portal sits behind a client login[44]." (v23 numbers; now 27 and 35). aria-label updated. Because 44 is now first cited in this tile, sources 35 to 40 were renumbered.

## Author: Exhibit 3 inputs (coordinator message)
- Outside-inputs row now reads "The client’s own and third-party data, stored with Aladdin data in Data Cloud or loaded into the Aladdin platform through the Data eXchange, and vendor data such as prices and ESG research". The Data Cloud page (20) and the ADX page (33) were already in the Exhibit 3 source line, so nothing was added. aria-label updated. Nothing else in Exhibit 3 changed.

## Mechanics
- Register entries removed (v23 numbers): 17, 19, 21, 47, 59, 70, 73, 80, 82. Register now 96 entries (v24 had 105).
- Register entries edited: 58 (adds "The notice gives BlackRock's Aladdin web page as the supplier web address."), 71 (quote times now "8:00 (Smith Garson)" only).
- renumber.py, sortreg.py, mech.py: first-citation order ok, no uncited entries, IDs sequential, register sorted. 207 superscripts.
- Exhibits renumbered after the 6 and 7 merge: old 8 to 17 became 7 to 16. Updated the titles, figure ids, the Exhibit 3 note ("Controls as in Exhibit 13"), p10 ("Exhibit 11 lists"), p12 ("Exhibit 12 shows the answers"), p14 ("Exhibit 15 follows"), p16 ("Exhibit 16 puts"). No aria-label or cover text cites an exhibit number.
- Cover Part pages: Part 1 page 3, Part 2 page 8, Part 3 page 13, Part 4 page 14 (was 15).
- PDF: 21 pages.
