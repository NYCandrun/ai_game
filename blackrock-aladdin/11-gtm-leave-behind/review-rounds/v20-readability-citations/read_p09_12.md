# Readability read, pages 9 to 12 (v20)

Scope: page 9 (end of Part 2 Section 2 callout, Section 3, Exhibit 11), page 10 (Exhibit 12, Section 3 callout, Section 4 opening), page 11 (Exhibit 13, Section 4), page 12 (Part 3 and Exhibit 14). Checked as text and as 90 dpi page images.

Types: 1 GARBLED, 2 HARD TO READ, 3 ALLUDING, 4 EXHIBIT.

---

## MUST FIX

### M1. p10, Section 3 callout ("What this finding suggests about direction")
- Current: "A public account of the Copilot plugin model would cover the production Aladdin APIs its tools call, which user groups may use each tool, and tested no-advice guardrails 9, 23. That account answers three governance questions: who can call what, with which permissions, and under which guardrails."
- Type: 3, also 1. It never says what BlackRock should do. The reader must infer "publish an account". Tense slips from "would cover" to "answers". The three listed items do not line up with the three questions. It also does not tie back to the finding (rivals publish how outside AI reaches their data, and Aladdin does not).
- Rewrite: "Rivals and data providers publish how outside AI tools reach their data. Aladdin has published only a job posting that mentions MCP [77]. BlackRock could publish how Copilot's plugin model works. That account would name the production Aladdin APIs each tool calls [9]. It would say which user groups may use each tool [9]. It would show the tested guardrails that block investment advice [9, 23]. Together these answer who can call what, with which permissions and under which guardrails."

### M2. p11, Section 4 callout
- Current: "Buyers now ask in RFPs whether they can build on the platform. Studio is the right kind of answer."
- Type: 3. "The right kind of answer" is a gesture. The reader has to work out why Studio answers the RFP question and what BlackRock should do with that.
- Rewrite: "Buyers now ask in RFPs about a vendor's API suite and its connectors to Snowflake and Databricks [10]. Studio is BlackRock's answer to that question. It gives clients APIs to build their own tools on Aladdin. BlackRock could lead with Studio in the API section of RFP responses."

### M3. p12, Part 3, paragraph 2, first sentence
- Current: "Letting AI tools act is unlikely to stay unique. SimCorp and Clearwater have announced AI agents, Arcesium an AI platform, and others will likely follow 7, 8, 73."
- Type: 1. It contradicts itself. "Unlikely to stay unique" says the capability is unique today. The next sentence says three rivals have already announced it. It also leaves unclear whose capability is "unique".
- Rewrite: "Letting AI tools act will not set Studio apart. SimCorp and Clearwater have announced AI agents [7, 8]. Arcesium has launched an AI platform [73]. Others will likely follow."

### M4. p12, Part 3, paragraph 4, citation placement on the 17x figure
- Current: "It projects API calls to grow 17x by 2030, and AI tools acting for clients could become a large source of them 11. Linking that figure to Studio is my inference."
- Type: 1 (misleading). Citation [11] sits after the AI-tools clause, so it reads as if BlackRock said AI tools would drive the calls. The next sentence then calls a different link (to Studio) the inference. The reader cannot tell which part is sourced.
- Rewrite: "It projects API calls to grow 17x by 2030 [11]. My inference is that a client's AI tools, acting through Studio, could become a large source of those calls."

### M5. p12, Exhibit 14, hatched box "Its AI tools" and the note
- Current (box): "Nearest public sign: an internal job posting." Current (note): "The nearest public sign is a September 2026 posting for an internal data role that names MCP and AI agents 77."
- Type: 1 and 4. The box calls the posting "internal", but it is offered as a public sign and was public. That contradicts itself. Exhibit 12 also describes the same posting differently: "A Forward Deploy Engineer posting for Aladdin Data". The reader cannot tell whether these are the same document.
- Rewrite (box): "Nearest public sign: a BlackRock job posting that names MCP." Rewrite (note): "The nearest public sign is a September 2026 Forward Deploy Engineer posting for Aladdin Data. It names MCP and AI agents [77]." (If "internal" was meant to describe the role, check [77]. A forward-deployed engineer usually works with clients.)

### M6. p12, Part 3, paragraph 1, last sentence
- Current: "I have not found it describe Studio this way."
- Type: 1. Wrong verb form ("found it describe"), and "it" is ambiguous after "the system of record" and "the data model".
- Rewrite: "I have not seen BlackRock describe Studio this way."

---

## SHOULD FIX

