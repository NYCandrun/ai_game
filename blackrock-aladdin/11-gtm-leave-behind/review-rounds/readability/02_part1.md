# Readability pass, Part 1 (pages 3 to 8, Exhibits 1 to 9)

Conventions. Superscript source numbers are written as trailing numbers (" 9") exactly as the text dump shows them; every rewrite keeps each number next to the fact it belonged to. Quoted and underlined link phrases are kept verbatim inside the rewrites so the links survive; where a rewrite splits a sentence, the underlined phrase stays whole inside one of the new sentences. Rewrites add no facts. Where a clearer sentence would require a fact the page does not state, the entry says so and marks it "author to confirm".

Severity: **Stop** = a busy reader would reread or come away unsure. **Slow** = reads once but costs effort. **Fix** = a small mechanical issue (fragment, unexplained term).

---

## Page 3

### 3.1 (Stop) The Rosales sentence, 58 words, three quotations joined by a colon and a semicolon

Current: "Brennan Rosales, its AI Engineering Lead, put the scale this way at a LangChain conference in 2025: “BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries”; the organization is “around 7,000 people, with over 4,000 of those being engineers,” who maintain “around 100 Aladdin front-end applications” 9."

Trying to say: Aladdin is big, and BlackRock's own AI engineering lead has said so publicly with three numbers.

Rewrite: "Brennan Rosales, its AI Engineering Lead, put the scale this way at a LangChain conference in 2025. “BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries.” The Aladdin organization is “around 7,000 people, with over 4,000 of those being engineers.” They maintain “around 100 Aladdin front-end applications” 9."

### 3.2 (Stop) "up 24 percent with Preqin": the reader cannot tell whether Preqin caused the growth or is included in the figure

Current: "BlackRock’s technology services and subscription revenue was $2.0 billion in 2025, up 24 percent with Preqin 10."

Trying to say: The revenue line that contains Aladdin was $2.0 billion in 2025, up 24 percent, and the 2025 figure includes Preqin.

Rewrite (author to confirm that "with Preqin" means "including Preqin"): "BlackRock’s technology services and subscription revenue was $2.0 billion in 2025, up 24 percent; the figure includes Preqin 10."

### 3.3 (Slow) Colon list, then "what is out there" twice in two sentences

Current: "Aladdin is sold the way enterprise platforms are sold: a conversation first, then documentation, a sandbox and credentials from the solutions team once a prospect is qualified. What follows is what is out there before that conversation."

Trying to say: Nothing technical is handed over until after a sales conversation; Part 1 covers what a prospect can see before that conversation.

Rewrite: "Aladdin is sold the way enterprise platforms are sold. The conversation comes first. Documentation, a sandbox and credentials come from the solutions team once a prospect is qualified. Part 1 covers what a prospect can see before that conversation."

### 3.4 (Fix) Exhibit 1, Aladdin Wealth cell: "with Morgan Stanley first" is a fragment the reader has to decode

Current: "Portfolio risk analysis and proposals for advisors; its AI “auto commentary” tool launched in October 2025 with Morgan Stanley first 11"

Trying to say: Morgan Stanley was the launch client.

Rewrite: "Portfolio risk analysis and proposals for advisors. Its AI “auto commentary” tool launched in October 2025, with Morgan Stanley as the first client 11."

### 3.5 (Stop) Exhibit 1, Aladdin Studio cell: two colons, a semicolon and a 30-word quotation in one cell

Current: "The developer and data layer: APIs and events, a Python SDK, Aladdin Compute and Aladdin Data Cloud; “API-first,” for “a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting” 13"

Trying to say: Studio is the developer layer, it has four named pieces, and BlackRock names three kinds of user for it.

Rewrite: "The developer and data layer. It covers APIs and events, a Python SDK, Aladdin Compute and Aladdin Data Cloud. BlackRock calls it “API-first” and names three users: “a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting” 13."

### 3.6 (Slow) Exhibit 1, Aladdin Data Cloud cell: three clauses chained with semicolons

