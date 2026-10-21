# Fix-list panel: competitive-intelligence analyst

Reviewer role: competitive-intelligence analyst covering investment-management platforms and financial data vendors. Date of checks: October 21, 2026. I did not edit the report or the fix list.

**What I checked myself**
- Saved competitor pages in `audit/E_web/`:
  - SimCorp: s7
  - Arcesium: aq_feature-aquata-mcp, aq_pricing, s96 raw FAQ JSON, arc_aw
  - Clearwater: cw_aws
  - Bloomberg: s77
  - FactSet: fs_finviz
  - LSEG: s2, s74
  - MSCI: s4
  - S&P Global: s78
  - Snowflake: s5
  - Databricks: s79
  - State Street: s90 and ss_*
  - Job posting: s73
- The v23 PDF, pages 2 and 9 to 14, and the source register.
- The source 71 transcript (`04-transcripts/product-pages/ms_podcast_2.txt`) and the Rosales and Valdez transcript.
- The PyPI JSON for `msci-sdk`.

**Web searches:** 8 of 8 used. Two pages fetched:
- The syndicated Arcesium Intelligence release (ABL Advisor, Business Wire copy, May 21, 2026).
- The State Street co-pilot article (investmentnews.co.nz).

---

## 1. Stance

As a CI analyst I read the fix list the way an Arcesium, SimCorp or Clearwater product manager would. Most of the comparative fixes go the right way. A few new wordings would still be taken apart:
- the State Street "Alpha Co-pilot" beta is from December 2023
- "some data providers let them act" has no source
- "most mapped to production APIs" has no source
- "runs AI over the … controls it sells" contradicts fixes 11 and 33

The list also misses the rival that matters most for the evolved thesis. Arcesium Intelligence (May 2026) already offers what the evolved thesis describes: client-built agents, model choice, a governed orchestration layer, and an MCP server for any enterprise AI tool, across Arcesium's front-to-back platform. So the evolved thesis is accurate but not differentiated on its own. Its edge has to come from what Aladdin's tools do (post orders, with compliance by default) and from scale already in production (about 2,000 registered tools and agents).

---

## 2. Verdicts

Counts over the 61 fixes:

| Verdict | Count |
|---|---|
| ACCEPT | 9 |
| ACCEPT WITH CHANGE | 12 |
| REJECT | 0 |
| DEFER | 40 |

### The evolved thesis (fix 1): ACCEPT WITH CHANGE
- **Headline.** Keep it as the author proposes: "Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls." Keep the MCP route labelled as an inference.
- **Why it needs more.** The headline alone is no longer differentiated:
  - **Bloomberg's split is the same.** Bloomberg's Enterprise MCP release (s77) describes the same server-side and model-side split as the author's reasoning. "Bloomberg validates a firm's entitlements before returning data on any agent request … tool-level limits cap the securities and fields returned." It also says "Bloomberg hosts and manages Enterprise MCP, while clients control the AI agents and applications … including the models, prompts, instructions."
  - **Arcesium makes the same control claim.** Arcesium's MCP page says "Every AI tool inherits the same access controls, audit trail, and schema discovery."
  - **SimCorp makes the same governance claim.** Launchpad puts agents "whether from SimCorp, a trusted partner, or built by the client" inside "a common governance framework", with an audit trail (s7).
  - **Arcesium Intelligence covers the rest.** It is "model-agnostic by design". Its orchestration layer offers "full control over model selection, access, human oversight, auditability, and governance". Its "MCP server … connect[s] any enterprise AI tool to their governed data foundation" (Business Wire, May 21, 2026).
- **Change.** The differentiation has to be carried in the body. Use the competitive paragraphs under fix 3, ending with this sentence (scoped absence, re-check before sending): "I found no rival that publishes a way for outside AI tools to post orders."

### Tier 1

