# Conceptual check: Exhibits 7 to 12 (pages 6 to 10, v23)

Scope: this checks whether each exhibit is conceptually right. Numbers were not re-checked against their citations. Evidence came from the local transcripts (04-transcripts), the product pages (drift22/dl_a), earlier check notes (citecheck, clientcheck), and four web lookups: the JPM 2026 proxy, the BLK Q2 and Q3 2026 call transcripts, and a search for any Aladdin MCP announcement.

| Exhibit | Verdict |
|---|---|
| 7 Four speakers, only Woodhead names all parts | SOUND WITH CAVEAT |
| 8 JPMorgan payments for Aladdin | SOUND |
| 9 Three public pension tenders | SOUND WITH CAVEAT |
| 10 Earnings-call term count | SOUND WITH CAVEAT (exhibit); the surrounding text overclaims |
| 11 Copilot query flow | SOUND WITH CAVEAT |
| 12 Ten of 11 providers have AI features or access | WRONG (title); MISLEADING (framing) |

---

## Exhibit 7: "Four speakers describe parts of Studio, and only Woodhead names them all"

**Verdict: SOUND WITH CAVEAT** (a judgment call, not a false picture).

- **The comparison is circular.** The "all parts" checklist (APIs and events, Data Cloud, developer tools) is Woodhead's own three-part definition. So "only Woodhead names them all" partly just says Woodhead's definition matches Woodhead's definition. The point the exhibit can honestly make is narrower: no other speaker gives a full list.
- **Goel arguably does name developer tooling.** The Parts column credits Goel with "APIs, events, Data Cloud". But the same transcript (source 41, `04-transcripts/part2-cloudfront-and-podcasts/050_...pensions.md`) has more:
  - He lists a third focus, "extending Aladdin into a platform."
  - He talks about "exposing some of the software and application that we're building". The exhibit quotes this but does not credit it in the Parts column.
  - He describes a governed platform for "citizen developers" that lets them build analyses and "promote these into production" via GitHub.
  - Caveat on that last point: the citizen-developer passage is framed around BlackRock's own 3,000 staff, so whether it describes something clients get is ambiguous.

  Read generously, Goel names all three parts in substance, though not as "developer tools" and never as "Studio". "Only Woodhead" holds only if "names" means "uses the words". The page 6 text ("Only Woodhead names every part, developer tools included") has the same problem.
- **Goel never says "Studio".** The source line discloses this, but the title still counts him as describing "parts of Studio". That is the author's mapping. It is fine as long as it is flagged, and it is.
- **Fair points.** Khara's row is fair: he says "the Aladdin studio estate", and "None by name" refers to the parts. The closing text, "Speakers since 2024 describe Studio as APIs and data access", follows from the rows.
- **Nit.** Exhibit 7 largely repeats Exhibit 6, one page earlier.
- **Fix if wanted:** "Only Woodhead lists all three parts in one definition". Credit Goel with "platform for developers (in substance)", or say why it is excluded.

## Exhibit 8: "JPMorgan Chase's payments for Aladdin rose from under $8 million a year to $25.6 million in 2025"

**Verdict: SOUND.**

- **The payments are for using Aladdin.** The 2026 proxy (source 52) says JPMorganChase paid BlackRock "approximately $25.6 million in 2025 to access and utilize its Aladdin® platform", in its section on transactions with 5% shareholders. So "payments for Aladdin" from a client is the right concept.
- **The chart matches its title.** The plotted values are 4.4, 5.0, 5.3, 6.8, 4.6, 7.6, 6.9, 14.7 and 25.6. The title says "under $8 million a year", which matches; it does not say "rising steadily", which would have been wrong because 2021 and 2023 dipped. Plotting each payment in the year it was made, from proxies filed the following year, is handled correctly. Showing the 2016 integration-services payment in grey keeps it out of the series.
- **The custody caveat is the right one.** The note covers the main risk: JPMorgan is also a custodian and an Aladdin service provider, so the payments may not be a plain client licence.
- **Small optional addition.** A reader may not know why a bank's proxy discloses this. It is a related-party disclosure, made because BlackRock holds more than 5% of JPM. One clause would pre-empt "is this cherry-picked?".
- **The text stays within what the chart shows.** It presents the chart as proof of Aladdin use, not Studio use. Page 8 explicitly says "None of this proof names Studio."

## Exhibit 9: "BlackRock won the tenders of three public pension bodies"

**Verdict: SOUND WITH CAVEAT.**

