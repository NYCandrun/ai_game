# Adversarial accuracy audit: common rules

The report "Aladdin Studio from the outside" (19 pages, v23) has already been sent to BlackRock's head of go-to-market. The author wants a rigorous, adversarial accuracy audit for their own confidence. Not encouragement, and not polishing. Do NOT edit the report.

The report:
- PDF: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_from_the_outside_v23.pdf (pdftotext -layout -f N -l N for page N; pdftoppm -r 90 -png to see a drawing)
- HTML source: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.html. Superscripts are <sup class="fnref">; the numbered source register is at the end.

## Evidence rules (strict)
- Go back to ORIGINAL sources: the API specifications, the SDK code, the transcripts or recordings, the filings and the live web pages. Re-derive any calculation yourself.
- Do NOT use earlier project summaries, receipts, fact-check reports, panel reviews or notes as evidence (anything under /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/citecheck, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/break34, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ex4check, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/drift22/out_*, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/redraw34/NOTES.md, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/compendium, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/v20check, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/uncited, or /home/user/ai_game/blackrock-aladdin/11-gtm-leave-behind/review-rounds). Don't assume the report's conclusions are correct.
- Primary artifacts you may use:
  - Specs: the 11 PyPI wheels in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/pkgs/ (asdk_plugin_*-2.0.0b3), already unpacked in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/unpacked/. To confirm they are the real cited versions, re-download at least two from PyPI (pip download asdk_plugin_trading==2.0.0b3 --no-deps -d <new dir under /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/>) and compare hashes.
  - SDK: clone fresh with git clone https://github.com/blackrock/aladdinsdk into a new dir under /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/ (also https://github.com/blackrock/aladdinsdk-plugin-builder). The GitHub API is blocked; git and raw.githubusercontent.com work.
  - Transcripts: /home/user/ai_game/blackrock-aladdin/04-transcripts/. Most are the project's own machine transcriptions or published captions of public recordings. Treat them as copies of the recording, and say so when a claim rests on a machine transcript. Where the recording is on YouTube, you may check the URL/timestamp exists (oEmbed) but you probably can't play audio.
  - Web: curl or WebFetch the live page. For sec.gov use curl -A "LinkCheck research-linkcheck@example.org". Saved page copies from earlier today exist in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/drift22/dl_a/ and dl_b/; you may use them, but say when you did.
- If you cannot access a source, say so plainly. Never present something as verified that you did not verify yourself in this task.
- Cap: at most 20 web searches per agent.

## Output
Write your report in markdown to the output path you are given. Be candid and specific. For every point, give: the exact claim and the page number, what the original source says (an exact quote, or a file and line or JSON path), what it actually establishes, what the report inferred beyond it, and a verdict: CORRECT / DEFENSIBLE BUT UNCERTAIN / OVERSTATED / UNSUPPORTED / WRONG. Also give the strongest wording the evidence would justify. Separate genuine factual mistakes from reasonable hypotheses based on incomplete public information.

End your report with a section "Top vulnerable statements": up to 5 statements from your area that are most open to factual or technical challenge, each with all the fields above.

Reply to me with a short summary of your main findings, plus your top vulnerable statements in one line each.
