# Agent D: the commercial evidence. Adversarial audit

Report audited: "Aladdin Studio from the outside", v23 (PDF pages 2, 3, 4, 7, 8, 9, 12, 13; source register entries 11, 12, 14, 49 to 69).

All downloads for this audit are in `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/audit/D/`. I fetched every source myself during this task, and I used no project notes, summaries or earlier fact-checks. The one exception is that I tried the saved copies of PR 52 and PR 53 in `drift22/dl_a/` (`pr52.html`, `pr53.html`). Both are 378-byte 403 error pages, so they added no evidence.

## Method and access (what I could and could not reach)

| Source | Access | File |
|---|---|---|
| BlackRock 2025 Investor Day deck (q4cdn) | Downloaded. 147 slides, created June 12, 2025 | `D/ID2025.pdf`, slide 23 rendered as `D/s23-023.png` |
| 2025 Investor Day transcript | **Not found.** The BlackRock newsroom page carries only a partial transcript (Fink and Small), with no mention of API calls, "17x" or marginal cost. The Quartr page is a summary with no mention of API calls. I found no full transcript. | `D/id_news.html` |
| BlackRock 2023 Investor Day deck | Downloaded | `D/ID2023.pdf` |
| BlackRock FY2025 10-K (sec.gov) | Downloaded | `D/blk10k.htm`, `D/blk10k.txt` |
| JPMorgan DEF 14A, filed 2017 to 2026 (10 proxies) | All 10 downloaded from EDGAR. I located them with the data.sec.gov submissions JSON. | `D/jpm/*.htm` and `*.txt` |
| UK Find a Tender notices 062522-2025, 001014-2025, 035311-2023 | The HTML pages return **403** to curl. I read the same notices through the official Find a Tender OCDS API (`/api/1.0/ocdsReleasePackages/<id>`). | `D/proc/*.json` |
| USAspending PBGC awards (both) | Downloaded award records plus the transaction lists (POST /api/v2/transactions/) | `D/proc/CONT_AWD_*.json` |
| Nest press release, Nov 13, 2023 | Downloaded live | `D/proc/nest.html` |
| Janus Henderson FY2025 10-K | Downloaded | `D/jhg10k.htm` |
| Royal London client video | The live page is up and gives the title "CEO". There is no audio in this task, so I used the project's **Whisper machine transcript** (`04-transcripts/part2-cloudfront-and-podcasts/058_...md` and `timestamped/20241113_RLAM-404...ts.txt`). | `D/rlam.html` |
| Aladdin Studio product page | Downloaded live | `D/studio.html` |
| roic.ai earnings transcripts (the report's source 64 and 66 to 69) | **Blocked** by Cloudflare (403) for both curl and WebFetch. **I re-ran the tally independently** on 27 third-party transcripts from Bullfincher (Q1 2020 to Q3 2026). I cross-checked the Q3 2026 call against Earnings Whispers. | `D/calls/bf_*.html` and `.txt` |
| aladdinsdk (git clone) | Cloned fresh. The cited commit 1c1bd25 patch URL on github.com returned 403 (the GitHub web and API are blocked). I read the squash-merged commits 0867c80 and 4677dd7 instead. | `D/sdk/` |
| The TRADE 2016 article (source 54) | **403. Not verified.** | n/a |
| EDGAR full-text search, "Aladdin Studio" | Run through efts.sec.gov | 0 hits |

Web searches used: 3 of 20. I did not re-download the PyPI wheels, because no claim in my area rests on the specifications.

---

## Q1. The 17x forecast (pages 2, 8, 9, 12)

### What slide 23 actually shows (primary, seen directly)
- **Title:** "4. Continuously drive marginal costs down". **Subtitle:** "All of BlackRock is built on a foundation of operating excellence in everything we do and what we do will continue to rapidly grow".
- **Right panel:** "2030 Estimate³", with columns "Metric | Increase by 2030":
  - Rows labelled **"BlackRock"**: Portfolios (#) **2x**, Model Portfolios (#) **4x**
  - Rows labelled **"BlackRock + Aladdin®"**: Trade Allocations (#) **1.3x**, API Calls (#) **17x**
- **Banner:** "Our objective is for the **marginal cost of this growth to be as low as possible** through continued investment in scale enablement".
- **Footnote 3 (slide 25):** "The figures and statements are forward-looking statements. These figures and statements are estimated based on various assumptions, and there is no guarantee that they will be realized as presented."
- **Not stated anywhere:** the base year (the left panel is "Since 2023 Investor Day", but the 2030 panel gives no base), whose API calls are counted (BlackRock internal, Aladdin clients, or Copilot), and how a "call" is defined.
- **"Studio" appears nowhere in the 2025 deck.** I checked all 147 slides.

**What it establishes:** BlackRock estimated that the count of API calls across BlackRock and the Aladdin business will rise about 17-fold by 2030. That is the largest multiple of four operating-scale metrics. The slide presents it as **volume to be absorbed at low marginal cost**. It is not a revenue or growth target, and it is an estimate, not a target. The actual targets in the deck sit elsewhere: for example, slide 42 gives a "Low to mid-teen long-term growth target" for Aladdin.

**The other three measures:** Portfolios (#) 2x (BlackRock only), Model Portfolios (#) 4x (BlackRock only), and Trade Allocations (#) 1.3x (BlackRock + Aladdin). Two of the four are BlackRock-only asset-management counts, so calling all four "usage measures" is loose.

**Related slides that the report does not use, but which are better evidence for its thesis:**
- Slide 33, "Growing Aladdin® as a Platform": "Aladdin seeks to provide the perfect fit for every organization; Expanding partner integrations; Unite our community through the language of Aladdin".
- Slide 35 ($20B+ addressable market, which the report cites for the market size). Its growth drivers include "**Aladdin as a platform**". The TAM components are about $8B + $5B + $8B, consistent with "$20B+".
- The FY2025 10-K (see Q2) says "BlackRock is empowering clients with data and APIs". That is an investor-facing statement about APIs which the report never mentions.

### Claim-by-claim

**1a. p.2:** "BlackRock has told investors that API calls will grow 17x by 2030 [11]."
- **Source:** slide 23, as above.
- **Inferred beyond the source:** "will grow" turns a disclaimed estimate into a statement of fact. It also drops the "BlackRock + Aladdin" scope and the marginal-cost framing.
- **Verdict: OVERSTATED (mildly).**
- **Strongest justified wording:** "At its 2025 Investor Day, BlackRock estimated that API calls across BlackRock and Aladdin would increase 17x by 2030."

**1b. p.8:** "At its 2025 Investor Day, BlackRock forecast four usage measures to 2030. API calls across BlackRock and Aladdin had the fastest forecast growth, 17 times [11]."
- **Source:** slide 23.
- **Assessment:** "Forecast" is acceptable, since the slide says "2030 Estimate". "Fastest" is arithmetically true (17 > 4 > 2 > 1.3). However, ranking multiples across unlike metrics (counts of portfolios against machine-generated call volumes) has little meaning, and the slide does not rank them.
- **Verdict: CORRECT on the facts**, but the framing is DEFENSIBLE BUT UNCERTAIN.

**1c. p.8:** "BlackRock tells investors that API calls will grow fastest, without naming the product behind them."
- **Assessment:** The first half matches 1a. The second half is true: the deck names no product. However, the 10-K does tell investors that BlackRock is "empowering clients with data and APIs".
- **Verdict: DEFENSIBLE.**

**1d. p.8:** "**I attribute those API calls to Studio, because the Studio page describes API use [14].**"
- **Source:** The live Studio page does say "Aladdin Studio APIs enable you to build your own solutions… Retrieve, write, and modify data from across the Aladdin ecosystem". So Studio is indeed the client-facing brand for the APIs. But slide 23 scopes the metric to "BlackRock + Aladdin". The report itself says that BlackRock's own ~100 applications and Copilot's roughly two thousand tools call production Aladdin APIs (pp. 3, 4, 9, 12). Copilot is "available to all Aladdin clients" (Exhibit 1), and its calls go through Copilot, not through a client's Studio code.
- **What it establishes:** Some unknown share of the counted calls could come from clients through Studio.
- **Inferred beyond the source:** That the calls are Studio's. This is a syllogism ("Studio describes APIs, therefore API calls are Studio") that ignores the slide's own scope label and the report's own evidence of heavy internal API consumption. The report concedes on the same page that BlackRock speaks "without naming the product behind them".
- **Verdict: UNSUPPORTED** as an attribution. It is reasonable only as a labelled hypothesis about a share of the calls.
- **Strongest justified wording:** "The slide does not say who makes these calls. BlackRock's own applications and Copilot use the same APIs, so the forecast covers internal use as well as clients' use through Studio. How much of the growth would come through Studio is not public."

**1e. p.8 heading:** "BlackRock's growth story to investors runs through Studio". **p.9 box:** "BlackRock's two growth bets both run through Studio. It projects API calls across BlackRock and Aladdin to grow 17x by 2030. That is the fastest of the four forecasts it showed investors."
- **Source:** Slide 23 is a **cost/scale** slide. Its stated objective is a low marginal cost for this volume. The 10-K (Q2) does not list API calls among its fee terms, and the report states this itself on p.8. That undercuts treating API-call growth as a revenue "growth bet".
- **Inferred beyond the source:** That the 17x is a growth bet, and that it runs through Studio.
- **Verdict: OVERSTATED.**
- **Strongest justified wording:** "BlackRock expects API traffic across BlackRock and Aladdin to rise about 17x by 2030 and aims to absorb it at low marginal cost. It lists 'Aladdin as a platform' among Aladdin's growth drivers (slide 35) and tells investors it is 'empowering clients with data and APIs' (10-K). It does not name Studio in either place."

**1f. p.12:** "BlackRock sizes Aladdin's addressable market at more than $20 billion [11]. It projects API calls to grow 17x by 2030 [11]. My inference is that clients' AI tools, acting through Studio, could become a large source of those calls."
- **Source:** Slide 35 reads "$20B+ addressable market". That is CORRECT.
- **Assessment:** The inference is labelled as such and uses "could".
- **Verdict: DEFENSIBLE BUT UNCERTAIN.** This is a reasonable hypothesis, not a factual error. Placing the $20B TAM next to the 17x invites the reader to link API calls to revenue, which neither slide does.

---

## Q2. The FY2025 10-K (pages 3, 4, 8, 12)

**2a. p.3:** "BlackRock's technology services and subscription revenue was $2.0 billion in 2025 [12]. Its 24 percent rise includes Preqin, the private-markets data firm BlackRock bought in 2025."
- **10-K, Item 1:** "Technology services and subscription revenue of $2.0 billion was up 24% year-over-year."
- **Income statement:** $1,981M (2025) against $1,603M (2024). Re-derived: 1,981/1,603 − 1 = **23.6%**, which rounds to 24%.
- **MD&A:** "increased $378 million … reflecting the sustained demand for Aladdin technology offerings and **approximately $210 million of revenue related to the Preqin Transaction**." Excluding Preqin, growth is (378 − 210)/1,603 = **about 10.5%**. ACV grew "31% … including … Preqin, and … 16% excluding".
- **Preqin:** "On March 3, 2025, BlackRock completed the acquisition of 100% of the shares of Preqin".
- **Verdict: CORRECT.** The report could add the organic figure (about 10 percent revenue, 16 percent ACV), which matters if a reader takes 24% as organic. p.12 calls it "technology services revenue", dropping "and subscription". That is trivial.

**2b. p.8:** "BlackRock's 10-K says technology services fees are generally set by the value of positions on the platform or at a fixed rate. Fees can also depend on subscriptions, client launches (go-lives) and support. The 10-K does not list API calls among its fee terms [12]."
- **10-K, Note 2:** "Fees earned for technology services are primarily recorded as services are performed over time and are generally determined using the value of positions on the Aladdin platform, or on a fixed-rate basis. Revenue derived from the sale of software licenses is recognized upon the granting of access rights."
- **10-K, Item 1:** "Revenue for these services may be based on several criteria including value of positions, number of subscriptions, implementation go-lives and software solution delivery and support."
- **API calls:** The only place "API" appears in the whole 10-K is "BlackRock is empowering clients with data and APIs, as well as creating connectivity with ecosystem providers…". There is no fee term based on usage, consumption or calls.
- **Verdict: CORRECT.** Minor omissions: the software-licence basis, and the fact that "subscriptions" is "number of subscriptions". The absence of API calls from the fee terms does not prove that API volume never affects price. The PPF award notice, for example, mentions "variable volume related fees" tied to AUM, users and asset types. The report does not claim that it does.

**2c. p.4, Exhibit 3, hosting row "Microsoft Azure | Amazon Web Services" [12]**
- **10-K, risk factors:** "the Aladdin infrastructure and environment for BlackRock and its external Aladdin clients are hosted on Microsoft Azure and Amazon Web Services."
- **Verdict: CORRECT.**

**2d. p.8:** "HPS … BlackRock bought in July 2025 [12]"
- **10-K:** "On July 1, 2025, BlackRock completed the acquisition of 100% of the business and assets of HPS".
- **Verdict: CORRECT.**

**2e. Omission relevant to Finding 2.** The 10-K's statement "BlackRock is empowering clients with data and APIs … This connectivity helps clients work in their Aladdin environments with a more customized and seamless end-to-end experience" is the strongest investor-facing support for an API/platform story. The report does not use it. Exhibit 10 says "the only investor-facing mention" of Studio is a 2023 slide. That claim is about the word "Studio", so it is still accurate. But the 10-K sentence would strengthen the finding more honestly than slide 23 does.

---

## Q3. JPMorgan proxy disclosures (Exhibit 8, page 7)

### Re-derived from the 10 proxies (each says "paid … in [year]")

| Proxy filed | Year paid | Exact wording | $M |
|---|---|---|---|
| 2017-04-05 | 2016 | "integrated with BlackRock's Aladdin® platform to provide a more seamless experience to our clients, and paid BlackRock approximately $1.5 million in 2016 for **integration services**" | 1.5 |
| 2018-04-05 | 2017 | "paid Blackrock approximately $4.4 million in 2017 **to access** its Aladdin® platform" | 4.4 |
| 2019-04-05 | 2018 | same wording | 5.0 |
| 2020-04-06 | 2019 | same wording | 5.3 |
| 2021-04-07 | 2020 | same wording | 6.8 |
| 2022-04-04 | 2021 | same wording | 4.6 |
| 2023-04-04 | 2022 | same wording | 7.6 |
| 2024-04-08 | 2023 | "**to access and utilize** its Aladdin® platform" | 6.9 |
| 2025-04-07 | 2024 | "to access and utilize" | 14.7 |
| 2026-04-06 | 2025 | "JPMorganChase paid BlackRock approximately $25.6 million in 2025 to access and utilize its Aladdin® platform." | 25.6 |

- The chart's bar heights in the HTML (height ÷ 5.2) and its aria-label match all ten values exactly.
- "$4.4 million to $7.6 million a year from 2017 to 2023" is CORRECT (minimum 4.4 in 2017, maximum 7.6 in 2022).
- "Under $8 million a year" is CORRECT.
- "$14.7 million in 2024 and $25.6 million in 2025" is CORRECT.
- Re-derived growth: +113% in 2024 and +74% in 2025.

**Why it is disclosed:** Each proxy's section "Transactions with directors, executive officers and 5% shareholders" names "BlackRock, Inc. and affiliated entities … beneficial owners of more than 5% of our outstanding common stock". These are therefore related-person disclosures, made because **BlackRock is a >5% shareholder of JPMorgan**. They are not a statement by JPMorgan about Aladdin. The same paragraph discloses BlackRock's management of JPMorgan's pension plans (for example $5.7M in 2025).

**What the payments are for:** Only "to access [and utilize] its Aladdin® platform". No product, module or business line is named. Two details the report does not mention:
1. The wording changed from "to access" to "to access and utilize" with the 2023 payments.
2. A separate line, present through the 2024 proxy, covered "information services and … consulting services from BlackRock, including … market data, analytics and modeling" ($0.33M to $6.5M a year). It **disappears from the 2025 and 2026 proxies**, exactly when the Aladdin figure jumps. Part of the jump could therefore be consolidation of what was previously reported separately. The magnitude cannot explain all of it (2023 information services were $0.33M), but the comparison across 2023 and 2024 is not strictly like for like.

**3a. p.7:** "JPMorgan Chase's proxy statements report Aladdin payments of $4.4 million to $7.6 million a year from 2017 to 2023, then $14.7 million in 2024 and $25.6 million in 2025."
- **Verdict: CORRECT.**

**3b. p.7:** Exhibit 8 used as "Proof that clients use Aladdin … what clients say and file".
- **Establishes:** JPMorgan pays BlackRock for Aladdin access, and its spend rose sharply in 2024 and 2025.
- **Does not establish:** That JPMorgan is an Aladdin *client* in the asset-manager sense, or what drove the increase (price, scope, new business lines, or reporting consolidation). The 2016 integration language ("to provide a more seamless experience to our clients") points to JPMorgan as an **asset servicer connecting to Aladdin**. The report's own Exhibit 1 notes that Aladdin Provider is paid for by "custodians and administrators". The report's caption hedges this ("JPMorgan is also a custodian, so the payments may cover more than a client license"). That hedge is appropriate, but it sits in small print while the heading claims client proof.
- **Verdict: DEFENSIBLE BUT UNCERTAIN** as evidence of adoption. CORRECT as evidence of growing JPMorgan spend. It says **nothing about Studio**, and the report does not claim it does.
- **Strongest justified wording:** "JPMorgan, in which BlackRock holds more than 5 percent, discloses paying BlackRock for access to Aladdin. The amount rose from under $8 million a year (2017 to 2023) to $25.6 million in 2025. The proxies do not say which Aladdin services are covered. JPMorgan is also a custodian that connects to Aladdin."
- **Not verified:** The TRADE 2016 article (source 54) returned 403.

---

## Q4. Procurement records and client examples (Exhibit 9, pages 7 and 8)

**4a. UK Pension Protection Fund.** Report: "BlackRock won both parts of the tender, at up to £74.0 million, against the fund's estimate of up to £55 million [58, 59]". Caption: "The PPF notice gives BlackRock's Aladdin web page as the supplier's address".
- **OCDS 062522-2025** (award, dated 2025-10-06, contracts signed 2025-07-29):
  - Both lot awards go to "BlackRock Financial Management, Inc", whose supplier URL is "http://www.blackrock.com/aladdin".
  - "the total estimated contract value across Lots 1 and 2 over the full ten-year term is projected to range between £48,766,000 and £74,025,496. This range reflects both fixed and variable fees, which are influenced by the total assets under management".
  - Bids received: Lot 1, **2**; Lot 2, **4**.
- **001014-2025** (tender, 2025-01-13): "estimated contract value … range between £43m and £55m across Lots 1 and 2 over the maximum contract term of 10 years."
- **Scope:** Lot 1 is an order management system plus portfolio monitoring and risk (LDI). Lot 2 is portfolio monitoring and risk for private markets.
- **Establishes:** Adoption of a BlackRock OMS and risk system. Given the supplier URL, this is very likely Aladdin, but the notice text never says "Aladdin" or any product name, and **nothing about Studio**.
- **Verdict: CORRECT.**
- **Minor issues:**
  - "Address" is really the supplier URL field.
  - The award range (£48.8m to £74.0m) and the estimate range (£43m to £55m) are both 10-year, both-lot figures, so the comparison is like for like. Saying "over up to ten years" would make that clear.
  - The source register's title for 58 ("investment risk and analytics platform") does not match the notice title ("Order management, portfolio monitoring and risk analytics system").

**4b. Nest.** Report: "Nest chose BlackRock's Aladdin over six other bids [60, 61]".
- **OCDS 035311-2023:** "Provision of Investment Risk Platform Services", 5 years, supplier BlackRock Financial Management Inc, **bids: 7**, contract value £1,750,000.
- **Nest release, Nov 13, 2023:** "Nest will use BlackRock Aladdin to manage the risk of its entire investment strategy"; "The Whole Portfolio View and Aladdin Climate components"; "Aladdin's Investment Risk and Aladdin Climate platforms".
- **Establishes:** Adoption of named Aladdin products (Investment Risk, Whole Portfolio View, Climate). **Not Studio.**
- **Verdict: CORRECT.**

**4c. PBGC.** Report: "BlackRock won an investment risk system contract both times, at about the same yearly price [62, 63]".
- **USAspending:**
  - 16PBGC17C5002 "INVESTMENT RISK MANAGEMENT SYSTEM (IRMS)", signed 2017-09-28, Sep 2017 to Mar 2023, $7,628,372 obligated, full and open competition, 4 offers, firm fixed price.
  - 16PBGC23C0006, signed 2023-03-27, base Mar 2023 to Mar 2027 (potential end 2033), $5,550,000 obligated, 4 offers.
- **Transaction lists:** Both contracts' base awards are **$1,389,350.64**, and option years are **$1,387,500.00** each in both contracts. "About the same yearly price" is therefore an understatement: the price is effectively identical.
- **Establishes:** That BlackRock Financial Management won a PBGC risk-system contract twice. **The records never name Aladdin**, let alone Studio. The report's own row text says "investment risk system", which is accurate. The surrounding framing ("Proof that clients use Aladdin") makes the Aladdin link an inference, a very plausible one.
- **Verdict: CORRECT** as worded. The Aladdin attribution is an inference, not on the record.

**4d. Royal London.** Report: "Hans Georgeson praises the Snowflake implementation in Royal London's Aladdin program [50]. He was then chief executive".
- **Whisper machine transcript at 5:21:** "the implementation of Snowflake that we did as part of the overall programme has been really successful for us". The live page reads "Hans Georgeson, CEO, Royal London Asset Management".
- **Assessment:** "Aladdin Data Cloud" is never said. "As part of the overall programme" is ambiguous between Aladdin Data Cloud and Royal London's own Snowflake estate.
- **Verdict: CORRECT** as worded. It rests on a machine transcript. If anyone reads it as "Royal London uses Aladdin Data Cloud (Studio)", that would be UNSUPPORTED.

**4e. Janus Henderson.** Report: "in the third quarter of 2025 the firm chose to move its investment management system to Aladdin, 'a complex, multi-year initiative' [53]".
- **JHG 10-K:** "we are engaged in a project to implement BlackRock's Aladdin platform, a complex, multi-year initiative to upgrade our Investment Management, Compliance, and Middle- and Back-Office services platform"; "the strategic decision in the third quarter of 2025 to transition our investment management platform to Aladdin".
- **Verdict: CORRECT.**

**4f. SDK contributions.** Report: "In December 2025 an engineer at a client firm submitted two changes to the open-source SDK [55]."
- **Git evidence (fresh clone):** squash commits 0867c80 "[FEATURE] URL rewriting (#52)" (2025-12-09) and 4677dd7 "[FEATURE] Additional HTTP headers (#53)" (2025-12-08). The author is Willem du Preez, with every sign-off reading "Signed-off-by: Willem du Preez <Willem.DuPreez@**janushenderson.com**>".
- **Establishes:** That the client is Janus Henderson (a self-declared DCO email, consistent with the JHG 10-K). This is the **only item in Finding 1 that touches a Studio component** (the SDK).
- **Not verifiable:** That a specific BlackRock engineer merged the PRs. The PR pages are blocked, and the git committer is "GitHub".
- **Verdict: CORRECT.**

### Does the report imply Studio-specific adoption where only Aladdin adoption is shown?

The report is mostly careful. p.7: "BlackRock's Studio page names no client building on Studio … Proof that clients use Aladdin, though, is public." p.8: "None of this proof names Studio." Where it overreaches:

- **p.8:** "It still backs a Studio pitch, because Studio is sold for building custom applications on Aladdin, and **a buyer wants to know that another institution built on the platform and stayed**." The PPF, Nest, PBGC and JPMorgan records show institutions **buying or using** Aladdin modules (OMS, risk, climate, access). They do not show institutions **building on** it. Only Janus Henderson's SDK patches show building, and Janus Henderson has not "stayed": it decided to move in Q3 2025. **OVERSTATED.**
- **p.8:** "Some clients are easier to name in public: public pension funds … They are the natural first subjects for a Studio case study that names the client." **p.13, Exhibit 15 row 3:** "One client story, cleared for the Studio page …: a public pension fund already on record". Nothing shows that PPF, Nest or PBGC use Studio. Nest bought Investment Risk, Whole Portfolio View and Climate, and PBGC bought a risk system. A Studio case study needs a Studio user. As a suggestion this is a reasonable hypothesis, but it should be conditional. **DEFENSIBLE BUT UNCERTAIN.**
- **Exhibit 9 title:** "BlackRock won the tenders of three public pension bodies" is accurate. The PBGC records do not name Aladdin.

---

## Q5. Exhibit 10: "Studio" on 26 earnings calls

- **Count:** Q1 2020 to Q2 2026 is 6.5 years × 4 = **26 calls**. CORRECT.
- **Independent replication:** roic.ai is blocked, so I ran the tally on **Bullfincher's** third-party transcripts for all 27 calls from Q1 2020 to Q3 2026 (each 45k to 77k characters, each running from the General Counsel's opening to the operator's close).

| Term | Report (26 calls) | My count (26 calls) | Q3 2026 (Oct 14) |
|---|---|---|---|
| Studio | 0 | **0** | 0 |
| Data Cloud | 2 (Q3 2022, Q4 2024) | **2, same calls** | 0 |
| API(s) | 1 (Q4 2021) | **1, same call**: "clients are really looking to use both data and APIs" | 0 |
| Copilot | 1 (Q4 2023) | **1, same call**: "Investments in Aladdin AI copilots, enhancements and openness" | 0 |
| Citizen developer | 0 | 0 | 0 |
| AI agent / agentic | 0 | 0 (the only "agent" hit, Q4 2023, is "an agent for … change") | 0 |

- **Q3 2026** (Oct 14, 2026, checked on both Bullfincher and Earnings Whispers): "Aladdin" appears 7 times, "Studio" 0 times, "API" 0 times. Its Aladdin content: "AI is amplifying the value of Aladdin as we accelerate innovation", ACV +12%, "Aladdin underpins everything we deliver to clients", and "Aladdin's role as an operating system for entire portfolio". **It does not change the finding**: the count becomes 0 of 27. The report is dated "As of October 19, 2026", five days after this call, so its window is one quarter stale. That should be acknowledged ("Q1 2020 to Q3 2026, 27 calls").
- **Data Cloud wording:** The report says Data Cloud was "described as an add-on sold with Aladdin Enterprise". Both calls actually say "clients leveraging Enterprise Aladdin alongside Aladdin Accounting or the Aladdin Data Cloud". "Add-on" is a paraphrase that the calls do not use. **DEFENSIBLE.** More exact: "cited among products clients use alongside Enterprise Aladdin".
- **"The only investor-facing mention found is one line on a 2023 Investor Day slide [65]":** Verified. 2023 deck slide 31 lists "Aladdin Studio" as one product tile among eight. There is no Studio mention in the 2025 deck or the FY2025 10-K. EDGAR full-text search for "Aladdin Studio" returns **0 hits**, which also verifies source 49.
- **Method caveat:** Both my source and the report's are third-party transcripts. Spelling variants ("Prequin" for Preqin appears in Earnings Whispers) show that transcription errors exist, but a transcription error is unlikely to hide "Studio" on every call. **Verdict: CORRECT.**

---

## Separation: factual mistakes vs hypotheses

**Genuine factual or reading errors (the facts are right, the reading is wrong):**
1. Treating slide 23's 17x as a "growth bet" or "growth story". The slide's own heading and banner frame it as marginal-cost and scale management.
2. Attributing the 17x API calls to Studio when the slide scopes them to "BlackRock + Aladdin" and the report itself documents heavy internal and Copilot API use.
3. "Will grow" (p.2) for a disclaimed estimate.
4. "Another institution built on the platform and stayed" as a description of what the procurement and proxy evidence shows.
5. Minor issues: the stale call window (Q3 2026 omitted), the "add-on" paraphrase, the mismatched register title for the PPF award notice, and "address" for a URL field.

**Every number checked is right:** $2.0B and +24% (with Preqin, about $210M), the fee basis, Azure/AWS hosting, all ten JPMorgan figures, the PPF £74.0M and £55M, the Nest bid count, PBGC's identical yearly price, the Janus Henderson quote, and the earnings-call tallies.

**Reasonable hypotheses on incomplete information:** that clients' AI tools could become a large source of API calls (p.12, labelled as an inference); that public pension clients would make good case-study subjects (if they use Studio); and that JPMorgan's rising payments reflect deeper Aladdin use (they are hedged, but the custodian/Provider reading is at least as likely).

---

## Top vulnerable statements

**1. p.8:** "I attribute those API calls to Studio, because the Studio page describes API use [14]."
- **Source:** Slide 23 labels the 17x row "BlackRock + Aladdin®". The Studio page says "Aladdin Studio APIs enable you to build your own solutions".
- **Establishes:** Studio markets APIs to clients, and API calls across BlackRock and Aladdin are estimated to rise 17x.
- **Inferred beyond the source:** That the counted calls are Studio calls. The slide includes BlackRock's own use, and by the report's own account the ~100 internal apps and Copilot's roughly two thousand tools call the same production APIs.
- **Verdict: UNSUPPORTED.**
- **Strongest wording:** "The slide does not say who makes these calls. They include BlackRock's own use, so the share that would come from clients through Studio is not public."

**2. p.8 heading and p.9 box:** "BlackRock's growth story to investors runs through Studio" / "BlackRock's two growth bets both run through Studio. It projects API calls … to grow 17x by 2030. That is the fastest of the four forecasts".
- **Source:** Slide 23 title "Continuously drive marginal costs down"; banner "Our objective is for the marginal cost of this growth to be as low as possible"; footnote 3 says the figures are estimates with no guarantee. The 10-K lists no API-based fee.
- **Establishes:** A scale estimate that BlackRock wants to absorb cheaply.
- **Inferred beyond the source:** A revenue growth bet tied to Studio.
- **Verdict: OVERSTATED.**
- **Strongest wording:** "BlackRock expects API traffic across BlackRock and Aladdin to rise about 17x by 2030 and plans to absorb it at low marginal cost. It lists 'Aladdin as a platform' as a growth driver (slide 35) and tells investors it is 'empowering clients with data and APIs' (10-K), without naming Studio."

**3. p.8:** "It still backs a Studio pitch, because Studio is sold for building custom applications on Aladdin, and a buyer wants to know that another institution built on the platform and stayed." With p.8 and p.13: public pension funds are "the natural first subjects for a Studio case study".
- **Source:** PPF (OMS and risk, 2 and 4 bids), Nest (Investment Risk, Whole Portfolio View, Climate, 7 bids), PBGC (a "risk management system" with no product named), and JPMorgan ("to access and utilize its Aladdin platform").
- **Establishes:** That these institutions buy or use Aladdin modules.
- **Inferred beyond the source:** That they built on the platform, and that they use Studio. Only Janus Henderson's SDK patches show building, and Janus Henderson is a new migrator, not a long-standing client.
- **Verdict: OVERSTATED.**
- **Strongest wording:** "These records show institutions buying and staying on Aladdin. None shows Studio use. A named Studio case study would first need a client that builds with it, such as the firm whose engineer contributed to the SDK."

**4. p.7, Exhibit 8:** JPMorgan's "payments for Aladdin rose from under $8 million a year to $25.6 million in 2025", offered as client proof.
- **Source:** DEF 14A related-person disclosures (BlackRock is a >5% holder): "to access [and utilize] its Aladdin® platform". The figures are exact. The separate information-services line disappears from the 2025 proxy onward, and the 2016 entry is integration "to provide a more seamless experience to our clients".
- **Establishes:** Rising JPMorgan spend on Aladdin access.
- **Inferred beyond the source:** Client adoption, or growth in use. It could equally be custodian connectivity (Aladdin Provider), pricing, or consolidated reporting.
- **Verdict:** DEFENSIBLE BUT UNCERTAIN (the numbers are CORRECT).
- **Strongest wording:** "JPMorgan, in which BlackRock holds more than 5 percent, discloses paying BlackRock for access to Aladdin: under $8 million a year in 2017 to 2023, then $14.7 million in 2024 and $25.6 million in 2025. The proxies do not say what the payments cover. JPMorgan is also a custodian that connects to Aladdin."

**5. p.2:** "BlackRock has told investors that API calls will grow 17x by 2030." With p.12: "It projects API calls to grow 17x by 2030. My inference is that clients' AI tools, acting through Studio, could become a large source of those calls."
- **Source:** Slide 23: "2030 Estimate", "Increase by 2030", row "BlackRock + Aladdin® | API Calls (#) | 17x", and "no guarantee that they will be realized".
- **Establishes:** A disclaimed estimate with no base year and no attribution of who makes the calls.
- **Inferred beyond the source:** Certainty ("will grow"). Placing it next to the $20B TAM also implies a revenue link that neither slide makes.
- **Verdict:** p.2 is OVERSTATED (mildly). The p.12 inference is DEFENSIBLE BUT UNCERTAIN.
- **Strongest wording:** "At its 2025 Investor Day, BlackRock estimated that API calls across BlackRock and Aladdin would increase 17x by 2030. I infer that clients' own AI tools could account for a growing share."
