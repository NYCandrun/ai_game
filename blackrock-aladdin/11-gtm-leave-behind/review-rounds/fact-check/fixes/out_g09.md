# g09 fix drafts (Exhibit 17 scores and citations)

Source numbers here are those in current.html: 67 FactSet portal, 68 State Street portal, 69 LSEG portal, 70 Snowflake developers, 71 Try Databricks. The findings used the older numbering, one lower.

Corrected row totals out of 16: Bloomberg 8 (was 5), Aladdin Studio 4, State Street 5 (was 4), Arcesium 4 (was 3), SimCorp 1, Clearwater 1, Snowflake 16, Databricks 16, LSEG 12, FactSet 11 (was 9), MSCI 8 (was 2).

## p15-26+p15-27+p15-28+p15-29: DECIDE

**Current:** Bloomberg: Public docs 1, API catalog 0, Trial or sandbox 1, First API call without a contract 1, Sample code 1, Community or marketplace 0, AI connector 0, Call to action 1

**Proposed:** Bloomberg: Public docs 1, API catalog 0, Trial or sandbox 1, First API call without a contract 0, Sample code 2, Community or marketplace 1, AI connector 2, Call to action 1

**New sources:**

- NEW, grade P: API Library. Bloomberg Professional Services, as of October 2026. https://professional.bloomberg.com/support/api-library/
- NEW, grade P: App Portal overview for developers. Bloomberg Professional Services, PDF dated June 30, 2022. https://assets.bbhub.io/professional/sites/10/App-Portal-Overview-for-Developers.pdf
- NEW, grade P: Bloomberg Launches Enterprise MCP to Seamlessly Connect Bloomberg Data with Clients’ Enterprise AI Applications. Bloomberg press release (PR Newswire), September 29, 2026. https://www.webull.com/news/15660486556124160

**Also change:**

- Exhibit 17 source line (the citations for this row): Adds NEW API Library, NEW App Portal overview and NEW Bloomberg MCP release (shared with g06 p11-34; keep one register entry, id sNEW-g06-bbg).
- Exhibit 12 note, page 11 (owned by g06 p11-34): Use the g06 p11-34 draft, which already lists the Bloomberg MCP launch. An AI connector score of 2 here and "no AI announcement" there cannot both stand.
- Part 4 body after Exhibit 17 (owned by g08 p15-118 and p15-119): No change needed from this row: Bloomberg rises from 5 to 8 of 16, still the top of a low cluster, and its first call now scores 0. g08 should use the corrected totals listed in this file.
- Alternative, if the author prefers to count Bloomberg's emailed trial as sign-up and to judge sample code on completeness: Bloomberg: Public docs 1, API catalog 0, Trial or sandbox 1, First API call without a contract 1, Sample code 1, Community or marketplace 1, AI connector 2, Call to action 1

**Why:** Bloomberg's API Library says its libraries "are only compatible with the Bloomberg Server API and B-Pipe data feed products", and the trial needs a signed Trial License Agreement, so a first call needs a contract (0). The same public page offers SDK zips with 127 example files, so sample code is public (2). The App Portal PDF describes a third-party app marketplace for "more than 350,000 Bloomberg users", which matches the 1 given to other client-only marketplaces. Bloomberg launched Enterprise MCP on September 29, 2026, which the exhibit's own footnote scores 2. DECIDE because the AI connector change must match the Exhibit 12 note (g06), and the first-call and sample-code scores have a reasonable alternative.

## p15-43: FIX

**Current:** State Street: Public docs 1, API catalog 0, Trial or sandbox 1, First API call without a contract 0, Sample code 0, Community or marketplace 1, AI connector 0, Call to action 1

**Proposed:** State Street: Public docs 1, API catalog 0, Trial or sandbox 1, First API call without a contract 0, Sample code 1, Community or marketplace 1, AI connector 0, Call to action 1

**Also change:**

- Exhibit 17 source line: No new citation. Source 68, the State Street developer portal, already covers this page.

