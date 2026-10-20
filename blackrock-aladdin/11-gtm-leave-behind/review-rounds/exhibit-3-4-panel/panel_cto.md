# Panel: CTO of a large asset manager evaluating Aladdin (Exhibits 3 and 4, page 4)

Check only. Nothing in the document was edited.

Reading as a buyer, the two exhibits tell me five things. (1) My engineers, PMs, analysts and Excel users all build on one Studio layer. (2) That is the layer BlackRock's own ~100 apps and Copilot sit on. (3) Everything below the apps is wrapped by "controls built into the APIs". (4) My data flows *in* through Data Cloud or ADX. (5) Studio is a mature set of six parts. Points 2 and 3 go further than the public sources. Point 4 leaves out half the flow. Point 5 leaves out maturity.

Abbreviations used below:
- README = /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/readme.md (the AladdinSDK README)
- specs = /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/unpacked/ (the 54 swagger.json files)
- TS = /home/user/ai_game/blackrock-aladdin/04-transcripts/

---

## BREAKS IT

### B1. The layer order puts BlackRock's ~100 apps and Copilot on top of Studio, and puts "Who builds" on top of the apps
**What a buyer reads.** In a layered stack, each row sits on the row below it. The picture therefore says two things. First, BlackRock's own applications run on Studio, so I would get the layer BlackRock builds on. Second, my builders work through BlackRock's applications. No public source says either.

**Evidence**
- Rosales says Copilot tools map to internal production APIs, and he never says Studio. TS/timestamped/yt_oyqeCHFM5U4.m4a.ts.txt:47-48: "define a tool as / Kind of mapping one-to-one to an existing Aladdin API already out in production".
- The document's own Exhibit 14 (same HTML) draws the two side by side, not stacked: "BlackRock's applications, Copilot and a client's code draw on Aladdin's shared services and APIs". It also says a client's applications "Run in the client's own environment, on the client's credentials" and that its engineers "Route Aladdin calls through the client's own gateway". That contradicts a "Who builds" row sitting above BlackRock's apps.
- Woodhead describes Studio as something offered to builders. He does not describe it as a layer under BlackRock's apps. TS/part1-youtube-and-site/01_From_Analytics_To_Intelligence_BlackRock_s_Journey_To_Data_P.md:22-26: "Aladdin Studio is essentially the user experience that allows people to think of Aladdin as a platform. It exposes everything Aladdin knows how to do as a set of APIs events ... the third pillar of studio is how do I bring those people in?"
- I found no source saying the ~100 apps call the public Studio APIs. I grepped TS for "same api(s)", "internally" + api/studio, and "our own" + platform.

**Smallest fix.** Put the BlackRock-applications row beside the Studio band, so both rest on the black band. Put "Who builds" over Studio only. This matches Exhibit 14. Failing that, add to the note: "Apps and Studio both draw on the shared services; the public record does not say the apps are built on Studio."

### B2. The "Controls built into the APIs" column spans every row from the apps to hosting, so it reads as covering everything I build. Studio's main data paths are not APIs.
**What a buyer reads.** The column's title is precise, but its geometry claims coverage of the apps, all of Studio (Data Cloud, Compute, storage, Excel) and hosting. Several Studio paths bypass the REST APIs. On those paths, none of the three controls shown is documented.

**Evidence**
- **Data Cloud is reached as Snowflake, not through the APIs.** README:343: "ADC (Snowflake) access is provided via the ADCClient. This is a wrapper around snowflake-connector-python or snowflake-snowpark-python"; it authenticates with "'oauth' or 'snowflake_jwt' (i.e. RSA Keys)" and lets you "update role, database, schema, warehouse". The README:360-363 sample both reads ("query_sql('SELECT * FROM \"CASH_ENTRY\"...')") and writes ("adc_client.write_frame(df=df, table_name='TARGET_TABLE_NAME')").
- **Storage uses its own keys.** README:160-162: "ACCESS_KEY_ID ... To be sourced from S3 Storage Integration in a Studio Project".
- **ADX is file and message transfer, not the APIs.** https://www.blackrock.com/aladdin/platforms/products/aladdin-data-exchange (live 2026-10-20): "Use Secure File Transfer Protocol or IBM MQ to manage files securely" and "Bulk import data with our 35 standard CSV loaders covering trades, orders, positions". Exhibit 3 draws ADX as a route for my data, under a column that implies API controls. Nothing public says that bulk-loaded orders go through "compliance by default".
- **The Data Cloud page names its own controls, separate from the API ones.** https://www.blackrock.com/aladdin/platforms/products/aladdin-data-cloud: "maintaining the Aladdin platform's security & controls and improving access with built-in governance".