Current: "A managed data service on Snowflake that puts Aladdin and outside data in one place; sold as an add-on to Aladdin Enterprise 14; Richard Newman, General Manager, Aladdin Studio, calls it “part of Studio” 15"

Trying to say: Data Cloud is a Snowflake data service, sold as an add-on, and the head of Studio counts it as part of Studio.

Rewrite: "A managed data service on Snowflake that puts Aladdin and outside data in one place. It is sold as an add-on to Aladdin Enterprise 14. Richard Newman, General Manager, Aladdin Studio, calls it “part of Studio” 15."

### 3.7 (Fix) "BlackRock’s own definition" does not say of what

Current: "BlackRock’s own definition comes from the head of Studio engineering, on Snowflake’s podcast in November 2025. It has three parts."

Trying to say: The best public definition of Studio comes from BlackRock's own head of Studio engineering, and it names three parts.

Rewrite: "BlackRock’s own definition of Studio comes from the head of Studio engineering, on Snowflake’s podcast in November 2025. It has three parts."

---

## Page 4

### 4.1 (Stop) After the Woodhead quotation, the three parts are never named in plain words; the reader has to extract them from a machine transcript ("a set of APIs events")

Current: (the quotation, then) "Exhibit 2 follows one trade through that platform, as far as the public specifications describe it: who acts, where BlackRock names a product or application, and which of the 54 APIs covers each step 17, 20."

Trying to say: The three parts are APIs and events, Data Cloud and developer tools; Exhibit 2 now traces a trade through the APIs.

Rewrite (bridge sentence uses only what the quotation says): "The three parts are APIs and events, the Aladdin Data Cloud on Snowflake, and developer tools. Exhibit 2 follows one trade through Aladdin, as far as the public specifications describe it. For each step it records who acts, which product or application BlackRock names, and which of the 54 public API specifications covers the step 17, 20."

Note: "the 54 APIs" appears here for the first time; the count is only explained in Exhibit 5 two pages later. The rewrite says "54 public API specifications" so the phrase explains itself; Exhibit 5 can carry the detail.

### 4.2 (Fix) Exhibit 2, step 1, Named column: "Explore" appears with no indication of what it is

Current: "Explore’s “new what-if model” compares a changed portfolio with the original before anything is traded 21; the specifications name no order screen 17"

Trying to say: The only named application at this step is Explore, and it is a what-if tool rather than an order screen.

Rewrite: "The Explore application: its “new what-if model” compares a changed portfolio with the original before anything is traded 21. The specifications name no order screen 17."

### 4.3 (Slow) Exhibit 2, step 1, API column: "stable" and "alpha" labels are used from this exhibit on but are not explained until Exhibit 5

Current: "OrderAPI v1, stable: order:post takes whatIf and runCompliance; the status examples run “Open,” “Compl Pending,” “Authorized,” “Active,” “Booked” 17"

Trying to say: The Order API is one of the stable ones; an order post carries two flags; and the spec's own examples show the order lifecycle.

Rewrite: "OrderAPI v1 (stable). Posting an order takes whatIf and runCompliance. The specification’s example statuses run “Open,” “Compl Pending,” “Authorized,” “Active,” “Booked” 17."

Suggest the Exhibit 2 source note add one clause: "alpha, beta and stable are the maturity labels each specification carries" (author to confirm the labels come from the specifications).

### 4.4 (Stop) Exhibit 2, step 2, Who acts: cell has no subject; "Automatic" what?

Current: "Automatic on posting, with runCompliance on by default; a violation then carries an owner, a disposition and a resolution comment 17"

Trying to say: No person acts; the check runs itself when the order is posted, and any violation is assigned to someone.

Rewrite: "No one. The check runs automatically when the order is posted, because runCompliance is on by default. Any violation then carries an owner, a disposition and a resolution comment 17."

### 4.5 (Slow) Exhibit 2, step 2, API column: four facts in one cell

