# Fix plan: Aladdin Studio from the outside (v2)

Revised after three readability reviews of the preview. Every “current” span occurs exactly once in current.html. Items are in document order. Page numbers are from the current render (the v2 preview keeps the same page numbers up to page 16; Sources run to page 20). Citations show as [n] with the current numbering; [NEW] marks a new register entry, listed once, at its first use.

Counts: 14 decisions, 88 fixes (78 FIX, 10 CITE), 3 no change. The v2 preview is 20 pages. See MERGE_NOTES.md for what changed from v1.

## Decisions for the author

### p02-09+p02-10 (page 2)

Current:
> About 100 of its applications and thousands of Copilot tools already call these APIs every day [8].

Recommended:
> About 100 of its applications carry Copilot. Each Copilot tool matches an Aladdin API already in production [8].

Alternative:
> About 100 of its applications carry Copilot. Copilot draws on about two thousand tools and agents. Each tool matches an Aladdin API already in production [8].

What it means and what else changes: This sentence carries the claim that BlackRock already runs on the APIs it offers clients. The sources say the apps carry Copilot and each Copilot tool maps to a production Aladdin API. Neither says the apps or tools call the public Studio APIs, so both options drop “these APIs” and “every day”. Recommended: the shorter sentence, which keeps page 2 the same length. Alternative: keep the tool count, which adds about one line to page 2. Under either option, page 13 (p13-06+p13-07+p13-08+p13-09) and Exhibit 14 (p13-22, p13-26, p13-27, p13-34+p13-35, p13-aria) use the same facts: about 100 applications, about two thousand tools and agents, 50 to 60 teams, each tool mapped to a production Aladdin API. The page 2 lede can stay, because it rests on the controls built into the APIs.


Why: The talk says “around 100 Aladdin front-end applications that thousands of people use every day” [1:53], Copilot “is currently embedded across all of those hundred” [2:34], and a tool maps “one-to-one to an existing Aladdin API already out in production” [4:39]. The count is “a couple thousands agents and tools that are registered” [6:42]. “Every day” in the talk describes people using the apps and the daily test runs.

### p03-16+p03-17 (page 3)

Current:
> Exhibit 1. Of Aladdin’s eight named products, Studio is the one for people who write code

Recommended:
> Exhibit 1. Of eight Aladdin products, Studio is the one for people who write code

Alternative:
> Exhibit 1. Of nine Aladdin products, Studio is the one for people who write code

What it means and what else changes: The count sits in an exhibit title. BlackRock names no set of eight. Its Aladdin site links to at least 13 products and solutions, and its boilerplate names four platforms, one of them Preqin. Recommended: “Of eight Aladdin products”, which keeps the eight rows and drops the claim that BlackRock names exactly eight. Alternative: “Of nine Aladdin products” plus a Preqin row after eFront, <tr><td class="first">Preqin</td><td>Private-markets data and analytics, bought by BlackRock in 2025<sup class="fnref"><a href="#s11">11</a></sup></td><td>Private-markets investors and fund managers</td></tr>. The alternative matches the four-part family in the new Part 1 sentence (p03-14) but adds a row to page 3. Nothing else in the document repeats “eight named products”.


Why: BlackRock’s Aladdin home page links to Accounting, Climate Risk, Aladdin Copilot, Aladdin Data Cloud, Asset Servicers, Risk Management, Aladdin Studio, Sustainability, Whole Portfolio, Aladdin, Aladdin Wealth, eFront and Preqin. All eight rows are real products, but the set of eight is the author’s choice.

### p05-01 (page 5)

Current:
> Exhibit 3. Apps, Copilot and Studio all call one shared API layer

Recommended:
> Exhibit 3. Apps, Copilot and Studio share the same Aladdin services and data

Alternative:
> Exhibit 3. Copilot and Studio call the same Aladdin APIs

What it means and what else changes: Recommended: “share the same Aladdin services and data”, which rests on the Studio page’s “shared services and data” [14] and needs no inference. Alternative: “Copilot and Studio call the same Aladdin APIs”. Page 10 (p10-07+p10-10+p10-13) calls that link my inference, so under the alternative the Exhibit 3 note must add “That Copilot and Studio call the same APIs is my inference.” and the Shared API layer box (p05-16) reads “Copilot and Studio call it · every call needs credentials”. Either way the Exhibit 3 description below changes, and the Exhibit 14 boxes on page 13 use the matching “shared services” wording (p13-26, p13-34+p13-35). Diagram: under the recommended title, the arrows from the Apps panel and the SDK into the API bar would still read as every app calling one API layer. The smallest fix is to rename that bar from “Shared API layer” to “Shared services and APIs” (p05-16), so the arrows show apps, Copilot and Studio using shared services. Under the alternative, the bar keeps its name.

Also change, Exhibit 3 aria-label (also carries p05-29 and p05-30):
> Apps, Copilot and Aladdin Studio call one shared API layer, which reaches the 11 public API domains, all using Aladdin Analytics, the risk engine. Every domain reads and writes shared data:
becomes
> Apps, Copilot and Aladdin Studio share the same Aladdin services and data. A layer of shared services and APIs reaches the 11 public API domains. The risk specifications name Aladdin Analytics as their risk engine. The domains read and write shared records:


Why: The Studio page says only “API-first approach across shared services and data” [14], and Rosales says Copilot tools map “one-to-one to an existing Aladdin API already out in production” [8]. No source says BlackRock’s own apps call the public API layer. The recommended title keeps all three actors on the sourced “shared services and data”. The alternative names only the two callers the sources show, and then the Exhibit 14 tile “all call these APIs” must also drop the apps. Either way the box text (p05-16) and Exhibit 14 on page 13 change with it. Both Exhibit 14 replacements are no longer than the current text.

### p05-47+p05-48 (page 5)

Current:
> Exhibit 4. Six pieces make up Studio

Recommended:
> Exhibit 4. Studio, grouped here into six pieces

Alternative:
> Exhibit 4. Studio, grouped here into eight pieces

What it means and what else changes: No source gives a count of six. Recommended: “Studio, grouped here into six pieces”, which keeps page 5 the same length. Alternative: “Studio, grouped here into eight pieces”, adding two rows, “Aladdin Data eXchange: automated file transfer to and from Aladdin” with the ADX page, and “Aladdin Tools for Excel: an Excel plugin that retrieves Aladdin data” with the ATX page. That lengthens page 5 by about four lines. The row fixes p05-48+p05-50, the Event-driven row and the Developer Portal row apply under either option.

Also change, Exhibit 4 note, say there is no official count:
> Woodhead [1] and Goel [26].
becomes
> Woodhead [1] and Goel [26]. BlackRock gives no count. Its APIs page also links Aladdin Data eXchange and Aladdin Tools for Excel, which Exhibit 3 shows [24].


Why: No source gives a count of six. BlackRock’s APIs page lists Studio home, Data Cloud, ADX, Compute and ATX, and Snowflake’s partner page lists five capabilities, so the six rows are the author’s grouping. The recommended title says so and keeps page 5 the same length. The alternative adds ADX and ATX, which Exhibit 3 already shows.

### p07-22+p07-27+p07-28+p07-31+p07-40+p07-45 (page 7)

Current:
> Four of the five describe Studio in the same terms, APIs and events plus the Data Cloud, and two of those four add developer tools. Newman calls Data Cloud “part of Studio” [16]. Goel describes events, APIs and a near-real-time data store [26]. Khara calls it programmatic access to data and reporting [30]. A 2026 job posting calls Studio “Aladdin’s extensibility layer” [32]. The message is consistent across speakers and years, so BlackRock already has a positioning for Studio.

Recommended:
> Khara, Newman, Goel and Woodhead describe ways for clients to reach Aladdin through code. Only Woodhead names every part, developer tools included [1]. Newman calls the Data Cloud and the analytics APIs part of Studio [16]. Goel says every transaction should be available to clients through an event or an API. He also describes a near-real-time data store [26]. Khara calls Studio programmatic access to data and reporting [30]. A 2026 job posting for a product director of Aladdin Studio Developer calls it “Aladdin’s extensibility layer” [32]. APIs and data access recur across speakers and years, so BlackRock already has the core of a positioning for Studio.

Alternative:
> Newman, Goel and Woodhead each name APIs and a data store. Only Woodhead also names developer tools [1]. Newman calls the Data Cloud and the analytics APIs part of Studio [16]. Goel says every transaction should be available to clients through an event or an API. He also describes a near-real-time data store [26]. Khara calls Studio programmatic access to data and reporting [30]. A 2026 job posting for a product director of Aladdin Studio Developer calls it “Aladdin’s extensibility layer” [32]. APIs and data access recur across speakers and years, so BlackRock already has the core of a positioning for Studio.

What it means and what else changes: The opening of the paragraph and the Exhibit 7 title carry the same claim, so both take the same option. Recommended: Exhibit 7 keeps all four speakers and replaces the tick columns with one “Parts they name” column, so the quote column keeps its width and rows stay at two lines. The title says “Four speakers describe parts of Studio, and only Woodhead names them all”, and the paragraph names the four speakers. Alternative: drop Khara from Exhibit 7, title it “Three speakers name APIs and a data store, and only Woodhead names developer tools”, and open the paragraph with those three. Under either option the paragraph closes with “APIs and data access recur across speakers and years”, which every row supports. Page 6 (p06-66) and the Exhibit 6 title (p07-01) already say “describe Studio or its parts”, which fits both options.

Also change, Exhibit 7 (title, columns, rows and note). Recommended table; the alternative table is in alternative_html of this entry.:
> Exhibit 7. All four speakers name APIs, events and the Data Cloud as parts of Studio
> Speaker, date | What they said | APIs and events | Data Cloud | Developer tools
> Kunal Khara, early 2024 | “More users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis” [30] | Yes | Yes | –
> Richard Newman, January 2025 | “The Aladdin data cloud ... which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella” [16] | Yes | Yes | –
> Diwakar Goel, 2025 | “Every single transaction ... via an event, via an API”; “a near real time data store”; exposing “the software and application that we’re building” [26] | Yes | Yes | Yes
> Dave Woodhead, November 2025 | “It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... developer tools” [1] | Yes | Yes | Yes
> Source: the four recordings cited [1, 16, 26, 30]. Quotations are verbatim; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. Yes means the speaker names that part; – means not. Only Goel and Woodhead name developer tools.
becomes
> Exhibit 7. Four speakers describe parts of Studio, and only Woodhead names them all
> Speaker, date | What they said | Parts they name
> Kunal Khara, early 2024 | “More users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis” [30] | None by name. Programmatic access implies APIs
> Richard Newman, January 2025 | “Aladdin data cloud specifically comes in, which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella” [16] | APIs, Data Cloud
> Diwakar Goel, 2025 | “Every single transaction ... via an event, via an API”; “a near real time data store”; exposing “the software and application that we’re building” [26] | APIs, events, a near-real-time data store
> Dave Woodhead, November 2025 | “It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... developer tools” [1] | APIs, events, Data Cloud, developer tools
> Source: the four recordings cited [1, 16, 26, 30]. Quotations are verbatim. Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. Goel does not use the name Studio.

Under the alternative it becomes:
> Exhibit 7. Three speakers name APIs and a data store, and only Woodhead names developer tools
> Speaker, date | What they said | Parts they name
> Richard Newman, January 2025 | “Aladdin data cloud specifically comes in, which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella” [16] | APIs, Data Cloud
> Diwakar Goel, 2025 | “Every single transaction ... via an event, via an API”; “a near real time data store”; exposing “the software and application that we’re building” [26] | APIs, events, a near-real-time data store
> Dave Woodhead, November 2025 | “It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... developer tools” [1] | APIs, events, Data Cloud, developer tools
> Source: the three recordings cited [1, 16, 26]. Quotations are verbatim. Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. Goel does not use the name Studio.


Why: Only Woodhead names APIs, events and the Data Cloud while calling it Studio (Simplecast transcript [00:05:25] "a set of APIs events. The Aladdin Data Cloud"). Newman has the Data Cloud and APIs but no events, Goel has all three without saying Studio, and Khara gives only programmatic access ([18:37] "on a programmatic basis at machine scale"). The job posting gives the label to Studio Developer: "Set and evolve the vision for Studio Developer as Aladdin's extensibility layer". The opening count is the paragraph's thesis, hence DECIDE. Recommended keeps "Four", which holds because Khara describes programmatic access and Miller speaks only about the Data Cloud. The alternative drops Khara from Exhibit 7 and names the three speakers who name APIs and the Data Cloud. Newman never says "event", Khara names none of the three ([18:42] "on a programmatic basis"), and Goel never says "developer tools" ([35:40] is about BlackRock staff). The “Parts they name” column shows Newman's APIs without events, Goel's data store and Khara's unnamed programmatic access. The Newman quote now matches the published transcript word for word: "and Aladdin data cloud specifically comes in, which is part of Studio". The old "The Aladdin data cloud ... which is part of Studio" dropped "data cloud and" without an ellipsis. The new title and column change the exhibit, hence DECIDE. Optional: Woodhead now has a published transcript (Simplecast, [00:05:25]), so source 1 could cite it instead of YouTube auto-captions.

