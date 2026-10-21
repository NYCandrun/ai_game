# Conceptual check: Exhibits 1 to 6 (pages 3 to 6, v23)

This is a read-only check. Nothing in the document was edited. I did not re-check numbers against their citations. I used the page renders at `concept/png16/p-03.png` to `p-06.png`, the 54 specifications in `unpacked/`, the transcripts in `04-transcripts/`, the product pages in `drift22/dl_a/`, the earlier panel reports in `break34/`, and the Exhibit 4 checks in `ex4check/`. I ran one web search, which found nothing conclusive.

| Exhibit | Verdict |
|---|---|
| 1. Eight Aladdin products | SOUND WITH CAVEAT |
| 2. One trade, order to NAV | MISLEADING (two cells in the "Where" row, plus one "Who" cell) |
| 3. Where Studio sits | MISLEADING (the order of the layers) |
| 4. What Studio is made of | SOUND WITH CAVEAT |
| 5. Operations by domain | SOUND (nits only) |
| 6. Five executives on Studio | SOUND WITH CAVEAT |

---

## Exhibit 1. "Of eight Aladdin products, Studio is the one for people who write code": SOUND WITH CAVEAT

**What holds up.** The title's claim about Studio is right. The Studio page names its users as engineers, data analysts and code-curious portfolio managers.

**Caveat 1 (judgment call, close to misleading): "eight" is the author's selection, but it reads as BlackRock's catalog.**
- BlackRock's own navigation (`dl_a/p_aladdin-studio.txt`, lines 17 to 35) lists:
  - four Platforms: Aladdin, Aladdin Wealth, eFront and Preqin;
  - nine Solutions: Accounting, Aladdin Studio, Aladdin Data Cloud, Whole Portfolio, Risk Management, Sustainability, Climate Risk, Aladdin Copilot and Private Markets Data.
- Exhibit 1 takes three of the four platforms and four of the nine solutions, then adds Aladdin Provider, which is not in the navigation.
- The text just above says "four platforms … Exhibit 1 lists eight products sold across them". A reader will take the eight as BlackRock's full lineup. It is not. Preqin is one of the four platforms the paragraph names, and it has no row.

**Caveat 2: the list mixes levels.**
- "Aladdin" is the platform that contains Studio, Copilot, Accounting and Provider.
- Data Cloud has its own row but is also described as "part of Studio". That sits awkwardly with the title's "Studio is *the one*", because Data Cloud users write SQL too.
- The eFront row says eFront "now includes Preqin". That is true of Preqin data inside eFront Insight (`linkcheck/pages/59.html`: "With Preqin inside"). Without a Preqin row, though, a reader could conclude that Preqin was absorbed into eFront. BlackRock still sells Preqin as a separate platform.

**Fix.** Retitle it "Eight Aladdin offerings that bear on Studio" or similar. Add one line to the note: "BlackRock's site lists 4 platforms and 9 solutions; this is a selection."

## Exhibit 2. "The public APIs cover a trade from order to NAV, except positions": MISLEADING (fixable cell by cell)

**What holds up.**
- The spine is right: order, then compliance, then trade, then IBOR, then ABOR, then NAV.
- The API mapping is right.
- The caption is honest that the order of steps 4 to 6 is unknown.
- ValuationsAPI really is about NAV. Its fields include "Describes the NAV after Valuation generated" and navId.

**Error 1: the "Where" cell for the Order step reads "Explore what-if".**
- This conflates two different "what-ifs".
- The cited source (27, `part1-youtube-and-site/09_Blackrock_Aladdin_Explore_Intro.md`) describes Explore as an app for "risk and reporting functionalities". Its what-if is a hypothetical portfolio you "save as portfolio" and compare side by side. Nothing in it creates an order.
- OrderAPI's `whatIf` flag ("True to post orders in a what-if mode") is a different mechanism.
- The same spec names where live orders appear: "Order Monitor of Aladdin Dashboard".
- An insider would say that orders are not entered in Explore.
- Fix: put "Aladdin Dashboard (Order Monitor)" in the Where cell for the order, and drop Explore from this exhibit.

**Error 2: the "Where" cell for "Position in the IBOR" reads "Data Cloud".**
- Every other "Where" cell names the Aladdin application in which the step happens.
- The IBOR is Aladdin's core book of record. Data Cloud is a downstream Snowflake copy of it. Newman: "complement the core IBOR and ABOR information … It does start with IBOR … linking that into the Aladdin Data Cloud". Fivetran, also cited here, describes ingestion into a landing zone.
- As drawn, a reader concludes that positions live in Data Cloud.
- Fix: "Read from: Data Cloud (a copy of the IBOR)". This also makes the useful point that Data Cloud is the public route to positions.

