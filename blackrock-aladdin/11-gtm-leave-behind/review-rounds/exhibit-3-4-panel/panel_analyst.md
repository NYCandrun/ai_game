# Panel: equity analyst covering BlackRock's technology business (Exhibits 3 and 4, page 4)

Angle: does the page match how BlackRock describes Aladdin to investors and in filings (FY2025 10-K, 2025 Investor Day deck, earnings calls), and does it agree with Exhibit 1 and the rest of the document? Check only; nothing was edited.

Evidence files (SP = /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad):
- 10-K FY2025 (blk-20251231, register 12): SP/fc/dl/b008/10k.htm. The same text is split into sentences at SP/break34_analyst/10k_lines.txt (line numbers below refer to that file).
- 2025 Investor Day deck (register 11): SP/invday/blk_id2025.pdf; text at SP/break34_analyst/id2025.txt.
- APIs page, live copy of 2026-10-20: SP/fc/dl/b024/live/apis.txt. Studio page: SP/studio_page.txt.
- AWS release, full copy with FAQ (register 21): SP/linkcheck/pages/5.html (TradingView). The Amazon press-center copy, dated December 1, 2025, is SP/linkcheck/pages/50.html.
- Document text: SP/break34_analyst/doc.txt.

---

## BREAKS IT

### B1. Hosting: "AWS option, announced" and the note's "the AWS option is announced, not live" conflict with BlackRock's own 10-K
- The 10-K the document cites as register 12 says, in the present tense (10k_lines.txt:835): "For instance, the Aladdin infrastructure and environment for BlackRock and its external Aladdin clients are hosted on Microsoft Azure and Amazon Web Services."
- The same 10-K also says (10k_lines.txt:726) that regulation "has required BlackRock to open data centers in those jurisdictions in order to host client data in the client's home location". A plain "Microsoft Azure today" therefore says less than the filing does.
- The AWS release FAQ (register 21; linkcheck/pages/5.html) gives the timing: "General availability for Aladdin Enterprise clients hosted in the United States is expected in the second half of 2026", and "Amazon Treasury will be among the first adopters". Today, 2026-10-20, falls inside that window. One WebSearch found no public statement either way on GA, so "not live" cannot be supported from the public record. BlackRock's filing reads the other way.
- "Azure today" itself is supported by the Microsoft blog (register 35), as quoted in 04-transcripts/part1-youtube-and-site/15_Reference_pages_text.md:203: "Today, all BlackRock's technology platform clients and services are hosted in the Azure cloud". That blog is dated December 2024 and predates the 10-K.
- Why it matters: an analyst or a BlackRock reader holding the 10-K will see the exhibit contradict the filing that the document cites for revenue.
- Smallest fix: make the hosting row "Microsoft Azure and AWS (10-K)" with a hatched sub-label "AWS for new US Aladdin Enterprise clients: GA expected H2 2026". Change the note to: "The 10-K says Aladdin is hosted on Azure and AWS; the AWS release dates general availability for US Aladdin Enterprise clients to the second half of 2026." Cite 12 as well as 21 and 35, and delete "not live".

---

## WEAKENS IT

### W1. The stack puts BlackRock's ~100 apps and Copilot above Studio. Exhibit 14 and the document's own text treat them as parallel to Studio.
- Exhibit 3's layer order (Who builds, then BlackRock's applications, then Studio, then shared services) reads as "BlackRock's apps and Copilot run on Studio", and as "client builders work inside BlackRock's apps".
- Exhibit 14 on page 12 draws it differently. "BLACKROCK'S OWN USE" (apps, Copilot) sits beside "A CLIENT'S USE · THROUGH STUDIO", and both "draw on Aladdin's shared services and APIs" (doc.txt:611-626). Its apps box says the apps "draw on Aladdin's shared services", not on Studio.
- On page 10 the document calls the link an inference: "So I infer that Copilot and Studio use the same APIs" (doc.txt:439). The stack shows that inference as structure.
- BlackRock's own placement: the Aladdin site navigation lists Studio under "Solutions" as a peer of Copilot, Data Cloud and Accounting (fc/dl/b024/live/apis.txt:33-36 and studio_page.txt:33-39). Woodhead calls Studio "the user experience that allows people to think of Aladdin as a platform" (doc.txt:240). The Studio page says "Build on top of Aladdin" (studio_page.txt:183). None of these puts the apps on top of Studio.
- Rosales says the domain teams "own all of the services that serve trading data to all Aladdin applications" (04-transcripts/timestamped/yt_oyqeCHFM5U4.m4a.ts.txt, 4:06-4:14). On this account the apps draw on services, not on Studio.
- Partial support for the current order, for fairness: the Aladdin Graph posting says the team builds "for BlackRock and over 200 institutions", covering "production runtime infrastructure for APIs and events" (SP/jobpost/r266598.html). The Investor Day 17x figure counts "API Calls" across "BlackRock + Aladdin" (id2025.txt:673). So BlackRock does use the API layer internally. What is not shown publicly is that its apps sit on Studio as a product.
- Smallest fix: put the applications-and-Copilot row and the Studio band side by side above the shared-services band. Label the left side "built by BlackRock" and the right side "built by clients, through Studio", and point "Who builds" only at the Studio side. This matches Exhibit 14. If the stack has to stay, add to the note: "Order shows reach, not dependency; that apps and Studio share the same APIs is my inference (page 10)."

