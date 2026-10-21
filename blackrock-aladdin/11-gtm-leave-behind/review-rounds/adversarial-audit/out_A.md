# Audit A: controls and the compliance finding

Auditor scope: the report's claims about API-level controls, the runCompliance finding, the controls specific to Copilot, and the central thesis. I did not edit the report.

## 0. What I verified myself, and how

| Artefact | What I did | Result |
|---|---|---|
| PyPI wheels | Re-downloaded `asdk_plugin_trading`, `asdk_plugin_compliance` and `asdk_plugin_platform` 2.0.0b3 into `audit/A_pypi/` and compared SHA-256 hashes with `scratchpad/pkgs/`. Unzipped them fresh into `audit/A_fresh/` and ran `diff -r` against `scratchpad/unpacked/`. | All three hashes match (trading `7d97ee85…fcbb`, compliance `fb52be2b…a0c`, platform `00621cac…ae5`). The unpacked trees are byte-identical. |
| SDK | Fresh `git clone` of blackrock/aladdinsdk (HEAD `c1c9f3c`, 2026-09-20) and blackrock/aladdinsdk-plugin-builder (HEAD `73df174`, 2026-01-22) into `audit/A_src/`. | The builder's `trading_order_management_order_v1_order_api.swagger.json` is identical to the wheel's OrderAPI spec. |
| Specs | Parsed all 54 `swagger.json` files with my own scripts (`audit/A_survey.py` plus inline scripts). | The counts are below. I re-derived 54 specs, 301 operations, 10 specs with an LRO endpoint and 35 LRO operations, and they match the report. |
| Transcript | Read `04-transcripts/part1-youtube-and-site/16_How_BlackRock_Built_Production_AI_Agents…md` (local Whisper base.en) and `04-transcripts/timestamped/yt_oyqeCHFM5U4.m4a.ts.txt` (a second machine transcript with timestamps). | Both are **machine transcripts**. I did not play the audio. The YouTube oEmbed for `oyqeCHFM5U4` resolves to "How BlackRock Built Production AI Agents for Asset Management with LangGraph \| LangChain Interrupt", channel LangChain. |
| Web | Fetched live `blackrock.com/aladdin/platforms/products/aladdin-copilot`, `aladdin-studio` and `apis` (HTTP 200) on 2026-10-21. Saved in `audit/A_web/`. | Quotes used below come from these live copies. |

I used no fc/, citecheck/, review-rounds or other project summaries as evidence.

---

## 1. The compliance finding: what runCompliance=false does

### 1.1 What the OrderAPI spec actually says (complete reading)

File: `asdk_plugin_trading/agraph/trading/order_management/order/v1/OrderAPI/swagger.json` (stable, `x-aladdin-spec-id` `agraph.trading.order_management.order.v1.OrderAPI`).

- `info.description`: "Filter, post or cancel orders. **An order is a directive from a portfolio manager to the trading desk** to execute a particular investment decision."
- Order-posting operations: `POST /order:post` (OrderAPI_PostOrder, returns `v1SinglePostOrderResponse`, `x-quota-limit` 3000) and `POST /orders:batchPost` (OrderAPI_BatchPostOrders, returns a long-running operation whose response type is `v1BatchPostOrdersResponse`, max 1,000 orders, `x-quota-limit` 250). Both take `postOrderConfig` → `v1PostOrderConfig`. The cancel operations (`/order:cancel`, `/orders:batchCancel`) have no compliance config.
- `definitions.v1PostOrderConfig`:
  - `whatIf` is **required**: "True to post orders in a what-if mode". Nothing else defines what-if mode.
  - `runCompliance` is optional: "**Default is true to run compliance on this post order request.**" No other text.
  - `complianceTimeout`: "The timer is set on the compliance run during order posting. If the non-zero time is reached and the run is not complete, **orders will be posted with the "Compl Pending" status set regardless of any violations** that may have resulted if the run was successful. Default is infinite…"
