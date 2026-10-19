# Review 3: machine-written tells, and how to make the prose read as one person's judgment

Reviewer perspective: an editor who specialises in spotting machine-written copy. The document says openly that AI agents pulled, transcribed and drafted, so the goal is not to hide that. The goal is that every sentence a reader meets sounds like Jacob deciding something, not like a model assembling evidence under instruction.

## Verdict

This is better than most AI-assisted drafts. Someone has already stripped the crude tells: there are no em-dashes in the body, no "leverage", "unlock", "robust" or "landscape" outside the titles of other people's press releases, no "notably" or "importantly", and a handful of sentences ("in custom-application land, proof from one firm counts even for a dissimilar buyer"; "that matters less than it looks"; "The specifications say more than their count") are unmistakably a person. What remains is structural, and it is the structure that will give the document away to a reader who has seen a lot of model output. The four findings share one headline template and one body shape (evidence, evidence, grey "What it suggests about direction" box that restates the headline). The enterprise-gating disclaimer is made five times in almost the same words, and the method disclaimer three times, which is what happens when a model is told a constraint and honours it in every section. The "X, not Y" construction appears nine times, twice with the identical pair. "The author" appears twelve times in the third person and then Part 3 switches to "What I would need from inside". "Own" appears 31 times, "already" 13. And in the one place where the reader most wants a view, the AI front door, the document offers a balanced For/Against table and a quick win that is a decision to make a decision. Fix the repetition, vary the finding shapes, write in the first person throughout, and take a position in Finding 3, and the document will read as one confident author who used good tools.

## Findings

### 1. The enterprise-gating disclaimer is made five times (pages 2, 3, 6, 8, 14)

Current text:

- p.2: "Enterprise gating is expected. Aladdin is enterprise software sold to large institutions, and gating documentation, sandboxes and credentials behind qualification is the normal model for that market; a qualified prospect gets them from BlackRock's solutions team. The right-hand column of Exhibit 6 describes the sequence after qualification, not an absence."
- p.3: "It is enterprise software, sold to large institutions through a solutions team; documentation, sandboxes and credentials follow qualification, which is the normal model in that market."
- p.6: "A qualified prospect gets documentation, a sandbox and credentials through BlackRock's solutions team; the right-hand column is that sequence, not a gap."
- p.8: "that fits how Aladdin is sold, through a solutions team to qualified institutions, after a conversation."
- p.14: "None opens the gate: documentation, sandboxes and credentials stay with the solutions team, after qualification." (and p.2 again: "None opens the gate.")

Why it reads as machine-made: a person who sells enterprise software knows gating is normal and says so once, without apology. A model that has been instructed "treat enterprise gating as the expected model" inserts the reassurance wherever the topic comes near, in near-identical phrasing ("documentation, sandboxes and credentials" four times; "solutions team" seven times). The repetition makes the author sound anxious about being read as a critic, which is the opposite of the confident effect intended.

Suggested change: say it once, on page 3, in the voice of someone who has sold this kind of software, and delete the other four. For example, on p.3: "Aladdin is sold the way enterprise platforms are sold: a conversation first, then documentation, a sandbox and credentials from the solutions team. Nothing in this document argues with that. What follows is what a prospect can see before the conversation, and where that leaves marketing." Then on p.6 cut "A qualified prospect gets ... not a gap" and let the column heading "After qualification" do the work. On p.8 end the sentence at "nothing can be run." On p.14 replace "None opens the gate: documentation, sandboxes and credentials stay with the solutions team, after qualification." with "None of them changes what a prospect can access."

### 2. The method disclaimer is made three times (pages 2, 15, 18)

Current text:

- p.2: "Public material only. ... Figures may be outdated, and there is no internal product context, so conclusions may be wrong for reasons the author cannot see."
- p.15: "On method: AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted; the author checked each claim against the document or recording it cites and takes responsibility for the reading. Public sources are limited, can be out of date and carry no internal product context, and machine transcription and synthesis are imperfect. The conclusions may be wrong for reasons the author cannot see, and the five questions above are where that would show first."
- p.18: "AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted the text. The author checked each claim against the document or recording it cites. Public material is limited, can be out of date and carries no internal product context; machine transcription and synthesis are imperfect; the conclusions may be wrong for reasons the author cannot see."

