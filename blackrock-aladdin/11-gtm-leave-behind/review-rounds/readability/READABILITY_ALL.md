# Readability reports: every flagged passage with its proposed rewrite

Six reviewers, one page range each. These are the inputs to the edit pass now running; the editor applies them with exact-match replacement, taking the plainer version where two overlap and adopting 'author to confirm' items only when the page already supports them.

---

# Readability pass: pages 1 and 2 (cover and executive summary)

Scope: every word on the cover and on page 2, including the three tiles and their source note, the two body paragraphs, the six quick wins, the method box, the receipts key and both footers. Read against the page images and the HTML source (so the underlined link phrases and superscripts below are exact).

Test applied: would a busy executive reading once, at normal speed, stop, reread, or come away unsure. Rewrites keep the author's first-person voice, add no facts, and keep every superscript and underlined phrase in place. Superscripts are written as ¹ ² ³ etc.; underlined link phrases are marked with _underscores_.

Verdict in one line: the cover is clean; page 2 has nine passages that force a reread, most of them in the lede, the tile source note, the two body paragraphs and the method box, and the six quick wins are noun fragments that read as labels rather than actions.

---

## Page 1 (cover)

### 1.1 Title
- Current: "Aladdin Studio, learned with AI"
- Trying to say: this is what the author learned about Aladdin Studio from public sources, using AI agents to do the collecting.
- Problem: "learned with AI" has no subject. On first read it can mean Studio itself learned something with AI (a product claim), rather than that the author learned about Studio using AI. The subtitle resolves it two lines later, but the title should not need rescuing.
- Rewrite (author's call; three options that keep the shape): "Aladdin Studio, learned from the outside with AI" / "What I learned about Aladdin Studio, with AI" / "Aladdin Studio, as the public record shows it".

### 1.2 Subtitle
- Current: "What public sources show about the product, where BlackRock is heading, and the quick wins for marketing Studio"
- Trying to say: three parts, three questions: what the product is, where BlackRock is going, what marketing can do quickly.
- Problem: minor. "the product" arrives before the reader is told the product is Studio, and "the quick wins" (definite article) assumes the reader already knows which wins. Not a stop, but a slight wobble.
- Rewrite: "What public sources show about Studio, where BlackRock is heading, and quick wins for marketing it"

### 1.3 Part cards
- Current: "Part 1 What the public record shows / Page 3", "Part 2 Four findings about BlackRock's direction and market / Page 9", "Part 3 Quick wins for marketing Studio / Page 14"
- Trying to say: the table of contents.
- Problem: none for readability. "BlackRock's direction and market" is compressed but clear enough in a card. If a second pass is wanted: "Four findings on where BlackRock is heading and what buyers want".

### 1.4 Cover footer
- Current: "Independent analysis compiled from public sources with AI agents. It was not produced, reviewed or endorsed by BlackRock."
- Trying to say: disclaimer.
- Problem: none. Note only that the page-2 footer uses a different form ("Independent analysis from public sources. Not produced, reviewed or endorsed by BlackRock."); the two should match or the cover one should be the fuller one by design.

---

## Page 2 (executive summary)

### 2.1 Lede
- Current: "Studio is the product behind the growth story BlackRock tells investors, but the story never names it, and the public proof of adoption is not Studio-specific. The quick wins close both gaps inside the enterprise selling model."
- Trying to say: two gaps: (1) BlackRock's investor growth story runs on Studio but never says so; (2) the public evidence that clients use Aladdin never says Studio either. The quick wins fix both without changing how Aladdin is sold.
- Problems: first sentence is 32 words with three ideas joined by "but" and "and". "The public proof of adoption is not Studio-specific" is abstract nouns doing the work (proof of whose adoption of what?). "Both gaps" requires the reader to go back and count. "Inside the enterprise selling model" is jargon that is not explained until page 3 (conversation first, then documentation, sandbox and credentials); an executive cannot tell what "inside" rules in or out.
- Rewrite: "Studio is the product behind the growth story BlackRock tells investors, but the story never names it. The public proof that clients use Aladdin never names Studio either. Six quick wins close both gaps, and none of them changes how Aladdin is sold."

### 2.2 Tile 1
- Current: "17x — Projected growth in API calls by 2030, the fastest-growing measure on a 2025 Investor Day slide"
- Trying to say: BlackRock projected 17x API-call growth by 2030, the biggest multiple on the slide.
- Problem: minor. The base year of the projection is not stated (the slide is from 2025, so the reader assumes 2025 to 2030). "Measure" is fine. Reads as a label, which is acceptable for a tile.
- Rewrite (optional): "Projected growth in API calls by 2030, the fastest-growing measure on BlackRock's 2025 Investor Day slide"

### 2.3 Tile 2
- Current: "$25.6M — JPMorgan Chase's 2025 payments to BlackRock for Aladdin, per its proxy statement; almost six times 2017"
- Trying to say: JPMorgan paid BlackRock $25.6M for Aladdin in 2025, almost six times what it paid in 2017.
- Problem: "almost six times 2017" is a fragment; the reader must supply "what it paid in". The semicolon stacks a second idea onto a caption.
- Rewrite: "JPMorgan Chase's 2025 payments to BlackRock for Aladdin, per its proxy statement, almost six times what it paid in 2017"

### 2.4 Tile 3
- Current: "0 — Mentions of Studio by a BlackRock executive on 26 earnings calls, Q1 2020 to Q2 2026"
- Trying to say: no BlackRock executive has said "Studio" on an earnings call in six and a half years.
- Problem: none. Clear. (Optional, more concrete: "Times a BlackRock executive said 'Studio' on 26 earnings calls, Q1 2020 to Q2 2026".)

### 2.5 Tile source note
- Current: "Source: _BlackRock 2025 Investor Day_¹, slide on keeping the cost of growth low: API calls 17x, model portfolios 4x, portfolios 2x, trade allocations 1.3x; the slide does not say which products generate the API calls, so reading them as Studio is my inference. _JPMorgan Chase proxy statements_², ³; _third-party earnings call transcripts_⁴."
- Trying to say: three sources, one per tile, left to right; and a caveat that the 17x slide does not name Studio.
- Problems: one 46-word sentence with a colon, a four-item list, a semicolon and a conclusion. "Reading them as Studio" ("them" = the API calls) is compressed to the point of ambiguity. The reader is not told that the three sources map to the three tiles in order.
- Rewrite: "Sources, left to right: _BlackRock 2025 Investor Day_¹, slide on keeping the cost of growth low. The slide projects API calls 17x, model portfolios 4x, portfolios 2x and trade allocations 1.3x. It does not say which products generate the API calls; attributing them to Studio is my inference. _JPMorgan Chase proxy statements_², ³. _Third-party earnings call transcripts_⁴."

### 2.6 Body paragraph 1, sentence 1
- Current: "Studio is Aladdin's developer and data layer: APIs and events, a Python SDK and Aladdin Data Cloud on Snowflake, described the same way by five BlackRock speakers since 2024⁵."
- Trying to say: what Studio is (three parts), and that five BlackRock speakers have all defined it the same way.
- Problems: colon plus list plus a dangling participle ("described the same way" has no clear subject: the layer? the list?). "Events" and "Aladdin Data Cloud on Snowflake" are jargon before explanation (page 3 explains Data Cloud as a managed data service on Snowflake).
- Rewrite: "Studio is Aladdin's developer and data layer. It has three parts: APIs and events, a Python SDK, and Aladdin Data Cloud, a managed data service on Snowflake. Five BlackRock speakers have described it the same way since 2024⁵."

### 2.7 Body paragraph 1, sentence 2
- Current: "Proof of use is public: JPMorgan Chase's proxy statements, Janus Henderson's commits and 10-K, Royal London's chief executive on video and three pension funds' tender notices."
- Trying to say: there is public evidence that named clients use Aladdin (not Studio specifically).
- Problems: this is the passage most likely to mislead. "Proof of use" does not say use of what. Coming straight after a definition of Studio, an executive reads it as proof of Studio use, which the lede has just said does not exist. "Commits" is developer jargon (code changes on GitHub, page 11). "Royal London's chief executive on video" is a fragment with no verb.
- Rewrite: "Public documents prove that named clients use Aladdin, though not Studio by name: JPMorgan Chase's proxy statements, Janus Henderson's code commits and 10-K, Royal London's chief executive on BlackRock's client video, and three pension funds' tender notices."

### 2.8 Body paragraph 1, sentence 3
- Current: "I assembled that with AI agents in about a day from 54 API specifications, 128 recordings, filings and code."
- Trying to say: how the evidence base was built and how fast.
- Problems: "that" has no clear referent (the proof just listed? the whole analysis?). The sentence also interrupts the argument between the proof and the findings; it belongs with the method.
- Rewrite: "I assembled all of this with AI agents in about a day, from 54 API specifications, 128 recordings, filings and code." Consider moving it to the end of the method box, where the same sources are listed again.

### 2.9 Body paragraph 2, sentence 1
- Current: "API calls are the fastest-growing measure BlackRock showed investors, 17x by 2030, though the slide does not name the products behind the calls, so Studio is my inference."
- Trying to say: finding 2: the growth story is API calls, and attributing them to Studio is the author's inference.
- Problems: 30 words, "though ... so ..." qualifies and concludes in one breath. "Studio is my inference" is elliptical (what is inferred is that the calls run through Studio). The sentence also repeats the tile source note almost word for word, so the reader meets the same caveat twice in four inches.
- Rewrite: "API calls are the fastest-growing measure BlackRock showed investors: 17x by 2030. The slide does not name the products behind the calls; that they run through Studio is my inference." If the source note keeps its caveat, this sentence can drop the second half.

### 2.10 Body paragraph 2, sentence 2
- Current: "The product is the whole portfolio, public and private, fed through Data Cloud and Explore⁶."
- Trying to say: BlackRock now sells Aladdin as covering the whole portfolio, public and private markets, and the new private-markets data arrives through Studio's surfaces, Data Cloud and Explore (page 10).
- Problems: "The product" is unanchored (Studio? Aladdin? the growth story?). "Public and private" needs "markets". "Explore" is a product name the reader has not met. "Fed through" is figurative.
- Rewrite: "The other half of the growth story is the whole portfolio, public markets and private. The new private-markets data arrives through Data Cloud and Explore, which are Studio's surfaces⁶."

### 2.11 Body paragraph 2, sentence 3
- Current: "Copilot, BlackRock's AI front door, stays inside the platform while data providers market connectors outside⁷."
- Trying to say: finding 3: Aladdin Copilot is available only inside the Aladdin login, whereas data providers sell connectors that outside AI tools can use.
- Problems: "AI front door" is a metaphor the reader has to decode; "stays inside the platform" and "market connectors outside" are compressed spatial shorthand; "connectors" is jargon until page 12. An executive gets the gist but not the contrast.
- Rewrite: "Aladdin Copilot, BlackRock's AI assistant, works only inside the Aladdin login. Data providers have gone the other way: they sell connectors that let outside AI tools pull their data⁷."

### 2.12 Body paragraph 2, sentence 4
- Current: "Buyers at BlackRock's own webinar said they want a core platform plus their own builds, and rivals are selling to that⁸."
- Trying to say: finding 4: buyers want a core platform they can build on, and competitors already pitch to that demand.
- Problems: "their own builds" and "selling to that" are shorthand; "that" refers to a demand that has not been named as a demand.
- Rewrite: "At BlackRock's own webinar, buyers said they want a core platform plus tools they build themselves, and rival platforms are already selling to that demand⁸."

### 2.13 Six quick wins (list)
- Current lead-in: "Six quick wins, in the order I would do them:"
- Problem with the lead-in: none.
- Problem with the list: every item is a noun phrase (a deliverable) with no verb, so the list reads as a parts inventory rather than six actions. Several items lean on terms not yet explained ("the API question", "plugin model", "the public catalog"). Rewrites below turn each into one declarative instruction, keeping every word that carries meaning.

1. Current: "Named proof from clients whose Aladdin relationship is already public."
   Trying to say: collect named client references from clients who have already disclosed they use Aladdin.
   Rewrite: "Collect named client proof, starting with clients whose Aladdin relationship is already public."
2. Current: "Studio's name beside the API-call projection, in investor and client materials."
   Trying to say: put Studio's name next to the 17x projection wherever it appears.
   Rewrite: "Put Studio's name beside the 17x API-call projection in investor and client materials."
3. Current: "A written one-page version of the definition five speakers give only in recordings."
   Trying to say: write down the definition of Studio that exists today only in talks.
   Rewrite: "Write the one-page definition of Studio that five speakers so far give only in recordings."
   Note: Exhibit 17 on page 14 says "four speakers" for the same win, and the body paragraph above says "five". One of the two numbers is wrong; fix before this rewrite is applied.
4. Current: "An RFP-ready answer to the API question buyers now ask."
   Trying to say: a document that answers "what is your API suite?", which page 13 shows buyers now put in RFPs.
   Problem: "the API question" is a definite reference to something the reader has not seen.
   Rewrite: "Prepare an RFP-ready answer to the question buyers now ask: what is your API suite?"
5. Current: "A published description of the Copilot plugin model."
   Trying to say: publish how Copilot's tools and plugins work.
   Problem: "plugin model" is undefined until page 12.
   Rewrite: "Publish a description of how Copilot's plugins map to Aladdin's APIs."
6. Current: "A prospect-facing 'what is in the box' summary of the public catalog."
   Trying to say: a one-page list of the public API catalog's domains for prospects.
   Problem: "the public catalog" (of what?) is undefined on this page.
   Rewrite: "Publish a prospect-facing 'what is in the box' summary of the public API catalog."

### 2.14 Method box, sentence 1
- Current: "Public material only. BlackRock pages, the 54 specifications inside 11 public asdk_plugin packages, 128 recordings, SEC filings, procurement notices, GitHub and PyPI, pulled by AI agents and checked by me against each document."
- Trying to say: the source list, and the division of labor between the agents (collecting) and the author (checking).
- Problems: a 36-word fragment with no main verb. "asdk_plugin packages" is unexplained jargon (Python packages published on PyPI, page 6). "Checked by me against each document" leaves out what was checked.
- Rewrite: "Public material only. The sources are BlackRock web pages, the 54 API specifications inside 11 public asdk_plugin Python packages, 128 recordings, SEC filings, procurement notices, GitHub and PyPI. AI agents pulled them; I checked every fact against its document."

### 2.15 Method box, sentence 2
- Current: "Part is machine-transcribed, and names and jargon can be misheard; the register marks which."
- Trying to say: some recordings were transcribed by machine, which can mishear names; the Source register flags those quotes.
- Problems: "Part" of what is unstated (the recordings). "The register marks which" leaves the object missing (which quotes? which recordings?).
- Rewrite: "Some recordings are machine-transcribed, so names and jargon can be misheard; the Source register marks which quotes come from machine transcripts."

### 2.16 Method box, sentence 3
- Current: "Figures may be outdated, and I have no internal product context, so conclusions may be wrong for reasons I cannot see."
- Trying to say: two further limits.
- Problem: none that stops a reader; it is two ideas in one sentence and would read faster split.
- Rewrite (optional): "Figures may be out of date. I have no internal product context, so some conclusions may be wrong for reasons I cannot see."

### 2.17 Receipts key, intro
- Current: "Underlined text links to the document behind the fact. Each superscript points to the Source register, which gives the grade, title, speaker and date and, for recordings, the minute and second of each quoted passage."
- Trying to say: two kinds of citation: the link (the document) and the number (the register entry).
- Problems: second sentence is 31 words with a nested "and, for recordings," clause. "The grade" is jargon until the P/S/T line below. The reader is not told where the register is (page 15).
- Rewrite: "Underlined text links to the document behind the fact. Each superscript number points to an entry in the Source register on page 15. The entry gives the source's grade (P, S or T, below), its title, speaker and date. For recordings, it also gives the minute and second at which each quoted passage begins."

### 2.18 Receipts key, grades
- Current: "P Primary document: a filing, a specification, a page, a notice, GitHub or PyPI" / "S BlackRock speaker on the record, with the name and title as given" / "T Third-party report: trade press or a secondary summary"
- Trying to say: the three evidence grades.
- Problems: "a page" (a web page? of what?), "a notice" (procurement notice), and "GitHub or PyPI" (code, not documents) are fragments the reader has to fill in. "As given" by whom is unstated; the register itself says "as the recording gives them". "A secondary summary" is vague.
- Rewrite: "P Primary document: an SEC filing, an API specification, a BlackRock web page, a procurement notice, or code on GitHub or PyPI" / "S BlackRock speaker on the record, with the name and title as the recording gives them" / "T Third-party report: trade press, or a summary written by someone other than BlackRock"

### 2.19 Page-2 footer
- Current: "Independent analysis from public sources. Not produced, reviewed or endorsed by BlackRock."
- Problem: none; see 1.4 on matching the cover wording.

---

## Exhibits in this range

Pages 1 and 2 contain no numbered exhibits. The one exhibit-like element is the three-tile row on page 2, which has no title at all; the lede above it does the work. Headings for the two boxes are listed for completeness.

| Element | Current title | Proposed title (states the finding) |
|---|---|---|
| Page 2, three-tile row (17x / $25.6M / 0) | none | "BlackRock's growth story is API calls and its proof of use is paying clients, but Studio's name appears in neither" |
| Page 2, method box | "What this method can and cannot do" | "This rests on public material only, pulled by AI agents and checked by me, so it can be out of date and cannot see inside the product" |
| Page 2, receipts key | "How to read the receipts" | "Every fact carries a link to its document and a number to its register entry" (if "receipts" is kept as the document's word, the current heading is fine) |

---

## Consistency catches made while reading (not readability, but found on this pass)

1. "Five speakers" (page 2, paragraph 1 and quick win 3) versus "four speakers" (Exhibit 17, page 14, same win). One is wrong.
2. The 17x caveat ("the slide does not say which products generate the API calls, so ... my inference") appears twice on page 2, in the tile source note and in paragraph 2, nearly verbatim. Keep one.
3. The cover footer and the page-2 footer use different wording for the same disclaimer.
4. The source note under the tiles does not say the three sources map to the three tiles left to right; the rewrite in 2.5 adds "left to right".

---

# Readability pass, Part 1 (pages 3 to 8, Exhibits 1 to 9)

Conventions. Superscript source numbers are written as trailing numbers (" 9") exactly as the text dump shows them; every rewrite keeps each number next to the fact it belonged to. Quoted and underlined link phrases are kept verbatim inside the rewrites so the links survive; where a rewrite splits a sentence, the underlined phrase stays whole inside one of the new sentences. Rewrites add no facts. Where a clearer sentence would require a fact the page does not state, the entry says so and marks it "author to confirm".

Severity: **Stop** = a busy reader would reread or come away unsure. **Slow** = reads once but costs effort. **Fix** = a small mechanical issue (fragment, unexplained term).

---

## Page 3

### 3.1 (Stop) The Rosales sentence, 58 words, three quotations joined by a colon and a semicolon

Current: "Brennan Rosales, its AI Engineering Lead, put the scale this way at a LangChain conference in 2025: “BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries”; the organization is “around 7,000 people, with over 4,000 of those being engineers,” who maintain “around 100 Aladdin front-end applications” 9."

Trying to say: Aladdin is big, and BlackRock's own AI engineering lead has said so publicly with three numbers.

Rewrite: "Brennan Rosales, its AI Engineering Lead, put the scale this way at a LangChain conference in 2025. “BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries.” The Aladdin organization is “around 7,000 people, with over 4,000 of those being engineers.” They maintain “around 100 Aladdin front-end applications” 9."

### 3.2 (Stop) "up 24 percent with Preqin": the reader cannot tell whether Preqin caused the growth or is included in the figure

Current: "BlackRock’s technology services and subscription revenue was $2.0 billion in 2025, up 24 percent with Preqin 10."

Trying to say: The revenue line that contains Aladdin was $2.0 billion in 2025, up 24 percent, and the 2025 figure includes Preqin.

Rewrite (author to confirm that "with Preqin" means "including Preqin"): "BlackRock’s technology services and subscription revenue was $2.0 billion in 2025, up 24 percent; the figure includes Preqin 10."

### 3.3 (Slow) Colon list, then "what is out there" twice in two sentences

Current: "Aladdin is sold the way enterprise platforms are sold: a conversation first, then documentation, a sandbox and credentials from the solutions team once a prospect is qualified. What follows is what is out there before that conversation."

Trying to say: Nothing technical is handed over until after a sales conversation; Part 1 covers what a prospect can see before that conversation.

Rewrite: "Aladdin is sold the way enterprise platforms are sold. The conversation comes first. Documentation, a sandbox and credentials come from the solutions team once a prospect is qualified. Part 1 covers what a prospect can see before that conversation."

### 3.4 (Fix) Exhibit 1, Aladdin Wealth cell: "with Morgan Stanley first" is a fragment the reader has to decode

Current: "Portfolio risk analysis and proposals for advisors; its AI “auto commentary” tool launched in October 2025 with Morgan Stanley first 11"

Trying to say: Morgan Stanley was the launch client.

Rewrite: "Portfolio risk analysis and proposals for advisors. Its AI “auto commentary” tool launched in October 2025, with Morgan Stanley as the first client 11."

### 3.5 (Stop) Exhibit 1, Aladdin Studio cell: two colons, a semicolon and a 30-word quotation in one cell

Current: "The developer and data layer: APIs and events, a Python SDK, Aladdin Compute and Aladdin Data Cloud; “API-first,” for “a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting” 13"

Trying to say: Studio is the developer layer, it has four named pieces, and BlackRock names three kinds of user for it.

Rewrite: "The developer and data layer. It covers APIs and events, a Python SDK, Aladdin Compute and Aladdin Data Cloud. BlackRock calls it “API-first” and names three users: “a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting” 13."

### 3.6 (Slow) Exhibit 1, Aladdin Data Cloud cell: three clauses chained with semicolons

Current: "A managed data service on Snowflake that puts Aladdin and outside data in one place; sold as an add-on to Aladdin Enterprise 14; Richard Newman, General Manager, Aladdin Studio, calls it “part of Studio” 15"

Trying to say: Data Cloud is a Snowflake data service, sold as an add-on, and the head of Studio counts it as part of Studio.

Rewrite: "A managed data service on Snowflake that puts Aladdin and outside data in one place. It is sold as an add-on to Aladdin Enterprise 14. Richard Newman, General Manager, Aladdin Studio, calls it “part of Studio” 15."

### 3.7 (Fix) "BlackRock’s own definition" does not say of what

Current: "BlackRock’s own definition comes from the head of Studio engineering, on Snowflake’s podcast in November 2025. It has three parts."

Trying to say: The best public definition of Studio comes from BlackRock's own head of Studio engineering, and it names three parts.

Rewrite: "BlackRock’s own definition of Studio comes from the head of Studio engineering, on Snowflake’s podcast in November 2025. It has three parts."

---

## Page 4

### 4.1 (Stop) After the Woodhead quotation, the three parts are never named in plain words; the reader has to extract them from a machine transcript ("a set of APIs events")

Current: (the quotation, then) "Exhibit 2 follows one trade through that platform, as far as the public specifications describe it: who acts, where BlackRock names a product or application, and which of the 54 APIs covers each step 17, 20."

Trying to say: The three parts are APIs and events, Data Cloud and developer tools; Exhibit 2 now traces a trade through the APIs.

Rewrite (bridge sentence uses only what the quotation says): "The three parts are APIs and events, the Aladdin Data Cloud on Snowflake, and developer tools. Exhibit 2 follows one trade through Aladdin, as far as the public specifications describe it. For each step it records who acts, which product or application BlackRock names, and which of the 54 public API specifications covers the step 17, 20."

Note: "the 54 APIs" appears here for the first time; the count is only explained in Exhibit 5 two pages later. The rewrite says "54 public API specifications" so the phrase explains itself; Exhibit 5 can carry the detail.

### 4.2 (Fix) Exhibit 2, step 1, Named column: "Explore" appears with no indication of what it is

Current: "Explore’s “new what-if model” compares a changed portfolio with the original before anything is traded 21; the specifications name no order screen 17"

Trying to say: The only named application at this step is Explore, and it is a what-if tool rather than an order screen.

Rewrite: "The Explore application: its “new what-if model” compares a changed portfolio with the original before anything is traded 21. The specifications name no order screen 17."

### 4.3 (Slow) Exhibit 2, step 1, API column: "stable" and "alpha" labels are used from this exhibit on but are not explained until Exhibit 5

Current: "OrderAPI v1, stable: order:post takes whatIf and runCompliance; the status examples run “Open,” “Compl Pending,” “Authorized,” “Active,” “Booked” 17"

Trying to say: The Order API is one of the stable ones; an order post carries two flags; and the spec's own examples show the order lifecycle.

Rewrite: "OrderAPI v1 (stable). Posting an order takes whatIf and runCompliance. The specification’s example statuses run “Open,” “Compl Pending,” “Authorized,” “Active,” “Booked” 17."

Suggest the Exhibit 2 source note add one clause: "alpha, beta and stable are the maturity labels each specification carries" (author to confirm the labels come from the specifications).

### 4.4 (Stop) Exhibit 2, step 2, Who acts: cell has no subject; "Automatic" what?

Current: "Automatic on posting, with runCompliance on by default; a violation then carries an owner, a disposition and a resolution comment 17"

Trying to say: No person acts; the check runs itself when the order is posted, and any violation is assigned to someone.

Rewrite: "No one. The check runs automatically when the order is posted, because runCompliance is on by default. Any violation then carries an owner, a disposition and a resolution comment 17."

### 4.5 (Slow) Exhibit 2, step 2, API column: four facts in one cell

Current: "ComplianceRuleAPI and ViolationAPI v1, alpha: violations are “generated at time of the compliance breach,” intraday and overnight; a check that times out posts the order as “Compl Pending” 17"

Rewrite: "ComplianceRuleAPI and ViolationAPI v1 (alpha). Violations are “generated at time of the compliance breach,” intraday and overnight. A check that times out posts the order as “Compl Pending” 17."

### 4.6 (Stop) Exhibit 2, step 3, Named column: "Aladdin Accounting’s leads" reads as sales leads

Current: "Aladdin Accounting’s leads: the run goes “from that first order through the trade, through all the operation protocols into accounting without lifting up the pencil” 20"

Trying to say: The people who run Aladdin Accounting describe the trade flowing straight through to accounting; no application is named for this step.

Rewrite: "The people who lead Aladdin Accounting say the run goes “from that first order through the trade, through all the operation protocols into accounting without lifting up the pencil” 20."

### 4.7 (Slow) Exhibit 2, step 3, API column: three systems and five field names in one cell

Current: "TradeAPI v2, alpha: trades:post, batchPost, filter; a block trade carries its per-portfolio trades, confirmedWith and confirmedBy; BrokerConfirmRoutingAPI routes the confirm 17"

Rewrite: "TradeAPI v2 (alpha), with trades:post, batchPost and filter. A block trade carries its per-portfolio trades, plus confirmedWith and confirmedBy. BrokerConfirmRoutingAPI routes the confirm 17."

### 4.8 (Fix) Exhibit 2, step 4, Who acts: "IBOR" is used in the row label and this cell before the next cell spells it out

Current: "The investment team’s live book; Newman: “It does start with IBOR” 15"

Rewrite: "The investment team, whose live book is the IBOR, the investment book of record. Newman: “It does start with IBOR” 15." (The expansion is taken from the Named column of the same row.)

### 4.9 (Slow) Exhibit 2, step 4, API column: parenthesis inside a semicolon chain

Current: "No position API among the 54; positions appear as fields (a PortfolioToolkitAPI positions source, a violation’s “underlying positions”); CashLadderAPI v2, stable, gives the settlement-date cash ladder 17"

Rewrite: "None of the 54 is a position API. Positions appear only as fields: a positions source in PortfolioToolkitAPI, and a violation’s “underlying positions.” CashLadderAPI v2 (stable) gives the settlement-date cash ladder 17."

### 4.10 (Fix) Exhibit 2, step 5, Who acts: "we" has no stated speaker

Current: "Accounting: “we are data managers more than anything else” 20"

Rewrite: "The accounting team, which says of itself: “we are data managers more than anything else” 20."

### 4.11 (Fix) Exhibit 2, step 5, Named column: "its" could point to Accounting or to the specification

Current: "Aladdin Accounting, the product its configuration specification is written for 17"

Rewrite: "Aladdin Accounting. The public portfolio-configuration specification is written for this product 17."

### 4.12 (Slow) Exhibit 2, step 5, API column

Current: "AborLotAPI v1, alpha: ABOR lots “retrieved from the ledger_a_summary table,” each with an oborLotId and open and close transaction ids; EnrichedCapitalFlowAPI v1, stable, posts subscriptions and redemptions 17"

Rewrite: "AborLotAPI v1 (alpha). ABOR lots are “retrieved from the ledger_a_summary table,” each with an oborLotId and open and close transaction ids. EnrichedCapitalFlowAPI v1 (stable) posts subscriptions and redemptions 17."

### 4.13 (Stop) Exhibit 2 source note: "do not order steps 4 to 6" reads as the verb "order" in an exhibit about orders

Current: "The statuses are the Order specification’s examples; the specifications hold no position or event API and do not order steps 4 to 6."

Trying to say: The specifications do not say in what sequence steps 4, 5 and 6 happen; the sequence shown is the author's.

Rewrite: "The statuses are the Order specification’s examples. The specifications hold no position or event API, and they do not say in what sequence steps 4 to 6 happen; the sequence shown is mine." (Author to confirm "is mine".)

---

## Page 5

### 5.1 (Fix) Exhibit 3, APIs box: "all “Aladdin Graph”" is a term the reader has not met yet

Current: "APIs and events: 54 public specifications, all “Aladdin Graph”"

Trying to say: All 54 specifications carry the Aladdin Graph id (explained in Exhibit 4).

Rewrite: "APIs and events: 54 public specifications, all tagged “Aladdin Graph” (see Exhibit 4)"

### 5.2 (Slow) Exhibit 3, Data Cloud box: "fed by Fivetran" assumes the reader knows Fivetran is a data-pipeline vendor

Current: "Aladdin Data Cloud on Snowflake, fed by Fivetran"

Rewrite: "Aladdin Data Cloud on Snowflake, with data moved in by Fivetran" (The same gloss appears in Exhibit 4, "with Fivetran moving the data"; using the same words in both places lets the reader connect them.)

### 5.3 (Fix) Exhibit 4, APIs row: "ADC" is used without expansion; "specs" and "specifications" alternate

Current: "The 54 specs include orders, trades, compliance rules, risk rules, security creation and ADC datasets 17."

Rewrite: "The 54 specifications include orders, trades, compliance rules, risk rules, security creation and Aladdin Data Cloud datasets 17."

### 5.4 (Slow) Exhibit 4, APIs row, second sentence: the point ("Aladdin Graph is a layer, not a product") arrives after a 12-character id pattern

Current: "Every public specification carries an id of the form agraph.<domain>.<segment>.<group>.v1.<API>, so Aladdin Graph is the whole API layer, not one API 17."

Rewrite: "Aladdin Graph is the whole API layer, not one API: every public specification carries an id of the form agraph.<domain>.<segment>.<group>.v1.<API> 17."

### 5.5 (Fix) Exhibit 4, Data Cloud row: "the latency" of what is not stated

Current: "A managed data store on Snowflake, with Fivetran moving the data; Goel gives the latency as “within 15 minutes” 25."

Rewrite: "A managed data store on Snowflake, with Fivetran moving the data. Goel says data arrives “within 15 minutes” 25." (Author to confirm this is what Goel's latency figure measures.)

### 5.6 (Fix) Exhibit 4, SDK row: "plugin builder" and "domain" appear before either is explained

Current: "Eleven add-on packages, one per domain, are generated from the specifications by the plugin builder 26."

Rewrite: "Eleven add-on packages, one per API domain (Exhibit 5), are generated from the specifications by a tool BlackRock publishes called the plugin builder 26."

### 5.7 (Fix) Exhibit 4, Investment research row: double colon, "alpha" unexplained

Current: "A domain of five alpha APIs: research notes, engagements, analyst coverage, watchlists and screening criteria 17."

Rewrite: "A domain of five APIs, all still labelled alpha. They cover research notes, engagements, analyst coverage, watchlists and screening criteria 17."

### 5.8 (Fix) Exhibit 4, Tools for Excel row: "little public detail" is a fragment with no subject

Current: "An Excel add-in listed on the APIs page as a Studio resource, with Aladdin Data eXchange for bulk delivery; little public detail 23."

Rewrite: "An Excel add-in. The APIs page lists it as a Studio resource, alongside Aladdin Data eXchange for bulk delivery, and gives little detail on either 23."

---

## Page 6

### 6.1 (Fix) Exhibit 5 column headers "Alpha, Beta, Stable, Sunset" are never defined

Current: column headers and source note as printed.

Trying to say: These are the maturity labels in the specifications, and most of the catalog is not yet stable.

Rewrite, add to the source note (author to confirm the labels are from the specifications): "Alpha, beta, stable and sunset are the maturity labels each specification carries."

### 6.2 (Stop) The "specifications say more than their count" paragraph lists five technical facts and never states what they add up to

Current: "The specifications say more than their count. Every one is tagged Access.Internal, a label BlackRock does not explain in public 17. Posting an order takes whatIf and runCompliance, which defaults to true, and returns compliance violations inline 17. Ten specifications expose a long-running-operations endpoint and 35 operations are flagged for it; the SDK polls them 24. Risk exceptions and ADC datasets carry bitemporal fields; rule assignments and dataset releases name a four-eyes approval 17. Every request carries an application key plus OAuth 2.0 scopes such as trading.order_management.order.v1.Order:read, and the client ID and secret come from the Studio UI 24."

Trying to say: Reading inside the specifications shows they are built for governed production use by an existing client's engineers, not for a stranger to try. (The conclusion is implied; the closing line of the next paragraph, "These are the needs of a client’s engineering team," is the nearest statement of it.)

Rewrite (conclusion sentence marked for the author to confirm): "The specifications say more than their count. Every one is tagged Access.Internal, a label BlackRock does not explain in public 17. Posting an order takes whatIf and runCompliance, which defaults to true, and the response returns any compliance violations inline 17. Ten specifications expose an endpoint for long-running operations, 35 operations are flagged as long-running, and the SDK polls them 24. Risk exceptions and Data Cloud datasets carry bitemporal fields, which record both when something was true and when the system learned it. Rule assignments and dataset releases name a four-eyes approval, a second sign-off before a change takes effect 17. Every request carries an application key plus OAuth 2.0 scopes such as trading.order_management.order.v1.Order:read, and the client ID and secret come from the Studio UI 24. [Author to confirm:] Each of these is a feature of a controlled production system for an existing client, not of a product a stranger can try."

Note: the glosses for "bitemporal" and "four-eyes" are standard meanings, not new facts about Aladdin; if the author prefers no gloss, drop the "which record ..." and "a second sign-off ..." clauses but keep the rest of the split.

### 6.3 (Slow) 32-word sentence introducing Exhibit 6, and "out there" again

Current: "Exhibit 6 follows a prospect’s engineer through six steps, from first hearing about Studio to getting help, and records what is out there at each step and what follows qualification."

Rewrite: "Exhibit 6 follows a prospect’s engineer through six steps, from first hearing about Studio to getting help. For each step it records what is public today and what a client receives after qualification."

### 6.4 (Stop) SDK paragraph: 38-word sentence, "MCP toolkit" before MCP is explained, "an outside fix" with no stated target, then a 52-word sentence and a "These" with no clear referent

Current: "The SDK is the one piece that installs before any conversation. It has had 14 releases since May 2024, all alpha or beta, with the core at 2.0.0b10 in July 2026 and the add-ons at 2.0.0b3 27, 17. Each release pins an old Snowflake library, so none installs on Python 3.13, and the SDK’s dependencies conflict with the official MCP toolkit; an outside fix was merged in August 2026 and has not shipped 28. The README documents three run modes, “a developer’s local machine,” “Aladdin Studio Compute sessions” and a test mode, stores a prompted password in the operating system’s credential manager, and carries settings for firms that consume “the Aladdin APIs via an enterprise API management platform such as Azure API Management” 24. These are the needs of a client’s engineering team."

Trying to say: The SDK is the only thing a prospect can install, it is still pre-release and has install problems, and its design shows it was written for existing clients' engineers rather than for prospects.

Rewrite: "The SDK is the one piece that installs before any conversation. It has had 14 releases since May 2024, all alpha or beta. The core is at 2.0.0b10 as of July 2026 and the add-ons at 2.0.0b3 27, 17. Each release pins an old Snowflake library, so none installs on Python 3.13. The SDK’s dependencies also conflict with the official toolkit for MCP, the standard that lets outside AI tools call a vendor’s APIs. An outside contributor’s fix for the conflict was merged in August 2026 and has not shipped 28. The README documents three run modes: “a developer’s local machine,” “Aladdin Studio Compute sessions” and a test mode. It stores a prompted password in the operating system’s credential manager. It carries settings for firms that consume “the Aladdin APIs via an enterprise API management platform such as Azure API Management” 24. Run modes, credential storage and API-gateway settings are the needs of a client’s engineering team, not of a prospect."

Notes: (a) the MCP gloss repeats the meaning Exhibit 7's footnote gives ("an MCP server or connector that outside AI tools can use"); if MCP is defined earlier in a revised draft, drop it here. (b) Author to confirm the August 2026 fix addresses the dependency conflict rather than the Python 3.13 problem; the current sentence does not say which. (c) "not of a prospect" states the implied contrast; drop it if the author prefers the softer original.

---

## Page 7

### 7.1 (Slow) Exhibit 6, Read row: three quoted phrases with no indication they are page headings

Current: "The Studio page: “Create & automate,” “Make Aladdin your own,” “Align internally & externally”; the APIs page: “dozens of APIs”"

Rewrite (author to confirm the three phrases are the page's section headings): "The Studio page, whose three sections are “Create & automate,” “Make Aladdin your own” and “Align internally & externally”; the APIs page, which promises “dozens of APIs”"

### 7.2 (Fix) Exhibit 6, See the catalog row: the cell hides the effort

Current: "54 specifications, by unpacking the 11 PyPI add-on packages"

Rewrite: "The 54 specifications, but only by unpacking the 11 PyPI add-on packages"

### 7.3 (Fix) Exhibit 6, Try row, After qualification: a list with no verb, and "the client’s Aladdin host" tacked on

Current: "Studio Compute, an API token or OAuth application “registered via Studio UI,” the client’s Aladdin host"

Rewrite: "Studio Compute; an API token or an OAuth application “registered via Studio UI”; and the client’s own Aladdin host to call"

### 7.4 (Fix) Exhibit 6, Build row, After qualification: colon fragment

Current: "Every call: the SDK needs a client host and credentials"

Rewrite: "A client host and credentials, which the SDK needs for every call"

### 7.5 (Fix) Exhibit 6, Get help row: two quoted button labels with no context

Current: "GitHub issues and pull requests on the SDK, answered by BlackRock engineers; “Book a meeting” and “Download the brochure”"

Rewrite: "GitHub issues and pull requests on the SDK, answered by BlackRock engineers; on the Studio page, two buttons, “Book a meeting” and “Download the brochure”"

### 7.6 (Stop) Exhibit 6 source note: "the right-hand column" is the Receipt column, but the sentence describes the After qualification column

Current: "Source: the pages and repositories in the Receipt column, read with no account or login, October 2026; the right-hand column is what they say a client receives, not tested."

Rewrite: "Source: the pages and repositories in the Receipt column, read with no account or login, October 2026. The After qualification column is what those sources say a client receives; I did not test it."

### 7.7 (Fix) Exhibit 7, column header "Call to action" is ambiguous (a button? a sales call?)

Current: "Call to action"

Trying to say: Whether the public page offers a developer a next step to take on their own.

Rewrite (author to confirm the criterion): "Developer call to action" or "Next step offered to developers". If space is tight, keep the header and add one line under the legend: "Call to action: a public next step for a developer, such as a sign-up or a get-started button."

### 7.8 (Fix) Exhibit 7 footnote: "MCP server" is undefined at this point in the document

Current: "For the AI connector, 2 means an MCP server or connector that outside AI tools can use; 1 means one announced or in limited release; 0 means none, or an assistant that works only inside the vendor’s own platform."

Rewrite: "For the AI connector, 2 means a connector that outside AI tools can use, such as an MCP server; 1 means one announced or in limited release; 0 means none, or an assistant that works only inside the vendor’s own platform."

### 7.9 (Fix) Exhibit 7 source note: "underrated" reads as an opinion about the vendor

Current: "Bloomberg, Clearwater and MSCI may be underrated: some pages blocked automated access."

Rewrite: "Bloomberg, Clearwater and MSCI may score lower than they deserve, because some of their pages blocked automated access."

---

## Page 8

### 8.1 (Stop) Exhibit 7 commentary: the "total" is described as a count of criteria met, but the table sums scores of 0 to 2 (maximum 16); then a colon list and a 29-word sentence of vendor names

Current: "Exhibit 7 puts Studio beside 10 platforms that a Studio buyer also deals with, on eight things a developer with no client relationship can reach 32, 33, 34. The total counts how many of the eight criteria a developer can meet before any client relationship exists, so it measures each vendor’s selling model. Investment platforms cluster low because they gate: documentation, a sandbox and a first call follow a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium. Data and cloud platforms, which sell to developers directly, cluster high. Only Studio, among the investment platforms, offers an open-source SDK 24."

Trying to say: The score measures how much a vendor opens to developers before a sale; investment platforms open little, data and cloud platforms open a lot, and Studio's one distinction among investment platforms is its open-source SDK.

Rewrite: "Exhibit 7 puts Studio beside 10 platforms that a Studio buyer also deals with 32, 33, 34. It scores each on eight things a developer with no client relationship can reach, from 0 to 2, so the total runs from 0 to 16. A high total means the vendor opens to developers before any sale; a low total means access follows a relationship. So the total measures each vendor’s selling model. Investment platforms cluster low because they gate. At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, documentation, a sandbox and a first call come after a relationship exists. Data and cloud platforms sell to developers directly and cluster high. Among the investment platforms, only Studio offers an open-source SDK 24."

### 8.2 (Stop) "Five BlackRock speakers define Studio on the record in the 128 recordings pulled for this document, with the titles the recordings give": the trailing phrase dangles, and "128 recordings" is introduced in passing

Current: "Five BlackRock speakers define Studio on the record in the 128 recordings pulled for this document, with the titles the recordings give 29, 30."

Trying to say: The author reviewed 128 recordings; five BlackRock speakers define Studio in them; Exhibit 8 lists them with the job titles the recordings use.

Rewrite: "I pulled 128 recordings for this document 29, 30. Five BlackRock speakers define Studio in them. Exhibit 8 lists each speaker with the title the recording gives."

### 8.3 (Fix) Exhibit 8, column header "What they add": add to what?

Current: "What they add"

Rewrite: "What each adds to the definition"

### 8.4 (Fix) Exhibit 8, Woodhead row: "three-pillar" and "citizen developers" are shorthand

Current: "The three-pillar definition; 3,000 internal citizen developers"

Rewrite: "The three-part definition quoted on page 4; 3,000 “citizen developers” inside BlackRock" (Author to confirm "citizen developers" is Woodhead's phrase; if not, write "3,000 non-engineers inside BlackRock who build on Studio".)

### 8.5 (Fix) Exhibit 8 and Exhibit 9 source notes: "marked in the register" assumes the reader knows a register exists

Current (Exhibit 8): "Quotations are verbatim from the transcripts; three of the five are machine transcriptions, marked in the register."
Current (Exhibit 9): "Quotations are verbatim; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked in the register."

Rewrite (both): replace "marked in the register" with "marked as such in the source register at the end of this document" (author to confirm the register's location and name).

### 8.6 (Stop) "Four of them describe Studio with the same three parts": 44 words, four semicolon clauses, and "so the positioning exists" is abstract

Current: "Four of them describe Studio with the same three parts: Woodhead names them outright 5; Newman calls Data Cloud “part of Studio” 15; Goel describes events, APIs and a near-real-time data store 25; Khara calls it programmatic access to data and reporting 40. A 2026 job posting calls Studio “Aladdin’s extensibility layer” 42. The message is consistent across speakers and years, so the positioning exists. Learning about Studio from outside takes effort: the catalog is unpacked from packages, the definitions transcribed from recordings, and nothing can be run."

Trying to say: BlackRock already has a consistent positioning for Studio; the problem is not the message but how hard it is to find and test from outside.

Rewrite: "Four of the five describe Studio with the same three parts. Woodhead names them outright 5. Newman calls Data Cloud “part of Studio” 15. Goel describes events, APIs and a near-real-time data store 25. Khara calls it programmatic access to data and reporting 40. A 2026 job posting calls Studio “Aladdin’s extensibility layer” 42. The message is the same across speakers and years, so BlackRock already has a positioning for Studio. What it lacks is reach. Learning about Studio from outside takes effort. The catalog has to be unpacked from packages. The definitions have to be transcribed from recordings. Nothing can be run."

Note: "What it lacks is reach" states the implied contrast; drop it if the author prefers not to add the gloss.

### 8.7 (Fix) Terminology drifts: "three parts" (page 3), "three pillars" (Exhibit 8, Exhibit 9 title), "one pillar" (Exhibit 4), "the same three parts" (page 8)

Rewrite: pick one word and use it everywhere. "Three parts" is plainer; if "pillars" stays, introduce it once on page 3: "It has three parts, which this document calls the three pillars."

### 8.8 (Fix) Exhibit 9, Developer tools column: "–" is used where the other columns use "Yes", and no legend says what "–" means

Current: "–" in the Developer tools column for Khara and Newman.

Rewrite: "No", or add to the source note: "– means the speaker does not name that part."

---

## Exhibit titles, current and proposed

Each proposed title states the finding in one sentence. All are drawn from the exhibit's own cells and notes.

| Exhibit | Current title | Proposed title |
|---|---|---|
| 1 | One core engine with separate entry points for each kind of buyer | BlackRock sells one engine through eight named products, and Studio is the entry point for people who write code |
| 2 | One trade, start to finish: the team, the named application and the public API at each step | The public APIs cover a trade from order to NAV, but they name no order screen and hold no position or event API |
| 3 | Studio sits between the people who build and the system of record | Studio is the layer between the people who build on Aladdin and the one record of holdings underneath, with Copilot above it and governance across every layer |
| 4 | Eight pieces, from read-and-write APIs to an Excel add-in | Studio has eight pieces, and the catalog, guides, notebooks and samples all sit behind a client login |
| 5 | The public catalog: 54 specifications across 11 domains | Investment operations and analytics hold 127 of the 301 public operations, and only 23 of the 54 specifications are stable |
| 6 | Six steps a prospect’s developer takes, before and after qualification | A prospect’s developer can hear about Studio, read the pages and unpack the catalog, but cannot run anything until qualified |
| 7 | Several access models coexist in this market: what a developer with no client relationship can reach, on eight criteria | Studio scores 4 of 16 on access for non-client developers, level with State Street, below Bloomberg, and far below every data and cloud platform but MSCI |
| 8 | The five BlackRock speakers who define Studio on the record | Five BlackRock executives have defined Studio on the record since early 2024, and the head of Studio engineering gave the fullest definition in November 2025 |
| 9 | Four BlackRock speakers, 2024 to 2025, and the three pillars each names | All four speakers name APIs and events and the Data Cloud; only Goel and Woodhead name developer tools |

Checks on the proposed titles: Exhibit 5, 74 + 53 = 127 operations and the Stable column sums to 23 (2+8+0+4+3+2+1+1+1+0+1). Exhibit 7, Studio 4, State Street 4, Bloomberg 5, MSCI 2, other data and cloud platforms 9 to 16. Exhibit 8, Khara's interview is early 2024 and Woodhead's podcast November 2025.

---

## Items noted but not rewritten

- Page 4, the Woodhead quotation is verbatim from a machine transcript ("a set of APIs events"). Leave it, but the bridge sentence in 4.1 gives the reader the plain version.
- Page 5, Exhibit 3 is a diagram; its cells are fragments by design and read fine except 5.1 and 5.2.
- Page 6, Exhibit 5 cells are numbers and API names; nothing to rewrite beyond 6.1.
- Page 7, Exhibit 7 legend ("2: Fully public or self-serve ...") is clear.
- Footer line on every page reads cleanly.

---

# Readability pass: page 9 (Finding 1, Exhibits 10 and 11, direction box)

Read against the extracted text and the page image (heading, body, both exhibits with legend, source notes, table cells, direction box, footer). Underlined link phrases on the page, which the rewrites keep in place: "Studio page", "full-text search of SEC EDGAR", "the Snowflake implementation", "proxy statement", "$25.6 million in 2025", "in 2016 it said it was connecting to Aladdin" (source note), "open-source SDK", "URL rewriting and custom headers", "launch post", "commits", "10-K", "UK Pension Protection Fund", "Nest (UK)", "US Pension Benefit Guaranty Corporation".

Convention below: superscripts are written as [n]; underlined link phrases are marked with _underscores_.

---

## Passages

### 1. Section heading

**Page:** 9

**Current text:**
"1. Public customer proof already exists, and it is viable even though it is not Studio-specific"

**Trying to say:** Public evidence that clients use Aladdin exists today, and a sales team can use it as Studio proof even though none of it mentions Studio.

**Why it stalls:** "Viable" is abstract; the reader has to guess viable for what. "It" has to carry back to "proof" across the comma. "Customer proof" is sales jargon the reader meets before the body explains that it means named clients on the record.

**Rewrite:**
"1. Public proof that clients use Aladdin already exists, and it works as Studio proof even though none of it names Studio"

---

### 2. Opening sentence

**Page:** 9

**Current text:**
"BlackRock's _Studio page_ names no client building on Studio [13], and a _full-text search of SEC EDGAR_ finds no filing mentioning it [43]."

**Trying to say:** Neither BlackRock's own Studio page nor any SEC filing names a Studio client.

**Why it stalls:** Minor. "Mentioning it" sits after two uses of "Studio" and one of "client", so the reader briefly checks which noun "it" is.

**Rewrite:**
"BlackRock's _Studio page_ names no client building on Studio [13], and a _full-text search of SEC EDGAR_ finds no filing that mentions Studio [43]."

---

### 3. The hinge sentence

**Page:** 9

**Current text:**
"Proof of Aladdin in use is public all the same."

**Trying to say:** Even so, there is public evidence of clients using Aladdin (as distinct from Studio).

**Why it stalls:** "All the same" is a soft hinge, and "Aladdin in use" is a compressed noun phrase. The contrast the sentence depends on (Studio proof: none; Aladdin proof: plenty) is implied rather than stated.

**Rewrite:**
"Proof that clients use Aladdin, though, is public."

---

### 4. Royal London sentence

**Page:** 9

**Current text:**
"On BlackRock's client video, Royal London's chief executive credits _the Snowflake implementation_ [44]."

**Trying to say:** A named client executive, on BlackRock's own video, praises an Aladdin deployment.

**Why it stalls:** "The Snowflake implementation" has no referent on this page. Snowflake was last mentioned on page 8 inside a Woodhead quotation ("The Aladdin data cloud built on top of Snowflake"). A reader who did not retain that detail does not know what was implemented, or why it counts as Aladdin proof. "Credits" also leaves open credits it for what.

**Rewrite (keep the underlined phrase; the clarifying clause uses only what page 8 already says):**
"On BlackRock's client video, Royal London's chief executive credits _the Snowflake implementation_, the Aladdin data cloud that runs on Snowflake [44]."

Check against source 44 that the video is about the data cloud before using this wording. If it is not, the minimum fix is: "credits Aladdin's _Snowflake implementation_ [44]."

---

### 5. JPMorgan payments sentence

**Page:** 9

**Current text:**
"JPMorgan Chase's _proxy statement_ reports Aladdin payments of $4.4 million to $7.6 million a year from 2017 to 2023, then $14.7 million in 2024 and _$25.6 million in 2025_ [2, 3]."

**Trying to say:** JPMorgan's payments to BlackRock for Aladdin were flat for seven years and then more than tripled.

**Why it stalls:** Thirty words with four numbers and a range; readable in one pass but the finding (flat, then a jump) is left for the reader to compute. The source note says "proxy statements, filed 2017 to 2026", so the singular "proxy statement" in the body is inconsistent with the exhibit.

**Rewrite:**
"JPMorgan Chase's _proxy statements_ report payments for Aladdin of $4.4 million to $7.6 million a year from 2017 to 2023. The figure then jumped to $14.7 million in 2024 and _$25.6 million in 2025_ [2, 3]."

---

### 6. Exhibit 10 legend and the 2016 bar

**Page:** 9

**Current text (legend):**
"Payments for Aladdin" (yellow) / "Integration services" (grey)

**Trying to say:** The grey 2016 bar is a different kind of payment from the yellow bars.

**Why it stalls:** Nothing on the page says what "Integration services" means, why only 2016 is grey, or whether the 2016 figure should be read as part of the series. The body text starts the series at 2017, so the grey bar looks like an unexplained exception. The reader stops to work out whether to count it.

**Rewrite (one sentence added to the source note; it states only what the chart already encodes):**
Add to the source note after the first sentence: "The grey 2016 bar is a payment for integration services, not a payment for Aladdin, and is excluded from the figures in the text."

If the 2016 figure is not needed for the argument, the simpler fix is to drop the 2016 bar and the second legend entry.

---

### 7. Exhibit 10 source note, second sentence

**Page:** 9

**Current text:**
"The payments may include more than a client license: JPMorgan is also a custodian, and _in 2016 it said it was connecting to Aladdin_ to serve custody clients on the platform [45]; that report is trade press, not a JPMorgan or BlackRock document."

**Trying to say:** The payments may not all be for a client license, because JPMorgan may also pay BlackRock as a custodian connecting to Aladdin; the evidence for that is a trade-press article, not a filing.

**Why it stalls:** Forty-four words, a colon and a semicolon stacking three ideas, and "that report" has no noun to point to (the preceding clause is "it said", not "a report").

**Rewrite:**
"The payments may cover more than a client license. JPMorgan is also a custodian, and _in 2016 it said it was connecting to Aladdin_ to serve custody clients on the platform [45]. That 2016 report is trade press, not a JPMorgan or BlackRock document."

---

### 8. Janus Henderson SDK sentence

**Page:** 9

**Current text:**
"In December 2025 a Janus Henderson engineer submitted two changes to the _open-source SDK_, _URL rewriting and custom headers_, for firms that route Aladdin calls through an enterprise gateway; the BlackRock engineer who co-wrote the SDK's _launch post_ merged them, and the _commits_ carry a janushenderson.com author line [31, 46, 47, 48]."

**Trying to say:** A Janus Henderson engineer contributed code to BlackRock's SDK, BlackRock accepted it, and the public record proves who wrote it.

**Why it stalls:** Sixty-one words. The appositive "URL rewriting and custom headers" reads on first pass as two more things in a list, not as the names of the two changes. The semicolon joins three separate facts (what was submitted, who merged it, what the commits show). "Author line" is Git jargon.

**Rewrite:**
"In December 2025 a Janus Henderson engineer submitted two changes to the _open-source SDK_: _URL rewriting and custom headers_, both for firms that route Aladdin calls through an enterprise gateway. The BlackRock engineer who co-wrote the SDK's _launch post_ merged them. The _commits_ name a janushenderson.com address as the author [31, 46, 47, 48]."

---

### 9. Janus Henderson 10-K sentence

**Page:** 9

**Current text:**
"Janus Henderson's _10-K_ says the firm chose in the third quarter of 2025 to move its investment management system to Aladdin, "a complex, multi-year initiative" [49]."

**Trying to say:** Janus Henderson's own filing confirms it is moving onto Aladdin.

**Why it stalls:** Minor. "Chose in the third quarter of 2025 to move" splits verb and object with a date. One reading is enough; listed for completeness.

**Rewrite:**
"Janus Henderson's _10-K_ says that in the third quarter of 2025 the firm chose to move its investment management system to Aladdin, "a complex, multi-year initiative" [49]."

---

### 10. Bridge to Exhibit 11

**Page:** 9

**Current text:**
"Public buyers add a third record: procurement notices that score the bids."

**Trying to say:** Besides proxy statements and 10-Ks, there is a third kind of public record: procurement notices, which show how bids were scored.

**Why it stalls:** "A third record" makes the reader count back to find the first two (a proxy statement and a 10-K), which were never labelled as a list. "Score the bids" has no antecedent for "the bids".

**Rewrite:**
"Public buyers add a third kind of record. Their procurement notices show how each bid for Aladdin was scored."

---

### 11. Exhibit 11, column header "Scoring"

**Page:** 9

**Current text:**
"Scoring" (header) with cells "Technical 85, price 6, price sensitivity 6, contract terms 3" / "Quality 70, cost 20, social value 10" / "Full and open competition, four bids each time"

**Trying to say:** For the two UK rows, the numbers are the weights (out of 100) each criterion carried; the US row describes the competition format instead.

**Why it stalls:** The numbers have no unit, so a reader cannot tell whether "Technical 85" is a weight or a score Aladdin received. The third row is a different kind of content under the same header. Cells are fragments, which is acceptable in a table, but the header must do the work and "Scoring" does not.

**Rewrite:**
Header: "How bids were weighted or run"
Cells: "Technical 85%, price 6%, price sensitivity 6%, contract terms 3%" / "Quality 70%, cost 20%, social value 10%" / "Full and open competition, four bids each time"
(The percentages add nothing new: each row already sums to 100.)

---

### 12. Exhibit 11, Outcome cells

**Page:** 9

**Current text:**
"Aladdin won both lots, above the fund's own price estimate"
"Aladdin won against six other bids"
"BlackRock won both; the 2023 rebid kept the same price"

**Trying to say:** Aladdin won every contest; in the PPF case at a price above the buyer's estimate; in the PBGC case twice, with no price change on rebid.

**Why it stalls:** "Above the fund's own price estimate" can read as "won by a margin above" rather than "at a price above". "Won both" in row three refers to two years, not two lots, so the same word means different things two rows apart. Rows one and two say "Aladdin won", row three says "BlackRock won".

**Rewrite:**
"Aladdin won both lots, at a price above the fund's own estimate"
"Aladdin won against six other bids"
"Aladdin won in 2017 and again in 2023; the 2023 rebid kept the same price"

---

### 13. "None of this is Studio-specific" paragraph, first two sentences

**Page:** 9

**Current text:**
"None of this is Studio-specific, and that matters less than it looks. Studio is sold for custom applications on Aladdin, and a buyer wants to know that another institution built on the platform and stayed; in custom-application land, proof from one firm counts even for a dissimilar buyer."

**Trying to say:** The evidence does not mention Studio, but that is not a big problem, because what a Studio buyer needs to see is that some institution built on Aladdin and stayed, whoever that institution is.

**Why it stalls:** "That" in sentence one points at a whole clause. Sentence two is 42 words with a semicolon stacking the premise and the conclusion. "Custom-application land" is colloquial; "a dissimilar buyer" is abstract (dissimilar to what?).

**Rewrite:**
"None of this proof names Studio. That matters less than it seems. Studio is sold for building custom applications on Aladdin, so a buyer wants to know that another institution built on the platform and stayed. For custom applications, proof from one firm counts even when the buyer is a different kind of firm."

---

### 14. Same paragraph, last sentence

**Page:** 9

**Current text:**
"Public pension funds, and firms whose filings or tenders already name BlackRock, can be named publicly more easily, and are the natural first candidates for a named Studio story."

**Trying to say:** Start with clients who are already on the public record, because they are easiest to name.

**Why it stalls:** Thirty words; the subject is split from its verb by a 10-word aside; "can be named publicly more easily" is passive with no agent (named by whom?).

**Rewrite:**
"Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public. They are the natural first candidates for a named Studio story."

---

### 15. Direction box

**Page:** 9

**Current text:**
"**What it suggests about direction.** Adoption is growing in client types whose records are public: a bank's proxy statement, an asset manager's 10-K and three pension funds' notices all record Aladdin between 2023 and 2025. Named proof for Studio can start where the relationship is already on the record."

**Trying to say:** The public record shows Aladdin adoption rising among banks, asset managers and pension funds; the first named Studio reference should come from one of those.

**Why it stalls:** The colon makes the reader hold "adoption is growing" while a three-item list arrives, and the list ends with a date range that attaches to the list, not to the growth claim. "It" in the box label refers to the finding; this appears to be a document-wide label, so change it everywhere or not at all.

**Rewrite:**
"**What this finding suggests about direction.** Adoption is growing among client types whose records are public. Between 2023 and 2025, a bank's proxy statement, an asset manager's 10-K and three pension funds' procurement notices all record Aladdin. Named proof for Studio can start where the relationship is already on the record."

---

### 16. Footer (no change needed)

"Independent analysis from public sources. Not produced, reviewed or endorsed by BlackRock." Clear. Listed only to confirm it was read.

---

## Exhibit titles

| Exhibit | Current title | Proposed title (states the finding) |
|---|---|---|
| 10 | "JPMorgan Chase payments to BlackRock for Aladdin, $ millions" | "JPMorgan Chase paid BlackRock under $8 million a year for Aladdin from 2017 to 2023, then $14.7 million in 2024 and $25.6 million in 2025" (keep "$ millions" as an axis label, not in the title) |
| 11 | "Public buyers that scored Aladdin bids" | "Three public pension bodies scored Aladdin bids in open competitions between 2017 and 2025, and Aladdin won every one" |

Both proposed titles use only figures already on the page. For Exhibit 11, "won every one" covers PPF (both lots), Nest (one award) and PBGC (2017 and 2023).

## Two consistency notes for the editor (not readability, but caught on this pass)

1. Body says "proxy statement" (singular); the Exhibit 10 source note says "proxy statements (DEF 14A), filed 2017 to 2026". Make them agree.
2. Exhibit 11 switches between "Aladdin won" and "BlackRock won" across rows; the direction box then calls Nest, PPF and PBGC "three pension funds". PBGC is a US federal pension insurer rather than a fund; "three pension bodies" or "three public pension buyers" avoids the quibble.

---

# Readability pass: page 10 (Finding 2, Exhibit 12, direction box)

Conventions: superscripts shown as [n]; underlined link phrases shown in _underscores_ where I could see them in the page image. Rewrites keep every superscript and link phrase in place. Nothing below adds a fact; where a rewrite makes an implied conclusion explicit, it says so.

Underlined link phrases identified on this page: _2025 Investor Day_, _Studio page_, _26 earnings calls_, _2023 Investor Day slide_ (body and exhibit), _10-K_, _Q3 2022_, _Q4 2024_, _Q4 2021_, _Q4 2023_, _third-party transcripts of BlackRock earnings calls_ (source note), _client webinar_, _Private credit analytics on Preqin_, _Data Cloud_ (in "joining Data Cloud", appears underlined), _all BlackRock's technology platform clients and services are hosted in the Azure cloud_, _general availability for US-hosted Aladdin Enterprise clients expected in the second half of 2026_.

---

## 1. Finding heading

**Page:** 10

**Current text:**
> 2. BlackRock's growth story is API consumption and the whole portfolio, and Studio is the vehicle even when it is not named

**Trying to say:** BlackRock tells investors its growth comes from API calls and from covering public and private markets together; both run through Studio, although BlackRock rarely says the name.

**Problem:** Three ideas joined by two "and"s in one 22-word line. "The vehicle" is a metaphor the reader has to decode; "when it is not named" does not say named by whom or where.

**Rewrite:**
> 2. BlackRock tells investors growth will come from API calls and the whole portfolio. Both run through Studio, though BlackRock rarely says the name

---

## 2. Opening sentence of the finding

**Page:** 10

**Current text:**
> At its _2025 Investor Day_, on a slide about keeping the cost of growth low, BlackRock projected that API calls across BlackRock and Aladdin would grow 17x by 2030, against 4x for model portfolios, 2x for portfolios and 1.3x for trade allocations.

**Trying to say:** API calls are the fastest-growing measure on BlackRock's 2025 Investor Day slide.

**Problem:** 43 words. Two qualifying clauses ("At its...", "on a slide about...") come before the point. The three comparators trail after the headline number and the reader has to work out that 17x is the largest.

**Rewrite:**
> BlackRock projected at its _2025 Investor Day_ that API calls across BlackRock and Aladdin would grow 17x by 2030 [1]. That was the fastest-growing measure on the slide, which was about keeping the cost of growth low. Model portfolios were projected at 4x, portfolios at 2x and trade allocations at 1.3x.

(Superscript [1] currently sits at the end of the third sentence of the paragraph; moving it here keeps it on the slide claim. If the author prefers, leave it where it is and the first sentence stands without a superscript.)

---

## 3. The inference sentences

**Page:** 10

**Current text:**
> The slide gave no starting number and does not say which products generate the API calls, so attributing them to Studio is my inference [1]. API use is the activity the _Studio page_ describes [13].

**Trying to say:** The slide does not name Studio; I link the API calls to Studio because the Studio page is about API use.

**Problem:** The second sentence is the reason for the first, but the connection is implied, not stated. A reader skimming sees two unrelated facts. Mixed tense ("gave" / "does not say").

**Rewrite:**
> The slide gives no starting number and does not say which products generate the API calls. Attributing them to Studio is my inference [1]. I make it because API use is the activity the _Studio page_ describes [13].

---

## 4. Earnings-call sentence

**Page:** 10

**Current text:**
> Across _26 earnings calls_ from the first quarter of 2020 to the second quarter of 2026, no executive said "Studio" [4]; a single line on a _2023 Investor Day slide_ is the only other investor mention found [53].

**Trying to say:** Executives never said "Studio" on an earnings call; outside the calls, the only investor-facing mention I found is one line on a 2023 slide.

**Problem:** 40 words with a semicolon. "The only other investor mention" has no clear referent: other than what? The calls had zero mentions, so "other" reads as a contradiction. The reader has to infer that "other" means "outside the earnings calls".

**Rewrite:**
> No executive said "Studio" on any of the _26 earnings calls_ from the first quarter of 2020 to the second quarter of 2026 [4]. Outside the calls, the only investor-facing mention I found is a single line on a _2023 Investor Day slide_ [53].

---

## 5. 10-K sentence

**Page:** 10

**Current text:**
> BlackRock's _10-K_ says technology services fees are generally set by the value of positions on the platform or at a fixed rate, and can depend on subscriptions, go-lives and support; API calls appear in none of those terms [10], [1].

**Trying to say:** BlackRock does not charge by API call, so the fastest-growing measure on the slide is not one it says it bills for.

**Problem:** 40 words with a semicolon. The point of the sentence (why the reader should care that API calls are absent from the fee terms) is left implied. "Those terms" is a loose referent.

**Rewrite:**
> BlackRock's _10-K_ says technology services fees are generally set by the value of positions on the platform or at a fixed rate. They can also depend on subscriptions, go-lives and support. API calls appear in none of those fee terms [10], [1].

(Optional, makes the implied conclusion explicit; the author should confirm it is the intended point: "So the measure BlackRock is growing fastest is not one it says it charges for.")

---

## 6. Exhibit 12, Studio row, Context cell

**Page:** 10

**Current text:**
> One line on a _2023 Investor Day slide_ is the only other investor mention found [53]

**Trying to say:** Never said on a call; the one investor-facing mention found anywhere is a line on a 2023 slide.

**Problem:** Same "other" problem as item 4, worse inside a table where the cell has no sentence before it to refer back to. The cell is a fragment without a subject.

**Rewrite:**
> Never on a call. The only investor-facing mention found is one line on a _2023 Investor Day slide_ [53]

---

## 7. Exhibit 12, Data Cloud row, Context cell

**Page:** 10

**Current text:**
> _Q3 2022_ [54] and _Q4 2024_ [55], as an add-on sold with Aladdin Enterprise

**Trying to say:** Mentioned twice, both times described as an add-on sold with Aladdin Enterprise.

**Problem:** Fragment; "as an add-on" could be read as describing the mention or the product.

**Rewrite:**
> _Q3 2022_ [54] and _Q4 2024_ [55], both times described as an add-on sold with Aladdin Enterprise

---

## 8. Exhibit 12, source note

**Page:** 10

**Current text:**
> Source: _third-party transcripts of BlackRock earnings calls_, Q1 2020 to Q2 2026 [4]. My tally. Zero counts are reliable; other counts are approximate.

**Trying to say:** I counted these myself; a zero means the word is absent from every transcript, while non-zero counts may be off by one or two.

**Problem:** Clear enough, but "Zero counts are reliable" leaves the reader asking why zeros are more reliable than ones. Low priority.

**Rewrite:**
> Source: _third-party transcripts of BlackRock earnings calls_, Q1 2020 to Q2 2026 [4]. My tally. A zero means the term appears in no transcript; the non-zero counts are approximate.

---

## 9. "Whole portfolio" opener of the second paragraph

**Page:** 10

**Current text:**
> The other half of the growth story is the whole portfolio.

**Trying to say:** The second growth driver is covering public and private markets in one system.

**Problem:** "The whole portfolio" was defined on page 2 ("public and private") but is used here as a bare label; a reader who opened to this page does not know what it means.

**Rewrite:**
> The other half of the growth story is the whole portfolio, public and private markets together.

---

## 10. The eFront / Preqin webinar sentence

**Page:** 10

**Current text:**
> BlackRock bought eFront in 2019 and Preqin in 2025, and in September 2025 its private markets team described the result on a _client webinar_: investors "now have access to over 15,000 fund investments within eFront Insight" for benchmarking; Preqin indices "are also available today in Aladdin Explore and our Aladdin Data Cloud capabilities"; and "over 10 different transaction types" were added to Aladdin, across commitments, fundings, paydowns and PIK, so private credit loans are captured natively, designed with BlackRock's own professionals and "our new colleagues from HPS" [6].

**Trying to say:** After buying eFront and Preqin, BlackRock put private-markets data into Explore and Data Cloud and added private-credit transaction types to Aladdin.

**Problem:** About 90 words in one sentence: a colon, three semicolon-separated items, a "so" clause and a dangling "designed with" participle whose subject is unclear (the transaction types? the loans?). "PIK" and "HPS" are unexplained abbreviations. The sentence stacks five facts.

**Rewrite:**
> BlackRock bought eFront in 2019 and Preqin in 2025. In September 2025 its private markets team described the result on a _client webinar_ [6]. Investors "now have access to over 15,000 fund investments within eFront Insight" for benchmarking. Preqin indices "are also available today in Aladdin Explore and our Aladdin Data Cloud capabilities". And "over 10 different transaction types" were added to Aladdin, covering commitments, fundings, paydowns and PIK, so private credit loans are captured natively. The team said those were designed with BlackRock's own professionals and "our new colleagues from HPS" [6].

(Superscript [6] is repeated so that each quoted passage stays anchored; if the register allows one anchor only, keep the final one. The author should consider glossing "PIK" and "HPS" on first use; I have not added glosses because they would be new facts.)

---

## 11. "Newman lists" sentence

**Page:** 10

**Current text:**
> Newman lists eFront data and Preqin among what is joining _Data Cloud_ [15].

**Trying to say:** The Studio general manager says eFront and Preqin data are being added to Data Cloud.

**Problem:** Newman was introduced on page 3; seven pages later the bare surname stalls the reader. "Among what is joining" is an abstract construction.

**Rewrite:**
> Newman, the Studio general manager, names eFront data and Preqin among the data being added to _Data Cloud_ [15].

---

## 12. Hosting sentence

**Page:** 10

**Current text:**
> Hosting moved the same way: Microsoft wrote in December 2024 that _all BlackRock's technology platform clients and services are hosted in the Azure cloud_, with new rollouts taking "weeks instead of quarters" [58], and in December 2025 BlackRock and AWS announced a second option, with _general availability for US-hosted Aladdin Enterprise clients expected in the second half of 2026_ [14].

**Trying to say:** The platform has also moved to public cloud: Azure since 2024, with AWS coming in 2026.

**Problem:** About 60 words after a colon. "Moved the same way" has no clear referent; the paragraph before is about data being added, not about anything "moving". The paragraph never says why hosting belongs in a finding about API calls and the whole portfolio, so the reader is left to guess the link.

**Rewrite:**
> Hosting has moved to the public cloud as well. Microsoft wrote in December 2024 that _all BlackRock's technology platform clients and services are hosted in the Azure cloud_, with new rollouts taking "weeks instead of quarters" [58]. In December 2025 BlackRock and AWS announced a second option, with _general availability for US-hosted Aladdin Enterprise clients expected in the second half of 2026_ [14].

(The author should add one clause saying why hosting matters to this finding, if it does; I could not infer it from the page, so I have not supplied one.)

---

## 13. Direction box

**Page:** 10

**Current text:**
> What it suggests about direction. Extensibility and data access are where BlackRock itself says growth is. The fastest-growing measure it showed investors is API calls, and the data it is adding, private markets and Preqin, arrives through Data Cloud and Explore, which are Studio's surfaces. Studio is the vehicle for that story whether or not the name appears.

**Trying to say:** BlackRock's own growth claims point at API access and data; both reach clients through parts of Studio, so Studio carries the growth story even unnamed.

**Problem:** The middle sentence is 35 words with an interrupting appositive ("private markets and Preqin") and a trailing relative clause. "Studio's surfaces" is jargon not used before in this sense. "The vehicle for that story" repeats the heading's metaphor; "that story" and "the name" have soft referents.

**Rewrite:**
> What it suggests about direction. BlackRock itself says growth will come from extensibility and data access. The fastest-growing measure it showed investors is API calls. The data it is adding, private markets and Preqin, arrives through Data Cloud and Explore, and both of those are part of Studio. So Studio carries the growth story even when BlackRock does not say its name.

---

## Exhibit titles in range

| Exhibit | Current title | Proposed title (states the finding) |
|---|---|---|
| Exhibit 12 | Mentions of Studio terms on 26 BlackRock earnings calls, Q1 2020 to Q2 2026 | On 26 earnings calls from Q1 2020 to Q2 2026, no BlackRock executive said "Studio", "citizen developer" or "agent"; Data Cloud, API and Copilot came up four times in total |

Shorter alternative if the layout needs one line: "No BlackRock executive has said 'Studio' on 26 earnings calls since 2020; related terms came up four times in total".

---

## Minor notes (no rewrite proposed)

- "against 4x for model portfolios, 2x for portfolios" places two near-identical labels side by side; this is the slide's wording, so it should stand, but the reader may pause on it.
- "API calls across BlackRock and Aladdin" does not say whether "BlackRock" means BlackRock's own internal use; the slide presumably does not either, so leave it.
- "_Private credit analytics on Preqin_ followed in May 2026 [12]" reads as "analytics about Preqin" rather than "analytics built on Preqin data"; if the latter is meant, "on Preqin data" would be clearer, but the underlined phrase would change, so I leave it to the author.

---

# Readability pass: pages 11 and 12 (Finding 3, Exhibits 13 to 15, direction box)

Checked against `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/review4/text.txt` (lines 575 to 678) and a 150 dpi render of pages 11 and 12 from `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.pdf` (same build as the text file, 21:26 UTC). Every word on both pages was read, including the running footer, the source notes and the receipt column.

Underlined link phrases on these pages, which every rewrite below keeps intact and in place: "Aladdin Copilot"; "couple of thousands agents and tools," (twice, body and Exhibit 13); "There's no copilot without plug-ins"; "the data model itself is structured for agentic use cases"; "what is my exposure to aerospace in Portfolio 1?"; "say, 20 to 30 tools and agents,"; "over a planning and action node"; "never provide investment advice"; "MCP"; "90 customers connected"; "Forward Deploy Engineer posting"; and the nine receipt-column links in Exhibit 14. Exhibit 15 and the direction box carry superscripts only, no underlines.

Priority order, if only some of this gets done: items 15, 16 and 17 (the direction box, which is the payoff of the finding and the hardest to read once), then 2 and 3 (the opening paragraph, which buries the finding's key sentence), then 9 and 10 (the paragraph that introduces the outside model), then 11 to 14 (Exhibit 15 cells), then flag A (Exhibit 14 title versus its rows).

---

## Passages

### 1. Page 11, section heading

**Current text:** "3. BlackRock has built an AI front door and keeps it inside the platform, while data providers market theirs outside"

**Trying to say:** BlackRock's AI entry point (Copilot) is only reachable from inside Aladdin; its data-provider rivals sell AI entry points that outside tools can reach.

**Assessment:** Readable; 20 words, one contrast. "Theirs" has to be carried back across the comma to "AI front door", and "front door" is a metaphor the reader last saw on page 2. Optional tightening only.

**Rewrite (optional):** "3. BlackRock keeps its AI front door inside the platform; data providers market theirs outside"

### 2. Page 11, opening paragraph, second sentence (53 words)

**Current text:** "Two of its engineers, Brennan Rosales, AI Engineering Lead, and Pedro Vicente Valdez, Principal AI Engineer, describe a plugin registry with "couple of thousands agents and tools," where the first way a team onboards is "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" 9."

**Trying to say:** Copilot works from a registry of thousands of tools, and the standard way an engineering team adds a tool is to wrap an existing production Aladdin API.

**Why it stops the reader:** Four ideas in one sentence (two names with titles, the registry, its size, how teams join it). "Plugin registry" and "onboards" arrive before either is explained; "a team onboards" leaves the reader asking onboards to what. The quotation is 24 words of conference speech inside a 53-word sentence.

**Rewrite:** "Two of its engineers, Brennan Rosales, AI Engineering Lead, and Pedro Vicente Valdez, Principal AI Engineer, describe how it works. Copilot draws on a registry of plugins, "couple of thousands agents and tools," built by Aladdin's engineering teams. The first way a team adds a tool is "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" 9."

### 3. Page 11, opening paragraph, third sentence (the finding's key claim)

**Current text:** "Copilot's tools are Studio's APIs; Microsoft's Adrian Crockett put it in one line on BlackRock's podcast: "There's no copilot without plug-ins" 59."

**Trying to say:** The tools Copilot calls are the same APIs Studio sells, so Copilot is built on Studio.

**Why it stops the reader:** This is the sentence the whole finding rests on, and it is buried after a 53-word sentence, welded by a semicolon to a quote that does not quite say the same thing (Crockett says Copilot needs plug-ins; he does not say the plug-ins are Studio's APIs). "Put it in one line" asks the reader to work out what "it" is.

**Rewrite:** "So Copilot's tools are Studio's APIs. Microsoft's Adrian Crockett made the dependence plain on BlackRock's podcast: "There's no copilot without plug-ins" 59."

(Consider also opening the paragraph with this sentence, so the finding is stated before the evidence: "Copilot's tools are Studio's APIs. Aladdin Copilot is "now available ..."")

### 4. Page 11, opening paragraph, fourth sentence

**Current text:** "BlackRock's AI product head says the team is making sure "the data model itself is structured for agentic use cases" 60."

**Trying to say:** BlackRock is shaping its data so AI agents can use it, which is the same direction as Copilot's plugin model.

**Assessment:** Clear enough. "Agentic use cases" is inside a quotation and cannot be changed. The only gap is that the sentence does not say why it is here; a four-word lead-in fixes that.

**Rewrite:** "The data layer is being shaped the same way: BlackRock's AI product head says the team is making sure "the data model itself is structured for agentic use cases" 60."

### 5. Page 11, Exhibit 13, box 1

**Current text:** "One question, with the app, portfolio and widgets on screen; the talk's example is "what is my exposure to aerospace in Portfolio 1?" 9"

**Trying to say:** The user asks one question, and Copilot also gets what is open on screen (the app, the portfolio, the widgets) as context.

**Why it stops the reader:** "With the app, portfolio and widgets on screen" reads as scene-setting, not as an input to the system, so the reader does not learn why it is mentioned.

**Rewrite:** "One question, plus what is on screen: the open app, portfolio and widgets go in as context. The talk's example is "what is my exposure to aerospace in Portfolio 1?" 9"

### 6. Page 11, Exhibit 13, box 3

**Current text:** "20 to 30 candidates: filtering by environment, user group and app leaves "say, 20 to 30 tools and agents," since more than "40, 50 tools" would hurt performance 9"

**Trying to say:** Copilot narrows the thousands of tools to 20 or 30 that fit the user's environment, group and app, because the model performs badly with more.

**Why it stops the reader:** "Candidates" for what is not said. "Filtering ... leaves" has no actor. "Hurt performance" is ambiguous between speed and answer quality; the talk means the model's answers.

**Rewrite:** "20 to 30 tools in play: Copilot filters the registry by environment, user group and app, leaving "say, 20 to 30 tools and agents," because giving the model more than "40, 50 tools" would hurt its answers 9"

(If "hurt its answers" is more than the talk supports, keep "would hurt performance".)

### 7. Page 11, Exhibit 13, box 4

**Current text:** "Plan and call the API: the orchestrator iterates "over a planning and action node" with GPT-4 function calling, then output guardrails check for hallucinations 9"

**Trying to say:** A controlling component plans which tool to call and calls it, in a loop, and a final check screens the answer for invented content.

**Why it stops the reader:** Three unexplained terms in 25 words ("orchestrator", "GPT-4 function calling", "output guardrails"). An executive can follow the box only if told what each does.

**Rewrite:** "Plan and call the API: an orchestrator, the component that decides which tool to call, loops "over a planning and action node" using GPT-4's function calling; a final check, the output guardrails, screens the answer for hallucinations 9"

### 8. Page 11, Exhibit 13, box 5 and source note

**Current text (box 5):** "One answer, never investment advice: the system prompt is tested so Copilot will "never provide investment advice" 9; the product page says the same 16"

**Trying to say:** Copilot's standing instructions are tested to make sure it refuses to give investment advice.

**Assessment:** Readable. "System prompt" is the one term an executive may not know; a three-word gloss fixes it. Source note is clear.

**Rewrite:** "One answer, never investment advice: Copilot's standing instructions (its system prompt) are tested so it will "never provide investment advice" 9; the product page says the same 16"

### 9. Page 11, paragraph below Exhibit 13, sentences 1 and 2

**Current text:** "Outside the login, the data market has chosen the other model. MCP is the common standard AI assistants use to pull data from other systems 61."

**Trying to say:** Data providers have taken the opposite approach: they let outside AI tools reach their data, mostly through a standard called MCP.

**Why it stops the reader:** "The other model" has no antecedent; nothing above has called Copilot's design "a model". "The data market" is abstract (it means data providers). MCP is used before it is expanded; the expansion "Model Context Protocol (MCP)" only appears three lines later inside a job-posting quote.

**Rewrite:** "Outside the login, data providers have chosen the opposite design: they let the buyer's own AI tools reach their data. MCP, the Model Context Protocol, is the common standard AI assistants use to pull data from other systems 61."

### 10. Page 11, same paragraph, sentences 3 and 4 (33 and 30 words)

**Current text:** "Seven providers that a Studio buyer also deals with offer a connector or an MCP server; LSEG had 90 customers connected by April 2026, according to a secondary summary of its results slides 62, 63. No public connector for Aladdin was found on BlackRock's pages or GitHub 13, 64; a Forward Deploy Engineer posting for Aladdin Data names "Model Context Protocol (MCP), AI agents, and Copilot extensions" 65."

**Trying to say:** Seven providers the same buyers use have connectors; one of them already has 90 customers on it; Aladdin has none in public, and the only hint of one is a job advert.

**Why it stops the reader:** Two semicolons join four separate facts. The passive "was found" hides who looked (the author). The job posting is dropped in without saying why it matters, so the conclusion, that BlackRock is at least hiring for connector work, is implied rather than stated.

**Rewrite:** "Seven providers that Studio buyers also use offer a connector or an MCP server. LSEG had 90 customers connected by April 2026, according to a secondary summary of its results slides 62, 63. I found no public connector for Aladdin on BlackRock's pages or GitHub 13, 64. The one public hint is a job advert: a Forward Deploy Engineer posting for Aladdin Data names "Model Context Protocol (MCP), AI agents, and Copilot extensions" 65."

### 11. Page 12, Exhibit 15, "For" row, inside column

**Current text:** "Governance in one place; inherited permissions ("permission-dependent access"); no-advice guardrails tested in the system prompt; enterprise trust; a controlled rollout team by team 16, 9"

**Trying to say:** Keeping Copilot inside gives BlackRock one point of control, reuses each user's Aladdin permissions, keeps the tested no-advice guardrails, carries the trust of the enterprise login, and lets BlackRock roll it out one engineering team at a time.

**Why it stops the reader:** Five fragments without subjects. "Inherited permissions" does not say inherited from what. "A controlled rollout team by team" can be read as "a controlled-rollout team" (a team that does rollouts).

**Rewrite:** "One place to govern access; each user keeps their Aladdin permissions ("permission-dependent access"); guardrails against giving advice, tested in the system prompt; the trust of an enterprise login; a rollout BlackRock controls, one engineering team at a time 16, 9"

### 12. Page 12, Exhibit 15, "For" row, outside column

**Current text:** "Discoverability; developer pull; an ecosystem signal; a ready answer to the RFP question about connectors; the terms FactSet, LSEG and MSCI now set 7, 63, 39, 8"

**Trying to say:** An outside connector lets prospects find Aladdin, lets developers adopt it on their own, signals an ecosystem, answers the connector question in RFPs, and matches what FactSet, LSEG and MSCI already offer.

**Why it stops the reader:** "Developer pull" and "an ecosystem signal" are marketing shorthand. "The terms FactSet, LSEG and MSCI now set" is a sentence-ending fragment whose meaning (those three now define what buyers expect) has to be inferred.

**Rewrite:** "Prospects can find it; developers adopt it on their own (developer pull); it signals an ecosystem; it gives a ready answer to the RFP question about connectors; and it matches what FactSet, LSEG and MSCI now offer, which is the comparison buyers make 7, 63, 39, 8"

### 13. Page 12, Exhibit 15, "Against" row, inside column

**Current text:** "Invisible to prospects and to the AI tools buyers already use; rivals set the terms of comparison; the plugin model is described only in a conference talk 9"

**Trying to say:** Nobody outside can see Copilot's plugin model, rivals therefore define the comparison, and the only public account of it is one conference talk.

**Why it stops the reader:** "The AI tools buyers already use" is a garden path ("AI tools, buyers already use"). Otherwise clear.

**Rewrite:** "Prospects cannot see it, and nor can the AI tools that buyers already run; rivals set the terms of comparison; the only public description of the plugin model is one conference talk 9"

### 14. Page 12, Exhibit 15, "Against" row, outside column

**Current text:** "A larger security surface; support cost; a partial catalog exposed and read as the whole; regulatory optics for a platform that will not give advice 16"

**Trying to say:** An outside connector means more to secure and support; if only part of the API catalog is exposed, buyers will assume that is all there is; and outside AI tools using Aladdin data could look, to regulators, like a platform giving advice.

**Why it stops the reader:** "A partial catalog exposed and read as the whole" needs two readings. "Regulatory optics for a platform that will not give advice" states a tension without saying what it is.

**Rewrite:** "More to secure and more to support; buyers would read a partial catalog as the whole catalog; and a platform that will not give advice 16 would have to explain to regulators what outside AI tools do with its data"

### 15. Page 12, direction box, sentence 1 (38 words)

**Current text:** "What it suggests about direction. I would describe the Copilot plugin model publicly now: Copilot's tools are production Aladdin APIs, the same governed APIs Studio exposes, with inherited permissions and no-advice guardrails tested in the system prompt, and it never gives investment advice 9, 16."

**Trying to say:** BlackRock should publish a plain description of how Copilot works, and here is what that description would say.

**Why it stops the reader:** A recommendation and its content are stacked after one colon into four clauses; "with inherited permissions" attaches ambiguously to the APIs or to Copilot; "it" at the end is Copilot, three clauses back.

**Rewrite:** "What it suggests about direction. I would describe the Copilot plugin model publicly, now. The description is short. Copilot's tools are production Aladdin APIs, the same governed APIs Studio exposes. Copilot inherits each user's permissions. Its guardrails against giving advice are tested in the system prompt, and it never gives investment advice 9, 16."

### 16. Page 12, direction box, sentence 2 (35 words)

**Current text:** "Said in BlackRock's own words, that is a stronger answer to the RFP connector question than an MCP server with a partial catalog, and it takes the terms of comparison back from FactSet and LSEG."

**Trying to say:** A published description of the inside model beats a half-built outside connector as an RFP answer, and it lets BlackRock, not its rivals, define the comparison.

**Why it stops the reader:** "That" and "it" both point back to a description that was never named as one. "Takes the terms of comparison back" is an idiom the reader must unpack.

**Rewrite:** "Said in BlackRock's own words, that description answers the RFP question about connectors better than an MCP server with a partial catalog would. It also lets BlackRock, not FactSet and LSEG, set the terms on which buyers compare."

### 17. Page 12, direction box, sentences 3 and 4 (31 words, then 8)

**Current text:** "I would hold any outside connector until the governance questions the inside model already answers, who can call what, with which permissions and under which guardrails, are solved for outside callers. Exhibit 15 is the evidence for that view."

**Trying to say:** Do not ship an outside connector until BlackRock can answer, for outside callers, the three access questions Copilot already answers inside.

**Why it stops the reader:** The subject ("the governance questions") is separated from its verb ("are solved") by a 15-word parenthesis listing the questions; the reader reaches "are solved" having lost the subject.

**Rewrite:** "I would hold any outside connector for now. The inside model already answers three governance questions: who can call what, with which permissions, and under which guardrails. An outside connector should wait until those are answered for outside callers too. Exhibit 15 is the evidence for that view."

(Optional, no new fact: end with "This is quick win 5." The box recommends exactly what page 2 lists as quick win 5, and the reader is not told so.)

---

## Content-clarity flags (not rewrites; the author should decide)

**A. Exhibit 14 title promises more than two rows deliver.** The title says all seven providers "let outside AI tools pull their data". The Arcesium row ("AI features in Aquata, and an AI platform announcement") and the S&P Global row ("Credit Ratings added to its AI Data Portal, September 2026") do not say an outside AI tool can pull anything; "Aquata" and "AI Data Portal" are also unexplained product names. A once-through reader will either take the title on trust or wonder whether those two rows belong. Either state the connector mechanism in those two cells, or soften the title (proposed below).

**B. Exhibit 15 and the direction box use "inside the login" and "outside the login" as if both were established designs.** The paragraph above Exhibit 14 is the first and only place the outside design is described, and it calls it "the other model". One consistent name pair, used in the paragraph, the column heads and the box, would remove the hunting.

**C. Table-cell fragments in Exhibit 14 are acceptable as cells.** "Managed MCP servers, documented" and "A documented MCP server for Cortex Agents" are fine for a receipts table; no change proposed. The Aladdin row, in bold, is the exhibit's point and reads clearly.

---

## Exhibit titles

| Exhibit | Current title | Proposed title (states the finding) |
|---|---|---|
| 13 (p. 11) | "How Aladdin Copilot answers a question" | "Every Copilot answer is a call to a production Aladdin API: thousands of registered tools are filtered to 20 or 30, the call is planned and checked, and advice is refused" |
| 14 (pp. 11-12) | "Seven data and platform providers let outside AI tools pull their data; no public Aladdin equivalent was found" | "Seven providers a Studio buyer also uses have shipped or announced AI connectors to their data; Aladdin has no public equivalent, only a job advert that mentions MCP" |
| 15 (p. 12) | "Two sides of the AI front door" | "Keeping the AI front door inside the login gives BlackRock governance and trust; opening it outside gives discoverability on rivals' terms, with more to secure and more to explain to regulators" |

Shorter alternatives if the above run long on the page:

- 13: "Copilot answers a question by choosing from thousands of registered tools and calling production Aladdin APIs, never giving advice"
- 14: "Seven providers offer or have announced AI connectors to their data; Aladdin has none in public"
- 15: "Inside the login buys governance; outside the login buys discoverability on rivals' terms"

---

# Readability pass, pages 13 to 18

Range: Finding 4 with Exhibit 16 (p. 13); Part 3 with Exhibits 17 and 18 (pp. 14 to 15); Source register intro and entries (pp. 15 to 17, read for sense only); back page (p. 18).

Method: read every word of the text extract and the page images (rendered at 150 dpi for pages 13 to 15 to confirm superscripts and underlined links). Superscripts are shown here as `^8`; underlined link phrases are shown as `_phrase_`. Rewrites keep both in place and add no facts. Where a sentence was split and the single superscript at its end covered the whole, I say so.

Jargon check: "enterprise selling model" (p. 2), "receipts" (p. 2), "qualification" (pp. 3, 7), "extensibility" (p. 8), "named proof" (p. 9), "plugin model" (p. 12) and "three parts" (p. 8) are all introduced before this range, so I do not flag them as unexplained. The Build vs. Buy webinar itself is not: it is first named in a source note on p. 12 and then treated as known on p. 13 (see item 1).

---

## Page 13. Finding 4 and Exhibit 16

### 1. Heading

**Current:** "4. Buyers at BlackRock's own webinar said they want a core platform plus their own builds, and rivals are selling to that"

**Trying to say:** Webinar attendees want a vendor core they can build on, and SimCorp is already winning deals with that pitch.

**Problem:** "selling to that" has no clear referent (that want? that buyer? that market?). The body text says "the same buyer," which is clearer.

**Rewrite:** "4. Buyers at BlackRock's own webinar said they want a core platform plus their own builds, and rivals are already selling to those buyers"

### 2. Opening sentence pair

**Current:** "BlackRock's own Build vs. Buy webinar polled its attendees; the attendee count was not given. In the first poll, 37 percent said they run "mostly vendor platforms," 30 percent "hybrid," 18 percent were "actively reevaluating" and 15 percent were "mostly built in house"^8."

**Trying to say:** The webinar ran polls; here is how the first poll split.

**Problems:** The webinar has not been introduced as a thing (the reader last saw it as a source-note citation on p. 12). The second sentence is 33 words, with the verb dropped in the middle items ("30 percent 'hybrid'") and the tense switching from "run" to "were." Nothing tells the reader what poll 1 asked, which Exhibit 16 then labels "Where firms sit today."

**Rewrite:** "BlackRock ran a Build vs. Buy webinar for asset managers and polled the attendees. The replay does not say how many attended. The first poll asked where firms sit today. 37 percent said they run "mostly vendor platforms," 30 percent run a "hybrid," 18 percent are "actively reevaluating," and 15 percent are "mostly built in house"^8."

### 3. Poll 2 sentence

**Current:** "Asked what is driving the decision, "AI and data demands" led at 42 percent, with cost and speed to market tied behind it^8."

**Trying to say:** The second poll asked what drives the build-or-buy decision; AI and data led, and cost and speed to market tied for second.

**Problems:** "the decision" is not named (it is the build-or-buy decision). "tied behind it" makes the reader work out that cost and speed are tied with each other, behind AI. The dangling "Asked ..." modifier attaches to "AI and data demands," which was not asked anything.

**Rewrite:** "The second poll asked what is driving the build-or-buy decision. "AI and data demands" led at 42 percent; cost and speed to market tied for second^8."

### 4. Poll 3 sentence

**Current:** "Asked what they would stop maintaining internally, 53 percent chose compliance reporting^8."

**Trying to say:** Compliance reporting is the first thing attendees would hand off.

**Problem:** Minor; the same dangling "Asked" form. Numbering the poll ties the sentence to the exhibit's "poll 3" label.

**Rewrite:** "The third poll asked what they would stop maintaining in house. 53 percent chose compliance reporting^8."

### 5. Host and panelist sentence

**Current:** "The host read from the slide that 60 to 70 percent of technology cost sits in "maintenance of current systems," and the Alpha FMC panelist said a transformation runs "roughly 12 to 18 months"^8."

**Trying to say:** Two more data points from the webinar: most technology spend is maintenance, and a platform change takes a year to 18 months.

**Problems:** 35 words carrying two unrelated facts. "the Alpha FMC panelist" is unnamed here, although he is named (Clark Schafer) in the pull quote a few lines later; the reader meets him twice before connecting the two. "a transformation" is unanchored (a transformation of what?). "read from the slide" implies a slide the reader has not seen.

**Rewrite:** "The host read out a slide saying that 60 to 70 percent of technology cost sits in "maintenance of current systems"^8. Clark Schafer of Alpha FMC, the panelist, said a platform transformation runs "roughly 12 to 18 months"^8." (The single `^8` at the end of the original covers both; if the sentence is split, repeat it on both halves.)

### 6. Exhibit 16 source note

**Current:** "Source: poll results as read out on the _Build vs. Buy webinar replay_, published captions^8. Attendee counts were not stated. Poll 2, on what is driving the decision, put "AI and data demands" at 42 percent, with cost and speed to market tied."

**Trying to say:** The numbers come from the host reading results aloud, as recorded in the captions; poll 2 is not charted, and here is its result.

**Problems:** "poll results as read out on the ... replay, published captions" is three nouns stacked without a verb between them. "tied" at the end is ambiguous (tied with AI? with each other?). The reader is not told why poll 2 is missing from the chart.

**Rewrite:** "Source: poll results as the host read them out on the _Build vs. Buy webinar replay_, taken from the published captions^8. The webinar did not state attendee counts. Poll 2, which is not charted, asked what is driving the decision: "AI and data demands" led at 42 percent, and cost and speed to market tied for second."

### 7. Pull quote attribution

**Current:** "— _Clark Schafer, Partner, Alpha FMC_, on the Build vs. Buy webinar^8"

No change needed. Clear.

### 8. Sewdass introduction

**Current:** "Alisha Sewdass, BlackRock's Head of Aladdin Solutions Engineering, Americas, answered on the same webinar."

**Trying to say:** BlackRock's own speaker on the panel responded to the buyer's point.

**Problem:** "answered" follows a pull quote that is not a question, so the reader looks for what she is answering.

**Rewrite:** "Alisha Sewdass, BlackRock's Head of Aladdin Solutions Engineering, Americas, gave BlackRock's side on the same webinar."

### 9. The long Sewdass sentence

**Current:** ""_That word monolith is definitely being challenged in the market,_" she said; the shift of the last two years is "to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows," with "very, very robust APIs that manage the end to end life cycle of a transaction" so that clients can build "their secret sauce rebalancing tools" on top^8."

**Trying to say:** Sewdass says the market is moving from one monolithic system to a modular one: a core data layer, robust APIs on top, and client-built tools on top of those.

**Problems:** About 75 words and four spliced quotations joined by a semicolon, "with," and "so that." A reader at normal speed loses the stack (data, then APIs, then client tools) and has to reread to see the layers. The executive takeaway, that she is describing a layered stack, is implied rather than stated.

**Rewrite:** ""_That word monolith is definitely being challenged in the market,_" she said. The shift of the last two years, she said, is "to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows." On top of that data sit "very, very robust APIs that manage the end to end life cycle of a transaction," so that clients can build "their secret sauce rebalancing tools" on top^8."

### 10. Sewdass on AI

**Current:** "On AI, "you need that system of record that underpins anything that AI is built upon," and "the other layer that is almost equally important is a really defined system of work"^8."

**Trying to say:** She says AI needs two things: a system of record and a defined system of work.

**Problem:** The speaker drops out ("On AI, 'you need ...'" has no "she said"), and two quotes are joined with "and" so they read as one thought.

**Rewrite:** "On AI, she said, "you need that system of record that underpins anything that AI is built upon." She added that "the other layer that is almost equally important is a really defined system of work"^8."

### 11. Rivals sentence

**Current:** "Rivals are selling to the same buyer. SimCorp announced wins at _AllianceBernstein_ in February 2026 and _Pictet_ in May 2026; AllianceBernstein keeps its "specialized in-house technology," and Pictet connects its own tools to SimCorp One by API^70, 71."

**Trying to say:** SimCorp is winning exactly the buyer who wants a core plus their own builds, and both wins show it.

**Problems:** "the same buyer" relies on the reader carrying the "core platform plus own builds" idea from the heading. The second sentence is 36 words with a semicolon joining the announcements to the proof.

**Rewrite:** "Rivals are selling to the same buyer, the one who wants a core platform and their own builds on it. SimCorp announced a win at _AllianceBernstein_ in February 2026 and another at _Pictet_ in May 2026. AllianceBernstein keeps its "specialized in-house technology," and Pictet connects its own tools to SimCorp One by API^70, 71."

### 12. BlackRock insight sentence

**Current:** "BlackRock's _August 2026 insight_ says "Build vs buy is no longer a binary question"^72."

**Trying to say:** BlackRock itself now says the same thing publicly.

**Problem:** "insight" is BlackRock's label for an article; a reader outside BlackRock reads it as "BlackRock's insight" in the ordinary sense and stalls. The point of the sentence, that BlackRock agrees with its rivals, is implied.

**Rewrite:** "BlackRock itself says so. Its _August 2026 insight_ piece says "Build vs buy is no longer a binary question"^72."

### 13. "What it suggests about direction" callout

**Current:** "What it suggests about direction. Extensibility is now an RFP question, and Studio is BlackRock's answer in direction: the APIs, events and Data Cloud that Sewdass describes are the pieces in Exhibit 4. The match is in direction, not yet in finish; the public catalog in Part 1 is mostly alpha and the SDK is beta. The quick wins put the answer where the buyer is asking."

**Trying to say:** Buyers now ask in RFPs whether they can build on the platform. Studio is the right answer in kind, but it is not finished. The quick wins get that answer in front of the buyer.

**Problems:** "answer in direction" and then "The match is in direction, not yet in finish" is an "X, not Y" pair where neither term is concrete; the reader has to decode "direction" as "the right kind of thing" and "finish" as "how complete it is." Colon stacking in the first sentence. "The quick wins put the answer where the buyer is asking" leaves both "the answer" (Studio) and "where" (the RFP) implied.

**Rewrite:** "What it suggests about direction. Buyers now ask in RFPs whether they can build on the platform. Studio is the right kind of answer: the APIs, events and Data Cloud that Sewdass describes are the pieces in Exhibit 4. It is not yet a finished answer. The public catalog in Part 1 is mostly alpha, and the SDK is beta. The quick wins in Part 3 put Studio into the RFP, where the buyer is asking the question."

---

## Page 14. Part 3 and Exhibit 17

### 14. Part 3 heading

**Current:** "Part 3 / Based on this, the quick wins in marketing Studio"

**Trying to say:** Here are the quick wins that follow from Part 1 and the findings.

**Problems:** "Based on this" has no referent on the page (the reader has turned from Finding 4, so "this" reads as Finding 4 alone). "the quick wins in marketing Studio" is a label, not a statement.

**Rewrite:** "Part 3 / Six quick wins for marketing Studio, built on Part 1 and the four findings"

### 15. Part 3 intro, first sentence

**Current:** "Each quick win uses what is already public or already true inside BlackRock, works inside the enterprise selling model, and changes nothing about what a prospect can access."

**Trying to say:** Every quick win passes three tests: no new facts, no change to how Aladdin is sold, no new public access.

**Problems:** Three criteria in one 29-word sentence; the reader does not know they are tests until the sentence ends. "already true inside BlackRock" is vague next to "already public."

**Rewrite:** "Each quick win passes three tests. It uses only what is already public, or already true inside BlackRock. It works inside the enterprise selling model described in Part 1. And it changes nothing about what a prospect can access."

### 16. Part 3 intro, second sentence

**Current:** "Product owns what is built and when; marketing owns positioning, stories and sales material; compliance checks the final version."

No change needed. Three parallel clauses, one idea each; reads at speed.

### 17. Exhibit 17 column header "Why"

**Current:** "Why"

**Problem:** The column holds "Finding 1," "Part 1," and so on. "Why" makes the reader expect a reason, then find a cross-reference.

**Rewrite:** "Rests on"

### 18. Row 1, Quick win cell

**Current:** "A named-proof program, starting where the relationship is already public"

**Trying to say:** Get clients to say on the record that they use Studio, starting with those whose Aladdin relationship is already on the record.

**Problems:** "named-proof" is hyphenated here and unhyphenated on p. 9 ("Named proof"). "where the relationship is already public" has no subject (whose relationship?).

**Rewrite:** "A named-proof program, starting with clients whose Aladdin relationship is already public"

### 19. Row 1, What it takes cell

**Current:** "Shortlist clients whose Aladdin relationship is on the record: tender winners (the Pension Protection Fund, Nest, PBGC), filers (JPMorgan Chase, Janus Henderson) and Royal London, which is already on video^50, 3, 49, 44. Ask each for one Studio-specific sentence or one build. Accept proof from a dissimilar firm; a pension fund's story serves an insurer."

**Trying to say:** Pick clients whose use of Aladdin is already in a public document, ask each for one small piece of Studio proof, and do not insist that the proof come from a firm like the prospect.

**Problems:** "tender winners" stops the reader: the Pension Protection Fund, Nest and PBGC ran the tenders; BlackRock won them. "filers" says nothing about what they filed. "one build" is compressed (one thing they built on Studio). "a dissimilar firm" needs a comparison point (dissimilar to the prospect).

**Rewrite:** "Shortlist clients whose Aladdin relationship is already on the record: the public funds whose tenders BlackRock won (the Pension Protection Fund, Nest, PBGC), the SEC filers that disclose Aladdin (JPMorgan Chase, Janus Henderson), and Royal London, which is already on video^50, 3, 49, 44. Ask each for one sentence about Studio, or one thing they built on it. Accept proof from a firm unlike the prospect; a pension fund's story still serves an insurer."

### 20. Row 1, Measure cell

**Current:** "Named references in use; deals in which one was cited"

**Problem:** Fragments without a subject; "in use" is ambiguous (in use by whom?).

**Rewrite:** "Number of named references the sales team can use; number of deals in which one was cited"

### 21. Row 2, Quick win and What it takes cells

**Current:** "Studio's name on the API growth story" / "Agree on one measure with investor relations and product, built on the API-call projection^1, and put Studio's name beside it in investor and client materials"

**Trying to say:** When BlackRock talks about API growth to investors, say "Studio."

**Problem:** Mostly clear. "the API growth story" assumes the reader recalls Finding 2 and the Investor Day slide. "built on the API-call projection" reads as if the measure is derived from the projection; it means the measure should be the one the projection already uses.

**Rewrite (What it takes):** "Agree with investor relations and product on one measure of API use, starting from the API-call projection^1 already shown to investors. Then put Studio's name beside that measure in investor and client materials."

### 22. Row 3, Quick win cell

**Current:** "A written one-page version of the spoken message"

**Problem:** "the spoken message" refers to the three-part definition that four BlackRock speakers give on recordings (p. 8). On its own the phrase is opaque.

**Rewrite:** "A written one-page version of the definition BlackRock's speakers already give"

### 23. Row 3, What it takes cell

**Current:** "Turn the three-part definition four speakers already give^5, 15, 25, 40 into one written page, reviewed by product and compliance, used in every deck and page"

**Problem:** One sentence stacking the action, the review, and the use. Acceptable in a table, but the final clause reads as part of the review.

**Rewrite:** "Turn the three-part definition four speakers already give^5, 15, 25, 40 into one written page. Have product and compliance review it. Use it in every deck and page."

### 24. Row 4, What it takes cell

**Current:** "A document that answers the question Schafer says buyers now ask^8: the domains, counts and status of the catalog, connectors to Snowflake and Databricks, how clients build on top. Delivered by the solutions team after qualification"

**Trying to say:** Write the API-suite answer once, in enough detail for an RFP, and have the solutions team hand it over once a prospect is qualified.

**Problems:** The colon list is four fragments with no verbs; "the catalog" means the API catalog. "after qualification" is established jargon (p. 3) but reads abruptly as a sentence fragment.

**Rewrite:** "A document that answers the question Schafer says buyers now ask^8: which API domains exist, how many specifications each has and at what status, what connectors exist for Snowflake and Databricks, and how clients build on top. The solutions team delivers it once a prospect is qualified."

### 25. Row 5, Quick win and What it takes cells

**Current:** "Publish a description of the Copilot plugin model" / "One page, in BlackRock's words, with no new access: how Copilot's tools map to production APIs^9, what governance applies^16, and how clients will connect their own AI tools, timed with the work described in the Forward Deploy Engineer posting^65"

**Trying to say:** Describe publicly how Copilot's tools work, without opening any new access, and publish it when the client-connection work lands.

**Problems:** 45 words in one cell; "with no new access" is compressed; "timed with the work" trails off and could attach to "AI tools" rather than to the whole page.

**Rewrite:** "One page, in BlackRock's words, that opens no new access. It says how Copilot's tools map to production APIs^9, what governance applies^16, and how clients will connect their own AI tools. Publish it when the work described in the Forward Deploy Engineer posting^65 is ready."

### 26. Row 5, Measure cell

**Current:** "The description exists, dated and public; prospects stop asking the question in deal reviews"

**Problem:** "the question" is not stated in this row (it is the "how does Copilot connect" question).

**Rewrite:** "The description is public and dated; prospects stop asking in deal reviews how Copilot connects"

### 27. Row 6, What it takes cell

**Current:** "One page listing the 11 domains with counts and status, as in Exhibit 5^17, with no specifications; shared before the first meeting or on the Studio page"

**Problems:** "with no specifications" means without the specification files themselves; as written it could mean "unspecified." "the 11 domains" needs "API."

**Rewrite:** "One page listing the 11 API domains with the count and status of each, as in Exhibit 5^17, but without the specifications themselves. Share it before the first meeting, or put it on the Studio page."

### 28. Row 6, Measure cell

**Current:** "First meetings that start past scope; prospects who arrive with the list"

**Problem:** "start past scope" is compressed to the point of opacity: it means meetings that no longer have to spend time on what is included.

**Rewrite:** "First meetings that skip the what-is-included discussion; prospects who arrive already holding the list"

### 29. Exhibit 17 source note

**Current:** "Source: my proposals, built on Part 1 and Findings 1 to 4. Receipts in the table point to the public facts each win rests on."

No change needed. "Receipts" is defined on p. 2.

---

## Page 15. "What I would need from inside" and Exhibit 18

### 30. Intro paragraph

**Current:** "Five questions need internal data that no public source holds. The answers would confirm or correct the findings before any of the wins is sized, and they are where any error in my reading would show first."

**Trying to say:** These five questions can only be answered inside BlackRock; answer them before sizing any quick win, because that is where my mistakes would surface.

**Problems:** Second sentence is 30 words with two ideas. "sized" is sales jargon (estimating the value of a win). "they" in "they are where" could be the answers or the questions.

**Rewrite:** "Five questions need internal data that no public source holds. The answers would confirm or correct the findings before anyone puts a number on a quick win. They are also where any error in my reading would show first."

### 31. Exhibit 18, question 4

**Current:** "How will clients connect their own AI tools to Aladdin, and is the Forward Deploy Engineer work the path?"

**Problem:** "the path" is vague.

**Rewrite:** "How will clients connect their own AI tools to Aladdin, and is the Forward Deploy Engineer work how they will do it?"

### 32. Exhibit 18, question 5 and its decision cell

**Current:** "Where does adoption stall most: awareness, the first API call, or getting a build into production?" / "Where marketing spends first: content, enablement or client success"

**Problem:** The question is clear. In the decision cell, "enablement" is sales jargon (sales enablement) and the three options do not map one-to-one onto the three stall points, so the reader tries to pair them and cannot.

**Rewrite (decision cell):** "Where marketing spends first: content for awareness, sales enablement for the first call, or client success for production builds"

The other three rows and the source note ("Source: my questions. Question 3 refers to the tag on the public specifications^17; question 4 to the job posting that names MCP^65.") read cleanly.

---

## Pages 15 to 17. Source register (read for sense only)

### 33. Register intro, first sentence

**Current:** "Numbered in order of first citation and grouped by grade: P is a primary document, S a BlackRock speaker on the record with the name and title as the recording gives them, T a third-party report; for recordings, the entry gives the minute and second at which each quoted passage begins."

**Trying to say:** Numbers follow first citation; the list is then regrouped into P, S and T; recordings carry timestamps.

**Problems:** 55 words; a colon, a three-item list with elided verbs, and a semicolon clause. The consequence of "numbered by first citation and grouped by grade" is that numbers within each group jump (1, 2, 3, 7, 10 ...), which the reader discovers on their own and may take for an error.

**Rewrite:** "Sources are numbered in the order they are first cited, then grouped by grade, so the numbers within a group are not consecutive. P is a primary document. S is a BlackRock speaker on the record, with name and title as the recording gives them. T is a third-party report. For recordings, each entry gives the minute and second at which each quoted passage begins."

### 34. Register intro, second sentence

**Current:** ""Machine transcription" means a local transcription of the downloaded audio and "auto-captions" means YouTube's captions; in both, names and jargon can be misheard, and only caption misspellings of proper names were corrected inside quotations."

**Trying to say:** Two kinds of transcript were used, both can mishear, and the only edits made to quotes were fixing misspelled names.

**Problems:** 40 words, two definitions and two caveats in one sentence. "only caption misspellings of proper names" is hard to parse (misspellings by the captions, of proper names).

**Rewrite:** ""Machine transcription" means a local transcription of the downloaded audio. "Auto-captions" means YouTube's captions. Both can mishear names and jargon. Inside quotations, the only correction made was to the spelling of proper names the captions got wrong."

### 35. Entries

Read for sense; all entries parse. Notes, none blocking:

- Entry 2: "JPMorgan Chase proxy statements (DEF 14A), filed 2017 to 2026, related-party payments to BlackRock for Aladdin." The third phrase hangs; "covering related-party payments to BlackRock for Aladdin" would attach it.
- Entry 8: the parenthetical "(Sewdass at 31:56, 32:01, 39:15 and 39:42; Schafer at 42:22)" after a ten-item timestamp list is dense but does its job.
- Entry 20 and entry 60 both carry a sentence explaining that the recording does not label speakers; both are clear.
- Entry 40: the URL "https://www.blackrock.com/aladdin/discover" is a landing page rather than the interview, which a reader looking for the recording will notice; flagged for the caller, not a readability issue.
- Entry 44: "Not quoted; the Snowflake passage referred to begins at 5:21." Clear.
- Entry 52: "award record: full and open competition, four offers received, performance March 2023 to March 2027." A list of fragments, acceptable in a register.
- The grade letter is repeated on every entry ("1 P BlackRock ...") although the entries are already grouped under "P. Primary documents." Redundant but harmless; it survives a two-column layout where the group header has scrolled away.

---

## Page 18. Back page

### 36. First paragraph

**Current:** "Independent analysis compiled from public sources: BlackRock product pages, SEC filings, procurement notices, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings. It was not produced, reviewed or endorsed by BlackRock."

**Trying to say:** This is an independent document built only from public material.

**Problem:** The first sentence is a 32-word fragment (no verb before the colon), so "It" in the second sentence has to reach back to "analysis." Acceptable for a colophon; a one-word fix makes it a sentence.

**Rewrite:** "This is an independent analysis compiled from public sources: BlackRock product pages, SEC filings, procurement notices, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings. BlackRock did not produce, review or endorse it."

### 37. Remaining paragraphs

"AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted the text. I checked each claim against the document or recording it cites." Clear.

"Facts are as of October 19, 2026, unless an exhibit gives another date. Underlined text links to the document behind each fact. Superscripts point to the Source register, which gives the grade, the title, the speaker and the date of every source." Clear.

"The quick wins and questions in Part 3 are my proposals, based on Part 1 and the findings in Part 2." Clear.

"BlackRock and Aladdin are registered trademarks of BlackRock, Inc. Other company and product names are the property of their owners." Clear.

**Current:** "Set in Barlow and Barlow Condensed, open-license stand-ins for BlackRock's licensed BLK Fort typeface. Code is set in IBM Plex Mono."

**Problem:** Fragment without a subject; minor.

**Rewrite:** "The text is set in Barlow and Barlow Condensed, open-license stand-ins for BlackRock's licensed BLK Fort typeface. Code is set in IBM Plex Mono."

---

## Exhibit titles in range

| Exhibit | Current title | Proposed title (states the finding) |
|---|---|---|
| 16 (p. 13) | What attendees of BlackRock's Build vs. Buy webinar said | Attendees of BlackRock's Build vs. Buy webinar mostly run vendor or hybrid platforms, and compliance reporting is the first thing they would stop maintaining |
| 17 (p. 14) | Quick wins | Six quick wins, each resting on a public fact, with an owner and a measure |
| 18 (p. 15) | Five questions for internal data | Five questions only internal data can answer, and what each answer would decide |

Sub-labels inside Exhibit 16 ("Where firms sit today," "What they would stop maintaining internally," "Share of attendees, poll 1 / poll 3") are fine as chart labels; the proposed exhibit title carries the finding so they do not need to.

---

## Priority, if only some fixes are made

1. Item 13 (the "direction, not yet in finish" callout): the finding's conclusion is the hardest sentence on p. 13 to parse.
2. Item 9 (the 75-word Sewdass sentence).
3. Item 19 ("tender winners" reads as the wrong party).
4. Items 2, 3, 5 (the poll paragraph: name the polls, name Schafer, split the host/panelist sentence).
5. Items 33 and 34 (register intro).
6. Exhibit titles 16, 17, 18.