- **The title is accurate.** USAspending records both PBGC awards as "full and open competition, four offers". Nest chose Aladdin over six other bids. PPF awarded both lots to BlackRock.
- **These are risk-system purchases.** All three are mainly investment-risk systems: PBGC's "Investment Risk Management System", Nest's "investment risk platform", and PPF's risk and analytics lot plus an OMS, portfolio monitoring and risk lot. The page 8 text says the proof shows "another institution built on the platform and stayed". The exhibit does not show that:
  - Tenders show **buying**, not building.
  - Only PBGC (re-won in 2023) shows **staying**.

  The exhibit is fine. The sentence after it claims more than it shows.
- **Possible apples to oranges on the PPF price.** The PPF row sets the award "up to £74.0 million" against "the fund's estimate of up to £55 million" (source 59, contract notice, estimate £43m to £55m). Earlier notes (clientcheck) describe the PPF contract as 5 + 5 years over two lots.
  - The comparison is fair only if both figures cover the same lots, term and extensions. I could not open Find a Tender (HTTP 403) to confirm.
  - Even if they match, the side-by-side invites the reading "won despite being 35% over budget". The tender weighted technical fit at 85 and price at 6, which explains the gap. If the comparison stays, the weighting should sit next to it.
- **Wins only.** The earlier compendium had a known loss: LACERA 2020, won by MSCI. Leaving it out is defensible because this exhibit is about proof of use, not a win rate. It still means the exhibit cannot be read as "Aladdin wins pension tenders".
- **Nit.** PBGC is a federal pension insurer, not a pension fund. "Public pension bodies" stretches to cover it, acceptably.

## Exhibit 10: "No BlackRock executive said 'Studio' on any of 26 earnings calls, Q1 2020 to Q2 2026"

**Verdict: SOUND WITH CAVEAT (exhibit). The text around it claims more than the exhibit shows.**

**The exhibit itself:**

- **The absences are properly scoped.** They cover earnings calls in the named window, and the note says "a zero means the term appears in no transcript."
- **One window nit.** BlackRock's Q3 2026 call (14 October 2026) had already happened by the document's "as of October 2026". A third-party transcript (earningswhispers) shows none of the terms Studio, agentic, agent, API, Copilot or Data Cloud on it, nor on the Q2 2026 call (mitrade). So the conclusion holds, and the window could be 27 calls.
- **"Add-on" is a slight gloss.** The Q3 2022 source line reads "clients leveraging Enterprise Aladdin, alongside Aladdin Accounting or the Aladdin Data Cloud." Calling that "an add-on sold with Aladdin Enterprise" is close, but it is an interpretation.
- **Weak channel for the inference.** Earnings calls rarely name product sub-brands, so "0 mentions of Studio" is weak evidence about BlackRock's investor messaging in general. The Investor Day decks the document also cites are the better channel, and the text already uses them.

**The surrounding text (a conceptual issue):**

