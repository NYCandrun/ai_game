# Senior editor's audit of the v23 fix list

Role: senior editor. I cover the writing rules, consistency across the document, page layout, and the connected set of Exhibits 3, 4 and 14.

This report applies the three corrections the author sent while I worked:
- **Explicit rule.** The new rule, "say things explicitly", is applied to every wording below.
- **Page fit.** The 19-page cap and the fixed Part page numbers are dropped. Page fit is now judged only by clean layout: no large gaps, no near-empty pages, no badly split exhibits, and cover page references that match where each Part starts.
- **Exhibits 3, 4 and 14** are treated as one set (section 7).

**How I measured layout.** Every layout claim below comes from a test render. I re-rendered the v23 HTML with the same headless Chromium. The render matches the sent PDF exactly: 19 pages, with identical text on pages 2, 6, 12 and 14. I then applied candidate wordings to scratch copies only.
- Scratch copies and their PDFs are in `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fixpanel/test/`.
- `editor2.html` holds Tiers 1 and 2 in my wording.
- `L4_150.html` adds the explicit-rule wording and an Exhibit 14 drawn 150pt high.
- `list.html` holds the fix list's literal wording.
- The scripts are in `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fixpanel/tools/`.
- The report itself was not touched.

## 1. Stance

The list's facts are mostly right. Its proposed wordings are not ready to paste:
- **Rule breaks.** Five wordings join two sentences with a semicolon: fixes 23, 27, 33, 38 and 41.
- **Allusive wording.** About a dozen hint at a point instead of stating it ("these APIs", "this way", "most probably", "if offered", "governed").
- **Internal contradictions.** Fixes 2 and 3 say Copilot runs on "these" public APIs and on the "controls it sells". Fix 33 says most Copilot tools probably do not use the public APIs.
- **Gaps in coverage.** Many fixes name one location when the same claim appears on two to six pages.

Layout breaks in exactly three places, and each fails visibly:
- On page 3, Exhibit 2 jumps and leaves about 21 blank lines.
- On pages 8 and 9, Part 2 cascades.
- On page 14, Part 4 spills onto a page that is about 90% empty.

All three can be avoided with the tested wordings below. None of them needs a fix to be dropped.

## 2. Verdicts

Counts: **20 ACCEPT, 41 ACCEPT WITH CHANGE, 0 REJECT, 0 DEFER.** The evolved thesis is ACCEPT WITH CHANGE.

"Tested" means I rendered the wording and the page still lays out cleanly.

### Evolved thesis: ACCEPT WITH CHANGE

The author's evolved thesis reads: "Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls."

- **Problem.** "Governed" and "API controls" allude to the controls without naming them.
- **Short form, for the cover, the page 2 lede, page 12 and Exhibit 15 row 2:** "Clients' AI tools could call the same Aladdin tools Copilot calls, under the same permissions and compliance checks."
- **Long form, once on page 12:** "A client's AI tools could share the controls that run on BlackRock's servers: tool permissions, API scopes, Aladdin user permissions and compliance on orders. Copilot's guardrails, planning and AI-graded tests would stay inside Copilot, because the client brings its own model. One route, and my inference, would be an MCP server onto Copilot's registry."

### Tier 1

**Fix 1: ACCEPT WITH CHANGE.**
- Use the thesis wording above.
- The list names only the cover, page 2 and page 12. The same claim appears in 11 places (section 4, row A). Every one must change.

**Fix 2: ACCEPT WITH CHANGE.**
- What is wrong with the list's wording:
  - "Runs AI on these APIs" points back to the public APIs. That contradicts fix 33.
  - "Most mapped" has no source. The talk names two onboarding paths and gives no proportion.
  - "Answering, not acting" implies a contrast instead of stating it.
- Merge with fix 3 into one page 2 paragraph: "Rivals have begun letting AI agents act: Arcesium through an MCP server, Clearwater and SimCorp inside their platforms 7, 8. BlackRock already runs AI on Aladdin's production APIs. Copilot answers questions for staff and clients by calling about two thousand registered tools and agents. Each tool maps to an Aladdin API already in production, and each user sees only the tools set for their environment, user group and app 9. No public source shows Copilot posting orders or changing data."
- No superscript for Arcesium on page 2. Exhibit 12 sources it. Citing source 75 on page 2 would break the first-cited numbering of the register.