### W2. eFront, Aladdin Wealth and Preqin are missing, though Exhibit 1 and Part 1 define Aladdin as four platforms
- Part 1 says: "BlackRock sells Aladdin as four platforms ... the Aladdin platform, eFront, Aladdin Wealth and Preqin" (doc.txt:71-72). The 10-K lists "Aladdin ®, Aladdin Wealth TM, eFront ®, Preqin, and Cachematrix ®" (10k_lines.txt:33), and the site navigation lists Platforms "Aladdin, Aladdin Wealth, eFront, Preqin" (apis.txt:25-31).
- Exhibit 3 is titled "Where Studio sits in Aladdin" but shows none of eFront, Aladdin Wealth or Preqin.
- The document says on page 8 that eFront and Preqin data go into Data Cloud, "which is part of Studio" (doc.txt:421-429). Newman, the General Manager of Aladdin Studio, says: "eFront's an obvious example of that, that data coming into the Aladdin Data Cloud. With the announcement of the Prequin acquisition, bringing in that data" (04-transcripts/product-pages/snowflake_audiocast.txt:112).
- The "Outside inputs" box calls vendor data external, yet Preqin has been owned by BlackRock since March 2025 (10k_lines.txt:282).
- None of the 54 public specifications covers eFront, Aladdin Wealth or Preqin. I checked by searching 02-api-catalog/apis.json for wealth, efront, preqin, private and alternative: there are no matches beyond generic "fund" wording.
- Smallest fix: add "eFront and Preqin data" to the data band, or as an arrow into Data Cloud, citing 22. Add one note line: "Shown: the Aladdin platform. The 54 public specifications cover none of eFront, Aladdin Wealth or Preqin (Exhibit 1)."

### W3. Exhibit 4 relegates ATX and ADX to a footnote line, while BlackRock's APIs page files them as Studio resources
- The live APIs page has a heading "Additional Aladdin Studio resources", and under it "Aladdin Studio home / Aladdin Data Cloud / Aladdin Data eXchange (ADX) / Aladdin Compute / Aladdin Tools for Excel (ATX)" (fc/dl/b024/live/apis.txt:122-127).
- Exhibit 4 gives Data Cloud and Compute full tiles but puts ATX and ADX in a footnote: "The APIs page also links Aladdin Tools for Excel and the Aladdin Data eXchange". That under-states how BlackRock groups Studio.
- It also clashes with Exhibit 3. There "Excel users building reports" is one of the four Studio builder groups, and "the Data eXchange" is a main route for outside inputs.
- The Aladdin Compute tile is sourced to Snowflake's archived 2024 partner page (register 42). BlackRock's own APIs page (register 30) names "Aladdin Compute" as a Studio resource.
- Smallest fix: change the line to "BlackRock's APIs page lists Data Cloud, ADX, Aladdin Compute and ATX as 'Additional Aladdin Studio resources'". Add 30 to the Compute citation.

### W4. Asset servicers and the ecosystem partners that the 10-K names are dropped, though Exhibit 1 has Aladdin Provider
- The 10-K's one sentence about opening Aladdin (10k_lines.txt:299): "BlackRock is empowering clients with data and APIs, as well as creating connectivity with ecosystem providers and third-party technology solutions, which include asset servicers, cloud providers, digital asset platforms, trading systems and others." It repeats at 10k_lines.txt:1211 and on the Q4 2022 call (fc/dl/b061/fool/blackrock-blk-q4-2022-earnings-call-transcript.txt).
- The Investor Day deck lists "Asset servicers" and "Service providers" among client types (id2025.txt:772).
- Exhibit 1 has Aladdin Provider ("custodians and administrators", doc.txt:90). Newman puts "firms that do asset servicing" into the Data Cloud picture (snowflake_audiocast.txt:108).
- Exhibit 3 shows neither group. Per BUILD_NOTES, "Brokers and custodians" were dropped from the earlier map.
- This is the closest filing language to Studio's purpose, and the document never quotes it.
- Smallest fix: add "asset servicers, trading systems and other connected providers (10-K)" to the Outside inputs box, cite 12, and quote the sentence in the note.

