# Panel: developer relations (Exhibit 4 tested hardest; Exhibit 3 where it touches the APIs)

Reviewer stance: a developer-relations lead who has built developer portals. Check only. Nothing in the document was edited.

Short names for the evidence files used below:
- README = `scratchpad/readme.md`, which is byte-identical to `blackrock-aladdin/02-api-catalog/aladdinsdk_README.md` (checked with diff)
- CORE = `scratchpad/uncited/dl/aladdinsdk/aladdinsdk/api/codegen/...`, the core SDK's own built-in specifications, which ship in the repository that register entry 29 covers ("README and source")
- APIS page = `scratchpad/devrel_fetch/apis.txt`, text of https://www.blackrock.com/aladdin/platforms/products/apis fetched live on 2026-10-20
- Studio page = `scratchpad/devrel_fetch/aladdin-studio.txt`, from https://www.blackrock.com/aladdin/platforms/products/aladdin-studio, fetched live the same day

## BREAKS IT

None. I found no box that a source flatly contradicts. Every label can be traced to a source. The problems are in how the pieces are split, named and grouped.

## WEAKENS IT

### W1. "APIs (Aladdin Graph)" and "Event-driven workflows" are split into two tiles, but BlackRock describes Aladdin Graph as covering both APIs and events, firm-wide.
- Evidence (register 82, fetched live on 2026-10-20): https://careers.blackrock.com/job/new-york/associate-software-engineer-aladdin-graph/45831/100968495568 says "Building solutions for BlackRock and over 200 institutions ... The team behind Aladdin Graph—enabling API‑first engineering through a schema repository, governance, and production runtime infrastructure for APIs and events."
- The document already cites this posting on another page, for the "200 institutions" figure.
- So putting "Aladdin Graph" in brackets on the APIs tile alone implies two things:
  - that events are something other than Graph;
  - that Graph is a Studio component, rather than the firm-wide API and event layer that Studio exposes. Exhibit 3 places the "11 public API domains" in the shared-services band below Studio.
- A BlackRock engineer would notice this straight away.
- Smallest fix:
  - retitle the first tile "APIs" and add one line: "Built on Aladdin Graph, BlackRock's firm-wide runtime for APIs and events";
  - or merge the two tiles into "APIs and events (Aladdin Graph)" and keep "No event specification is public" as the second line.

### W2. Compute appears in both groups under two names, and nothing says it is the same thing.
- The upper group has the tile "Aladdin Compute: Hosted, ready-to-use Python environments". The lower group has "Studio Compute: Sessions where SDK code can run".
- Evidence:
  - README:179: "AladdinSDK can run on a developer's local machine or in Aladdin Studio Compute sessions."
  - Snowflake partner page (register 42, receipt in `scratchpad/citecheck/cb07_receipts.txt:54`): "Aladdin Compute – a hosted analytics platform with ready to use python environments and automation tools."
  - The project's own fact check, `blackrock-aladdin/05-fact-check/FACT_CHECK_briefing_and_what_it_does.md:123`: "the README says 'Aladdin Studio Compute sessions' while marketing says 'Aladdin Compute', so use both." This treats the two names as one product.
- The two groups suggest that a client gets the offers on top and a separate set of workspace parts below. A reader will therefore count two compute components.
- The same pairing runs through the whole lower list, and none of it is shown:
  - API tokens and applications belong to the APIs;
  - ADC Admin Center belongs to Data Cloud;
  - Studio Compute belongs to Aladdin Compute;
  - notifications are themselves an API (W5).
- Smallest fix:
  - change the lower line to "Studio Compute: Aladdin Compute as the SDK names it; sessions where SDK code can run";
  - optionally relabel the lower group "Where a client sets up the offers above, as the SDK files name it".

### W3. BlackRock's own list of Studio resources is shrunk to a footer, while the Compute tile rests on that same list.
- Evidence: the APIS page (lines 111 to 116) has a heading "Additional Aladdin Studio resources". Under it are "Aladdin Studio home", "Aladdin Data Cloud", "Aladdin Data eXchange (ADX)", "Aladdin Compute" and "Aladdin Tools for Excel (ATX)".
- This is the only BlackRock page that names "Aladdin Compute", and its link points back to the Studio page, not to a page of its own.
- The exhibit uses this list to give Data Cloud and Compute full tiles. It reduces ADX and ATX to "The APIs page also links ...", which reads as "linked from", not "listed by BlackRock as Studio resources".
- Exhibit 3 also names "Excel users building reports" as one of four builder groups, and those builders need ATX.
- The note's "BlackRock gives no count of pieces" is literally true, but BlackRock does give a list.
- Smallest fix:
  - reword the footer to: "BlackRock's APIs page also lists Aladdin Tools for Excel and the Aladdin Data eXchange as Studio resources";
  - or give ATX and ADX a slim seventh tile.
  - In the note, add: "The APIs page lists five Studio resources; the six tiles are my grouping."

