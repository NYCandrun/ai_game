# Exhibit 3 previews: three variants

The real file was not modified. Every preview is built by `build.py` in this folder, which reads the real file and writes a copy. The real file was updated to v17 (the source fixes) at 16:17 while this work was in progress. All three previews are built from v17, so no port is needed. If the real file changes again, rerun `python3 -I build.py`. Citations are resolved by URL against the live register, so the build follows any renumbering. After the replacement, the build runs `gtm/renumber.py`, sorts the flat register numerically and sorts the numbers inside each superscript.

Files:
- `preview_A.html`, `preview_A.pdf`
- `preview_B.html`, `preview_B.pdf`
- `preview_C.html`, `preview_C.pdf`
- `compare_ex3.png`: four panels at 110 dpi, in this order: current page 5, A, B, C.

Exhibit 1 was not changed (scope change). No register entries were added. Before the change of scope I had confirmed the Aladdin Climate product page live (https://www.blackrock.com/aladdin/platforms/products/aladdin-climate, page title "Climate Scenarios and Risk Analytics | Aladdin by BlackRock"). It is not used in any preview.

## Variant A: layered stack (adapted from the briefing's Exhibit 23)

Title (unchanged): "Apps, Copilot and Studio share the same Aladdin services and data".

The exhibit is an HTML/CSS grid that uses the document's tokens: Barlow and Barlow Condensed, a yellow Studio band, a pink Copilot tile as in Exhibit 14, a black core band and a dashed outside-inputs box. Text is 9pt and the labels are 8pt.

Layers, from top to bottom:
1. **Who builds:** client engineers; code-curious portfolio managers; data analysts; Excel users building reports.
2. **BlackRock's own applications:** about 100, such as Explore, Dashboard and Risk Radar. Aladdin Copilot sits inside them, and each Copilot tool matches an Aladdin API already in production.
3. **Aladdin Studio:** six tiles.
   - APIs that read and write Aladdin data.
   - Event-driven workflows.
   - Python SDK, Aladdin Compute and notebooks.
   - Aladdin Data Cloud on Snowflake, each client's own data store.
   - Aladdin Tools for Excel and the Data eXchange.
   - Data Dictionary and Developer Portal, behind a client login.
4. **Aladdin's shared services and data:** portfolio management, trading, risk, compliance, operations and accounting. The band lists the 11 public API domains by name, with the hyphenated names used in the specifications.
5. **Outside inputs:** the client's own and third-party data, loaded into Data Cloud or through the Data eXchange, and vendor data such as prices and ESG research.

A side column titled "Controls built into the APIs" spans layers 2 to 4. It copies Exhibit 14's wording word for word:
- Access set per API
- Compliance by default (the order API)
- A second approver (dataset releases)

The source note cites every current Exhibit 3 source, plus the developer portal register entry. Hosting moved from the drawing into the note: Azure, with an AWS option announced for US-hosted Aladdin Enterprise clients.

### New or reworded facts in A, each checked live on 2026-10-20

| Wording in A | Source | Quote |
|---|---|---|
| "Excel users building reports" | ATX page | "an Excel plugin that enables users to retrieve Aladdin data to build custom reports" |
| "each client's own data store" | Data Cloud launch release | "Each Aladdin Data Cloud client receives an independent, centrally-managed data store" |
| Client and third-party data loaded into Data Cloud | Data Cloud launch release | "can then be supplemented with proprietary and other third-party data sources" |
| Data loaded through the Data eXchange | ADX page | "load large custom data sets to Aladdin through Aladdin Data eXchange (ADX)" |
| "Aladdin's shared services and data" list | The 11 SDK package names (accounting, analytics, clients, compliance, data, investment-operations, investment-research, platform, portfolio, portfolio-management, trading) and the Aladdin Risk page for "risk" | Not "one shared record" or "one data model" |

All other wording repeats fact-checked text already in the document:
- About 100 apps, Copilot in them, and each tool mapped to a production API: Rosales and Vicente Valdez.
- Dashboard and Risk Radar: named in the specifications.
- Notebooks: the APIs page.
- Portal behind a client login: the developer portal entry.

Dropped from the current map:
- "Aladdin Analytics" as an engine name
- "test trades" for Explore
- Brokers and custodians
- The individual shared-data cylinders

## Variant B: the Studio parts named in the SDK files (adapted from "What It Does", Exhibit 3)

Title: "The Studio parts named in BlackRock's public SDK files".

**Variant B does not carry the message "Apps, Copilot and Studio share the same Aladdin services and data."** It shows what is inside Studio. Every Exhibit 3 source has to stay cited, so B's note adds one context sentence taken from the current Exhibit 3: apps and Copilot draw on the same services, along with Explore, the risk engine, the hosting, and ICE and Sustainalytics data. I added no new content to stand in for the message.

Facts in B, each checked against the live README (raw.githubusercontent.com/blackrock/aladdinsdk/main/README.md, HTTP 200) and against the unpacked specifications:

| Wording in B | Quote from the file |
|---|---|
| Login apps (OAuth) made "under a Project in Studio" | README: "Create/Modify OAuth Application under a Project in Studio" |
| Storage bucket keys from "S3 Storage Integration in a Studio Project" | README storage settings: "To be sourced from S3 Storage Integration in a Studio Project"; "Bucket assigned to user/project workspace" |
| Compute sessions | README: "AladdinSDK can run on a developer's local machine or in Aladdin Studio Compute sessions" |
| API tokens "registered via Studio UI" | README: "API Token registered via Studio UI" |
| Alerts by email or push to a user, project or space | README notification settings: STUDIO_NOTIFICATION_ACTION_SMTP / _PUSH; STUDIO_ENTITY_TYPE_USER / _PROJECT / _SPACE |
| Spaces: named, role not described | README names Space only as a notification event type and entity type |
| ADC Admin Center: dataset owners edit Data Cloud datasets before a second check | AdcDatasetAPI: "Manages Datasets in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center."; "dataset owners may update the dataset details in Admin Center"; "ready for a 4-eyes check prior to release" |
| Counts: 54 public specifications, 301 operations, 11 packages | Recomputed from the unpacked folder (`scratchpad/unpacked`): 54 Swagger files, 301 operations, 11 packages. The other document's "58 APIs, 326 operations" was not used. |

Other points for the author:
- The other document's "INFERENCE / STRONG" flag became a yellow "My reading" tag: "These parts form one hosted place to build". This label is new to this document, whose key is P/S/T only. The wording follows the fact-checked "hosted places to build".
- I added a third base box, ATX and ADX "linked from the APIs page", so that Exhibit 4's note "which Exhibit 3 shows" stays true.
- Dropped as unverified: nothing. The other document's Exhibit 3 boxes all checked out.

## Variant C: one stack replaces Exhibits 3 and 4

C starts from A. The Studio band becomes Exhibit 4's six pieces, each with one plain line:
- APIs (Aladdin Graph): read and write Aladdin data
- Event-driven workflows: Aladdin tells a program when something happens
- Aladdin Data Cloud: a managed data store on Snowflake, Fivetran moving the data
- Aladdin Compute: hosted Python environments
- Aladdin SDK: open-source Python library for login, retries, rate limits
- Developer Portal and Data Dictionary: behind a client login

A slim line below the tiles reads: "The APIs page also links Aladdin Tools for Excel and the Aladdin Data eXchange". It keeps the ATX and ADX sources cited.

The note now also cites every Exhibit 4 source:
- Naik and Kalish
- the plugin builder
- Snowflake's partner page (Compute)
- Fivetran
- Goel
- the job posting
- the developer portal

The note keeps three lines from Exhibit 4: "BlackRock gives no count", "No event specification is public" and the portal behind a client login.

Exhibit numbering changes:
- Exhibit 4 is removed, and Exhibits 5 to 17 become 4 to 16.
- In-text references were updated:
  - "Exhibit 5 counts them" became 4
  - "Exhibit 5's counts" became 4
  - "Exhibit 6 lists" became 5
  - "Exhibit 12 lists" became 11
  - "Exhibit 16 follows" became 15
  - "Exhibit 17 puts" became 16
  - C's own note, "controls are those in Exhibit 13" (formerly 14)
- The cover, summary and part dividers name no exhibit numbers, so nothing changed there. A CSS comment in the head that reads "Exhibit 23" was left alone.

### Exhibit 4 details that no longer appear in C (for the author to decide)

- "Aladdin Graph is the whole API layer, not one API"
- "Every public specification's id starts `agraph.<domain>`"
- Woodhead naming "APIs events" as one part (the quote)
- Goel's "every single transaction ... via an event, via an API" (the quote; Goel is still cited)
- Goel's "within 15 minutes" Data Cloud latency
- Compute as "a hosted analytics platform with ready-to-use Python environments" (now just "hosted Python environments")
- The SDK's run mode for "Aladdin Studio Compute sessions"
- SDK handling of pagination and long-running operations (only login, retries and rate limits remain)
- "Eleven add-on packages, one per API domain, are generated from the specifications by BlackRock's plugin builder" (the plugin builder is still cited in the note)
- The Developer Portal contents: "API catalog, framework guides, field dictionary, notebooks and code samples the APIs page describes"
- The job posting's name "Aladdin Studio Developer Portal"
- "The APIs page describes the catalog, guides, notebooks and samples but does not link them"

Some of these still appear elsewhere in the document: Goel’s quotes, including the 15-minute latency, are in Exhibits 5 and 6 (formerly 6 and 7), and the Compute run mode is in the Part 4 text on page 15.

## Page fit (rendered with render_chromium.js, checked with pdftotext and page images)

| | Pages | Exhibit 3 | Exhibit 4 | Part 2 / 3 / 4 start |
|---|---|---|---|---|
| Current v17 | 20 | p5 | p5 (six pieces) | 8 / 13 / 14 |
| A | 20 | p5 | p5 (six pieces), whole | 8 / 13 / 14 |
| B | 20 | p5 | p5 (six pieces), whole | 8 / 13 / 14 |
| C | 20 | p5 (combined) | p5–6 (domains table, formerly 5) | 8 / 13 / 14 |

- Nothing overflows.
- In A and B, page 5 is the only page with changed text. The other differences are citation digits after renumbering, which reflow a few lines in the register.
- In C, the domains table (now Exhibit 4) starts on page 5 and continues on page 6 with its header repeated. Part 1 still ends on page 7.
  - If the author would rather not split the table, adding `break-before:page` to it would put it whole on page 6. That should still end Part 1 on page 7, because pages 6 and 7 would then match the current layout, but I have not rendered it.
