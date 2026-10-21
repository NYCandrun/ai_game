import html

# Panel votes, transcribed from the six full reports.
TPM_C = {1,2,3,4,5,6,7,9,10,11,12,14,16,21,22,23,25,26,27,28,29,31,32,33,34,36,37,38,41,42,51,52}; TPM_R = {61}
ENG_C = {1,2,3,5,6,7,8,9,10,11,14,16,20,22,23,24,27,29,31,33,38,41,61}
GTM_C = {1,2,3,6,7,8,9,10,16,23,26,27,31,32,33,34,38,50,56}; GTM_D = {60,61}
CI_A = {10,14,17,18,26,42,45,49,56}; CI_C = {1,2,3,4,9,15,16,32,34,35,36,59}
ED_A = {12,15,20,25,28,29,32,37,43,44,46,47,48,49,52,54,55,57,58,60}
DV_C = {2,10,13}; DV_D = {7,14,15,35,49}

def votes(n):
    def v(acc, chg=set(), rej=set(), dfr=set(), default='A'):
        if n in chg: return 'C'
        if n in rej: return 'R'
        if n in dfr: return 'D'
        if acc is not None: return 'A' if n in acc else default
        return default
    out = [
        ('Devil', 'C' if n in DV_C else ('D' if n in DV_D else 'R')),
        ('Mkt', 'C' if n in TPM_C else ('R' if n in TPM_R else 'A')),
        ('Eng', 'C' if n in ENG_C else 'A'),
        ('GTM', 'C' if n in GTM_C else ('D' if n in GTM_D else 'A')),
        ('CI', 'A' if n in CI_A else ('C' if n in CI_C else 'D')),
        ('Ed', 'A' if n in ED_A else 'C'),
    ]
    return ' '.join(f'{k}&nbsp;<b class="v{x}">{x}</b>' for k, x in out)

# (number, where, current v23 wording, recommended wording, why and disputes)
R = []
def add(*a): R.append(a)

T1 = "Tier 1. The thesis and its headline claims"
add(1, "Cover, p2, p12 and 8 other places", "Clients' AI tools could act on Aladdin under the same controls BlackRock uses for its own business.",
    "See Decision 2. Recommended: \"Through Studio, clients' own AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions.\" Apply in all 11 places the claim appears (the editor listed them).",
    "All six agree the old line merges two sets of controls. The devil would keep the old line on the cover and fix only Exhibit 15 row 2.")
add(2, "p2", "BlackRock's advantage is that it already runs its own business this way.",
    "\"BlackRock already runs AI on Aladdin. Copilot answers questions for staff and clients in about 100 Aladdin applications. It draws on about two thousand registered tools and agents, and each tool maps to an Aladdin API already in production. The team that owns each tool sets which environments, user groups and apps can use it. No public source shows Copilot posting orders.\"",
    "Unanimous that the old sentence is false. My list's \"most mapped\" and \"these APIs\" were unsourced, and the panel removed them. The devil prefers a one-line swap.")
add(3, "p2 \"will not be alone\"; p12 \"unlikely to stay unique\"", "Aladdin will not be alone in letting AI tools act. / Letting AI tools act is unlikely to stay unique.",
    "p2: \"Rivals have begun letting AI agents act. Arcesium's MCP server lets outside AI tools build data pipelines. Clearwater says clients use its agents for trade settlement and cash management. SimCorp offers a portfolio management agent and has announced Agent Launchpad for agents that clients build.\" p12 adds Arcesium's May 2026 AI platform (see Decision 6) and ends: \"What BlackRock can show is scale in production: Copilot runs across about 100 applications on about two thousand registered tools and agents.\"",
    "Five agree the framing is backwards. The devil says rivals are already named. SimCorp's source shows no agent acting, so SimCorp is described accurately, not as \"acting\".")
add(4, "p2", "Many data providers now offer AI tools a way to read their data. Aladdin's APIs can also write, not only read.",
    "\"Many data providers now let outside AI tools read their data. Aladdin's APIs can also post orders and assign compliance rules to portfolios.\"",
    "My \"some let them act\" had no source and was dropped. Arcesium is covered in fix 3.")
add(5, "p2, p5", "Access is granted per API, to read or to write. / With OAuth, access is granted per API and per action.",
    "p2: \"Each API has its own OAuth scopes, and most split read from write.\" p5: delete \"and per action\" and add \"The specifications also name Aladdin user permissions, set by function, action and portfolio.\"",
    "The engineer warns that the specs name permissions but do not show them enforced, so the wording describes, not asserts. The devil says the split holds for the APIs the thesis uses.")
