# Fix-list audit: Aladdin Studio / Aladdin Graph engineering view

Reviewer role: a skeptical engineering leader for Aladdin Studio and Aladdin Graph. I checked the claims that matter against the 54 specs in `scratchpad/unpacked/`, the SDK clone in `scratchpad/audit/sdk_C` (HEAD c1c9f3c), and the Rosales and Valdez and Smith Garson transcripts. Everything I recomputed is listed in the "What I verified" note at the end.

---

## 1. Stance

The fix list is good. On the spec facts it is almost always right, and it catches the errors an Aladdin engineer would raise first: the read/write scope claim, `complianceTimeout`, the job posting, and the solid Copilot-to-public-API arrow. But several of its own replacement sentences would draw a second correction from an engineer:
- some bring the "Copilot uses the public APIs" inference back in;
- one gets the SDK's rate limiting wrong;
- one gets the order-approval sequence wrong;
- six break the semicolon rule.

The evolved thesis is a real improvement, but "the same permissions and API controls" is still too literal. The control that matters most, the registry's per-group tool gating, runs inside Copilot's own orchestration graph, not on a server. Copilot is never shown passing through OAuth scopes. And Copilot is never shown posting an order.

---

## 2. Verdicts

**Counts: ACCEPT 38, ACCEPT WITH CHANGE 23, REJECT 0, DEFER 0.** The evolved thesis is ACCEPT WITH CHANGE.

### The evolved thesis: ACCEPT WITH CHANGE

The proposed thesis is: "Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls."

The direction is right. It moves the claim from "same controls" to "same tools", and the public evidence supports a tools claim: about 2,000 tools and agents in the registry, against 301 public operations with no holdings or exposure read. That coverage gap is the real product gap. What follows is what an engineer would call naive in the reasoning behind the thesis.

**1. Registry permissions are not a server-side control today.** Rosales describes them inside the orchestration graph [06:38–07:22]: "we go into this filtering and access control node … they have complete control over which environments this plug-in is enabled in, which user groups have access … and even which Aladdin apps can even access these plugins". That node is one step of Copilot's LangChain graph, between the input guardrail and planning. It also does tool retrieval, cutting the list down to "20 to 30 tools and agents".
- A client that brings its own orchestrator skips that node entirely.
- An MCP server would have to re-implement the gating at `tools/list` and `tools/call`.
- The result is the same policy data enforced at a new point, which is not "literally the same" control.
- The "app" dimension (which Aladdin apps may use a plug-in) has no value for an outside AI tool until BlackRock defines one.

**2. "API scopes" are not shown to be a Copilot control at all.** OAuth scopes, the application key and `x-quota-limit` belong to the Studio client route (`client.blackrock.com/api/oauth2/...`). No source shows Copilot's tools passing through them, and Copilot more likely uses internal service authentication. An MCP route would bring scopes with it, but they would be the Studio client's scopes, not Copilot's. The controls that are truly the same for every caller are the ones built into Aladdin's services:
- Aladdin user permissions;
- compliance on order posts;
- the order workflow;
- approval records.

**3. "Same permissions" depends on whose identity the call carries.** Copilot calls "on behalf of the user". A client agent gets that user's Aladdin permissions only through a delegated user flow: OAuth access code, or the SDK's `refresh_token`. With `client_credentials`, which the SDK supports and the fix list cites, the agent runs as an application or system account. It then carries that account's permissions, which for a shared agent are usually wider than any one user's. That is a confused-deputy problem, not "the same permissions".
- An MCP server could not simply forward the client's token either. The MCP authorization spec forbids token passthrough, so BlackRock would need token exchange into an Aladdin identity.

**4. Compliance on orders is not a Copilot control.** Copilot is shown answering, never posting ("hopefully next year … autonomous agents"). `runCompliance` applies to any order post by any caller. It belongs in the list of service controls, not in "what Copilot calls".

**5. The thesis quietly drops "act", but Part 3 does not.** Exhibit 15 row 4 (an AI-proposed rebalance) and p12's "a person approves each action" are about writes. Copilot's tools are read tools. A coherent v24 thesis needs two parts:
- the same tools Copilot uses, to answer;
- the same order workflow, to act. The public OrderAPI has no call to authorize an order, because `orderStatus` and `authorizeTime` are read-only.

