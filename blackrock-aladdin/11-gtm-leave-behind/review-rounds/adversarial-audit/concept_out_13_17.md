# Conceptual check: Exhibits 13 to 17

Reviewer scope: whether each exhibit is conceptually right. I did not re-check numbers against their citations. Evidence I used: the webinar transcript (`/home/user/ai_game/blackrock-aladdin/04-transcripts/part2-cloudfront-and-podcasts/049_Build_vs_Buy_Webinar_Replay.md`), the Rosales and Valdez transcript (`.../part1-youtube-and-site/16_How_BlackRock_Built_Production_AI_Agents_for_Asset_Managemen.md`), the Copilot product page (`scratchpad/drift22/dl_a/p_aladdin-copilot.txt`), the OrderAPI and EnrichedCapitalFlowAPI specifications in `scratchpad/unpacked/`, the SDK in `scratchpad/drift22/sdk_b` (README, SUPPORT.md, config), and the job postings `dl_a/job41.html` and `dl_a/job50.html`. Three web searches, on whether Clearwater has an MCP server and whether Aladdin has a Databricks connector, turned up nothing either way, so I make no claim on those points.

Severity key: **Real error** means a reader would come away believing something false. **Judgment call** means a reasonable expert might draw it differently. **Nit** is minor.

---

## Exhibit 13. Webinar poll results (page 11)

**Verdict: SOUND WITH CAVEAT**

The title matches the bars, and the section heading's "two thirds" (37 + 30) follows from them. The caveats concern what the poll can carry.

- **Judgment call: who answered.** The respondents are a self-selected audience at a webinar BlackRock ran to market Aladdin to asset managers, and the number of respondents is not given. The axis label "Share of attendees" really means share of the attendees who answered. Part 3 does say the poll "gives no sample size", but the exhibit and the heading on page 10 do not. One line under the exhibit would fix this: "Respondents to a BlackRock-hosted webinar; number of respondents not given."
- **Judgment call: forced choice.** The moderator framed poll 3 as "choosing only from these fours, there's others, apologies … what capability would you most like to stop maintaining internally?" The title's "would stop maintaining … first" turns a forced pick of a preference into an implied plan or order of work. "Would most like to stop maintaining, of four options offered" is what the poll actually measured.
- **Nit: mixed categories in poll 1.** "Actively reevaluating" is not a kind of platform, since a firm can be reevaluating while mostly on vendors. That does not affect the 67 percent, which leaves it out.
- **Fit with the text.** The chart is about buying commodity functions. The section's "direction" (that Studio could lead the API section of an RFP) rests on Schafer's quote and Sewdass's remarks, not on the chart. That is fine, because the text does not say the chart shows it. Schafer's actual RFP question is about "openness structure … API suite … connectors to Snowflake or to data bricks". The text's paraphrase "whether they can build on the platform" is a fair reading.

---

## Exhibit 14. BlackRock's apps, Copilot and client code share APIs and controls (page 12)

**Verdict: MISLEADING**

The underlying idea is defensible: Aladdin Graph is one API runtime "for BlackRock and over 200 institutions" (job41), and the Studio Developer posting talks of turning "internal success into client adoption" (job50). But three framing problems would lead a reader to believe false things.