add(6, "p2, p12, Exhibits 3 and 14", "Posting an order runs compliance by default. The caller can turn it off. Whether turning it off needs a separate permission is not public.",
    "p2: keep as is. p12: \"Posting an order runs a compliance check by default. The caller can skip that check with the same Order:write scope it uses to post. If the caller sets a time limit and the check runs over it, the order posts with the status Compl Pending. Whether an Aladdin permission restricts either option is not public. A portfolio manager authorizes each order before a trader works it, and the public order API has no call to authorize one.\"",
    "The reader and engineer both want the detail out of the executive summary. Adding the authorization step turns a weakness into the human-approval control.")
add(7, "p2, p8 heading and text, p9 box, p12", "API calls will grow 17x / I attribute those API calls to Studio / BlackRock's growth story to investors runs through Studio / two growth bets both run through Studio",
    "p2: \"BlackRock estimated that API calls across BlackRock and Aladdin would grow 17x by 2030.\" p8 heading: \"2. BlackRock tells investors Aladdin is growing as a platform, but rarely names Studio\". p8 text: \"The slide counts calls across BlackRock and Aladdin together and does not say who makes them.\" p9 box: \"BlackRock tells investors it is 'empowering clients with data and APIs' and lists 'Aladdin as a platform' among Aladdin's growth drivers. Studio is the product clients use to build on Aladdin.\" Add slides 33 and 35 to source 11.",
    "My \"They include BlackRock's own applications and Copilot\" was unsourced and is dropped. \"Rarely\", because one 2023 slide does name Studio.")
add(8, "p9, p12, Exhibit 14", "Aladdin has published no such route. / How those tools would connect is not public.",
    "\"A licensed client's own programs, AI tools included, can already call the APIs with credentials registered in Studio. BlackRock has published no guide or connector for AI tools.\"",
    "\"Licensed\" was added because licence terms on automated use are not public. The devil rejects any claim about what is allowed.")
add(9, "Exhibit 14 note, p9", "Nearest public sign: a September 2026 Forward Deploy Engineer posting ... that names MCP",
    "\"Asked about clients using BlackRock's plug-ins in their own copilots, BlackRock's Head of Product for AI said, 'we are hearing that from our clients.'\" [source 71, Never Done podcast, November 6, 2024] Drop the posting from Exhibit 14. Keep it on p9, described as an internal data-platform role.",
    "I checked the transcript. \"100%\" follows Crockett's list ending with plug-ins in a client's own copilot. Dated, because it is two years old.")
add(10, "Exhibit 15 row 2", "A page on how a client's own AI tools could read data and take actions through Aladdin's APIs, under the same permissions, compliance checks and guardrails Copilot uses.",
    "\"Once BlackRock decides to offer it: a page on how a client's AI tools could use the tools Copilot uses, for each user under that user's Aladdin permissions, with a portfolio manager authorizing each order before it trades.\"",
    "Unanimous. My \"approval before any order posts\" had the order wrong: an order is posted, then authorized. The reader notes this row needs a product decision first.")
add(11, "Exhibit 14 (p12)", "Two columns headed \"BlackRock's own use\" and \"A client's use\"; Copilot's guardrails under the client column; legend covers boxes only.",
    "Redraw. See Decision 3.", "Five accept a redraw. The devil rejects it on page-fit grounds, which no longer apply.")
add(12, "Exhibit 3 (p4)", "Layers stack Studio under BlackRock's applications.",
    "Redraw side by side. See Decision 3.", "Same split as fix 11.")

add(13, "Exhibit 2, Order \"Where\" and caption", "Explore what-if 27",
    "\"Order Monitor in Aladdin Dashboard\" [source 6, the API specifications]. Delete the Explore training recording [source 27] from the caption.", "Unanimous, the devil included.")
add(14, "p9, Exhibit 12 note", "Its only public mention of MCP is a job posting 73.",
    "\"BlackRock has published no MCP server or AI connector for Aladdin.\"", "\"AI connector\", because Data Cloud has a Snowflake connector.")
add(15, "p14, Exhibit 17", "a first API call needs a contract or a relationship, at Aladdin as at ... Arcesium; Arcesium first call 0",
    "Arcesium first call 1, trial stays 1. \"Investment platforms score low because a first API call needs a client relationship at Aladdin, Bloomberg, State Street, SimCorp and Clearwater. Arcesium offers its Aquata data platform on a 30-day trial.\" [source 96, Aquata Demo Center]", "Verified in source 96.")