**6. The model-side split is not clean either.** Half the registry is "custom agents", which are BlackRock-built LLM workflows. If an MCP server exposed them, some BlackRock model-side behaviour would travel with them, inside each agent. That raises the question of whose policy governs the answer.

**7. MCP is the author's protocol, not BlackRock's.** The Copilot team said it built a "slim, very specific" Aladdin agent protocol and is "actively evaluating" LangChain's agent protocol and A2A [05:04–05:18]. MCP fits tools. A2A may fit agents. The labelled inference should name both.

**8. Tool count.** An MCP server cannot list 2,000 tools to a client's model. Copilot's own team says more than "40, 50 tools" hurts performance. BlackRock would have to offer server-side tool search, which is part of Copilot's filtering node offered as a service.

**Proposed wording**
- Cover and p2 headline: "Clients' AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions."
- If the thesis must cover acting, use a longer p2 or p12 version: "Clients' AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions, with a portfolio manager still authorizing each order."
- Supporting p12 paragraph, which replaces the current second paragraph at about the same length:

  "Some controls sit inside Aladdin's services and apply to every caller: each user's Aladdin permissions, compliance on order posts, and the order workflow. In Aladdin's PM and trader model, the portfolio manager authorizes an order before a trader works it, and the public order API has no call to authorize one 6. Other controls sit where a caller connects. Copilot applies its registry rules by environment, user group and app as it picks tools 9. Studio clients connect with an application key and OAuth scopes 6. A route for clients' AI tools would need BlackRock to apply the registry rules at that point. Copilot's guardrails, planning and AI-graded tests run inside Copilot, so a client's own model would not get them 9. One such route would be an MCP server onto Copilot's registry. That is my inference. Copilot's team has said it is evaluating A2A and LangChain's agent protocol 9."

### Tier 1

| # | Verdict | Reasoning, and the exact replacement where changed |
|---|---|---|
| 1 | ACCEPT WITH CHANGE | Evolve the thesis, but use the wording above. "Same permissions and API controls" overstates what carries over (points 1–4). Label the inferred route as "MCP or A2A". |
| 2 | ACCEPT WITH CHANGE | "Runs AI on these APIs" brings back the same-API inference (the referent is the public APIs). "Most mapped to production Aladdin APIs" is unsupported, because the share of tools against agents is not public. Replace with: "BlackRock already runs AI across Aladdin. Copilot answers questions for BlackRock and client users by choosing from about two thousand registered tools and agents. Each tool maps to an Aladdin API already in production. Public sources show Copilot answering questions, not taking actions." |
| 3 | ACCEPT WITH CHANGE | The first sentence is fine. "Production APIs and controls it sells" asserts that Copilot runs on the APIs clients buy. Second sentence: "BlackRock already runs AI across Aladdin itself, in Copilot." |
| 4 | ACCEPT | Correct, and the spec supports "post orders and assign compliance rules". |
| 5 | ACCEPT WITH CHANGE | The counts are verified: 17 single-scope specs, 3 mixed, 96 of 301 operations under a whole-API scope. The proposed permissions sentence leans on PermissionAPI, whose own text says "This is not intended to be used for Authorization". The per-operation prerequisites appear only on broker, contact, capital-flow and ADC specs, none on OrderAPI or TradeAPI. p2: "With OAuth, each API has its own scopes, and most separate read from write. Aladdin's user permissions are defined by function, action and portfolio, and several APIs state which permission each operation needs 6." p5: delete "and per action", and add if space allows: "Client-key and password logins carry no scopes." |
| 6 | ACCEPT WITH CHANGE | Right finding, two precision problems. First, the timeout posts the order as "Compl Pending", not as a clean order. Second, "Trades posted directly have no compliance setting" reads as "trades skip compliance", but TradeAPI (alpha) has a read-only `compliancePending` flag. p2 (short): "Posting an order runs a compliance check by default. The caller can skip it with the same scope it uses to post. Whether an Aladdin permission restricts this is not public 6." p12 (full): "Posting an order runs a compliance check by default. The caller can skip that check with the same Order:write scope it uses to post. If the caller sets a time limit and the check runs over it, the order posts with the status Compl Pending. Whether an Aladdin permission restricts either option is not public. The trade API, still in alpha, has no compliance option, and each trade shows whether compliance is pending 6." |
| 7 | ACCEPT WITH CHANGE | "They include BlackRock's own applications and Copilot" is unsourced. The slide does not define a call or name callers. p8: "The slide covers BlackRock and Aladdin together. It does not say whose calls it counts or how it counts a call 11." The rest of fix 7 is accepted. |
| 8 | ACCEPT WITH CHANGE | "Any client program" is too broad. Access needs a licence, an Aladdin environment, Studio registration and Aladdin permissions. Replace with: "A licensed client's own programs, AI agents included, can already call the APIs with credentials registered in Studio, acting for a user or as an application 6, 29. BlackRock has published no support, guidance or connector for AI agents." |
| 9 | ACCEPT WITH CHANGE | Right swap, but attribute and date it. Crockett (Microsoft) raised the idea and Garson agreed, in November 2024. "On BlackRock's podcast in November 2024, Microsoft's Adrian Crockett said clients with their own copilots may want BlackRock's plug-ins exposed there. BlackRock's Head of Product for AI, Syril Smith Garson, answered '100%' and 'we are hearing that from our clients' 71." Drop the posting from Exhibit 14. |
| 10 | ACCEPT WITH CHANGE | "Approval before any order posts" gets the mechanics wrong. In Aladdin's model the order is posted first and the portfolio manager then authorizes it. Replace with: "A governed route for clients' AI tools: the tools Copilot uses, called for each user under that user's Aladdin permissions, with a portfolio manager authorizing each order before it trades." |
| 11 | ACCEPT WITH CHANGE | Redraw, but do not put "registry permissions" or "API scopes" in the shared band. Copilot enforces the first in its own graph, and the second is only shown on the Studio client route. Use three bands. **Shared, inside Aladdin's services:** Aladdin user permissions, compliance on order posts, the order workflow (the portfolio manager authorizes; there is no authorize call in the public API), and approval records. **At each connection:** on Copilot's arrow, "registry rules by environment, user group and app"; on the Studio arrows, "application key, OAuth scopes, quotas"; on the dashed client-AI arrow, "proposed: registry rules applied here". **Inside Copilot only:** guardrails, planning and AI-graded tests. The legend covers arrows. If page 12 cannot take three bands, keep two and put the connection-level controls as labels on the arrows. |
| 12 | ACCEPT | Matches how the platform is built: apps and Studio both sit over shared services. |

