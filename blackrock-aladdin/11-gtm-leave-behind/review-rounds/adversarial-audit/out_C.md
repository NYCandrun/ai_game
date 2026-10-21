# Agent C audit: the API inventory and the trade workflow

Report audited: "Aladdin Studio from the outside" v23 (PDF pages 2 to 5 and 12 to 14). I did not edit the report.
All evidence below comes from primary artifacts I fetched or opened myself in this task. I did not use the fc, citecheck, break34, drift22/out_*, compendium or review-rounds material.

## 0. What I used, and how I made sure it was genuine

| Artifact | How I got it | Check |
|---|---|---|
| 11 wheels `asdk_plugin_*-2.0.0b3` | `scratchpad/pkgs/`, unzipped fresh into `scratchpad/audit/unz_C/` (I did not use the earlier `unpacked/` tree) | I re-downloaded 4 wheels from PyPI (`pip download ... ==2.0.0b3 --no-deps`) into `scratchpad/audit/dl_C/`: trading, compliance, accounting, investment_operations. Their SHA-256 hashes match the local copies byte for byte (for example trading `7d97ee85c4d4…`, compliance `fb52be2bf089…`, accounting `b921b73a10a6…`, investment_operations `4e905d73ba94…`). The first 12 hex digits of the PyPI JSON digest match all 11 local wheels. |
| PyPI release history | `https://pypi.org/pypi/asdk_plugin_<x>/json`, queried 2026-10-21 | All 11 packages have exactly 3 releases (2.0.0a2, 2.0.0b2, 2.0.0b3). **2.0.0b3 is still the latest**, uploaded 2026-01-22 and not yanked, so no newer version changes the counts. The core `aladdinsdk` is at 2.0.0b10. |
| Plugin builder | fresh `git clone https://github.com/blackrock/aladdinsdk-plugin-builder` → `scratchpad/audit/builder_C` (HEAD 73df174, 2026-01-22, "Jan 2026 Plugin Updates") | It holds 54 `*.swagger.json` files under `resources/swagger_plugin_bundles/`, **JSON-identical to all 54 in the wheels**. `.github/workflows/build-publish.yml` publishes `asdk-plugin-${{matrix.plugin}}` to PyPI using secret `BLK_PYPI_ALADDINSDK`. PyPI metadata names no author, so the attribution to BlackRock rests on this repo. |
| Core SDK | fresh `git clone https://github.com/blackrock/aladdinsdk` → `scratchpad/audit/sdk_C` (HEAD c1c9f3c, 2026-09-20) | Used for the README, the LRO polling code and the 4 core utility specs. |
| Transcripts | `/home/user/ai_game/blackrock-aladdin/04-transcripts/` | Sources 27 and 26 are **machine (Whisper) transcripts**. Source 10 uses published captions and source 22 a published transcript. I did not play any audio. |
| Fivetran blog (source 28) | live `curl`, 2026-10-21 | quoted below |

Scripts (all run with `python3 -I`) are in `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/scripts_C/`: `count.py`, `lro.py`, `lro2.py`, `security.py`, `positions.py` (output in `positions_out.txt`), and `inventory.json` (the per-spec inventory).

---

## 1. Reproducing the counts

**Counting rule.** A "specification" is one `swagger.json` file in a wheel. An "operation" is one key under `paths.<path>` whose name is one of get, put, post, delete, patch, head or options (non-method keys such as `parameters` are excluded; none exist here). A "domain" is the second segment of `info.x-aladdin-api-id` (`agraph.<domain>.…`). The stability label is `info.x-aladdin-api-stability`.

`count.py` output (verbatim, trimmed):
```
specs 54 packages 11
swagger versions Counter({'2.0': 54})
access level Counter({'Public': 54})          # top-level x-access-level
total ops 301
method counts Counter({'post': 190, 'get': 81, 'patch': 18, 'delete': 11, 'put': 1})
id prefix agraph. all? True True              # x-aladdin-api-id and x-aladdin-spec-id
domains from id [...] 11
pkg==domain? True
stability Counter({'alpha': 24, 'stable': 23, 'beta': 6, 'sunset': 1})
domain                   specs ops alpha beta stable sunset
investment_operations       15  74     9    4      2      0
analytics                    9  53     0    0      8      1
investment_research          5  41     5    0      0      0
platform                     6  29     2    0      4      0
portfolio_management         4  28     1    0      3      0
portfolio                    3  23     1    0      2      0
data                         1  15     0    0      1      0
trading                      2  14     1    0      1      0
compliance                   4   9     3    0      1      0
accounting                   4   8     2    2      0      0
clients                      1   7     0    0      1      0
distinct (spec,method,path) 301 ; operationIds 301, all distinct
```
Other counting rules give the same 301: distinct operationIds, and distinct (basePath + path, method) pairs.

