# Three-page brief: production notes

- **Built from:** `nine-targeted-edits/Aladdin_Studio_Prep_2.html`, by `build.py`.
- **Reused from Prep 2:** the head (embedded Barlow fonts and colour tokens) and the chevron style of the original Exhibit 2.
- **Sources:** renumbered 1 to 17 in order of first use. Each superscript links directly to the source. Each page ends with a source line for that page. `source_map.txt` maps each brief number to its Prep 2 number.

## Where the text departs from the supplied wording, and why

1. **Page 1, Studio definition.** The paragraph now uses the two sentences you supplied in the second round. The second sentence keeps Woodhead's framing ("the experience that allows clients to treat Aladdin as a platform") and cites him and the Studio page.
2. **Page 2, Sewdass.**
   - **Change:** "shared data foundations" became "foundational data".
   - **Why:** her words are "that backbone foundational data that supports both publics and privates workflows". The word "shared" is not in the source.
3. **Page 2, Arcesium.**
   - **Change:** the text keeps Prep 2's wording, "added AI features to Aquata, including an MCP server that connects external AI tools to client data", and cites Prep 2 source 75 only.
   - **Why:** the earlier audit found the Aquata MCP server generally available to Aquata users, so "announced … intended to" would understate it. Prep 2 source 76 supports Arcesium's separate AI platform launch, which the brief does not mention, so it is not cited.
4. **Page 3, workstream 1 evidence.**
   - **Change:** "buyers ask increasingly detailed questions" became "questions about API suites and data-platform connectivity have become more prominent in RFPs".
   - **Why:** this is Schafer's claim ("that part of the RFP has become much more prominent"). The source does not say the questions are more detailed.
5. **Sentences joined with semicolons were split into two sentences:** the limitation, the method note, the enterprise-gateway finding and the developer-tools caption. Em-dash callouts became figure boxes.
6. **Page 1, intro.** The intro has two sentences, as permitted. The second keeps every limitation.
7. **Page 1, the limitation sentence.** It sits in the same grey box as the method note, to fit the page.

## Citations added beyond the listed sources

- **Janus Henderson 10-K (Prep 2 source 53)** and **the EDGAR full-text search (Prep 2 source 49)**, on workstream 2's evidence. These are the sources behind Prep 2's Finding 1. The company is not named in the text.
- **Rosales and Valdez (Prep 2 source 9)**, on the technical note about Copilot's tool-registry rules and guardrails.

## Accuracy checks (the ten requested)

1. Studio is drawn as three groups of capabilities above a band of Aladdin services. No applications, layers or Copilot appear in the diagram.
2. The 54, 301 and 11 counts are scoped to "the public packages examined, not necessarily Studio's full API surface".
3. Public APIs, Copilot's tools and Copilot's tool registry are kept separate. Copilot appears only in the page 3 technical note.
4. The OAuth wording is limited to "API-specific OAuth scopes". Nothing claims how permissions are enforced.
5. The what-if and compliance options are described as API settings, not as a workflow. The rebalance demo is not included.
6. The page 3 note states that external AI tools do not automatically inherit Copilot's tool-registry rules or AI guardrails.
7. "Announced" (SimCorp), "added" (Arcesium) and "launched" (Bloomberg) are kept distinct. The takeaway rules out parity and ranking.
8. Nothing from Exhibit 17, the scorecard, is included.
9. No Aladdin client is named as Studio proof. Workstream 2 says that named Studio examples are limited.
10. The poll is labelled "directional webinar-attendee responses, sample size not disclosed, not a representative industry survey".

## Words per page

These counts include diagram labels and captions and leave out each page's source line:

| Page | Words |
|---|---|
| 1 | 438 |
| 2 | 383 |
| 3 | 355 |

Body copy alone is about 330, 300 and 300 words.

## Second round

- **Date line:** now reads "Research conducted October 2026". The method note now reads "Public-source review, October 2026." The source lines keep each source's own check date.
- **Page 1 introduction:** replaced with the supplied two-sentence version, keeping its citations.
- **Page 3:** three validation questions per workstream.
  - Workstream 1's first question now covers partner integrations: "Which questions and partner integrations, such as Snowflake and Databricks, recur in deals?"
  - Workstream 3's second question keeps permissions and safeguards: "What can the product safely support, and under which permissions and safeguards?"

## Third round: what Studio lets clients do

- **New section on page 1:** "What these capabilities enable" replaces the two technical observations. It opens with the extensibility point, then gives the supplied three items:
  - Extend investment workflows
  - Use Aladdin data beyond its standard interfaces
  - Build client-specific tools
- **Sources for the extensibility point:**
  - BlackRock's APIs page (brief source 3): the APIs let clients "create tools and workflows that expand beyond native Aladdin functionality".
  - Sewdass on the Build vs. Buy webinar (brief source 9): rebalancing tools as an example. Her words were "if clients want to build … their secret sauce rebalancing tools … they can absolutely do so", so the brief says she gave them "as an example", not that clients have built them.
- **Dropped from page 1:**
  - The OAuth-scope and gateway observation. The gateway point stays on page 2 under "Enterprise integration signal". API permissions stay in the page 3 technical note.
  - The list of domains under the API counts. The services band in Exhibit 1 names the same areas.
- **Room made on page 1:**
  - The count explanation is shorter and sits inside the figures box.
  - The diagram's "Aladdin Studio" label was removed, because the exhibit title already names Studio.
  - The introduction is at 10pt.
  - The method note moved to the foot of page 3. The limitation stays on page 1.

## Fourth round: Arcesium row

- **Exhibit 2, Arcesium row:** now reads "Arcesium launched Arcesium Intelligence in May 2026, with more than 100 pre-configured agents across its Opterra and Aquata platforms. It builds on an MCP server, released in December 2025, that connects external AI tools to client data in Aquata."
- **Source 11:** now FinTech Global, "Arcesium launches AI platform for institutional investment," May 20, 2026. The source title links to https://fintech.global/2026/05/20/arcesium-launches-ai-platform-for-institutional-investment/
  - The URL was opened on October 21, 2026. It loaded with HTTP 200.
  - It states the "catalogue of over 100 pre-configured agents" across Opterra and Aquata.
  - It also states the "December rollout of AI features, which included an MCP server enabling investment firms to connect enterprise AI tools to their governed data foundation in the Aquata platform."
  - It is trade press (grade T). It is not part of the Prep 2 source register.