**Fix 3: ACCEPT WITH CHANGE.**
- "BlackRock already runs AI over the production APIs and controls it sells" is wrong. Copilot's guardrails are not sold. It also duplicates fix 2.
- Page 2: use the merged paragraph above.
- Page 12: "Rivals have begun letting AI agents act, Arcesium through an MCP server and Clearwater and SimCorp inside their platforms 7, 8, 75. BlackRock can point to its own AI assistant."
- That second sentence replaces "What BlackRock can show is its own use", which only alludes.

**Fix 4: ACCEPT WITH CHANGE.**
- "Some let them act" is wrong for data providers. Arcesium is grouped as a system-of-record rival, and fix 3 now covers it.
- Use: "Many data providers now let outside AI tools read their data 2–5. Aladdin's APIs can also write. They post orders and assign compliance rules to portfolios."

**Fix 5: ACCEPT WITH CHANGE.**
- Page 2: "Each API has its own OAuth scopes, and most split read from write."
- Page 5: "With OAuth, access is granted per API. A typical OAuth scope reads … 6. Aladdin user permissions add limits by function, action and portfolio 6."
- Tested: page 5 is unchanged.

**Fix 6: ACCEPT WITH CHANGE.**
- "Trades posted directly" is vague. Write "Trades posted through the TradeAPI have no compliance setting."
- Page 2 takes the full text, which is tested.
- Page 12 and the Exhibit 14 box take a short form: "Runs by default. The caller can turn it off with the scope it uses to post."
- Also apply to the Exhibit 3 side panel and Exhibit 15 row 4. The list misses both.

**Fix 7: ACCEPT WITH CHANGE.**
- This is the tested wording. The list's version adds about 2 lines on page 8 and cascades Part 2: page 8 is left with 11 blank lines, page 9 with 26, and Part 2 runs one page longer.
- Page 8 heading: "2. BlackRock tells investors it is growing Aladdin as a platform, but rarely names Studio to them".
- Page 8 text: "BlackRock tells investors it is growing Aladdin as a platform, without naming Studio. At its 2025 Investor Day, BlackRock estimated that API calls across BlackRock and Aladdin would grow 17 times by 2030 11. The slide does not say who makes these calls. Another slide lists "Aladdin as a platform" among Aladdin's growth drivers 11."
- Page 9 box: "BlackRock tells investors it is growing Aladdin as a platform and "empowering clients with data and APIs" 11, 12. Studio is how clients reach those APIs and that data 1. Its new eFront and Preqin private-markets data is going into Data Cloud, which is part of Studio 22."
- Page 12: "It estimates that API calls across BlackRock and Aladdin will grow 17x by 2030 11."
- Page 2: as the list proposes.
- Add slide 33 to register entry 11.
- I dropped the list's "They include BlackRock's own applications and Copilot". It is an unlabelled inference.

**Fix 8: ACCEPT WITH CHANGE.**
- Use the report's own term, "AI tools", not "AI agent".
- "Support, guidance" is vague. Use: "A client's AI tools can already call the APIs with credentials registered in Studio 29. BlackRock has published no guide or connector for them."
- The Exhibit 14 tile reads: "Can call the APIs with Studio credentials today. No published guide or connector."

**Fix 9: ACCEPT WITH CHANGE.**
- Exact wording for page 12: "When Microsoft's Adrian Crockett said clients might want BlackRock's plug-ins in their own copilots, BlackRock's head of product for AI replied, "we are hearing that from our clients" 71."
- Garson's "100%" answers a different Crockett line, about clients using BlackRock's orchestrator. Do not attach it to the plug-ins point.
- Keep the job posting on page 9, accurately described (fix 14 wording). That keeps source 73 cited, in order. Dropping it everywhere orphans 73, and leaving it only in Exhibit 12 puts 74 before 73.

**Fix 10: ACCEPT WITH CHANGE.**
- "A governed route" turns a piece of marketing work into a product.
- Use: "A page on how a client's own AI tools could call the same Aladdin tools Copilot calls, under the same permissions and compliance checks, with a person approving before any order posts." Tested.

**Fix 11: ACCEPT WITH CHANGE.**
- Redraw Exhibit 14 using the shared vocabulary in section 7.
- New title, on one line: "What a client's AI tools could share with Copilot, and what would stay inside Copilot."
- Draw it **no more than 150pt high** (today it is 183pt). Section 3 explains why.
- Update the Exhibit 14 aria-label, which still mentions the job posting.