| Claim (page) | My result | Verdict |
|---|---|---|
| "54 API specifications" in "11 public Python plugin packages" (p2, p3, p5, p13) | 54 specs in 11 packages; every spec carries `x-access-level: "Public"` | CORRECT |
| "301 public API operations" (p5) | 301 | CORRECT |
| "11 domains", "span 11 domains and 11 PyPI packages", "Domain names are BlackRock's own, taken from each specification's id" (p4, p5) | 11 distinct id domains, and each package maps one-to-one to a domain | CORRECT. The display names, such as "Investment operations", are humanised forms of `investment_operations`. |
| "Two domains hold 127 of the 301" (Exhibit 5 title) | 74 + 53 = 127 | CORRECT |
| Exhibit 5, every per-domain cell (specs, operations, alpha, beta, stable, sunset) | all match; the totals 54/301/24/6/23/1 match | CORRECT |
| Exhibit 5, "Largest APIs by operations" | All names match the API class names, in descending order. There are two ties: CouponReset and Broker both have 7 (the report lists CouponReset), and UserGroupPermission and UserGroupMember both have 3 (the report lists UserGroupPermission). | CORRECT, with arbitrary tie-breaks (cosmetic) |
| "Each specification carries one stability label: alpha, beta, stable or sunset" (p5) | Each of the 54 has exactly one, drawn from those four values | CORRECT |
| Exhibit 2 labels: OrderAPI v1 stable, ComplianceRuleAPI alpha, ViolationAPI v1 alpha, TradeAPI v2 alpha, AborLotAPI v1 alpha, ValuationsAPI v1 beta | all match `info.x-aladdin-api-stability` | CORRECT |
| "The core aladdinsdk package adds four utility APIs (token, subscription, notification and a demo), not counted here" (p5) | `sdk_C/aladdinsdk/api/codegen/codegen_allow_list.yaml` lists StudioNotificationAPI, StudioSubscriptionAPI, TokenAPI and TrainJourneyAPI (the "Demonstrate feature of Aladdin Graph services using train journeys") | CORRECT. They add 25 operations, which the report rightly excludes. |
| "Ten specifications offer a way to track them, and 35 operations are marked long-running" (p5) | 35 operations carry `x-aladdin-lro`, at `paths.<p>.<m>.responses.200.x-aladdin-lro`, across exactly 10 specs (AdcDataset, CollateralStatement, EvaluatorAnalytics, Order, PortfolioConfiguration, RiskCustomEvaluationMetric, RiskException, RiskRule, RiskWorkflow, Trade). All 35, and only those 35, return a `*LongrunningOperation` schema. Each of the 10 specs has one status GET, such as `OrderAPI GET /longrunningoperations/{id}`. | CORRECT as a literal count. Note: **10 of the 35 marked operations are the status-polling endpoints themselves.** Only 25 operations actually *start* long-running work. A reader would assume all 35 do. Stronger wording: "25 operations run as long-running jobs; each of the 10 specifications that has them offers a status endpoint to poll." |
| "The SDK checks back on these operations at set intervals" (p5) | `sdk_C/aladdinsdk/api/client.py:378-430`: `_poll_lro_status` loops `await asyncio.sleep(status_check_interval)` until `done`. `config/user_settings.py:295-300` sets the defaults to an interval of 10 s and a timeout of 300 s. README line 288 says "LRO Utilities to trigger and poll Long Running Operation endpoint calls". | CORRECT |
| "linked on GitHub" (p13) | The builder repo holds byte-equivalent copies of all 54 | CORRECT |

**Bottom line for Q1: every number the report uses about the specs reproduces exactly from the genuine, still-current 2.0.0b3 wheels.** I found no counting error.

---

## 2. Exhibit 2 (page 3), step by step

