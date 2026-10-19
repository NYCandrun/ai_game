<!-- agent af23ec260db82be3b; started 2026-10-19T14:04:33.057Z; finished 2026-10-19T14:09:23.490Z -->

## Fact-check of sections 4–6 ("What Aladdin costs", "What Aladdin replaces", "Competitors") against the session corpus

Document: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/pdfcheck/Aladdin_and_Aladdin_Studio_-_Briefing_and_Interview_Guide.txt (lines 793–1502). Corpus root: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ (paths below are relative to it).

**Headline: the corpus contains essentially no pricing or contract data.** Greps for "pricing", "basis point", "fee" (as a charge), "price list", every named buyer in Exhibits 10–13 (Texas PSF, Nest, LACERA, PBGC, CalPERS, PPF, UBS/Credit Suisse, GPIF, Envestnet, JPMorgan proxy figures) and every rival vendor name (SimCorp, Charles River, State Street Alpha, Bloomberg AIM, Clearwater, Enfusion, Arcesium, SS&C, Amundi ALTO, Barra) return nothing relevant. "Bloomberg" appears once (a panelist scraping CDS codes). "Amundi" appears only inside a cookie-consent vendor list in page HTML. Section 4 therefore cannot be verified or refuted from this corpus at all; sections 5–6 only in part. The two web-derived files (aladdin_studio_briefing.md, aladdin_suite_architecture.md) add: Q2 2026 tech services revenue +13% YoY and tech ACV +15% YoY; job postings calling Aladdin a "$1BN+ technology business"; Preqin acquired March 2025 (integrated as eFront Insight Feb 2026); eFront 2019; Azure today, AWS option announced Dec 2025 for H2 2026; ADC = managed Snowflake store launched 2021; and the note that "rate limits, SLAs, pricing and the Studio UI are behind the client login".

### 1. Contradicted

No claim in scope is flatly contradicted. Three places where the corpus says something materially different from the document's framing:

- **BNP Paribas AM "retired more than 60 applications when it moved to Aladdin"** (sec. 5 opening, Exhibit 16 labelled "Reported"). yt/transcripts2/008_BNP_Paribas_Asset_Management_and_Aladdin_Client_Story.md: "we were able to decommission more than 60 applications". But the speaker attributes this to the 2016–2020 "Back in the Race" programme as a whole, "with BlackRock Aladdin in the front to back chain, with Salesforce in the CRM, and transversally DataHub as a data platform". The 60 decommissions belong to the whole programme, not Aladdin alone. Also, this is BlackRock's own published transcript, so the label should be Confirmed, not Reported. (Exhibit 15's "BNP kept Salesforce" is confirmed by the same line.)
- **Royal London: "move took over two years and was the largest and most complicated program the firm had ever run"; "moved two order systems, reportedly thinkFolio and Murex".** yt/transcripts2/058_Shaping_Tomorrow_with_Technology.md (CEO Hans Georgeson, Nov 2024): the programme was "achieved it largely on time, if not ahead of plan, and we came in under budget", moved from "multiple order management systems" (not "two"; no system names), replaced systems "people have used for, in some cases 30, 35 years", and included "the implementation of Snowflake". Duration, "largest ever" and the thinkFolio/Murex names are absent. The "hired an analyst to build pre-trade tools" story is absent. HSBC is confirmed as the third partner ("yourselves in Aladdin, ourselves in Royal London, and also, of course, HSBC") but the words "middle office" are not used.
- **Exhibit 21 WatersTechnology row labelled "Reported".** yt/transcripts2/061_Best_Overall_Technology_Provider_for_2023.md is BlackRock's own winner interview: "Best iBOR or Investment Book and Record platform, Best Portfolio Analysis Tool and Best Overall Technology Provider for 2023" (Buy-Side Technology Awards). Should be Confirmed, and the document omits the third award. The 2024 Bloomberg/SimCorp results are not in the corpus.

### 2. Unsupported and risky (interviewer could challenge; nothing in corpus)

