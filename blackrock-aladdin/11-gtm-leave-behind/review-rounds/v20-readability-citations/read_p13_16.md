# Readability read, pages 13 to 16 (v20)

Scope: Exhibit 15 (p13), Part 4 intro and Exhibit 16 (p13 to 14), SDK paragraph, Exhibit 17 and its text (p14), About this document (p15), Sources intro and register skim (p16 to 19, garbled or unreadable entries only). Pages checked as text and as 90 dpi images.

Types: 1 GARBLED, 2 HARD TO READ, 3 ALLUDING, 4 EXHIBITS.

## MUST FIX

**M1. p13, Exhibit 15, row 4 ("A worked example"), "What it is" cell. Type 1 (misleading citation placement) and 2.**
Current: "Aladdin runs what-if and compliance on every order and returns any violations, and a portfolio manager approves before anything trades 6."
Problem: one sentence joins a cited fact about the order API with a design choice for the demo (the PM approval). The [6] lands on "a portfolio manager approves before anything trades", so it reads as if the specifications require PM approval of orders. The text on p5 says the specs name four-eyes approval for rule assignments and dataset releases, not orders. "Runs what-if" is also a spec field used as a noun.
Rewrite: "Aladdin runs a what-if test and a compliance check on every order. It returns any violations [6]. In the demo, a portfolio manager approves before anything trades."

**M2. p15, About this document, paragraph 1, last sentence. Type 1 (contradicts nearby text).**
Current: "Facts are as of October 19, 2026, unless an exhibit gives another date."
Problem: facts on these pages rest on sources dated later than October 19 that no exhibit dates. The Exhibit 16 note relies on the developer portal "checked October 20, 2026" [43]. The Client Forum page [85] and register entries 31, 32, 33, 37 and 77 are dated October 20.
Rewrite: "Facts are as of October 19, 2026, unless an exhibit or a source entry gives another date."

## SHOULD FIX

**S1. p13, Exhibit 16 title. Type 4.**
Current: "What I was not able to see from outside, and what opens after qualification"
Problem: both halves describe the After qualification column. The title leaves out the Public today column, which is half the table. It also does not name the six-step path.
Rewrite: "At each step of a prospect engineer's path, what is public today and what opens only after qualification"

**S2. p13, Part 4 intro, sentence 1. Type 3.**
Current: "Everything here was read from outside, which limits what this document can be sure of."
Problem: a hedge that does not say what the limit is.
Rewrite: "I read everything here from outside, with no client login. So this document cannot confirm what clients see after login."

**S3. p13, Part 4 intro, last sentence. Type 1 (unclear antecedent).**
Current: "Where this document describes those, it relies on what sources say."
Problem: "those" could mean the catalog, the guides, the notebooks, or everything a client receives.
Rewrite: "Where this document describes the catalog, the guides or what a client receives, it relies on what sources say."

**S4. p13, Part 4 intro and Exhibit 16 column head, "after qualification". Type 2.**
Current: "For each step it records what is public today and what a client receives after qualification."
Problem: "qualification" is never defined. The column mixes items for qualified prospects (the Client Forum, Solutions Engineering) with items only signed clients get (a client host, credentials). The source note then calls the whole column "what a client receives".
Rewrite: "For each step it records what is public today. It also records what opens only to qualified prospects and clients." (Optionally rename the column "After qualification or signing".)

**S5. p13, Exhibit 15, row 1 ("An answer for RFPs"), "What it is" cell. Type 2.**
Current: "A ready answer to "what APIs do you have, and can we connect to them": the APIs by area with their stability labels, how permissions work, how a client routes calls through its own gateway, and an answer on Snowflake and Databricks connectors, plus how a client's own AI tools would connect."
Problem: a five-item list stacked in one 50-word sentence, with "and an answer on ... plus how ..." at the end.
Rewrite: "A ready answer to "what APIs do you have, and can we connect to them". It lists the APIs by area, each with its stability label. It explains how permissions work and how a client routes calls through its own gateway. It covers Snowflake and Databricks connectors. It also says how a client's own AI tools would connect."

