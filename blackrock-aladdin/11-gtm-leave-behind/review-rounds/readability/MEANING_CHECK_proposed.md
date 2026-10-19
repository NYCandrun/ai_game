# Meaning-preservation check of the six readability reports

Scope: every numbered item and every proposed exhibit title in `01_cover_summary.md` to `06_finding4_part3_back.md`, compared against the current text in `review4/text.txt`. Verdicts: **OK** (wording, order or splitting only; glosses that repeat a fact the document states elsewhere are OK and the source page is named), **CHANGES MEANING** (a fact added, dropped, narrowed, widened, re-hedged, re-attributed, a receipt moved, or a title that claims more than the cells show), **OK (option flagged)** (the main rewrite is fine but an optional addition the report offers would change meaning). "(minor)" marks a change a reader could reasonably accept but that the author should decide on. Exhibit arithmetic was checked against the cells.

## Report 01: cover and executive summary (pages 1 and 2)

| Report | Item | Page | Verdict | What changed | Suggested fix that keeps the readability gain |
|---|---|---|---|---|---|
| 01 | 1.1 | 1 | OK | Three title options; option 3 ("as the public record shows it") drops the "with AI" method claim from the title (the cover footer still carries it) | Prefer option 1 or 2 if the method should stay in the title |
| 01 | 1.2 | 1 | OK | Wording only | |
| 01 | 1.3 | 1 | CHANGES MEANING (minor) | Optional card text narrows "BlackRock's direction and market" to "where BlackRock is heading and what buyers want"; Findings 3 and 4 also cover data providers and rivals, which are "market" but not "buyers" | "Four findings on where BlackRock is heading and what the market is doing" or leave the card as is |
| 01 | 1.4 | 1 | OK | No change proposed | |
| 01 | 2.1 | 2 | OK | "inside the enterprise selling model" becomes "none of them changes how Aladdin is sold"; page 3 defines the selling model as how Aladdin is sold, and page 14 says each win works inside it | |
| 01 | 2.2 | 2 | OK | Adds "BlackRock's" before "2025 Investor Day slide"; the source note already attributes the slide | |
| 01 | 2.3 | 2 | OK | Supplies "what it paid in"; same numbers | |
| 01 | 2.4 | 2 | OK | Optional reword, same fact | |
| 01 | 2.5 | 2 | OK | Adds "left to right"; checked: tile 1 = source 1, tile 2 = sources 2 and 3, tile 3 = source 4, so the mapping is correct; the caveat stays with source 1 | |
| 01 | 2.6 | 2 | OK | Gloss "a managed data service on Snowflake" is Exhibit 1's own wording (page 3); superscript 5 stays on the five-speakers claim | |
| 01 | 2.7 | 2 | OK | Adds "BlackRock's client video" (page 9 says so) and "though not Studio by name" (the lede says so) | |
| 01 | 2.8 | 2 | OK | "that" becomes "all of this"; the sources listed (54 specifications, 128 recordings) are the whole evidence base, so the wider reading is the one the sentence supports | If only the proof list was meant, write "that proof" |
| 01 | 2.9 | 2 | OK (option flagged) | Main rewrite keeps the inference caveat. The option "this sentence can drop the second half" would remove the inference caveat from the body paragraph and leave it only in a source note | Keep at least "that they run through Studio is my inference" in the body |
| 01 | 2.10 | 2 | CHANGES MEANING | Superscript 6 (the private-markets webinar) now closes a sentence whose last clause is "which are Studio's surfaces", an author claim the webinar does not make; the original put 6 after "Data Cloud and Explore". The added clause itself is on page 10 (direction box) | "The new private-markets data arrives through Data Cloud and Explore⁶, both of which are Studio's surfaces." |
| 01 | 2.11 | 2 | CHANGES MEANING (minor) | "market connectors" becomes "sell connectors"; Exhibit 14 shows documented MCP servers and press releases, not prices, so "sell" asserts a commercial model the page does not | "they offer connectors that let outside AI tools pull their data⁷" |
| 01 | 2.12 | 2 | OK | "rivals" becomes "rival platforms", "that" becomes "that demand"; page 13 supports both | |
| 01 | 2.13 win 1 | 2 | OK | "starting with" matches Exhibit 17 row 1 ("starting where the relationship is already public") | |
| 01 | 2.13 win 2 | 2 | OK | Adds "17x", which is on the page | |
| 01 | 2.13 win 3 | 2 | OK | Wording; the 4-vs-5 speakers inconsistency is correctly left to the author | |
| 01 | 2.13 win 4 | 2 | OK | Supplies the question "what is your API suite?"; that is Schafer's quoted question (page 13) and Exhibit 17 row 4's title | |
| 01 | 2.13 win 5 | 2 | CHANGES MEANING | "A published description of the Copilot plugin model" becomes "how Copilot's plugins map to Aladdin's APIs"; Exhibit 17 row 5 says the page covers the API mapping, what governance applies, and how clients will connect their own AI tools. Scope narrowed to one of three | "Publish a description of the Copilot plugin model: how its tools map to Aladdin's APIs and what governs them." |
| 01 | 2.13 win 6 | 2 | CHANGES MEANING (minor) | "A prospect-facing summary" becomes "Publish a ... summary"; Exhibit 17 row 6 says "shared before the first meeting or on the Studio page", so publication is one of two options | "Write a prospect-facing 'what is in the box' summary of the public API catalog." |
| 01 | 2.14 | 2 | OK | Glosses "Python packages" (page 6: PyPI) and "every fact against its document" (back page: "each claim against the document or recording it cites") | |
| 01 | 2.15 | 2 | CHANGES MEANING (minor) | "the register marks which" becomes "marks which quotes come from machine transcripts"; the register marks recordings (entries), not individual quotes | "...the Source register marks which recordings are machine-transcribed." |
| 01 | 2.16 | 2 | OK | Split only | |
| 01 | 2.17 | 2 | OK | Adds "on page 15" (the register starts on page 15) and "(P, S or T, below)"; "begins" matches the register intro | |
| 01 | 2.18 | 2 | CHANGES MEANING | P grade narrowed: "a filing" to "an SEC filing" (entry 18 is an iShares prospectus, not an SEC filing), "a page" to "a BlackRock web page" (entries 22, 32 to 36, 58, 61, 68, 69 are third-party pages and documentation; 7, 39, 63, 66, 67, 70 are third-party press releases). T grade redefined: "a secondary summary" becomes "a summary written by someone other than BlackRock", which would also cover LSEG's own slides; the register's T summary (62) is a third party's summary of a primary source | P: "a filing, an API specification, a web page or press release, a procurement notice, or code on GitHub or PyPI". T: "trade press, or a third party's summary of a primary source" |
| 01 | 2.19 | 2 | OK | No change | |
| 01 | Exhibit: tile row | 2 | CHANGES MEANING (minor) | Proposed title says "its proof of use is paying clients"; the tile shows one client (JPMorgan Chase). "Growth story is API calls" is page 10's heading, acceptable | "BlackRock's growth story is API calls and a client pays it millions for Aladdin, but Studio's name appears in neither" |
| 01 | Exhibit: method box | 2 | OK | Restates the box | |
| 01 | Exhibit: receipts key | 2 | OK | Restates the key | |

