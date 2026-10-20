# Exhibit 4 truth check: claims 10 to 16, plus the Compute inference

Read-only. Nothing was edited.

## Sources examined

- SDK [29]: clone at `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/drift22/sdk_b`. HEAD is c1c9f3c (Sep 20 2026). `git ls-remote` shows this is still the current GitHub HEAD, so the clone matches the register's "as of October 19, 2026".
- Specs [6]: `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/unpacked/`. There are 11 packages and 54 `swagger.json` files, which I recounted myself.
- Studio page [14]: saved text in `drift22/dl_a/p_aladdin-studio.txt`.
- APIs page [30]: saved copy in `drift22/dl_a/p_apis.html`.
- Snowflake partner page [43]: the live fetch from web.archive.org failed twice because the proxy reset the connection. I relied on the earlier receipt at `scratchpad/citecheck/cb07_receipts.txt:54,639`.
- 3 web searches and 1 WebFetch.

The Studio product page [14] contains none of the items in claims 10 to 16. It has no mention of a UI, projects, tokens, compute, storage, notifications or Admin Center. Each of these claims therefore rests only on the SDK [29] or the specs [6].

---

## Verdicts

### 10. "Studio UI: The screens where tokens, applications and storage are set up"
**TRUE.** Source: SDK README [29].
- L89: "API Token registered via Studio UI."
- L258: "Client ID and Secret can be sourced from Studio UI by creating a OAuth application under a Project."
- L432: "Pre-requisite: Create a Storage integration on Studio UI under a personal / shared project."
- "Screens" is the note's own word, and a fair one for "UI". README L384 adds that users authenticate to the ADC OAuth application "by logging into Aladdin Studio UI". So the UI is also where users sign in, not only where things are set up. This is not an error.

### 11. "Projects: Personal or shared, each holding OAuth applications and storage"
**TRUE, with one stretch.** Source: SDK README [29].
- L432: "under a personal / shared project".
- L258: "creating a OAuth application under a Project".
- L430: "an S3 integration in a Project".
- L162: "Name of Bucket assigned to user/project workspace".
- Stretch: "each holding" reads as though every project contains both. The source says only that each can be created under a project. The "personal / shared" wording comes from the storage sentence only. No source says OAuth applications can live in personal projects. This is minor.

### 12. "API tokens and OAuth applications: Sign-in for the APIs"
**TRUE.** Sources: SDK README [29] and specs [6].
- README L88–89: AUTH_TYPE `Basic Auth` / `OAuth`, and "API Token registered via Studio UI. Required only for Basic Auth".
- README L258: OAuth client ID and secret come from an OAuth application.
- Spec securityDefinitions (for example AdcDatasetAPI) list `APIKeyHeader` (`VND.com.blackrock.API-Key`), `ClientKeyHeader` (`X-API-Key`), `basicAuth`, `OAuth2AccessCode` and `OAuth2ClientCredentials`.
- Nuances an insider could raise (not a verdict issue):
  - (a) The token is not a sign-in on its own. Basic Auth also needs a username and password (README L90–93).
  - (b) OAuth applications are also used to sign in to Data Cloud, not only the APIs. README L381: "client environments where ADC OAuth is configured via Studio application". Token API spec info: "For pre-registered OAuth applications such as ADC Studio".

### 13. "Studio Compute sessions: Where Aladdin Compute runs SDK code"
**TRUE.** Source: SDK README and source [29].
- README L179: "AladdinSDK can run on a developer's local machine or in Aladdin Studio Compute sessions."
- `aladdinsdk/common/secrets/fsutil.py:29`: "in Aladdin Compute sessions to read secret files injected by Vault init container".
- `aladdinsdk/config/user_settings.py:27`: `CONF_RUN_MODE_ALADDIN_COMPUTE = "aladdin-compute"`.
- Caveats:
  - The README's permitted value for RUN_MODE is `compute`, but the code accepts only `local` / `aladdin-compute` / `test` (user_settings.py:173). The README also says the default is `local`, while `get_run_mode()` falls back to `aladdin-compute` (user_settings.py:233). These are faults in the source itself, not in the exhibit.
  - The code shows that Compute hosts more than SDK code: notebook sessions, detected through the `NB_USER` env var (user_settings_file_util.py:33, 140), and Streamlit/Dash apps (`COMPUTE_APP_TYPE`, local_token_server_client.py:29, 55–57). "Runs SDK code" is true but narrow.