- `definitions.v1PostOrderResponse`: `complianceViolations` ("Compliance violations triggered by posting this order.") **alongside** `order` ("The order that was created").
- `definitions.v1Violation.description`: "Violation describes the **intraday and overnight** violation generated at time of the compliance breach". It has fields `violationOwner` ("team or group who owns the next step in resolving this violation"), `actionStatus`, `violationDisposition` ("Approved, Rejected, Manual etc."), `resolutionComment`, `modifier`, `program` ("Compliance engine that evaluated this violation") and `complianceSeverity` (WARNING, RESTRICTION, SILENT_ALARM, …).
- `v1Order.orderStatus` is read-only: "Open", "**Compl Pending**", "Authorized", "Active", "Expired", "Rejected", "Canceled", "Booked".
- `v1Order.authorizeTime` is read-only: "The **PM authorizes** the order… From the authorized PM order, the trader order is created." `activeTime`: "Time when the order was **activated by trader**." `assignedToStatus` takes values including HOLD and DNT ("Do not Trade"). `ownerType` is PM, TRADER or HYBRID.
- Security: both post operations require `trading.order_management.order.v1.Order:write` on the OAuth alternatives. The other alternatives, `APIKeyHeader+ClientKeyHeader` and `APIKeyHeader+basicAuth`, carry no scopes. **No field, scope or description ties runCompliance=false to any extra scope or permission.** The OrderAPI documents no Aladdin permission at all. Contrast the 15+ operations in other specs that state "Users needs to have permissions under permType='…'" (section 2.3).

### 1.2 What this establishes, and what it does not

- **Established.** Compliance runs on the posting request unless the caller sets `runCompliance=false`. When it runs, violations come back in the response together with the created order. The spec therefore implies that, at least in some cases, violations do not prevent creation. Exactly the same OAuth scope (`Order:write`) covers posting with compliance on or off.
- **Established.** There is a second documented route to an order posted without a completed compliance result: `complianceTimeout`. On timeout, orders are posted as "Compl Pending" "regardless of any violations". The report never mentions this.
- **Not established: skipped vs. deferred vs. run elsewhere.** The text says only "run compliance on this post order request". It does not say what happens when the order is later authorized, activated by a trader, or booked. Circumstantial evidence points to compliance runs outside posting: the violation definition says "intraday and overnight", LevelAPI "Retrieves start-of-day and intraday Compliance levels", the "Compl Pending" order state exists, and TradeAPI v2 has a read-only `compliancePending` flag on trades. Read "turn it off" as "turn off the check on this request", not "turn off compliance".
- **Other controls downstream of an order post** (from the spec): PM authorization and trader activation (the PM/Trader split model), hold or do-not-trade statuses, and violation ownership and resolution. In ComplianceRuleAssignmentAPI there is an optional `resolutionRequiresFourEyesApproval` flag on rule assignments ("By default it is false"). ViolationAPI lets a caller with `Violation:write` close a violation with a disposition through `/violation/{id}/resolutions:add`. The spec does not say whether the four-eyes flag is enforced on that path.
- **A gap in the report's "order to NAV" view.** TradeAPI v2 (alpha) `POST /trades:post` and `/trades:batchPost` accept trades with a `PostTradeConfig` that has **no compliance option** (`mode`, `overrideRelationships`, `overrideCharges`, …). The spec does not say whether compliance runs on direct trade posting. A caller with `Trade:write` can post trades without going through OrderAPI.
- **Permissions and scopes for runCompliance=false compared with the default.** The public spec establishes that the OAuth scope is the same. It establishes nothing about Aladdin user permissions for this flag. Because other specs in the same set do document per-operation Aladdin permissions, a server-side permission on this flag is plausible but undocumented.

### 1.3 Every place the report describes this, judged