add(16, "Exhibit 12 title", "Ten of the 11 providers I compared have announced AI features or AI access to their data",
    "\"Eight of the 11 providers offer outside AI tools a connector or an MCP server. Aladdin's AI, like SimCorp's and Clearwater's, works inside the platform.\" Update the page 9 counts to match.",
    "My premise was wrong. The devil and I checked: Aladdin is a separate comparison row, so \"Ten of the 11\" was arithmetically right. The title still changes because Aladdin meets its test.")
add(17, "Exhibit 12 Aladdin row", "A Forward Deploy Engineer posting ... names Model Context Protocol (MCP)",
    "\"Copilot for clients, inside the platform. No published connector for outside AI tools.\" [source 23, the Copilot page]", "The reader: \"the comparison I would mind most\".")
add(18, "Exhibit 17 title", "Data platforms open to any developer, investment platforms like Studio mostly to clients",
    "\"Snowflake and Databricks are self-serve. Most others, Studio included, open fully only to clients.\"", "")
add(19, "Exhibit 2 Valuation", "Each valuation carries an exception list", "\"Each valuation counts its exceptions. Another call lists them.\"", "")
add(20, "Exhibit 4 SDK tile", "typed clients for the APIs and Data Cloud, with login, retries and rate limits built in",
    "\"Open-source Python library with typed clients for the APIs and a Snowflake connection for Data Cloud, with login and retries built in.\"",
    "The engineer: the SDK applies only limits the user sets, not BlackRock's quotas.")
add(21, "Exhibit 6 Miller; Exhibit 7 note", "replaced \"flat files ... FTP and related transfers\"",
    "\"Data Cloud is 'much simpler' than sending flat files over FTP.\" Fix the Exhibit 7 note to match.", "The devil calls \"replaced\" a fair paraphrase. ADX still does bulk file transfer.")

add(22, "Exhibit 2 title", "The public APIs cover a trade from order to NAV, except positions",
    "\"The public APIs post orders and trades, and read lots and valuations. None reads portfolio holdings.\"", "")
add(23, "Exhibit 2 Compliance", "Who: No one / Runs automatically",
    "Who: \"Runs automatically. The owner of each violation resolves it.\" API: \"OrderAPI (runCompliance), then ViolationAPI to resolve\".", "The check runs inside the order post, not in the APIs v23 named.")
add(24, "Exhibit 2 Position", "Where: Data Cloud / Positions appear only as fields in other APIs",
    "Where: \"Read from Data Cloud, which carries IBOR holdings\". Detail: \"No holdings API.\"", "")
add(25, "p8", "a buyer wants to know that another institution built on the platform and stayed",
    "\"...because Studio is sold for building on Aladdin, and a buyer who builds on a platform wants to know that other institutions chose it and kept it.\"", "The devil reads the old sentence as about what a buyer wants. The new wording states the link explicitly.")
add(26, "p8, Exhibit 15 row 3", "public pension funds ... natural first subjects for a Studio case study",
    "Row 3: \"One named client that builds with Studio.\" p8: \"Firms whose filings or tenders already name BlackRock are easier to name in public as Aladdin references.\"",
    "The devil notes that the US federal rule my list cited does not bind UK pension bodies. The recommendation holds either way.")
add(27, "Exhibit 8 note", "The grey 2016 bar is a payment for integration services; the figures in the text start with 2017. JPMorgan is also a custodian...",
    "\"Disclosed because BlackRock owns more than 5 percent of JPMorgan. The proxies do not say which Aladdin services the payments cover. A 2016 trade press report says JPMorgan was connecting to Aladdin for its custody clients.\"",
    "This also removes a v23 semicolon. The reader advises leaving out the disappearing information-services line, because it reads as insinuation. The marketer would include it.")
add(28, "p5", "Compliance rule assignments move through review states before they are approved",
    "\"Compliance rule assignments carry a review state, such as draft, review required or approved.\"", "")
add(29, "Exhibit 14 Approvals", "Capital flows record who approved them.",
    "\"Capital flows need the user's Aladdin cash permissions and record who authorized and approved them.\"", "Callers can create a flow already authorized, so no sequence is implied.")
add(30, "Exhibit 14 client tiles", "Route Aladdin calls through the client's own gateway. / Run in the client's own environment",
    "\"Can route calls through the client's own gateway.\" \"Run in the client's environment or in Aladdin Compute.\"", "")
add(31, "Exhibit 11 (p9)", "...then calling production Aladdin APIs; no input guardrail step",
    "Add \"Input guardrails\" first. Title: \"...then calling tools, each mapped to a production Aladdin API, and agents\". Add \"as of the May 2025 talk\". Last box: \"One answer. The product page says Copilot will not give investment advice.\"", "")