**Error 3 (smaller): "Who: No one" for the compliance check.**
- The check runs automatically, but people deal with its results:
  - ViolationAPI has `post /violation/{id}/resolutions:add`.
  - Orders sit in "Compl Pending" status.
  - The order model has PM authorization (spec: "The PM authorizes the order…").
- Fix: "Runs automatically; violations are resolved by compliance or the PM."

**Caveat on the title's word "cover".**
- Steps 1 to 3 can be written through the APIs (OrderAPI and TradeAPI post).
- Steps 5 and 6 are read-only:
  - AborLotAPI has only `aborLots:filter`;
  - ValuationsAPI has only get and filter.
- Allocation and settlement, which come between trade and ABOR, are not shown.
- The executive summary stresses "APIs can also write". A reader could therefore infer that an AI tool could drive a trade end to end to NAV. It cannot.
- Fix: "cover" → "touch", or add a read/write marker per step.
- Nit: "None of the 54 is a position API" is true for security positions. However, CashLadderAPI returns "a settlement date based ladder of cash balances", which is a cash-position view.

## Exhibit 3. "Where Studio sits in Aladdin": MISLEADING

**The main error: the layer order.**
- The rows stack from top to bottom: Who builds, then BlackRock's applications and Copilot, then the Aladdin Studio band, then shared services. A layer diagram reads as "each row runs on the row below". So the exhibit says two things:
  - (a) BlackRock's ~100 apps and Copilot reach Aladdin through Studio.
  - (b) Client engineers, PMs and analysts build on BlackRock's apps. Visually, data analysts and Excel users sit directly above the Copilot box.
- No source says either. The sources describe Studio as a second, parallel way in to the same services:
  - Khara (46): Studio lets users work with data "on a programmatic basis at machine scale, **over and above what they get through our front end applications**".
  - Newman (22): "we have these engines that historically were run through interfaces. So we're providing those APIs now."
  - Rosales (9, 4:06): the domain teams "own all of the services that serve trading data to all Aladdin applications". The apps sit directly on the services.
- The document contradicts itself here:
  - Exhibit 14 (page 12) draws "BlackRock's own use" and "A client's use · through Studio" side by side over "Aladdin's APIs".
  - Page 10 calls the Copilot/Studio link an inference ("So I infer that Copilot and Studio use the same APIs").
  - Exhibit 3 presents that inference as structure, and in a stronger form.
- This was the top objection in four of the six earlier panels (architect, CTO, designer and insider). It is still unfixed in v23.
- Fix: put "BlackRock's applications + Copilot" and "Aladdin Studio" side by side over the shared-services band. Point "Who builds" at the Studio side only.

**Secondary issues (judgment calls).**
- **The controls column claims more than the controls cover.** The grey "Controls in the API specifications" column runs from the applications row down to the hosting row. It therefore appears to cover Copilot, the whole of Studio (Data Cloud included) and hosting. Exhibit 14's own note says the opposite: "The left-hand controls apply to calls through the APIs. Data Cloud, storage and the Data eXchange have their own access controls." Fix: end the column at the shared-services row, or copy that note sentence.
- **The black band is narrower than the services it names.**
  - Its subtitle says the services are "reached through the 11 public API domains". The 11 domains are the client SDK's packaging. They are not how the ~100 apps or Copilot (~2,000 tools from 50 to 60 teams) reach the services.
  - "Risk" in the band is not one of the 11 domains. The risk APIs sit under `analytics`.
  - The `platform` domain holds Studio's own AdcDatasetAPI, so part of Studio is drawn below Studio.
- **Data Cloud and ADX appear only as ways to load data in** ("Outside inputs … loaded into Data Cloud"). Their main job is outbound:
  - Woodhead says Data Cloud "pushes that into Snowflake".
  - Miller (47) says Data Cloud gets "our clients' data and market data … back to our clients".
  - Exhibit 14 says "Each client reads its own Data Cloud".
- **Nit: the Copilot box.** "Each tool matches an Aladdin API" is literally true, because Rosales defines a tool that way. The registry also holds custom agents, though ("a couple thousands agents and tools"). Exhibit 14 says "tools and agents", and this box should match.

## Exhibit 4. "What Studio is made of": SOUND WITH CAVEAT

**What holds up.**
- The earlier fixes have landed: ATX, ADX and Governance are now inside the Studio frame, and the workspace list is inside it too.
- Every tile traces to a source that ties it to Studio.
- "No event specification is public" is true for the 54 public specifications.

