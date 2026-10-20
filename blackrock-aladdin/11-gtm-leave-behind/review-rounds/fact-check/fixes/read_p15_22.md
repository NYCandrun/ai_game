# Readability review: preview pages 15 to 22

Scope: Exhibit 15, Part 4, Exhibit 16, Exhibit 17 (scores, notes, closing paragraph), About, and the Sources register. Current pages 14 to 19 map to preview pages 15 to 22. Images were rendered at 80 dpi, and at 150 dpi for close checks, under rp15/.

Per the author's update, I did not judge which new register entries could be dropped. All 31 new entries were checked for title, date, URL and readability (see "New register entries" below).

## Fix table

| fix id | where (preview page) | verdict | problem | proposed cleaner text (visible words) |
|---|---|---|---|---|
| p14-02+p14-04 | 15, Exhibit 15 row 1 | CLEARER | "An answer on Snowflake and Databricks connectors" reads better than "the Snowflake and Databricks answer". The cell grows by one line, but the row stays balanced. | Keep as drafted. |
| p14-ex15-row | 15, Exhibit 15 row 2 | SAME | No change. | None. |
| p14-15 | 15, Part 4 paragraph | WORSE | The nested list "open the catalog, the API guides or their notebooks and code samples, or test …" is tangled: three "or"s in one clause. The old semicolon also stays in. | "I could not run anything or test what a client receives. I could not open the catalog, the API guides, or the guides' notebooks and code samples. Where this document describes those, it relies on what sources say." |
| p14-18 | 15, Exhibit 16 Hear row | CLEARER | The cell is more specific. The Receipt cell grows to 5 lines, the tallest in the exhibit, but it still reads cleanly. | Keep as drafted. |
| p14-24 | 15, Exhibit 16 Read row | SAME | The quotation is now exact. It adds one wrapped line ("Aladdin APIs"). | Keep. |
| p14-25 | 15, Exhibit 16 Read row receipt | SAME | "developer portal 6, 37, 41": 37 is a Technical Writer job posting, but its label says "developer portal". A reader who clicks 37 expects the portal. | "Studio page 13, APIs page 28, developer portal 6, 41, job posting 37" |
| p14-28 | 15, Exhibit 16 See the catalog receipt | SAME | One more receipt. The cell fits in 2 lines. | Keep. |
| p15-08+p15-10 | 16, Exhibit 16 Build and Get help rows | SAME | Build gains "sample code and demo notebooks" (clear). Under Get help, "Pull requests … reviewed and merged by a BlackRock engineer" is accurate, but merged pull requests read less like help than "answered" did. "Jupyter notebooks and code samples from the API guides" is clearer than "Notebooks, code samples, support". | Keep. Optional: "Pull requests on the SDK, merged by a BlackRock engineer; on the Studio page, "Book a meeting" and "Download the brochure"". |
| p14-25+p14-28 (exhibit note) | 16, Exhibit 16 source note | SAME | "…opens only after a client login 6, 41, so I could not test it." In this sentence, "it" seems to mean the portal, but it means the column. The note grows to 2 lines. | "The After qualification column is what those sources say a client receives. I could not test it, because the developer portal opens only after a client login 6, 41." |
| p15-26+p15-27+p15-28+p15-29 (DECIDE, Bloomberg row) | 16, Exhibit 17 | SAME | The row reads fine. Bloomberg now totals 8, the same as MSCI (8). So "investment platforms cluster low" is still true, but the gap at the boundary is gone. | None. |
| p15-43 (State Street sample code 1) | 16, Exhibit 17 | SAME | None. | None. |
| p15-54 (Arcesium trial 1, CTA 1) | 16, Exhibit 17 | SAME | None. | None. |
| p15-97+p15-102 (FactSet trial 1, CTA 1) | 16, Exhibit 17 | SAME | None. | None. |
| p15-103+…+p15-110 (MSCI row) | 16, Exhibit 17 | SAME | None. MSCI now totals 8, the same as Bloomberg. | None. |
| p15-38 (DECIDE, Call to action definition) | 16, Exhibit 17 notes | CLEARER | Makes the 0s for Studio, SimCorp and Clearwater make sense. It adds 2 lines to page 16, which helps push the closing paragraph onto page 17 (see Layout). | Keep. |
| p15-31+…+p15-106 (source note CITE) | 16, Exhibit 17 source note | SAME | The superscript now holds 26 numbers (2, 4, 5 … 102) and fills most of a line. That is tolerable in a source note but visually heavy. | Keep. If space is needed: "Source: my test of each platform's public pages, listed in Sources [list], no accounts or payments, October 8, 2026." |
| p15-114 (CITE) | 17, closing paragraph line 1 | WORSE | Nine superscripts (4, 7, 13, 71, 88, 89, 90, 91, 92) sit on a short opening line. The list also leaves out Bloomberg (93, 73) and Clearwater (72), so it does not cover all 10 platforms, which is what the citation is meant to show. The exhibit note directly above already cites every page. | "Exhibit 17 puts Studio beside 10 platforms that a Studio buyer also deals with." (no superscript, because the exhibit's source note carries the receipts) |
| p15-116 | 17, closing paragraph | CLEARER | Now matches the three-level legend. About ten words longer, but plain. | Keep. |
| p15-118 (DECIDE) + title | 16 title, 17 paragraph | WORSE (sentence), SAME (title) | "full documentation, a sandbox and a first call mostly come after" stacks two hedges ("full", "mostly") on one list. The title with "mostly" still wraps to 2 lines, as before. | Sentence: "At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, a first API call needs a contract or a relationship." (This is the plan's alternative. It holds for all six rows, because every investment platform scores 0 for first API call, Bloomberg included under the recommended score.) Title can stay. |
| p15-119 (DECIDE, recommended text only) | 17, closing paragraph | CLEARER | Three short sentences that name the platforms, which is plainer than "Data and cloud platforms … cluster high". Only "keep a first API call for licensed clients" reads slightly odd. The extra group row in the preview belongs to the alternative, was applied by mistake, and is not judged here. The band stays "Data and cloud platforms". On the alternative: splitting the band into "Cloud data platforms" and "Market data vendors" would make the exhibit's two-tier pattern visible at a glance, but it adds a row and the page is already over-full (see Layout). The recommended sentence is the better fit. | "Snowflake and Databricks sell to developers directly and score highest. LSEG and FactSet come next. FactSet and MSCI allow a first API call only for licensed clients 4, 88." |
| p16-02 | 18, About | SAME | Fuller and accurate. In "Others are public code …", "Others" is vague. The paragraph grows from 3 to 5 lines. | "The sources are BlackRock product pages, investor presentations, SEC filings, a fund prospectus, procurement notices, press releases and job postings. They also include public code and packages on GitHub and PyPI, other vendors' product and developer pages, blogs and trade press. The rest are transcripts of recordings and earnings calls with BlackRock speakers." |
| p16-05 | 18, About | SAME | Longer but clear. | Keep. |
| p16-09 | 18, About | SAME | "publisher or speaker, and date where known" is fine. | Keep. |
| p16-10 | 18, About | CLEARER | Matches BlackRock's own wording. | Keep. |
| s02 | 19, entry 2 | CLEARER | Full title and exact date. | Keep. |
| s04 | 19, entry 4 | CLEARER | Full title and exact date. | Keep. |
| s09 | 19, entry 9 | SAME | The title is now Title Case as published. The cue list is longer (14 times) but correct and readable. | Keep. |
| s21 | 20, entry 24 | CLEARER | Date added, and the unused cue was dropped. | Keep. |
| p07-16 (Khara entry) | 20, entry 42 | SAME | The entry now has two URLs and runs 7 lines, but it reads clearly. | Keep. |
| s31 (+ receipt "Snowflake video, May 2026") | 20, entry 43 | SAME | "BlackRock. Snowflake Inc., May 21, 2026." reads a little choppily. | "…Global Head of Data Platform and Product Engineering, BlackRock. Snowflake video, May 21, 2026." |
| s36 | 20, entry 48 | SAME | Date only. | Keep. |
| s40 | 20, entry 36 | CLEARER | Authors and exact date added. | Keep. |
| s54 | 21, entry 68 | CLEARER | Both speakers are named. The "left unnamed" closing reads cleanly. | Keep. |
| s59 (+ receipt link) | 21, entry 75 | SAME | Title, date and URL updated. | Keep. |
| s60 (+ Exhibit 12 receipt) | 21, entry 76 | WORSE | One long sentence with four clauses. It also drops the "Job posting:" prefix that entries 44, 81 and 85 use, so the register is now inconsistent. | "Job posting: Forward Deploy Engineer, Aladdin Data, Associate (R264906, Mumbai). BlackRock, posted September 4, 2026. Removed from BlackRock Careers by October 20, 2026. Copy kept by Saarthi. [URL]" |
| s66 (finding s65) | 21, entry 87 | CLEARER | Real PR title and exact date. | Keep. |

## New register entries (31): accuracy and readability

I fetched each URL on October 20, 2026, and compared the title, date and URL with the entry. Unless a problem is listed, the entry matched.

- 12 (Feb 5, 2026 press release): the H1 and date match.
- 14 Whole Portfolio Management: the title matches. The URL redirects to https://www.blackrock.com/aladdin/platforms/products/whole-portfolio. Use that canonical address.
- 16 eFront Insight, 27 Risk Management Services, 29 ATX, 30 ADX: page titles match.
- 18 AWS release (TradingView): the title matches the page, but the "PRESSR:" wire tag is clutter. The publisher clause is long ("BlackRock press release with its questions and answers, distributed by Reuters and carried by TradingView News"). This is the same release as entry 32 (Amazon copy), so readers will see two entries for one release. Suggested: "BlackRock partners with AWS to deliver Aladdin on secure, scalable cloud infrastructure (full release with questions and answers). BlackRock press release, Reuters copy on TradingView News, December 5, 2025."
- 31 Aladdin Data Cloud launch: the H1 and February 22, 2021 date match.
- 34 ICE (2016), 72 Clearwater (Business Wire), 100 Arcesium Marketplace (Business Wire), 102 databricks-sdk-py (GitHub): blocked (403) or not reachable from here. Not verified.
- 35 Sustainalytics: the H1 matches ("Access our research through your preferred platform"), and the page lists Aladdin under Institutional Investor Platforms. The page's own title is "Partner Platforms". Either name works.
- 37 Technical Writer (Built In Bristol), grade T: datePosted 2026-02-21 matches. Problems: (a) the title carries the site's " - BlackRock" suffix, (b) the job is in Edinburgh, not Bristol, and (c) the page says the job "was removed … on Monday, Feb 23, 2026". The quoted text ("Aladdin Studio Developer Portal", "event-driven workflows, including streaming APIs, webhook subscriptions") is on the page. Suggested: "Job posting: Technical Writer, Vice President (Edinburgh). BlackRock, posted February 21, 2026, removed February 23, 2026. Copy kept by Built In Bristol. [URL]"
- 39 Snowflake partner page (Wayback): timed out from here. Not verified.
- 41 developer portal: fine, and readable.
- 55 PPF contract notice 001014-2025: "Published 13 January 2025" and "between £43m and £55m across Lots 1 and 2 over the maximum contract term of 10 years" match.
- 57 Nest release: the H1 and 13 November 2023 match.
- 59 PBGC 2017 award: the API record shows signed 2017-09-28, end 2023-03-27, 4 offers, full and open. All match. Its URL style matches entry 58.
- 73 Bloomberg Enterprise MCP: the title and the "Sept. 29, 2026 /PRNewswire/" dateline match. The URL is a copy on webull.com, a brokerage news feed. A prnewswire.com or bloomberg.com copy would look more authoritative.
- 80 eFront acquisition: the H1 and May 10, 2019 match.
- 84 Client Forum: the page title is "Aladdin Client Forum 2026". The "invitation-only" and "select group of prospective clients" text is present.
- 85 Solutions Engineering VP: R265631, "Date posted: Oct. 02, 2026" and the "help prospective clients" text match.
- 93 Bloomberg API Library: the title matches.
- 94 Bloomberg App Portal PDF: the PDF has no title, so the descriptive name is fair. The June 30, 2022 creation date matches, and "more than 350,000 Bloomberg users" is present.
- 95 Aquata Demo Center: the title matches. The "30-day trial … no sales calls required" text is present.
- 96 MSCI Developer Community: the page is a JavaScript app with no readable text from here. Not verified.
- 97 MSCI API User Guide: the heading ("How to get access to MSCI APIs on Developer Community") and the December 13, 2021 date match.
- 98 msci.sdk: version 1.37.1, uploaded 2026-09-23, author MSCI. Matches.
- 99 SimCorp Data Model Portal: the H1 matches, and the "strictly limited and controlled by SimCorp" text is present.
- 101 Databricks REST API reference: the title matches. The URL redirects to /api/workspace/ (minor).
- Style across the register: new entries keep publishers' Title Case (12, 31, 72, 73, 80, 100, and the updated 9 and 36), while older entries use sentence case. Job postings now follow three different patterns (44/81/85 vs 37 vs 76). One pattern, "Job posting: Title (requisition, city). Publisher, date.", would read more evenly.

## Layout

- **Page 17: orphaned paragraph (BROKEN LAYOUT).** The 7-line closing paragraph of Exhibit 17 now sits alone at the top of an otherwise blank page 17. In the original it fit at the bottom of the page with the exhibit (original page 15). Several things grew on page 16: Exhibit 16's Build and Get help rows (about 2 lines), its source note (+1 line) and the new Call to action definition (+2 lines). Page 15 grew too, through the Hear, Read and See the catalog receipts. Page 16 has room for about 4 more lines, so roughly 4 to 5 lines must be saved. Options:
  1. Use the shorter rewrites above. p15-114 without superscripts, the p15-118 alternative and the one-line Exhibit 16 note would save about 1 to 2 lines.
  2. Fold the Call to action definition into one line with the AI connector definition, or shorten the source-note superscript run (it is already one line).
  3. Move Exhibit 17 and its paragraph to page 17 together. This leaves white space at the bottom of page 16 but keeps the exhibit with its text.
  Whatever is chosen, the paragraph must not stand alone on page 17.
- **Page 16, Exhibit 17 group band (preview artifact, not part of the recommended fix):** the preview shows "Cloud data platforms" over LSEG, FactSet and MSCI because the alternative's row change was applied by mistake. The final document keeps "Data and cloud platforms".
- **Page 16, Exhibit 17 source note:** a 26-number superscript run. It is legible at print size but dense.
- **Page 15, Exhibit 16:** the Hear receipt cell runs to 5 lines, and the Read receipt stacks "6, 37, 41" on one link. Nothing overflows. Exhibit 16 still splits across pages 15 and 16, as in the original, with the header repeated on page 16.
- **Page 16, Exhibit 17 title:** wraps to 2 lines, as before.
- **Page 18 (About):** grew from 10 to 13 lines. It fits easily on the page.
- **Pages 19 to 22 (Sources):** 102 entries over 4 pages in two columns. No broken entries and no cut-off URLs. Page 22 is about one third full. Number and grade columns line up.
