# Fix panel: the devil's advocate (no changes)

## 1. Stance

v23 has been sent. It will be judged on its argument and how readable it is, not on whether it survives a 61-item line edit. Most of the list makes a persuasive leave-behind into a hedged audit memo. Several of its proposed wordings are worse than the original, a few rest on misreadings, and two (fixes 11 and 12) mean redrawing exhibits on the most tightly fitted pages. I concede three fixes, because each one makes a knowledgeable reader believe something false, or catch a plain mistake, in a way that damages the author. All three are same-length swaps inside one sentence or one cell. Even for these, I would fix the master file and not re-send it.

My test for conceding: either an outside reader comes away believing something false, or a BlackRock insider catches it at once, and in both cases it costs the author credibility. Being imprecise, incomplete or unhedged does not pass this test.

**Counts (61 fixes):** ACCEPT 0 · ACCEPT WITH CHANGE 3 · DEFER 5 · REJECT 53. I also REJECT the evolved thesis for the document and keep it for the interview.

DEFER means: make it only if the three concessions are being made anyway, and only if it causes no reflow.

## 2. Verdicts

### The evolved thesis: REJECT for v24, keep it for the conversation
- **v23's thesis is better sourced than the evolved one.** "Same controls" rests on things printed in the public specifications: OAuth scopes, runCompliance by default, whatIf. "The same governed tools Copilot calls, under the same permissions" rests on a conference talk about an internal registry, plus an MCP route the author admits is inference. That puts the inference on the cover.
- **It undercuts itself.** Fix 33 argues that most of Copilot's roughly 2,000 tools probably do not use the 54 public APIs. The evolved thesis then proposes that clients call exactly those tools. That is a larger ask of BlackRock, not a safer claim.
- **It loses "act".** "Call" drops the read-versus-write contrast that the whole executive summary builds on.
- **A changed thesis on the cover of a re-sent document shows a visible reversal.** The same idea, presented in the interview as "how my thinking moved after I sent this", shows growth instead.
- **Concession 2 below removes the real conflict.** With Exhibit 15 row 2 fixed, the only remaining place that puts Copilot's guardrails onto client tools is gone. The cover then reads as API-level controls, which is true.

### Tier 1 (fixes 1 to 12)
| # | Verdict | Reason |
|---|---|---|
| 1 | REJECT | Keep the cover. "Could" plus "same controls" is defensible once row 2 is fixed (fix 10). Exhibit 14 already separates API controls from what Copilot adds. |
| 2 | **ACCEPT WITH CHANGE** | Concession. "Already runs its own business this way", where "this way" means letting AI tools act, is false: Valdez says autonomous agents are "hopefully next year". The listed three-sentence replacement adds a hedge ("answering, not acting") to the executive summary. Use a same-length swap instead (wording in section 3). |
| 3 | REJECT | p2 already names SimCorp and Clearwater in the next breath, and p12 adds Arcesium. No reader concludes Aladdin is alone. The replacement rewrites a paragraph to make the case for rivals. |
| 4 | REJECT | The sentence contrasts Aladdin with *data providers*. Arcesium sits with the system-of-record rivals in Exhibit 12. Aquata's MCP writes to data pipelines, not orders or compliance rules, so the contrast still holds. |
| 5 | REJECT | OrderAPI, TradeAPI, ComplianceRuleAssignment and EnrichedCapitalFlow all split read from write (I checked the specs). The claim holds exactly where the thesis needs it. "Most split" is pedantry, and the added p5 sentence risks reflow. |
| 6 | REJECT | v23 already says the caller can turn compliance off, and that whether this needs a separate permission is not public. Both remain true: a scope is not an Aladdin user permission. The four-sentence list of bypasses belongs in a security review, not a pitch. |
| 7 | DEFER (p9 box only) | p8 already says "I attribute" and gives the reason. The heading and p2 are the author's framing. Only the p9 box drops the hedge. If reopened: "In my reading, both of BlackRock's growth bets run through Studio." Reject the slide 33/35 and 10-K additions, which are new material on a full page. |
| 8 | REJECT | "Not published" is true. "Any client program, an AI agent included, can already call the APIs" is a *new* claim about what client licence terms allow, which nobody has checked. |
| 9 | REJECT | The posting is described accurately ("Forward Deploy Engineer posting for Aladdin Data that names MCP"). "Nearest public sign" is the author's judgment. The Garson "100%" exchange works better spoken in the interview than buried in a caption. |
| 10 | **ACCEPT WITH CHANGE** | Concession. This is the one place the report promises that client AI tools would run under "guardrails Copilot uses". They cannot, because a client brings its own model. A GTM reader would see a marketing claim that legal would strike. Use a shorter swap than the list's rewrite (section 3). |
| 11 | REJECT | Redrawing Exhibit 14 on page 12, the page with the strictest fit rule (Part 3 text plus Exhibit 14). The caption already says the left controls apply to API calls and the right ones are Copilot's. |
| 12 | REJECT | Redrawing Exhibit 3. It is marked "for illustrative purposes only". Layer diagrams are read loosely. |

