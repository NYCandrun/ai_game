# Short-text pass, pages 12 to 15 (Findings 3 and 4, Exhibits 13 to 16, direction callouts, "What would change my view")

Test applied to every item: read once at speed, do you know what it says? Items are in page order. Superscripts are written as [n]; links are kept where the current text has them. Items marked **minor** pass the test with a stumble; the others fail it.

---

## Page 12

### 1. Finding 2 direction callout (top of page) — minor

**Current:** "The data it is adding, private markets and Preqin, arrives through Data Cloud and Explore, the surfaces Studio provides. So Studio carries the growth story even when BlackRock does not say its name."

**Trying to say:** the new data lands on Studio surfaces, so the growth story is a Studio story.

**Rewrite:** "The data it is adding, private markets and Preqin, arrives through Data Cloud and Explore. Both are Studio surfaces. So Studio carries the growth story, whether or not BlackRock says its name."

The first sentence stacks two appositives; splitting it removes the double comma-clause. The rest of the callout is fine.

### 2. Finding 3 headline

**Current:** "3. BlackRock keeps its AI front door inside the platform; data providers market theirs outside"

**Trying to say:** Aladdin's AI (Copilot) is reachable only by logged-in users; the data providers Studio buyers also use let outside AI tools reach their data.

**Rewrite:** "3. Aladdin's AI works only inside the login; data providers let outside AI tools reach their data"

"Front door" is a metaphor the reader has not met, "theirs" has no clear antecedent (their door? their AI? their data?), and "market" is doing unexplained work. The rewrite keeps one contrast but in parallel plain words, 16 words, with "inside the login" introduced here so Exhibit 15 can reuse it. If a single clause is wanted: "3. Aladdin's AI is reachable only from inside the login, unlike the data providers' AI access" and let the first body sentence carry the providers' side.

### 3. Exhibit 13 title

**Current:** "Exhibit 13. Copilot answers a question by choosing from thousands of registered tools and calling production Aladdin APIs, never giving investment advice"

**Trying to say:** Copilot's mechanism is: choose tools, call production APIs.

**Rewrite (14 words):** "Exhibit 13. Copilot answers a question by choosing from thousands of tools and calling production Aladdin APIs"

Twenty words and three ideas. "Never giving investment advice" is already the last box of the funnel and is in the body paragraph above ("will not give investment advice"), so it needs no place in the title. If the author wants it kept near the exhibit, add to the source note: "The last step is a tested guardrail: Copilot never gives investment advice[9], [16]."

### 4. Exhibit 13, funnel box 1 — minor

**Current:** "**One question**, plus what is on screen: the open app, portfolio and widgets go in as context. The talk's example is 'what is my exposure to aerospace in Portfolio 1?'[9]"

**Trying to say:** the question goes in with the screen state as context.

**Rewrite:** "**One question**, with the screen as context: the open app, portfolio and widgets go in with it. The talk's example is 'what is my exposure to aerospace in Portfolio 1?'[9]"

### 5. Exhibit 13, funnel box 3 — minor

**Current:** "**20 to 30 tools in play**: Copilot filters the registry by environment, user group and app, leaving 'say, 20 to 30 tools and agents.' That is because more than '40, 50 tools' would hurt performance[9]"

**Trying to say:** the registry is filtered down to a shortlist for each question.

**Rewrite:** "**20 to 30 tools shortlisted**: Copilot filters the registry by environment, user group and app, leaving 'say, 20 to 30 tools and agents.' More than '40, 50 tools' would hurt performance[9]"

"In play" is idiom; "That is because" points backwards at a reason that reads fine without the connector.

### 6. Exhibit 13, funnel box 4

**Current:** "**Plan and call the API**: the orchestrator (the component that runs the loop) iterates 'over a planning and action node' with GPT-4 function calling. Then output guardrails check for hallucinations[9]"

**Trying to say:** a planning loop picks and calls the API, then a guardrail checks the output.

**Rewrite:** "**Plan and call the API**: an orchestrator loops 'over a planning and action node' using GPT-4 function calling. Output guardrails then check the answer for hallucinations[9]"

The parenthetical defines "orchestrator" by "the loop", which the reader has not met either. "Loops" shows the mechanism in one word.

### 7. Exhibit 13, funnel box 5 — minor

**Current:** "**One answer**, never investment advice: Copilot's standing instructions (its system prompt) are tested so it will 'never provide investment advice'[9]; the product page says the same[16]"