**Fix 12: ACCEPT.** Apply the shared vocabulary in section 7.

### Tier 2

**Fix 13: ACCEPT WITH CHANGE.**
- Use "Order Monitor 6". This is tested.
- "Aladdin Dashboard (Order Monitor)", and even "Dashboard Order Monitor", wraps the cell. Exhibit 2 then jumps to page 4 and page 3 is left with 21 blank lines.
- Also cut "the Explore training recording 27" from the Exhibit 2 source line.
- Source 27 then first appears after source 28. Swap the numbers of the two register entries.

**Fix 14: ACCEPT WITH CHANGE.** Fold it into the page 9 paragraph. That also removes the allusive "Aladdin has published no such route":
- "Eight of the 11 offer a connector or an MCP (Model Context Protocol) server, a standard way for outside AI tools to connect."
- "BlackRock has published no MCP server or connector for Aladdin."
- "MCP comes up only in passing, in a remark on BlackRock's Build vs. Buy webinar and in a posting for BlackRock's internal data platform 10, 73."

**Fix 15: ACCEPT.**
- Arcesium's first call scores 1. Its trial stays 1, because a requested trial is a 1 under the legend. Drop the list's "or 2".
- Cut Arcesium from the page 14 list. Tested.

**Fix 16: ACCEPT WITH CHANGE.**
- State the count, which I verified at 8: Arcesium, Bloomberg, FactSet, LSEG, MSCI, S&P, Snowflake and Databricks.
- Title: "Eight of the 11 providers I compared offer outside AI tools a connector or MCP server. Aladdin, SimCorp and Clearwater offer AI inside their platforms."
- Tested: it costs 1 line on page 10, which has room.
- The page 9 paragraph must match (fix 14). The list misses this.

**Fix 17: ACCEPT WITH CHANGE.**
- Wording as proposed.
- Change the Source cell to the Copilot page (23).
- Delete "Aladdin has only a job posting that mentions MCP 73" from the Exhibit 12 note.

**Fix 18: ACCEPT WITH CHANGE.**
- The list's title wraps to 2 lines. Part 4 then spills onto a page with 51 blank lines.
- Tested one-line title: "Snowflake and Databricks are self-serve. Most others open fully only to clients."

**Fix 19: ACCEPT WITH CHANGE.**
- The list's two sentences wrap the narrow cell, with the same page 3 failure as fix 13.
- Tested: "Counts exceptions. Another call lists them 6."

**Fix 20: ACCEPT.** Tested.

**Fix 21: ACCEPT WITH CHANGE.**
- "Used before" alludes. Quote Miller verbatim instead: Data Cloud is "much simpler" than "flat files ... FTP". Tested.
- Also change the Exhibit 7 note to "Miller, in Exhibit 6, speaks only about Data Cloud, so he is not shown." The list misses this.

### Tier 3

**Fix 22: ACCEPT WITH CHANGE.**
- "Read what follows" is vague. Use: "The public APIs post orders and trades, and read later steps except positions."
- The list's length is tested. Re-test this wording.

**Fix 23: ACCEPT WITH CHANGE.**
- The list's wording has a semicolon joining two sentences, and it overflows page 3.
- Tested: Who: "The engine, then a named team". API: "OrderAPI (runCompliance), ViolationAPI to resolve".

**Fix 24: ACCEPT WITH CHANGE.**
- "(A copy of the IBOR)" is unsourced. Keep "Data Cloud".
- Tested detail: "No holdings API. Collateral and cash can be read 6."

**Fix 25: ACCEPT.**

**Fix 26: ACCEPT WITH CHANGE.** "If they use Studio" is a hedge.
- Exhibit 15 row 3: "One client story, cleared for the Studio page and the RFP answer, from a client whose engineers have contributed to the SDK."
- Page 8: "Firms whose filings or tenders already name BlackRock are natural subjects for an Aladdin case study. For Studio, the natural first subject is a client whose engineers have contributed to the SDK 55."