### Tier 2 (fixes 13 to 21)
| # | Verdict | Reason |
|---|---|---|
| 13 | **ACCEPT WITH CHANGE** | Concession. "Explore what-if" mixes up Explore's what-if portfolio modelling with OrderAPI's whatIf flag because the two share a name. An insider spots this in the first walkthrough exhibit. Use a same-length cell, and also fix the caption (section 3). |
| 14 | DEFER | It is true that the webinar moderator said "MCP". But the list's wording repeats the sentence before it on p9 ("Aladdin has published no such route"). If reopened, *delete* "Its only public mention of MCP is a job posting 73." on p9 and the matching sentence in the Exhibit 12 note. Do not replace them. |
| 15 | DEFER | A real error about a rival, but low stakes. If reopened, change Arcesium's first-call cell from 0 to 1 and delete "and Arcesium" from the p14 sentence. Exhibit 17 prints no totals, so the list's "re-total" step does not apply. |
| 16 | REJECT | **The premise is wrong.** Aladdin is not one of the 11. It is the separate "for comparison" row. The 11 are the 10 rows plus State Street (Audit E confirms this), so "Ten of the 11" is correct. |
| 17 | REJECT | The reader has just read a full page and Exhibit 11 on Copilot. Nobody concludes Aladdin has no AI. |
| 18 | REJECT | The title says "open"; public docs and catalogs score 2 for the data group, and the text below names the FactSet and MSCI limits. |
| 19 | REJECT | Count versus list is invisible to the target reader. |
| 20 | REJECT | Library nuance in a tile. No reader is misled about anything that matters. |
| 21 | REJECT | Miller said "prior to... Data Cloud... we sent flat files... FTP", so "replaced" is a fair paraphrase. The quoted words are verbatim. |

### Tier 3 (fixes 22 to 42)
| # | Verdict | Reason |
|---|---|---|
| 22 | REJECT | The title already carries its own exception. The replacement ("read what follows") is vaguer. |
| 23 | REJECT | "No one" plus "Runs automatically" is clear. The replacement uses a semicolon to join two sentences. |
| 24 | REJECT | "Where" means where Studio exposes positions. The extra detail crowds a dense cell. |
| 25 | REJECT | **Misread.** The sentence describes what a buyer *wants to know*. It does not claim the tenders show building. |
| 26 | REJECT | 5 CFR 2635.702 binds US federal employees, not UK pension bodies, so the cited bar is misapplied. Row 3 already offers the SDK-contributor alternative. |
| 27 | REJECT | The custodian caveat is already in the caption. The vanished information-services line peaked at $6.5M ($0.33M in 2023), so it cannot explain the jump. The wording joins two sentences with a semicolon. |
| 28 | REJECT | Review states exist. "Writable in the request" is an engineering footnote. |
| 29 | REJECT | "Record who approved them" is exactly what the spec shows. It never claims an enforced gate. |
| 30 | REJECT | Exhibit 4 covers Studio Compute. Box text is not an exhaustive list. |
| 31 | REJECT | Adds a box on page 9, which risks reflow. Input guardrails already appear in Exhibit 14. The source date is in the caption and Sources. |
| 32 | REJECT | The two-sentence heading carries its own contrast, and the body explains it. |
| 33 | REJECT | v23 labels the inference ("So I infer"). The replacement adds a new, weaker inference ("most probably do not"), and the 54 are only the specs in public wheels, not the client catalog. It also joins two sentences with a semicolon. |
| 34 | REJECT | Each row reports the vendor's own claim with its source. Re-sourcing 11 rows is the biggest page-fit risk on page 10. |
| 35 | DEFER (date only) | Rescoring is judgment presented as correction. If sources are dated after the test date, fix the date, but the list never says what the right date is. |
| 36 | REJECT | "May compete... for certain uses" is already hedged. Exhibit 3 already shows Data Cloud on Snowflake. |
| 37 | REJECT | Exhibit redraw. |
| 38 | REJECT | Tile nuance. The Governance quote is BlackRock's own wording. |
| 39 | REJECT | The p6 text already says "should be available". |
| 40 | REJECT | "Lists eight products" already reads as a selection. |
| 41 | REJECT | The column header is the author's framing of the funnel. The new cell is long and joins two sentences with a semicolon. |
| 42 | REJECT | The window is stated exactly, "Q1 2020 to Q2 2026", and the finding holds (0). |

### Tier 4 (fixes 43 to 61)
| # | Verdict | Reason |
|---|---|---|
| 43 | REJECT | The counts are as marked in the specs. |
| 44 | REJECT | Notification specs are not business events. The reader is not misled. |
| 45 | REJECT | "Fastest" is arithmetically true. Audit D rates p8 correct. |
| 46 | REJECT | "Add-on" is the 10-K and release framing (Exhibit 1, source 21). |
| 47 | REJECT | "Aladdin web page as the supplier's address" already says it is a web address. |
| 48 | REJECT | "About the same" understates. It is not false. The row never says Aladdin. |
| 49 | DEFER | Register only, no reflow. Make it if reopening. |
| 50 | REJECT | p3 already says the rise "includes Preqin". The list itself marks this optional. |
| 51 | REJECT | The report attributes the line to the posting, which says it. |
| 52 | REJECT | The daily tests check the guardrail behaviour ("never investment advice"). Close enough. |
| 53 | REJECT | Stylistic. |
| 54 | REJECT | Stylistic. |
| 55 | REJECT | p12 already says the poll "gives no sample size". |
| 56 | REJECT | Buyers ask about Databricks connectors (the Schafer quote). Row 1 is a proposal. |
| 57 | REJECT | "In the PyPI add-on packages" already says where. |
| 58 | REJECT | The note already says "I read Studio Compute sessions as the SDK's name for Aladdin Compute". |
| 59 | REJECT | Qualifiers on rivals' rows add length to page 10 for no change in meaning. |
| 60 | REJECT | The list marks it optional. |
| 61 | REJECT | The list marks it optional. |

