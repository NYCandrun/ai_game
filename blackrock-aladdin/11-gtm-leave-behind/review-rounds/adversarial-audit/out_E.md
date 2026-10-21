# Agent E: adversarial audit of the competitive analysis (Exhibits 12 and 17, pages 2, 9–12, 14)

Auditor: Agent E. Date of checks: October 21, 2026. I did not edit the report.

## What I used, and what I could not reach

- **Report text**: `pdftotext -layout` on pages 2, 9, 10, 11, 12, 13 and 14 of `Aladdin_Studio_from_the_outside_v23.pdf`. Source entries came from the HTML register (`id="sN"`).
- **Live pages fetched today** with curl and saved in `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/E_web/` (`sN.raw` / `sN.txt`):
  - fetched: s2, s4, s5, s7, s14, s30, s73, s74, s77, s78, s79, s81, s90 (and its sub-pages `ss_*.txt`), s91, s92, s93, s94, s95, s96 (and Aquata sub-pages `aq_*.txt`), s98, s100 (and `sc_gs.txt`), s102, s104, plus the Aladdin Copilot page (`br_copilot.txt`) and the Data Cloud page (`br_adc.txt`).
- **Pages that blocked me, and what I used in their place**:
  - **s8** (Clearwater, Business Wire): 403. I read the same release, word for word, on the AWS press center mirror (`cw_aws.txt`).
  - **s75 and s76** (Arcesium press releases): a Vercel bot checkpoint returned 429. For s75 I read Alternatives Watch's report of the release (`arc_aw.txt`, Dec 15, 2025; grade T). For s76 I saw only The Drawdown's headline, "Arcesium launches AI platform" (May 2026), and a search-engine summary. **I did not verify s76's contents.**
  - **s80** (AllianceBernstein investor-relations page): 403. I read the same release on simcorp.com (`ab_sc.txt`).
  - **s3** (FactSet release): its body is rendered by JavaScript. I read the text in the page's og:description and in the copy syndicated on Finviz (`fs_finviz.txt`, GlobeNewswire, Dec 16, 2025).
  - **s89** (FactSet developer portal) and **s97** (MSCI developer portal) are JavaScript-only. For FactSet I used its sitemap and app bundle (`fs_dev.js`). I could not render MSCI.
  - **s101** (Business Wire) and **s103** (github.com over curl): 403. I cloned the SDK repositories with git instead.
- **SDK code**: fresh clones of `blackrock/aladdinsdk` (HEAD c1c9f3c, Sep 20, 2026) and `aladdinsdk-plugin-builder` (HEAD 73df174) in `.../audit/E_git/`.
- **PyPI**: I re-downloaded `asdk_plugin_trading` and `asdk_plugin_portfolio` 2.0.0b3 into `.../audit/E_pypi/`. Their SHA-256 hashes match the copies in `scratchpad/pkgs/` (7d97ee85… and 7e493a68…).
- **Transcripts**: the project copy of the Build vs. Buy webinar, which the project marks as BlackRock's published CloudFront captions (`04-transcripts/part2-cloudfront-and-podcasts/049_…md`, and `requested-recordings/nine_recordings_transcripts.md` line 246). The webinar page is live, but the captions track URL on it is empty and the guessed .vtt URLs return 403. **So I did not re-download the captions themselves.**
- **Web searches**: 8 of the 20 allowed.

---

## Q1. Exhibit 12 (page 10), row by row

Title: "Ten of the 11 providers I compared have announced AI features or AI access to their data." The arithmetic holds: 10 rows plus State Street make 11, and Aladdin sits outside the 11 as the "for comparison" row.

### SimCorp: "Agent Launchpad, announced in 2026, is to offer prebuilt AI agents and let clients build their own on SimCorp One's data layer" (source 7)
- **Source** (s7, dated April 22, 2026):
  - "Investment managers will be able to access a growing range of pre‑built AI agents from SimCorp and curated partners… Agent Launchpad will allow clients to build their own agents, with controlled access to data from SimCorp One and approved third‑party providers."
  - "Building on SimCorp One's unified data layer…"
  - "The first SimCorp One clients are expected to gain access this year."
  - Also: "**Today**, SimCorp One clients can use a portfolio management agent as a standalone solution."