**Fix 27: ACCEPT WITH CHANGE.**
- The list's wording has a semicolon joining sentences.
- Use: "They disclose the payments because BlackRock owns more than 5% of JPMorgan, and do not say what they cover. … The grey 2016 bar is a payment for integration services. The figures in the text start with 2017. JPMorgan is also a custodian, so some payments may be for custody connections rather than a client licence."
- The shorter test version fitted page 7. The custodian clause was not tested. If it wraps, cut "The report is not a JPMorgan or BlackRock document", because the register's T grade already says so. Otherwise Exhibit 9 jumps.

**Fix 28: ACCEPT.**

**Fix 29: ACCEPT.** Fold it into the Exhibit 14 redraw under the label "Aladdin user permissions".

**Fix 30: ACCEPT WITH CHANGE.** Use "Run in the client's environment or in Aladdin Compute" (section 7 vocabulary).

**Fix 31: ACCEPT WITH CHANGE.** Tested: page 9 is fine and Exhibit 12 stays on page 10.
- Title: "Copilot answers a question by shortlisting from about two thousand tools and agents, then calling them in a loop."
- Last box: "One answer. Copilot "will not give investment advice" 23".
- Drop the unsourced "most of them production Aladdin APIs".

**Fix 32: ACCEPT.** Tested.

**Fix 33: ACCEPT WITH CHANGE.**
- The list's wording has a semicolon and the hedge "most probably".
- Use: "Studio's public APIs run on Aladdin Graph, BlackRock's firm-wide runtime 39, and some back BlackRock's own screens, such as Risk Radar 6. Copilot has about two thousand tools and agents, and the public specifications hold 301 operations. So most of Copilot's tools must call APIs that are not public."
- The length is tested.

**Fix 34: ACCEPT WITH CHANGE.** The list says "reword" but gives no wording. Use:
- SimCorp: "Agent Launchpad, announced in April 2026, is to let clients use prebuilt agents and build their own, with controlled access to SimCorp One data. A portfolio management agent is already available."
- Clearwater: "CWAN GenAI, deployed in November 2025, runs more than 800 agents inside Clearwater's platform, built by clients and Clearwater teams."
- Arcesium: "Aquata's MCP server lets outside AI tools read client data, deploy connectors, build pipelines and create quality rules."
- FactSet: "FactSet has run an MCP server for its data since December 2025 and calls it "the industry's first production-grade" MCP server."
- Bloomberg: move it to the data group. "Bloomberg launched an MCP server for its licensed data in September 2026."

**Fix 35: ACCEPT WITH CHANGE.**
- Adding the note on top of the existing legend overflows page 14.
- Replace the legend instead. Tested, with fix 36 and the new date: "In every column, 0 means not reachable without a client relationship. AI connector: 2 means one outside AI tools can use, such as an MCP server, 1 one announced or in limited release, and 0 none. Most connectors are for licensed clients. Call to action: 2 means a developer can sign up alone, 1 a trial or access request, and 0 sales contact only."
- Date: "October 8 to 20, 2026".

**Fix 36: ACCEPT WITH CHANGE.**
- Replace the sentence instead of adding one. Tested: "Exhibit 17 puts Studio beside 10 platforms, with Snowflake and Databricks as benchmarks for developer access."
- That Data Cloud runs on Snowflake is already stated in Exhibits 1 and 4.

**Fix 37: ACCEPT.** Apply the section 7 vocabulary.

**Fix 38: ACCEPT WITH CHANGE.** The list's Admin Center wording misreads the source, and its Portal wording has a semicolon and contradicts its own finding.
- Admin Center: "The screen for managing Data Cloud datasets. Four of its ten API operations are for BlackRock's internal use."
- Portal: "API guides, behind a client login 44".
- Governance: ""Access management and usage monitoring" 45".

**Fix 39: ACCEPT WITH CHANGE.** Tested: "Aims for every transaction "via an event, via an API" and Data Cloud "within 15 minutes of latency"".

**Fix 40: ACCEPT WITH CHANGE.**
- The list's note overflows page 3 (tested).
- Tested title instead: "Of eight Aladdin products shown, Studio is the one for people who write code."
- The "four platforms and nine solutions" fact can go on page 5 or page 2, which have room.

**Fix 41: ACCEPT WITH CHANGE.**
- The list's Get help wording has a semicolon.
- Change "qualification" in all six places: the Exhibit 16 title, the header on pages 13 and 14, the note, and the page 13 text.
- Get help: "SUPPORT.md lists no support channels. A BlackRock engineer merged a client engineer's changes."
- This cell is what tips page 14 over. Shorten the same row's Receipt cell, for example to "Two SDK changes 56, 57; Studio and APIs pages 14, 30". If page 14 still overflows, see section 3.

