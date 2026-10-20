# Exhibit 4 truth check: claims 1 to 9 and 17

This was a read-only check. Nothing in the document was edited.

## How I checked

- **Specs [6].** I read all 54 `swagger.json` files in `scratchpad/unpacked/` (11 `asdk_plugin_*` 2.0.0b3 packages).
  - I counted them myself: 54 specs in 11 packages. Every spec has `x-access-level: "Public"`.
  - Stability is not uniform: 23 stable, 24 alpha, 6 beta and 1 sunset.
  - PyPI today still lists `asdk_plugin_trading` at 2.0.0b3 as its latest release.
- **SDK [29] and plugin builder [40].** I made fresh git clones into `ex4check/sdk` (HEAD c1c9f3c, Sep 20 2026) and `ex4check/pb` (HEAD 73df174, Jan 22 2026). Both READMEs match the `drift22` copies byte for byte.
- **Product pages [14, 30, 31, 32, 33].** I used the saved copies in `drift22/dl_a/`, reading both the text and the HTML.
- **[45].** I fetched this page live on Oct 20 2026 and saved it as `ex4check/dl/s45.html`.
- **[44].** I fetched it live. The response was a 302 to `aladdin-login.blackrock.com/oauth2/v1/authorize...`, and the final page is titled "Aladdin - Sign In".
- **[39], [42].** I used the saved copies `drift22/dl_a/job41.html` and `scratchpad/devrel_fetch/job41.txt` (the Built In Bristol copy).
- **[43].** I could not refetch it, because web.archive.org resets the connection and the live URL returns 404. I used the earlier saved copy `scratchpad/fc/r015_p.html.txt`, whose canonical link is the Snowflake powered-by page.
- **[38].** Medium returns a Cloudflare 403. I relied on the earlier archive receipt in `citecheck/cb07_receipts.txt`: "interact with curated Aladdin Graph APIs and ADC datasets". I did not re-verify it this time.
- **[28].** I used the saved copy `citecheck/web21/fivetran.html`.
- **[1], [41].** I used the transcripts in `/home/user/ai_game/blackrock-aladdin/04-transcripts/`.
- **Web searches.** I used 1 of the 15 allowed (AsyncAPI Aladdin). It found nothing.

---

## Verdicts

### 1. APIs: TRUE

**"Read and write Aladdin data." TRUE.**
- APIs page [30]: "Aladdin REST APIs allow you to take control of your data, granting read and write access to Aladdin data".
- Studio page [14]: "Retrieve, write, and modify data from across the Aladdin ecosystem".

**"Built on Aladdin Graph, BlackRock's firm-wide runtime for APIs and events." TRUE, with one wording note.**
- SDK README [29], L276: "OpenAPI generated python client code based on Aladdin Graph API's swagger specifications".
- Naik and Kalish [38] (archive receipt): "curated Aladdin Graph APIs".
- Job posting [39]: "Building solutions for BlackRock and over 200 institutions ... The team behind Aladdin Graph—enabling API‑first engineering through a schema repository, governance, and production runtime infrastructure for APIs and events."
- Wording note: "firm-wide" is not a word in any source. It is a fair reading of "for BlackRock and over 200 institutions", which is a team-level "We are:" bullet. The posting also says Graph covers more than a runtime: a "schema repository, governance, and production runtime infrastructure".

**"Every public specification's ID begins agraph.<domain>, for Aladdin Graph". TRUE.**
- All 54 Public specs have `x-aladdin-spec-id` and `x-aladdin-api-id` values that begin `agraph.`, followed by the domain, which matches the package. Example: `"x-aladdin-spec-id": "agraph.accounting.transactions.abor_lot.v1.AborLotAPI"`. There are 0 exceptions.
- What "agraph" stands for is stated most directly in the plugin builder [40], not in the specs. `asdk_agraph_plugin_builder.py` L112-113 says: "Given path to an Aladdin Graph swagger file ... Assumption here is x-aladdin-spec-id is of the format 'agraph.<domain>.<segment>.<api>.<VERSION>.<API_NAME>'".
- Within the specs, the closest link is OrderAPI: "postOrder is the agreed naming with Aladdin Graph team."

### 2. Event-driven workflows: TRUE (thin, but present)

