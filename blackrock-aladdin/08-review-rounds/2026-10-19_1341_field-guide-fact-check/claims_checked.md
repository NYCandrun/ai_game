# Claims made by the Aladdin Field Guide artifact (extracted copy, for fact-checking)


## Section: overview
role="tabpanel" aria-labelledby="h-overview">
What Aladdin is 
Aladdin is the software BlackRock built to run its own investment business, then sold to other institutions. One system holds what each portfolio owns, every order and trade, the rules each portfolio must obey, the cash it has available, its accounting records and its risk numbers. The product's value is that one booked trade updates every one of those views at once. 
The investment process in six roles 
A client hands money and a mandate to an asset manager. A portfolio manager decides what to buy or sell and raises an order . A trader executes it with a broker . A day or two later the trade settles : cash and securities change hands at the custodian , the bank that holds the client's assets. Accountants record each purchase as a lot and compute the fund's daily price, the NAV . Compliance and risk teams check every step against the mandate and regulation. Aladdin is the one system all six roles share. 
[figure caption] scroll sideways → One trade, six consequences. The holdings it changes are read by the compliance check (how close each rule is to its limit), the cash forecast by settlement day, the collateral owed on derivatives, the accounting lots and NAV, and the risk rules. The trade is also confirmed with the broker and copied to the client's Data Cloud. Each arrow is a dependency visible in the API specs; the coloured bands are the office tier that owns each view. 
 54 / 301 public APIs and operations this guide is built from 
 11 API domains, one per business function 
 ~100 front-end apps on the platform 
 ~4,000 engineers maintaining it 
 $1BN+ technology business, revenue up 13% in Q2 2026 
Who uses it 
Asset managers, insurers, pension funds, wealth managers, banks and corporate treasuries. Institutional clients only; no retail investors. 
How it is delivered 
Hosted software. Each client gets its own Aladdin environment (a tenant), and BlackRock staff can be granted access into it as "provider" users. Hosted on Microsoft Azure today, with an AWS option expected in late 2026. 
How this guide reads it 
From the 54 machine-readable API descriptions (OpenAPI specs) in BlackRock's public SDK packages. Every field, state and internal name here comes from those documents. 
 How to read this. Lessons 2 to 3 explain what the platform does. Lessons 4 to 6 explain how it is built and are written for engineers and technical product people; a non-engineer can skim them. Move between lessons with the tabs, the arrow keys, or the buttons at the foot of each lesson. Click the nodes in the diagrams.

## Section: lifecycle
role="tabpanel" aria-labelledby="h-lifecycle">
The investment lifecycle Aladdin covers 
Each stage hands a record to the next, and the hand-off is a state change on that record. Click a stage to see the record it owns, the states it moves through, and the APIs that move it. 
[figure caption] scroll sideways → The coloured band on each stage is its office tier: blue front office (decides and acts), amber middle office (controls), green back office (settles and accounts). The word under each arrow is what one stage hands to the next. 
 ← Previous stage Next stage →

## Section: domains
role="tabpanel" aria-labelledby="h-domains">
Domain explorer 
The API layer is called Aladdin Graph, and every API in it has an address of the form agraph.<domain>.<segment>.<group>.<version>.<API> . The domain is the business function that owns it. Pick a tier or a domain, filter by stability, or search all 54 public APIs. 
 All tiers 
 Front office 
 Middle office 
 Back office 
 Platform 
 Search 
 Stability 
 any stable beta alpha sunset

## Section: architecture
role="tabpanel" aria-labelledby="h-architecture">
How it is layered 
Every caller, whether a BlackRock app, a client script or Copilot, enters through the same gateway and the same domain services. There is no privileged path. Click a layer to see what the specs say about it. 
[figure caption] scroll sideways → The specs describe the middle three layers directly. The top and bottom come from BlackRock's announcements and job postings.

## Section: request
role="tabpanel" aria-labelledby="h-request">
Anatomy of one request 
Follow a portfolio manager's order from a Python script to a booked order with a compliance verdict. Watch for three things: two separate permission checks, compliance running inside the order post rather than as its own call, and the HTTP response coming back before the work is done. 
[figure caption] scroll sideways →

## Section: conventions
role="tabpanel" aria-labelledby="h-conventions">
Design conventions you can see in every spec 
The same dozen patterns repeat across all 54 APIs, which is itself the finding: the platform is governed, not grown. Each card gives the pattern, the evidence in the documents, and why it matters to someone building on or running the platform.

## Section: products
role="tabpanel" aria-labelledby="h-products">
The product family 
The products are entry points onto one set of positions and portfolios, not separate systems. A client that buys Aladdin Risk and later adds the full platform does not reload its data. The APIs in this guide belong to the core; Studio is how clients build on it.