### p08-31 (page 8)

Current:
> Aladdin won the tenders of three public pension bodies

Recommended:
> BlackRock won the tenders of three public pension bodies

Alternative:
> Aladdin won the tenders of two UK public pension bodies

What it means and what else changes: All three award records name BlackRock Financial Management as the winner, and only the PPF and Nest records tie a win to Aladdin. Recommended: retitle to “BlackRock won” and keep all three rows. The PPF, PBGC and note fixes (p08-35, p08-40+p08-41+p08-42, p08-43) already say “BlackRock won”. Alternative: keep “Aladdin” and drop the PBGC row, which weakens the exhibit to two UK bodies. Then the PPF and Nest cells start “Aladdin won”, the note drops USAspending.gov and both PBGC sources leave the register. Nothing else in the document counts the pension bodies.

Also change, Exhibit 9, Nest row (needed under either option):
> 2023 | Aladdin won against six other bids
becomes
> 2023 | Nest chose BlackRock’s Aladdin over six other bids [NEW]

- New source (register): [P] Nest selects BlackRock’s Aladdin as its investment risk platform. Nest press release, November 13, 2023. https://www.nestpensions.org.uk/schemeweb/nest/nestcorporation/news-press-and-policy/press-releases/Nest-selects-BlackRock-s-Aladdin-as-its-investment-risk-platform.html

Why: All three award records name BlackRock Financial Management as the winner. Only the PPF notice (supplier web address blackrock.com/aladdin) and Nest’s own press release (“Nest selects BlackRock’s Aladdin as its investment risk platform”, 13 November 2023) tie a win to Aladdin. The PBGC records describe an “Investment Risk Management System” and name no product, and a search found no PBGC source naming Aladdin. Recommended: retitle to BlackRock and keep all three rows. Alternative: keep Aladdin and drop the PBGC row, which weakens the exhibit to two UK bodies.

### p09-01 (page 9)

Current:
> BlackRock tells investors growth will come from API calls, without naming the product behind them. It projected at its 2025 Investor Day that API calls across BlackRock and Aladdin would grow 17x by 2030 [10].

Recommended:
> BlackRock tells investors that API calls will grow fastest, without naming the product behind them. At its 2025 Investor Day it forecast four volumes to 2030. API calls across BlackRock and Aladdin led, with 17x growth [10].

Alternative:
> BlackRock tells investors that API calls will grow fastest, without naming the product behind them. At its 2025 Investor Day it forecast four volumes to 2030. API calls across BlackRock and Aladdin led, with 17x growth [10].

What it means and what else changes: Slide 23 forecasts four volumes and does not say growth comes from API calls. Recommended: fix the two lead sentences and the direction box (p10-01) and keep the Finding 2 heading, which the paragraph already labels as my inference. Alternative: also retitle the heading to “2. BlackRock’s fastest-growing forecast for investors runs through Studio, though it rarely says the name”. Page 2 and Part 3 already state the 17x forecast correctly.

Also change, Finding 2 heading (alternative only) (not applied unless the alternative is chosen):
> 2. BlackRock’s growth story to investors runs through Studio, though it rarely says the name
becomes
> 2. BlackRock’s fastest-growing forecast for investors runs through Studio, though it rarely says the name


Why: Slide 23 of the 2025 Investor Day deck (source 10) sits under “Continuously drive marginal costs down”. It forecasts four volumes to 2030: portfolios 2x, model portfolios 4x, trade allocations 1.3x and API calls 17x. It does not say growth comes from API calls. The fix changes the lead sentence of Finding 2 and its direction box. Recommended: change those two and keep the heading, which the paragraph already labels as the author’s inference. Alternative: also retitle the heading as shown. Page 2 (“API calls will grow 17x by 2030”) is already correct.

### p11-34 (page 11)

Current:
> Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources. State Street, Clearwater and Bloomberg have none, so they are not listed.

Recommended:
> State Street is not listed because my sources show no AI feature it offers clients.

Alternative:
> Clearwater announced CWAN GenAI, with more than 800 AI agents for clients, in November 2025 [NEW]. Bloomberg launched an MCP server for licensed data in late September 2026 [NEW]. State Street is not listed because my sources show no AI feature it offers clients.

What it means and what else changes: Bloomberg launched Enterprise MCP on September 29, 2026 and Clearwater announced CWAN GenAI with 800+ AI agents on November 5, 2025. Recommended: add both as rows, so the title reads “Of 11 providers a Studio buyer compares, ten have announced AI features or AI access to their data” and the prose before the exhibit counts four rivals. Alternative: keep nine rows, put both facts in the note (alternative_html), and change the prose to “Six data and cloud providers that Studio buyers also use offer a connector or an MCP server, and system-of-record rivals have announced AI features.” Under either option, Part 3 on page 13 adds Clearwater (same length), and Exhibit 17 scores Bloomberg’s AI connector 2 (p15-26+p15-27+p15-28+p15-29). Exhibit 17 keeps Clearwater’s AI connector at 0, which fits its definition if CWAN’s agents run only inside Clearwater’s platform. The author should confirm that from the release.

Also change, Exhibit 12 table, add Clearwater and Bloomberg rows after the Arcesium row (recommended only):
> Arcesium press releases [56, 57]
becomes
> Arcesium press releases [56, 57]
> Clearwater | Clearwater announced CWAN GenAI, with more than 800 AI agents for clients, in November 2025 | Clearwater press release [NEW]
> Bloomberg | Bloomberg launched an MCP server for licensed data in September 2026 | Bloomberg press release [NEW]

Also change, Exhibit 12 title (recommended only):
> Of nine providers a Studio buyer compares, eight have announced AI features or AI access to their data
becomes
> Of 11 providers a Studio buyer compares, ten have announced AI features or AI access to their data

Also change, Page 10 prose before Exhibit 12 (recommended only):
> Six data and cloud providers that Studio buyers also use offer a connector or an MCP server, and two system-of-record rivals have announced AI features.
becomes
> Six data and cloud providers that Studio buyers also use offer a connector or an MCP server. Four system-of-record rivals have announced AI features or AI access to their data.

Also change, Part 3, page 13 (both options; same length or shorter, so page 13 still fits):
> SimCorp has announced AI agents, Arcesium an AI platform, and other systems of record will likely follow [7, 56, 57].
becomes
> SimCorp and Clearwater have announced AI agents, Arcesium an AI platform, and others will likely follow [7, NEW, 56, 57].

- New source (register): [P] Bloomberg Launches Enterprise MCP to Seamlessly Connect Bloomberg Data with Clients’ Enterprise AI Applications. Bloomberg press release, PR Newswire, September 29, 2026. https://www.prnewswire.com/news-releases/bloomberg-launches-enterprise-mcp-to-seamlessly-connect-bloomberg-data-with-clients-enterprise-ai-applications-302891331.html
- New source (register): [P] CWAN Reports 800+ AI Agents Now Available for Deployment Across $10 Trillion in Client Assets. Clearwater Analytics press release (Business Wire), November 5, 2025. https://www.businesswire.com/news/home/20251105092732/en/

Why: Bloomberg announced Enterprise MCP, “an AI access layer for Data License Plus”, on September 29, 2026 (PR Newswire), and Clearwater “announced the global deployment of CWAN GenAI” with 800+ AI agents on November 5, 2025 (Business Wire), both before the October 2026 as-of date. Recommended: add both rows, which changes the exhibit title count and the prose count. State Street has stated AI plans but no client AI feature in the sources found, so it alone stays off the table.

### p11-38 (page 11)

Current:
> 4. Buyers at BlackRock’s own webinar said they want a core platform plus their own builds

Recommended:
> 4. At BlackRock’s own webinar, two thirds of attendees said they run vendor or hybrid platforms

Alternative:
> 4. BlackRock’s own webinar panel described a core platform plus each firm’s own builds

What it means and what else changes: The heading is the finding. Attendees reported where they sit today, and the core-plus-builds model is the panel’s description. Recommended: “4. At BlackRock’s own webinar, two thirds of attendees said they run vendor or hybrid platforms”, which matches the Exhibit 13 title. Alternative: “4. BlackRock’s own webinar panel described a core platform plus each firm’s own builds”. Under either option the page 12 rivals sentence changes as below.

Also change, Page 12 body, first sentence of the rivals paragraph (repeats the same 'want' claim):
> Rivals are selling to the same buyer, the one who wants a core platform plus their own builds.
becomes
> Rivals sell the same model, a core platform with the client’s own builds on top.


Why: Attendees reported where they sit today, “mostly vendor platforms at 37%” and “hybrid ... at 30”, so 67 percent (source 9, 00:04:40). The core-plus-builds model is the panel’s description: Schafer says hybrid firms use “vendor platforms ... as the core architecture” and build around it, and Sewdass calls it “that hybrid approach” (00:05:15, 00:49:09). No attendee said they want it.

### p13-22 (page 13)

Current:
> Exhibit 14. BlackRock’s applications and a client’s code call the same APIs under the same permissions

Recommended:
> Exhibit 14. BlackRock’s applications and a client’s code draw on Aladdin’s shared services and APIs

Alternative:
> Exhibit 14. BlackRock’s applications and a client’s code call the same APIs

What it means and what else changes: No source says BlackRock’s apps and a client’s code call identical APIs under identical permissions. Recommended: “draw on Aladdin’s shared services and APIs”, from the Studio page’s “shared services” [14], with the right-hand header “A CLIENT’S USE · THROUGH STUDIO”. Alternative: “call the same APIs”, keeping the header, plus a note sentence after “The hatched box is not.”: “That both sides call the same APIs is my inference. Copilot’s tools map to production Aladdin APIs, and Studio offers clients APIs built on shared services.” The alternative adds about one line to the note on page 13, so something else on that page must shrink. Under either option the boxes, the band caption and the description (p13-26, p13-27, p13-34+p13-35, p13-37, p13-40, p13-aria) change as listed, and the Part 3 lede stays, because it is about controls. This choice should match p05-01 (Exhibit 3 title) and page 10, which calls the Copilot and Studio link my inference.

Also change, Exhibit 14 right-hand band header (recommended only):
> A CLIENT’S USE · THE SAME APIS
becomes
> A CLIENT’S USE · THROUGH STUDIO


Why: No source says BlackRock’s apps and a client’s code call identical APIs under identical permissions. The Studio page (source 14) says “API-first approach across shared services and data” and “secure, common, and extensible services”. Source 8 says the trading team owns “all of the services that serve trading data to all Aladdin applications” (4:06). The recommended title states only that. Permissions are shown in the boxes below and drop out of the title. The new title is shorter than the old one.

### p15-26+p15-27+p15-28+p15-29 (page 15)

Current:
> Bloomberg | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1

Recommended:
> Bloomberg | 1 | 0 | 1 | 0 | 2 | 1 | 2 | 1

Alternative:
> Bloomberg | 1 | 0 | 1 | 1 | 1 | 1 | 2 | 1

What it means and what else changes: Recommended scores: First API call 0, because the trial needs a signed Trial License Agreement, and Sample code 2, because the API Library page offers SDK downloads with example files. Alternative: First API call 1, counting the emailed trial as sign-up, and Sample code 1. Both give Bloomberg 8 of 16, still the top of the investment-platform cluster. The AI connector goes from 0 to 2 under both options. That matches Exhibit 12, which lists the Bloomberg MCP launch under either option of p11-34. The p15-118 alternative works only with the recommended First API call score of 0.

- New source (register): [P] API Library. Bloomberg Professional Services, as of October 2026. https://professional.bloomberg.com/support/api-library/
- New source (register): [P] App Portal overview for developers. Bloomberg Professional Services, PDF dated June 30, 2022. https://assets.bbhub.io/professional/sites/10/App-Portal-Overview-for-Developers.pdf