**"Aladdin tells a program when something happens." TRUE.**
- Woodhead [1], Whisper transcript 05:25-05:27: "It exposes everything Aladdin knows how to do as a set of APIs, events".
- Job posting [42]: "Document event-driven workflows, including streaming APIs, webhook subscriptions, and real-time data integration patterns" and "event publishing/subscription models".
- Aladdin Risk page [31]: "concrete capabilities such as Aladdin Studio, APIs, and event-driven workflows".
- Caveat: Goel [41] frames this as a goal, not a current fact: "we really want to make every single event that happens in [Aladdin] available to you. So every single transaction ... should be available ... via an event, via an API." [42] was a job ad that was taken down after two days.

**"Events run on the same Aladdin Graph runtime." TRUE as a reading of [39].**
- [39]: "production runtime infrastructure for APIs and events."
- Caveat: the posting does not say that the client-facing Studio events in particular run on it. That part is inference.

**"No event specification is public". TRUE, within the corpus checked.**
- All 54 Public specs are Swagger 2.0 REST specs. None is AsyncAPI, and none has webhook or stream definitions.
- The plugin builder's `resources/swagger_plugin_bundles` holds only the 54 swagger files.
- The one web search found nothing.
- Adversarial caveat: the open-source SDK repo [29] publicly ships 4 more agraph specs:
  - `agraph.platform.studio.studio_notification.v1.StudioSubscriptionAPI` ("For creating and managing Aladdin Studio notification subscriptions.")
  - `StudioNotificationAPI`
  - `TokenAPI`
  - `TrainJourneyAPI`
- All four are marked `x-access-level: "Internal"`. They define `v1StudioNotificationEvent`, described as "the information about the event that triggers a Studio notification".
- They are REST notification APIs, not an event-stream spec, so the claim survives. But an insider could point at them.

### 3. Aladdin SDK: PARTLY

**"Open-source Python library". TRUE.**
- [29] LICENSE: "Apache License Version 2.0".
- README L3: "The goal is to make it easier for everyone to efficiently access and utilize Aladdin APIs and Data Cloud."

**"with typed clients for the APIs and Data Cloud". PARTLY. The word that goes beyond the source is "typed" as applied to Data Cloud.**
- The API client is generated and validated. README L276: "wraps over OpenAPI generated python client code". L282: "Input parameter validation using pydantic". It also offers "Response deserialization to codegen response objects".
- The Data Cloud client is not typed. README: "ADC (Snowflake) access is provided via the ADCClient. This is a wrapper around snowflake-connector-python or snowflake-snowpark-python". It is used as `adc_client.query_sql('SELECT * FROM "CASH_ENTRY" LIMIT 10')`, which is SQL strings and dataframes.
- What the source supports: a typed, generated API client and a Snowflake connection wrapper for Data Cloud.

**"with login, retries and rate limits built in". TRUE for the APIs. Only partly for Data Cloud.**
- README L284-288: "Authentication: Using Basic Auth or OAuth ... Retry mechanism - Rate limiting per API endpoint".
- `API.RATE_LIMITING.ENABLED` defaults to `true`.
- ADC has authentication ("'oauth' or 'snowflake_jwt'") and retries (`ADC.RETRY`). It has no rate limiting; rate limiting is API-only.

**"A BlackRock plugin builder generates its 11 plugin packages from the specifications". TRUE.**
- [40] README: "This project builds API bundle plugins for AladdinSDK using swagger specifications. Plugins are built via Github Actions based on specifications included in plugin directories".
- The README has 11 "### asdk_plugin_*" sections, and there are 11 bundle directories holding 54 swagger files.
- The SDK README L312-323 lists the same 11 packages.

### 4. Aladdin Data Cloud: TRUE

- Studio page [14]: "Aladdin Data Cloud (ADC) is a managed data-as-a-service offering that brings together Aladdin ... with Snowflake's data platform".
- Data Cloud page: "Leverage a managed investment data pipeline with preloaded Aladdin data".
- Fivetran [28]: "ADC is supported by Fivetran for data movement and Snowflake as its cloud data platform."
- Caveat: [28] is Fivetran's own August 2024 marketing blog. It describes Fivetran moving data "from a single source ... into a Snowflake landing zone, where we transform it using our enterprise data platform". Fivetran is the ingestion path, not the whole data flow.
- Woodhead [1] also says "We share data to hundreds of Snowflake accounts", which is Snowflake sharing, not Fivetran.

