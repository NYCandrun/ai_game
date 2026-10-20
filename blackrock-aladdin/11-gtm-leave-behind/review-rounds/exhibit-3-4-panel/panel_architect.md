# Panel: enterprise platform architect, Exhibits 3 and 4 (page 4)

This is a check only. Nothing in the document was edited.

Path abbreviations used below:
- `SP` = /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad
- `UNP` = SP/unpacked
- `README` = SP/readme.md (AladdinSDK README)
- `ORDER` = UNP/asdk_plugin_trading-2.0.0b3-py3-none-any/asdk_plugin_trading/agraph/trading/order_management/order/v1/OrderAPI/swagger.json
- `ADC` = UNP/asdk_plugin_platform-2.0.0b3-py3-none-any/asdk_plugin_platform/agraph/platform/studio/adc/adc_dataset/v1/AdcDatasetAPI/swagger.json
- `ROSALES` = /home/user/ai_game/blackrock-aladdin/04-transcripts/timestamped/yt_oyqeCHFM5U4.m4a.ts.txt (source 9)
- `WOODHEAD` = /home/user/ai_game/blackrock-aladdin/04-transcripts/requested-recordings/snowflake_data_cloud_podcast_woodhead_whisper.txt (the same interview as source 1, YouTube auto-captions at 04-transcripts/part1-youtube-and-site/01_From_Analytics_To_Intelligence_BlackRock_s_Journey_To_Data_P.md)
- Live pages were fetched on 2026-10-20: https://www.blackrock.com/aladdin/platforms/products/aladdin-studio, .../apis and .../aladdin-data-cloud.

---

## BREAKS IT

### B1. The stack puts BlackRock's ~100 apps and Copilot on top of Studio, and the builders on top of the apps

**What the layout claims.** In a layer diagram, each layer uses the one below it. Exhibit 3 stacks four rows in this order:
1. Who builds
2. BlackRock's applications (with Copilot)
3. Aladdin Studio
4. Shared services and data

Read this way, the exhibit says two things:
- Client engineers, PMs, analysts and Excel users build through BlackRock's apps.
- BlackRock's apps and Copilot reach Aladdin's services through Studio.

**What the sources say.** No source puts the apps on top of Studio. They describe the apps and Studio as parallel consumers of the same services.
- ROSALES:43 [04:06]: the trading team "own all of the services that serve trading data to all Aladdin applications". The apps draw on the domain services directly.
- WOODHEAD:127-130 [05:18-05:27]: "Aladdin Studio is essentially the user experience that allows people to think of Aladdin as a platform. It exposes everything Aladdin knows how to do as a set of APIs, events, the Aladdin data cloud". Studio is an exposure layer for builders, not a substrate under BlackRock's apps.
- The document contradicts its own Exhibit 3. Exhibit 14 draws two side-by-side columns, "BLACKROCK'S OWN USE" and "A CLIENT'S USE · THROUGH STUDIO", over one "Aladdin's APIs" bar. Its title is "BlackRock's applications and a client's code draw on Aladdin's shared services and APIs" (doc text, the Exhibit 14 block).
- The body text says the Copilot/Studio link is inferred: "So I infer that Copilot and Studio use the same APIs" (doc text, Part 3 paragraph citing 9, 1). Exhibit 3's stacking presents that inference as fact, and in a stronger form (Copilot sitting above Studio).

**Smallest fix.** Put "BlackRock's applications + Copilot" and "Aladdin Studio" side by side in one row, both resting on the shared-services band. Put "Who builds" above the Studio cell only. This matches Exhibit 14 and the build note's original title, "Apps, Copilot and Studio share the same Aladdin services and data".

### B2. Data Cloud is drawn on the wrong side of the shared data: the SDK's second, non-API path to Aladdin data is missing

**What the layout claims.** The black band says shared services and data are "reached through the 11 public API domains". Data Cloud appears in only two places:
- as a Studio tile in Exhibit 4;
- as a sink for outside inputs ("loaded into Data Cloud").

So the exhibit implies one road to Aladdin's data, the APIs, governed by the API controls column.

