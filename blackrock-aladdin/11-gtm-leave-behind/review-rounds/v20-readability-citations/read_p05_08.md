# Readability read, pages 5 to 8 (v20)

Scope: rest of Part 1 (Exhibit 5, the specifications paragraph, "What Studio is", Exhibits 6 and 7) and start of Part 2 (finding 1 with Exhibits 8 and 9, finding 2 with Exhibit 10, private-markets paragraph). Checked against page text and page images at 90 dpi. Citations shown as [n].

---

## MUST FIX (garbled or misleading)

### M1. p8, first sentence of the page (finding 1, closing paragraph)
- Current: "None of this proof names Studio, which matters less than it seems."
- Type: 3 ALLUDING. This is the exact gesture the author's standard bans. The reader must infer why it matters less.
- Rewrite: "None of this proof names Studio. It can still back a Studio pitch. Studio is sold for building custom applications on Aladdin. So a buyer wants to know that another institution built on the platform and stayed."

### M2. p7, Exhibit 8 note, last two sentences
- Current: "In 2016 it said it was connecting to Aladdin for custody clients 51. That 2016 report is trade press, not a JPMorgan or BlackRock document."
- Type: 1 GARBLED. "That 2016 report" has no antecedent, since no report was named. "It said" reads as JPMorgan speaking, and the next sentence then says the source is trade press.
- Rewrite: "A 2016 trade press report says JPMorgan was connecting to Aladdin for its custody clients [51]. The report is not a JPMorgan or BlackRock document."

### M3. p6, Goel in Exhibit 6, the body paragraph and Exhibit 7
- Current: Exhibit 6, Goel row: "Data Cloud “within 15 minutes of latency”". Body: "He also describes a near-real-time data store 40." Exhibit 7, Goel "Parts they name": "APIs, events, a near-real-time data store".
- Type: 1 GARBLED (text contradicts a nearby exhibit). Exhibit 6 says Goel speaks about Data Cloud. Exhibit 7 and the body give only "a near-real-time data store". The reader cannot tell they are the same thing, so Exhibit 7 seems to deny Goel names Data Cloud.
- Rewrite, body: "He also describes Data Cloud as a near-real-time data store [40]."
- Rewrite, Exhibit 7 Goel "Parts they name": "APIs, events, Data Cloud (as “a near real time data store”)"

### M4. p6, Exhibit 6 Woodhead row versus Exhibit 7 Woodhead row
- Current: Exhibit 6: "Gives the three-part definition quoted above". Exhibit 7: "APIs, events, Data Cloud, developer tools" (four items).
- Type: 1 GARBLED (exhibits contradict each other on the count).
- Rewrite, Exhibit 7 Woodhead "Parts they name": "APIs and events, Data Cloud, developer tools". Use the same three-part grouping in the Newman and Goel rows ("APIs and events" where both appear).

### M5. p5 block quote and p6 Exhibit 7, Woodhead quotation
- Current: "It exposes everything Aladdin knows how to do as a set of APIs events."
- Type: 1 GARBLED. The verbatim auto-caption text reads as a typo by the author. It appears twice.
- Rewrite (editorial insertion, quote stays faithful): "It exposes everything Aladdin knows how to do as a set of APIs [and] events."

### M6. p7, paragraph after Exhibit 8 (the "kinds of record" list)
- Current: "A second kind of record is code written by a client’s engineers. ... Janus Henderson’s 10-K says that in the third quarter of 2025 the firm chose to move its investment management system to Aladdin, “a complex, multi-year initiative” 55. Public buyers add a third kind of record: procurement notices."
- Type: 1 GARBLED (broken list). The paragraph announces a second kind (client code), then gives a 10-K, which is not code, then a third kind. The first kind is never named.
- Rewrite: move the Janus Henderson sentence into the opening paragraph, after the JPMorgan sentence, and name the first kind there.
  - Opening paragraph, add after the JPMorgan sentence: "Company filings are the first kind of record. Janus Henderson’s 10-K says it chose in the third quarter of 2025 to move its investment management system to Aladdin. It calls the move “a complex, multi-year initiative” [55]."
  - Paragraph after Exhibit 8 then reads: "A second kind of record is code written by a client’s engineers. [SDK sentences.] Public buyers add a third kind of record: procurement notices."

---

