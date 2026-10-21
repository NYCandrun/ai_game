# Audit: extra information that does not serve the overall point

## Purpose
"Aladdin Studio from the outside" (v23, 19 pages) has been sent to BlackRock's head of go-to-market. The author wants a clean, tight v24. Find the extra information in the document: clauses, sentences, table cells, exhibit labels and notes that are asides, side details or trivia. The key test is not "is this extra within its own sentence?" but "**does this serve the point of its paragraph, its section, and the document's overall argument?**" Something that looks like an aside in its sentence may be needed elsewhere, so keep it. Something that fits its sentence may still be off the point of the section, so flag it.

This is an audit only. Do NOT edit the document.

## The document's points (what everything should serve)
- **Overall argument.** Aladdin Studio could be where clients' own AI tools work on Aladdin under Aladdin's controls. The direction the author is moving to (v24) is: "Through Studio, clients' own AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions." The document backs this with what the public record shows, four findings, directions for go-to-market, and what the author could not see.
- **Part 1 (p3 to p6), what the public record shows:** what BlackRock sells, what Studio is, its APIs and controls, and how executives describe it.
- **Part 2 (p7 to p11), four findings:**
  1. Public proof of clients using Aladdin can serve as Studio's proof.
  2. BlackRock's investor story about APIs and platform growth, and how rarely it names Studio.
  3. Aladdin's AI works inside the login, while other providers let outside AI tools in.
  4. Buyers at BlackRock's own webinar are rethinking build versus buy.
- **Part 3 (p12 to p13), directions to explore**, including Exhibit 15's four pieces of marketing work.
- **Part 4 (p13 to p14), what I could not see:** what is public versus what opens only to clients.
- **Supporting matter (p15 to p19):** "About this document" and the source register. Judge "About this document" for asides. Do not audit the register entries themselves.

## Files
- **PDF:** /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_from_the_outside_v23.pdf. Use pdftotext -layout -f N -l N for page N, and pdftoppm -r 90 -png for exhibits.
- **HTML:** /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.html
- **Pending changes:** the author is already reviewing /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/review24/Proposed_v24_changes.html. If a sentence you flag is already changed there, say so ("already in fix N") and judge the proposed wording instead of the old one.

## What counts as extra
- Detail that the point of the paragraph, section or document does not need: background, history, colour, a second example where one is enough, a number that adds precision nobody uses, a name or date that does no work, a "by the way".
- Repetition of something already said elsewhere, where the repeat adds nothing. Say where else it appears.
- Method or sourcing detail in body text that belongs in the source list or "About this document".

## What does NOT count as extra (keep, and say why if it looks like an aside)
- Scoping and hedges that keep a claim honest: "not public", "my inference", "I found no…".
- Facts another part of the document relies on.
- The single fact that makes a comparison fair.
- The only place a cited source is used. If cutting it orphans a source in the register, say so.

## Output
Write your report to the path you are given. Use one table per page, with these columns:
| p | Exact text (quote the words to cut) | Point it is supposed to serve | Why it is extra (or why it only looks extra) | Verdict: CUT / TRIM / KEEP | Clean replacement (if TRIM) | Dependencies (source orphaned, used elsewhere, already in fix N) |

Write any replacement wording to the author's rules:
- Plain English.
- No em-dashes.
- No semicolons joining two sentences.
- Never use "suggested".
- State only the correct fact. Never mention the old wording.
- Say things explicitly.

Layout does not matter; the author will fix it later.

End your report with:
- **The 10 cuts that would most tighten your pages.**
- **Larger aside-heavy passages or exhibits.** List any whole paragraph, exhibit or exhibit element that is mostly off-point, with a recommendation.

Reply to me with:
- counts of CUT, TRIM and KEEP;
- your top 10, one line each;
- any larger passages.