### 14. "S3 storage integration: File storage for SDK code, set up in a Project"
**TRUE, with the wording "for SDK code" narrower than the source.** Source: SDK README [29].
- L430: "The S3 Storage client provides a simple way to interact with an S3 integration in a Project."
- L432: "Create a Storage integration on Studio UI under a personal / shared project. This will provide details for access key and bucket name."
- L160: "To be sourced from S3 Storage Integration in a Studio Project."
- The README describes the integration only from the SDK side, through the S3Client wrapper over boto3. Nothing makes the integration SDK-specific. L162 calls it the "Bucket assigned to user/project workspace".
- "File storage for SDK code" can also be misread as storage *of* code. The source says files are uploaded and downloaded (L441–445). In Compute, the credentials are injected at `/secrets/s3integration-creds-key.yaml` (user_settings.py:34).

### 15. "Studio notifications: Alerts sent through Studio's notification APIs"
**TRUE.** Source: SDK README and source [29].
- README L587: "AladdinSDK provides a Studio Notifications utility that can be used to programmatically send SMPT/Push notifications using the Studio Subscription and Notification APIs".
- Spec bundled in the SDK (`aladdinsdk/api/codegen/platform/studio/studio_notification/v1/studio_notification/swagger.json`), info: "For creating and managing Aladdin Studio notifications."
- Precision points:
  - These two APIs (`agraph.platform.studio.studio_notification.*`) are NOT among the 54 public plugin specs [6]. They ship only inside the core SDK, and both are labelled `alpha`.
  - The notifications are email (SMTP) or push, and a subscription is needed before sending (README L593–604).
  - The SDK's convenience wrapper tags every message as event type `STUDIO_NOTIFICATION_EVENT_TYPE_COMPUTE` (studio_notifications.py:204).

### 16. "ADC Admin Center: The screen for managing Data Cloud datasets"
**PARTLY.** Source: spec [6], `asdk_plugin_platform/.../platform/studio/adc/adc_dataset/v1/AdcDatasetAPI/swagger.json`.

What the source does say:
- info.description: "Manages Datasets in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center."
- v1State: "STATE_DRAFT: In draft state, dataset owners may update the dataset details in Admin Center" / "STATE_REVIEW: … ready for a 4-eyes check prior to release" / "STATE_RELEASED: … currently live in ADC Snowflake".
- Register operation: "Datasets are stored in STATE_RELEASED in ADC and indexed on Aladdin Studio. The use of this operation requires "StudioAdmin" Aladdin perm".

What goes beyond the source:
- "The screen": the spec never calls Admin Center a screen or UI. It calls it a consumer of the API with an "Admin Center workflow". Read it as a UI is a reasonable reading, but it is not stated.
- Placing it "Inside a client's Studio workspace" is not supported, and the spec partly cuts against it:
  - Four of the 10 operations (create, update, reconcile, release) say "This endpoint is intended for internal BlackRock use only and is in the process of being depreciated."
  - Filters return "dataset configurations across clients".
  - Notification emails refer to "a BlackRock managed pipeline".
  - The parts open to clients are narrower: register custom datasets with the StudioAdmin permission, plus get, filter, refresh and delete.
- "Managing … datasets" is too broad. The documented workflow is registration, 4-eyes review, approval and release of dataset definitions, with only the StudioAdmin permission tying any of it to client users.
- The spec is labelled `x-aladdin-api-stability: alpha`.