### S1. p9, Section 2 callout (top of page)
- Current: "BlackRock projects API calls across BlackRock and Aladdin to grow 17x by 2030, the fastest of the four volumes it showed investors 11. The private-markets data it is adding from eFront and Preqin is going into Data Cloud, which is part of Studio 22."
- Type: 3. Under a "direction" label it only repeats two facts. It never states the direction. "Four volumes" is shorthand for the four 2030 forecasts on page 7.
- Rewrite: "BlackRock's two growth bets both run through Studio. It projects API calls across BlackRock and Aladdin to grow 17x by 2030 [11]. That is the fastest of the four forecasts it showed investors [11]. Its new eFront and Preqin private-markets data is going into Data Cloud, which is part of Studio [22]. BlackRock could name Studio when it tells investors this growth story."

### S2. p9, Section 3, sentences 2 and 3
- Current: "It draws on a registry of plugins, "couple of thousands agents and tools," built by Aladdin's engineering teams. The first way a team adds a tool is "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" 9. Teams can also register agents of their own 9."
- Type: 2. The ungrammatical quote is wedged in as an appositive. "The first way a team adds a tool" reads as the first of several ways to add a tool. That seems to clash with page 12 and Exhibit 14 ("Each Copilot tool maps to a production Aladdin API").
- Rewrite: "It draws on a registry of plugins built by Aladdin's engineering teams. The speakers put it at a "couple of thousands agents and tools" [9]. Teams add to the registry in two ways. The first is "to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production" [9]. The second is to register an agent of their own [9]."

### S3. p9, Section 3, Crockett sentence
- Current: "Microsoft's Adrian Crockett made the dependence plain on BlackRock's podcast: "There's no copilot without plug-ins" 69."
- Type: 1/2. "The dependence" has no antecedent. The reader must work out that it means Copilot depends on plugins.
- Rewrite: "On BlackRock's podcast, Microsoft's Adrian Crockett said Copilot depends on its plugins: "There's no copilot without plug-ins" [69]."

### S4. p9, Section 3 heading and body: Aladdin's own position never stated in the text
- Current (heading): "Aladdin's AI answers inside the login; data providers let outside AI tools reach their data". Current (body): "Six data and cloud providers that Studio buyers also use offer a connector or an MCP server. Four system-of-record rivals have announced AI features or AI access to their data."
- Type: 3 and 2. The section's point is that Aladdin has no public route for outside AI tools while ten others do. That point only appears in the Exhibit 12 note. "Inside the login" is shorthand. The heading uses a semicolon to join two clauses. "MCP" is never spelled out in the body (only inside a quote in Exhibit 12).
- Rewrite (heading): "Aladdin's AI works only for logged-in users. Data providers let outside AI tools reach their data." Rewrite (body, add after the two sentences): "Many offer an MCP (Model Context Protocol) server, a standard way for outside AI tools to connect. Aladdin has published no such route. Its only public mention of MCP is a job posting [77]."

### S5. p9 body and p10 Exhibit 12 LSEG row: "connected" to what
- Current: "LSEG had 90 customers connected by April 2026, according to a secondary summary of its results slides 71." and "It had 90 customers connected by April 2026".
- Type: 1. "Connected" has no object, so the reader cannot tell what the 90 customers connected to.
- Rewrite: "LSEG had 90 customers connected to [its MCP server / AI offering, per 71] by April 2026 [71]. The figure comes from a secondary summary of its results slides." Fill the bracket from source 71.

### S6. p10, Exhibit 12 title
- Current: "Of 11 providers a Studio buyer compares, ten have announced AI features or AI access to their data"
- Type: 4 and 3. The title leaves the reader to work out that the eleventh is Aladdin. That is the point of the exhibit.
- Rewrite: "Ten of the 11 providers a Studio buyer compares have announced AI features or AI access. Aladdin has not."

### S7. p10, Exhibit 12 column header "Receipt"
- Current: "Receipt"
- Type: 4. Cryptic label. The note itself calls these "press releases, documentation and job posting".
- Rewrite: "Source"

### S8. p9, Exhibit 11 note
- Current: "The tool counts are the speakers' own approximations; the talk is a machine transcription, marked as such in the Sources section."
- Type: 2/1. A semicolon joins two sentences. "The talk is a machine transcription" is wrong: the talk is not a transcription, the record of it is.
- Rewrite: "The tool counts are the speakers' own estimates. Quotes come from a machine transcript of the talk, marked as such in Sources."

### S9. p9, Exhibit 11, box 4
- Current: "Plan and call the API: an orchestrator loops "over a planning and action node" using GPT-4 function calling. Output guardrails then check the answer for hallucinations 9"
- Type: 2/4. "Orchestrator", "planning and action node" and "function calling" are engineering terms that a business reader would not know.
- Rewrite: "Plan and call the APIs: Copilot plans which tools to call, calls them through GPT-4, and repeats. The talk describes a loop "over a planning and action node" [9]. Output guardrails then check the answer for hallucinations [9]."