- **What it establishes**: an announcement, with access not yet given to clients. The report's future tense ("is to offer") is right.
- **What the row leaves out**: SimCorp already ships a portfolio management agent today. The release also describes Launchpad as the "connective layer" for client-built agents "within a common governance framework", with an audit trail. That is close to the proposition Part 3 puts forward for Aladdin.
- **Verdict**: CORRECT, but understated.
- **Strongest wording**: "SimCorp announced Agent Launchpad in April 2026. It is to let clients use prebuilt agents and build their own, with controlled access to SimCorp One data. A portfolio management agent is already available."

### Arcesium: "added AI features to Aquata, including an MCP server that connects outside AI tools to client data, and launched an AI platform" (sources 75, 76)
- **Source**:
  - The primary pages were blocked (see above).
  - Alternatives Watch (Dec 15, 2025): "the Aquata MCP server allows investment managers to use natural language to work with their investment lifecycle data in Aquata from any enterprise AI interface… The new AI tools are now available to all users of the Aquata platform."
  - Arcesium's own live product page, aquata.ai/feature-aquata-mcp (`aq_feature-aquata-mcp.txt`): "Ask Claude to deploy a connector. It does. Point Claude, ChatGPT, or Microsoft Copilot at one MCP endpoint. Your team queries datasets, **deploys connectors, builds pipelines, and creates quality rules** from the tools they already use… with full audit trail."
- **What it establishes**:
  - An outside-AI MCP endpoint exists and is generally available to Aquata users.
  - It can **act** (deploy connectors, build pipelines, create rules), not only read.
- **Beyond the source**: nothing for the MCP part. For "launched an AI platform" I have only a headline and a search summary (Arcesium Intelligence, about May 2026).
- **Verdict**:
  - MCP part: CORRECT, but understated. The row calls it a connection to data and leaves out that the server can act.
  - AI-platform part: DEFENSIBLE BUT UNCERTAIN, because I could not read the primary release.

### Clearwater: "announced CWAN GenAI, with more than 800 AI agents for clients, in November 2025" (source 8)
- **Source** (AWS mirror of the Nov 5, 2025 release):
  - "today announced the global deployment of CWAN GenAI, a newly-launched, embedded generative AI platform…"
  - "The platform currently supports 800+ AI agents **created by CWAN clients and internal teams**, plus 20 highly trained domain-specific agents."
  - "CWAN GenAI operates as a 24/7 embedded operations layer within its unified platform… where its AI agents are ready to act." It lists "autonomous trade settlement, real-time cash management".
- **What it establishes**: an embedded platform that is in production, by Clearwater's own claim. Most of the 800+ agents were built by clients and Clearwater teams, not supplied by Clearwater "for clients". The release mentions no external AI connector or MCP.
- **What the report inferred beyond it**: "800 AI agents for clients" reads as 800 agents offered to clients. The release says many were built by clients.
- **Verdict**: DEFENSIBLE BUT UNCERTAIN as worded. The date is right and the 800 figure is right. The framing is slightly off.
- **Strongest wording**: "In November 2025 Clearwater announced the global deployment of CWAN GenAI, an AI platform embedded in its own system. It says the platform runs more than 800 agents built by clients and Clearwater teams, including agents that act on operations."

### Bloomberg: "launched an MCP server for licensed data in September 2026" (source 77)
- **Source** (s77, Sep 29, 2026): "Bloomberg today announced the launch of Bloomberg Enterprise Model Context Protocol (MCP), an AI access layer for Data License Plus (DL+)… enables clients' AI agents to discover, understand, and retrieve licensed Bloomberg data…" and "Bloomberg Enterprise MCP is an enterprise offering."
- **Verdict**: CORRECT.
- **Classification caveat**: the product is a **data** product (Data License). Placing it under "System-of-record rivals" lets the page 14 sentence say "Studio… trails Bloomberg… on AI connectors". But Bloomberg's system-of-record product (AIM) is not what this server exposes. A Bloomberg PM would accept the row and question the bucket.

### FactSet: "runs an MCP server for its data and calls it the first in its market" (source 3)
- **Source** (GlobeNewswire copy, Dec 16, 2025): "today announced availability of the **industry's first production-grade** model context protocol (MCP) server…". It also mentions an "Explorer" beta of 45 firms and 800 users. The headline reads "First to Announce MCP Sans Intermediary".
- **Beyond the source**: "first in its market" drops FactSet's qualifiers ("production-grade", "sans intermediary"). LSEG's own release (s2) says LSEG's MCP server was "live in the Claude MCP Partner Directory from Monday 27 October [2025]". That is seven weeks before FactSet's claim. The report attributes the claim to FactSet ("calls it"), so it is not asserting it, but it passes on a contested "first" without context.
- **The register**: it dates s3 only as "2025". The date is December 16, 2025.
- **Verdict**: DEFENSIBLE BUT UNCERTAIN.
- **Strongest wording**: "FactSet has offered an MCP server for its data since December 2025, which it calls 'the industry's first production-grade' MCP server."