### Step 1: Order. "Who: Portfolio manager · Where: Explore what-if 27 · API: OrderAPI v1 (stable) · Detail: Test (whatIf) and compliance (runCompliance)"
- **Spec, OrderAPI.** `info.description` reads: "Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision." `definitions.v1PostOrderConfig` has `whatIf` (boolean, **required**, "True to post orders in a what-if mode") and `runCompliance` ("Default is true to run compliance on this post order request."). The 7 operations are order:post, orders:batchPost (LRO), order:cancel, orders:batchCancel (LRO), orders:filter, orderIds:filter and the LRO status GET.
- **"Who: Portfolio manager": CORRECT.** The spec also gives a lifecycle the report does not use. `v1Order.authorizeTime`: "The PM authorizes the order … From the authorized PM order, the trader order is created." `activeTime`: "Time when the order was activated by trader." `fillAmount`: "Amount filled and booked". `orderStatus` (readOnly) gives examples "Open", "Compl Pending", "Authorized", "Active", … "Booked".
- **"Where: Explore what-if 27": UNSUPPORTED as stated.** The cited recording (machine transcript, `timestamped/yt_BahCi45_BTc.m4a.ts.txt`, [09:34]) says: "If you go to the New What If model button in the top right corner of Explore…". It goes on to describe Through Time and Point in Time analysis, comparing "my new What If portfolio side by side" on risk metrics, and "Save As portfolio". This is **hypothetical portfolio modelling for risk and performance analysis.** The session never mentions orders, order entry or the OrderAPI `whatIf` flag. The report links two different "what-if" features because they share a name. The spec itself names a different place for orders: `v1Order.basketId` says "visible in the 'Basket' column in Order Monitor of Aladdin Dashboard."
  - Strongest wording: "Where: not stated publicly. Orders appear in Order Monitor in Aladdin Dashboard (OrderAPI spec). Portfolio managers can model what-if portfolios in Explore (27)."

### Step 2: Compliance check. "Who: No one · Where: Aladdin Compliance · API: ComplianceRuleAPI and ViolationAPI v1 (alpha) · Detail: Runs automatically: runCompliance is on by default"
- **runCompliance default true: CORRECT** (quote above). `v1PostOrderResponse.complianceViolations` reads "Compliance violations triggered by posting this order." "Aladdin Compliance" appears in ComplianceRuleAPI: "A unique name for a rule in Aladdin Compliance."
- **The named APIs do not run the check.** ComplianceRuleAPI has **one operation**, `POST /complianceRules:filter`, which is read-only. ViolationAPI has `GET /violations/{id}`, `POST /violation/{id}/details:add` and `POST /violation/{id}/resolutions:add`. The check itself runs inside OrderAPI's post. The exhibit lists ComplianceRuleAPI and ViolationAPI as the step's API, and a reader may assume they execute compliance. They do not. LevelAPI (stable, "start-of-day and intraday Compliance levels") and ComplianceRuleAssignmentAPI also belong to this step and are not named.
- **"Who: No one": OVERSTATED.** It holds only for *running* the check. `v1Violation` has `violationOwner` ("The current team or group who owns the next step in resolving this violation"), `violationDisposition` ("Approved, Rejected, Manual etc."), `actionStatus` ("Closed, Action Required, Action Taken") and `resolutionComment` ("populated by a user"). `v1ComplianceRuleAssignment.resolutionRequiresFourEyesApproval` is "The rule assignment's violation4EyesFlag". So people resolve violations, sometimes under four-eyes approval.
- **A caveat the report omits.** `v1PostOrderConfig.complianceTimeout` reads: "If the non-zero time is reached and the run is not complete, orders will be posted with the "Compl Pending" status set regardless of any violations that may have resulted … Default is infinite." So "returns any violations" holds by default, but a caller who sets a timeout can post an order before compliance has finished.
- Strongest wording: "Runs automatically when an order is posted, unless the caller sets runCompliance to false. Breaches come back with the order and are resolved by a named owner."

### Step 3: Trade. "Who: Trading desk, then operations · Where: – · API: TradeAPI v2 · Detail: BrokerConfirmRoutingAPI holds where confirms go"
- TradeAPI v2 (alpha): "Post, cancel, filter and retrieve trade(s)". It has 7 operations: trades:post, trades:batchPost (LRO), trades:cancel, trades:batchCancel (LRO), trades:filter, trades:retrieve and the LRO status GET. `v2Trade.orderId` reads "Order id for the trade - add reference".
- BrokerConfirmRoutingAPI (alpha, investment_operations): "BrokerConfirmRouting describes instructions for delivering trade information to a broker desk. After a trade is booked in Aladdin, it needs to be confirmed with broker. Confirm routings are setup at broker level in order for the confirmation deliveries to be created and sent out." **"Holds where confirms go": CORRECT.** It is reference data (delivery type, format, recipient contact, autoSend), not a confirmation or matching API. `v2BlockTrade` also carries `confirmedWith` ("external party which confirms the trade") and `confirmedBy`.
- "Trading desk" is supported by the Order description. "Then operations" is DEFENSIBLE, because BrokerConfirmRouting sits in the investment_operations domain.
- **Not in the exhibit, and relevant to the report's control thesis.** `v2PostTradeConfig` has only `mode`, `overrideRelationships`, `overrideCharges`, `updateEntireBlock`, `accountCode`, `entityType` and `entity`. There is **no runCompliance and no whatIf** on trade posting; `compliancePending` is an output-only field. A caller with Trade:write can post a trade directly, and `orderId` is only an optional reference. The specs do not say whether compliance runs on such a trade.