**S6. p13, Exhibit 15, row 1, "How to know it worked" cell. Type 2.**
Current: "Time to answer the API section of an RFP; RFPs that score Studio; how many of those are won"
Problem: "RFPs that score Studio" does not say what is counted.
Rewrite: "Time to answer the API section of an RFP. Number of RFPs in which buyers score Studio. How many of those are won."

**S7. p14, Exhibit 16, "Try" row, After qualification cell. Type 2.**
Current: "Studio Compute; an API token or an OAuth application "registered via Studio UI"; and the client's own Aladdin host to call"
Problem: three spec terms in a row ("Studio Compute", "OAuth application", "Aladdin host") with no gloss, joined by semicolons.
Rewrite: "Studio Compute, BlackRock's hosted Python environments. Credentials: an API token, or an OAuth application "registered via Studio UI". The address of the client's own Aladdin environment to call."

**S8. p14, Exhibit 16, "Get help" row, Public today cell. Type 2 and 3.**
Current: "Pull requests on the SDK, reviewed and merged by a BlackRock engineer; on the Studio page, "Book a meeting" and "Download the brochure""
Problem: "pull requests" is developer shorthand. The reader must infer why a code review counts as help.
Rewrite: "Code changes that outside developers propose to the SDK, which a BlackRock engineer reviews and merges. The Studio page offers "Book a meeting" and "Download the brochure"."

**S9. p14, Exhibit 16, "Get help" row, Receipt cell. Type 2.**
Current: "Pull request 52 52, pull request 57 88"
Problem: the label number and the superscript are both 52, so the image reads "Pull request 52⁵²", which looks like a typo.
Rewrite: "SDK change for enterprise gateways [52], SDK change for Pydantic v2 [88]"

**S10. p14, SDK paragraph below Exhibit 16. Type 3 and 2.**
Current: "Its README documents three run modes: ... and a test mode. It stores a prompted password in the operating system's credential manager. It carries settings for firms that consume "the Aladdin APIs via an enterprise API management platform such as Azure API Management" 29."
Problem: three details listed with no point stated, so the reader has to infer what they show. "A prompted password" is unclear. "Consume" is jargon.
Rewrite: "The SDK is the one piece of Studio a prospect can install before any conversation. Its README shows it is built for firms with strict IT controls. It runs in three modes: "a developer's local machine," "Aladdin Studio Compute sessions" and a test mode. When it asks the user for a password, it keeps it in the operating system's credential manager. It has settings for firms that call "the Aladdin APIs via an enterprise API management platform such as Azure API Management" [29]."
(The second sentence is a reading of the README. Keep it only if the author agrees.)

**S11. p14, Exhibit 17 title. Type 4.**
Current: "Investment platforms, Studio among them, open to developers mostly after a relationship"
Problem: half the table (the data and cloud platforms, which score highest) is missing from the title, so the contrast the exhibit shows is not stated. "Studio among them" interrupts the sentence.
Rewrite: "Data platforms let any developer start, while investment platforms, Studio included, mostly open only after a relationship"

**S12. p14, Exhibit 17 legend, "0: None or blocked". Type 4.**
Current: "0: None or blocked"
Problem: the note says some Bloomberg and Clearwater pages "blocked automated access". So a reader can take a 0 to mean the test was blocked, not that the vendor closes access.
Rewrite: "0: None, or closed to non-clients"

**S13. p14, paragraph after Exhibit 17, sentences 3 and 4. Type 3 and 2.**
Current: "The pattern is each vendor's selling model. Investment platforms cluster low because they gate."
Problem: "the pattern is ... model" gestures at the point instead of stating it. "Gate" is used as shorthand with no object.
Rewrite: "The scores follow how each vendor sells. Investment platforms score low because they keep API access behind a contract."

