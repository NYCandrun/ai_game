# Slim Exhibits 1 and 2: preview notes

The real file was not touched. `gtm/out/Aladdin_Studio_With_AI.html` and `.pdf` still match v19 (same md5).
All edits are in `slim12/preview.html`. They are made by `edit.py`, which starts each run from the real HTML, then `finalize.py` (renumber.py, a flat numeric sort of the register, and numbers sorted inside each superscript). `build.sh` runs both and renders.

## Result
- Exhibit 1 and Exhibit 2 now share page 3, under the Part 1 opening text. Each takes about 196pt, roughly 29% of the text area. In v19, Exhibit 1 took most of page 3 and Exhibit 2 filled page 4.
- The document goes from 20 pages to 19. Text on preview pages 4 to 19 matches v19 pages 5 to 20 line for line (checked with pdftotext against a fresh render of the v19 HTML).
- Citation order did not change: renumber.py renumbered 0 entries, 103 cited, 103 in the register, no orphans.

## Exhibit 1: what was cut
- The "Main users" column is gone. Only Studio keeps its users, in plain words: "For engineers, data analysts and code-curious portfolio managers" (s14).
- Every quotation is gone and each row is one line. Studio is the exception: it runs to two lines because it carries its users. Studio is still the highlighted row (bold, with a pale yellow tint added).
- Text dropped from the cells:
  - Aladdin Wealth: "auto commentary" and "Morgan Stanley as the first client". The row now reads "AI commentary tool since October 2025" (s17).
  - eFront: "due diligence through cash flows and reporting" and "eFront Insight". The row now reads "private-fund platform holding Preqin" (s18).
  - Studio: the "API-first" quotation and the three long user descriptions.
  - Data Cloud: "puts Aladdin and outside data in one place", plus Newman's name and title. "Part of Studio" stays, with its link and s22.
  - Copilot: the quotation marks only. The facts stay ("available to all Aladdin clients", "gives no investment advice").
  - Accounting: "configuration" was dropped from the list of API areas. It now reads valuations, lots and composites (s6).
  - Provider: unchanged in substance ("they pay BlackRock for it", s25).
- Every citation from v19 (1, 6, 9, 14 to 25) is still on the short line it supports, so none had to move. The source note did not change.

## Exhibit 2: what was cut
- The 6x4 table became a left-to-right flow of six yellow chevrons (Order, Compliance check, Trade, Position in the IBOR, Lot in the ABOR, NAV). It is a CSS grid with four rows, labelled Who / Where / API / Detail. Body text is Barlow 8pt and API names are IBM Plex Mono 8pt. Nothing is smaller than 8pt.
- All quotations were dropped: the Order spec definition, the Explore "new what-if model", the ComplianceRule and Violation spec quotes, the BrokerConfirmRouting quote, Schneid's "without lifting up the pencil", Newman's "It does start with IBOR", Fivetran's IBOR/ABOR quote, Shannon's "data managers", the AborLot and Valuations spec quotes, and Schneid's "CFOs, controllers".
- Facts dropped with them: the example order statuses, the timeout that posts "Compl Pending", the violation record fields, the block trade fields `confirmedWith` and `confirmedBy`, and the named fields that hold positions (PortfolioToolkitAPI, CollateralStatementAPI, a violation's underlying positions). Those fields are now summed up as "Positions appear only as fields in other APIs". The people's names and titles (Schneid, Shannon, Newman) were also dropped from the cells.
- One detail kept per step:
  - Order: posting takes whatIf and runCompliance.
  - Compliance: runs automatically because runCompliance is on by default.
  - Trade: broker confirms via BrokerConfirmRoutingAPI. I did not use "confirmed with the broker via BrokerConfirmRoutingAPI": v19 only says that API "holds each broker's instructions for delivering confirms", so "via" is as far as I would go. Reword if you prefer.
  - Position: the dashed box reads "None of the 54 is a position API".
  - Lot: retrieved from the ledger_a_summary table.
  - NAV: each valuation carries an exception list.
- The Trade step has no application name, because v19 names none for it. Its Where cell shows an en dash.
- The key finding is now the bold first line of the note. The stability-label sentence and the source note are kept. I changed the semicolon before "Exhibit 5 counts them" to a full stop. The source note shortens "the Aladdin Accounting episode with David Schneid and Daniel Shannon" to "the Aladdin Accounting episode", because their names no longer appear in the cells.
- Citations: v19 cited 6, 22, 26, 27 and 28 here. All five are still in the flow and all five are in the source note. 22 (Newman) is now on "Investment team". 26 (Schneid/Shannon) is on "Accounting team" and "Accounting". 27 is on Explore and 28 on Data Cloud. Nothing had to move to the note.

## Page numbers
| Part | v19 | preview |
|---|---|---|
| Part 1 | 3 (ends on 7) | 3 (ends on 6) |
| Part 2 | 8 | 7 |
| Part 3 | 13 | 12 |
| Part 4 | 14 | 13 |

The cover part cards were updated to Pages 3, 7, 12 and 13. The rule for page 13 still holds on its new page 12: the Part 3 text and Exhibit 14 are together on that page, unchanged from v19 page 13.

## Things to know / not kept
- Page 3 is now full. The Exhibit 2 note ends about 4pt above the bottom margin. Any longer wording in either exhibit will push Exhibit 2, which is set to keep together, onto page 4, and Part 1 would then end on page 7 again.
- I hit a rendering trap while building the chevrons. A negative margin made the grid slightly wider than the page, and Chromium then shrank the whole document, which re-wrapped lines on every later page. It is fixed: there is no overflow now, and the later pages match v19 exactly.
- Not kept: the "Main users" column for the seven products other than Studio, all quotations in both exhibits, and the per-step evidence for who acts (the named speakers). Those claims are still cited, but the reader now sees a 2-4 word label in place of the quotation.
- Comparison file: `Exhibits_1_2_slim_preview.pdf`. Its pages are vector pages split out with pdfseparate (v19 pages 3 and 4, preview page 3). pypdf and reportlab add a 30pt yellow label band above each page, so no page content is covered.
