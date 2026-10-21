# Fix panel: the actual reader (BlackRock, head of go-to-market for Aladdin)

## 1. My stance

I would read v23 as the work of someone who understands Aladdin's plumbing better than most outside candidates. I would also see three things wrong with the commercial judgment. First, it has the competitive picture backwards: Arcesium's MCP server already acts, and Clearwater and SimCorp have agents in production. Second, it hangs our 17x API-call estimate on Studio, though slide 23 is about scale and cost and never names Studio. Third, it leaves our own Copilot out of a competitive table and pitches a compliance switch that can be turned off. Those are the fixes that would change my opinion of the author. Most of the rest I would never notice. The evolved thesis is the most valuable change on the list. It is close to what our own Head of Product for AI said clients are asking for, so a short, confident v24 helps. A long "corrections" mail would hurt.

Counts: **ACCEPT 40, ACCEPT WITH CHANGE 19, REJECT 0, DEFER 2**. The evolved thesis gets ACCEPT, with conditions on where its caveats go.

## 2. Verdicts

The reader column means: **N** = I would notice in v23 and it shapes my view of the author. **n** = a specialist on my team might notice. **–** = I would never notice.

### Evolved thesis: ACCEPT (with conditions)
"Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls."
- I would act on this as a hypothesis and take it to the Aladdin product and AI leads. It matches demand we have heard ourselves. On the Never Done podcast (source 71, published transcript), Microsoft's Crockett raised clients using "your plug-ins in their custom copilot". Syril Smith Garson replied "And we are hearing that from our clients."
- It is also more defensible than "act under the same controls". SimCorp now claims "controlled access … within a common governance framework" (source 7), so governance alone is no differentiator. "The tools BlackRock's own Copilot already runs on" is.
- Conditions:
  - (a) The model-side caveat goes in Part 3's text, not only in Exhibit 14. A client brings its own model, so Copilot's guardrails, planning loop and AI-graded tests do not travel with it.
  - (b) The MCP route appears once, labelled as inference. Wording: "My inference is that one route would be an MCP server that offers the registry's tools to a client's own AI tools."
  - (c) "What would have to be true" gains a fourth condition on packaging and price (see section 4).

### Tier 1
| # | Verdict | Reader | Reasoning and wording |
|---|---|---|---|
| 1 | ACCEPT WITH CHANGE | N | Use the evolved thesis on the cover, p2 and p12. Also add condition (b) above, word for word, on p12. |
| 2 | ACCEPT WITH CHANGE | N | "Most mapped to production Aladdin APIs" has no source; the talk names two ways to register, with no proportion. "These APIs" contradicts fix 33. Replace with: "BlackRock already runs AI on Aladdin. Copilot answers questions for staff and clients by calling about two thousand registered tools and agents. Teams can register a tool that maps one to one to an Aladdin API already in production. Public sources show Copilot answering, not acting." |
| 3 | ACCEPT WITH CHANGE | N | This is the fix I care about most. As proposed, it calls SimCorp's agent "acting", which no source shows. Its "production APIs and controls it sells" also contradicts fix 33. Replace with: "Rivals have begun letting AI agents act. Arcesium's MCP server lets outside AI tools build pipelines and create quality rules, and Clearwater says its agents act inside its platform. SimCorp has announced controlled access for agents that clients build. BlackRock runs Copilot across about 100 of its own applications." Cite the Aquata MCP feature page as a new source entry, plus sources 8, 7 and 9. On p12, delete "unlikely to stay unique" and use the same facts. |
| 4 | ACCEPT | N | Correct, and it removes a contrast any Arcesium seller would quote back. |
| 5 | ACCEPT | n | Accept the p2 and p5 wording as given. Adding Aladdin user permissions also improves the commercial story, because it is the strongest public control. |
| 6 | ACCEPT WITH CHANGE | N | The facts are right, but the four-sentence version does not belong in the executive summary. It reads like a security finding and costs p2 two lines. Keep p2 as v23 has it, ending "The caller can turn it off". On p12 use: "Posting an order runs compliance by default. The caller can turn the check off with the same scope it uses to post. If the check runs past a set time, the order posts with compliance pending. Whether Aladdin user permissions limit this is not public. TradeAPI posts trades with no compliance setting." |
| 7 | ACCEPT WITH CHANGE | N | A misread investor slide is the error I would hold against a GTM hire. Accept the p2 sentence. For p8, "They include BlackRock's own applications and Copilot" asserts what the slide does not say, so use: "The slide counts calls across BlackRock and Aladdin and does not say who makes them. How many would come through Studio is not public." p8 heading: "2. BlackRock tells investors Aladdin is growing as a platform, but has not named Studio to them". p9 box: "BlackRock tells investors it is 'empowering clients with data and APIs' and lists 'Aladdin as a platform' among Aladdin's growth drivers. Its new eFront and Preqin data is going into Data Cloud, which is part of Studio." |
| 8 | ACCEPT WITH CHANGE | n | Add the licensing condition, or it reads as open access: "A licensed client's programs, AI agents included, can already call the APIs with credentials registered in Studio. BlackRock has published no support, guidance or connector for AI agents." |
| 9 | ACCEPT WITH CHANGE | N | Use the source 71 exchange with the full name and accurate turn-taking. Drop the job posting from Exhibit 14, because it is about internal tooling. Exhibit 14 hatched box: "How they would connect is not published. Asked about clients using Aladdin plug-ins in their own copilots, BlackRock's Head of Product for AI said 'we are hearing that from our clients'." The posting can stay, described accurately, only in the Exhibit 12 note (see 17). |
| 10 | ACCEPT WITH CHANGE | N | The facts are right, but row 2 is a product decision, not marketing work. Change "What it is" to: "Once BlackRock decides to offer it, a page on how a client's AI tools would call the same registered tools Copilot calls, under the same tool and user permissions, with a person approving before any order posts." |
| 11 | ACCEPT | N | The heading "BlackRock's own use" over apps that clients also use, and the client column holding Copilot's guardrails, would both catch my eye. Check that Part 3's text and the redrawn exhibit still fit on page 12. |
| 12 | ACCEPT | n | Khara's "over and above … front end applications" settles it. |