**Fix 42: ACCEPT WITH CHANGE.** Apply it in all five places:
- page 8 text;
- the Exhibit 10 title;
- the Exhibit 10 note, where "six and a half years" becomes "nearly seven years";
- register entry 64.

Audit D checked the Q3 2026 call on Bullfincher and Earnings Whispers, because roic.ai blocks access. Name the source that was actually used. All six counts stay the same.

**Fix 43: ACCEPT.**

**Fix 44: ACCEPT.** Apply it to the Exhibit 4 events tile and the Exhibit 2 note.

**Fix 45: ACCEPT WITH CHANGE.** Fix 7 makes this sentence unnecessary, so cut it.

**Fixes 46 to 49: ACCEPT.**

**Fix 50: ACCEPT WITH CHANGE.**
- The list's added clause overflows page 3.
- Tested: "Its 24 percent rise includes Preqin, bought in 2025, and was about 10 percent without it 12."

**Fix 51: ACCEPT WITH CHANGE.**
- There is one posting, not several.
- Use: "A 2026 BlackRock technology job posting says the firm builds for itself and over 200 institutions 39."

**Fix 52: ACCEPT.** The sentence moves into the Exhibit 14 Copilot-only row.

**Fix 53: ACCEPT WITH CHANGE.**
- Change the page 6 text too: "Only Woodhead lists all three parts in one definition 1."
- Title: "…and only Woodhead lists all three in one definition".
- Both are tested.

**Fixes 54 and 55: ACCEPT.** For fix 55, also change the page 10 sentence to "chose compliance reporting, from four options".

**Fix 56: ACCEPT WITH CHANGE.** "If offered" is a hedge. Use: "It covers the Snowflake connection for Data Cloud, and how a client's own AI tools can call the APIs today."

**Fixes 57 and 58: ACCEPT.**

**Fix 59: ACCEPT WITH CHANGE.**
- MSCI: "MSCI, mainly an index provider, offers "AI connectors" to its proprietary data".
- S&P: "S&P Global's AI Data Portal, reachable "via any MCP-enabled AI application", added Credit Ratings in September 2026".
- Databricks: "…managed MCP servers, some in beta".
- Exhibit 12 note: "State Street has discussed an Alpha copilot in beta. I found no AI feature it has released to clients."

**Fix 60: ACCEPT.**

**Fix 61: ACCEPT WITH CHANGE.** Avoid the semicolon: "Spaces: named alongside Projects, not described publicly."

## 3. Page layout: net line change and where pages fail

**Tiers 1 and 2 in my wording (`editor2.html`) render cleanly. Every Part starts where it does today and the cover references stay correct. The list's literal wording (`list.html`) does not.** With the list's wording:
- Page 3 is left with 21 blank lines, Part 1 runs to page 7, Part 3 starts on page 13 with 22 blank lines, and Part 4 ends on a page with 23 blank lines.
- The document grows to 21 pages and every cover reference is wrong.

The table shows blank space at the foot of each page, in lines of 12pt.

| Page | v23 blank lines | Tier 1–2 change (my wording) | Risk |
|---|---|---|---|
| 2 | 16.3 | −3.5 (−4.8 with the explicit thesis) | None |
| 3 | 0.4 | 0 | **High.** Any extra line in Exhibit 1, Exhibit 2 or the lede pushes Exhibit 2 to page 4 and leaves about 21 blank lines (fixes 13, 19, 22–24, 40, 50). |
| 4 | 5.8 | about 0; the redraws of fixes 12 and 37 were not tested | Low. There is room for about 5 lines. |
| 5 | 9.8 | 0 | Low. If page 5 text shrinks, the Woodhead quote moves up, which is good. |
| 6 | 0.3 | 0 | **High.** Fixes 21, 39 and 53 fit only in the tested wordings. |
| 7 | 0.7 | 0 | **High.** Any extra line pushes Exhibit 9 and cascades Part 2 (fix 27). |
| 8 | 0.8 | +1.0 freed | **High** with the list's fix 7, which cascades Part 2. |
| 9 | 4.1 | 0 | Medium. Fixes 31 and 33 together use about 2 lines (tested). |
| 10 | 4.5 | −0.3 | Low |
| 11 | 20.0 | 0 | This end-of-Part gap already exists in v23. |
| 12 | 1.8 | 0 in my wording; +2 with the explicit thesis and the poll caveat restored | **High.** See below. |
| 13 | 0.5 | 0 | **High.** Exhibit 15 rows must stay the same length (fixes 10, 26, 56). |
| 14 | 0.8 | 0 with the one-line fix 18 title | **High.** A two-line Exhibit 17 title, or fix 41, spills about 5 lines onto a page with 51 blank lines. |

