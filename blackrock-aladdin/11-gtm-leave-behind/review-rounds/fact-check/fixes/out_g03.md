# Group g03 fixes (Exhibits 3 and 4, page 5)

Counts: FIX 11, CITE 2, NO CHANGE 0, DECIDE 2.

## p05-01: DECIDE

- Current: Exhibit 3. Apps, Copilot and Studio all call one shared API layer
- Proposed: Exhibit 3. Apps, Copilot and Studio share the same Aladdin services and data
- Alternative: Exhibit 3. Copilot and Studio call the same Aladdin APIs
- Also change (Exhibit 3 aria-label (also carries p05-29 and p05-30)): “Apps, Copilot and Aladdin Studio call one shared API layer, which reaches the 11 public API domains, all using Aladdin Analytics, the risk engine. Every domain reads and writes shared data:” becomes “Apps, Copilot and Aladdin Studio share the same Aladdin services and data. Copilot and Studio reach the 11 public API domains through a shared API layer. The risk specifications name Aladdin Analytics as their risk engine. The domains read and write shared records:”
- Also change (Exhibit 14 (page 13), BlackRock’s own use tile; same length or shorter): “all call these APIs.” becomes “share these services and data.”
- Also change (Exhibit 14 (page 13), Aladdin’s APIs bar; same length): “BlackRock’s applications, Copilot and a client’s own code call the same APIs and read the same Data Cloud,” becomes “BlackRock’s apps, Copilot and a client’s own code use the same services and read the same Data Cloud,”
- Why: The Studio page says only “API-first approach across shared services and data” [14], and Rosales says Copilot tools map “one-to-one to an existing Aladdin API already out in production” [8]. No source says BlackRock’s own apps call the public API layer. The recommended title keeps all three actors on the sourced “shared services and data”. The alternative names only the two callers the sources show, and then the Exhibit 14 tile “all call these APIs” must also drop the apps. Either way the box text (p05-16) and Exhibit 14 on page 13 change with it. Both Exhibit 14 replacements are no longer than the current text.

## p05-16: FIX

- Current: every app, Copilot and Studio call it · access checked on every call
- Proposed: apps, Copilot and Studio use the same services · every call needs credentials
- Also change (Exhibit 3 note, add citations for the box after the Rosales clause): “2:35 [8]. The 11 domains” becomes “2:35 [8]. Shared services, the Studio page [14]. Copilot tools map to Aladdin APIs already in production [8]. All 301 public operations require credentials [6]. The 11 domains”
- Why: No source says every app calls the API layer. The Studio page says “shared services and data” [14] and Copilot tools map to “an existing Aladdin API already out in production” [8]. All 301 operations in the 54 specifications declare a security requirement (rechecked on the PyPI 2.0.0b3 files), but scope checks apply only to the OAuth options, so “needs credentials” is the accurate claim. If the p05-01 alternative is chosen, the box reads “Copilot and Studio call it · every call needs credentials”.

## p05-04: FIX

- Current: quants
- Proposed: data analysts
- Also change (Exhibit 3 note, cite the Studio page for the users): “Woodhead at 4:49 [1];” becomes “Woodhead at 4:49 [1]; its users, the Studio page [14];”
- Why: The Studio page names “a professional engineer”, “a code-curious portfolio manager” and “a data analyst automating reporting” as Studio users [14]. No source names quants.

## p05-15+p05-44: FIX

- Current: Excel tools and feeds, the APIs page [24];
- Proposed: Excel tools, the APIs and ATX pages [24, NEW]; files in and out of Aladdin, the ADX page [NEW]; events, Woodhead [1];
- Also change (Exhibit 3 Studio box subtitle): “events and files out” becomes “events, files in and out”
- Also change (Exhibit 3 arrow from the Excel tools box to Client systems, make it two-way): drawing markup only, add marker-start so the arrow points both ways
- New source: NEW · P ATX: Aladdin tools for Excel. BlackRock product page, as of October 20, 2026. https://www.blackrock.com/aladdin/platforms/products/aladdin-tools-for-excel
- New source: NEW · P ADX: Aladdin Data eXchange. BlackRock product page, as of October 20, 2026. https://www.blackrock.com/aladdin/platforms/products/aladdin-data-exchange
- Why: The APIs page [24] only names and links ATX and ADX. The ATX page says it lets users “retrieve Aladdin data”, and the ADX page describes “automated data transfer to and from Aladdin” by SFTP or IBM MQ, so files go both ways. Events rest on Woodhead’s “a set of APIs events” at 4:49 [1].

