# Group g07: drafted fixes (page 13, Part 3 and Exhibit 14)

## p13-01 · CITE

- **Current:** It sells Aladdin as the system it runs internally [8, 14, 17, 19].
- **Proposed:** It sells Aladdin as the system it runs internally [8, NEW].
- **Source entry:** NEW P BlackRock Completes Acquisition of eFront . BlackRock press release, May 10, 2019. https://www.blackrock.com/corporate/newsroom/media/press-releases/blackrock-efront-acquisition
- **Why:** The words are true, but sources 14, 17 and 19 do not mention internal use. BlackRock’s eFront release says “Aladdin was first built to manage BlackRock’s business” and the firm offers clients “the same technology … that BlackRock uses to manage investments day-to-day”. Source 8 at 1:33 says “BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients”.

## p13-06+p13-07+p13-08+p13-09 · FIX

- **Current:** About 100 of its applications and thousands of Copilot tools, built by 50 to 60 of its teams, call these APIs every day under each user’s permissions [8].
- **Proposed:** About 100 of its applications carry Copilot. Each Copilot tool maps to a production Aladdin API, and the team that owns it sets which user groups can use it [8].
- **Also change:** Executive summary, page 2. Owned by g01 (p02-09+p02-10, marked DECIDE there). It must use the same facts as this sentence. This proposal is word for word the Part 3 text g01 drafted in its own also_change, so the two groups agree.
  - Current: About 100 of its applications and thousands of Copilot tools already call these APIs every day [8].
- **Why:** Source 8 says “around 100 Aladdin front-end applications that thousands of people use every day” (1:53) and that Copilot is “embedded across all of those hundred” (2:34). It defines a tool “as kind of mapping one-to-one to an existing Aladdin API already out in production” (4:39). Teams that onboard a plugin control “which user groups have access to this” (6:51). No source says the apps or tools call the APIs every day or under each user’s permissions. The 50 to 60 teams build tools and agents, not the apps, so that count moves to the Copilot box in Exhibit 14. Length: 29 words in place of 27, so page 13 does not grow.

## p13-22 · DECIDE

- **Current:** Exhibit 14. BlackRock’s applications and a client’s code call the same APIs under the same permissions
- **Proposed:** Exhibit 14. BlackRock’s applications and a client’s code draw on Aladdin’s shared services and APIs
- **Alternative:** Exhibit 14. BlackRock’s applications and a client’s code call the same APIs plus this sentence added to the exhibit note: “That both sides call the same APIs is my reading: Copilot’s tools map to production Aladdin APIs, and Studio offers clients APIs built on shared services.” (Keeps the exhibit’s thesis but labels it as the author’s inference. It adds about one line to the note on page 13, so something else on the page would have to shrink.)
- **Source entry:** NEW P BlackRock To Launch the “Aladdin Data Cloud” Powered by Snowflake . BlackRock press release, February 22, 2021. https://www.blackrock.com/corporate/newsroom/media/press-releases/aladdin-data-cloud-powered-by-snowflake
- **Also change:** Exhibit 14 source line (notes): add the Studio page, which says “shared services”, and the Data Cloud launch release used by the new centre caption (p13-34+p13-35). The release is the same entry g03 adds as sNEW-g03-adcpr; add it once.
  - Current: Sources: Rosales and Valdez [8], the Copilot page
  - Proposed: Sources: Rosales and Valdez [8], the Studio page [14], the Data Cloud launch release [NEW], the Copilot page
- **Also change:** Exhibit 14 right-hand band header (recommended option only; the alternative keeps it)
  - Current: A CLIENT’S USE · THE SAME APIS
  - Proposed: A CLIENT’S USE · THROUGH STUDIO
