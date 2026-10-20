# Exhibit 4 truth check (read-only)

The document has already been sent. Do NOT edit anything. Your job is to say, for every claim in Exhibit 4 ("What Studio is made of", page 4 of the document), whether its sources actually back it.

The exhibit text, exactly as sent:

What Studio offers
1. APIs: "Read and write Aladdin data." / "Built on Aladdin Graph, BlackRock's firm-wide runtime for APIs and events." / "Every public specification's ID begins agraph.<domain>, for Aladdin Graph"
2. Event-driven workflows: "Aladdin tells a program when something happens." / "Events run on the same Aladdin Graph runtime." / "No event specification is public"
3. Aladdin SDK: "Open-source Python library with typed clients for the APIs and Data Cloud, with login, retries and rate limits built in." / "A BlackRock plugin builder generates its 11 plugin packages from the specifications"
4. Aladdin Data Cloud: "A managed data store on Snowflake, with Fivetran moving the data"
5. Aladdin Compute: "Hosted, ready-to-use Python environments"
6. Aladdin Tools for Excel (ATX): "An Excel plugin that pulls Aladdin data into custom reports and analyses"
7. Aladdin Data eXchange (ADX): "Bulk file transfer to and from Aladdin, with standard extracts and loaders"
8. Developer Portal and Data Dictionary: "Catalog, guides, field dictionary, notebooks and samples, behind a client login"
9. Governance: "Data, tools, and governance support", including "access management and usage monitoring"
Inside a client's Studio workspace
10. Studio UI: The screens where tokens, applications and storage are set up
11. Projects: Personal or shared, each holding OAuth applications and storage
12. API tokens and OAuth applications: Sign-in for the APIs
13. Studio Compute sessions: Where Aladdin Compute runs SDK code
14. S3 storage integration: File storage for SDK code, set up in a Project
15. Studio notifications: Alerts sent through Studio's notification APIs
16. ADC Admin Center: The screen for managing Data Cloud datasets
17. The framing itself: that all nine tiles are parts of (or offered by) Aladdin Studio. The note says the APIs, ATX and ADX pages list Data Cloud, ADX, Aladdin Compute and ATX as "Additional Aladdin Studio resources". Check whether each tile has a source tying it to Studio.

Source note under the exhibit: Studio page [14]; APIs, ATX and ADX pages [30, 32, 33]; the 54 public specifications [6], for the ids, the portal link and the Admin Center; the SDK README [29], for the SDK and the workspace; Naik and Kalish [38] and the Aladdin Graph job posting [39], for Aladdin Graph; the plugin builder [40]; Woodhead [1], Goel [41], the Aladdin Risk page [31] and a BlackRock job posting [42], for events and the portal; Fivetran [28]; Snowflake's partner page, for Compute [43]; the developer portal [44]; Studio for Aladdin Risk, for access management [45]. "I read Studio Compute sessions as the SDK's name for Aladdin Compute."

Register entries for those numbers (title, publisher, URL): /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ex4check/register.txt

Where to find source text:
- Specs [6]: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/unpacked/ (asdk_plugin_* 2.0.0b3 Swagger files). grep them. Count packages yourself.
- SDK [29]: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/drift22/sdk_b (a git clone of blackrock/aladdinsdk) or clone https://github.com/blackrock/aladdinsdk into a new dir under /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ex4check/. Plugin builder [40]: git clone https://github.com/blackrock/aladdinsdk-plugin-builder. The GitHub API is blocked; git works.
- Product pages: saved copies in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/drift22/dl_a/ (p_apis.html, p_aladdin-tools-for-excel.html, p_aladdin-data-exchange.html, p_aladdin-studio.html, p_aladdin-data-cloud.html, p_aladdin-risk.html, job41.html, job50.html). Otherwise curl the register URL.
- Transcripts (Woodhead, Goel): /home/user/ai_game/blackrock-aladdin/04-transcripts/ (grep for a distinctive phrase).
- Earlier evidence: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/redraw34/NOTES.md, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/break34/panel_*.md, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/.
- Use at most 15 web searches.

For each numbered claim give: verdict (TRUE / PARTLY / NOT SUPPORTED / CONTRADICTED), the source, and a short exact quote. For PARTLY or worse, say exactly which words go beyond the source and what the source does say. Do not suggest style rewording. Be adversarial: the reader is BlackRock's head of go-to-market, who knows Studio well. Also flag anything important a Studio insider would say is missing or misplaced, but keep that separate from the verdicts.

Write the report to the output path you are given. Reply with a one-paragraph summary plus the list of non-TRUE items.