## SHOULD FIX

### S1. p5, specifications paragraph, opening
- Current: "The specifications say more than Exhibit 5’s counts: they show how the APIs behave."
- Type: 3 ALLUDING. The paragraph then lists eight facts and never says what they add up to. Most of them are controls built into the APIs (compliance by default, four-eyes sign-off, scoped access), which Exhibit 3 also names.
- Rewrite: "The specifications also show how the APIs behave. Several controls are built into the APIs themselves."

### S2. p5, specifications paragraph, order sentence
- Current: "Posting an order takes whatIf and runCompliance, which defaults to true, and the response returns any compliance violations inline 6."
- Type: 2 HARD TO READ (spec field names used as if self-explanatory, stacked clauses).
- Rewrite: "An order can be posted as a test (the whatIf setting). A compliance check runs by default (runCompliance). The response lists any compliance breaches with the order [6]."

### S3. p5, specifications paragraph, long-running operations
- Current: "Ten specifications expose an endpoint for long-running operations, and 35 operations are flagged as long-running 6. The SDK polls them 29."
- Type: 2 HARD TO READ ("endpoint", "polls"; "them" could be the specifications or the operations).
- Rewrite: "Some operations take time to finish. Ten specifications offer a way to track them, and 35 operations are marked long-running [6]. The SDK checks back on these operations until they finish [29]."

### S4. p5, specifications paragraph, bitemporal and four-eyes
- Current: "Risk exceptions and Data Cloud datasets carry bitemporal fields, which record two time dimensions. Rule assignments and dataset releases name a four-eyes approval, a second sign-off 6."
- Type: 2 HARD TO READ ("two time dimensions" does not say which two; "name" is an odd verb; "Rule assignments" is shorthand for compliance rule assignments).
- Rewrite: "Risk exceptions and Data Cloud datasets carry bitemporal fields. These record when a fact was true and when the system recorded it. Assigning a compliance rule and releasing a dataset both call for four-eyes approval, a second person’s sign-off [6]."

### S5. p5, specifications paragraph, credentials and scopes
- Current: "Every request carries an application key and a second credential. That is an OAuth 2.0 token, a client key, or a user name and password 6. OAuth scopes look like trading.order_management.order.v1.Order:read 6. The client ID and secret come from the Studio UI 29."
- Type: 2 HARD TO READ and 3 ALLUDING. "That is" reads as "i.e.". The scope string is shown without its point. "Client ID and secret" and "UI" are unexplained.
- Rewrite: "Every request carries an application key and a second credential. The second credential is an OAuth 2.0 token, a client key, or a user name and password [6]. Access is granted per API and per action. A typical OAuth scope reads trading.order_management.order.v1.Order:read [6]. Developers get their OAuth client ID and secret from Studio’s screens [29]."

### S6. p5, Exhibit 5 note
- Current: "Alpha, beta, stable and sunset are the stability labels each specification carries (its x-aladdin-api-stability field), alpha being the earliest; the four columns count specs by label."
- Type: 4 EXHIBITS (spec field name in a reader note, semicolon, "sunset" not explained).
- Rewrite: "Each specification carries one stability label: alpha, beta, stable or sunset. Alpha is the earliest stage and sunset marks an API being retired. The four columns count specifications by label."

### S7. p5, Exhibit 5 labels
- Current: rows "Portfolio management" and "Portfolio" side by side; Total row puts "11 domains, 11 PyPI packages" under "Largest APIs by operations".
- Type: 4 EXHIBITS. A reader cannot tell how "Portfolio" differs from "Portfolio management". The total text sits under a column it does not describe.
- Rewrite, note: add "Domain names are BlackRock’s own, taken from each specification’s id." Total row: move "11 domains, 11 PyPI packages" into the note as "The 54 specifications span 11 domains and 11 PyPI packages."

### S8. p6, Exhibit 6 Khara row
- Current: "Named “the Aladdin studio estate” as a 2024 focus, meaning programmatic access “at machine scale”"
- Type: 4 EXHIBITS ("meaning" leaves unclear whether Khara or the author gives the meaning).
- Rewrite: "Named “the Aladdin studio estate” a 2024 focus. Described it as programmatic access “at machine scale”"

