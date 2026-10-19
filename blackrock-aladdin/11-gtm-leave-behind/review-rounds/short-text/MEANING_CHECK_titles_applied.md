# Meaning check: short-text readability pass (titles), as applied

BEFORE: `gtm/out/Aladdin_Studio_With_AI.before_titles.html`  
AFTER: `gtm/out/Aladdin_Studio_With_AI.html`  
Script: `gtm/titleswork/apply.py` (137 content pairs E1–E137, 5 layout pairs L1–L5).

## Method

1. Every (old, new) pair was loaded from `apply.py`, tag-stripped (superscript refs kept as `^n`) and judged on its own against the surrounding exhibit, page and source entries in AFTER. The editor's log was not relied on.
2. Independent check: applying the 142 pairs to BEFORE reproduces AFTER byte for byte (`apply(BEFORE) == AFTER: True`). So nothing outside `apply.py` changed.
3. Full tag-stripped text of BEFORE and AFTER was split into sentences and diffed with `difflib.SequenceMatcher` (1,237 vs 1,254 units, 124 hunks). Every hunk maps to a pair in the table; no unlisted change.
4. Reintroduction grep on AFTER for ordering language ('in the order', 'first/second/…/fifth/sixth direction', 'ordered', 'priority') and for the selling/access idea ('how Aladdin is sold', 'opens no new access', 'prospect can access', 'selling model'): none. The only 'selling model' hit is the pre-existing Exhibit 7 note ('So the total measures each vendor's selling model'), which is about the vendors, not the directions.
5. Superscripts: every relocated or added reference (E25 ^17 ^24; E74 ^65; E102 ^51 ^52 ^53 ^3 ^50 ^45) was checked against its source entry.
6. The Exhibit 3 SVG is byte-identical (script guard); the Exhibit 10 chart SVG changed only in its legend text (E46).

Page numbers are from the AFTER PDF (`gtm/out/Aladdin_Studio_With_AI.pdf`, 20 pages); where the PDF line-wraps a cell, the page is from the exhibit's position.

Verdict key: SAME = wording only; SAME* = one of the brief's required removals (the four IMPLIED edits and the cover subtitle), otherwise wording only; MOVED = a dropped idea now lives elsewhere in the same exhibit or page (where stated); CHANGED = a fact, hedge, subject or claim differs.

## All pairs

| id | label | page | verdict | note |
|---|---|---|---|---|
| E1 | COVER subtitle | 1 | SAME* | Cover subtitle; the decided wording. 'Where BlackRock is heading' dropped per the brief. |
| E2 | A2 | 1 | SAME | Wording only. |
| E3 | A1 cover | 1 | SAME | 'points' to 'suggests': same tentative level; the decided wording. |
| E4 | A1 page 15 | 15 | SAME | Part 3 title, same as E3. |
| E5 | A4 | 2 | MOVED | Dropped 'the fastest-growing measure'; the source note on the same page (E7) lists all four multiples (17x, 4x, 2x, 1.3x), from which it follows. |
| E6 | A3 | 2 | SAME | Superseded by L1 (see L1). 'to BlackRock' dropped from the tile; recipient is implicit in 'for Aladdin' and explicit in Finding 1 body (p.10) and source 2. |
| E7 | A5 | 2 | SAME | 'It projects' attributes the figures to the slide, as before; inference hedge kept. |
| E8 | IMPLIED 1 (supersedes A6) | 2 | SAME* | IMPLIED 1: the ordering and 'none changes how Aladdin is sold' removed, as required. |
| E9 | A7 (checker fix) | 2 | SAME | Superseded by L2 (see L2). |
| E10 | A8 | 2 | SAME | 'one-page' is in BEFORE (Exhibit 17 row 6: 'One page listing the 11 API domains'). |
| E11 | A9 | 2 | SAME | Punctuation. |
| E12 | A11 | 3 | MOVED | 'Sells one engine' lives in the body line above the exhibit on the same page: 'BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code' (after.txt 68). |
| E13 | A12 (checker fix) | 3 | SAME | 'on Preqin' resolves an ambiguity in the old sentence in the direction the cited URL slug gives (…private-credit-solutions-on-preqin…). Subject (Preqin inside eFront Insight) unchanged. |
| E14 | A13 | 3 | SAME | 'Its public APIs' = Aladdin Accounting's; same superscript 17. |
| E15 | A14 | 3 | SAME | 'service providers' to 'The providers' (custodians and administrators just named). |
| E16 | A15 title | 4 | MOVED | 'name no order screen' moved to the exhibit's source note (E17) and already sits in the step 1 cell ('The specifications name no order screen^17', after.txt 132). 'except positions and events' = no position or event API. |
| E17 | A15 note + A20 (sentence moved to Exhibit 5) | 4 | CHANGED | Stability-label definition (alpha/beta/stable/sunset, x-aladdin-api-stability field) left Exhibit 2's note and now lives only in Exhibit 5's note on p.6 (E28). Exhibit 2's cells still carry '(stable)', '(alpha)', 'beta' with no explanation on p.4. Low severity; fix below. |
| E18 | A16 | 4 | SAME | Header wording. |
| E19 | A17 (verb fix only) | 4 | SAME | Verb only; quotation and superscript 20 intact. |
| E20 | A18 | 4 | SAME | Punctuation; quotation and superscript 17 intact. |
| E21 | A19 | 4 | SAME | Punctuation; quotation intact. |
| E22 | A21 title | 5 | MOVED | 'the 11 public domains sit behind it' moved into the source note of the same exhibit (E23). |
| E23 | A21 second idea into source note | 5 | SAME | Carries the idea dropped from the E22 title; superscripts 17, 23 unchanged. |
| E24 | A26 title | 5 | MOVED | Both dropped clauses are in the new note sentence (E25) of the same exhibit; the login clause is also in the Developer Portal cell ('All sit behind a client login^24'). |
| E25 | A26 note | 5 | SAME | New note sentence restates E24's dropped clauses; ^17 (the specifications) supports 'no event specification is public', ^24 (APIs page) supports the login clause. Verified s17, s24. |
| E26 | A27 title | 6 | MOVED | The two domain names are the top rows of the same table; 'only 23 of the 54 specifications are stable' moved to the body paragraph under the exhibit on the same page (E27) and the Stable column total (23). |
| E27 | A27 body | 6 | SAME | Carries the clause dropped from E26. |
| E28 | A28 + A20 (stability sentence now in Exhibit 5 note) | 6 | SAME | Stability sentence moved here verbatim from Exhibit 2 (see E17); 'the four columns count specs by label' verified: 24+6+23+1 = 54 specs. |
| E29 | A30 h3 | 6 | SAME | 'out there' to 'public'. |
| E30 | A30 header | 7 | SAME | Header matches E29. |
| E31 | A29 | 7 | MOVED | Hear/Read/unpack the catalog are the Hear, Read and See-the-catalog rows of the same table; 'cannot run anything until qualified' = Try row ('Nothing to run') plus Build row (client host and credentials needed). |
| E32 | A39 Exhibit 6 Hear row (checker fix) | 7 | SAME | Adds 'podcast' / 'video series' descriptors, which sources 30 and 31 give; superscripts and links kept. |
| E33 | A31 | 7 | SAME | Quotations unchanged. |
| E34 | A32 | 8 | MOVED | 'data and cloud platforms sell to developers directly' is in the same exhibit's note, pre-existing: 'Data and cloud platforms sell to developers directly and cluster high.' 'Two access models coexist' is implied by the two groups. |
| E35 | A33 | 8 | SAME | 'non-client' = 'without a contract' (no relationship). |
| E36 | A35 | 8 | CHANGED | 'since 2024' is a new date claim covering all five speakers; Jeff Miller's Snowflake video is 'undated' in the table and in source 42. The dropped November 2025 three-part definition is MOVED (Woodhead row, same exhibit). Fix below. |
| E37 | A36 headers | 8 | SAME | Header wording; 'Where' to 'Recording' matched by E38. |
| E38 | A36 note reference to renamed column | 9 | SAME | Follows E37. |
| E39 | A37 (checker fix) | 8 | SAME | Same facts (definition, 3,000, Goel). 'at the start of Part 1' is true: the quote is on Part 1's first page (p.3), directly after Exhibit 1. |
| E40 | A38 | 9 | SAME | Colon to 'meaning'; quotations intact. |
| E41 | A39 Exhibit 8 Newman cell | 8 | SAME | Adds 'podcast', which source 15 gives. |
| E42 | A40 title | 9 | MOVED | 'only Goel and Woodhead name developer tools' moved to the same exhibit's note (E43); table shows '–' for Khara and Newman under Developer tools. |
| E43 | A40 + A41 note | 9 | SAME | Key for Yes/–; the cells use 'Yes' and '–'. Carries E42's dropped clause. |
| E44 | B1 | 10 | MOVED | 'none of it names Studio' is the first body sentence on the same page ('BlackRock's Studio page names no client building on Studio^13, and a full-text search of SEC EDGAR finds no filing that mentions Studio^44') and page 2. |
| E45 | B2 | 10 | MOVED | Dropped '2017 to 2023' and '$14.7 million in 2024' are in the chart labels of the same exhibit (2024 bar labelled 14.7) and in the Finding 1 body sentence on the same page; 'paid BlackRock' recipient is in source 2 and 'Payments for Aladdin' series label. |
| E46 | B3 legend | 10 | SAME | '(2016 only)' verified by the note: 'The grey 2016 bar is a payment for integration services'; only the 2016 bar is grey. |
| E47 | B4 first sentence | 10 | SAME | 'by year of payment' restated as a sentence. |
| E48 | B4 third sentence (optional tightening) | 10 | SAME | Clause order. |
| E49 | B6 (decided wording) | 10 | SAME | Decided wording; same claim. |
| E50 | B7 (checker fix) | 10 | SAME | Header. |
| E51 | B8 row 1 (checker fix) | 10 | SAME | Adds 'Weights:' label; numbers unchanged. |
| E52 | B8 row 2 (checker fix) | 10 | SAME | Same. |
| E53 | B9 (checker fix) | 10 | SAME | Matches source 53 ('four offers received'). |
| E54 | B10 | 10 | SAME | 'lots' = 'parts of the tender'. |
| E55 | B11 | 10 | SAME | 'kept the same price' = 'at an unchanged price'. |
| E56 | B12 sentence 1 (checker fix) | 11 | SAME | 'client types' to 'clients'; adds 'Aladdin' (the subject). |
| E57 | B12 sentence 3 | 11 | SAME | Same claim. |
| E58 | B13 headline | 11 | MOVED | 'API calls and the whole portfolio' and 'Both run through Studio' moved to the body: E59 (first sentence) and E65 ('Both are Studio surfaces. So Studio carries the growth story'). |
| E59 | B13 new first body sentence | 11 | SAME | 'public and private markets together' is in BEFORE (Exhibit 12 follow-on paragraph, before.txt 792). Carries E58's clause. |
| E60 | B14 title | 11 | MOVED | 'citizen developer' and 'agent' are rows of the same table (both 0); 'about four times in total' moved to the note (E61). |
| E61 | B14 note (total moved from title) | 11 | SAME | 'six and a half years' is Q1 2020 to Q2 2026 as stated in the title. Carries E60's total. |
| E62 | B15 | 11 | SAME | Header. |
| E63 | B16 (checker fix) | 11 | SAME | 'where it was described' = on those calls. |
| E64 | B18 sentence 1 | 12 | SAME | Replaces the author's paraphrase ('extensibility and data access') with BEFORE's own phrase from the old Finding 2 headline; no new claim. |
| E65 | C1 (chosen over B18 for sentences 3 and 4) | 12 | SAME | Sentence split; 'whether or not' = 'even when … does not'. |
| E66 | C2 | 12 | SAME | 'works only inside the login' matches BEFORE's own framing (Copilot 'will not respond to questions outside Aladdin platform boundaries'; Exhibit 7 note: an assistant 'that works only inside the vendor's own platform'); 'let outside AI tools reach their data' is the body's sentence 'they let the buyer's own AI tools reach their data'. |
| E67 | C3 | 12 | MOVED | 'registered' = the registry named in the first body row; 'never giving investment advice' is the exhibit's last row (E72). |
| E68 | C4 | 12 | SAME | Wording. |
| E69 | C5 label | 12 | SAME | 'in play' to 'shortlisted'. |
| E70 | C5 connector | 12 | SAME | Drops 'That is because'; quotation intact. |
| E71 | C6 | 12 | SAME | Quotation and GPT-4 detail intact. |
| E72 | C7 | 12 | SAME | Punctuation; superscripts 9, 16 intact. |
| E73 | C8 title (checker fix) | 13 | CHANGED | BEFORE distinguished rivals that 'announced AI features' (SimCorp, Arcesium) from data and cloud providers that 'shipped or announced AI access to their data'. AFTER says all eight others shipped or announced AI access to their data. Arcesium's row ('added AI features to Aquata and announced an AI platform') does not say that, and the Finding 3 body (same page) still keeps the old distinction. Count of nine and 'a Studio buyer compares' verified. Fix below. |
| E74 | C8 job-advert line into source note | 13 | SAME | Job-advert sentence moved from the title to the note; ^65 is the job posting. |
| E75 | C10 SimCorp (checker fix) | 13 | SAME | 'is to offer' matches 'announced'. |
| E76 | C10 Arcesium | 13 | SAME | Superseded by L3. |
| E77 | C10 FactSet | 13 | SAME | Superseded by L4. |
| E78 | C10 LSEG (checker fix) | 13 | SAME | Same facts, split. |
| E79 | C10 MSCI | 13 | SAME | Subject named. |
| E80 | C10 S&P Global | 13 | SAME | Subject named. |
| E81 | C10 Snowflake | 13 | SAME | Subject named. |
| E82 | C10 Databricks | 13 | SAME | Subject named. |
| E83 | C11 | 13 | SAME | Drops a repeated 'in my sources'. |
| E84 | C12 | 13 | MOVED | Title's conclusion (governance inside; discoverability on rivals' terms outside) is in the table cells and in the callout on the same page ('lets BlackRock, not FactSet and LSEG, set the terms of comparison'; 'The inside model already answers three governance questions'). |
| E85 | C13 (checker fix) | 13 | SAME | 'public' is implied by 'outside the login'; 'for the buyer's own AI tools' is in the Against/Inside cell. |
| E86 | C14 For / Inside | 13 | SAME | Sentence split; superscripts 16, 9 intact. 'platform's' trimmed by L5. |
| E87 | C14 For / Outside | 13 | SAME | Sentence split; superscripts intact. |
| E88 | C14 Against / Inside | 13 | SAME | Sentence split. |
| E89 | C14 Against / Outside (checker fix) | 13 | SAME | 'regulatory optics' to 'would look awkward to a regulator'; same hedge level. |
| E90 | C15 fold (checker wording) + dangling opener | 13 | SAME | Compressed; 'governed', 'in the system prompt' and 'never gives investment advice' are in Exhibit 15's For/Inside and Against/Outside cells on the same page and Exhibit 13; superscripts 9, 16 intact. |
| E91 | C15 closing + IMPLIED 3 | 13 | SAME* | IMPLIED 3: 'fifth direction' (ordering) to 'the Copilot direction'; row 5 of Exhibit 17 is the Copilot description. |
| E92 | C16 | 14 | MOVED | 'rivals are already selling to those buyers' is in the Finding 4 body on the same page: 'Rivals are selling to the same buyer, the one who wants a core platform plus their own builds.' |
| E93 | C17 (checker fix) | 14 | SAME | Which webinar is in the same exhibit's note (E95). |
| E94 | C18 | 14 | SAME | 'they' to 'firms'. |
| E95 | C19 | 14 | SAME | Same. |
| E96 | C21 | 14 | SAME | Same. |
| E97 | C23 | 15 | SAME | Drops 'again'. |
| E98 | D2 + IMPLIED 2 | 15 | SAME* | IMPLIED 2: the selling-model and no-new-access tests removed as required; the public-fact test kept. 'from inside' gains 'BlackRock' (E115 matches). |
| E99 | D3 | 15 | MOVED | 'each resting on a public fact' is the 'Rests on' column (E100) and the intro sentence 'Each direction uses only what is already public'; 'a way to know it worked' = 'Measure of success' column. |
| E100 | D4 + D5 headers | 15 | SAME | Headers. |
| E101 | D6 | 15 | MOVED | 'starting with clients whose Aladdin relationship is already public' is the same row's first cell: 'Shortlist clients already on the record'. |
| E102 | D7 (with Nest 52 and PBGC 53 added, per checker) | 15 | SAME | Superscripts re-seated beside the client each supports: s51 PPF tender, s52 Nest tender, s53 PBGC award, s3 JPM proxy, s50 Janus 10-K, s45 Royal London video. Verified all six source entries. Clause order swapped. |
| E103 | D8 (checker fix) | 15 | SAME | Matches the row's cell ('one measure of API use … put Studio's name beside that measure'). |
| E104 | D9 | 15 | SAME | Punctuation. |
| E105 | D10 | 15 | MOVED | 'BlackRock's speakers already give' is the same row's cell: 'Turn the definition four speakers already give^5, 15, 26, 41 into one written page'. |
| E106 | D11 | 15 | SAME | Same. |
| E107 | D12 | 16 | MOVED | 'for qualified buyers' is the same row's cell: 'The solutions team delivers it once a prospect is qualified'. |
| E108 | D13 row 5 noun form | 16 | SAME | Noun form. |
| E109 | D14 (checker fix) | 16 | SAME | 'what is your API suite?' is in BEFORE (p.2 list item 4 and the Finding 4 quotation); counts and status as before. |
| E110 | IMPLIED 4 + D15 | 16 | SAME* | IMPLIED 4: 'that opens no new access' removed as required; rest wording only, superscripts 9, 16, 65 intact. |
| E111 | D16 | 16 | SAME | Same. |
| E112 | D17 (checker fix) | 16 | SAME | Same. |
| E113 | D18 (checker fix) | 16 | SAME | 'count' made precise as the two counts Exhibit 5 shows. |
| E114 | D19 | 16 | SAME | Adds 'Number of'. |
| E115 | D20 | 16 | SAME | Adds 'BlackRock'. |
| E116 | D21 | 16 | MOVED | 'what each answer would decide' is the second column header of the same exhibit. |
| E117 | D22 (checker fix) | 16 | SAME | Wording. |
| E118 | D23 (checker fix) | 16 | SAME | Split. |
| E119 | D24 / D17 carry-through | 16 | SAME | Follows E112. |
| E120 | D25 (checker fix) | 16 | SAME | Split. |
| E121 | D26 | 16 | SAME | 'in full' is supported by row 5 (publish two parts now, add the third later). |
| E122 | D27 | 16 | SAME | Split. |
| E123 | D28 | 17 | SAME | '(P, S or T)' are the three grades defined on the Sources page. |
| E124 | D29 | 18 | SAME | Three grades verified (P 52, S 12, T 8 entries). |
| E125 | D30 (checker fix) | 18 | SAME | 'speech-to-text software run locally' = 'a local transcription'. |
| E126 | D32 'page as captured' x4 | 13,18,19 | SAME | 'page as captured' to 'as of' (x4). |
| E127 | D32 'seen' x2 | 18,19 | SAME | 'seen' to 'as of' (x2). |
| E128 | D33 | 18 | MOVED | '2017 to 2026' remains in the same entry's title ('filed 2017 to 2026'). |
| E129 | D34 | 18 | MOVED | 'version 2.0.0b3' remains in the same entry's title. |
| E130 | D35 | 19 | SAME | Same. |
| E131 | D36 speakers (no attributions added) | 19 | SAME | Same. |
| E132 | D37 date | 19 | SAME | Same. |
| E133 | D37 cross-reference | 19 | SAME | Punctuation. |
| E134 | D38 | 19 | SAME | Same. |
| E135 | D39 | 20 | SAME | 'that Finding 1 refers to' verified: Finding 1 body cites the Royal London video^45 for the Snowflake implementation. |
| E136 | D40 | 19 | SAME | Punctuation. |
| E137 | D41 | 20 | SAME | Word order. |
| L1 | A3 trim (tile 2 caption back to three lines) | 2 | SAME | Final tile caption. Drops 'to BlackRock' (see E6) and 'level' to 'payments'; 6x and dates unchanged. |
| L2 | A7 trim (list item 5 back to two lines) | 2 | SAME | Final list item 5; same three parts as BEFORE. |
| L3 | C10 Arcesium trim (one line) | 13 | SAME | Tense only. |
| L4 | C10 FactSet trim (one line) | 13 | SAME | Wording only. |
| L5 | C14 For / Inside trim (four lines) | 13 | SAME | 'the platform's' dropped; context is the inside-the-login column. |

