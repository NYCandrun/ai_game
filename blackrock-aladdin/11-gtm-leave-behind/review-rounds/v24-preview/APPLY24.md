# Build the v24 preview

Edit ONLY: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/v24/preview.html (a copy of v23).
Never touch scratchpad/gtm/out/ or the repo.
v23 base for reference: scratchpad/v24/v23_base.html. v23 PDF: scratchpad/gtm/out/Aladdin_Studio_from_the_outside_v23.pdf.

## What to apply
Apply the author-approved changes:
1. The recommended wording in the review: scratchpad/review24/Proposed_v24_changes.html. It has fixes 1 to 61 and new items N1 to N13.
2. The overrides and verbatim text in this file. **Where this file and the review differ, this file wins.**

For the 11 places the thesis claim appears, and for every other location of a repeated claim, use the editor's map in scratchpad/fixpanel/out_editor.md section 4. A fix must be applied everywhere its claim appears.

## Author decisions (overrides)
- **Fix 43:** NOT applied. Leave the v23 long-running sentence as is.
- **N9:** NOT applied.
- **N6:** NOT applied. Add no owners line to Exhibit 15.
- **Fixes 50, 58, 60 and 61:** apply (the author chose to keep them).
- **N2:** use THREE conditions. Add no pricing or packaging condition. Verbatim text is below.
- **Fix 26:** row 3 of Exhibit 15 reads "One named client that builds with Studio." The page 8 sentence reads "Firms whose filings or tenders already name BlackRock may be easier to name in public as Aladdin references." It must say "may be", not "are".
- **Decision 5:** leave every "What this finding suggests about direction" heading as is.
- **Fixes 11, 12 and 37 (redrawing Exhibits 3, 4 and 14):** NOT in this build. Another agent is drawing them separately. In v24, keep the v23 drawings and apply only the text-level fixes listed under "Exhibit text" below.
- **Exhibit 15:** reorder the rows to 1, 4, 3, 2 (RFP answer, worked example, named client, page) and renumber them 1 to 4. Apply fix 56 to row 1, N5 to the worked-example row, fix 26 to the named-client row and fix 10 to the page row.
- **Arcesium (Decision 6):** citing a reprint is acceptable. Add a register entry, grade T: "Arcesium Launches Comprehensive AI Platform to Operationalize Agentic AI for Institutional Investment (reprint of Arcesium's release). ABF Journal, May 21, 2026. https://www.abfjournal.com/arcesium-launches-comprehensive-ai-platform-to-operationalize-agentic-ai-for-institutional-investment/". In the text below this entry is called [NEW-ABF]. Its supported facts are: "Arcesium Intelligence"; "over 100 pre-configured agents"; "Agent Studio, a self-service development platform enabling users to create their own agents"; and "model-agnostic by design".
- **N10:** add a register entry, grade P, for Arcesium's Aquata MCP product page: "Aquata MCP server. Aquata by Arcesium product page, as of October 2026. https://aquata.ai/feature-aquata-mcp". It is called [NEW-AQMCP]. It supports "deploys connectors, builds pipelines, and creates quality rules". Add no State Street article, because fix 59's Alpha Co-pilot sentence is dropped.
- **Citation corrections found by audit:**
  - p12: "It sells Aladdin as the system it runs internally" cites [9] only. Remove 83, which does not support it. If 83 is then cited nowhere, remove it from the register.
  - Exhibit 6 note: "Three of the five transcripts" becomes "Four of the five transcripts".
  - Exhibit 1 source line: add the sources its table cites but the line omits (9, 16, 17, 19, 22, 24), each with a short label in the same style as the line.

## Verbatim new text
Write these exactly. Source numbers are v23 numbers; renumber at the end.

### Cover thesis line
Through Studio, clients’ own AI tools could use the tools Copilot uses, acting for each user under that user’s Aladdin permissions.

### Cover heading (N1)
What public sources show, and one direction they point to.

### p2 lede
Through Studio, clients’ own AI tools could use the tools Copilot uses, acting for each user under that user’s Aladdin permissions.