**Caveats (judgment calls).**
- **Nine flat, equal tiles mix different kinds of thing:**
  - separately sold products: Data Cloud, ATX and ADX (BlackRock's navigation lists Data Cloud as a sibling of Studio);
  - an internal runtime: Aladdin Graph, inside the APIs tile;
  - a quality rather than a component: Governance.
- Woodhead's own structure has three pillars: APIs and events, Data Cloud, and developer tools and environments. The flat grid hides it.
- The ATX and ADX ties rest only on a related-links heading, "Additional Aladdin Studio resources". That is weaker than "made of".
- **The Governance tile's quote is misapplied** (as `ex4check/out_tiles.md` §9 found). "Data, tools, and governance support" is the Studio page's description of the whole of Studio, not of a governance component. "Access management and usage monitoring" is the apt quote.
- **The workspace half partly duplicates the top half.** "Studio Compute sessions" is the same thing as the Aladdin Compute tile; the note discloses this. "ADC Admin Center" is placed inside "a client's Studio workspace", but AdcDatasetAPI marks its write operations "intended for internal BlackRock use only", so it may be partly a BlackRock-operated screen.
- **Nits:**
  - "typed clients for the APIs and Data Cloud": the Data Cloud client is a Snowflake connector wrapper that takes SQL strings.
  - The SDK repository ships StudioNotification "event" REST specs marked Internal. An insider could point to these against "No event specification is public", although that statement still holds for the 54 public specifications.

## Exhibit 5. "Two domains hold 127 of the 301 public API operations": SOUND

**What holds up.**
- I recomputed the counts from the files and got the same results:
  - investment_operations 74 and analytics 53, total 301;
  - stability is one `x-aladdin-api-stability` label per specification.
- The title is a plain description, and the note scopes it to the 54 specifications.

**Nits.**
- **Not every "public" operation is open to clients.** Five of the 301 operations are flagged in their own descriptions as not for clients: four AdcDataset operations ("intended for internal BlackRock use only and is in the process of being depreciated") and RiskWorkflow `workflows:batchCreate` ("For internal use only").
- **Operation count measures CRUD granularity, not importance.**
  - Investment operations is large mainly because of seven broker reference-data specifications.
  - The domains the thesis depends on, trading (14 operations) and compliance (9), are among the smallest and mostly alpha.
  - The exhibit shows this honestly. A reader should not take "largest" as "most important".

## Exhibit 6. "Five BlackRock executives describe Studio or its parts on the record": SOUND WITH CAVEAT

**What holds up.**
- The titles and quotes match the transcripts.
- "Or its parts" correctly lets in Goel and Miller, who never say "Studio". Exhibit 7's note says so.

**Caveat 1: two cells in "What they add to the definition" present more than the speakers said.**
- **Goel.** His words are aspirations: "we **really want to** make every single event … available … every single transaction … **should be** available … via an event, via an API", and "we **actually want to give you** a near real time data store … within 15 minutes of latency". The body text keeps "should be", but the exhibit cell presents both as current facts. Fix: prefix the cell with "Aims for:".
- **Miller.** The cell says Data Cloud "replaced 'flat files … FTP and related transfers'". He said that before Data Cloud "we sent flat files … FTP and related transfers, but the Aladdin Data Cloud and Snowflake makes it much simpler". "Replaced" overstates this. It also clashes with Exhibit 4, which still lists ADX bulk file transfer, with standard extracts, as part of Studio. Fix: "Data Cloud is simpler than the flat files and FTP used before."

**Caveat 2 (scope): "on the record" in the title is broader than the evidence.**
- The body scopes the count to "about 125 recordings". Other BlackRock staff describe Studio parts in writing: Naik (Lead Engineer, Aladdin Studio) and Kalish (Product Manager, Aladdin Studio) on the SDK (register 38), and the Studio Developer job posting.
- Fix: "in recordings" in place of "on the record".

**Nit.** Woodhead's own definition is a three-pillar one, and the third pillar is "how do I bring those people in": sandboxes, research environments, building apps and automating workloads. "Developer tools" undersells it slightly.

---

## Most important, in order

1. **Exhibit 3's stack** says BlackRock's apps and Copilot run on Studio and that clients build on BlackRock's apps. It contradicts Exhibit 14 and the sources (Khara: "over and above … our front end applications").
2. **Exhibit 2's "Where" row** places orders in Explore, which is a risk and reporting app, and places the IBOR in Data Cloud, which is a copy of it.
3. **Exhibit 1's "eight products"** reads as BlackRock's catalog. BlackRock lists 4 platforms and 9 solutions.
4. **Exhibit 6's Goel and Miller cells** turn an aspiration and a comparison into facts ("replaced").
