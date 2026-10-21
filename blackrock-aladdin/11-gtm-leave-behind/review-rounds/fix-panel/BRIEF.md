# Expert panel: audit the proposed fix list

## Background
"Aladdin Studio from the outside" is a 19-page leave-behind written from public sources by a job candidate for BlackRock's head of go-to-market. Version v23 has already been sent. An adversarial audit then produced a list of 61 proposed fixes plus 8 pieces of unused evidence. The author is deciding whether to make a corrected v24 and which fixes to make. Your panel audits the FIX LIST, not the report. You decide whether each proposed fix is right, needed, and correctly worded, and you make recommendations.

The author has also discussed evolving the central thesis rather than patching it:
- Old: "Clients' AI tools could act on Aladdin under the same controls BlackRock uses for its own business."
- Evolved: "Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls."

The reasoning behind the evolved thesis:
- Server-side controls could be literally the same if, for example, BlackRock offered an MCP server onto Copilot's plugin registry: tool permissions by environment, user group and app; API scopes; Aladdin user permissions; compliance on orders.
- Copilot's model-side controls could not be the same, because a client brings its own model: input and output guardrails, the planning loop, and AI-graded tests of BlackRock's prompts.
- The MCP route itself is the author's inference.

## Files (absolute paths)
- **Fix list (what you are auditing):** /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/final/Full_fix_list.html
- **Report as sent:** /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_from_the_outside_v23.pdf. Use pdftotext -layout -f N -l N for page N, and pdftoppm -r 90 -png to see an exhibit. The HTML is /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.html, with the source register at the end.
- **Audit reports behind the fixes:**
  - /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/out_A.md: controls and compliance
  - /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/out_B.md: Copilot and connectivity
  - /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/out_C.md: specs and workflow
  - /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/out_D.md: commercial evidence
  - /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/out_E.md: competitors
  - /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/concept/out_1_6.md, out_7_12.md and out_13_17.md: conceptual exhibit checks
  - /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ex4check/out_tiles.md and out_workspace.md: Exhibit 4
- **Primary sources, to check anything yourself:**
  - API specs: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/unpacked/
  - SDK clone: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/sdk_C
  - Transcripts: /home/user/ai_game/blackrock-aladdin/04-transcripts/
  - Saved pages: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/E_web/, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/A_web/, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/D/
  - Live web: at most 8 web searches.

## The author's writing rules for any wording you propose
- Plain English.
- No em-dashes.
- No semicolons joining two sentences.
- Never use the word "suggested".
- New text states only the correct fact. It never mentions, contrasts with or corrects the old wording.
- Every fact needs a source, though not every fact needs its own superscript.
- The report must stay at 19 pages. Part 1 starts on page 3, Part 2 on page 7, Part 3 on page 12 and Part 4 on page 13. Part 3's text and Exhibit 14 must share page 12.

## What to produce
Write your report to the output path you are given. Use these sections:
1. **Your stance in two or three sentences.** Stay in your assigned role.
2. **Verdict on each of the 61 fixes and on the evolved thesis.** For each, give ACCEPT, ACCEPT WITH CHANGE (give the exact replacement wording), REJECT or DEFER, with one line of reasoning. You may group fixes you treat the same way, but every number must appear.
3. **Fixes the list gets wrong.** Cases where the proposed wording introduces a new error, a new conceptual distortion, or breaks the writing rules.
4. **Anything missing** from the list.
5. **Your top 5 recommendations**, in priority order.

Do not edit the report or the fix list. Reply to me with your stance, counts (accept / change / reject / defer), the fixes you would reject or change and why (one line each), and your top 5.
