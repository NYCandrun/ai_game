# Readability review, preview pages 8 to 14 (Part 2, Exhibits 8 to 13, Part 3, Exhibit 14)

Preview pages 8 to 14 hold the content of original pages 8 to 13. Every change in that span was diffed (current.html against preview.html) and both PDFs were rendered at 80 dpi, with Exhibit 14 also at 200 dpi. Proposed rewrites were test-rendered with the same headless Chromium that built preview.pdf. Test files are in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/rd08 (e3.pdf has every proposal below, and e4.pdf adds the Bloomberg trim). Both come to 21 pages, with Exhibit 9 back on page 8.

Process note: apply_preview.py applies every `also_change`, including those marked "alternative only". On these pages that put the p09-01 **alternative** Finding 2 heading into the preview, although the recommended option keeps the heading. Outside my scope, p15-119 has an "alternative only" group row that was probably applied the same way.

## Fix table

| fix id | where (page in preview) | verdict | problem | proposed cleaner text (visible words) |
|---|---|---|---|---|
| p08-03 | 8, first paragraph | SAME | The appositive is longer, but the paragraph stays at 5 lines and the name is needed. | None needed. |
| p08-31 (title) | 9, Exhibit 9 title | CLEARER | None. | None. |
| p08-31 (Nest row, also_change) | 9, Exhibit 9 Nest row | BROKEN LAYOUT | The Nest cell grows from 1 line to 2. Rows 1 and 3 were already 2 lines because their buyer names wrap. That one extra line pushes the whole of Exhibit 9 off page 8 onto a page of its own, about 75% blank. | Nest chose BlackRock’s Aladdin over six other bids<sup>57</sup> (tested: on its own this brings Exhibit 9 back onto page 8) |
| p08-35 | 9, Exhibit 9 PPF row | SAME | A superscript in the middle of the cell, and "valued at up to … against the fund’s estimate of up to" reads heavily. Source 54 is already on the buyer name. | BlackRock won both parts of the tender, at up to £74.0 million, against the fund’s estimate of up to £55 million<sup>55</sup> |
| p08-40+p08-41+p08-42 | 9, Exhibit 9 PBGC row | WORSE | It repeats "2017 and again in 2023" from the Year column beside it, and the cell is longer than the one it replaces. | BlackRock won an investment risk system contract both times, at about the same yearly price<sup>58, 59</sup> |
| p08-43 | 9, Exhibit 9 note | SAME | The note is longer but stays on one line. The semicolons separate sources, not sentences, so they are fine. | None needed. |
| p09-01 | 10, Finding 2 lead sentence | WORSE | The new first sentence and the second sentence both say API calls grow to 2030 ("grow fastest of the four volumes it forecasts to 2030" and then "would grow 17x by 2030"). "Grow fastest of the four volumes" reads awkwardly. | BlackRock tells investors that API calls will grow fastest, without naming the product behind them. At its 2025 Investor Day it projected four volumes to 2030, and API calls across BlackRock and Aladdin led at 17x<sup>10</sup>. (This replaces both sentences. "Attributing them to Studio…" follows unchanged.) |
| p09-01 (heading, alternative only) | 10, Finding 2 heading | WORSE | Applied by mistake: the recommended option keeps the heading. "BlackRock’s fastest-growing forecast for investors runs through Studio" is stilted. | Keep the current heading: "2. BlackRock’s growth story to investors runs through Studio, though it rarely says the name" |
| p09-27 | 10, Exhibit 10 last row | CLEARER | None. | None. |
| p10-03+p10-04 (also_change "Much of") | 10, private-markets paragraph | SAME | A light hedge. It reads fine. | None needed. |
| p10-01 | 11, direction box | CLEARER | None. | None. |
| p10-03+p10-04 | 11, direction box | CLEARER | None. | None. |
| p10-07+p10-10+p10-13 (with s54 wording) | 11, Finding 3 paragraph | WORSE | The Crockett quote sits between the inference and its premise. The fronted "That Copilot and Studio use the same APIs is my inference<sup>1, 8</sup>" is clumsy and adds a superscript pair. The paragraph grows by about 1.5 lines. | …already out in production”<sup>8</sup>. Teams can also register agents of their own<sup>8</sup>. Studio “exposes everything Aladdin knows how to do” as APIs and events<sup>1</sup>. So I infer that Copilot and Studio use the same APIs. Microsoft’s Adrian Crockett made the dependence plain… (the rest unchanged) |
| p10-ex11-title | 11, Exhibit 11 title | SAME | Still two lines. | None needed. |
| p10-ex11-aria | 11 (not printed) | SAME | None. | None. |
| p10-ex11-box | 11, Exhibit 11 second box | SAME | It repeats the quote that follows, as before. Still 2 lines. | None needed. |
| p10-25 | 11, Exhibit 11 black box | WORSE | The box grows from 4 to 5 lines and holds 3 sentences, with "investment advice" 3 times in a small funnel box. | **One answer**, never investment advice: the product page says Copilot “will not give investment advice”<sup>20</sup>. The team tests every rule in its system prompts<sup>8</sup>. (Keep the video link on "tests every rule". Tested: 4 lines.) |
| p11-34 (prose, also_change) | 11, paragraph before Exhibit 12 | SAME | Now two sentences. It reads fine. | None needed. |
| p11-34 (title, rows, note) | 12, Exhibit 12 | SAME | The Bloomberg row wraps and leaves "2026" alone on the second line. The Bloomberg row describes data access but sits under "System-of-record rivals". The title's "AI access to their data" covers this, so it is acceptable. Its receipt says "Bloomberg press release" but links to a Webull copy, although register entry 73 names PR Newswire. | Bloomberg launched an MCP server for licensed data in September 2026 (tested: one line) |
| p11-12 | 12, Exhibit 12 group row | CLEARER | None. | None. |
| s59 (also_change, link only) | 12, Databricks receipt | SAME | No visible change. | None. |
| s60 (also_change) | 12, Aladdin receipt | SAME | None. | None. |
| p11-35 | 12, direction box | WORSE | "The user groups each tool’s owning team allows" is a hard noun stack. | A public account of the Copilot plugin model would cover the production Aladdin APIs its tools call, which user groups may use each tool, and tested no-advice guardrails<sup>8, 20</sup>. |
| p11-38 | 12, Finding 4 heading | CLEARER | Still 2 lines. It matches the Exhibit 13 title. | None. |
| p11-38 (also_change) | 13, rivals paragraph | CLEARER | None. | None. |
| p13-01 | 14, Part 3 paragraph 1 | SAME | Only the citations changed. | None. |
| p11-34 (also_change, Part 3) | 14, Part 3 paragraph 2 | SAME | A cluster of 4 superscripts, which was 3 before. | None needed. |
| p13-06+p13-07+p13-08+p13-09 | 14, Part 3 paragraph 2 | SAME | In "the team that owns it", "it" could mean the tool or the API. | About 100 of its applications carry Copilot. Each Copilot tool maps to a production Aladdin API. The team that owns each tool sets which user groups can use it<sup>8</sup>. |
| p13-47 (also_change, body) | 14, Part 3 paragraph 2 | CLEARER | Dropping the citation is fine. | None. |
| p13-22 | 14, Exhibit 14 title | CLEARER | Now fits on one line. | None. |
| p13-22 (also_change, band header) | 14, "A CLIENT’S USE · THROUGH STUDIO" | SAME | None. | None. |
| p13-aria | 14 (not printed) | SAME | None. | None. |
| p13-26 | 14, Exhibit 14 apps box | SAME | Fits. | None. |
| p13-27 | 14, Exhibit 14 Copilot box | SAME | The third line fits the box. | None. |
| p13-34+p13-35 | 14, Exhibit 14 band caption | CLEARER | Shorter, two plain sentences. | None. |
| p13-34+p13-35 (also_change, sources line) | 14, Exhibit 14 note | SAME | Two more superscripted sources. The note is still 3 lines. | None needed. |
| p13-37 | 14, Exhibit 14 controls header and box titles | BROKEN LAYOUT | "Access scoped per API" runs into the right border of its box at print size. ("Compliance by default" now fits. "Compliance on every order" used to overflow.) | Access set per API (tested: fits, and matches page 2’s "Access is set API by API") |
| p13-40 | 14, Exhibit 14 "A second approver" box | SAME | The body says "second check" under the title "approver". It is close enough. | None needed. |
| p13-47 | 14, Exhibit 14 note and hatched box | CLEARER | "Nearest public sign:" works as a box label. | None. |

