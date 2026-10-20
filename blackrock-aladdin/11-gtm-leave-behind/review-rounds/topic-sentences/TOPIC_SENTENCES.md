# Topic-sentence check: "Aladdin Studio, learned with AI" (18 pages, as of Oct 19, 2026)

Question asked of every body paragraph: does its first sentence frame what follows?
Scope: exec summary, Part 1, Part 2 (opening paragraphs, second paragraphs, direction callouts), About page.
Excluded: table cells, exhibit titles, source notes, pull quotes, Sources section.
Source of truth for wording: `gtm/out/Aladdin_Studio_With_AI.html`; cut sentences recovered from `gtm/out/Aladdin_Studio_With_AI.before_cuts.html`.

Verdict key: OK = opening frames the paragraph. FIX = it does not. Flags: [1-sent] one-sentence paragraph; [dangle] last sentence points at something that is no longer there.

## All paragraphs, page order

| # | Page | First five words | Verdict |
|---|------|------------------|---------|
| 1 | 2 | Studio is the product behind | OK [1-sent, by design: it is the deck line] |
| 2 | 2 | Studio is Aladdin's developer and | OK |
| 3 | 2 | API calls are the fastest-growing | FIX |
| 4 | 2 | Public material only: BlackRock web | OK (box heading "What this method can and cannot do" does the framing) |
| 5 | 2 | Underlined text links to the | OK |
| 6 | 3 | Aladdin is the investment platform | OK |
| 7 | 3 | Everything here was read from | OK (optional reorder, see note) |
| 8 | 4 | The SDK's README documents three | FIX |
| 9 | 4 | Exhibit 2 puts Studio beside | OK |
| 10 | 5 | I pulled 128 recordings for | FIX |
| 11 | 5 | BlackRock's own definition of Studio | OK as a quote lead-in [1-sent]; folds into #10 fix |
| 12 | 5 | Exhibit 3 lists each speaker | FIX [1-sent] |
| 13 | 5 | Four of the five describe | OK (see note on the tail and on Exhibit 4) |
| 14 | 7 | Exhibit 6 follows one trade | OK as an exhibit lead-in [1-sent] |
| 15 | 9 | Posting an order takes whatIf | FIX |
| 16 | 10 | BlackRock's Studio page names no | OK |
| 17 | 10 | In December 2025 a Janus | FIX |
| 18 | 10 | None of this proof names | OK |
| 19 | 11 | What this finding suggests about (1) | OK [1-sent, by design] |
| 20 | 11 | BlackRock projected at its 2025 | FIX |
| 21 | 11 | BlackRock bought eFront in 2019 | FIX |
| 22 | 12 | What this finding suggests about (2) | OK |
| 23 | 12 | Aladdin Copilot draws on a | FIX |
| 24 | 12 | Six data and cloud providers | FIX |
| 25 | 13 | What this finding suggests about (3) | OK |
| 26 | 13 | BlackRock ran a Build vs. | OK |
| 27 | 14 | Alisha Sewdass, BlackRock's Head of | OK |
| 28 | 14 | Rivals are selling to the | OK |
| 29 | 14 | What this finding suggests about (4) | OK |
| 30 | 15 | This is an independent analysis | OK |
| 31 | 15 | AI agents pulled the pages, | OK |
| 32 | 15 | Facts are as of October | FIX (minor, reorder) |
| 33 | 15 | BlackRock and Aladdin are registered | OK |
| 34 | 15 | The text is set in | OK |

Page 6 ("What BlackRock sells") and page 8 (Exhibits 7 and 8) carry no prose paragraphs. Pages 1 and 16 to 18 are the cover and Sources.