### S10. p11, Sewdass paragraph, sentences 2 to 4
- Current: "She described the shift of the last two years. It is "to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows." That comes, she said, with "very, very robust APIs that manage the end to end life cycle of a transaction.""
- Type: 2. "It is "to more of..."" does not read as English because the quote starts mid-phrase. "That comes" has a loose antecedent.
- Rewrite: "She said clients have moved over the last two years "to more of a modular approach" [10]. They want "that backbone foundational data that supports both publics and privates workflows" [10]. They also want "very, very robust APIs that manage the end to end life cycle of a transaction" [10]."

### S11. p11, Sewdass paragraph, last sentence
- Current: "She also said "the other layer that is almost equally important is a really defined system of work" 10."
- Type: 3/2. "System of work" is left unexplained, and the text does nothing with it. The reader cannot tell why it is quoted.
- Rewrite: say in one sentence what she meant by it, if the transcript says. If it does not, cut the sentence. For example: "She called a "really defined system of work" the other layer that is "almost equally important" [10]. By that she meant [her gloss from 10]."

### S12. p12, Part 3, opening sentence
- Current: "The findings suggest that Studio could be presented as the place where a client's own AI tools act on investment data under the same controls BlackRock's own business runs on."
- Type: 2/3. Hedges are stacked ("suggest", "could be presented") in a 30-word sentence.
- Rewrite: "BlackRock could present Studio as the place where a client's own AI tools act on investment data. Those tools would run under the same controls as BlackRock's own business."

### S13. p12, Exhibit 14 title, and the caption under "Aladdin's APIs"
- Current (title): "BlackRock's applications and a client's code draw on Aladdin's shared services and APIs". Current (caption): "BlackRock's applications, Copilot and a client's code draw on Aladdin's shared services and APIs. Each client reads its own Data Cloud, which BlackRock runs on Snowflake."
- Type: 4. The title states the plumbing, not the message: the controls already exist, and the client AI-tool path is the one missing piece. The caption repeats the title almost word for word.
- Rewrite (title): "BlackRock's apps, Copilot and client code share Aladdin's APIs and controls. How a client's AI tools would connect is not public." Rewrite (caption): "Each client reads its own Data Cloud, which BlackRock runs on Snowflake."

### S14. p12, Exhibit 14, Copilot control boxes
- Current: "Input guardrails: Off-topic content is caught and personal data handled before any plan." and "LLM judges: Every system prompt is tested daily and on every change."
- Type: 4/2. "Before any plan" is cryptic. "Personal data handled" does not say how it is handled. "LLM judges" is jargon the box does not explain.
- Rewrite: "Input guardrails: Copilot catches off-topic requests and handles personal data before it plans any API calls." and "AI-graded tests: AI models ("LLM judges") test every system prompt daily and on every change."

### S15. p12, Exhibit 14 note, source list
- Current: "... the Copilot page 23, pull requests 52 and 53 52, 53, the SDK README 29, the public specifications 6, ..."
- Type: 2/4. "52 and 53 52, 53" doubles the numbers and clutters the line. "The public specifications" does not say whose.
- Rewrite: "... the Copilot page [23], two SDK pull requests [52, 53], the SDK README [29], Aladdin's public API specifications [6], ..."

---

## OPTIONAL

### O1. p10, Exhibit 12 SimCorp row
- Current: "Agent Launchpad, announced in 2026, is to offer prebuilt AI agents and let clients build their own on SimCorp One's data layer"
- Type: 2. "Is to offer" is stiff.
- Rewrite: "SimCorp announced Agent Launchpad in 2026. It will offer prebuilt AI agents and let clients build their own on SimCorp One's data layer."

### O2. p11, "Rivals sell the same model" paragraph
- Current: "Rivals sell the same model, a core platform with the client's own builds on top."
- Type: 2. "The same model" points back loosely, and "builds" used as a noun is shorthand.
- Rewrite: "Rivals sell the same modular model: a core platform, with tools the client builds on top."

### O3. p12, Exhibit 14 client column labels
- Current: "Its engineers", "Its applications", "Its AI tools"
- Type: 4. "Its" relies on the small-caps band header.
- Rewrite: "Client engineers", "Client applications", "Client AI tools".

### O4. p12, Exhibit 14, "Compliance by default" box
- Current: "The order API runs compliance by default and returns any violations."
- Type: 2. "Runs compliance" is shorthand.
- Rewrite: "The order API runs compliance checks by default and returns any violations."

### O5. p11, Exhibit 13 note
- Current: "Source: poll results read out on the Build vs. Buy webinar, from the replay's published captions 10."
- Type: 4. Page 12 says the poll "gives no sample size". The exhibit note should say so too, so that a reader of the chart alone is not misled.
- Rewrite: "Source: poll results read out on the Build vs. Buy webinar, from the replay's published captions [10]. The webinar gave no sample size."

### O6. "What this finding suggests about direction" label (pp. 9, 10, 11)
- Type: 3 (mild). "Suggests" hedges every takeaway box.
- Rewrite: "What this means for direction."