### Step 4: Position in the IBOR. "Who: Portfolio management, trading, operations 10 · Where: Data Cloud 22, 28 · API: None of the 54 is a position API · Detail: Positions appear only as fields in other APIs"
I searched every path, operationId, summary, definition name and property name or description in all 54 specs for position, holding and IBOR (`positions.py`; 118 hits in `positions_out.txt`).
- **Paths and operations: none.** No path or operationId in any of the 54 contains position, holding or IBOR. **"None of the 54 is a position API" is CORRECT.**
- **What exists:**
  1. **CollateralStatementAPI (beta)** defines a full **`v1Position`** object, "Represents the position for exposures and collateral held/pledged". It has 54 properties, including `asset`, `invnum`, `originalFace`, `currentFace`, `notional`, `tradeNumber`, `positionStatus`, `positionSettleDate`, `positionTradeDate`, `exposure`, `dirtyPrice` and `portfolioReference`. It is nested under `v1CollateralDetails.positions` and read through `collateralStatements:filter` and `GET /collateralStatement/{id}`. These are collateral positions only, not the portfolio book.
  2. **CashLadderAPI (stable)**: "a settlement date based ladder of cash balances for all the exposure currencies for a given portfolio group and cash date". `v2PortfolioCurrencyLadder` has `settleDateBalances`, `sodNav` and `intradayNav`. The query has `includeIntradayTradesCashImpact`, `includeIntradayAuthAndActiveOrdersCashImpact`, `includeCollateralHeld` and more. This is a read of **cash positions**, including the cash effect of the day's trades and orders.
  3. Position fragments in violations: `v1ViolationContribution` (`assetId`, `allocationQuantity`, `portfolioId`, `compliancePositionSource` "ORD for orders and TRD for trades"). Order allocations: `v1OrderDetail.quantity`, `portfolioReference`, `quantityBooked`. Trade: `v2Trade.quantity`, `portfolioReference`.
  4. Position-related configuration: PortfolioToolkitAPI `v1Portfolio.positionSource`, `clientLot` ("lot takedown methodology: FIFO, LIFO, HIPP, NET"), `positionReconIndicator` and others. ComplianceRule flags `settledPositionsOnly` and `includeNonInvestmentPosition`. LevelAPI `triggeringEvent` ("…or the end of day position calculation").
- **Verdict on "Positions appear only as fields in other APIs": DEFENSIBLE BUT IMPRECISE.** A whole nested position object exists (collateral) and a cash-balance read exists (CashLadder). "Fields" undersells both.
- Where: Data Cloud is supported. Fivetran blog (live, 2026-10-21): "Users can access their Investment Books of Record (IBOR), Accounting Books of Record (ABOR) holdings and other market data". Newman (22, published transcript): "It does start with IBOR … linking that into the Aladdin Data Cloud." **DEFENSIBLE:** positions are offered through Data Cloud and Snowflake, not through a REST spec.
- Who (10, published captions): "being able to push trades and positions automatically to your middle office team, automatically to your back office team". DEFENSIBLE.
- Strongest wording: "No public specification offers holdings as a resource. Collateral positions and cash balances can be read (CollateralStatementAPI, CashLadderAPI), and IBOR holdings are offered through Data Cloud (28)."

### Step 5: Lot in the ABOR. "Who: Accounting team 26 · Where: Aladdin Accounting · API: AborLotAPI v1 (alpha) · Detail: Retrieved from the ledger_a_summary table"
- `v1AborLot.description`: "AborLot describes the data of ABOR lots retrieved from the ledger_a_summary table." **CORRECT, verbatim.**
- What the report does not say: AborLotAPI has **one operation**, `POST /aborLots:filter`, which is read-only and needs `portfolioId` and `bases`. The lot schema has identifiers, basis, dates, `openTransactionId` and `closeTransactionId`, `assetId` and settings, but **no quantity, cost or book-value fields**. Calling it the API for this step is accurate. Calling the step "covered" is generous.
- Who (26, machine transcript, `blq_accounting-232…ts.txt` [00:32]): "Our clients are CFOs, they're controllers, they're heads of performance". DEFENSIBLE.