- **Also change:** Exhibit 14 aria-label. One rewrite that also carries p13-27, p13-34+p13-35, p13-37 and p13-47.
  - Current: Diagram. On the left, BlackRock's own use: about 100 BlackRock applications and Copilot's thousands of tools. On the right, a client's use: its engineers behind its own gateway, its applications, and, hatched, its AI tools, on which BlackRock has published nothing beyond a job posting. All sit on one band, Aladdin's APIs, which all of them call and whose Data Cloud they read. Below, two groups: controls on every call (permissions per user, a second approver, compliance on every order) and what Copilot adds for AI (input guardrails, output guardrails, LLM judges).
  - Proposed: Diagram. On the left, BlackRock's own use: about 100 BlackRock applications and Copilot's two thousand or so tools and agents. On the right, a client's use: its engineers behind its own gateway, its applications, and, hatched, its AI tools, for which the nearest public sign is an internal job posting. All sit on one band, Aladdin's APIs built on shared services, which all of them call. Each client reads its own Data Cloud. Below, two groups: controls built into the APIs (permissions per user, a second approver, compliance by default on orders) and what Copilot adds for AI (input guardrails, output guardrails, LLM judges).
- **Also change:** Exhibit 14 centre caption: see p13-34+p13-35. Under the alternative, it may keep “the same APIs”, but the Data Cloud clause must still change.
- **Also change:** Part 3 lede sentence (thesis) keeps “under the same controls BlackRock’s own business runs on”. That phrase is about controls, not identical APIs, so it can stay with either option.
  - Current: the place where a client’s own AI tools act on investment data under the same controls BlackRock’s own business runs on
- **Why:** No source says BlackRock’s apps and a client’s code call identical APIs under identical permissions. The Studio page (source 14) says “API-first approach across shared services and data” and “secure, common, and extensible services”. Source 8 says the trading team owns “all of the services that serve trading data to all Aladdin applications” (4:06). The recommended title states only that. Permissions are shown in the boxes below and drop out of the title. The new title is shorter than the old one.

## p13-26 · FIX

- **Current:** all call these APIs.
- **Proposed:** draw on Aladdin’s shared services.
- **Also change:** None needed for the citation. The exhibit note already cites the public specifications (6), which name Risk Radar, Explore and Aladdin Dashboard, and p13-22 adds the Studio page (14). g01 drafted “all carry Copilot.” for this line. Either is true. The reviewer should pick one.
- **Why:** The specifications tie only some APIs to these apps, for example RiskRuleAPI rules “as surfaced in Risk Radar” and orders “visible in the "Basket" column in Order Monitor of Aladdin Dashboard”. Source 8 says services “serve trading data to all Aladdin applications” (4:06), and source 14 speaks of “shared services”. No source says every app calls these APIs.

## p13-27 · FIX

- **Current:** Thousands of tools, each one an Aladdin / API, built by 50 to 60 BlackRock teams.
- **Proposed:** About two thousand tools and agents, / from 50 to 60 BlackRock teams. Each / tool maps to an Aladdin API.
- **Also change:** Exhibit 14 source line: the Copilot page (17) gives no count. It can stay in the line because it supports other boxes (Copilot’s guardrails).
- **Why:** Source 8 says “a couple thousands agents and tools that are registered in the plug-in registry” (6:42). A tool maps “one-to-one to an existing Aladdin API already out in production” (4:39), while an agent is a separate path for “complex workflows” (4:49). There are “50 60 Aladdin engineering teams” (3:58). The box has room for a third line at y=134, and each line is no wider than the line it replaces.

## p13-34+p13-35 · FIX

- **Current:** BlackRock’s applications, Copilot and a client’s own code call the same APIs and read the same Data Cloud, the client’s Aladdin data in a Snowflake account BlackRock runs for it.
- **Proposed:** BlackRock’s applications, Copilot and a client’s code all call Aladdin APIs built on shared services. Each client reads its own Data Cloud, which BlackRock runs on Snowflake.
- **Source entry:** NEW P BlackRock To Launch the “Aladdin Data Cloud” Powered by Snowflake . BlackRock press release, February 22, 2021. https://www.blackrock.com/corporate/newsroom/media/press-releases/aladdin-data-cloud-powered-by-snowflake
- **Also change:** Exhibit 14 source line: add 14 and the Data Cloud launch release. This is the same edit listed under p13-22; make it once.
  - Current: Sources: Rosales and Valdez [8], the Copilot page
  - Proposed: Sources: Rosales and Valdez [8], the Studio page [14], the Data Cloud launch release [NEW], the Copilot page