**Why:** The public Development Environment page gives one complete example, in cURL, NodeJS, Python and Java, that gets a token and calls Sample Transactions ("find an example below that incorporates authentication and a successful invocation of State Street API"). Running it needs client credentials and there is no public SDK, so the score is 1, partial. Source 68 already covers it.

## p15-54: FIX

**Current:** Arcesium: Public docs 0, API catalog 0, Trial or sandbox 0, First API call without a contract 0, Sample code 0, Community or marketplace 1, AI connector 2, Call to action 0

**Proposed:** Arcesium: Public docs 0, API catalog 0, Trial or sandbox 0, First API call without a contract 0, Sample code 0, Community or marketplace 1, AI connector 2, Call to action 1

**New sources:**

- NEW, grade P: Demo Center. Aquata by Arcesium, as of October 2026. https://aquata.ai/demo-center

**Also change:**

- Exhibit 17 source line: Adds NEW Aquata Demo Center.
- Depends on the Call to action definition (object p15-38): Score 1 fits "a developer can request a trial or access". If the author takes the p15-38 alternative, it stays 1.
- Outside this group, for the author to check: Arcesium "Trial or sandbox" is 0, and the Part 4 body says a sandbox comes after a relationship (g08 p15-118): Aquata offers "a 30-day trial" on request with "no sales calls required", which may support 1 for Trial or sandbox. Not changed here because no finding covers it.

**Why:** Aquata, Arcesium's platform, has a public free-trial request: "You can request a 30-day trial ... There are no sales calls required to get started." A trial request scores 1 under the Call to action definition in p15-38.

## p15-97+p15-102: FIX

**Current:** FactSet: Public docs 2, API catalog 2, Trial or sandbox 0, First API call without a contract 0, Sample code 2, Community or marketplace 1, AI connector 2, Call to action 0

**Proposed:** FactSet: Public docs 2, API catalog 2, Trial or sandbox 1, First API call without a contract 0, Sample code 2, Community or marketplace 1, AI connector 2, Call to action 1

**Also change:**

- Exhibit 17 source line: No new citation. Source 67, the FactSet developer portal, holds the contact page and the getting-started page.
- Depends on the Call to action definition (object p15-38): Call to action 1 fits "a developer can request a trial or access".

**Why:** FactSet's developer portal invites requests for "a free trial to our APIs", and access follows a login with a corporate email or approval. That is "after sign-up or approval", so Trial or sandbox and Call to action both score 1, as Bloomberg and State Street do. Source 67 supports it.

## p15-103+p15-104+p15-107+p15-108+p15-110: FIX

**Current:** MSCI: Public docs 0, API catalog 0, Trial or sandbox 0, First API call without a contract 0, Sample code 0, Community or marketplace 0, AI connector 2, Call to action 0

**Proposed:** MSCI: Public docs 1, API catalog 2, Trial or sandbox 0, First API call without a contract 0, Sample code 1, Community or marketplace 1, AI connector 2, Call to action 1

**New sources:**

- NEW, grade P: MSCI Developer Community. MSCI, as of October 2026. https://developer.msci.com/
- NEW, grade P: MSCI API User Guide: how to get access to MSCI APIs on Developer Community. MSCI, PDF dated December 13, 2021. https://www.msci.com/documents/1296102/28171902/MSCI-API-Developer-Community-User+Guide.pdf
- NEW, grade P: msci.sdk, version 1.37.1. PyPI, published by MSCI, September 23, 2026. https://pypi.org/project/msci.sdk/

**Also change:**

- Exhibit 17 source line and its access caveat: Adds the three MSCI sources and drops MSCI from the "blocked automated access" caveat, since developer.msci.com answers plain requests.
- Depends on the Call to action definition (object p15-38): Call to action 1 fits "a developer can request a trial or access".
- Part 4 body after Exhibit 17 (owned by g08 p15-119): MSCI rises from 2 to 8 of 16 and FactSet from 9 to 11. g08 should use these totals if its draft quotes scores.