Report 01: 31 rows. OK 22, OK (option flagged) 1, CHANGES MEANING 8 (of which 5 minor).

## Report 02: Part 1 (pages 3 to 8, Exhibits 1 to 9)

| Report | Item | Page | Verdict | What changed | Suggested fix that keeps the readability gain |
|---|---|---|---|---|---|
| 02 | 3.1 | 3 | CHANGES MEANING (minor) | "the organization" becomes "The Aladdin organization"; the page does not say which organization the 7,000 figure covers (author to confirm against source 9) | Keep "The organization is ..." as its own sentence, or confirm against the talk |
| 02 | 3.2 | 3 | CHANGES MEANING | "up 24 percent with Preqin" becomes "the figure includes Preqin"; the current text is ambiguous between "including Preqin" and "driven by Preqin", and the rewrite picks one (report marks it author to confirm) | Confirm against the 10-K (source 10); until then keep "with Preqin" |
| 02 | 3.3 | 3 | OK | Splits; "Part 1 covers" names the referent | |
| 02 | 3.4 | 3 | OK | "with Morgan Stanley first" becomes "as the first client"; register entry 11 is the Morgan Stanley launch release | |
| 02 | 3.5 | 3 | OK | Quotation intact; "names three users" matches the three quoted roles | |
| 02 | 3.6 | 3 | OK | Split only; receipts 14 and 15 stay on their facts | |
| 02 | 3.7 | 3 | OK | Adds "of Studio", which is the paragraph's subject | |
| 02 | 4.1 | 4 | OK | Bridge names the three parts from the quotation; Exhibit 9 lists the same three. "54 public API specifications" is Exhibit 5's count | |
| 02 | 4.2 | 4 | OK | "The Explore application"; register 21 and page 10 treat Explore as an application | |
| 02 | 4.3 | 4 | OK (option flagged) | Cell rewrite is fine. The suggested source-note clause "alpha, beta and stable are the maturity labels each specification carries" is a new fact (report marks author to confirm) | Add only after confirming the labels come from the specification files |
| 02 | 4.4 | 4 | OK | "No one" is what "Automatic" means in a Who-acts column; "because runCompliance is on by default" matches page 6 ("runCompliance, which defaults to true") | |
| 02 | 4.5 | 4 | OK | Split only | |
| 02 | 4.6 | 4 | OK | "Aladdin Accounting's leads" becomes "the people who lead Aladdin Accounting", same claim | |
| 02 | 4.7 | 4 | OK | Split only | |
| 02 | 4.8 | 4 | OK | IBOR expansion comes from the Named column of the same row | |
| 02 | 4.9 | 4 | OK | "only as fields" follows from "No position API among the 54" | |
| 02 | 4.10 | 4 | OK | Supplies "the accounting team" as the speaker; register 20 names two Aladdin Accounting speakers | |
| 02 | 4.11 | 4 | OK | "portfolio-configuration specification" is Exhibit 5's PortfolioConfiguration in the Accounting domain | |
| 02 | 4.12 | 4 | OK | Split only | |
| 02 | 4.13 | 4 | CHANGES MEANING | Adds "the sequence shown is mine" (report marks author to confirm); the current note only says the specifications do not order steps 4 to 6 | Stop after "do not say in what sequence steps 4 to 6 happen" unless the author confirms the ordering is theirs |
| 02 | 5.1 | 5 | OK | "tagged" and "(see Exhibit 4)"; Exhibit 4 explains the agraph id | |
| 02 | 5.2 | 5 | OK | Same gloss as Exhibit 4 | |
| 02 | 5.3 | 5 | OK | ADC expanded; Exhibit 5's Platform row has AdcDataset | |
| 02 | 5.4 | 5 | OK | Reorder only | |
| 02 | 5.5 | 5 | OK | "latency 'within 15 minutes'" becomes "data arrives 'within 15 minutes'"; standard meaning of latency for a data store, report flags for confirmation anyway | |
| 02 | 5.6 | 5 | OK | "a tool BlackRock publishes called the plugin builder": register 26 is github.com/blackrock/aladdinsdk-plugin-builder | |
| 02 | 5.7 | 5 | CHANGES MEANING (minor) | "five alpha APIs" becomes "all still labelled alpha"; "still" implies an expected progression the page does not state | "A domain of five APIs, all labelled alpha." |
| 02 | 5.8 | 5 | CHANGES MEANING (minor) | "little public detail" (about the Excel add-in) becomes "gives little detail on either", extending the claim to Aladdin Data eXchange | "...alongside Aladdin Data eXchange for bulk delivery, and gives little detail on the add-in 23." |
| 02 | 6.1 | 6 | CHANGES MEANING | Adds "Alpha, beta, stable and sunset are the maturity labels each specification carries" to the Exhibit 5 source note; not stated on the page (report marks author to confirm) | Confirm against the specification files first; the existing "Counts are mine, recomputed from the files" implies it but does not say it |
| 02 | 6.2 | 6 | CHANGES MEANING | (a) Adds a closing conclusion, "Each of these is a feature of a controlled production system for an existing client, not of a product a stranger can try" (marked author to confirm); the page's nearest statement is about the SDK, not the specifications. (b) Adds glosses for "bitemporal" and "four-eyes approval"; generic definitions, but "before a change takes effect" asserts how the approval works in Aladdin | Keep the split and the long-running-operations rewording; drop the conclusion unless the author adopts it; keep glosses as "fields that record two time dimensions" and "a second sign-off" without "before a change takes effect" |
| 02 | 6.3 | 6 | OK | "what is public today" for "what is out there"; same column meaning | |
| 02 | 6.4 | 6 | CHANGES MEANING (minor) | (a) "These are the needs of a client's engineering team" gains "not of a prospect"; stated contrast, not on the page (report offers to drop it). (b) MCP gloss "the standard that lets outside AI tools call a vendor's APIs" differs from the page's own definition on page 11 ("the common standard AI assistants use to pull data from other systems"). (c) "An outside contributor's fix for the conflict" is confirmed: register entry 28 is "Pull request 57, dependency conflict with the MCP toolkit", so no confirmation needed | Drop "not of a prospect"; use the page-11 wording for the MCP gloss |
| 02 | 7.1 | 7 | CHANGES MEANING | "whose three sections are" asserts the quoted phrases are the Studio page's section headings (report marks author to confirm) | "The Studio page, with the headings 'Create & automate,' ..." only after confirming; otherwise keep the quoted list |
| 02 | 7.2 | 7 | OK | "only by unpacking" follows from Exhibit 4 (catalog sits behind a client login) | |
| 02 | 7.3 | 7 | OK | List made parallel | |
| 02 | 7.4 | 7 | OK | Same content | |
| 02 | 7.5 | 7 | OK | "on the Studio page, two buttons"; the Receipt column cites the Studio page 13 | |
| 02 | 7.6 | 7 | OK | Corrects "the right-hand column" (which is Receipt) to "the After qualification column"; the current note appears to be an error, and the rewrite matches what the column holds. Author should confirm | |
| 02 | 7.7 | 7 | CHANGES MEANING | Header "Call to action" becomes "Developer call to action" or "Next step offered to developers", and the proposed legend line defines the criterion ("a public next step for a developer, such as a sign-up or a get-started button"); neither definition is on the page (report marks author to confirm) | Confirm the criterion used in the October 8 test before changing the header or adding the legend |
| 02 | 7.8 | 7 | OK | Reorder only | |
| 02 | 7.9 | 7 | OK | "underrated" restated as "score lower than they deserve" | |
| 02 | 8.1 | 8 | OK | Rewrite replaces "counts how many of the eight criteria" with a 0-to-2-per-criterion sum, max 16; checked against Exhibit 7 (Snowflake and Databricks total 16), so the rewrite corrects the current text rather than changing a supported fact. Receipts 32, 33, 34 and 24 stay on their facts | |
| 02 | 8.2 | 8 | OK | Receipts 29, 30 (the two series pages) move from the end of the sentence to "I pulled 128 recordings"; the series pages are where the recordings come from, so the anchor fits. Author to glance | |
| 02 | 8.3 | 8 | OK | Header clarified | |
| 02 | 8.4 | 8 | CHANGES MEANING | Puts "citizen developers" in quotation marks as Woodhead's phrase (report marks author to confirm); the alternative "3,000 non-engineers inside BlackRock who build on Studio" adds "non-engineers" and "build on Studio", neither on the page. Note also: register entry 25 (Goel) says "the 3,000 figure is given at 35:23", while Exhibit 8 credits the figure to Woodhead; the author should check which speaker gives it | "The three-part definition quoted on page 4; 3,000 internal citizen developers" (no quotation marks) until confirmed |
| 02 | 8.5 | 8 | OK | Names the register and its location (pages 15 to 17) | |
| 02 | 8.6 | 8 | CHANGES MEANING | Adds "What it lacks is reach", a new characterization (report offers to drop it); "consistent" becomes "the same", slightly stronger | Drop "What it lacks is reach"; "The message is consistent across speakers and years, so BlackRock already has a positioning for Studio. Learning about it from outside takes effort." |
| 02 | 8.7 | 8 | OK | Terminology only | |
| 02 | 8.8 | 8 | CHANGES MEANING | The "No" option changes "–" (speaker does not name developer tools) into a claim the speaker says there are none | Use the report's second option: add "– means the speaker does not name that part" to the source note |
| 02 | Exhibit 1 title | 3 | OK | Eight rows counted; "Studio is the entry point for people who write code" is page 3's sentence | |
| 02 | Exhibit 2 title | 4 | OK | "name no order screen" (step 1) and "hold no position or event API" (source note) are on the page. "cover a trade from order to NAV" is loose given step 4 has no position API | Consider "trace a trade from order to NAV" |
| 02 | Exhibit 3 title | 5 | OK | Restates the diagram's layers | |
| 02 | Exhibit 4 title | 5 | OK | Last row says all those items sit behind a client login | |
| 02 | Exhibit 5 title | 6 | OK | Checked: 74 + 53 = 127 of 301; Stable column 2+8+4+3+2+1+1+1+1 = 23, matching the Total row | |
| 02 | Exhibit 6 title | 7 | OK | "cannot run anything until qualified" is the Try row ("Nothing to run") | |
| 02 | Exhibit 7 title | 7 | OK | Checked: Studio 4, State Street 4, Bloomberg 5, MSCI 2, FactSet 9, LSEG 12, Snowflake and Databricks 16 | |
| 02 | Exhibit 8 title | 8 | CHANGES MEANING (minor) | "gave the fullest definition" is an evaluation the page does not make (Exhibit 9 shows Goel and Woodhead both naming all three parts); "since early 2024" is fine for the four dated rows but Miller's video is undated | "Five BlackRock executives have defined Studio on the record, and the head of Studio engineering gave the three-part definition in November 2025" |
| 02 | Exhibit 9 title | 8 | OK | Checked against the Yes/– cells | |