- **The section's thesis rests on an attribution.** The thesis is "BlackRock's growth story to investors runs through Studio". It depends on attributing the 2025 Investor Day "API calls (#) 17x", which the deck groups under "BlackRock + Aladdin", to Studio. That metric includes:
  - BlackRock's own internal use. BlackRock is Aladdin's biggest user, per the LangChain talk.
  - Machine-generated calls. Exhibit 11 itself shows Copilot calling production Aladdin APIs as tools, so Copilot and agent growth alone would drive API call counts.
- **The hedge disappears in the box.** The body text hedges with "I attribute". The "What this finding suggests" box on page 9 drops the hedge and states it as fact: "BlackRock's two growth bets both run through Studio." A BlackRock insider would likely say the 17x is a platform-wide machine-traffic metric, not a Studio adoption forecast. The box should keep the hedge, for example "the API-call forecast, which I attribute to Studio, …".

## Exhibit 11: "Copilot answers a question by picking from about two thousand tools and agents, then calling production Aladdin APIs"

**Verdict: SOUND WITH CAVEAT.** Checked against the talk transcript (`04-transcripts/part1-youtube-and-site/16_How_BlackRock_Built_Production_AI_Agents...md`). The flow's order and content are faithful: query plus screen context, the registry, filtering and access control down to 20 to 30 tools, a planning and action loop with GPT-4 function calling, then output guardrails. Gaps:

- **The input guardrail step is missing.** The talk says "the first node in that graph is an input guardrail node": moderation of off-topic and toxic content, and PII handling. It comes before filtering. The exhibit skips it, yet ends on a safety claim ("never investment advice"). The guardrails sit on both ends, not just the output.
- **Not every step is an API call.** The title says "calling production Aladdin APIs". But the registry has two onboarding paths: tools that map one-to-one to production APIs, and custom agents "for very complex workflows". The talk also mentions "communicating with the other agents". "Calls tools and agents, most of which wrap production APIs" would be exact.
- **The last box mixes two sources.** "One answer, never investment advice" combines a product-page promise (source 23) with an evaluation practice, and draws both as an output stage of the pipeline. In the talk, "you must never provide investment advice" is "a very dummy example" of a system-prompt behaviour they test. The flow does not guarantee it. Calling it a stated policy, enforced by guardrails and tested by evaluations, would be accurate.
- **The model may be out of date.** "Copilot uses GPT-4 function calling" is present tense from a May 2025 talk ("we're very reliant on GPT-4 function calling today"). By October 2026 it may have changed. "At the time of the talk" would fix it.
- **The text after the exhibit is an inference, and is labelled as one.** "So I infer that Copilot and Studio use the same APIs" is honest. Note the talk's "production APIs" are the internal services behind all ~100 Aladdin apps. The public Studio surface (301 operations, Exhibit 5) is likely a subset, so "same APIs" may be too strong. "Overlapping" is safer.

## Exhibit 12: "Ten of the 11 providers I compared have announced AI features or AI access to their data"

**Verdict: WRONG (title). MISLEADING (framing).**

- **The title's count is false for Aladdin.** The 11 are the 10 listed providers plus Aladdin, which is the implied "one". But Aladdin has announced AI features:
  - The Copilot page (source 23, `drift22/dl_a/p_aladdin-copilot.txt`) says "Introducing Aladdin® Copilot, now available to all Aladdin clients".
  - The same page announces eFront Copilot.
  - Exhibit 11, two pages earlier, describes Copilot in detail.

  So the title contradicts the document itself. A reader comes away believing Aladdin is the only one of the 11 with no announced AI, which is false. The author's real point is narrower: AI access for outside AI tools.
- **Apples to oranges within the rows.**
  - Two "system-of-record rival" rows are in-product agent platforms, the same kind of thing as Aladdin Copilot, not outside-tool access: SimCorp Agent Launchpad ("is to offer", so not yet shipped) and Clearwater's CWAN GenAI agents.
  - Aladdin's row shows only a job posting and leaves out Copilot.
  - So on like-for-like in-product AI, Aladdin (generally available to all clients) is arguably ahead of SimCorp (announced). The table hides that.
  - Bloomberg is filed as a "system-of-record rival", but its row is the data MCP for "licensed data". That is Bloomberg acting as a data provider, not as AIM/PORT.
- **Selection on the outcome.** State Street (Charles River / Alpha) is the most direct system-of-record rival, and it is excluded "because my sources show no AI feature it offers clients". Dropping a peer because it lacks the trait being counted inflates the count. If it is excluded, say "selected from providers that have announced AI access" rather than presenting the result as a tally.
- **Snowflake row: the route may already exist.**
  - Aladdin Data Cloud is built on Snowflake. Woodhead says ADC delivers to clients "through snowflake and through data sharing" into "their data ecosystem" (source 1, `part1-youtube-and-site/01_From_Analytics_To_Intelligence...md`).
  - So a client holding shared ADC data in its own Snowflake account can plausibly expose it to outside AI tools through the Snowflake MCP server the exhibit lists.
  - This is my inference; I have not tested it against Snowflake's documentation for shared databases.
  - "Aladdin has published no such route" is true for a BlackRock-published route. Set next to the Snowflake row without that link, it reads as "Aladdin data cannot reach outside AI tools", which is likely false.
- **The MCP absence is too absolute.** "Its only public mention of MCP is a job posting" (page 9 text and the Exhibit 12 note) is contradicted by the document's own source 10. On BlackRock's Build vs. Buy webinar, BlackRock's Michael Campos says "You can have your MCP, you can have your different APIs" (`drift22/dl_a/bvb.txt`). It is a passing mention, not a product, but the sentence needs a scope: "the only Aladdin product or hiring material I found that mentions MCP". A web search found no Aladdin MCP announcement, so "no published route" itself stands.
- **Nit.** S&P Global's row ("added Credit Ratings to its AI Data Portal") does not clearly show "a connector or an MCP server", which is how the text describes all six data and cloud providers.
- **Fix:**
  - Retitle, for example: "Six data and cloud providers and two system-of-record rivals let outside AI tools reach their data. Aladdin's AI stays inside the login."
  - Put Copilot in Aladdin's row.
  - Either move SimCorp and Clearwater to an "in-product AI agents" group alongside Aladdin Copilot, or drop them.
  - Note the Snowflake/ADC link.
  - Scope the MCP absence.
