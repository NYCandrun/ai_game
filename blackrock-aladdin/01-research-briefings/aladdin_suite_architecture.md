# Aladdin, reconstructed from its API documentation

What the suite does, how it is broken down, and how it is architected, as evidenced by the 54 OpenAPI specifications (301 operations) shipped in BlackRock's 11 public `asdk_plugin_*` packages, version 2.0.0b3. Compiled 2026-10-19. Everything here is read off the specs themselves unless marked otherwise. The public packages are a subset of the catalog in the login-only developer portal, so absences are noted, not assumed.

---

## 1. The one-paragraph version

Aladdin is a single system of record and workflow engine for the entire life of an institutional investment: research and idea capture, portfolio setup and mandate rules, order raising, pre-trade compliance, execution and allocation, settlement instructions and cash movement, corporate actions and income, collateral and margin, accounting lots and NAV, risk and regulatory oversight, and client capital flows in and out of funds. Every one of those stages appears as a domain in the API namespace, and the specs show the same shape across all of them: a master entity (Portfolio, Order, Trade, Security, Broker, Rule), a lifecycle state machine with maker-checker approval, bitemporal history, and a batch-plus-long-running-operation interface for bulk work. The suite is not an analytics library with a database attached; it is an operational platform whose analytics sit on top of positions it also books.

---

## 2. How the suite is broken down

The API namespace is `agraph.<domain>.<segment>.<group>.<version>.<API>`, and the eleven public domains map onto the classic front, middle, back office split.

### Front office: deciding and acting

**investment-research** (5 APIs, all alpha). A research management system.
- ResearchNote v2: templated notes with custom field definitions, permission groups with expiry, tagged to entities (issuer, asset, investment strategy), HTML body.
- Engagement: records of meetings with companies and issuers, with attendees, topics, KPIs and "momentum", draft and published states.
- AnalystCoverage: who covers which issuer or asset, with transfer and historical lookup.
- Watchlist: securities with pre-trade notes and expiry dates.
- Criterion: stored screening expressions evaluated against CUSIPs, for example `((price > 55 OR oas = 75) AND market_cap < 1mm) OR msci_social_score > 5.0`, with alert frequencies and recipients. This is the surveillance and alerting layer over research.

**portfolio** (3 APIs). The portfolio master.
- PortfolioToolkit: the Portfolio entity has 850 attributes. They cluster into mandate and benchmark assignments, cash and sweep instructions per currency, trade routing to custodians, legal and regulatory classification (ERISA, UCITS, 40 Act, Dodd-Frank, EMIR, SFTR, MiFID, SFDR, FATCA, AIFMD, Volcker, CRS), securities lending terms, treasury bank account settings, ESG taxonomy percentages, alternatives fund terms (waterfall, clawback, investment period), model portfolio settings, and dozens of eligibility indicators (can this portfolio hold TBAs, CDS, 144A, emerging markets, short sales). "Slices" expose subsets of this to keep payloads small.
- PortfolioGroup: a hierarchy of groups and portfolios with ancestor and descendant queries. Nearly every other API accepts a portfolio group ticker as scope.
- RestrictedAsset: per-portfolio trading blocks.
- Relationship types on the entity reveal structures the platform models natively: master-sleeve, master-feeder, create-redeem, common pool, SMA roll-up, model suites.

**portfolio-management** (4 APIs).
- Strategy: named investment strategies that orders and trades are tagged with, so intent is traceable through to accounting.
- CashLadder v2: settlement-date ladder of projected cash by currency, with switches to include intraday trades, authorised and open orders, confirmed and estimated new cash, collateral pledged and held, unfunded commitments and prefunding. This is the cash forecasting engine that order generation depends on.
- CIDS reader and writer: "Custom Investment Datasets", a schema-driven way for clients to load their own data (scores, classifications, targets) into Aladdin so portfolio management tools can use it. Datasets live in a Category.Class.Group.Dataset hierarchy with permission groups, draft, approved and retired states. The spec says plainly that Aladdin does not transform this data and the writer owns it.

