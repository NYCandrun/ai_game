# APPLY63 log: 68 should-fix rewrites, plus author edits, on the preview

Target: `redraw34/preview.html`. Backup before any edit: `redraw34/preview_before63.html`. The script `redraw34/a63/apply63.py` rebuilds `preview.html` from that backup, applies every edit, runs `gtm/renumber.py`, sorts the register and the numbers inside each superscript, and then `a63/build.sh` renders the PDF. The real document `gtm/out/Aladdin_Studio_With_AI.html` was not touched. Its md5 is still 131d807ccbdf86c0cf26100e56ce07f4.

Superscript numbers below are the final numbers after renumbering. The register has 105 entries, with no orphans and no dangling references.

## Counts

| Result | Items |
|---|---|
| Applied as approved (including 44 and 50, filled from source) | 37 |
| Applied with change | 27 (2, 9, 11, 13, 14, 19, 20, 22, 24, 25, 28, 32, 34, 39, 43, 45, 48, 55, 56, 58, 59, 61, 62, 64, 65, 67, 68) |
| Skipped | 3 (17, 18, 23) |
| Mostly skipped, one part applied | 1 (16) |
| Total | 68 |
| Author edits | 1 on page 14, 9 in Exhibit 3, 1 in Exhibit 14 |

Item 12 (Exhibit 2 note: IBOR, ABOR and NAV) appears in `Six_adapted_items` but is **not** in `should_apply.json`. That file has 68 items and only five `adapt` fields, for items 11, 54, 63, 64 and 69. I did not apply item 12. If the author wants it, it is a one-line addition to the Exhibit 2 note, and page 3 has no spare line for it.

## Page fit (final render, 19 pages, vector, no raster images)

- Part 1 starts on page 3, Part 2 on page 7, Part 3 on page 12 and Part 4 on page 13. The cover's page numbers (3, 7, 12, 13) are unchanged and correct.
- Exhibits 3 and 4 are both on page 4.
- Part 3's text and Exhibit 14 are together on page 12.
- Exhibit 16 starts on page 13 and continues on page 14 with its header repeated, exactly as in the baseline. Every other exhibit is whole.
- Exhibit 17 and its closing paragraph are on page 14. Page 14 ends at y=728pt (the baseline ended at 726pt). Page 15 is "About this document". Sources run from page 16 to page 19.
- There are no near-empty pages.

The first full render had 21 pages. Three places overflowed, and I fixed each by tightening the rewrites that caused it:
- **Page 3:** Exhibit 2 moved to page 4 (items 9, 11 and 13).
- **Page 13:** Exhibit 16 no longer started on page 13 (items 55, 56, 58 and 59).
- **Page 14:** Exhibit 17's paragraph moved to page 15 (items 61, 62, 64, 65, 67 and 68).

Each tightened item is marked below.

## Items

**Pages 1 to 4**
1. Applied.
2. Applied with change. The redraw had already rewritten the compliance sentence ("Posting an order runs compliance by default. The caller can turn it off [6]"). I kept that wording and added the new sentence after it: "An AI tool calling these APIs would work under the same controls."
3. Applied.
4. Applied, on page 2 only. Part 3 has the same sentence but is outside this item.
5. Applied. [10] now sits on the buyers sentence and [11] on the API-calls sentence.
6. Applied, keeping the `<code>asdk_plugin</code>` markup.
7. Applied.
8. Applied.
9. Applied with change, for page 3 fit: "...was $2.0 billion in 2025 [12]. Its 24 percent rise includes Preqin, the private-markets data firm BlackRock bought in 2025 [12]." The link stays on "$2.0 billion in 2025".
10. Applied. The link is kept.
11. (adapt) Applied with change, for page 3 fit: "Gives custodians and administrators access to Aladdin. These providers pay BlackRock for it [25]". "These providers" keeps the row to one line and is unambiguous in the Aladdin Provider row. The link is kept.
13. Applied with change, for page 3 fit: "Test (`whatIf`) and compliance (`runCompliance`) [6]".
    - The approved wording took five lines in the narrow cell and pushed Exhibit 2 to page 4. I rendered seven variants, and only this one fits.
    - Checked in the OrderAPI spec: whatIf is "True to post orders in a what-if mode".
    - The step 5 (`ledger_a_summary`) rewrite in the original review is not in the approved item, so I did not apply it.
14. Applied with change. The redraw moved Studio into the client column, so "Studio sits between BlackRock's applications and Aladdin's shared services" no longer matches the drawing. The title is now "Clients reach Aladdin through Studio, and the APIs carry their own controls".
15. Applied ("Who builds on Studio"). "Code-curious portfolio managers" now wraps to three lines, and page 4 still fits.
16. Mostly skipped. The redraw had already rewritten this note: the semicolons, the AWS clause, the Dashboard and Risk Radar sentence and "Controls as in Exhibit 14" are gone. I applied the remaining part, "public software development kit (SDK)". This is the document's first use of SDK.
17. Skipped. The redraw replaced the Projects text ("Personal or shared, each holding OAuth applications and storage").
18. Skipped. The redraw rewrote the Exhibit 4 note. The "no count" sentence is gone, and the note now says "for the SDK and the workspace".
19. Applied with change. The tile and the aria-label now read "Every public specification's ID begins agraph.<domain>, for Aladdin Graph". I added no superscript in the tile. The note already cites [6] "for the ids", and no other tile carries superscripts.