| # | Verdict | Reasoning and exact wording |
|---|---|---|
| 2 | ACCEPT WITH CHANGE | "most mapped to production Aladdin APIs" has no source. The talk gives two ways to onboard, a tool "mapping one-to-one to an existing Aladdin API" or a custom agent, and no proportion. Wording: "BlackRock already runs AI on these APIs. Copilot answers questions for staff and clients by calling about two thousand registered tools and agents. A team can map a tool one-to-one to a production Aladdin API or register an agent of its own. Public sources show Copilot answering, not acting." |
| 3 | ACCEPT WITH CHANGE | The direction is right. Three problems with the wording: (a) "BlackRock already runs AI over the production APIs and controls it sells" asserts what fixes 11 and 33 say is not public (no evidence that Copilot goes through OAuth scopes or the public APIs). (b) SimCorp's source does not say its agent acts. (c) Arcesium's MCP actions are data-pipeline actions, not investment actions. **p2:** "Rivals have begun letting AI agents act. Arcesium lets outside AI tools build data pipelines, and Clearwater and SimCorp offer AI agents to their clients 7, 8, 75. BlackRock already runs Copilot for staff and clients on about two thousand registered tools and agents 9. I found no rival that publishes a way for outside AI tools to post orders." **p12:** "Rivals have begun letting AI agents act. Arcesium's MCP server lets outside AI tools build data pipelines, and its May 2026 AI platform lets clients build their own agents 75, 76. Clearwater says clients use its agents for trade settlement and cash management 8. SimCorp has announced Agent Launchpad, which is to give client-built agents controlled access to SimCorp One data, with an audit trail 7. What BlackRock can show is scale in production. Copilot runs in about 100 BlackRock applications on about two thousand registered tools and agents, and the team that owns each tool sets which user groups can use it 9." Add the Aquata MCP page (aquata.ai/feature-aquata-mcp) to the register as the source for "build data pipelines". |
| 4 | ACCEPT WITH CHANGE | "some let them act" is unsourced for any data provider. The cited sources (2, 3, 4, 5) are all read routes, and Arcesium is filed as a system-of-record rival. The real contrast is what gets written. Wording: "Many data providers now let outside AI tools read their data 2, 3, 4, 5. Aladdin's APIs can also post orders and assign compliance rules to portfolios 6." |
| 5, 6 | DEFER | Controls and spec scopes are outside my remit. |
| 7 | DEFER | Investor Day attribution is commercial evidence. No competitive issue. |
| 8 | DEFER | Connectivity. For context, it is consistent with rivals: a client program can call Aladdin today, as with any OAuth API. |
| 9 | ACCEPT WITH CHANGE | Confirmed against s73: the posting is for BlackRock's internal Enterprise Data Platform (DPaaS) and is not a client route. Drop it from Exhibits 12 and 14. Hatched box: "How they would connect is not published." Exhibit 14 note: "Asked in November 2024 about clients wanting Aladdin plug-ins in their own copilots, BlackRock's Head of Product for AI said '100%' and 'we are hearing that from our clients' 71." Keep the date: the demand evidence is two years old, and rivals have shipped since. |
| 10 | ACCEPT | It matches what rivals already promise ("human oversight", "humans remain accountable"), so it is credible and not overclaimed. |
| 11, 12 | DEFER | Exhibit architecture. |

### Tier 2

| # | Verdict | Reasoning and exact wording |
|---|---|---|
| 13 | DEFER | Spec detail. |
| 14 | ACCEPT | "BlackRock has published no MCP server or connector for Aladdin." This is correct. A search on October 21 found no BlackRock MCP announcement. |
| 15 | ACCEPT WITH CHANGE | Confirmed in the s96 FAQ: "request a 30-day trial … There are no sales calls required." The pricing FAQ says "Reach out and we will provision one." So the trial is by request: **trial stays 1** (not 2), **first call becomes 1**, call to action stays 1, and Arcesium's total becomes 6. p14: "Investment platforms score low because a first API call needs a client relationship at Aladdin, Bloomberg, State Street, SimCorp and Clearwater. Arcesium offers its Aquata data platform on a 30-day free trial, on request 96." |
| 16 | ACCEPT WITH CHANGE | I verified the count: 8 of the 11 offer outside AI tools a connector or MCP server (FactSet, LSEG, MSCI, S&P, Snowflake, Databricks, Bloomberg, Arcesium). The proposed second sentence leaves out Arcesium's in-platform agents and LSEG's Workspace AI tools, so name only the like-for-like group. Title: "Eight of the 11 providers offer outside AI tools a connector or an MCP server. Aladdin's AI, like SimCorp's and Clearwater's, works inside the platform." |
| 17 | ACCEPT | Matches the Copilot page ("now available to all Aladdin clients"; eFront Copilot "now available within eFront Insight"). |
| 18 | ACCEPT | "Snowflake and Databricks are self-serve. Most others, Studio included, open fully only to clients." This still holds after the Arcesium rescore, because Arcesium's trial is by request. |
| 19–24 | DEFER | Specs and workflow. |

### Tier 3