### p2 paragraph 1
Studio is Aladdin’s developer and data layer: APIs and events, Aladdin Data Cloud on Snowflake, and developer tools[1]. Many data providers now let outside AI tools read their data[2,3,4,5]. Aladdin’s APIs can also post orders and assign compliance rules to portfolios. Each API has its own OAuth scopes, and most split read from write. Posting an order runs compliance by default. The caller can turn it off[6]. Whether turning it off needs a separate permission is not public. An AI tool calling these APIs would work under the same API controls as any other client program.

### p2 paragraph 2
Rivals have begun letting AI agents act. Arcesium’s MCP server lets outside AI tools build data pipelines[NEW-AQMCP]. Clearwater says clients use its agents for trade settlement and cash management[8]. SimCorp offers a portfolio management agent and has announced Agent Launchpad for agents that clients build[7]. BlackRock already runs AI on Aladdin. Copilot answers questions for staff and clients in about 100 Aladdin applications. It draws on about two thousand registered tools and agents, and each tool maps to an Aladdin API already in production. The team that owns each tool sets which environments, user groups and apps can use it. No public source shows Copilot posting orders[9]. Buyers of investment software say AI is changing what they build[10]. BlackRock estimated that API calls across BlackRock and Aladdin would grow 17x by 2030[11]. Part 3 sets out this direction: clients’ AI tools using the tools Copilot uses, under each user’s Aladdin permissions. It covers what would have to be true, and four pieces of marketing work that would follow.

### Part 3: replace the five v23 paragraphs before Exhibit 14 with these seven
P1: BlackRock could present Studio as the place where clients’ own AI tools use the tools Copilot uses, acting for each user under that user’s Aladdin permissions. BlackRock has made related claims. It sells Aladdin as the system it runs internally[9]. Its speakers have said that the system of record underpins anything built with AI[10], and that the data model is being structured for agentic use[72]. I have not seen BlackRock describe Studio this way.

P2: Rivals have begun letting AI agents act. Arcesium’s MCP server lets outside AI tools build data pipelines[NEW-AQMCP], and its May 2026 AI platform, Arcesium Intelligence, lets clients build their own agents[76, NEW-ABF]. Clearwater says clients use its agents for trade settlement and cash management[8]. SimCorp has announced Agent Launchpad, which is to give agents that clients build controlled access to SimCorp One data, with an audit trail[7]. What BlackRock can show is scale in production: Copilot runs across about 100 applications on about two thousand registered tools and agents[9].

P3: Some controls sit inside Aladdin’s services and apply to every caller. The specifications tie operations to Aladdin user permissions, set by function, action and portfolio. Posting an order runs a compliance check by default. The caller can skip that check with the same Order:write scope it uses to post. If the caller sets a time limit and the check runs over it, the order posts with the status Compl Pending. Whether an Aladdin permission restricts either option is not public. A portfolio manager authorizes each order before a trader works it, and the public order API has no call to authorize one[6].

P4: Other controls sit where a caller connects. Copilot applies its registry rules by environment, user group and app as it picks tools[9]. Studio clients connect with an application key and OAuth scopes[6]. A licensed client’s own programs, AI tools included, can already call the APIs with credentials registered in Studio[29]. A tool that signs in for a user carries that user’s permissions. A tool that signs in as an application carries the application’s permissions.

P5: Copilot’s own guardrails, planning and AI-graded tests run inside Copilot. Its system prompts are tested daily by AI judges[9]. A client’s own AI model would not get these. A route for clients’ AI tools would need BlackRock to apply Copilot’s registry rules where those tools connect, and to offer checks of its own in place of Copilot’s guardrails. One such route would be an MCP server onto Copilot’s registry, or an agent protocol such as A2A. That is my inference. Copilot’s team has said it is evaluating A2A and LangChain’s agent protocol[9].

P6: Keep the v23 paragraph that starts "Buyers say AI is changing what they build." exactly as it is.

P7: The client base is large. BlackRock serves hundreds of Aladdin clients in 70 countries[9], and its technology services revenue was $2.0 billion in 2025[12]. BlackRock sizes Aladdin’s addressable market at more than $20 billion[11]. It projects API calls across BlackRock and Aladdin to grow 17x by 2030[11]. My inference is that clients’ AI tools, acting through Studio, could become a large source of those calls. How many clients run their own AI tools is not public.