### S9. p6, Exhibit 6 and Exhibit 7 notes
- Current: Exhibit 6: "Quotations are verbatim from the transcripts; three of the five are machine transcriptions, marked as such in the Sources section at the end of this document." Exhibit 7: "Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked as such..."
- Type: 4 EXHIBITS (semicolon; people are called transcriptions).
- Rewrite, Exhibit 6: "Quotations are verbatim from the transcripts. Three of the five transcripts are machine-made, as marked in the Sources section."
- Rewrite, Exhibit 7: "The Khara, Goel and Woodhead quotations come from machine or auto-caption transcripts, as marked in the Sources section."

### S10. p6, Jeff Miller drops out between Exhibit 6 and Exhibit 7
- Current: Exhibit 6 lists five speakers, including Miller on Data Cloud. Body: "Khara, Newman, Goel and Woodhead describe ways for clients to reach Aladdin through code." Exhibit 7: "Four speakers describe parts of Studio".
- Type: 1/4. Miller also names a part (Data Cloud), so the reader wonders why he is left out.
- Rewrite, add to Exhibit 7 note: "Miller, in Exhibit 6, speaks only about Data Cloud replacing file transfers, so he is not shown."

### S11. p6, job posting sentence
- Current: "A 2026 job posting for a product director of Aladdin Studio Developer calls it “Aladdin’s extensibility layer” 46."
- Type: 1 GARBLED (dangling "it": Studio, or Aladdin Studio Developer).
- Rewrite: "A 2026 job posting calls Studio “Aladdin’s extensibility layer” [46]. The role is a product director for Aladdin Studio Developer."

### S12. p6, last sentence of body paragraph
- Current: "APIs and data access recur across speakers and years, so BlackRock already has the core of a positioning for Studio."
- Type: 3 ALLUDING ("the core of a positioning" hints without saying what it is).
- Rewrite: "Speakers since 2024 describe Studio as APIs and data access. BlackRock can build Studio’s positioning on that shared description."

### S13. p7, Georgeson sentence
- Current: "On BlackRock’s video, Hans Georgeson, then chief executive of Royal London Asset Management, credits Aladdin’s Snowflake implementation 48."
- Type: 1/2. "Credits" has no object (credits it with what). "Aladdin’s Snowflake implementation" reads as BlackRock’s own work, while the speaker means his firm’s implementation within its Aladdin programme. "On BlackRock’s video" names no video.
- Rewrite: "In a BlackRock client video, Hans Georgeson praises the Snowflake implementation in Royal London’s Aladdin programme [48]. He was then chief executive of Royal London Asset Management."

### S14. p7, SDK contribution sentences
- Current: "In December 2025 an engineer at a client firm submitted two changes to the open-source SDK: URL rewriting and custom headers. Both are for firms that route Aladdin calls through an enterprise gateway. The BlackRock engineer who co-wrote the SDK’s launch post merged them 38, 52, 53, 54."
- Type: 2 HARD TO READ ("URL rewriting", "custom headers", "enterprise gateway", "merged").
- Rewrite: "In December 2025 an engineer at a client firm submitted two changes to the open-source SDK. Both help firms that send Aladdin calls through their own enterprise gateway. One rewrites web addresses and one adds custom headers. The BlackRock engineer who co-wrote the SDK’s launch post accepted both into the SDK [38, 52, 53, 54]."

### S15. p8, finding 1 closing sentences and callout
- Current: "Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public. So they are the natural first candidates for a named Studio story." Callout: "A named Studio story can start with clients whose Aladdin use is already on the record."
- Type: 2 HARD TO READ ("named Studio story" is shorthand; firms do not issue tenders, public buyers do).
- Rewrite: "Some clients are easier to name in public: public pension funds, and firms whose filings already name BlackRock. They are the natural first subjects for a Studio case study that names the client." Callout: "A Studio case study that names the client can start with clients whose Aladdin use is already on the record."

### S16. p8, finding 2 heading
- Current: "2. BlackRock’s growth story to investors runs through Studio, though it rarely says the name"
- Type: 1 GARBLED (dangling "it": a story cannot say a name, and BlackRock is in the possessive).
- Rewrite: "2. BlackRock’s growth story to investors runs through Studio, but BlackRock rarely names Studio to investors"

