# Review rounds for the leave-behind

- `panel/`: six reviewers of the reframed edition (American English, clarity, AI tells in the copy, quality of the findings, a devil's advocate for leaving it unchanged, a consulting-trained MBA), with the brief they followed and the bundle `PANEL_ALL.md`. The agreed items were applied in one pass.
- `readability/`: six identifiers, one per page range, who listed every passage a reader would have to read twice, with plain rewrites (`READABILITY_ALL.md`); `MEANING_CHECK_proposed.md` checked those rewrites for changes in meaning before they were applied (45 of 181 flagged, each with a fix); `MEANING_CHECK_applied.md` compared the document before and after the edit (96 passages, 5 meaning shifts and 5 additions, all corrected).
- Every edit pass is a replayable script under `../../tools/` that asserts each replaced string occurs exactly once.