**Count: 34 paragraphs checked. 11 FIX (one of them minor), 23 OK. One-sentence paragraphs: 6 (#1, #11, #12, #14, #19 are deliberate lede, lead-ins or callout; #12 is the one that should go). Dangling last sentence: none that points at cut text; two loose tails noted under #13 and #23.**

---

## FIX items in full

### FIX 3. Page 2, "API calls are the fastest-growing..."

**As it stands.**
> API calls are the fastest-growing measure BlackRock showed investors: 17x by 2030. Buyers at BlackRock's webinar want a core platform plus their own builds, and rivals already sell to that demand 6.

**What it is about.** The Part 2 findings, compressed: BlackRock's own growth projection (finding 2) and buyer demand for a platform they can build on (finding 4).

**Why the opening does not frame it.** Two sentences, two different findings, no sentence that holds them together. Before the cuts this paragraph summarised findings 2, 3 and 4 in four sentences; findings 3 and most of 2 were cut and nothing frames the two that remain. Sentence 1 (an investor projection) does not set up sentence 2 (a buyer poll).

**Proposed fix (a), new opening sentence.**
> BlackRock's investor story and its buyers' own answers both point to Studio.

Facts used: the lede on page 2 ("Studio is the product behind the growth story BlackRock tells investors") and the finding 4 callout on page 14 ("Studio is the right kind of answer"). 12 words.

Alternative (c): if the author would rather the exec summary name all four findings, this paragraph is where findings 1 and 3 used to be; that is an addition, not a topic-sentence fix.

---

### FIX 8. Page 4, "The SDK's README documents three..."

**As it stands.**
> The SDK's README documents three run modes: "a developer's local machine," "Aladdin Studio Compute sessions" and a test mode. It stores a prompted password in the operating system's credential manager. It carries settings for firms that consume "the Aladdin APIs via an enterprise API management platform such as Azure API Management" 14.

**What it is about.** What the SDK, the one piece of Studio that is public before any conversation, reveals about how clients run it: run modes, credential storage, gateway settings.

**Why the opening does not frame it.** Starts mid-thought. The paragraph sits alone at the top of page 4, after Exhibit 1 (page 3) and before Exhibit 2, under no heading. Its first sentence is the first of three README details; nothing says why the README is being read. Before the cuts it opened "The SDK is the one piece that installs before any conversation." and closed "Run modes, credential storage and API-gateway settings are the needs of a client's engineering team." Both were cut, so the paragraph now has neither a frame nor a point. The reader also has to recall that "the SDK" was introduced only in Exhibit 1's Build row and the previous paragraph's "read the SDK's code".

**Proposed fix (a), new opening sentence.**
> The SDK is the one piece of Studio a prospect can install before any conversation, and its README describes how clients run it.

Facts used: Exhibit 1, Try row ("Nothing to run") and Build row ("The open-source SDK on GitHub and PyPI, with a detailed README"); Exhibit 8, "Aladdin SDK" row. 23 words.

Optional: restoring the cut closing sentence ("Run modes, credential storage and API-gateway settings are the needs of a client's engineering team.") would give the paragraph its point back at no new-claim cost; it is the author's own sentence.

---

### FIX 10. Page 5, "I pulled 128 recordings for..."

**As it stands.**
> I pulled 128 recordings for this document 9, 10. Five BlackRock speakers define Studio in them.

Followed by a one-sentence paragraph (#11) "BlackRock's own definition of Studio comes from the head of Studio engineering, on Snowflake's podcast in November 2025.", the Woodhead quote, and another one-sentence paragraph (#12) "Exhibit 3 lists each speaker with the title the recording gives."

**What it is about.** Under the heading "What Studio is": that five BlackRock speakers have defined Studio on the record, with Woodhead's as the definition.

**Why the opening does not frame it.** Opens on a method detail (how many recordings were pulled) that the paragraph does not develop; the point is sentence 2. Before the cuts the sentence lived in a three-sentence paragraph that led into the speakers table ("...Exhibit 8 lists each speaker with the title the recording gives."); the author moved it to open the section, and the Exhibit 3 sentence was left behind as a one-liner (#12). The result is three fragments, two of them one sentence long, around one quote.

**Proposed fix (b)+(c), reorder and merge #10, #11 and #12 into one paragraph before the quote.**
> Five BlackRock speakers define Studio in the 128 recordings I pulled for this document 9, 10. Exhibit 3 lists each with the title the recording gives. BlackRock's own definition comes from the head of Studio engineering, on Snowflake's podcast in November 2025.

No new words beyond the existing sentences recombined; the first sentence is 15 words. Exhibit 3 follows the quote anyway, so the forward reference still lands.

If the author prefers to keep #11 as a separate lead-in to the quote (conventional), then the merged paragraph is #10 + #12 only: "Five BlackRock speakers define Studio in the 128 recordings I pulled for this document. Exhibit 3 lists each with the title the recording gives."

---

### FIX 12. Page 5, "Exhibit 3 lists each speaker..." [1-sent]

**As it stands.**
> Exhibit 3 lists each speaker with the title the recording gives.

**What it is about.** A pointer to Exhibit 3.

**Why it fails.** A one-sentence paragraph stranded between the Woodhead quote and the exhibit it names; it was the tail of the recordings paragraph before the cuts and belongs with "Five BlackRock speakers define Studio". The Exhibit 6 lead-in (#14) is also one sentence, but it carries the `lead-in` style and opens a section; this one is a plain paragraph.

**Proposed fix (c).** Merge into #10 as shown above.

---

### FIX 15. Page 9, "Posting an order takes whatIf..."

**As it stands.**
> Posting an order takes whatIf and runCompliance, which defaults to true, and the response returns any compliance violations inline 13. Ten specifications expose an endpoint for long-running operations, 35 operations are flagged as long-running, and the SDK polls them 14. Risk exceptions and Data Cloud datasets carry bitemporal fields, which record two time dimensions. Rule assignments and dataset releases name a four-eyes approval, a second sign-off 13. Every request carries an application key plus OAuth 2.0 scopes such as trading.order_management.order.v1.Order:read, and the client ID and secret come from the Studio UI 14.

**What it is about.** What the specifications show about how the APIs behave in use, beyond the counts in Exhibit 9: compliance on order entry, long-running operations, bitemporal fields, four-eyes approval, per-request auth.

**Why the opening does not frame it.** Opens on a detail. Before the cuts the paragraph opened "Only 23 of the 54 specifications are stable, and the specifications say more than their count. Every one is tagged Access.Internal..." The framing clause ("the specifications say more than their count") went with the cut, so the paragraph is now five unrelated facts, the first of which (whatIf/runCompliance) repeats Exhibit 6 row 1 and reads as if it continued that exhibit rather than following Exhibit 9.

**Proposed fix (a), new opening sentence.**
> The specifications say more than Exhibit 9's counts: they show how the APIs behave.

Facts used: the author's own cut clause; Exhibit 9's title ("Two domains hold 127 of the 301 public API operations"); everything after the colon is what the five sentences then do. 14 words.

---

### FIX 17. Page 10, "In December 2025 a Janus..."

**As it stands.**
> In December 2025 a Janus Henderson engineer submitted two changes to the open-source SDK: URL rewriting and custom headers. Both are for firms that route Aladdin calls through an enterprise gateway. The BlackRock engineer who co-wrote the SDK's launch post merged them. The commits name a janushenderson.com address as the author 17, 45, 46, 47. Janus Henderson's 10-K says that in the third quarter of 2025 the firm chose to move its investment management system to Aladdin, "a complex, multi-year initiative" 48. Public buyers add a third kind of record: procurement notices.

**What it is about.** A second kind of public proof that a named client builds on Aladdin: the client's own engineers in the SDK's commit history, confirmed by its 10-K.

**Why the opening does not frame it.** Opens on a narrative detail (a date and a pull request). The paragraph's point, that code commits are a kind of record and that they name a client, is never stated; the reader infers it. The closing sentence says "a third kind of record", which presumes the first two kinds were counted, and they were not: the previous paragraph lists a video and proxy statements without calling them kinds, and this one never calls commits a kind. The enumeration existed in the pre-cut exec summary ("JPMorgan Chase's proxy statements, Janus Henderson's code commits and 10-K, Royal London's CEO on video, and three pension tenders"), which was cut.

**Proposed fix (a), new opening sentence.**
> A second kind of record is code written by a client's engineers.

Facts used: this paragraph's own closing sentence ("a third kind of record") and its commit facts; Exhibit 1, Get help row (pull requests 52 and 57). 12 words. "In December 2025 a Janus Henderson engineer submitted..." then follows as the example, and "Public buyers add a third kind of record" closes the count.

Last sentence: not dangling; it points forward to Exhibit 11, which follows.

---

### FIX 20. Page 11, "BlackRock projected at its 2025..."

**As it stands.**
> BlackRock projected at its 2025 Investor Day that API calls across BlackRock and Aladdin would grow 17x by 2030 1. Attributing them to Studio is my inference 1. I make that inference because API use is the activity the Studio page describes 11. No executive said "Studio" on any of the 26 earnings calls from the first quarter of 2020 to the second quarter of 2026 4. Outside the calls, the only investor-facing mention I found is a single line on a 2023 Investor Day slide 52. BlackRock's 10-K says technology services fees are generally set by the value of positions on the platform or at a fixed rate. They can also depend on subscriptions, go-lives and support. The 10-K does not list API calls among the fee terms it names 8, 1.

**What it is about.** Three strands: the growth story is told in API calls (and I attribute those to Studio); BlackRock never says the name to investors; API calls are not among the fee terms the 10-K names.

**Why the opening does not frame it.** Borderline, but the original topic sentence was cut ("BlackRock tells investors growth will come from two things: API calls, and the whole portfolio, public and private markets together.") and what remains opens on the projection itself. Sentences 2 and 3 develop it; sentences 4 and 5 switch to the silence on the name; sentences 6 to 8 switch to fee terms, and nothing says why fee terms matter here (that API calls are an activity measure, not a billing measure). The heading carries the first two strands; the third is unframed.

**Proposed fix (a), new opening sentence.**
> BlackRock tells investors growth will come from API calls, without naming the product behind them.

Facts used: the 17x projection (this paragraph, stat tile page 2); the page 2 stat note ("does not say which products generate the API calls"); the zero-mentions tally (Exhibit 12). 15 words.

Note on the tail: the three 10-K sentences are a caveat whose relevance is unstated. Not a forward dangle, but if the author wants one more change, a half-sentence such as "...so the measure BlackRock shows investors is not one it bills on" would close it using only facts in the paragraph. That is a new sentence, so it is offered as a note, not a fix.

---

### FIX 21. Page 11, "BlackRock bought eFront in 2019..."

**As it stands.**
> BlackRock bought eFront in 2019 and Preqin in 2025. In September 2025 its private markets team described the result on a client webinar 57. Investors "now have access to over 15,000 fund investments within eFront Insight" for benchmarking. Preqin indices "are also available today in Aladdin Explore and our Aladdin Data Cloud capabilities". And "over 10 different transaction types" were added to Aladdin, covering commitments, fundings, paydowns and PIK, so private credit loans are captured natively. The team said those were designed with BlackRock's own professionals and "our new colleagues from HPS" 57. Private credit analytics on Preqin followed in May 2026 33. Newman, the Studio general manager, names eFront data and Preqin among the data being added to Data Cloud 27.

**What it is about.** The private-markets data BlackRock has been adding (eFront, Preqin, HPS transaction types) reaches clients through Data Cloud and Explore, so this part of the growth story also runs through Studio.

**Why the opening does not frame it.** Refers back to something that was cut. Before the cuts it opened "The other half of the growth story is the whole portfolio, public and private markets together." That sentence, and the matching line in the exec summary, were both cut, so "the whole portfolio" half of the Investor Day story no longer exists anywhere in the body (the phrase survives only in a Sources entry title). The paragraph now opens on two acquisitions, and the reason it sits under finding 2 is stated only afterwards, in the callout ("Both are Studio surfaces").

**Proposed fix (a), new opening sentence.**
> The private-markets data BlackRock has been adding reaches clients through Data Cloud and Explore.

Facts used: this paragraph (Preqin indices "available today in Aladdin Explore and our Aladdin Data Cloud"; Newman on eFront and Preqin in Data Cloud); callout 2 on page 12. 14 words.

---

### FIX 23. Page 12, "Aladdin Copilot draws on a..."

**As it stands.**
> Aladdin Copilot draws on a registry of plugins, "couple of thousands agents and tools," built by Aladdin's engineering teams. The first way a team adds a tool is "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" 7. So Copilot's tools are Studio's APIs. Microsoft's Adrian Crockett made the dependence plain on BlackRock's podcast: "There's no copilot without plug-ins" 58. On the data side, BlackRock's AI product head says the team is making sure "the data model itself is structured for agentic use cases" 59.

**What it is about.** Aladdin's own AI, Copilot, is built on the same production APIs Studio exposes and works inside the login.

**Why the opening does not frame it.** Opens on a detail (the plugin registry); the point arrives in sentence 3 ("So Copilot's tools are Studio's APIs"). Before the cuts the paragraph opened "Aladdin Copilot is 'now available to all Aladdin clients' and 'will not give investment advice...'. Two of its engineers, Brennan Rosales... and Pedro Vicente Valdez... describe how it works." Both sentences were cut, so the quotes in sentences 1 and 2 now have no named speaker in the prose (the attribution survives only in the Exhibit 13 source note), and the heading's first clause, "Aladdin's AI works only inside the login", is never stated in the paragraph.

**Proposed fix (a), new opening sentence.**
> Aladdin Copilot, the AI inside the login, is built on the same APIs Studio exposes.

Facts used: the heading; callout 3 on page 13 ("production Aladdin APIs, the same ones Studio exposes"); Exhibit 7 ("answers through the same APIs"). 15 words.

Loose tail: the last sentence ("On the data side...") opens a second thread that nothing develops. It does not refer to cut text, so no dangle flag, but it would sit more naturally as the second sentence, before the tool story, or be dropped.

---

### FIX 24. Page 12, "Six data and cloud providers..."

**As it stands.**
> Six data and cloud providers that Studio buyers also use offer a connector or an MCP server, and two system-of-record rivals have announced AI features. LSEG had 90 customers connected by April 2026, according to a secondary summary of its results slides 60, 61.

**What it is about.** The other half of finding 3: outside Aladdin, data providers let the buyer's own AI tools reach their data, and Exhibit 14 (next page) lists them.

**Why the opening does not frame it.** Refers back to something that was cut and starts mid-thought. Before the cuts it opened "Outside the login, data providers have chosen the opposite design: they let the buyer's own AI tools reach their data. MCP is the common standard AI assistants use to pull data from other systems." Both were cut. The contrast with the Copilot paragraph, which is the whole finding, is now stated only in the heading; "MCP server" and "connector" arrive undefined (the only gloss left is Exhibit 2's key on page 4); and the paragraph, which is the lead-in to Exhibit 14, never mentions Exhibit 14 (the old second paragraph that did was cut too).

**Proposed fix (a), restore the cut opening sentence.**
> Outside the login, data providers have chosen the opposite design: they let the buyer's own AI tools reach their data.

Facts used: the finding 3 heading; the author's own cut sentence. 20 words. The existing two sentences then follow as the evidence.

Optional: appending "Exhibit 14 lists them." would restore the exhibit pointer; it is a cross-reference, not a claim.

---

### FIX 32 (minor). Page 15, "Facts are as of October..."

**As it stands.**
> Facts are as of October 19, 2026, unless an exhibit gives another date. Underlined text links to the document behind each fact. Superscripts point to the Sources section, which follows this page and gives each source's grade (P, S or T), title, speaker and date.

**What it is about.** Three housekeeping notes: the as-of date, and two reading conventions (links, superscripts).

**Why the opening does not frame it.** The first sentence is a date; the other two are how to read the receipts, which page 2 already explains in the same words. Minor, because this is a colophon, but the date does not frame the two sentences after it.

**Proposed fix (b), reorder.** Move "Facts are as of October 19, 2026, unless an exhibit gives another date." to the end of paragraph #30 (after "BlackRock did not produce, review or endorse it."), leaving the two reading-convention sentences as their own paragraph, which then opens on its subject ("Underlined text links to the document behind each fact.").

---

## Notes on paragraphs marked OK

- **#7, page 3, "Everything here was read from outside..."** The opener frames it. The Exhibit 1 pointer (sentences 2 and 3) interrupts the could/could-not pair; an optional reorder puts "I could read the pages... I could not run anything..." straight after sentence 1 and ends with "Exhibit 1 follows a prospect's engineer... For each step it records...", so the paragraph closes on the exhibit it sits above.
- **#13, page 5, "Four of the five describe..."** The opener frames sentences 1 to 5. The last three sentences ("Learning about it from outside takes effort...") are a second idea; before the cuts they ended "Nothing can be run.", which was cut, so the tail now ends on "transcribed from recordings" without a close. Not a forward dangle. Two asides outside this check's scope: the opener says "the same three parts" while Exhibit 4's own note says only Goel and Woodhead name developer tools; and Exhibit 4 is never pointed to from prose (this paragraph is in effect its commentary, printed on the page before it).
- **#16, page 10.** Sentence 1 is the setup, sentence 2 ("Proof that clients use Aladdin, though, is public.") is the real topic sentence; the pairing works because of "though".
- **#19 and #22, pages 11 and 12.** Both direction callouts are orphaned at the top of the page after their finding; a layout point, not a wording one.
- **#28, page 14.** The last sentence is BlackRock's own page rather than a rival; "says the same" ties it in.
- **Page 6, "What BlackRock sells".** The heading runs straight into Exhibit 5 with no prose and Exhibit 5 is never referenced in text; then the Exhibit 6 lead-in on page 7 jumps from "eight products" to "one trade through the APIs" with no bridge. Out of scope for topic sentences, noted because a cut sentence may have been the bridge ("The three parts are APIs and events, the Aladdin Data Cloud on Snowflake, and developer tools." preceded the lead-in before the cuts).
