# Forward references in "Aladdin Studio, learned with AI" (20 pp., as of October 19, 2026)

Read page 1 to page 20 as a first-time reader, keeping a running list of what had been defined. Text checked against `gtm/out/Aladdin_Studio_With_AI.html`; layout checked on the rendered page images (`gtm/fwd/p/pg-NN.png`). Footnote superscripts and the Sources section (pages 18 to 20) are not flagged. The cover and executive summary were judged strictly.

**Counts: HIGH 1 · MEDIUM 8 · LOW 25 · total 34.** The document is in good shape: almost every term is glossed at first use (IBOR, ABOR, MCP, Access.Internal, Aladdin Graph, bitemporal, four-eyes, system prompt), and the Finding callouts and Part 3 point backwards. The gaps cluster in the executive summary (names used before Part 1 defines them), one explicit forward cross-reference in Exhibit 2, a missing Part 2 opener, and one argument on page 13 that rests on evidence shown on page 14.

## The five that matter most

| # | Page | What | Rating | Smallest fix |
|---|------|------|--------|--------------|
| 1 | 13 | Exhibit 15 and the Finding 3 callout say the inside-the-login model "answers the RFP question about connectors" / "the RFP connector question". That buyers put a connector question in RFPs is established only by Schafer's quote on page 14 (Finding 4). | HIGH | In the callout: "answers the connector question buyers now put in RFPs (Schafer, Finding 4)". In Exhibit 15: "It answers the connector question in RFPs (Finding 4)". |
| 2 | 10 | Part 2 begins with no opener. Part 1 (p3) and Part 3 (p15) carry a "Part N" kicker and title; page 10 goes straight to "1. The public record of clients...". The cover promises "Part 2, Four findings..., Page 10", and the labels "Finding 1" to "Finding 4" (p15, p16) and "the findings in Part 2" (p17) are never attached to these numbered headings. | MEDIUM | Add the kicker "Part 2 / Four findings on BlackRock's direction and the market" above heading 1 on page 10 (the HTML already has the anchor `#f1`). Optionally head the four sections "Finding 1." to "Finding 4." |
| 3 | 2 | Direction 5, "Describe the Copilot plugin model publicly". The reader of the executive summary has not been told that Copilot answers through plugins that wrap Aladdin's production APIs; that is page 12 (Finding 3, Exhibit 13). | MEDIUM | In the paragraph above, after "works only inside the Aladdin login", add ", answering through plugins that call Aladdin's own APIs,". |
| 4 | 2 | "the new private-markets data arrives through Data Cloud and Explore". Explore is not introduced until Exhibit 2 step 1 (p4) and the map in Exhibit 3 (p5). | MEDIUM | "Data Cloud and Explore, Aladdin's portfolio-analysis app". |
| 5 | 4 | Exhibit 2's API column carries "(stable)", "(alpha)", "beta" and the source note says "The labels in brackets are each specification's stability label; Exhibit 5 explains them." An explicit forward reference the reader needs in order to read the column; Exhibit 5 is two pages on. | MEDIUM | Replace "Exhibit 5 explains them" with "alpha is the earliest, then beta, stable and sunset; Exhibit 5 counts them". |

## All flags, in page order

Kinds: (a) term, name or shorthand used before it is defined; (b) explicit cross-reference the reader must follow; (c) idea resting on a finding or number only established later. "Never" in the "first explained" column means the document never explains it.

### Page 1, cover

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| LOW | (a) | "What the research suggests for this role's first six months" (Part 3 title; repeated on p15) | Which role. The document never names it; the subtitle says only "directions for marketing it". | Never | "for a Studio marketing lead's first six months", or leave, since the recipient knows the role. |