Why: "may be wrong for reasons the author cannot see" three times, and "pulled the pages, unpacked the packages, transcribed the recordings" three times, is a safety paragraph being re-emitted, not an author's caveat. Readers trust a caveat said once and plainly more than one that follows them around. The "Three corrections already made" paragraph is likewise duplicated word for word on pages 2 and 18.

Suggested change: keep the full statement once, on page 18, in the first person. Reduce the page 2 box to two lines: "Public sources only, read with AI agents and checked by me against each document; the register says which recordings are machine-transcribed. I have no internal context, so some conclusions will be wrong in ways I cannot see from outside." Delete the "On method" paragraph on page 15 entirely; the "five questions above are where that would show first" thought is the only new idea in it and belongs in the Exhibit 18 lead-in. Keep "Three corrections" on page 18 only.

### 3. "The author" twelve times, then "What I would need from inside" (pages 2, 6, 7, 10, 12, 14, 15, 18)

Current text: "conclusions may be wrong for reasons the author cannot see" (p.2); "Counts recomputed by the author from the files" (p.6); "the author's test of each platform's public pages" (p.7); "Counts are the author's tally" (p.10); "the author's reading of the Copilot page" (p.12); "the author's proposals" (p.14); "the author's questions" (p.15); "The author checked each claim" (p.18). Then the Part 3 sub-heading: "What I would need from inside" (p.14).

Why: third-person self-reference is one of the clearest signatures of a model writing about its user. The one first-person heading proves the author can speak directly, and the contrast makes the rest sound ghostwritten.

Suggested change: "I" throughout. "Counts are mine, recomputed from the files." "My test of each platform's public pages, with no account or payment, October 8, 2026." "My reading of the Copilot page, the LangChain talk and the announcements in Exhibit 14." "These are my proposals." "I checked each claim against the document or recording it cites." The leave-behind is from a named candidate to a named reader; there is no reason to hide behind "the author".

### 4. Four finding headlines on one template (pages 9, 10, 11, 13)

Current text:

1. "Public customer proof already exists, and it is viable even though it is not Studio-specific"
2. "BlackRock's growth story is API consumption and the whole portfolio, and Studio is the vehicle even when it is not named"
3. "BlackRock has built an AI front door and keeps it inside the platform, while data providers market theirs outside"
4. "Buyers say they want a core platform plus their own builds, and rivals are selling to that"

Why: every one is "[claim], and/while [concession or twist]", and two use the same "even though/even when it is not" turn. Headlines that all scan the same way are a reliable sign that one generator wrote them to one pattern. They are also long for headlines, because each is trying to pre-empt an objection.

Suggested change: vary the length and shape, and let the concession go into the body where it already is.

1. "Aladdin already has public customer proof. Studio can borrow it."
2. "BlackRock told investors its growth is API calls and the whole portfolio. That is Studio, unnamed."
3. "Copilot is Aladdin's AI front door, and it only opens from inside. FactSet, LSEG and MSCI have put theirs on the street."
4. "Buyers now ask for a core platform they can build on. SimCorp is answering in public; BlackRock has the answer and has not written it down."

### 5. Four "What it suggests about direction" boxes that restate the headline (pages 9, 10, 12, 13)

Current text:

- Finding 2 headline: "Studio is the vehicle even when it is not named." Box: "Studio is the vehicle for that story whether or not the name appears."
- Finding 1 body: "...are the natural first candidates for a named Studio story." Box: "Named proof for Studio can start where the relationship is already on the record."
- Finding 4 box: "The buyer's question and the product already match. The quick wins put the answer where the buyer is asking." (two sentences saying one thing)
- Finding 3 box: "The choice is deliberate and consistent with the governance message: permission-dependent access, content filtering, no investment advice."

