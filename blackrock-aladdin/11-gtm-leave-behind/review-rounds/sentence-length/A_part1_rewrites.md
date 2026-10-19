# Sentence-length pass, section A: cover, executive summary, Part 1 (pages 1 to 9)

Method. I re-scanned pages 1 to 9 in both text.txt and the HTML (cover, `#executive-summary` and `#part-1` sections, up to `#f1`), stripping tags, superscripts, the SVG and the style block, and counting words in every paragraph, table cell, exhibit title, caption and source note. Word counts below are whitespace-split, with superscripts excluded.

Result. Of the five items on the splitter's list, none is a single sentence over 30 words: four are runs of two or three sentences the splitter failed to split (quotation marks and a parenthesis confused it), and one is the SVG label text of Exhibit 3, not prose. My own scan found one sentence the splitter missed that fails the rule: a 30-word sentence on page 8, which is not under 30. One rewrite is needed.

## Rewrite needed

### Page 8, prose paragraph after Exhibit 7

Current text (HTML, line 1016; no link or superscript inside this sentence):

> It scores each on eight things a developer with no client relationship can reach, from 0 to 2, so the total sums eight scores and runs from 0 to 16.

Word count: 30 (not under 30).

Rewrite:

> It scores each on eight things a developer with no client relationship can reach, from 0 to 2. The total sums the eight scores, so it runs from 0 to 16.

- Sentence 1: 18 words.
- Sentence 2: 13 words.

Facts kept: eight things, a developer with no client relationship, the 0 to 2 scale, the total as the sum of eight scores, the 0 to 16 range, and the causal "so". The surrounding sentences in the paragraph are unchanged. The preceding sentence ends with superscripts 33, 34, 35, which stay where they are.

## Items on the splitter's list that need no rewrite

### 1. Page 3, opening paragraph of Part 1 (listed as 40 words)

Current text (HTML):

> <a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“BlackRock is the biggest user of Aladdin, but we also sell and support hundreds of clients globally across 70 countries.”</a> The organization is “around 7,000 people, with over 4,000 of those being engineers.” They maintain “around 100 Aladdin front-end applications”<sup class="fnref"><a href="#s9">9</a></sup>.

This is already three sentences; the splitter did not break on the closing quotation marks.

- Sentence 1 (the linked verbatim quotation): 20 words.
- Sentence 2: 13 words.
- Sentence 3 (with superscript 9): 7 words.

No change. The link phrase and superscript 9 stay as they are.

### 2. Page 5, Exhibit 3 (listed as 243 words)

The text beginning "THE ALADDIN PLATFORM · INSTITUTIONAL PEOPLE Portfolio manager Trader ..." is the label text of the SVG diagram (`#pmap`): box titles and two- or three-word captions such as "Explore analyse portfolios, test trades" and "Shared API layer every app, Copilot and Studio call it · access checked on every call". None is a sentence of prose; the longest label phrase is under 15 words. The exhibit's title (25 words, "Exhibit 3. Every app, Copilot and Studio call one API layer, and the 11 public domains sit behind it") and its source note are separate and each sentence is under 30 words.

No change.

### 3. Page 7, SDK paragraph (listed as 44 words)

Current text (HTML):

> The SDK’s dependencies also <a href="https://github.com/blackrock/aladdinsdk/pull/57">conflict with the official MCP toolkit</a>. (MCP, the Model Context Protocol, is the standard AI assistants use to pull data from other systems.) An outside contributor’s fix for the conflict was merged in August 2026 and has not shipped<sup class="fnref"><a href="#s29">29</a></sup>.

Already three sentences; the splitter did not break before the parenthesis.

- Sentence 1 (with the link phrase "conflict with the official MCP toolkit"): 10 words.
- Sentence 2 (the parenthetical): 17 words.
- Sentence 3 (with superscript 29): 16 words.

No change. (The splitter's 44 comes from a stray " ." token left when it removed the link.)

### 4. Page 7, Exhibit 7 note (listed as 42 words)

Current text (HTML, line 1015):

> For the AI connector score: 2 means a connector that outside AI tools can use, such as an MCP server. 1 means one announced or in limited release. 0 means none, or an assistant that works only inside the vendor’s own platform.

Already three sentences; the splitter did not break before sentences that start with a digit.

- Sentence 1: 20 words.
- Sentence 2: 8 words.
- Sentence 3: 14 words.

No change.

### 5. Page 9, Exhibit 9 source note (listed as 34 words)

Current text (HTML, line 1042):

> Quotations are verbatim; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. – means the speaker does not name that part.

Already two sentences; the splitter did not break before the en dash.

- Sentence 1: 25 words.
- Sentence 2: 9 words.

No change.

## Borderline sentences checked (all under 30, no change)

For the record, the longest compliant sentences on pages 1 to 9, so the next pass knows they were counted:

- Page 2, executive summary: "Public documents prove named clients use Aladdin (none names Studio): JPMorgan Chase’s proxy statements, Janus Henderson’s commits and 10-K, Royal London’s chief executive on video, and three pension tenders." 29 words.
- Page 3: "Aladdin is sold the way enterprise platforms are sold: the conversation comes first, and documentation, a sandbox and credentials come from the solutions team once a prospect is qualified." 29 words.
- Page 4, Woodhead quotation, second sentence: "The Aladdin data cloud built on top of Snowflake takes all of that information that’s generated through our analytics factory and inside of Aladdin and pushes that into Snowflake." 29 words, verbatim quotation.
- Page 4, Exhibit 2 step 3: "The people who lead Aladdin Accounting say the run goes “from that first order through the trade, through all the operation protocols into accounting without lifting up the pencil”" 29 words.
- Page 2, stat-tile source note: "Sources, left to right: BlackRock 2025 Investor Day, slide on keeping the cost of growth low: API calls 17x, model portfolios 4x, portfolios 2x, trade allocations 1.3x." 28 words.
- Page 3, Exhibit 1 Studio row: "BlackRock calls it “API-first” and names three users: “a professional engineer ... or a data analyst automating reporting”" 28 words.
- Page 5, Exhibit 2 source note, first sentence: 28 words.
- Page 6, Exhibit 4 Event-driven APIs row: "Woodhead names “APIs events” as one part; Diwakar Goel, Global Head of Data, Aladdin, wants “every single transaction ... via an event, via an API”." 27 words.
- Page 4, Woodhead quotation, first sentence: 27 words, verbatim quotation.