## CHANGED items and fixes

### E73 — Exhibit 14 title (page 13)

BEFORE: "Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data. Aladdin has only a job advert that mentions MCP"  
AFTER: "Of nine providers a Studio buyer compares, only Aladdin has not shipped or announced AI access to its data"

What differs: the new title says the other eight providers have all shipped or announced *AI access to their data*. BEFORE said that only of the six data and cloud providers; for SimCorp and Arcesium it said *AI features*. Arcesium's own row ("added AI features to Aquata and announced an AI platform") does not say data access, and the Finding 3 body on the same page still says "two system-of-record rivals have announced AI features". The title now overstates one row and disagrees with its body. (Nine providers and "a Studio buyer compares" are both supported: nine rows; "Exhibit 14 lists both comparisons a Studio buyer makes".)

Fix (keeps the nine-provider frame and one sentence):  
"Exhibit 14. Of nine providers a Studio buyer compares, eight have announced AI features or AI access to their data; Aladdin has a job advert"  
The note sentence added by E74 ("Aladdin has only a job advert that mentions MCP^65.") can stay as is.

### E36 — Exhibit 8 title (page 8)

BEFORE: "Five BlackRock executives have defined Studio on the record, and the head of Studio engineering gave the three-part definition in November 2025"  
AFTER: "Five BlackRock executives have defined Studio on the record since 2024"

