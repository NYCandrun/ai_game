import sys, io
path = "/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/gtm/out/Aladdin_Studio_With_AI.html"
html = open(path, encoding="utf-8").read()

R = []
def add(label, old, new): R.append((label, old, new))

# ---- A ----
add("A1 p8 scoring sentence",
 "It scores each on eight things a developer with no client relationship can reach, from 0 to 2, so the total sums eight scores and runs from 0 to 16.",
 "It scores each on eight things a developer with no client relationship can reach, from 0 to 2. The total sums the eight scores, so it runs from 0 to 16.")

# ---- B ----
add("B1 p10 Janus SDK commits",
 '<a href="https://github.com/blackrock/aladdinsdk/pull/53">custom headers</a>, both for firms that route Aladdin calls through an enterprise gateway.',
 '<a href="https://github.com/blackrock/aladdinsdk/pull/53">custom headers</a>. Both are for firms that route Aladdin calls through an enterprise gateway.')
add("B2 p10 public pension funds",
 "Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public, so they are the natural first candidates for a named Studio story.",
 "Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public. So they are the natural first candidates for a named Studio story.")
add("B3 p11 direction box",
 "Adoption is growing among client types whose records are public: between 2023 and 2025, a bank’s proxy statement, an asset manager’s 10-K and three public pension buyers’ notices all record Aladdin.",
 "Adoption is growing among client types whose records are public. Between 2023 and 2025, a bank’s proxy statement, an asset manager’s 10-K and three public pension buyers’ notices all record Aladdin.")
add("B4 p11 Exhibit 12 title",
 "On 26 earnings calls from Q1 2020 to Q2 2026, no BlackRock executive said “Studio”, “citizen developer” or “agent”; Data Cloud, API and Copilot came up about four times in total",
 "On 26 earnings calls from Q1 2020 to Q2 2026, no BlackRock executive said “Studio”, “citizen developer” or “agent”. Data Cloud, API and Copilot came up about four times in total")

# ---- C ----
add("C1 p12 fbox 20 to 30 tools",
 '<a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“say, 20 to 30 tools and agents,”</a> because more than “40, 50 tools” would hurt performance<sup class="fnref"><a href="#s9">9</a></sup></div>',
 '<a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“say, 20 to 30 tools and agents.”</a> That is because more than “40, 50 tools” would hurt performance<sup class="fnref"><a href="#s9">9</a></sup></div>')
add("C2 p12 fbox Plan and call",
 '<a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a> with GPT-4 function calling, then output guardrails check for hallucinations<sup class="fnref"><a href="#s9">9</a></sup></div>',
 '<a href="https://www.youtube.com/watch?v=oyqeCHFM5U4">“over a planning and action node”</a> with GPT-4 function calling. Then output guardrails check for hallucinations<sup class="fnref"><a href="#s9">9</a></sup></div>')
add("C3 p13 Exhibit 14 title",
 '<span class="ex-num">Exhibit 14.</span> Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data; Aladdin has only a job advert that mentions MCP</p>',
 '<span class="ex-num">Exhibit 14.</span> Two system-of-record rivals have announced AI features; the data and cloud providers have shipped or announced AI access to their data. Aladdin has only a job advert that mentions MCP</p>')
add("C4 p13 Ex15 For/Outside",
 '<td>Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors; and it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make<sup class="fnref"><a href="#s7">7</a>, <a href="#s63">63</a>, <a href="#s40">40</a>, <a href="#s8">8</a></sup></td>',
 '<td>Prospects can find it; developers adopt it on their own; it signals an ecosystem; a ready answer to the RFP question about connectors. And it matches what FactSet, LSEG and MSCI now offer, the comparison buyers make<sup class="fnref"><a href="#s7">7</a>, <a href="#s63">63</a>, <a href="#s40">40</a>, <a href="#s8">8</a></sup></td>')
add("C5 p13 Ex15 Against/Inside",
 '<td>Prospects cannot see it, and nor can the AI tools that buyers already run; rivals set the terms of comparison; the only public description of the plugin model is one conference talk<sup class="fnref"><a href="#s9">9</a></sup></td>',
 '<td>Prospects cannot see it, and nor can the AI tools that buyers already run. Rivals set the terms of comparison; the only public description of the plugin model is one conference talk<sup class="fnref"><a href="#s9">9</a></sup></td>')
add("C6 p13 Ex15 Against/Outside",
 '<td>More to secure and more to support; buyers would read a partial catalog as the whole catalog; and the regulatory optics of outside AI tools drawing on a platform that will not give advice<sup class="fnref"><a href="#s16">16</a></sup></td>',
 '<td>More to secure and more to support; buyers would read a partial catalog as the whole catalog. And the regulatory optics of outside AI tools drawing on a platform that will not give advice<sup class="fnref"><a href="#s16">16</a></sup></td>')
add("C8 p14 Sewdass shift",
 'The shift of the last two years is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows.”',
 'She described the shift of the last two years. It is “to more of a modular approach where clients are looking for that backbone foundational data that supports both publics and privates workflows.”')
add("C9 p14 Sewdass APIs",
 'That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction,” so that clients can build “their secret sauce rebalancing tools” on top<sup class="fnref"><a href="#s8">8</a></sup>.',
 'That comes, she said, with “very, very robust APIs that manage the end to end life cycle of a transaction.” Those APIs let clients build “their secret sauce rebalancing tools” on top<sup class="fnref"><a href="#s8">8</a></sup>.')
add("C10 p14 Sewdass AI",
 'On AI, she said, “you need that system of record that underpins anything that AI is built upon,” and “the other layer that is almost equally important is a really defined system of work”<sup class="fnref"><a href="#s8">8</a></sup>.',
 'On AI, she said, “you need that system of record that underpins anything that AI is built upon.” She also said “the other layer that is almost equally important is a really defined system of work”<sup class="fnref"><a href="#s8">8</a></sup>.')

# ---- D ----
add("D1 p17 About",
 "This is an independent analysis compiled from public sources: BlackRock product pages, SEC filings, procurement notices, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings.",
 "This is an independent analysis compiled from public sources. The sources are BlackRock product pages, SEC filings, procurement notices, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings.")
add("D2 p19 Source 6 speakers",
 "Melissa Faraz, Global Head of Business Development for Private Markets Analytics Platforms and Head of Preqin London; Paul McGaugh, Managing Director, Aladdin Private Markets Product; Cameron Skinner, Managing Director and Global Head of Solutions Engineering, BlackRock, September 2025.",
 "Melissa Faraz, Global Head of Business Development for Private Markets Analytics Platforms and Head of Preqin London. Paul McGaugh, Managing Director, Aladdin Private Markets Product. Cameron Skinner, Managing Director and Global Head of Solutions Engineering; all three at BlackRock, September 2025.")
add("D3 p20 Source 60 closing",
 "The episode also features Jess Fitzgibbon, Head of Product for Aladdin Risk; the recording does not label speakers, so the 10:00 passage is not attributed to either by name in this document.",
 "The episode also features Jess Fitzgibbon, Head of Product for Aladdin Risk. The recording does not label speakers, so the 10:00 passage is not attributed to either by name in this document.")

ok = True
for label, old, new in R:
    n = html.count(old)
    if n != 1:
        print(f"FAIL {label}: {n} occurrences")
        ok = False
if not ok:
    sys.exit(1)
for label, old, new in R:
    assert html.count(old) == 1
    html = html.replace(old, new)
    print("applied", label)
open(path, "w", encoding="utf-8").write(html)
print("done", len(R))