Current: "ComplianceRuleAPI and ViolationAPI v1, alpha: violations are “generated at time of the compliance breach,” intraday and overnight; a check that times out posts the order as “Compl Pending” 17"

Rewrite: "ComplianceRuleAPI and ViolationAPI v1 (alpha). Violations are “generated at time of the compliance breach,” intraday and overnight. A check that times out posts the order as “Compl Pending” 17."

### 4.6 (Stop) Exhibit 2, step 3, Named column: "Aladdin Accounting’s leads" reads as sales leads

Current: "Aladdin Accounting’s leads: the run goes “from that first order through the trade, through all the operation protocols into accounting without lifting up the pencil” 20"

Trying to say: The people who run Aladdin Accounting describe the trade flowing straight through to accounting; no application is named for this step.

Rewrite: "The people who lead Aladdin Accounting say the run goes “from that first order through the trade, through all the operation protocols into accounting without lifting up the pencil” 20."

### 4.7 (Slow) Exhibit 2, step 3, API column: three systems and five field names in one cell

Current: "TradeAPI v2, alpha: trades:post, batchPost, filter; a block trade carries its per-portfolio trades, confirmedWith and confirmedBy; BrokerConfirmRoutingAPI routes the confirm 17"

Rewrite: "TradeAPI v2 (alpha), with trades:post, batchPost and filter. A block trade carries its per-portfolio trades, plus confirmedWith and confirmedBy. BrokerConfirmRoutingAPI routes the confirm 17."

### 4.8 (Fix) Exhibit 2, step 4, Who acts: "IBOR" is used in the row label and this cell before the next cell spells it out

Current: "The investment team’s live book; Newman: “It does start with IBOR” 15"

Rewrite: "The investment team, whose live book is the IBOR, the investment book of record. Newman: “It does start with IBOR” 15." (The expansion is taken from the Named column of the same row.)

### 4.9 (Slow) Exhibit 2, step 4, API column: parenthesis inside a semicolon chain

Current: "No position API among the 54; positions appear as fields (a PortfolioToolkitAPI positions source, a violation’s “underlying positions”); CashLadderAPI v2, stable, gives the settlement-date cash ladder 17"

Rewrite: "None of the 54 is a position API. Positions appear only as fields: a positions source in PortfolioToolkitAPI, and a violation’s “underlying positions.” CashLadderAPI v2 (stable) gives the settlement-date cash ladder 17."

### 4.10 (Fix) Exhibit 2, step 5, Who acts: "we" has no stated speaker

Current: "Accounting: “we are data managers more than anything else” 20"

Rewrite: "The accounting team, which says of itself: “we are data managers more than anything else” 20."

### 4.11 (Fix) Exhibit 2, step 5, Named column: "its" could point to Accounting or to the specification

Current: "Aladdin Accounting, the product its configuration specification is written for 17"

Rewrite: "Aladdin Accounting. The public portfolio-configuration specification is written for this product 17."

### 4.12 (Slow) Exhibit 2, step 5, API column

Current: "AborLotAPI v1, alpha: ABOR lots “retrieved from the ledger_a_summary table,” each with an oborLotId and open and close transaction ids; EnrichedCapitalFlowAPI v1, stable, posts subscriptions and redemptions 17"

Rewrite: "AborLotAPI v1 (alpha). ABOR lots are “retrieved from the ledger_a_summary table,” each with an oborLotId and open and close transaction ids. EnrichedCapitalFlowAPI v1 (stable) posts subscriptions and redemptions 17."

### 4.13 (Stop) Exhibit 2 source note: "do not order steps 4 to 6" reads as the verb "order" in an exhibit about orders

Current: "The statuses are the Order specification’s examples; the specifications hold no position or event API and do not order steps 4 to 6."

Trying to say: The specifications do not say in what sequence steps 4, 5 and 6 happen; the sequence shown is the author's.

