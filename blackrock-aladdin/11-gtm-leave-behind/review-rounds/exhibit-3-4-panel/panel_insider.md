# Panel: insider (former Aladdin Studio PM), Exhibits 3 and 4, page 4

This is a check only. Nothing in the document was edited.

Live pages were fetched on 2026-10-20 into `scratchpad/break34_insider_dl/` (apis.html/.txt, aladdin-tools-for-excel.*, aladdin-data-exchange.*, aladdin-copilot.*, aladdin-risk.html and risk.txt, aws.html/.txt). The crawled Studio and Data Cloud pages were extracted to `scratchpad/studio_page.txt` and `scratchpad/adc_page.txt`. In the evidence below, "DL/" means `scratchpad/break34_insider_dl/`.

---

## BREAKS IT

### B1. Exhibit 4 places ATX and ADX outside Studio, but BlackRock files them under Studio

**What the exhibit shows.** Under "What Studio offers", Exhibit 4 shows six tiles. Aladdin Tools for Excel and the Aladdin Data eXchange appear only in a footer line: "The APIs page also links Aladdin Tools for Excel and the Aladdin Data eXchange". That wording reads as "related, not part of Studio".

**What BlackRock's pages say.** BlackRock's own product pages list both under a heading that names them as Studio resources:
- DL/apis.txt:109 reads "Additional Aladdin Studio resources", followed by "Aladdin Studio home / Aladdin Data Cloud / Aladdin Data eXchange (ADX) / Aladdin Compute / Aladdin Tools for Excel (ATX)".
- DL/aladdin-tools-for-excel.txt:106 has the same heading and lists ADC, ADX, APIs and Compute.
- DL/aladdin-data-exchange.txt:106 reads "Additional Aladdin studio resources" and lists ADC, ATX, APIs and Compute.

**Why it matters.** BlackRock's public Studio family is APIs, Data Cloud, Compute, ATX and ADX. The exhibit keeps three of those five and demotes the other two, while promoting the SDK and the portal, which BlackRock's pages do not list as products. ATX is how most Aladdin users meet Studio, and Exhibit 3's own "Excel users building reports" persona depends on it. A BlackRock go-to-market reader will see straight away that the exhibit leaves out two of their five named Studio products.

**Smallest fix.**
- Replace the footer line with: "BlackRock's product pages also list Aladdin Tools for Excel (ATX) and the Aladdin Data eXchange (ADX) as 'Additional Aladdin Studio resources'."
- Better: add both as two slim tiles inside the yellow frame.
- Cite pages 30, 32 and 33.

### B2. Exhibit 3's stacking puts BlackRock's apps on top of Studio, and client builders on top of BlackRock's apps

**What the layout claims.** The rows are stacked top to bottom: Who builds, then BlackRock's applications with Copilot, then the Aladdin Studio band, then shared services. A layered stack reads as "each row runs on the row below", so it says two things:
- (a) BlackRock's ~100 apps and Copilot reach Aladdin's services through Studio.
- (b) Client engineers, analysts and PMs build on top of BlackRock's applications.

**What the sources say.** They describe Studio as a parallel route to the same services for clients, not a layer under BlackRock's apps:
- Rosales, DL-free source `04-transcripts/timestamped/yt_oyqeCHFM5U4.m4a.ts.txt:43`: domain teams "own all of the services that serve trading data to all Aladdin applications". The apps sit directly on the services, and Studio is not mentioned.
- Studio for Aladdin Risk page, `04-transcripts/product-pages/studio_for_risk.txt:101`: "Aladdin® Studio extends Aladdin Risk beyond the user interface". Studio is an alternative to the application UI, not its substrate.
- Newman (General Manager, Aladdin Studio), `04-transcripts/part2-cloudfront-and-podcasts/013_Data_The_key_ingredient.md:25`: "we have these engines that historically were run through interfaces. So we're providing those APIs now". The APIs are a second path to the same engines.
- Studio page, `scratchpad/studio_page.txt:184`: "Whether you're a professional engineer ... Aladdin Studio gives you the data, tools, and governance support to make Aladdin your own". The builders sit on Studio, not on the apps.

**Why it matters.** "Where Studio sits" is the whole point of the exhibit, and the stack puts Studio in the wrong place relative to the apps. A BlackRock reader would wince at "client engineers build on top of our 100 apps".

**Smallest fix.** Split the two middle rows into two columns over one shared-services band:
- Left: "BlackRock's applications + Copilot (for users)".
- Right: "Aladdin Studio (for builders)", with the Who builds row over the right column only.

This also matches the document's earlier message: "Apps, Copilot and Studio share the same Aladdin services and data".

---

## WEAKENS IT

