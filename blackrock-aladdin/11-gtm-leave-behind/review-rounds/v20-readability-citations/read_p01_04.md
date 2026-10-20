# Readability read, v20, pages 1 to 4

Pages read as text (page_01.txt to page_04.txt) and as 90 dpi images. Types: 1 GARBLED, 2 HARD TO READ, 3 ALLUDING, 4 EXHIBITS.

## MUST FIX

**M1. Page 2, executive summary, last sentence of paragraph 2. Type 1 (dangling reference).**
Current: "Part 3 sets out this direction, what would have to be true for it to hold, and four pieces of marketing work that would follow."
Problem: "this direction" has no antecedent. The sentence before it is about API calls growing 17x. The direction (clients' AI tools acting on Aladdin under BlackRock's own controls) is only in the headline.
Rewrite: "Part 3 proposes a direction: let clients' AI tools act on Aladdin under BlackRock's own controls. It sets out what would have to be true for this to work. It ends with four pieces of marketing work that would follow."

**M2. Page 3, Part 1 opening, sentences 3 and 4. Type 1 (dangling reference, misleading).**
Current: "The organization is "around 7,000 people, with over 4,000 of those being engineers." They maintain "around 100 Aladdin front-end applications" [9]."
Problem: "The organization" and "They" have no clear antecedent. The nearest noun is BlackRock, so a reader takes 7,000 as BlackRock's headcount, which a BlackRock reader knows is wrong. It reads as an error.
Rewrite: "He said the Aladdin organization is "around 7,000 people, with over 4,000 of those being engineers." That team maintains "around 100 Aladdin front-end applications" [9]."
(Author: confirm at 1:53 of [9] that "the organization" is the Aladdin organization, and name it as the speaker does.)

**M3. Page 3, Part 1 opening against Exhibit 1. Type 1 (text contradicts nearby exhibit).**
Current text: "BlackRock sells Aladdin as four platforms that share one data language. They are the Aladdin platform, eFront, Aladdin Wealth and Preqin [13]."
Current exhibit title: "Exhibit 1. Of eight Aladdin products, Studio is the one for people who write code" and eFront row: "A private-fund platform holding Preqin [18]"
Problem: The text says four platforms with Preqin as one of them. The exhibit directly below says eight products, has no Preqin row, and puts Preqin inside eFront. The reader cannot tell whether it is four or eight, or where Preqin sits.
Rewrite (add one bridging sentence after the [13] sentence, and fix the eFront row):
- Text: "BlackRock sells Aladdin as four platforms that share one data language. They are the Aladdin platform, eFront, Aladdin Wealth and Preqin [13]. Exhibit 1 lists eight products sold across these platforms."
- eFront row: "A private-fund platform that now includes Preqin [18], with private credit analytics added in May 2026 [19]"

**M4. Page 3, Exhibit 2 title against its own note. Type 4 (title contradicts the exhibit).**
Current title: "Exhibit 2. The public APIs follow a trade from order to NAV"
Current note: "The public specifications cover the trade but hold no position or event API, and do not say in what sequence steps 4 to 6 happen." Step 4 cell: "None of the 54 is a position API".
Problem: The title says the APIs follow the whole trade. The exhibit and note say step 4 has no API and the order of steps 4 to 6 is unknown. The title overclaims what the exhibit shows.
Rewrite title: "Exhibit 2. The public APIs cover a trade from order to net asset value (NAV), except the position step"
Rewrite note: "The public specifications cover the trade. They hold no position API and no event API. They do not say in what order steps 4 to 6 happen."

## SHOULD FIX

**S1. Page 2, paragraph 1, sentence 3. Type 2 and 3 (jargon, makes reader infer the contrast).**
Current: "Aladdin's APIs also change the book."
Problem: "the book" is trader shorthand. "also" makes it sound as if the data providers' tools change the book too. The point (Aladdin's APIs write, not only read) is left to inference.
Rewrite: "Aladdin's APIs can also write, not only read."

**S2. Page 2, paragraph 1, last two sentences. Type 3 (the controls are never tied to the headline).**
Current: "Access is granted per API, to read or to write. Compliance runs on each order by default [6]."
Problem: The headline promises "the same controls BlackRock's own business runs on". The paragraph lists two controls but never says these are the controls an AI tool would work under.
Rewrite: "Access is granted per API, to read or to write. Compliance runs on each order by default [6]. An AI tool calling these APIs would work under the same controls."