**Page 12.**
- In my first wording page 12 holds, because the compliance detail moves into Exhibit 14, the Exhibit 14 title goes to one line and its note gets shorter.
- With the explicit thesis sentence and the poll caveat kept ("The poll did not ask…", which should stay), the text grows about 2 lines. Exhibit 14 then jumps and page 12 is left with 21.7 blank lines.
- Moving Exhibit 14 mid-chapter, or starting Part 4 on a new page, made it worse in testing: gaps of 14 to 30 lines.
- **The fix that works (tested in `L4_150.html`) is to draw the redrawn Exhibit 14 no more than 150pt high.** It fits: two bands of tiles, a shared row and a Copilot-only row, in a viewBox of about 1280×380.

**Page 14.**
- Part 4 has no room. Use the replacement legend (fixes 35 and 36, tested) and the one-line fix 18 title.
- For fix 41, shorten the same row's Receipt cell.
- If Tier 3 still adds a line, cut the Exhibit 16 Receipt column to source numbers only. Do not start Part 4 on a fresh page: in testing that leaves 30 blank lines on page 13.

## 4. Where each claim appears in v23 (pdftotext)

| Claim | Pages and places | What the list misses |
|---|---|---|
| A. Thesis ("same controls" / "this way") | p1 cover; p2 lede; p2 "would work under the same controls"; p2 "already runs its own business this way"; p2 "under BlackRock's own controls"; p12 ¶1 (twice); p12 ¶2 "controls BlackRock already relies on"; p12 ¶5 "open its controls"; Exhibit 14 title; Exhibit 14 note "the model … could follow"; p13 Exhibit 15 row 2 | All except the cover, the lede and page 12 ¶1 |
| B. "Each Copilot tool matches/maps" | p2, p4 Exhibit 3, p12 text, p12 Exhibit 14 | Exhibit 3 and Exhibit 14 |
| C. Compliance by default / turn it off | p2, p3 Exhibit 2, p4 Exhibit 3, p5, p12 text, p12 Exhibit 14, p13 Exhibit 15 row 4 | Exhibit 3, Exhibit 14 box, Exhibit 15 row 4 |
| D. 17x | p2, p8, p9 box, p12, p16 register entry 11 | Page 12 wording, register entry 11 |
| E. Per API / per action | p2, p4 Exhibit 3, p5, p12 Exhibit 14 | None (Exhibits 3 and 14 are already correct) |
| F. "Would connect is not public" / job posting / MCP | p9, p10 Exhibit 12 row and note, p12 text, p12 Exhibit 14 title, tile and note, p13 Exhibit 15 row 1 | Exhibit 15 row 1, Exhibit 14 title |
| G. 26 calls / Q2 2026 | p8 text, Exhibit 10 title, Exhibit 10 note (twice), p18 register entry 64 | All except the Exhibit 10 window |
| H. "Fastest" / "four usage measures" | p8 (twice), p9 box | — |
| I. Miller "replaced" | p6 Exhibit 6, p6 Exhibit 7 note | Exhibit 7 note |
| J. "Only Woodhead names…" | p6 text, Exhibit 7 title | Page 6 text |
| K. "Qualification" | p13 text, Exhibit 16 title and header, p14 header and note | All except the column |
| L. No event specification | p3 Exhibit 2 note, p4 Exhibit 4 tile | — |
| M. Studio Compute / Aladdin Compute | p4 (tile, workspace, note), p14 Exhibit 16 and SDK paragraph, Exhibit 14 (fix 30) | Fix 30 |
| N. Pension fund case study | p8, p13 Exhibit 15 row 3 | — |

The HTML aria-labels of Exhibits 3, 11 and 14 repeat claims A, B and F. They need the same edits.

## 5. Rule breaks, in the list and in v23