Pricing and contracts (all of section 4):
- FY2025 10-K quotes on fee basis; "$1.3 billion fixed minimum fees", "two thirds of 2025 technology revenue", "one to five years"; "over half of new mandates in 2024 covered more than one product". Plausible (10-K language is checkable) but unverified here. The "two thirds" is the document's own arithmetic.
- Texas PSF schedule ($1.575m base, 0.85 bp, $20k/user, $5k/portfolio, $600/derivative line, $160k/month implementation). Highly specific; if wrong, it is the single most damaging table. Plausible as a public-records contract but unverifiable here.
- Exhibit 11 price points: Nest ~$463k; LACERA $675–865k; PBGC $1.39m; CalPERS $1.85m/$9.26m and the Nov 2025 $9.3m→$15.0m note; PPF $6.5–9.8m; UBS CHF 50–100m; JPMorgan $14.7–25.6m; GPIF ¥2.78bn; Envestnet $3.7m/$4.1m. The GPIF row is already marked Unconfirmed. The two conflicting CalPERS figures are a visible soft spot.
- Exhibit 12 "JPMorgan payments rose almost sixfold 2017–2025" (chart data not in text). Risky.
- Exhibit 13 scoring weights (85/6/6/3; 70/20/10), LACERA finalists and the quotes "groupthink" and "unlike MSCI, BlackRock has limited on-going data management services". Attributed quotes with no corpus support.
- "0.0004% to 0.0015% of assets", "$20 million per point of retention/ACV on a $2 billion business" (own estimates; fine if presented as such).
- Exhibit 14: AWS FAQ "Enterprise add-on" and Studio "free and premium capabilities" job posting. The corpus confirms the AWS partnership (briefing file) but not the FAQ wording; "free and premium" is absent.
- Envestnet, iShares prospectus (custodians pay for Aladdin Provider), Australian trade press 2018.

Section 5:
- Janus Henderson $14.9m write-down and 10-K quotes; Corebridge three-year adoption; Aegon→Citi Aug 2026 ($380bn); Korea NPS/State Street/BNY; MAPFRE; Border to Coast; Santander 2019–2021; New Mexico SIC $26bn; Amundi/Pioneer 18 months; CRD contractor ad quote. None in corpus. Franklin Templeton appears only as a webinar panelist (yt/transcripts2/051, 045, on its Mosaic platform), not as an Aladdin decision or a "lower long-run cost" citation. STANLIB appears in the Africa webinar (yt/transcripts2/055) with no cost statement, so "Franklin Templeton and STANLIB both cited [lower long-run cost]" is unsupported.
- Exhibit 15 "routes orders to more than 200 [venues]"; FundApps, FlexTrade, Portware, Talos, Saphyre, AccessFintech, Avaloq: none in corpus.
- Exhibit 17: Securitize 2026, OTCX, AccessFintech investment, Tradeweb 2024, FactSet 2022, MarketAxess 2013 not in corpus. Coinbase: partnership confirmed but not the 2022 date ("Coinbase was the first of those", yt/transcripts2/015). Tokenization as a "fall 2026 Client Forum theme" is not in the 127-word ACF 2026 clip (yt/transcripts2/060).

Section 6:
- All revenue comparisons: "$1.98bn 2025 technology services revenue", "$1.77bn without Preqin", Deutsche Börse Software Solutions €745m / €680m ARR / +18%, "16% organic contract value growth at Aladdin [2025]", ALTO €100m. The briefing file has only Q2 2026 figures (+13% revenue, +15% ACV), a different period, so the 16% is unverified but not contradicted.
- Exhibit 18 figures ($59tn on Charles River, 28 Alpha clients, 800+ SimCorp clients, 14,000 AIM users, Clearwater $8.4bn take-private, Arcesium/Limina) and Exhibit 19's 25 dated decisions: none in corpus. Suspicious detail: several dates (Sep 2026, Aug 2026) sit within a month of today, so they rest entirely on press releases the reader cannot check here.
- Named hires: Iyan Adewuya (CPO, Dec 2025) and Gareth Morris (Sep 2026, "16 years"). Named-person claims are high-risk if wrong.
- **"BlackRock's own 2026 survey with Forrester of 303 firms found 68% favor core platforms plus their own builds."** Not in the corpus. The Build vs Buy webinar (yt/transcripts2/049) has a live poll with different numbers (below); if the Forrester figure comes from the same event cycle the document should cite it precisely.
- Celent April 2025 "63%"; Deloitte Dec 2025 "integration tax"; Chartis RiskTech100 ranks (26th→40th, dropped 2024/25) and BuySideRisk50 9th; Enfusion S-1 quote "single-tenant and cloud-migrated rather than cloud-native"; MSCI/FactSet/Clearwater naming BlackRock in 10-Ks. None in corpus.
- Exhibit 22 AI moves (SimCorp Agent Launchpad, Clearwater ~900 clients/+197%, FactSet/LSEG/MSCI/Arcesium/S&P MCP servers, BQuant wins, BlackRock Advisor Center skills repo and "Claude for Financial Advisors" Sept 2026). None in corpus.
- Private-markets and wealth rival lists (Allvue, Investran, Dynamo, Juniper Square, Burgiss, PitchBook, Addepar, InvestCloud, FNZ): Addepar/Allvue/Altvia/"amunditechnology.com" appear only in cookie-vendor HTML, not as content.

