# Fix-list audit: senior technical product marketer (conceptual accuracy)

Reviewer role: I tested each fix for whether its wording ties true facts to the right idea, the right heading and the right comparison. I spent most of my time on the evolved thesis and on Exhibits 3 and 14. I checked the key points against the OrderAPI spec, the Rosales and Valdez transcript (source 9), the Never Done podcast transcript (source 71), and Audits A, B, D and E.

## 1. Stance

The evolved thesis is the right move, and a go-to-market reader can act on it: "bring your own AI, use Aladdin's governed tools" is a real offer, with stated client demand, live competitor pressure and an existing asset behind it. But the proposed wording still fuses the two things the audit set out to separate. It uses one word, "same", for two comparisons: Copilot's registry permissions and the public APIs' OAuth scopes. Those belong to two different routes into Aladdin. The redrawn Exhibit 14 repeats that fusion in its "shared" middle layer. Several Tier 1 rewrites (2, 3, 4, 10) also join true facts to the wrong idea. Fix those, and v24 tells one clean story.

## 2. Verdicts

**Counts: 28 ACCEPT, 32 ACCEPT WITH CHANGE, 1 REJECT, 0 DEFER. Evolved thesis: ACCEPT WITH CHANGE.**

### The evolved thesis: ACCEPT WITH CHANGE

Proposed: "Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls."

What is conceptually sound:
- The split into server-side controls (which can carry over) and model-side controls (which cannot) is correct.
- Pointing at Copilot's governed tools gives a client's AI something it cannot get today by calling the APIs directly.
- Dropping "for its own business" is right, because Copilot and the apps are client products too.

