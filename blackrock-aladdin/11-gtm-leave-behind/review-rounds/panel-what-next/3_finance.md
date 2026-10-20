# Finance read: what the filings and calls actually support

## 1. What the evidence indicates

**Direction.** The page 2 headline, "Studio is the product behind the growth story BlackRock tells investors," is not what the sources say. The 17x figure comes from the 2025 Investor Day slide on *keeping the cost of growth low* (source 1, per the author's own footnote). That is an operating-leverage exhibit, not a revenue slide. The 10-K (source 8) confirms it: technology services fees are set on positions on the platform, fixed rates, subscriptions, go-lives and support. API calls appear nowhere in the fee terms. The filings support the opposite. Zero mentions on 26 calls (Exhibit 12), zero EDGAR hits (source 42) and no Studio line in the 10-K make a strong case that Studio is packaging inside Aladdin enterprise contracts, not a SKU. Data Cloud is the exception, and the only component an executive has priced out loud: "an add-on sold with Aladdin Enterprise" on the Q3 2022 and Q4 2024 calls (Exhibit 12). Strong inference.

**Position in market.** Exhibit 2 measures revenue model, not access. Snowflake and Databricks score 16 because they sell consumption to developers; Aladdin scores 4 because it sells multi-year ACV to a COO. A low score is the model working. Exhibit 9 cuts the other way: 24 of 54 specifications are alpha against 23 stable, so the monetizable surface is still narrow. Moderate inference.

**The buyer.** Exhibit 10 is the best primary evidence here: JPMorgan's DEF 14A related-party disclosures, $7.6M in 2023 to $25.6M in 2025. But a 3.4x step over two years at a client flat for seven looks like go-live or implementation recognition on a new mandate, exactly the fee type the 10-K names, not usage growth. The footnote concedes JPMorgan is a custodian, so the figure may include Provider fees. Exhibit 11 holds a pricing signal the author passes over: PBGC renewed in 2023 at an *unchanged* price after six years. The proposed first references are the buyers with flat renewals. The webinar polls (Exhibit 15) are self-selected and vendor-run, with no n: weak.

## 2. The buried insight

Page 11, under Exhibit 12: Data Cloud is the one Studio piece BlackRock has priced and described to investors, and it is the delivery channel for Preqin indices, eFront data and the new private-credit transaction types. So Studio's monetization runs through *data attach*, not API calls: Preqin is a cash acquisition BlackRock must earn a return on, Data Cloud is the add-on carrying it, and the 24 percent growth "including Preqin" is year one. The document has all three facts and buries them under a number nobody is paid on.

## 3. Over-claimed, missing, wrong

- **The 17x attribution.** The slide says "across BlackRock and Aladdin." BlackRock is Aladdin's largest user and Exhibit 13 shows Copilot calling APIs on every question, so much of the 17x may be internal traffic touching no client contract.
- **$2.0B up 24 percent, "including Preqin."** No organic figure, and no mention of ACV growth, the metric BlackRock reports every quarter for this business. An argument that never says "ACV" is not yet a finance argument.
- **Exhibit 12's method.** Third-party transcripts, approximate counts, Investor Day not tallied. Zero is as consistent with "immaterial" as with "under-told."
- **Exhibit 10's chart.** Payment year without contract phase invites the wrong read. I would want the proxy footnote text (license, Provider, or both), the dating of JPMorgan Asset Management's migration, and whether 2025 includes implementation fees.
- **Missing.** Retention, client count, Data Cloud pricing, Preqin's revenue contribution, and SimCorp's segment disclosure inside Deutsche Börse to size the "core plus builds" market.

## 4. First six months, in the marketing remit

1. **First: write the claims file.** A one-page substantiation sheet agreed with Aladdin finance and investor relations: Studio is not a fee term, Data Cloud is a priced add-on, the 17x is a cost-of-growth metric including internal traffic. Why: every claim here rests on the 10-K fee terms and Exhibit 12, and a PMM who gets the investor story wrong in front of a CFO buyer loses the room; every other deliverable inherits its language.
2. **Reposition Studio around data attach.** Rewrite the Studio page and pitch so Data Cloud plus Preqin and eFront data is the expansion story and APIs the retention story. Why: page 11 shows data is the priced surface; the page today leads with "Create & automate," the unpriced one.
3. **Produce one named reference from the public record.** Draft the Janus Henderson case from its 10-K and merged commits (page 10), with an Exhibit 11 pension as fallback, and take it through legal. Why: proof already in a filing needs the least new approval, and the Studio page names nobody.
4. **Ship the governance one-pager for RFPs.** From Exhibit 13 and the Schafer quote on page 14: which APIs, whose permissions, what guardrails. Why: RFPs now score API suite and connectors, and Aladdin's only public MCP statement is a job advert (Exhibit 14).
5. **Publish the pre-conversation developer kit.** A public catalog summary, the Exhibit 6 walkthrough and an SDK quickstart, no sandbox. Why: Exhibit 1 shows a prospect's engineer must unpack PyPI packages to learn what exists; content closes that gap without a sandbox the ACV model does not need.

## 5. What the boxes should say

Each box should name a deliverable, an owner and a test. Finding 1: "One named reference in print within two quarters; candidates Janus Henderson, PPF, Nest; owner PMM with legal; test is a quote cleared for the Studio page." Finding 2: "API calls are not a fee term, so the message to CFO and investor-facing audiences is retention through APIs, expansion through Data Cloud and Preqin data; test is that the Studio page, brochure and IR language agree." Finding 3: "The governance one-pager in sales enablement by quarter end; test is use in the next three RFP replies." Finding 4: "A 'core platform plus your builds' message track aimed at the 48 percent who said hybrid or reevaluating; test is RFPs answered with it and pipeline tagged to it."