add(32, "p9 Finding 3 heading", "Aladdin's AI works only for logged-in users. Data providers let outside AI tools reach their data.",
    "\"3. Many providers let outside AI tools connect. Aladdin's own AI assistant works only inside Aladdin.\"", "")
add(33, "p9", "So I infer that Copilot and Studio use the same APIs.",
    "\"The public APIs are Aladdin Graph APIs, and some back BlackRock's own screens, such as Risk Radar. Copilot's tools map to Aladdin APIs already in production. Whether those include the public APIs is not public. Copilot draws on about two thousand tools and agents, and the public specifications hold 301 operations, so many of Copilot's tools likely sit on APIs clients cannot call.\"",
    "The engineer: compare with 301 operations, not 54 specs, and do not cite the \"Internal\" label.")
add(34, "Exhibit 12 rows", "SimCorp, Arcesium, Clearwater, Bloomberg, FactSet rows",
    "The competitive analyst's exact rows, keeping Bloomberg in the rivals group with \"its MCP covers Data License data\". Add dates to each row.", "Moving Bloomberg would conflict with Exhibit 17.")
add(35, "Exhibit 17 scores, legend, date", "State Street trial 1; Aladdin sample code 1; Bloomberg docs 1; MSCI sample code 1; legend 0 = \"None, or closed to non-clients\"; \"October 8, 2026\"",
    "State Street trial 0, Aladdin sample code 2, Bloomberg docs 2, MSCI sample code 2. Replace the legend: \"In every column, 0 means not reachable without a client relationship. The AI connector column scores whether a connector exists. Most connectors are for licensed clients.\" Date: \"October 8 to 20, 2026\".", "")
add(36, "p14", "10 platforms that may compete with Aladdin for certain uses",
    "\"Exhibit 17 puts Studio beside five investment platforms that compete with Aladdin and five data and cloud platforms, included as benchmarks for developer access.\"", "My \"Databricks is a named connector partner\" had no source and was dropped.")
add(37, "Exhibit 3 secondary", "Controls column spans every row; Data Cloud and ADX shown only as inputs", "Folded into Decision 3.", "")
add(38, "Exhibit 4 tiles", "ADC Admin Center: The screen for managing Data Cloud datasets / Developer Portal: Catalog, guides, field dictionary... behind a client login / Governance quote",
    "Admin Center: no change. Portal: \"Guides, behind a client login.\" Governance: quote only \"access management and usage monitoring\".", "Only \"guides\" is tied to the portal in the sources.")
add(39, "Exhibit 6 Goel", "every transaction via an event, via an API ... within 15 minutes of latency", "Prefix with \"Aims for:\".", "")
add(40, "Exhibit 1 title", "Of eight Aladdin products, Studio is the one for people who write code",
    "\"Of eight Aladdin products shown, Studio is the one for people who write code.\" Note: \"BlackRock lists four platforms and nine solutions.\"", "")
add(41, "Exhibit 16 and p13", "after qualification; Get help: SDK changes from outside developers...",
    "\"After becoming a client\" in all six places. Get help, public: \"No public support channel.\" Move the merged code changes to the Build row.", "")
add(42, "p8, Exhibit 10, register 64", "26 earnings calls, Q1 2020 to Q2 2026; six and a half years",
    "\"27 earnings calls, Q1 2020 to Q3 2026\", \"nearly seven years\". All six terms were recounted on Q3 2026, all zero. Name the transcript source used.", "")

add(43, "p5", "35 operations are marked long-running", "Your decision: cut. No change to v23. (Was: \"25 operations run as long-running jobs, and each of the 10 specifications that has them offers a status call.\")", "")
add(44, "Exhibit 4, Exhibit 2 note", "No event specification is public", "\"No public specification covers business events.\"", "")
add(45, "p8, p9 box", "four usage measures; fastest", "\"four volume estimates to 2030\". Drop \"fastest\".", "")
add(46, "Exhibit 10", "an add-on sold with Aladdin Enterprise", "\"cited among products clients use alongside Aladdin Enterprise\"", "")
add(47, "Exhibit 9 PPF", "up to £74.0 million ... estimate of up to £55 million; supplier's address", "Add \"over ten years\". Say \"supplier web address\".", "")
add(48, "Exhibit 9 PBGC", "about the same yearly price", "\"at the same yearly price\". The records name BlackRock, not Aladdin.", "")
add(49, "Register 3 and 58", "FactSet dated \"2025\"; 58 title mismatch", "Date 3 as December 16, 2025. Correct 58's title.", "")
add(50, "p3", "Its 24 percent rise includes Preqin", "Your decision: keep. Add \"Annual contract value grew 16 percent excluding Preqin.\"", "The reader: use BlackRock's own figure, not a derived one.")
add(51, "p12", "A 2026 job posting for Aladdin Graph ... over 200 institutions", "Delete the sentence. It repeats the client base line before it.", "")
add(52, "p12", "Copilot's guardrails are tested daily", "\"Copilot's system prompts are tested daily by AI judges\", placed with the controls that stay inside Copilot.", "")
add(53, "p6, Exhibit 7", "Only Woodhead names every part / names them all", "\"Only Woodhead lists all three parts in one definition.\"", "")
add(54, "Exhibit 6 title", "on the record", "\"in recordings\"", "")
add(55, "Exhibit 13", "would stop maintaining compliance reporting in house first",
    "Title: \"...would most like to stop maintaining, of four options\". Note: \"Respondents to a BlackRock webinar. Number not given.\"", "")
