<!-- agent a86689be5c8b336c5; started 2026-10-19T13:42:07.779Z; finished 2026-10-19T13:45:58.878Z -->

## Evidence caveat (read first)

File 04 is not BlackRock Aladdin. It is a sales demo of "Aladdin CMMS", a facility-maintenance product from SG Group International, Dubai (04: "I'm a training specialist at SG Group International"; modules are "the dashboard, we have work orders, we have PPMs, we have asset module"). Across 17,000 words it never mentions BlackRock, portfolios, trades, risk or Snowflake; the one "custodian" is the department that owns a smart TV. Its "hosting our database on Microsoft Azure" is about the CMMS. Nothing from it can support UI/workflow claims about Aladdin; do not cite it. The low-authority files (02, 03, 05) contain nothing that contradicts the page.

## 1. Contradictions

1. Overview: "Institutional clients only; no retail investors." Misleading as written. BlackRock's own framing is that Aladdin "allows them to cover the needs of both institutional and retail investors" (16), and Aladdin Wealth exists so advisers run individual clients' portfolios and now move "from a proposal into the subscription and redemption process in iCapital" (08). The buyers are institutions; retail investors' portfolios are on the platform. Suggested wording: sold only to institutions, including wealth managers whose end-investors are retail.

No other page claim is contradicted by a BlackRock speaker.

## 2. Refinements

1. "~4,000 engineers": the figure is "around 7,000 people, with over 4,000 of those being engineers" in the Aladdin organisation (16). Add the 7,000.
2. "~100 front-end apps": Copilot is "currently embedded across all of those 100 front-end applications" (16); the page says only "across the apps".
3. AI lesson is sourced to "a 2025 BlackRock AI engineering talk (third party)". The primary source is the LangChain Interrupt 2025 talk by Brennan Rosales ("AI engineering lead at BlackRock") and Pedro Vicente Valdez ("Principal AI Engineer") (16). Also add: orchestration "From day one, it's been built using" LangGraph, traced in LangSmith, planner "very reliant on GPT-4 function calling today" (16), and design began "two, two and a half years ago" (16), i.e. late 2022/early 2023.
4. Plugin registry size: "couple of thousands agents and tools that are registered in the plug-in registry" (16). Page gives team count only.
5. Onboarding has a condition the page omits: "for every plugin that comes into a system, we ask them for ground truth" (16); teams supply a configuration layer (app, screen context, portfolios, widgets, chat history) and a solution layer.
6. Data Cloud card says each client "gets its own Snowflake database". Woodhead describes delivery as data sharing into the client's own account and cloud: "sitting in their cloud provider of choice ... through snowflake and through data sharing" (01); "We share data to hundreds of Snowflake accounts" (01). Jeff Miller: ADC replaced "flat files ... large schema definitions, FTP" (17). The page's per-client database is BlackRock's side; the client-facing product is a share.
7. ADC dating: the page cites a 2021 press release; Woodhead says "it was around 2019 we started" and the interviewer puts it at "about five years into that" (01).
8. Studio definition: Woodhead's three pillars are "a set of APIs events" (events as a first-class channel, absent from the page), "The Aladdin data cloud built on top of Snowflake", and "developer tools ... sandboxes, research environments" (01). He never says "Compute", "Aladdin Graph" or "Studio Developer". Add events to the Studio card.
9. Citizen developers "the primary audience for Studio": Woodhead gives the number, "inside of black rock we have 3,000 citizen developers in business engineers", and adds "I think that number has probably peaked" with natural language next (01). The page should carry the number and the caveat.
10. "Copilot ... assistant embedded across the apps": BlackRock states the three value drivers as every user "become an Aladdin expert", personalisation, and "democratize access to all of these insights" (16); Woodhead frames the AI strategy as three-fold: AI in every product, "AI as a platform", and AI "to power the builder" (01). The page's "Why it matters for Studio" paragraph would be stronger quoting the third.

## 3. Confirmations

- Front-to-back single system: Rosato, "end-to-end from risk to investment to trading to post-trade to accounting" (10); Woodhead, Aladdin "has evolved from being an analytics factory to becoming an intelligence factory" (01).
- Origin story: "our clients ... asked could they use the same software ... we started offering Aladdin as a service" (01); "BlackRock is the biggest user of Aladdin" (16).
- Copilot architecture: tool "mapping one-to-one to an existing Aladdin API already out in production" or "spin up a custom agent" (16); "say, 50, 60 Aladdin engineering teams" (16); filtering "which environments ... which user groups ... which Aladdin apps" (16); "more than 40, 50 tools, we probably won't have that good of a performance", leaving "20 to 30 tools and agents" (16); input guardrails for "off topic and toxic content" and PII, output guardrails to "detect hallucinations" (16); "supervisor" pattern (16); evaluation "runs every day. It runs on every PR", "LLMs as a judge", "evaluation-driven development" (16).
- Bitemporal data: clients asked for tools to "ask like bite temporal questions of the history of our investment process" (01), the stated reason for ADC.
- "Environment" as the tenant word: "portfolios in your environment", "our test environment" (09); plug-ins enabled per "environments" (16).
- "Citizen developer" is BlackRock vocabulary: used by Woodhead (01) and Garbien, "the technologists or the citizen developer" (18).
- Data Cloud for joining Aladdin with external data: ESG example, "Mapping that data ... in the context of the investments that you've made is very very hard" (01).