## p05-29: FIX

- Current: the risk engine every domain uses · turns positions and market data into risk numbers
- Proposed: the risk engine · turns positions and market data into risk numbers
- Also change (Exhibit 3 note, Aladdin Analytics sentence): “Aladdin Analytics is the name the risk specifications give the engine [6].” becomes “Aladdin Analytics is the name the risk specifications give the engine [6]. BlackRock’s product page calls Aladdin Risk “BlackRock’s analytics engine” [NEW].”
- Also: Exhibit 3 aria-label. Covered by the aria-label change listed under p05-01.
- New source: NEW · P Risk Management Services (Aladdin Risk product page). BlackRock, as of October 20, 2026. https://www.blackrock.com/aladdin/platforms/products/aladdin-risk
- Why: The specs name “Aladdin Analytics” only as a metric source in four risk APIs [6], so “every domain uses” has no support. BlackRock’s Aladdin Risk page calls that product “BlackRock’s analytics engine” and says it integrates “positions, data, and analytics”, which supports the rest of the box.

## p05-30: FIX

- Current: SHARED DATA · EVERY DOMAIN READS AND WRITES IT
- Proposed: SHARED DATA · THE DOMAINS READ AND WRITE THESE RECORDS
- Also: Exhibit 3 aria-label. Covered by the aria-label change listed under p05-01.
- Why: In the specs the data domain only creates records (15 POST operations) and accounting mostly reads (4 GET and 4 POST, three of the POSTs filters and one a config submit) [6]. So the domains together read and write the records, but not every domain does both.

## p05-32: CITE

- Current: Data Cloud fed by Aladdin data and analytics [1, 19];
- Proposed: Data Cloud fed by Aladdin data and analytics [1, 19]; a separate data store for each client, the 2021 launch release [NEW];
- New source: NEW · P BlackRock To Launch the “Aladdin Data Cloud” Powered by Snowflake. BlackRock press release, February 22, 2021. https://www.blackrock.com/corporate/newsroom/media/press-releases/aladdin-data-cloud-powered-by-snowflake
- Why: Source 19 confirms Snowflake but not “this client’s own”. The February 22, 2021 BlackRock release says “Each Aladdin Data Cloud client receives an independent, centrally-managed data store”, so the box words stand and only the citation is added.

## p05-36: FIX

- Current: prices, ESG, Preqin
- Proposed: prices, ESG data
- Also change (Exhibit 3 note, cite the vendors after hosting): “hosting [15, 25].” becomes “hosting [15, 25]; data vendors, ICE and Sustainalytics [NEW, NEW].”
- New source: NEW · P BlackRock Solutions Integrates ICE Data Services’ Continuous Evaluated Pricing Tool. Intercontinental Exchange press release, December 5, 2016. https://ir.theice.com/press/news-details/2016/BlackRock-Solutions-Integrates-ICE-Data-Services-Continuous-Evaluated-Pricing-Tool/default.aspx
- New source: NEW · P Access our research through your preferred platform. Morningstar Sustainalytics, as of October 20, 2026. Lists Aladdin among institutional investor platforms. https://www.sustainalytics.com/investor-solutions/analytic-reporting-solutions/esg-investment-platform
- Why: BlackRock’s own boilerplate puts Preqin inside BlackRock Aladdin, “inclusive of the Aladdin platform, eFront®, Aladdin Wealth™, and Preqin” [13], so it is not an outside vendor. ICE’s 2016 release says its pricing “has been integrated into BlackRock Solutions’ Aladdin”, and Sustainalytics lists Aladdin among its platforms. Preqin is already placed inside Aladdin in Exhibit 1 and the private-markets finding, so the map does not need a new tile.

## p05-41: FIX

- Current: App names other than Explore come from field descriptions in those specifications, so their screens are not drawn [6, 21].
- Proposed: App names other than Explore come from descriptions in those specifications, so their screens are not drawn [6]. Explore comes from a training recording [21].
- Why: Dashboard appears in field descriptions, but Risk Radar appears only in the API-level description, e.g. “Retrieve, update, or create Exceptions as surfaced in Risk Radar” [6]. Source 21 names Explore only, so its citation moves to its own sentence.

## p05-47+p05-48: DECIDE