add(56, "Exhibit 15 row 1", "It lists the APIs by area, with stability labels. ... It covers Snowflake and Databricks connectors",
    "\"It lists the APIs by area and marks which are stable. It covers the Snowflake connection for Data Cloud, and how a client's own AI tools can call the APIs today.\"", "The reader: showing that 24 of 54 specs are alpha would cost marks.")
add(57, "Exhibit 16", "See the catalog: public", "\"Public, but only by unpacking the packages\"", "")
add(58, "Exhibit 4 note", "I read Studio Compute sessions as the SDK's name for Aladdin Compute", "Your decision: keep. \"The SDK uses both names for the same hosted environment.\"", "")
add(59, "Exhibit 12 smaller rows, note", "MSCI, S&P, Snowflake, Databricks rows; State Street note",
    "The competitive analyst's qualifiers. State Street note: \"State Street is not listed because I found no AI feature it has released to clients.\"", "")
add(60, "Exhibit 5 note", "", "Your decision: keep. Add \"five are marked for internal use\".", "")
add(61, "Exhibit 4 Spaces", "", "Your decision: keep. Add \"Spaces: named alongside Projects. Not described publicly.\"", "The marketer: not actionable. The reader defers. The others would add it.")

NEW = [
 ("N1", "Cover heading", "What public sources show.", "\"What public sources show, and one direction they point to.\"", "The marketer: the thesis is a proposal and should not sit under a findings heading."),
 ("N2", "p12 conditions", "Three things would have to be true ... BlackRock would have to open its controls to tools it did not build.",
  "\"Four things would have to be true. Clients would have to want Aladdin's tools inside their own AI tools, and later want those tools to act. Their risk teams and regulators would have to accept it, with a portfolio manager authorizing each order. BlackRock would have to offer tools it built to AI models it did not build. And BlackRock would have to decide how to package and price that access.\"", "The marketer, reader and engineer each added part of this."),
 ("N3", "p12", "What BlackRock can show is its own use.", "Folded into fix 3: \"What BlackRock can show is scale in production...\"", ""),
 ("N4", "p10 direction box", "BlackRock could publish ... which production APIs each tool calls, which user groups may use each tool, and the tested guardrails that block investment advice",
  "\"BlackRock could describe how Copilot's tools are registered, permissioned and tested.\"", "The reader and engineer: no risk or security function would publish the tool-to-API map."),
 ("N5", "Exhibit 15 row 4", "Posting an order runs compliance by default, unless the caller turns it off...",
  "\"In the demo, the client's AI tool proposes a rebalance and posts it as what-if orders with compliance on. A portfolio manager authorizes them before a trader works them.\"", "The reader: do not pitch the off-switch to a buyer's risk team."),
 ("N6", "Exhibit 15 order and owners", "Rows 1, 2, 3, 4", "Reorder to 1, 4, 3, 2. Your decision: keep. Add the owners line: \"Only the RFP answer is marketing's to ship alone. The demo needs product and legal, the client story needs client consent, and the page needs a product decision.\"", "From the reader."),
 ("N7", "p12 identity", "(absent)", "\"Acting for each user\" means a delegated sign-in for that user. An application account would carry its own permissions.", "The engineer: this is what makes \"that user's permissions\" true."),
 ("N8", "Route label", "(absent)", "Label the route \"an MCP server or an agent protocol such as A2A, my inference\".", "The Copilot team said it is evaluating A2A and LangChain's agent protocol."),
 ("N9", "Why the tools matter", "(absent)", "Your decision: cut. No change to v23. (Was: \"Copilot's flagship example, a portfolio's exposure to a sector, has no public API today.\")", "The engineer: this is the concrete reason opening Copilot's tools adds something."),
 ("N10", "Register", "(absent)", "Add the Aquata MCP page and the State Street article. Fix numbering at 27/28 and 73/74.", ""),
 ("N11", "Existing v23 rule breaks", "p2, p7, p10, p13 semicolons; p6, p11 em-dashes", "Replace each with full stops or plain attribution lines.", "The editor found these."),
 ("N12", "Accessibility labels", "Exhibits 3, 11, 14", "Update to match the new text.", ""),
 ("N13", "Freshness checks before sending", "", "Check whether SimCorp Launchpad is live, and re-run the \"no rival lets outside AI tools post orders\" search.", "SimCorp said first clients get access \"this year\"."),
]

