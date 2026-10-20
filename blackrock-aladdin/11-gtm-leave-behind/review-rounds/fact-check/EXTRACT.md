# Claim extraction brief (no checking yet)

You are enumerating every checkable factual claim on the pages assigned to you, from "Aladdin Studio from the outside", a 19-page analysis of BlackRock's Aladdin Studio. Another set of checkers will verify them; your job is only to list them completely and precisely.

Page text files: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/page_NN.txt (pdftotext layout; the small numbers after sentences are source numbers pointing at the Sources register in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/sources.tsv).

What counts as a claim: every number, count, date, year, name, job title, quotation, attribution (who said it, where, when, at what timestamp), product or application name, price or contract value, percentage, version number, "first"/"only"/"every"/"none"/"no public" statement, and every cell of every exhibit (table rows, diagram boxes, notes under exhibits). A sentence with three facts is three claims. If the document says "eight named products", the count AND the identity of the eight are separate claims. Author inferences explicitly marked as such ("my inference", "I have not found", "likely") are not claims, but the facts inside them are. Skip pure navigation text ("Part 3 sets out...") and the receipts key.

Output: write /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/claims/claims_pNN.tsv (one file per page you own) with tab-separated columns and no header:
id<TAB>page<TAB>location<TAB>claim<TAB>sources
- id: pNN-kk, e.g. p07-03 (page 7, third claim), numbered in reading order.
- location: "body para 2", "Exhibit 7 row Goel col 'Data'", "Exhibit 14 box 'LLM judges'", "exhibit note", etc.
- claim: the document's own words, quoted exactly, trimmed to the clause that carries the fact. Keep enough context to be checkable on its own (e.g. "Woodhead: 3,000 citizen developers" not "3,000").
- sources: the source numbers attached to it in the text, comma-separated, or "-" if none.
Be exhaustive: a dense exhibit page can have 40 or more claims. Reply with only the count of claims per page.
