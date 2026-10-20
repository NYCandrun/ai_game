# Strategy read: what the evidence says, and what it does not

## 1. What the evidence indicates

**Direction.** The strongest structural inference is Exhibit 7 read with Exhibit 13: apps, Copilot and client code call one shared API layer, and Copilot's tools map "one-to-one to an existing Aladdin API". Two engineers on the record make that strong evidence: Studio's catalogue and Copilot's tool registry are one asset. Exhibit 9 says how far along it is: 24 of 54 specs are alpha, trading has two specs, and there is no position or event API. Moderately strong inference: the platform is being opened from the back office and data outward, not from the front-office workflow a portfolio manager would build on. The 17x API-call figure on page 2 is the weakest link. The slide is about the cost of growth, and the 10-K ties fees to positions, not calls (page 11). It is an operating-leverage claim; the attribution to Studio is the author's, and I would not act on it.

**Market position.** Exhibit 2 is more useful than its framing. Studio scores 4; system-of-record peers score 1 to 5, so gating is the category norm. The telling cluster is Snowflake and Databricks at 16, and Aladdin Data Cloud sits on one of them. With confidence: Studio's competitor for the client's developers is not SimCorp but the Snowflake or Databricks estate the client already owns, where it can build around Aladdin rather than on it. Exhibit 14 sharpens this: every data provider the buyer compares has an outside-AI connector; Aladdin has a job posting.

**Buyer.** Exhibit 15 and the Sewdass quotes (page 14) agree: two-thirds run vendor or hybrid stacks, AI and data demands lead, and the buyer's language is "system of record" plus "system of work". The Janus Henderson pull requests (page 10) add a detail the document under-reads: the client routes Aladdin calls through its own gateway. The buyer is the CTO who owns that gateway and answers Schafer's RFP question; the engineer is the user.

## 2. The buried insight

The document proves, then walks away from, the fact that changes Studio's weight: the API layer is the agent layer. Finding 3 establishes it (Exhibit 13, "no copilot without plug-ins") and reduces it to a governance-communications tip. Every API that reaches stable becomes a Copilot capability and a client-agent capability at once; every alpha in Exhibit 9 is something Copilot cannot yet do either. And pull request 57, cited only as a "get help" receipt in Exhibit 1, is a dependency conflict with an MCP toolkit merged in August 2026: someone is already combining the SDK with outside agent tooling. That, and the 3,000 citizen-developer figure source 28 mentions but the body omits, is adoption evidence the document had and did not use.

## 3. Over-claimed, missing, wrong

- **The headline over-claims.** "Studio is the product behind the growth story" rests on the 17x inference and on JPMorgan's $25.6 million (Exhibit 10), which the footnote concedes may be custody and Provider fees.
- **Exhibit 12's zero needs a control.** Without a count for "eFront" or "Aladdin Wealth", zero mentions of Studio says nothing about priority.
- **Exhibit 2 sums unlike things.** Equal weights, three vendors blocked, substitutes beside complements, and a premise that openness is good. For a system of record holding client positions, gating execution is right; gating documentation is the only real question.
- **Missing: how Studio makes money.** Bundled, priced, or metered through Compute? Only Data Cloud is shown as a sold add-on (Exhibit 5).
- **Missing: was Aladdin in the AllianceBernstein and Pictet tenders** (page 14)?
- **Editing error.** The sources entry for 28 says Exhibit 3 credits a 3,000 figure to Woodhead; Exhibit 3 contains none.

Before acting I would want Studio telemetry: client-originated API calls as a share of total, active client developers, and the price sheet.

## 4. First six months, in marketing's remit

1. **Rebuild the proof base, first.** Audit every Studio claim in deck, web page and RFP library against the public record (Exhibits 10, 11, page 10) and replace 17x and the JPMorgan number with claims the evidence carries: Janus Henderson engineers contributing to the SDK, three pension tenders, five executives with one definition (Exhibit 3). First because repeating page 2 to a CTO will get caught, and every move below reuses this base.
2. **Rewrite positioning around the governed API layer (Exhibits 7, 9, 13).** A CTO- and CISO-facing narrative on scopes, per-user permissions, four-eyes approval and no-advice guardrails, with the alpha-to-stable map stated plainly, because the buyer's top driver is AI (Exhibit 15) and rivals have shipped connectors (Exhibit 14).
3. **Publish the catalogue the gate does not need to hold (Exhibits 1, 2, 9).** A public page listing the 54 APIs, domains and stability labels, since the specs are already on PyPI and today an engineer must unpack packages to learn what BlackRock sells.
4. **Secure two named Studio references (Exhibits 10, 11).** Start with clients whose Aladdin use is already public, because Studio is sold on Aladdin's reputation, which SimCorp's modular pitch can match.
5. **Write the RFP answer and SimCorp One competitive card (page 14).** Package Sewdass's system-of-record plus system-of-work language and the stability map into enablement; track win rate where "build on platform" is scored.

## 5. What a "what next" box should say

Each box should name what marketing produces, for whom, and how it is measured. Finding 1: a named Studio case study from clients already on the record, in every RFP response by mid-2027. Finding 2: drop 17x from Studio material until telemetry supports it, and lead with the attributable private-markets story, Preqin through Data Cloud and Explore. Finding 3: a published governance narrative for Copilot and Studio, written for the CTO who owns the gateway, before the agent conversation moves to Snowflake and Databricks collateral; measured by use in security reviews. Finding 4: an RFP answer to the "API suite" question with the honest stability map and a SimCorp One card; measured by win rate in scored build-on-platform tenders.