### 5. Aladdin Compute: TRUE, from a weak, dated source

- Snowflake partner page [43] (saved copy): "Aladdin Compute – a hosted analytics platform with ready to use python environments and automation tools."
- Caveats:
  - [43] is a third-party page archived in 2024. Its live URL now returns 404, and the Wayback Machine cannot be reached from here.
  - BlackRock has no Compute page today. `/aladdin/products/aladdin-compute` and `/aladdin/platforms/products/aladdin-compute` both return 404.
  - The "Aladdin Compute" link in the "Additional Aladdin Studio resources" block on [30], [32] and [33] points to the Studio home page: `href="https://www.blackrock.com/aladdin/platforms/products/aladdin-studio"`.

### 6. ATX: TRUE

- ATX page [32] meta description: "Aladdin Tools for Excel (ATX) is an Excel plugin that enables users to retrieve Aladdin data to build custom reports and run bespoke analyses."
- Body text: "Automate reports, streamline your workflows".

### 7. ADX: TRUE

- ADX page [33]: "Securely bulk transfer your data"; "automated data transfer to and from Aladdin"; "more than 40 standard XML, CSV, and JSON extracts"; "our 35 standard CSV loaders".
- Small caveat: the transport is "Secure File Transfer Protocol or IBM MQ". "File transfer" leaves out the MQ messaging route.

### 8. Developer Portal and Data Dictionary: PARTLY. The location of the contents is inferred.

**The items themselves are backed by the APIs page [30]:**
- "Dozens of Aladdin APIs available" (catalog).
- "developer guides".
- "Download Python Jupyter Notebooks, or cut and paste code samples".
- "Our Data Dictionary allows you to explore Aladdin data and search for the field definitions you need."

**"behind a client login" is backed by [44].** I fetched it live: it redirects with a 302 to `aladdin-login.blackrock.com` ("Aladdin - Sign In").

**What goes beyond the source:**
- No source says the catalog, the field dictionary, the notebooks or the samples sit inside the Developer Portal behind that login. [30] never names a portal.
- Only "guides" is tied to the portal. The UserAPI spec [6] links `apps/aladdin-developer-portal/#/guides/developer-guide`.
- [42] says only "discoverability and usability of content within the Aladdin Studio Developer Portal".
- The ADC dataset spec points at a different internal host for its data model: `https://dev.blackrock.com/adlvisualizer/?repositoryName=ADCDatasets`.

### 9. Governance: PARTLY. The quote is misapplied.

**"access management and usage monitoring". TRUE.**
- [45]: "Its centralized experience supports the building, configuration, and governance of Studio workflows, including access management and usage monitoring."

**"Data, tools, and governance support". PARTLY.**
- The Studio page [14] sentence describes all of Studio, not a governance component: "Aladdin Studio gives you the data, tools, and governance support to make Aladdin your own."
- Quoting "Data, tools, and governance support" as the description of a "Governance" tile pulls "data" and "tools" into governance.
- A better-fitting source is [43]: "Governance and administrative tools to control and monitor usage." That source is already in the note, cited for Compute.

### 17. The framing that all nine tiles belong to Aladdin Studio: TRUE. Every tile has a source, but the ATX and ADX ties are thin.

| Tile | Source tying it to Studio |
|---|---|
| APIs | [30]: "How can I use them in Aladdin Studio?". [14]: "Aladdin Studio APIs enable you to build your own solutions". [43]: "Aladdin Studio includes ... API surface to retrieve, write, and modify data". |
| Events | [1]: Studio "exposes everything Aladdin knows how to do as a set of APIs, events". [42]: "Aladdin Studio is transforming how developers ... extend the Aladdin platform through open APIs and event-driven workflows". |
| SDK | [42]: "documentation for Aladdin Studio's APIs, SDKs, and event streaming interfaces". [29]: "can run on a developer's local machine or in Aladdin Studio Compute sessions". [38] authors are Aladdin Studio staff. The note cites [42] only "for events and the portal", not for the SDK tie. |
| Data Cloud | [14] features ADC. [43]: "Aladdin Studio: Data and Developer platform including the Aladdin Data Cloud". The spec id `agraph.platform.studio.adc...` is described as "Used by Studio's ADC Admin Center". It is also in the related-links block on [30], [32] and [33]. |
| Compute | [43]: "Aladdin Studio includes ... Aladdin Compute". It is in the related-links block, whose link goes to Studio home. |
| ATX | Only the "Additional Aladdin Studio resources" heading on [30] and [33]. The Studio page [14] never mentions ATX. |
| ADX | Only the "Additional Aladdin Studio resources" heading on [30] and [32] ([33] spells it "Additional Aladdin studio resources"). The Studio page [14] never mentions ADX. |
| Portal and Dictionary | [42]: "Aladdin Studio Developer Portal". [30]: "Aladdin Studio documentation teaches you how Aladdin API requests are built". [43]: "Developer guides, templates, and documentation". |
| Governance | [14], [45]: "governance of Studio workflows". [43]. |