Why: identical paragraph shape across all four findings (evidence paragraph, exhibit, evidence paragraph, grey box labelled "What it suggests about direction") is the single strongest structural tell in the document. Worse, each box repeats what the headline or the last body sentence already said, so the reader pays for the same thought twice. A person ends a section when the point has landed.

Suggested change: either drop the boxes and end each finding with one sentence the body has not yet said, or keep the box but fill it with the one thing you would say to the head of GTM across a table. For example:

- Finding 1: cut the box. "None of this is Studio-specific, and that matters less than it looks" plus the sentence after it is the ending.
- Finding 2: "If API calls are the number BlackRock wants investors to watch, Studio's name belongs next to it. Nobody has written that sentence yet. I would."
- Finding 3: see finding 11 below; this is where a view is owed.
- Finding 4: "The question Schafer describes has a one-page answer sitting in Exhibits 4 and 5. Write it and hand it to the solutions team."

Also drop the label "What it suggests about direction." It is a colon-label (see finding 8) and, used four times, a template marker.

### 6. "X, not Y" nine times, with two pairs repeated (pages 2, 5, 6, 7, 8, 9, 12, 14)

Current text: "the sequence after qualification, not an absence" (p.2); "that sequence, not a gap" (p.6); "the whole API layer, not one API" (p.5); "what they say a client receives, not tested" (p.7); "each vendor's model, not a score against Aladdin" (p.8); "trade press, not a JPMorgan or BlackRock document" (p.9); "The open question is timing and description, not access" (p.12); "A description, not access" (p.14); "not re-pulled" (p.9).

Why: the corrective "X, not Y" is a model's favourite way to sound judicious. Once or twice it is fine. Nine times, with "sequence/gap" and "description/access" each used twice, it becomes a tic that reads as defensive, because most of these are the author guarding against a reading nobody has proposed.

Suggested change: keep two at most (p.5 "Aladdin Graph is the whole API layer, not one API" earns its place because the name invites the mistake; p.9 "trade press, not a JPMorgan or BlackRock document" is a real provenance point). Rewrite the rest as positive statements: p.8 "The exhibit shows each vendor's access model; it is not a league table." becomes "Each row is a vendor's chosen model." p.12 "The open question is timing and description, not access" becomes "The question is when BlackRock describes how clients' own AI tools will reach Aladdin, and in whose words." p.14 "A description, not access: how Copilot's tools map to production APIs..." becomes "Describe in public how Copilot's tools map to production APIs..."

### 7. The subtitle triplet is restated three times in two pages (cover, page 2)

Current text: cover subtitle "What public sources show about the product, where BlackRock is heading, and the quick wins for marketing Studio"; p.2 first paragraph "This is what it looks like, what it says about direction, and the quick wins for marketing Studio."; p.1 and p.2 Part labels "What the public record shows / Four findings about BlackRock's direction and market / Quick wins for marketing Studio".

Why: a three-part frame announced on the cover, announced again in the first sentence, and announced a third time as the parts list is a model being faithful to its outline. The executive summary's first paragraph is currently a table of contents; a person would use that space to say the finding.

Suggested change: replace the p.2 opening paragraph with the point. "In about a day, an outsider with AI agents can see most of what Studio is: 54 public API specifications, an open-source SDK, and five BlackRock executives describing the same three parts on the record. What they cannot see is a single client saying they built on it, or the word Studio next to the growth number BlackRock showed investors. The quick wins fix those two gaps without opening anything."

### 8. Colon-label paragraph openers (pages 2, 9 to 13, 15)

Current text: "What was found." "What it says about direction." "The quick wins." (p.2); "Public material only." "Enterprise gating is expected." "Three corrections already made." (p.2 box); "What it suggests about direction." (four boxes); "On method:" (p.15); "A description, not access:" (p.14).

Why: bold-label-then-sentence is the shape of a model's structured output. Ten of them in one document is a pattern, not a style.