## Section: ai
role="tabpanel" aria-labelledby="h-ai">
Where AI plugs in 
Aladdin Copilot is an assistant embedded across the apps. When it needs data or wants to act, it calls Aladdin APIs as "tools", the same governed APIs Studio exposes to clients. That is why API quality and AI readiness are one problem for the platform team. 
[figure caption] scroll sideways → From a 2025 BlackRock AI engineering talk. Tool access is filtered by environment, user group and application before planning, because more than 40 to 50 tools degrades the planner. 
Federated ownership 
The central AI team owns orchestration, guardrails and evaluation. Domain teams onboard by registering existing production APIs as tools or by building custom agents. That mirrors the domain split in the API namespace. 
Evaluation-driven development 
Synthetic data, subject-matter-expert cases and model-graded pipelines run on every pull request and nightly, with reports per plugin owner. The team compares it to test-driven development. 
Why it matters for Studio 
An agent can only use an API that describes itself well: clear metadata, consistent methods, fine-grained scopes. The Studio Developer product postings list AI-assisted developer tooling among the role's concerns.

## Section: glossary
role="tabpanel" aria-labelledby="h-glossary">
Names that leak through the docs 
Internal systems, modules and jargon the API descriptions mention by name. They appear in the API text itself, so an interviewer will recognise them.

## Section: quiz
role="tabpanel" aria-labelledby="h-quiz">
Test yourself 
Click a card to reveal the answer. Then use the questions at the bottom in the interview; each one comes from something in the specs. 
Questions worth asking them 
Of the public APIs, nearly half are alpha. How does an API graduate to stable, and how do you handle clients who built on alpha when it changes? 
Compliance and Risk Governance are two limit frameworks with separate rules, exceptions and workflows. Are they converging? 
What share of Studio usage is BlackRock's own teams versus clients, and what is the path from internal success to external adoption? 
Is the Copilot plugin registry fed from the same catalog as the Studio developer portal, or are they separate? 
Where is the line between exposing something as an API, as a Data Cloud dataset, or as an event stream? 
The specs still cite legacy permission codes under OAuth scopes. Is the goal to retire those, or to keep two layers? 
What changes for Studio when a client is hosted on AWS rather than Azure?

## Section: sources
role="tabpanel" aria-labelledby="h-sources">
Sources and caveats 
Primary evidence 
The 11 asdk_plugin_* packages on PyPI, version 2.0.0b3: 54 Swagger 2.0 specs, 301 operations, read in full. 
 blackrock/aladdinsdk and aladdinsdk-plugin-builder on GitHub. 
 BlackRock Aladdin Studio and APIs pages. 
 Aladdin Data Cloud press release , 2021. 
Secondary evidence 
 AWS partnership announcement , December 2025. 
 Microsoft customer story on the Azure migration. 
 Summary of a 2025 BlackRock AI engineering talk (third party). 
BlackRock careers postings for Studio Developer product and engineering roles, 2025 and 2026. 
 Q2 2026 results coverage . 
 What is not here: positions, risk analytics outputs, performance, pricing, benchmarks, execution connectivity, settlement messaging, eFront and wealth APIs. They sit behind the client login to the Studio developer portal. Inferences about gRPC, the linter and internal system names come from field names and comments inside the specs, not from BlackRock architecture documents.
[diagram] A booked trade creates positions. Those positions are read by compliance levels, the cash ladder, collateral exposure, accounting lots and risk exceptions. The trade is also confirmed via the broker and lands in the client's data cloud.
[diagram] Nine stages from research to oversight. The label under each arrow is what is handed to the next stage: idea, mandate, order, verdict, trade, settled trade, income, NAV.
[diagram] Five layers: consumers, gateway and identity, Aladdin Graph domain services, data and engines, and hosting.
[diagram] Six hops: SDK, gateway, Order API, compliance engine, long-running operation store, poll for result.
[diagram] Copilot pipeline: a prompt passes context collection, input guardrails, tool filtering to 20 to 30 tools, a plan and act loop that calls Aladdin APIs, output guardrails, then an answer.
[diagram] Filter glossary