What differs: "since 2024" is a new date claim. Four of the five recordings are dated (early 2024, January 2025, 2025, November 2025); Jeff Miller's Snowflake video is "undated" in the Recording column and in source 42. BEFORE made no claim about when all five spoke. (The dropped November 2025 clause is fine: it is the Woodhead row of the same table.)

Fix: drop the two words.  
"Exhibit 8. Five BlackRock executives have defined Studio on the record"

### E17 — Exhibit 2 source note (page 4), low severity

BEFORE (note): "… Alpha, beta, stable and sunset are the stability labels each specification carries (its x-aladdin-api-stability field), alpha being the earliest. …"  
AFTER: sentence removed here and placed verbatim in Exhibit 5's note (page 6, E28).

What differs: Exhibit 2's cells still read "OrderAPI v1 (stable)", "ComplianceRuleAPI and ViolationAPI v1 (alpha)", "ValuationsAPI v1, beta", and page 4 no longer says what those labels are; the definition is two pages later. Nothing is false, but a definition left the page and exhibit that use it, which the brief's rule on dropped facts does not allow.

Fix (one clause, no new fact), appended to Exhibit 2's note:  
"The labels in brackets are each specification's stability label; Exhibit 5 explains them."  
Or, if page 4 has no room, accept as MOVED and leave as is.

## Totals

- Pairs checked: 142 (137 content + 5 layout)
- SAME: 116 (of which 5 are the brief's required removals, marked SAME*)
- MOVED: 23
- CHANGED: 3 (E73, E36, E17)
- Changes outside apply.py: 0 (apply(BEFORE) == AFTER; all 124 sentence-diff hunks map to pairs)
- Reintroduced ordering / selling / access statements: 0
- Superscripts moved to unsupported text: 0
- Altered quotations: 0