P8: Three things would have to be true for this direction to hold. Clients would have to want Aladdin’s tools inside their own AI tools, and later want those tools to act. Their risk teams and regulators would have to accept it, with a portfolio manager authorizing each order. And BlackRock would have to offer tools it built to AI models it did not build.

(P6 and P7 together replace v23 paragraphs 3 and 4. Fix 51's job-posting sentence is gone. P8 replaces "Three things would have to be true…". That makes eight paragraphs in total.)

### Exhibit text (text-level only, no redraw)
- **Exhibit 14:**
  - Title: "Exhibit 14. BlackRock’s apps, Copilot and client code run on Aladdin’s APIs. Whether Copilot’s tools use the APIs clients can call is not public."
  - Left column heading: "BUILT BY BLACKROCK · USED BY BLACKROCK AND CLIENTS".
  - Client AI tools box: "Its AI tools" / "Can call the APIs with Studio credentials today. No published guide or connector."
  - Approvals box: fix 29 wording.
  - Client tiles: fix 30 wording.
  - Compliance box: "Posting an order runs compliance by default. The caller can turn it off with the scope it uses to post."
  - Note: replace the job-posting sentence with fix 9's quote: "Asked about clients using BlackRock’s plug-ins in their own copilots, BlackRock’s Head of Product for AI said, ‘we are hearing that from our clients’[71]." Replace "which is the model a client’s own AI tools could follow" with "The right-hand controls are Copilot’s own and stay inside Copilot."
  - Keep the SVG layout. Change text only, wrapping lines as needed.
- **Exhibit 3:** apply only the text fixes from the review that touch it. Keep the layout.
- **Exhibit 4:** apply fixes 20, 38, 44, 58 and 61 as worded in the review. For 61, add "Spaces: named alongside Projects. Not described publicly." as a workspace item.
- **Exhibit 11:** apply fix 31.

### Page 9 MCP sentences (resolves fixes 8, 9 and 14 together)
Replace "Aladdin has published no such route. Its only public mention of MCP is a job posting[73]." with:
A licensed client’s own programs, AI tools included, can already call the APIs with credentials registered in Studio[29]. BlackRock has published no guide, MCP server or AI connector for them. The one BlackRock job posting that names MCP is for its internal data platform[73].

Keep page 9's Crockett sentence as fix 3 of the review and the v23 text have it ("said firms building their own copilots need plugins"). Do not duplicate the Smith Garson quote on page 9.

## Writing rules for anything you write yourself
- Plain English.
- No em-dashes.
- No semicolons joining sentences.
- Never "suggested".
- State only the correct fact, and never mention the old wording.
- Say things explicitly.

## Mechanics
- Citation markup: `<sup class="fnref"><a href="#sN">N</a></sup>`. Register entry format: copy an existing `<p id="sN">` entry.
- Add each new register entry with a temporary high number (for example s901). Then run:
  `python3 -I /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/renumber.py <file>`
  After that, re-sort the register and every superscript: `python3 -I /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/v24/sortreg.py <file>`.
- Remove register entries that end up cited nowhere, then renumber again.
- Check that the mapping did not drift: `python3 -I scratchpad/drift22/mech.py <file>` must show first-citation order ok, no uncited entries, and sequential IDs.
- Render:
  `cd /home/user/ai_game && node /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/htmlrev/tools/render_chromium.js scratchpad/v24/preview.html scratchpad/v24/preview.pdf`
  Use the absolute paths.
- Layout is NOT a constraint. The author will fix it later. Do still update the cover's Part page numbers to match where the Parts land.
- Update the aria-labels of any exhibit whose text you change.
- Write scratchpad/v24/APPLY24_LOG.md with one line per fix and item: applied, applied with change (say why), or not applied (say why).
- Write the full, exact sentence for every change. Do not leave placeholders.

## Reply
Report counts, every fix you could not apply as specified and why, the page count, and anything that needs the author's judgment.