### Note's inference: "I read Studio Compute sessions as the SDK's name for Aladdin Compute."
**SUPPORTED, but the stated premise is slightly wrong.** The SDK does not use a separate name. It uses both names for the same run mode.
- README L179: "Aladdin Studio Compute sessions".
- fsutil.py:29: "Aladdin Compute sessions".
- user_settings.py:27: run mode `"aladdin-compute"`. user_settings_file_util.py:33: `"NB_USER"  # For Aladdin Compute run modes`.
- Notification enum (SDK-bundled spec): "STUDIO_NOTIFICATION_EVENT_TYPE_COMPUTE: Studio Compute".
- Within one repository, "Aladdin Compute" and "Studio Compute" name the same hosted session environment. The other descriptions fit this: hosted, secrets injected by a Vault init container, Jupyter user, Streamlit/Dash apps.
  - Snowflake [43], via earlier receipt: "Aladdin Compute – a hosted analytics platform with ready to use python environments and automation tools".
  - APIs page [30]: lists "Aladdin Compute" under "Additional Aladdin Studio resources".
- What is still unproven: no BlackRock *marketing* page says that "Studio Compute" equals "Aladdin Compute". The note should treat this as more than a personal reading: the SDK source calls the run mode "Aladdin Compute" itself.
- Unverified corroboration: a web search snippet attributes to an AI Summit New York speaker bio (Infant Vasanth) the statement that he leads the "Studio Compute Platform", described as BlackRock's analytics and automation platform. The page (https://newyork.theaisummit.com/speakers/infant-vasanth) now redirects to the speakers list, and I could not retrieve the text. Do not cite it.

---

## Not verdicts: what a Studio insider would say is missing or misplaced

1. **Studio Spaces are missing.** BlackRock's own enum (SDK-bundled notification spec) lists "Studio Space" alongside "Studio Project", "Studio Compute" and "API Applications". Entity types are USER / PROJECT / SPACE. An insider will notice a workspace list that names Projects but not Spaces.
2. **"Workspace" is not BlackRock's term for this level.** The only use in the sources is the S3 bucket "assigned to user/project workspace" (README L162). The heading "Inside a client's Studio workspace" is the note's own framing.
3. **Compute shown twice.** Tile 5 (Aladdin Compute) and item 13 (Studio Compute sessions) are the same environment, according to the SDK's own source. Without the inference line, a reader counts two compute products.
4. **Compute is more than SDK code.** It hosts notebooks and Streamlit/Dash apps, served through a gateway with a local token server (local_token_server_client.py:37–41). Items 13 and 5 both under-describe it.
5. **The OAuth application's role in Data Cloud is missing.** Item 12 says "for the APIs". The SDK fetches Data Cloud OAuth tokens through the Token API for a Studio-registered "ADC Studio" OAuth application (README L381–384; Token spec info).
6. **The notification APIs are not public specs.** Item 15 rests on two alpha specs that ship only inside the SDK, not among the 54 public specifications. The note's sourcing for item 15 is the SDK [29], which is correct. But item 1's "Every public specification's ID begins agraph.<domain>" covers 54 specs, and these two notification specs are outside that set.
7. **The ADC Admin Center may be at least partly a BlackRock-operated workflow** (see 16), so listing it as a client workspace screen may draw pushback.
8. **The Studio page [14] does not support anything in the workspace half.** Every item in 10 to 16 depends on the SDK repository or one alpha spec. None comes from BlackRock product marketing.

## Non-TRUE items
- 16 ADC Admin Center: PARTLY. "The screen" is not stated. Placement inside a client's workspace is unsupported, because the spec marks most write operations as internal to BlackRock and works "across clients".
- Inference (Studio Compute = Aladdin Compute): supported, but its premise is wrong. The SDK uses both names itself, so this is not "the SDK's name" for something else.
- TRUE with notes: 11 ("each holding"), 13 (README `compute` vs code `aladdin-compute`), 14 ("for SDK code" is narrower than the source).