**Rewrite:** "**One answer**, never investment advice: Copilot's standing instructions (its system prompt) are tested so it will 'never provide investment advice'[9], and the product page says the same[16]"

Semicolon to "and"; nothing else.

---

## Page 13

### 8. Exhibit 14 title

**Current:** "Exhibit 14. Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data. Aladdin has only a job advert that mentions MCP"

**Trying to say:** every provider in the comparison has public AI access or an AI announcement except Aladdin.

**Rewrite (13 words):** "Exhibit 14. Of nine providers a Studio buyer compares, only Aladdin has no public AI announcement"

Thirty-one words, two sentences, three ideas. The split (two rivals, six data and cloud providers) is already the body sentence just above the exhibit ("Six data and cloud providers ... offer a connector or an MCP server, and two system-of-record rivals have announced AI features"), and the job advert is already the body sentence before that and the Aladdin row itself. Nothing is lost. If the author wants the advert in the exhibit text, put it at the start of the source note: "Aladdin's only public mention of MCP is a job advert[65]."

### 9. Exhibit 14 column headers — minor

**Current:** "Provider | What is public | Receipt"

"What is public" names the content and passes. "Receipt" is the document's own term, used as a column header in Part 1 and in Exhibit 17, so it is met by now; no change. If a plainer word were wanted everywhere, "Source" would do, but change it everywhere or not at all.

### 10. Exhibit 14 cells, "What is public" column