Why: Bloomberg's API Library says its libraries "are only compatible with the Bloomberg Server API and B-Pipe data feed products", and the trial needs a signed Trial License Agreement, so a first call needs a contract (0). The same public page offers SDK zips with 127 example files, so sample code is public (2). The App Portal PDF describes a third-party app marketplace for "more than 350,000 Bloomberg users", which matches the 1 given to other client-only marketplaces. Bloomberg launched Enterprise MCP on September 29, 2026, which the exhibit's own footnote scores 2. DECIDE because the AI connector change must match the Exhibit 12 note (g06), and the first-call and sample-code scores have a reasonable alternative.

### p15-38 (page 15)

Current:
> For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform.

Recommended:
> For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform. For the Call to action score: 2 means a developer can sign up and start alone, 1 a trial or access request, and 0 sales contact only.

Alternative:
> For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform. For the Call to action score: 2 means a developer can sign up and start alone, and 1 means a request form, a meeting or a demo.

What it means and what else changes: The definition sets the scale for the whole Call to action column. Recommended: 2 for self-serve sign-up, 1 for a trial or access request, 0 for sales contact only. FactSet, MSCI and Arcesium then score 1, Studio, SimCorp and Clearwater stay 0, and Snowflake and Databricks stay 2. Alternative: count any call to action, sales contact included, as 1. Then the last cell of the Aladdin Studio, SimCorp and Clearwater rows also goes from 0 to 1, and Studio shows “Book a meeting”, which Exhibit 16 already quotes.


Why: The Studio page offers "Book a meeting" and "Download the brochure", so it has calls to action, but they are sales contacts. Clearwater and SimCorp have the same kind and also score 0, while the 1s go to trial or access requests such as State Street's "Get Started". A one-line definition makes the 0 accurate and keeps the column consistent. DECIDE because the definition sets the scale for the whole column.

### p15-118 (page 15)

Current:
> At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, documentation, a sandbox and a first call come after a relationship exists.

Recommended:
> At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, a first API call needs a contract or a relationship.

Alternative:
> At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, a first API call needs a contract or a relationship.