### Tier 2
| # | Verdict | Reader | Reasoning |
|---|---|---|---|
| 13 | ACCEPT | n | Orders do not live in Explore. A trading product manager would spot it. |
| 14 | ACCEPT | N | "Only mention is a job posting" invites a quick rebuttal. The new wording is safe. |
| 15 | ACCEPT | n | Arcesium's self-serve trial is something our competitive team knows. Re-total the scores. |
| 16 | ACCEPT WITH CHANGE | N | Give the count rather than "most". On the rows it is 8 of 11: Arcesium, Bloomberg, FactSet, LSEG, MSCI, S&P, Snowflake and Databricks. Title: "Eight of the 11 providers offer outside AI tools a connector or MCP server. Aladdin, SimCorp and Clearwater offer AI inside their platforms." |
| 17 | ACCEPT | N | A comparison that leaves out our own Copilot is the one I would mind most. Use the wording as given. |
| 18 | ACCEPT | – | Consistent with the scores. |
| 19, 20, 21 | ACCEPT | – | Accurate wording. I would not notice these. |

### Tier 3
| # | Verdict | Reader | Reasoning |
|---|---|---|---|
| 22 | ACCEPT | n | A safer title. |
| 23 | ACCEPT WITH CHANGE | – | The semicolon joins two sentences. Who: "The compliance engine runs it. Assigned owners resolve violations." API: "OrderAPI (runCompliance), and ViolationAPI to resolve violations". |
| 24 | ACCEPT | n | "Data Cloud" as the book of record would bother an operations reader. |
| 25 | ACCEPT | N | "Chose Aladdin and kept it" is accurate, and it is how we would say it in a pitch. |
| 26 | ACCEPT WITH CHANGE | N | A pension fund as the lead Studio case study is naive about client references, and PBGC is a federal agency. The proposed "keep pension funds … 'if they use Studio'" contradicts itself. Exhibit 15 row 3: "One client story, cleared for the Studio page and the RFP answer, from a client whose engineers have contributed to the SDK." On p8, replace the last two sentences of the paragraph with: "Firms whose filings or tenders already name BlackRock are easier to name in public as Aladdin references." |
| 27 | ACCEPT WITH CHANGE | n | The semicolon joins two sentences. The custodian point needs its source, and the "information-services line disappears" point from the Problem column must not go into the report, because it reads as insinuation about a major relationship. Note: "Disclosed because BlackRock owns more than 5 percent of JPMorgan. The proxies do not say which Aladdin services the payments cover. A 2016 trade press report says JPMorgan was connecting to Aladdin for its custody clients." |
| 28, 29, 30 | ACCEPT | – | Accurate. 30 also stops overclaiming from one client's code changes. |
| 31 | ACCEPT WITH CHANGE | n | "Most of them production Aladdin APIs" has no source (see 2). Title: "Copilot answers a question by picking from about two thousand tools and agents, then calling them". Keep the other three changes as proposed. |
| 32 | ACCEPT WITH CHANGE | N | Arcesium and Bloomberg let outside AI in, and the report does not group them with data providers. "Aladdin's own AI assistant works inside Aladdin. Other providers let outside AI tools in." |
| 33 | ACCEPT WITH CHANGE | n | The semicolon joins two sentences, and "most probably do not" is an inference presented as fact. "Copilot and Studio's public APIs run on the same Aladdin Graph runtime, and some public APIs back BlackRock's own screens, such as Risk Radar. Whether Copilot's tools use the public APIs is not public. With about 2,000 tools against 54 public APIs, I infer that most do not." Then make 2 and 3 agree with this, as done above. |
| 34 | ACCEPT WITH CHANGE | N | Reword each row to its source, using Audit E's strongest wording. Do not move Bloomberg out of the system-of-record group. AIM is a real rival, and moving it changes Exhibit 17 and the p14 sentence. Add to its row: "The MCP server is part of Bloomberg's Data License, not AIM." |
| 35 | ACCEPT | n | Internal consistency of the scores. A competitor would test it. |
| 36 | ACCEPT | N | Calling Snowflake a possible competitor in a document for BlackRock, when Snowflake is our Data Cloud partner, would grate. This fixes it. |
| 37, 38 | 37 ACCEPT. 38 ACCEPT WITH CHANGE | – | 38 joins two sentences with a semicolon. Portal: "Catalog, guides, field dictionary, notebooks and samples. The portal sits behind a client login." |
| 39–42 | ACCEPT | – (42 n) | The Q3 2026 call came before the document's date. Someone in IR would notice that 42 was missed. |