The cells mix shapes: some are noun phrases, some have verbs, two use a colon or semicolon to stack a second fact. Read at speed the eye has to re-parse each row. Make every cell a sentence with the provider as subject (the provider's name is in the first column, so the subject can be "it" or implied; I give the full-subject version so each cell stands alone).

| Row | Current | Rewrite |
|---|---|---|
| SimCorp | "Agent Launchpad, announced 2026: prebuilt AI agents, and clients can build their own on SimCorp One's data layer" | "Agent Launchpad, announced in 2026, ships prebuilt AI agents and lets clients build their own on SimCorp One's data layer" |
| Arcesium | "AI features in Aquata, and an AI platform announcement" | "Arcesium has added AI features to Aquata and has announced an AI platform" |
| FactSet | "An MCP server for its data, which FactSet calls the first in its market" | "FactSet runs an MCP server for its data, which it calls the first in its market" |
| LSEG | "A collaboration with Anthropic and an MCP server; 90 customers connected by April 2026" | "LSEG's MCP server, announced alongside a collaboration with Anthropic, had 90 customers connected by April 2026" |
| MSCI | "'AI connectors' to its proprietary data" | "MSCI offers 'AI connectors' to its proprietary data" |
| S&P Global | "Credit Ratings added to its AI Data Portal, September 2026" | "S&P Global added Credit Ratings to its AI Data Portal in September 2026" |
| Snowflake | "A documented MCP server for Cortex Agents" | "Snowflake documents an MCP server for Cortex Agents" |
| Databricks | "Managed MCP servers, documented" | "Databricks documents managed MCP servers" |
| Aladdin | "None found. A Forward Deploy Engineer posting for Aladdin Data names 'Model Context Protocol (MCP), AI agents, and Copilot extensions'" | No change. Subject and verb are clear and the quotation is intact. |

The LSEG and SimCorp rows are the ones that fail the test outright (semicolon and colon stacking); the rest are tidy-ups for consistency.

### 11. Exhibit 14 source note — minor

**Current:** "Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources; State Street, Clearwater and Bloomberg have none in my sources, so they are not listed."

**Rewrite:** "Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources. State Street, Clearwater and Bloomberg have none, so they are not listed."

### 12. Exhibit 15 title

**Current:** "Exhibit 15. Inside the login buys governance; outside the login buys discoverability on rivals' terms"

**Trying to say:** the table weighs AI access inside the login (Copilot plugins) against AI access outside it (a public connector).

**Rewrite (12 words):** "Exhibit 15. For and against offering AI access inside the Aladdin login or outside it"

The current title is the conclusion, compressed: "buys" is a metaphor, "inside the login" has not been defined as a term (the body on page 12 uses "outside the login" once, in passing), and "on rivals' terms" needs the Against cell to unpack. A for/against table takes a descriptive title. The conclusion already opens the direction callout ("I would describe the Copilot plugin model publicly now") and can be stated there in plain words: "Inside the login, BlackRock keeps control; outside it, rivals set the terms of comparison." See item 15.

### 13. Exhibit 15 column headers

**Current:** "" | "Inside the login: Copilot plugins on production APIs" | "Outside the login: a connector or MCP server for the buyer's own AI tools"

**Trying to say:** the two options being compared.

**Rewrite:** "" | "Inside the login (Copilot plugins on Aladdin APIs)" | "Outside the login (a public connector or MCP server)"

The second header is 14 words with a colon; a header should name the option in a glance. The gloss in parentheses reads as a gloss, not as a second clause. "The buyer's own AI tools" is said in the For cell below. The blank corner cell is fine for a for/against grid.

### 14. Exhibit 15 cells

All four cells are strings of semicolon-separated fragments, and two open a sentence with "And". Each cell holds four or five separate points. Rewrite each as short sentences (or, better, render them as a bulleted list inside the cell, one point per line).

**For / Inside, current:** "Governance in one place; users keep their Aladdin permissions ('permission-dependent access'); guardrails against advice, tested in the system prompt; enterprise trust; a rollout BlackRock controls, team by team[16], [9]"

**Rewrite:** "Governance sits in one place. Users keep their Aladdin permissions ('permission-dependent access'). Guardrails against advice are tested in the system prompt. It carries the platform's enterprise trust. BlackRock controls the rollout, team by team[16], [9]"

**For / Outside, current:** "Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors. And it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make[7], [63], [40], [8]"

**Rewrite:** "Prospects can find it. Developers adopt it on their own. It signals an ecosystem. It answers the RFP question about connectors. It matches what FactSet, LSEG and MSCI now offer, which is what buyers compare against[7], [63], [40], [8]"

**Against / Inside, current:** "Prospects cannot see it, and nor can the AI tools that buyers already run. Rivals set the terms of comparison; the only public description of the plugin model is one conference talk[9]"

**Rewrite:** "Prospects cannot see it, and neither can the AI tools buyers already run. Rivals set the terms of comparison. The only public description of the plugin model is one conference talk[9]"

**Against / Outside, current:** "More to secure and more to support; buyers would read a partial catalog as the whole catalog. And the regulatory optics of outside AI tools drawing on a platform that will not give advice[16]"

**Rewrite:** "There is more to secure and more to support. Buyers would read a partial catalog as the whole catalog. Outside AI tools drawing on a platform that will not give advice would raise a regulatory question[16]"

"The regulatory optics of ..." has no verb and leaves the reader to supply "are bad". The rewrite says what the risk is.

### 15. Finding 3 direction callout

**Current, two sentences that fail:** "Said in BlackRock's own words, that description answers the RFP connector question better than an MCP server with a partial catalog." and "Exhibit 15 is the evidence; this is the fifth direction in Part 3."

**Trying to say:** a public description, from BlackRock, beats a half-built connector; the evidence is Exhibit 15; this becomes direction five.

**Rewrite:** "That description, in BlackRock's own words, answers the RFP connector question better than an MCP server with a partial catalog would." and "Exhibit 15 is the evidence. This is the fifth direction in Part 3."

The opener "Said in BlackRock's own words" dangles (it is the description that is said, not the sentence's subject on first read). The closing semicolon stacks two unrelated pointers.

**Also, length:** the callout is eleven sentences, the longest of the four. Sentences two to four ("Copilot's tools are production Aladdin APIs ... it never gives investment advice") repeat the body and Exhibit 13. The callout reads as one thought if they are folded into one: "I would describe the Copilot plugin model publicly now: production Aladdin APIs, each user's own permissions, and tested no-advice guardrails[9], [16]." That takes the callout from eleven sentences to eight. If Exhibit 15's title becomes descriptive (item 12), the conclusion it used to carry goes here too: "Inside the login, BlackRock keeps control; outside it, rivals set the terms of comparison."

---

## Page 14

### 16. Finding 4 headline

**Current:** "4. Buyers at BlackRock's own webinar said they want a core platform plus their own builds, and rivals are already selling to those buyers"

**Trying to say:** the buyer wants a core plus their own builds; that is the buyer rivals are winning.

**Rewrite (15 words):** "4. Buyers at BlackRock's own webinar said they want a core platform plus their own builds"

Twenty-three words and two findings joined by "and". The second half (rivals already sell to that buyer) is the last body paragraph of the finding, which opens "Rivals are selling to the same buyer", and the SimCorp wins are there with receipts; it does not need the headline. If the rivals point is the one the author wants in the headline instead: "4. Rivals are already winning the buyer who wants a core platform plus their own builds" (15 words), and the poll becomes the first body sentence, which it already is.

### 17. Exhibit 16 title

**Current:** "Exhibit 16. Attendees of BlackRock's Build vs. Buy webinar mostly run vendor or hybrid platforms, and compliance reporting is the first thing they would stop maintaining"

**Trying to say:** the two polls charted: where attendees sit, and what they would drop first.

**Rewrite (13 words):** "Exhibit 16. Webinar attendees mostly run vendor or hybrid platforms and would drop compliance reporting first"

Twenty-four words with a change of subject halfway ("attendees ... and compliance reporting is ..."). The rewrite keeps one subject with two verbs, which reads as one statement. "BlackRock's Build vs. Buy webinar" is in the headline paragraph, the source note and the pull-quote attribution; the title does not need the full name. The two side heads carry which poll is which.

### 18. Exhibit 16 side heads and axis captions — minor

**Current:** "Where firms sit today" | "What they would stop maintaining internally"; axis captions "Share of attendees, poll 1" | "Share of attendees, poll 3"

Both pass. One tidy-up: the body says "in house" and the right-hand chart's bar labels are the poll's own wording, so "What firms would stop maintaining in house" matches the body and gives the head its own subject instead of "they". The axis captions are clear and should stay.

### 19. Exhibit 16 source note — minor

**Current:** "Source: poll results as read out on the Build vs. Buy webinar replay, taken from the published captions[8]."

**Rewrite:** "Source: poll results read out on the Build vs. Buy webinar, from the replay's published captions[8]."

"As read out on the replay, taken from the captions" sources the same fact twice in one clause. The rest of the note (no attendee count; poll 2 not charted) is clear.

### 20. Pull quote (Schafer) — no change

Quotation intact, attribution clear.

### 21. Finding 4 direction callout — minor

**Current:** "Studio is the right kind of answer: the APIs, events and Data Cloud that Sewdass describes are the pieces in Exhibit 4. It is not yet a finished answer: the public catalog in Part 1 is mostly alpha, and the SDK is beta."

**Trying to say:** Studio has the right parts but they are not yet shipped at full status.

**Rewrite:** "Studio is the right kind of answer. The APIs, events and Data Cloud that Sewdass describes are the Studio pieces listed in Exhibit 4. It is not yet a finished answer, because the public catalog in Part 1 is mostly alpha and the SDK is beta."

Two colons in two sentences; "the pieces in Exhibit 4" points at a cross-reference where "the Studio pieces" says the meaning. The "right kind of answer / not yet a finished answer" pair is good and is kept.

---

## Page 15 (up to the Part 3 heading)

### 22. "What would change my view" heading and intro — no change

"What would change my view" and "Each finding rests on public facts, so a public fact could overturn it. I would revise:" both pass.

### 23. List item "Finding 2 again"

**Current:** "Finding 2 again, if a slide attributed the API-call growth to specific products."

**Trying to say:** a second thing that would overturn Finding 2.

**Rewrite:** "Finding 2, if a slide attributed the API-call growth to specific products."

"Again" makes the reader check whether this is a correction of the line above. Repeating "Finding 2" on its own line is enough; the list already reads as one condition per line. The other four items ("Finding 1, if ...") pass.

---

## The five changes that matter most

1. **Finding 3 headline (page 12).** Drop "AI front door" and the unanchored "theirs": "3. Aladdin's AI works only inside the login; data providers let outside AI tools reach their data." This also introduces "inside the login", which Exhibit 15 then reuses without explanation.

2. **Exhibit 14 title (page 13).** Thirty-one words and three ideas to thirteen words and one: "Of nine providers a Studio buyer compares, only Aladdin has no public AI announcement." The split and the job advert are already in the two body sentences above the exhibit.

3. **Exhibit 15 title, headers and cells (page 13).** Give the for/against table a descriptive title ("For and against offering AI access inside the Aladdin login or outside it"), shorten the two column headers to the option plus a parenthetical gloss, and break the four semicolon-chain cells into short sentences or bullets. Move the "buys governance / buys discoverability" conclusion into the direction callout, where it is argued.

4. **Finding 4 headline and Exhibit 16 title (page 14).** Both join two findings with "and" and change subject halfway. Headline: "4. Buyers at BlackRock's own webinar said they want a core platform plus their own builds" (the rivals point is the finding's last paragraph). Exhibit title: "Webinar attendees mostly run vendor or hybrid platforms and would drop compliance reporting first" (one subject, two verbs).

5. **Exhibit 14 "What is public" cells (page 13).** Make every row a sentence with the provider as subject; the LSEG and SimCorp rows currently stack two facts with a semicolon or colon, and the rest switch shape from row to row.
