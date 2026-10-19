# Rewrites: Findings 3 and 4 and "What would change my view" (pages 12 to 15)

Scope: HTML lines 1087 to 1187 of `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.html`, from the Finding 3 heading to the end of the "What would change my view" list.

Word counts exclude superscript numerals and count each hyphenated or quoted token as one word, the same way the splitter does. "Current (HTML)" is the verbatim markup, so it can be matched. "Rewrite (HTML)" keeps every link, link phrase and superscript. Links are shown with their `href` cut to `…` for readability; the `href` values are unchanged.

## Summary of the re-scan

The splitter listed six items. My own scan of the section (every `p`, `td`, `th`, `li`, funnel box, exhibit title and source note) found:

| # | Page | Where | Words | Status |
|---|---|---|---|---|
| 1 | 12 | Exhibit 13, box "20 to 30 tools in play" | 33 | Missed by the splitter. Rewrite below. |
| 2 | 12 | Exhibit 13, box "Plan and call the API" | 30 | Missed by the splitter; 30 is not under 30. Rewrite below. |
| 3 | 13 | Exhibit 14 title | 30 | Missed by the splitter; 30 is not under 30. Rewrite below. |
| 4 | 13 | Exhibit 15, "For / Outside the login" cell | 37 | On the splitter's list. Rewrite below. |
| 5 | 13 | Exhibit 15, "Against / Inside the login" cell | 32 | On the splitter's list. Rewrite below. |
| 6 | 13 | Exhibit 15, "Against / Outside the login" cell | 34 | On the splitter's list. Rewrite below. |
| 7 | 14 | Finding 4, poll 1 sentence | 8 + 26 | False positive. The splitter joined "The first poll asked where firms sit today." (8 words) with the next sentence because it begins with a digit. The second sentence is 26 words. No change needed; an optional split is given. |
| 8 | 14 | Finding 4, Sewdass "The shift of the last two years is …" | 30 | The splitter merged this (30 words) with the next sentence (32 words) into one 62-word item because the first ends in `.”`. Both need a rewrite; given separately below. |
| 9 | 14 | Finding 4, Sewdass "That comes, she said, …" | 32 | See item 8. Rewrite below. |
| 10 | 14 | Finding 4, Sewdass "On AI, she said, …" | 34 | On the splitter's list. Rewrite below. |

Everything else in the section is under 30 words, including the Exhibit 14 source note (29 words for its longest sentence), the "Governance in one place" cell (28), the Exhibit 16 source note (29), the Schafer pull quote, the two direction boxes, and the five "I would revise" list items. No verbatim quotation in this section is over 30 words on its own, so nothing has to stay as it is.

---

## 1. Page 12, Exhibit 13, funnel box "20 to 30 tools in play" (33 words)

Current (HTML):

```
<div class="fbox" style="width:75%"><b>20 to 30 tools in play</b>: Copilot filters the registry by environment, user group and app, leaving <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“say, 20 to 30 tools and agents,”</a> because more than “40, 50 tools” would hurt performance<sup class="fnref"><a href="#s9">9</a></sup></div>
```

Current (text): 20 to 30 tools in play: Copilot filters the registry by environment, user group and app, leaving “say, 20 to 30 tools and agents,” because more than “40, 50 tools” would hurt performance 9

Rewrite (HTML):

```
<div class="fbox" style="width:75%"><b>20 to 30 tools in play</b>: Copilot filters the registry by environment, user group and app, leaving <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“say, 20 to 30 tools and agents.”</a> That is because more than “40, 50 tools” would hurt performance<sup class="fnref"><a href="#s9">9</a></sup></div>
```

Rewrite (text):
- 20 to 30 tools in play: Copilot filters the registry by environment, user group and app, leaving “say, 20 to 30 tools and agents.” (24 words)
- That is because more than “40, 50 tools” would hurt performance 9 (11 words)

Notes: the only change inside the link phrase is its final comma becoming a full stop, as in the document's other quotation-ending sentences. Without the bold label the original is 27 words, so this box is borderline; the rewrite is offered in case the label counts.

## 2. Page 12, Exhibit 13, funnel box "Plan and call the API" (30 words, not under 30)

Current (HTML):

```
<div class="fbox ai" style="width:62%"><b>Plan and call the API</b>: the orchestrator (the component that runs the loop) iterates <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a> with GPT-4 function calling, then output guardrails check for hallucinations<sup class="fnref"><a href="#s9">9</a></sup></div>
```