### Tier 2

| # | Verdict | Reasoning |
|---|---|---|
| 13 | ACCEPT | The spec places orders in "Order Monitor of Aladdin Dashboard". The OrderAPI's own required `whatIf` flag is a different thing from Explore's what-if. |
| 14 | ACCEPT WITH CHANGE | "Connector" clashes with Data Cloud's Snowflake and Databricks connectors (fixes 36 and 56). Use: "BlackRock has published no MCP server or AI connector for Aladdin." |
| 15 | ACCEPT | Outside my lane; accepted on audit E's evidence. A trial with sign-up scores 1 under the legend. Re-total Exhibit 17 and its text. |
| 16 | ACCEPT WITH CHANGE | The count is 8 (Arcesium, Bloomberg, FactSet, LSEG, MSCI, S&P, Snowflake, Databricks). "Eight of the other 10 offer outside AI tools a connector or an MCP server. Aladdin, SimCorp and Clearwater offer AI inside their own platforms." |
| 17 | ACCEPT | Correct. |
| 18 | ACCEPT | Matches the scores. |
| 19 | ACCEPT | Verified: `exceptionCount` on the valuation, and a separate `/valuations/{parent}/valuationExceptions` call. |
| 20 | ACCEPT WITH CHANGE | "API rate limits built in" is wrong in a way an engineer will spot. The SDK's limiter (`common/ratelimiting`) applies only the `max_calls`/`window_seconds` the user sets in settings. It has no defaults and does not read the specs' `x-quota-limit`. Use: "Open-source Python library with typed clients for the APIs and a Snowflake connection for Data Cloud, with login, retries and configurable rate limiting built in." |
| 21 | ACCEPT | Correct. |

### Tier 3