### Step 6: NAV. "Who: Accounting · API: ValuationsAPI v1 (beta) · Detail: Each valuation carries an exception list"
- `info.description` reads: "In an accounting workflow, valuations are generated for various processes at the portfolio/portfolio group level. This service can be used to retrieve and filter for accounting valuations data." `v1Valuation` has `valuationNav` ("the NAV after Valuation generated"), `navStatus`, `startNav`, `publisher`, `adminApprover` and `pmgApprover`. Calling it the NAV step is CORRECT.
- **"Each valuation carries an exception list": OVERSTATED (imprecise).** `v1Valuation` carries only `exceptionCount` ("the count of exception occured while runing valuation"). The list comes from a separate operation, `GET /valuations/{parent}/valuationExceptions` → `navLogExceptionRecords[]` of `v1ValuationException`. Better wording: "Each valuation records how many exceptions it raised, and a separate call lists them."
- All 3 operations are read-only. There is no operation to run, approve or publish a valuation.

### Caption: "do not say in what sequence steps 4 to 6 happen"
**CORRECT** for steps 4 to 6. I found no statement ordering position, lot and valuation. There are only hints: `v1AborLotQuery.lastValuationDate`, and LevelAPI's "end of day position calculation". The specs **do** sequence steps 1 to 3, and the exhibit could say so: PM authorises, then the trader order is created, then the trader activates it, then it is filled and booked (OrderAPI field descriptions), then "After a trade is booked in Aladdin, it needs to be confirmed with broker" (BrokerConfirmRouting). The caption is therefore accurate. The wider "event API" clause is discussed in section 4.

### Exhibit 2 title: "The public APIs cover a trade from order to NAV, except positions"
**OVERSTATED.** See section 3.

---

## 3. Have operations been confused with an end-to-end workflow?

Partly, in the Exhibit 2 title, and in the impression the exhibit gives of a usable "order-to-NAV" API path. Mapping what a caller can **do** against what it can only **read**:

| Stage | Public write operation? | What is public |
|---|---|---|
| Order | YES: post, batchPost, cancel | `orderStatus`, `authorizeTime`, `activeTime` and `fillAmount` are **readOnly**. No operation authorises, activates, routes or executes an order. |
| Compliance | Indirect, via OrderAPI's `runCompliance`. ViolationAPI can add details and resolutions. ComplianceRuleAssignment can create and patch. | No operation runs compliance on demand. |
| Execution / fill | NONE | `fillAmount`, `averagePrice` and `traderInitials` are fields only |
| Trade booking | YES: TradeAPI (alpha) post, batchPost, cancel | No compliance or what-if option |
| Broker confirmation and matching | NONE | Confirm *routing* reference data, plus `confirmedWith`/`confirmedBy` fields |
| Settlement | NONE | SSIs (CounterPartySettlementInstructionAPI, alpha) are reference data. `settlementInstructionId1`, `settlementDate` and `actualSettlementDate` are trade fields. MiscellaneousCashflow can create and transmit misc cash flows. |
| Position (IBOR) | NONE | CashLadder cash balances, collateral positions; holdings via Data Cloud (not a spec) |
| ABOR lot | Read only (1 op) | Ids and dates, no quantities |
| NAV | Read only (3 ops) | NAV, returns, approvers, exception count |

**Conclusion.** Using only public operations, a caller can post an order (with compliance) or post a trade directly, and then *observe* lots and valuations. It **cannot drive** execution, confirmation, settlement, position update or accounting. Those happen inside Aladdin. Schneid (26, machine transcript, [01:23]) says: "a process where you can go from that first order through the trade, through all the operation protocols into accounting without lifting up the pencil". That is internal automation, not a public API chain. The webinar (10, published captions) says "very, very robust APIs that manage the end to end life cycle of a transaction … full interoperability in terms of being able to pipe in orders and trades and kind of continue through that life cycle". That is a speaker's claim, and the public specs do not show it beyond orders and trades.

To its credit, the report never says a client can run the whole chain through the API. The caption limits itself to "cover the trade". But "cover a trade from order to NAV" reads as end-to-end. A reader at BlackRock would likely notice that steps 3 to 6 are mostly read-only or reference data, and that TradeAPI, AborLotAPI, ViolationAPI, ComplianceRuleAPI and BrokerConfirmRoutingAPI are all **alpha**.

Strongest wording for the title: "Public APIs can post orders and trades and read what follows, up to NAV. None covers execution, confirmation, settlement or positions."