### W1. Governance, a pillar BlackRock sells, is missing from "What Studio is made of"

BlackRock names governance as part of Studio three times:
- Studio page, `scratchpad/studio_page.txt:184`: "the data, tools, and governance support".
- Aladdin Risk page, DL/risk.txt:116: "Aladdin Studio provides APIs, development tools, and governance frameworks".
- Studio for Risk, `studio_for_risk.txt:126`: "Its centralized experience supports the building, configuration, and governance of Studio workflows, including access management and usage monitoring".

Exhibit 4 has no governance tile. Exhibit 3's controls column is titled "built into the APIs" and sits outside the Studio band, so the reader concludes that governance is a side effect of the APIs rather than something Studio provides.

**Fix.** Add a strip or tile: "Governance: access management and usage monitoring (BlackRock's words)". Alternatively, retitle the side column "Governance BlackRock sells with Studio" and add the usage-monitoring line, citing the Risk and Studio-for-Risk pages.

### W2. "Aladdin Compute" and "Studio Compute" appear as two separate things

The top group has an "Aladdin Compute" tile ("Hosted, ready-to-use Python environments"). The lower group has "Studio Compute: Sessions where SDK code can run". The project's own compendium treats them as one product:
- `10-compendium/Aladdin_Studio_BlackRock_Compendium.md:299`: "BlackRock marketing calls the hosted environment Aladdin Compute".
- The README calls the same thing "Aladdin Studio Compute sessions".

The top/bottom split therefore implies 13 parts where there are fewer. The same pairing applies to ADC Admin Center with Data Cloud, and to API tokens with APIs.

**Fix.** Make the lower list's lead-in "The same parts as a client sees them inside Studio (SDK file names)". Rename the line "Studio Compute sessions (the workspace side of Aladdin Compute)".

### W3. Exhibit 3 shows Data Cloud and ADX only as ways to load data in; BlackRock sells both mainly as ways to get Aladdin data out

The only Data Cloud and ADX mention in Exhibit 3 is in "Outside inputs": "loaded into Data Cloud or through the Data eXchange". BlackRock's own descriptions lead with outbound data:
- Woodhead, `04-transcripts/requested-recordings/snowflake_data_cloud_podcast_woodhead_whisper.txt:131-135`: Data Cloud "takes all of that information that's generated through our analytics factory and inside of Aladdin and pushes that into Snowflake".
- Data Cloud page, `scratchpad/adc_page.txt:265`: "a managed investment data pipeline with preloaded Aladdin data".
- ADX page, DL/aladdin-data-exchange.txt:88: "Securely bulk transfer your data, consume large data sets downstream, and load large custom data sets". Line 103: "more than 40 standard XML, CSV, and JSON extracts".

**Fix.** Make the outside-inputs arrow two-way and add: "Aladdin data delivered out to the client through Data Cloud and ADX extracts".

### W4. The core "common data language" is missing from the shared-services band

The black band lists functions only: "Portfolio management, trading, risk, compliance, operations, accounting". BlackRock's own framing of the core is its data:
- AWS release boilerplate, DL/aws.txt:198: "providing a common data language across the whole portfolio".
- Studio and Data Cloud pages, `studio_page.txt:237-238`: "Aladdin—the language of portfolios".
- Newman, `013_Data_The_key_ingredient.md:17,25`: "the core IBOR and ABOR information" and "It does start with IBOR".

The build notes avoided "one data model". BlackRock's own phrase, however, is citable and safe.

**Fix.** Add a subtitle to the band: "BlackRock calls it 'a common data language' (IBOR, ABOR, analytics)", citing pages 21 and 22.

### W5. eFront, Aladdin Wealth and Preqin are absent from "Where Studio sits in Aladdin"

BlackRock defines Aladdin as four platforms:
- DL/aws.txt:198: "BlackRock Aladdin®—inclusive of the Aladdin platform, eFront®, Aladdin Wealth™, and Preqin".
- The site navigation lists the Platforms as "Aladdin, Aladdin Wealth, eFront, Preqin" (`studio_page.txt` nav).

The Studio GM ties two of them to Studio, in `013_Data_The_key_ingredient.md:25`: "eFront's an obvious example of that, that data coming into the Aladdin Data Cloud. With the announcement of the Prequin acquisition, bringing in that data."

The exhibit shows only "About 100 applications", which are the Aladdin platform's front ends (Rosales 1:53). It is silent on the other three platforms. The current pitch is "whole portfolio, public and private", so a BlackRock reader will notice.

**Fix.** Add one line to the applications row or the note: "Aladdin also includes eFront, Aladdin Wealth and Preqin; BlackRock says eFront and Preqin data flow into Data Cloud (Newman)".

---