Report 02: 58 rows. OK 43, OK (option flagged) 1, CHANGES MEANING 14 (of which 5 minor).

## Report 03: Finding 1 (page 9, Exhibits 10 and 11)

| Report | Item | Page | Verdict | What changed | Suggested fix that keeps the readability gain |
|---|---|---|---|---|---|
| 03 | 1 | 9 | CHANGES MEANING (minor) | Heading's "it is viable" becomes "it works as Studio proof", a stronger claim than the body's hedged "matters less than it looks" | "...and it can serve as Studio proof even though none of it names Studio" |
| 03 | 2 | 9 | OK | Pronoun resolved; receipts 13 and 43 stay in place | |
| 03 | 3 | 9 | OK | Wording only | |
| 03 | 4 | 9 | CHANGES MEANING | Adds "the Aladdin data cloud that runs on Snowflake" as the referent of "the Snowflake implementation"; register entry 44 says only "the Snowflake passage referred to begins at 5:21", so the page does not establish that the video is about Data Cloud (report says check source 44) | Use the report's minimum fix, "credits Aladdin's _Snowflake implementation_ [44]", unless source 44 confirms the Data Cloud reading |
| 03 | 5 | 9 | OK | "proxy statement" becomes "proxy statements", matching the Exhibit 10 source note (filed 2017 to 2026); "jumped" is supported by 7.6 to 14.7 | |
| 03 | 6 | 9 | CHANGES MEANING | Proposed source-note sentence says the grey 2016 bar is "not a payment for Aladdin"; the exhibit title counts it among "payments to BlackRock for Aladdin" and the legend says only "Integration services", so the page does not say what the integration was for | "The grey 2016 bar is a payment for integration services; the figures in the text start with 2017." |
| 03 | 7 | 9 | OK | Split; "That 2016 report" resolves "that report"; receipt 45 stays on the 2016 claim | |
| 03 | 8 | 9 | OK | Split; "name a janushenderson.com address as the author" restates "author line"; receipts 31, 46, 47, 48 stay at the end | |
| 03 | 9 | 9 | OK | Reorder only | |
| 03 | 10 | 9 | OK | "show how each bid for Aladdin was scored"; "each" slightly overreaches since the PBGC row shows the competition format rather than weights | Drop "each": "show how the bids for Aladdin were scored" |
| 03 | 11 | 9 | OK | Adds "%" to the weights; checked: 85+6+6+3 = 100 and 70+20+10 = 100, so the cells already encode percentages. Header "How bids were weighted or run" covers the PBGC row | |
| 03 | 12 | 9 | OK | "at a price above" resolves the ambiguity the same way the exhibit intends; "won in 2017 and again in 2023" matches the Year cell | |
| 03 | 13 | 9 | OK | "and" becomes "so"; the causal link is the paragraph's argument. "a different kind of firm" for "dissimilar" | |
| 03 | 14 | 9 | OK | Split; same claim | |
| 03 | 15 | 9 | OK | Same three records and date range; "procurement notices" is the body's term | |
| 03 | 16 | 9 | OK | No change | |
| 03 | Exhibit 10 title | 9 | OK | Checked: 4.4 to 7.6 is "under $8 million"; 14.7 and 25.6 as stated | |
| 03 | Exhibit 11 title | 9 | CHANGES MEANING (minor) | "in open competitions" is stated only in the PBGC row ("Full and open competition"); the PPF and Nest rows say nothing about openness. "scored" does not fit the PBGC row either, but the current title has the same issue. "won every one" checks out (PPF both lots, Nest, PBGC 2017 and 2023) | "Three public pension bodies put Aladdin through competitive tenders between 2017 and 2025, and Aladdin won every one" |