**Implication for the report's thesis** (p2, p12: "An AI tool calling these APIs would work under the same controls"). The only *explicit* pre-trade control in the specs is OrderAPI's default compliance run. TradeAPI write, MiscellaneousCashflow write ("…AndSendTransmission"), CounterPartySettlementInstruction write and PortfolioGroup write carry no comparable flag. The phrase "Compliance by default on orders" in Exhibits 3 and 14 is accurate. The broader "same controls" claim is a hypothesis that the specs support only for orders.

---

## 4. Other spec claims (pages 2 to 5 and 12 to 14)

**(a) "Access is granted per API, to read or to write" (p2). "With OAuth, access is granted per API and per action. A typical OAuth scope reads trading.order_management.order.v1.Order:read" (p5). "Access set per API. Each API has its own OAuth scopes." (p4, p12)**
- `security.py` results. 37 specs define `<path>.vN.<Name>:read` and `:write` scopes, and every scope prefix equals the spec-id path. But **17 specs define only a single API-wide scope with no read/write split**, described in the spec as "This grants access to all endpoints in the … API". They are AborLot, AccountInfo, Audit, Broker, BrokerConfirmRouting, BrokerDesk, BrokerExternalAlias, Contact, CorporateAction, CorporateActionEntitlement, CounterPartySettlementInstruction, CounterPartySettlementInstructionTemplate, MiscellaneousCashflow, AdcDataset, PortfolioGroup, RestrictedAsset and Strategy. 3 more (PrincipalInterestFactor, CollateralStatement, User) use the API-wide scope for some operations. In total **96 of 301 operations (32%) are gated by one API-wide scope**. These include write operations such as MiscellaneousCashflow create-and-send-transmission, PortfolioGroup and CounterPartySettlementInstruction.
- Also, two of the four credential alternatives (`APIKeyHeader + ClientKeyHeader` and `APIKeyHeader + basicAuth`) carry **no scopes at all** in the spec. Per-API control for those credentials, if any, is not described. Some descriptions point to user-level permissions instead, for example BrokerConfirmRouting: "Users needs to have permissions under permType='brkrDskCon'".
- "Each API has its own OAuth scopes": **CORRECT** for all 54. "The typical scope" example: CORRECT (205 operations use the `:read`/`:write` form). "Per API and per action" and "to read or to write": **OVERSTATED**.
- Strongest wording: "Each API has its own OAuth scopes, and for most APIs, including orders and trades, separate read and write scopes."

**(b) "Every request carries an application key and a second credential … an OAuth 2.0 token, a client key, or a user name and password" (p5).**
- Every one of the 54 specs, and every one of the 301 per-operation `security` arrays, lists exactly 4 alternatives. Each pairs `APIKeyHeader` (header `VND.com.blackrock.API-Key`) with one of `OAuth2AccessCode`, `OAuth2ClientCredentials`, `ClientKeyHeader` (header `X-API-Key`) or `basicAuth`. **CORRECT per the spec** (two OAuth flows count as one credential type).
- Caveat: the SDK only *requires* the API key for Basic Auth (`aladdinsdk/common/authentication/api.py:105`; README line 89 "API Token registered via Studio UI. Required only for Basic Auth"). In practice, the key may be optional with OAuth. "Application key" is the report's own term. DEFENSIBLE BUT UNCERTAIN on "every request".
- Strongest wording: "Every specification asks for an API key plus one of: an OAuth 2.0 token, a client key, or a user name and password."

**(c) "Developers get their OAuth client ID and secret from Studio's screens" (p5).** SDK README line 258: "Client ID and Secret can be sourced from Studio UI by creating a OAuth application under a Project." **CORRECT.**

**(d) "Risk exceptions record both the date a record is valid and the time it entered the system" (p5).** `RiskExceptionAPI definitions.v1RiskException` has `validBeginDate` ("The date on which the exception record is valid. Dictated by the date of the underlying positions…"), `validEndDate` and `entryTime` ("The timestamp when the record entered the system"). **CORRECT.**

**(e) "A Data Cloud dataset carries a flag that says whether it is bitemporal" (p5).** `AdcDatasetAPI` definition property `bitemporal`, titled "Is dataset bitemporal". **CORRECT.**

**(f) "Compliance rule assignments move through review states before they are approved" (p5).** `enumsComplianceRuleAssignmentReviewState` has DRAFT, PROPOSED_READY_FOR_TESTING, PROPOSED_REVIEW_REQUIRED, PROPOSED_REVIEW_REJECTED, APPROVED_REVIEW_REQUIRED, APPROVED_REVIEW_REJECTED and APPROVED. But `reviewState` is an ordinary, non-readOnly field of the `v1ComplianceRuleAssignment` body accepted by `POST /complianceRuleAssignments`, and the spec says nothing about enforced transitions. **DEFENSIBLE BUT UNCERTAIN.** The states exist; that every assignment must pass through them is not shown. Strongest wording: "Compliance rule assignments carry a review state, from draft through proposed to approved."

