<!-- agent aed9d724db4ecf1de; started 2026-10-19T04:11:32.713Z; finished 2026-10-19T04:13:23.282Z -->

## Readability review: aladdin_field_guide.html (outsider's view)

File: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/aladdin_field_guide.html

### 1. Terms used before or without explanation (first location → suggested gloss)

Finance / operations
- **collateral** – L1 lead "the cash and collateral they move" → "collateral, the assets pledged to back a derivative or loan".
- **positions, compliance levels, cash ladder, accounting lots, ABOR, risk exceptions** – L1 figure + figcaption "compliance Levels, the Cash Ladder, Collateral Statements, ABOR lots". Six undefined nouns on the first screen; ABOR is only defined in L9.
- **mandate** – STAGES setup "with its mandate, benchmarks" (also DOMDESC compliance) → "the mandate (the client's written rules on what the portfolio may hold)".
- **benchmark** – same sentence → "the index it is measured against".
- **custodian** – setup "trade routing to custodians" → "the bank that holds the client's securities and cash".
- **portfolio manager vs trading desk/trader** – STAGES order "a directive to the trading desk" → "the portfolio manager (who decides what to buy) sends an order to the trading desk (who buys it in the market)".
- **dealing capacity, basket** – order stage; cut or gloss "whether the desk acts as agent or principal".
- **settlement / settlement date** – order detail "projected settlement-date cash" → "settlement, the day one or two days later when cash and securities actually change hands".
- **broker, block trade, quotes in competition** – STAGES trade → "a broker (the outside firm that executes in the market)"; "one large block trade, executed once and then split (allocated) across the portfolios".
- **counterparty, broker desk, confirms, transmission framework** – STAGES settle.
- **corporate action, entitlement, elected/instructed, coupon reset, MBS factor, ISDA, DECO** – STAGES lifecycle → "a corporate action is an issuer event (dividend, split, takeover offer) that changes what holders own or must choose".
- **lot, NAV, Dietz** – STAGES accounting "Accounting and NAV" → "a lot is one purchase tracked separately for cost"; "NAV, net asset value, the fund's daily per-share price".
- **tracking error, bps, look-through** – STAGES oversight detail.
- **subscriptions/redemptions, in-kind, true-up** – DOMDESC clients.
- **VaR, four-eyes, room-to-limit** – DOMDESC compliance (four-eyes defined only in L9).
- **CDS, CDX, NDF, swaption, repo, TBA** – DOMDESC data; TBA never defined ("to-be-announced mortgage bond trade").
- **CUSIP/ISIN/SEDOL/RIC, OAS** – STAGES research detail, HOPS 3 → "security identifier codes".
- **master-feeder, master-sleeve, SMA roll-up** – STAGES setup detail.

Tech
- **OpenAPI/Swagger spec** – L1 card "54 OpenAPI specs" → "machine-readable API descriptions".
- **multi-tenant** – L1 card "hosted, multi-tenant SaaS".
- **namespace, master entity, state machine** – L2 lead.
- **protobuf, gRPC, transcoded, Google AIP, api-linter** – L5 lead/figcaption and graph layer `sub` → "protobuf (Google's schema language), gRPC (its binary RPC protocol), translated to ordinary REST".
- **OAuth scope** – L5 gateway body → "a scope is a permission string attached to the login token".
- **long-running operation** – used in HOPS 3 before HOPS 5 explains it.
- **pydantic, Dynaconf, pandas DataFrame** – HOPS 1/6.
- **maker-checker, bitemporal, optimistic concurrency, idempotency** – CONV cards.
- **LangGraph supervisor, function calling, LLM-as-judge** – L8 figure and cards.
- **citizen developer** – L5 graph body quote, defined only in L9.

### 2. Read-twice passages
- L1 lead, sentence 2: seven comma-separated nouns ("the portfolios, the securities, the orders and trades, the rules…").
- L1 figcaption "Every arrow is a real dependency in the API specs: compliance Levels…" – five undefined systems.
- L2 lead "maps to a domain in the API namespace, a master entity, and a state machine" – three abstractions before any example.
- STAGES trade detail "Trades key on portfolio plus investment number plus trade number, with touch count and version for concurrency. Quote statuses include covered, tied, done away…"
- STAGES lifecycle detail "margin calculators reading ISDA agreements set up in a tool called DECO."
- STAGES accounting detail "ABOR lots carry a parallel OBOR lot id, so investment book and accounting book reconcile at lot level. Valuations record Dietz…"
- STAGES oversight detail "absolute limits (250 bps tracking error) or relative ones, look-through and benchmark configuration."
- DOMDESC trading: the BlockTrade parenthesis ("settlement FX, TBA stipulations, repo collateral and FX legs").
- LAYERS graph body "Every spec carries gRPC status types, update masks, page tokens… fingerprint of services defined in protobuf and exposed through gRPC-gateway style transcoding."
- LAYERS data body: one 70-word sentence with six subsystems.
- L8 lead "Its tools are the same governed APIs Studio exposes, which is why API quality and AI readiness are one problem" – assumes the reader knows LLM tool-calling.
- CONV two-layer authorisation: "Modern API security sits on a thirty-year-old entitlement model."