## Data: DOMDESC
{
 accounting:'"Aladdin Accounting": the accounting book of record. Lots (each purchase tracked separately for cost) with a parallel investment-book lot id, the NAV valuation workflow with sign-off and exceptions, membership of performance composites, and per-portfolio accounting configuration.',
 analytics:'Two things live here. Sustainability data feeds (Climate and multi-vendor ESG), and Risk Governance, the risk team's limit framework, which lives in an app called Risk Radar: rules, subscriptions of portfolios to rules, overrides, custom metrics, exceptions and the workflows that resolve them.',
 clients:'Capital flows: money moving into and out of funds as subscriptions and redemptions, in cash or in kind, estimated or actual. Records move through authorise and confirm actions and a true-up against the fund accountant's prices. The specs call the underlying module newcash.',
 compliance:'Rule-based checking that each portfolio obeys regulation, its mandate and internal guidelines. Rule types (prohibition, concentration, value at risk, disclosure, scripted, counterparty), assignments of rules to portfolios with four-eyes review, intraday "room to limit" levels, and violations that name the positions responsible.',
 data:'The security master write interface. One API creates the instruments Aladdin can price and book: credit default swaps and indices, equities, options, futures, FX spot, forward, swap, non-deliverable forward and options, interest rate and total return swaps, swaptions, time deposits, repo and mortgage TBAs.',
 investment_operations:'The largest domain, and where the write-heavy operational work lives: corporate actions and the elections sent to custodians, floating-rate coupon resets, mortgage factors, cash payments with settlement instructions and transmission, daily collateral statements, and the broker, desk, settlement-instruction and contact reference data.',
 investment_research:'A research management system: templated notes, logged meetings with companies, which analyst covers which issuer, watchlists with pre-trade notes, and stored screening expressions that evaluate over securities and alert on a schedule.',
 platform:'Identity and administration (users, hierarchical groups, graded permissions) plus the dataset registry behind Aladdin Data Cloud, which shows per-client Snowflake databases with draft, review and released states.',
 portfolio:'The portfolio master. The Portfolio entity has 850 attributes because the portfolio is where every other domain's configuration meets: compliance reads the mandate, trading reads the routing, accounting reads the valuation rules, risk reads the benchmark. One entity shared by all of them is the price of "one booked trade updates every view". Groups form a hierarchy; restricted assets block trading per portfolio.',
 portfolio_management:'Tools the portfolio manager works with between deciding and ordering: strategies that tag orders and trades with intent, a settlement-date cash ladder that folds in open orders and collateral, and CIDS. Clients have proprietary inputs such as internal ratings or scores that they want screens, rules and reports to use. Without CIDS they export positions to Excel to join them; with CIDS the join happens inside Aladdin, and BlackRock never has to understand or transform the client's data.',
 trading:'Order (a portfolio manager's instruction to the desk, with dry-run and compliance flags on post) and BlockTrade (one execution split across the portfolios that ordered, with the broker quotes received in competition, settlement currency details and, for repo and FX, the extra legs).'}