**Smallest fix.** Shorten the column so it spans only the black "shared services" band (the APIs). Add one line: "Data Cloud (Snowflake), storage, file transfer (ADX) and Excel have their own access controls, not shown."

---

## WEAKENS IT

### W1. Each control is stronger as worded than as specified (this also applies to Exhibit 14, which uses the same wording)
- **"Access set per API. Each API has its own access scope."** That is true only for OAuth. All 301 operations in the 54 specs also accept a non-OAuth option with no scope: the API key plus `X-API-Key`, or basic auth. I recomputed this over specs. Example: OrderAPI swagger.json, security list of each operation (lines 39, 43): `"ClientKeyHeader": []`, `"basicAuth": []`. The SDK can also switch scopes off (README:45: "AGRAPH_SCOPES_ENABLED | If enabled, adds scopes from swagger specs to oauth access token request | No | True").
- **"Compliance by default."** It is a flag the caller can set. OrderAPI swagger.json:3028 says "runCompliance ... Default is true to run compliance on this post order request." Line 3041 adds `complianceTimeout`: "If the non-zero time is reached and the run is not complete, orders will be posted with the "Compl Pending" status set regardless of any violations". (The OrderAPI itself is labelled `stable`, which holds up.)
- **"A second approver: Dataset releases need a second check."** This is a state in an alpha API about publishing Data Cloud datasets. It is not a control on my code. AdcDatasetAPI swagger.json:17 `"x-aladdin-api-stability": "alpha"`; line 3400: "STATE_REVIEW: In review state, dataset is ready for a 4-eyes check prior to release". The spec does not say that release is blocked without approval.
- **"A user sees only what their entitlements allow."** The entitlements are themselves writable through stable public APIs. UserGroupPermissionAPI swagger.json:255 `/userGroups/{parent}/userGroupPermissions:batchCreate` ("Add Permissions to a User Group"). UserGroupMemberAPI `members:batchCreate` ("Add Users to a User Group").

**Smallest fix**
- "With OAuth, each API has its own scope."
- "The order API runs compliance unless the caller turns it off."
- "Data Cloud datasets have a four-eyes review state before release."

### W2. My data is drawn flowing only in; the outbound half is missing
**What a buyer reads.** "Outside inputs" shows data going one way only. For a CTO, getting Aladdin data into my own data platform is the first question. BlackRock markets that direction prominently.

**Evidence**
- Fivetran blog (source 28), TS/product-pages/fivetran_blog.txt:30, Woodhead: "enabling clients to bring their own data into ADC, and to distribute Aladdin data to their own data ecosystems."
- Woodhead (source 1), TS/part1-youtube-and-site/01_...md:52: "we can deliver that to them where they are. So if they're sitting in their cloud provider of choice ... through snowflake and through data sharing".
- ADX page: "automated data transfer to and from Aladdin. It helps you access Aladdin data in your own ecosystem" and "more than 40 standard XML, CSV, and JSON extracts".
- The README write path (`write_frame`, README:363) is a third inbound route that the picture does not show.

**Smallest fix.** Make the bottom row two-way: "...and Aladdin data out to the client's own systems, through Data Cloud data sharing or Data eXchange extracts."

### W3. The black band says that all six functions are "reached through the 11 public API domains"
**What a buyer reads.** These 11 domains are the surface I get. In fact the public set lacks core objects, and BlackRock says more APIs exist.

