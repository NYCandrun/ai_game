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