| # | Verdict | Reasoning |
|---|---|---|
| 22 | ACCEPT WITH CHANGE | "Read what follows" overclaims: there is no execution, confirmation or settlement-status API. "Except positions" also clashes with fix 24's collateral positions. Use: "The public APIs post orders and trades, and read lots and valuations. None reads portfolio holdings." |
| 23 | ACCEPT WITH CHANGE | The substance is right, but there is a semicolon between sentences. Who: "The compliance engine runs it. The team that owns each violation resolves it." API: "OrderAPI (runCompliance), then ViolationAPI to resolve". |
| 24 | ACCEPT WITH CHANGE | "A copy of the IBOR" is an engineer's shorthand that the sources do not quite say. Where: "Read from Data Cloud, which carries IBOR holdings". The detail is accepted as written. |
| 25 | ACCEPT | Correct. |
| 26 | ACCEPT | Correct. Clear any named SDK contributor with the client first. Their identity comes only from commit emails. |
| 27 | ACCEPT WITH CHANGE | Semicolon between sentences. Use: "Disclosed because BlackRock owns more than 5% of JPMorgan. The proxies do not say what the payments cover. JPMorgan is also a custodian that connects to Aladdin." |
| 28 | ACCEPT | Verified: `reviewState` is writable in the POST/PATCH body. |
| 29 | ACCEPT WITH CHANGE | "Move from open to authorized to confirmed" implies the sequence is enforced. `manualStateCycle` lets the caller create a flow directly as authorized or confirmed. Use: "Capital flows need the user's Aladdin cash permissions for each action, such as paying, modifying and confirming, and record who authorized and approved each one." |
| 30 | ACCEPT | Verified: SDK `RUN_MODE` includes Studio Compute. |
| 31 | ACCEPT WITH CHANGE | "Most of them production Aladdin APIs" is unsupported, and "One answer; policy: …" uses a semicolon. Title: "…then calling tools, each mapped to a production Aladdin API, and agents". Last box: "One answer. The product page says Copilot will not give investment advice." The other parts are accepted. |
| 32 | ACCEPT | Correct, and consistent with fix 8. |
| 33 | ACCEPT WITH CHANGE | Three problems. It states "same Aladdin Graph runtime" as fact. It has a semicolon between sentences. And "2,000 tools against 54 public APIs" compares unlike units, because a tool maps to an API operation, not to a whole spec, so compare with 301 operations. Use: "The public APIs are Aladdin Graph APIs, and some back BlackRock's own screens, such as Risk Radar 6. Copilot's tools map to Aladdin APIs already in production 9. Whether those include the public APIs is not public. Copilot draws on about two thousand tools and agents, and the public specifications hold 301 operations, so many of Copilot's tools likely sit on APIs clients cannot call." Do not cite the SDK's "Internal" label as evidence. It is on four utility specs only (token, notification, subscription, demo). |
| 34 | ACCEPT | Outside my lane; accepted on audit E's evidence. |
| 35 | ACCEPT | Verified that `resources/sample_code_snippets/` and two demo notebooks are public in the SDK repo, so 2 is fair. Re-total. |
| 36 | ACCEPT | Correct. |
| 37 | ACCEPT | Correct. The controls panel applies to API calls only. |
| 38 | ACCEPT WITH CHANGE | Verified: 4 AdcDataset writes are marked "internal BlackRock use only". The portal wording has a semicolon between sentences. Portal: "Catalog, guides, field dictionary, notebooks and samples. The portal sits behind a client login." The Admin Center and Governance parts are accepted. |
| 39 | ACCEPT | Correct. |
| 40 | ACCEPT | Correct. |
| 41 | ACCEPT WITH CHANGE | Verified: SUPPORT.md has three empty headings. Semicolon between sentences. Get help, public: "The SDK repo's SUPPORT.md has headings but no channels. The maintainers merged a client engineer's changes." The column rename is accepted. |
| 42 | ACCEPT | Correct. |

### Tier 4

