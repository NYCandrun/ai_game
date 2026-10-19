<!-- agent a4be6e45adf70dca7; started 2026-10-19T14:47:43.086Z; finished 2026-10-19T15:37:32.596Z -->

## Outputs
- HTML: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.html (head byte-identical to the original; no scripts or external resources added; html.parser check: no mismatched tags, no duplicate ids, no dangling #anchors)
- PDF (Chromium, the deliverable): /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/htmlrev/out/Aladdin_Studio_Briefing_and_Interview_Guide_REVISED.pdf — **81 pages** (untouched original renders at 74 in the same Chromium; +7 pages from the added material and re-flowed footnote pages)
- Build is reproducible: `python3 -I htmlrev/work/edits.py` (edits.py + edits2.py, 96 exact-match replacements from src/briefing_original.html), then `htmlrev/work/fnfit.py fit|refit` (footnote margin tuner) and `pagenums.py` (TOC/divider numbers). `work/chain.sh` runs the whole sequence.

## Changes ported (all items in REVISED.md's verification notes)
- 58 → 54 API specifications (301 operations kept); new spec-facts list in §7 (24 alpha / 6 beta / 23 stable / 1 sunset; app-key header + OAuth scopes; 35 long-running ops; linter comment; Access.Internal; ADX).
- Exhibit 24 APIs row: Aladdin Graph described as the API layer (every public spec is an "agraph" API); investment research as a domain of five alpha APIs.
- Citizen developers: Exhibit 6 row, §7 "How big it is" and Appendix A now 3,000 BlackRock-internal, verbatim Woodhead ("has probably peaked") and Goel, linked to the Snowflake podcast and the pensions webinar; Nair's Citisoft note dropped. Exhibit 26 first use → November 2023 (Global Insurance Report podcast), later uses March 2024 and SDK README.
- SLC Management (Exhibit 33) downgraded to "placement only"; Exhibit 8 gains a "Featured in BlackRock-published podcasts or videos" sub-table (Intesa, SLC, Aviva, TCW, UPP, Ingka, Helvetia, Northstar, eFront testimonial clients) with links.
- "Never named a Studio reference client" softened in Summary, §7, §8, §11, §13 question, Appendix A, with the Royal London CEO/Snowflake caveat.
- Royal London re-sourced to Hans Georgeson's client video (§3 bullet, §5 switching-costs bullet, Exhibit 16 row; note 42 reworded, thinkFolio/Murex kept as trade-press names). BNP Paribas: §5 lede, Exhibit 16 row, note 43 and Appendix A now attribute the 60 apps to the whole 2016–2020 programme, linked to BlackRock's podcast.
- Exhibit 21 awards: three 2023 awards named, linked to BlackRock's winner interview.
- 68%/303: §6 paragraph rewritten as unconfirmed; §7 paragraph; Exhibit 40 row; §18 closing question replaced with the Build vs Buy poll; new Appendix A row.
- New Exhibit 20A (Build vs Buy webinar poll, 7 rows) placed after the §6 paragraph, with source line; Exhibit 40 gets "Studio as a leadership priority" (Khara) and "Build vs buy evidence" rows; Fink-letter row re-attributes "language of the portfolio" to Woodhead and the ACF 2026 opener; private-credit row restated as the author's framing + product facts.
- "More than 5,000 risk factors" → "thousands", with the Fivetran source linked (Exhibit 5 + notes line; Appendix A bullet).
- Titles: Schaefer, Stratigos, Nair, Rosales/Valdez, Woodhead (two published titles), Goel, Pemmaraju/Skinner/Somasundaram dates, in Exhibits 27 and 38.
- Three Studio benefits shown as the Studio page's headings in §7 and §11 (with &amp;).
- Exhibit 27: Woodhead Snowflake quote replaced with verbatim podcast lines; Skinner guardrails line; Goel webinar lines; Garson "transparency / human in the loop"; Newman governance line; Rosales/Valdez evaluation line linked to the LangChain recording (ZenML note 53 dropped); new Pemmaraju and Somasundaram rows; Woodhead three-pillar paragraph and Data Cloud scale paragraph added in §7; Khara "major unlock" paragraph after Exhibit 25 and "eat our own cooking" in §8.
- Stratigos (§12), Skinner semantics (§7, §15), Goel "must be codified" (§15), Rivosecchi (§7, §16 → Jeff Miller flat-files/FTP line, linked) replaced as REVISED.md does. "No copilot without plugins" now verbatim, attributed to Adrian Crockett, linked to the Microsoft part-2 podcast page; the WatersTechnology/secondhand notes 54–55 dropped.
- Client Forum cadence removed (links to ACF 2026 and the APAC 2025 recap); engineer-led content sentence added.
- CalPERS revision note in Exhibit 11 notes and Appendix A row. Insurer scale quote (Anderson) in §3 table.
- Appendix A: 68% row, risk-factor bullet, Client Forum cadence bullet, BNP bullet, Skinner-semantics row extended. Appendix B: new "BlackRock podcasts, webinars and videos used for this revision" list (all linked), plugin-builder entry notes 54 specs, LangChain recording added.
- Front matter: cover meta "As of October 8, 2026 | Revised October 19, 2026" (one line), cover footer and back page carry the fact-check sentence; new "Verification notes for this revision" chapter (section.chapter, h2, lede, two h3s) after Appendix B; row added to the contents list and the Appendices divider (letter column left blank, since the chapter is not titled "Appendix C").
- Footnotes: 3 notes removed (12 Citisoft, 53 ZenML, 54/55 WatersTechnology+secondhand summary; 66 remain), all markers and notes renumbered continuously by script.

## Footnote check (Chromium render)
Script `work/fnfit.py check` measures every `.footnotes` block via pdfplumber: all 26 blocks sit at the foot of the page that carries their markers (bottom ≈ 733pt, matching the reference render); 0 flags after the final render. To keep them on their pages I moved/split blocks and table cuts: fnb-u106 now before Exhibit 8 (its asset-manager table re-joined), fnb-u125 before the Insurers sub-table, fnb-u143 split (notes 16–17 after the Nest row; 18–20 merged into fnb-u159, which now sits after the banks table and before the new featured sub-table), Exhibit 22 cut before its BlackRock row (fnb-u338), Exhibit 26 cut after the "Open, opening Aladdin" row (fnb-u377), fnb-u422 moved before the "Community" h3, fnb-u394 after chapter 8's lede. Exhibit 27's `keep` class was removed so the longer table can flow across pages 37–38.

## Page numbers
Contents and all four divider lists re-numbered from the final render (Summary 3, Part 1 5, ch1 6, 2 9, 3 10, 4 18, 5 22, 6 26, 7 32, 8 39, Part 2 46, 9 47, 10 49, 11 51, 12 54, 13 57, Part 3 61, 14 62, 15 64, 16 66, 17 69, 18 71, Appendices 73, A 74, B 77, Verification notes 79); re-rendered and re-measured, unchanged.

## Judgement calls / not placed
- Evidence-label spans (`span.lbl`) are not used: the HTML edition carries no Label columns anywhere (0 in the original and in key_findings), expressing evidence by links + numbered notes, so REVISED.md's "(Confirmed …)" parentheticals became links to the BlackRock-published page/recording (URLs taken from the transcript headers) and source lines. Exhibit 20A therefore has Finding / What was said columns plus a source line, no Label column.
- The Khara winner-interview video's only recorded source URL is the generic blackrock.com/aladdin/discover hub; that is what is linked.
- Vedant Naik's name stays redacted (the HTML's existing `.redact` span) although REVISED.md prints it.
- Edition-level differences between REVISED.md (built from the PDF/docx edition) and the HTML that are not fact-check items were not ported: e.g. $462,000 vs $463,000 (Nest), JPMorgan 2016 vs 2018, Exhibit 32 "6 vs 7 contributors", Exhibit 28 dates, the md's "(the original shows this as a bar chart)" remarks.
- Sudhir Nair's Exhibit 38 title changed to "Global Head of Aladdin" per REVISED.md, keeping the AWS release link.

## Layout caveats
- Part-page gaps on pages 16, 39, 40 and 15/16 area come from the original's keep-together exhibits (Exhibit 9, Exhibit 30) and the runon chapter 8 heading now landing late on page 39; the reference render shows the same gaps before Exhibits 9 and 30. Page 39 has the chapter 8 heading and lede with the note for chapter 7's marker 52 at its foot and ~150pt of white space between.
- WeasyPrint render was not produced (coordinator instruction: Chromium is the deliverable; the footnote tuning is Chromium-specific).