### W4. The Aladdin SDK tile undersells the SDK: it leaves out Data Cloud access and the typed API clients.
- The tile says "Open-source Python library for login, retries and rate limits."
- Evidence:
  - README:3: "The goal is to make it easier for everyone to efficiently access and utilize Aladdin APIs and Data Cloud."
  - README:276: "`AladdinAPI` which wraps over OpenAPI generated python client code based on Aladdin Graph API's swagger specifications."
  - README:343: "ADC (Snowflake) access is provided via the ADCClient."
  - README also documents an `S3Client` (line 432) and Studio notifications (line 587).
- A developer reading "login, retries and rate limits" will picture a thin HTTP helper. In fact the SDK provides typed API clients and a Snowflake client for Data Cloud, which is half of its stated purpose.
- The plugin sentence is accurate. The plugin builder README (https://raw.githubusercontent.com/blackrock/aladdinsdk-plugin-builder/main/README.md:3) says: "This project builds API bundle plugins for AladdinSDK using swagger specifications."
- Smallest fix: "Open-source Python library: typed clients for the APIs and Data Cloud, with login, retries and rate limits built in. BlackRock's plugin builder generates its 11 plugin packages from the specifications."

### W5. The lower list calls the same object by two names, and the cited source does not use one of them.
- The Projects line says "OAuth applications". The next line says "API tokens and API applications".
- Evidence:
  - The README uses only "OAuth application" (README:258) and "Studio application" (in the ADC OAuth note). It never says "API application".
  - "API Applications" appears only in the core SDK's Studio Notification specification: `CORE/platform/studio/studio_notification/v1/studio_notification/swagger.json`, enum `v1StudioNotificationEventType`: "STUDIO_NOTIFICATION_EVENT_TYPE_API: API Applications". That specification is `"x-access-level": "Internal"`.
  - The note credits "the SDK README 29, for ... the lower group".
- Nothing in the sources says that an "API application" is the same thing as an "OAuth application".
- Smallest fix:
  - use one name, "OAuth applications", in both lines (the README's word);
  - or keep "API applications" and change the note to "the SDK README and source 29".

### W6 (Exhibit 3, side column). "A second approver: Dataset releases need a second check" rests on endpoints that the specification marks as BlackRock-internal and being deprecated.
- Evidence, from AdcDatasetAPI (`scratchpad/unpacked/.../AdcDatasetAPI/swagger.json`):
  - the state enum includes "STATE_REVIEW: In review state, dataset is ready for a 4-eyes check prior to release";
  - but POST `/adcDatasets:releaseAdcDataset`, POST `/adcDatasets`, PATCH `/adcDatasets` and `:reconcile` each say "This endpoint is intended for internal BlackRock use only and is in the process of being depreciated."
- So the four-eyes check is real. The column's title, "Controls built into the APIs", presents it as a control that clients get through the public APIs. That is a stretch.
- Smallest fix: "A second approver: in the Data Cloud dataset workflow, a release needs a second check (a step BlackRock runs)."

## NIT

### N1. Studio Space is missing as an item, although BlackRock's own enum puts it on a par with Project and Compute.
- Evidence: the CORE enum `v1StudioNotificationEventType` lists "Studio Compute", "API Applications", "Studio Space" and "Studio Project". It also lists "ACM: Aladdin Credit Management".
- This enum is the nearest thing to an official list of Studio console objects. It confirms three of the exhibit's names and adds Space.
- The build notes left Space out on purpose ("role not described"). That is defensible, but a BlackRock developer would expect it.
- Fix: add "Spaces: named in the SDK files as a level above or beside Projects; role not described", or leave it as is.

### N2. "Studio UI" is listed as a peer of things that live inside it.
- Tokens, applications, storage integrations and the ADC Admin Center are all set up in the Studio UI. README:89 says "API Token registered via Studio UI", and README:432 says "Create a Storage integration on Studio UI under a personal / shared project".
- Fix: put Studio UI first, as the container ("Studio UI, the console where the following are set up").

### N3. The heading "Inside a client's Studio workspace" uses "workspace" in the author's own sense.
- The README uses "workspace" only for storage: "Bucket assigned to user/project workspace" (README:162) and "Storage S3 workspace".
- No source says the ADC Admin Center is in a client's workspace. Its specification says only "Used by Studio's ADC Admin Center", and its write and release endpoints are BlackRock-internal (see W6).
- Fix: use the build notes' own wording, "Parts of Studio named in the public SDK files".

### N4. "Sign-in details for programs: a token, or an OAuth client ID and secret" simplifies the specifications.
- Evidence: every specification's `security` block pairs `APIKeyHeader` (`VND.com.blackrock.API-Key`) with each option: OAuth access code, OAuth client credentials, `X-API-Key`, or basic auth. See OrderAPI swagger.json, `security`.
- The README says the token is "Required only for Basic Auth" (README:89), where it is used together with a user name and password.
- So the "or" holds for the README but not for the specifications.
- Fix: "Sign-in details for programs: an API token with a user name and password, or an OAuth client ID and secret."

### N5. "No event specification is public" is slightly too broad.
- The core SDK ships a public-repository specification for subscribing to Studio events: `studio_subscription/swagger.json`, "Creates a Studio subscription for a user and Studio notification event". It is marked Internal, and it covers alerts to people, not business events.
- The job posting (register 41) describes "streaming APIs, webhook subscriptions" and "OpenAPI/AsyncAPI specs".
- Fix: "No AsyncAPI, webhook or streaming specification is public."

### N6. "Notebooks and samples, behind a client login" is partly untrue.
- The public SDK repository ships `resources/sample_code_snippets/SDK_Demo_template.ipynb`, `SDK_Demo_ADC_template.ipynb` and sample-call files (README:226).
- The portal's notebooks may be different ones, but the tile implies that none are public.
- Fix: "... behind a client login (the SDK repository has public demo notebooks)".

### N7. The Compute tile drops "automation tools" from the only description of Compute.
- Snowflake page (register 42): "ready to use python environments and automation tools".
- The README backs this up with scheduled runs: "scripts / scheduled jobs" (README:626).
- Fix: "Hosted, ready-to-use Python environments and automation tools."

### N8. Naming.
- BlackRock's pages call the APIs "Aladdin Studio APIs" (APIS page, and Studio page line 120: "Aladdin Studio APIs enable you to build your own solutions").
- The README writes "AladdinSDK" as one word.
- Neither is wrong as the exhibit has it, but "Aladdin Studio APIs" is the name a BlackRock reader will expect on the tile.

### N9 (outside Exhibits 3 and 4, but it is a developer-portal claim).
- The document says elsewhere that the 54 specifications can be seen "only by unpacking the 11 PyPI add-on packages".
- In fact the plugin-builder README links every specification on GitHub. For example, https://raw.githubusercontent.com/blackrock/aladdinsdk-plugin-builder/main/resources/swagger_plugin_bundles/trading/trading_order_management_order_v1_order_api.swagger.json returned HTTP 200 on 2026-10-20.

## Holds up

- **Every public specification's id starts `agraph.<domain>`.** All 54 public specifications carry `x-aladdin-spec-id: agraph.<domain>...`. So do the 4 core specifications. The 54 are exactly those marked `"x-access-level": "Public"`; the 4 core ones are marked "Internal". The count of 54 is right.
- **"Event-driven workflows" is BlackRock's own phrase.**
  - Aladdin Risk page (register 31, live): "Aladdin supports this through concrete capabilities such as Aladdin Studio, APIs, and event-driven workflows".
  - Job posting (register 41, live): "build, integrate, and extend the Aladdin platform through open APIs and event-driven workflows".
- **The Data Cloud tile.**
  - Studio page: "Aladdin Data Cloud (ADC) is a managed data-as-a-service offering ... with Snowflake's data platform".
  - Fivetran blog: "ADC is supported by Fivetran for data movement and Snowflake as its cloud data platform".
- **Open source.** The SDK's LICENSE is Apache License 2.0.
- **The 11 plugin packages generated from the specifications.** README:276 and the plugin builder README:3-6 both say so.
- **Developer Portal and Data Dictionary.**
  - APIS page lines 108-110 name the notebooks, code samples, guides and "Our Data Dictionary".
  - UserAPI swagger links "[Developer Guide]: apps/aladdin-developer-portal/#/guides/developer-guide".
  - Register 43 redirects to a login page.
  - The note honestly says that the APIs page does not link these.
- **The lower list's facts** each match the README word for word:
  - Projects are "personal / shared" (README:432);
  - OAuth applications sit "under a Project" (README:258);
  - S3 storage integration (README:162);
  - "Studio UI" (README:89);
  - Compute sessions (README:179);
  - notifications by "SMPT/Push" (README:587), with entity types USER, PROJECT and SPACE (CORE `v1StudioEntityType`, "the entity type of the notification receiver");
  - ADC Admin Center (AdcDatasetAPI: "Used by Studio's ADC Admin Center").
- **What the build notes left out.** Space has no box and no "hosted workspace" inference is made. Both are careful choices.
- **The split into two groups.** One group is what is marketed; the other is what the SDK files name. This is a useful idea that few outside readers could build. It needs only the cross-mapping in W2 so that it does not read as two separate inventories.
