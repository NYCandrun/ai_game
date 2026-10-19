# Timeline of the work (October 19, 2026, times in UTC)

Each row is one round of research, review or production. The commit for each round carries the time the work finished, so `git log` reads as the same series.

| Time | Round | What was produced | Where |
|---|---|---|---|
| 03:27 | API packages pulled | The 11 public `asdk_plugin_*` packages unpacked; 54 Swagger specs and the AladdinSDK README | `02-api-catalog/specs/`, `02-api-catalog/aladdinsdk_README.md` |
| 03:30 | Research briefing 1 | What Aladdin Studio is and how it is architected | `01-research-briefings/aladdin_studio_briefing.md` |
| 03:38 | API digest | Every API, operation and schema condensed into one file | `02-api-catalog/api_digest.txt` |
| 03:41 | Research briefing 2 | The whole Aladdin suite, broken down by the 11 API domains | `01-research-briefings/aladdin_suite_architecture.md` |
| 04:07 | Interactive guide, version 1 | First draft of the HTML field guide, published as an artifact | `03-interactive-field-guide/versions/v1_*.html` |
| 04:11 to 04:17 | Expert panel review | Four reviews: outsider readability, UI/UX interaction, visual design, copy and explanation; screenshots before and after | `08-review-rounds/2026-10-19_0411_expert-panel-review-of-field-guide/` |
| 04:19 | API summary | `apis.json` with domain, stability label and operation counts | `02-api-catalog/apis.json` |
| 04:31 to 05:47 | Interactive guide, version 2 | Review findings applied; verified at 1280 and 390 px, light and dark | `03-interactive-field-guide/versions/v2_*.html` |
| 05:40 to 05:47 | Transcripts, part 1 | The requested YouTube videos and BlackRock site videos; product-page text captured | `04-transcripts/part1-youtube-and-site/`, `04-transcripts/product-pages/` |
| 06:01 to 06:50 | Media crawl | BlackRock media CDN, podcast feeds and site crawled for every video and audio file; blocked YouTube audio fetched through a proxy | `08-review-rounds/2026-10-19_0601_media-crawl-and-audio-fetch/` |
| 06:11 to 07:33 | Transcripts, part 2 | 95 items from the crawl, transcribed from published captions or audio | `04-transcripts/part2-cloudfront-and-podcasts/` |
| 13:41 to 13:46 | Field guide fact-check | Five reviewers checked every claim on the page against the transcripts | `08-review-rounds/2026-10-19_1341_field-guide-fact-check/` |
| 13:48 | Interactive guide, version 3 | 31 corrections applied; transcript indexes re-assembled | `03-interactive-field-guide/aladdin_field_guide.html`, `04-transcripts/*_index.md` |
| 14:03 to 14:13 | Document fact-check | Five reviewers checked the Briefing (sections 1 to 17) and What It Does V7 against the sources | `08-review-rounds/2026-10-19_1403_document-fact-check/` |
| 14:15 | Consolidated fact-check report | Findings merged into one report with confirmed, corrected and unverifiable items | `05-fact-check/FACT_CHECK_briefing_and_what_it_does.md` |
| 14:25 to 14:47 | Document corrections | Briefing (revised) and What It Does V8 rewritten with every finding applied; change logs | `06-revised-documents/`, `08-review-rounds/2026-10-19_1425_document-corrections/` |
| 14:47 to 15:37 | Branded HTML editions | V8 rebuilt in the Key Findings design; the Briefing edited in place in its original HTML; Chromium PDFs; page numbers fixed | `06-revised-documents/*/*.html`, `08-review-rounds/2026-10-19_1447_branded-html-editions/` |
| 15:43 | Final PDFs | PDF editions of the fact-check, the briefings, the field guide and the transcript indexes | see `README.md` |
| 15:52 to 16:15 | Related AI concept videos | Four IBM Technology videos transcribed into one Markdown | `09-related-ai-concepts/` |
| 16:15 | Index | README, folder READMEs and this timeline | `README.md`, `00-timeline.md` |
| 16:20 to 16:55 | Compendium | Three writers drafted Aladdin, Studio and BlackRock parts from the pulls; assembled into one PDF and HTML | `10-compendium/` |
| 19:20 | Compendium review | Nine reviewers checked the compendium against the nine requested recordings; agreed corrections applied; two new transcripts added | `10-compendium/review-rounds/`, `04-transcripts/requested-recordings/` |
| 19:25 to 19:54 | GTM leave-behind | Built from the Key Findings design and the corrected corpus; layout tightened to 18 pages; 60-claim receipts check (0 wrong) | `11-gtm-leave-behind/` |
| 20:00 to 20:29 | Leave-behind, second build | Trade-lifecycle exhibit, Copilot funnel and timestamp receipts added; 13 recordings re-transcribed with cue times | `11-gtm-leave-behind/`, `04-transcripts/timestamped/` |