| # | Verdict | Reasoning and exact wording |
|---|---|---|
| 25 | DEFER | Commercial evidence. |
| 26 | ACCEPT | From a competitive angle, rivals lead with named institutions (SimCorp with AllianceBernstein and Pictet, 80 and 81). A named engineering client is the right equivalent. |
| 27–31 | DEFER | Outside my remit, but see section 3: the wordings of 27 and 31 break rules or carry the unsourced "most". |
| 32 | ACCEPT WITH CHANGE | Arcesium, a system-of-record rival, also lets outside AI tools in. "Data providers" alone would be challenged. Heading: "Aladdin's own AI assistant works only inside Aladdin. Data providers and Arcesium let outside AI tools reach their data." |
| 33 | DEFER | The logic is sound and I agree with it, but it is outside my remit. Its wording has a semicolon (section 3). |
| 34 | ACCEPT WITH CHANGE | "Reword each row to the source" is not wording. Exact rows follow this table. Keep Bloomberg in the rivals group (AIM is a real system-of-record rival) and make the row say it is a data product. Moving it would cascade into page 9, Exhibit 17 and the p14 prose. |
| 35 | ACCEPT WITH CHANGE | I agree with the rescoring. The proposed note has a semicolon, the date fix has no wording, and MSCI is missed: MSCI publishes `msci.sdk` 1.37.1 on PyPI (PyPI JSON, author "MSCI"), the same footing as Bloomberg's public SDK scored 2. Exact changes follow this table. |
| 36 | ACCEPT WITH CHANGE | (a) The proposed sentence joins two clauses with a semicolon. (b) The problem cell says "Databricks is a named connector partner", but no source in the report or the audits shows an Aladdin Databricks connector (fix 56 says the same), so that claim must not reach the text. (c) LSEG, FactSet and MSCI also feed Aladdin, so they are not "compete" cases either. Replace the first sentence of the p14 paragraph rather than adding one: "Exhibit 17 puts Studio beside five investment platforms that compete with Aladdin and five data and cloud platforms, included as benchmarks for developer access. Aladdin Data Cloud runs on Snowflake." |
| 37–41 | DEFER | Exhibit design and spec detail. Fixes 38 and 41 have semicolons (section 3). |
| 42 | ACCEPT | The arithmetic checks: 24 quarters from 2020 to 2025, plus Q1 to Q3 2026, makes 27. |

**Exact Exhibit 12 rows (fix 34)**
- **SimCorp:** "SimCorp offers a portfolio management agent today. Agent Launchpad, announced in April 2026, is to let clients use prebuilt agents and build their own, with controlled access to SimCorp One data" (7).
  - Re-check before sending: s7 says "The first SimCorp One clients are expected to gain access this year."
- **Arcesium:** "Aquata's MCP server lets outside AI tools query data and build pipelines. Arcesium Intelligence, launched in May 2026, adds over 100 agents and a studio for clients to build their own" (75, 76, plus the Aquata MCP page).
  - Neither auditor read s76's primary release. I read the Business Wire text syndicated by ABL Advisor. Confirm on arcesium.com.
- **Clearwater:** "Clearwater's CWAN GenAI, launched in November 2025, runs over 800 agents built by clients and Clearwater teams inside its platform" (8).
- **Bloomberg:** "Bloomberg launched Enterprise MCP in September 2026, giving clients' AI agents access to its licensed Data License data" (77).
- **FactSet:** "FactSet has offered an MCP server for its data since December 2025, and calls it the industry's first production-grade MCP server" (3).
- **LSEG:** keep the row. It is correct.

**Exact Exhibit 17 changes (fix 35)**
- **Scores:**
  - State Street: trial 0
  - Aladdin: sample code 2
  - Bloomberg: public docs 2
  - MSCI: sample code 2
  - Optional, my judgment: State Street call to action 0. Its only route is "contact your Client Service Manager", which is the same footing as Aladdin's "Book a meeting", scored 0.
- **New totals:**

  | Platform | Total |
  |---|---|
  | Bloomberg | 9 |
  | MSCI | 9 |
  | Arcesium (with fix 15) | 6 |
  | Aladdin | 5 |
  | State Street | 3 or 4 |
  | SimCorp | 1 |
  | Clearwater | 1 |

  "Studio scores in line with them" and "LSEG and FactSet come next" still hold.
- **Note:** "A 0 can mean the item exists but is closed to non-clients. The AI connector column scores whether a connector exists, and most connectors are for licensed clients."
- **Date:** "October 8 to 20, 2026".

### Tier 4