Current (text): Plan and call the API: the orchestrator (the component that runs the loop) iterates “over a planning and action node” with GPT-4 function calling, then output guardrails check for hallucinations 9

Rewrite (HTML):

```
<div class="fbox ai" style="width:62%"><b>Plan and call the API</b>: the orchestrator (the component that runs the loop) iterates <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a> with GPT-4 function calling. Then output guardrails check for hallucinations<sup class="fnref"><a href="#s9">9</a></sup></div>
```

Rewrite (text):
- Plan and call the API: the orchestrator (the component that runs the loop) iterates “over a planning and action node” with GPT-4 function calling. (24 words)
- Then output guardrails check for hallucinations 9 (6 words)

Notes: without the bold label the original is 25 words, so this is borderline like item 1.

## 3. Page 13, Exhibit 14 title (30 words, not under 30)

Current (HTML):

```
<p class="ex-title"><span class="ex-num">Exhibit 14.</span> Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data; Aladdin has only a job advert that mentions MCP</p>
```

Current (text): Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data; Aladdin has only a job advert that mentions MCP

Rewrite (HTML):

```
<p class="ex-title"><span class="ex-num">Exhibit 14.</span> Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data. Aladdin has only a job advert that mentions MCP</p>
```

Rewrite (text):
- Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data. (21 words)
- Aladdin has only a job advert that mentions MCP (9 words)

Notes: the "Exhibit 14." label is not counted. Only the second semicolon becomes a full stop.

## 4. Page 13, Exhibit 15, "For" row, "Outside the login" cell (37 words)

Current (HTML):

```
<td>Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors; and it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make<sup class="fnref"><a href="#s7">7</a>, <a href="#s63">63</a>, <a href="#s40">40</a>, <a href="#s8">8</a></sup></td>
```

Current (text): Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors; and it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make 7, 63, 40, 8

Rewrite (HTML):

```
<td>Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors. And it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make<sup class="fnref"><a href="#s7">7</a>, <a href="#s63">63</a>, <a href="#s40">40</a>, <a href="#s8">8</a></sup></td>
```

Rewrite (text):
- Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors. (23 words)
- And it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make 7, 63, 40, 8 (14 words)

Notes: the four superscripts stay together at the end of the cell, where the original had them. Source 8 (the webinar) supports both "the RFP question about connectors" and "the comparison buyers make", so moving it after "connectors" alone would narrow what it covers; it is left where it was.

## 5. Page 13, Exhibit 15, "Against" row, "Inside the login" cell (32 words)

Current (HTML):

```
<td>Prospects cannot see it, and nor can the AI tools that buyers already run; rivals set the terms of comparison; the only public description of the plugin model is one conference talk<sup class="fnref"><a href="#s9">9</a></sup></td>
```

Current (text): Prospects cannot see it, and nor can the AI tools that buyers already run; rivals set the terms of comparison; the only public description of the plugin model is one conference talk 9

Rewrite (HTML):

```
<td>Prospects cannot see it, and nor can the AI tools that buyers already run. Rivals set the terms of comparison; the only public description of the plugin model is one conference talk<sup class="fnref"><a href="#s9">9</a></sup></td>
```

Rewrite (text):
- Prospects cannot see it, and nor can the AI tools that buyers already run. (14 words)
- Rivals set the terms of comparison; the only public description of the plugin model is one conference talk 9 (18 words)

## 6. Page 13, Exhibit 15, "Against" row, "Outside the login" cell (34 words)

Current (HTML):

```
<td>More to secure and more to support; buyers would read a partial catalog as the whole catalog; and the regulatory optics of outside AI tools drawing on a platform that will not give advice<sup class="fnref"><a href="#s16">16</a></sup></td>
```

Current (text): More to secure and more to support; buyers would read a partial catalog as the whole catalog; and the regulatory optics of outside AI tools drawing on a platform that will not give advice 16

Rewrite (HTML):

```
<td>More to secure and more to support; buyers would read a partial catalog as the whole catalog. And the regulatory optics of outside AI tools drawing on a platform that will not give advice<sup class="fnref"><a href="#s16">16</a></sup></td>
```

Rewrite (text):
- More to secure and more to support; buyers would read a partial catalog as the whole catalog. (17 words)
- And the regulatory optics of outside AI tools drawing on a platform that will not give advice 16 (17 words)

