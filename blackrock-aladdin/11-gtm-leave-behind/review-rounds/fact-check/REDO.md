# Redo brief: claims first checked without web search

An earlier pass fact-checked these claims from "Aladdin Studio from the outside" (an independent analysis of BlackRock's Aladdin Studio), but the shared web-search allowance had run out, so the checkers could only fetch pages directly. Your job is a fresh, independent check of each claim WITH web search, to find receipts the earlier checker could not and to confirm or overturn its verdict.

Rules, sources register and corpus map: read /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/CHECK.md (the verdict list and receipt rule apply exactly).

## Search budget (hard rule)
Web search is shared by every agent in this run and is limited. Use AT MOST 2 WebSearch calls per claim and at most 10 in total. Prefer a targeted query (exact phrase, company + product + date). Use WebFetch / curl freely for pages you already have URLs for; those do not count.
If WebSearch returns an error saying the search budget or limit is used up, STOP searching, do not fall back to fetch-only verdicts, and set "searched": false for every claim you have not yet searched. Those claims will be re-run later.

## For each claim
- Search the open web for the strongest primary source, then a second independent source where one plausibly exists.
- Treat the earlier verdict and finding as a hypothesis to test, not a conclusion. Say whether you agree.
- Receipt: URL plus the exact quoted words. No quote, no CONFIRMED.
- For "wrong citation" findings, say which source in the register does support the sentence, or the URL that should be added.

## Output
Write a Markdown table to /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/reports/redo_RID.md with columns | id | claim | earlier verdict | new verdict | agrees | searches run | receipt (URL + exact quote) | finding / recommended fix |, then return every row in the structured output.
