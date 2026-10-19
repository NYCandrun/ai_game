<!-- agent ab5048ecf4735a1b7; started 2026-10-19T13:42:07.865Z; finished 2026-10-19T13:45:45.612Z -->

Fact-check of claims.md against transcripts 14, 15, 21–31, 33–35 and transcripts2 040–042. File names shortened to their numeric prefix; all quotes ≤20 words. Note: file 14 (labelled "eFront Copilot page") actually contains scraped text of a Never Done episode page and FT headline, not Copilot product text.

## 1. CONTRADICTIONS

1. **"eFront and Preqin … Combined as eFront Insight in February 2026"** (PRODUCTS). Misleading: eFront Insight is a long-standing eFront LP/GP data-and-benchmarking product, not a 2026 combination. 34_: "Thanks to eFront Insight, limited partners now have access to everything they need… through one single point of access", with "the growing eFront Insight database" and "eFront Pevara" benchmarks. 15_ (Copilot page): "eFront Copilot, now available within eFront Insight." The Feb 2026 event itself is not in these sources; the page should not present Insight as a new name.

2. **"Institutional clients only; no retail investors"** is stated more narrowly than BlackRock's own wording, and the client list omits two segments BlackRock markets to. 15_ (disclaimer): "designed for institutional, wholesale, qualified, and professional investor/client use only and is not intended for end investor use." Nav on every page: "Asset managers, Asset servicers, Banks & brokers, Corporates, Insurers, Pension funds, Private markets, Wealth managers." Page omits asset servicers and private-markets GPs/LPs.

3. **Glossary "ABOR / OBOR: … the other (investment) book of record."** BlackRock speakers and pages say IBOR, never OBOR. 15_ (Fivetran): "Investment Books of Record (IBOR), Accounting Books of Record (ABOR) holdings". 040_: "from a investment book of record perspective". If a spec field literally says OBOR, keep it but state the spoken term is IBOR.

4. **Data Cloud described as one-way ("preloaded … to join with their own and third-party data")**. The official description is a two-way "data network". 15_ (Fivetran, Woodhead): "enabling clients to bring their own data into ADC, and to distribute Aladdin data to their own data ecosystems."

No source contradicts the Azure/AWS, lifecycle, API or Copilot-architecture claims; most are simply outside this evidence set (see §3).

## 2. REFINEMENTS

- **Copilot "launched 2023 on Azure OpenAI"**: no source in this set dates the launch. What is stated: 15_ (Copilot page): "Introducing Aladdin Copilot, now available to all Aladdin clients." 15_ (Ignite, Dec 2024): "BlackRock technology clients are already using this capability today." 27_ (2024): "We're still in very early innings." Say "announced 2023, generally available to all clients by 2026" or drop the year.
- **Copilot guardrails** are attributed on the page to a third-party talk; the official page states them. 15_: "Will not give investment advice or respond to questions outside Aladdin platform boundaries"; "content filtering and parameters to limit risk of hallucination, misinformation or inappropriate outputs"; "permission-dependent access to insights"; "configurable experiences to make the Aladdin platform your own." 27_ confirms both input and output checks: "the prompt that the user is giving isn't toxic… the copilot doesn't respond back with something that it shouldn't."
- **Aladdin Wealth "AI commentary tool added in October 2025"**: exact name, date and first client. 15_ (press release): "NEW YORK – 2 October 2025", feature is "Auto Commentary"; "Morgan Stanley's Portfolio Risk Platform… will be the first to implement"; inputs are "robust data and risk analytics, an individual firm's CIO market outlook, and… the client's portfolio holdings and investment preferences." Executive: Ted Stratigos, "Global Head of Aladdin Wealth Tech". Wealth audience is "wealth managers and private banks".
- **Azure migration**: page says "client-by-client … Microsoft Treasury first" (not in this set). What this set gives: 15_ (Ignite): "Five years ago, we began working on a strategy to move them into the cloud on Microsoft Azure" (i.e. ~2019); "Today, all BlackRock's technology platform clients and services are hosted in the Azure cloud"; "New rollouts now take weeks instead of quarters"; "data encrypted at rest and in transit"; better performance "during… index rebalances". 28_ (Fradin): migration "was always meant to be the springboard… essentially a perpetual cloud journey."
- **ADC product category and pipeline**: 15_ (Fivetran): ADC is "a next-generation data-as-a-service solution enabled by Fivetran and Snowflake"; "Fivetran allows us to take data from a single source and move that with low latency into a Snowflake landing zone, where we transform it using our enterprise data platform"; "dynamic tables for building Snowpark apps"; pipelines built "in just a few months". HVR is not mentioned anywhere in this set. Owner: Dave Woodhead, "Head of Aladdin Studio Engineering".
- **Product family** omits names BlackRock uses as solutions: 15_ nav: "Accounting, Aladdin Studio, Aladdin Data Cloud, Whole Portfolio, Risk Management, Sustainability, Climate Risk, Aladdin Copilot, Private Markets Data"; platforms "Aladdin, Aladdin Wealth, eFront, Preqin". "Aladdin Enterprise" does not appear in any source; "Aladdin Risk" does (15_: "Aladdin Studio for Aladdin Risk").
- **"citizen developer"** is confirmed but BlackRock frames it as a client trend, not only a Studio audience. 25_: "this new emerging class of citizen developers at an organization"; 26_: "they want programmatic access to the data to build various kinds of applications… last five to seven years."
- **Insurer segment** deserves a figure: 040_: "roughly about 500 billion of insurance asset management on the system and 6 trillion of insurance assets that are actually processed through Aladdin."

