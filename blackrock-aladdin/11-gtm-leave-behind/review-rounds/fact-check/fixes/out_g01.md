# Group g01: drafted fixes

Counts: FIX 6, CITE 3, DECIDE 2, NO CHANGE 0. DECIDE: p02-09+p02-10, p03-16+p03-17.

## p02-05+p02-06+p02-07: FIX

Current: They post orders and set compliance rules, under each user’s permissions and with a compliance check on every order [6].

Proposed: They post orders and assign compliance rules to portfolios. OAuth sign-in grants read or write rights API by API, and compliance runs on each order by default [6].

Why: The order spec says “Filter, post or cancel orders”, but the compliance specs only filter rules and “assign compliance rules for portfolio” (ComplianceRuleAssignmentAPI). Every operation also accepts client-credentials, client-key and basic auth, so “each user’s permissions” overstates it, while OAuth scopes are read or write per API. runCompliance is “Default is true”, and the caller can turn it off, so “every order” becomes “by default”.

Also change (Exhibit 15, control box title (Part 3)): “Permissions per user” → “Access scoped per API”

Also change (Exhibit 15, control box title (Part 3)): “Compliance on every order” → “Compliance by default”

Also change (Exhibit 15 aria-label): “(permissions per user, a second approver, compliance on every order)” → “(access scoped per API, a second approver, compliance by default)”

Also change (Part 3 body, page 13): “call these APIs every day under each user’s permissions” → “Covered by the p02-09+p02-10 also_change for the same sentence.”

## p02-09+p02-10: DECIDE

Current: About 100 of its applications and thousands of Copilot tools already call these APIs every day [8].

Proposed: About 100 of its applications carry Copilot, whose tools each map to an Aladdin API already in production [8].

Alternative: About 100 of its applications carry Copilot. Copilot draws on about two thousand tools and agents, and each tool maps to an Aladdin API already in production [8]. (Keeps the counts but adds about one line to page 2.)

Decision: This sentence carries the claim that BlackRock already runs on the APIs it offers clients. The sources say the apps carry Copilot and each Copilot tool maps to a production Aladdin API. Neither says the apps or tools call the public Studio APIs, so the recommended text drops “these APIs” and “every day”. The nearest bridge is Woodhead (source 1): Studio “exposes everything Aladdin knows how to do as a set of APIs”. If the author can find a source saying the Studio APIs are the ones BlackRock’s own apps use, “these APIs” can stay. The lede can stay, because it rests on the controls built into the APIs.

Why: The talk says “around 100 Aladdin front-end applications that thousands of people use every day” [1:53], Copilot “is currently embedded across all of those hundred” [2:34], and a tool maps “one-to-one to an existing Aladdin API already out in production” [4:39]. The count is “a couple thousands agents and tools that are registered” [6:42]. “Every day” in the talk describes people using the apps and the daily test runs.

Also change (Part 3 body, page 13 (must not lengthen; the proposal is about the same length)): “About 100 of its applications and thousands of Copilot tools, built by 50 to 60 of its teams, call these APIs every day under each user’s permissions [8].” → “About 100 of its applications carry Copilot. Each Copilot tool maps to a production Aladdin API, and the team that owns it sets which user groups can use it [8].”

Also change (Exhibit 15, left box): “all call these APIs.” → “all carry Copilot.”

Also change (Exhibit 15, Copilot box): “Thousands of tools, each one an Aladdin
API, built by 50 to 60 BlackRock teams.” → “Thousands of tools and agents, from 50
to 60 BlackRock teams. Each tool maps
to an Aladdin API in production.”

Also change (Exhibit 15, API band caption): “BlackRock’s applications, Copilot and a client’s own code call the same APIs and read the same Data Cloud, the client’s Aladdin data in a Snowflake account BlackRock runs for it.” → “Copilot’s tools map to Aladdin’s production APIs. Studio offers a client’s own code Aladdin’s APIs and its Data Cloud, the client’s Aladdin data in a Snowflake account BlackRock runs for it.”