**Pages 5 to 8**
20. Applied with change. The second sentence reads "They set out several controls." The approved "Several controls are built into the APIs themselves" would contradict the redraw, which renamed these "controls in the API specifications".
21. Applied.
22. Applied with change. The sentence reads "The SDK checks back on these operations at set intervals [33]". The README supports polling ("LRO Utilities to trigger and poll Long Running Operation endpoint calls", with a status-check interval), but it also has a 300-second timeout, so "until they finish" is not supported. The link is kept.
23. Skipped. The factual fixes had already replaced the bitemporal and four-eyes sentences.
24. Applied with change. The sentence reads "With OAuth, access is granted per API and per action". The redraw limits per-API access to OAuth scopes ("Other sign-in methods carry none"). The link is kept on "OAuth client ID and secret from Studio's screens". The README says: "Client ID and Secret can be sourced from Studio UI by creating a OAuth application under a Project."
25. Applied with change. I dropped "Alpha is the earliest stage and sunset marks an API being retired". Factual fix 5 had removed that ordering claim as unsourced (VERIFIED V11).
26. Applied. The note gains "The 54 specifications span 11 domains and 11 PyPI packages. Domain names are BlackRock's own, taken from each specification's id." The Total row's cell is now empty. I checked that the domain names are the second segment of each spec id, for example `agraph.portfolio_management...` and `agraph.portfolio...`.
27. Applied.
28. Applied with change, to both notes. The Exhibit 7 note is adapted to read: "Three of the four transcripts (Khara, Goel and Woodhead) are machine-made, as marked in the Sources section."
29. Applied. The Miller sentence is added at the end of the Exhibit 7 note.
30. Applied.
31. Applied.
32. Applied with change. I wrote "program", not "programme", because the document uses US spelling. Checked against the transcript at 5:21: "the implementation of Snowflake that we did as part of the overall program has been really successful for us". The link is kept on "Snowflake implementation".
33. Applied. The links moved to "rewrites web addresses" (PR 52) and "adds custom headers" (PR 53).
34. Applied with change. I kept "or tenders": the current text reads "filings or tenders", and the approved fix dropped that fact. The callout is applied as approved.
35. Applied.
36. Applied. The links are kept.
37. Applied. The new last sentence is an inference from the fee terms in [12]. It is hedged with "under the terms it names", so I kept it.
38. Applied.
39. Applied with change.
    - I wrote "payment in kind (PIK)" without "interest", because the source says only "PIK".
    - The HPS gloss is a separate sentence: "HPS is the credit investment manager BlackRock bought in July 2025 [12]". The FY2025 10-K says "On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS Investment Partners ... a leading global credit investment manager".

**Pages 9 to 12**
40. Applied.
41. Applied. The YouTube link moved onto the quotation.
42. Applied.
43. Applied with change.
    - The heading is applied as approved.
    - In the body, the added sentences go after the factual-fix wording: "Many of the 11 offer an MCP (Model Context Protocol) server... Aladdin has published no such route. Its only public mention of MCP is a job posting [73]".
    - I wrote "Many of the 11", not "Many", so it is clear whom the sentence means. Exhibit 12 shows six of the 11 with an MCP server.
    - Support comes from the Exhibit 12 note: "Aladdin has only a job posting that mentions MCP".
44. Filled from the source, in both the body and the Exhibit 12 LSEG row: "connected to its MCP server".
    - LSEG's Q1 2026 trading update says "90 customers have connected via our Model Context Protocol ('MCP') server".
    - The Investing.com summary [74] says "90 customers now actively connected".
45. Applied with change. I kept the factual fix's "I compared" in place of "a Studio buyer compares".
46. Applied. I also changed the note's "Receipt column" to "Source column" so the two match.
47. Applied.
48. Applied with change. The sentence reads "Copilot uses GPT-4 function calling to plan which tools to call, calls them, and repeats." The approved "calls them through GPT-4" would misdescribe function calling.
49. Applied, with [10] after each quotation.
50. Filled from the transcript: "By that she meant integrated workflows across portfolio management, trading, operations and compliance, governed by operational controls and run on the same data [10]." The webinar captions right after 32:10 read: "So integrated work flows across portfolio management, trading, operations, compliance, all of that ... highly governed with the appropriate operational controls in place ... need to be operating on that same foundational data elements."
51. Applied.
52. Applied. The title is now two sentences, and the first sentence of the caption is removed.
53. Applied. The SVG text is rewrapped to four lines and three lines. The tile sizes are unchanged and nothing is clipped.
54. (adapt) Applied with current numbering: "two SDK pull requests [34, 35], the SDK README [33], Aladdin's public API specifications [6]".
    - Exhibit 3's note still has the same pattern, "pull requests 52 and 53, for the gateway [34, 35]". It is not in the approved list, so I left it.