**trading** (2 APIs).
- Order v1: "a directive from a portfolio manager to the trading desk to execute a particular investment decision." Owner types are PM, trader and hybrid, and PM orders map to trader orders. Posting an order takes `whatIf` and `runCompliance` flags and returns compliance violations inline, so pre-trade compliance is a property of the order API. Orders carry baskets, dealing capacity, limits and stops, benchmarks, credit and locate reservations, urgency, and a free custom-field block.
- Trade v2: a BlockTrade with child trades allocated to portfolios, broker and executing broker, desk, quotes received in competition (statuses such as covered, tied, done away, did not trade), price types (clean, dirty, yield, amortised), settlement FX, TBA and pool stipulations, repo collateral legs, FX legs, trade relationships, and external trade references for reconciliation against other systems.

**data** (1 API). SecurityCreation: a security master write interface covering CDS, CDX, equities, equity options, futures, FX spot, forward, swap, NDF and options, interest rate swaps, total return swaps, swaptions, time deposits, repo, ARM and MBS TBAs. It shows the instrument breadth the platform prices and books natively.

### Middle office: control and oversight

**compliance** (4 APIs). Rule-based mandate and regulatory monitoring.
- ComplianceRule: rule types are prohibition, concentration, value at risk, disclosure, scripted, look-through definition, information, trade, counterparty and counterparty exposure limit. Rules carry a regulation reference, jurisdiction, labels (restricted issuers, credit quality, cash and leverage, duration, geography, counterparty, prospectus and so on), run flags for overnight and intraday, and a lifecycle of draft, ready for testing, review required, review rejected, approved. An "Abacus mode" of parallel or live suggests a compliance engine with shadow evaluation.
- ComplianceRuleAssignment: binds rule configurations to portfolios, with four-eyes approval and an applicability type (aggregate versus individual).
- Level: start-of-day and intraday "room to limit" per rule per portfolio, including as-traded levels.
- Violation: breaches with contributing positions, sourced from orders or trades, with ownership, disposition and resolution workflow.

**analytics / oversight / governance** (7 APIs, surfaced in an app the specs call Risk Radar). A separate, risk-team-owned limit framework distinct from compliance.
- RiskRule: conditions of metric, limit and breakdown, with absolute limits (250 bps tracking error) or relative limits, sector-level limits, benchmark and look-through configuration, versions, draft and approved states, overrides, and subscriptions that attach portfolios to rules for date ranges.
- EvaluatorAnalytics: triggers evaluation of a portfolio against all or one rule as a long-running operation. Metric source is either Aladdin Analytics or custom data.
- RiskCustomEvaluationMetric: upload your own metric values so the evaluator can test rules against them.
- RiskException and RiskWorkflow: breach and warning records, then assigned, commented, prioritised work items with state transitions and twelve months of revision history.
- RiskConfig: configuration records with revision history that drive both evaluation behaviour and the Risk Radar user interface.

**analytics / data** (2 APIs). Climate (physical, transition and temperature-alignment metrics under named scenarios, per security, deal or issuer) and ESG (multi-vendor measures normalised into one schema, with issuer traversal and time series). These are the sustainability data feeds behind Aladdin Climate.

**clients** (1 API). EnrichedCapitalFlow: subscriptions and redemptions into funds, both cash and in-kind, with estimate and actual states, authorise and confirm actions, true-up against fund accountant prices, and validation. Permissions reference a module called "newcash".

### Back office: operations and accounting

**investment-operations** (15 APIs). The largest domain, and the most "write" heavy.
- Asset lifecycle: CorporateAction (mandatory and voluntary events with the full date set: ex, record, payable, deadline), CorporateActionEntitlement (per-portfolio entitlements with elections instructed to the custodian and compliance checks on election), CouponReset (floating-rate resets from an internal "Bulk Rate Mechanism" or vendors), PrincipalInterestFactor (MBS and ABS factors used with positions to generate cash flows, with audit trails).
- Cash flows: MiscellaneousCashflow with standard settlement instruction defaulting and a "transmission framework" that actually sends money out once a confirmer and reviewer are recorded.
- Collateral management: CollateralStatement, generated daily by margin calculators from agreements set up in a tool called DECO, covering ISDA with and without CSA, cleared and exchange-traded, with exposure, independent amount, pledged and held positions and dispute fields.
- Reference data: Broker, BrokerDesk, BrokerExternalAlias, BrokerConfirmRouting (how a booked trade gets confirmed to a desk), CounterPartySettlementInstruction and templates, Contact (custodian and broker recipients, including FTP and SWIFT-style delivery details), AccountInfo, plus an Audit API over all broker entities.