## Data: STAGES
[
 {id:'research',short:'Research',dshort:'research',tier:'front',name:'Research',dom:'investment_research',what:'Analysts record their thinking: templated notes, logged meetings with companies, who covers which issuer, watchlists, and stored screening rules that alert when a security meets them.',entity:'ResearchNote, Engagement, Watchlist, Criterion',apis:['ResearchNote v2','Engagement','AnalystCoverage','Watchlist','Criterion'],states:['draft','published'],why:'Research is where an idea starts, and the platform keeps it attached to the issuer or security it is about, so a later order can be traced back to the note that justified it.',detail:'Screening criteria are real expressions evaluated over security identifiers, such as ((price > 55 OR oas = 75) AND market_cap < 1mm). Notes carry permission groups that expire, so research can be shared for a bounded time.'},
 {id:'setup',short:'Setup',dshort:'portfolio',tier:'front',name:'Portfolio setup',dom:'portfolio',what:'A portfolio is created with its mandate (the client's rules on what it may hold), the index it is measured against, cash and sweep rules per currency, routing of trade confirmations to its custodian, and its legal and regulatory classification.',entity:'Portfolio (850 attributes), PortfolioGroup, RestrictedAsset',apis:['PortfolioToolkit','PortfolioGroup','RestrictedAsset','CIDReader / CIDWriter'],states:['inception','active','terminated'],why:'Every other stage reads this record. The 850 attributes exist because compliance, trading, accounting and risk each keep their configuration on the same portfolio rather than in their own copies.',detail:'Relationship types show the fund structures the platform models natively: master-sleeve, master-feeder, create-redeem, common pool and model suites. Clients add their own data through CIDS.'},
 {id:'order',short:'Order',dshort:'trading',tier:'front',name:'Order',dom:'trading',what:'The portfolio manager (who decides what to buy) raises an order, an instruction to the trading desk (who buys it in the market). It records the strategy behind the decision, price limits, and the benchmark the execution will be judged against.',entity:'Order (PM order, then trader order)',apis:['Order v1','Strategy','CashLadder v2'],states:['Open','Compl Pending','Authorized','Active','Booked'],why:'Separating the decision (order) from the execution (trade) is what lets compliance run on intent before any money moves, and lets one trade later be split across many orders.',detail:'Posting an order accepts a dry-run flag and a run-compliance flag, so a manager can test a rebalance without booking it. The cash ladder shows the cash the order will consume on its settlement date, counting other open orders and collateral already committed.'},
 {id:'compliance',short:'Compliance',dshort:'compliance',tier:'middle',name:'Pre-trade compliance',dom:'compliance',what:'Rules assigned to the portfolio run against the order before it is accepted. Each violation comes back with a severity, warning or restriction, and the positions that caused it.',entity:'ComplianceRule, ComplianceRuleAssignment, Level, Violation',apis:['ComplianceRule','ComplianceRuleAssignment','Level','Violation'],states:['passed','warning','restriction'],why:'Compliance asks whether a trade is allowed by law or mandate, so it has to answer before the order leaves. That is why it runs inside the order post and can block it, rather than reporting afterwards.',detail:'Rule types: prohibition, concentration, value at risk, disclosure, scripted, counterparty. A rule itself moves through draft, ready for testing, review required and approved before it can be assigned. Levels show intraday "room to limit" per rule.'},
 {id:'trade',short:'Execute',dshort:'trading',tier:'front',name:'Execution and allocation',dom:'trading',what:'The desk executes with a broker, the outside firm that deals in the market, as one block trade. The block is then allocated (split) across the portfolios whose orders it filled, with the quotes received from competing brokers recorded.',entity:'BlockTrade, then one Trade per portfolio',apis:['Trade v2','Broker','BrokerDesk','SecurityCreation'],states:['entered','authorised','confirmed','settled'],why:'One execution for many portfolios gets a better price and one confirmation; allocating it afterwards is what keeps each portfolio's records separate.',detail:'A trade is identified by portfolio, investment number and trade number, with a touch count and version so two users cannot overwrite each other. Quote outcomes recorded include covered, tied, done away and did not trade.'},
 {id:'settle',short:'Settle',dshort:'inv. ops',tier:'back',name:'Settlement and cash',dom:'investment_operations',what:'The trade is confirmed with the broker's desk, settlement instructions say which accounts cash and securities move between, and payments go out through a transmission framework once two people have signed off.',entity:'BrokerConfirmRouting, CounterPartySettlementInstruction, MiscellaneousCashflow',apis:['BrokerConfirmRouting','CounterPartySettlementInstruction','Contact','MiscellaneousCashflow'],states:['entered','confirmed','reviewed','transmitted'],why:'Settlement is where mistakes cost real money, so the platform models the reference data (who to confirm with, where to send cash) as governed records with review states, not free text on a trade.',detail:'Sending money out requires both a confirmer and a reviewer on the record. Settlement instructions carry approved and review states and a soft delete so history is never lost.'},
 {id:'lifecycle',short:'Lifecycle',dshort:'inv. ops',tier:'back',name:'Asset lifecycle',dom:'investment_operations',what:'Holdings generate events over time. A corporate action (a dividend, split or takeover offer) creates an entitlement for every portfolio that holds the security, which must be elected and instructed to the custodian. Floating coupons reset, mortgage factors arrive, and collateral statements are generated daily for derivatives.',entity:'CorporateAction, Entitlement, CouponReset, PrincipalInterestFactor, CollateralStatement',apis:['CorporateAction','CorporateActionEntitlement','CouponReset','PrincipalInterestFactor','CollateralStatement'],states:['elected','authorised','instructed','processed'],why:'None of this is a trade, yet all of it changes what a portfolio holds and is owed. Modelling these events as first-class records is what keeps positions correct between trades.',detail:'Elections are checked against compliance before instruction. Collateral statements come from margin calculators reading the legal agreements (ISDA and credit support annexes) set up in a tool called DECO.'},
 {id:'accounting',short:'Accounting',dshort:'accounting',tier:'back',name:'Accounting and NAV',dom:'accounting',what:'Trades become lots in an accounting book of record. A valuation workflow prices the portfolio, lists exceptions, and after sign-off publishes the NAV, the fund's daily per-share value.',entity:'AborLot, Valuation, ValuationException, CompositeMembership',apis:['AborLot','Valuations','CompositeMembership','PortfolioConfiguration'],states:['snapshot','exceptions','signed off','published'],why:'The investment book and the accounting book answer different questions and are kept separately; carrying both lot ids on one record is how they are reconciled without a nightly file.',detail:'Valuations record Dietz and total return fields and a NAV impact per exception. Composite membership tracks which portfolios count toward a published performance record.'},
 {id:'oversight',short:'Oversight',dshort:'analytics',tier:'middle',name:'Oversight and client flows',dom:'analytics',dom2:'clients',what:'Risk teams subscribe portfolios to metric rules in Risk Governance (the rules) within Risk Radar (the app), evaluate them, and work breaches through assigned workflows. Separately, client money arrives and leaves as capital flows.',entity:'RiskRule, RiskException, RiskWorkflow, EnrichedCapitalFlow',apis:['RiskRule','EvaluatorAnalytics','RiskException','RiskWorkflow','EnrichedCapitalFlow','Climate','EsgData'],states:['OK','warning','breach','workflow resolved'],why:'This is a second limit framework next to compliance, and they are separate because they answer different questions. Compliance asks whether a trade is allowed and must block it in time. Risk Governance asks whether modelled exposure (tracking error, value at risk) is where the risk team wants it, which can only be judged after analytics run and is resolved by discussion, not by rejecting a trade.',detail:'Limits can be absolute (250 basis points of tracking error) or relative to a benchmark, with look-through into funds the portfolio holds. Capital flows live in the clients domain.'}
]

## Data: PRODUCTS
[
 {n:'Aladdin Enterprise',t:'The core platform: portfolio management, risk analytics, trading, compliance, operations and accounting across public markets. The 11 API domains in this guide belong here.'},
 {n:'Aladdin Risk',t:'The risk analytics engine offered on its own: factor exposures, value at risk, scenario and stress testing. Its outputs are the metric source for the Risk Governance rules in the analytics domain.'},
 {n:'Aladdin Studio',t:'The data and developer platform: the Aladdin Graph APIs with a login-only developer portal, the open-source Python SDK and plugins, Aladdin Data Cloud, hosted Compute for Python, and Excel and data-exchange tools. Studio Developer is its developer-facing half, which BlackRock's product postings describe as the platform's extensibility layer.'},
 {n:'Aladdin Data Cloud',t:'Each client gets its own Snowflake database preloaded with front-to-back Aladdin data, to join with their own and third-party data. The AdcDataset API shows draft, review and released dataset states and ETL configuration.'},
 {n:'Aladdin Copilot',t:'Generative AI assistant across the apps, launched 2023 on Azure OpenAI. A supervisor agent with a federated plugin registry where domain teams register existing APIs as tools. See the AI lesson.'},
 {n:'Aladdin Wealth',t:'Portfolio analytics and proposals for wealth managers and advisers, with an AI commentary tool added in October 2025.'},
 {n:'Aladdin Climate',t:'Physical, transition and temperature-alignment risk analytics. The Climate API returns metrics per security, deal or issuer under named scenarios and timeframes.'},
 {n:'eFront and Preqin',t:'Private markets: eFront (acquired 2019) for post-investment workflow and risk, Preqin (acquired March 2025) for pre-investment data. Combined as eFront Insight in February 2026.'}
]

## Data: LAYERS
[
 {id:'consumers',y:20,h:62,name:'Consumers',sub:'~100 Aladdin apps · Studio (SDK, notebooks, Compute) · Copilot tools · client systems',
  body:' Who calls the APIs  BlackRock's own front-end applications (Risk Radar, DECO, CID Manager, the ADC Admin Center and about a hundred others), client code written against the Studio SDK or raw REST, notebooks running in Aladdin Compute, and Copilot, whose registered tools map to these same APIs. The SDK generates its clients from the published specs and adds retries, rate limiting, pagination and polling of long-running operations. '},
 {id:'gateway',y:98,h:62,name:'Gateway and identity',sub:'application key · OAuth 2.0 token with per-resource scopes · per-client environment',
  body:' How a call is admitted  Every request carries an application key registered in Studio ( VND.com.blackrock.API-Key ), which identifies the calling app. The user behind the call is identified by one of: an OAuth 2.0 token (authorization code or client credentials flow), a client key header, or basic auth. A scope is a permission string attached to the token, and here scopes are per resource, for example  trading.order_management.order.v1.Order:write . OAuth endpoints sit at  client.blackrock.com . Inside the service a second layer applies: Aladdin permission codes such as  brkrMaint  or  PortGroupMOD  that the user's group must hold. '},
 {id:'graph',y:176,h:110,name:'Aladdin Graph domain services',sub:'11 domains · defined in protobuf, served over gRPC, translated to REST · Google API conventions, linted',
  body:' The service layer the specs describe  Protobuf is Google's schema language for describing messages and services; gRPC is the binary protocol that serves them. Every Aladdin spec carries the fingerprints of both (gRPC status types, update masks, page tokens, LongrunningOperation, enums named  FOO_UNSPECIFIED ), which means the services are defined once in protobuf and translated to ordinary REST and JSON at the edge. URLs follow  /api/&lt;domain&gt;/&lt;segment&gt;/&lt;group&gt;/v1/ . Inline comments such as  api-linter: aladdin::9016 … aip.dev/not-precedent  show BlackRock runs Google's API linter plus its own rule set, and that exceptions need a written reason. The commonest reason given is that changing a URI "will break all citizen developers code", BlackRock's term for finance staff who write some code. '},
 {id:'data',y:302,h:62,name:'Data and engines',sub:'positions and ledgers · ADL data layer · compliance engine · margin calculators · Aladdin Analytics · Snowflake (ADC)',
  body:' What the services read and write  Positions, lots and ledgers come first; the specs cite a ledger summary table and an accounting system whose fields are prefixed "alpha". A data layer the specs call ADL holds dataset repositories and portfolio search. The compliance engine runs in parallel or live mode. Margin calculators read DECO agreements. Aladdin Analytics is the metric source for risk rules. Aladdin Data Cloud is a Snowflake database per client. A BQL expression language appears in filters and routing rules. '},
 {id:'hosting',y:380,h:28,name:'Hosting',sub:'Microsoft Azure today · AWS option announced Dec 2025, GA H2 2026 · Kubernetes container platform',
  body:' Where it runs  Hosted on Microsoft Azure after a client-by-client migration from BlackRock's own data centres; Microsoft Treasury was the first environment moved. A December 2025 AWS partnership adds AWS hosting, with general availability expected in the second half of 2026 and Amazon Treasury as an early adopter. Job postings describe an Aladdin Container Platform on Kubernetes with a Go control plane and Prometheus and Grafana observability. The specs themselves are hosting-neutral. '}
]

## Data: HOPS
[
 {name:'Python script',sub:'AladdinSDK',cap:'A portfolio manager's script posts a batch of orders through the SDK.',body:' 1. The call  synchronous  The SDK validates the request body, attaches the application key and an OAuth bearer token, and sends one HTTP request. Configuration comes from layered settings files; run mode is local, compute or test.  POST /api/trading/order-management/order/v1/orders:batchPost
VND.com.blackrock.API-Key: &lt;app key from Studio&gt;
Authorization: Bearer &lt;token with scope …Order:write&gt;

{"postOrderConfig":{"whatIf":false,"runCompliance":true,"complianceTimeout":"30s"},
 "orders":[{"assetReference":{"isin":"US0378331005"},"transactionType":"BUY",
   "orderDetails":[{"portfolioReference":{"portfolioTicker":"EQ_CORE"},"quantity":10000,"strategyName":"Q4 rebalance"}]}]} '},
 {name:'Gateway',sub:'client.blackrock.com',cap:'The gateway checks the app key, the token and its scope for this client's environment.',body:' 2. Admission (first permission check)  synchronous  The application key identifies the registered Studio app. The token must carry the resource scope  trading.order_management.order.v1.Order:write . Rate limits and the client environment are resolved here. Nothing about the order itself has been examined yet. '},
 {name:'Order API',sub:'trading domain service',cap:'The order service resolves references, checks the user's Aladdin permissions, and acknowledges at once with an operation id.',body:' 3. The domain service (second permission check)  synchronous, then hands off  Asset references resolve by ISIN, CUSIP, SEDOL, RIC or a client alias; portfolio references by ticker or id. The user behind the token must hold the order-raising permission in their Aladdin user group. Because this is a batch post, the service does not wait for the work: it returns an operation id immediately and continues in the background.  202 Accepted
{"id":"9f1c…","done":false} '},
 {name:'Compliance',sub:'rules bound to EQ_CORE',cap:'In the background, the rules assigned to the portfolio run against each order.',body:' 4. Pre-trade compliance  asynchronous, inside the service  Rule assignments for the portfolio fire: prohibition, concentration, counterparty and scripted rules, each with warning or restriction severity. Violations list the contributing positions. A restriction stops the order; a warning rides along in the result. The flags on the request control this step:  runCompliance  defaults to true;  whatIf  runs the same checks without booking, which is how a manager tests a rebalance;  complianceTimeout  caps how long to wait, and if it expires the order is posted in a "Compl Pending" status regardless of outcome. '},
 {name:'LRO store',sub:'longrunningoperations/{id}',cap:'When the batch finishes, the result is written to the long-running operation record.',body:' 5. Long-running operation  asynchronous  A batch post can carry hundreds of orders, and each one runs every rule assigned to its portfolio. Holding an HTTP connection open for that long would time out at the gateway and tie up a worker, so the service acknowledges at once and does the work behind an operation id the caller can come back for. The record carries done, error and response fields. Ten public APIs expose this pattern and 35 operations are flagged as long-running. '},
 {name:'Poll and result',sub:'SDK polls, returns result',cap:'The SDK polls the operation until done and hands back order ids, versions and any violations.',body:' 6. Back to the script  synchronous polling  GET /api/trading/order-management/order/v1/longrunningoperations/9f1c…
{"id":"9f1c…","done":true,
 "response":{"results":[{"output":{"order":{"id":"8812345","orderStatus":"Open","version":1},
   "complianceViolations":[{"complianceSeverity":"COMPLIANCE_SEVERITY_WARNING","ruleAssignmentName":"Max 5% single issuer"}]}}]}}  The SDK deserialises the response and can convert it to a pandas table or export it. From here the order appears in the cash ladder as an open order and in compliance levels as as-traded exposure. Once executed it becomes a trade with allocations, and the fan-out in the Overview figure begins. '}
]

## Data: CONV
[
 {t:'Resources plus custom methods',p:'Google-style URIs: a collection, then a colon verb for anything that is not plain create, read, update or delete.',e:'POST /orders:filter, /orders:batchPost, /order:cancel, /brokerDesks:undelete, /workflows:listRevisions. 36 filter, 17 batchCreate and 13 batchUpdate methods across the public set.',w:'A client learns one grammar once and can guess the shape of an API they have never seen. Filtering by POST with a criteria body allows large, structured queries that would not fit in a URL.'},
 {t:'Long-running operations',p:'Bulk and heavy calls return an operation id; the caller polls for done, error and response.',e:'GET /longrunningoperations/{id} in 10 APIs, 35 operations flagged x-aladdin-lro. Order and trade batch posts, risk evaluation, ADC dataset registration.',w:'A request that would take minutes does not hold a connection open or time out at the gateway. The cost is that callers must handle "not yet", and retries have to be safe to repeat.'},
 {t:'Stability labels and independent versions',p:'Every API is stamped alpha, beta, stable or sunset and versioned on its own.',e:'x-aladdin-api-stability: 24 alpha, 6 beta, 23 stable, 1 sunset. Order v1 beside Trade v2; CashLadder v2 keeps a GET "solely for backward compatibility".',w:'Clients can see how much to trust an endpoint, and BlackRock can evolve one domain without re-versioning the whole catalog. Nearly half the public surface being alpha is the product problem that follows.'},
 {t:'Linter-enforced design with written exceptions',p:'Google's API linter plus BlackRock's own aladdin:: rules run on every spec, and deviations must be justified inline.',e:'api-linter: aladdin::9016::query-custom-method-http=disabled aip.dev/not-precedent: "changing existing URI will break all citizen developers code".',w:'Consistency is a review gate, and each exception is written down. The recurring justification tells you that not breaking existing client code outranks design purity.'},
 {t:'Protobuf under REST',p:'Services are defined once in protobuf (Google's schema language) and exposed over REST by translation.',e:'rpcStatus (google.rpc.Status), Any with @type, google.type.DateTime, updateMask, pageToken, enums named FOO_UNSPECIFIED, request messages like v1FilterOrdersRequest.',w:'The contract for each service is written once. BlackRock's own apps and client scripts both read from it, and the Python SDK is generated from it rather than typed by hand, so the public API and the internal one cannot drift apart. For a product manager that means a new field reaches clients the day it ships, not after a documentation sprint.'},
 {t:'Governance in the data model',p:'Maker-checker approval (one person proposes, another approves) and lifecycle states are fields on the records themselves.',e:'Compliance rules: draft, testing, review, approved. ADC datasets: draft, review, released with four-eyes. Cash transmissions need confirmedBy and reviewedBy. Elections: elected, authorised, instructed, processed.',w:'Control evidence is produced by normal operation. Regulated clients audit exactly this, and it means no separate workflow tool has to be kept in sync.'},
 {t:'Bitemporal records and audit',p:'Records carry two timelines, when something was true and when it was entered, plus a touch count and version.',e:'validBeginDate and validEndDate, entryTime and expiryTime, asOfDate on queries, touchCount and version on trades and orders, Audit APIs for brokers and factors, listRevisions on rules and workflows.',w:'Supports as-was reporting ("what did we know on the 3rd"), and lets two users edit without locks because a stale version is rejected.'},
 {t:'Two-layer authorisation',p:'OAuth scopes at the gateway, Aladdin permission codes inside the service.',e:'Scope trading.order_management.order.v1.Order:read; spec text "Users needs to have permissions under permType='brkrMaint'", "You must have the Aladdin Permission PERMS_GROUP_MOD".',w:'Modern API security sits on top of a pre-OAuth entitlement model that the hundred internal apps still use. Any change to permissions has to respect both layers.'},
 {t:'Bulk by default, with dry runs',p:'Most writes are batches with caps, and many offer validate-only.',e:'190 of 301 operations are POST. Caps of 100 per request for brokers, 1,000 for restricted assets, 10,000 rows per page. :batchValidate on brokers, desks and capital flows; validateOnly on cashflows; whatIf on orders.',w:'Operations teams load reference data in files, and the API matches how they work: check the whole file first, then commit it.'},
 {t:'Multi-tenant by construction',p:'Each client is its own environment, and the model carries the tenant everywhere.',e:'clientAbbreviation on datasets, accountCode on external references, a per-client ADC database, reconciliation of one client against a "gold-copy" client, provider users granted into a client.',w:'This is why hosting can move one client at a time, and why offering a second cloud is feasible without re-architecting.'},
 {t:'Client extensibility in the schema',p:'The data model expects clients to bring their own data and logic.',e:'CIDS datasets, custom evaluation metrics for risk rules, custom fields on orders, trades and research notes, scripted compliance rules, research criteria expressions, user-defined fields on portfolios.',w:'Clients can adapt the platform without asking BlackRock for a change. Studio extends the same principle from data fields to code.'},
 {t:'Internal expression languages',p:'Filters and routing rules are written in platform query languages as well as JSON.',e:'bqlExpression, bqlFilter, skipBqlValidation, "refer to BQL ord_flags", jql on trade routing, scripted compliance rules.',w:'These APIs are doors into tools BlackRock's desks have used for years. The client gets the real thing, but filtering may require a query language never designed for outsiders, and BlackRock cannot simplify it without breaking its own apps. Expect this to be where Studio onboarding is hardest.'}
]

## Data: GLOSS
[
 ['Aladdin Graph (AGraph)','The unified API layer. Spec ids start agraph. …; the "agraph team" agrees naming.'],
 ['Studio','The data and developer platform: APIs, portal, SDK, Data Cloud, Compute. Studio Developer is its developer-facing half.'],
 ['ADC','Aladdin Data Cloud: per-client Snowflake databases of Aladdin data, managed through an Admin Center.'],
 ['ADL','A data layer the specs reference as the store for ADC dataset repositories and for portfolio search.'],
 ['Risk Radar','The oversight application where Risk Governance rules, exceptions and workflows are surfaced. The analytics/oversight APIs serve it.'],
 ['Risk Governance','The risk team's limit framework (rules, subscriptions, exceptions, workflows), distinct from compliance.'],
 ['DECO','The tool where collateral legal agreements (ISDA, CSA) are set up. Margin calculators read it to generate collateral statements.'],
 ['Abacus','A compliance engine mode on rules: parallel or live. Suggests shadow evaluation of a new engine.'],
 ['newcash','The capital flows module. Its permissions (VIEW_NEWCASH, CASH_PAY, CASH_CONF…) gate the EnrichedCapitalFlow API.'],
 ['CIDS','Custom Investment Datasets: client-owned data loaded into Aladdin in a Category.Class.Group.Dataset hierarchy for use in portfolio management tools.'],
 ['BRM','Bulk Rate Mechanism, the internal module that generates floating-rate coupon resets.'],
 ['BQL','An expression language used in filters, order flags and routing rules (bqlExpression, bqlFilter). JQL appears on trade routing.'],
 ['ABOR / OBOR','Accounting book of record and the other (investment) book of record. ABOR lots carry a parallel OBOR lot id.'],
 ['PIF','Principal and Interest Factor: payment per 1,000 of original face on mortgage and asset-backed securities, used with positions to generate cash flows.'],
 ['SSI','Standard Settlement Instruction. Cashflows can default an SSI from the broker and then be transmitted.'],
 ['Transmission framework','The mechanism that sends money out once a cashflow has a confirmer and reviewer.'],
 ['LRO','Long-running operation. Returned by batch and heavy calls; polled at /longrunningoperations/{id}.'],
 ['Four eyes','Maker-checker approval: one person proposes, a second approves. Named on ADC dataset review and compliance rule assignments.'],
 ['Portfolio group','A hierarchy of portfolios and sub-groups. Most APIs accept a group ticker as scope.'],
 ['invnum','Investment number, part of the trade key with portfolio and trade number.'],
 ['touchCount','A per-record modification counter used for optimistic concurrency alongside version.'],
 ['Provider user','A BlackRock employee granted access into a client's Aladdin environment. Users are client employees, providers or system accounts.'],
 ['Citizen developer','BlackRock's term for finance professionals with some programming skill, the primary audience for Studio and the SDK.'],
 ['TBA','To-be-announced: a forward trade in agency mortgage bonds where the exact pools are assigned later.'],
 ['ISDA / CSA','The master agreement for over-the-counter derivatives and its credit support annex, which sets collateral terms.'],
 ['Access.Internal','A tag on every public spec. Appears to be a visibility classification; its exact meaning is not documented publicly.'],
 ['Alpha (accounting)','Fields prefixed alpha (alphaLedgerTable, alphaStartDate, alphaPriceGroup) point to the accounting engine behind Aladdin Accounting.']
]

## Data: QUIZ
[
 ['What is an Order, in Aladdin's own words?','"A directive from a portfolio manager to the trading desk to execute a particular investment decision." A PM order becomes a trader order when the desk picks it up.'],
 ['How does pre-trade compliance reach a client script?','Pre-trade compliance runs inside the order post: runCompliance defaults to true and violations come back in the response. The Compliance APIs manage rules and read levels; they do not check an order.'],
 ['Name the two limit frameworks and who owns them.','Compliance (regulatory and mandate rules, run on orders and trades, owned by compliance) and Risk Governance in Risk Radar (metric thresholds on analytics, owned by risk, with its own exceptions and workflows).'],
 ['What does the Cash Ladder include beyond settled cash?','Intraday trades, authorised and open orders, confirmed and estimated capital flows, and collateral pledged and held, laid out by settlement date and currency.'],
 ['How is Aladdin Data Cloud structured per client?','Each client gets its own Snowflake database. Datasets are tables, views or history views, moving through draft, review (four eyes) and released, with ETL config and reconciliation against a gold-copy client.'],
 ['What tells you the services are protobuf and gRPC underneath?','google.rpc.Status, Any with @type, google.type.DateTime, updateMask, pageToken, LongrunningOperation and FOO_UNSPECIFIED enums in every spec.'],
 ['How many public APIs are alpha, and why does that matter?','24 of 54. Nearly half the public surface can still change, so graduation criteria and client migration are live product problems.'],
 ['What are the two layers of authorisation?','OAuth scopes per resource at the gateway, then Aladdin permission codes (brkrMaint, PortGroupMOD, VIEW_NEWCASH) checked inside the service.'],
 ['How does Copilot get its tools?','A federated plugin registry: 50 to 60 domain teams register existing production APIs as tools or build custom agents. The central team filters to 20 to 30 tools per query by environment, user group and app.'],
 ['What does "one booked trade updates every view" mean concretely?','Level reads positions for room to limit, CashLadder folds in open orders and collateral, CollateralStatement reads positions for margin, AborLot is created from the trade, and RiskRule evaluates analytics computed on the same positions.'],
 ['What is CIDS for?','Letting clients load their own datasets (scores, targets, classifications) into Aladdin so screens, rules and reports can use them without exporting to Excel. Aladdin does not transform the data; the writer owns it.'],
 ['Which cloud, and what changed in December 2025?','Azure today, after a client-by-client migration. BlackRock and AWS announced an AWS hosting option with general availability expected in the second half of 2026.']
]