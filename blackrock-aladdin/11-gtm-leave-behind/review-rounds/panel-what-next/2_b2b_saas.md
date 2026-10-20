# Panel 2, B2B SaaS go-to-market: what the Aladdin Studio evidence indicates

## 1. What the evidence indicates

**Direction.** Studio is Aladdin's extensibility layer; the open question is whether it is a product or a feature. Exhibits 3 and 4 (five executives, one definition, 2024 to 2025) settle the first point strongly. Exhibit 12 answers the second: zero mentions on 26 earnings calls, and a 10-K that prices on positions and fixed fees, not API calls. Strong primary evidence that Studio is an attach-and-retention asset inside the Aladdin Enterprise contract, not a revenue line; Data Cloud is the only piece sold as an add-on (Exhibit 5, Q3 2022 call). Exhibit 9 says the surface is real but young: 24 of 54 specs alpha, SDK at 2.0.0b3.

**Market position.** Exhibit 2 is the clearest statement of the selling model: Studio scores 4 of 16, gated like every system of record. That Studio is sales-led and will stay so is a strong inference; that this is a weakness is not. Nobody buys an IBOR off a free tier. Exhibit 14 shows the real exposure: the data providers a buyer also uses have shipped connectors or MCP servers; Aladdin has a job advert. Strong on the facts, moderate as a threat, since those are not system-of-record rivals. Among rivals, SimCorp has two named wins (page 14).

**Buyer.** The best buyer evidence is the plumbing, not the poll. The SDK README carries Azure API Management settings (page 4); a Janus Henderson engineer contributed gateway URL rewriting and custom headers (page 10); pull request 57 is a dependency conflict with an MCP toolkit. The buyer's developer is a platform-engineering team routing Aladdin through its own gateway. Schafer (page 14) says the evaluation moment is the RFP and the questions are "what APIs, which connectors." Exhibit 15 is a self-selected audience with no sample size, but its direction (42 percent cite AI and data; 53 percent would outsource compliance reporting first) fits.

## 2. The strongest buried insight

The GitHub repository is the only live demand signal in the document, filed as a footnote under "proof." Clients are gatewaying Aladdin and loading the SDK beside agent toolkits, unprompted. Add Finding 3 (Copilot's "couple of thousand" tools are one-to-one mappings of production APIs, built by 50 to 60 internal teams) and the story is: BlackRock's 4,000 engineers are Studio's customer zero, and clients now want to do with their own agents what Copilot does inside the login. Positioning, proof and demand in one place, filed under governance.

## 3. Over-claimed, missing, wrong

- The executive summary leads with 17x API calls attributed to Studio. The author concedes the inference; the slide is about unit cost across all of BlackRock and Aladdin, Wealth, Provider and Copilot included. The weakest number holds the most prominent position.
- Exhibit 2 sums unweighted scores across two selling models and implies a gap. The right metric for a gated product is time-to-first-call after contract, unmeasured here.
- Exhibit 12 over-reads negative evidence; earnings calls discuss segments. Exhibit 10 says nothing about Studio; JPMorgan is a custodian.
- The document drops its only adoption number: source note 28 says Goel and Woodhead give a 3,000 citizen-developer figure, yet it appears nowhere in the body.
- A mismatch goes undrawn: buyers would outsource compliance reporting first (Exhibit 15), and compliance is the thinnest, least stable public domain (9 operations, 3 alpha, Exhibit 9). And there is no public position API (Exhibit 6, step 4) in a story about building on the IBOR.
- Missing: packaging and entitlement, PyPI download trends, win/loss against SimCorp, and the Snowflake, Microsoft and AWS co-marketing channel. Before acting I would want active OAuth applications by client, external API calls by domain, and a defined citizen-developer count.

## 4. First six months, marketing's remit

1. **Produce the RFP and evaluation kit; do this first.** Exhibits 6, 9 and 13 are the raw material: the trade-to-NAV walkthrough, the catalog by domain with stability labels, gateway and connector support, and the Copilot permission model as the governance answer. Schafer says the deal is decided here and Exhibit 2 says PLG is not the motion, so this is where product marketing has the most leverage, soonest.
2. **Write the positioning and messaging hierarchy around customer zero.** "The APIs Copilot runs on, built on by 50 to 60 BlackRock teams" (Exhibit 13, Finding 3) is a proof point no rival in Exhibit 14 can make, and replaces the borrowed 17x in every deck.
3. **Run a named-reference program.** PPF, Nest, PBGC and Janus Henderson are already on the record (Exhibit 11, page 10); one case study fills an empty Studio page.
4. **Publish the developer-facing catalog page and the plugin-model explainer.** The 54 specs are already public via PyPI (Exhibit 1), so gating the catalog costs discovery and gains nothing; the explainer answers the question every provider in Exhibit 14 is answering.
5. **Ship a compliance-reporting solution brief and demo.** Exhibit 15 names the demand and Exhibit 9 shows the thin API; a worked example on Data Cloud plus the compliance domain is the sharpest wedge content available, and tells product where the gap hurts.

## 5. What a "what next" box should say

Each box should name what marketing produces, a measurable, and what would refute it.

- **Finding 1.** Secure one on-record quote from PPF, Nest or Janus Henderson on building on Aladdin by the second quarter. Measure: a named client on the Studio page. If none will go on record, that is the finding.
- **Finding 2.** Stop borrowing 17x. Agree a Studio metric with product and IR (active client applications or external API calls) and put it in the next investor narrative. The test: will IR say the word.
- **Finding 3.** Publish the plugin and permission model as the external position on AI access, and brief analysts and press on it before FactSet and LSEG define the agent entry point for the buyer.
- **Finding 4.** Turn the poll into sales content: a compliance-reporting reference story with the connector and gateway answers the RFP now asks. Measure: win rate where the build-on-platform section is scored.