| # | Verdict | Reasoning |
|---|---|---|
| 43 | ACCEPT | Verified: 35 `x-aladdin-lro` markers in 10 specs, 10 of them on status calls, which leaves 25. |
| 44 | ACCEPT | Verified: the Studio notification specs cover Studio entities (user, project, space) and event types (ACM, compute, API, space, project), not business events. |
| 45 | ACCEPT | Correct. |
| 46–49 | ACCEPT | Outside my lane; accepted on audit D's evidence. |
| 50 | ACCEPT | Optional, but it heads off an analyst's correction. |
| 51 | ACCEPT | Correct. The line is the generic technology preamble. |
| 52 | ACCEPT | Matches the talk. |
| 53–55 | ACCEPT | Correct. |
| 56 | ACCEPT | Correct, and 24 of 54 specs are alpha. Keep the labels only if that is deliberate. |
| 57 | ACCEPT | Correct. |
| 58 | ACCEPT | Correct. |
| 59 | ACCEPT | Correct. |
| 60 | ACCEPT | Verified 5: AdcDataset create, update, reconcile and release, plus RiskWorkflow batchCreate. Optional. |
| 61 | ACCEPT WITH CHANGE | Semicolon. Use: "Spaces: named alongside Projects. Not described publicly." |

### Evidence items 62–69

- **62:** use it, with the attribution and date given under fix 9.
- **63:** weaker than it looks. "On behalf of the user" comes in a sentence about "respecting those preferences", introduced with "ideally". Pair it with the Copilot page's "permission-dependent access to insights", and use both only for "Copilot answers within each user's permissions".
- **64:** use it, as in fix 33.
- **65:** use it for the permission model and its per-operation prerequisites, but not as proof of enforcement. PermissionAPI says it is "not intended to be used for Authorization", and neither OrderAPI nor TradeAPI documents a permission. Add EnrichedCapitalFlow's "standard API permission ALADDIN_API_USER", which shows that using the APIs at all is itself an Aladdin permission.
- **66:** this is the strongest control for the "acting" half of the thesis, and no fix uses it (see section 4).
- **67:** use it with the caveat in point 3 above: `client_credentials` is an application identity.
- **68 and 69:** use both.

---

## 3. Fixes whose wording would itself draw a correction

**New technical errors or distortions**
1. **Fix 20, "API rate limits built in".** The SDK enforces only limits the user configures. It does not apply BlackRock's quotas.
2. **Fix 10, "approval before any order posts".** Aladdin posts the order first, and the portfolio manager then authorizes it.
3. **Fix 2, "runs AI on these APIs" and "most mapped".** This brings the unproven same-API link back, and the tool-to-agent share is not public.
4. **Fix 3, "the production APIs and controls it sells".** The same problem.
5. **Fix 11 and the evolved thesis.** Both put registry permissions and API scopes in the shared server-side layer. The first runs inside Copilot's graph, and the second is not shown on Copilot's path.
6. **Fix 33.** It states "same Aladdin Graph runtime" as fact and compares tools with specs instead of operations.
7. **Fix 6, "Trades posted directly have no compliance setting".** This reads as "trades skip compliance". Trades carry a `compliancePending` flag.
8. **Fix 22 against fix 24.** "Except positions" contradicts "collateral positions can be read".
9. **Fix 14, "or connector".** This collides with the Snowflake and Databricks connectors elsewhere in the report.
10. **Fix 7, "They include … Copilot".** This is unsourced.
11. **Fix 8, "Any client program".** Access needs a licence and Studio registration.
12. **Fix 29, "move from open to authorized to confirmed".** `manualStateCycle` lets a caller skip states.
13. **Fix 31, "most of them".** This is unsupported.

**Breaks the semicolon rule:** fixes 23, 27, 31, 33, 38, 41 and 61. The fix list does not use "suggested" or em-dashes, and none of its wording refers back to the old text.

**Space risk:** fixes 6, 11 and the p12 thesis paragraph all add text to pages 2 and 12. The short p2 version of fix 6 and the arrow-label fallback for fix 11 keep page 12 intact.

---

## 4. Missing from the list

1. **No public call can authorize an order.** OrderAPI has post, batch post, cancel, batch cancel and filter only. `orderStatus` and `authorizeTime` are read-only, and in the PM and trader model the portfolio manager authorizes. This is the strongest public basis for "a person approves each action" (p12, Exhibit 15 row 4).
2. **TradeAPI (alpha) can post a trade with no order behind it,** because `orderId` is optional. That skips the order workflow and its compliance step. An agent route should exclude it, and p12 should say the public trade API is alpha.
3. **Identity type decides "same permissions".** A delegated user token, as with Copilot "on behalf of the user", carries that user's permissions. `client_credentials` or a bot account carries the account's own. The report should say which one the proposal means.
4. **Every OAuth scope is labelled "non-sensitive read/write",** Order:write included. Sensitivity is graded in Aladdin permissions (`sensitivityGrade` LOW to ULTRA), not in scopes. This supports moving the emphasis from scopes to permissions.
5. **Other server-side controls an agent would meet:**
   - `x-quota-limit` on all 301 operations;
   - required `Request-ID` and `Origin-Timestamp` headers on every call;
   - the required `whatIf` flag on every order post, which forces an explicit choice of test or live.

   Nothing in the specs marks a call as coming from an AI agent. An "agent X for user Y" audit trail would be new work.