## 3. CONFIRMATIONS

- Built for BlackRock, then sold: 15_ (Fivetran): "backbone of BlackRock's technology and investment operations since the company's early days, while subsequently serving institutional investors"; 33_: "we're the user of the same software"; 28_: "Aladdin was created, you know, 30 years ago."
- Azure today, previously own data centres: 15_ (Ignite): "pouring resources into maintaining its data center operations"; "all… clients and services are hosted in the Azure cloud."
- Front-to-back single record, accounting sign-off: 33_: "from that first order through the trade, through all the operation protocols into accounting without lifting up the pencil"; "sign your name against as the executives of the firm."
- Risk Governance rules/evaluations/exceptions/workflows exposed programmatically via Studio: 15_ (Studio for Risk): "Support programmatic rules, evaluations, exceptions, escalation, and downstream reporting workflows."
- Copilot as a layer across apps: 27_: "We see the Aladdin copilot as this connective tissue across Aladdin"; 15_ (Copilot page) uses the same phrase.
- Copilot built with Azure OpenAI/Microsoft engineering: 28_: "deep partnership with OpenAI… Azure OpenAI integration. We are co-located"; "close engineering partnership between the BlackRock and the Microsoft team."
- API-first/extensibility language: 15_ (Whole Portfolio): "open, API-first platform… flexibility, extensibility, and interoperability."
- Climate physical/transition: 040_: "impact of things like transition and physical risk, and how does catastrophe impact my portfolio."
- Not verifiable from this set: 54/301 API counts, ~100 apps, ~4,000 engineers, Q2 2026 revenue, AWS Dec 2025, Copilot tool registry/20–30 tool filter, Risk Radar/DECO/CIDS/BQL, provider users, Preqin March 2025.

## 4. NEW FACTS (prioritised)