### Tier 4
| # | Verdict | Reader | Reasoning |
|---|---|---|---|
| 43–49 | ACCEPT | – | Precise and harmless. 45 also stops calling a cost slide a ranking of growth. |
| 50 | ACCEPT WITH CHANGE | N | Use BlackRock's own reported figure, not a derived one. Investor messaging leads with ACV, and the 10-K gives it: "Annual contract value grew 16 percent excluding Preqin." |
| 51–55 | ACCEPT | – | Accurate. |
| 56 | ACCEPT WITH CHANGE | N | Do not publish stability labels in an RFP answer. Publishing that 24 of 54 are alpha lowers our score. "It lists the APIs by area and marks which are stable." Keep "Snowflake (and Databricks, if offered) connectors". |
| 57–59 | ACCEPT | – | Accurate. |
| 60, 61 | DEFER | – | Optional. Spend the page space elsewhere. |

Items 62–69 (unused evidence): use 62, 63, 65, 66, 68 and 69. Number 69 matters most. SimCorp's Launchpad pitch is the evolved thesis in a rival's words, and admitting that is what makes the comparison credible.

## 3. Where the list's wording is wrong

1. **The list contradicts itself on whether Copilot uses the public APIs.** Fix 2 ("BlackRock already runs AI on these APIs") and fix 3 ("production APIs and controls it sells") say it does. Fix 33 says most of Copilot's tools probably do not. Fix 33 is right, and the evolved thesis depends on it, since the tools to open are the registry's tools, not the 54 specifications. My wording for 2 and 3 removes the conflict.
2. **"Most mapped to production Aladdin APIs"** (fixes 2 and 31) has no source.
3. **SimCorp "acting"** (fix 3). The source says only that a portfolio management agent is available today. Clearwater's "ready to act" is Clearwater's own claim and should be attributed to it.
4. **Semicolons joining two sentences:** fixes 23, 27, 33 and 38. (31 "One answer; policy: …" and 61 are fragments. I would still use a full stop.)
5. **Fix 26 contradicts itself.** "Keep pension funds as an Aladdin reference only, 'if they use Studio'" contradicts "reference only".
6. **Fix 6 is right in substance but wrong in placement.** On p2 it costs about two lines on a full page and gives the executive summary an exposé tone.
7. **Fix 8 leaves out "licensed".** As worded, it implies anyone can call the APIs.
8. **Fix 9 says "Garson".** The name is Syril Smith Garson, Head of Product for AI. "100%" answers Crockett's list of options. "We are hearing that from our clients" answers his point about plug-ins in a client's custom copilot. The wording should keep that order.
9. **Fix 7's p8 sentence** ("They include BlackRock's own applications and Copilot") states as fact what the slide does not say.
10. **Fix 34's "move Bloomberg"** would quietly change Exhibit 17 and p14. A note does the job.