**P2, Exec summary:** "Posting an order runs compliance by default. The caller can turn it off 6. Whether turning it off needs a separate permission is not public."
- Source: `v1PostOrderConfig.runCompliance` "Default is true to run compliance on this post order request."
- Verdict: **CORRECT**, with one ambiguity. "Turn it off" could be read as disabling compliance as a whole. "Not public" is accurate, but it understates what *is* public: the OAuth scope is identical.
- Strongest wording: "Posting an order runs compliance on that request by default. The caller can skip that run (runCompliance=false) with the same Order:write scope. The spec does not say whether an Aladdin permission governs this, or whether compliance runs again later."

**P2:** "Access is granted per API, to read or to write."
- Source: survey of the 54 specs. Read and write are split in 21 specs, 11 are read-only, 2 are write-only, and **17 use a single scope described as "This grants access to all endpoints in the … API"**. Three mix both styles. Examples of the single-scope specs: RestrictedAsset, PortfolioGroup, Strategy, AdcDataset, Broker, CounterPartySettlementInstruction, MiscellaneousCashflow and AborLot. Only the OAuth alternatives carry scopes at all. Client-key and basic-auth calls declare none.
- Verdict: **OVERSTATED.**
- Strongest wording: "With OAuth, access is granted per API; most APIs, though not all, separate read from write."

**P2:** "An AI tool calling these APIs would work under the same controls."
- Verdict: **DEFENSIBLE BUT UNCERTAIN.** Server-side controls apply to any caller, so the sentence is true in a trivial sense. "Same" lacks a referent, though, and the controls listed are partial. The sentence also leaves out that the most visible compliance control can be switched off by the caller.

**P3, Exhibit 2, step 2 "Compliance check":** "Who: No one … Runs automatically: runCompliance is on by default."
- Source: `violationOwner`, `resolutionComment`, `violationDisposition`, `resolutionRequiresFourEyesApproval`, ViolationAPI AddResolution.
- Verdict: **OVERSTATED / misleading.** The check runs without a person, but the spec shows people owning and resolving violations. "Runs automatically" holds only when the caller does not opt out and the run finishes before any timeout.
- Strongest wording: "Who: the compliance engine runs it; a named team owns and resolves any violation."

**P3, Exhibit 2, step 1:** "Test (whatIf) and compliance (runCompliance)."
- Verdict: **CORRECT.** Adding that whatIf is required would sharpen it.

**P4, Exhibit 3, side panel:** "Access set per API. Each API has its own OAuth scopes."
- Verdict: **CORRECT.** Every spec's scope names are unique to that API.

**P4, Exhibit 3:** "Posting an order runs compliance unless the caller turns it off, and returns any violations."
- Verdict: **DEFENSIBLE.** On a timeout, the order is posted "regardless of any violations", so the response may not carry the final result. In batch posts, violations come back through the LRO.

**P5:** "An order can be posted as a test (the whatIf setting)."
- Verdict: **DEFENSIBLE BUT UNCERTAIN.** "what-if mode" is not defined, and "test" is a reasonable reading.

**P5:** "A compliance check runs by default (runCompliance). The response lists any compliance breaches with the order."
- Verdict: **CORRECT.**

**P5:** "Ten specifications offer a way to track them, and 35 operations are marked long-running."
- Verdict: **CORRECT.** Recomputed: 10 specs, 35 `x-aladdin-lro` operations.

**P5:** "Compliance rule assignments move through review states before they are approved 6."
- Source: `enumsComplianceRuleAssignmentReviewState` (DRAFT, PROPOSED_READY_FOR_TESTING, PROPOSED_REVIEW_REQUIRED, …, APPROVED). However, `reviewState` is **not read-only** and sits in the POST/PATCH body.
- Verdict: **DEFENSIBLE BUT UNCERTAIN.** The spec lists the states but does not show the API enforcing the sequence.
- Strongest wording: "Rule assignments carry a review state, from draft through review to approved or rejected."