**Semicolons joining two sentences.**
- In the list: fixes 23, 27, 33, 38 and 41.
- Already in v23:
  - p2 method box: "AI agents gathered them; I checked…"
  - p7 Exhibit 8 note: "…integration services; the figures…" (fix 27 touches this one)
  - p10: "…led at 42 percent; cost and speed…"
  - p13 Exhibit 15 row 2: "The page is published; RFPs…"

**Em-dashes.** Two quote attributions in v23 use one: p6 "— Dave Woodhead" and p11 "— Clark Schafer". Replace each with a plain attribution line.

**"Suggest".** It appears in all four "What this finding suggests about direction" boxes. The rule bans "suggested", so this is a judgement call. If the rule is meant to cover the verb, use "What this finding means for direction".

**Allusion (the new rule).** In the list:
- "governed" and "API controls" (fix 1)
- "these APIs" and "answering, not acting" (fix 2)
- "controls it sells" (fix 3)
- "some let them act" (fix 4)
- "a governed route" (fix 10)
- "most" (fix 16)
- "used before" (fix 21)
- "read what follows" (fix 22)
- "a copy of the IBOR" (fix 24)
- "if they use Studio" (fix 26)
- "JPMorgan is also a custodian that connects" (fix 27)
- "most probably do not" (fix 33)
- "partly run by BlackRock" (fix 38)
- "headings but no channels" (fix 41)
- "if offered" (fix 56)

In v23, in sentences a fix already touches:
- "this way" (p2 and p12)
- "BlackRock has said parts of this" (p12; use "BlackRock has made two related claims")
- "What BlackRock can show is its own use" (p12)
- "open its controls" (p12)
- "no such route" (p9)
- "the model … could follow" (Exhibit 14 note)

The replacements are in section 2.

## 6. Missing from the list

- **Register numbering.** Order of first citation breaks in two places:
  - fix 13 puts source 28 before 27;
  - removing the posting (fix 9) would orphan 73 or put 74 before 73.
  - Add slide 33 to entry 11, and name the Q3 2026 transcript source (fix 42).
- **The Exhibit 7 note** repeats the Miller error.
- **The page 9 paragraph's counts** ("Six…", "Four…", "Many of the 11") must match the new Exhibit 12 title.
- **Exhibit 15 row 1** must match fix 8.
- **The existing semicolons and em-dashes** listed in section 5.
- **The Exhibit 3, 11 and 14 aria-labels.**
- **Exhibits 3, 4 and 14 need one shared vocabulary.** See section 7.

## 7. Exhibits 3, 4 and 14 as one set

### Terms and styles that differ today

| Thing | Exhibit 3 (p4) | Exhibit 4 (p4) | Exhibit 14 (p12) |
|---|---|---|---|
| Studio | Yellow row, "Aladdin Studio: the developer and data layer" | Yellow frame, "What Studio offers" | No Studio layer. Yellow is used for the client's own tiles, under "A client's use · through Studio". |
| BlackRock apps | White tile, "About 100 applications such as Explore, Dashboard and Risk Radar", row "BlackRock's applications" | — | Pink tile, "About 100 BlackRock applications", band "BlackRock's own use" |
| Copilot | Pink, "Aladdin Copilot, inside them", "matches" | — | Pink, "Copilot", "maps" |
| APIs | Inside the black shared-services row, "reached through the 11 public API domains" | A tile inside Studio, "APIs" | A grey band of its own, "Aladdin's APIs", under BlackRock and clients alike |
| Data Cloud | Named in "Outside inputs" ("loaded into Data Cloud") | A tile inside Studio | Inside the API band ("Each client reads its own Data Cloud"), although it is not an API |
| ADX | "Data eXchange", in outside inputs | A tile inside Studio, "Aladdin Data eXchange (ADX)" | "the Data eXchange", in the note |
| Compute | — | Tile "Aladdin Compute" and workspace "Studio Compute sessions" | (Fix 30) "Studio Compute" |
| ATX / Excel | "Excel users building reports" in Who builds | ATX tile | Absent |
| Builders | Who builds: "Client engineers", "Code-curious portfolio managers", "Data analysts", "Excel users" | — | "Its engineers", "Its applications", "Its AI tools" |
| Credentials | — | "API tokens and OAuth applications" | "the client's credentials" (fix 8 adds "Studio-registered credentials") |
| Controls | Grey side panel "Controls in the API specifications": "Access set per API", "Compliance by default on orders" | Tile "Governance" | "Access set per API", "Approvals on record", "Compliance by default", plus "What Copilot adds for AI" in blue-grey |
| Visual key | Dashed outline = outside data. Black = shared services. Note: "Every box is named in the sources." | Yellow frame = Studio | Pink = BlackRock's own use. Hatched = not in the public record. Grey band = APIs. Legend covers boxes only. |