**What the sources say.**
- **Data Cloud holds Aladdin's own data, copied out of the core.**
  - WOODHEAD:130-136: Data Cloud "takes all of that information that's generated through our analytics factory and inside of Aladdin and pushes that into Snowflake".
  - WOODHEAD [14:16-14:22]: "The purpose of the Aladdin data cloud is to take all of the data that lives inside of Aladdin, to take all of that third party data ... and then to deliver that to our clients".
  - Live Data Cloud page: "a managed investment data pipeline with preloaded Aladdin data that is normalized & mapped on ingestion".
  - ADC:291 ff. (reconcile operation) refers to "all ADC Datasets under ALADDINDB schema ... against another gold-copy client".
- **It is reached by SQL over Snowflake, not through the 11 domains.**
  - README:3: the SDK is there to "access and utilize Aladdin APIs and Data Cloud". These are two things.
  - README:343: "ADC (Snowflake) access is provided via the ADCClient. This is a wrapper around snowflake-connector-python or snowflake-snowpark-python".
  - README:360 and 363: `adc_client.query_sql('SELECT * FROM "CASH_ENTRY" ...')` and `adc_client.write_frame(...)`.
  - README:147: "Snowflake user role to be used".
  - README:220: "ADC account URL, up to and including '.privatelink'".
  - README:413: `CALL ALADDINDB.PUBLIC.UPDATE_PUB_KEY_SP(...)`, run "From Snowflake UI".
  - None of this goes through an `agraph.*` API, an API scope or the API controls.
- **Its main flow is outbound, to the client's own Snowflake.**
  - WOODHEAD:341-352 [14:38-14:52]: "we can deliver that to them where they are. So they're sitting in their cloud provider of choice ... through Snowflake and through data sharing".
  - WOODHEAD:449-450: "We operate hundreds of snowflake accounts. We share data to hundreds of snowflake accounts".
  - The exhibit shows no outbound arrow.
- **Data from eFront and Preqin, which are not in the 11 domains, arrives through Data Cloud.** The document says so itself: "The private-markets data it is adding from eFront and Preqin is going into Data Cloud, which is part of Studio 22" (doc text, Part 3). The black band implies it all comes through the domains.

**Smallest fix.**
1. Change the black band's subtitle to "reached through the 11 public API domains and, as a copy, through Data Cloud (SQL on Snowflake)".
2. Draw Data Cloud as a second data store fed from the core and shared out to clients' Snowflake accounts. A side bracket would do; a new row is not needed.
3. Say in the note that Data Cloud access is governed by Snowflake roles, not by the API controls.

---

## WEAKENS IT

### W1. The "Controls built into the APIs" column spans four rows (applications, Studio, shared services, hosting), but the controls cover only part of the API layer

The column runs from the top of the applications row to the bottom of the hosting row (page image). So it implies the controls apply to Copilot, to all of Studio (Data Cloud included) and to hosting. Each item applies more narrowly than that.

**Access set per API.**
- The per-API scope exists only on the OAuth path. Every operation in all 54 specs accepts four alternatives: OAuth2AccessCode or OAuth2ClientCredentials, each with an API scope such as `trading.order_management.order.v1.Order:read`; `{"APIKeyHeader": [], "ClientKeyHeader": []}`; or `{"APIKeyHeader": [], "basicAuth": []}`. The last two carry no scope (ORDER:24-44; the same in all 54 per securityDefinitions).
- The SDK's default AUTH_TYPE is `Basic Auth` (README:88, Default column).
- Scopes can be switched off: "AGRAPH_SCOPES_ENABLED | If enabled, adds scopes from swagger specs to oauth access token request | ... | True | True/False" (README:45).
- "A user sees only what their entitlements allow" is a platform-wide permission service, not something inside each API. It lives in the `platform` domain, for example PermissionAPI: "The permission grants access to portfolios" (UNP/.../platform/access/permission/v1/PermissionAPI/swagger.json:565).
- The same service governs the apps. UserAPI: "may be granted access to Aladdin applications" (UNP/.../platform/identity/user/v1/UserAPI/swagger.json:13).

**Compliance by default.**
- It is a caller-overridable flag on one API. ORDER:3028: `runCompliance` "Default is true to run compliance on this post order request".
- With a timeout, orders post anyway. ORDER:1955: "orders will be posted with the "Compl Pending" status set regardless of any violations".
- `runCompliance` appears in OrderAPI only. TradeAPI (`/trades:post`, `/trades:batchPost`, "Post or update trade") has no compliance parameter. The text is accurate, but a column framed as built-in controls overstates its reach.