## 4. What the list misses

1. **The p9 "direction" box would publish a map of the attack surface.** "BlackRock could publish … which production APIs each tool calls, which user groups may use each tool, and the tested guardrails". No one in our risk or security functions would allow this, and I would see it as naive. Replace with: "BlackRock could describe, at a high level, how Copilot's tools are registered, permissioned and tested."
2. **Exhibit 15 row 4 pitches the compliance switch.** "Posting an order runs compliance by default, unless the caller turns it off" is the wrong line for a demo in front of a buyer's risk team. Use the order lifecycle from item 66: "In the demo, the client's AI tool posts the rebalance as orders with compliance on. A portfolio manager authorises them, and a trader releases them." Keep the what-if test line.
3. **No word on how the AI route would be packaged or priced.** The report itself notes that fees follow position value and fixed rates, not API calls. Copilot is "available to all Aladdin clients". The questions a GTM head asks first are whether this is included, priced, or tied to Copilot, and who is accountable when a client's model proposes a bad order. Add a fourth condition on p12: "And BlackRock would have to decide how to package and price access for AI tools it did not build."
4. **Exhibit 15 has no owners or dependencies.** Only row 1 is marketing's to ship alone. Row 2 needs a product decision, row 3 needs client consent, and row 4 needs product and legal. One line in the note would show the candidate knows how the work actually gets done.
5. **Order of Exhibit 15.** I would start in the order 1, 4, 3, 2. The RFP answer is fast and measurable. The demo tests demand in meetings without a public promise. The client story follows. The public page comes after product commits. Today row 2 sits second.
6. **Timing for the client story.** The SDK contributor's firm is still mid-migration (its 10-K calls the move "a complex, multi-year initiative"). Clients rarely go on record before go-live, and the report should not name the engineer. Row 3 could add "after go-live".
7. **The headings "What this finding suggests about direction"** (four boxes). The author's rule bans "suggested". Ask whether it also covers "suggests". If so: "What this finding means for direction".
8. **Microsoft is the likely first client AI tool.** Source 71 is a Microsoft conversation, and many clients' "own copilot" will be Microsoft's. This is optional and only worth a clause in Part 3.

## 5. Whether to send v24, and how

- **Make v24.** Do Tier 1, fixes 13–17, 25, 26, 32, 34, 36, 50 and 56, plus section 4 items 1 to 3. Those are what I would notice. The rest are worth doing for accuracy, but none would change my view.
- **Do not send it as a corrected version.** v23 is already in my inbox. A second 19-page PDF with a list of changes, or "an audit found 61 errors", makes me count errors and reread nothing. Under no circumstances list the fixes.
- **What helps:** a three-sentence note, sent only if the interview is more than two working days away, with v24 attached. Something like: "Since sending this I have sharpened the central idea. Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls. The updated version also corrects the competitive picture: Arcesium, Clearwater and SimCorp have begun letting agents act." This reads as thinking that moved forward, which is what I am hiring for. If the interview is sooner, bring v24 printed and make the same point in person.

## 6. Top 5 recommendations, in priority order

1. **Fix the competitive picture (3, 4, 16, 17, 32, 34, using item 69).** Rivals already let agents act. Put our own Copilot in the comparison. Admit that SimCorp claims the same governance pitch.
2. **Adopt the evolved thesis (1, 10, 11)**, with the model-side caveat in Part 3's text and the MCP route labelled as inference. Make 2, 3 and 33 agree that the registry's tools, not the 54 public APIs, are what would be opened.
3. **Stop hanging 17x on Studio (7, 45).** Use the slide's real scope plus "Aladdin as a platform" and "empowering clients with data and APIs". Use ACV ex-Preqin rather than a derived figure (50).
4. **Make Exhibit 15 something I would act on.** Change the order to 1, 4, 3, 2. Drop the stability labels from the RFP answer (56). Rewrite the demo with compliance on and PM authorisation (section 4, item 2). Drop pension funds as the Studio case study (26). Add packaging and price as a condition.
5. **Replace the job posting with the source 71 demand quote (9, 14)** and the p9 "publish which APIs each tool calls" box (section 4, item 1). Then send v24 with a three-sentence note, not a list of corrections.