css = """@page{size:Letter landscape;margin:0.42in 0.45in}
body{font-family:Helvetica,Arial,sans-serif;font-size:8.3pt;color:#111;line-height:1.3}
h1{font-size:15pt;margin:0 0 3pt}h2{font-size:11pt;margin:12pt 0 4pt;padding:3pt 6pt;background:#111;color:#fff}
h3{font-size:9.6pt;margin:8pt 0 3pt}
p{margin:0 0 5pt}ul{margin:0 0 5pt 14pt;padding:0}li{margin:0 0 2pt}
.lead{font-size:9pt;color:#333}
table{width:100%;border-collapse:collapse;margin:0 0 6pt}th,td{border:1px solid #bbb;padding:3pt 4pt;vertical-align:top;text-align:left}
th{background:#eee;font-size:7.8pt}tr{break-inside:avoid}
td.n{width:20pt;text-align:center;font-weight:bold}td.w{width:62pt}td.cur{width:20%;color:#444}td.rec{background:#fff3c4;width:34%}
td.vt{width:66pt;font-size:7.2pt;line-height:1.5}
b.vA{color:#1a7f37}b.vC{color:#b26b00}b.vR{color:#c62828}b.vD{color:#666}
.box{background:#fff3c4;padding:6pt 8pt;margin:4pt 0 8pt}.k{font-weight:bold}
.dec{border:1.5px solid #111;padding:6pt 8pt;margin:0 0 8pt;break-inside:avoid}
.opt td{font-size:8.2pt}"""

def row(n, w, cur, rec, why):
    return f"<tr><td class='n'>{n}</td><td class='w'>{html.escape(w)}</td><td class='cur'>{html.escape(cur)}</td><td class='rec'>{html.escape(rec)}</td><td class='vt'>{votes(n) if isinstance(n,int) else ''}</td><td>{html.escape(why)}</td></tr>"

head = "<tr><th>#</th><th>Where</th><th>Now (v23)</th><th>Recommended, written to your six rules</th><th>Panel</th><th>Why, and disputes</th></tr>"