**Evidence**
- APIs page https://www.blackrock.com/aladdin/platforms/products/apis: "Dozens of Aladdin APIs available – with constant new additions" and "Aladdin Studio already has a large universe of available APIs".
- The document's own Exhibit 2 says "None of the 54 is a position API".
- The public "risk" APIs are governance workflow, not risk numbers. The analytics domain holds RiskRule, RiskException, RiskWorkflow, RiskTask and RiskConfig (spec paths `analytics/oversight/governance/v1/...`) plus ESG and Climate data. Risk outputs reach clients through Data Cloud. Woodhead (source 1), TS/.../01_...md:24: "The Aladdin data cloud ... takes all of that information that's generated through our analytics factory ... and pushes that into Snowflake."

**Smallest fix.** "...reached through APIs; BlackRock's public SDK names 11 domains, and more sit behind the client login."

### W4. The picture never shows where my code runs
**What a buyer reads.** The hosting row shows only BlackRock's clouds, so all building appears to happen inside BlackRock's hosting.

**Evidence**
- Exhibit 14 (same document): client applications "Run in the client's own environment, on the client's credentials".
- README:179: "AladdinSDK can run on a developer's local machine or in Aladdin Studio Compute sessions" (`local` is the default).

**Smallest fix.** Add a box "The client's own environment (local or own cloud)" at the left of the hosting row, or a one-line note.

### W5. Exhibit 4 gives no sign of maturity
**What a buyer reads.** "Read and write Aladdin data" and "Open-source Python library" sound production-ready.