**P5:** "Every request carries an application key and a second credential … OAuth 2.0 token, a client key, or a user name and password."
- Verdict: **CORRECT.** All 301 operations list exactly four alternatives, each pairing APIKeyHeader with one of OAuth access-code, OAuth client-credentials, ClientKeyHeader or basicAuth.

**P5:** "With OAuth, access is granted per API and per action."
- Verdict: **OVERSTATED.** No scope is finer than read or write on a whole API. 17 specs grant one scope for all endpoints. "Per action" can be read as per operation, which is false: post and cancel share `Order:write`.

**P5:** "Developers get their OAuth client ID and secret from Studio's screens."
- Source: SDK README: "Client ID and Secret can be sourced from Studio UI by creating a OAuth application under a Project."
- Verdict: **CORRECT.**

**P12:** "Posting an order runs compliance by default. The caller can turn it off. Whether turning it off needs a separate permission is not public."
- Verdict: **CORRECT**, with the same caveats as P2.

**P12, Exhibit 14, "Controls in the API specifications":** "Access set per API / Approvals on record: Capital flows record who approved them / Compliance by default … Any violations are returned."
- Source: EnrichedCapitalFlow has `approverUserId`, `authorizerUserId`, `cancelApprover`, `creator` and a state machine Open → Authorized → Confirmed, plus cancel-request and authorize-cancel.
- Verdict: **CORRECT** as far as it goes. It omits the stronger layer: Aladdin user permissions (section 2.3).

**P13, Exhibit 15 #2:** "under the same permissions, compliance checks and guardrails Copilot uses."
- Verdict: **UNSUPPORTED as a description of the present.** Copilot's guardrails are not exposed (section 3). No source shows Copilot posting orders or using order compliance checks. The talk's examples are read queries, such as "how many shares I can buy to be compliant" at 13:19. As a *proposal* it is fine, but it presupposes that BlackRock exposes things it does not expose today.

**P13, Exhibit 15 #4:** "Posting an order runs compliance by default, unless the caller turns it off. An order can also be posted as a what-if test. In the demo, a portfolio manager approves…"
- Verdict: **CORRECT.** The spec's PM-authorization model (`authorizeTime`) supports a PM-approval step.

---

## 2. Controls demonstrably in the public API layer

Would a client calling the API with its own credentials be subject to each control? Answers come from the specs and SDK.