### Page 2, executive summary

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| MEDIUM | (a) | "the new private-markets data arrives through Data Cloud and Explore" | That Explore is an Aladdin application (portfolio analysis and what-if). | p4, Exhibit 2 step 1 ("The Explore application: its 'new what-if model'"); p5, Exhibit 3 | "Data Cloud and Explore, Aladdin's portfolio-analysis app" |
| MEDIUM | (a) | "Janus Henderson's commits and 10-K" | That "commits" means code changes a Janus Henderson engineer contributed to Studio's open-source SDK. A GTM reader may not read "commits" as software. | p10, paragraph after Exhibit 10 | "Janus Henderson's code commits to Studio's SDK, and its 10-K" |
| MEDIUM | (a) | "Describe the Copilot plugin model publicly: API mapping, governance, how client AI tools plug in." | That Copilot answers by choosing plugins that map one-to-one to production Aladdin APIs. The colon list half-explains it, but "plugin model" is used as a known thing. | p12, Finding 3 text and Exhibit 13 | In paragraph 2, after "works only inside the Aladdin login", add ", answering through plugins that call Aladdin's own APIs,". |
| LOW | (a) | "the 54 API specifications inside 11 public asdk_plugin Python packages" (method box) | That asdk_plugin is the naming prefix of the SDK's add-on packages. | p5, Exhibit 4 (SDK row: "Eleven add-on packages, one per API domain"); p6, Exhibit 5 source | "inside 11 public Python add-on packages (asdk_plugin)" |
| LOW | (a) | "GitHub and PyPI" (method box; again p7, p10) | What PyPI is. | Never | "GitHub and PyPI, the Python package index" |
| LOW | (a) | "Studio is Aladdin's developer and data layer" | A one-line definition of Aladdin, which only arrives on page 3. Not a problem for the BlackRock recipient; noted because the brief asks for the summary to be judged as if read alone. | p3, first sentence of Part 1 | Optional: "Studio is the developer and data layer of Aladdin, BlackRock's investment platform". |
| LOW | (a) | "Buyers at BlackRock's own webinar want a core platform plus tools they build themselves" | The webinar's name, "Build vs. Buy", is used as a known label on p13 (Exhibit 15 source) before p14 introduces it. Naming it here fixes both places. | p14, first sentence of Finding 4 | "Buyers at BlackRock's own Build vs. Buy webinar" |

Not a forward reference, but noticed while listing terms: the summary gives Studio's "three parts" as "APIs and events, a Python SDK and Aladdin Data Cloud"; page 4 gives them as "APIs and events, the Aladdin Data Cloud on Snowflake, and developer tools"; Exhibit 1 (p3) lists four items (APIs and events, a Python SDK, Aladdin Compute, Aladdin Data Cloud). The SDK is a developer tool, so these agree in substance, but a reader tracking "the three parts" sees three different lists by page 4.

