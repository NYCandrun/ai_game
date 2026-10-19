# Fact-check: "Aladdin and Aladdin Studio: Briefing and Interview Guide" (76 pp) and "Aladdin Studio: What It Does (V7)" (22 pp)

Checked against the evidence gathered in this session: 54 public Aladdin API specs and the SDK README; BlackRock product pages, press releases and job postings; the Fivetran and Microsoft write-ups; and about 120 transcripts (LangChain and Snowflake talks, 42 Never Done and Client Stories podcast episodes, 12 webinar replays, 15 Big Little Questions episodes, client stories and eFront videos). Transcript references are to files in `yt/transcripts/` (two-digit numbers) and `yt/transcripts2/` (three-digit numbers).

Three verdicts are used. **Contradicted**: a source says something different. **Unsupported**: nothing in this corpus speaks to it, so it is neither confirmed nor refuted; the risk is that an interviewer knows the figure. **Confirmed**: a source supports it.

An important limit: the corpus holds almost no pricing, contract, 10-K, tender or trade-press material. Everything in the briefing's cost, competitor and named-deal sections rests on sources outside this corpus and could not be checked either way.

---

## Part A. Briefing and Interview Guide

### A1. Contradicted or materially off (fix before the interview)

| # | Where | Document says | Sources say |
|---|---|---|---|
| 1 | §7 Studio in depth | 11 plugin packages contain **58** API specifications, 301 operations | **54** specs, 301 operations. digest.txt and the unpacked packages hold exactly 54 swagger files. An interviewer with the packages can count. |
| 2 | Exhibit 24 | "the Graph API for portfolio data and risk, an Investment Research API" | Aladdin Graph is the name of the whole API layer: every spec id starts `agraph.`, and the specs say "agreed naming with Aladdin Graph team". There is no single Investment Research API; it is a domain of five alpha APIs (ResearchNote, Engagement, AnalystCoverage, Watchlist, Criterion). Exhibit 28 already treats Graph as the layer, so the document is inconsistent with itself. |
| 3 | §7, Exhibit 6 | Sudhir Nair "has said more than 2,000 citizen developers actively use Studio", about 2024, including BlackRock staff | Two BlackRock statements both say **3,000**, both BlackRock-internal headcount, neither about Studio clients. Woodhead (01): "inside of BlackRock we have 3,000 citizen developers and business engineers"; Goel (050): "we have 3,000 people who qualify in this bracket". The Nair podcast (033) has no citizen-developer figure. Woodhead adds the number "has probably peaked". |
| 4 | Exhibit 26 | "Citizen developer: first seen May 2024, SDK launch blog" | Used by BlackRock speakers in Nov 2023 (010: "citizen developers are what are driving these organizations today") and Mar 2024 (001), and in the SDK README. |
| 5 | Exhibit 33 | SLC Management "Confirmed (featured)" as a Data Cloud reference | Both SLC episodes (025, 031) contain no mention of Data Cloud, Snowflake, Studio or APIs. Placement only. |
| 6 | §7, §8, Exhibit 6 | "BlackRock has never named a Studio reference client"; client quotes "talk about adopting Aladdin in general, not about what they built" | Royal London's CEO in BlackRock's own client video (058): "the implementation of Snowflake that we did as part of the overall programme has been really successful". He does not say "Data Cloud", so the claim survives on a technicality; soften to "no client named as building on Studio APIs or the SDK". |
| 7 | §3, §5, Exhibits 15/16 | Royal London: COO quote; "largest and most complicated programme the firm had ever run"; "over two years"; "two order systems, reportedly thinkFolio and Murex" | The published video (058) has the CEO, Hans Georgeson, saying it came in "largely on time, if not ahead of plan, and we came in under budget", replacing "multiple order management systems" with one, with HSBC as the third partner and Snowflake in scope. No duration, no "largest ever", no system names. |
| 8 | §5, Exhibit 16 | BNP Paribas AM "retired more than 60 applications when it moved to Aladdin", labelled Reported | Confirmed in BlackRock's own transcript (008), but the 60 belong to the whole 2016–2020 programme "with BlackRock Aladdin in the front to back chain, with Salesforce in the CRM, and transversally DataHub". Relabel Confirmed, attribute to the programme. |
| 9 | Exhibit 21 | WatersTechnology 2023 awards, labelled Reported | BlackRock's own winner interview (061) confirms three awards: Best IBOR, Best Portfolio Analysis Tool, Best Overall Technology Provider. Relabel Confirmed; the document omits the third. |
| 10 | Exhibit 38 | "Pia Schäfer, Head of Value Engineering for Aladdin, Undated" | 011 (July 2025): "Pia Schaefer, Global Head of Value Engineering for the Aladdin Client Business". |
| 11 | Exhibit 38 | "Ted Stratigos, Global Head of Aladdin Wealth" | Press release, 2 Oct 2025: "Global Head of Aladdin Wealth Tech". |
| 12 | §11 | Studio's "three stated benefits: create and automate, make Aladdin your own, and align inside and outside the firm" | Not BlackRock wording anywhere in the corpus. The Studio page lists "Create & automate", "Make Aladdin your own", "Align internally & externally" as benefit headings (verified earlier from the page), so the substance is right but the phrase "make Aladdin your own" is otherwise only on the Copilot page. Present as the page's headings, not a quote. |
| 13 | Exhibit 40, §16 | "68% of 303 firms favor core platforms plus their own builds (September 2026)" | Looks like two facts fused: a site banner announcing an "AI Adoption Report 2026 based on a global survey of 303 investment firms", and a different webinar (052) where "68% of investors ... believe that having a singular view across public and private holdings is crucial". The combined statistic is not in the corpus. Verify before using it in the close. |
| 14 | §7 | Dave Woodhead quote "Snowflake is central to our strategy of delivering a whole-portfolio data solution", "about July 2026" | Not in the corpus. His podcast (01) says "we are very much on a journey to what we call a whole portfolio view" and "we love the partnership with Snowflake ... it's a part of a platform". His titles: "managing director and head of engineering for Aladdin Studio" (01) and "Head of Aladdin Studio Engineering" (Fivetran, Aug 2024). |
| 15 | Exhibit 2 | "Aladdin Risk uses more than 5,000 risk factors" | Corpus has "2k+ private markets risk factors monitored daily" (Whole Portfolio page), "a 3,000 risk factor model" (08, Aladdin Wealth), "2500 plus factors" in an Explore stress demo (048), and the Fivetran blog's "monitors over 5,000 risk factors daily". The 5,000 is defensible only with the Fivetran citation; say "thousands" unless citing it. |