| # | Verdict | Reasoning and exact wording |
|---|---|---|
| 43, 44 | DEFER | Specs. |
| 45 | ACCEPT | Ranking unlike measures ("fastest") is a comparison a rival analyst would dismiss. "four volume estimates to 2030" is right. |
| 46–48 | DEFER | Commercial evidence. |
| 49 | ACCEPT | I verified the source 3 half: the FactSet release is dated December 16, 2025. I did not check source 58. |
| 50–55 | DEFER | Commercial, controls and webinar detail. |
| 56 | ACCEPT | "Snowflake (and Databricks, if offered) connectors". Buyers ask about both (Schafer, 10), and no public Aladdin Databricks connector was found. |
| 57, 58 | DEFER | Specs. |
| 59 | ACCEPT WITH CHANGE | The State Street "Alpha Co-pilot" beta comes from an article dated **December 3, 2023** (investmentnews.co.nz, quoting Clayton Issitt, head of Alpha APAC client solutions). It was "running on mocked-up data" with no release date. A search on October 21, 2026 found no release since. Undated, "has discussed … in beta" reads as current, and a State Street PM or a BlackRock reader would catch it. Exact rows follow this table. |
| 60, 61 | DEFER | Specs. |

**Exact wording for fix 59**
- **MSCI:** "MSCI offers AI connectors in ChatGPT and Claude, starting with index data" (4).
- **S&P Global:** "S&P Global's AI Data Portal serves its data to any MCP-enabled AI application. It added Credit Ratings in September 2026" (78).
- **Snowflake:** "Snowflake documents a managed MCP server for its Cortex AI tools and SQL" (5).
- **Databricks:** "Databricks documents managed MCP servers, some of them in beta" (79).
- **State Street note:** "State Street is not listed because I found no AI feature it has released to clients. In December 2023 it described an Alpha Co-pilot in beta." Add the article to the register as a T source.

### Section 5 evidence (62–69)
- **62: ACCEPT, with the date and the framing.** Microsoft's Crockett raised the idea of plug-ins in clients' own copilots. Garson answered "100%" and "we are hearing that from our clients". She did not raise it herself.
- **63–68: DEFER.**
- **69: ACCEPT WITH CHANGE.** The two SimCorp phrases come from different sentences. "Controlled access to data from SimCorp One" refers to client-built agents. "Within a common governance framework" refers to multiple agents working together. Quote them separately. Pair the item with Arcesium Intelligence and Bloomberg's server/client split (see section 4). That keeps the comparison honest: three rivals are moving the same way.

---

## 3. Fixes the list gets wrong

### New factual errors or unsourced claims
- **Fixes 2 and 31, "most mapped to / most of them production Aladdin APIs".** No source gives a proportion. The talk describes two onboarding paths only. Fix 33 itself argues that most tools probably do not use the 54 public APIs, so "most" also risks misleading.
- **Fix 3, "runs AI over the production APIs and controls it sells".** This contradicts fix 11 (no evidence Copilot goes through OAuth scopes) and fix 33 (whether Copilot uses the public APIs is not public). It also groups SimCorp with rivals that let agents act, when its source shows only an available agent and an announced Launchpad.
- **Fix 4, "some let them act".** No data provider source shows outside AI tools acting. Arcesium, the only outside-AI write case, is filed as a rival, and its writes are data-pipeline actions, not investment actions.
- **Fix 59, State Street "Alpha Co-pilot" in beta.** The source is from December 2023. Undated, it reads as current.
- **Fix 36 problem cell, "Databricks is a named connector partner".** Nothing in the sources supports it, and fix 56 contradicts it.
- **Fix 15, "trial 1 or 2".** The trial is by request ("Reach out and we will provision one"), so it is 1 under the legend. A 2 would breach the report's own scale.
- **Fix 34.** It gives no wording. Its option "Move Bloomberg to the data group" cascades into page 9, Exhibit 17 and p14 without the list saying so.

### Writing-rule breaks in proposed wording
**Semicolons joining two sentences:**
- 23: "The engine runs it; a named team resolves violations."
- 27: "…what the payments cover; JPMorgan is also a custodian…"
- 33: "…is not public; with about 2,000 tools…"
- 35: "…a connector exists; most are for licensed clients."
- 36: "…developer access; Aladdin Data Cloud runs on Snowflake."
- 38: "…samples; the portal sits behind a client login."
- 41: "…no channels; the maintainers merged…"
- 61: "named alongside Projects; not described publicly."

Replace each semicolon with a full stop.

**Borderline fragments:** 31's "One answer; policy: no investment advice". Better: "One answer. Copilot does not give investment advice."

