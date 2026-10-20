# Group g06: drafted fixes

## p10-01 (FIX)

**Current:** BlackRock itself says growth will come from API calls, the fastest-growing measure it showed investors.

**Proposed:** BlackRock projects API calls across BlackRock and Aladdin to grow 17x by 2030, the steepest of the volume estimates it showed investors [10].

**Also change (Page 9 body, first sentence of finding 2 (owned by g05, p09-01). Same wrong words; keep the two wordings consistent.):** BlackRock tells investors growth will come from API calls, without naming the product behind them.  
-> See g05 p09-01. Any wording that states the 17x as a volume forecast, not a growth source, is consistent with this fix.

**Why:** Slide 23 of the 2025 Investor Day deck (source 10) lists four 2030 volume estimates under “4. Continuously drive marginal costs down”: portfolios 2x, model portfolios 4x, trade allocations 1.3x and “API Calls (#) 17x”. It is a volume forecast, and the growth areas BlackRock names for Aladdin are Whole Portfolio, Wealth and Data (slides 31 to 33).

## p10-03+p10-04 (FIX)

**Current:** The data it is adding, private markets and Preqin, arrives through Data Cloud and Explore. Both are Studio surfaces.

**Proposed:** The private-markets data it is adding from eFront and Preqin is going into Data Cloud, which is part of Studio [16].

**Also change (Page 9 body, opening sentence of the private-markets paragraph (optional, same overstatement of routes)):** The private-markets data BlackRock has been adding reaches clients through Data Cloud and Explore.  
-> Much of the private-markets data BlackRock has been adding reaches clients through Data Cloud and Explore.

**Why:** Newman, the Studio general manager (source 16), says eFront data is “coming into the Aladdin Data Cloud” and Preqin is “bringing in that data”, and calls Data Cloud “part of Studio”. No source calls Explore a Studio surface, and Preqin benchmarks also reach clients through Preqin Pro, eFront, Aladdin Wealth and APIs (BlackRock press release, July 8, 2026), so the sentence names only the Data Cloud route.

## p10-07+p10-10+p10-13 (FIX)

**Current:** , the AI inside the login, is built on the same APIs Studio exposes. It draws on a registry of plugins, “couple of thousands agents and tools,” built by Aladdin’s engineering teams. The first way a team adds a tool is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production” [8]. So Copilot’s tools are Studio’s APIs. Microsoft’s Adrian Crockett made the dependence plain on BlackRock’s podcast: “There’s no copilot without plug-ins” [53]. On the data side, BlackRock’s AI product head says the team is making sure “the data model itself is structured for agentic use cases” [54].

**Proposed:** , the AI inside the login, calls Aladdin’s production APIs as tools. It draws on a registry of plugins, “couple of thousands agents and tools,” built by Aladdin’s engineering teams. The first way a team adds a tool is “to define a tool as kind of mapping one-to-one to an existing Aladdin API already out in production” [8]. Teams can also register agents of their own [8]. Microsoft’s Adrian Crockett made the dependence plain on BlackRock’s podcast: “There’s no copilot without plug-ins” [53]. Studio “exposes everything Aladdin knows how to do” as APIs and events [1]. That Copilot and Studio use the same APIs is my inference [1, 8]. On the data side, a BlackRock product leader says the team is making sure “the data model itself is structured for agentic use cases” [54].

**Also change (Sources register, entry 54 (owned by g10, s54). The speaker at 17:37 refers to “what Pavana is speaking to”, so the entry must not name Pemmaraju as that speaker.):** Quoted at 10:00, 17:37. The episode also features Jess Fitzgibbon, Head of Product for Aladdin Risk. The recording does not label speakers, so this document does not attribute the 10:00 passage to either by name.  
-> See g10 s54. Suggested: Quoted at 17:37. The episode also features Jess Fitzgibbon, Head of Product for Aladdin Risk. The recording does not label speakers, so this document does not attribute the 17:37 passage to either by name.

**Why:** Rosales and Valdez (source 8) describe two ways to add a tool: “mapping one-to-one to an existing Aladdin API already out in production”, or teams registering “their own agents”. No source says these are the APIs Studio exposes, so the link rests on Woodhead (source 1, “It exposes everything Aladdin knows how to do as a set of APIs events”) and is marked as inference. In source 54 the 17:37 speaker refers to “what Pavana is speaking to”, so the quote is not Pemmaraju’s.

## p10-25 (FIX)

**Current:** One answer, never investment advice: Copilot’s standing instructions (its system prompt) are tested so it will “never provide investment advice” [8], and the product page says the same [17]

**Proposed:** One answer, never investment advice: the product page says Copilot “will not give investment advice” [17]. The team tests each rule written into its system prompts. The talk’s example rule is “never provide investment advice” [8]

**Why:** The talk (source 8) says the team writes test cases “for every intended behavior encoded in system prompts” and gives “you must never provide investment advice” as “a very dummy example”, so it is not a quoted rule from Copilot’s actual prompt. The Aladdin Copilot page (source 17, fetched October 20, 2026) does say “Aladdin Copilot: Will not give investment advice or respond to questions outside Aladdin platform boundaries”, so the no-advice claim keeps 17.

## p11-12 (FIX)

**Current:** Aladdin

**Proposed:** Aladdin, for comparison / Aladdin

**Why:** Aladdin is the platform under study, which BlackRock calls “a tech platform that unifies the investment management process” (blackrock.com/aladdin), so it sits badly under “Data and cloud providers”. A separate group row fixes the label without changing any count, because the title already counts Aladdin as the ninth provider.

## p11-34 (DECIDE)

**Current:** Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources. State Street, Clearwater and Bloomberg have none, so they are not listed.

**Proposed:** State Street is not listed because my sources show no AI feature it offers clients.

**New source:** NEW P Bloomberg Launches Enterprise MCP to Seamlessly Connect Bloomberg Data with Clients’ Enterprise AI Applications. Bloomberg press release (PR Newswire), September 29, 2026. https://www.webull.com/news/15660486556124160

**New source:** NEW P CWAN Reports 800+ AI Agents Now Available for Deployment Across $10 Trillion in Client Assets. Clearwater Analytics press release (Business Wire), November 5, 2025. https://www.businesswire.com/news/home/20251105092732/en/

**Also change (Exhibit 12 table, add Clearwater and Bloomberg rows after the Arcesium row (system-of-record rivals group)):** Arcesium press releases [56, 57]  
-> Arcesium press releases [56, 57] / Clearwater Clearwater announced CWAN GenAI, an AI platform with more than 800 AI agents for clients, in November 2025 Clearwater press release [NEW] / Bloomberg Bloomberg launched an MCP server for its licensed data in late September 2026 Bloomberg press release [NEW]

**Also change (Exhibit 12 title):** Of nine providers a Studio buyer compares, eight have announced AI features or AI access to their data  
-> Ten providers a Studio buyer compares have announced AI features or AI access to their data

**Also change (Page 10 prose before Exhibit 12):** Six data and cloud providers that Studio buyers also use offer a connector or an MCP server, and two system-of-record rivals have announced AI features.  
-> Six data and cloud providers that Studio buyers also use offer a connector or an MCP server. Four system-of-record rivals have announced AI features or AI access to their data.

**Also change (Part 3, page 13 (same length or shorter, so page 13 still fits)):** SimCorp has announced AI agents, Arcesium an AI platform, and other systems of record will likely follow [7, 56, 57].  
-> SimCorp and Clearwater have announced AI agents, Arcesium an AI platform, and others will likely follow [7, NEW, 56, 57].

**Also change (Exhibit 15 Bloomberg AI connector score and the 'cluster low' sentence on page 15 (owned by g09 p15-29 and g08 p15-118). g09 adds the same Bloomberg release to the register; keep one entry.):** Investment platforms cluster low because they gate.  
-> See g09 p15-29 and g08 p15-118.

**Also change (Alternative (if the author keeps Exhibit 12 at nine rows): replace the note sentence instead with this, and leave the title and prose as they are):** Among system-of-record rivals, only SimCorp and Arcesium have an AI announcement in my sources. State Street, Clearwater and Bloomberg have none, so they are not listed.  
-> Clearwater announced AI agents for clients in November 2025 [NEW]. Bloomberg launched an MCP server for its data in late September 2026 [NEW]. State Street is not listed because my sources show no AI feature it offers clients.

**Why:** Bloomberg announced Enterprise MCP, “an AI access layer for Data License Plus”, on September 29, 2026 (PR Newswire), and Clearwater “announced the global deployment of CWAN GenAI” with 800+ AI agents on November 5, 2025 (Business Wire), both before the October 2026 as-of date. Recommended: add both rows, which changes the exhibit title count and the prose count. State Street has stated AI plans but no client AI feature in the sources found, so it alone stays off the table.

## p11-35 (FIX)

**Current:** A public account of the Copilot plugin model would cover production Aladdin APIs, the same ones Studio exposes, each user’s own permissions, and tested no-advice guardrails [8, 17].

**Proposed:** A public account of the Copilot plugin model would cover the production Aladdin APIs its tools call, each user’s own permissions, and tested no-advice guardrails [8, 17].

**Why:** Source 8 supports “an existing Aladdin API already out in production”, but no source says these are the APIs Studio exposes, so that phrase goes. Source 17 stays because the Copilot page says it “will not give investment advice”, which supports the no-advice guardrail.

## p11-38 (DECIDE)

**Current:** 4. Buyers at BlackRock’s own webinar said they want a core platform plus their own builds

**Proposed:** 4. At BlackRock’s own webinar, two thirds of attendees said they run vendor or hybrid platforms

**Also change (Page 12 body, first sentence of the rivals paragraph (repeats the same 'want' claim)):** Rivals are selling to the same buyer, the one who wants a core platform plus their own builds.  
-> Rivals sell the same model, a core platform with the client’s own builds on top.

**Also change (Alternative heading, if the author wants to keep the core-plus-builds idea in the title):** 4. Buyers at BlackRock’s own webinar said they want a core platform plus their own builds  
-> 4. BlackRock’s own webinar panel described a core platform plus each firm’s own builds

**Why:** Attendees reported where they sit today, “mostly vendor platforms at 37%” and “hybrid ... at 30”, so 67 percent (source 9, 00:04:40). The core-plus-builds model is the panel’s description: Schafer says hybrid firms use “vendor platforms ... as the core architecture” and build around it, and Sewdass calls it “that hybrid approach” (00:05:15, 00:49:09). No attendee said they want it.