**accounting** (4 APIs, described as "Aladdin Accounting").
- AborLot: accounting-book-of-record lots with a parallel OBOR lot id, so investment book and accounting book are reconciled at lot level.
- Valuations: NAV workflow per portfolio and process type, with status, sign-off, publication time, Dietz and total return fields, and valuation exceptions with NAV impact.
- CompositeMembership: entry and exit of portfolios in performance composites.
- PortfolioConfiguration: accounting attributes by process code, with history.

### Platform

**platform** (6 APIs).
- User: client employees, "provider" employees (BlackRock staff with access to the client's environment) and system or bot accounts, with alternate ids mapping to the client's HR identifiers.
- UserGroup, UserGroupMember, Permission, UserGroupPermission: a hierarchical group model where permissions attach to groups only, each permission having a functional area, action and sensitivity grade. The specs state these APIs are for administration, "not intended to be used for Authorization".
- AdcDataset: the registry behind Aladdin Data Cloud. Datasets are Snowflake tables, views or history views in a per-client database, bitemporal, with draft, review (four-eyes) and released states, ETL configuration, column metadata refresh, and a reconciliation of one client's datasets against a gold-copy client. Several operations are marked internal to BlackRock.

### What is absent from the public packages

Positions and holdings, risk analytics outputs (factor exposures, VaR, scenario results), performance attribution, pricing and market data, benchmark and index data, execution management and FIX connectivity, settlement messaging, private markets (eFront) and wealth. BlackRock's own pages say dozens of APIs exist and third-party directories list positions, risk and securities APIs, so these almost certainly live in the portal. The public set skews toward operational write APIs and reference data.

---

## 3. How it is architected, as the specs reveal it

**Protobuf and gRPC underneath, REST on top.** Every spec carries `rpcStatus` (google.rpc.Status), `Any`, `google.type.DateTime`, `updateMask`, `pageToken`, `LongrunningOperation`, enums named `FOO_UNSPECIFIED`, and request and response message names of the form `v1FilterOrdersRequest`. That is the fingerprint of services defined in protobuf and exposed through gRPC-gateway style transcoding. "Aladdin Graph" is the name of this unified API layer, and the specs refer to an "agraph team" that agrees naming.

**Google API design conventions, enforced by a linter.** Resources with custom methods (`:filter`, `:batchCreate`, `:cancel`, `:undelete`, `:listRevisions`), AIP-160 style filter strings, and standard pagination. The specs contain inline linter suppressions such as `api-linter: aladdin::9016::query-custom-method-http=disabled aip.dev/not-precedent`, with a reason attached. BlackRock runs Google's api-linter plus its own `aladdin::` rule set, and exceptions must be justified. The most common justification is that changing the URI "will break all citizen developers code", which tells you backwards compatibility is enforced in review.

**A deliberate lifecycle.** Each API is stamped `x-aladdin-api-stability` of alpha, beta, stable or sunset, and versioned independently (OrderAPI v1, TradeAPI v2, CashLadder v2 with a GET kept "solely for backward compatibility"). Of the 54 public specs, 24 are alpha, 6 beta, 23 stable, 1 sunset.

**Bulk by default.** POST is 190 of 301 operations. Filtering is POST with a criteria body. Batch endpoints are capped (100 per request for reference data, 1,000 for restricted assets, 10,000 rows per page) and heavy operations return a long-running operation id to poll. Ten specs expose an LRO endpoint and 35 operations are flagged `x-aladdin-lro`. Several APIs offer `validateOnly` or `:batchValidate` so callers can dry-run before writing.

**Identity and versioning of records.** Portfolios are addressed by id, ticker, asset id or UUID. Securities by Aladdin asset id or CUSIP, ISIN, SEDOL, RIC, CINS. Trades by portfolio plus investment number ("invnum") plus trade number, with `touchCount` and `version` for optimistic concurrency. Most entities carry modifier and modify time, and many carry entry and expiry times or valid-begin and valid-end dates, which is a bitemporal pattern that supports as-was reporting. Audit APIs exist for brokers and PIFs, and revision listing exists for rules, configs and workflows.

**Workflow state machines everywhere.** Compliance rules: draft, testing, review, approved. Risk rules: draft and approved with overrides and sign-off authors. ADC datasets: draft, review, released. Capital flows: open, authorised, confirmed, cancelled. Corporate action elections: elected, authorised, instructed, processed. Cash transmissions need a confirmer and reviewer. "Four-eyes" appears by name. Governance is modelled in the data, not bolted on.

**Multi-tenant, per-client environments.** Specs refer to the "Aladdin client's website", `clientAbbreviation`, `accountCode` on external references, a per-client ADC database, and reconciliation against a gold-copy client. The OAuth endpoints are at client.blackrock.com. Each client runs in its own tenant with BlackRock "provider" users granted access into it.

**Authentication and entitlement.** Every call carries an application key header (`VND.com.blackrock.API-Key`) registered in Studio, plus OAuth 2.0 (authorization code or client credentials), a client key header, or basic auth. OAuth scopes are per resource, for example `trading.order_management.order.v1.Order:read` and `:write`. Underneath, the specs still cite legacy permission codes (`brkrMaint`, `asReAsMOD`, `PortGroupMOD`, `PERMS_GROUP_MOD`, `VIEW_NEWCASH`) that the user must hold, so authorisation is two-layered: OAuth scope at the gateway, Aladdin permission inside the service.

**Internal expression languages.** Fields named `bqlExpression`, `bqlFilter`, `skipBqlValidation` and `jql` on trade routing, and comments that say "refer to BQL ord_flags", point to a query language used across the platform for filters and routing rules. Compliance scripted rules and research criteria are further expression surfaces.

**Named internal systems that surface in the docs.** Risk Radar (oversight app), DECO (collateral agreements), Bulk Rate Mechanism (coupon resets), Abacus (compliance engine mode), newcash (capital flows), CIDS and CID Manager, ADC Admin Center, the transmission framework (payments out), ADL (a data layer referenced as the store for ADC dataset repositories and portfolio search), and an accounting system whose fields are prefixed "alpha" (ledger tables, start dates, price groups). The Copilot talk's "about 100 front-end apps" are these.

**Hosting (from outside the specs).** SaaS on Azure today, with an AWS option announced December 2025 for H2 2026, and job postings describing an Aladdin Container Platform on Kubernetes with a Go control plane. The specs themselves are hosting-neutral.

---

## 4. Reading the suite as a product

- **The spine is Portfolio, Security, Order, Trade, Position.** Positions are not in the public set, but every domain references them: compliance levels, cash ladders, PIF cash flows, collateral exposures, ABOR lots. Aladdin's value is that one booked trade updates all of those views.
- **Two limit frameworks coexist.** Compliance (regulatory and mandate rules, run against orders and trades, owned by compliance) and Risk Governance (risk metrics against thresholds, run on analytics, owned by risk, with its own exceptions and workflow). A good interview question is how they are converging.
- **Client extensibility is designed in.** CIDS for custom data, custom evaluation metrics for risk rules, custom fields on orders, trades and research notes, scripted compliance rules, research criteria, ADC for analytical data, and Studio for code. The platform expects clients to bring data and logic.
- **The operational side is where the write APIs are.** Reference data (brokers, SSIs, contacts), corporate action elections, cash transmissions, coupon and factor maintenance. These are the workflows clients automate first, which explains why they were packaged publicly.
- **The analytics core stays close.** Risk and climate analytics are exposed as data retrieval and rule evaluation, not as a calculation engine clients call directly. Aladdin Analytics is a metric source for rules, not an API you post a portfolio to.

---

## 5. Caveats

- Counts and stability labels are for plugin version 2.0.0b3 on PyPI and can lag the developer portal.
- Every public spec is tagged `Access.Internal`, which appears to be a visibility classification BlackRock applies to specs. Its exact meaning is not documented publicly.
- Inferences about gRPC, the linter, BQL, ADL and the named internal systems come from field names, comments and linter annotations inside the specs, not from BlackRock architecture documents.
- Hosting and Copilot details come from press releases, Microsoft and AWS pages, job postings and a third-party summary of a BlackRock talk, as cited in the companion Studio briefing.