Rewrite: "The statuses are the Order specification’s examples. The specifications hold no position or event API, and they do not say in what sequence steps 4 to 6 happen; the sequence shown is mine." (Author to confirm "is mine".)

---

## Page 5

### 5.1 (Fix) Exhibit 3, APIs box: "all “Aladdin Graph”" is a term the reader has not met yet

Current: "APIs and events: 54 public specifications, all “Aladdin Graph”"

Trying to say: All 54 specifications carry the Aladdin Graph id (explained in Exhibit 4).

Rewrite: "APIs and events: 54 public specifications, all tagged “Aladdin Graph” (see Exhibit 4)"

### 5.2 (Slow) Exhibit 3, Data Cloud box: "fed by Fivetran" assumes the reader knows Fivetran is a data-pipeline vendor

Current: "Aladdin Data Cloud on Snowflake, fed by Fivetran"

Rewrite: "Aladdin Data Cloud on Snowflake, with data moved in by Fivetran" (The same gloss appears in Exhibit 4, "with Fivetran moving the data"; using the same words in both places lets the reader connect them.)

### 5.3 (Fix) Exhibit 4, APIs row: "ADC" is used without expansion; "specs" and "specifications" alternate

Current: "The 54 specs include orders, trades, compliance rules, risk rules, security creation and ADC datasets 17."

Rewrite: "The 54 specifications include orders, trades, compliance rules, risk rules, security creation and Aladdin Data Cloud datasets 17."

### 5.4 (Slow) Exhibit 4, APIs row, second sentence: the point ("Aladdin Graph is a layer, not a product") arrives after a 12-character id pattern

Current: "Every public specification carries an id of the form agraph.<domain>.<segment>.<group>.v1.<API>, so Aladdin Graph is the whole API layer, not one API 17."

Rewrite: "Aladdin Graph is the whole API layer, not one API: every public specification carries an id of the form agraph.<domain>.<segment>.<group>.v1.<API> 17."

### 5.5 (Fix) Exhibit 4, Data Cloud row: "the latency" of what is not stated

Current: "A managed data store on Snowflake, with Fivetran moving the data; Goel gives the latency as “within 15 minutes” 25."