### 3. Ordering
Overview → Lifecycle is right, but Lifecycle assumes the reader already knows who a PM, trader, broker, custodian and fund accountant are. Products (L3) interrupts the Lifecycle→Domains thread; move it to after Architecture (or merge into Overview). Glossary (L9) defines ABOR, four-eyes, LRO, citizen developer that L1, L2, L5 rely on; link to it from Lesson 1 or convert its first eight entries into inline `<abbr title>` tooltips. The page serves two readers (interview prep: "Questions worth asking them"; engineers: L5–L7). Add a two-line "how to read this" in the L1 note: non-engineers can skip 5–7. Recommended order: Overview (+primer) → Lifecycle → Domains → Architecture → One request → Conventions → Products → AI → Glossary → Quiz → Sources.

### 4. Marketing tone and duplication
- Marketing: L1 stats strip ("$1BN+", "+13%", "~4,000 engineers") reads as pitch deck and does not help understanding; "The thesis in one picture"; "including Microsoft Treasury and soon Amazon Treasury"; PRODUCTS Studio "Positioned as the extensibility layer"; L8 "connective tissue"; L9 lead "makes you sound like you have read the platform".
- Explained twice or more: Azure/AWS hosting (L1 stat, LAYERS hosting, QUIZ); two-layer auth (LAYERS gateway, CONV, QUIZ); LRO (HOPS 5, CONV, GLOSS); Copilot plugin registry (PRODUCTS, L8 figure, L8 card, QUIZ); ADC draft/review/released (PRODUCTS, DOMDESC platform, CONV, QUIZ); "24 alpha" (CONV, QUIZ, interview Q1). Quiz repetition is fine; PRODUCTS duplicating L5/L8 is not.

### 5. Three highest-leverage edits

**A. Add a one-screen primer in Lesson 1**, inserted directly after the lead, before `<div class="stats">` (consider dropping the stats strip):
> **The investment process in six roles.** A client hands money and a *mandate* (rules on what may be held) to an asset manager. A *portfolio manager* decides what to buy or sell and raises an *order*. A *trader* executes it with a *broker*, the outside firm that deals in the market. Two days later the trade *settles*: cash and securities change hands at the *custodian*, the bank that holds the client's assets. *Accountants* record each purchase as a *lot* and compute the fund's daily price, the *NAV*. *Compliance* and *risk* teams check every step against the mandate and regulation. Aladdin is the one system all six roles share.

**B. Rewrite the L1 lead sentence 2 and figcaption.** Replace "One system holds the portfolios, the securities, the orders and trades, the rules they must obey, the cash and collateral they move, the accounting records they produce, and the risk views that sit on top." with:
> One system holds what each portfolio owns, every order and trade, the rules each portfolio must obey, the cash it has available, its accounting records and its risk numbers.

Replace figcaption "The thesis in one picture. Every arrow is a real dependency in the API specs: compliance Levels, the Cash Ladder, Collateral Statements, ABOR lots and Risk Exceptions all read the positions a trade creates." with:
> One trade, six consequences. The holdings it changes are read by the compliance check (how close each rule is to its limit), the cash forecast by settlement day, the collateral owed on derivatives, the accounting lots, and the risk rules, and are copied to the client's Data Cloud. Each arrow is a dependency visible in the API specs.

**C. Plain-language the Lesson 2 entry point.** Replace the lead "Click a stage. Each one maps to a domain in the API namespace, a master entity, and a state machine the specs document." with:
> Click a stage. For each one you get the API domain that owns it, the main record it creates, and the states that record moves through (for example an order goes open → authorised → filled).

And replace STAGES order `what` "The portfolio manager raises an order, a directive to the trading desk. It carries strategy, basket, dealing capacity, limits and benchmark." with:
> The portfolio manager (who decides what to buy) raises an order, an instruction to the trading desk (who buys it in the market). It records the strategy behind the decision, price limits and the benchmark the portfolio is measured against.