Report 03: 18 rows. OK 14, CHANGES MEANING 4 (of which 2 minor).

## Report 04: Finding 2 (page 10, Exhibit 12)

| Report | Item | Page | Verdict | What changed | Suggested fix that keeps the readability gain |
|---|---|---|---|---|---|
| 04 | 1 | 10 | OK | "even when it is not named" becomes "though BlackRock rarely says the name"; the page shows zero earnings-call mentions and one slide line, so "rarely" is supported | |
| 04 | 2 | 10 | OK | Receipt [1] is added to the projection sentence while item 3 keeps it on the inference sentence; both facts come from the same slide, so the receipt is duplicated, not moved. "fastest-growing measure" checks against 4x, 2x, 1.3x | |
| 04 | 3 | 10 | OK | "I make it because API use is the activity the Studio page describes" makes the author's own reasoning explicit; the two sentences are adjacent in the original and the inference is the author's to state | |
| 04 | 4 | 10 | OK | "other" resolved as "outside the calls"; receipts 4 and 53 stay on their facts | |
| 04 | 5 | 10 | OK (option flagged) | Main rewrite is a split. The optional closing sentence "So the measure BlackRock is growing fastest is not one it says it charges for" states a conclusion the page implies but does not make, and "is growing fastest" turns a 2030 projection into current growth | If adopted: "So the measure BlackRock projects to grow fastest is not one it says it charges for." |
| 04 | 6 | 10 | OK | "Never on a call" is what the 0 cell shows | |
| 04 | 7 | 10 | CHANGES MEANING (minor) | "as an add-on sold with Aladdin Enterprise" becomes "both times described as an add-on"; the cell does not say both mentions used that description (author to confirm against 54 and 55) | "_Q3 2022_ [54] and _Q4 2024_ [55], described as an add-on sold with Aladdin Enterprise" |
| 04 | 8 | 10 | OK | Restates what a zero means | |
| 04 | 9 | 10 | OK | "public and private" is page 2's gloss | |
| 04 | 10 | 10 | OK | Split; quotations intact; receipt 6 repeated on each quoted passage. "The team said those were designed" resolves the dangling participle to the transaction types, the most natural reading | If the author meant the loan capture was designed with HPS, adjust "those" |
| 04 | 11 | 10 | OK | "the Studio general manager" is Newman's title in Exhibit 1 | |
| 04 | 12 | 10 | OK | "Hosting has moved to the public cloud as well"; Azure and AWS are the cloud facts quoted | |
| 04 | 13 | 10 | CHANGES MEANING (minor) | "which are Studio's surfaces" becomes "both of those are part of Studio"; Newman calls Data Cloud "part of Studio" (page 3), but nothing on the page says Explore is part of Studio rather than a surface Studio feeds | "...arrives through Data Cloud and Explore, the surfaces Studio provides" |
| 04 | Exhibit 12 title | 10 | OK | Checked: 2 + 1 + 1 = 4; "Studio", "citizen developer" and "agent" are the three zero rows | |