---

## NIT

- N1. The row label "BlackRock's applications" can read as internal-only. Rosales calls them "around 100 Aladdin front-end applications that thousands of people use every day" (ts.txt 1:53), and Exhibit 1 calls Copilot "available to all Aladdin clients" (doc.txt:88). Exhibit 14's heading "BLACKROCK'S OWN USE" makes this worse. Fix: "Aladdin's applications (built by BlackRock, used by clients)".
- N2. The tile "APIs (Aladdin Graph)" ties Graph to the APIs only. The Graph posting describes "production runtime infrastructure for APIs and events" (jobpost/r266598.html). Fix: "APIs and events run on Aladdin Graph" in the note, or rename the tile.
- N3. The shared-services band leaves out the books of record. Newman: "It does start with IBOR" and "the core IBOR and ABOR information" (snowflake_audiocast.txt:108, 113). The Investor Day slide 41 layers "Investment book of record ... workflow and data ... accounting" (id2025.txt:1308). Fix: append "on the investment and accounting books of record (IBOR, ABOR)". This is consistent with Exhibit 2's point that no position API is public.
- N4. The investor term is missing. Investor Day lists "Aladdin as a platform" as an Aladdin growth driver (id2025.txt:1149, slide 35), and the flywheel slide reads "Growing Aladdin as a Platform". Tagging the Studio band "BlackRock's 'Aladdin as a platform' growth driver (Investor Day 2025)" would tie Exhibit 3 to the investor story in Finding 2. This is OPINION on value, but the term itself is sourced.
- N5. The Data Cloud tile omits how it is sold. Exhibit 1 says "sold as an add-on to Aladdin Enterprise", and the calls describe it the same way (Q3 2022, Q4 2024: "clients leveraging enterprise Aladdin, alongside Aladdin Accounting or the Aladdin Data Cloud", fc/dl/b061/fool/blackrock-blk-q4-2024-earnings-call-transcript.txt). Investors hear of Data Cloud as a separately sold product. Fix: add "sold as an add-on" to the tile, or point to Exhibit 1.
- N6. "Aladdin Compute" (top half) and "Studio Compute" (workspace half) appear as two items. Public sources do not say whether they are one product. The split implies they are distinct. OPINION. Fix: add "(likely the same service)" or merge them.
- N7. Exhibit 1's source line and register 21 date the AWS release December 5, 2025. That is the Zawya/Reuters redistribution; the original is dated December 1, 2025 (linkcheck/pages/50.html: "New York— December 1, 2025"). Outside page 4, but it is the hosting source.

---

## Holds up

- **Shared-services band.** It matches the filings closely. The 10-K says: "combine risk analytics with portfolio management, trading and operations tools on a single platform" (10k_lines.txt:629), plus Aladdin Risk and "investment accounting capabilities" (10k_lines.txt:277). The Studio page's own tagline is "our API-first approach across shared services and data" (studio_page.txt:181), so the band's name is BlackRock's.
- **Studio above the shared services.** The Studio page supports it: "Build on top of Aladdin"; "innovating on the Aladdin platform through Studio" (studio_page.txt:181-183).
- **About 100 apps, Copilot inside all of them, each tool mapped to a production API.** Rosales says it verbatim: "embedded across all of those hundred front-end applications"; "mapping one-to-one to an existing Aladdin API already out in production" (ts.txt 2:32-2:41, 4:31-4:39).
- **Azure as the main host.** Consistent with the Microsoft blog and with the cloud-migration commentary on the earnings calls ("migrating Aladdin clients to the cloud, which is now substantially complete", Q4 2022 call). Only the AWS half is wrong (B1).
- **Data Cloud inside Studio.** Supported three ways: Newman's "part of Studio", the APIs page listing it under "Additional Aladdin Studio resources", and Exhibit 1's "part of Studio".
- **Who builds.** The engineers, code-curious PMs and data analysts are the Studio page's own three personas (studio_page.txt:184). "Excel users" is supported by ATX's listing as a Studio resource (see W3).
- **The 11 domains, `agraph.<domain>` ids, the developer portal behind a login, and "No event specification is public".** All consistent with the specifications and the register. The core SDK's "Studio Subscription and Notification APIs" (readme.md:587) are for notifications, not data events, so "no event specification" stands.
- **Every lower-group item in Exhibit 4 traces to the SDK README or the AdcDataset spec**, as BUILD_NOTES documents.
- **Nothing on the page contradicts Exhibit 1's product rows** (Studio, Data Cloud, Copilot, Accounting). The conflicts are omissions (W2, W4) and the hosting line (B1).
