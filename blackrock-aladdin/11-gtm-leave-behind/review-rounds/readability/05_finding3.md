# Readability pass: pages 11 and 12 (Finding 3, Exhibits 13 to 15, direction box)

Checked against `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/review4/text.txt` (lines 575 to 678) and a 150 dpi render of pages 11 and 12 from `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.pdf` (same build as the text file, 21:26 UTC). Every word on both pages was read, including the running footer, the source notes and the receipt column.

Underlined link phrases on these pages, which every rewrite below keeps intact and in place: "Aladdin Copilot"; "couple of thousands agents and tools," (twice, body and Exhibit 13); "There's no copilot without plug-ins"; "the data model itself is structured for agentic use cases"; "what is my exposure to aerospace in Portfolio 1?"; "say, 20 to 30 tools and agents,"; "over a planning and action node"; "never provide investment advice"; "MCP"; "90 customers connected"; "Forward Deploy Engineer posting"; and the nine receipt-column links in Exhibit 14. Exhibit 15 and the direction box carry superscripts only, no underlines.

Priority order, if only some of this gets done: items 15, 16 and 17 (the direction box, which is the payoff of the finding and the hardest to read once), then 2 and 3 (the opening paragraph, which buries the finding's key sentence), then 9 and 10 (the paragraph that introduces the outside model), then 11 to 14 (Exhibit 15 cells), then flag A (Exhibit 14 title versus its rows).

---

## Passages

### 1. Page 11, section heading

**Current text:** "3. BlackRock has built an AI front door and keeps it inside the platform, while data providers market theirs outside"

**Trying to say:** BlackRock's AI entry point (Copilot) is only reachable from inside Aladdin; its data-provider rivals sell AI entry points that outside tools can reach.

**Assessment:** Readable; 20 words, one contrast. "Theirs" has to be carried back across the comma to "AI front door", and "front door" is a metaphor the reader last saw on page 2. Optional tightening only.

**Rewrite (optional):** "3. BlackRock keeps its AI front door inside the platform; data providers market theirs outside"

### 2. Page 11, opening paragraph, second sentence (53 words)

**Current text:** "Two of its engineers, Brennan Rosales, AI Engineering Lead, and Pedro Vicente Valdez, Principal AI Engineer, describe a plugin registry with "couple of thousands agents and tools," where the first way a team onboards is "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" 9."

**Trying to say:** Copilot works from a registry of thousands of tools, and the standard way an engineering team adds a tool is to wrap an existing production Aladdin API.

**Why it stops the reader:** Four ideas in one sentence (two names with titles, the registry, its size, how teams join it). "Plugin registry" and "onboards" arrive before either is explained; "a team onboards" leaves the reader asking onboards to what. The quotation is 24 words of conference speech inside a 53-word sentence.

**Rewrite:** "Two of its engineers, Brennan Rosales, AI Engineering Lead, and Pedro Vicente Valdez, Principal AI Engineer, describe how it works. Copilot draws on a registry of plugins, "couple of thousands agents and tools," built by Aladdin's engineering teams. The first way a team adds a tool is "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" 9."

### 3. Page 11, opening paragraph, third sentence (the finding's key claim)

**Current text:** "Copilot's tools are Studio's APIs; Microsoft's Adrian Crockett put it in one line on BlackRock's podcast: "There's no copilot without plug-ins" 59."

**Trying to say:** The tools Copilot calls are the same APIs Studio sells, so Copilot is built on Studio.

**Why it stops the reader:** This is the sentence the whole finding rests on, and it is buried after a 53-word sentence, welded by a semicolon to a quote that does not quite say the same thing (Crockett says Copilot needs plug-ins; he does not say the plug-ins are Studio's APIs). "Put it in one line" asks the reader to work out what "it" is.

**Rewrite:** "So Copilot's tools are Studio's APIs. Microsoft's Adrian Crockett made the dependence plain on BlackRock's podcast: "There's no copilot without plug-ins" 59."

(Consider also opening the paragraph with this sentence, so the finding is stated before the evidence: "Copilot's tools are Studio's APIs. Aladdin Copilot is "now available ..."")

### 4. Page 11, opening paragraph, fourth sentence

**Current text:** "BlackRock's AI product head says the team is making sure "the data model itself is structured for agentic use cases" 60."

**Trying to say:** BlackRock is shaping its data so AI agents can use it, which is the same direction as Copilot's plugin model.

**Assessment:** Clear enough. "Agentic use cases" is inside a quotation and cannot be changed. The only gap is that the sentence does not say why it is here; a four-word lead-in fixes that.

**Rewrite:** "The data layer is being shaped the same way: BlackRock's AI product head says the team is making sure "the data model itself is structured for agentic use cases" 60."

### 5. Page 11, Exhibit 13, box 1

**Current text:** "One question, with the app, portfolio and widgets on screen; the talk's example is "what is my exposure to aerospace in Portfolio 1?" 9"

**Trying to say:** The user asks one question, and Copilot also gets what is open on screen (the app, the portfolio, the widgets) as context.

**Why it stops the reader:** "With the app, portfolio and widgets on screen" reads as scene-setting, not as an input to the system, so the reader does not learn why it is mentioned.

**Rewrite:** "One question, plus what is on screen: the open app, portfolio and widgets go in as context. The talk's example is "what is my exposure to aerospace in Portfolio 1?" 9"

### 6. Page 11, Exhibit 13, box 3

**Current text:** "20 to 30 candidates: filtering by environment, user group and app leaves "say, 20 to 30 tools and agents," since more than "40, 50 tools" would hurt performance 9"

**Trying to say:** Copilot narrows the thousands of tools to 20 or 30 that fit the user's environment, group and app, because the model performs badly with more.

**Why it stops the reader:** "Candidates" for what is not said. "Filtering ... leaves" has no actor. "Hurt performance" is ambiguous between speed and answer quality; the talk means the model's answers.

**Rewrite:** "20 to 30 tools in play: Copilot filters the registry by environment, user group and app, leaving "say, 20 to 30 tools and agents," because giving the model more than "40, 50 tools" would hurt its answers 9"

(If "hurt its answers" is more than the talk supports, keep "would hurt performance".)

### 7. Page 11, Exhibit 13, box 4

**Current text:** "Plan and call the API: the orchestrator iterates "over a planning and action node" with GPT-4 function calling, then output guardrails check for hallucinations 9"

**Trying to say:** A controlling component plans which tool to call and calls it, in a loop, and a final check screens the answer for invented content.

**Why it stops the reader:** Three unexplained terms in 25 words ("orchestrator", "GPT-4 function calling", "output guardrails"). An executive can follow the box only if told what each does.

**Rewrite:** "Plan and call the API: an orchestrator, the component that decides which tool to call, loops "over a planning and action node" using GPT-4's function calling; a final check, the output guardrails, screens the answer for hallucinations 9"

### 8. Page 11, Exhibit 13, box 5 and source note

**Current text (box 5):** "One answer, never investment advice: the system prompt is tested so Copilot will "never provide investment advice" 9; the product page says the same 16"

**Trying to say:** Copilot's standing instructions are tested to make sure it refuses to give investment advice.

**Assessment:** Readable. "System prompt" is the one term an executive may not know; a three-word gloss fixes it. Source note is clear.

**Rewrite:** "One answer, never investment advice: Copilot's standing instructions (its system prompt) are tested so it will "never provide investment advice" 9; the product page says the same 16"

### 9. Page 11, paragraph below Exhibit 13, sentences 1 and 2

**Current text:** "Outside the login, the data market has chosen the other model. MCP is the common standard AI assistants use to pull data from other systems 61."

**Trying to say:** Data providers have taken the opposite approach: they let outside AI tools reach their data, mostly through a standard called MCP.

**Why it stops the reader:** "The other model" has no antecedent; nothing above has called Copilot's design "a model". "The data market" is abstract (it means data providers). MCP is used before it is expanded; the expansion "Model Context Protocol (MCP)" only appears three lines later inside a job-posting quote.

**Rewrite:** "Outside the login, data providers have chosen the opposite design: they let the buyer's own AI tools reach their data. MCP, the Model Context Protocol, is the common standard AI assistants use to pull data from other systems 61."

### 10. Page 11, same paragraph, sentences 3 and 4 (33 and 30 words)

**Current text:** "Seven providers that a Studio buyer also deals with offer a connector or an MCP server; LSEG had 90 customers connected by April 2026, according to a secondary summary of its results slides 62, 63. No public connector for Aladdin was found on BlackRock's pages or GitHub 13, 64; a Forward Deploy Engineer posting for Aladdin Data names "Model Context Protocol (MCP), AI agents, and Copilot extensions" 65."

**Trying to say:** Seven providers the same buyers use have connectors; one of them already has 90 customers on it; Aladdin has none in public, and the only hint of one is a job advert.

**Why it stops the reader:** Two semicolons join four separate facts. The passive "was found" hides who looked (the author). The job posting is dropped in without saying why it matters, so the conclusion, that BlackRock is at least hiring for connector work, is implied rather than stated.

**Rewrite:** "Seven providers that Studio buyers also use offer a connector or an MCP server. LSEG had 90 customers connected by April 2026, according to a secondary summary of its results slides 62, 63. I found no public connector for Aladdin on BlackRock's pages or GitHub 13, 64. The one public hint is a job advert: a Forward Deploy Engineer posting for Aladdin Data names "Model Context Protocol (MCP), AI agents, and Copilot extensions" 65."

### 11. Page 12, Exhibit 15, "For" row, inside column

**Current text:** "Governance in one place; inherited permissions ("permission-dependent access"); no-advice guardrails tested in the system prompt; enterprise trust; a controlled rollout team by team 16, 9"

**Trying to say:** Keeping Copilot inside gives BlackRock one point of control, reuses each user's Aladdin permissions, keeps the tested no-advice guardrails, carries the trust of the enterprise login, and lets BlackRock roll it out one engineering team at a time.

**Why it stops the reader:** Five fragments without subjects. "Inherited permissions" does not say inherited from what. "A controlled rollout team by team" can be read as "a controlled-rollout team" (a team that does rollouts).

**Rewrite:** "One place to govern access; each user keeps their Aladdin permissions ("permission-dependent access"); guardrails against giving advice, tested in the system prompt; the trust of an enterprise login; a rollout BlackRock controls, one engineering team at a time 16, 9"

### 12. Page 12, Exhibit 15, "For" row, outside column

**Current text:** "Discoverability; developer pull; an ecosystem signal; a ready answer to the RFP question about connectors; the terms FactSet, LSEG and MSCI now set 7, 63, 39, 8"

**Trying to say:** An outside connector lets prospects find Aladdin, lets developers adopt it on their own, signals an ecosystem, answers the connector question in RFPs, and matches what FactSet, LSEG and MSCI already offer.

**Why it stops the reader:** "Developer pull" and "an ecosystem signal" are marketing shorthand. "The terms FactSet, LSEG and MSCI now set" is a sentence-ending fragment whose meaning (those three now define what buyers expect) has to be inferred.

**Rewrite:** "Prospects can find it; developers adopt it on their own (developer pull); it signals an ecosystem; it gives a ready answer to the RFP question about connectors; and it matches what FactSet, LSEG and MSCI now offer, which is the comparison buyers make 7, 63, 39, 8"

### 13. Page 12, Exhibit 15, "Against" row, inside column

**Current text:** "Invisible to prospects and to the AI tools buyers already use; rivals set the terms of comparison; the plugin model is described only in a conference talk 9"

**Trying to say:** Nobody outside can see Copilot's plugin model, rivals therefore define the comparison, and the only public account of it is one conference talk.

**Why it stops the reader:** "The AI tools buyers already use" is a garden path ("AI tools, buyers already use"). Otherwise clear.

**Rewrite:** "Prospects cannot see it, and nor can the AI tools that buyers already run; rivals set the terms of comparison; the only public description of the plugin model is one conference talk 9"

### 14. Page 12, Exhibit 15, "Against" row, outside column

**Current text:** "A larger security surface; support cost; a partial catalog exposed and read as the whole; regulatory optics for a platform that will not give advice 16"

**Trying to say:** An outside connector means more to secure and support; if only part of the API catalog is exposed, buyers will assume that is all there is; and outside AI tools using Aladdin data could look, to regulators, like a platform giving advice.

**Why it stops the reader:** "A partial catalog exposed and read as the whole" needs two readings. "Regulatory optics for a platform that will not give advice" states a tension without saying what it is.

**Rewrite:** "More to secure and more to support; buyers would read a partial catalog as the whole catalog; and a platform that will not give advice 16 would have to explain to regulators what outside AI tools do with its data"

### 15. Page 12, direction box, sentence 1 (38 words)

**Current text:** "What it suggests about direction. I would describe the Copilot plugin model publicly now: Copilot's tools are production Aladdin APIs, the same governed APIs Studio exposes, with inherited permissions and no-advice guardrails tested in the system prompt, and it never gives investment advice 9, 16."

**Trying to say:** BlackRock should publish a plain description of how Copilot works, and here is what that description would say.

**Why it stops the reader:** A recommendation and its content are stacked after one colon into four clauses; "with inherited permissions" attaches ambiguously to the APIs or to Copilot; "it" at the end is Copilot, three clauses back.

**Rewrite:** "What it suggests about direction. I would describe the Copilot plugin model publicly, now. The description is short. Copilot's tools are production Aladdin APIs, the same governed APIs Studio exposes. Copilot inherits each user's permissions. Its guardrails against giving advice are tested in the system prompt, and it never gives investment advice 9, 16."

### 16. Page 12, direction box, sentence 2 (35 words)

**Current text:** "Said in BlackRock's own words, that is a stronger answer to the RFP connector question than an MCP server with a partial catalog, and it takes the terms of comparison back from FactSet and LSEG."

**Trying to say:** A published description of the inside model beats a half-built outside connector as an RFP answer, and it lets BlackRock, not its rivals, define the comparison.

**Why it stops the reader:** "That" and "it" both point back to a description that was never named as one. "Takes the terms of comparison back" is an idiom the reader must unpack.

**Rewrite:** "Said in BlackRock's own words, that description answers the RFP question about connectors better than an MCP server with a partial catalog would. It also lets BlackRock, not FactSet and LSEG, set the terms on which buyers compare."

### 17. Page 12, direction box, sentences 3 and 4 (31 words, then 8)

**Current text:** "I would hold any outside connector until the governance questions the inside model already answers, who can call what, with which permissions and under which guardrails, are solved for outside callers. Exhibit 15 is the evidence for that view."

**Trying to say:** Do not ship an outside connector until BlackRock can answer, for outside callers, the three access questions Copilot already answers inside.

**Why it stops the reader:** The subject ("the governance questions") is separated from its verb ("are solved") by a 15-word parenthesis listing the questions; the reader reaches "are solved" having lost the subject.

**Rewrite:** "I would hold any outside connector for now. The inside model already answers three governance questions: who can call what, with which permissions, and under which guardrails. An outside connector should wait until those are answered for outside callers too. Exhibit 15 is the evidence for that view."

(Optional, no new fact: end with "This is quick win 5." The box recommends exactly what page 2 lists as quick win 5, and the reader is not told so.)

---

## Content-clarity flags (not rewrites; the author should decide)

**A. Exhibit 14 title promises more than two rows deliver.** The title says all seven providers "let outside AI tools pull their data". The Arcesium row ("AI features in Aquata, and an AI platform announcement") and the S&P Global row ("Credit Ratings added to its AI Data Portal, September 2026") do not say an outside AI tool can pull anything; "Aquata" and "AI Data Portal" are also unexplained product names. A once-through reader will either take the title on trust or wonder whether those two rows belong. Either state the connector mechanism in those two cells, or soften the title (proposed below).

**B. Exhibit 15 and the direction box use "inside the login" and "outside the login" as if both were established designs.** The paragraph above Exhibit 14 is the first and only place the outside design is described, and it calls it "the other model". One consistent name pair, used in the paragraph, the column heads and the box, would remove the hunting.

**C. Table-cell fragments in Exhibit 14 are acceptable as cells.** "Managed MCP servers, documented" and "A documented MCP server for Cortex Agents" are fine for a receipts table; no change proposed. The Aladdin row, in bold, is the exhibit's point and reads clearly.

---

## Exhibit titles

| Exhibit | Current title | Proposed title (states the finding) |
|---|---|---|
| 13 (p. 11) | "How Aladdin Copilot answers a question" | "Every Copilot answer is a call to a production Aladdin API: thousands of registered tools are filtered to 20 or 30, the call is planned and checked, and advice is refused" |
| 14 (pp. 11-12) | "Seven data and platform providers let outside AI tools pull their data; no public Aladdin equivalent was found" | "Seven providers a Studio buyer also uses have shipped or announced AI connectors to their data; Aladdin has no public equivalent, only a job advert that mentions MCP" |
| 15 (p. 12) | "Two sides of the AI front door" | "Keeping the AI front door inside the login gives BlackRock governance and trust; opening it outside gives discoverability on rivals' terms, with more to secure and more to explain to regulators" |

Shorter alternatives if the above run long on the page:

- 13: "Copilot answers a question by choosing from thousands of registered tools and calling production Aladdin APIs, never giving advice"
- 14: "Seven providers offer or have announced AI connectors to their data; Aladdin has none in public"
- 15: "Inside the login buys governance; outside the login buys discoverability on rivals' terms"