What it means and what else changes: Under the corrected scores, Aladdin, Bloomberg and State Street show partial public docs, and Bloomberg, State Street and Arcesium a trial on request. All six investment platforms score 0 for a first API call without a contract. The sentence states that one fact, which holds for all six (it needs Bloomberg's first call at 0, the recommended option of p15-26+p15-27+p15-28+p15-29). Recommended: that sentence, and the Exhibit 17 title says the platforms “open to developers mostly after a relationship”. Alternative: the same sentence, and the title narrows to the first call: “At investment platforms, Studio among them, a first API call needs a relationship”. Both titles fit on one line.

Also change, Exhibit 17 title (recommended):
> Exhibit 17. Investment platforms, Studio among them, open to developers only after a relationship exists
becomes
> Exhibit 17. Investment platforms, Studio among them, open to developers mostly after a relationship

Also change, Exhibit 17 title (alternative only) (not applied unless the alternative is chosen):
> Exhibit 17. Investment platforms, Studio among them, open to developers only after a relationship exists
becomes
> Exhibit 17. At investment platforms, Studio among them, a first API call needs a relationship


Why: Exhibit 17 scores Aladdin, Bloomberg and State Street 1 for public docs, and Bloomberg 1 for sandbox and first call. The public SDK README is real documentation [23]. The sentence holds fully for SimCorp, Clearwater and Arcesium, which score 0 on all three. Reviewer: after g09’s score changes, SimCorp and Clearwater score 0 on all three and Arcesium scores 1 for its trial (p15-54), so the sentence needs “mostly” and the title must agree.

### p15-119 (page 15)

Current:
> Data and cloud platforms sell to developers directly and cluster high.

Recommended:
> Snowflake and Databricks sell to developers directly and score highest. LSEG and FactSet come next. FactSet and MSCI allow a first API call only for licensed clients [4, 67].

Alternative:
> Cloud data platforms sell to developers directly and score highest. Market data vendors publish their API catalogs but tie a first call to sign-up or a license.

What it means and what else changes: This is the paragraph’s closing claim. Totals out of 16 after the g09 score fixes: Snowflake 16, Databricks 16, LSEG 12, FactSet 11, MSCI 8. Recommended: name the platforms. Alternative: split the “Data and cloud platforms” band of Exhibit 17 into “Cloud data platforms” (Snowflake, Databricks) and “Market data vendors” (LSEG, FactSet, MSCI) and use the alternative sentence. Reviewer: g08’s draft said FactSet keeps trials for licensed clients, but FactSet’s trial now scores 1 on request (p15-97+p15-102), so the sentence speaks of the first call, which FactSet and MSCI both score 0.

Also change, Exhibit 17 group row (alternative only; the second group row goes before LSEG) (not applied unless the alternative is chosen):
> Data and cloud platforms
becomes
> Cloud data platforms


Why: This is the paragraph’s closing claim, so it changes the argument. Snowflake and Databricks score 16 of 16 and offer self-serve trials (“Start your 30-day trial with $400 in free credits”). LSEG scores 12. FactSet scores 9: its “Try for free” is a contact form and its guide says to “contact your FactSet account manager”. MSCI scores 2 and “grants no right or license ... without an appropriate license” [4].

## Fixes

### Page 2

#### p02-lede (NO CHANGE)

Current:
> Clients’ AI tools could act on Aladdin under the same controls BlackRock’s own business runs on.


Why: The lede is about controls, not identical APIs. The controls it rests on, access set per API, a second check on dataset releases and compliance by default on orders, stay sourced after the fixes [6].

#### p02-05+p02-06+p02-07 (FIX)

Current:
> They post orders and set compliance rules, under each user’s permissions and with a compliance check on every order [6].

Proposed:
> They post orders and assign compliance rules to portfolios. Access is granted per API, to read or to write. Compliance runs on each order by default [6].


Why: The order spec says “Filter, post or cancel orders”, but the compliance specs only filter rules and “assign compliance rules for portfolio” (ComplianceRuleAssignmentAPI). Every operation also accepts client-credentials, client-key and basic auth, so “each user’s permissions” overstates it, while OAuth scopes are read or write per API. runCompliance is “Default is true”, and the caller can turn it off, so “every order” becomes “by default”. Reviewer: “OAuth sign-in” was replaced with plain words. The matching Exhibit 14 control-box titles change under p13-37, and the Exhibit 14 description under p13-aria.

#### p02-simcorp (NO CHANGE)

Current:
> Letting AI tools act will not stay unique; SimCorp has announced AI agents


Why: SimCorp is one true example [7]. Adding Clearwater here would lengthen page 2, and page 13 carries the fuller list (p11-34).

#### p02-14 (FIX)

Current:
> 11 public asdk_plugin Python packages, 128 recordings,

Proposed:
> 11 public asdk_plugin Python packages, about 125 recordings,


Why: The two corpus indexes have 34 and 95 rows, which gives 129. One row is text notes, at least three recordings appear in both indexes, and at least one is in neither, so there are about 126 distinct recordings. The 11 packages and 54 specifications were reconfirmed on PyPI. The same count on page 6 changes under p06-66.

#### p02-20 (FIX)

Current:
> at the end of this document, giving the grade (P, S or T), title, speaker and date.

Proposed:
> at the end of this document, giving the grade (P, S or T), title, publisher or speaker, and date where known.


Why: P entries name a publisher, not a speaker, such as “Aladdin Data Cloud product page. BlackRock, as of October 2026.” Several entries have no date, such as source 20 (“undated”), source 21 (“speaker not named, undated”) and source 9 (“Replay page undated”). Page 16 gets the same words under p16-09.

### Page 3

#### p03-02 (FIX)

Current:
> Brennan Rosales, its AI Engineering Lead, put the scale

Proposed:
> Brennan Rosales, an AI Engineering Lead at BlackRock, put the scale


Why: He introduces himself as “an AI engineering lead at BlackRock” [0:15], and the LangChain Interrupt speaker list gives “AI Engineering Lead at BlackRock”. “Its” makes him the only one.

#### p03-14 (FIX)

Current:
> BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code.

Proposed:
> BlackRock sells Aladdin as four platforms that share one data language. They are the Aladdin platform, eFront, Aladdin Wealth and Preqin [NEW]. Studio is the entry point for people who write code [14].

- New source (register): [P] BlackRock Aladdin Drives Private Markets Transparency By Unifying Pre- and Post-Investment Tech On a Single Platform. BlackRock press release, February 5, 2026. https://www.blackrock.com/aladdin/discover/press-release/blackrock-aladdin-drives-private-markets-transparency

Why: BlackRock’s 5 February 2026 release says “BlackRock Aladdin, inclusive of the Aladdin platform, eFront, Aladdin Wealth, and Preqin … providing a common data language across the whole portfolio.” “One engine” overstates it, because BlackRock lists four platforms and sells eFront and Preqin on their own. The Studio page says “Build on top of Aladdin”, so source 14 supports the second sentence. Reviewer: reworded so “family of the Aladdin platform” cannot be misread. Exhibit 1 has no Preqin row; see the DECIDE item p03-16+p03-17.

#### p03-19 (FIX)

Current:
> The front-to-back system for public markets, the same system BlackRock runs internally [8]

Proposed:
> The front-to-back system for public and private markets [NEW], the same system BlackRock runs internally [8]

Also change, Exhibit 1 source note (page 3). One combined change covers p03-19, p03-27, p03-30 and p03-36.:
> Source: BlackRock product pages [14, 17, 19]; Amazon press release, December 2025 [15]; iShares prospectus [18]; the public specifications [6].
becomes
> Source: BlackRock product pages [14, 17, 19, NEW, NEW]; BlackRock AWS release, December 2025 [15]; Woodhead [1]; iShares prospectus [18]; the public specifications [6].

- New source (register): [P] Whole Portfolio Management. BlackRock Aladdin product page, as of October 2026. https://www.blackrock.com/aladdin/platforms/products/whole-portfolio

Why: BlackRock’s Whole Portfolio page says “Streamline front-to-back workflows with a unified IBOR for public and private assets.” Source 8 says Aladdin gives “access to both public and private markets” and “BlackRock is the biggest user of Aladdin”, but never says “front-to-back”. The also_change below is the one combined Exhibit 1 source note for p03-19, p03-27, p03-30 and p03-36.

#### p03-27 (CITE)

Current:
> Preqin now sits inside eFront Insight, and

Proposed:
> Preqin now sits inside eFront Insight [NEW], and

- New source (register): [P] Powerful Analytics for Private Markets (eFront Insight product page). eFront, BlackRock, as of October 2026. https://www.efront.com/en/alternative-investment-software/efront-insight

Why: The eFront Insight page says “With Preqin® inside, eFront® Insight makes private markets investing more seamless and more informed.” Source 13 says only that the expansion “brings together Aladdin technology with Preqin and eFront data and analytics”, so 13 stays on the May 2026 clause. The Exhibit 1 source note changes once, under p03-19.

#### p03-30 (CITE)

Current:
> It covers APIs and events, Aladdin Data Cloud, and developer tools. BlackRock calls it

Proposed:
> It covers APIs and events, Aladdin Data Cloud, and developer tools [1]. BlackRock calls it


Why: Source 14 covers APIs, Data Cloud and developer tools but not events. Woodhead (source 1, already cited for the same list on page 2) says Studio “exposes everything Aladdin knows how to do as a set of APIs [and] events” and that Data Cloud is “built on top of Snowflake”. The Exhibit 1 source note changes once, under p03-19.

#### p03-36 (CITE)

Current:
> It is sold as an add-on to Aladdin Enterprise [15].

Proposed:
> It is sold as an add-on to Aladdin Enterprise [15].

Also change, Sources register, existing AWS release entry (reused instead of a duplicate new entry):
> BlackRock partners with AWS to deliver Aladdin on secure, scalable cloud infrastructure. Amazon press release, December 2025. https://press.aboutamazon.com/aws/2025/12/blackrock-partners-with-aws-to-deliver-aladdin-on-secure-scalable-cloud-infrastructure
becomes
> BlackRock partners with AWS to deliver Aladdin on secure, scalable cloud infrastructure. BlackRock press release, December 5, 2025. Full release with its questions and answers, Reuters copy on TradingView News: https://www.tradingview.com/news/reuters.com,2025-12-05:newsml_Zaw4R27h7:0-pressr-blackrock-partners-with-aws-to-deliver-aladdin-on-secure-scalable-cloud-infrastructure/ Copy without the questions and answers, on Amazon’s press site: https://press.aboutamazon.com/aws/2025/12/blackrock-partners-with-aws-to-deliver-aladdin-on-secure-scalable-cloud-infrastructure


Why: The full release with its questions and answers says AWS hosting will first cover “Aladdin Enterprise (US-hosted only) Accounting (Enterprise add-on) ADC (Enterprise add-on)”. The Amazon copy has no “add-on” wording. The existing AWS release entry (source 15) now carries the full-release copy as well as the Amazon copy, so one release has one entry. Exhibit 3 still cites it for hosting.

### Page 4

#### p04-06 (FIX)

Current:
> compares a changed portfolio with the original before anything is traded [21]

Proposed:
> shows a changed portfolio beside the original [21]


Why: The recording shows the original and the what-if portfolio "side by side" (BahCi45_BTc captions ~11:09) but never mentions trading. "Before anything is traded" was the author's inference, so it goes.

#### p04-11 (FIX)

Current:
> Any violation then carries an owner, a disposition and a resolution comment [6]

Proposed:
> A violation record can hold an owner and a user’s resolution comment. It gets a disposition when closed [6]


Why: The Violation spec says the disposition "will be populated for closed violations" and the comment is one "populated by a user". Only actionStatus is required, so not every violation carries all three.

#### p04-13 (FIX)

Current:
> (ComplianceRule spec); no application is named [6]

Proposed:
> (ComplianceRule spec). The Level spec names the application “Aladdin Compliance” [6]


Why: Source 6's Level spec says "A unique name for a rule in Aladdin Compliance", and step 5 already counts Aladdin Accounting from the same kind of spec text. The alternative is to drop Aladdin Accounting from step 5 so both rows use the stricter standard, but that throws away a true fact.

#### p04-22 (FIX)

Current:
> BrokerConfirmRoutingAPI routes the confirm [6]

Proposed:
> BrokerConfirmRoutingAPI holds each broker’s instructions for delivering confirms [6]


Why: The spec says BrokerConfirmRouting "describes instructions for delivering trade information to a broker desk" and that routings "are setup at broker level". Its only operations create, update, remove, validate and filter those records, so it does not send the confirm itself.

#### p04-28 (FIX)

Current:
> Positions appear only as fields: a positions source in PortfolioToolkitAPI, and a violation’s

Proposed:
> Positions appear only as fields, for example a positions source in PortfolioToolkitAPI, collateral positions in CollateralStatementAPI and a violation’s


Why: "Only as fields" holds, but the colon made two examples read as the full list. CollateralStatementAPI also has "Details of collateral positions" (swagger.json:979), so the sentence now gives examples.

#### p04-41 (FIX)

Current:
> the Aladdin Accounting episode with David Schneid and Daniel Shannon, which does not label who is speaking [20]

Proposed:
> the Aladdin Accounting episode with David Schneid and Daniel Shannon [20]

Also change, Exhibit 2, step 3, product column:
> Schneid or Shannon of Aladdin Accounting describes the run
becomes
> David Schneid, head of product management for Aladdin Accounting, describes the run

Also change, Exhibit 2, step 5, who acts:
> The accounting team, which says of itself: “we are data managers more than anything else” (Schneid or Shannon) [20]
becomes
> The accounting team. Daniel Shannon, BlackRock’s head of outsourced platform services, says “we are data managers more than anything else” [20]

Also change, Exhibit 2, step 6, who acts:
> heads of performance” (Schneid or Shannon) [20]
becomes
> heads of performance” (Schneid) [20]

Also change, Sources register, entry 20:
> David Schneid and Daniel Shannon, Aladdin Accounting, BlackRock, undated; the recording does not label which of the two is speaking.
becomes
> David Schneid, Head of Product Management for Aladdin Accounting, and Daniel Shannon, Head of Outsourced Platform Services, BlackRock, undated.


Why: The video names each speaker on screen: Shannon at 0:13 ("Head of Outsourced Platform Services, BlackRock") and Schneid at 0:35 ("Head of Product Management for Aladdin Accounting"), checked on frames of the published video. Shannon says "data managers" (1:05). Schneid says "heads of performance" (0:35) and "from that first order" (1:23).

#### p04-43 (FIX)

Current:
> The specifications name no order screen and hold no position or event API, and they do not say in what sequence steps 4 to 6 happen.

Proposed:
> The specifications hold no position or event API. They do not say in what sequence steps 4 to 6 happen.


Why: OrderAPI swagger.json:2244 says the Basket ID "is visible in the Basket column in Order Monitor of Aladdin Dashboard". So the specifications do name an order screen. Readability review: the Order Monitor sentence was an aside that nothing in the exhibit uses, so the fix now simply drops the wrong clause.

#### layout (table cells ending on one word plus a superscript) (FIX)

Current:
> “Active,” “Booked”

Proposed:
> “Active,” “Booked”

Also change, Exhibit 2, step 3, product column:
> without lifting up the pencil”
becomes
> without lifting up the pencil”

Also change, Exhibit 2, step 5, product column:
> portfolio-configuration specification
becomes
> portfolio-configuration specification

Also change, Exhibit 2, step 5, API column:
> (AborLot spec)
becomes
> (AborLot spec)

Also change, Exhibit 6, Goel receipt:
> >Pensions webinar, 2025
becomes
> >Pensions webinar, 2025

Also change, Exhibit 9, PPF buyer:
> UK Pension Protection Fund
becomes
> UK Pension Protection Fund

Also change, Exhibit 9, PBGC buyer:
> US Pension Benefit Guaranty Corporation
becomes
> US Pension Benefit Guaranty Corporation

Also change, Exhibit 12, LSEG receipt:
> Investing.com summary
becomes
> Investing.com summary


Why: Layout only, no visible word changes. In these cells the last printed line held one word and its superscript. A non-breaking space keeps the last two words together. Most of these were already in the original; the plan fixes them while the tables are being touched.

### Page 5

#### p05-04 (FIX)

Current:
> quants

Proposed:
> data analysts


Why: The Studio page names “a professional engineer”, “a code-curious portfolio manager” and “a data analyst automating reporting” as Studio users [14]. No source names quants.

#### p05-copilot-box (FIX)

Current:
> reads what is on screen · answers through the same APIs

Proposed:
> reads what is on screen · answers by calling Aladdin APIs


Why: Consistency. “The same APIs” implies Copilot and Studio share one API set, which page 10 now calls my inference. Source 8 supports only that each tool maps to a production Aladdin API (4:39). The new text is shorter.

#### p05-16 (FIX)

Current:
> Shared API layerevery app, Copilot and Studio call it · access checked on every call

Proposed:
> Shared services and APIsused by apps, Copilot and Studio · public calls need credentials


Why: No source says every app calls the API layer. The Studio page says “shared services and data” [14] and Copilot tools map to “an existing Aladdin API already out in production” [8]. All 301 operations in the 54 specifications declare a security requirement (rechecked on the PyPI 2.0.0b3 files), but scope checks apply only to the OAuth options, so “needs credentials” is the accurate claim. If the p05-01 alternative is chosen, the box reads “Copilot and Studio call it · every call needs credentials”. Readability review: the arrows from the Apps panel still run into this bar, so the bar is renamed “Shared services and APIs”. Then the picture says what the Studio page says, that apps, Copilot and Studio use shared services. The note cites the Studio page and the specifications.

#### p05-29 (FIX)

Current:
> the risk engine every domain uses · turns positions and market data into risk numbers

Proposed:
> the risk engine · turns positions and market data into risk numbers

- New source (register): [P] Risk Management Services (Aladdin Risk product page). BlackRock, as of October 20, 2026. https://www.blackrock.com/aladdin/platforms/products/aladdin-risk

Why: The specs name “Aladdin Analytics” only as a metric source in four risk APIs [6], so “every domain uses” has no support. BlackRock’s Aladdin Risk page calls that product “BlackRock’s analytics engine” and says it integrates “positions, data, and analytics”, which supports the rest of the box.

#### p05-30 (FIX)

Current:
> SHARED DATA · EVERY DOMAIN READS AND WRITES IT

Proposed:
> SHARED DATA · READ AND WRITTEN BY THE DOMAINS


Why: In the specs the data domain only creates records (15 POST operations) and accounting mostly reads (4 GET and 4 POST, three of the POSTs filters and one a config submit) [6]. So the domains together read and write the records, but not every domain does both.

#### p05-36 (FIX)

Current:
> prices, ESG, Preqin

Proposed:
> prices, ESG data

- New source (register): [P] BlackRock Solutions Integrates ICE Data Services’ Continuous Evaluated Pricing Tool. Intercontinental Exchange press release, December 5, 2016. https://ir.theice.com/press/news-details/2016/BlackRock-Solutions-Integrates-ICE-Data-Services-Continuous-Evaluated-Pricing-Tool/default.aspx
- New source (register): [P] Access our research through your preferred platform. Morningstar Sustainalytics, as of October 20, 2026. Lists Aladdin among institutional investor platforms. https://www.sustainalytics.com/investor-solutions/analytic-reporting-solutions/esg-investment-platform

Why: BlackRock’s own boilerplate puts Preqin inside BlackRock Aladdin, “inclusive of the Aladdin platform, eFront®, Aladdin Wealth™, and Preqin” [13], so it is not an outside vendor. ICE’s 2016 release says its pricing “has been integrated into BlackRock Solutions’ Aladdin”, and Sustainalytics lists Aladdin among its platforms. Preqin is already placed inside Aladdin in Exhibit 1 and the private-markets finding, so the map does not need a new tile.

#### p05-41+p05-32 (Exhibit 3 note) (FIX)

Current:
> For illustrative purposes only. Source: about 100 apps, with Copilot in all of them, Rosales and Vicente Valdez at 2:35 [8]. The 11 domains behind the shared layer are the packages of BlackRock’s public SDK, named as in its specifications [6, 23]. App names other than Explore come from field descriptions in those specifications, so their screens are not drawn [6, 21]. Aladdin Analytics is the name the risk specifications give the engine [6]. Studio, Woodhead at 4:49 [1]; Excel tools and feeds, the APIs page [24]; Data Cloud fed by Aladdin data and analytics [1, 19]; hosting [15, 25]. Solid outline = shown in sources; hatched = announced, not live.

Proposed:
> For illustrative purposes only. The 11 domains are the packages of BlackRock’s public SDK, named as in its specifications. Other app names come from those specifications, so their screens are not drawn. Source: Rosales and Vicente Valdez at 2:35, for the apps and Copilot [8]; Woodhead at 4:49, for Studio, events and the Data Cloud [1]; the public specifications and SDK [6, 23]; a training recording, for Explore [21]; BlackRock’s Studio, APIs, ATX, ADX, Data Cloud and Aladdin Risk pages [14, 24, NEW, NEW, 19, NEW]; the Data Cloud launch release [NEW]; hosting [15, 25]; data vendors, ICE and Sustainalytics [NEW, NEW]. Solid outline = shown in sources; hatched = announced, not live.

- New source (register): [P] BlackRock To Launch the “Aladdin Data Cloud” Powered by Snowflake. BlackRock press release, February 22, 2021. https://www.blackrock.com/corporate/newsroom/media/press-releases/aladdin-data-cloud-powered-by-snowflake

Why: Dashboard appears in field descriptions, but Risk Radar appears only in the API-level description, e.g. “Retrieve, update, or create Exceptions as surfaced in Risk Radar” [6]. Source 21 names Explore only, so its citation moves to its own sentence. Source 19 confirms Snowflake but not “this client’s own”. The February 22, 2021 BlackRock release says “Each Aladdin Data Cloud client receives an independent, centrally-managed data store”, so the box words stand and only the citation is added. Readability review: the note had grown to six lines with 18 superscripts in two styles. It is now two plain sentences and one source list grouped by source, with 8 superscript groups. It also carries the citations that p05-04, p05-16, p05-29, p05-36 and p05-15+p05-44 used to add one by one: shared services and Studio's users (Studio page), credentials (specifications), Aladdin Risk page, ATX and ADX pages, ICE and Sustainalytics.

#### p05-15+p05-44 (FIX)

Current:
> events and files out

Proposed:
> events, files in and out

Also change, Exhibit 3 arrow from the Excel tools box to Client systems, make it two-way:
> (empty)
becomes
> (empty)

- New source (register): [P] ATX: Aladdin tools for Excel. BlackRock product page, as of October 20, 2026. https://www.blackrock.com/aladdin/platforms/products/aladdin-tools-for-excel
- New source (register): [P] ADX: Aladdin Data eXchange. BlackRock product page, as of October 20, 2026. https://www.blackrock.com/aladdin/platforms/products/aladdin-data-exchange

Why: The APIs page [24] only names and links ATX and ADX. The ATX page says it lets users “retrieve Aladdin data”, and the ADX page describes “automated data transfer to and from Aladdin” by SFTP or IBM MQ, so files go both ways. Events rest on Woodhead’s “a set of APIs events” at 4:49 [1].

#### p05-48+p05-50 (FIX)

Current:
> Aladdin Graph is the whole API layer, not one API: every public specification carries an id of the form agraph.<domain>.<segment>.<group>.v1.<API> [6].

Proposed:
> Aladdin Graph [23, 40] is the whole API layer, not one API. Every public specification’s id starts agraph.<domain> [6].


Why: All 54 ids start agraph.<domain>, but three specs are v2 and three have an extra segment, so only 48 match the five-part v1 form [6]. The name Aladdin Graph is backed by the SDK README, “based on Aladdin Graph API’s swagger specifications” [23], and BlackRock’s engineering blog, “curated Aladdin Graph APIs” [40], which is already in the register.

#### p05-48 (Event-driven row) (FIX)

Current:
> Event-driven APIs | Aladdin tells a program when something happens.

Proposed:
> Event-driven workflows | Aladdin tells a program when something happens [NEW, NEW].

- New source (register): [T] Job posting: Technical Writer, Vice President (Edinburgh). BlackRock, posted February 21, 2026, removed February 23, 2026. Copy kept by Built In Bristol. https://builtinbristol.uk/job/technical-writer-aladdin-product-vice-president/7444888

Why: No BlackRock page uses “Event-driven APIs” as a product name. BlackRock’s Aladdin Risk page lists “Aladdin Studio, APIs, and event-driven workflows” as capabilities, and a BlackRock job posting covers “event-driven workflows, including streaming APIs, webhook subscriptions”. The Aladdin Risk entry is added under p05-29.

#### p05-56 (FIX)

Current:
> A hosted space where developers run Python next to their Aladdin data; the SDK has a run mode for

Proposed:
> A hosted analytics platform with ready-to-use Python environments [NEW]. The SDK has a run mode for

- New source (register): [P] Aladdin® by BlackRock (Powered by Snowflake partner page). Snowflake, archived September 9, 2024. https://web.archive.org/web/20240909090246/https://www.snowflake.com/powered-by/aladdin-by-blackrock/

Why: Snowflake’s BlackRock partner page says “Aladdin Compute – a hosted analytics platform with ready to use python environments and automation tools.” No source says it runs “next to their Aladdin data”, so that phrase goes.

#### p05-48 (Developer Portal row) (CITE)

Current:
> notebooks and code samples the APIs page describes.

Proposed:
> notebooks and code samples the APIs page describes [24]. A BlackRock job posting names the “Aladdin Studio Developer Portal” [NEW].


Why: The APIs page describes the content but never says “Developer Portal”. The name comes from the job posting: “the Aladdin Studio Developer Portal”. The job posting entry is added under the Event-driven row.

#### p05-65 (FIX)

Current:
> No event specification is public [6]; the catalog, guides, notebooks and samples sit behind a client login [24].

Proposed:
> No event specification is public [6]. The APIs page describes the catalog, guides, notebooks and samples but does not link them [24]. The specifications link the guides to a portal behind a client login [6, NEW].

- New source (register): [P] Aladdin developer portal. BlackRock, checked October 20, 2026. The address redirects to the Aladdin client login. https://www.blackrock.com/apps/aladdin-developer-portal/

Why: Source 24 never mentions a login. Seventeen specs link to “apps/aladdin-developer-portal/#/guides/developer-guide” [6], and that address returns a 302 to aladdin-login.blackrock.com (rechecked October 20, 2026). That the catalog, notebooks and samples are also behind it is an inference, so the text states only what was observed.

### Page 6

#### p06-58+p06-59 (CITE)

Current:
> Ten specifications expose an endpoint for long-running operations, 35 operations are flagged as long-running, and the SDK polls them [23].

Proposed:
> Ten specifications expose an endpoint for long-running operations, and 35 operations are flagged as long-running [6]. The SDK polls them [23].


Why: Both counts are right and come from the 54 specifications in source 6: 10 specs have a /longrunningoperations/{id} endpoint and "x-aladdin-lro" appears on 35 operations. The SDK README (23) supports only the polling ("LRO Utilities to trigger and poll Long Running Operation endpoint calls"), so 23 stays on that clause alone.

#### p06-63+p06-64 (FIX)

Current:
> Every request carries an application key plus OAuth 2.0 scopes such as trading.order_management.order.v1.Order:read, and the client ID and secret come from the Studio UI [23].

Proposed:
> Every request carries an application key and a second credential. That is an OAuth 2.0 token, a client key, or a user name and password [6]. OAuth scopes look like trading.order_management.order.v1.Order:read [6]. The client ID and secret come from the Studio UI [23].


Why: Every security option in all 54 specs pairs the "VND.com.blackrock.API-Key" header with one of OAuth2 (access code or client credentials), "ClientKeyHeader" or "basicAuth" (OrderAPI/swagger.json:24-45), and the scope string appears only in those specs (source 6, :27-28). The SDK README (23) lists "`Basic Auth` / `OAuth`" with Basic Auth as the default, so OAuth is one option, and 23 stays only on the Studio UI clause.

#### p06-66+p02-14 (FIX)

Current:
> Five BlackRock speakers define Studio in the 128 recordings I pulled for this document [28, 29]; Exhibit 6 lists each

Proposed:
> I pulled about 125 recordings. Five BlackRock speakers in them describe Studio or its parts [1, 16, 26, 30, 31]. Exhibit 6 lists each


Why: Sources 28 and 29 are series index pages whose only "Studio" is navigation text, so the five recordings themselves (1, 16, 26, 30, 31) are cited instead. Goel and Miller describe parts (events, APIs, the Data Cloud) without naming Studio (Goel webinar [28:52] "via an event, via an API"; Miller transcript has 0 hits for "studio"), so "define" becomes "describe Studio or its parts". Sources 28 and 29 stay cited in the Exhibit on where recordings live, so neither is orphaned. The recording count matches page 2 (p02-14): about 125, because the two indexes overlap.

### Page 7

#### p07-01 (FIX)

Current:
> Exhibit 6. Five BlackRock executives have defined Studio on the record

Proposed:
> Exhibit 6. Five BlackRock executives describe Studio or its parts on the record


Why: Only Woodhead, Newman and Khara name Studio. Miller speaks only about the Data Cloud ("We sent flat files, we sent large schema definitions, FTP and related transfers", 0 hits for "studio") and Goel never says Studio, so the title matches the body text in p06-66.

### Page 8

#### p08-03 (FIX)

Current:
> On BlackRock’s video, Royal London’s chief executive credits

Proposed:
> On BlackRock’s video, Hans Georgeson, then chief executive of Royal London Asset Management, credits


Why: BlackRock’s page for the video (source 34) reads “A conversation with Hans Georgeson, CEO of Royal London Asset Management”. The Royal London group chief executive is Barry O’Dwyer, and Georgeson stepped down in September 2026, so “then” keeps the sentence true as of October 2026. Register entry 34 already names Georgeson with his title at recording and needs no change.

#### p08-35 (FIX)

Current:
> 2025 | Aladdin won both parts of the tender, at a price above the fund’s own estimate

Proposed:
> 2025 | BlackRock won both parts of the tender, at up to £74.0 million, against the fund’s estimate of up to £55 million [NEW]

- New source (register): [P] Contract notice 001014-2025, order management, portfolio monitoring and risk analytics system, Pension Protection Fund. UK Find a Tender, January 13, 2025. Estimated value £43 million to £55 million across both lots over ten years. https://www.find-tender.service.gov.uk/Notice/001014-2025

Why: The award notice (source 43, 6 October 2025) values the contract at “between £48,766,000 and £74,025,496” over ten years. The earlier contract notice 001014-2025 (13 January 2025) gives an estimate “between £43m and £55m across Lots 1 and 2”. The low end of the award sits inside the estimate, so the honest comparison is ceiling against ceiling, and the estimate needs its own citation. If the author takes the p08-31 alternative, the cell starts “Aladdin won”.

#### p08-40+p08-41+p08-42 (FIX)

Current:
> 2017 and 2023 | Aladdin won in 2017 and again in 2023, at an unchanged price

Proposed:
> 2017 and 2023 | BlackRock won an investment risk system contract both times, at about the same yearly price [45, NEW]

- New source (register): [P] Award 16PBGC17C5002, Investment Risk Management System (IRMS), Pension Benefit Guaranty Corporation to BlackRock Financial Management. USAspending.gov award record. Full and open competition, four offers received, signed September 28, 2017, performance September 2017 to March 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_16PBGC17C5002_1665_-NONE-_-NONE-/

Why: The two USAspending awards, 16PBGC17C5002 (signed 28 September 2017) and 16PBGC23C0006 (source 45, signed 27 March 2023), both go to BlackRock Financial Management for an “Investment Risk Management System” after full and open competition with four offers each. Neither names Aladdin. Each base year is $1,389,350.64 and each option year $1,387,500, so the yearly price is about the same, but only both records together show it.

#### p08-43 (FIX)

Current:
> Source: UK Find a Tender [43, 44]; USAspending.gov [45].

Proposed:
> Source: UK Find a Tender [43, NEW, 44]; Nest [NEW]; USAspending.gov [45, NEW]. The PPF notice gives BlackRock’s Aladdin web page as the supplier’s address [43].


Why: Source 45 covers only the 2023 PBGC award, so the 2017 award record joins it. The PPF estimate notice and Nest’s press release are now cited in the rows and belong in the note too. The PPF award record lists the supplier URL as “http://www.blackrock.com/aladdin”, which is the public link from that win to Aladdin. Its three NEW entries are listed under p08-31, p08-35 and p08-40+p08-41+p08-42. Page fit: Exhibit 9 ends just before a forced page break, and the longer rows add about two lines, so check that page 8 still fits.

### Page 9

#### p09-27 (FIX)

Current:
> Agent | 0 | Never

Proposed:
> AI agent or agentic | 0 | Never


Why: The word “agent” appears once, in Fink’s Q4 2023 remarks (“being an agent for and adapting to change”), which are not about AI. No transcript checked uses “AI agent” or “agentic”. Relabelling the row keeps the note “A zero means the term appears in no transcript” true without touching it.

### Page 10

#### p10-01 (FIX)

Current:
> BlackRock itself says growth will come from API calls, the fastest-growing measure it showed investors.

Proposed:
> BlackRock projects API calls across BlackRock and Aladdin to grow 17x by 2030, the fastest of the four volumes it showed investors [10].


Why: Slide 23 of the 2025 Investor Day deck (source 10) lists four 2030 volume estimates under “4. Continuously drive marginal costs down”: portfolios 2x, model portfolios 4x, trade allocations 1.3x and “API Calls (#) 17x”. It is a volume forecast, and the growth areas BlackRock names for Aladdin are Whole Portfolio, Wealth and Data (slides 31 to 33). Reviewer: “the four volumes” matches the page 9 sentence (p09-01).

#### p10-03+p10-04 (FIX)

Current:
> The data it is adding, private markets and Preqin, arrives through Data Cloud and Explore. Both are Studio surfaces.

Proposed:
> The private-markets data it is adding from eFront and Preqin is going into Data Cloud, which is part of Studio [16].

Also change, Page 9 body, opening sentence of the private-markets paragraph (optional, same overstatement of routes):
> The private-markets data BlackRock has been adding reaches clients through Data Cloud and Explore.
becomes
> Much of the private-markets data BlackRock has been adding reaches clients through Data Cloud and Explore.


Why: Newman, the Studio general manager (source 16), says eFront data is “coming into the Aladdin Data Cloud” and Preqin is “bringing in that data”, and calls Data Cloud “part of Studio”. No source calls Explore a Studio surface, and Preqin benchmarks also reach clients through Preqin Pro, eFront, Aladdin Wealth and APIs (BlackRock press release, July 8, 2026), so the sentence names only the Data Cloud route.

#### p10-07+p10-10+p10-13 (FIX)

Current:
> , the AI inside the login, is built on the same APIs Studio exposes. It draws on a registry of plugins, “couple of thousands agents and tools,” built by Aladdin’s engineering teams. The first way a team adds a tool is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production” [8]. So Copilot’s tools are Studio’s APIs. Microsoft’s Adrian Crockett made the dependence plain on BlackRock’s podcast: “There’s no copilot without plug-ins” [53]. On the data side, BlackRock’s AI product head says the team is making sure “the data model itself is structured for agentic use cases” [54].

Proposed:
> , the AI inside the login, calls Aladdin’s production APIs as tools. It draws on a registry of plugins, “couple of thousands agents and tools,” built by Aladdin’s engineering teams. The first way a team adds a tool is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production” [8]. Teams can also register agents of their own [8]. Studio “exposes everything Aladdin knows how to do” as APIs and events [1]. So I infer that Copilot and Studio use the same APIs. Microsoft’s Adrian Crockett made the dependence plain on BlackRock’s podcast: “There’s no copilot without plug-ins” [53]. On the data side, a BlackRock product leader says the team is making sure “the data model itself is structured for agentic use cases” [54].


Why: Rosales and Valdez (source 8) describe two ways to add a tool: “mapping one-to-one to an existing Aladdin API already out in production”, or teams registering “their own agents”. No source says these are the APIs Studio exposes, so the link rests on Woodhead (source 1, “It exposes everything Aladdin knows how to do as a set of APIs events”) and is marked as inference. In source 54 the 17:37 speaker refers to “what Pavana is speaking to”, so the quote is not Pemmaraju’s. Register entry 54 changes under s54.

#### p10-ex11-title (FIX)

Current:
> Copilot answers a question by choosing from thousands of tools and calling production Aladdin APIs

Proposed:
> Copilot answers a question by picking from about two thousand tools and agents, then calling production Aladdin APIs


Why: Consistency. Source 8 says “a couple thousands agents and tools” (6:42). Pages 2 and 13 and Exhibit 14 now say “about two thousand tools and agents”, so Exhibit 11 says the same.

#### p10-ex11-aria (FIX)

Current:
> aria-label="Funnel: one question, thousands of registered tools, 20 to 30 candidate tools,

Proposed:
> aria-label="Funnel: one question, about two thousand registered tools and agents, 20 to 30 candidate tools,


Why: Consistency with the Exhibit 11 title and Exhibit 14.

#### p10-ex11-box (FIX)

Current:
> Thousands of registered tools: a plugin registry

Proposed:
> About two thousand registered tools and agents: a plugin registry


Why: Consistency with the Exhibit 11 title. The quotation in the same box, “couple of thousands agents and tools”, supports it.

#### p10-25 (FIX)

Current:
> One answer, never investment advice: Copilot’s standing instructions (its system prompt) are tested so it will “never provide investment advice” [8], and the product page says the same [17]

Proposed:
> One answer, never investment advice: the product page says Copilot “will not give investment advice” [17]. The team tests every rule in its system prompts [8]


Why: The talk (source 8) says the team writes test cases “for every intended behavior encoded in system prompts” and gives “you must never provide investment advice” as “a very dummy example”, so it is not a quoted rule from Copilot’s actual prompt. The Aladdin Copilot page (source 17, fetched October 20, 2026) does say “Aladdin Copilot: Will not give investment advice or respond to questions outside Aladdin platform boundaries”, so the no-advice claim keeps 17.

### Page 11

#### p11-12 (FIX)

Current:
> Aladdin

Proposed:
> Aladdin, for comparison
> Aladdin


Why: Aladdin is the platform under study, which BlackRock calls “a tech platform that unifies the investment management process” (blackrock.com/aladdin), so it sits badly under “Data and cloud providers”. A separate group row fixes the label without changing any count, because the title already counts Aladdin as the ninth provider.

#### p11-35 (FIX)

Current:
> A public account of the Copilot plugin model would cover production Aladdin APIs, the same ones Studio exposes, each user’s own permissions, and tested no-advice guardrails [8, 17].

Proposed:
> A public account of the Copilot plugin model would cover the production Aladdin APIs its tools call, which user groups may use each tool, and tested no-advice guardrails [8, 17].


Why: Source 8 supports “an existing Aladdin API already out in production”, but no source says these are the APIs Studio exposes, so that phrase goes. Source 17 stays because the Copilot page says it “will not give investment advice”, which supports the no-advice guardrail. Reviewer: “each user’s own permissions” became “the user groups each tool’s owning team allows”, to match page 13 (p13-06+p13-07+p13-08+p13-09). Source 8 says teams control “which user groups have access to this” (6:51).

### Page 13

#### p13-01 (CITE)

Current:
> It sells Aladdin as the system it runs internally [8, 14, 17, 19].

Proposed:
> It sells Aladdin as the system it runs internally [8, NEW].

- New source (register): [P] BlackRock Completes Acquisition of eFront. BlackRock press release, May 10, 2019. https://www.blackrock.com/corporate/newsroom/media/press-releases/blackrock-efront-acquisition

Why: The words are true, but sources 14, 17 and 19 do not mention internal use. BlackRock’s eFront release says “Aladdin was first built to manage BlackRock’s business” and the firm offers clients “the same technology … that BlackRock uses to manage investments day-to-day”. Source 8 at 1:33 says “BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients”.

#### p13-06+p13-07+p13-08+p13-09 (FIX)

Current:
> About 100 of its applications and thousands of Copilot tools, built by 50 to 60 of its teams, call these APIs every day under each user’s permissions [8].

Proposed:
> About 100 of its applications carry Copilot. Each Copilot tool maps to a production Aladdin API. The team that owns each tool sets which user groups can use it [8].


Why: Source 8 says “around 100 Aladdin front-end applications that thousands of people use every day” (1:53) and that Copilot is “embedded across all of those hundred” (2:34). It defines a tool “as kind of mapping one-to-one to an existing Aladdin API already out in production” (4:39). Teams that onboard a plugin control “which user groups have access to this” (6:51). No source says the apps or tools call the APIs every day or under each user’s permissions. The 50 to 60 teams build tools and agents, not the apps, so that count moves to the Copilot box in Exhibit 14. Length: 29 words in place of 27, so page 13 does not grow. Page 2 uses the same facts under p02-09+p02-10.

#### p13-aria (FIX)

Current:
> aria-label="Diagram. On the left, BlackRock's own use: about 100 BlackRock applications and Copilot's thousands of tools. On the right, a client's use: its engineers behind its own gateway, its applications, and, hatched, its AI tools, on which BlackRock has published nothing beyond a job posting. All sit on one band, Aladdin's APIs, which all of them call and whose Data Cloud they read. Below, two groups: controls on every call (permissions per user, a second approver, compliance on every order) and what Copilot adds for AI (input guardrails, output guardrails, LLM judges)."

Proposed:
> aria-label="Diagram. On the left, BlackRock's own use: about 100 BlackRock applications, and Copilot with about two thousand tools and agents. On the right, a client's use: its engineers behind its own gateway, its applications, and, hatched, its AI tools, for which the nearest public sign is an internal job posting. All sit on one band, Aladdin's APIs. BlackRock's applications, Copilot and a client's code draw on Aladdin's shared services and APIs, and each client reads its own Data Cloud. Below, two groups: controls built into the APIs (access set per API, a second check on dataset releases, compliance by default) and what Copilot adds for AI (input guardrails, output guardrails, LLM judges)."


Why: The screen-reader description of Exhibit 14 must say what the fixed boxes say. One rewrite replaces the four partial rewrites drafted under p02-05+p02-06+p02-07, p02-09+p02-10 and p13-22, and carries p13-26, p13-27, p13-34+p13-35, p13-37, p13-40 and p13-47. It is not printed, so page 13 does not change length.

#### p13-26 (FIX)

Current:
> all call these APIs.

Proposed:
> draw on Aladdin’s shared services.


Why: The specifications tie only some APIs to these apps, for example RiskRuleAPI rules “as surfaced in Risk Radar” and orders “visible in the "Basket" column in Order Monitor of Aladdin Dashboard”. Source 8 says services “serve trading data to all Aladdin applications” (4:06), and source 14 speaks of “shared services”. No source says every app calls these APIs. Reviewer: three groups drafted this line differently (“all carry Copilot.”, “share these services and data.”, this one). This one matches the recommended Exhibit 14 title and the band caption, and fits the box.

#### p13-27 (FIX)

Current:
> Thousands of tools, each one an Aladdin / API, built by 50 to 60 BlackRock teams.

Proposed:
> About two thousand tools and agents, / from 50 to 60 BlackRock teams. Each / tool maps to a production Aladdin API.


Why: Source 8 says “a couple thousands agents and tools that are registered in the plug-in registry” (6:42). A tool maps “one-to-one to an existing Aladdin API already out in production” (4:39), while an agent is a separate path for “complex workflows” (4:49). There are “50 60 Aladdin engineering teams” (3:58). The box has room for a third line at y=134, and each line is no wider than the line it replaces. Reviewer: merged with the g01 draft. “Production” is kept so the box matches pages 2 and 13. The longest line is 38 characters, against 39 now.

#### p13-34+p13-35 (FIX)

Current:
> BlackRock’s applications, Copilot and a client’s own code call the same APIs and read the same Data Cloud, the client’s Aladdin data in a Snowflake account BlackRock runs for it.

Proposed:
> BlackRock’s applications, Copilot and a client’s code draw on Aladdin’s shared services and APIs. Each client reads its own Data Cloud, which BlackRock runs on Snowflake.

Also change, Exhibit 14 source line: add the Studio page and the Data Cloud launch release (both options):
> Sources: Rosales and Valdez [8], the Copilot page
becomes
> Sources: Rosales and Valdez [8], the Studio page [14], the Data Cloud launch release [NEW], the Copilot page


Why: Source 8 says services “serve trading data to all Aladdin applications” (4:06) and Copilot tools map “to an existing Aladdin API already out in production” (4:39). The Studio page (14) says “API-first approach across shared services and data”. BlackRock’s Data Cloud release says “Each Aladdin Data Cloud client receives an independent, centrally-managed data store”. No source says Copilot reads the Data Cloud. Reviewer: three groups drafted this caption. This version uses the same “shared services” wording as the Exhibit 14 title, the left box and Exhibit 3, and is 170 characters against 178 now.

#### p13-37 (FIX)

Current:
> CONTROLS ON EVERY CALL

Proposed:
> CONTROLS BUILT INTO THE APIS

Also change, Exhibit 14, first control box title:
> Permissions per user
becomes
> Access set per API

Also change, Exhibit 14, third control box title:
> Compliance on every order
becomes
> Compliance by default


Why: In the 54 public specifications, all 301 operations require an API key together with OAuth, a client key or a user name and password (source 6). OAuth scopes are set per API, which the first box’s text already says. The four-eyes check covers only dataset workflow states. Compliance applies to order posts, where OrderAPI says runCompliance “Default is true to run compliance on this post order request.”, so “every order” becomes “by default”. The first box title follows page 2 (p02-05+p02-06+p02-07).

#### p13-40 (FIX)

Current:
> Rule assignments and dataset / releases record a second / sign-off.

Proposed:
> Dataset releases need a / second check. Capital flows / record who approved them.


Why: AdcDatasetAPI says “STATE_REVIEW: In review state, dataset is ready for a 4-eyes check prior to release”. EnrichedCapitalFlowAPI records an “approverUserId” (“Approver Aladdin user Id”) and an “authorizerUserId” (source 6). The rule assignment spec has review states but no approver field, and its four-eyes flag is “By default … false”, so rule assignments leave the box. No new line is longer than the widest line now in the box (28 characters).

#### p13-47 (FIX)

Current:
> The hatched box is not: on a client’s AI tools BlackRock has published nothing beyond a job posting [60].

Proposed:
> The hatched box is not. The nearest public sign is a September 2026 posting for an internal data role that names MCP and AI agents [60].

Also change, Exhibit 14 hatched box, last two lines:
> BlackRock’s only public / word is a job posting.
becomes
> Nearest public sign: / an internal job posting.

Also change, Part 3 body. The sentence is true and stays. The posting is about an internal role, so it does not support this sentence. Recommend dropping the citation.:
> How those tools would connect is not public [60].
becomes
> How those tools would connect is not public.


Why: The posting (Workday R264906, posted September 4, 2026) asks the hire to “Implement emerging AI tooling including Model Context Protocol (MCP), AI agents, and Copilot extensions to automate repetitive onboarding tasks” with “partner engineering and data teams”. That is internal data-platform work, not client AI tools. The careers URL now returns 404, so entry 60 moves to the Saarthi copy. The new note is shorter than the old one. Register entry 60 is replaced once, under s60.

### Page 14

#### p14-02+p14-04 (FIX)

Current:
> the APIs by area with their package labels, how permissions work, how a client routes calls through its own gateway, and the Snowflake and Databricks answer, plus

Proposed:
> the APIs by area with their stability labels, how permissions work, how a client routes calls through its own gateway, and an answer on Snowflake and Databricks connectors, plus


Why: The labels belong to each specification, and one package can mix them: in asdk_plugin_trading 2.0.0b3, OrderAPI carries “x-aladdin-api-stability”: “stable” and TradeAPI carries “alpha”. The RFP question Schafer quotes is “Are you using connectors to Snowflake or to Databricks?” [9]. No public source shows a Databricks connection, so the row now names the answer to that question and asserts no connection.

#### p14-ex15-row (NO CHANGE)

Current:
> under the same permissions, compliance checks and guardrails Copilot uses


Why: This row describes a page BlackRock could publish, not a current fact. It stays consistent with the fixed Exhibit 14, which keeps permissions, compliance and Copilot’s guardrails as its two control groups.

#### p14-15 (FIX)

Current:
> I could not run anything, open the catalog, guides, notebooks or samples, or test what a client receives; where this document describes those, it relies on what sources say.

Proposed:
> I could not run anything, test what a client receives, or open the catalog and the API guides with their notebooks and code samples. Where this document describes those, it relies on what sources say.


Why: The APIs page offers notebooks and code samples “from carefully curated API guides” with no public link [24]. The SDK’s own sample code is public on GitHub (README line 226: “Sample code snippets ... are provided under resources/sample_code_snippets”), so the sentence now names only the guide material.

#### p14-18 (FIX)

Current:
> Client forums and the solutions team | the Never Done podcast [28], the Big Little Questions video series [29], Woodhead [1], Rosales and Valdez [8]

Proposed:
> The invitation-only Aladdin Client Forum and the Solutions Engineering team | the Never Done podcast [28], the Big Little Questions video series [29], Woodhead [1], Rosales and Valdez [8], Client Forum page [NEW], Solutions Engineering job posting [NEW]

- New source (register): [P] Aladdin Client Forum 2026. BlackRock Aladdin event page, as of October 20, 2026. https://www.blackrock.com/aladdin/discover/expertise/events/aladdin-client-forum-2026
- New source (register): [P] Job posting: Aladdin Client Business, Solutions Engineering, Vice President (R265631, Singapore). BlackRock Careers, posted October 2, 2026. https://careers.blackrock.com/job/singapore/aladdin-client-business-solutions-engineering-vice-president/45831/98412767088

Why: The Forum page says it “is an invitation-only event” whose attendees include “a select group of prospective clients”. BlackRock’s job posting R265631 (October 2, 2026) says the Solutions Engineering team works “to help prospective clients understand how Aladdin and eFront can address” their needs. Both fit the After qualification column and now carry receipts. The Receipt cell grows by about one line.

#### p14-24 (FIX)

Current:
> the APIs page, which promises “dozens of APIs”

Proposed:
> the APIs page, which promises “dozens of Aladdin APIs”


Why: The APIs page reads “Dozens of Aladdin APIs available – with constant new additions” [24]. The quotation now matches it word for word.

#### p14-25 (CITE)

Current:
> The Developer Portal and the API framework guides | Studio page [14], APIs page [24]

Proposed:
> The Developer Portal and the API framework guides | Studio page [14], APIs page [24], developer portal [6, NEW], job posting [NEW]


Why: The words hold, but their receipts were missing. Seventeen of the public specifications link to “apps/aladdin-developer-portal/#/guides/developer-guide” [6], and that address redirects to aladdin-login.blackrock.com (rechecked October 20, 2026, HTTP 302). A BlackRock job posting names the “Aladdin Studio Developer Portal”. Both NEW entries are already drafted by g03 (sNEW-g03-portal, sNEW-g03-job). The APIs page says “Learn about our API framework” [24].

#### p14-28 (CITE)

Current:
> The API catalog and the Data Dictionary | asdk_plugin packages [6], APIs page [24]

Proposed:
> The API catalog and the Data Dictionary | asdk_plugin packages [6], APIs page [24], developer portal [NEW]


Why: The APIs page describes the Data Dictionary (“Our Data Dictionary allows you to explore Aladdin data”) and “Dozens of Aladdin APIs available” with no public link [24]. “API catalog” is a plain description of that list. The gate itself is shown by the developer portal address, which redirects to the Aladdin client login (sNEW-g03-portal). The note now says that is the basis.

### Page 15

#### p15-08+p15-10 (FIX)

Current:
> The open-source SDK on GitHub and PyPI, with a detailed README; the plugin builder | A client host and credentials, which the SDK needs for every call | SDK README [23], PyPI history [65], plugin builder [27]
> Get help | GitHub issues and pull requests on the SDK, answered by BlackRock engineers; on the Studio page, “Book a meeting” and “Download the brochure” | Notebooks, code samples, support | Pull request 52 [38], pull request 57 [66], Studio page [14]

Proposed:
> The open-source SDK on GitHub and PyPI, with a detailed README, sample code and demo notebooks; the plugin builder | A client host and credentials, which the SDK needs for every call | SDK README [23], PyPI history [65], plugin builder [27]
> Get help | Pull requests on the SDK, reviewed and merged by a BlackRock engineer; on the Studio page, “Book a meeting” and “Download the brochure” | Jupyter notebooks and code samples from the API guides | Pull request 52 [38], pull request 57 [66], Studio page [14], APIs page [24]


Why: The SDK’s only issue (59) has no BlackRock reply. Pull requests 52 (from Janus Henderson) and 57 were both approved (“LGTM”) and merged by Vedant Naik, Lead Engineer, Aladdin Studio [38, 66, 40]. The APIs page offers “Python Jupyter Notebooks” and “code samples ... from carefully curated API guides” [24]. No public source offers support, so that word goes. The SDK’s sample snippets and two demo notebooks (SDK_Demo_template.ipynb, SDK_Demo_ADC_template.ipynb) are public in the repository [23], so the Build row now lists them. Register entry 66 changes once, under s66.

#### p14-25+p14-28 (exhibit note) (FIX)

Current:
> The After qualification column is what those sources say a client receives; I did not test it.

Proposed:
> The After qualification column is what those sources say a client receives. I could not test it, because the developer portal opens only after a client login [6, NEW].


Why: Neither BlackRock page says these resources are for clients only. The gate is observed at the developer portal address that the specifications link to, which redirects to aladdin-login.blackrock.com [6, sNEW-g03-portal]. The note now names that basis. It adds about half a line on page 15.

#### p15-43 (FIX)

Current:
> State Street | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1

Proposed:
> State Street | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1


Why: The public Development Environment page gives one complete example, in cURL, NodeJS, Python and Java, that gets a token and calls Sample Transactions ("find an example below that incorporates authentication and a successful invocation of State Street API"). Running it needs client credentials and there is no public SDK, so the score is 1, partial. Source 68 already covers it.

#### p15-54 (FIX)

Current:
> Arcesium | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0

Proposed:
> Arcesium | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 1

- New source (register): [P] Demo Center. Aquata by Arcesium, as of October 2026. https://aquata.ai/demo-center

Why: Aquata, Arcesium's platform, has a public free-trial request: "You can request a 30-day trial ... There are no sales calls required to get started." A trial request scores 1 under the Call to action definition in p15-38. Reviewer: Trial or sandbox also goes from 0 to 1. The same Aquata trial request gives the Call to action its 1, and FactSet’s trial request scores 1 in both columns (p15-97+p15-102), so the two rows now follow one rule. Arcesium totals 5 of 16.

#### p15-97+p15-102 (FIX)

Current:
> FactSet | 2 | 2 | 0 | 0 | 2 | 1 | 2 | 0

Proposed:
> FactSet | 2 | 2 | 1 | 0 | 2 | 1 | 2 | 1


Why: FactSet's developer portal invites requests for "a free trial to our APIs", and access follows a login with a corporate email or approval. That is "after sign-up or approval", so Trial or sandbox and Call to action both score 1, as Bloomberg and State Street do. Source 67 supports it.

#### p15-103+p15-104+p15-107+p15-108+p15-110 (FIX)

Current:
> MSCI | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0

Proposed:
> MSCI | 1 | 2 | 0 | 0 | 1 | 1 | 2 | 1

- New source (register): [P] MSCI Developer Community. MSCI, as of October 2026. https://developer.msci.com/
- New source (register): [P] MSCI API User Guide: how to get access to MSCI APIs on Developer Community. MSCI, PDF dated December 13, 2021. https://www.msci.com/documents/1296102/28171902/MSCI-API-Developer-Community-User+Guide.pdf
- New source (register): [P] msci.sdk, version 1.37.1. PyPI, published by MSCI, September 23, 2026. https://pypi.org/project/msci.sdk/

Why: MSCI's Developer Community is public: it has a catalog of 28 APIs ("Explore our catalog to find APIs"), public overview pages, a public SDK with example code on PyPI, and Skills and Labs sections. API definitions and notebook downloads need a login, and keys come through a "Get Access" request, so docs, sample code, community and call to action score 1 and the catalog 2. The row link moves to the portal because the old link was the AI-connector press release. Trial or sandbox and First API call stay 0 (see p15-105+p15-106). The source line drops MSCI from the access caveat under the p15-31 CITE item. Totals used in p15-119: MSCI 8, FactSet 11.

#### p15-31+p15-32+p15-52+p15-55+p15-56+p15-57+p15-58+p15-77+p15-80+p15-83+p15-85+p15-93+p15-105+p15-106 (CITE)

Current:
> Source: my test of each platform’s public pages [4, 7, 14, 57, 67, 68, 69, 70, 71], no accounts or payments, October 8, 2026. Bloomberg, Clearwater and MSCI may score lower than they deserve, because some of their pages blocked automated access.

Proposed:
> Source: my test of each platform’s public pages [2, 4, 5, 6, 7, 14, 23, 24, 57, 59, 67, 68, 69, 70, 71, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW], no accounts or payments, October 8, 2026. Bloomberg and Clearwater may score lower than they deserve, because some of their pages blocked automated access.

- New source (register): [P] Data Model Portal. SimCorp, as of October 2026. https://thesim.dev/
- New source (register): [P] Arcesium Unveils Aquata® Marketplace to Power Data Connectivity, Elevate Workflows and Accelerate AI Readiness for Institutional Investors. Arcesium press release (Business Wire), October 7, 2025. https://www.businesswire.com/news/home/20251007929556/en/
- New source (register): [P] Databricks REST API reference. Databricks, as of October 2026. https://docs.databricks.com/api/workspace/introduction
- New source (register): [P] Databricks SDK for Python, README and examples, databricks/databricks-sdk-py. GitHub, as of October 2026. https://github.com/databricks/databricks-sdk-py

Why: The scores in these cells are right, but the cited sources did not show them. Studio docs and catalog: sources 6, 23 and 24 (SDK README, PyPI plugins, APIs page). SimCorp: thesim.dev, whose content "is strictly limited and controlled by SimCorp". Arcesium marketplace: the Aquata Marketplace release ("available to users of the Aquata platform"). Snowflake and LSEG AI connectors: sources 5 and 2. Databricks: the REST API reference, the SDK README examples and source 59, which lists "Claude Code, Codex, Cursor" setups. MSCI trial and first call: the portal and user guide, where clients without keys can try APIs "only after requesting for the API Keys". MSCI leaves the access caveat because its developer portal answered plain requests.

#### p15-114 (FIX)

Current:
> deals with [67, 68, 69].

Proposed:
> deals with.


Why: The count of 10 holds. Sources 67 to 69 cover only FactSet, State Street and LSEG. Readability review: the exhibit's own source note directly above already cites every platform page tested, so the sentence drops its citation instead of repeating nine numbers.

#### p15-116 (FIX)

Current:
> It scores each on eight things a developer with no client relationship can reach: 2 where the vendor opens it before any sale, 0 where access follows a relationship.

Proposed:
> It scores each from 0 to 2 on eight things a developer with no client relationship can reach.


Why: The exhibit legend reads “2: Fully public or self-serve, 1: Partial or after sign-up or approval, 0: None or blocked”. State Street’s sandbox scores 1 behind an account (“Start here using your State Street account”), so a two-level description is wrong. Readability and layout review: the sentence now points to the three-level key printed above the table instead of restating it, which saves the lines that kept this paragraph on the exhibit's page.

### Page 16

#### p16-02 (FIX)

Current:
> The sources are BlackRock product pages, SEC filings, procurement notices, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings. BlackRock did not produce, review or endorse it.

Proposed:
> The sources are BlackRock product pages, investor presentations, SEC filings, a fund prospectus, procurement notices, press releases and job postings. They also include public code and packages on GitHub and PyPI, other vendors’ product and developer pages, blogs and trade press. The rest are transcripts of recordings and earnings calls with BlackRock speakers. BlackRock did not produce, review or endorse this analysis.


Why: The register also holds two Investor Day presentations [10, 47], the iShares V plc prospectus [18], earnings call transcripts [46, 48 to 51], blogs by Fivetran, Microsoft and BlackRock Engineering [22, 25, 40], trade press [37, 55] and other vendors’ pages [5, 59, 67 to 71]. The list now covers every kind.

#### p16-05 (FIX)

Current:
> AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted the text.

Proposed:
> AI agents pulled the pages, unpacked the packages, transcribed the recordings that had no published transcript or captions, and drafted the text.


Why: The transcript corpus README says “Published transcript or caption text was preferred; local Whisper ... was used only where neither existed”. In the register, 9 recordings are machine transcriptions and 4 use published transcripts, published captions or auto-captions.

#### p16-09 (FIX)

Current:
> each source’s grade (P, S or T), title, speaker and date.

Proposed:
> each source’s grade (P, S or T), title, publisher or speaker, and date where known.


Why: Only S entries name a speaker. P and T entries give a publisher, for example entry 2, “LSEG press release, 2025.” Entries 9, 20, 21 and 31 are undated (“Replay page undated”). Page 2 gets the same words under p02-20.

#### p16-10 (FIX)

Current:
> BlackRock and Aladdin are registered trademarks of BlackRock, Inc.

Proposed:
> BlackRock and Aladdin are trademarks of BlackRock, Inc. or its affiliates.


Why: The ALADDIN registration (US 5829287) is owned by BlackRock Finance, Inc., the renamed former parent that is now a subsidiary. BlackRock’s own Studio page uses this wording: “BLACKROCK and ALADDIN are trademarks of BlackRock, Inc. or its affiliates.”

### Page 17

#### s02 (FIX)

Current:
> LSEG announces collaboration with Anthropic. LSEG press release, 2025.

Proposed:
> LSEG and Anthropic collaborate to make more financial data accessible to Claude for Enterprise customers. LSEG press release, October 27, 2025.


Why: The cited LSEG page carries the title and H1 “LSEG and Anthropic collaborate to make more financial data accessible to Claude for Enterprise customers” and the date “October 27, 2025” (re-fetched 2026-10-20). The URL is unchanged.

#### s04 (FIX)

Current:
> MSCI unveils new AI connectors. MSCI press release, 2025.

Proposed:
> MSCI unveils new AI connectors transforming access to proprietary data. MSCI press release, February 24, 2026.


Why: The MSCI page headline is “MSCI unveils new AI connectors transforming access to proprietary data”, datelined “February 24, 2026” (re-fetched 2026-10-20). fintech.global reported the launch on February 25, 2026.

#### s09 (FIX)

Current:
> Build vs. buy: how asset managers are rethinking key decisions (webinar replay; published captions). Michael Campos, US asset manager coverage, and Alisha Sewdass, Head of Aladdin Solutions Engineering, Americas, BlackRock, with Clark Schafer, Partner, Alpha FMC. Replay page undated.

Proposed:
> Build vs. Buy: How Asset Managers Are Rethinking Key Decisions Today (webinar replay; published captions). Michael Campos, US asset manager coverage, and Alisha Sewdass, Head of Aladdin Solutions Engineering, Americas, BlackRock, with Clark Schafer, Partner, Alpha FMC. Replay page dated June 2026.

Also change, Same entry, the cue list at its end (separate span because the URL sits between).:
> Quoted at 4:37, 4:40, 14:46, 24:34, 31:56, 32:01, 39:15, 39:42, 42:22, 47:41 (Sewdass at 31:56, 32:01, 39:15 and 39:42; Schafer at 42:22).
becomes
> Quoted at 4:37, 4:40, 4:47, 24:34, 24:39, 31:56, 32:01, 39:42, 40:11, 40:20, 42:22, 50:41, 50:46, 50:49 (Sewdass at 31:56, 32:01, 39:42, 40:11 and 40:20; Schafer at 42:22).


Why: The replay page H1 reads “Build vs. Buy: How Asset Managers Are Rethinking Key Decisions Today” and the page shows “June 2026” (re-fetched 2026-10-20). The cue list is checked against the published captions: 4:37 “15%”, 4:40 “18%” and “30”, 4:47 “37%”, 24:34 and 24:39 “AI and data demands at 42%” and the tie, 31:56 and 32:01 system of record and system of work, 39:42 “modular approach”, 40:11 “very, very robust APIs”, 40:20 “secret sauce rebalancing tools”, 42:22 to 42:29 Schafer on APIs, Snowflake and RFPs, 50:41 to 50:49 poll 3. The document quotes nothing at 14:46, 39:15 or 47:41.

#### s21 (FIX)

Current:
> 21TBlackrock Aladdin Explore: Intro (an Aladdin classroom session; third-party YouTube upload; machine transcription). Uploaded by the channel “jas jas,” speaker not named, undated. https://www.youtube.com/watch?v=BahCi45_BTc Quoted at 6:26, 9:34.

Proposed:
> 21TBlackrock Aladdin Explore - Intro (an Aladdin classroom session; third-party YouTube upload; machine transcription). Uploaded by the channel “jas jas” on December 25, 2022. Speaker not named. https://www.youtube.com/watch?v=BahCi45_BTc Quoted at 9:34.


Why: YouTube oEmbed gives the title “Blackrock Aladdin Explore - Intro” and channel “jas jas”. The watch page saved on 2026-10-20 shows “Dec 25, 2022”. The document quotes only “new what-if model”, at 9:34 in the machine transcript (9:37 in YouTube’s captions). Nothing at 6:26 is quoted.

### Page 18

#### p07-16 (CITE)

Current:
> Kunal Khara, Managing Director and Global Head of Aladdin Product, BlackRock, early 2024. https://www.blackrock.com/aladdin/discover This is the hub page; the interview video is linked from it.

Proposed:
> Kunal Khara, Managing Director and Global Head of Aladdin Product, BlackRock, interviewed by Victor Anderson, WatersTechnology, February 8, 2024. https://www.waterstechnology.com/awards-rankings/7951675/bst-awards-2023-best-overall-technology-provider-for-2023-winners-interview-blackrock The video is also on the Aladdin hub page, https://www.blackrock.com/aladdin/discover.


Why: The Exhibit 6 cell actually reads "Awards interview, early 2024" next to "as a 2024 focus" in the column before it, and both are right: Khara says the themes are "where we're very, very focused in 2024" [18:59], and WatersTechnology dated the 2023 BST Awards winner's interview "2024-02-08". Only the register entry improves: it gains the exact date and the article URL instead of the hub page alone.

#### s31 (FIX)

Current:
> Jeff Miller, Managing Director, Global Head of Data Platform and Product Engineering, BlackRock, undated.

Proposed:
> Jeff Miller, Managing Director, Global Head of Data Platform and Product Engineering, BlackRock. Snowflake video, May 21, 2026.

Also change, Exhibit of BlackRock speakers, Jeff Miller row, receipt cell:
> Snowflake video, undated
becomes
> Snowflake video, May 2026


Why: YouTube oEmbed gives the channel “Snowflake Inc.”. The watch page saved on 2026-10-20 gives “publishDate” “May 21, 2026”. The job title is the one Miller gives on camera. The video description calls him “Global Head of Data Factory and Enterprise Data Platforms”, so the author may prefer to keep the spoken title.

#### s36 (FIX)

Current:
> payments for 2025. SEC EDGAR, filed April 2, 2026.

Proposed:
> payments for 2025. SEC EDGAR, filed April 6, 2026.


Why: The EDGAR filing index for accession 0000019617-26-000096 shows “Filing Date 2026-04-06” (re-fetched 2026-10-20). “20260402” is only part of the file name. The URL and the $25.6 million figure stand.

#### s40 (FIX)

Current:
> Open-sourcing the AladdinSDK: empower Python developers with a quantitative edge. BlackRock Engineering, on Medium, 2024.

Proposed:
> Open Sourcing the Aladdin SDK: Empowering Python Developers with a Quantitative Edge. Vedant Naik, Lead Engineer, Aladdin Studio, and Eli Kalish, Product Manager II, Aladdin Studio. BlackRock Engineering, on Medium, May 7, 2024.


Why: The BlackRock Engineering feed item for this URL has the title “Open Sourcing the Aladdin SDK: Empowering Python Developers with a Quantitative Edge”, pubDate “Tue, 07 May 2024”, and the byline “By: Vedant Naik, Lead Engineer, Aladdin Studio, and Eli Kalish, Product Manager II, Aladdin Studio” (re-fetched 2026-10-20). The authors are added because page 9 cites this entry for “the BlackRock engineer who co-wrote the SDK’s launch post”.

#### s54 (FIX)

Current:
> Pavan Pemmaraju, Head of AI Product and Engineering, BlackRock, July 16, 2026. https://www.blackrock.com/aladdin/discover/podcast/reducing-time-to-insight-how-ai-is-reshaping-risk-management Quoted at 10:00, 17:37. The episode also features Jess Fitzgibbon, Head of Product for Aladdin Risk. The recording does not label speakers, so this document does not attribute the 10:00 passage to either by name.

Proposed:
> Pavan Pemmaraju, Head of AI Product and Engineering, and Jess Fitzgibbon, Head of Product for Aladdin Risk, BlackRock, July 16, 2026. https://www.blackrock.com/aladdin/discover/podcast/reducing-time-to-insight-how-ai-is-reshaping-risk-management Quoted at 17:37. The recording does not label speakers, so the speaker of that passage is left unnamed.


Why: The episode page lists “Pavan Pemmaraju, Head of AI Product & Engineering, and Jess Fitzgibbon, Head of Product for Aladdin Risk”. The 17:37 speaker builds on “what Pavana is speaking to”, so that speaker is not Pemmaraju. The document quotes this episode only at 17:37 (“the data model itself is structured for agentic use cases”), so 10:00 goes.

### Page 19

#### s59 (FIX)

Current:
> Managed MCP servers, product documentation. Databricks, as of October 2026. https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp

Proposed:
> Databricks-provided MCPs, product documentation. Databricks, last updated October 16, 2026. https://docs.databricks.com/aws/en/agents/mcp-tools/built-in-mcp-services

Also change, Exhibit of AI connections by vendor, Databricks row, receipt cell:
> Databricks documentation
becomes
> Databricks documentation


Why: The old URL now returns 301 to /aws/en/agents/mcp-tools/built-in-mcp-services. That page is titled “Databricks-provided MCPs” and shows “Last updated on Oct 16, 2026” (re-fetched 2026-10-20). It says “You don’t need to host or register a server”, so the exhibit row “Databricks documents managed MCP servers” stays true. Only its link changes.

#### s60 (FIX)

Current:
> 60PJob posting: Forward Deploy Engineer, Aladdin Data, Associate (Mumbai). BlackRock Careers, as of October 2026. https://careers.blackrock.com/job/mumbai/forward-deploy-engineer-aladdin-data-associate/45831/97466309856

Proposed:
> 60PJob posting: Forward Deploy Engineer, Aladdin Data, Associate (R264906, Mumbai). BlackRock, posted September 4, 2026. Removed from BlackRock Careers by October 20, 2026. Copy kept by Saarthi. https://joinsaarthi.com/jobs/blackrock/forward-deploy-engineer-aladdin-data-associate-mumbai/46c71ea1-8135-43ac-9591-17a49139ceb6

Also change, Exhibit 12, Aladdin row, Receipt cell (the careers address now returns 404):
> BlackRock Careers
becomes
> BlackRock job posting


Why: The careers URL returns 404 (“no longer exists”) and has no archive copy. The Saarthi copy keeps the title and the line “Implement emerging AI tooling including Model Context Protocol (MCP), AI agents, and Copilot extensions”, with “datePosted” “2026-09-04” and the Workday link ending R264906. This is the same replacement g07 drafted under p13-47, so apply it once. The exhibit row and the other uses of [60] are handled in g07 p13-47. Reviewer: the Exhibit 12 receipt link pointed at the dead careers address, so it moves to the same copy.

#### s66 (finding s65)+p15-08 register (FIX)

Current:
> Pull request 57, dependency conflict with the MCP toolkit, blackrock/aladdinsdk. GitHub, merged August 2026.

Proposed:
> Pull request 57, add Pydantic v2 compatibility support, blackrock/aladdinsdk. GitHub, merged August 11, 2026.


Why: Pull request 57 is titled “add Pydantic v2 compatibility support” and was merged on August 11, 2026. Neither the PR nor its patch mentions MCP. The document cites it only as an example of a pull request BlackRock merged, so the entry gives the PR’s own title. This is the same span and text g08 drafted under p15-08+p15-10, so apply it once. The entry is now number 66.
