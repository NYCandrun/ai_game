<!-- agent a166f99aed19bdcd7; started 2026-10-19T13:42:07.812Z; finished 2026-10-19T13:46:08.871Z -->

Fact-check of the Aladdin Field Guide claims against 39 podcast transcripts (transcripts2/001–039) plus transcripts/11_, 12_, 13_. All read in full. Note: 11_/12_/13_ are the published-page versions of 013_/019_/023_ respectively.

## 1. CONTRADICTIONS
No transcript directly falsifies a page claim. Two claims are in tension with what BlackRock speakers say:

- "~100 front-end apps / about a hundred others" (overview, LAYERS). Afwa Kandawire (Global Head of Aladdin Platforms) describes the platform as going "from thousands of applications to hundreds of thousands and maybe at some point millions of services" (027_Principles_of_Design_Podcast.md). The "front-end" qualifier may save the page, but an interviewer will think in thousands of applications, not ~100.
- "Citizen developer: BlackRock's term" (GLOSS). It is used by Microsoft's Jason Wild, UPP's CIO ("the concept of a citizen developer is really interesting to me", 034_The_Evolution_of_the_Canadian_Pension_Model.md) and Lance Braunstein says "we call that program broadly citizen development, but like the title is not important" (022_Microsoft_and_Aladdin_Partner_Story.md). It is an industry term BlackRock adopted, and the program is "citizen development".

## 2. REFINEMENTS
- Cloud migration (LAYERS "client-by-client migration"): the first stage was explicitly "a lift and shift, and that meant really focusing on moving the infrastructure" with "minimal change" to applications; the stated reason was reach, "available to more prospects in more regions than we had datacentres available" (027). Elasticity and PaaS were deferred; Lance in June 2024 still said "there is still a lot to be done in the cloud, especially as we think about elastic compute" (038_The_Way_Forward_Part_2_podcast.md).
- "One booked trade updates every view" / single source of truth: the founding principle was literally "one database" (Sybase); trading was carved out onto Cassandra with write-behind, and now "the database is no longer the single source of truth, but rather the domain is the single source of truth for that domain" via domain-driven design (027). The page's 11-domain split should be described as this deliberate move from "layered architecture to a services architecture".
- Tenant model (overview): every client runs the same code. "Every single client environment looks the same, is built the same way, we have a single control plane" and "we always try to push the same software out to all clients" (027). The page never states the single-code-base principle, which is central to how Studio changes are shipped.
- Aladdin Accounting (DOMDESC): not a mature everywhere-feature. Kunal Khara (Nov 2023): clients are "pushing us very hard to move faster in the way we are designing and deploying our accounting capabilities", most "have been using us today for the investment book of record" (010_Bringing_to_life_the_Global_Insurance_Report.md). Accounting work is "almost entirely predicated on" IBOR/ABOR unification for insurers.
- Studio scope (PRODUCTS): Richard Newman, GM Aladdin Studio, confirms "Aladdin data cloud specifically ... is part of Studio" and that analytics APIs "portfolio analysis, security analysis" were "releasing soon" (Jan 2025) under "the Studio umbrella" (013_Data_The_key_ingredient.md). The page's "what is not here: risk analytics outputs" should say these APIs exist but are login-only.
- ADC content (PRODUCTS): beyond IBOR/ABOR the stated vision is eFront data, Preqin data, LSEG data, plus BlackRock IP "around credit analytics, around mortgage-backed security data, around insurance analytics" (013).
- Preqin date: page says March 2025; Sudhir Nair (June 2025) confirms "about three months ago, we closed our next acquisition" (033_The_art_of_the_possible...md). James Werner (Mar 2026) says "about 18 months ago, we acquired" (039_Why_APAC_Investors...md), i.e. counts from the mid-2024 announcement. Say "announced 2024, closed March 2025".
- Aladdin Wealth AI commentary (PRODUCTS): internal name is "AI auto commentary"; it blends holdings, market data and "the bank's CIO views, buy lists ... model portfolios" into "your first draft or script for your client meeting" (039). Morgan Stanley is a named user.
- Copilot evaluation (AI section, "evaluation-driven development"): in Nov 2024 Syril Smith Garson said "there's no easy way to evaluate the responses. There's no universal way to do that yet" and "POC is easy. getting past the POC has been a much bigger challenge" (023_Microsoft_Copilot_Episode_Part_2.md / 13_). The 2025 eval pipeline is therefore recent; frame it that way.
- eFront role (PRODUCTS): Tarek Chouman says bringing eFront in "led us eventually to the creation of the whole portfolio concept" (014_Democratizing_private_markets.md); Sudhir calls eFront "our first major technology acquisition" in 2019 (033).

## 3. CONFIRMATIONS
- Built for BlackRock first, then sold: "Aladdin was a BlackRock system before anyone else" (014); "over 20 years for external clients" (036_The_invisibility_of_the_engine.md, recorded 2023).
- Institutional only: every Never Done episode closes "designed for institutional, wholesale, qualified, and professional investor or client use only" (018, 028, 029, 033, 034).
- Cloud partner Microsoft: "you're great at data centers. We will never be the data center operator that you are" (022); "We had chosen our cloud provider" (027).
- eFront 2019, Preqin 2025: "we acquired eFront in 2019 ... We did that with Preqin this year" (016_How_Asset_Managers_Rethink_Operating_Models.md).
- Copilot plugin model: "how do we have each team be able to build their own plug-in or capability into the product"; "There's no copilot without plug-ins" (023/13_).
- Citizen developers as Studio audience: "python notebooks up on the desks of the traders" (001_4IR_Part_2.md); "burgeoning community of individuals saying 'I need that in the form of an API'" (017_How_Data_Architecture_Shapes_Modern_Trading.md).
- Human-in-the-loop and unchanged control framework for AI (037_The_Way_Forward_podcast.md).
- Shared compliance service history: Sue Zheng stripped compliance out of an app to "build this other server sitting on top of the service that handles the compliance checks" (027).