### LSEG: "collaboration with Anthropic and an MCP server… 90 customers connected to its MCP server by April 2026" (sources 2, 74)
- **Source**:
  - s2 (Oct 27, 2025): "LSEG today announced a collaboration with Anthropic… LSEG's MCP server, live in the Claude MCP Partner Directory from Monday 27 October."
  - s74 (Apr 23, 2026): "Since launch in December 2025, 90 customers have connected via our Model Context Protocol ('MCP') server… A further 64 customers are in the process of onboarding."
- **Verdict**: CORRECT.
- **Minor point**: LSEG itself gives two launch dates (October 27 in the directory; "launch in December 2025" in the Q1 update).

### MSCI: "offers 'AI connectors' to its proprietary data" (source 4)
- **Source** (Feb 24, 2026): "MSCI unveils new AI connectors…" and "the MSCI app in OpenAI's ChatGPT and the MSCI connector in Claude." The launch product is IndexAI Insights (index data). Other areas, such as Private Assets, are only "planned".
- **Verdict**: CORRECT. The scope is narrower (index data first) than "its proprietary data" suggests.

### S&P Global: "added Credit Ratings to its AI Data Portal in September 2026" (source 78)
- **Source** (Sep 28, 2026): RatingsXpress data "is now available through the S&P Global AI Data Portal, a solution that enables customers to seamlessly access verifiable data **via any MCP-enabled AI application**." Deterministic Retrieval is available now; Adaptive Retrieval is "expected in the coming weeks".
- **Verdict**: CORRECT. The row never says the portal is an MCP route, which is the point of the exhibit. Page 9 counts S&P among the "six… [that] offer a connector or an MCP server", and that count is correct.

### Snowflake: "documents an MCP server for Cortex Agents" (source 5)
- **Source**: the page is now titled "Snowflake-managed MCP server". The server serves "Cortex Analyst, Cortex Search, and Cortex Agents as tools, along with custom tools and SQL executions." It notes per-tool RBAC and sharing MCP servers with other accounts.
- **Verdict**: CORRECT, but narrow. The server is broader than Cortex Agents.

### Databricks: "documents managed MCP servers" (source 79)
- **Source** (last updated Oct 16, 2026): "Databricks provides MCPs in the system.ai schema… You don't need to host or register a server."
  - Some of them need the "Unity Gateway **Beta**".
  - "The Genie One MCP is generally available."
- **Verdict**: CORRECT. Part of the offering is in beta, and the row does not say so.

### Aladdin, for comparison: a job posting naming "Model Context Protocol (MCP), AI agents, and Copilot extensions" (source 73)
- **Source** (Saarthi copy; BlackRock removed the posting): the quote is verbatim. The context matters, though:
  - The role belongs to "BlackRock's Enterprise Data Platform (EDP)… Data Platform as a Service (DPaaS)". That is internal data-product onboarding.
  - MCP appears as tooling: "Implement emerging AI tooling including Model Context Protocol (MCP), AI agents, and Copilot extensions **to automate repetitive onboarding tasks**".
- **What it establishes**: BlackRock engineers use MCP internally for developer productivity. It says nothing about AI access for clients.
- **What the report inferred beyond it**: placing the posting in a row against vendors' client-facing MCP servers, and calling it "the nearest public sign" of how client AI tools would connect (Exhibit 14 note, page 12), stretches it. The posting points to internal tooling, not a client route.
- **Fairness of the row**: the row is unfair to Aladdin in one direction and lenient in another.
  - **Unfair**: the exhibit's own criterion is "AI features **or** AI access". State Street is excluded because it shows "no AI feature it offers clients", so offering AI features to clients counts. By that test Aladdin qualifies. BlackRock's live Copilot page says "Introducing Aladdin® Copilot, now available to all Aladdin clients", and "eFront Copilot, now available within eFront Insight" (`br_copilot.txt`). SimCorp and Clearwater are credited for agents that live inside their own platforms. Aladdin's equivalent (Copilot) is left out of its row.
  - **Lenient**: the posting is presented as an MCP signal when it is internal tooling.