## 4. New facts (priority order)

1. Scale: "hundreds of clients globally across 70 countries", BlackRock "over $11 trillion in AUM", apps used by "thousands of people ... every day" (16).
2. Explore is the main analysis and reporting UI and is absent from the page: "a One-Stop shop for reporting and portfolio analysis" (06), "our new application Explore[r]", launched from the toolbar or the client site at "/app/explore" (09). It is web-based because legacy apps are Java: "save time on a lot of Java issues that we have been facing with other applications" (09).
3. Explore concepts: workspaces (saveable, shareable by URL), widgets (risk and exposure, bar, line), reports/tabs, report groups, "quick column set" to switch analytical VaR to "stress P&L columns", what-if modelling with "through time analysis" versus "point in time analysis", "compare to", "save as portfolio" (09). Risk summary "pulling straight from PRT" with risk model, weighting scheme, horizon and VaR confidence (84% default, 95% option) (09).
4. Performance methodology: "Returns on Aladdin are calculated at the security level and aggregated to the sector portfolio and Enterprise levels daily" (06); three return types (P&L, return, contribution); P&L split into price, income, paydown, FX, trade; risk-based attribution factors (duration, curve, convexity, risk-free, roll-down, FX, FX carry) then "Brinson 2 or three Factor attribution" with sector weighting by market value, spread duration or DTS; ex-post stats; export to Excel/PDF and "batch report" (06).
5. Risk model: "a 3,000 risk factor model" dating from "BlackRock's founding", reused in Aladdin Wealth with stress testing and cash-flow analytics (08).
6. ADC operations: "hundreds of Snowflake accounts ... hundreds of vendors, tens of thousands of pipelines"; "fleet management" is the biggest challenge; moving "from batch oriented pipelines to more real time pipelines" with dynamic tables; vector storage for private-markets data (01).
7. Usage shift: "more of our users are consuming data programmatically through R through Python ... than they are bringing it down to Excel", measured by queries and users (01).
8. Copilot example query "what is my exposure to aerospace in Portfolio 1", answered "5%"; context includes app, on-screen portfolios, assets, widgets and "predefined global settings" (16). BlackRock built its own slim agent protocol and is "actively evaluating" LangChain's agent protocol and A2A (16).
9. Operations strategy "five pillars": Aladdin workflow, real-time data, interoperability, intelligent workflow ("We call it AI or Aladdin intelligence"), finality; Symphony-Aladdin integration live, "five more queued up", chatbots moving trade-status data to brokers and custodians (10).
10. Data quality vocabulary: KPIs are "straight-through processing rate" and "first time right rate on analytics", driven by "shift left QC" (01); data governance (stewards, "data product owners") was "a muscle that we didn't have organizationally" (01).
11. People: Dave Woodhead, MD, head of engineering, Aladdin Studio (01); Jeff Miller, MD, "Global Head of Data Platform and Product Engineering", chief architect (17); Tim Garbien, MD Aladdin, sells "business and technology transformation" including outsourced operations (18).
12. Aladdin Wealth: "public assets and private assets side by side since the beginning" but "historically stopped at ... proposal generation"; iCapital integration targeted "second half of the year" (08). Preqin collects from "4 million news articles a day" with "hundreds of researchers" (07).

## 5. Terminology

- "The language of the portfolio": BlackRock's name for the unified symbology/data model the page calls "one system" (01).
- "Analytics factory" / "intelligence factory"; "green package" = the daily portfolio risk report, "printed on green paper" (01).
- "Whole portfolio" (view/solution/narrative) is the public-plus-private framing (01, 16, 08); the page's products tab does not use it.
- "Business engineer(ing)" is used alongside "citizen developer" (01).
- "Plug-in" is the umbrella; "tool" means an existing production API; "custom agent" is the other kind (16). Page uses "tools" for both.
- "Data product", "data product owner", "data joy" (01); "governance-first", "federated data environment" (17).
- "Aladdin intelligence" as Rosato's expansion of AI (10).
- "Client site", "Aladdin Client Services", "Aladdin classroom" (training series), "workspace", "widget", "what-if" (09, 06).
- Not heard in any transcript: Aladdin Graph, Studio Developer, Compute, Risk Radar, DECO, CIDS, ADL, BQL. The page should say these are spec-derived names.