1. **Real error: the "BlackRock's own use" vs "a client's use" split is false.** The left column puts "About 100 BlackRock applications" (Explore, Dashboard, Risk Radar) and Copilot under "BLACKROCK'S OWN USE". These are Aladdin's client-facing products. Rosales calls them "the around 100 Aladdin front-end applications that thousands of people use every day". The Copilot page says "now available to all Aladdin clients", and Exhibit 1 in this same document says the same. A BlackRock insider would say clients use those apps and Copilot every day. The true split is *built by BlackRock (used by BlackRock and clients)* against *built by the client through Studio*. Relabelling the left column fixes this, and it also makes the document's argument stronger: clients already run an AI tool (Copilot) on Aladdin under these controls. The same misframing is in the Part 3 text ("What BlackRock can show is its own use").
2. **Real error: the hatched box puts the gap in the wrong place.** "How they would connect is not published" reads as though no path exists for a client's AI tool. In fact the public specifications already define how *any* client program connects. Every spec lists OAuth 2.0 access-code (acting for a user) and client-credentials (acting as an application) flows; the Order spec, for example, has the scopes `trading.order_management.order.v1.Order:read/write` at `client.blackrock.com`. The open-source SDK wraps those flows. Nothing stops a client's agent from calling the APIs through the SDK today. What is unpublished is an *AI-specific* connector (for example an MCP server) and any policy for AI callers. The box should say exactly that.
3. **Judgment call, close to an error: Copilot's guardrails are drawn under the client column.** The input guardrails, output guardrails and LLM judges are nodes inside Copilot's own LangGraph orchestration (Rosales: an input guardrail node, then a filtering and access-control node, then planning, then output guardrail nodes). They govern Copilot's model, not calls to the API. A client's own AI tool calling the APIs would never pass through them. The caption's hedge ("the model a client's own AI tools could follow") is accurate, but the layout puts these boxes directly under "A client's use", which suggests they apply there. These are also guardrails for an assistant that *answers questions* (Rosales's examples are exposure and how much can be bought). They are not controls on actions, and the document's thesis is about AI that acts. The Copilot control that matters most here, the plug-in registry's per-tool gating by environment, user group and app, is in the Part 3 text but missing from the exhibit.