- Current: Exhibit 4. Six pieces make up Studio
- Proposed: Exhibit 4. Six pieces of Studio, as this analysis groups them
- Alternative: Exhibit 4. Eight pieces of Studio, as this analysis groups them (and add two rows: “Aladdin Data eXchange: automated file transfer to and from Aladdin” with the ADX page, and “Aladdin Tools for Excel: an Excel plugin that retrieves Aladdin data” with the ATX page; this lengthens page 5 by about four lines)
- Also change (Exhibit 4 note, say there is no official count): “Woodhead [1] and Goel [26].” becomes “Woodhead [1] and Goel [26]. BlackRock gives no count. Its APIs page also links Aladdin Data eXchange and Aladdin Tools for Excel, which Exhibit 3 shows [24].”
- Also: Exhibit 4 rows. Row fixes for p05-48 are listed as their own objects: the APIs row (with p05-50), the Event-driven row and the Developer Portal row. They apply under either option.
- Why: No source gives a count of six. BlackRock’s APIs page lists Studio home, Data Cloud, ADX, Compute and ATX, and Snowflake’s partner page lists five capabilities, so the six rows are the author’s grouping. The recommended title says so and keeps page 5 the same length. The alternative adds ADX and ATX, which Exhibit 3 already shows.

## p05-48+p05-50: FIX

- Current: Aladdin Graph is the whole API layer, not one API: every public specification carries an id of the form agraph.<domain>.<segment>.<group>.v1.<API> [6].
- Proposed: Aladdin Graph is the whole API layer, not one API [23, 40]. Every public specification’s id begins agraph.<domain>, and 48 of the 54 take the form agraph.<domain>.<segment>.<group>.v1.<API> [6].
- Why: All 54 ids start agraph.<domain>, but three specs are v2 and three have an extra segment, so only 48 match the five-part v1 form [6]. The name Aladdin Graph is backed by the SDK README, “based on Aladdin Graph API’s swagger specifications” [23], and BlackRock’s engineering blog, “curated Aladdin Graph APIs” [40], which is already in the register.

## p05-48 (Event-driven row): FIX

- Current: Event-driven APIs | Aladdin tells a program when something happens.
- Proposed: Event-driven workflows | Aladdin tells a program when something happens [NEW, NEW].
- New source: NEW · T Technical Writer, Vice President - BlackRock. BlackRock job posting as republished by Built In Bristol, posted February 21, 2026. https://builtinbristol.uk/job/technical-writer-aladdin-product-vice-president/7444888
- Why: No BlackRock page uses “Event-driven APIs” as a product name. BlackRock’s Aladdin Risk page lists “Aladdin Studio, APIs, and event-driven workflows” as capabilities, and a BlackRock job posting covers “event-driven workflows, including streaming APIs, webhook subscriptions”. The Aladdin Risk entry is added under p05-29.

## p05-48 (Developer Portal row): CITE

- Current: notebooks and code samples the APIs page describes.
- Proposed: notebooks and code samples the APIs page describes [24]. A BlackRock job posting names the “Aladdin Studio Developer Portal” [NEW].
- Why: The APIs page describes the content but never says “Developer Portal”. The name comes from the job posting: “the Aladdin Studio Developer Portal”. The job posting entry is added under the Event-driven row.

## p05-56: FIX

- Current: A hosted space where developers run Python next to their Aladdin data; the SDK has a run mode for
- Proposed: A hosted analytics platform with ready-to-use Python environments [NEW]. The SDK has a run mode for
- New source: NEW · P Aladdin® by BlackRock (Powered by Snowflake partner page). Snowflake, archived September 9, 2024. https://web.archive.org/web/20240909090246/https://www.snowflake.com/powered-by/aladdin-by-blackrock/
- Why: Snowflake’s BlackRock partner page says “Aladdin Compute – a hosted analytics platform with ready to use python environments and automation tools.” No source says it runs “next to their Aladdin data”, so that phrase goes.

## p05-65: FIX

- Current: No event specification is public [6]; the catalog, guides, notebooks and samples sit behind a client login [24].
- Proposed: No event specification is public [6]. The APIs page describes the catalog, guides, notebooks and samples but links none of them publicly [24]. The specifications point to the guides on a developer portal that opens only after a client login [6, NEW].
- New source: NEW · P Aladdin developer portal. BlackRock, checked October 20, 2026. The address redirects to the Aladdin client login. https://www.blackrock.com/apps/aladdin-developer-portal/
- Why: Source 24 never mentions a login. Seventeen specs link to “apps/aladdin-developer-portal/#/guides/developer-guide” [6], and that address returns a 302 to aladdin-login.blackrock.com (rechecked October 20, 2026). That the catalog, notebooks and samples are also behind it is an inference, so the text states only what was observed.