## Layout

- **Pages 8 and 9 (the main problem).** Exhibit 9 no longer fits on page 8. Page 8 ends about 20% blank, and page 9 holds only Exhibit 9 with about 75% white space. The page 8 text did not grow: the p08-03 paragraph is still 5 lines. Only the Nest row grew, from 1 line to 2, because the PPF and PBGC rows were already 2 lines from their wrapping buyer names. Original page 8 had almost no slack, so one line was enough to move the exhibit.
  - **Fix that keeps the content (tested):** set the Nest cell to "Nest chose BlackRock’s Aladdin over six other bids" with source 57, keeping source 56 on the buyer name. Exhibit 9 then fits back on page 8 and the document is 21 pages. Both facts stay: the award (56, seven bids) and Nest’s own "selects BlackRock’s Aladdin" (57). The note’s PPF-to-Aladdin sentence also stays.
  - The PPF and PBGC trims above are optional and also tested. They fit, but give no extra room, because those rows stay 2 lines from their buyer names. The exhibit note sits just above the footer, which is as tight as the original was.
- **Page 10.** The Finding 2 heading (alternative, applied in error) wraps to 2 lines, as the old one did. Page fit is fine.
- **Page 11.** Exhibit 11’s black box grows to 5 lines. Everything still fits on the page.
- **Page 12.** Exhibit 12 gains three rows (Clearwater, Bloomberg and the Aladdin group row) and stays on one page. Finding 4 still fits below it. The Bloomberg row has "2026" alone on its second line.
- **Page 14.** Part 3 text and Exhibit 14 still fit together on one page, with about half an inch to spare. Part 3 paragraph 2 grew by one line. The only defect in Exhibit 14 is "Access scoped per API" touching its box border. The Copilot box’s third line, the 2-line band caption and the 3-line note all fit cleanly.