### A2. Attributed quotes, titles and dates the corpus does not support (drop or re-source)

- §12: Ted Stratigos "in March 2026" on Auto Commentary guardrails built with risk, legal, information security and model governance, and "real impact came from adoption". The only Stratigos source is the Oct 2025 press release, which says none of this.
- §15: Cameron Skinner on "how data is defined before rolling out AI agents". Title confirmed (016: "Global Head of Solutions Engineering for BlackRock Aladdin"); the remark is not in any of his five transcripts. His nearest line: "There are guardrails that we can put in place ... We can't replace the judgment of the trader."
- §15: Diwakar Goel, "October 2026", context "must be codified". Title roughly confirmed (050: "Global Head of Data"); quote not in corpus.
- §16: "Kunal Khara, May 2026: private credit is becoming a core part of portfolios, but its data remains fragmented". Khara appears only in 2023–2024 items and never says this.
- Exhibit 40: Larry Fink's 2026 letter and "the language of portfolios". The phrase is Woodhead's (01: "a single symbology, a single language, the language of the portfolio") and the ACF 2026 opener's "a common language for portfolios". Cite those.
- §7: Syril Smith Garson quote on "common services and capabilities that underpin all of these different copilot experiences", "November 2024". Not in either Humans-in-the-loop transcript. Her title "Head of Product for AI" is confirmed (019).
- §7: Bernadette Rivosecchi "database ready on day one". Not in corpus. Better-sourced substitute: Jeff Miller, MD, Global Head of Data Platform and Product Engineering and Chief Architect (17): ADC replaced "flat files ... FTP".
- Exhibit 38: Sudhir Nair's "Senior Managing Director" (corpus: "Global Head of Aladdin"); Drew Ellis, Vedant Naik, Eli Kalish titles and the SDK-blog co-authorship; Priyanka Singh and Vijay Kasi (from your own interviews, not checkable).
- §8: "Rosales and Valdez, AI engineering leads". Transcript (16): Rosales "AI engineering lead", Valdez "Principal AI Engineer".
- §8: "Aladdin Client Forum, held regionally every two years". Corpus shows ACF 2026 in New York and an APAC forum recap for 2025; cadence not established.
- §8: "podcasts feature executives rather than developers". Engineer-led public content exists: Snowflake Summit 2024 talk, LangChain Interrupt 2025 talk, Principles of Design engineering podcast (027) with Afwa Kandawire and Sue Zheng.
- §7: "There's no copilot without plug-ins", labelled "Reported, secondhand". It is verbatim in the corpus (023), spoken by Microsoft's Adrian Crockett on BlackRock's podcast. Upgrade and attribute.