Suggested change: let the first sentence be the label. "What was found. Studio is Aladdin's developer and data layer" becomes "Studio is Aladdin's developer and data layer". "Enterprise gating is expected. Aladdin is enterprise software" becomes "Aladdin is enterprise software, and gating is how it is sold." Keep bold only where the reader genuinely needs a signpost; in an 18-page document with exhibit titles already doing that job, that is nowhere in the body text.

### 9. The quick-wins sentence on page 2 is a six-item semicolon chain

Current text: "The quick wins. Named proof from clients whose Aladdin relationship is already public; Studio's name on the API growth story; a written one-page version of the spoken message; an RFP-ready API answer; a decision on describing the Copilot plugin model; a "what is in the box" summary. None opens the gate."

Why: the semicolon has replaced the em-dash as this document's connector, and a six-item list with no ranking is an inventory, not a recommendation. A person would say which one matters most.

Suggested change: "Six quick wins, in the order I would do them: get one named client to say one Studio-specific sentence, starting with the funds and filers who have already named BlackRock in public; put Studio's name beside the API-call projection; write down the three-part definition five executives keep saying out loud; and give the solutions team a one-page answer to the API question buyers now put in RFPs. Two more, on Copilot and the catalog summary, follow in Exhibit 17."

### 10. Two of the three headline stats are about the process, not the subject (page 2)

Current text: "54 Public API specifications read, in 11 PyPI packages covering 301 operations"; "128 Recordings transcribed and checked, 121 of them from BlackRock's own channels and partner stages"; "17x Projected growth in API calls".

Why: "recordings transcribed and checked" is what an agent run reports when it finishes. It tells the head of GTM how hard the tools worked, not what was found. The number 128 appears nowhere else in the argument.

Suggested change: lead with findings. "17x: projected growth in API calls by 2030, the fastest-growing measure on the 2025 Investor Day slide." "$25.6m: what JPMorgan Chase paid BlackRock for Aladdin in 2025, up from $4.4m in 2017, in its own proxy statement." "0: times an executive said 'Studio' on 26 earnings calls since 2020." Move "54 specifications, 128 recordings" into the method line under the tiles.

### 11. Exhibit 15 and its box avoid the view the reader is paying for (page 12), and the quick win is a decision to decide (page 14)

Current text: Exhibit 15, "Two sides of the AI front door", For/Against on each side in balanced five-item lists ("Governance in one place; inherited permissions; no-advice guardrails tested in the system prompt; enterprise trust; a controlled rollout team by team" against "Discoverability; developer pull; an ecosystem signal; a ready answer to the RFP question about connectors; the terms FactSet, LSEG and MSCI now set"). Box: "The choice is deliberate and consistent with the governance message ... The open question is timing and description, not access: when BlackRock describes how clients' own AI tools will reach Aladdin, and in what words, while rivals set the terms of that comparison." Exhibit 17: "A decision on when and how to describe the Copilot plugin model publicly."

Why: a symmetrical pros-and-cons table followed by "the open question is timing" is how a model declines to commit. A senior technical PMM candidate who has read a LangChain talk, a job posting naming MCP, and three rival announcements has an opinion, and the reader wants to hear it, even hedged. "A decision on when and how to describe" is not a quick win; it is a meeting.

Suggested change: keep the exhibit but cut each cell to the two items that matter, and replace the box with a position. For example: "My read: BlackRock will not ship an outside connector until governance is solved, and it should not. But it can describe the plugin model it already has, in its own words, this quarter: Copilot's tools are production APIs with inherited permissions and tested no-advice guardrails. Said publicly, that is a stronger answer to the RFP connector question than an MCP server with a partial catalog, and it takes the terms of comparison back from FactSet and LSEG. Wait, and the Forward Deploy Engineer posting will be the public record of BlackRock's plan." Then rewrite the quick-win row to match: "Publish a description of the Copilot plugin model" with "What it takes: one page, product and compliance review, no new access."

### 12. Tacked-on verdict sentences that sound synthesized (pages 6, 8, 10, 13)

Current text:

- p.6: "These are the needs of a client's engineering team."
- p.8: "The message is consistent across speakers and years, so the positioning exists."
- p.10: "The investor story is told without the product's name." and three sentences later "Exhibit 12 is an observation about how the story is told."
- p.10: "Hosting moved the same way:"
- p.13: "The buyer's question and the product already match."