Rewrite: "A managed data store on Snowflake, with Fivetran moving the data. Goel says data arrives “within 15 minutes” 25." (Author to confirm this is what Goel's latency figure measures.)

### 5.6 (Fix) Exhibit 4, SDK row: "plugin builder" and "domain" appear before either is explained

Current: "Eleven add-on packages, one per domain, are generated from the specifications by the plugin builder 26."

Rewrite: "Eleven add-on packages, one per API domain (Exhibit 5), are generated from the specifications by a tool BlackRock publishes called the plugin builder 26."

### 5.7 (Fix) Exhibit 4, Investment research row: double colon, "alpha" unexplained

Current: "A domain of five alpha APIs: research notes, engagements, analyst coverage, watchlists and screening criteria 17."

Rewrite: "A domain of five APIs, all still labelled alpha. They cover research notes, engagements, analyst coverage, watchlists and screening criteria 17."

### 5.8 (Fix) Exhibit 4, Tools for Excel row: "little public detail" is a fragment with no subject

Current: "An Excel add-in listed on the APIs page as a Studio resource, with Aladdin Data eXchange for bulk delivery; little public detail 23."

Rewrite: "An Excel add-in. The APIs page lists it as a Studio resource, alongside Aladdin Data eXchange for bulk delivery, and gives little detail on either 23."

---

## Page 6

### 6.1 (Fix) Exhibit 5 column headers "Alpha, Beta, Stable, Sunset" are never defined

Current: column headers and source note as printed.

Trying to say: These are the maturity labels in the specifications, and most of the catalog is not yet stable.

Rewrite, add to the source note (author to confirm the labels are from the specifications): "Alpha, beta, stable and sunset are the maturity labels each specification carries."

### 6.2 (Stop) The "specifications say more than their count" paragraph lists five technical facts and never states what they add up to

Current: "The specifications say more than their count. Every one is tagged Access.Internal, a label BlackRock does not explain in public 17. Posting an order takes whatIf and runCompliance, which defaults to true, and returns compliance violations inline 17. Ten specifications expose a long-running-operations endpoint and 35 operations are flagged for it; the SDK polls them 24. Risk exceptions and ADC datasets carry bitemporal fields; rule assignments and dataset releases name a four-eyes approval 17. Every request carries an application key plus OAuth 2.0 scopes such as trading.order_management.order.v1.Order:read, and the client ID and secret come from the Studio UI 24."

Trying to say: Reading inside the specifications shows they are built for governed production use by an existing client's engineers, not for a stranger to try. (The conclusion is implied; the closing line of the next paragraph, "These are the needs of a client’s engineering team," is the nearest statement of it.)

Rewrite (conclusion sentence marked for the author to confirm): "The specifications say more than their count. Every one is tagged Access.Internal, a label BlackRock does not explain in public 17. Posting an order takes whatIf and runCompliance, which defaults to true, and the response returns any compliance violations inline 17. Ten specifications expose an endpoint for long-running operations, 35 operations are flagged as long-running, and the SDK polls them 24. Risk exceptions and Data Cloud datasets carry bitemporal fields, which record both when something was true and when the system learned it. Rule assignments and dataset releases name a four-eyes approval, a second sign-off before a change takes effect 17. Every request carries an application key plus OAuth 2.0 scopes such as trading.order_management.order.v1.Order:read, and the client ID and secret come from the Studio UI 24. [Author to confirm:] Each of these is a feature of a controlled production system for an existing client, not of a product a stranger can try."

Note: the glosses for "bitemporal" and "four-eyes" are standard meanings, not new facts about Aladdin; if the author prefers no gloss, drop the "which record ..." and "a second sign-off ..." clauses but keep the rest of the split.

### 6.3 (Slow) 32-word sentence introducing Exhibit 6, and "out there" again

Current: "Exhibit 6 follows a prospect’s engineer through six steps, from first hearing about Studio to getting help, and records what is out there at each step and what follows qualification."

Rewrite: "Exhibit 6 follows a prospect’s engineer through six steps, from first hearing about Studio to getting help. For each step it records what is public today and what a client receives after qualification."

### 6.4 (Stop) SDK paragraph: 38-word sentence, "MCP toolkit" before MCP is explained, "an outside fix" with no stated target, then a 52-word sentence and a "These" with no clear referent

Current: "The SDK is the one piece that installs before any conversation. It has had 14 releases since May 2024, all alpha or beta, with the core at 2.0.0b10 in July 2026 and the add-ons at 2.0.0b3 27, 17. Each release pins an old Snowflake library, so none installs on Python 3.13, and the SDK’s dependencies conflict with the official MCP toolkit; an outside fix was merged in August 2026 and has not shipped 28. The README documents three run modes, “a developer’s local machine,” “Aladdin Studio Compute sessions” and a test mode, stores a prompted password in the operating system’s credential manager, and carries settings for firms that consume “the Aladdin APIs via an enterprise API management platform such as Azure API Management” 24. These are the needs of a client’s engineering team."

Trying to say: The SDK is the only thing a prospect can install, it is still pre-release and has install problems, and its design shows it was written for existing clients' engineers rather than for prospects.

Rewrite: "The SDK is the one piece that installs before any conversation. It has had 14 releases since May 2024, all alpha or beta. The core is at 2.0.0b10 as of July 2026 and the add-ons at 2.0.0b3 27, 17. Each release pins an old Snowflake library, so none installs on Python 3.13. The SDK’s dependencies also conflict with the official toolkit for MCP, the standard that lets outside AI tools call a vendor’s APIs. An outside contributor’s fix for the conflict was merged in August 2026 and has not shipped 28. The README documents three run modes: “a developer’s local machine,” “Aladdin Studio Compute sessions” and a test mode. It stores a prompted password in the operating system’s credential manager. It carries settings for firms that consume “the Aladdin APIs via an enterprise API management platform such as Azure API Management” 24. Run modes, credential storage and API-gateway settings are the needs of a client’s engineering team, not of a prospect."

Notes: (a) the MCP gloss repeats the meaning Exhibit 7's footnote gives ("an MCP server or connector that outside AI tools can use"); if MCP is defined earlier in a revised draft, drop it here. (b) Author to confirm the August 2026 fix addresses the dependency conflict rather than the Python 3.13 problem; the current sentence does not say which. (c) "not of a prospect" states the implied contrast; drop it if the author prefers the softer original.

---

## Page 7

### 7.1 (Slow) Exhibit 6, Read row: three quoted phrases with no indication they are page headings

Current: "The Studio page: “Create & automate,” “Make Aladdin your own,” “Align internally & externally”; the APIs page: “dozens of APIs”"

Rewrite (author to confirm the three phrases are the page's section headings): "The Studio page, whose three sections are “Create & automate,” “Make Aladdin your own” and “Align internally & externally”; the APIs page, which promises “dozens of APIs”"

### 7.2 (Fix) Exhibit 6, See the catalog row: the cell hides the effort

Current: "54 specifications, by unpacking the 11 PyPI add-on packages"

Rewrite: "The 54 specifications, but only by unpacking the 11 PyPI add-on packages"

### 7.3 (Fix) Exhibit 6, Try row, After qualification: a list with no verb, and "the client’s Aladdin host" tacked on

Current: "Studio Compute, an API token or OAuth application “registered via Studio UI,” the client’s Aladdin host"

Rewrite: "Studio Compute; an API token or an OAuth application “registered via Studio UI”; and the client’s own Aladdin host to call"

### 7.4 (Fix) Exhibit 6, Build row, After qualification: colon fragment

Current: "Every call: the SDK needs a client host and credentials"

Rewrite: "A client host and credentials, which the SDK needs for every call"

### 7.5 (Fix) Exhibit 6, Get help row: two quoted button labels with no context

Current: "GitHub issues and pull requests on the SDK, answered by BlackRock engineers; “Book a meeting” and “Download the brochure”"

Rewrite: "GitHub issues and pull requests on the SDK, answered by BlackRock engineers; on the Studio page, two buttons, “Book a meeting” and “Download the brochure”"

### 7.6 (Stop) Exhibit 6 source note: "the right-hand column" is the Receipt column, but the sentence describes the After qualification column

Current: "Source: the pages and repositories in the Receipt column, read with no account or login, October 2026; the right-hand column is what they say a client receives, not tested."

Rewrite: "Source: the pages and repositories in the Receipt column, read with no account or login, October 2026. The After qualification column is what those sources say a client receives; I did not test it."

### 7.7 (Fix) Exhibit 7, column header "Call to action" is ambiguous (a button? a sales call?)

Current: "Call to action"

Trying to say: Whether the public page offers a developer a next step to take on their own.

Rewrite (author to confirm the criterion): "Developer call to action" or "Next step offered to developers". If space is tight, keep the header and add one line under the legend: "Call to action: a public next step for a developer, such as a sign-up or a get-started button."

### 7.8 (Fix) Exhibit 7 footnote: "MCP server" is undefined at this point in the document

Current: "For the AI connector, 2 means an MCP server or connector that outside AI tools can use; 1 means one announced or in limited release; 0 means none, or an assistant that works only inside the vendor’s own platform."

Rewrite: "For the AI connector, 2 means a connector that outside AI tools can use, such as an MCP server; 1 means one announced or in limited release; 0 means none, or an assistant that works only inside the vendor’s own platform."

### 7.9 (Fix) Exhibit 7 source note: "underrated" reads as an opinion about the vendor

Current: "Bloomberg, Clearwater and MSCI may be underrated: some pages blocked automated access."

Rewrite: "Bloomberg, Clearwater and MSCI may score lower than they deserve, because some of their pages blocked automated access."

---

## Page 8

### 8.1 (Stop) Exhibit 7 commentary: the "total" is described as a count of criteria met, but the table sums scores of 0 to 2 (maximum 16); then a colon list and a 29-word sentence of vendor names

Current: "Exhibit 7 puts Studio beside 10 platforms that a Studio buyer also deals with, on eight things a developer with no client relationship can reach 32, 33, 34. The total counts how many of the eight criteria a developer can meet before any client relationship exists, so it measures each vendor’s selling model. Investment platforms cluster low because they gate: documentation, a sandbox and a first call follow a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium. Data and cloud platforms, which sell to developers directly, cluster high. Only Studio, among the investment platforms, offers an open-source SDK 24."

Trying to say: The score measures how much a vendor opens to developers before a sale; investment platforms open little, data and cloud platforms open a lot, and Studio's one distinction among investment platforms is its open-source SDK.

Rewrite: "Exhibit 7 puts Studio beside 10 platforms that a Studio buyer also deals with 32, 33, 34. It scores each on eight things a developer with no client relationship can reach, from 0 to 2, so the total runs from 0 to 16. A high total means the vendor opens to developers before any sale; a low total means access follows a relationship. So the total measures each vendor’s selling model. Investment platforms cluster low because they gate. At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, documentation, a sandbox and a first call come after a relationship exists. Data and cloud platforms sell to developers directly and cluster high. Among the investment platforms, only Studio offers an open-source SDK 24."

### 8.2 (Stop) "Five BlackRock speakers define Studio on the record in the 128 recordings pulled for this document, with the titles the recordings give": the trailing phrase dangles, and "128 recordings" is introduced in passing

Current: "Five BlackRock speakers define Studio on the record in the 128 recordings pulled for this document, with the titles the recordings give 29, 30."

Trying to say: The author reviewed 128 recordings; five BlackRock speakers define Studio in them; Exhibit 8 lists them with the job titles the recordings use.

Rewrite: "I pulled 128 recordings for this document 29, 30. Five BlackRock speakers define Studio in them. Exhibit 8 lists each speaker with the title the recording gives."

### 8.3 (Fix) Exhibit 8, column header "What they add": add to what?

Current: "What they add"

Rewrite: "What each adds to the definition"

### 8.4 (Fix) Exhibit 8, Woodhead row: "three-pillar" and "citizen developers" are shorthand

Current: "The three-pillar definition; 3,000 internal citizen developers"

Rewrite: "The three-part definition quoted on page 4; 3,000 “citizen developers” inside BlackRock" (Author to confirm "citizen developers" is Woodhead's phrase; if not, write "3,000 non-engineers inside BlackRock who build on Studio".)

### 8.5 (Fix) Exhibit 8 and Exhibit 9 source notes: "marked in the register" assumes the reader knows a register exists

Current (Exhibit 8): "Quotations are verbatim from the transcripts; three of the five are machine transcriptions, marked in the register."
Current (Exhibit 9): "Quotations are verbatim; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked in the register."

Rewrite (both): replace "marked in the register" with "marked as such in the source register at the end of this document" (author to confirm the register's location and name).

### 8.6 (Stop) "Four of them describe Studio with the same three parts": 44 words, four semicolon clauses, and "so the positioning exists" is abstract

Current: "Four of them describe Studio with the same three parts: Woodhead names them outright 5; Newman calls Data Cloud “part of Studio” 15; Goel describes events, APIs and a near-real-time data store 25; Khara calls it programmatic access to data and reporting 40. A 2026 job posting calls Studio “Aladdin’s extensibility layer” 42. The message is consistent across speakers and years, so the positioning exists. Learning about Studio from outside takes effort: the catalog is unpacked from packages, the definitions transcribed from recordings, and nothing can be run."

Trying to say: BlackRock already has a consistent positioning for Studio; the problem is not the message but how hard it is to find and test from outside.

Rewrite: "Four of the five describe Studio with the same three parts. Woodhead names them outright 5. Newman calls Data Cloud “part of Studio” 15. Goel describes events, APIs and a near-real-time data store 25. Khara calls it programmatic access to data and reporting 40. A 2026 job posting calls Studio “Aladdin’s extensibility layer” 42. The message is the same across speakers and years, so BlackRock already has a positioning for Studio. What it lacks is reach. Learning about Studio from outside takes effort. The catalog has to be unpacked from packages. The definitions have to be transcribed from recordings. Nothing can be run."

Note: "What it lacks is reach" states the implied contrast; drop it if the author prefers not to add the gloss.

### 8.7 (Fix) Terminology drifts: "three parts" (page 3), "three pillars" (Exhibit 8, Exhibit 9 title), "one pillar" (Exhibit 4), "the same three parts" (page 8)

Rewrite: pick one word and use it everywhere. "Three parts" is plainer; if "pillars" stays, introduce it once on page 3: "It has three parts, which this document calls the three pillars."

### 8.8 (Fix) Exhibit 9, Developer tools column: "–" is used where the other columns use "Yes", and no legend says what "–" means

Current: "–" in the Developer tools column for Khara and Newman.

Rewrite: "No", or add to the source note: "– means the speaker does not name that part."

---

## Exhibit titles, current and proposed

Each proposed title states the finding in one sentence. All are drawn from the exhibit's own cells and notes.

| Exhibit | Current title | Proposed title |
|---|---|---|
| 1 | One core engine with separate entry points for each kind of buyer | BlackRock sells one engine through eight named products, and Studio is the entry point for people who write code |
| 2 | One trade, start to finish: the team, the named application and the public API at each step | The public APIs cover a trade from order to NAV, but they name no order screen and hold no position or event API |
| 3 | Studio sits between the people who build and the system of record | Studio is the layer between the people who build on Aladdin and the one record of holdings underneath, with Copilot above it and governance across every layer |
| 4 | Eight pieces, from read-and-write APIs to an Excel add-in | Studio has eight pieces, and the catalog, guides, notebooks and samples all sit behind a client login |
| 5 | The public catalog: 54 specifications across 11 domains | Investment operations and analytics hold 127 of the 301 public operations, and only 23 of the 54 specifications are stable |
| 6 | Six steps a prospect’s developer takes, before and after qualification | A prospect’s developer can hear about Studio, read the pages and unpack the catalog, but cannot run anything until qualified |
| 7 | Several access models coexist in this market: what a developer with no client relationship can reach, on eight criteria | Studio scores 4 of 16 on access for non-client developers, level with State Street, below Bloomberg, and far below every data and cloud platform but MSCI |
| 8 | The five BlackRock speakers who define Studio on the record | Five BlackRock executives have defined Studio on the record since early 2024, and the head of Studio engineering gave the fullest definition in November 2025 |
| 9 | Four BlackRock speakers, 2024 to 2025, and the three pillars each names | All four speakers name APIs and events and the Data Cloud; only Goel and Woodhead name developer tools |

Checks on the proposed titles: Exhibit 5, 74 + 53 = 127 operations and the Stable column sums to 23 (2+8+0+4+3+2+1+1+1+0+1). Exhibit 7, Studio 4, State Street 4, Bloomberg 5, MSCI 2, other data and cloud platforms 9 to 16. Exhibit 8, Khara's interview is early 2024 and Woodhead's podcast November 2025.

---

## Items noted but not rewritten

- Page 4, the Woodhead quotation is verbatim from a machine transcript ("a set of APIs events"). Leave it, but the bridge sentence in 4.1 gives the reader the plain version.
- Page 5, Exhibit 3 is a diagram; its cells are fragments by design and read fine except 5.1 and 5.2.
- Page 6, Exhibit 5 cells are numbers and API names; nothing to rewrite beyond 6.1.
- Page 7, Exhibit 7 legend ("2: Fully public or self-serve ...") is clear.
- Footer line on every page reads cleanly.