**S3. Page 2, paragraph 2, sentence 1. Type 2 and 3 (semicolon join, "unique" with no stated subject).**
Current: "Letting AI tools act will not stay unique; SimCorp and Clearwater have announced AI agents [7, 8]."
Rewrite: "Aladdin will not be alone in letting AI tools act. SimCorp and Clearwater have announced AI agents [7, 8]."

**S4. Page 2, paragraph 2, sentence 2. Type 3 (alludes to the advantage instead of stating it).**
Current: "What BlackRock can show is its own use."
Rewrite: "BlackRock's advantage is that it already runs its own business this way."

**S5. Page 2, paragraph 2, sentence 5. Type 2 (two unrelated claims stacked, "Buyers" undefined).**
Current: "Buyers say AI is changing what they build, and BlackRock has told investors that API calls will grow 17x by 2030 [10, 11]."
Rewrite: "Buyers of investment software say AI is changing what they build [10]. BlackRock has told investors that API calls will grow 17x by 2030 [11]."

**S6. Page 2, Limitations box, sentence 1. Type 2 (package name used as if self-explanatory).**
Current: "the 54 API specifications inside 11 public asdk_plugin Python packages"
Rewrite: "the 54 API specifications inside BlackRock's 11 public Python plugin packages (named asdk_plugin)"

**S7. Page 1, cover subtitle. Type 2 (stacked, "why ... could" reads oddly, drops "the same").**
Current: "What public sources show, and why clients' AI tools could act on Aladdin under controls BlackRock's own business runs on"
Rewrite: "What public sources show. Clients' AI tools could act on Aladdin under the same controls BlackRock uses for its own business."

**S8. Page 1, cover footer. Type 1 (misparse: reads as "sources with AI agents").**
Current: "Independent analysis from public sources with AI agents. Not produced, reviewed or endorsed by BlackRock."
Rewrite: "Independent analysis of public sources, done with AI agents. Not produced, reviewed or endorsed by BlackRock."

**S9. Page 3, Part 1 opening, revenue sentence. Type 2 (compressed: "up 24 percent including Preqin").**
Current: "BlackRock's technology services and subscription revenue was $2.0 billion in 2025, up 24 percent including Preqin, the private-markets data firm bought in 2025 [12]."
Rewrite: "BlackRock's technology services and subscription revenue was $2.0 billion in 2025 [12]. It rose 24 percent, a figure that includes Preqin [12]. Preqin is the private-markets data firm BlackRock bought in 2025."

**S10. Page 3, Exhibit 1, Aladdin Copilot row. Type 1 (modifier attaches to "clients").**
Current: "A chat assistant available to all Aladdin clients that gives no investment advice [23]"
Problem: Reads as "clients that give no investment advice".
Rewrite: "A chat assistant available to all Aladdin clients. It gives no investment advice [23]"

**S11. Page 3, Exhibit 1, Aladdin Provider row. Type 2 ("they" could be clients or custodians).**
Current: "Links custodians and administrators to a client's Aladdin, and they pay BlackRock for it [25]"
Rewrite: "Links custodians and administrators to a client's Aladdin. The custodians and administrators pay BlackRock for it [25]"

**S12. Page 3, Exhibit 2, step labels and title. Type 4 (unexplained acronyms).**
Current: "Position in the IBOR", "Lot in the ABOR", "NAV"
Rewrite: "Position in the investment book of record (IBOR)", "Lot in the accounting book of record (ABOR)", "Net asset value (NAV)". If space is short, keep the short labels and add one line to the note: "IBOR is the investment book of record. ABOR is the accounting book of record. NAV is net asset value."

**S13. Page 3, Exhibit 2, Detail row, steps 1 and 5. Type 4 (spec field names used as if self-explanatory).**
Current step 1: "Posting takes whatIf and runCompliance [6]"
Rewrite: "An order can be posted as a test (whatIf) and with a compliance check (runCompliance) [6]"
Current step 5: "Retrieved from the ledger_a_summary table [6]"
Rewrite: "Lots are read from a ledger summary table (ledger_a_summary) [6]"

**S14. Page 4, Exhibit 3 title. Type 4 (names the topic, not the finding).**
Current: "Exhibit 3. Where Studio sits in Aladdin"
Rewrite: "Exhibit 3. Studio sits between BlackRock's applications and Aladdin's shared services, and the APIs carry their own controls"

