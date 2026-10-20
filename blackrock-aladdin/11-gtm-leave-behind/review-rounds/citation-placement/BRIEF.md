# Citation placement check

Document: "Aladdin Studio from the outside" (final version: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.pdf and .html). Every claim was already fact-checked. Your question is narrower: is each superscript citation attached to the right words, and does each cited source actually support the words it sits on?

Your batch: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/citecheck/BATCH.json. Each unit has the text the superscript sits on ("supported_text": the words between the previous superscript, or the start of the sentence/cell, and this one), some surrounding context, and the full register entry for each cited source. Use the PDF/HTML to see the full sentence where the extract is unclear.

For each unit and each cited source, decide:
- SUPPORTS: the source says what the supported words claim.
- PARTLY: it supports part; say which words it does not cover.
- NOT SUPPORT: it does not back these words (it may back a nearby sentence; say which).
- CANNOT CHECK: the source cannot be reached; say what you tried.
Then a verdict for the superscript: RIGHT, MISSING (a claim in the supported words has no cited source that backs it; name the register entry that would), EXTRA (a cited source adds nothing to these words), MISPLACED (the superscript belongs on different words), or WRONG.

Evidence: prior fact-check receipts with quotes are in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/compiled_redo.json (field fin.<id>.receipt; search by text) and may answer most units fast. Otherwise open the source: the register URL (WebFetch or curl -A "Mozilla/5.0"; for sec.gov use -A "LinkCheck research-linkcheck@example.org"), or our local copies for recordings and specs (corpus map in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/CHECK.md). At most 6 WebSearch calls in total. Quote the words that show support or its absence.

Do not edit the document. Write /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/citecheck/out_BATCH.md (table: uid | page | supported words (short) | cites | per-source verdicts | superscript verdict | evidence quote | fix) and return every unit in the structured output.
