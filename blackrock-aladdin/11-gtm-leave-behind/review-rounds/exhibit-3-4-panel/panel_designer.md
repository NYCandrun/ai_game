# Panel: designer (information design). Exhibits 3 and 4, page 4

Checked: page4-04.png, page4.txt, BUILD_NOTES.md, page 12 of gtm/out/Aladdin_Studio_With_AI.pdf (Exhibit 14; text extracted to break34/des_tmp/doc.txt), the transcripts, the crawled Studio page and AWS release, the SDK README, and three live pages fetched on 2026-10-20 (the APIs page and job postings 46 and 82). I edited nothing. This file is the only one I wrote, apart from scratch extracts in break34/des_tmp/.

Reading convention used throughout: in a layered stack with no arrows, a reader takes each band as built on, or reached through, the band below it. Column alignment inside a row reads as pairing with the box directly underneath. Everything below follows from that convention.

---

## BREAKS IT

### B1. The stack puts BlackRock's ~100 applications and Copilot on top of Studio, so it says BlackRock's own apps reach Aladdin through Studio. No source says this, and Exhibit 14 on page 12 draws the opposite.

- **What the picture claims.** The row order is Who builds > BlackRock's applications (apps + Copilot) > Aladdin Studio > Shared services and data. The apps and Copilot never touch the black services band; the yellow Studio band runs between them across the full width. The page title is "Where Studio sits in Aladdin", and the picture's answer is "under BlackRock's apps, over the core". The four "Who builds" boxes sit directly on BlackRock's applications, so the picture also says client engineers, PMs, analysts and Excel users build on, or through, BlackRock's apps. Column alignment makes it worse: "Data analysts" and "Excel users building reports" sit exactly over the Copilot box, and "Client engineers" and "Code-curious portfolio managers" sit over the apps box.
- **Exhibit 14 contradicts it.** Page 12 puts apps and Copilot in a pink group headed "BLACKROCK'S OWN USE · IN THE PUBLIC RECORD", side by side with a separate yellow group headed "A CLIENT'S USE · THROUGH STUDIO" (doc.txt:613). Both groups have their own arrows to one shared bar, "Aladdin's APIs" (doc.txt:625). The caption reads: "BlackRock's applications, Copilot and a client's code draw on Aladdin's shared services and APIs" (doc.txt:626). In Exhibit 14, Studio is the client's path, a sibling of BlackRock's apps, and not a layer under them. One reader turning from page 4 to page 12 sees two different architectures.
- **Sources.**
  - Rosales, /home/user/ai_game/blackrock-aladdin/04-transcripts/timestamped/yt_oyqeCHFM5U4.m4a.ts.txt:43: "[04:06] Maybe the trading team and they own all of the services that serve trading data to all Aladdin applications". The services serve the apps directly, and Studio is not mentioned anywhere in the talk.
  - The same file, :44-45: "these engineers build and maintain ... around 100 Aladdin front-end applications". BlackRock's own engineers build the apps, not the four personas stacked on top of them.
  - Studio Developer job posting (register 46, live 2026-10-20, https://careers.blackrock.com/job/new-york/senior-product-director-aladdin-studio-developer/45831/96232273856): "Studio Developer as Aladdin's extensibility layer, enabling customization and automation within the platform while preserving the integrity of core functionality". That is an extension layer beside the core, not the substrate under the core apps. The same posting does say "partnering closely with BlackRock and other key users", so BlackRock staff also use Studio. That supports "BlackRock uses Studio" but not "the ~100 apps sit on Studio".
  - Studio page (crawl2/aladdin.json, Studio entry; extract des_tmp/studio.txt:112): "Whether you're a professional engineer building new workflow applications, a code-curious portfolio manager ... or a data analyst automating reporting, Aladdin Studio gives you the data, tools, and governance support". The personas build through Studio, not through BlackRock's apps.
- **Smallest fix.** Copy Exhibit 14's topology. Merge rows 2 and 3 into one row: [About 100 applications | Copilot] on the left, and the yellow [Aladdin Studio] band on the right, both sitting directly on the black band. Put "Who builds" over the Studio half only, or keep it full width and label it "build through Studio". If space forces a single column, add a one-line key: "Applications and Studio sit side by side on the same services; BlackRock's apps do not run through Studio."

---

## WEAKENS IT

### W1. The API layer has three different homes across Exhibits 3, 4 and 14.

- **Exhibit 3.** The API domains sit in the black band below Studio: "reached through the 11 public API domains". The note adds "The 11 domains are the packages of BlackRock's public SDK", and the SDK is a Studio part in Exhibit 4.
- **Exhibit 4.** "APIs (Aladdin Graph)" is a tile inside the yellow Studio frame.
- **Exhibit 14.** "Aladdin's APIs" is its own shared bar under both BlackRock's own use and the client's use through Studio (doc.txt:625-626).
- **The same layer also carries three names:** "Shared services and data" (Ex 3 row label), "Aladdin's APIs" (Ex 14 bar) and "Aladdin's shared services and APIs" (Ex 14 title).
- **Sources.**
  - Aladdin Graph job posting (register 82, live): "Building solutions for BlackRock and over 200 institutions ... The team behind Aladdin Graph—enabling API‑first engineering through a schema repository, governance, and production runtime infrastructure for APIs and events." Aladdin Graph is firm-wide API infrastructure, which fits Exhibit 14's shared bar better than a Studio-only tile.
  - APIs page (live): "Aladdin APIs allow for programmatic access to Aladdin operational services" and "Aladdin Studio already has a large universe of available APIs". Studio exposes the APIs, so a tile is defensible from the client's side.
- **The misreading.** A reader cannot tell whether "the APIs" belong to Studio or to the core. That matters for page 12's argument that BlackRock's controls are "built into the APIs".
- **Smallest fix.** Pick one home and caption it once. For example, Exhibit 4's tile becomes "APIs (Aladdin Graph, shared with BlackRock's own apps): Studio exposes them", and Exhibit 3's band text reads "Aladdin's shared services, exposed as APIs in 11 public domains". Rename the Ex 3 row "Shared services and APIs" to match Ex 14.