Also change (Exhibit 15 aria-label): “All sit on one band, Aladdin's APIs, which all of them call and whose Data Cloud they read.” → “All sit on one band, Aladdin's APIs and Data Cloud. Copilot's tools map to these production APIs.”

## p02-14: FIX

Current: 11 public asdk_plugin Python packages, 128 recordings,

Proposed: 11 public asdk_plugin Python packages, about 125 recordings,

Why: The two corpus indexes have 34 and 95 rows, which gives 129. One row is text notes, at least three recordings appear in both indexes, and at least one is in neither, so there are about 126 distinct recordings. The 11 packages and 54 specifications were reconfirmed on PyPI.

Also change (Part 2, opening of the definitions section): “Five BlackRock speakers define Studio in the 128 recordings I pulled for this document” → “Five BlackRock speakers define Studio in about 125 recordings I pulled for this document”

## p02-20: FIX

Current: at the end of this document, giving the grade (P, S or T), title, speaker and date.

Proposed: at the end of this document, giving the grade (P, S or T), title, publisher or speaker, and date where known.

Why: P entries name a publisher, not a speaker, such as “Aladdin Data Cloud product page. BlackRock, as of October 2026.” Several entries have no date, such as source 20 (“undated”), source 21 (“speaker not named, undated”) and source 9 (“Replay page undated”).

Also change (Note before Sources (page 16)): “gives each source’s grade (P, S or T), title, speaker and date.” → “gives each source’s grade (P, S or T), title, publisher or speaker, and date where known.”

## p03-02: FIX

Current: Brennan Rosales, its AI Engineering Lead, put the scale

Proposed: Brennan Rosales, an AI Engineering Lead at BlackRock, put the scale

Why: He introduces himself as “an AI engineering lead at BlackRock” [0:15], and the LangChain Interrupt speaker list gives “AI Engineering Lead at BlackRock”. “Its” makes him the only one.

## p03-14: FIX

Current: BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code.

Proposed: BlackRock sells Aladdin as one family of the Aladdin platform, eFront, Aladdin Wealth and Preqin, joined by a common data language [NEW]. Studio is the entry point for people who write code [14].

Why: BlackRock’s 5 February 2026 release says “BlackRock Aladdin, inclusive of the Aladdin platform, eFront, Aladdin Wealth, and Preqin … providing a common data language across the whole portfolio.” “One engine” overstates it, because BlackRock lists four platforms and sells eFront and Preqin on their own. The Studio page says “Build on top of Aladdin”, so source 14 supports the second sentence.

New source: NEWPBlackRock Aladdin Drives Private Markets Transparency By Unifying Pre- and Post-Investment Tech On a Single Platform. BlackRock press release, February 5, 2026. https://www.blackrock.com/aladdin/discover/press-release/blackrock-aladdin-drives-private-markets-transparency

Also note (Exhibit 1 title): See p03-16+p03-17. The new sentence names Preqin as part of the family, and Exhibit 1 has no Preqin row. The recommended Exhibit 1 title handles this.

## p03-16+p03-17: DECIDE

Current: Exhibit 1. Of Aladdin’s eight named products, Studio is the one for people who write code

Proposed: Exhibit 1. Of eight Aladdin products, Studio is the one for people who write code

Alternative: Exhibit 1. Of nine Aladdin products, Studio is the one for people who write code plus a new Preqin row after eFront: PreqinPrivate-markets data and analytics, bought by BlackRock in 2025 [11]Private-markets investors and fund managers. This matches the four-part family in the new Part 1 sentence, but it adds a row to page 3.

Decision: The count sits in an exhibit title. BlackRock names no set of eight. Its Aladdin site links to at least 13 products and solutions, and its boilerplate names four platforms, one of them Preqin. The recommended title keeps the eight rows and drops the claim that BlackRock names exactly eight. Nothing else in the document repeats “eight named products”.