**S14. p14, paragraph after Exhibit 17, whole. Type 3.**
Problem: the paragraph ranks the other vendors but never says where Studio stands. The reader has to read that off the table.
Add (from the exhibit's own scores): "Studio scores in line with the other investment platforms. It trails Bloomberg and Arcesium on AI connectors, where it scores 0 and they score 2."

**S15. p15, About this document, paragraph 1, sentences 2 to 4. Type 1 and 2.**
Current: "The sources are BlackRock product pages, ... and job postings. They also include public code ... trade press. The rest are transcripts of recordings and earnings calls with BlackRock speakers."
Problem: "The sources are" reads as a complete list, then two more groups follow. "The rest are" is vague. Some recordings also include non-BlackRock speakers (for example Crockett of Microsoft [69] and Schafer of Alpha FMC [10]).
Rewrite: "The sources include BlackRock product pages, investor presentations, SEC filings, a fund prospectus, procurement notices, press releases and job postings. They also include public code and packages on GitHub and PyPI, other vendors' product and developer pages, blogs and trade press. Finally, they include transcripts of recordings and earnings calls in which BlackRock speakers take part."

## OPTIONAL

**O1. p13, Exhibit 16, "Read" row, Public today cell. Type 3.**
Current: "The Studio page ("Create & automate," "Make Aladdin your own," "Align internally & externally") and the APIs page, which promises "dozens of Aladdin APIs""
Problem: the quoted taglines hint that the public pages offer slogans rather than detail, but the cell does not say so.
Rewrite: "The Studio page, with taglines such as "Create & automate," "Make Aladdin your own" and "Align internally & externally". The APIs page, which promises "dozens of Aladdin APIs" but does not link the catalog." (p5 already says the APIs page "does not link" the catalog.)

**O2. p13, Exhibit 15, rows 2 and 4, "How to know it worked" cells. Type 2.**
Current: "API calls from client AI tools" / "API calls from clients who build it"
Problem: these fragments do not say whether the measure is a count or growth.
Rewrite: "Number of API calls from client AI tools" / "Number of API calls from clients who build it"

**O3. p13, Exhibit 15, row 3, "What it is" cell. Type 3.**
Current: "a public pension fund already on record"
Rewrite: "a public pension fund already on public record as an Aladdin client"

**O4. p13, Exhibit 15, row 4, last sentence. Type 2.**
Current: "Sewdass names rebalancing tools as what clients build on Aladdin's APIs 10."
Problem: Sewdass was last introduced in Part 2.
Rewrite: "BlackRock's Alisha Sewdass names rebalancing tools as something clients build on Aladdin's APIs [10]."

**O5. p14, Exhibit 17 source note. Type 2 (citation clutter).**
Current: "Source: my test of each platform's public pages 2, 4, 5, ... 103, no accounts or payments, October 8, 2026."
Problem: 28 superscripts sit in the middle of the sentence, and "no accounts or payments" is a fragment.
Rewrite: "Source: my test of each platform's public pages on October 8, 2026, without accounts or payments. Pages tested: [2, 4, 5, 6, 7, 8, 14, 29, 30, 72, 73, 74, 76, 89 to 103]."

**O6. p14, Exhibit 16 against Exhibit 17. Type 1 (possible apparent contradiction).**
Problem: Exhibit 16 lists public "sample code and demo notebooks" for the SDK, but Exhibit 17 gives Studio a 1 (partial) for Sample code. The API-guide samples behind the login explain the 1, but the reader is not told.
Add to the Exhibit 17 note: "Studio's sample code scores 1 because the SDK's samples are public but the API guides' samples are not."

**O7. p14, Exhibit 16, "Hear" row, Receipt cell. Type 2.**
Current: "Woodhead 1, Rosales and Valdez 9"
Problem: these are bare names in a list of items such as "podcast" and "video". Elsewhere (the p6 note) the second name is given as "Rosales and Vicente Valdez".
Rewrite: "Woodhead podcast [1], Rosales and Vicente Valdez talk [9]"

**O8. p15, About page layout. Type 2.**
Problem: the body is set in small BarlowCondensed-Light on a black page, so it is harder to read than the rest of the document.
Fix: use the regular body face and size on this page.

**O9. p18, register entry 68. Type 2.**
Current: "Cameron Skinner, Managing Director and Global Head of Solutions Engineering; all three at BlackRock, September 2025."
Rewrite: "Cameron Skinner, Managing Director and Global Head of Solutions Engineering. All three are at BlackRock. September 2025."

**O10. p16, register entry 10. Type 2.**
Current: "Michael Campos, US asset manager coverage"
Problem: this reads as a role fragment.
Rewrite (if the replay gives no fuller title): "Michael Campos, who covers US asset managers"

Register skim (p16 to 19): no other garbled or unreadable entries. Line-wrapped URLs break mid-word in the PDF, which is normal for long links.
