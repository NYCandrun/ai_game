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