### Page 3, Part 1 opener and Exhibit 1

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| MEDIUM | (a)(c) | "BlackRock's technology services and subscription revenue was $2.0 billion in 2025, up 24 percent with Preqin" | That Preqin is a private-markets data firm BlackRock bought in 2025, so "with Preqin" means the acquisition is in the growth figure. Exhibit 1 on the same page mentions Preqin twice, also without saying what it is. | p11, Finding 2 ("BlackRock bought eFront in 2019 and Preqin in 2025") | "up 24 percent including Preqin, the private-markets data firm bought in 2025" |
| LOW | (a) | Exhibit 1, Aladdin Data Cloud row: "It is sold as an add-on to Aladdin Enterprise" (again p11, Exhibit 12 p11) | What Aladdin Enterprise is; Exhibit 1's first row is called "Aladdin", not "Aladdin Enterprise". | Never | "an add-on to Aladdin Enterprise, the full platform licence" |
| LOW | (a) | Exhibit 1, Aladdin Studio row: "APIs and events, a Python SDK, Aladdin Compute and Aladdin Data Cloud" | What Aladdin Compute is. | p5, Exhibit 4 (Aladdin Compute row) | "Aladdin Compute (hosted Python)" or leave; Exhibit 4 follows soon. |
| LOW | (a) | Exhibit 1, eFront row: "Preqin now sits inside eFront Insight" | What eFront Insight is (eFront's benchmarking module). | Never (p11 uses it again without a gloss) | "inside eFront Insight, eFront's benchmarking module" |

### Page 4, Woodhead quote and Exhibit 2

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| MEDIUM | (b) | Source note: "The labels in brackets are each specification's stability label; Exhibit 5 explains them." Column cells: "OrderAPI v1 (stable)", "ViolationAPI v1 (alpha)", "TradeAPI v2 (alpha)", "AborLotAPI v1 (alpha)", "ValuationsAPI v1, beta" | The order of the labels (alpha earliest). The note sends the reader two pages forward. | p6, Exhibit 5 source note ("alpha being the earliest") | Replace "Exhibit 5 explains them" with "alpha is the earliest, then beta, stable and sunset; Exhibit 5 counts them". |
| LOW | (a) | Source note: "Fivetran 22" and Exhibit 2 step 4 cites Fivetran for the IBOR/ABOR quotation | Who Fivetran is. | p5, Exhibit 4 (Data Cloud row: "with Fivetran moving the data") | "Fivetran, the Data Cloud's pipeline vendor 22" |

### Page 5, Exhibits 3 and 4

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| LOW | (a) | Exhibit 3 source: "Rosales and Vicente Valdez at 2:35" (again p7, Exhibit 6: "Rosales and Valdez") | Who Valdez is; he is cited by surname only. Rosales was introduced on p3. | p12, Finding 3 ("Pedro Vicente Valdez, Principal AI Engineer") | On p3, where Rosales is introduced, add "with his colleague Pedro Vicente Valdez"; or in the p5 note, "Rosales and his colleague Pedro Vicente Valdez". |
| LOW | (a) | Exhibit 4, SDK row: "generated from the specifications by BlackRock's plugin builder" (again p7, Exhibit 6 Build row: "the plugin builder") | What the plugin builder is. Also: "plugin" here means an SDK add-on package, while from p12 "plugin" means a Copilot tool; the two senses are never distinguished. | Never beyond this sentence (Source 27 is the GitHub repository) | "by BlackRock's plugin builder, a code generator on GitHub" |
| LOW | (c) | Exhibit 3 hosting strip: "AWS option, H2 2026" (hatched) | Why AWS is hatched. The legend ("hatched = announced, not live") covers it; the announcement itself is on p11. | p11, last sentence of Finding 2 | None needed; legend suffices. |

### Page 6, Exhibit 5 and SDK paragraph

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| LOW | (a) | Exhibit 5 source: "the 54 Swagger 2.0 specifications" | What Swagger is. | Never | "the 54 Swagger 2.0 specifications (a standard API description format)" |
| LOW | (a) | "the client ID and secret come from the Studio UI" (again p7, Exhibit 6 Try row: "registered via Studio UI") | What the Studio UI is; nothing earlier mentions a Studio web console. | Never (the phrase is the README's) | "the Studio UI, the client-facing web console" |

### Page 7, Exhibits 6 and 7

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| LOW | (a) | Exhibit 6, Get help receipts: "Pull request 52 32, pull request 57 29" | What these two pull requests are. p6 described PR 57's content (the MCP-toolkit conflict fix) without its number; PR 52 (Janus Henderson's URL rewriting) is on p10. | p6 (content of 57), p10 (content of 52) | None needed; receipts are for lookup. Optionally "Janus Henderson's pull request 52". |
| LOW | (b) | Exhibit 7 (table starts p7, ends p8) appears before the paragraph that explains it on p8: "It scores each on eight things a developer with no client relationship can reach, from 0 to 2. The total sums the eight scores, so it runs from 0 to 16... So the total measures each vendor's selling model." | What the total means. The 2/1/0 legend on p7 carries most of it. | p8, paragraph after the exhibit | Move that paragraph above the Exhibit 7 heading, between Exhibit 6 and Exhibit 7. |

### Page 8, Exhibit 8

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| MEDIUM | (a) | Exhibit 8, Woodhead row: "Puts BlackRock's internal citizen developers at 3,000, a figure Goel also gives" | What a citizen developer is. The term recurs as a searched term in Exhibit 12 (p11) and is never glossed. | Never | "internal citizen developers (staff outside engineering who write code) at 3,000" |

### Page 9: no flags.

### Page 10, Finding 1

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| MEDIUM | (a) | Heading "1. The public record of clients using Aladdin can serve as Studio's proof", with no "Part 2" kicker above it (compare p3 "Part 1" and p15 "Part 3") | That Part 2 has begun and that sections 1 to 4 are "the four findings" referred to as "Finding 1" to "Finding 4" on p15 and p16, "Findings 1 to 4" (p16) and "the findings in Part 2" (p17). | Cover (promise only); the label "Finding" first appears on p15 | Add the kicker "Part 2 / Four findings on BlackRock's direction and the market" above heading 1. Optionally head the sections "Finding 1." to "Finding 4." |
| LOW | (a) | "The BlackRock engineer who co-wrote the SDK's launch post merged them." | That the SDK had a launch blog post. | Never (Source 47 to 49 presumably) | "the SDK's 2024 launch blog post" |
| LOW | (a) | Exhibit 11: "US Pension Benefit Guaranty Corporation" | Nothing here, but p15 refers to it as "PBGC" without the acronym ever being given. | Never | Add "(PBGC)" after the name in Exhibit 11. |

### Page 11, Finding 2

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| LOW | (a) | "designed with BlackRock's own professionals and 'our new colleagues from HPS'" | Who HPS is (the private credit manager BlackRock acquired). | Never | "'our new colleagues from HPS'," followed by "the private credit manager BlackRock acquired". |
| LOW | (a) | "covering commitments, fundings, paydowns and PIK" | What PIK is. | Never | "PIK (payment-in-kind)" |
| LOW | (a) | Exhibit 12 rows "Citizen developer" and "Agent" | Why these two terms were searched; "Agent" means AI agent. | Citizen developer: never; Agent: implied by Finding 3 (p12) | "Agent (AI agent)"; citizen developer gloss on p8 covers the other. |

### Page 12, Finding 3 and Exhibit 13: no forward references.

Noticed, not a forward reference: the Finding 2 callout at the top of p12 says "arrives through Data Cloud and Explore. Both are Studio surfaces", but Exhibit 3 (p5) draws Explore as one of the 100 apps, outside the Studio box. Exhibit 13 uses "GPT-4 function calling" without a gloss (LOW jargon, never explained).

### Page 13, Exhibits 14 and 15, Finding 3 callout

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| HIGH | (c) | Callout: "That description, in BlackRock's own words, answers the RFP connector question better than an MCP server with a partial catalog would." | That buyers now ask in RFPs about the API suite and connectors to Snowflake or Databricks. The executive summary mentions "the question buyers now ask: what is your API suite?" but not connectors; the connector evidence is Schafer's quote on p14. The callout's central claim rests on it. | p14, Schafer quotation and Finding 4 | "answers the connector question buyers now put in RFPs (Schafer, Finding 4) better than..." |
| MEDIUM | (c) | Exhibit 15, Outside the login, For: "It answers the RFP question about connectors." | Same as above. | p14 | "It answers the connector question in RFPs (Finding 4)." |
| LOW | (a) | Exhibit 15 source: "the provider announcements in Exhibit 14 and the Build vs. Buy webinar 8" | That "Build vs. Buy" is the name of "BlackRock's own webinar" from p2. | p14, first sentence of Finding 4 | Name the webinar on p2 (see page 2 flags); nothing then needs changing here. |
| LOW | (a) | Exhibit 14, Arcesium row: "Arcesium added AI features to Aquata" | What Aquata is. | Never | "to Aquata, its data platform," |

### Page 14, Finding 4: no flags.

### Page 15, "What would change my view" and Part 3

| Rating | Kind | Exact text | What the reader needs | First explained | Smallest fix |
|---|---|---|---|---|---|
| LOW | (a) | "Finding 1, if BlackRock published..." through "Finding 4, if..." and Exhibit 17's "Rests on: Finding 1" | That these labels mean the numbered sections 1 to 4 on pages 10 to 14. Readable by inference; the root cause is the missing Part 2 opener on p10. | p10 (by inference) | Fix on p10 (see above). |
| LOW | (a) | Exhibit 17, named proof row: "the Pension Protection Fund 51, Nest 52, PBGC 53" | What PBGC stands for. | p10, Exhibit 11 gives the full name without the acronym | Add "(PBGC)" in Exhibit 11, p10. |

### Page 16, Exhibits 17 and 18: no forward references.

Noticed, not a forward reference: the RFP-ready answer row says the document "lists each API domain ... plus the Snowflake and Databricks connectors". The document establishes Data Cloud on Snowflake (p3, p5) but nowhere establishes an Aladdin connector to Databricks; Databricks appears only in Schafer's question (p14) and as a rival in Exhibits 7 and 14. A reader may take the row as asserting that a Databricks connector exists.

### Page 17, About this document: no flags. Pages 18 to 20, Sources: not reviewed for forward references by design.

## Summary of fixes, grouped by the edit that clears the most flags

1. Page 10: add the "Part 2 / Four findings..." kicker (clears the p10 MEDIUM and the p15 LOW on "Finding N").
2. Page 2: three glosses in the executive summary (Explore; code commits; plugins that call Aladdin's own APIs) and naming the "Build vs. Buy" webinar (clears three MEDIUM and two LOW, including the p13 source-note LOW).
3. Page 13: one gloss in the callout and one in Exhibit 15 pointing to Finding 4 (clears the HIGH and one MEDIUM).
4. Page 4: rewrite the Exhibit 2 note so it states the label order instead of deferring to Exhibit 5 (clears one MEDIUM).
5. Page 3: "including Preqin, the private-markets data firm bought in 2025" (clears one MEDIUM).
6. Page 8: gloss "citizen developers" (clears one MEDIUM).
7. One-word or parenthetical glosses for the LOWs: PyPI, Aladdin Enterprise, eFront Insight, Fivetran, Vicente Valdez (introduce on p3 beside Rosales), plugin builder, Swagger, Studio UI, launch post, PBGC, HPS, PIK, Aquata; and move the Exhibit 7 explanatory paragraph above the exhibit.