### Recommended shared vocabulary and key

**Colours.**
- Yellow means **Aladdin Studio** only, in all three exhibits.
- Pink means **Aladdin Copilot** only. BlackRock's applications are white.
- Black means **Aladdin's shared services and APIs** ("Aladdin APIs, on Aladdin Graph").
- A grey panel means **controls**.
- Hatched tiles with dashed arrows mean **proposed / my inference**.
- Outside data takes a thin grey outline, not dashed, so it does not clash with "proposed".
- One legend for all three exhibits, covering both boxes and arrows.

**Structure.** Exhibit 3 (fix 12) has one row, "Built by BlackRock" (BlackRock applications + Aladdin Copilot), beside "Aladdin Studio, built on by clients".
- **Exhibit 4** zooms into that yellow Studio box. Use the same title word ("Aladdin Studio") and the same yellow frame.
- **Exhibit 14** repeats Exhibit 3's row and shared row, then adds two rows. One is the shared controls: tool permissions, API scopes, Aladdin user permissions, compliance on orders. The other is "Stays inside Copilot": input guardrails, output guardrails and planning, AI-graded tests.

**Placement.**
- The APIs are drawn once, as the black shared layer. Exhibit 4's tile becomes "API access: OAuth apps and tokens for the Aladdin APIs".
- Data Cloud, ADX, ATX, Aladdin Compute, the SDK and the Developer Portal appear only inside Studio.
- Exhibit 3's outside-inputs row names no Studio parts. It shows two-way arrows into Data Cloud and ADX (fix 37).
- Exhibit 14 moves Data Cloud out of the API band.

**Names.**
- Products: "Aladdin Copilot", "Aladdin Studio", "Aladdin Data Cloud", "Aladdin Data eXchange (ADX)", "Aladdin Tools for Excel (ATX)", "Aladdin Compute" (Exhibit 4 notes once that the SDK calls it Studio Compute sessions).
- Counts and verbs: "about 100 BlackRock applications"; "each tool maps to a production Aladdin API".
- Credentials: "credentials registered in Studio".

**Client side.** Exhibit 14's client tiles use Exhibit 3's Who builds list plus "Its AI tools (proposed)". Each is tagged with the Exhibit 4 part it uses:
- client engineers: SDK and API access, own gateway optional
- data analysts: Data Cloud
- Excel users: ATX
- applications: own environment or Aladdin Compute
- AI tools: API access today, with an MCP route proposed

**Controls labels.** Use one set everywhere: "API scopes", "Aladdin user permissions", "Compliance on orders", "Tool permissions (Copilot registry)".
- Exhibit 3's side panel shows the first three and ends at the shared row (fix 37).
- Exhibit 4's Governance tile quotes "access management and usage monitoring" and points to the same panel.

## 8. Top 5 recommendations, which are also the order of work

1. **Settle words before pictures.** Fix the explicit thesis (short and long forms) and the shared vocabulary in section 7. Then apply the thesis in all 11 places in row A of section 4.
2. **Redraw Exhibits 3, 4 and 14 together under one key.** Draw Exhibit 14 no more than 150pt high so page 12 holds the text and the exhibit. Then update the three aria-labels.
3. **Apply Tier 1–2 text in the tested wordings.** These are the page 2 and page 12 paragraphs, the fix 7 set on pages 8 and 9, and the short forms for Exhibits 2 and 17 and the Miller cell. The list's literal wording breaks pages 3, 8 and 14.
4. **Work through Tiers 3–4 page by page**, from the pages with most room to the fullest. Do pages 5, 9, 10 and 2 first, then 3, 6, 7, 13 and 14 last, using the tested wordings. Render after each full page, and check that the cover's Part page numbers match.
5. **Finish with a rule and register pass.** Grep for "; " between sentences, "—", "suggest", "this way", "these" and "such". Fix the numbering for sources 27/28 and 73/74, register entries 11 and 64, and the existing v23 semicolons and em-dashes.
