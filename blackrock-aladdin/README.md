# BlackRock Aladdin and Aladdin Studio: research pack

Interview preparation research on BlackRock's Aladdin platform and Aladdin Studio, built from BlackRock's public API specifications, product pages, press releases, job postings and about 230 transcripts of BlackRock talks, podcasts, webinars and client videos. Independent work. Not produced, reviewed or endorsed by BlackRock.

## Start here

| Folder | What is in it | Open first |
|---|---|---|
| `01-research-briefings/` | Two written briefings: what Aladdin Studio is, and how the whole Aladdin suite is architected and broken down by domain | `aladdin_suite_architecture.pdf` |
| `02-api-catalog/` | The 54 public Aladdin Graph API specifications (Swagger 2.0) from the 11 `asdk_plugin_*` packages, a one-file digest of every API and operation, and the AladdinSDK README | `api_digest.txt` |
| `03-interactive-field-guide/` | The interactive HTML explainer (11 lessons, diagrams, domain explorer, glossary), a print PDF with every lesson expanded, and the claims list used to fact-check it | `aladdin_field_guide.html` |
| `04-transcripts/` | Full transcripts: part 1 (YouTube and BlackRock site videos), part 2 (CloudFront captions, Never Done and Client Stories podcasts, webinars), plus product-page text and the transcription tools | `transcripts_index.pdf`, `transcripts2_index.pdf` |
| `05-fact-check/` | The fact-check of the two draft documents against the sources, and the original drafts for comparison | `FACT_CHECK_briefing_and_what_it_does.pdf` |
| `06-revised-documents/` | The corrected documents: Briefing and Interview Guide (revised) and What It Does (V8), each as Markdown, DOCX, a plain PDF and the BlackRock-styled HTML edition with its PDF | the `.pdf` without `_plain` in each subfolder |
| `07-design-references/` | The three HTML design samples the branded editions follow: the BlackRock web brand guide, the Key Findings sample and the original October 8 Briefing HTML | `blackrock-web-brand-guide.html` |
| `08-review-rounds/` | Every review and production round in time order: the expert panel, the media crawl, both fact-checks, the corrections and the HTML builds, with the reviewers' reports and screenshots | `README.md` inside, then the 0411 folder |
| `09-related-ai-concepts/` | Transcripts of four IBM Technology explainers (agents, agentic harness, RAG vs fine-tuning, MCP vs API) in one Markdown, for the AI part of the interview | `ibm_ai_concepts_transcripts.md` |
| `10-compendium/` | One matter-of-fact document (revised after nine recording-by-recording reviews, see `review-rounds/`) laying out everything the pulls show about Aladdin, Aladdin Studio and BlackRock, in that order, with a source tag on every fact | `Aladdin_Studio_BlackRock_Compendium.pdf` |
| `11-gtm-leave-behind/` | The leave-behind for the head of GTM, framed as what an outsider can learn with AI: the product, and four findings about BlackRock's direction, with a graded and timestamped source register | `Aladdin_Studio_With_AI.pdf` |
| `tools/` | Rendering and editing scripts: Chromium and WeasyPrint renderers, the V8 HTML builder, the Briefing HTML edit chain and page-number fixer | `render_chromium.js` |

## Final deliverables (PDF)

- `11-gtm-leave-behind/Aladdin_Studio_With_AI.pdf` (18 pages, the GTM leave-behind)

- `10-compendium/Aladdin_Studio_BlackRock_Compendium.pdf` (35 pages, the single reference document)

- `06-revised-documents/briefing-and-interview-guide/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.pdf` (81 pages, branded edition)
- `06-revised-documents/what-it-does-v8/Aladdin_Studio_What_It_Does_V8.pdf` (34 pages, branded edition)
- `05-fact-check/FACT_CHECK_briefing_and_what_it_does.pdf`
- `03-interactive-field-guide/aladdin_field_guide_print.pdf` (the live version is the interactive HTML; published copy at https://claude.ai/artifact/SmPi1sZLYJ54QFn7Cwofca)
- `01-research-briefings/aladdin_suite_architecture.pdf` and `aladdin_studio_briefing.pdf`

## How the work was sequenced

`00-timeline.md` lists every round with its time. The commits on this branch are dated to when each round finished, so `git log --date=iso` reads as the same series, and the three versions of the interactive guide can be diffed commit to commit.

## Rendering

The branded HTML editions are print-styled pages (Letter, Barlow fonts embedded). Render with `node tools/render_chromium.js in.html out.pdf` (Playwright Chromium, which the originals were produced with). `tools/render.py` is a WeasyPrint alternative; footnote spacing in the Briefing is tuned for Chromium.