Report 04: 14 rows. OK 11, OK (option flagged) 1, CHANGES MEANING 2 (both minor).

## Report 05: Finding 3 (pages 11 and 12, Exhibits 13 to 15)

| Report | Item | Page | Verdict | What changed | Suggested fix that keeps the readability gain |
|---|---|---|---|---|---|
| 05 | 1 | 11 | OK | Optional shortening; same contrast | |
| 05 | 2 | 11 | OK | "built by Aladdin's engineering teams" is Exhibit 13 box 2 ("from '50, 60 Aladdin engineering teams'"); quotations intact | |
| 05 | 3 | 11 | OK | "So" presents the claim as following from the one-to-one mapping quote, which is the page's argument; "made the dependence plain" is what Crockett's line supports | |
| 05 | 4 | 11 | CHANGES MEANING (minor) | Lead-in "The data layer is being shaped the same way" adds a link between the data-model quote and the plugin model that the page does not draw | "On the data side, BlackRock's AI product head says..." |
| 05 | 5 | 11 | CHANGES MEANING | Box 1 "with the app, portfolio and widgets on screen" becomes "the open app, portfolio and widgets go in as context", asserting that screen state is an input to Copilot; the page does not say so (author to confirm against source 9) | Confirm against the talk; otherwise "One question, asked with the app, portfolio and widgets open on screen" |
| 05 | 6 | 11 | CHANGES MEANING | "would hurt performance" becomes "would hurt its answers"; the report itself says to keep "performance" if the talk does not support it | Keep "would hurt performance"; the actor "Copilot filters" is fine |
| 05 | 7 | 11 | CHANGES MEANING (minor) | Adds a definition of the orchestrator ("the component that decides which tool to call") and reframes guardrails as "a final check"; generic glosses, but the orchestrator definition is asserted as Copilot's design (author to confirm) | Gloss more neutrally: "the orchestrator (the component that runs the loop) iterates ..." |
| 05 | 8 | 11 | OK | Gloss "standing instructions (its system prompt)" is a definition, not a new fact | |
| 05 | 9 | 11 | OK | "the opposite design: they let the buyer's own AI tools reach their data" is Exhibit 15's column head; MCP expansion is on the page | |
| 05 | 10 | 11 | CHANGES MEANING (minor) | "The one public hint is a job advert" asserts it is the only hint; the original and Exhibit 14 just place the posting after "None found" | "One public hint is a job advert: ..." |
| 05 | 11 | 12 | CHANGES MEANING (minor) | "Governance in one place" narrowed to "One place to govern access"; "enterprise trust" rendered as "the trust of an enterprise login", one reading of an ambiguous phrase; "team by team" becomes "one engineering team at a time" (supported by Exhibit 13's engineering teams) | "Governance in one place; each user keeps their Aladdin permissions ('permission-dependent access'); guardrails against giving advice, tested in the system prompt; enterprise trust; a rollout BlackRock controls, one engineering team at a time 16, 9" |
| 05 | 12 | 12 | OK | "which is the comparison buyers make" restates "the terms ... now set"; receipt 8 (the webinar, Schafer on RFP questions) supports buyers asking | |
| 05 | 13 | 12 | OK | Garden path fixed; same three points | |
| 05 | 14 | 12 | CHANGES MEANING | "regulatory optics for a platform that will not give advice" becomes "would have to explain to regulators what outside AI tools do with its data", a specific mechanism the page does not state | "...and the regulatory optics of outside AI tools drawing on a platform that will not give advice 16" |
| 05 | 15 | 12 | OK | Split; "The description is short" is editorial but adds no fact; receipts 9, 16 stay at the end | |
| 05 | 16 | 12 | OK | Pronouns resolved; same comparison | |
| 05 | 17 | 12 | OK | "three governance questions" counts the three listed. Optional "This is quick win 5": Exhibit 17 row 5 is the published description, not the hold, so if used it belongs after sentence 1 of the box, not at the end | |
| 05 | Exhibit 13 title | 11 | CHANGES MEANING | "Every Copilot answer is a call to a production Aladdin API": the registry holds "agents and tools" and the exhibit shows one question's path, not that every answer is an API call. "advice is refused" drops "investment" from "never provide investment advice" | Use the shorter alternative with one word restored: "Copilot answers a question by choosing from thousands of registered tools and calling production Aladdin APIs, never giving investment advice" |
| 05 | Exhibit 14 title | 11-12 | OK | Softer than the current title ("shipped or announced"). Still says all seven have "AI connectors" while the Arcesium and S&P Global cells describe AI features and an AI Data Portal, which the report's own flag A notes | "Seven providers a Studio buyer also uses have shipped or announced AI access to their data; Aladdin has no public equivalent, only a job advert that mentions MCP" |
| 05 | Exhibit 15 title | 12 | CHANGES MEANING | "more to explain to regulators" carries the same invented mechanism as item 14; the cell says "regulatory optics" | "...with more to secure and regulatory optics to manage", or the shorter alternative "Inside the login buys governance; outside the login buys discoverability on rivals' terms" |

Report 05: 20 rows. OK 10, CHANGES MEANING 10 (of which 5 minor).

## Report 06: Finding 4, Part 3, register, back page (pages 13 to 18)

| Report | Item | Page | Verdict | What changed | Suggested fix that keeps the readability gain |
|---|---|---|---|---|---|
| 06 | 1 | 13 | OK | "selling to that" becomes "selling to those buyers"; body says "the same buyer" | |
| 06 | 2 | 13 | OK | "for asset managers" is register entry 8's title; "The first poll asked where firms sit today" is Exhibit 16's label; receipt 8 stays | |
| 06 | 3 | 13 | OK | "tied for second" is what "tied behind it" means | |
| 06 | 4 | 13 | OK | Numbering matches the exhibit | |
| 06 | 5 | 13 | OK | Names the Alpha FMC panelist as Clark Schafer; register entry 8 lists him as the only Alpha FMC speaker. "a platform transformation" adds "platform", which the context supports; receipt 8 repeated on both halves | |
| 06 | 6 | 13 | CHANGES MEANING (minor) | "poll results as read out" becomes "as the host read them out", attributing the reading to the host; the note does not say who read them | "Source: poll results as read out on the _Build vs. Buy webinar replay_, taken from the published captions⁸." |
| 06 | 7 | 13 | OK | No change | |
| 06 | 8 | 13 | OK | "answered" becomes "gave BlackRock's side" | |
| 06 | 9 | 13 | CHANGES MEANING | "On top of that data sit 'very, very robust APIs'" asserts a layering (APIs above the data) that Sewdass's quoted words do not give; the original says only that the modular approach comes "with" robust APIs and that clients build on top | "...publics and privates workflows.' That comes, she said, with 'very, very robust APIs that manage the end to end life cycle of a transaction,' so that clients can build 'their secret sauce rebalancing tools' on top⁸." |
| 06 | 10 | 13 | OK | Attribution restored; quotations intact | |
| 06 | 11 | 13 | OK | Gloss of "the same buyer" is the heading's own words | |
| 06 | 12 | 13 | CHANGES MEANING (minor) | "BlackRock itself says so" follows the SimCorp sentence, so "so" reads as BlackRock confirming the rival wins; the quote only says build vs buy is not binary | "BlackRock's own marketing agrees. Its _August 2026 insight_ piece says 'Build vs buy is no longer a binary question'⁷²." |
| 06 | 13 | 13 | OK | "Buyers now ask in RFPs whether they can build on the platform" restates "Extensibility is now an RFP question"; "not yet a finished answer" restates "not yet in finish" | |
| 06 | 14 | 14 | OK | "built on Part 1 and the four findings" is the Exhibit 17 source note | |
| 06 | 15 | 14 | OK | Three tests split; "described in Part 1" is where the model is described | |
| 06 | 16 | 14 | OK | No change | |
| 06 | 17 | 14 | OK | Header only | |
| 06 | 18 | 14 | OK | Supplies "clients whose Aladdin relationship", which the What-it-takes cell states | |
| 06 | 19 | 14 | OK | Replaces "tender winners" (which misnames the funds as winners) with "the public funds whose tenders BlackRock won", matching Exhibit 11; "SEC filers that disclose Aladdin" matches sources 3 and 49. PBGC is a federal insurer rather than a fund, as report 03 notes | "the public pension buyers whose tenders BlackRock won" |
| 06 | 20 | 14 | CHANGES MEANING (minor) | "Named references in use" becomes "named references the sales team can use", a count of available rather than used references | "Number of named references in use by sales; number of deals in which one was cited" |
| 06 | 21 | 14 | OK | "one measure of API use, starting from the API-call projection" restates "one measure ... built on the API-call projection"; receipt 1 stays | |
| 06 | 22 | 14 | OK | Names the referent of "the spoken message" | |
| 06 | 23 | 14 | OK | Split; receipts stay | |
| 06 | 24 | 14 | CHANGES MEANING (minor) | "the domains, counts and status of the catalog" becomes "how many specifications each has and at what status"; Exhibit 5 gives both specification and operation counts, so "counts" is narrowed to one | "which API domains exist, how many specifications and operations each has and at what status, ..." |
| 06 | 25 | 14 | OK | Split; "when the work ... is ready" restates "timed with"; receipts 9, 16, 65 stay on their facts | |
| 06 | 26 | 14 | CHANGES MEANING (minor) | Supplies "how Copilot connects" as the question prospects ask; row 5 and Exhibit 15 frame it as the connector question (how clients connect their own AI tools), not how Copilot connects | "prospects stop asking about connectors in deal reviews" |
| 06 | 27 | 14 | OK | "11 API domains" and "without the specifications themselves" resolve the ambiguities as intended | |
| 06 | 28 | 14 | OK | "skip the what-is-included discussion" is a fair reading of "start past scope" | |
| 06 | 29 | 14 | OK | No change | |
| 06 | 30 | 15 | OK | Split; "puts a number on" for "sized" | |
| 06 | 31 | 15 | OK | Wording | |
| 06 | 32 | 15 | CHANGES MEANING | Decision cell gains a one-to-one mapping (content for awareness, enablement for the first call, client success for production builds); the report itself says the page's three options do not map one-to-one, so the mapping is new | "Where marketing spends first: content, sales enablement or client success" |
| 06 | 33 | 15 | OK | "so the numbers within a group are not consecutive" describes what the register shows (1, 2, 3, 7, 10 ...) | |
| 06 | 34 | 15 | OK | Split; same two definitions and caveats | |
| 06 | 35 | 15-17 | OK | Notes only; entry 2 suggestion adds "covering" | |
| 06 | 36 | 18 | OK | Adds "This is"; passive to active with the same agent | |
| 06 | 37 | 18 | OK | Adds "The text is" | |
| 06 | Exhibit 16 title | 13 | OK | Checked: 37 + 30 = 67 percent for "mostly run vendor or hybrid"; compliance reporting 53 percent is the top poll-3 answer | |
| 06 | Exhibit 17 title | 14 | OK | Source note says receipts point to the public fact each win rests on; Owner and Measure columns exist | |
| 06 | Exhibit 18 title | 15 | OK | Restates the two columns | |

Report 06: 40 rows. OK 33, CHANGES MEANING 7 (of which 5 minor).

## Summary

| Report | Rows checked | OK | OK (option flagged) | CHANGES MEANING | of which minor |
|---|---|---|---|---|---|
| 01 cover and summary | 31 | 22 | 1 | 8 | 5 |
| 02 Part 1 | 58 | 43 | 1 | 14 | 5 |
| 03 Finding 1 | 18 | 14 | 0 | 4 | 2 |
| 04 Finding 2 | 14 | 11 | 1 | 2 | 2 |
| 05 Finding 3 | 20 | 10 | 0 | 10 | 5 |
| 06 Finding 4, Part 3, back | 40 | 33 | 0 | 7 | 5 |
| Total | 181 | 133 | 3 | 45 | 24 |

Exhibit-title arithmetic checked and correct: Exhibit 5 (127 of 301; 23 stable), Exhibit 7 (totals), Exhibit 10 (under $8 million 2017 to 2023), Exhibit 11 scoring rows (each sums to 100), Exhibit 12 (four non-zero mentions), Exhibit 16 (67 percent vendor or hybrid).

## The flags that matter most

1. **01 item 2.18, receipts key.** Narrowing "a filing" to "an SEC filing" and "a page" to "a BlackRock web page" misdescribes the P grade: the register's P entries include an iShares prospectus and a dozen third-party pages, docs and press releases. The T rewrite ("written by someone other than BlackRock") would also cover LSEG's own slides.
2. **01 quick win 5.** Narrows the Copilot description from three things (API mapping, governance, how clients connect their AI tools) to one.
3. **02 item 6.2.** Adds a conclusion ("a controlled production system for an existing client, not a product a stranger can try") that the page implies at most for the SDK, not for the specifications.
4. **02 item 8.6.** Adds "What it lacks is reach", a new characterization.
5. **02 item 3.2.** Resolves "up 24 percent with Preqin" to "includes Preqin" without the 10-K confirming which reading is right.
6. **02 item 8.4.** Quotation marks would attribute "citizen developers" to Woodhead unverified. Incidental finding: register entry 25 (Goel) says "the 3,000 figure is given at 35:23", but Exhibit 8 credits the 3,000 figure to Woodhead. One of the two is wrong.
7. **03 item 6.** Says the grey 2016 bar is "not a payment for Aladdin"; the page does not say what the integration services were for, and the exhibit title counts the bar under Aladdin payments.
8. **03 item 4.** Equates "the Snowflake implementation" with Aladdin Data Cloud; register entry 44 does not confirm it.
9. **05 item 14 and the Exhibit 15 title.** Turn "regulatory optics" into "would have to explain to regulators what outside AI tools do with its data", a mechanism the page never states.
10. **05 Exhibit 13 title.** "Every Copilot answer is a call to a production Aladdin API" overclaims (the registry holds agents as well as tools; the exhibit traces one question), and "advice is refused" drops "investment".
11. **05 items 5 and 6.** Assert that screen state is fed to Copilot as context, and that too many tools hurt "its answers" rather than "performance"; both need the talk to confirm.
12. **06 item 9.** Puts Sewdass's APIs "on top of that data", a layering her quoted words do not give.
13. **06 item 32.** Imposes a one-to-one mapping between the three stall points and the three spending options that the page does not make.
14. **01 item 2.10.** Moves superscript 6 (the private-markets webinar) onto an added clause ("which are Studio's surfaces") that the webinar does not support.

Cross-document observations made while checking (not readability): page 2 says five speakers define Studio and Exhibit 17 says four (report 01 already caught this); Exhibit 8 and register entry 25 disagree on who gives the 3,000 citizen-developer figure; the Exhibit 6 source note's "right-hand column" points at the Receipt column rather than After qualification (report 02 item 7.6 corrects it).