Notes: superscript 16 stays on the "will not give advice" clause, which is the Copilot page's statement.

## 7. Page 14, Finding 4, poll 1 sentence (false positive: 8 + 26 words)

Current (HTML):

```
The first poll asked where firms sit today. 37 percent said they run “mostly vendor platforms,” 30 percent run a “hybrid,” 18 percent are “actively reevaluating,” and 15 percent are “mostly built in house”<sup class="fnref"><a href="#s8">8</a></sup>.
```

These are already two sentences: "The first poll asked where firms sit today." (8 words) and "37 percent said they run … “mostly built in house”" (26 words). The splitter did not break at the full stop because the next sentence begins with a digit. No change is needed.

Optional, if the editor prefers a shorter second sentence anyway (same facts, same order):

```
The first poll asked where firms sit today. 37 percent said they run “mostly vendor platforms,” and 30 percent run a “hybrid.” 18 percent are “actively reevaluating,” and 15 percent are “mostly built in house”<sup class="fnref"><a href="#s8">8</a></sup>.
```

- The first poll asked where firms sit today. (8 words)
- 37 percent said they run “mostly vendor platforms,” and 30 percent run a “hybrid.” (14 words)
- 18 percent are “actively reevaluating,” and 15 percent are “mostly built in house” 8 (13 words)

## 8. Page 14, Finding 4, Sewdass: "The shift of the last two years is …" (30 words, not under 30)

Current (HTML):

```
The shift of the last two years is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows.”
```

Current (text): The shift of the last two years is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows.”

The quotation is 22 words and cannot be split, so the split goes around it.

Rewrite (HTML):

```
She described the shift of the last two years. It is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows.”
```

Rewrite (text):
- She described the shift of the last two years. (9 words)
- It is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows.” (24 words)

Notes: "she" is Sewdass, named in the first sentence of the paragraph; the preceding sentence already has "she said". No superscript is attached to this sentence in the original; the paragraph's 8 comes after the next sentence (item 9).

## 9. Page 14, Finding 4, Sewdass: "That comes, she said, …" (32 words)

Current (HTML):

```
That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction,” so that clients can build “their secret sauce rebalancing tools” on top<sup class="fnref"><a href="#s8">8</a></sup>.
```

Current (text): That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction,” so that clients can build “their secret sauce rebalancing tools” on top 8.

Rewrite (HTML):

```
That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction.” Those APIs let clients build “their secret sauce rebalancing tools” on top<sup class="fnref"><a href="#s8">8</a></sup>.
```

Rewrite (text):
- That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction.” (20 words)
- Those APIs let clients build “their secret sauce rebalancing tools” on top 8. (12 words)

Notes: "so that clients can build … on top" becomes "Those APIs let clients build … on top", which keeps the purpose link between the APIs and the clients' builds. The first quotation's trailing comma becomes a full stop. Superscript 8 stays at the end of the pair, as in the original; it covers both quotations, which come from the same webinar.

## 10. Page 14, Finding 4, Sewdass: "On AI, she said, …" (34 words)

Current (HTML):

```
On AI, she said, “you need that system of record that underpins anything that AI is built upon,” and “the other layer that is almost equally important is a really defined system of work”<sup class="fnref"><a href="#s8">8</a></sup>.
```

Current (text): On AI, she said, “you need that system of record that underpins anything that AI is built upon,” and “the other layer that is almost equally important is a really defined system of work” 8.

Rewrite (HTML):

```
On AI, she said, “you need that system of record that underpins anything that AI is built upon.” She also said “the other layer that is almost equally important is a really defined system of work”<sup class="fnref"><a href="#s8">8</a></sup>.
```

Rewrite (text):
- On AI, she said, “you need that system of record that underpins anything that AI is built upon.” (18 words)
- She also said “the other layer that is almost equally important is a really defined system of work” 8. (18 words)

Notes: both quotations are intact; only the first one's trailing comma becomes a full stop. Superscript 8 stays at the end of the pair, as in the original.

---

## Items on the splitter's list that are not reproduced above

- The splitter's fifth item (62 words, "The shift of the last two years … on top.") is two sentences; see items 8 and 9.
- The splitter's fourth item (34 words, "The first poll asked … built in house") is two sentences of 8 and 26 words; see item 7.