**Copilot's controls are its own.**
- ROSALES:71 and 74 [06:38, 06:58]: "this filtering and access control node ... which user groups have access to this and even which Aladdin apps can even access these plugins".
- Exhibit 14 keeps these separate as "WHAT COPILOT ADDS FOR AI". The Exhibit 3 column visually claims the Copilot cell.

**Data Cloud has separate governance.** The live Data Cloud page says "maintaining the Aladdin platform's security & controls and improving access with built-in governance". Snowflake roles and keys sit outside the API path (README:141-147), as set out in B2.

**Smallest fix.** Shorten the column so that it sits against the shared-services band only. Retitle it "Controls in the public API specifications". Add "on the OAuth path" to the first item, and "callers can turn it off" to the second.

### W2. "A second approver: Dataset releases need a second check" is contradicted by the API that defines the check

- The four-eyes step is a state in the Admin Center workflow. ADC:3400: "STATE_REVIEW: In review state, dataset is ready for a 4-eyes check prior to release".
- The same API releases datasets with no review state:
  - **register:** "Datasets are stored in STATE_RELEASED in ADC and indexed on Aladdin Studio" (ADC:1689).
  - **refresh:** "When a major version increment occurs ... the state of the new version is set to STATE_RELEASED" (ADC:1461).
  - Both require only the "StudioAdmin" permission.
- This is a Data Cloud (Studio) control, not a shared-services API control, so its place in an "into the APIs" column is also doubtful.

**Smallest fix.** Reword the item to "Data Cloud datasets edited in the Admin Center go through a four-eyes review state before release". Alternatively, drop it from Exhibit 3 and keep it in Exhibit 14 with the same rewording.

### W3. The "11 public API domains" band is neither "the business services" nor "the way in"

**The band's label does not match the domain list.**
- The label reads "Portfolio management, trading, risk, compliance, operations, accounting".
- The 11 packages are accounting, analytics, clients, compliance, data, investment-operations, investment-research, platform, portfolio, portfolio-management and trading (README:313-323).
- "risk" is not a domain. The risk APIs sit under `analytics.oversight.governance` (RiskRuleAPI etc.).
- The `platform` domain is not a business service. It holds identity, user groups, permissions, and **Studio's own API**: `agraph.platform.studio.adc.adc_dataset.AdcDatasetAPI`, "Used by Studio's ADC Admin Center" (ADC:13).
- So part of Studio is drawn inside the band that sits below Studio.

**The band is not the whole public API surface.**
- The SDK names Studio APIs outside the 54 specifications:
  - "the Studio Subscription and Notification APIs" (README:587);
  - "Aladdin's TokenAPI" (README:381).
- The live APIs page says "Dozens of Aladdin APIs available – with constant new additions".

**Apps and Copilot do not reach the services through these 11 packages.** Copilot draws on "a couple thousands agents and tools" from "50 60 Aladdin engineering teams that cover specific domains" (ROSALES:72 and 41). The 11 are a client-facing SDK packaging. The note says this ("the packages of BlackRock's public SDK"), but the band reads as the architecture.

**Smallest fix.** Change the subtitle to "11 public API domains (SDK packages), including a platform domain for identity, access and Studio's own Data Cloud admin". Replace "risk" with "analytics and risk".

---

## NIT

**N1. Hosting row.**
- The row spans the full width, which places Studio and Data Cloud on Azure.
- The Data Cloud page says "Leverage a cloud-agnostic platform". Woodhead says "hundreds of snowflake accounts" (WOODHEAD:449).
- The AWS FAQ lists "ADC (Enterprise add-on)" separately (fact-check compiled.json quoting the joint release).
- Client code can run "on a developer's local machine" (README:179), and Exhibit 14 says client apps "Run in the client's own environment".

Smallest fix: add to the note "Data Cloud runs on Snowflake; client code may run outside Aladdin's hosting".

**N2. Return path missing.**
- WOODHEAD (part1 file, line 26): "taking those artifacts that people come and build on top of Aladdin and natively integrating them into the investment process".
- Nothing in the drawing returns from builders into Aladdin.

This is optional. One line in the note would cover it.

**N3. Copilot box: "each tool matches an Aladdin API already in production".**
- This is the first of two onboarding paths. The second is "the ability to spin up a custom agent" (ROSALES:50 [04:49]).
- The body text already says "Teams can also register agents of their own".