- **Why:** Source 8 says Copilot tools map “to an existing Aladdin API already out in production” (4:39) and that services serve “all Aladdin applications” (4:06). The Studio page (14) says “API-first approach across shared services and data”. BlackRock’s Data Cloud release says “Each Aladdin Data Cloud client receives an independent, centrally-managed data store”. No source says Copilot reads the Data Cloud, so Copilot leaves that clause. The new caption is 174 characters, against 178 now, so it still fits one line.

## p13-37 · FIX

- **Current:** CONTROLS ON EVERY CALL
- **Proposed:** CONTROLS BUILT INTO THE APIS
- **Also change:** Exhibit 14, third control box title. The compliance check runs by default on order posts and can be switched off, so “every order” overstates it. The box text below it is already accurate.
  - Current: Compliance on every order
  - Proposed: Compliance by default
- **Also change:** Exhibit 14 aria-label: carried in the single aria-label rewrite under p13-22.
- **Why:** In the 54 public specifications, all 301 operations require an API key and an OAuth scope (source 6). The four-eyes check covers only dataset workflow states. Compliance applies only to order posts, where OrderAPI says runCompliance “Default is true to run compliance on this post order request.”

## p13-40 · FIX

- **Current:** Rule assignments and dataset / releases record a second / sign-off.
- **Proposed:** Dataset releases need a / second check. Capital flows / record who approved them.
- **Why:** AdcDatasetAPI says “STATE_REVIEW: In review state, dataset is ready for a 4-eyes check prior to release”. EnrichedCapitalFlowAPI records an “approverUserId” (“Approver Aladdin user Id”) and an “authorizerUserId” (source 6). The rule assignment spec has review states but no approver field, and its four-eyes flag is “By default … false”, so rule assignments leave the box. No new line is longer than the widest line now in the box (28 characters).

## p13-47 · FIX

- **Current:** The hatched box is not: on a client’s AI tools BlackRock has published nothing beyond a job posting [60].
- **Proposed:** The hatched box is not. The nearest public sign is a September 2026 posting for an internal data role that names MCP and AI agents [60].
- **Source entry:** REPLACES the existing entry 60 (same number, new URL and details): 60 P Forward Deploy Engineer, Aladdin Data, Associate . BlackRock job posting, Mumbai, Workday requisition R264906, posted September 4, 2026, and no longer on BlackRock Careers on October 20, 2026. Text as kept by Saarthi. https://joinsaarthi.com/jobs/blackrock/forward-deploy-engineer-aladdin-data-associate-mumbai/46c71ea1-8135-43ac-9591-17a49139ceb6
- **Also change:** Sources register, entry 60 (the careers URL now returns 404)
  - Current: 60 P Job posting: Forward Deploy Engineer, Aladdin Data, Associate (Mumbai) . BlackRock Careers, as of October 2026. https://careers.blackrock.com/job/mumbai/forward-deploy-engineer-aladdin-data-associate/45831/97466309856
  - Proposed: 60 P Forward Deploy Engineer, Aladdin Data, Associate . BlackRock job posting, Mumbai, Workday requisition R264906, posted September 4, 2026, and no longer on BlackRock Careers on October 20, 2026. Text as kept by Saarthi. https://joinsaarthi.com/jobs/blackrock/forward-deploy-engineer-aladdin-data-associate-mumbai/46c71ea1-8135-43ac-9591-17a49139ceb6
- **Also change:** Exhibit 14 hatched box, last two lines
  - Current: BlackRock’s only public / word is a job posting.
  - Proposed: Nearest public sign: / an internal job posting.
- **Also change:** Part 3 body. The sentence is true and stays. The posting is about an internal role, so it does not support this sentence. Recommend dropping the citation.
  - Current: How those tools would connect is not public [60].
  - Proposed: How those tools would connect is not public.
- **Also change:** Exhibit 14 aria-label: carried in the single aria-label rewrite under p13-22.
- **Why:** The posting (Workday R264906, posted September 4, 2026) asks the hire to “Implement emerging AI tooling including Model Context Protocol (MCP), AI agents, and Copilot extensions to automate repetitive onboarding tasks” with “partner engineering and data teams”. That is internal data-platform work, not client AI tools. The careers URL now returns 404, so entry 60 moves to the Saarthi copy. The new note is shorter than the old one.