**Why:** MSCI's Developer Community is public: it has a catalog of 28 APIs ("Explore our catalog to find APIs"), public overview pages, a public SDK with example code on PyPI, and Skills and Labs sections. API definitions and notebook downloads need a login, and keys come through a "Get Access" request, so docs, sample code, community and call to action score 1 and the catalog 2. The row link moves to the portal because the old link was the AI-connector press release. Trial or sandbox and First API call stay 0 (see p15-105+p15-106).

## p15-38: DECIDE

**Current:** For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform.

**Proposed:** For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform.

For the Call to action score: 2 means a developer can sign up and start alone. 1 means a developer can request a trial or access. 0 means the page offers only sales contact, such as a meeting or a demo.

**Also change:**

- Rows that rely on this definition: Each moves to 1 under this definition. Studio, SimCorp and Clearwater stay 0. Snowflake and Databricks stay 2.
- Alternative: count any call to action, sales contact included, as 1: For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform.

For the Call to action score: 2 means a developer can sign up and start alone. 1 means the page offers a request form, a meeting or a demo.
- If the alternative is chosen, these Call to action cells (the last cell of each row) also go from 0 to 1: 1. Studio then shows "Book a meeting", which Exhibit 16 already quotes.

**Why:** The Studio page offers "Book a meeting" and "Download the brochure", so it has calls to action, but they are sales contacts. Clearwater and SimCorp have the same kind and also score 0, while the 1s go to trial or access requests such as State Street's "Get Started". A one-line definition makes the 0 accurate and keeps the column consistent. DECIDE because the definition sets the scale for the whole column.

## p15-31+p15-32+p15-52+p15-55+p15-56+p15-57+p15-58+p15-77+p15-80+p15-83+p15-85+p15-93+p15-105+p15-106: CITE

**Current:** Source: my test of each platform’s public pages [4, 7, 14, 57, 67, 68, 69, 70, 71], no accounts or payments, October 8, 2026. Bloomberg, Clearwater and MSCI may score lower than they deserve, because some of their pages blocked automated access.

**Proposed:** Source: my test of each platform’s public pages [2, 4, 5, 6, 7, 14, 23, 24, 57, 59, 67, 68, 69, 70, 71, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW, NEW], no accounts or payments, October 8, 2026. Bloomberg and Clearwater may score lower than they deserve, because some of their pages blocked automated access.

**New sources:**

- NEW, grade P: Data Model Portal. SimCorp, as of October 2026. https://thesim.dev/
- NEW, grade P: Arcesium Unveils Aquata® Marketplace to Power Data Connectivity, Elevate Workflows and Accelerate AI Readiness for Institutional Investors. Arcesium press release (Business Wire), October 7, 2025. https://www.businesswire.com/news/home/20251007929556/en/
- NEW, grade P: Databricks REST API reference. Databricks, as of October 2026. https://docs.databricks.com/api/workspace/introduction
- NEW, grade P: Databricks SDK for Python, README and examples, databricks/databricks-sdk-py. GitHub, as of October 2026. https://github.com/databricks/databricks-sdk-py

**Also change:**

- New register entries used here but listed in other objects: Bloomberg entries in p15-26+...; MSCI entries in p15-103+...; Aquata entry in p15-54. The Bloomberg MCP entry is shared with g06 as sNEW-g06-bbg.
- Page fit: The source line grows by about one line on page 15. Exhibit 17 is not on page 13 or page 2.

**Why:** The scores in these cells are right, but the cited sources did not show them. Studio docs and catalog: sources 6, 23 and 24 (SDK README, PyPI plugins, APIs page). SimCorp: thesim.dev, whose content "is strictly limited and controlled by SimCorp". Arcesium marketplace: the Aquata Marketplace release ("available to users of the Aquata platform"). Snowflake and LSEG AI connectors: sources 5 and 2. Databricks: the REST API reference, the SDK README examples and source 59, which lists "Claude Code, Codex, Cursor" setups. MSCI trial and first call: the portal and user guide, where clients without keys can try APIs "only after requesting for the API Keys". MSCI leaves the access caveat because its developer portal answered plain requests.
