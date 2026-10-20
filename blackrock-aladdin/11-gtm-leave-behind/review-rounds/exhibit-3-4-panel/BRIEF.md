# Try to break Exhibits 3 and 4 (CHECK ONLY: do not edit anything)

Document: "Aladdin Studio from the outside", a leave-behind for BlackRock's head of go-to-market, built only from public sources. Page 4 holds two exhibits:
- Exhibit 3, "Where Studio sits in Aladdin": a layered picture (who builds; BlackRock's own ~100 applications with Copilot inside; Aladdin Studio as one band; shared services and data with the 11 public API domains; hosting; outside inputs) and a side column "Controls built into the APIs".
- Exhibit 4, "What Studio is made of": "What Studio offers" (six tiles: APIs (Aladdin Graph), event-driven workflows, Aladdin Data Cloud, Aladdin Compute, Aladdin SDK, Developer Portal and Data Dictionary; plus a line on Excel tools and the Data eXchange) and "Inside a client's Studio workspace" (Projects, Studio Compute, S3 storage integration, API tokens and API applications, Studio notifications, Studio UI, ADC Admin Center).

Files: page image /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/break34/page4-04.png (read it), page text page4.txt, the exhibits' build notes with source quotes BUILD_NOTES.md (same folder). Whole document: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.pdf/.html (Sources register at the end of the HTML).
Source material in the repo and scratchpad: /home/user/ai_game/blackrock-aladdin/ (04-transcripts/ with part1-youtube-and-site, part2-cloudfront-and-podcasts, product-pages, requested-recordings, timestamped; 02-api-catalog/ with apis.json and specs/; 01-research-briefings/; 10-compendium/), /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/readme.md (AladdinSDK README), scratchpad/unpacked/ (the 11 plugin packages' swagger.json files), scratchpad/crawl2/ (crawled BlackRock pages). Use grep -rn. You may fetch live pages (curl -A "Mozilla/5.0" or WebFetch); at most 3 WebSearch calls.

Your job, from your expert angle: try to BREAK the two exhibits. Look for:
1. A box, label or line that the sources contradict or do not support.
2. A STRUCTURAL claim the layout makes that the sources do not support: layer order, what sits above or below what, what is grouped inside Studio vs outside it, what the side column implies it covers, what the split in Exhibit 4 implies.
3. Something important that is missing, so the picture misleads by omission (e.g. a major part of Studio or of Aladdin that a BlackRock insider would expect to see).
4. Anything a BlackRock reader would find naive, wrong-named or embarrassing.
For every objection quote the evidence (file:line or URL plus exact words). An objection without evidence must be marked OPINION. Also say what holds up well. Be adversarial but fair: do not object to things that are clearly labelled as the author's own grouping or "For illustrative purposes only" unless the grouping itself is misleading.

Write /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/break34/panel_ROLE.md: objections ranked BREAKS IT / WEAKENS IT / NIT, each with evidence and the smallest fix; then "Holds up". Reply with your BREAKS IT and WEAKENS IT items only, one line each.