### Conceptual distortion
- **Fix 16** names only Aladdin, SimCorp and Clearwater as offering in-platform AI. Arcesium (Arcesium Intelligence) and LSEG (Workspace AI tools, s74) do too.
- **Fix 32** says only "data providers" let outside AI tools in, which leaves out Arcesium.

---

## 4. Anything missing

1. **Arcesium Intelligence (May 21, 2026).** It is the closest published version of the evolved thesis:
   - over 100 pre-configured agents across Opterra, Arcesium's front-to-back operations platform, and Aquata
   - Agent Studio for client-built agents
   - a model-agnostic orchestration layer with "human oversight, auditability, and governance"
   - an MCP server for "any enterprise AI tool"

   v23 cites it (76) only as "launched an AI platform", and neither auditor read it. The comparative text has to reflect it, and someone must read the primary release.
2. **Bloomberg's server/model split (s77) as evidence for the evolved thesis.** It shows the MCP route the author infers is the industry's standard pattern: the vendor hosts the server and checks entitlements per request, and the client owns models and prompts. That strengthens the inference. It also shows the control split is table stakes, not a moat.
3. **Page 9 count sentence.** Fix 16 changes the title, but page 9 still says "Six data and cloud providers … Four system-of-record rivals have announced AI features or AI access", and it carries the job posting sentence. Wording: "Eight of the 11 providers I compared offer outside AI tools a connector or an MCP server: all six data and cloud providers, Bloomberg and Arcesium. BlackRock has published no MCP server or connector for Aladdin."
4. **The Aquata MCP page needs a register entry.** The "deploys connectors, builds pipelines, and creates quality rules" claim behind fixes 3, 4 and 34 sits on aquata.ai/feature-aquata-mcp, which is not in the register. Source 75's trade-press summary says only "query" and "analytical or data transformation workloads".
5. **Exhibit 17 scores the list leaves out.** MSCI sample code should be 2 (public `msci.sdk`). State Street's call to action could be 0.
6. **Dates on the Exhibit 12 rows.** Every rival move falls between October 2025 and September 2026. Showing the dates tells a BlackRock reader how fast the field is moving, which is the point of the comparison.
7. **Freshness checks just before v24 goes out.**
   - SimCorp said first Launchpad clients would get access "this year". If it is live by the send date, "is to" becomes wrong.
   - Re-run the "no rival lets outside AI tools post orders" check.
8. **A risk to note, not to add.** If the thesis leans again on "BlackRock runs its own business on it", an Arcesium PM can point to Arcesium's D.E. Shaw origin. That origin is not in the report's sources, so don't assert it either way. The evolved thesis avoids this by resting on Copilot's tool registry instead.

---

## 5. Top 5 recommendations, in priority order

1. **Rewrite the competitive paragraphs on p2 and p12 using the fix 3 wording above.**
   - Name what each rival actually does: Arcesium builds data pipelines through MCP, Clearwater runs settlement and cash agents, SimCorp has a live agent and an announced Launchpad.
   - Drop the unsourced "most mapped" and "controls it sells".
   - End on the scoped differentiator: scale in production, and no rival publishing a way for outside AI tools to post orders.
2. **Fix the Arcesium errors as one set.**
   - p14 and Exhibit 17: first call 1, trial stays 1, total 6 (fix 15).
   - The Exhibit 12 row: MCP that acts, plus Arcesium Intelligence (fix 34).
   - The register: add the Aquata MCP page and read s76's primary release.

   Arcesium is the rival that would most easily embarrass the report today.
3. **Make Exhibit 12 fair both ways** (fixes 16, 17, 14, 9, 59, plus missing item 3).
   - "Eight of the 11" title.
   - The Aladdin row shows Copilot and drops the internal job posting.
   - Page 9 count sentence updated.
   - State Street note dated or dropped.
4. **Make Exhibit 17 consistent and rule-compliant** (fixes 35, 18, 36).
   - Apply the rescoring including MSCI.
   - Use the semicolon-free note, the date range "October 8 to 20, 2026", and the "benchmarks for developer access" framing.
   - No Databricks-partner claim.
5. **Adopt the evolved thesis headline, but treat it as a direction rivals share, not a unique claim.**
   - Add fix 69, Arcesium Intelligence and Bloomberg's server/client split as evidence that the market is moving this way.
   - Let the edge rest on Aladdin's order and compliance tools and Copilot's production scale.
   - Keep the MCP route labelled as the author's inference.