Why: each is a one-line abstraction appended after a run of evidence, the summarising reflex of a model closing a paragraph. "So the positioning exists" is especially odd: a positioning is not something that exists or not, it is something someone wrote. "Exhibit 12 is an observation about how the story is told" is a pre-emptive hedge against an unmade objection, and "Hosting moved the same way" connects cloud hosting to private-markets data with a "same way" that is not the same.

Suggested change: p.6: "The README is written for a client's engineering team: enterprise gateway settings, credential storage, three run modes. That is the right audience; it is also the only audience it reaches." p.8: "Five people, two years, one definition. The positioning is done; it has just never been written down." p.10: cut "Exhibit 12 is an observation about how the story is told" and "The investor story is told without the product's name"; the headline and the zero in the exhibit say it. p.10: replace "Hosting moved the same way:" with "Hosting is opening up too:". p.13: cut "The buyer's question and the product already match."

### 13. Lexical tics: "own" (31), "already" (13), "on the record" (7)

Current text, a sample: "BlackRock's own specifications" (p.2), "BlackRock's own channels" (p.2), "BlackRock's own webinar" (p.2), "BlackRock's own definition" (p.3), "BlackRock's own client video" (p.9), "BlackRock's own Build vs. Buy webinar" (p.13), "BlackRock's own professionals" (p.10); "already exists ... already public ... already on the record ... already true ... already match ... already on video ... already give ... already use"; "define Studio on the record" twice in six lines (p.8).

Why: "own" is doing the work of insisting the evidence is first-party, and "already" the work of insisting the wins are cheap. Repeated this often, both become noise, and a reader who notices starts to hear the generator.