**(g) "Capital flows record who approved them" (Exhibit 14, p12).** `EnrichedCapitalFlowAPI v1EnrichedCapitalFlow` has `approverUserId` ("Approver Aladdin user Id"), `approvingSystem` and `cancelApprover`. **CORRECT.**

**(h) "Every public specification's ID begins agraph.<domain>, for Aladdin Graph" (Exhibit 4).** All 54 `x-aladdin-api-id` and `x-aladdin-spec-id` values start `agraph.<domain>.`. The gloss is supported inside the specs: OrderAPI descriptions say "Design was agreed with agraph team" and "agreed naming with Aladdin Graph team". **CORRECT.**

**(i) "No event specification is public" (Exhibit 4); "hold no … event API" (Exhibit 2 caption).** None of the 54 has webhook, callback or event-stream operations. However, the core SDK ships public StudioNotificationAPI and StudioSubscriptionAPI specs (alpha), with `v1StudioNotificationEvent` ("the event that triggers a Studio notification"). Their only event type is `NOTIFICATION_TYPE_PROJECT` (for example `project_user_added`), delivered by PUSH or SMTP. These are Studio project notifications, not business events. **DEFENSIBLE.** Stronger wording: "No public specification covers business events; the only public notification API covers Studio project events."

**(j) "The specifications also name Dashboard and Risk Radar" (Exhibit 3 note).** Risk Radar appears in 4 analytics descriptions (for example "Retrieve, update, or create Exceptions as surfaced in Risk Radar."). Dashboard appears in OrderAPI ("Order Monitor of Aladdin Dashboard"; "Dashboard Column Requirement"). **CORRECT.**

**(k) "Aladdin Accounting … with public APIs for valuations, lots and composites" (Exhibit 1).** ValuationsAPI, AborLotAPI and CompositeMembershipAPI are all in the accounting domain. **CORRECT.**

**(l) "They post orders and assign compliance rules to portfolios" (p2).** `POST /order:post` and `POST /complianceRuleAssignments` ("Rule assignment assigns compliance rules for portfolio."). **CORRECT.**

**(m) "Posting an order runs compliance by default. The caller can turn it off. Whether turning it off needs a separate permission is not public" (p2, p12, p13).** The default is true. `runCompliance=false` sits in the same request under the same `Order:write` scope, and the spec defines no separate scope. **CORRECT**, and the hedge is accurate. Add the `complianceTimeout` caveat from section 2.

**(n) "An order can also be posted as a what-if test" (p13).** `whatIf` is "True to post orders in a what-if mode", and it is a required field. **CORRECT.** The spec does not define what "what-if mode" returns or persists.

**(o) Page 14 SDK claims** ("an API token or OAuth app 'registered via Studio UI'"). The README line 89 phrase is "API Token registered via Studio UI". CORRECT for the API token. The OAuth app is "created … under a Project" in Studio UI (line 258), which is consistent.

Unused evidence that would strengthen the report. Every operation carries `x-quota-limit` (100 to 5000), which gives per-operation rate quotas. The OrderAPI shows that **order authorisation is read-only** (`authorizeTime`/`orderStatus` readOnly; "The PM authorizes the order"). That supports the report's "a person approves each action" hypothesis on p12 better than anything it currently cites, but it is not proof that API-posted orders need authorisation.

---

## Genuine mistakes vs reasonable hypotheses

**Factual mistakes or misreadings (fixable wording):**
1. Order step "Where: Explore what-if" conflates Explore's what-if *portfolio modelling* with OrderAPI's `whatIf` order flag.
2. "Access is granted per API, to read or to write" / "per API and per action": false for 96 of 301 operations (20 specs).
3. "Each valuation carries an exception list": it carries a count; the list is a separate call.
4. Compliance "Who: No one": violations have owners, dispositions and optional four-eyes approval.

**Overstatements of scope:**
5. Exhibit 2 title "cover a trade from order to NAV": writes stop at trade booking; execution, confirmation, settlement and positions have no operations; lots and NAV are read-only.
6. "Positions appear only as fields": a nested `v1Position` object (collateral) and a cash-balance API exist.
7. "35 operations are marked long-running": a true count, but it includes the 10 status endpoints.

**Reasonable hypotheses, flagged as such or acceptably hedged:** "Whether turning it off needs a separate permission is not public"; "do not say in what sequence steps 4 to 6 happen"; the Data Cloud home for IBOR data; the "same controls" thesis (supported for orders only).