- **Verdict**: OVERSTATED as a signal, and incomplete as a comparison.
- **Strongest wording**: "Aladdin Copilot and eFront Copilot are available to clients inside the platform. BlackRock has published no MCP server or connector for outside AI tools. A September 2026 posting for BlackRock's internal data platform lists MCP among tools for automating onboarding work."

### Page 9: "Aladdin has published no such route. Its only public mention of MCP is a job posting 73." (also in the Exhibit 12 note)
- **"Published no such route"**: I found no MCP or AI-connector code or text in the fresh SDK clone, the plugin builder, the 54 specs, or the live Studio, APIs, Copilot and Data Cloud pages. One web search found no BlackRock MCP announcement. CORRECT, scoped to what BlackRock has published.
- **"Only public mention of MCP is a job posting"**: **WRONG as written.**
  - BlackRock's own Build vs. Buy webinar, which the report cites as source 10, has a BlackRock moderator say: "Because of course, there's the ways that we can make sure this data all comes in the same format. **You can have your MCP, you can have your different APIs**, but how do we actually make use of that data? If you're an engineer and you use one of your cloud code [Claude Code] or Copilot…" (`nine_recordings_transcripts.md` line 246; captions file 049 cue 5c0a032d).
  - By context, the speaker is the moderator, Michael Campos, who introduces himself as covering "the US Asset Managers for Aladdin". This rests on the project's copy of BlackRock's published captions, which I could not re-download.
  - It is a passing mention, not a product statement. It still disproves "only".
- **Strongest wording**: "BlackRock has published no MCP server or connector for Aladdin. The public mentions of MCP I found are a passing remark by a BlackRock moderator on the Build vs. Buy webinar, and a job posting for BlackRock's internal data platform."

### State Street exclusion: "State Street is not listed because my sources show no AI feature it offers clients."
- **What I found**: the claim is scoped to "my sources", which is honest.
  - State Street's developer portal (s90 and sub-pages) shows no AI features.
  - Trade press found by search (ioandc, "State Street wants to give its clients an AI copilot", date unknown; the page returned 500 when I fetched it) describes an "Alpha Co-pilot" in beta on mocked-up data with no release date.
- **Verdict**: DEFENSIBLE BUT UNCERTAIN.
- **Strongest wording**: "State Street has discussed an Alpha copilot in beta. I found no AI feature it has released to clients."

### Page 9: "Six data and cloud providers offer a connector or an MCP server. Four system-of-record rivals have announced AI features or AI access."
- **Counts**: both counts are right on the exhibit's rows.
- **Bucket**: putting Bloomberg among "system-of-record rivals" is debatable, as noted under the Bloomberg row.
- **Verdict**: CORRECT on counts.

---

## Q2. Exhibit 17 (page 14): criteria, consistency, and my re-scoring

### Are the criteria defined?
- **Defined columns**: only two have specific rubrics, the AI connector and the Call to action.
- **Undefined columns**: the other six (public docs, API catalog, trial or sandbox, first call without a contract, sample code, community or marketplace) use only the general legend: "2: Fully public or self-serve / 1: Partial or after sign-up or approval / 0: None, or closed to non-clients".
- **Problems with the general legend**:
  1. "1" mixes two separate ideas. One is coverage (partial). The other is gating (behind sign-up or approval).
  2. "0" mixes **absence** ("None") with **gated to clients** ("closed to non-clients"). Readers will take many of the zeros as "doesn't exist". (Q3 covers this.)
  3. The text says the exhibit scores "eight things a developer with no client relationship can reach". The AI connector column breaks that premise. Bloomberg (2), FactSet (2), LSEG (2) and MSCI (2) offer MCP or connectors **only to licensed clients**, per their own releases ("Bloomberg Enterprise MCP is an enterprise offering"; LSEG "data licensed through LSEG products"). That column measures whether a connector exists, not whether an outsider can reach it.
  4. The exhibit says it was tested on "October 8, 2026". Its source list includes s104, dated October 20, 2026, and s79, updated October 16.
- **Title vs. text**: the title says "Data platforms open to any developer". The text under it says "FactSet and MSCI allow a first API call only for licensed clients" and scores both 0 on the first call. **The title is OVERSTATED.** It holds for Snowflake and Databricks, and partly for LSEG.

### Scores I would change after re-checking live