### S17. p8, Investor Day sentences
- Current: "At its 2025 Investor Day it forecast four volumes to 2030. API calls across BlackRock and Aladdin led, with 17x growth 11. Attributing them to Studio is my inference. I make that inference because API use is the activity the Studio page describes 14."
- Type: 2 HARD TO READ ("four volumes" is shorthand, "17x", two sentences to state one inference).
- Rewrite: "At its 2025 Investor Day, BlackRock forecast four usage measures to 2030. API calls across BlackRock and Aladdin had the fastest forecast growth, 17 times [11]. I attribute those API calls to Studio, because the Studio page describes API use [14]."

### S18. p8, 10-K fee sentences
- Current: "BlackRock’s 10-K says technology services fees are generally set by the value of positions on the platform or at a fixed rate. They can also depend on subscriptions, go-lives and support. The 10-K does not list API calls among the fee terms it names 12."
- Type: 3 ALLUDING (the reader must infer what this means for the 17x forecast) and 2 ("go-lives" is jargon).
- Rewrite: "BlackRock’s 10-K says technology services fees are generally set by the value of positions on the platform or at a fixed rate. Fees can also depend on subscriptions, client launches (go-lives) and support. The 10-K does not list API calls among its fee terms [12]. So, under the terms it names, more API calls do not by themselves raise fees."

### S19. p8, Exhibit 10 note
- Current: "My tally. The non-zero counts add up to about four mentions in six and a half years. A zero means the term appears in no transcript; the non-zero counts are approximate."
- Type: 4 EXHIBITS (fragment, semicolon; "about four" beside a column that adds to exactly four).
- Rewrite: "The tally is mine. The non-zero counts total four mentions in six and a half years, and are approximate. A zero means the term appears in no transcript."

### S20. p8, private-markets paragraph
- Current: "In September 2025 its private markets team described the result on a client webinar 68. ... And “over 10 different transaction types” were added to Aladdin, covering commitments, fundings, paydowns and PIK, so private credit loans are captured natively. The team said those were designed with BlackRock’s own professionals and “our new colleagues from HPS” 68."
- Type: 2 HARD TO READ ("the result" is vague; "PIK", "captured natively" and "HPS" are unexplained; "those" is loose).
- Rewrite: "In September 2025 its private markets team described what the two deals brought clients, on a client webinar [68]. ... More than 10 new transaction types were added to Aladdin (“over 10 different transaction types”). They cover commitments, fundings, paydowns and payment-in-kind (PIK) interest. So Aladdin now records private credit loans directly. The team said it designed the new types with BlackRock’s own professionals and “our new colleagues from HPS” [68]." Add a short gloss for HPS where it first appears (for example, "HPS, the private credit firm BlackRock bought").

---

## OPTIONAL

### O1. p5, "What Studio is", first sentence
- Current: "I pulled about 125 recordings. Five BlackRock speakers in them describe Studio or its parts 1, 22, 40, 44, 45."
- Type: 2 ("pulled" is informal and does not say recordings of what).
- Rewrite: "I gathered about 125 recordings. In them, five BlackRock speakers describe Studio or its parts [1, 22, 40, 44, 45]."

### O2. p7, Exhibit 8 note, middle sentences
- Current: "The grey 2016 bar is a payment for integration services; the figures in the text start with 2017."
- Type: 4 (semicolon joining sentences).
- Rewrite: "The grey 2016 bar is a payment for integration services. The figures in the text start with 2017."

### O3. p7, Exhibit 9 note
- Current: "The PPF notice gives BlackRock’s Aladdin web page as the supplier’s address 56."
- Type: 4 and 3 ("PPF" is not used in the table; the point of the address is left to the reader).
- Rewrite: "The Pension Protection Fund notice gives BlackRock’s Aladdin web page as the supplier’s address [56]. This links the award to Aladdin."

### O4. p8 (and the same label on later pages), callout label
- Current: "What this finding suggests about direction."
- Type: 3 (vague label; it does not say what kind of direction).
- Rewrite: "What this means for Studio’s marketing."

### O5. p8, private-markets paragraph has no stated point until the p9 callout
- Current: paragraph ends "Newman, the Studio general manager, names eFront data and Preqin among the data being added to Data Cloud 22."
- Type: 3 (the link to finding 2 is left for the callout on the next page).
- Rewrite, add as the last sentence: "So the private-markets data BlackRock bought reaches clients partly through Studio."