| Control | Evidence | Granularity | Client caller subject to it? |
|---|---|---|---|
| Application key on every call | `APIKeyHeader` (`VND.com.blackrock.API-Key`) in all four alternatives of all 301 operations | per app | Yes |
| Second credential | OAuth access-code (user), OAuth client-credentials (app), `X-API-Key` client key, or HTTP basic (user and password). The SDK supports OAuth (`refresh_token` / `client_credentials`) and Basic Auth (`aladdinsdk/config/user_settings.py`). The code defaults to OAuth (`get_api_auth_type`), though the README table shows `Basic Auth`. | n/a | Yes, but **the caller chooses the scheme**, and only OAuth carries scopes |
| OAuth scopes | Per-API scope names. 21 specs split read/write, 11 read-only, 2 write-only, 17 single all-endpoints scope, 3 mixed. All "non-sensitive read/write" (the boilerplate covers Order:write and Violation:write too). The SDK requests per-endpoint scopes from the spec (`aladdinsdk/api/client.py` `_fetch_scopes_from_swagger`; env switch `AGRAPH_SCOPES_ENABLED`). The README says selected scopes "must be a subset of scopes setup for the app in Studio UI". | per API, at best read/write; **never per operation, per parameter or per portfolio** | Yes, on OAuth paths. The scope ceiling is set on the OAuth app in Studio |
| Aladdin user permissions (entitlements) | PermissionAPI: a permission has `functionalArea`, `action` ("View, Modify, Delete"), `permGroup` (PORTFOLIO / PORTGROUP scope) and `sensitivityGrade` (LOW…ULTRA). Permissions are applied to user groups, not users. Operation descriptions state prerequisites, for example "permType='brkrSettlm'" (CPSI), "brkrMaint", "brkrDskCon", "brkrAka", "asContMOD", "PERMS_GROUP_CREATE or MOD_PERMS", "StudioAdmin … DATACLOUD". EnrichedCapitalFlow: "User needs standard API permissison ALADDIN_API_USER … and standard newcash permissions … based on business workflow and user's role". MiscellaneousCashflow: permissions are in Release Notes "on Studio". | per function, per action, **per portfolio or portfolio group** | Very likely yes. The descriptions are written as prerequisites on the calling user. The specs label the platform APIs "not intended to be used for Authorization", so enforcement is implied, not specified. **The report omits this layer, which is the most granular control in the public record.** |
| Identity types | UserAPI `enumsUserType`: CLIENT_EMPLOYEE, PROVIDER, SYSTEM, BLK_EMPLOYEE; "bot accounts granted access to Aladdin" | per user | Yes. An AI agent would run as a user or a system account |
| Compliance on order post | runCompliance (default true), complianceTimeout, violations in response | per request, caller-controlled | Yes, unless the caller opts out |
| What-if posting | whatIf (required) | per request | Yes |
| Order workflow | statuses Open / Compl Pending / Authorized / Active / Booked, PM authorizes, trader activates, Hold/DNT | per order | Yes. Posting an order does not trade |
| Approvals and audit fields ("who approved") | EnrichedCapitalFlow approver, authorizer and cancel approver. RiskRule `finalSignOffAuthor` ("The user who approved the Rule"). Valuations `pmgApprover`. CPSI `settlementInstructionReviewer`. BrokerConfirmRouting `reviewerSignRequired`. Orders and violations carry `modifier` and `modifyTime`. AuditAPI `/entityRevisions:filter` (broker entities only). | per record | Yes |
| Four-eyes | AdcDataset `STATE_REVIEW`: "ready for a 4-eyes check prior to release". Rule assignment `resolutionRequiresFourEyesApproval` (default false) | per dataset or assignment | Yes, where configured. Enforcement on API paths is not specified |
| **Caller-set approval bypass flags** | CPSI create `autoApproved`: "creation supports two ways - unapproved and approved". OrderAPI `runCompliance`. RestrictedAsset (a trading safeguard: "used [to] prevent assets from being traded") is writable under one all-endpoints scope | per request | Yes. The caller chooses |
| Long-running operations | 10 specs, 35 operations. SDK polls (`api.lro.status_check_interval` default 10 s, timeout 300 s) | n/a | Yes. This is mechanics, not a control |
| Request tracing | All 301 operations require `VND.com.blackrock.Request-ID` (UUID) and `Origin-Timestamp` headers | per request | Yes |
| Rate limits | All 301 operations carry `x-quota-limit` (e.g. order post 3000, batch post 250) | per operation | Yes |
| Optimistic concurrency | ViolationAPI requires `modificationTime` "to validate that the violation being updated has not already been altered by someone else". Capital-flow transitions require `version` | per record | Yes |

Oddity worth knowing: all 54 specs carry `tags: [{"name": "Access.Internal"}]` and `x-access-level: "Public"`. AdcDataset write operations say "intended for internal BlackRock use only … Please refrain from using unless authorized". I would not build an argument on the tag either way.

---

## 3. Controls specific to Copilot (Rosales and Valdez, machine transcript)