### W2. Exhibit 3 puts two of BlackRock's named Studio resources outside the Studio band, Exhibit 4 puts them inside the Studio frame, and both demote them below the author's own tiles.

- **Source.** The live APIs page (https://www.blackrock.com/aladdin/platforms/products/apis) lists: "Additional Aladdin Studio resources / Aladdin Studio home / Aladdin Data Cloud / Aladdin Data eXchange (ADX) / Aladdin Compute / Aladdin Tools for Excel (ATX)".
- **Exhibit 3.** ATX shows up only as a persona in the top row ("Excel users building reports"). ADX shows up only inside the bottom dashed "Outside inputs" box, two rows below Studio and outside the yellow band. A dashed box at the bottom reads as "outside Aladdin".
- **Exhibit 4.** ADX and ATX are inside the yellow frame, but as a single small centred line: "The APIs page also links ...". The SDK and the Developer Portal, which are not on BlackRock's list, get full tiles.
- **The misreading.** A BlackRock reader sees their own five-item resource list split apart: two items promoted, two demoted to a footnote line, and two treated as outside Studio on the facing exhibit. The words "also links" are accurate. The hierarchy is the problem.
- **Smallest fix.**
  - Exhibit 4: make the line read "BlackRock's APIs page also lists Aladdin Tools for Excel and the Aladdin Data eXchange as Studio resources", or give them two half-height tiles.
  - Exhibit 3: change the persona to "Excel users (ATX)", and in the outside-inputs box write "through the Data eXchange (a Studio resource)".

### W3. Exhibit 4 places the client's Studio workspace outside the yellow Studio frame, and its parts duplicate the tiles above without saying so.

- **The encoding.** Yellow is Studio: the Ex 3 band and the Ex 4 frame share the same yellow, which is a good link between them. The grey "INSIDE A CLIENT'S STUDIO WORKSPACE" panel sits below that frame and outside it, so the encoding says the workspace is not part of what Studio offers. The panel's own title says it is.
- **The pairs.** The lower list repeats the upper tiles under different names, with no link between them:
  - "Studio Compute" against the "Aladdin Compute" tile
  - "ADC Admin Center" against the "Aladdin Data Cloud" tile
  - "API tokens and API applications" against the "APIs" tile
- **What a reader concludes.** There are 13 distinct parts, including two compute products.
- **Sources.**
  - SDK README, /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/readme.md:179: "AladdinSDK can run on a developer's local machine or in Aladdin Studio Compute sessions".
  - The Studio briefing pairs the two compute names in one row: /home/user/ai_game/blackrock-aladdin/01-research-briefings/aladdin_studio_briefing.md:20: "Aladdin Compute | Hosted analytics platform ... The SDK has a `compute` run mode for "Aladdin Studio Compute sessions"".
  - No source says whether the two compute names are one product or two. That is a reason to state the relationship, not to imply a split.
- **Smallest fix.** Move the grey panel inside the yellow frame as a lower tier, headed "How the SDK files name the same pieces". Alternatively, add one line: "Names used in BlackRock's SDK files. Studio Compute, the ADC Admin Center and API tokens belong to the Compute, Data Cloud and API pieces above; BlackRock does not map them."

### W4. Hatch and dash mean different things on page 4 and page 12.

- **Exhibit 14's key** (doc.txt:638): "Solid boxes are in the public record. The hatched box is not." Its dashed arrow means "How they would connect is not published".
- **Exhibit 3 uses the same codes for other things.**
  - The hatched box is "AWS option, announced", which is in the public record: the AWS release in crawl2/aladdin3b.json says "today announced a strategic partnership".
  - A dashed border marks both "not live" (the AWS box) and "outside Aladdin" (the outside-inputs box).
- **The misreading.** A reader who learns the page 12 key reads the AWS box as unsourced, and reads the outside-inputs box as not yet live or uncertain.
- **Smallest fix.** Give the AWS box a different treatment from Exhibit 14's hatch, such as a lighter tint or an "announced" tag, and keep the dash for "outside Aladdin" only. Or add one sentence to the Ex 14 key: "On page 4, hatching marks an announced, not-live option."

### W5. The pink of the Copilot box means something else on page 12.

- **Exhibit 3.** Only Copilot is pink; the apps box is white. On page 4, pink reads as "AI" or "Copilot".
- **Exhibit 14.** Pink fills both the apps and Copilot tiles under "BLACKROCK'S OWN USE" (doc.txt:613). There pink means "BlackRock's own".
- **The misreading.** The same colour carries two meanings in one document. A page 12 reader may take Exhibit 3's white apps box as "not BlackRock's own".
- **Smallest fix.** Tint the Ex 3 apps box pink as well, so pink means "BlackRock's own" in both exhibits.

### W6. The "Controls built into the APIs" column runs from the applications row down to the hosting row, so it claims coverage it does not have and hides Copilot's own controls.

- **What the column spans.** In the image, the grey column starts at the top of the BlackRock's applications row and ends at the bottom of the Hosting row. That says the three controls govern the apps, Copilot, Studio, the services and the Azure/AWS hosting. The title says they are "built into the APIs". Hosting has no API control in any source.
- **Copilot's own controls.** The column sits level with the Copilot box, so it reads as Copilot's control set. Exhibit 14 lists separate Copilot controls ("WHAT COPILOT ADDS FOR AI": input guardrails, output guardrails, LLM judges; doc.txt:629). Rosales describes a control at the level of the tool, which Exhibit 14's lower row does not show either: the page 12 text says "The team that owns each tool sets which user groups can use it". Exhibit 3 shows none of these.
- **"Controls as in Exhibit 14" is loose.**
  - Exhibit 3 orders the controls Access, Compliance, Second approver. Exhibit 14 orders them Access, Second approver, Compliance.
  - Exhibit 3 drops "Capital flows record who approved them" (doc.txt:634).
- **Smallest fix.**
  - Shorten the column so it spans only the Studio and Shared services rows, the layer the APIs actually sit in.
  - Add one line in the column: "Copilot adds its own guardrails (Exhibit 14)".
  - Match Exhibit 14's order.

---

## NIT

- **N1. The outside-inputs box sits at the very bottom, under Hosting.** The stack reads as data entering below everything. The words say data is "loaded into Data Cloud" (a Studio part in Ex 4) or "through the Data eXchange" (a Studio resource), while vendor prices and ESG data go into the core. Woodhead, /home/user/ai_game/blackrock-aladdin/04-transcripts/requested-recordings/snowflake_data_cloud_podcast_woodhead_whisper.txt:41-43: "the raw ingredients into the factory, the market data, the economic data that we bring into the platform". The box mixes two destinations and has no arrows. Fix: two short arrows or labels, "client data → Data Cloud" and "vendor data → shared services".
- **N2. The hosting row spans the full width under everything, so it also claims Data Cloud runs on Azure/AWS.** Exhibit 14 says "Each client reads its own Data Cloud, which BlackRock runs on Snowflake" (doc.txt:626). The Microsoft blog does support Azure for the rest: /home/user/ai_game/blackrock-aladdin/04-transcripts/product-pages/ms_cloud_blog.txt:130, "all BlackRock's technology platform clients and services are hosted in the Azure cloud". Fix: add "Data Cloud on Snowflake" to the hosting row, or a footnote.
- **N3. The AWS box has the same width as Azure and no scope.** The release (crawl2/aladdin3b.json; des_tmp/aws.txt:119) says "General availability for Aladdin Enterprise clients hosted in the United States is expected in the second half of 2026". The document is dated October 2026, inside that window, so "announced, not live" may already be stale. One WebSearch found no GA announcement, so I have not verified it either way. Fix: label the box "AWS option for US-hosted Aladdin Enterprise, GA expected H2 2026", narrow it, and recheck before release.
- **N4. The Copilot box sits beside the apps, while the words say "inside them".** Rosales, yt_oyqeCHFM5U4.m4a.ts.txt:25: "[02:34] application is currently embedded across all of those hundred front-end applications". Fix: draw Copilot as a strip inside the apps box. Exhibit 14 also shows them as peers, so change both or neither.
- **N5. "APIs (Aladdin Graph)" and "Event-driven workflows" are separate tiles, but job posting 82 describes Aladdin Graph as "production runtime infrastructure for APIs and events".** The label implies Graph covers APIs only. Fix: "APIs and events run on Aladdin Graph", or a note.
- **N6. Grey means "controls" in Exhibit 3 and "workspace" in Exhibit 4.** The two meanings sit on the same page. (OPINION, low stakes.)
- **N7. "Excel users building reports" gets the same box weight as client engineers in "Who builds".** The Studio page names only three personas (des_tmp/studio.txt:112); the fourth comes from the ATX page. Fine if W2's fix makes the ATX link visible.
- **N8. The black band is the heaviest element on the page, and the Studio band, the document's subject, is the thinnest.** (OPINION.) The emphasis reads as "Studio is a thin slice of Aladdin", which may be intended, but it is worth a conscious choice.
- **N9. Woodhead's third pillar has no picture anywhere: client-built artifacts flowing back into the investment process.** Woodhead :150-151: "taking those artifacts that people come and build on top of Aladdin and natively integrating them into the investment process". The stack is static, so a reader cannot see that client-built work returns into Aladdin. (Omission; an arrow from "Who builds" back down would be enough.)

---

## Holds up

- **"Shared services and data" is BlackRock's own phrase.** Studio page, des_tmp/studio.txt:107: "Empowering unique outcomes via our API-first approach across shared services and data".
- **The yellow carries across from the Ex 3 band to the Ex 4 frame.** The band's "its parts are in Exhibit 4" is a clean cross-reference, and the two exhibits use the same names for Data Cloud, the Data eXchange and the Excel tools.
- **Woodhead's definition supports the Studio band's content: APIs, events, Data Cloud and developer tools.** woodhead_whisper.txt:129-135: "It exposes everything Aladdin knows how to do as a set of APIs, events, the Aladdin data cloud ... And increasingly we're building a set of developer tools."
- **The app and Copilot claims match the source wording.**
  - "About 100 applications", Rosales :18: "around 100 Aladdin front-end applications".
  - "Each tool matches an Aladdin API already in production", Rosales :48: "mapping one-to-one to an existing Aladdin API already out in production".
- **Hosting is correctly ordered below services, and the AWS box is visibly marked as not equivalent to Azure.** It is hatched and keyed in the note.
- **The Exhibit 4 workspace lines are each traceable to README or specification wording.** The note's "BlackRock gives no count of pieces" correctly defuses any reading of "six" as an official count.
- **The note keeps the hedges a careful reader needs.** "For illustrative purposes only", "announced, not live" and "behind a client login" are all there.
- **The Ex 3 and Ex 14 control wording ("Access set per API", "Compliance by default", "A second approver") matches word for word, apart from the order and the dropped capital-flows clause (W6).**