| Platform | Cell | Report | Mine | Evidence |
|---|---|---|---|---|
| **Arcesium** | First API call without a contract | 0 | **1** (arguably 2) | aquata.ai Demo Center FAQ (s96, the report's own source): "You can request a 30-day trial and get your own production-grade, enterprise environment… **There are no sales calls required to get started**." Pricing FAQ: "most teams start in the $2,000–$4,000 per month range… with a full-featured 30-day free trial." |
| **Arcesium** | Trial or sandbox | 1 | 1 or 2 | Same FAQ; the trial is requested, then self-run. |
| **State Street** | Trial or sandbox | 1 | **0** | developer.statestreet.com/faqs: "Logging into this site requires permissions granted from your State Street Client Service Manager." The sandbox (Sample Transactions API) sits behind a my.statestreet.com login. That is "closed to non-clients" (0), which is also how Aladdin's client-only Studio Compute is scored. |
| **State Street** | Call to action | 1 | 0 or 1 | The only route is "contact your Client Service Manager" or a contact form. That is no more self-serve than Aladdin's "Book a meeting" (0). |
| **Aladdin Studio** | Sample code | 1 | **2** | The public repo has `resources/sample_code_snippets/` (several .md and .py files plus `SDK_Demo_template.ipynb` and `SDK_Demo_ADC_template.ipynb`), and the README links them. Bloomberg gets 2 for a public SDK with examples. Aladdin's are just as public. |
| **Bloomberg** | Public docs | 1 | 2 (or keep 1 with a reason) | professional.bloomberg.com/support/api-library/ (s94) is public. It carries the BLPAPI Core User and Developer Guides and a pip-installable SDK. I had no blocking problem today, so the "blocked automated access" caveat does not apply to this page. |
| **SimCorp** | AI connector | 0 | 0 or 1 | Under the rubric, "1 means one announced". Agent Launchpad is announced and gives client-built agents "controlled access to data from SimCorp One". Whether that counts as an outside AI tool is ambiguous. The rubric needs a ruling. |
| **MSCI** | Sample code | 1 | 1 or 2 | `msci.sdk` 1.37.1 is public on PyPI (published by MSCI, Sep 23, 2026; checked with the PyPI JSON API). It is treated differently from Bloomberg's public SDK. |

### Scores I could not verify or would keep
- **Snowflake and Databricks** (all 2s): consistent with s92, s93 and s102.
- **FactSet**: catalog 2 and trial 1 are supported. The sitemap lists public `/api-catalog/...` pages and `/mcp/factset-ai-ready-data-mcp`, and the app bundle has a "RequestTrial" CTA. I could not render the page text.
- **LSEG**: first call 1 and docs 1 not verified (registration exists; whether data calls need a license was not established).
- **Clearwater** (all 0 except community): developer.cwan.com returned 522 and developer.clearwateranalytics.com returned 403. CWAN owns Beacon Platform, a developer platform, and a CWAN blog post on "Rapid development on Beacon Platform" exists. Those zeros may reflect blocked pages, as the report itself warns.
- **SimCorp** docs, catalog and sample code 0: thesim.dev sends every page to a login "for clients, vendors, and partners". This is a "closed to non-clients" 0, not a "none" 0. The SimCorp landing page says the portal holds "Swagger documentation, practical example code".

### Effect on the conclusions
- **Totals as printed**: Bloomberg 8, State Street 5, Arcesium 5, Aladdin 4, SimCorp 1, Clearwater 1; Snowflake and Databricks 16, LSEG 12, FactSet 11, MSCI 8.
- **Totals after my changes**: Aladdin 5, State Street 3–4, Arcesium 6+, Bloomberg 9.
- "Studio scores in line with them" still holds roughly.
- The sentence "**a first API call needs a contract or a relationship, at Aladdin as at… Arcesium**" does not survive for Arcesium/Aquata. (See the top vulnerable statements.)

---

## Q3. Every "no", "none", "not public" and "0", and whether it is scoped correctly

**Prose and Exhibit 12**

| Statement | Scope | Assessment |
|---|---|---|
| p9: "Aladdin has published no such route" | Publication | CORRECT. It is properly about publication. Possible but unshown: a client could build its own MCP wrapper over the OAuth/Swagger APIs. A Data Cloud client might also use Snowflake's managed MCP server on Aladdin data in its account, since the SDK's ADC connection takes a "Snowflake Account" (README line 146) and Snowflake documents sharing MCP servers across accounts. Neither is documented by BlackRock. Treat both as hypotheses, not capabilities. |
| p9 and Exhibit 12 note: "Its only public mention of MCP is a job posting" | Absolute | **WRONG.** See the Build vs. Buy captions above. |
| Exhibit 12 note: State Street "my sources show no AI feature it offers clients" | Scoped to "my sources" | DEFENSIBLE. A beta Alpha copilot has been discussed in the press. |
| p12 and Exhibit 14: "How a client's AI tools would connect is not public" / "not published" | Publication | CORRECT. |
| Exhibit 14: job posting as "nearest public sign" | Inference | OVERSTATED. The posting is about internal onboarding automation. |

**Exhibit 17 zeros**

| Platform | Cells scored 0 | Assessment |
|---|---|---|
| Aladdin | trial, first call, AI connector, CTA | Correct as "not public". The AI connector 0 is correct under the rubric ("an assistant that works only inside the vendor's own platform"), which in effect admits that Aladdin Copilot exists. |
| Bloomberg | catalog, first call | Correct as gated. |
| State Street | catalog ("No API currently available" in the public grid), first call, AI | Correct as gated or unseen. Its trial should also be 0 (see Q2). |
| Arcesium | docs, catalog, sample code | Unverified; no public API docs found. **First call 0 is wrong**: a 30-day free trial with no sales call is offered. |
| SimCorp | docs, catalog, trial, first call, sample code, CTA | Gated, not absent. A login-only portal with Swagger docs and example code exists. **AI 0** is ambiguous (Launchpad is announced). |
| Clearwater | docs, catalog, trial, first call, sample code, AI, CTA | Mostly unverifiable because of blocking. The AI 0 is correct under the rubric, since CWAN GenAI is embedded, but CWAN GenAI is a large AI offering. A reader of the AI column alone would miss it. |
| FactSet | first call | Correct (licensed clients). |
| MSCI | trial, first call | Consistent with the MSCI access guide (s98). |

**Overall**: the report mostly words absences as "public" or "published". The main exception is Exhibit 17's "0" legend, which merges "none" and "closed to non-clients", together with the "only public mention" sentence. A one-line note under Exhibit 17 would fix most of the risk. For example: "0 means not reachable without a client relationship; it does not mean the capability is absent."

---

## Q4. What would survive a competitor PM's scrutiny, and what they would attack

**Would survive**
- Bloomberg launched an Enterprise MCP for licensed data (Sep 29, 2026).
- LSEG had 90 MCP customers connected (and 64 onboarding) by April 2026.
- MSCI's ChatGPT and Claude connectors.
- Snowflake and Databricks documentation for managed MCP servers.
- SimCorp Agent Launchpad as an announcement.
- Aladdin has published no outside-AI connector.
- Snowflake and Databricks are the most self-serve.
- FactSet and MSCI gate first calls to licensed clients.
- SimCorp's AllianceBernstein and Pictet wins keep "specialized in-house technology". I verified this in both releases on simcorp.com (AB, Feb 17, 2026; Pictet, May 20, 2026: "Pictet AM will leverage API connectivity to integrate SimCorp One… with its specialized in-house technology").

**Would be attacked**
- **Arcesium PM**:
  1. "Aquata has a self-run 30-day trial with no sales call and published pricing. Your page 14 says a first call needs a contract at Arcesium."
  2. "Our MCP lets Claude deploy connectors and build pipelines. It writes, not only reads." That undercuts the executive summary's contrast ("Many data providers now offer AI tools a way to read their data. Aladdin's APIs can also write").
- **Clearwater PM**: "CWAN GenAI agents built by clients are in production and act (settlement, cash management). Agents acting on a system of record is not something Aladdin will be first to." They would also say "800 AI agents for clients" misstates who built them.
- **SimCorp PM**: "A PM agent is live today. Launchpad gives client-built agents governed, audited access to SimCorp One data." That is the same proposition Part 3 offers for Aladdin.
- **FactSet PM vs. LSEG PM**: whoever was "first" with MCP. The report repeats FactSet's claim without its "production-grade" qualifier, while its own LSEG source shows LSEG live seven weeks earlier.
- **Bloomberg PM**: the MCP is a Data License product, not an AIM (system-of-record) product. Its BLPAPI docs and SDK are fully public, so docs should not score 1.
- **State Street PM**: "Our sandbox is client-only, like Aladdin's. Why does ours score 1 and Aladdin's 0?" (They might also cite Alpha AI work.)
- **Snowflake or Databricks PM**:
  - "We are not competitors for 'certain uses'. Aladdin Data Cloud runs on Snowflake."
  - The report's own quoted RFP question ("Are you using connectors to Snowflake or to Databricks?") treats them as complements.
  - A Snowflake PM might add that Snowflake-managed MCP could already serve Aladdin Data Cloud data to a client's AI tool. That is untested, and the report should not assert it either way.
- **MSCI PM**: little to attack. They might note that the connector scope is index data first.

---

## Q5. "Compete with Aladdin for certain uses" (page 14) and "Letting AI tools act will not stay unique"

- **Where the wording actually is**: the brief quotes "Part 1". The words are in the **executive summary** (page 2: "Aladdin will not be alone in letting AI tools act") and **Part 3** (page 12: "Letting AI tools act is unlikely to stay unique"). The executive summary hardens Part 3's hedge ("unlikely") into a certainty ("will not be alone").
- **"Unique" assumes Aladdin is unique today**: both sentences presuppose that letting AI tools act is currently Aladdin's alone. The report's own evidence does not support that. By the report's own account, a client's AI tools have no published route to act on Aladdin ("How those tools would connect is not public"). Meanwhile:
  - Arcesium publicly sells an MCP endpoint through which Claude, ChatGPT or Copilot can perform write actions on Aquata.
  - Clearwater claims client-built agents acting in production.
  - SimCorp has a live agent and an announced framework for client-built agents.
- **What is still defensible**: BlackRock's *own* use (Copilot over production APIs, with per-tool user-group gating and tested guardrails) is the differentiator. So is the breadth of actions in the public specs (orders with compliance by default).
- **Verdict**: OVERSTATED, and the wrong way round.
- **Strongest wording**: "Rivals have begun letting AI agents act: Arcesium through an MCP server, Clearwater and SimCorp inside their platforms. What BlackRock can show that they have not shown publicly is its own business running AI tools on the same production APIs and controls it sells, including order APIs that run compliance by default."
- **"May compete with Aladdin for certain uses"**: the hedge makes it DEFENSIBLE.
  - Fair for SimCorp, Clearwater, Arcesium, State Street (Alpha), Bloomberg (AIM) and, for analytics and risk, FactSet and MSCI.
  - Weak for Snowflake and Databricks, which are Aladdin Data Cloud's substrate and named connector partners.
  - LSEG competes mainly as a data distributor.
  - A note saying Snowflake and Databricks are included as benchmarks for developer experience, not as rivals, would remove the objection.

---

## Factual mistakes vs. reasonable hypotheses

**Genuine factual mistakes**
1. "Its only public mention of MCP is a job posting." BlackRock's own webinar (source 10) contains a BlackRock speaker's mention.
2. Page 14: a first API call "needs a contract or a relationship… at… Arcesium". Aquata offers a self-run free trial with no sales calls (s96, the report's own source).
3. Exhibit 17 title: "Data platforms open to any developer". It contradicts the exhibit's own 0s for FactSet and MSCI.

**Inconsistent application** (mistakes of method, not of fact)
- State Street's client-only sandbox scored 1 vs. Aladdin's 0.
- Aladdin's public sample code and notebooks scored 1 vs. Bloomberg's 2.
- Exhibit 12 credits rivals' in-platform AI but leaves Aladdin Copilot out of Aladdin's row.
- The AI connector column scores existence while the text says it scores what is reachable without a client relationship.

**Framing that overreaches**
- The job posting as "the nearest public sign" of a client AI route.
- "Letting AI tools act… unique".
- "800 AI agents for clients".
- FactSet "first in its market".
- Bloomberg as a system-of-record row for a data MCP.

**Reasonable hypotheses on incomplete information**
- Clearwater's and SimCorp's developer zeros (blocked or login-gated pages).
- State Street having no client AI feature.
- Arcesium's AI platform (primary release not reachable).
- Whether Aladdin clients could already reach Data Cloud through Snowflake's MCP. Unknown either way, and the report does not claim it.

---

## Top vulnerable statements

### 1. "Aladdin has published no such route. Its only public mention of MCP is a job posting." (page 9; repeated in the Exhibit 12 note, page 10)
- **Source**:
  - Build vs. Buy webinar, project copy of BlackRock's published captions (`04-transcripts/requested-recordings/nine_recordings_transcripts.md` line 246). A BlackRock moderator (Michael Campos, by context) says: "You can have your MCP, you can have your different APIs, but how do we actually make use of that data?"
  - Job posting s73 (Saarthi copy): MCP listed among tools "to automate repetitive onboarding tasks" on BlackRock's internal Enterprise Data Platform.
- **What it establishes**: BlackRock staff talk about MCP publicly. BlackRock has published no MCP product. The posting concerns internal tooling.
- **What the report inferred beyond it**: that the posting is the *only* mention; elsewhere, that it is the "nearest public sign" of a client route.
- **Verdict**: "published no such route" is CORRECT. "Only public mention" is WRONG. The "nearest sign" framing is OVERSTATED.
- **Strongest wording**: "BlackRock has published no MCP server or connector for Aladdin. MCP comes up only in passing: from a BlackRock moderator on the Build vs. Buy webinar, and in a posting for BlackRock's internal data platform."

### 2. "Investment platforms score low because a first API call needs a contract or a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium." (page 14; Exhibit 17 Arcesium "First API call" = 0)
- **Source**: aquata.ai/demo-center FAQ (s96): "You can request a 30-day trial and get your own production-grade, enterprise environment… There are no sales calls required to get started." Pricing FAQ: "$2,000–$4,000 per month… with a full-featured 30-day free trial."
- **What it establishes**: an outsider can request and use Arcesium's Aquata without a contract.
- **What the report inferred beyond it**: it groups Arcesium with the contract-only platforms.
- **Verdict**: WRONG for Arcesium/Aquata. CORRECT for the rest, as far as I could check.
- **Strongest wording**: "At Aladdin, Bloomberg, State Street, SimCorp and Clearwater a first API call needs a client relationship. Arcesium's Aquata data platform is the exception, with a 30-day free trial."

### 3. "Aladdin will not be alone in letting AI tools act" (page 2) / "Letting AI tools act is unlikely to stay unique" (page 12)
- **Source**:
  - aquata.ai/feature-aquata-mcp: "Ask Claude to deploy a connector. It does… deploys connectors, builds pipelines, and creates quality rules."
  - CWAN release (Nov 5, 2025): "800+ AI agents created by CWAN clients and internal teams… ready to act."
  - SimCorp s7: "Today, SimCorp One clients can use a portfolio management agent."
  - The report itself, page 12: "How those tools would connect is not public."
- **What it establishes**: rivals already publicly offer or claim AI agents that act. Aladdin publishes no route for clients' AI tools.
- **What the report inferred beyond it**: that Aladdin is currently unique and others will follow.
- **Verdict**: OVERSTATED (presupposition reversed). The executive summary's "will not be alone" is also stronger than Part 3's "unlikely".
- **Strongest wording**: "Rivals have begun letting AI agents act on their platforms. BlackRock's distinctive evidence is its own business running AI tools on the same production APIs and controls it sells."

### 4. Exhibit 12 "Aladdin, for comparison" row: only the job posting (page 10)
- **Source**:
  - BlackRock Copilot page (live): "Introducing Aladdin® Copilot, now available to all Aladdin clients" and "eFront Copilot, now available within eFront Insight."
  - The exhibit's criterion (title and note): "announced AI features or AI access"; State Street is excluded for having "no AI feature it offers clients".
- **What it establishes**: by the exhibit's own test, Aladdin has AI features for clients.
- **What the report inferred beyond it**: the row implies Aladdin's public AI story is a single job posting.
- **Verdict**: OVERSTATED (unfair comparison). The rest of the report does mention Copilot (Exhibit 1, page 9), so this is a problem of the exhibit's framing.
- **Strongest wording**: "Aladdin: Copilot and eFront Copilot for clients, inside the platform. No published connector or MCP server for outside AI tools."

### 5. Exhibit 17 title and legend: "Data platforms open to any developer…"; "0: None, or closed to non-clients"; the AI connector scored on "eight things a developer with no client relationship can reach" (page 14)
- **Source**:
  - The exhibit's own cells give FactSet and MSCI 0 for a first call.
  - Bloomberg s77: "Bloomberg Enterprise MCP is an enterprise offering."
  - LSEG s2: "data licensed through LSEG products".
  - State Street FAQ: "Logging into this site requires permissions granted from your State Street Client Service Manager." Yet State Street's trial is scored 1.
  - aladdinsdk repo: public sample snippets and two demo notebooks, scored 1 vs. Bloomberg's 2.
- **What it establishes**: the scale merges "absent" with "gated". The AI connector column scores existence, not reachability. At least two cells are applied inconsistently.
- **What the report inferred beyond it**: that every data platform is open to any developer, and that the scores are comparable across vendors.
- **Verdict**: OVERSTATED (title), and inconsistently applied (State Street trial, Aladdin sample code).
- **Strongest wording**: Title it "Snowflake and Databricks are self-serve. Most others, including Studio, open fully only to clients." Add to the note: "0 means not reachable without a client relationship, not that the capability is absent; AI connector scores whether a connector exists, most of which are for licensed clients only."