## 3. Fixes the list gets wrong

**Wrong premise or misreading**
- **16:** Aladdin is outside the 11, so the title is correct as printed.
- **25:** The sentence states what a buyer wants to know. It is not an evidential claim.
- **26:** The cited federal ethics rule does not reach UK pension bodies.
- **15:** "Re-total" does not apply, because Exhibit 17 shows no totals.

**Proposed wording that adds a new unsupported claim**
- **8:** "Any client program, an AI agent included, can already call the APIs." Licence terms for automated agents are not public.
- **33:** "Most probably do not." The 54 public specs are not the full client catalog.
- **Evolved thesis:** moves an admitted inference (the MCP route) and an internal registry onto the cover.

**Proposed wording that breaks the writing rules (semicolons joining sentences)**
- 23 ("The engine runs it; a named team resolves violations.")
- 27 ("...what the payments cover; JPMorgan is also a custodian...")
- 33 ("...is not public; with about 2,000 tools...")
- 38 ("...notebooks and samples; the portal sits behind...")
- 41 ("...but no channels; the maintainers merged...")
- **2:** "Public sources show it answering, not acting" contrasts with the old claim, against the rule that new text never corrects or contrasts with the old wording.

**Proposed wording that is redundant or incomplete**
- **14:** The replacement repeats "Aladdin has published no such route" from the sentence before it. Delete the sentence instead.
- **13:** It drops source 27 from the cell but not from the Exhibit 2 caption. "Aladdin Dashboard (Order Monitor)" is also about twice as long as the current cell and may wrap the Where row.
- **35:** "Fix the date" gives no date.

**Exact wording for my three concessions (each about the same length, no reflow expected)**
- **Fix 2, p2.** Replace "BlackRock's advantage is that it already runs its own business this way." with:
  > "BlackRock's advantage is that its own AI already runs on Aladdin's production APIs."

  The next two sentences stay as they are, and source 9 already covers this.
- **Fix 10, Exhibit 15 row 2.** Replace "under the same permissions, compliance checks and guardrails Copilot uses." with:
  > "under the same permissions and compliance checks as BlackRock's own business."
- **Fix 13, Exhibit 2, Order "Where".** Replace "Explore what-if 27" with:
  > "Order Monitor 6"

  This is the screen the OrderAPI spec names, and it is the same length. In the Exhibit 2 caption, delete "the Explore training recording 27;". Source 27 stays in use in the Exhibit 3 note, so the source register is unaffected.

## 4. Missing from the list

- **The fix list never asks whether to re-send.** It tiers fixes by type of error, not by how likely a reader is to notice or how much it would cost the author. By that measure, only about three items matter.
- **Delivery options.** One is to correct the master and not re-send it. Another is to raise one or two points out loud in the interview ("one thing I would sharpen since sending this"). The list considers neither, and both avoid signalling insecurity.
- **No regression plan.** The list has no page-fit check or diff review for the 19-page and part-start rules, and no check that each source cited in a cell is still cited somewhere after an edit (see fix 13's caption).
- **The cover date and version.** A v24 dated after October 19 sits oddly beside unchanged findings. If made, keep "As of October 19, 2026".
- **The unused evidence (62 to 69) is better used in the interview.** Garson's "100%", the registry permissions and the PermissionAPI are strong spoken points. Adding them to v24 means new text on full pages.

## 5. Top 5 recommendations

1. **Do not re-send.** v23 stands. A revision two days after sending, with a changed thesis, reads as insecurity, and the target reader will not have found most of these issues.
2. **Fix the master silently, with three same-length swaps:** fix 2 (p2 "runs its own business this way"), fix 10 (Exhibit 15 row 2 guardrails) and fix 13 (Exhibit 2 "Explore what-if"). Hand over this version only if a copy is asked for again.
3. **Make DEFER items only alongside those three, and only with zero reflow:** fix 14 (delete, not replace), 15 (one cell plus "and Arcesium"), 49 (register), the p9-box hedge from fix 7, and fix 35's date once the right date is known.
4. **Take the evolved thesis to the interview, not the cover.** Use it as the next step in the argument, with Garson's "we are hearing that from our clients" and the registry permissions as the evidence.
5. **Reject the redraws (fixes 11, 12 and 37) and every semicolon or hedge rewording.** They carry the highest risk of new errors and page breakage for the least gain to the reader.