Suggested change: cut "own" wherever the possessive already says it ("BlackRock's webinar" is BlackRock's own). Keep "already" where the contrast is real (p.9 "already exists") and cut it from the quick-wins table, where it appears four times in one column. Use "on the record" once, in the register key.

### 14. One flourish used three ways: "in those words / in what words / in rivals' words" (pages 12, 13, 14)

Current text: "and in what words, while rivals set the terms of that comparison" (p.12); "Extensibility is now an RFP question, asked in those words" (p.13); "prospects stop asking the question in rivals' words" (p.14).

Why: a good phrase, generated three times. The third one (p.14, as a measure) is the best and the most specific; a human writer would have noticed the repetition and kept that one.

Suggested change: keep p.14. On p.13 write "Extensibility is now an RFP question; Schafer uses the word." On p.12 cut "and in what words".

### 15. The Part 1 opening paragraph is assembled, not argued (page 3)

Current text: "Aladdin is the investment platform BlackRock built for itself and sells to other institutions. Its AI engineering lead put the scale this way at a LangChain conference in 2025: "BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries"; the organization is "around 7,000 people, with over 4,000 of those being engineers," who maintain "around 100 Aladdin front-end applications". BlackRock's technology services and subscription revenue was $2.0 billion in 2025, up 24 percent with Preqin. It is enterprise software, sold to large institutions through a solutions team; documentation, sandboxes and credentials follow qualification, which is the normal model in that market. BlackRock sells the platform as one engine with separate entry points, and Studio is the entry point for people who write code."

Why: five facts from four sources in a row, each with its citation, then the gating disclaimer, then the point. The reader gets the point last. This is the order a retrieval pipeline produces: facts, caveat, conclusion.

Suggested change: lead with the sentence that matters and let the facts support it. "Studio is the door into Aladdin for people who write code. Aladdin itself is the system BlackRock runs and sells: hundreds of clients in 70 countries, 4,000 of its 7,000 people engineers, about 100 front-end applications, $2.0 billion of technology services revenue in 2025. It is sold the way enterprise platforms are sold, conversation first; what follows is what a prospect can see before that conversation."

### 16. Page 8 closing paragraph: triplet plus the gating apology

Current text: "Learning about Studio from outside takes effort: the catalog is unpacked from packages, the definitions transcribed from recordings, and nothing can be run; that fits how Aladdin is sold, through a solutions team to qualified institutions, after a conversation."

Why: a three-part list for rhythm, a colon, a semicolon, and the fourth repetition of the gating line.

Suggested change: "From outside, Studio has to be reassembled: the catalog from packages, the definition from podcasts. That is normal for enterprise software. It is still a cost that marketing can remove with one written page."

### 17. Part 3 introduction: two triplets and the fifth disclaimer (page 14)

Current text: "Each quick win uses what is already public or already true inside BlackRock, works inside the enterprise selling model, and changes nothing about what a prospect can access. None opens the gate: documentation, sandboxes and credentials stay with the solutions team, after qualification. Product owns what is built and when; marketing owns positioning, stories and sales material; compliance checks the final version."

Why: "uses / works / changes" is a triplet built for balance, and the ownership sentence is a tidy tripartite division that no real organisation observes so neatly. Together with the gating line, the paragraph spends its whole length reassuring.

Suggested change: "Every win below uses something already public or already true inside BlackRock, and none changes what a prospect can access. Owners are my guess; the head of GTM will know better."

### 18. Provenance notes that read as an agent's run log (pages 9, 10)

Current text: p.9, Exhibit 11 source: "Weights and outcomes are from an earlier draft of this research (October 2026) and its reading of the notices, not re-pulled; the 2023 PBGC record was re-read on October 19, 2026." p.10, Exhibit 12 source: "Counts are the author's tally. Zero counts are reliable; other counts are approximate."

Why: the honesty is right and should stay; the phrasing ("re-pulled", "re-read on October 19", "Zero counts are reliable") is a pipeline reporting its state. A person says the same thing in fewer, warmer words.

Suggested change: p.9: "Weights and outcomes are as I read the notices on an earlier pass; I re-checked only the 2023 PBGC award on October 19." p.10: "My tally. I am sure of the zeros; the other counts could be off by one."

### 19. "put it in one line" (page 11)

Current text: "Copilot's tools are Studio's APIs; Microsoft's Adrian Crockett put it in one line on BlackRock's podcast: "There's no copilot without plug-ins"."

Why: "put it in one line" is a stock model lead-in for a quotation. Minor, but it is in the finding where voice matters most.

Suggested change: "Copilot's tools are Studio's APIs. Microsoft's Adrian Crockett, on BlackRock's own podcast: "There's no copilot without plug-ins.""

### 20. Keep: the sentences that already sound like a person

Current text, to keep unchanged and to use as the model for the rest:

- p.9: "None of this is Studio-specific, and that matters less than it looks. Studio is sold for custom applications on Aladdin, and a buyer wants to know that another institution built on the platform and stayed; in custom-application land, proof from one firm counts even for a dissimilar buyer."
- p.6: "The specifications say more than their count."
- p.6: "The SDK is the one piece that installs before any conversation."
- p.11: "Outside the login, the data market has chosen the other model."
- p.2 and the Receipt columns: "How to read the receipts". The word "receipts" is a human choice; keep it.
- p.14, Measure column: "prospects stop asking the question in rivals' words"; "First meetings that start past scope; prospects who arrive with the list". These are the most specific, most expert lines in the document.

Why: each has a judgment in it, a slight colloquialism, or a specific that only someone who has done the job would write. The rewrite of everything else should aim at this register.

## The three changes I would make first

1. Cut the gating disclaimer to one appearance (page 3) and the method disclaimer to one (page 18), and write both in the first person. This removes the most visible repetition and the "the author" voice in one pass (findings 1, 2, 3).
2. Break the finding template: rewrite the four headlines to different shapes, delete the "What it suggests about direction" label, and replace each box with either nothing or one sentence the body has not said (findings 4, 5).
3. Take a view in Finding 3. Replace the balanced Exhibit 15 box with what you would actually advise on the AI front door, and turn the Copilot quick win from "a decision on when and how to describe" into "publish a description" (finding 11). That is the page where the reader will decide whether a person or a pipeline wrote this.
