<!-- agent a77bec0b03694f90d; started 2026-10-19T04:11:32.791Z; finished 2026-10-19T04:13:45.004Z -->

Review of /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/aladdin_field_guide.html (read in full: HTML sections and STAGES, PRODUCTS, LAYERS, HOPS, CONV, GLOSS, QUIZ, DOMDESC, APIS).

Overall: the Overview and AI lessons each carry a real thesis and the evidence base is unusually honest. The middle lessons (Lifecycle, Products, Architecture, One request) are well-sourced inventories that let the reader infer the idea rather than stating it. The fixes below are mostly one-sentence additions.

## 1. Lesson theses

- Lifecycle lead "Click a stage. Each one maps to a domain" is an instruction, not an idea. Replace with: "Each stage hands a record to the next, and the hand-off is a state change on that record. Click a stage to see the record, its states, and the APIs that move it."
- Products lead "Aladdin is sold as a set of named products" lists packaging. Replace with: "The products are entry points onto one set of positions and portfolios, not separate systems. That is why a client who buys Risk and later adds Enterprise does not re-load its data."
- Architecture lead "Click a layer. The specs reveal the middle three" describes sourcing. Replace with: "Every caller, whether a BlackRock app, a client script or Copilot, enters through the same gateway and the same domain services. There is no privileged path. Click a layer."
- Lifecycle stage details are fact lists ("Trades key on portfolio plus investment number", "Quote statuses include covered, tied"). Each `detail` should open with what the stage is for; see the "why" drafts below for two of them.

## 2. Missing "why" sentences

- Oversight stage, "A second limit framework next to compliance" — add: "They are separate because they answer different questions. Compliance asks whether a trade is allowed by law or mandate, so it must block an order before it leaves. Risk Governance asks whether the portfolio's modelled exposure (tracking error, VaR) is where the risk team wants it, which can only be judged after analytics run and is resolved by discussion, not by rejecting a trade."
- HOPS 5, "Heavy operations do not block the HTTP call." — add: "A batch post can carry hundreds of orders, and each one runs every rule assigned to its portfolio. Holding an HTTP connection open for that long would time out at the gateway and tie up a worker, so the service acknowledges at once and does the work behind an operation id the caller can come back for."
- DOMDESC portfolio, "The Portfolio entity has 850 attributes" — add: "It is that large because the portfolio is where every other domain's configuration meets: compliance reads the mandate, trading reads the routing, accounting reads the valuation rules, risk reads the benchmark. One entity shared by all of them is the price of 'one booked trade updates every view'."
- QUIZ "What is CIDS for?" and DOMDESC portfolio_management — add: "Clients have proprietary inputs, such as internal ratings or ESG scores, that they want screens, rules and reports to use. Without CIDS they export positions to Excel to join them; with CIDS the join happens inside Aladdin, and BlackRock never has to understand or transform the client's data."

## 3. Anatomy of one request

It is currently six hops with no stated lesson, and the timeline is contradictory: hop 3 says the service "returns a long-running operation id immediately rather than the result", yet hop 4 says rules run "before it is accepted" and only hop 5 introduces the LRO. Suggestions:
- Lead "Follow a portfolio manager's order from a Python script" — add: "Watch for three things: two separate permission checks, compliance running inside the order post rather than as its own call, and the HTTP response coming back before the work is done."
- Label each hop synchronous or asynchronous, and move the operation-id response into hop 3 as a second codebox so the reader sees two responses: the immediate acknowledgement and the later result.
- Hop 4 "With runCompliance set, assigned rules run" — say what the two flags change: "whatIf: true runs the same checks and discards the order, which is how a PM tests a rebalance; runCompliance: false books it without the pre-trade check." (Confirm the second half against the spec before publishing.)
- Hop 2 "The SDK can also rewrite URLs for an enterprise gateway" is a tangent; cut it.
- Hop 6 already fans out to cash ladder and levels; make that the closing sentence of the lesson and link it to the Lesson 1 figure.

## 4. Weakest Convention "why" texts

- Protobuf under REST: "One definition serves gRPC internally and REST externally" — replace with: "The contract for each service is written once. BlackRock's own apps and client scripts both read from it, and the Python SDK is generated from it rather than typed by hand, so the public API and the internal one cannot drift apart. For a product manager that means a new field reaches clients the day it ships, not after a documentation sprint."
- Internal expression languages: "A tell that these APIs wrap mature internal tools" — replace with: "These APIs are doors into tools BlackRock's desks have used for years. The client gets the real thing, but filtering may require a query language never designed for outsiders, and BlackRock cannot simplify it without breaking its own apps. Expect this to be where Studio onboarding is hardest."
- Runner-up: "Studio is the code-level expression of a principle" is too abstract to land.

## 5. Flashcards

- "The specs show each of those reading position data." is vague for the page's central claim. Replace with: "Level reads positions for room-to-limit, CashLadder folds in open orders and collateral, CollateralStatement reads positions for margin, AborLot is created from the trade, RiskRule evaluates analytics computed on the same positions."
- "owner types are PM, trader and hybrid" appears nowhere else on the page; either add it to the Order stage or drop it.
- "unfunded commitments and optional prefunding" likewise only appears in the answer.
- "Compliance is a property of the Order API, not a separate call." is also slightly wrong, since the compliance domain has four APIs. Replace with: "Pre-trade compliance runs inside the order post. The Compliance APIs manage rules and read levels; they do not check an order."
- Counts check out: 10 APIs with lro:true, 24+6+23+1 = 54.

## 6. Mannered writing

No em-dash asides. Recurring "not X but Y": "lifted from those documents, not from marketing"; "fields on the records, not a separate workflow tool"; "platform query languages, not only JSON"; "Consistency is enforced in review, not by hope" (replace: "Consistency is a review gate, and each exception is written down"). Stock or marketing phrases: "Positioned as the extensibility layer"; "Knowing these makes you sound like you have read the platform, because you have" (replace: "They appear in the API text, so an interviewer will recognise them"). Fragments posing as sentences: "Treated like test-driven development."; "Explains why hosting can move client by client". "thirty-year-old entitlement model" is an unsupported number; say "a pre-OAuth entitlement model".

## 7. Terminology

- Risk Governance versus Risk Radar: DOMDESC defines the pair, but the Oversight stage never names either ("A second limit framework"). Use "Risk Governance (rules) in Risk Radar (the app)" on first mention in each lesson.
- The Oversight stage has dom:'analytics' but its EnrichedCapitalFlow API lives in the clients domain, so "Open analytics in the explorer" hides capital flows. Either split the stage or note the second domain.
- Domains lead uses `agraph.<domain>` without saying it is Aladdin Graph; add "(Aladdin Graph)".
- Three keys: "application key", "X-API-Key client key", "VND.com.blackrock.API-Key". State once in the Gateway layer that the application key identifies the Studio app and the client key is an alternative to OAuth for the user.
- "environment", "tenant", "instance" are used interchangeably for the same thing; pick "environment" and say "tenant" once in parentheses.
- "Studio", "Aladdin Studio", "Studio Developer": the glossary implies Studio Developer is a product, PRODUCTS does not list it. Say in PRODUCTS that Studio Developer is the developer-facing half of Aladdin Studio.
- "OrderAPI" (HOPS, explorer) versus "Order API" (QUIZ); standardise on "Order API" in prose.