Smallest fix: change the box to "its tools map to Aladdin APIs already in production; teams also add agents".

**N4. "Client engineers".**
- Studio is not only for clients. WOODHEAD:236 [10:12]: "inside of BlackRock, we have 3,000 citizen developers".
- The Studio page says "professional engineer".

Smallest fix: "Engineers (clients' and BlackRock's)", or just "Professional engineers".

**N5. "About 100 applications".** The source says "around 100 Aladdin front-end applications" (ROSALES:18 [01:53]). Adding "front-end" stops a reader treating them as services.

**N6. Exhibit 4 split.**
- The "offers" / "workspace" split is by source (marketing names vs README config names), not by architecture. As a result:
  - Aladdin Compute (tile) and Studio Compute (workspace) look like one service counted twice;
  - Data Cloud and ADC Admin Center, and APIs and API tokens/applications, pair the same way.
- The note does say the lower group comes from the README.

Smallest fix: add "(the Compute tile)" and "(for the Data Cloud tile)" to the matching workspace lines.

**N7. Aladdin SDK tile.** The tile says "login, retries and rate limits". It omits that the SDK is also the Data Cloud client (README:341-363), which matters for B2. Add "and a Data Cloud (Snowflake) client".

**N8. "Outside inputs" placed below "Hosting". OPINION.**
- The position suggests inputs enter at the hosting layer.
- ADX loads "to Aladdin", so into the core, while Data Cloud loads go into Studio.
- A side-entry arrow into the shared-data band and the Data Cloud would be more accurate.

---

## Holds up

- **Studio sits between builders and Aladdin's services.**
  - Live Studio page: "Empowering unique outcomes via our API-first approach across shared services and data".
  - WOODHEAD:129-130: "It exposes everything Aladdin knows how to do as a set of APIs, events, the Aladdin data cloud".
  - The "shared services and data" band name is BlackRock's own wording.
- **BlackRock's apps sit on the same services the public APIs expose.**
  - ROSALES:43 ("all of the services that serve trading data to all Aladdin applications").
  - RiskRuleAPI info: "Retrieve, update, and create Rules and Rule Subscriptions as surfaced in Risk Radar". This is a public spec naming an app it shares data with.
  - (B1 objects only to the stacking order, not to the shared base.)
- **Data Cloud as part of Studio.**
  - Woodhead lists it among Studio's parts.
  - Snowflake partner page (source 42): "Aladdin Studio includes tailored products and capabilities for the investment process: • Aladdin Data Cloud powered by Snowflake ... • API surface ... • Aladdin Compute".
- **The 11 domains are the official plugin set.** README:313-323 lists exactly 11. All 54 specs carry `x-aladdin-api-id` beginning `agraph.` (ORDER:16 shows the pattern), so Exhibit 4's "Every public specification's id starts agraph.<domain>" is correct.
- **Per-API OAuth scopes exist in every spec**, with read/write granularity per resource (ORDER:24-35).
- **runCompliance defaults to true and violations are returned** (`complianceViolations`, "Compliance violations triggered by posting this order").
- **The four-eyes state exists** in the Admin Center workflow (ADC:3400). W2 objects only to "need".
- **Hosting on Azure today.** Microsoft Cloud blog (source 35): "all BlackRock's technology platform clients and services are hosted in the Azure cloud". The AWS option is correctly marked "announced".
- **Every "Inside a client's Studio workspace" line matches the README.**
  - Projects: "under a personal / shared project".
  - S3 integration: README:160-162.
  - Compute sessions: README:179.
  - Tokens and OAuth apps: README:89 and 258.
  - Notifications to USER/PROJECT/SPACE by SMTP/PUSH: README:184-188.
  - ADC Admin Center: ADC:13.
  - Space is correctly not given a box.
- **"Who builds" wording comes from the Studio page**: "a professional engineer ..., a code-curious portfolio manager ..., or a data analyst automating reporting". The Excel row comes from the ATX page. ATX and ADX are correctly placed as links from the APIs page ("Additional Aladdin Studio resources").
- **"No event specification is public" is correct.** None of the 54 specs is an event/AsyncAPI spec. The only "event" types in the SDK are Studio notification event types (README:186).