**S15. Page 4, Exhibit 3, top row label. Type 4 (label misreads: clients appear to build BlackRock's applications).**
Current: "Who builds"
Rewrite: "Who builds on Studio"

**S16. Page 4, Exhibit 3 note, first part. Type 2 and 3 (semicolon joins, fragment, unexplained aside).**
Current: "For illustrative purposes only. Every box is named in the sources below; the AWS option is announced, not live. The 11 domains are the packages of BlackRock's public SDK; the specifications also name Dashboard and Risk Radar. Controls as in Exhibit 14."
Rewrite: "For illustrative purposes only. Every box is named in the sources below. The AWS option is announced, not live. The 11 domains are the packages of BlackRock's public software development kit (SDK). Dashboard and Risk Radar are also named in the specifications. Exhibit 14 shows the same controls."

**S17. Page 4, Exhibit 4, workspace item "Projects". Type 1 (dangling "one").**
Current: "Projects Personal or shared. OAuth applications and storage are set up under one"
Rewrite: "Projects Personal or shared. Sign-in applications (OAuth) and storage are set up inside a Project"

**S18. Page 4, Exhibit 4 note, end. Type 3 (alludes to the point that the grouping is the author's).**
Current: "BlackRock gives no count of pieces. The APIs page describes the catalog, guides, notebooks and samples but does not link them; the specifications link the guides to a portal behind a client login."
Also: "the SDK README 29, for the SDK and the lower group"
Rewrite: "The grouping into parts is mine. BlackRock does not give a count. The APIs page describes the catalog, guides, notebooks and samples but does not link them. The specifications link the guides to a portal behind a client login." And: "the SDK README [29], for the SDK and the workspace items"

**S19. Page 4, Exhibit 4, APIs box. Type 4 (spec id format shown without saying why it matters).**
Current: "Read and write Aladdin data. Every public specification's id starts agraph.<domain>"
Rewrite: "Read and write Aladdin data. Every public specification's ID begins agraph.<domain>, for Aladdin Graph [6]"

## OPTIONAL

**O1. Page 2, paragraph 2, sentence 4. Type 2 ("Copilot tool" is shorthand).**
Current: "Each Copilot tool matches an Aladdin API already in production [9]."
Rewrite: "Each action Copilot can take (a Copilot tool) matches an Aladdin API already in production [9]."

**O2. Page 2, heading. Type 2 (slang).**
Current: "How to read the receipts"
Rewrite: "How to read the sources"

**O3. Page 2 legend and every exhibit source line. Type 4.**
The black square printed before "Source:" in Exhibits 1 to 4 is the same mark the legend uses for grade P. Exhibit 3's source line cites speakers (grade S) after that square. A reader may take the square as a grade. Use a different mark, or none.

**O4. Page 3, Exhibit 2, "Where" cell for step 3 (Trade). Type 4.**
Current: "–"
Rewrite: "Not stated"

**O5. Page 3, Exhibit 2, Detail cell for step 3. Type 2 ("confirms" reads as a verb).**
Current: "Broker confirms via BrokerConfirmRoutingAPI [6]"
Rewrite: "Broker confirmations arrive through BrokerConfirmRoutingAPI [6]"

**O6. Page 3, Exhibit 2 note, last sentence. Type 2 ("them" is vague).**
Current: "Exhibit 5 counts them."
Rewrite: "Exhibit 5 counts the specifications by label."

**O7. Page 4, Exhibit 3, Copilot box. Type 2 ("inside them").**
Current: "Aladdin Copilot, inside them; each tool matches an Aladdin API already in production"
Rewrite: "Aladdin Copilot, inside these applications. Each Copilot tool matches an Aladdin API already in production"

**O8. Page 4, Exhibit 3, controls panel. Type 2 ("Dataset releases" is vague).**
Current: "A second approver. Dataset releases need a second check."
Rewrite: "A second approver. Releasing a Data Cloud dataset needs a second person to approve it."

**O9. Page 4, Exhibit 4, workspace items. Type 2 (unexplained ADC, S3, bucket, Space).**
Current: "ADC Admin Center Studio's screen for managing Data Cloud datasets"
Rewrite: "Data Cloud (ADC) Admin Center Studio's screen for managing Data Cloud datasets"
Current: "S3 storage integration File storage set up in a Studio Project, its bucket assigned to a user or project"
Rewrite: "S3 storage integration File storage on Amazon S3, set up in a Studio Project. Each storage bucket belongs to a user or a project"
"a Space" in "Studio notifications" is never defined. Add a short gloss or drop it if the source allows.

**O10. Page 4, Exhibit 4. Type 2 (two compute names).**
"Aladdin Compute" (top panel) and "Studio Compute" (workspace) look like two products. If they are the same, say so. If not, one line should say how they differ.