Smaller points:
- **Judgment call: "share … controls".** The left-hand controls (OAuth scopes, `runCompliance`) are documented for external callers. Whether BlackRock's own front-end apps and Copilot tools go through the same OAuth-scoped gateway is not public. Rosales says only that each tool maps "one-to-one to an existing Aladdin API already out in production". `runCompliance` is a parameter of the Order API, so it plausibly applies to any caller; OAuth scopes may not. Either "share Aladdin's APIs" without "and controls", or a caveat, would be safer.
- **Judgment call: one "Aladdin's APIs" bar.** A single bar can be read as one shared instance. In fact each client has its own environment and host (the SDK's `defaultWebServer` is "BlackRock client environment's default web server"). The line "Each client reads its own Data Cloud" also sits awkwardly inside an API bar, because Data Cloud is reached through Snowflake and not through these APIs. The caption partly covers this.
- **Nit: "Approvals on record".** The capital-flow fields (`approverUserId`, `cancelApprover`) are an audit trail. The stronger control in the same spec is that each write needs the user's Aladdin "newcash" entitlements (CASH_PAY, CASH_CONF …) and moves through states (OPEN → AUTHORIZED → CONFIRMED). In other words, API calls carry the user's Aladdin permissions. That is worth showing, and it supports the thesis.
- **Nit: overgeneralized client boxes.** "Route Aladdin calls through the client's own gateway" generalizes from one client's two SDK changes; per the README, routing through a gateway is an option, not the norm. "Its applications run in the client's own environment" leaves out Studio Compute, which BlackRock hosts and which the SDK supports as a run mode.
- **Nit: "Each tool maps to a production Aladdin API".** This is correct for tools. Rosales describes a second onboarding path, custom agents for complex workflows, and the box counts "tools and agents" together.

---

## Exhibit 15. Four pieces of marketing work (page 13)

**Verdict: SOUND WITH CAVEAT** (one real error in row 2 that should be fixed)

The four rows follow from the findings. Row 4, the worked example, fits the APIs well: `whatIf` and `runCompliance` exist on the Order API, Sewdass names rebalancing tools, and a portfolio manager approves before anything trades.

- **Real error: row 2, "under the same permissions, compliance checks and guardrails Copilot uses".** Permissions and compliance checks sit on the API side, so they would apply to a client's AI tool. Copilot's guardrails do not: they run inside Copilot's orchestration (see Exhibit 14, point 3). A page that promised client AI tools run under Copilot's guardrails would describe something that does not exist unless BlackRock builds a hosted gateway or MCP layer that embeds them. Either say "with guardrails modelled on Copilot's", or make the gateway itself the proposal.
- **Judgment call: row 3, "a public pension fund already on record".** The procurement records (PPF, Nest, PBGC) show the buyer bought Aladdin, not that it uses Studio, so a Studio case study needs a Studio user. Public bodies are also often the *hardest* to name in marketing. PBGC is a US federal agency, and federal rules generally bar employees from endorsing commercial products (5 CFR 2635.702). The SDK-contributor client is the better-evidenced Studio user.
- **Judgment call: row 1, "with stability labels".** Publishing labels shows that 24 of the 54 public specs are alpha. That is honest, but it may weaken an RFP answer. It is worth flagging as a deliberate choice. "Covers Snowflake and Databricks connectors" is fine as a topic to answer. I found no public evidence of a Databricks connector for Aladdin, so the answer may have to be "Snowflake only".
- **Nit: measures.** "API calls from client AI tools" can only be measured if AI callers are identified, for example by a separate OAuth application or the SDK's user-agent suffix. "Number of RFPs in which buyers score Studio" assumes RFPs score Studio separately from Aladdin.

---

## Exhibit 16. What is public at each step, and what opens after qualification (pages 13 to 14)

**Verdict: SOUND WITH CAVEAT**

The journey framing is reasonable, and the absences are well scoped ("read with no account or login", "what those sources say a client receives", "I could not test it"). "Nothing to run: no public sandbox or trial is offered" holds: the SDK's `test` run mode is for SDK developers, not a sandbox.

- **Judgment call: "qualification" vs "client".** The title and column say "after qualification", but most of what that column lists (developer portal login, credentials, client host, Studio Compute) comes with being a *client*, not a qualified prospect. The caption itself says the portal opens "only after a client login". A reader may think a qualified prospect gets a token. Use "After becoming a client", or split the column into prospect and client.
- **Judgment call: the "Get help" row is in the wrong category.** The "public" cell gives SDK pull requests from a *client's* engineer, merged by BlackRock. That shows the maintainers respond, but it is not help a prospect can get. The "after qualification" cell lists notebooks and code samples, which are documentation, not support. The real help channels (client service, Solutions Engineering) are in the "Hear" row instead. The repo's SUPPORT.md has empty "Documentation / Slack Channel / Forum" headings, which would be the sharper public fact for this row.
- **Nit: "See the catalog — public".** The 54 specs are public, but only inside wheel files that have to be unpacked. A prospect would not see them as a catalog. "Public, but only by unpacking the packages" sets expectations correctly.

---

## Exhibit 17. Developer openness scores across 11 platforms (page 14)

**Verdict: SOUND WITH CAVEAT**

The headline split (Snowflake and Databricks self-serve; investment platforms gated by contract) follows from the rows. The text's conclusion, "The scores follow how each vendor sells", is the right and fair one. AI connector scores are consistent with Exhibit 12 under the stated definitions: SimCorp's and Clearwater's agents are in-platform, so 0; State Street has no AI offering, so 0.

- **Real error (moderate): the text's frame does not match the AI connector column.** The text says the exhibit scores "eight things a developer with no client relationship can reach". The AI connector column scores whether a connector *exists*, not whether a non-client can reach it. Bloomberg's MCP server is "for licensed data" (Exhibit 12), and FactSet and MSCI allow a first API call only to licensed clients, yet all three get 2. Either rescope the sentence ("eight signals of developer openness, mostly what a non-client can reach") or rescore the column for non-client reach.
- **Judgment call: the title over-generalizes.** "Data platforms open to any developer" fits Snowflake and Databricks, partly fits LSEG, and does not fit FactSet or MSCI (first API call 0, as the text says).
- **Judgment call: "platforms that may compete with Aladdin".** Snowflake runs Aladdin Data Cloud, and LSEG, FactSet and MSCI feed data into Aladdin. A BlackRock reader will see these as partners and benchmarks, not competitors. "Benchmarks for developer access" is the safer word.
- **Nit: unlike units compared.** Studio, a developer layer, is scored against whole vendors (Bloomberg, LSEG). The caption's note that blocked pages may have lowered Bloomberg's and Clearwater's scores is good practice.

---

## Cross-cutting issue (Exhibits 14 and 15, and the executive summary)

The document's thesis says a client's AI tools would act "under the same controls BlackRock uses". That holds for the **API-side** controls: per-API OAuth scopes, the user's Aladdin entitlements, `runCompliance` by default, `whatIf`, and state transitions. It does not hold for **Copilot's model-side** guardrails, which live inside Copilot. The exhibits mostly hedge this, but Exhibit 15 row 2 states it outright. Keeping the two layers apart throughout would make the thesis both true and stronger.