6. **BlackRock's protocol direction.** The talk names A2A and LangChain's agent protocol, not MCP.
7. **The p10 "direction" box** proposes publishing "which production APIs each tool calls, which user groups may use each tool". An engineering or security leader would refuse to publish that mapping, because it exposes attack surface and internal entitlement design. Publish the model instead: "how each tool's access is set by environment, user group and app." The same box's "guardrails that block investment advice" goes further than the page's "will not give investment advice".
8. **Exposure, Copilot's flagship example, has no public API.** This is the concrete reason the "same tools" thesis has value. It belongs in the evolved thesis text, not only in fix 33's problem column.

---

## 5. Top 5 recommendations, in priority order

1. **Adopt the evolved thesis with the identity-based wording.** "Clients' AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions." Do not claim the registry gating or API scopes are "the same". Say they would be applied at the new connection point.
2. **Rebuild Exhibit 14 (fix 11) around where each control is enforced.** Inside Aladdin's services is shared. At each connection is different per route, with registry rules on Copilot's arrow and scopes on the Studio arrows. Inside Copilot only is not transferable. Draw the client AI route dashed and label it "MCP or A2A, my inference".
3. **Make the acting half rest on the order workflow, not on Copilot.** Add to p12 and Exhibit 15 row 4 that the public order API cannot authorize an order and that a portfolio manager does. Use the fix 6 wording above, with Compl Pending and the alpha trade API.
4. **Correct the replacement sentences that would draw a second correction:** fixes 2, 3, 10, 20, 22 and 33 at minimum. Fix the seven semicolon breaks.
5. **Use the source 71 exchange with correct attribution and date (fix 9), and state technical access plainly (fix 8, licensed clients only).** Together they show demand plus a route that already exists, which makes the proposal credible to an engineer.

---

### What I verified

- **Scopes:** 17 specs use a whole-API scope only and 3 mix both styles, which puts 96 of 301 operations under a whole-API scope. All 120 read/write scope descriptions read "non-sensitive read" or "non-sensitive write".
- **Authentication:** every operation pairs `APIKeyHeader` with OAuth access-code, OAuth client-credentials, a client key or basic auth.
- **Long-running operations:** 35 `x-aladdin-lro` markers, of which 10 are status calls.
- **Stability labels:** 24 alpha, 6 beta, 23 stable, 1 sunset.
- **Order posting:** OrderAPI `v1PostOrderConfig` has `whatIf` (required), `runCompliance` and `complianceTimeout` ("Compl Pending … regardless of any violations"). `orderStatus` and `authorizeTime` are read-only, and there is no authorize operation.
- **Trade posting:** TradeAPI is alpha. `v2PostTradeConfig` has no compliance option, and `compliancePending` is output-only.
- **Users and permissions:**
  - UserAPI lists "bot accounts granted access to Aladdin" and the user type `USER_TYPE_SYSTEM`.
  - PermissionAPI says "not intended to be used for Authorization", and its `permGroup` field is scoped to PORTFOLIO or PORTGROUP.
  - The per-operation `permType` notes appear on broker and contact APIs only.
  - EnrichedCapitalFlow requires `ALADDIN_API_USER` plus newcash permissions.
- **SDK:**
  - It supports both the `client_credentials` and `refresh_token` flows.
  - Its rate limiting is user-configured, with no defaults.
  - The Data Cloud client wraps the Snowflake connector.
  - The only specs labelled "Internal" are its four utility specs.
  - SUPPORT.md has empty headings.
- **Copilot talk:** the filtering and access-control node sits inside the orchestration graph, and the team names A2A and the LangChain protocol [05:12–05:18, 06:38–07:22].
- **Source 71 (official transcript):** Crockett raises plug-ins in custom copilots, Garson answers "100%" and "we are hearing that from our clients". The source is dated November 6, 2024.