- The note says the APIs, ATX and ADX pages list Data Cloud, ADX, Aladdin Compute and ATX. That is accurate:
  - APIs page lists Data Cloud, ADX, Compute and ATX.
  - ATX page lists Data Cloud, ADX, APIs and Compute.
  - ADX page lists Data Cloud, ATX, APIs and Compute.
- Caveats:
  - A related-links heading is weaker than "part of".
  - The Aladdin Risk page [31] lists "Aladdin Studio, APIs, and event-driven workflows" side by side, not as parent and child.
  - BlackRock's site navigation puts "Aladdin Studio" and "Aladdin Data Cloud" as sibling products.

---

## Missing or misplaced (separate from the verdicts)

1. **Data Cloud is sold as its own product.** BlackRock's navigation lists "Aladdin Studio" and "Aladdin Data Cloud" as separate solutions, and ADC has its own product page and "Book a meeting". A go-to-market head will know whether ADC is licensed separately from Studio. Drawing it as just one Studio tile may read as wrong commercially, even though [43] says "including the Aladdin Data Cloud".
2. **"Aladdin Compute" looks like a retired or merged brand.** There is no BlackRock page for it (both candidate URLs return 404), and its link goes to Studio home. The SDK and specs call it "Studio Compute": the notification enum includes `STUDIO_NOTIFICATION_EVENT_TYPE_COMPUTE: Studio Compute`. The only description is a 2024 Snowflake page that is now dead.
3. **"Studio Developer" is BlackRock's current product name for the extensibility layer, and the exhibit never uses it.** Job posting R264530, posted Sep 09 2026 (`drift22/dl_a/job50.html`): "Studio Developer, Aladdin's platform for extending and automating workflows" and "the vision for Studio Developer as Aladdin's extensibility layer".
4. **Studio entities the specs reveal are absent.**
   - The Studio notification enums include "Studio Space" and "Aladdin Credit Management". Neither appears in the exhibit (this touches the workspace half, claims 10 to 16, which are not mine).
   - AdcDatasetAPI requires a "StudioAdmin" Aladdin permission type.
   - The platform domain publicly exposes PermissionAPI, UserGroupAPI and UserGroupMemberAPI.
   - These are concrete public evidence for the Governance tile that the note does not use.
5. **Woodhead's own structure is flattened.** Woodhead [1] describes Studio in three pillars: APIs and events; Data Cloud; developer tools and environments ("sandboxes, research environments"). The nine flat tiles hide that structure and give equal weight to ATX and ADX, which predate Studio.
6. **Spec maturity is not shown.** 31 of the 54 Public specs are alpha (24), beta (6) or sunset (1). Only 23 are "stable". An insider reading "APIs" as a mature surface may object.
7. **The spec count could be challenged.** The SDK repo publicly ships 4 more agraph specs, all marked Internal. "54 public" is right only if "public" means `x-access-level: Public`. All 58 still begin `agraph.`, so claim 1 holds either way.
8. **Goel's "investment automation" is not shown** ("build on top of [Aladdin] and rebalance ... overlay your own configuration and code"). Neither is the Studio page's "automate workflows" as a product capability.

## Non-TRUE items

- **3 (PARTLY).** "typed clients for the ... Data Cloud": the ADC client is a Snowflake connector wrapper using SQL strings, and rate limiting applies to the APIs only.
- **8 (PARTLY).** No source places the catalog, field dictionary, notebooks and samples inside the login-gated Developer Portal. Only guides are linked to the portal.
- **9 (PARTLY).** "Data, tools, and governance support" describes all of Studio, not a governance component. "access management and usage monitoring" is accurate.