---

## Top vulnerable statements

**1. "Access is granted per API, to read or to write." (p2, executive summary); "With OAuth, access is granted per API and per action." (p5)**
- Source: in 17 specs `securityDefinitions.OAuth2ClientCredentials.scopes` holds a single scope such as `investment_operations.cash_flows.miscellaneous_cashflow.v1.MiscellaneousCashflow`, described as "This grants access to all endpoints in the … API". Three more specs use that kind of scope for some operations, for 96 of 301 operations in total. The ClientKey and basicAuth alternatives carry no scopes.
- Establishes: per-API scopes everywhere. The read/write split applies only in 37 specs (205 operations), including Order and Trade.
- Inferred beyond: a universal read/write split, and that the split applies to every credential type.
- Verdict: **OVERSTATED** (a factual error on a headline control).
- Strongest wording: "Each API has its own OAuth scopes, and most APIs, including orders and trades, split read from write."

**2. Exhibit 2 title: "The public APIs cover a trade from order to NAV, except positions" (p3)**
- Source: write operations exist only on OrderAPI and TradeAPI (alpha). BrokerConfirmRouting is confirm-delivery reference data. No operation covers execution, confirmation matching or settlement. AborLotAPI has 1 read operation and ValuationsAPI 3 read operations. `orderStatus`, `authorizeTime` and `fillAmount` are readOnly.
- Establishes: a caller can post orders and trades and read lots and valuations later.
- Inferred beyond: API coverage of the whole lifecycle.
- Verdict: **OVERSTATED.**
- Strongest wording: "Public APIs can post orders and trades and read what follows, up to NAV. None covers execution, confirmation, settlement or positions."

**3. Exhibit 2, Order step "Where: Explore what-if 27" (p3)**
- Source: machine transcript `yt_BahCi45_BTc` [09:34] reads "If you go to the New What If model button in the top right corner of Explore…". It describes sector and security weight changes compared on risk metrics, and "Save As portfolio". Nothing about orders.
- Establishes: Explore offers what-if portfolio modelling.
- Inferred beyond: that orders, or OrderAPI what-if posting, happen in Explore.
- Verdict: **UNSUPPORTED.**
- Strongest wording: "Where: not stated publicly. Orders appear in Order Monitor in Aladdin Dashboard (OrderAPI spec, `basketId`), and portfolio managers can model what-if portfolios in Explore."

**4. Exhibit 2, Compliance step "Who: No one … Runs automatically", together with the "Compliance by default" control on p4, p12 and p13**
- Source: `v1PostOrderConfig.runCompliance` reads "Default is true". `complianceTimeout` reads "orders will be posted with the 'Compl Pending' status set regardless of any violations". `v1Violation.violationOwner`, `violationDisposition` and `resolutionComment`, and `resolutionRequiresFourEyesApproval`. `v2PostTradeConfig` has no compliance option.
- Establishes: compliance runs by default when an order is posted, and people resolve violations.
- Inferred beyond: no human role, and an unconditional control (it can be bypassed by `runCompliance=false`, cut short by a timeout, or bypassed by posting trades directly).
- Verdict: **OVERSTATED.**
- Strongest wording: "Posting an order runs compliance unless the caller turns it off or sets a timeout. Breaches come back with the order and are resolved by a named owner. Trade posting has no such option in the spec."

**5. Exhibit 2, Position step "Positions appear only as fields in other APIs" (p3), together with "None of the 54 is a position API"**
- Source: `CollateralStatementAPI definitions.v1Position` ("Represents the position for exposures and collateral held/pledged", 54 properties, nested in `v1CollateralDetails.positions`). `CashLadderAPI` reads "a settlement date based ladder of cash balances…", with `sodNav`, `intradayNav` and `includeIntradayTradesCashImpact`. No path or operationId mentions positions or holdings.
- Establishes: no holdings or IBOR endpoint exists. Collateral positions and cash balances are readable.
- Inferred beyond: that position data exists only as scattered fields.
- Verdict: **DEFENSIBLE BUT UNCERTAIN.** The headline "no position API" is CORRECT; the detail is imprecise.
- Strongest wording: "No public specification offers holdings as a resource. Collateral positions and cash balances can be read, and IBOR holdings are offered through Data Cloud."

(Next in line: "Each valuation carries an exception list" is OVERSTATED, since it carries a count; "Compliance rule assignments move through review states before they are approved" is DEFENSIBLE BUT UNCERTAIN, since the states exist but the spec shows no enforcement.)