parts = []
parts.append(f"<!doctype html><html><head><meta charset='utf-8'><title>Proposed v24 changes</title><style>{css}</style></head><body>")
parts.append("""<h1>Proposed changes for v24: panel review</h1>
<p class='lead'>Nothing in the document has changed. This is for you to mark up.</p>
<p class='lead'>Six reviewers audited my 61-item fix list: a devil's advocate who wanted no changes, a technical product marketer focused on conceptual accuracy, a skeptical Aladdin Studio engineering leader, BlackRock's head of go-to-market (your reader), a competitive-intelligence analyst, and a senior editor. I read all six reports in full and checked the disputed points against the sources myself.</p>
<p class='lead'>Every recommended wording follows your rules:</p>
<ul class='lead'>
<li>Plain English.</li>
<li>No em-dashes.</li>
<li>No semicolons joining sentences.</li>
<li>Never "suggested".</li>
<li>New text states only the fact.</li>
<li>Say things explicitly.</li>
</ul>
<p class='lead'>Layout is left to fix later, as you asked, so no wording here was shortened to fit a page. Asides that do not serve the point have been cut. Your decisions on the extra-detail items are marked: keep 50, 58, 60, 61 and N6. Cut 43 and N9. Citations appear as [source N, name] so they do not read as part of the wording.</p>
<p class='lead'>Panel key: A accept, C accept with change (my recommendation uses the changed wording), R reject, D defer.</p>
<div class='box'><b>Bottom line.</b> Five of six reviewers back an evolved thesis and a v24. The devil's advocate argues for leaving v23 alone and fixing only three lines. All six agree on three changes: page 2's "already runs its own business this way", Exhibit 15 row 2's promise of Copilot's guardrails, and Exhibit 2's "Explore what-if". The panel also found real faults in my own fix list:
<ul>
<li><b>It contradicted itself</b> on whether Copilot uses the public APIs (fixes 2 and 3 against fix 33).</li>
<li><b>It got the approval order wrong</b> (fix 10).</li>
<li><b>It made claims with no source:</b> "most mapped", "some let them act" and "Databricks connector partner".</li>
<li><b>Fix 16 rested on a wrong premise.</b></li>
<li><b>Seven wordings broke the semicolon rule.</b></li>
</ul>
All of these are corrected below.</div>
<h2>Six decisions for you first</h2>
<div class='dec'><h3>Decision 1. Make a v24, and how to use it</h3>
<p><b>The devil's advocate:</b> don't re-send. A changed thesis two days after sending reads as insecurity. Fix three lines in your master copy and take the evolved thesis to the interview.</p>
<p><b>Your reader (head of go-to-market):</b> make a short, confident v24 and never present it as a list of corrections. If the interview is more than two working days away, attach it to a three-sentence note that leads with the sharpened idea. If it is sooner, bring it printed and say the same thing in person.</p>
<p><b>My recommendation:</b> make v24 and follow your reader's advice on how to share it. Both agree on one thing: never send a list of corrections.</p></div>
<div class='dec'><h3>Decision 2. The thesis wording</h3>
<table class='opt'><tr><th>Version</th><th>Wording</th><th>Problem</th></tr>
<tr><td>v23</td><td>Clients' AI tools could act on Aladdin under the same controls BlackRock uses for its own business.</td><td>It merges the API controls a client gets with Copilot's guardrails, which a client's own model cannot get. "Its own business" suggests AI already acts at BlackRock.</td></tr>
<tr><td>Our evolved draft</td><td>Clients' AI tools could call the same governed tools Copilot calls, under the same permissions and API controls.</td><td>"Same" covers two different gates: Copilot's tool registry and the public APIs' OAuth scopes. Nothing shows Copilot using OAuth scopes. "Governed" hints without naming. Studio is missing. "Act" quietly became "call".</td></tr>
<tr><td>Marketer</td><td>Studio could let clients' own AI tools call the governed tools Copilot calls, under each user's Aladdin permissions.</td><td>Names Studio and the user's own permissions. "Governed" still hints.</td></tr>
<tr><td>Engineer</td><td>Clients' AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions.</td><td>Ties permissions to identity, which is technically exact. Studio is missing.</td></tr>
<tr><td><b>Recommended</b></td><td class='rec'><b>Through Studio, clients' own AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions.</b></td><td>Combines both. Supporting text on page 12 says, explicitly:
<ul>
<li>Which controls apply to every caller: user permissions, compliance on order posts, and the order workflow, in which a portfolio manager authorizes each order.</li>
<li>That Copilot's registry rules would have to be applied at the new connection.</li>
<li>That Copilot's guardrails, planning and tests stay inside Copilot.</li>
<li>That the route (an MCP server or A2A) is your inference.</li>
</ul></td></tr></table>
<p><b>The competitive analyst's warning:</b> this direction is not unique. SimCorp's Launchpad, Bloomberg's MCP release and Arcesium describe the same split between the vendor's server and the client's model. So the edge has to be two things: tools that reach orders and compliance, and about two thousand tools and agents already in production. Name that in the text rather than claim uniqueness.</p></div>
<div class='dec'><h3>Decision 3. Exhibits 3, 4 and 14 as one set (not drawn yet)</h3>
<p><b>One key for all three:</b></p>
<ul>
<li><b>Yellow</b> is Aladdin Studio only.</li>
<li><b>Pink</b> is Aladdin Copilot only. BlackRock's applications are white.</li>
<li><b>Black</b> is Aladdin's shared services and APIs.</li>
<li><b>Grey panels</b> are controls.</li>
<li><b>Hatched boxes with dashed arrows</b> are proposed, your inference.</li>
<li>One legend covers boxes and arrows.</li>
</ul>
<p><b>Exhibit 3, the map.</b> "Built by BlackRock" (applications and Copilot) sits beside "Aladdin Studio, built on by clients", over the shared services. The controls panel attaches to Studio only. Data Cloud and ADX sit inside Studio, with data flowing both ways.</p>
<p><b>Exhibit 4, the zoom.</b> The same yellow Studio box, opened up. The APIs are drawn once, as the shared layer. The tile becomes API access.</p>
<p><b>Exhibit 14, the extension.</b> The same layout as Exhibit 3, organised by where each control is enforced:</p>
<ol>
<li><b>Shared inside Aladdin's services:</b> user permissions, compliance on orders, and the order workflow with portfolio-manager authorization.</li>
<li><b>At each connection:</b> registry rules on Copilot's arrow. Credentials and OAuth scopes on Studio's arrows.</li>
<li><b>Inside Copilot only:</b> guardrails, planning and AI-graded tests, attached to the Copilot box.</li>
</ol>
<p>Two client AI routes:</p>
<ul>
<li><b>Direct through Studio credentials:</b> solid, because it exists today.</li>
<li><b>Through Copilot's tools:</b> dashed, labelled as your inference.</li>
</ul>
<p>Client tiles carry the Exhibit 4 part each one uses.</p>
<p>I will draw these for your approval only after you sign off this review.</p></div>
<div class='dec'><h3>Decision 4. Exhibit 15 (marketing work)</h3>
<p>Your reader would act on rows 1, 4 and 3 now. Row 2 needs a product decision first. The recommendations:</p>
<ul>
<li>Reorder the rows to 1, 4, 3, 2.</li>
<li>Rewrite the demo with compliance on and a portfolio manager authorizing (N5).</li>
<li>Name one client that builds with Studio (fix 26).</li>
<li>Drop the stability labels from the RFP answer (fix 56).</li>
<li>Optional: one line on who owns each row (N6).</li>
<li>Add a pricing and packaging condition on page 12 (N2).</li>
</ul></div>
<div class='dec'><h3>Decision 5. Does your "suggested" rule cover "suggests"?</h3>
<p>All four boxes are headed "What this finding suggests about direction". If the rule covers the verb, the alternative is "What this finding means for direction".</p></div>
<div class='dec'><h3>Decision 6. New competitor evidence not yet confirmed at source</h3>
<p>The competitive analyst read a reprint of Arcesium's May 21, 2026 release, "Arcesium Intelligence". It describes:</p>
<ul>
<li>over 100 agents</li>
<li>a studio for client-built agents</li>
<li>a choice of AI model</li>
<li>a governed orchestration layer with human oversight</li>
<li>an MCP server for any AI tool</li>
</ul>
<p>Arcesium's own page refused automated access ("too many requests") for me too. It is source 76 in your register, titled "Arcesium launches comprehensive AI platform". Please open it in a browser before we rely on these details.</p></div>
""")
parts.append(f"<h2>{T1}</h2><table>{head}" + "".join(row(*r) for r in R if r[0] <= 12) + "</table>")
parts.append("<h2>Tier 2. Plain factual errors</h2><table>" + head + "".join(row(*r) for r in R if 13 <= r[0] <= 21) + "</table>")
parts.append("<h2>Tier 3. Overstatements a knowledgeable reader would catch</h2><table>" + head + "".join(row(*r) for r in R if 22 <= r[0] <= 42) + "</table>")
parts.append("<h2>Tier 4. Precision and optional</h2><table>" + head + "".join(row(*r) for r in R if r[0] >= 43) + "</table>")
parts.append("<h2>New items the panel found (not on my list)</h2><table><tr><th>#</th><th>Where</th><th>Now</th><th>Recommended</th><th>Why</th></tr>" +
             "".join(f"<tr><td class='n'>{a}</td><td class='w'>{html.escape(b)}</td><td class='cur'>{html.escape(c)}</td><td class='rec'>{html.escape(d)}</td><td>{html.escape(e)}</td></tr>" for a,b,c,d,e in NEW) + "</table>")
