# Reader 7: head of go-to-market, Bloomberg enterprise

## 1. What the evidence indicates

**Direction.** Exhibit 9 is the most informative page and the author reads it as a count. Read it as a roadmap: 24 of 54 specs are alpha, weighted to investment operations (9 of 15), compliance (3 of 4) and accounting (none stable). The stable core is analytics, the old risk engine. BlackRock is building Studio outward from risk into operations and accounting plumbing, the "end to end life cycle of a transaction" Sewdass sells on page 14. Strong on the specs; moderate as direction. The MCP job posting in Exhibit 14 says agent access is being built, not shipped. Moderate. Exhibit 4 carries a signal the author misses: only the two 2025 speakers name developer tools. The definition is drifting toward tooling, which is what a platform does before it courts third-party builds.

**Position.** Exhibit 2 is honest about one thing: the system-of-record tier gates and the data tier does not. Bloomberg 5 against Studio 4 is noise. The scorecard that matters is Exhibit 14: FactSet, LSEG, MSCI, S&P, Snowflake and Databricks have shipped AI access; Aladdin has a job advert. Strong. The 17x headline I reject: the slide is about the cost of growth, the 10-K ties fees to positions and fixed rates, and Exhibit 12 shows nobody has said "Studio" to investors in six years. The strong inference is the reverse of the author's: Studio is an Aladdin Enterprise feature, not a product line BlackRock monetises or reports.

**Buyer.** Exhibit 15 and the Schafer quote are the best buyer evidence in the document. I see that RFP section weekly: list your API suite, your Snowflake and Databricks connectors. Poll 3, 53 percent would stop maintaining compliance reporting, names the first build. The Janus Henderson pull requests on page 10 and the Azure API Management setting on page 4 say who the buyer's engineer is: an integration team behind an enterprise gateway, not a quant in a notebook. Strong.

## 2. The buried insight

Exhibit 13, source 18 (pull request 57, "dependency conflict with the MCP toolkit," merged August 2026) and the MCP job posting in Exhibit 14 belong on one page and are spread across three. Together they say: the agent surface already exists inside Aladdin, thousands of tools mapped one-to-one to production APIs with per-user entitlements and a tested no-advice guardrail; the door is what is missing; and a client is already putting the SDK next to an MCP toolkit. That is the finding I would fear most at Bloomberg. Every AI row in Exhibit 14 is a data vendor. Data can be read; a system of record can act, and an agent on Aladdin can post an order with runCompliance on.

## 3. Over-claimed, missing, wrong

Over-claimed: the executive summary headline, and "four speakers have defined it the same way" when Exhibit 4 shows two of four omitting developer tools. Exhibit 2 weights "call to action" the same as a sandbox, and three vendors blocked the scraper. "None in my sources" in Exhibit 14's note is not "none"; I would not accept that in an RFP response.

Missing, and disqualifying for a product marketer if not fixed: the commercial model. Nothing on whether Studio is bundled with Enterprise, whether Data Cloud or Compute is metered, or whose API calls the 17x counts. Missing: the bake-off set. Charles River, Bloomberg AIM and State Street Alpha are who Aladdin meets in a tender; the document names none as a rival. Before acting I would want the price schedule, a Data Cloud client count, one scored RFP and the Developer Portal contents.

## 4. First six months, marketing's remit

1. **Write the Studio RFP answer pack** from Exhibits 6, 8 and 9: catalog by domain with stability labels, the OAuth scope model, gateway support (PRs 52 and 53), the Snowflake connector answer. Why: Schafer says the question is in RFPs now and solutions engineers answer it ad hoc today. **Do this first**: it ships in thirty days from material that exists and touches revenue in flight.
2. **Secure one named Studio reference**, from page 10: Janus Henderson, whose engineer commits to the SDK, with Nest or PPF as the public-tender fallback. Why: enterprise deals close on references, and client code is the only Studio proof in the document.
3. **Reposition Studio around the compliance-reporting build**, from Exhibit 15 poll 3: a use-case page, demo script and reference architecture, with the alpha status of those APIs stated honestly. Why: the buyer named the job; the current page sells three personas and no job.
4. **Publish the governance story for AI on Aladdin**, from Exhibits 13 and 14: a page and a sales one-pager on the plugin model, per-user entitlements, the no-advice guardrail, and what "your agent calling Aladdin" means today. Why: FactSet and LSEG own the AI narrative while BlackRock has the better model, unwritten.
5. **Put the catalog in front of the gate**, from Exhibits 1 and 2: a public developer page listing the 54 APIs by domain with stability labels, since they are already on PyPI. Why: it is the first thing an architect looks for and the gate protects nothing.

## 5. What a "what next" box should say

Each box restates its finding. A marketing box names the asset, the audience, the proof it needs and the date. Finding 1: a Janus Henderson or Nest case study for the RFP pack by end of Q1; proof is the client's sign-off. Finding 2: drop "growth story" from Studio messaging, since IR has never used it; message Studio as the build layer of Enterprise. Finding 3: a governance page and SE talk track within 90 days, so "can my agent call Aladdin" gets one answer before a product date exists. Finding 4: the RFP pack and compliance demo, measured by the share of RFPs where Studio is scored and the win rate when it is demoed.

As a hiring manager: the specification work beats most product marketers I have hired, and the receipts habit is rare. The headline shows he will sell past his evidence. I would hire him for the technical seat and pair him with whoever owns pricing.
