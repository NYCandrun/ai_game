# Second pass: apply the accepted cuts and trims, keeping every citation honest

Start from scratchpad/v24/preview.html, which already has the v24 fixes from APPLY24.md. First copy it to scratchpad/v24/preview_after_fixes.html as a backup. Edit only preview.html.

## What to apply
The author accepted every CUT and TRIM recommendation in the three audit reports for extra information:
- scratchpad/asides/out_p1_6.md
- scratchpad/asides/out_p7_11.md
- scratchpad/asides/out_p12_15.md

That includes the "larger passages" and top-10 recommendations at the end of each report:
- merge Exhibits 6 and 7 into one exhibit and drop the Miller row
- cut the p8 private-markets paragraph entirely, since fix 7's new box is in
- drop poll 3 and its Exhibit 13 panel
- merge the p12 paragraphs
- trim the p14 SDK paragraph and the text under Exhibit 17
- trim About this document
- rewrite direction box 2 as a direction

KEEP rows stay as they are.

The reports were written against v23 and the v24 review wording, so some target text has changed since. For each recommendation, find where that text or its fact now sits in preview.html and apply the recommendation's intent there. If the target no longer exists because a v24 fix already replaced it, log it as "superseded" and move on.

## Exceptions (earlier author decisions that stand)
- **Exhibit 3's Hosting row stays**, with Microsoft Azure and Amazon Web Services and their sources.
- **Fix 50 stays.** Keep the "24 percent rise includes Preqin" sentence, with its added line on contract value growth excluding Preqin.
- **Exhibit 3 stays complete.** Do not cut or trim any element of Exhibit 3 for being off the argument: its boxes, its Studio parts, the outside-inputs row with its vendor-data examples, the Copilot box, the controls panel text, Explore, and the Hosting row with its sources. The only Exhibit 3 change from the audit is to drop the timestamps from its source line ("Rosales, for the apps and Copilot 9 ... Woodhead, for Studio 1"), because 2:35 is not in source 9's list.
- **Exhibit 4's workspace panel stays**, with the Spaces item (fix 61) and the Studio Compute note (fix 58). You may trim the wording of individual items. Exhibit 4's other tile trims from the audit DO apply. The accuracy fixes from the v24 review must still hold after trimming (for example, fix 20's Snowflake connection for Data Cloud).
- Elsewhere (Exhibit 5, p5, p14 SDK paragraph and the rest), the audit's cuts and trims apply as written.

## Specific reconciliations with the new Part 3 text
These come from APPLY24.md and are already in preview.html.

- **p2:** apply the audit's trims to the new text.
  - Drop SimCorp from the rivals sentence.
  - Drop the registry-rules sentence from the Copilot sentences.
  - Shorten the compliance sentences to "Posting an order runs a compliance check by default[6]."
  - The "Part 3 sets out this direction…" sentence becomes "Part 3 sets out this direction, what would have to be true for it to hold, and four pieces of marketing work that would follow."
- **p12, P1:** cut "It sells Aladdin as the system it runs internally[9]." If nothing else cites it, source 83 is already gone.
- **p12, P2 (rivals):** cut down to "SimCorp, Clearwater and Arcesium have announced AI agents or AI platforms" with superscripts 7, 8, 76 and the ABF Journal reprint entry (the reprint backs Arcesium's platform). Keep "What BlackRock can show is scale in production: Copilot runs across about 100 applications on about two thousand registered tools and agents[9]."
- **p12, P3 (service controls):** cut the time-limit and Compl Pending sentence. The permission sentence becomes "Whether an Aladdin permission restricts skipping the check is not public."
- **p12, P5 (inside Copilot):** cut "Its system prompts are tested daily by AI judges[9]."
- **p12, P6 and P7:** replace both with the audit's merged paragraph:
  > "At BlackRock's webinar, buyers named AI and data demands as the top reason to rethink what to build and what to buy[10]. The poll did not ask whether clients want AI tools that act on Aladdin. BlackRock sizes Aladdin's addressable market at more than $20 billion and projects API calls across BlackRock and Aladdin to grow 17x by 2030[11]. My inference is that clients' AI tools, acting through Studio, could become a large source of those calls. How many clients run their own AI tools is not public."
- **Exhibits 3, 4 and 14:** apply the audit's text-level cuts and trims to the exhibits in preview.html as well, subject to the exceptions above. A separate redraw of these exhibits is being made with the same cuts.

## The citation rule (the author's top concern)
For every edit, decide which facts survive and which go.
1. **A fact that is cut completely:** remove its superscript. If that source is then cited nowhere in the document, remove its register entry.
2. **A fact that survives in edited, shortened or merged wording:** its superscript must stay attached to that fact, placed right after the words its source supports.
   - When you merge sentences that had different superscripts, give each clause its own superscript.
   - When you cut words around a superscript, check the words left in front of it are still what that source says.
3. **No superscript may end up next to words its source does not support.** No fact that keeps its place in the text may lose its only citation, unless the same fact is cited in the same paragraph.
4. **Source lines under exhibits:** if every use of a source in that exhibit is cut, remove it from the source line. Keep each source line in step with the exhibit.

Write **scratchpad/v24/CITATION_LEDGER.md**, a table with one row per affected superscript:

| v23 source number and title | Action | Exact words it now sits on (or "fact cut") | Why |
|---|---|---|---|

Action is one of: removed (fact cut) / kept in place / moved / added.

Also list the register entries removed.

## Mechanics (the same as APPLY24.md)
- Renumber: `python3 -I scratchpad/gtm/renumber.py scratchpad/v24/preview.html`
- Sort: `python3 -I scratchpad/v24/sortreg.py scratchpad/v24/preview.html`
- Check: `python3 -I scratchpad/drift22/mech.py scratchpad/v24/preview.html` must show the first-citation order ok, no uncited entries and sequential IDs.
- **Exhibit renumbering after the 6+7 merge:** renumber every later exhibit and every cross-reference ("Exhibit 14", "as in Exhibit 14", and so on) everywhere, including notes, aria-labels and the cover.
- Render to scratchpad/v24/preview.pdf (see APPLY24.md). Layout is not a constraint, but update the cover's Part page numbers.
- **Writing rules for anything you write:**
  - Plain English.
  - No em-dashes.
  - No semicolons joining sentences.
  - Never "suggested".
  - State only the correct fact.
  - Say things explicitly.
- Write **scratchpad/v24/CUTS24_LOG.md**: one line per audit row, marked applied / superseded / exception, with the page.

## Reply
Report counts, the register entries removed, the exhibit renumbering, the page count, and anything that needs the author's judgment.

## Additional items (from the first pass's open questions)
1. **Exhibit 1:** apply the audit's Exhibit 1 trims and cuts as written. The author confirmed only Exhibit 3 is exempt.
2. **Fix 27:** the audit and the author's reader both cut "The proxies disclose the payments because BlackRock owns more than 5 percent of JPMorgan." Cut it.
3. **Exhibit 14 note:** the first pass wrote "The hatched box marks a use no public source shows: clients' AI tools calling the APIs." Make it explicit and true: "The hatched box marks a use no public source shows yet: a client's AI tool calling the APIs."
4. **Page 9, fix 33 and Woodhead:** the Woodhead sentence and the fix 33 conclusion pull against each other. Make the relationship explicit:
   > "Woodhead describes Studio as exposing "everything Aladdin knows how to do" as APIs and events[1]. The public specifications hold 301 operations. Whether Copilot's tools include the public APIs is not public. Copilot draws on about two thousand tools and agents, so many of its tools likely sit on APIs clients cannot call."
   Apply the audit's p9 trims around it only where they do not remove these four sentences.
5. **Finding 1 direction box:** align it with Exhibit 15 row 3: "A Studio case study that names the client can start with a client that builds with Studio."
6. **Exhibit 17 legend:** make it consistent: "Except in the AI connector column, 0 means not reachable without a client relationship." Keep the AI connector definitions as they are.
7. **Fix 40:** "BlackRock lists four platforms and nine solutions" must cite the Studio product page (source 14 in v23 numbering), whose site navigation lists them. It must not cite the Copilot page.