### 3. Confirmed (grouped)

- Aladdin Provider and custodians: yt/transcripts2/059 (JPMorgan Securities Services): "we developed the Aladdin provider network to bring a greater connectivity between asset managers and asset servicers"; "JP Morgan was an early adopter". Supports Exhibit 15 "custodians run services inside the client's Aladdin" and the JPMorgan custody note (date 2018 not given).
- BNP: 60+ decommissioned apps and Salesforce retained (yt/transcripts2/008, 009), with the caveat in §1.
- Royal London: HSBC partnership, single OMS replacing multiple, Snowflake (yt/transcripts2/058).
- Intesa Sanpaolo "full adoption of your platform, across the enterprise on asset management, wealth management" (yt/transcripts2/002) supports the "groups of systems at once" theme.
- Snowflake/Data Cloud rationale ("partnering... whether it's with Snowflake", yt/transcripts2/013; Fivetran blog: "ADC is supported by Fivetran for data movement and Snowflake as its cloud data platform", yt/pages/fivetran_blog.txt).
- Hosting on Azure (yt/transcripts/28, pages/ms_cloud_blog.txt); AWS H2 2026 (aladdin_studio_briefing.md).
- Coinbase and iCapital partnerships (yt/transcripts2/015; yt/transcripts/08); Symphony interoperability (yt/transcripts/10).
- 2023 Buy-Side Technology Awards (yt/transcripts2/061).
- Preqin acquisition and eFront Insight (briefing file; yt/transcripts2/062).
- In-house as the main competitor and the "hybrid" modular trend: yt/transcripts2/049 ("I don't think that clients are OK with that monolithic approach anymore... move to more of a modular approach").

### 4. Material the corpus has that the document lacks or gets slightly wrong

1. Build vs Buy webinar poll (yt/transcripts2/049, with Alpha FMC's Clark Schafer): operating model today, "mostly built in house at about 15%... actively reevaluating at 18%, hybrid... 30 and... mostly vendor platforms at 37%". Usable where the document relies on the unverified Forrester 68%.
2. Same webinar: "60 to 70% of tech costs or maintenance of current systems" and "if you have 60 to 70% of your tech organisation focused on keeping [the lights on]". A sourced maintenance-share figure the document never uses.
3. Same webinar: typical migration "12 to 18 months is what we see most regularly", with ROI visible "about that six month post implementation". Stronger, sourced timeline than the document's Corebridge/Royal London anecdotes.
4. Same webinar: top driver for change "AI and data demands at 42%, an exact tie between cost and speed to market"; capability firms most want to stop maintaining "compliance reporting... 53%, position and cash management 22%, trade life cycle at 17 and... risk infrastructure at 9%". Directly relevant to "what Aladdin replaces".
5. Same webinar on in-house risk: key-person risk, "decisions were made often times by a single architect", "by year 10, that spaghetti diagram is no longer sustainable"; and RFPs now ask "what's the API suite... connectors to Snowflake or to data bricks". Good support for the Studio-vs-build argument.
6. Citisoft episode (yt/transcripts2/029, 016): "you're locking into the backbone partnership... but then you maintain optionality on the other things", a BlackRock-hosted articulation of the "core platform plus optionality" model the document attributes to Deloitte.
7. Alpha FMC episode (yt/transcripts2/021): "70% of AI ventures fail within a client", an argument against clients building their own AI layer.
8. Royal London CEO's own framing (on time, under budget, award-winning) is a better interview talking point than the document's unsourced "largest and most complicated" line.
9. The 2023 awards included Best Portfolio Analysis Tool as well as Best Overall and Best IBOR.
10. BLQ "Is efficiency a dirty word?" (yt/transcripts/24): managers "who perhaps had previously outsourced their operations workflows... now bringing them back", useful nuance for the document's "middle office can go either way" point.
