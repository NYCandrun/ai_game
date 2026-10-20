# Readability review of drafted fact-check fixes

The document "Aladdin Studio from the outside" is a leave-behind for BlackRock's head of go-to-market. A fact check found wrong or partly wrong claims, and fixes were drafted. They have been applied to a PREVIEW copy only. Your job: check that the fixes do not make the text, the exhibits or the graphics more garbled, harder to read, or worse looking. Do not edit any file except your own report.

Files (all in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix):
- original.pdf: the current document (19 pages). preview.pdf: the same with every fix applied (22 pages). preview.html / current.html: their sources.
- FIX_PLAN.md and FIX_PLAN.json: each fix with current text, proposed text and why. DECIDE items were applied with the recommended option.
Page mapping: pages 1-7 line up. From page 8 the preview runs one page later (Exhibit 9 moved to its own page). Sources grew from 3 to 5 pages because 31 new entries were added.

## What to check, for every fix on your pages
1. Read the original and the preview sentence, cell, title or box side by side. Is the new version as clear as the old one, or clearer? Flag: longer or tangled sentences, hedges piling up, jargon, shorthand, allusion, citations cluttering a short line, lists that read as a run-on, a semicolon joining sentences, an em-dash, parentheticals, "suggested", or anything that mentions or contrasts with the old fact.
2. Render the changed pages to images (pdftoppm -r 80 -f N -l N -png) for both PDFs and look at them. For exhibits, tables and diagrams: check wrapping, crowding, overflowing boxes, text cut off, columns now uneven, a table or diagram split across pages, a title wrapping to three lines, superscript clutter.
3. Check that the meaning still serves the document's argument and that each exhibit still says one clear thing.

## Rules for any rewrite you propose
Plain English, one idea per sentence, about 20 words or fewer. No em-dashes, no semicolons between sentences, no "suggested", no reference to what the text used to say. It must stay as accurate as the drafted fix (same facts, same sources). Prefer cutting words to adding them.

## Report
Write /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix/read_PART.md with:
- A table: | fix id | where (page in preview) | verdict: CLEARER / SAME / WORSE / BROKEN LAYOUT | problem | proposed cleaner text (visible words) |. Include every fix on your pages.
- A short section "Layout": page-level problems found in the images, with page numbers.
Reply with the ids you marked WORSE or BROKEN LAYOUT, one line each.