parts.append("""<h2>What I checked myself to settle disputes</h2><ul>
<li><b>Exhibit 12's count.</b> The 11 are the ten rows plus State Street. Aladdin is a separate comparison row. So "Ten of the 11" was right, and my fix 16 premise was wrong. Eight of the 11 offer outside AI tools a connector or MCP server.</li>
<li><b>Order authorization.</b> The OrderAPI offers only post, batch post, cancel, batch cancel, filter and a status call. Its order status, authorize time and active time fields are all read-only.</li>
<li><b>The Garson exchange (source 71, November 6, 2024).</b> "100%" comes right after Crockett's list of options, which ends with "they want your plug-ins exposed there". "We are hearing that from our clients" comes after his line about clients leveraging "your plug-ins in their custom copilot". The editor's alternative reading was wrong.</li>
<li><b>Arcesium's release.</b> Not reachable (HTTP 429).</li>
<li><b>Counts the engineer re-ran.</b> All match: 17 single-scope specs, 3 mixed, 96 of 301 operations without a read/write split, 25 long-running jobs, and 24 alpha, 6 beta, 23 stable and 1 sunset spec.</li>
</ul></body></html>""")
open('/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/review24/Proposed_v24_changes.html','w',encoding='utf-8').write(''.join(parts))
print(len(R), 'fixes;', len(NEW), 'new items')
