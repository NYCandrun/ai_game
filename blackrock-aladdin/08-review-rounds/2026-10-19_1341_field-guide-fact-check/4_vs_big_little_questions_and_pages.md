<!-- agent afef8a543de26abcd; started 2026-10-19T13:42:07.836Z; finished 2026-10-19T13:46:19.237Z -->

Scope: read claims.md in full and transcripts 043–063 (Uncharted 043–044, webinars 045–056, client stories 057–059, site videos 060–063). 057 (Helvetia) and 063 are mostly untranscribable; 054 (ILPA/FAIR) and 055 (Africa) are market content with almost no platform detail. All files are in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/transcripts2/.

1. CONTRADICTIONS
- "Aladdin Copilot ... launched 2023" (PRODUCTS). Speakers describe eFront Copilot as the first Copilot, reaching select clients in 2024, with Aladdin's following. 061_Best_Overall_Technology_Provider (early 2024, Kunal Kapoor): "on the E-front side in particular, we have a co-pilot that is out in the market very soon". 046_Accelerating_Innovation: "recently introduced the Aladdin Co-Pilot ecosystem with a select number of clients. The first example of that was e-front co-pilot". 047_Aladdin_Climate (2024 demo): "Microsoft co-pilot at the top right. At the moment, this is something that we are rolling out". A 2023 launch "across the apps" overstates.
- "Aladdin Enterprise ... across public markets" and privates = eFront (PRODUCTS, Sources). The core IBOR is positioned as public plus private. 056_Unifying (Paul, private markets product): "introduced over 10 different transaction types to Aladdin across commitments, fundings, pay downs, picks"; "private credit IBOR". 052_Navigating_private_markets: "using Aladdin's SWIFT capabilities to send cash flow out for transactions happening within the private market."
- "Combined as eFront Insight in February 2026". eFront Insight is a long-standing LP product, not a 2026 creation. 053_PRIVATE_MARKET_SUSTAINABILITY (2024): "all of this incorporated in one platform, e-front insight". 044_Uncharted_Ep2 (mid-2024): "Insight Research Fund Universe grew from 8,900 to 9,300 funds". 056 (Sept 2025): "over 15,000 fund investments within e front insight directly". If Feb 2026 was a rebrand, say Preqin was folded into an existing product.
- "Aladdin is the one system all six roles share" (custodian included). 059_JPM: "Our teams can stay in our workstation that we have built and clients can stay within Aladdin." The custodian connects through the Aladdin Provider network; it is not an Aladdin user.

2. REFINEMENTS
- Data Cloud is near-real-time, not instant. 050_Data_as_strategic_asset (Aladdin Global Head of Data): "one single source within 15 minutes of latency". Same speaker: "every single transaction that happens should be available and accessible to you via an event, via an API".
- Citizen developer. 050: "some people like to call them as embedded engineers now because they actually have a PhD degree"; "at BlackRock, we have 3,000 people who qualify in this bracket"; governance = code "into GitHub in the same governance level" plus "survivorship" after the author leaves.
- Climate (PRODUCTS, analytics domain). 047: coverage "around 3 million securities for about 9,000 ultimate holding issuers"; scenarios from NGFS and IPCC; "not cat models ... really asset evaluation models" (DCF on climate-adjusted cash flows); historical emissions via Clarity AI, projections proprietary; team "around 100 people, 60% ... modelers". 053: transition = two NGFS scenarios (orderly, disorderly); physical = six (three NGFS, three IPCC SSPs); outlooks today–2050 and 2050–2090; private models cover PE and infrastructure, real estate later, via "public market equivalent" proxy cohorts.
- eFront 2019 confirmed (045, 052, 056). Ignore 052 Darren's "acquisition of EFRON in 2017" (ops speaker, self-contradicting).
- Preqin scale. 062: "1600 colleagues from prequin"; 052: "500 researchers", "4 million articles a day", "400,000 sponsored back portfolio companies", "65 regulatory registries"; 050: data began with Freedom of Information requests to pensions.
- Whole portfolio framing. 056: "6040 has really morphed into more of a 50 30 20"; 052: "50% of our private market sales now are actually whole portfolio solutions".
- Studio. 061: "the Aladdin studio estate ... this year be a major unlock" for data "on a programmatic basis at machine scale, over and above ... front end applications".
- Copilot is described as a Microsoft partnership ("Microsoft co-pilot", 047), with principles "human in the loop", "walled garden", RAG (046).

3. CONFIRMATIONS
- Built for BlackRock, sold on; user-provider: 061 "we eat our own cooking"; 048, 051, 056 "user provider model".
- Single IBOR across public and private: 052 "singular investment book, a record across your public, private and maybe even your crypto assets"; 051 "the iBOR, the A-BOR to really be the source of truth".
- eFront = post-investment, Preqin = pre-investment: 052, 056.
- Cloud-hosted, configurable, API/open-architecture demand: 061 "very scalable cloud-based infrastructure", "big focus on open architecture and access to APIs"; 049 "very robust APIs that manage the end to end life cycle of a transaction".
- Snowflake under ADC: 050; 058 Royal London "implementation of Snowflake ... part of the overall programme".
- GenAI drafting compliance rules: 046 "create the relevant code for that new compliance rule".
- Scenario/stress analytics in Aladdin Risk: 048. Clients include insurers, pensions, wealth: 061, 050.