## NIT

- **N1. Data Cloud is also sold as its own solution.**
  - Inside Studio is supported: Newman (013:17) says "Aladdin data cloud specifically ... which is part of Studio", and the "Additional Aladdin Studio resources" lists include it.
  - BlackRock also lists "Aladdin Data Cloud" as a peer of "Aladdin Studio" under Solutions in the site navigation. Its own page (`adc_page.txt`) never mentions Studio, and the contact form offers "Data Cloud Capabilities" as a separate interest.
  - Fix: add "also listed by BlackRock as a solution in its own right" to the tile.
- **N2. Explore is sourced to a third-party upload.** Explore is sourced to a third-party YouTube upload of an Aladdin classroom session (register 27, channel "jas jas"). Citing a leaked-looking training video to BlackRock's head of go-to-market will grate. BlackRock's own webinar names it: register 68, `requested-recordings/nine_recordings_transcripts.md:382`, "Prequin indices are also available today in Aladdin explore". Fix: cite 68.
- **N3. The APIs tile leads with an engineering codename.** "APIs (Aladdin Graph)" uses a name that exists only in the files; the compendium (:210) notes "No transcript speaker says 'Aladdin Graph'". BlackRock sells them as "Aladdin APIs" or "Aladdin Studio APIs" (DL/apis.txt). Fix: "Aladdin APIs (engineering name: Aladdin Graph)".
- **N4. The Copilot box omits custom agents.** Rosales gives two onboarding paths: "mapping one-to-one to an existing Aladdin API already out in production" (ts.txt:48 [04:39]) and "spin up a custom agent" (ts.txt:50 [04:49]). Fix: "tools map to production Aladdin APIs; complex workflows plug in as custom agents".
- **N5. The AWS box needs scope.** DL/aws.txt:196 reads "General availability for Aladdin Enterprise clients hosted in the United States is expected in the second half of 2026". Fix: "AWS option announced for US Aladdin Enterprise clients". GA status as of 2026-10-20 is not confirmed; one web search found only the December 2025 announcement.
- **N6. Name the app as "Aladdin Dashboard".** "Dashboard" alone reads as a generic word. The specifications say "Order Monitor of Aladdin Dashboard" and "Dashboard Events Monitor".
- **N7. The "A second approver" control is narrower than the column title.** It is a Data Cloud dataset control (AdcDatasetAPI: "ready for a 4-eyes check prior to release ... in Admin Center"), not an API-wide one. The column also visually spans the hosting row. Fix: "Data Cloud dataset releases need a second check", and end the column at shared services.
- **N8. "Space" is never explained.** It appears in "Studio notifications ... a Space". The build notes admit the files do not define it. Drop it, or add "(not defined in the files)".
- **N9. "Compliance by default" can be switched off.** The same spec has "Determines whether to ignore compliance violations while performing operation", so the default can be overridden. This is acceptable as worded ("by default").

---

## Holds up

- **Who builds.** The personas match BlackRock's Studio page almost word for word (`studio_page.txt:184`): "professional engineer ... code-curious portfolio manager ... data analyst automating reporting". The fourth, Excel users, is backed by the ATX page.
- **Studio over shared services.** Placing Studio over "shared services and data" matches the Studio page (`studio_page.txt:181`): "API-first approach across shared services and data".
- **About 100 apps with Copilot inside.** Rosales, ts.txt [01:53]: "around 100 Aladdin front-end applications". At [02:34]: "embedded across all of those hundred front-end applications".
- **Events as part of Studio.** This is supported:
  - Woodhead [05:25-05:27]: "a set of APIs, events, the Aladdin data cloud".
  - Aladdin Risk page, DL/risk.txt:159: "Aladdin Studio, APIs, and event-driven workflows". This matches the tile name exactly.
  - "No event specification is public" is honest.
- **Data Cloud inside Studio.** This is supported by Newman ("which is part of Studio"), by the Studio page featuring ADC (`studio_page.txt:237`) and by the "Additional Aladdin Studio resources" lists. See N1 for the separate-solution caveat.
- **Platform facts.** Snowflake plus Fivetran is correct (Fivetran blog line 33). Azure is correct: Althoff, `ms_cloud_blog.txt:130`, "all BlackRock's technology platform clients and services are hosted in the Azure cloud". "AWS announced, not live" matches the release.
- **Controls.** The control wording traces to the specs: "Default is true to run compliance on this post order request" and "4-eyes check prior to release".
- **Workspace list.** It traces line by line to the README and the AdcDatasetAPI spec, with no hosted-workspace inference.
- **Disclosures.** The developer portal is correctly shown as behind a client login, and "BlackRock gives no count of pieces" is a good, honest disclaimer.