**Pages 13 to 16**
55. Applied with change, for page 13 fit. The title reads "At each step, what is public today and what opens only after qualification". The full title took two lines. The intro directly above already names the prospect engineer's path.
56. Applied with change, for page fit. The sentence reads "So this document cannot confirm what clients see."
57. Applied.
58. Applied with change, for page fit. The two sentences are merged: "For each step it records what is public today and what opens only to qualified prospects and clients." I did not rename the column (that was optional).
59. Applied with change, for page fit: "It lists the APIs by area, with stability labels. It explains permissions and how a client routes calls through its own gateway. It covers Snowflake and Databricks connectors, and how a client's own AI tools would connect."
60. Applied.
61. Applied with change, for page 14 fit: "Studio Compute (hosted Python), an API token or OAuth app “registered via Studio UI”, the client's Aladdin address". The approved three-sentence version added two lines to the row and pushed Exhibit 17's paragraph onto a 20th page. Only this version fit.
62. Applied with change, for page fit: "SDK changes from outside developers, reviewed and merged by a BlackRock engineer. On the Studio page, “Book a meeting” and “Download the brochure”."
63. (adapt) Applied: "SDK change for enterprise gateways [34], SDK change for Pydantic v2 [89]". The links are kept. Register entry 89 is "Pull request 57, add Pydantic v2 compatibility support".
64. (adapt) Applied with change, for page fit.
    - The password sentence reads "It keeps a password it asks for in the operating system's credential manager." The README says SDK "will prompt the user for their password in command line, and store the password in the OS specific credential manager".
    - I kept the README reading, "built for firms with strict IT controls", because the author approved all 68.
65. Applied with change. The title is one line: "Data platforms open to any developer, investment platforms like Studio mostly to clients".
66. Applied.
67. Applied with change, for page fit. The first sentence is as approved. The second merges with the next one: "Investment platforms score low because a first API call needs a contract or a relationship, at Aladdin as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium."
68. Applied with change. I treated it as an addition: the review says "Add", and item 67 edits the same paragraph. The new sentence is "Studio scores in line with them, but trails Bloomberg and Arcesium on AI connectors (0 against 2)." I checked it against the Exhibit 17 scores: Aladdin 0, Bloomberg 2, Arcesium 2.
69. (adapt) Applied. The rest of the paragraph is unchanged, including "unless an exhibit or a source entry gives another date".

## Author edits

- **Author edit, page 14.** "10 platforms that a Studio buyer also deals with" now reads "10 platforms that may compete with Aladdin for certain uses". The rest of the sentence is unchanged, and it has no citation.
- **Author edit, Exhibit 3.** Deleted "BlackRock calls it “a common data language”." from the shared services box.
- **Author edit, Exhibit 3.** Deleted ", as in Exhibit 1" from the platforms line.
- **Author edit, Exhibit 3.** Deleted "Other sign-in methods carry none." from the Access tile, in Exhibit 3 only.
- **Author edit, Exhibit 3.** Deleted the Data Cloud description. The label "Data Cloud: data out" stays.
- **Author edit, Exhibit 3.** Deleted the AWS general-availability sentence from the Hosting row.
- **Author edit, Exhibit 3.** Removed ", which BlackRock calls a common data language" from the aria-label. In the source note, the AWS release [21] now reads "for the platforms". The Data Cloud launch release [36] is still listed.
- **Author edit, Exhibit 3.** Deleted the controls paragraph "Data Cloud, storage and the Data eXchange have their own access controls: Snowflake roles and keys, S3 keys and SFTP." and the matching aria-label sentence. The Exhibit 14 notes are untouched.
- **Author edit, Exhibit 3.** Nothing left in Exhibit 3 mentions SQL, so the specs and SDK entry now reads "for the domains, apps and controls [6, 33]".
- **Author edit, Exhibit 3, layout.** No gap needed tightening. The Data Cloud box now sits as a one-line box beside the Data eXchange box. The grey controls panel stretches to the height of the shared layer and has a little empty space at its foot. Exhibits 3 and 4 are on page 4.
- **Author edit, Exhibit 14.** The Access set per API tile now reads "Each API has its own OAuth" / "scopes." The third `<text>` element is removed. The tile size and the other tiles are unchanged. Part 3's text and Exhibit 14 are still together on page 12, and the document is 19 pages.

## Checks
- No new em-dashes and no new semicolons in the text. "suggest" now appears once fewer: item 51 removed "The findings suggest", and the existing "What this finding suggests about direction" labels are untouched.
- Deliverable: `redraw34/Full_preview.pdf`, 19 pages, US Letter, vector (pdfimages lists no images).