**Evidence**
- 24 of the 54 public specs are labelled alpha and 6 beta (recomputed over specs: alpha 24, stable 23, beta 6, sunset 1).
- PyPI `aladdinsdk` is at 2.0.0b10, a beta (https://pypi.org/pypi/aladdinsdk/json, latest upload 2026-07-27). The plugins are 2.0.0b3.
- The four-eyes control's API is alpha (W1).
- Exhibit 5 shows this on the next page, but page 4 does not refer to it.

**Smallest fix.**
- In the APIs tile: "most public specifications are labelled alpha or beta (Exhibit 5)".
- In the SDK tile: "in beta (2.0.0b10)".

### W6. The AWS box drops the release's scope
**Evidence.** AWS release (source 21), Amazon press site, fetched 2026-10-20: "General availability for Aladdin Enterprise clients hosted in the United States is expected in the second half of 2026." The box says only "AWS option, announced". A non-US buyer will read it as applying to them. Nothing public says whether Studio, Data Cloud or Compute come along.

**Smallest fix.** "AWS option announced for US-hosted Aladdin Enterprise clients, H2 2026".

---

## NIT

- **N1. "Excel users building reports" sits in "Who builds" above the stack, as if Excel users build on Studio under the API controls.**
  - The Studio page names three personas, not four (https://www.blackrock.com/aladdin/platforms/products/aladdin-studio): "a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting".
  - The APIs page does list ATX among Studio resources, so the box is defensible.
  - Nothing public says ATX uses the Studio APIs. The ATX page claims "the full spectrum of Aladdin data, including analytics, trades, orders", which is broader than the public specs.
  - Fix: mark it "(via Aladdin Tools for Excel)".
- **N2. Exhibit 4 shows "Aladdin Compute" (offer) and "Studio Compute" (workspace) as if they were two things.** The sources do not separate them. README:179 says "Aladdin Studio Compute sessions"; the APIs page says "Aladdin Compute". Fix: "Studio Compute: sessions of Aladdin Compute".
- **N3. "Studio notifications" are messages my code sends; they are not Aladdin events.** README:587: "a Studio Notifications utility that can be used to programmatically send SMPT/Push notifications using the Studio Subscription and Notification APIs". Placed under the "Event-driven workflows" tile, a reader may take them for the event feed. Fix: "Email or push alerts a program sends to...".
- **N4. "BlackRock's applications" undersells them.** These are the Aladdin front-end apps that clients license too. Rosales, yt_oyqeCHFM5U4.m4a.ts.txt:24-25 / 01:53: "around 100 Aladdin front-end applications that thousands of people use every day", after "hundreds of clients globally". Fix: "Aladdin's applications (built by BlackRock)".
- **N5. The title "Where Studio sits in Aladdin" omits eFront, Aladdin Wealth and Preqin.** The AWS release defines Aladdin as "inclusive of the Aladdin platform, eFront, Aladdin Wealth, and Preqin". None of the 11 public domains covers them. Fix, in the note: "Shown: the Aladdin platform; eFront, Wealth and Preqin are not in the public specifications."
- **N6. "Each tool matches an Aladdin API" leaves out the agents.** Rosales 4:45-4:49: "the second onboarding path ... is the ability to spin up a custom agent". Fix: "tools map to production APIs; complex workflows are custom agents".
- **N7. Packaging is unclear.** OPINION, supported by BlackRock's own navigation. The Aladdin site lists "Aladdin Studio" and "Aladdin Data Cloud" as separate solutions (navigation on every product page fetched). Exhibit 4 puts Data Cloud inside Studio, so a buyer may assume that one licence covers both.

---

## Holds up

- **Spec ids.** "Every public specification's id starts agraph.<domain>": 54 of 54 have `x-aladdin-api-id` starting `agraph.` (recomputed).
- **Code-curious portfolio managers.** The phrase is verbatim on the Studio page.
- **Studio as "the developer and data layer".** This matches Woodhead's three pillars: APIs and events, Data Cloud, and developer tools and environments (01_...md:24).
- **Apps and Copilot.** "About 100 applications" and "Copilot inside them" match Rosales 01:53 and 02:34 ("embedded across all of those hundred front-end applications").
- **Azure today.** Microsoft Cloud blog (35): "all BlackRock's technology platform clients and services are hosted in the Azure cloud". The AWS box is honestly hatched and "announced".
- **Data Cloud on Snowflake, with Fivetran moving the data.** Fivetran blog: "ADC is supported by Fivetran for data movement and Snowflake as its cloud data platform".
- **SDK.** The SDK is open source (Apache License 2.0 in the repo LICENSE). The README covers login, retries and rate limits.
- **Order API.** OrderAPI is `stable`, and runCompliance does default to true.
- **Events.** "No event specification is public" is honest and correct.
- **Developer portal.** "Behind a client login" is correct.
- **Workspace items.** All seven workspace items trace to README or AdcDatasetAPI lines, with no invented "Space" box.

## Questions I would ask in the meeting (what the picture gets wrong or leaves out)

1. Do your ~100 apps and Copilot call the same APIs my code gets, at the same version? How many APIs sit behind the login beyond the 54 public specs, and is there a position API?
2. Can my code post an order with `runCompliance=false`, and who is allowed to? Is that logged? What happens under `complianceTimeout`?
3. Can I turn off API-key-plus-client-key and basic-auth access for my tenant, so that every call carries an OAuth scope?
4. Who in my firm can call `userGroupPermissions:batchCreate`? Is there four-eyes on entitlement changes, and is release of a Data Cloud dataset blocked until it is approved?
5. Which controls apply to Snowflake SQL (roles), the S3 buckets, the ADX SFTP/MQ loaders and ATX? Do bulk-loaded orders and trades go through compliance?
6. How do I get Aladdin data into my own Snowflake account or lake: share, extract or API? On which cloud and region, and with what egress cost?
7. Where does my code run, Studio Compute or my environment? What is the private network path? Is AWS hosting available outside the US, and does Studio come along?
8. What is the deprecation policy for alpha and beta APIs and the beta SDK? What SLAs and rate limits apply?
9. What is the event mechanism (transport, schema, delivery guarantees), given that no event spec is public?
10. Are there sandboxes and non-production environments with realistic data?
11. Can Studio reach eFront, Aladdin Wealth and Preqin data?
12. Are Studio, Data Cloud and Compute licensed together or separately?
