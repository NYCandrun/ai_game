# Short-text readability pass: what was applied

Live file: `gtm/out/Aladdin_Studio_With_AI.html` (backup untouched at `gtm/out/Aladdin_Studio_With_AI.before_titles.html`). Script: `gtm/titleswork/apply.py` (137 content replacements + 5 layout trims, each asserted to occur exactly once; idempotent on re-run). Rules followed: checker verdict OK → reviewer's rewrite; CHANGES MEANING → checker's suggested fix; DO NOT APPLY → unchanged; plus the decisions in the brief.

Status key: **applied** (reviewer's rewrite as written) · **applied, checker fix** · **applied, decided wording** (brief's decision) · **applied, trimmed** (shortened for layout, meaning kept) · **skipped**.

## Cover and decisions

| Item | Status | Note |
|---|---|---|
| Cover subtitle | applied, decided wording | "What public sources show about Studio and the likely initial directions for marketing it". No other place repeated the old subtitle wording (the cover Part 2 line's "where BlackRock is heading" went with A2). |
| A1 (vs D1) | applied, decided wording | "What the research suggests for this role’s first six months" on the cover and as the Part 3 title (both occurrences). |
| IMPLIED 1 | applied | Page 2 lead-in → "Six likely initial directions:" (supersedes A6). |
| IMPLIED 2 | applied | Part 3 intro three-test sentences → "Each direction uses only what is already public, or already true inside BlackRock." (combined with D2). |
| IMPLIED 3 | applied | Finding 3 callout → "Exhibit 15 is the evidence. This is the Copilot direction in Part 3." (combined with C15's semicolon split). |
| IMPLIED 4 | applied | Exhibit 17 row 5 cell: "that opens no new access" dropped per its minimal edit (combined with D15). The borderline "I would hold any outside connector for now" softening was NOT applied. |

## A_cover_part1.md (pages 1 to 9)

| Item | Status | Note |
|---|---|---|
| A2 | applied | Cover Part 2 line. There is no separate Part 2 h2 on page 10 (findings start at "1."), so nothing else to align. |
| A3 | applied, trimmed | Reviewer's caption made the stat-tile row four lines and pushed the receipts key to a stub page. Final: "JPMorgan Chase’s 2025 payments for Aladdin, per its proxy statement, almost 6x its 2017 payments" (three lines; both "its" now refer to JPMorgan, which was the reviewer's point). |
| A4 | applied | |
| A5 | applied | |
| A6 | skipped | Superseded by IMPLIED 1. |
| A7 | applied, checker fix, trimmed | Checker's wording made list item 5 three lines and (with A3) overflowed page 2. Final: "Describe the Copilot plugin model publicly: API mapping, governance, how client AI tools plug in." Keeps the document's "plugin model" term (the checker's concern) and gives the third item, the unclear one, a clause. |
| A8 | applied | Keeps "public API catalog" per decision. |
| A9 | applied | |
| A10 | skipped | Reviewer and checker: keep "receipts" / "Receipt". |
| A11 | applied | "Of Aladdin’s eight named products, Studio is the one for people who write code". |
| A12 | applied, checker fix | Addition attached to Preqin, not eFront Insight. |
| A13, A14 | applied | |
| A15 | applied | Title as proposed; source note gains "name no order screen and" as the item says. |
| A16 | applied | "Product or application BlackRock names". |
| A17 | applied, verb fix only | No "None named." sentence. |
| A18, A19 | applied | |
| A20 | applied | Stability sentence moved verbatim from Exhibit 2's note to Exhibit 5's note (with A28). Not duplicated in Exhibit 2. |
| A20b | skipped | Target absent: the step 5 cell no longer carries EnrichedCapitalFlowAPI (an earlier Exhibit 2 trim). |
| A21 | applied | Title "Apps, Copilot and Studio all call one shared API layer". The dropped idea went into the existing note sentence: "The 11 domains behind the shared layer are the packages of BlackRock’s public SDK ..." (no new sentence, so page 5 layout is untouched). |
| A22, A23, A24, A25 | skipped | Exhibit 3 SVG labels untouched (script asserts the SVG is byte-identical). |
| A26 | applied | Title "Six pieces make up Studio"; both dropped ideas added to the source note with superscripts 17 and 24. The optional intro line before Exhibit 4 was not added (no new sentence on the full map page). |
| A-note (three parts vs six pieces) | skipped | A new reconciling claim; not in the current document. |
| A27 | applied | Title "Two domains hold 127 of the 301 public API operations"; the body paragraph after the exhibit now opens "Only 23 of the 54 specifications are stable, and the specifications say more than their count." |
| A28 | applied | Exhibit 5 note ends with the stability-label sentence plus "; the four columns count specs by label." |
| A29 | applied | |
| A30 | applied | Header "Public today" and h3 "What is public before a conversation starts" so the two match. |
| A31 | applied | |
| A32 | applied | |
| A33 | applied | "First API call without a contract" (still three header lines, same as before). |
| A34 | skipped | "Call to action" kept; nothing added, per decision. |
| A35 | applied | |
| A36 | applied | Headers "Title, as the recording gives it" / "What they add to the definition" / "Recording"; the note's "Where column" changed to "Recording column" to match. |
| A37 | applied, checker fix | "quoted at the start of Part 1"; no definition of citizen developers added. |
| A38 | applied | |
| A39 | applied, checker fix | Exhibit 8 cell "Never Done podcast, January 2025"; Exhibit 6 Hear row "the Never Done podcast^30, the Big Little Questions video series^31, Woodhead^5, Rosales and Valdez^9" (existing superscripts and links kept). |
| A40 | applied | Title as proposed; "Only Goel and Woodhead name developer tools." added to the note. |
| A41 | applied | Note now starts the key with "Yes means the speaker names that part; – means not." |

## B_findings12.md (pages 10 to 12)

| Item | Status | Note |
|---|---|---|
| B1 | applied | |
| B2 | applied | |
| B3 | applied | SVG legend text "Payment for integration services (2016 only)" (the Exhibit 10 chart SVG, not the Exhibit 3 map). |
| B4 | applied | First sentence as proposed; the optional third-sentence tightening ("JPMorgan is also a custodian, so the payments may cover more than a client license.") also applied; link kept. |
| B5 | skipped | No change proposed. |
| B6 | applied, decided wording | "Exhibit 11. Aladdin won every bid that three public pension bodies scored, 2017 to 2025". No note line added. |
| B7 | applied, checker fix | "Weights or process". |
| B8 | applied, checker fix | "Weights: technical 85, ..." and "Weights: quality 70, ..."; no "%"; no sum sentence. |
| B9 | applied, checker fix | "Run as a full and open competition; four bids were received each time"; no "(the standard US federal process)". |
| B10, B11 | applied | |
| B12 | applied, checker fix (sentence 1) + reviewer (sentence 3) | "Aladdin adoption is growing among clients whose records are public." / "A named Studio story can start with clients whose Aladdin use is already on the record." |
| B13 | applied | Headline as proposed; new first body sentence "BlackRock tells investors growth will come from two things: API calls, and the whole portfolio, public and private markets together." followed by "It projected at its 2025 Investor Day ..." |
| B14 | applied | Title as proposed; the "about four mentions" total moved into the source note after "My tally." |
| B15 | applied | "Where it came up". |
| B16 | applied, checker fix | "where it was described as ..." |
| B17 | skipped | No change proposed. |
| B18 | applied, sentence 1 only | Sentence 1 → "API calls and from the whole portfolio" (checker: OK). Sentences 3 and 4 taken from C1 per decision. |

## C_findings34.md (pages 12 to 15)

| Item | Status | Note |
|---|---|---|
| C1 | applied, decided (over B18) | "... arrives through Data Cloud and Explore. Both are Studio surfaces. So Studio carries the growth story, whether or not BlackRock says its name." |
| C2 | applied | |
| C3 | applied | |
| C4, C5, C6, C7 | applied | |
| C8 | applied, checker fix | "Of nine providers a Studio buyer compares, only Aladdin has not shipped or announced AI access to its data"; the job advert moved into the note as "Aladdin has only a job advert that mentions MCP^65." (the current title's own words). |
| C9 | skipped | No change proposed. |
| C10 | applied (SimCorp, LSEG: checker fix; Arcesium, FactSet: trimmed; others as proposed; Aladdin unchanged) | Arcesium: "Arcesium added AI features to Aquata and announced an AI platform"; FactSet: "FactSet runs an MCP server for its data and calls it the first in its market" (each kept to one line so page 13 holds the Finding 3 callout again). |
| C11 | applied | |
| C12 | applied | Descriptive title. The conclusion it carried is already stated in the callout ("It also lets BlackRock, not FactSet and LSEG, set the terms of comparison"; "The inside model already answers three governance questions ..."), so no extra sentence was added there. |
| C13 | applied, checker fix | "production" kept in the inside header. |
| C14 | applied (For/Inside trimmed; Against/Outside checker fix) | "It carries enterprise trust." instead of "It carries the platform’s enterprise trust." to keep the row at four lines. Against/Outside: "would look awkward to a regulator". |
| C15 | applied, checker fix for the fold | Callout opens "I would describe the Copilot plugin model publicly now: production Aladdin APIs, the same ones Studio exposes, each user’s own permissions, and tested no-advice guardrails^9, 16." then "That description, in BlackRock’s own words, answers ... better than an MCP server with a partial catalog would." Closing per IMPLIED 3. "I would hold any outside connector for now" unchanged. |
| C16, C17 (checker fix), C18, C19, C21 | applied | C17: "would stop maintaining compliance reporting in house first". |
| C20, C22 | skipped | No change proposed. |
| C23 | applied | |

## D_part3_sources.md (pages 15 to 20)

| Item | Status | Note |
|---|---|---|
| D1 | skipped | A1 chosen per decision. |
| D2 | applied | With IMPLIED 2. |
| D3 | applied | "Six likely initial directions, with an owner and a measure for each". |
| D4 | applied | "Rests on". |
| D5 | applied | "Measure of success". |
| D6 | applied | |
| D7 | applied, with Nest^52 and PBGC^53 added (checker: adopt) | Each superscript now sits beside the client it supports. |
| D8 | applied, checker fix | "Studio’s name beside one measure of API use". |
| D9, D10, D11, D12 | applied | |
| D13 | applied | Row 5 noun form "A public description of the Copilot plugin model"; imperative alternative not used. |
| D14 | applied, checker fix | "... buyers now ask^8: what is your API suite? It lists each API domain with its specification count, operation count and status, ..." |
| D15 | applied | With IMPLIED 4. |
| D16 | applied | |
| D17 | applied, checker fix / decided | "A prospect-facing summary of the public API catalog". |
| D18 | applied, checker fix | "with the specification and operation counts and status of each". |
| D19, D20, D21 | applied | |
| D22, D23, D25 | applied, checker fix | Two-sentence forms for rows 3 and 4. |
| D24 | applied, decided | "What the public API catalog summary may say". |
| D26, D27 | applied | |
| D28, D29 | applied | |
| D30 | applied, checker fix | "speech-to-text software run locally on the downloaded audio". |
| D31 | skipped | No change. |
| D32 | applied | "page as captured October 2026" (4) and "seen October 2026" (2) → "as of October 2026"; "run" and "unpacked" kept; precise dates kept. |
| D33, D34, D35 | applied | |
| D36 | applied, speakers sentence only | "Replay page undated." as its own sentence; no speaker attributions added. |
| D37, D38, D39, D40, D41 | applied | |

## Counts

- Applied as written: 79
- Applied with checker fix or decided wording: 36 (A1, A3*, A7*, A12, A17, A37, A39, B6, B7, B8, B9, B12, B16, C1, C8, C10 SimCorp, C10 LSEG, C13, C14 Against/Outside, C15, C17, D8, D14, D17, D18, D22, D23, D24, D25, D30, cover subtitle, IMPLIED 1 to 4; * also trimmed)
- Trimmed for layout (meaning kept): 5 (A3, A7, C10 Arcesium, C10 FactSet, C14 For/Inside)
- Skipped: 16 (A6, A10, A20b, A22, A23, A24, A25, A34, A-note, B5, B17, C9, C20, C22, D1, D31 — D1 and A6 superseded; the rest "no change", map labels, or absent target)

## Layout

First render after the content pass came to 22 pages: page 2 grew two lines (A3, A7) and pushed the receipts key onto a stub page; page 13 grew about two lines (C10 cells, C14 For row) and pushed the Finding 3 callout, which in turn made Chromium start Exhibit 17 on a fresh page and Exhibit 18 on another. The five trims above restored the backup's pagination exactly: 20 pages, receipts key on page 2, Exhibit 2 whole on page 4, Exhibit 8 split at the Khara row between pages 8 and 9 exactly as in the backup (the backup render also splits it there, via the pre-existing `break-before:auto` row; it cannot fit on page 8 with Exhibit 7), Finding 3 callout on page 13, Part 3 on pages 15 to 16, Sources on 18 to 20. No exhibit or finding title wraps to three lines; the two-line Part 3 title is the only heading that gained a line.

## Checks

- Every `<a href="#sN">` has a matching `id="sN"` and every Sources id is referenced (72 / 72).
- Exhibit 3 SVG byte-identical; all style attributes, colgroups, external URLs and Sources titles identical to the backup; the only attribute differences are 8 added `class="fnref"` superscripts and the five added internal links (#s17, #s24, #s52, #s53, #s65).
- Zero hits for "in the order I would take them", "none changes how Aladdin is sold", "opens no new access", "fifth direction", "three tests" (also zero for "what is in the box", "Why (finding)", "front door", "Out there today").

## Layout change after the pass (by the session lead)

Exhibit 7 was `exhibit keep` (never split) and did not fit below Exhibit 6, leaving half of page 7 blank and pushing Exhibit 8 into a split across pages 8 and 9. Change: Exhibit 7 may now split, and only at its group boundary (`break-before:page` on the "Data and cloud platforms" group row, header row repeats). Result: Exhibit 7's investment platforms close page 7, its data and cloud platforms open page 8, Exhibit 8 sits whole on page 8, and the remaining white space falls at the end of Part 1 on page 9, before the Part 2 page break. Still 20 pages. No text changed.

## After the before/after meaning check (MEANING_CHECK_titles_applied.md: 142 pairs, 116 same, 23 moved, 3 changed)

Three fixes applied by `fix3.py`: Exhibit 14 title now "Of nine providers a Studio buyer compares, eight have announced AI features or AI access to their data; Aladdin has a job advert" (the applied title had claimed all eight shipped or announced data access, which the SimCorp and Arcesium rows do not say); Exhibit 8 title drops "since 2024" (Miller's video is undated); Exhibit 2's source note regains a pointer to the stability labels ("The labels in brackets are each specification's stability label; Exhibit 5 explains them").