Why: BlackRock’s Aladdin home page links to Accounting, Climate Risk, Aladdin Copilot, Aladdin Data Cloud, Asset Servicers, Risk Management, Aladdin Studio, Sustainability, Whole Portfolio, Aladdin, Aladdin Wealth, eFront and Preqin. All eight rows are real products, but the set of eight is the author’s choice.

## p03-19: FIX

Current: The front-to-back system for public markets, the same system BlackRock runs internally [8]

Proposed: The front-to-back system for public and private markets [NEW], the same system BlackRock runs internally [8]

Why: BlackRock’s Whole Portfolio page says “Streamline front-to-back workflows with a unified IBOR for public and private assets.” Source 8 says Aladdin gives “access to both public and private markets” and “BlackRock is the biggest user of Aladdin”, but never says “front-to-back”.

New source: NEWPWhole Portfolio Management. BlackRock Aladdin product page, as of October 2026. https://www.blackrock.com/aladdin/view-whole-portfolio

Also change (Exhibit 1 source note (page 3). One combined change covers p03-19, p03-27, p03-30 and p03-36.): “Source: BlackRock product pages [14, 17, 19]; Amazon press release, December 2025 [15]; iShares prospectus [18]; the public specifications [6].” → “Source: BlackRock product pages [14, 17, 19, NEW, NEW]; BlackRock’s AWS release and its questions and answers, December 2025 [NEW]; Woodhead [1]; iShares prospectus [18]; the public specifications [6].”

## p03-27: CITE

Current: Preqin now sits inside eFront Insight, and

Proposed: Preqin now sits inside eFront Insight [NEW], and

Why: The eFront Insight page says “With Preqin® inside, eFront® Insight makes private markets investing more seamless and more informed.” Source 13 says only that the expansion “brings together Aladdin technology with Preqin and eFront data and analytics”, so 13 stays on the May 2026 clause.

New source: NEWPPowerful Analytics for Private Markets (eFront Insight product page). eFront, BlackRock, as of October 2026. https://www.efront.com/en/alternative-investment-software/efront-insight

Also note (Exhibit 1 source note): See the combined note change under p03-19.

## p03-30: CITE

Current: It covers APIs and events, Aladdin Data Cloud, and developer tools. BlackRock calls it

Proposed: It covers APIs and events, Aladdin Data Cloud, and developer tools [1]. BlackRock calls it

Why: Source 14 covers APIs, Data Cloud and developer tools but not events. Woodhead (source 1, already cited for the same list on page 2) says Studio “exposes everything Aladdin knows how to do as a set of APIs [and] events” and that Data Cloud is “built on top of Snowflake”.

Also note (Exhibit 1 source note): See the combined note change under p03-19, which adds Woodhead (source 1).

## p03-36: CITE

Current: It is sold as an add-on to Aladdin Enterprise [15].

Proposed: It is sold as an add-on to Aladdin Enterprise [NEW].

Why: The full release with its questions and answers says AWS hosting will first cover “Aladdin Enterprise (US-hosted only) Accounting (Enterprise add-on) ADC (Enterprise add-on)”. The Amazon copy (source 15) has no “add-on” wording. Source 15 stays in the register because Exhibit 3 still cites it for hosting.

New source: NEWPPRESSR: BlackRock partners with AWS to deliver Aladdin on secure, scalable cloud infrastructure. BlackRock press release with its questions and answers, distributed by Reuters and carried by TradingView News, December 5, 2025. https://www.tradingview.com/news/reuters.com,2025-12-05:newsml_Zaw4R27h7:0-pressr-blackrock-partners-with-aws-to-deliver-aladdin-on-secure-scalable-cloud-infrastructure/

Also change (Exhibit 1 source note (page 3). One combined change covers p03-19, p03-27, p03-30 and p03-36.): “Source: BlackRock product pages [14, 17, 19]; Amazon press release, December 2025 [15]; iShares prospectus [18]; the public specifications [6].” → “Source: BlackRock product pages [14, 17, 19, NEW, NEW]; BlackRock’s AWS release and its questions and answers, December 2025 [NEW]; Woodhead [1]; iShares prospectus [18]; the public specifications [6].”