What is not:
1. **"API controls" names the wrong comparison.** API scopes are the control on the public Studio route. Nothing public shows Copilot's tools going through OAuth scopes. Audit B: the registry controls "are environment, user group and app. They are not OAuth scopes." Fix 33 adds that most of Copilot's roughly 2,000 tools probably wrap APIs outside the 54 public ones, and those would have no published scopes at all. So "the same API controls [as Copilot]" brings back the fusion this thesis was meant to remove. The correct comparison for scopes is with any other Studio client program, not with Copilot.
2. **"The same permissions" has two possible readings.** One is "Copilot's level of access". The other is "the user's own Aladdin permissions". Only the second is true: Copilot calls "on behalf of the user", and the Copilot page says access is "permission-dependent".
3. **Studio is missing from the sentence.** The document is "Aladdin Studio from the outside" and is written for the go-to-market lead. Read alone, the thesis is a Copilot proposition. The reader needs to know which product carries it. The route is an MCP server or similar onto the registry, reached with Studio credentials, so Studio is the natural channel. That is the author's inference and should be labelled as one.
4. **"Act" has quietly become "call".** That makes the claim more honest, because public sources show Copilot answering questions, not acting. But the go-to-market story should then state its order: first, Aladdin's tools inside clients' own AI (this is what Smith Garson's "100%" supports). Second, actions, under Aladdin's own order workflow.

Replacement (cover, p2 headline and Part 3):
> "Studio could let clients' own AI tools call the governed tools Copilot calls, under each user's Aladdin permissions."

Supporting line for p2 or Part 3:
> "Copilot's own guardrails, planning and tests would stay with Copilot. A client's AI brings its own. The route, such as an MCP server, is my inference."

Also fix the cover heading. "What public sources show." currently sits directly above a proposal, which puts a direction under a heading for findings. Use: "What public sources show, and one direction they point to."

### Tier 1

| # | Verdict | Reason, and replacement wording where changed |
|---|---|---|
| 1 | CHANGE | Adopt the evolved thesis in the corrected wording above, and change the cover heading. |
| 2 | CHANGE | "On these APIs" re-asserts that Copilot uses the public APIs, which fix 33 says it probably mostly does not. "Most mapped to production APIs" is a proportion no source gives (Rosales names two onboarding paths and no split). "By calling about two thousand tools" is wrong too: Copilot shortlists 20 to 30. The wording also leaves out the governance, which is the asset the thesis relies on. Replace with: "BlackRock already runs an AI assistant on Aladdin. Copilot answers questions for BlackRock staff and clients in about 100 Aladdin applications. It draws on a registry of about two thousand tools and agents built by BlackRock's engineering teams. Each tool wraps an Aladdin API already in production, and the team that owns it sets which environments, user groups and apps can use it. Public sources show Copilot answering questions, not taking actions." |
| 3 | CHANGE | "Letting AI agents act" puts three different things in one category: outside AI running data tasks (Arcesium), a vendor's own agents (Clearwater) and client-built agents under vendor governance (SimCorp Launchpad). Only SimCorp's matches the thesis. "Controls it sells" is not a thing, because controls are not sold. "Over the production APIs … it sells" again implies Copilot uses the public APIs. Replace with: "Rivals are opening their platforms to AI agents. Arcesium's MCP server lets outside AI tools run data tasks, such as building pipelines. Clearwater runs its own agents inside its platform. SimCorp offers a portfolio management agent today and plans to give agents that clients build controlled access to SimCorp One data, under common governance. BlackRock already runs about two thousand governed tools behind Copilot." Use the same wording on p12. |
| 4 | CHANGE | "Many data providers … and some let them act" files Arcesium, a system-of-record rival in the report's own grouping, under data providers. The original sentence, read within its data-provider scope, was true. The sharper true contrast is the kind of action. Arcesium's outside AI acts on data pipelines, and Aladdin's write APIs reach investment actions. Replace with: "Many data providers now let outside AI tools read their data. Arcesium's MCP server also lets them run data tasks. Aladdin's APIs reach investment actions: they post orders and assign compliance rules to portfolios." (The colon introduces a list, so it does not join two sentences.) |
| 5 | CHANGE | The proposed "Aladdin user permissions add limits" asserts enforcement. Audit A finds enforcement implied, not specified, and only some operations name a permission. Replace the added sentence with: "The specifications also name Aladdin user permissions, which are set by function, action and portfolio." Keep "Each API has its own OAuth scopes, and most split read from write" and the deletion of "and per action". |
| 6 | CHANGE | The facts are right, but two of them are framed misleadingly. "A timeout can post the order before the check finishes" reads like a bypass, yet the spec marks such an order "Compl Pending". "Trades posted directly have no compliance setting" reads as "trades skip compliance", yet TradeAPI trades carry a read-only compliancePending flag. Replace the p2 text with: "Posting an order runs compliance by default. The caller can turn the check off, or set a timeout after which the order posts marked 'Compl Pending'. Whether either needs a separate permission is not public." Move the trade point to p5: "The trade API's requests have no compliance option. Its trades carry a compliance-pending flag." In Part 3, tie these facts to the thesis (labelled as inference): "A tool BlackRock builds would set these options itself, so the client's AI model would not choose them." |
| 7 | CHANGE | The proposed p8 text contradicts itself: "The slide does not say who makes these calls. They include BlackRock's own applications and Copilot." If the slide does not say, the second sentence has no source. Use: "The slide counts calls across BlackRock and Aladdin and does not say who makes them." The fix also drops "runs through Studio" without giving finding 2 a new claim. New heading: "2. BlackRock tells investors Aladdin is growing as a platform, but rarely names Studio". New p9 box: "BlackRock lists 'Aladdin as a platform' among Aladdin's growth drivers and tells investors it is 'empowering clients with data and APIs'. Studio is the product clients use to build on that platform, so Studio could carry the platform story by name." Source it to slides 33 and 35, the 10-K and the Studio page. Keep the p2 sentence as proposed. |
| 8 | ACCEPT | It separates technical access from support and from a packaged connector. This becomes the solid "today" route in Exhibit 14. |
| 9 | CHANGE | Right evidence, but the attribution is too narrow. Crockett, not BlackRock, raised the idea. "100%" answered a list of four options: using BlackRock's copilot, using its orchestrator, injecting client plug-ins into it, or exposing Aladdin's plug-ins in a client's custom copilot. "We are hearing that from our clients" followed a similar list. Her surname is Smith Garson, not Garson. The exchange supports demand for plug-ins (tools), not for AI that acts, so do not cite it for Part 3's "want AI tools that act". Wording: "In November 2024, on BlackRock's podcast, Microsoft's Adrian Crockett said clients might want Aladdin's plug-ins in their own copilots. Syril Smith Garson, BlackRock's Head of Product for AI, answered '100%', and later added, 'we are hearing that from our clients' 71." Drop the job posting from Exhibit 14 rather than re-describe it. In Exhibit 12, describe it accurately: "an internal data-platform posting that names MCP for onboarding tasks". |
| 10 | CHANGE | "Approval before any order posts" puts the human control at the wrong step and invents a new one. The spec's existing control comes after posting: posting does not trade, a portfolio manager authorises, a trader activates, and authorisation is read-only through the API (fix 66). Replace with: "A governed route for clients' AI tools: the same registered tools Copilot calls, under each user's Aladdin permissions. Orders a tool posts still need a portfolio manager's authorisation before they trade." The "What it is" cell should say that Copilot's guardrails stay with Copilot. |
| 11 | CHANGE | The redraw brief is the most important fix and is conceptually unsound in three places (section 3 gives the full redraw). (a) The "shared server-side layer" puts registry permissions under the client's existing apps, which do not use the registry, and API scopes under Copilot, which fix 11's own problem statement says is unevidenced. (b) The client AI route appears only as dashed and proposed, but fix 8 says a client's AI can already call the public APIs today. (c) Model-side controls go in a bottom band. In a layered diagram the bottom reads as the foundation, and Copilot's guardrails are a foundation for nothing. "Planning" is a function, not a control. |
| 12 | CHANGE | Side by side is right. Two parts are missing. The controls column must attach to the Studio side only, because the spec controls govern Studio callers. The black band's subtitle, "reached through the 11 public API domains", says the apps and Copilot reach the services through the SDK's packaging. Change it to "Aladdin's shared services" and put "54 public APIs in 11 domains" on the Studio box. |

### Tiers 2 to 4

| # | Verdict | Reason, and replacement wording where changed |
|---|---|---|
| 13 | ACCEPT | Orders sit in the Order Monitor, and Explore's what-if is a different idea. |
| 14 | CHANGE | "Connector" alone is ambiguous, because Data Cloud is itself a Snowflake connection. Use: "BlackRock has published no MCP server or other connector for outside AI tools." |
| 15 | ACCEPT | A factual rescore. |
| 16 | CHANGE | "Most of the 11" counts Aladdin in the denominator, and the two sentences read as mutually exclusive groups (Arcesium does both). Use: "Eight of the 11 providers let outside AI tools connect through an MCP server or connector. Aladdin's AI, like SimCorp's and Clearwater's, works inside its own platform." The count of 8 is Arcesium, Bloomberg, FactSet, LSEG, MSCI, S&P, Snowflake and Databricks. Verify it before use. |
| 17 | ACCEPT | It compares like with like. |
| 18 | ACCEPT | The title now matches the scores. |
| 19, 20 | ACCEPT | Correct descriptions. |
| 21 | CHANGE | "Used before" implies file transfer is retired, but ADX (Exhibit 4) still does bulk transfer. Use: "Data Cloud is 'much simpler' than sending flat files over FTP." |
| 22 | CHANGE | "Read what follows" claims reads for execution, confirmation and settlement, which do not exist. Use: "The public APIs post orders and trades and read lots and NAV. None returns positions." |
| 23 | CHANGE | It breaks the semicolon rule ("The engine runs it; a named team…"), and "named team" goes beyond the source, which shows violation owners. Use: Who: "Runs automatically. Violation owners resolve the results." API: "OrderAPI (runCompliance), with ViolationAPI to resolve". |
| 24 | ACCEPT | "A copy of the IBOR" fixes the book-of-record misreading. |
| 25 | CHANGE | The causal "because" link needs to be explicit. Use: "…because Studio is sold for building on Aladdin, and a buyer who builds on a platform wants to know that other institutions chose it and kept it." |
| 26 | CHANGE | "Keep pension funds as an Aladdin reference only, 'if they use Studio'" contradicts itself. Use in Exhibit 15 row 3: "One client willing to be named: a client whose engineers have contributed to the SDK." Keep pension funds in Part 2 as Aladdin references only. |
| 27 | CHANGE | It breaks the semicolon rule, and it leaves out the fact that most changes the chart's meaning. Use: "Disclosed because BlackRock owns more than 5% of JPMorgan. The proxies do not say what the payments cover. JPMorgan is also a custodian that connects to Aladdin. A separate line for BlackRock information services appears through the 2024 proxy and not after." |
| 28 | CHANGE | "From draft through review to approved" still implies a sequence, which is the problem the fix names. Use: "Compliance rule assignments carry a review state, such as draft, review required or approved." |
| 29 | CHANGE | The same error as 28: "move from open to authorized to confirmed" implies an enforced sequence, yet manualStateCycle lets the caller create flows already authorised or confirmed. Use: "Capital flows need the user's Aladdin cash permissions and record who authorised and approved them." |
| 30 | ACCEPT | "Can route" and "or in Studio Compute" are accurate. |
| 31 | CHANGE | "Most of them production Aladdin APIs" invents a proportion. Use title: "…then calling tools that wrap production Aladdin APIs, and agents". Keep the rest. Optional: shade the registry and filter step as "server side" and the guardrail, planning and output steps as "inside Copilot", to match Exhibit 14. |
| 32 | CHANGE | The proposed heading compares unlike things: Aladdin's in-platform assistant against other providers' outside access. That is the same flaw fix 16 corrects in Exhibit 12. Use: "3. Many providers let outside AI tools connect. Aladdin's AI works inside Aladdin." |
| 33 | CHANGE | "Copilot and Studio's public APIs run on the same Aladdin Graph runtime" asserts that Copilot runs on Aladdin Graph, which no source says. Use: "Copilot's tools wrap Aladdin APIs already in production. Studio's public APIs run on Aladdin Graph, BlackRock's firm-wide API runtime, and some back BlackRock's own screens, such as Risk Radar. Whether Copilot's tools use the public APIs is not public. With about two thousand tools and agents against 54 public APIs, most probably do not." Note that this sentence is why the thesis must name the registry route, not the public APIs. |
| 34 | CHANGE | Moving Bloomberg to the data group in Exhibit 12 while it stays under investment platforms in Exhibit 17 would group the same firm two ways. Keep it in place and add: "Its MCP server serves Data License content." Reword the other rows to the source, as proposed. |
| 35 | ACCEPT | The rescore and legend note make the premise explicit. |
| 36 | CHANGE | It breaks the semicolon rule. It also adds a sentence where one should be replaced: "may compete with Aladdin" stays and still frames partners as competitors. Replace that sentence with: "Exhibit 17 puts Studio beside 10 platforms as benchmarks for developer access. Several also work with Aladdin. Aladdin Data Cloud runs on Snowflake." |
| 37 | CHANGE | Under the side-by-side layout from fix 12, ending the column "at the shared-services row" still sets it beside BlackRock's apps and Copilot. Attach the controls to the Studio box. Keep the two-way Data Cloud and ADX and "about two thousand tools and agents". |
| 38 | CHANGE | The Portal fix leaves out the problem it names (only "guides" are sourced), and it breaks the semicolon rule. "Partly run by BlackRock" is an inference. Use: Admin Center: "The screen for Data Cloud datasets. Some of its API operations are for BlackRock's internal use." Portal: "Guides, behind a client login." Add the catalog, dictionary, notebooks and samples only where a source ties them to the portal. Governance: as proposed. |
| 39, 40 | ACCEPT | They mark an aim as an aim and a selection as a selection. |
| 41 | CHANGE | It breaks the semicolon rule. It also keeps a client's merged code changes in the "Get help" row, which the conceptual check said is the wrong category (it is not help a prospect can get). Column: "After becoming a client", as proposed. Get help, public cell: "No public support channel. The SDK's support file has headings but no channels listed." Move the merged changes to the Build row. |
| 42 | CHANGE | Widening the window to Q3 2026 means recounting all six terms, not only Studio. "AI agent or agentic: 0" on a Q3 2026 call is the row most likely to change. Also update p8's "26 calls … second quarter of 2026" and the note's "six and a half years". |
| 43 to 50 | ACCEPT | Precision fixes that keep the idea right. Fix 45 must also remove "fastest" from the p9 box. |
| 51 | CHANGE | The proposed sentence is now generic and repeats "hundreds of Aladdin clients" from source 9 one line earlier. Delete it, which also saves a line on page 12. |
| 52 | CHANGE | The wording is right, but the sentence sits in the p12 list of controls a client's AI "would work under". The evolved thesis says AI-graded tests stay with Copilot. Keep "Copilot's system prompts are tested daily by AI judges", but move it next to the statement that Copilot's own guardrails stay with Copilot. |
| 53 to 59 | ACCEPT | Correct scoping and qualifiers. |
| 60 | ACCEPT | It keeps "public" honest. |
| 61 | REJECT | It adds a component that no source describes. A go-to-market reader can do nothing with "not described publicly". |

## 3. Fixes the list gets wrong

**New conceptual distortions**
- **Thesis (1) and the Exhibit 14 brief (11):** "same … API controls" and a "shared" middle layer that includes both API scopes and registry permissions. This joins two routes, each with its own gate, into one layer, which is the merge the audit set out to undo.
- **11, the routes:** the client AI route is drawn only as dashed and proposed. That contradicts fix 8, which says it exists today. The real contrast for a buyer is between two routes. Today's direct route lets the client's code choose compliance options. The proposed route uses tools whose parameters BlackRock sets and whose use the registry gates.
- **11, the bottom band:** the model-side band is placed as a foundation layer, and it lists "planning" as a control.
- **2 and 31:** "most mapped to / most of them production Aladdin APIs" is a proportion no source gives.
- **2 and 3:** "on these APIs" and "production APIs … it sells" re-assert that Copilot uses the public APIs, which contradicts fix 33.
- **3:** "letting AI agents act" groups outside-AI data tasks, a vendor's in-platform agents, and client-built agents under vendor governance as one thing.
- **4:** files Arcesium under "data providers".
- **6:** the timeout and trade wording reads as bypasses, without the "Compl Pending" status and the compliancePending flag that the spec gives.
- **7:** "does not say who … They include …" contradicts itself, and finding 2 is left without a claim.
- **9:** attaches "100%" to one option when it answered a list of four. It names her as "Garson".
- **10:** "approval before any order posts" puts the human step before posting. The existing Aladdin control comes after posting and before trading.
- **28 and 29:** the wording implies an enforced sequence, which is the error both fixes say they correct.
- **32:** the heading compares an in-platform assistant with outside-AI connectors.
- **33:** "Copilot … run on the same Aladdin Graph runtime" is unsupported.
- **34:** regroups Bloomberg in one exhibit only.
- **38:** the Portal wording does not fix its own stated problem.
- **41:** keeps help that a prospect cannot get in the "Get help" row.
- **42:** widens the window without recounting the other terms.

**Breaks of the writing rules (semicolons joining two sentences)**
- 23 ("The engine runs it; a named team resolves violations")
- 27 ("…cover; JPMorgan is also a custodian…")
- 36 ("…developer access; Aladdin Data Cloud runs on Snowflake")
- 38 ("…samples; the portal sits behind a client login")
- 41 ("…no channels; the maintainers merged…")

None of the proposed wording uses an em-dash or the banned word.

**The Exhibit 14 redraw I would use** (it should fit the present footprint if fix 51's deletion and a tighter Part 3 free the space):
- **Title:** "Exhibit 14. A client's AI tool can call Aladdin's public APIs today. A governed route would let it call Copilot's tools under each user's permissions."
- **Top row:** "Built by BlackRock, used by BlackRock and clients" (About 100 apps; Copilot) beside "Built by the client" (Its applications; Its AI tools).
- **Attached to the Copilot box only:** "Stays inside Copilot: input and output guardrails, planning, AI-graded tests."
- **Gates row:** under Copilot, "Plugin registry: each tool enabled by environment, user group and app". Under the client column, "Studio credentials and API scopes".
- **Arrows:**
  - client applications go to the Studio gate (solid);
  - client AI tools go to the Studio gate (solid, "possible today, with no AI support published");
  - client AI tools go to the registry (dashed, "proposed: for example an MCP server. My inference").
- **Base:** "Aladdin's production APIs and services. Calls carry the user's Aladdin permissions. Orders run compliance by default and need a portfolio manager's authorisation before they trade." Add a small note: "Studio exposes 54 of these APIs publicly. Whether Copilot's tools use them is not public."
- **Legend:** covers both boxes and arrows.

**Exhibit 3 under fix 12:** sound only with the two additions in my verdict on 12: the controls attach to Studio, and the band subtitle is rewritten. Optional: show "tool registry" under the Copilot box so Exhibit 14 can refer back to it.

## 4. What the list leaves out

1. **The cover heading** places the thesis under "What public sources show". (Covered under the thesis verdict.)
2. **Part 3's three conditions are now the wrong way round.** Under the evolved thesis, BlackRock would open tools it built to AI models it did not build, not "open its controls to tools it did not build". A new condition is also needed: BlackRock would have to make available tools that wrap APIs not public today. The first condition should follow the demand evidence: "Clients would have to want Aladdin's tools inside their own AI tools, and later want those tools to act."
3. **The p12 text still says "What BlackRock can show is its own use."** Fix 11 relabels the exhibit but not the text. Use: "What BlackRock can show is Copilot."
4. **Exhibit 15 row 4** demos a rebalance "through the order API" with the client's AI as the caller. That is the direct route, not the governed one the thesis proposes. Run the demo through a BlackRock-built tool that posts a what-if order with compliance on, then have a portfolio manager authorise it in the order workflow. **Row 1** can now answer "how a client's own AI tools would connect" with today's facts (fix 8).
5. **The direction box on p10** proposes publishing "the tested guardrails that block investment advice". Under the evolved thesis, what clients' AI needs published is the tool catalogue and per-tool permissions, because guardrails stay with Copilot. Rewrite the box: "BlackRock could publish which tools Copilot's registry holds, which production APIs each wraps, and which user groups may use each."
6. **SimCorp Launchpad (evidence 69)** makes the same offer, with governance and an audit trail. The report must say so plainly, and the differentiator must be what BlackRock has and SimCorp has announced: about two thousand tools already running across about 100 apps. Otherwise a BlackRock reader will raise it first.
7. **The p2 facts in fix 6 should connect to the governed-tool idea** (see my fix 6), or they read as reasons for doubt with no answer.
8. **Evidence 64 (Risk Radar and Admin Center on public APIs)** belongs in Exhibit 3's Studio note as well, as the one public link between BlackRock's screens and the public APIs.

## 5. Top 5 recommendations, in priority order

1. **Adopt the evolved thesis in this form:** "Studio could let clients' own AI tools call the governed tools Copilot calls, under each user's Aladdin permissions." Drop "API controls" as a comparison with Copilot, label the MCP route as inference, and retitle the cover line "What public sources show, and one direction they point to."
2. **Redraw Exhibit 14 with two client-AI routes.** The direct route through Studio credentials is solid and exists today. The governed route through the registry is dashed and proposed. Give each route its own gate over a common base of user permissions and the order workflow. Attach Copilot's guardrails, planning and tests to the Copilot box, not to a bottom layer. Make the legend cover arrows.
3. **Rewrite fixes 2, 3, 4 and 10 so they agree with the thesis.** Copilot answers questions using about two thousand governed tools. Rivals' "acting" is three different things. Aladdin's write APIs reach investment actions. A human authorises after posting and before trading.
4. **Realign Part 3 and Exhibit 15 (not on the list).** The conditions should open BlackRock's tools to clients' models and expose tools over APIs not public today. Change "its own use" to "Copilot". Run the row 4 demo through a governed tool. Name SimCorp Launchpad as the competitor making the same offer.
5. **Fix Exhibit 3 with the side-by-side layout, controls attached to Studio only, and the band subtitle rewritten.** Then clear the five semicolon breaks (23, 27, 36, 38, 41) and the two invented-sequence wordings (28, 29) before anything goes into v24.