1. **Aladdin Studio for Aladdin Risk** is a named offering: Studio "extends Aladdin Risk beyond the user interface" so firms "automate processes, connect risk information to downstream workflows, and build a more scalable risk operating model" (15_). Four pillars: run analytics programmatically; automate portfolio oversight workflows; build tailored risk solutions; strengthen data governance.
2. Studio has a governance console: "Its centralized experience supports the building, configuration, and governance of Studio workflows, including access management and usage monitoring" (15_).
3. ADC "data network": clients bring their own data into ADC and distribute Aladdin data outward; Fivetran moves data "with low latency into a Snowflake landing zone", transformed by an "enterprise data platform"; answers "in near real-time" (15_).
4. ADC's Fivetran adoption addressed "disaster recovery, data recoverability, and consolidation of previously siloed data sets" (15_).
5. Copilot is GA to all clients, with explicit refusals (no investment advice, no out-of-platform questions) and content filtering; eFront Copilot lives inside eFront Insight (15_).
6. Microsoft's framing: Aladdin moved from "user and application programming interfaces" to "natural language interfaces"; sample prompt "What is my exposure to companies building AI processors?" (15_).
7. Azure timeline: strategy began ~2019, all clients on Azure by Dec 2024; rollouts "weeks instead of quarters"; BlackRock started an "AI Lab in 2018"; uses Microsoft 365 Copilot, GitHub Copilot, Copilot Studio, Dynamics 365 (15_).
8. Roadmap method: "start at the root cause as opposed to over-solutioning"; "formulate the roadmap in a way that's informed by our user community"; heavy use of "telemetry and adoption metrics" plus client conversations; willingness to "inspect, adapt and change" mid-build; "security is definitely number one" (23_).
9. Kunal Khara (Global Head of Aladdin Product): clients drive "identifying needs and gaps to solutioning to prioritizing strategic objectives, to ultimately deploying"; build "in a way that can benefit the entire Aladdin community"; innovation must never degrade "core business", which earns the "license to go innovate" (30_).
10. UX direction: shift from "command-based interaction" to "intent-based interaction"; "contextual personalization which we applied in all of our apps"; "deep link technology… bypassing several unnecessary clicks"; "Interface adapts to the user" (31_).
11. AI data-isolation principle: "separate instances and separate platforms of whatever models we're developing"; external tools risk "data leakage… being used to retrain models"; persona-aware news surfacing by "sector… or any region that they're covering" (042_).
12. Whole Portfolio numbers: "6 years delivering Whole Portfolio solutions—with 20+ years… for private markets"; "50,000 unique private markets companies maintained and 2k+ private markets risk factors monitored daily"; "unified IBOR for public and private assets"; "models private market cashflows natively"; supports a "Total Portfolio Approach" (15_).
13. Accounting positioning: users are "CFOs… controllers… heads of performance"; team sees itself as "data managers more than anything else" (33_).
14. Analytics stance: risk models "translate data into actionable information"; research to "classify the noise into the noise that is just noise"; next years' job is "to integrate it all, to bring it to scale, to have it be clean" (22_).
15. Wealth Auto Commentary synthesises "hundreds of data points"; Morgan Stanley's platform "leverages a combination of BlackRock's Aladdin risk analytics and Morgan Stanley data" (15_) — a Risk-analytics-only client pattern.

## 5. TERMINOLOGY

- IBOR, not OBOR (040_, 15_).
- "Portfolio oversight" is BlackRock's term for what the page calls Oversight/Risk Governance workflows (15_: "scalable portfolio oversight"; "exception monitoring and governance workflows").
- "Connective tissue" = Copilot's role (27_, 15_).
- "Data-as-a-service" and "data network" = ADC (15_); page says "per-client Snowflake database".
- "Whole Portfolio" and "Total Portfolio Approach" = cross-public/private product (15_); absent from page.
- "Aladdin Risk" confirmed; "Aladdin Enterprise" unattested; "Risk Management"/"Risk" in nav (15_).
- "Private Markets Data" = Preqin solution name; "Pre-Investment IQ" (15_).
- "Citizen developers", "controlled customization at scale" (25_); "micro applications", "programmatic access", "RQA function" (26_).
- "Perpetual cloud journey"; "re-underwrite the stack"; clients are "technologists" (28_).
- "Living organisms" for Aladdin/eFront; "license to innovate" (30_).
- "Command-based" vs "intent-based interaction"; "contextual personalization"; "deep link" (31_).
- "Data managers" (33_); "data prep" 70% of data-scientist time (26_).
- Org titles: "Aladdin Studio Engineering" (Woodhead), "Aladdin Engineering" (Braunstein), "Aladdin Product" (Khara), "Solutions Engineering" (Khaneja), "Aladdin Wealth Tech" (Stratigos), "Aladdin Client Business" (Chouman), "Aladdin Relationship Management" (disclaimer).
- "Ecosystem" and "partner" rather than vendor/client; "Apple phone" with "open architecture" analogy (21_).
- "eFront Pevara" benchmarks and "eFront Insight database" (34_, Whisper spells "Pavara").