### A3. Unverifiable from this corpus, and high risk if wrong

These are outside the evidence set. Plausible is not the same as confirmed; the ones most likely to be challenged are listed first.

- All of §4 pricing: the Texas PSF fee schedule ($1.575m base, 0.85 bp, $20k per user, $5k per portfolio, $600 per derivative line, $160k per month implementation); Exhibit 11 price points (Nest, LACERA, PBGC, CalPERS with two conflicting figures, PPF, UBS, JPMorgan, GPIF, Envestnet); "JPMorgan payments rose almost sixfold"; "$1.3 billion fixed minimum fees" and "two thirds"; Exhibit 13 scoring weights and the "groupthink" and "unlike MSCI" quotes; the "0.0004% to 0.0015% of assets" and "$20m per retention point" estimates (fine if stated as your estimates).
- §5 and §6 named decisions and figures: Janus Henderson $14.9m write-down; Corebridge; Aegon to Citi; NPS; MAPFRE; Border to Coast; Santander; New Mexico SIC; Amundi/Pioneer; the 25 dated decisions in Exhibit 19; Deutsche Börse and ALTO revenue; "$59tn on Charles River", "28 Alpha clients", "800+ SimCorp clients", "14,000 AIM users", Clearwater take-private; Chartis rankings; Celent and Deloitte figures; the Enfusion S-1 quote; Exhibit 22 AI moves; named hires Iyan Adewuya and Gareth Morris. Several dates sit within a month of today and rest entirely on press releases.
- "Franklin Templeton and STANLIB both cited lower long-run cost". Both appear only as webinar panellists (Franklin on its own Mosaic platform, STANLIB in the Africa webinar) with no cost statement.
- §3 client lists and counts: "over 95% of transactions flow through without manual work"; "more than 150 insurance clients, 200 with Preqin and Colmore"; segment-page counts (400 asset managers, 150 insurers, 180 pensions, 11 category-4 banks); Preqin "210,000 funds / 14,000 with performance / 10,000 in indices"; "IBOR since 1990"; the ALADDIN acronym; TAM $20bn split; Citi for $4.0tn of iShares; OTCX, FlexTrade, Tradeweb, MarketAxess, Trumid; Coinbase as an Aladdin trading venue (the Coinbase podcast, 015, is about a partnership, not Aladdin connectivity); Bank of Israel quote; all of Exhibits 8 and 9 (wins, losses, exits).
- Exhibit 2 dates (Studio 2020, ADC Feb 2021, eFront Copilot 2023, SDK 2024, Climate 2020, Freddie Mac 1998, Bear Stearns $30bn). ADC "launched 2021" and SDK 2.0 first release May 2024 are consistent with verified web facts; the rest are unsourced here.
- Exhibit 28 requisition IDs, pay bands, Forward Deploy Engineer and MCP, Technical Writer removal date; Exhibit 32 SDK repository statistics (stars, forks, commit share, Python 3.13 failure, download counts); Janus Henderson's SDK contribution; Franklin Templeton, Barings, Thrivent, Spyrosoft, Strata, EY as Studio users; "1,100 Aladdin clients" (corpus: "hundreds of clients globally across 70 countries"); "over 200 institutions"; "API calls 17x by 2030"; HACK:BLK producing Aladdin Wealth; Databricks and FactSet comparison numbers.
- Exhibit 40 financials (AUM $15.3tn, 2030 targets, Q2 2026 technology revenue $566m, Martin Small's ACV guidance, HPS and GIP close dates, the 2026 partnership list, DORA and bank-regulatory citations, fund-finance Exhibit 37). Not checkable here; the "Confirmed" labels are the author's.

### A4. Confirmed (safe to use)

- Scale and organisation (16): "hundreds of clients globally across 70 countries"; "around 7,000 people, with over 4,000 of those being engineers"; "around 100 Aladdin front-end applications"; "BlackRock is the biggest user of Aladdin"; 50 to 60 engineering teams.
- Copilot (16, Copilot page): embedded across all 100 front-end apps; tools map one-to-one to existing production APIs; "now available to all Aladdin clients"; "Will not give investment advice"; eFront Copilot "within eFront Insight".
- Studio composition: APIs with read and write, ADC on Snowflake, Python SDK in beta (2.0.0b10), notebooks, Excel add-in, portal behind login; Newman (11): "Aladdin data cloud specifically ... is part of Studio"; Studio for Risk page: governance "including access management and usage monitoring"; Woodhead (01): Studio "exposes everything Aladdin knows how to do as a set of APIs, events".
- Finance and corporate: Q2 2026 technology revenue +13%, ACV +15% ex-Preqin; technology plus private markets above 30% of revenue by 2030; AWS announced Dec 2025, GA H2 2026; Azure hosting with Microsoft Treasury first; Preqin closed March 2025 (033: "about three months ago, we closed our next acquisition"); eFront 2019 (045).
- Azure: Ignite 2024 recap, "Five years ago, we began working on a strategy to move them into the cloud on Microsoft Azure"; "all BlackRock's technology platform clients and services are hosted in the Azure cloud".
- Wealth Auto Commentary: press release 2 Oct 2025, Morgan Stanley first.
- §2 jobs: common data language (061), Market Driven Scenarios (048), Climate physical/transition/temperature alignment (047 and Climate API), compliance rules by API, ABOR APIs, bitemporal as-was fields, CIDS, cash ladder, what-if orders (specs).
- Aladdin Provider: JPMorgan "early adopter ... from 2016"; "nine of the largest global asset servicers" (059).
- Customer groups as BlackRock's site lists them; AustralianSuper, Columbia Threadneedle, Intesa, BNP Paribas AM as named clients (podcasts).
- Job-posting substance: "extensibility layer", "build, adapt, and run custom workflows in a governed, enterprise-ready way", "reduce off-platform development risk", "AI-assisted developer tooling"; Technical Writer postings on streaming APIs, webhooks and AsyncAPI.
- Gating assessment: the SDK needs a host URL and a token "registered via Studio UI" (README), consistent with your "blocked at step four" account.
- Exhibit 36 IBOR/ABOR lifecycle is consistent with the specs (AborLot carries a parallel lot id; bitemporal fields).

### A5. Better-sourced material the corpus offers (use these instead of the unsupported lines)

1. Woodhead's definition of Studio (01): three pillars, APIs and events; ADC on Snowflake; developer tools ("sandboxes, research environments ... automate the investment process"). Scale: "hundreds of Snowflake accounts ... hundreds of vendors, tens of thousands of pipelines". ADC conversation began "around 2019". Programmatic use (Python, R) overtook Excel "several years ago" by queries and users.
2. Goel (050): "every single transaction ... should be available ... via an event, via an API"; ADC is a "data integration hub" with "15 minutes of latency"; citizen-developer code goes "into GitHub in the same governance level" with "survivorship"; agents as "digital employees".
3. Build vs Buy webinar (049): live poll 15% mostly in-house, 18% actively re-evaluating, 30% hybrid, 37% mostly vendor; "60 to 70% of tech costs" is maintenance; AI and data demands top driver at 42%; firms most want to stop maintaining compliance reporting (53%), position and cash (22%), trade lifecycle (17%), risk infrastructure (9%); migrations "12 to 18 months" with ROI about six months after; RFPs ask for "the API suite ... connectors to Snowflake or to Databricks"; closing line, maintaining "functions that are solved or commoditized may not be the best source of generating alpha".
4. Khara (061): "the Aladdin studio estate ... this year be a major, major unlock ... programmatic basis at machine scale", an executive naming Studio as a 2024 focus, which cuts against "Studio is absent from the top-level story". Also "we eat our own cooking at BlackRock".
5. Khara (30): "innovation ... should not ever come at the cost of anything being different or worse off"; "Our clients are the key driver behind how that product also evolves". Fradin (28): "our ability to do that without disrupting customers is kind of our superpower".
6. Braunstein (022): "with power comes responsibility. So, there's a control framework around that"; "we call that program broadly citizen development".
7. Newman (013): "speed to market doesn't necessarily imply better data. You still have to have the data governance."
8. Garson (12): "getting to trust is going to be predominantly about transparency ... human in the loop on the vast majority of operations". Copilot talk (16): "build an evaluation pipeline and make sure that we are never going to give investment advice".
9. Insurers (040): "roughly about 500 billion of insurance asset management on the system and 6 trillion of insurance assets that are actually processed through Aladdin".
10. Preqin inside Aladdin (056, Sept 2025): "Preqin indices are also available today in Aladdin Explore and our Aladdin data cloud", with Wealth and eFront Insight extensions still planned.
11. Pemmaraju, Head of AI Product and Engineering (028, July 2026): "the data model itself is structured for agentic use cases"; a more current AI lead than the 2024 Garson material.
12. Somasundaram, Global Head of Aladdin Partnerships and Trading Product Marketing (017): "a burgeoning community of individuals saying 'I need that in the form of an API'", a product-marketing peer's demand signal.
13. Named clients missing from Exhibit 8, all from BlackRock-published material: Intesa Sanpaolo, SLC Management, Aviva Investors, TCW, UPP, Ingka Investments, Helvetia, Northstar, plus eFront users APG, Allianz Capital Partners, Velliv, Mizuho, Bouwinvest, Meridiam, BBH, Alter Domus.
14. Spec facts to add to §7: 24 alpha / 6 beta / 23 stable / 1 sunset; application-key header plus OAuth scopes per resource; 35 long-running operations; the linter comment "will break all citizen developers code" as evidence that backward compatibility is enforced in review; every public spec tagged Access.Internal; ADX (Aladdin Data eXchange) as a listed Studio resource missing from Exhibit 24's "eight pieces".

---

## Part B. "Aladdin Studio: What It Does (V7)"

### B1. Verdict

Numerically solid. Every per-package count, operation tally, batch and filter count, long-running-operation count and linter-note count in Exhibits 8 and 11 was recomputed from the swagger files and matched exactly. All quoted spec and README phrases were found verbatim. Stability labels (24/6/23/1), "Risk Tasks is sunset", "only two for trading", "no operation carries a deprecated flag", "11 of 12 packages use :filter" all check out.

### B2. Contradicted

- p.3: "BlackRock shows little of Studio in public" and "Reading those files is the closest an outsider can get to seeing what Studio does." The corpus has a Studio product page, a Studio for Aladdin Risk page (with a "centralized experience ... governance of Studio workflows, including access management and usage monitoring"), the APIs page describing the portal's catalog, Data Dictionary, notebooks and samples, a 27-minute podcast by Studio's head of engineering, a podcast with Studio's GM, the SDK blog, and postings describing Studio Developer. Soften to "shows little of the Studio screens and catalog"; the packages are the best public view of the API surface, not of Studio as a whole.

### B3. Unsupported (state as your own tally)

- Core package facts: 4 APIs, 25 operations, the "train_journey" demo, and the derived totals (58 APIs, 326 operations, 27 alpha / 7 beta, 218 scoped ops, 65 batch, 11 LRO, 90 linter notes). The corpus holds the 11 plugin wheels only. TokenAPI, Studio Subscription and Notification APIs and Train Journey are named in the README, so the four API names are plausible; the counts are unverifiable here but arithmetically consistent with the add-on figures.
- PyPI release history (Exhibit 12). Only "2.0.0b10 as of July 2026" is verified.
- "ACM stands for Aladdin Credit Management". Only the enum value ACM appears; the expansion is unverified, though a job posting cited earlier describes a Credit Management system generating events across Studio, so it is plausible.
- Exhibit 7's read/check/change split is your classification; the scope tags (105 read vs 100 write on 205 scoped add-on ops) are broadly consistent.
- "Studio Space ... named only in alert settings". Confirmed as far as the README goes; phrase it as "not defined in the files" rather than implying it does not exist elsewhere.

### B4. Material to add (prioritised)

1. Woodhead's three-pillar definition (APIs and events, ADC, developer tools) and the 3,000 internal citizen developers; this directly supports conclusions 1, 2, 6 and 7.
2. Events are missing entirely. Woodhead names them a pillar; postings describe streaming and webhook APIs documented with AsyncAPI; the Build vs Buy webinar: "you need access to APIs, you need access to events". Conclusion 6 should cover event-driven integration, not only Studio Notifications.
3. Auth specifics: `VND.com.blackrock.API-Key` application key (108 hits), `X-API-Key`, OAuth endpoints at client.blackrock.com, per-resource scopes (your "access tags" on p.18 are these scopes), two-layer authorisation, separate ADC auth via TokenAPI or JWT.
4. Developer portal contents and tools: catalog, API-framework docs, Data Dictionary, Jupyter notebooks, multi-language samples, ADX, ATX, and the "Aladdin Developer" notebook environment named in the README.
5. Conclusion 9 support: the APIs page says "dozens of APIs"; Newman: "releasing soon the ability to actually access those analytic APIs, portfolio analysis, security analysis"; Studio for Risk: "Run analytics programmatically". Positions, risk outputs, pricing and performance are absent from the public set.
6. ADC facts: started about 2019, launched 2021; Fivetran plus Snowflake pipelines; hundreds of accounts and tens of thousands of pipelines; replaced flat files and FTP (17); Woodhead 2024: clients "bring their own data into ADC, and ... distribute Aladdin data to their own data ecosystems", which confirms conclusion 3's inference publicly.
7. Copilot exists and is available to all clients; tools map to existing APIs; Woodhead's AI strategy includes a copilot "to help me build". The "what Studio offers for AI" row should say so, so absence in the files is not read as absence in the product.
8. Architecture signals an interviewer will expect: protobuf and gRPC-gateway fingerprint, 190 of 301 operations POST, 35 LRO-flagged operations, bitemporal fields, four-eyes state machines, the 850-attribute Portfolio entity, BQL expressions, Dynaconf config, keyring, openapi-generator via the plugin builder, discovery through api_registry.py and domain_apis_list.json.
9. Hosting and people: Azure today, AWS H2 2026; Aladdin org about 7,000 people, 4,000-plus engineers, hundreds of clients in 70 countries; Woodhead, Newman, Braunstein, Nair, Miller.
10. Minor: AdcDataset registration also needs the DATACLOUD permission; UserAPI distinguishes client employees, BlackRock "provider" employees and bots; the README says "Aladdin Studio Compute sessions" while marketing says "Aladdin Compute", so use both.

---

## Part C. Cross-cutting recommendations

1. Replace every attributed quote in A2 with a verbatim line from the transcripts (A5 lists the strongest), or drop the attribution and state the point in your own voice.
2. Fix the numbers that are checkable from public packages: 54 specs, 3,000 citizen developers (internal), Aladdin Graph as the layer.
3. Treat §4 pricing and the named-deal exhibits as outside what this corpus can confirm. If you keep them, be ready to name the public record each figure came from, and remove the two conflicting CalPERS figures or explain them.
4. Re-source the Royal London and BNP Paribas stories to BlackRock's own client videos, which give you the CEO's "on time, under budget" line and the programme-level 60 decommissioned applications.
5. Correct the three titles (Schaefer, Stratigos, Rosales/Valdez) and the "every two years" cadence claim.
6. Add events, auth specifics and the developer-portal contents to the "What It Does" document, and soften its "little of Studio in public" framing.