## 4. NEW FACTS (prioritised)
1. "Whole portfolio" is BlackRock's strategic frame, absent from the page: a holistic view "regardless of the asset class", expected to "become the norm" (014); Cam Skinner: privates must coexist with publics but "you cannot lose the fidelity and the uniqueness of the data sets" (016).
2. "User provider model": BlackRock is first user and provider of the same software; "BlackRock, the house, is using the same software ... We have skin in the game" (027). Explains how product decisions are validated.
3. Platform org runs a "product operating model" with "product families": mission control, hosting services, engineering services, enterprise architecture, product office (027).
4. Design principles: "stability being our first feature", "stability, resilience, scale, performance, security, as a feature" (037); design for worst case, eager caching, and over-provision "plus another like 20 or 30% just in case" (027).
5. APIs were "opened up ... over the last five years" (016, Jan 2026), reducing lock-in to non-backbone vendors; clients now lock in the backbone and "maintain optionality on the other things".
6. Copilot productisation: clients may want "your orchestrator", "your plug-ins" in their own copilot, or inject plug-ins into Aladdin Copilot; answers in M365 Copilot must show "powered by Aladdin" (023/13_). Product work shifted to "the platform and services level ... setting up the factory floor".
7. Newman's role is "between Commercials and Engineering"; biggest ADC risk is "production ... users who ... are assuming the data is right" (013).
8. AI product today (2026): Pavan Pemmaraju, Head of AI Product & Engineering, describes a "memory module" for preferences, "portfolio becomes a living system", and expects "high confidence, low risk actions" automated in "12 to 18 month" (028_Reducing_time_to_insight...md). He built PM tooling with "99% of generated code".
9. Risk product: Jess Fitzgibbon says products are being refactored so "the data model itself is structured for agentic use cases" and agents must work "without data transfer, without needing to duplicate data" (028).
10. Workflow design doctrine: "How do we go from 10 steps to 3 steps?" and "not just augmenting but transforming workflows" (019/12_); Kunal counters "it's not as simple as ... 14 steps ... three" (037).
11. Trading connectivity: via FIX "Aladdin ... communicates to a network of hundreds of participants, broker dealers, venues, trading platforms" (017). Kamya's "shift left" concept: construct portfolios with execution in view.
12. Client implementation numbers: BNPP AM decommissioned "more than 60 applications" with Aladdin front-to-back, Salesforce CRM and a DataHub (008); Intesa did "full adoption ... across the enterprise" and built Fideuram Direct on Aladdin (002); Morgan Stanley embedded risk "into their advisor desktops" from 2015-16 (036); SLC: IBOR/ABOR "we'll never build those. Those will always be outsourced" (025).
13. Market sizing used by BlackRock: private markets "$13 trillion today ... $30 trillion" ("30 by 30", 014, 016); institutions ~30% in privates; insurers manage ~$35T, outsourcing doubled 7% to 15% (010); APAC 40-45% of assets in cash (039).
14. Private markets engineering: Aladdin's SWIFT capability reused for private-market cash wires; private credit modelled multi-asset by "structural features", no DVP/STP in privates (027).
15. Leaders and titles: Sudhir Nair (Global Head of Aladdin, 25 years), Kunal Khara (Global Head of Aladdin Product), Tarek Chouman (Global Head Aladdin Client Business, ex-eFront CEO), Lance Braunstein (engineering), Afwa Kandawire, Sue Zheng (Tech Fellow), Syril Smith Garson (Head of Product for AI), Cameron Skinner (Solutions Engineering), Pia Schaefer (Value Engineering), Meera Jessa (host).

## 5. TERMINOLOGY
- IBOR, not OBOR: speakers say "investment book of record"/IBOR (010, 013, 016, 025); the page's "ABOR / OBOR" gloss will read oddly.
- "Provider user" (page) vs "user provider model" (BlackRock): different concepts; make the distinction explicit.
- "Whole portfolio" (BlackRock) vs "total portfolio approach / TPA" (Canadian pensions, "Maple 8", 021, 034).
- "Private markets", not "alternatives": Tarek "tells us often it's not alternatives, it's private markets" (014).
- Copilot vocabulary: "orchestrator", "plug-ins", "skills", "micro apps", "springboard moments", "factory floor", "agentic workflows", "human in the loop"; the page's "supervisor agent", "plugin registry", "tools" are not the words used.
- "Federated": used once by the host for BlackRock's AI approach; Alpha FMC's Laura Kayrouz names "federated model" as jargon to retire (021).
- "Operational alpha" and "change alpha" (011/012), "time to insight", "knowing to doing" (028), "shift left" (017), "Never done", "tech optimism and tech pragmatism" (037), "stability as a feature", "services architecture", "domain driven design", "single control plane", "product families", "mission control" (027).
- "Aladdin Graph" is never spoken in any transcript; speakers say "Studio umbrella", "APIs", "Aladdin Data Cloud".
