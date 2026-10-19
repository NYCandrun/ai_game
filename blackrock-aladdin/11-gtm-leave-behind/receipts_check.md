# Receipts check: Aladdin_Studio_From_The_Outside.html

Checked 2026-10-19 against the corpus under `scratchpad/` (B). Document body read from `B/gtm/out/Aladdin_Studio_From_The_Outside.html` (text extracted to `B/gtm/body.txt`, line numbers below refer to that extract). The document was not edited.

Verdicts: **OK** = corpus supports the claim as stated; **OK (note)** = supported, with a nuance worth knowing; **UNVERIFIED** = not contradicted, but no corpus file independently supports it; **WRONG** = corpus contradicts it.

## 1. Executive summary numbers

| # | Claim (body.txt line) | Verdict | Correction / note | Where checked |
|---|---|---|---|---|
| 1.1 | 54 public API specifications, 11 PyPI packages, 301 operations (l.18-19, 26) | OK | 54 entries, 11 distinct `d` values, sum of `o` = 301 | `B/apis.json` (recomputed); `B/unpacked/` holds 54 `swagger.json` files in 11 `asdk_plugin_*` dirs |
| 1.2 | "3,000 citizen developers", Woodhead, head of Studio engineering, 2025 (l.20-21, 25) | OK | Verbatim "we have 3,000 citizen developers in business engineers that are interacting with all that in using python or using r" | `B/yt/transcripts/01_From_Analytics_To_Intelligence_...md` |
| 1.3 | 4 of 16 on an eight-criterion test (l.22-23, 158, 263) | OK | Exhibit 6 Aladdin Studio row 1,1,0,0,1,1,0,0 sums to 4; all 11 rows re-added and match their stated scores (Bloomberg 5, State Street 4, Snowflake/Databricks 16, LSEG 12, FactSet 9) | body.txt Exhibit 6 (author's test; no external receipt possible) |
| 1.4 | JPMorgan paid $25.6M for Aladdin in 2025, "almost six times its 2017 level" (l.25) | OK | KF series 2016-2025: 1.5 (integration services), 4.4, 5.0, 5.3, 6.8, 4.6, 7.6, 6.9, 14.7, 25.6; 2017 = 4.4, 25.6/4.4 = 5.8 | `B/gtm/key_findings_v52.html` chart desc ("2016 to 2025: 1.5 ... 4.4 ... 25.6"); `B/gtm/kf_body.txt` l.20-21, 30 |
| 1.5 | 26 earnings calls since 2020, no executive said "Studio" (l.26) | OK | KF: "Across 26 earnings calls from the first quarter of 2020 to the second quarter of 2026, no executive said 'Studio'" | `B/gtm/kf_body.txt` l.26, 46-47 |
| 1.6 | API calls to grow 17 times by 2030, highest figure on the Investor Day slide (l.26) | OK | KF: 17x APIs vs 4x model portfolios, 2x portfolios, 1.3x trade allocations; tile says "the highest on BlackRock's slide" | `B/gtm/kf_body.txt` l.18-19, 42-43 |
| 1.7 | Seven data providers already connect AI tools (l.27) | OK | KF names FactSet, LSEG, MSCI, Arcesium, S&P Global, Snowflake, Databricks = 7; Exhibit 11 lists the same seven | `B/gtm/kf_body.txt` l.26, 200-201; body.txt Exhibit 11 |
| 1.8 | "every one tagged Access.Internal" (l.26, 101) | OK (note) | All 54 swagger.json files carry `"tags":[{"name":"Access.Internal"}]`. Note: every one of the 54 also carries `"x-access-level": "Public"`, which the document does not mention; "a label BlackRock does not explain in public" remains fair, but the co-existing Public level is worth a sentence | `B/unpacked/*/swagger.json` (54/54 hits for both strings) |
| 1.9 | Four speakers, early 2024 to late 2025 (l.27) | OK | Khara early 2024, Newman Jan 2025, Goel 2025, Woodhead Nov 2025 | transcript headers (see section 3) |
| 1.10 | Method: "Ten specifications expose a long-running-operations endpoint and 35 operations are flagged" (l.101) | OK | `lro: true` on 10 of 54 entries; `x-aladdin-lro` key occurs 35 times | `B/apis.json`; `B/unpacked/*/swagger.json` |
| 1.11 | Technology services revenue $2.0B in 2025, up 24% with Preqin (l.44) | OK | KF tile "$2.0B ... up 24% with Preqin" | `B/gtm/kf_body.txt` l.22-23 |

## 2. Exhibit 4 per-domain counts (recomputed from `B/apis.json`, fields d/n/s/o)

| Domain | Doc (specs/ops/alpha/beta/stable/sunset) | Recomputed | Verdict |
|---|---|---|---|
| Investment operations | 15/74/9/4/2/– | 15/74/9/4/2/0 | OK |
| Analytics | 9/53/–/–/8/1 | 9/53/0/0/8/1 | OK |
| Investment research | 5/41/5/–/–/– | 5/41/5/0/0/0 | OK |
| Platform | 6/29/2/–/4/– | 6/29/2/0/4/0 | OK |
| Portfolio management | 4/28/1/–/3/– | 4/28/1/0/3/0 | OK |
| Portfolio | 3/23/1/–/2/– | 3/23/1/0/2/0 | OK |
| Data | 1/15/–/–/1/– | 1/15/0/0/1/0 | OK |
| Trading | 2/14/1/–/1/– | 2/14/1/0/1/0 | OK |
| Compliance | 4/9/3/–/1/– | 4/9/3/0/1/0 | OK |
| Accounting | 4/8/2/2/–/– | 4/8/2/2/0/0 | OK |
| Clients | 1/7/–/–/1/– | 1/7/0/0/1/0 | OK |
| **Total** | 54/301/24/6/23/1 | 54/301/24/6/23/1 | OK |

"Largest APIs by operations" column: every named API is the top-N by `o` in its domain (e.g. investment operations: PrincipalInterestFactor, CounterPartySettlementInstruction, MiscellaneousCashflow, CouponReset; analytics: RiskRule, RiskWorkflow, RiskException, RiskConfig; portfolio: PortfolioGroup, RestrictedAsset, PortfolioToolkit). "and 1 more" for investment research = Engagement. OK. The document's "11 domains, 11 PyPI packages" matches 11 distinct `d` values and 11 unpacked package directories.

## 3. Verbatim quotations attributed to BlackRock (and partner) speakers

All fragments were grepped (case- and quote-normalised) across `B/yt/transcripts/*.md` and `B/yt/transcripts2/*.md`. Each was found exactly once in the file named (twice where the same recording exists in both folders).

| # | Quote (body.txt line) | Verdict | Wording / speaker / title / date | Where checked |
|---|---|---|---|---|
| 3.1 | Woodhead three-pillar definition, "So we think about Aladdin today as a platform ... set of developer tools." (l.56-57) | OK | Verbatim. Host credits him at the close as "managing director and head of engineering for Aladdin Studio at Black Rockck" (caption spelling); title matches | `B/yt/transcripts/01_From_Analytics_To_Intelligence_BlackRock_s_Journey_To_Data_P.md` |
| 3.2 | Woodhead "3,000 citizen developers in business engineers that are interacting with Aladdin using Python or using R" (l.218) | OK (note) | Captions read "interacting with all that in using python or using r"; the document silently renders "all that in" as "Aladdin" (a caption mis-hearing of a proper name, which the method statement allows) and drops "all that". Acceptable under the stated rule; a bracket would be cleaner | same file |
| 3.3 | Woodhead "I think that number has probably peaked" / "increasingly sophisticated workloads are going to be presented through natural language" (l.218) | OK | Verbatim | same file |
| 3.4 | Woodhead "hundreds of Snowflake accounts ... tens of thousands of pipelines" (l.83, 167) | OK | Verbatim ("we operate um hundreds of snowflake accounts ... tens of thousands of pipelines") | same file |
| 3.5 | Woodhead date "published November 11, 2025" (l.57, register 2) | UNVERIFIED | The transcript header (`Channel: Snowflake Inc. Length: 27:21 Source: youtube.com/watch?v=Me_H_-E6lSg`) carries no date; no yt-dlp metadata for this video is in `B/yt4`. The date appears only as an assertion in `B/compendium/Aladdin_Studio_BlackRock_Compendium.md` ("published 11 Nov 2025"). Not contradicted, but no primary receipt in the corpus | `B/yt/transcripts/01_...md` header; `B/yt/subs/Me_H_-E6lSg.en.vtt` (no date) |
| 3.6 | Woodhead venue "Snowflake Data Cloud podcast" (l.24, 57) | OK | Transcript opens "Welcome to the Data Cloud podcast, Dave"; channel Snowflake Inc. | same file |
| 3.7 | Newman "which is part of Studio"; "we're releasing soon the ability to actually access those analytic APIs ... That's all part of the Studio umbrella" (l.63, 168, 331) | OK | Verbatim. "General Manager, Aladdin Studio"; series date Wed 08 Jan 2025; title "Data: The key ingredient" | `B/yt/transcripts2/013_Data_The_key_ingredient.md` (also `B/yt/transcripts/11_...md`) |
| 3.8 | Goel "every single transaction that happens should be available and accessible to you via an event, via an API" (l.80, 169, 332) | OK | Verbatim. Self-intro (Whisper) "Global Head of Data from Aladdin"; webinar page undated, 2025 inferred from "recent close to the Preqin acquisition" | `B/yt/transcripts2/050_Data_as_a_strategic_asset_for_pensions.md` |
| 3.9 | Goel "within 15 minutes of latency"; "a near real time data store"; "3,000 people who qualify in this bracket today"; "start exposing some of the software and application that we're building" (l.81, 218, 320, 332) | OK | All verbatim | same file |
| 3.10 | Khara "the Aladdin studio estate ... is going to this year be a major, major unlock"; "more users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis at machine scale, over and above what they get through our front end applications" (l.170, 235, 330) | OK | Verbatim. Host introduces "MD and Global Head of Aladdin Product"; Buy-Side Technology Awards 2023 winner interview; "very, very focused in 2024" supports "early 2024" | `B/yt/transcripts2/061_Best_Overall_Technology_Provider_for_2023.md` |
| 3.11 | Miller: Data Cloud replaced "flat files ... FTP and related transfers" (l.171) | OK | "we sent flat files, we sent large schema definitions, ftp and related transfers"; self-intro "Managing Director, Global Head of Data Platform and Product Engineering at BlackRock"; undated | `B/yt/transcripts/17_BlackRock_Transforms_Client_Data_Delivery_With_Snowflake_s_A.md` |
| 3.12 | Rosales: "BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries"; "around 7,000 people, with over 4,000 of those being engineers"; "around 100 Aladdin front-end applications" (l.44) | OK | Verbatim. "AI engineering lead at BlackRock"; Valdez "Principal AI Engineer"; LangChain Interrupt 2025 | `B/yt/transcripts/16_How_BlackRock_Built_Production_AI_Agents_for_Asset_Managemen.md` |
| 3.13 | Rosales/Valdez: "couple of thousands agents and tools"; "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" (l.291) | OK | Verbatim | same file |
| 3.14 | Crockett "There's no copilot without plug-ins" (l.291) | OK | Verbatim ("there's no copilot without plug-ins"); page credits "Adrian Crockett, General Manager, Microsoft Cloud for Financial Services, and Syril Smith Garson, Head of Product for AI"; series date Wed 06 Nov 2024 | `B/yt/transcripts/13_Never_Done_podcast_Microsoft_part_2_Humans_in_the_loop.md`; `B/yt/pages/ms_podcast_2.txt`; `B/yt/transcripts2/023_Microsoft_Copilot_Episode_Part_2.md` header |
| 3.15 | Georgeson (Royal London) "credits the Snowflake implementation inside its Aladdin programme" (l.25, 199) | OK (note) | Paraphrase, not a quotation. Transcript: "the implementation of Snowflake that we did as part of the overall programme has been really successful for us". He says "overall programme", not "Aladdin programme"; the video is the Aladdin client story, so the gloss is reasonable. CEO title and Chouman title match the page description; "recorded November 2024" rests on the media filename `20241113_RLAM-404` | `B/yt/transcripts2/058_Shaping_Tomorrow_with_Technology.md` |
| 3.16 | Schafer "What's the API suite that you have? Are you using connectors to Snowflake or to Databricks? And I think that that part of the RFP has become much more prominent." (l.322-323) | OK (note) | Verbatim except captions read "data bricks" (corrected proper-name spelling, allowed by method). Introduced as "a partner in the Asset & Wealth Management Consulting at Alpha FMC" | `B/yt/transcripts2/049_Build_vs_Buy_Webinar_Replay.md` |
| 3.17 | Sewdass "Head of Aladdin Solutions Engineering, Americas"; Campos "US asset manager coverage" (register 63) | OK | Captions: "Alisha Sewdass, who runs our Aladdin Solutions Engineering team for Aladdin in the Americas"; "My name is Michael Campos. I cover the US Asset Managers for Aladdin" | same file |
| 3.18 | Pemmaraju "the data model itself is structured for agentic use cases" (l.291) | OK | Verbatim; "Head of AI Product & Engineering"; series date Thu 16 Jul 2026 | `B/yt/transcripts2/028_Reducing_time_to_insight_how_AI_reshapes_risk_management.md` |
| 3.19 | Somasundaram "a burgeoning community of individuals saying 'I need that in the form of an API'" (l.236) | OK | Verbatim; "Global Head of Aladdin Partnerships & Trading Product Marketing"; series date Thu 25 Dec 2025 | `B/yt/transcripts2/017_How_Data_Architecture_Shapes_Modern_Trading.md` |

## 4. Page quotations

| # | Claim | Verdict | Note | Where checked |
|---|---|---|---|---|
| 4.1 | Copilot "now available to all Aladdin clients" (l.66, 291) | OK | "Introducing Aladdin® Copilot, now available to all Aladdin clients." | `B/yt/pages/copilot_page.txt` l.97 |
| 4.2 | Copilot "will not give investment advice or respond to questions outside Aladdin platform boundaries" (l.66, 291) | OK | Page bullet: "Will not give investment advice or respond to questions outside Aladdin platform boundaries" | `B/yt/pages/copilot_page.txt` l.110 |
| 4.3 | Studio page headings "Create & automate," "Make Aladdin your own," "Align internally & externally" (l.117, 343) | OK | FACT_CHECK: "The Studio page lists 'Create & automate', 'Make Aladdin your own', 'Align internally & externally' as benefit headings (verified earlier from the page)"; presented as headings, as the fact check asked | `B/pdfcheck/FACT_CHECK_briefing_and_what_it_does.md` l.28 (not in `B/aladdin_studio_briefing.md`) |
| 4.4 | APIs page says "dozens of APIs" (l.76, 117) | OK | FACT_CHECK: "the APIs page says 'dozens of APIs'" | `B/pdfcheck/FACT_CHECK_briefing_and_what_it_does.md` l.118 |
| 4.5 | Studio page persona quote "a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting" (l.64) | OK | Verbatim on the captured page | `B/crawl2/` captured Studio page (grep "code-curious") |

## 5. SDK facts and the Janus Henderson commit (vs `B/gtm/key_findings_v52.html`)

| # | Claim (l.263) | Verdict | Note | Where checked |
|---|---|---|---|---|
| 5.1 | 14 releases since May 2024, all alpha or beta | OK | KF: "The SDK itself has had 14 releases since May 2024, all alpha or beta" | `B/gtm/kf_body.txt` l.72 |
| 5.2 | Core at 2.0.0b10 in July 2026; add-ons at 2.0.0b3 | OK (note) | **Not in the Key Findings file** (no "b10" in its text). 2.0.0b3 is the unpacked package version. 2.0.0b10/July 2026 is supported elsewhere in the corpus: `B/compendium/_pre_edit_part2.md` l.17 ("stood at version 2.0.0b10 in July 2026 ... only the 2.0.0b10 version independently verified") | `B/gtm/kf_body.txt` (absent); `B/compendium/_pre_edit_part2.md`; `B/unpacked/` dir names |
| 5.3 | None installs on Python 3.13, each pins an old Snowflake library | OK | KF l.72 verbatim | `B/gtm/kf_body.txt` l.72 |
| 5.4 | Conflicts with the official MCP toolkit; outside fix merged August 2026, not shipped | OK | KF l.72 verbatim; register 31 = PR 57 "merged August 2026" | `B/gtm/kf_body.txt` l.72 |
| 5.5 | Janus Henderson commit block: "From 1c1bd2559e4e4da2591f13dccfd7db6c2f9dc68c Mon Sep 17 00:00:00 2001 / From: <@janushenderson.com> / Date: Mon, 1 Dec 2025 16:53:28 +0000 / Subject: [PATCH 1/3] Added ability to add additional HTTP headers." (l.210) | OK | Character-for-character identical to KF l.39-40, including the redacted name/address and "View the raw commit on GitHub: blackrock/aladdinsdk, commit 1c1bd25" | `B/gtm/kf_body.txt` l.39-40 |
| 5.6 | "All six commits carry the same author line"; "The SDK's contributor history shows no code from any other company" (l.209, 218) | UNVERIFIED | KF shows one patch header ([PATCH 1/3]); the six-commit count and contributor graph are cited to GitHub (register 44, 46), not present in the corpus as files | `B/gtm/kf_body.txt` l.39 |

## 6. Statements of absence

| # | Statement (line) | Verdict | How attributed |
|---|---|---|---|
| 6.1 | "No executive has said 'Studio' on 26 earnings calls since 2020" (l.26, 228, 352) | OK | Cited to [10] roic.ai third-party transcripts, graded **T**; Exhibit 9 source line says "Counts are the author's tally. Zero counts are reliable; other counts are approximate." Matches KF l.26/46 wording |
| 6.2 | "No public connector for Aladdin was found on BlackRock's product pages or GitHub" (l.270) | OK | Framed as "was found", cited to [8] product page and [55] GitHub org (both **P**, author's search); matches KF l.201 verbatim. Exhibit 11 Aladdin row: "None found." |
| 6.3 | "A full-text search of SEC EDGAR finds no company filing that mentions 'Aladdin Studio'" (l.199) | OK | Cited to [40], the EDGAR search URL itself (**P**, author's test); KF l.30/46 say the same |
| 6.4 | "Try: Nothing: no sandbox, trial or public test environment was found" (l.119) | OK | Author's test, Exhibit 5 source line "read with no account, login or payment, October 2026" |
| 6.5 | "the webinar did not name it [Studio]" (l.325) | OK (note) | Author's reading of the 049 captions; grep of `B/yt/transcripts2/049_*.md` for "studio" confirms zero hits |

## 7. Build vs. Buy poll numbers (vs `B/yt/transcripts2/049_Build_vs_Buy_Webinar_Replay.md`)

| # | Claim (l.298-319) | Verdict | Caption text |
|---|---|---|---|
| 7.1 | Poll 1: 37% mostly vendor, 30% hybrid, 18% actively re-evaluating, 15% mostly built in house | OK | "mostly built in house at about 15%. The next is actively reevaluating at 18%, hybrid second most at 30 and then mostly vendor platforms at 37%" |
| 7.2 | Poll 2: "AI and data demands" 42%, cost and speed to market tied | OK | "the most common answer was AI and data demands at 42% an exact tie between cost and speed to market And last place was regulatory comp[liance]" |
| 7.3 | Poll 3: compliance reporting 53%, position and cash management 22%, trade lifecycle 17%, risk infrastructure 9% | OK | "compliance reporting is number one at 53% followed by position and cash management 22% ... trade life cycle at 17 and finally risk infrastructure at 9%" |
| 7.4 | "The slide put 60 to 70 percent of technology cost in 'maintenance of current systems'" | OK (note) | Host: "the number we have in here is 6070% of tech costs or maintenance of current systems" (caption drops the dash; elsewhere "60 to 70% of your tech organisation focused on keeping the lights on"). "In 'maintenance of current systems'" is quoted from a caption, which reads "or maintenance"; the slide itself is not in the corpus |
| 7.5 | "the Alpha FMC panellist said a transformation runs 'roughly 12 to 18 months'" | OK | Host: "Clark, to continue, what's an honest timeline?" followed by "Typically we see a transformation like the one we're talking about now, roughly 12 to 18 months." Speaker = Schafer |
| 7.6 | "Attendee counts were not stated" | OK | No attendee count in captions |

## 8. Source register

| # | Check | Verdict | Note |
|---|---|---|---|
| 8.1 | Every superscript in the body resolves to a register entry | OK | 68 distinct numbers cited (1-68, none missing); 68 register entries; no dangling citation; no uncited entry; first-citation order is strictly 1,2,3...68 as the register claims |
| 8.2 | Every entry has a grade letter | OK | 68/68 carry P, S or T (P: 51, S: 11, T: 6 by the register's grouping) |
| 8.3 | Every entry has a date | OK | 68/68 carry a year or "undated" (12: "early 2024"; 14: "2025, page undated"; 39: "undated"; 63: "replay page undated") |
| 8.4 | Every entry has a URL; none malformed | OK | 68/68 have one well-formed https URL. 47 (2023 Investor Day) sits under a `/2025/` folder on q4cdn, which looks odd but is the URL the corpus itself carries (`B/htmlrev/src/key_findings_original.html`) |
| 8.5 | URLs vs corpus headers | OK (note) | All YouTube and blackrock.com recording URLs (2, 13, 14, 18, 39, 52, 61, 62, 63, 7, 12) match the `Source` lines of the transcript headers exactly. **Entry 25** gives `blackrock.com/aladdin/products/aladdin-data-cloud`; the captured page and 360 corpus references use `blackrock.com/aladdin/platforms/products/aladdin-data-cloud` (the short form appears only 9 times, in the earlier briefing/KF drafts). Probably a redirect, but inconsistent with 8, 23, 26, which all use `/platforms/products/`. Entries 1 and 4 (a PyPI search URL and an EDGAR browse URL) appear nowhere else in the corpus; both are generic index pages, not malformed |
| 8.6 | Register 2 title/venue | OK (note) | Title "From Analytics To Intelligence: BlackRock's Journey To Data Productization" matches the transcript header; "(Snowflake Data Cloud podcast; auto-captions)" matches header "YouTube auto-captions"; publication date see 3.5 |

## Things the document states that the corpus does not independently support

1. **"published November 11, 2025"** for the Woodhead podcast (register 2, Exhibit 7, l.57). The transcript header and the caption file carry no date; the only corpus mention is a later compendium that asserts it. Not contradicted; just no primary receipt in the corpus.
2. **"the core at 2.0.0b10 in July 2026"** (l.263) is not in the Key Findings file the paragraph otherwise follows; it rests on `B/compendium/_pre_edit_part2.md`, which says only the b10 version was independently verified. The cited receipt [30] is PyPI, which is fine, but the KF cross-check fails for this one number.
3. **"All six commits carry the same author line"** and **"The SDK's contributor history shows no code from any other company"** (l.209, 218). The corpus holds one patch header ([PATCH 1/3]); the six-commit count and contributors graph are GitHub receipts [44, 46] with no corpus copy.
4. **Access.Internal** (l.26, 101, 384): accurately reported, but every one of the 54 specs also carries `"x-access-level": "Public"`. The document never mentions this, and Exhibit 15 question 5 asks what the tag means without noting the co-existing Public level.
5. **Georgeson "credits the Snowflake implementation inside its Aladdin programme"** (l.25, 199): he says "as part of the overall programme"; "Aladdin" is the document's gloss.
6. **Woodhead "interacting with Aladdin"** (l.218): captions read "interacting with all that in"; the document corrected the mis-hearing without a bracket. Allowed by its own method statement, but it is a correction of more than a spelling.
7. **"The slide put 60 to 70 percent ... in 'maintenance of current systems'"** (l.298): the slide is not in the corpus; the phrase is the host reading it out ("6070% of tech costs or maintenance of current systems").
8. Not checked (outside the brief): the Method paragraph's counts of 126 recordings, 121 BlackRock-channel, 15 product pages, and the breakdown 39/12/15/3/2/32 (l.137).

## Counts

- Claims checked: 60 rows across sections 1-8.
- WRONG: 0.
- OK: 52.
- OK with a note: 8 (1.8, 3.2, 3.15, 3.16, 5.2, 6.5, 7.4, 8.5, 8.6 overlap; see table).
- UNVERIFIED (not contradicted, no corpus receipt): 2 (3.5 publication date; 5.6 six commits / contributor graph).
- Exhibit 4: 11/11 rows and all 6 totals match the recomputation exactly.
- Quotations: 19/19 found verbatim in the named transcript, with the speaker, title and date as the recording or page gives them (two proper-name caption corrections noted).
- Register: 68/68 entries cited, graded, dated, with a URL; one URL path variant flagged (entry 25).