| Control (report wording) | Transcript (timestamped file) | Verdict | Exposed to API callers? |
|---|---|---|---|
| Tool ownership and user-group access: "The team that owns each tool sets which user groups can use it" (P12) | [06:51–06:58] "they have complete control over which environments this plug-in is enabled in which user groups have access to this and even which Aladdin apps can even access these plugins" | CORRECT | **No.** The plugin-to-group mapping lives in Copilot's registry. Aladdin user groups themselves are exposed (UserGroupAPI), and so are Aladdin permissions |
| Each tool maps to a production API (P2, P9, P12, Ex. 14) | [04:31–04:39] "define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production". The second path is custom agents | DEFENSIBLE for "tool" (not "agent"). It does **not** establish that these are the same APIs as the 54 public specs. The report's P9 rightly calls this an inference ("So I infer"), but Ex. 14's title states it as fact | n/a |
| Input guardrails: off-topic and PII (Ex. 14) | [06:09] "input guard real node"; md transcript: "find off topic and toxic content… identify all of the relevant PII" | CORRECT | No |
| Filtering and access-control node, 20–30 tools shortlisted (Ex. 11) | [06:38], [07:22] | CORRECT | No |
| Planning loop with GPT-4 function calling (Ex. 11) | [07:34] "iterate over a planning and action node" | CORRECT | No |
| Output guardrails: hallucination and domain checks (Ex. 11, 14) | [07:48]; [09:33] "output guard rails custom to our domain and hallucination checks" | CORRECT | No |
| LLM judges test every system prompt "daily and on every change" (Ex. 14); "Copilot's guardrails are tested daily" (P12) | [10:57–11:12] "LLMs as a judge… we do this for every system prompt… It runs every day. It runs on every PR". [13:51] end-to-end routing tests "every day every night" | Ex. 14: CORRECT. P12: DEFENSIBLE BUT UNCERTAIN, because what is tested daily is the system-prompt behaviours and end-to-end routing, of which the guardrails are part | No |
| Calls made "on behalf of the user", respecting app settings | [06:01] "preferences as we make all these calls on behalf of the user" | Not in the report, and it helps the report: it suggests Copilot's API calls carry the user's identity and so the user's Aladdin permissions. This is inferred, not stated | n/a |
| Ground-truth end-to-end tests supplied by plugin owners | [12:46–13:28] | Not in the report | No |
| Product page: "Will not give investment advice…", "content filtering and parameters to limit risk of hallucination", "permission-dependent access to insights" | live Copilot page, 2026-10-21 | CORRECT as quoted | No (except that the underlying permissions are Aladdin's) |

Two facts matter for the thesis:

- **No public source shows Copilot taking write actions.** The page describes "surfacing answers" and "access to insights". The talk's examples are exposure, buyable quantity and cash, all reads. Valdez says they use a supervisor pattern, "hopefully next year we are here doing autonomous agents" [08:31–08:36]. None of Copilot's published controls covers approval of an action.
- **Copilot is a client product, not only BlackRock's own business.** The page says "now available to all Aladdin clients", and [09:07] says Copilot is deployed to "all our clients". Exhibit 14's label "BlackRock's own use" is therefore imprecise.

---

## 4. What would need to be built or exposed for an external AI agent to work under equivalent controls

1. **A first-party agent connection** (MCP server or similar) bound to an Aladdin identity, ideally OAuth access-code so that it acts as the user with that user's Aladdin permissions. Today none is published. The only sign is a job posting, which the report correctly flags.
2. **Finer-grained authorization than read/write per API.** This means per-operation scopes (post vs cancel), a separate entitlement for `runCompliance=false`, `complianceTimeout` and `autoApproved`-type flags, and portfolio-scoped limits that an agent's token cannot exceed. Aladdin permissions already have portfolio and action scope, so this mainly needs exposing and documenting.
3. **Server-enforced human approval for agent-originated writes.** Examples: force whatIf, or force an "Open" status that requires PM authorization, for system or agent identities. Enforce four-eyes on violation resolution and rule-assignment approval through the API.
4. **Agent identity and audit.** A distinct user type or tag for agent calls, so that `modifier`, `orderSource` and `raiser` show "agent X on behalf of user Y". Request-ID headers exist, but nothing marks an agent.
5. **Copilot-equivalent guardrails as a service**: input moderation and PII handling, tool filtering by user group, and output checks. Alternatively, publish the plugin registry model so that clients can register their own agents under the same access control.
6. **Documented compliance semantics.** Whether compliance re-runs at authorization or activation, whether RESTRICTION-severity violations block, and what direct TradeAPI posting does about compliance.
7. **Event APIs**, so that an agent can react to state changes. No event spec is public, as the report says.
8. **Public documentation of the permission model and release notes** that today sit behind the client login (MiscellaneousCashflow points to "Release Notes … on Studio").

---

## 5. The central thesis

Cover, P2 and P12: "Clients' AI tools could act on Aladdin under the same controls BlackRock uses for its own business."

- **What the evidence supports.** (a) The public write APIs (orders, trades, rule assignments, capital flows and more) apply server-side controls to any caller: authentication, OAuth scopes, Aladdin user permissions, compliance on order post by default, workflow states and approval records. An AI agent holding a user's credentials would inherit those, exactly as a script would. (b) BlackRock runs an AI assistant, Copilot, over production Aladdin APIs with additional AI-specific controls.
- **Where it goes beyond the evidence.**
  1. "The same controls BlackRock uses for its own business" merges two different sets. The API-layer controls are what a client caller gets. Copilot's AI controls (guardrails, tool access by user group, LLM-judge testing) are internal and not available to client tools. The report concedes this on P12 ("BlackRock would have to open its controls to tools it did not build"), and that concession contradicts the unqualified cover line.
  2. No public source shows BlackRock's own business, or Copilot, *acting* (posting orders) through AI. P2 says "BlackRock's advantage is that it already runs its own business this way", in a paragraph about AI tools that act. That is **unsupported**: Copilot is shown answering questions.
  3. No public source shows that BlackRock's own investment teams run on the client-facing Studio APIs and their OAuth scopes. Copilot uses "an existing Aladdin API already out in production", and identity with the 54 public specs is the report's own inference (P9).
  4. The headline compliance control is caller-optional (`runCompliance=false`, and also `complianceTimeout`), with the same scope either way. That weakens "same controls" as a safety claim for autonomous callers, and the report itself says the permission question is not public.
- **Verdict: OVERSTATED.** It is not false as a possibility ("could"), but it is presented on the cover as a finding of "what public sources show".
- **Strongest wording the evidence supports:** "Aladdin's public APIs already let client code write (post orders, assign compliance rules) under server-side controls: per-API OAuth scopes, Aladdin user permissions, and compliance checks on orders by default, which the caller can turn off. A client's AI tool using these APIs would be subject to the same API controls as any other client program. BlackRock's own AI assistant, Copilot, adds AI-specific controls on top (guardrails, per-group tool access, daily tests), but those are not exposed to client tools, and nothing public shows Copilot taking actions."

---

## 6. Genuine mistakes vs. reasonable hypotheses

**Factual or technical errors, fixable from the public specs:**
- "Access is granted per API, to read or to write" (P2) and "per API and per action" (P5). 17 of 54 specs use one all-endpoints scope, and nothing is per operation.
- Exhibit 2's "Who: No one" for the compliance check. The spec has violation owners, resolution and an optional four-eyes flag.
- "BlackRock … already runs its own business this way" (P2), in the context of AI tools that act. No source shows AI acting.
- Exhibit 14's title, "Copilot and client code share Aladdin's APIs and controls", states as fact what P9 calls an inference. It also implies that Copilot's controls are shared.

**Omissions that a technical reader at BlackRock would notice:**
- `complianceTimeout`, which posts as "Compl Pending" "regardless of any violations".
- The Aladdin permission layer (portfolio- and action-scoped, documented per operation in several specs). This undersells BlackRock's controls.
- TradeAPI direct posting with no compliance option.
- CPSI's caller-set `autoApproved` flag.
- That `reviewState` on rule assignments is writable.

**Reasonable hypotheses, labelled as such or acceptably hedged:**
- Copilot and Studio use the same APIs (P9, labelled "I infer").
- What-if equals a test post.
- Risk teams would need a person to approve each action (P12, "likely").

---

## Top vulnerable statements

**1. P2, Exec summary: "BlackRock's advantage is that it already runs its own business this way."** (Context: "Aladdin will not be alone in letting AI tools act.")
- Source: the Copilot page says Copilot surfaces "answers" with "permission-dependent access to insights". The talk's examples are read queries. Valdez [08:31–08:36]: "hopefully next year we are here doing autonomous agents".
- What it establishes: BlackRock runs an AI assistant over production APIs.
- Inferred beyond it: that AI already *acts* inside BlackRock's business.
- Verdict: **UNSUPPORTED.**
- Strongest wording: "BlackRock already runs an AI assistant, Copilot, across about 100 Aladdin applications, calling production Aladdin APIs as tools."

**2. Cover, P2 and P12: "Clients' AI tools could act on Aladdin under the same controls BlackRock uses for its own business."**
- Source: API-layer controls in the specs. Copilot-only controls in the talk. P12 itself: "BlackRock would have to open its controls to tools it did not build."
- What it establishes: client tools would get the API-layer controls.
- Inferred beyond it: equivalence with BlackRock's internal AI controls, and that BlackRock's business uses the same API controls.
- Verdict: **OVERSTATED.**
- Strongest wording: "Clients' AI tools could act on Aladdin through the same public APIs and API-level controls as any client program. Copilot's AI-specific controls would have to be opened to them."

**3. P2: "Access is granted per API, to read or to write"; P5: "With OAuth, access is granted per API and per action."**
- Source: the 54 specs. Read/write split in 21, read-only in 11, write-only in 2, **one all-endpoints scope in 17** (e.g. "This grants access to all endpoints in the portfolio.configuration.restricted_asset.v1.RestrictedAsset API"), mixed in 3. No operation-level scopes: `/order:post` and `/order:cancel` both need `Order:write`. Client-key and basic-auth alternatives carry no scopes.
- What it establishes: per-API scopes, often split by read and write.
- Inferred beyond it: universal read/write separation, and per-action granularity.
- Verdict: **OVERSTATED.**
- Strongest wording: "With OAuth, each API has its own scopes, and most separate read from write. Finer control comes from Aladdin user permissions, which several specs document per operation."

**4. P3, Exhibit 2: Compliance check, "Who: No one … Runs automatically: runCompliance is on by default."**
- Source: OrderAPI `v1Violation.violationOwner` ("team or group who owns the next step in resolving this violation"), `violationDisposition`, `resolutionComment`. ComplianceRuleAssignment `resolutionRequiresFourEyesApproval`. ViolationAPI AddResolution. `complianceTimeout`.
- What it establishes: the check is automatic by default, but violations are handled by people and the check can be skipped or time out.
- Inferred beyond it: no human role, and an unconditional automatic check.
- Verdict: **OVERSTATED.**
- Strongest wording: "The compliance engine runs on each order post unless the caller opts out. A named team owns and resolves any violation."

**5. P2 and P12: "The caller can turn it off. Whether turning it off needs a separate permission is not public."**
- Source: `runCompliance` "Default is true to run compliance on this post order request". Both post operations require the same `Order:write`. No permission is documented on OrderAPI. `complianceTimeout` posts "regardless of any violations". Violations are described as "intraday and overnight".
- What it establishes: compliance on that request can be skipped with the same scope, and later runs are undocumented.
- Inferred beyond it: only an ambiguity. A reader may take "turn it off" to mean that compliance is disabled, and the report omits the timeout route and the identical-scope fact.
- Verdict: **CORRECT but incomplete.** It is the statement most likely to be probed by a BlackRock technologist.
- Strongest wording: "A caller can skip the compliance run on an order post (runCompliance=false), or cap it with a timeout after which the order posts as 'Compl Pending' regardless of violations. Both need only the standard Order:write scope. Whether an Aladdin permission restricts this, and whether compliance runs again later, is not public."
