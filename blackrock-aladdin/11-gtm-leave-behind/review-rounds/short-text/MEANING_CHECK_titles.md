# Meaning-preservation check: short-text rewrites (A, B, C, D review files)

Checked against `titles/text.txt` (page text) and `out/Aladdin_Studio_With_AI.html` (exact wording, superscripts, links). Verdicts: **OK** (wording, order or split only; any dropped idea is verified to live where the item says, or the item adds it there), **CHANGES MEANING** (a fact, number, hedge, scope, subject, quotation or superscript changes), **DO NOT APPLY** (meaning unchanged, but the text is a diagram label that must stay as verified). "Minor" in the verdict means the change is small but real; apply the suggested fix rather than the rewrite as given.

---

## A_cover_part1.md (pages 1 to 9)

| Item | Page | Verdict | What changed | Suggested fix (keeps the readability gain) |
|---|---|---|---|---|
| A1 Part 3 contents line | 1 | OK | Wording. Note D1 proposes a different rewrite for the same line ("Six directions for this role's first six months"); pick one and apply to cover and Part 3 title together. | — |
| A2 Part 2 contents line | 1 | OK | Compression only. | — |
| A3 Stat tile 2 caption | 2 | OK | "6x its 2017 level" → "6x its 2017 payment"; same fact (25.6 / 4.4 = 5.8). | — |
| A4 Stat tile 1 caption | 2 | OK | Drops "the fastest-growing measure"; verified as the first sentence of paragraph two on page 2 ("API calls are the fastest-growing measure BlackRock showed investors"). | — |
| A5 Stat tiles source note | 2 | OK | Re-punctuated; all four multiples, the inference caveat and superscripts ^1^, ^2, 3^, ^4^ kept in place. | — |
| A6 List intro | 2 | OK | Semicolon to full stop. | — |
| A7 List item 5 | 2 | OK (minor) | "Describe the Copilot plugin model publicly" → "Publish how Copilot connects to the APIs". Same three contents, but the document's own term "plugin model" (Exhibit 17 row 5 label, Exhibit 18 row 4, Finding 3 callout) disappears from the summary, which breaks the cross-reference for a reader going from page 2 to Exhibit 17. | "Describe the Copilot plugin model publicly: which APIs its tools map to, how it is governed, and how clients' own AI tools can plug in." |
| A8 List item 6 | 2 | OK | "what is in the box" → "what the public API catalog contains"; same object. "One-page" is supported by Exhibit 17 row 6 ("One page listing the 11 API domains"). Note: conflicts with D17's carry-through for the same line, which widens the object (see D17). | — |
| A9 Method callout | 2 | OK | Punctuation only. | — |
| A10 "Receipts" heading and column header | 2, 7 | OK | Keep as is. | — |
| A11 Exhibit 1 title | 3 | OK | Drops "one engine"; verified as the body sentence above ("BlackRock sells the platform as one engine with separate entry points"). Eight rows confirmed. "Aladdin's eight named products" is loose (Aladdin is itself one of the eight; eFront is not an Aladdin-branded product) but claims nothing new. | Optional: "Exhibit 1. Of BlackRock's eight named products, Studio is the one for people who write code" |
| A12 Exhibit 1 eFront cell | 3 | CHANGES MEANING (minor) | Subject of the May 2026 addition changes. Current text attaches "private credit analytics added in May 2026" loosely; the body (page 11, "Private credit analytics on Preqin followed in May 2026^12^") and Source 12's title ("expands private credit solutions on Preqin") put the addition on Preqin. Rewrite makes eFront Insight the thing that "added" them. | "A private-fund investment platform covering due diligence through cash flows and reporting. Preqin now sits inside eFront Insight, and [private credit analytics were added on Preqin in May 2026]^12^" |
| A13 Exhibit 1 Accounting cell | 3 | OK | "the public accounting APIs" → "Its public APIs"; same referent. | — |
| A14 Exhibit 1 Provider cell | 3 | OK | "its use" → "to use it" (Aladdin Provider); matches Source 18 ("Aladdin Provider fees paid by service providers"). | — |
| A15 Exhibit 2 title | 4 | OK | Drops "name no order screen" and the item adds it to the source note (which already says "hold no position or event API"). "except positions and events" is a slightly loose rendering of "hold no position or event API" (events are not a trade step) but claims nothing new; step 4 cell confirms "None of the 54 is a position API". | Tighter: "Exhibit 2. The public APIs follow a trade from order to NAV, with no position or event API" (15 words) |
| A16 Exhibit 2 header | 4 | OK | Matches the intro sentence ("which product or application BlackRock names"). | — |
| A17 Exhibit 2 step 3 cell | 4 | CHANGES MEANING | Adds "None named." The current cell does not say that no product is named for the trade step, and nothing else in the document says so (steps 1 and 2 carry their own "name no order screen" / "no application is named" statements with ^17^; step 3 has no such statement or receipt). A new fact is being asserted. | Keep the verb fix without the new claim: "The people who lead Aladdin Accounting describe the run as going ["from that first order ... without lifting up the pencil"]^20^". If the author can confirm from the specifications that no application is named for the trade step, add "The specifications name no trading application^17^" as a second sentence. |
| A18 Exhibit 2 step 3 Who acts | 4 | OK | Punctuation; quotation and ^17^ intact. | — |
| A19 Exhibit 2 step 1 Who acts | 4 | OK | Punctuation; quotation and ^17^ intact. | — |
| A20 Exhibit 2 stability sentence (move) | 4 → 6 | OK | Sentence kept verbatim, relocated to Exhibit 5's note. Exhibit 2's cells still use "(stable)", "(alpha)", "beta", so a reader of Exhibit 2 loses the definition. | Keep in Exhibit 2's note as well, or add "(stability labels are explained under Exhibit 5)" to it. |
| A20b Step 5 "Also:" lead | 4 | OK | Adds a one-word lead; no fact changed. | — |
| A21 Exhibit 3 title | 5 | OK | Drops "the 11 public domains sit behind it" and the item adds an intro sentence or note line carrying it. "Every app" → "Apps" softens slightly; the diagram's own caption says "every app". | "Exhibit 3. Every app, Copilot and Studio call one shared API layer" (11 words) |
| A22 Exhibit 3 tile "Research sandboxes / hosted places to build" | 5 | CHANGES MEANING | Renames a diagram label from a separately verified source, and asserts an equivalence (Research sandboxes = Aladdin Compute) that no source in the document states. Exhibit 3's source note credits the Studio tiles to Woodhead at 4:49^5^, not to the SDK README. | Do not change the label. If the author wants the link made, add to the Exhibit 3 source note only after checking Woodhead 4:49: "the research sandboxes are what the SDK calls Aladdin Studio Compute sessions^23^". |
| A23 Exhibit 3 tile caption "events and files out" | 5 | DO NOT APPLY | Meaning unchanged ("send events and files out"), but it is a map label and must stay as verified. | Leave as is. |
| A24 Exhibit 3 tile caption "Snowflake, this client's own" | 5 | CHANGES MEANING | "one account per client" asserts exactly one account each; the sources say "hundreds of Snowflake accounts" (Woodhead^5^) and "this client's own", not a one-to-one count. Also a map label. | Leave as is. |
| A25 Exhibit 3 band label "THE ALADDIN PLATFORM · INSTITUTIONAL" | 5 | CHANGES MEANING | "(INSTITUTIONAL, NOT WEALTH)" adds a claim about what the diagram excludes that no source note or body sentence makes; dropping "INSTITUTIONAL" removes a qualifier. Map label. | Leave as is. If a gloss is wanted, add to the source note: "The diagram shows the institutional platform; Aladdin Wealth (Exhibit 1) is not drawn." |
| A26 Exhibit 4 title | 6 | OK | Both dropped ideas verified in the cells ("No event specification is in the public packages^17^"; "All sit behind a client login^24^") and the item repeats them, with superscripts, in the source note. Proposed intro line adds no fact. | — |
| A27 Exhibit 5 title | 6 | OK | 74 + 53 = 127 of 301 confirmed. "Only 23 of 54 stable" moved to the body sentence after the exhibit, which the item writes. "Two domains" drops the names, which the top two rows supply. | If the names matter: "Exhibit 5. Investment operations and analytics hold 127 of the 301 public API operations" (12 words) |
| A28 Exhibit 5 stability headers | 6 | OK | "the four columns count specs by label" is true (24 + 6 + 23 + 1 = 54). | — |
| A29 Exhibit 6 title | 7 | OK | "Nothing in Studio runs until a prospect is qualified" is the same strength as "cannot run anything until qualified"; the Try row says "Nothing to run". The hear / read / unpack sequence is the intro sentence on page 7. | Optional precision, since the SDK does install: "Exhibit 6. Nothing in Studio can be run against Aladdin until a prospect is qualified" |
| A30 Exhibit 6 header "Out there today" | 7 | OK | "Public today" matches the source note ("read with no account or login, October 2026"). | — |
| A31 Exhibit 6 Read cell | 7 | OK | Punctuation; all three slogans and the "dozens of APIs" quotation intact. | — |
| A32 Exhibit 7 title | 8 | OK | "gate access until a relationship exists" → "open to developers only after a relationship exists"; same claim. Second idea verified in the body ("Data and cloud platforms sell to developers directly and cluster high"). | — |
| A33 Exhibit 7 header "First call as a non-client" | 8 | OK | "without a contract" ≈ "as a non-client" (body: "a developer with no client relationship"). | Closer to the body: "First API call as a non-client" |
| A34 Exhibit 7 header "Call to action" | 8 | CHANGES MEANING | "Developer sign-up" names a scoring criterion the document does not state; the reviewer admits not knowing what was scored. A header that guesses the criterion may misdescribe the column (Bloomberg 1, State Street 1, LSEG 1 under a "sign-up" header would read as partial sign-up). | Keep "Call to action" and add one sentence to the existing score footnote, written by the author, saying what a 2, 1 and 0 mean for it. |
| A35 Exhibit 8 title | 8 | OK | "since 2024" is already the document's claim on page 2 ("Five BlackRock speakers have defined it on the record since 2024"). Note Miller's recording is undated (Source 42), so "since 2024" rests on the other four. Woodhead's November 2025 three-part definition is on pages 3 to 4 and in his row. | — |
| A36 Exhibit 8 headers | 8 | OK | "Recording" describes the cells (podcast, webinar, interview, video). | — |
| A37 Exhibit 8 Woodhead cell | 8 | CHANGES MEANING | (1) Adds a definition, "staff who code without being engineers", that no source in the document gives for "citizen developers". (2) "quoted on page 3" is wrong: the page 3 footer falls before the block quote, which sits at the top of page 4 (only its introduction is on page 3). | "Gives the three-part definition quoted at the start of Part 1. Puts BlackRock's internal citizen developers at 3,000, a figure Goel also gives" |
| A38 Exhibit 8 Khara cell | 9 | OK | "meaning" states the relation the colon implied; both quotations intact. | — |
| A39 Exhibit 8 Newman Where cell, and Exhibit 6 Hear row | 8, 7 | CHANGES MEANING (secondary suggestion only) | "Never Done podcast" is correct (Source 15). But the Exhibit 6 suggestion "the Never Done and Big Little Questions podcasts" is wrong: Source 31 is "Big Little Questions, video series page", not a podcast. | Exhibit 8 cell: apply as proposed. Exhibit 6 Hear row: "the Never Done podcast^30^ and the Big Little Questions video series^31^". |
| A40 Exhibit 9 title | 9 | OK | All four rows show Yes under APIs and events and Data Cloud. "as parts of Studio" is the body's framing ("Four of the five describe Studio with the same three parts"). "only Goel and Woodhead name developer tools" moved to the source note, which the item writes. | — |
| A41 Exhibit 9 Yes/– columns | 9 | OK | Explains Yes; adds nothing. | — |
| A-note "three parts versus six pieces" | 6 | OK (author's framing) | The proposed sentence "Woodhead's three parts break into six pieces in the public sources" is a new reconciling claim. It is consistent with the cells (APIs + events = 2 pieces; Data Cloud = 1; developer tools = Compute, SDK, Portal = 3) but is the author's inference, not a sourced fact. | Keep, or phrase as inference: "The six pieces in Exhibit 4 are how Woodhead's three parts appear in the public sources." |

**A counts:** 41 items + 1 note. OK 32 · CHANGES MEANING 8 (A12 minor, A17, A22, A24, A25, A34, A37, A39 secondary) · DO NOT APPLY 1 (A23).

---

## B_findings12.md (pages 10 to 12 top)

| Item | Page | Verdict | What changed | Suggested fix |
|---|---|---|---|---|
| B1 Finding 1 headline | 10 | OK | Drops "none of it names Studio"; verified as the first body sentence ("names no client building on Studio^13^ ... no filing that mentions Studio^44^") and repeated on page 10 ("None of this proof names Studio"). | — |
| B2 Exhibit 10 title | 10 | OK | $14.7M (2024) is a labelled bar; "2017 to 2023" and the range are in the body sentence above ("$4.4 million to $7.6 million a year from 2017 to 2023, then $14.7 million in 2024"). | — |
| B3 Exhibit 10 legend | 10 | OK | "Payment for integration services (2016 only)" restates the source note ("The grey 2016 bar is a payment for integration services"). | — |
| B4 Exhibit 10 source note | 10 | OK | "by year of payment" → "plots each payment in the year it was made"; same. Link on "In 2016 it said ..." kept. | — |
| B5 Exhibit 10 labels | 10 | OK | No change proposed. | — |
| B6 Exhibit 11 title | 10 | CHANGES MEANING | (1) "on record" claims completeness the document never makes; the body says only that public buyers "add a third kind of record". (2) "all three ... tenders" miscounts: three bodies but four awards (PPF 2025 in two lots, Nest 2023, PBGC 2017 and PBGC 2023). The current "three bodies ... Aladdin won every one" is accurate. (3) The optional note line "Each notice records how the bids were weighted or run" calls Source 53 a notice; it is an award record. | "Exhibit 11. Aladdin won every bid that three public pension bodies scored, 2017 to 2025" (14 words). Note line, if used: "Each notice or award record says how the bids were weighted or run." |
| B7 Exhibit 11 header | 10 | CHANGES MEANING (minor) | "How bids were judged" no longer describes row 3, whose cell ("Full and open competition, four bids each time") describes how the competition was run, not how bids were judged. | "Basis of award" or "Weights or process" |
| B8 Exhibit 11 weights cells | 10 | CHANGES MEANING | Adds "%". The tender notices (Sources 51, 52) are not in the corpus, so the unit is unverified; the cells currently give bare numbers as the notices were read. "Weighted" is fine, since the current header already calls them weights. | "Weights: technical 85, price 6, price sensitivity 6, contract terms 3" and "Weights: quality 70, cost 20, social value 10". Optionally in the source note: "Both sets of weights sum to 100." |
| B9 Exhibit 11 PBGC cell | 10 | CHANGES MEANING | Adds "(the standard US federal process)", a gloss no source in the document gives. The rest is a verb fix (Source 53: "four offers received"). | "Run as a full and open competition; four bids were received each time" |
| B10 Exhibit 11 PPF outcome | 10 | OK | "both lots" → "both parts of the tender"; same. | Or keep the procurement term: "Aladdin won both lots of the tender, at a price above the fund's own estimate" |
| B11 Exhibit 11 PBGC outcome | 10 | OK | "the 2023 rebid kept the same price" → "at an unchanged price"; same. | — |
| B12 Finding 1 callout, sentence 1 | 11 | CHANGES MEANING | Current: "Adoption is **growing** among client types whose records are public." Rewrite: "Aladdin adoption is **showing up** in public records." The claim of growth is dropped. Sentence 3 rewrite is OK. | "Aladdin adoption is growing among clients whose records are public." |
| B13 Finding 2 headline | 11 | OK | The two growth sources move into a new first body sentence, which the item writes; "public and private markets together" is the body's own phrase (page 11). "rarely" kept. | — |
| B14 Exhibit 12 title | 11 | OK | "citizen developer" and "agent" at 0, and Data Cloud 2 + API 1 + Copilot 1 = "about four", are table rows; the item offers the total for the source note. | — |
| B15 Exhibit 12 header | 11 | OK | "Where it came up" fits cells of dates, quotes and "Never". | — |
| B16 Exhibit 12 Data Cloud cell | 11 | CHANGES MEANING (minor) | Current "described as an add-on" is ambiguous about whether both calls described it that way; rewrite asserts "both times". The two transcripts (Sources 55, 56) are not quoted in the document, so the stronger claim is unverified. | "[Q3 2022]^55^ and [Q4 2024]^56^, where it was described as an add-on sold with Aladdin Enterprise" (keeps the subject, keeps the ambiguity, keeps both links) |
| B17 Exhibit 12 source note | 11 | OK | No change. | — |
| B18 Finding 2 callout | 12 | CHANGES MEANING (sentence 3, safer version) | Sentence 1 rewrite is OK: "extensibility and data access" was a gloss; "API calls and the whole portfolio" is the body's claim. Sentence 3, the "safer close" ("Data Cloud is part of Studio") drops the current claim that Explore is also a Studio surface, which narrows the finding and weakens the "So Studio carries the growth story" that follows. The reviewer is right that Part 1 and Exhibit 3 show Explore as an app, so the current claim is the author's inference; but removing it is a change of meaning the author must choose, not a readability edit. The first alternative in the item ("Both are parts of Studio") preserves meaning. "from eFront and Preqin" is supported (page 11, Newman^15^). | Use C1's version, which preserves the claim: "The private markets data it is adding, from eFront and Preqin, arrives through Data Cloud and Explore. Both are surfaces Studio provides. So Studio carries the growth story, whether or not BlackRock says its name." Flag the Explore-as-Studio point to the author separately. |

**B counts:** 18 items. OK 11 · CHANGES MEANING 7 (B6, B7 minor, B8, B9, B12, B16 minor, B18).

---

## C_findings34.md (pages 12 to 15)

| Item | Page | Verdict | What changed | Suggested fix |
|---|---|---|---|---|
| C1 Finding 2 callout, sentences 3 and 4 | 12 | OK | Split only; "Both are Studio surfaces" keeps the Explore claim; "whether or not" = "even when ... does not". Note B18 proposes a narrower version of the same sentence; this one preserves meaning. | — |
| C2 Finding 3 headline | 12 | OK | The rewrite is the executive summary's own sentence ("works only inside the Aladdin login, while data providers offer connectors that let outside AI tools pull their data"). Single-clause alternative also OK. | — |
| C3 Exhibit 13 title | 12 | OK | "never giving investment advice" is the last funnel box and the body ("will not give investment advice"). "registered" dropped from the title but box 2 keeps it. | — |
| C4 Funnel box 1 | 12 | OK | Wording; quotation and ^9^ intact. | — |
| C5 Funnel box 3 | 12 | OK | "in play" → "shortlisted"; both quotations and ^9^ intact. | — |
| C6 Funnel box 4 | 12 | OK | "iterates" (author's paraphrase, outside the quotation) → "loops"; the parenthetical definition dropped; quotation intact. | — |
| C7 Funnel box 5 | 12 | OK | Semicolon to "and"; both superscripts intact. | — |
| C8 Exhibit 14 title | 13 | CHANGES MEANING | "only Aladdin has no public AI announcement" claims more than the cells show and contradicts page 12: Aladdin Copilot is a public AI product ("now available to all Aladdin clients"^16^), and Aladdin Wealth's AI tool is on page 3. The exhibit is about AI access to data (connectors, MCP) for the data and cloud rows and AI features for the two rivals; the Aladdin row's "None found" is about a public connector. Also, Snowflake and Databricks rows are documented servers, not announcements. Nine rows confirmed. | "Exhibit 14. Of nine providers a Studio buyer compares, only Aladdin has not shipped or announced AI access to its data" (19 words), or "Exhibit 14. Eight providers a Studio buyer compares have AI access or features in public; Aladdin has a job advert" (18 words). The job-advert note line proposed for the source note is fine. |
| C9 Exhibit 14 headers | 13 | OK | No change. | — |
| C10 Exhibit 14 cells, SimCorp | 13 | CHANGES MEANING | "announced 2026: prebuilt AI agents ..." → "announced in 2026, **ships** prebuilt AI agents". The current cell and Source 38 ("Introducing Agent Launchpad") say announced; "ships" asserts delivery. | "Agent Launchpad, announced in 2026, is to offer prebuilt AI agents and let clients build their own on SimCorp One's data layer" |
| C10 Exhibit 14 cells, LSEG | 13 | CHANGES MEANING | Current: "A collaboration with Anthropic and an MCP server; 90 customers connected by April 2026". Rewrite: "LSEG's MCP server, announced alongside a collaboration with Anthropic, had 90 customers connected" attaches the 90 customers to the MCP server and says the two were announced together. The body (page 12) says only "LSEG had 90 customers connected by April 2026, according to a secondary summary of its results slides"; neither link is stated. | "LSEG has announced a collaboration with Anthropic and an MCP server. It had 90 customers connected by April 2026" (two sentences, both receipts unchanged) |
| C10 Exhibit 14 cells, Arcesium, FactSet, MSCI, S&P Global, Snowflake, Databricks, Aladdin | 13 | OK | Subject added, facts and dates unchanged; "has added AI features" matches Source 66 ("unveils new suite of AI features in Aquata"). | — |
| C11 Exhibit 14 source note | 13 | OK | Split; "in my sources" kept once, which still scopes both halves. | — |
| C12 Exhibit 15 title | 13 | OK | The conclusion ("Inside the login buys governance; outside the login buys discoverability on rivals' terms") is moved into the Finding 3 callout as "Inside the login, BlackRock keeps control; outside it, rivals set the terms of comparison", which the item writes. "Discoverability" survives in the For / Outside cell ("Prospects can find it"). | — |
| C13 Exhibit 15 headers | 13 | OK (minor) | "Copilot plugins on **production** APIs" → "on Aladdin APIs" drops "production", the fact Finding 3 leans on ("Copilot's tools are production Aladdin APIs"). "public" added to the outside header is implied by "outside the login". "for the buyer's own AI tools" is not in the For cell as claimed, but the Against / Inside cell has "the AI tools that buyers already run". | "Inside the login (Copilot plugins on production APIs)" |
| C14 Exhibit 15 cells, For / Inside, For / Outside, Against / Inside | 13 | OK | Sentences; every point survives ("enterprise trust" → "carries the platform's enterprise trust"; "a ready answer" → "It answers"); superscript groups unchanged. | — |
| C14 Exhibit 15 cell, Against / Outside | 13 | CHANGES MEANING (minor) | "the regulatory optics of ..." (how it would look) → "would raise a regulatory question" (a substantive issue). A hedge about appearance becomes a claim about regulation. | "Outside AI tools drawing on a platform that will not give advice would look awkward to a regulator^16^" |
| C15 Finding 3 callout, two sentences | 13 | OK | Dangling opener fixed; semicolon split. | — |
| C15 Finding 3 callout, fold of sentences 2 to 4 | 13 | OK (minor) | The fold drops "the same governed APIs Studio exposes", the Copilot-equals-Studio-APIs link, which the body states ("So Copilot's tools are Studio's APIs"). Nothing lost from the document, but the callout loses its link to Studio. | "I would describe the Copilot plugin model publicly now: production Aladdin APIs, the same ones Studio exposes, each user's own permissions, and tested no-advice guardrails^9, 16^." |
| C16 Finding 4 headline | 14 | OK | "rivals are already selling to those buyers" is the last body paragraph ("Rivals are selling to the same buyer ... SimCorp announced wins ..."^70, 71^). | — |
| C17 Exhibit 16 title | 14 | CHANGES MEANING (minor) | "the first thing they would **stop maintaining**" → "would **drop** compliance reporting first". Poll 3 asked what firms would stop maintaining in house (i.e. hand to a vendor); "drop" reads as abandoning the function. | "Exhibit 16. Webinar attendees mostly run vendor or hybrid platforms and would stop maintaining compliance reporting in house first" (17 words) |
| C18 Exhibit 16 side heads | 14 | OK | "in house" matches the body. | — |
| C19 Exhibit 16 source note | 14 | OK | Same source, said once; ^8^ kept. | — |
| C20 Pull quote | 14 | OK | No change. | — |
| C21 Finding 4 callout | 14 | OK | "the pieces in Exhibit 4" → "the Studio pieces listed in Exhibit 4"; "because" for the colon. | — |
| C22 "What would change my view" | 15 | OK | No change. | — |
| C23 "Finding 2 again" | 15 | OK | "again" dropped; the list still shows two Finding 2 lines. | — |

**C counts:** 23 items (C10 counted once, C14 and C15 once each). OK 19 · CHANGES MEANING 4 (C8, C10 SimCorp and LSEG rows, C14 Against / Outside minor, C17 minor).

---

## D_part3_sources.md (pages 15 to 20)

| Item | Page | Verdict | What changed | Suggested fix |
|---|---|---|---|---|
| D1 Part 3 title | 15 | OK | "Where the research points" is the intro's first sentence ("Part 1 and the four findings point to six likely initial directions"). Conflicts with A1's rewrite of the same line; choose one for cover and Part 3. | — |
| D2 Part 3 intro | 15 | OK | "from inside" → "from inside BlackRock"; that is what it means (page 2: "I have no internal product context"). | — |
| D3 Exhibit 17 title | 15 | OK | "each resting on a public fact" is the source note ("Receipts in the table point to the public facts each direction rests on"). | — |
| D4 Header "Why (finding)" → "Rests on" | 15 | OK | Cells "Finding 1 ... Part 1" fit. | — |
| D5 Header "How I would know it worked" | 15 | OK | "Measure of success" / "Sign it worked"; same. | — |
| D6 Row 1 Direction | 15 | OK | "starting with clients whose Aladdin relationship is already public" is the first sentence of What it involves. | — |
| D7 Row 1 What it involves | 15 | OK | Superscripts reassigned to the clients they support, and each checks out: 51 = PPF contract award notice; 3 = JPMorgan Chase proxy, payments for 2025; 50 = Janus Henderson 10-K; 45 = Royal London video. Order 51, 3, 50, 45 in the current cell matches the listing order PPF, JPMorgan, Janus Henderson, Royal London, so the reassignment is the intended one. Adding Nest^52^ and PBGC^53^ cites entries that exist and are already attached to those buyers in Exhibit 11. Rule-and-reason reorder keeps both. | — (adopt the Nest^52^, PBGC^53^ addition) |
| D8 Row 2 Direction | 15 | CHANGES MEANING (minor) | "on the API growth story" → "beside the API-call projection" narrows the object. What it involves says: agree "one measure of API use, starting from the API-call projection^1^ ... Then put Studio's name beside **that measure**", and the Measure cell says "beside the measure". The projection is the starting point, not necessarily the measure. (Page 2 already uses the narrower form, so the inconsistency is pre-existing.) | "Studio's name beside one measure of API use" |
| D9 Row 2 Owner | 15 | OK | Split; same owners and role. | — |
| D10 Row 3 Direction | 15 | OK | "the definition BlackRock's speakers already give" is the first sentence of What it involves ("the definition four speakers already give^5, 15, 26, 41^"). | — |
| D11 Row 3 Measure | 15 | OK | Verb added. | — |
| D12 Row 4 Direction | 16 | OK | "for qualified buyers" is the last sentence of What it involves. "API suite" kept. | — |
| D13 Direction column, parallel form | 15 to 16 | OK, except row 6 alternative | Noun form for row 5 is fine. In the imperative alternative, "Write a prospect-facing summary of what Studio includes" widens the object (see D17). | Imperative row 6: "Write a prospect-facing summary of the public API catalog" |
| D14 Row 4 What it involves | 16 | OK (minor) | Adds the question in words: "what is the API suite, and can we build on it?" Schafer's quotation (page 14) is "What's the API suite that you have? Are you using connectors ...", and the Finding 4 callout says buyers ask "whether they can build on the platform"; page 2 renders the question as "what is your API suite?". The composite is defensible but the second half is the author's framing, not Schafer's words. Three measures listed in parallel; fine. | Safer: "A document that answers the question Schafer says buyers now ask^8^: what is your API suite? It lists each API domain with its specification count, operation count and status, plus the Snowflake and Databricks connectors and how clients build on top. ..." |
| D15 Row 5 What it involves | 16 | OK | Split; ^65^ kept. | — |
| D16 Row 5 Owner | 16 | OK | "compliance review" → "Compliance reviews it", which the Part 3 intro states ("compliance checks the final version"). | — |
| D17 Row 6 Direction, and carry-through to page 2 and Exhibit 18 | 16, 2 | CHANGES MEANING | "what is in the box" → "what Studio includes" widens the object. The document defines the box as the public API catalog: page 2 ("summary of the public API catalog"), this row's What it involves ("One page listing the 11 API domains ... as in Exhibit 5"), and Exhibit 18 row 3, which ties what the summary may say to the Access.Internal tag on the specifications. Studio also includes the SDK, Compute, Data Cloud and the portal (Exhibit 4), which the summary does not list. Also conflicts with A8, which keeps the catalog. | "A prospect-facing summary of the public API catalog" (Exhibit 17 row 6); page 2 as in A8; Exhibit 18 row 3 right column: "What the public API catalog summary may say" (or D24's wording, which is neutral) |
| D18 Row 6 What it involves, first sentence | 16 | CHANGES MEANING (minor) | "the count and status of each" → "the specification count and status" picks one reading. Exhibit 5, which the sentence cites, carries both a specification count and an operation count per domain, and row 4 lists both. | "One page listing the 11 API domains with the specification and operation counts and status of each, as in Exhibit 5^17^, ..." |
| D19 Row 6 Measure | 16 | OK | "Number of" added; both are counts, as in row 1. | — |
| D20 h3 "What I would need from inside" | 16 | OK | As D2. | — |
| D21 Exhibit 18 title | 16 | OK | The right-hand header is "What the answer would decide". | — |
| D22 Exhibit 18 row 1 | 16 | CHANGES MEANING (minor) | "how has that changed since 2024" (a trend over 2024 to 2026) → "today, compared with 2024" (two points). The trajectory is lost. | "How many clients have active API credentials or a Data Cloud instance, and how has that number moved since 2024?" |
| D23 Exhibit 18 row 3 | 16 | CHANGES MEANING | Drops "What does the Access.Internal tag ... mean". That is a distinct open question (page 6: "a label BlackRock does not explain in public"), not answered by the yes/no half; the source note refers to "the tag", which the second half alone still covers, but the meaning question is gone. | Two sentences: "What does the Access.Internal tag on every public specification mean? Does it limit what can be described without a login?" |
| D24 Exhibit 18 row 3 right column | 16 | OK | Neutral wording; works with either D17 outcome. | — |
| D25 Exhibit 18 row 4 | 16 | CHANGES MEANING (minor) | "How will clients connect their own AI tools" (open) + "is the FDE work how they will do it" (yes/no) → only the yes/no. If the answer is no, the open question remains and the rewrite no longer asks it. | Two sentences: "How will clients connect their own AI tools to Aladdin? Is the Forward Deploy Engineer work that path?" |
| D26 Exhibit 18 row 4 right column | 16 | OK | "in full" matches row 5's two-step publication ("Publish ... now; add the client AI-tool section when ..."). | — |
| D27 Exhibit 18 source note | 16 | OK | Verb restored; ^17^, ^65^ kept. | — |
| D28 About, "grade" | 17 | OK | "(P, S or T)" already appears on page 2. | — |
| D29 Sources intro | 18 | OK | "three grades" is true. | — |
| D30 "Machine transcription" definition | 18 | CHANGES MEANING (minor) | "a local transcription" → "speech-to-text software run on the downloaded audio" drops "local", the qualifier that distinguishes the author's own run from YouTube's auto-captions and from any cloud service. | ""Machine transcription" means speech-to-text software run locally on the downloaded audio." |
| D31 Grade labels | 18 | OK | No change. | — |
| D32 Date-seen wording | 18 to 20 | OK | "page as captured" / "seen" → "as of"; the precise dates are kept where given, and "run" and "unpacked" stay. "captured" hinted at a saved copy, but no claim about a copy is made anywhere. | — |
| D33 Entry 2 | 18 | OK | Duplicate range removed; "filed 2017 to 2026" stays. | — |
| D34 Entry 17 | 18 | OK | Duplicate version removed; "version 2.0.0b3" stays in the title. | — |
| D35 Entry 5 | 19 | OK | Reordered; same date and feed. | — |
| D36 Entry 8, speakers | 19 | OK | "Replay page undated." as its own sentence. | — |
| D36 Entry 8, quoted-at list | 19 | CHANGES MEANING (conditional) | The proposed "(Campos)" attribution for 4:37, 4:40, 14:46, 24:34 and 47:41 is a fact the document does not state; the body says only "The host read out a slide". The reviewer conditions it on "if they are all Campos", so it must not be applied without checking the recording. | Apply only after verifying the speaker at each of the five timestamps; otherwise leave the list as it is. |
| D37 Entry 26 | 19 | OK | "page undated" → "(the replay page gives no date)"; same. | — |
| D38 Entry 41 | 19 | OK | Punctuation. | — |
| D39 Entry 45 | 20 | OK | "that Finding 1 refers to" is correct: page 10, "Royal London's chief executive credits Aladdin's Snowflake implementation^45^". | — |
| D40 Entry 53 | 19 | OK | Punctuation; "four offers received" kept. | — |
| D41 Entry 60 | 20 | OK | Active voice; same fact. | — |

**D counts:** 41 items. OK 32 · CHANGES MEANING 9 (D8 minor, D13 row 6 alternative, D17, D18 minor, D22 minor, D23, D25 minor, D30 minor, D36 conditional).

---

## Totals

| File | Items | OK | CHANGES MEANING | Other |
|---|---|---|---|---|
| A_cover_part1.md | 41 (+1 note) | 32 | 8 | 1 DO NOT APPLY (map label) |
| B_findings12.md | 18 | 11 | 7 | — |
| C_findings34.md | 23 | 19 | 4 | — |
| D_part3_sources.md | 41 | 32 | 9 | — |
| **All** | **123** | **94** | **28** | **1** |

Of the 28, 12 are minor (a qualifier or one reading of an ambiguity) and are fixed by the suggested wording; 16 would put a wrong or unsupported statement into the document if applied as written.

## The flags that matter most

1. **C8, Exhibit 14 title.** "only Aladdin has no public AI announcement" is false on the document's own terms: Copilot is a public AI product (page 12, ^16^). The cells compare AI access to data; say that. Use "only Aladdin has not shipped or announced AI access to its data".
2. **B6, Exhibit 11 title.** "all three public pension tenders on record" overclaims completeness ("on record") and miscounts: three bodies, four awards (PBGC won twice). Use "Aladdin won every bid that three public pension bodies scored, 2017 to 2025".
3. **B8 and B9, Exhibit 11 cells.** The "%" unit and "(the standard US federal process)" are unverified additions; the notices are not in the corpus. Use "Weights: technical 85, ..." and drop the parenthetical.
4. **B18 versus C1, Finding 2 callout.** B18's "safer close" removes the claim that Explore is a Studio surface; C1 keeps it. Removing it is an editorial decision for the author (Exhibit 3 does draw Explore as an app), not a readability edit. Apply C1's split, and raise the Explore question separately.
5. **A22, A24, A25 (and A23), Exhibit 3 labels.** Four diagram labels renamed; "Research sandboxes" is equated with Aladdin Compute on no stated source, "one account per client" and "NOT WEALTH" are new claims. The map's labels stay as verified.
6. **A17, Exhibit 2 step 3.** "None named." asserts something no cell or note states for the trade step.
7. **D17 (with D13 row 6 and the page 2 carry-through), "what is in the box".** "what Studio includes" widens the summary from the public API catalog (page 2, the row's own What it involves, Exhibit 18 row 3) to all of Studio. Use "summary of the public API catalog"; it also keeps A8 and D17 consistent.
8. **C10, Exhibit 14 SimCorp and LSEG cells.** "ships" turns an announcement into a delivery; "LSEG's MCP server ... had 90 customers connected" attaches the 90 to the MCP server, which the secondary source summary does not say.
9. **B12, Finding 1 callout.** "Adoption is growing" becomes "adoption is showing up"; the growth claim is dropped.
10. **A37, Exhibit 8 Woodhead cell.** Adds an unsourced definition of "citizen developers" and points to page 3 for a quote that sits on page 4.
11. **A34, Exhibit 7 "Call to action" header.** Renaming to "Developer sign-up" guesses the scoring criterion; keep the header and let the author add a footnote sentence.
12. **D23 and D25, Exhibit 18 questions.** Each rewrite drops one of two genuinely separate questions (what the tag means; how clients will connect). Split into two sentences instead.

Two cross-file conflicts to settle when applying: A1 versus D1 (two rewrites of the Part 3 title / cover line; either is fine, use one); A8 versus D17's carry-through (A8's "public API catalog" is the one that preserves meaning).