4. NEW FACTS (priority order)
1. Explore is the flagship portfolio analysis and reporting app (048: "flagship tools ... called Explore"). Demos (047, 048, 053) show group→portfolio→sector→asset drill-down, heat maps, time series, factor and correlation views, customizable "pre-canned widgets", what-if reallocation, and a stress panel with "2500 plus factors" and selectable risk model. 047 also shows an issuer-level "research tool" (Iberdrola). The page glossary omits Explore.
2. Market Driven Scenarios (MDS), owned by RQA, follow rationale→catalysts→calibration→"policy variable shocks"→plausibility check→implied shocks via covariance→whole-portfolio P&L; BlackRock ships the scenario and clients customize it (048).
3. ADC is called a "data integration hub" (~15 min latency); analytics are exposed via API and stored as time series in ADC; "investment automation" (rebalancing used by BlackRock) is being opened as a platform where clients "overlay your own configuration and code" (050).
4. Build-vs-buy data (049, Alisha Sewdass, Aladdin Solutions Engineering Americas): poll 37% mostly vendor, 30% hybrid, 18% re-evaluating, 15% in-house; "60 to 70% of tech costs" is maintenance; top pressure "AI and data demands at 42%"; want to stop maintaining: "compliance reporting ... 53%", position/cash 22%, trade lifecycle 17%, risk infra 9%; transformation "12 to 18 months", ROI ~6 months after; the CTO is now in the decision; RFPs ask for the API suite, Snowflake/Databricks connectors and latency ("every 15 seconds or ... every four hours"); framing "system of record" plus "system of work".
5. Private credit rebuilt natively in Aladdin (056): facility- and contract-level data model from "500 page credit agreements", 10+ transaction types, ex-ante cash-flow tables, PD/LGD with restructuring instead of default, HPS input, delivered "in less than a year post acquisition", extensible to infrastructure/real assets via a collateral lens (GIP).
6. Preqin inside Aladdin (056): indices "available today in Aladdin explore and our Aladdin data cloud"; roadmap into SAA tools, Aladdin Wealth, allocator hub into eFront Insight; entity mastering / "common identifier" is the stated unlock (052).
7. BlackRock ops metrics (052): PE trade cost "$120 in 2017. Today, we sit at below $20"; 65% of team in Mumbai; 300-person ops team spends ~30% reconciling with administrators; SVB exposure found in one system. 056: SWIFT capital calls "24 hours now down to one hour".
8. Aladdin Provider network (059): "nine of the largest global asset servicers"; JPM since 2016; "gold copy messaging"; integrated reconciliation-break workflow rolled out "through simple configuration ... no customization, no coding".
9. Insight Sustainability (053): RepRisk, GP-reported ESG (campaign "1,700 GPs ... just over 6,000 funds"), Clarity AI estimates for nine metrics, Aladdin Climate; joint "whole portfolio view" demoed in Explore for a 45bn pension.
10. Royal London implementation (058): on time, "under budget", three parties including HSBC; a "sentiment tracker" for front-office change; single OMS; award-winning.
11. 061: 2023 BST awards for Best IBOR, Best Portfolio Analysis Tool, Best Overall Provider; Kunal Kapoor "Global Head of Aladdin Product"; 2024 themes: GenAI on a data foundation, cloud elasticity, network ecosystem, whole portfolio, Studio.
12. AI use cases to be exposed to clients (050): "creation of security, coding binary compliance rules ... client reporting and reg reporting"; agents framed as "digital employees". 046 survey: 88% see GenAI edge, 8% implementing.
13. 056: economic scenario simulator projects "as far as 30 years" for SAA; Liberation Day tariff exposure answered "in the matter of minutes" with look-through.
14. ACF 2026 positioning (060): "investment intelligence platform powered by AI-native intelligence", "built with Aladdin, built on Aladdin".
15. "Change alpha" / "operational alpha" is a named Aladdin message (046, 051).

5. TERMINOLOGY
- "Provider": page = BlackRock employee in a client tenant; speakers use "user provider model" (BlackRock as user and vendor) and "Aladdin Provider" (asset-servicer network).
- "Gold copy": page = reference client for recon; 059 = "gold copy messaging" to custodians.
- "Whole portfolio" / "whole portfolio solution/view" is the product name for public+private; page never uses it.
- Speakers say "IBOR" and "ABOR" (051); page's "OBOR" is unused.
- Internal names: Explore, research tool, eFront Insight, Insight Research Index, FAIR (fee validation, 054), MDS, RQA, policy variables, "common language for portfolios", "Studio estate", "embedded engineers", "system of work", "Microsoft Copilot" (not "Azure OpenAI"), "Risk Governance" used by RQA as a process (048), "Aladdin Provider", "gold copy messaging".
