---
title: "Aladdin and Aladdin Studio: Briefing and Interview Guide"
subtitle: "Revised edition, incorporating the fact-check of October 2026"
---

**Prepared for:** Jacob Nikolau

**Role:** Senior Product Marketing Manager, Technical Product Marketing (Vice President), Aladdin Studio, New York

**As of:** October 8, 2026 (text); revised October 19, 2026 after a fact-check against BlackRock's public API specifications, product pages, press releases, job postings and about 120 transcripts of its talks and podcasts

*Independent interview preparation compiled from public sources and the candidate's own notes. It was not produced, reviewed or endorsed by BlackRock.*

**How to read the evidence labels.** Tables that list individual facts carry a Label column with one of four labels. Descriptive tables, such as the jobs Aladdin does inside a client firm, rely on the sources named beneath them.

| Label | Meaning |
|--------------------------------------|--------------------------------------------------------------|
| Confirmed | Taken from a primary document, such as a filing, contract notice or official page |
| Reported | Taken from press coverage, a job board or a secondary summary of a document |
| Estimate | A calculation from stated inputs |
| Unconfirmed | Found in research files but not yet checked against the primary document |

# Contents

| Section | Page in original |
|-------------------------------------------------------------------|---------------------------------|
| Summary | 3 |
| **Part 1. The Business** | 5 |
| 1. What Aladdin is | 6 |
| 2. What Aladdin is used for | 10 |
| 3. Who the customers are | 11 |
| 4. What Aladdin costs | 17 |
| 5. What Aladdin replaces and what it complements | 21 |
| 6. Competitors | 25 |
| 7. Aladdin Studio in depth | 31 |
| 8. Studio's developer marketing and adoption | 37 |
| **Part 2. Third Round: Product Manager Interviews** | 43 |
| 9. How the third round works | 44 |
| 10. Technical depth | 45 |
| 11. Knowledge of the customers | 47 |
| 12. Fit with a large, regulated company | 50 |
| 13. Working with product managers | 54 |
| **Part 3. Final Round: Managing Director** | 58 |
| 14. How the final round works | 59 |
| 15. Motivation and fit | 61 |
| 16. Understanding of the business and strategy | 62 |
| 17. Operating at the VP level | 65 |
| 18. Closing the final round | 67 |
| **Appendices** | 69 |
| Appendix A. Evidence notes and caveats | 70 |
| Appendix B. Key sources | 71 |
| Verification notes for this revision | new |

# Summary

Aladdin Studio is the part of BlackRock's Aladdin platform that lets clients build their own tools on Aladdin's data, and this role owns how it is explained and sold. Aladdin is a $2 billion a year software business growing in the low to mid teens. Most of that growth comes from selling more into accounts BlackRock already has. Studio is meant to drive that growth, but its outside adoption is still hard to see in public.

| $1.98B | 15% | 0 of 26 | 4 of 16 |
|-------------------------|-------------------------|-------------------------|-------------------------|
| Aladdin technology revenue in 2025, up 24% with Preqin | Annual contract value growth, excluding Preqin, Q2 2026 | Earnings calls that named "Studio," 2020 to mid-2026 | Studio's score on a developer access test |

Source: Exhibit 1.

**Exhibit 1. The numbers that matter most**

| Measure | Value | As of | Label |
|---------------------------------|---------------------------------|---------------|--------------------|
| Aladdin technology revenue | $1.98 billion, up 24% with Preqin | 2025 | Confirmed |
| Annual contract value (ACV) growth, excluding Preqin | 15% | Q2 2026 | Confirmed |
| Share of technology revenue that recurs | 98% | 2024 | Confirmed |
| Average client retention | 97% | 2022 to 2024 | Confirmed |
| Fixed minimum fees on current contracts | About $1.3 billion a year | FY2025 10-K | Confirmed |
| Assets managed on the platform | About $25 trillion | December 2025 | Confirmed |
| JPMorgan Chase's yearly payments for Aladdin | $4.4 million (2017) to $25.6 million (2025) | Proxy statements | Confirmed |
| Earnings calls that named "Studio," 2020 to mid-2026 | 0 of 26 | Q2 2026 | Confirmed |
| Outside firms shown in public building on Studio | 1 (Janus Henderson, through SDK code) | December 2025 | Confirmed |
| Studio's score on a developer access test | 4 of 16 (Snowflake and Databricks scored 16) | October 2026 | Estimate |

## The business in five points

1. **Aladdin runs the whole investment process on one shared record.** Large asset managers, insurers, pension funds, banks and wealth firms use it for portfolios, trading, risk, compliance, operations and accounting. Clients rarely swap one product for another. They retire a group of systems at once.
2. **Aladdin is priced on assets and seats plus a fixed base, and accounts grow over time.** Public prices run from about $0.5 million a year for risk tools to more than $20 million for the largest accounts. JPMorgan's payments rose almost sixfold from 2017 to 2025. Buyers weight technical fit far above price.
3. **Few vendors compete with the whole platform.** SimCorp and State Street Alpha are the usual shortlist. Every insurer decision found since July 2025 went at least partly to Clearwater: Versicherungskammer, BarmeniaGothaer, MSIG Europe, NFU Mutual and PREPAR-VIE. Rivals now promise clients they can keep their own tools connected by API, which is Studio's pitch.
4. **Studio's main competitor is the client's own data team.** A large firm can build its own setup on Snowflake or Databricks. Meanwhile, seven data and platform firms, including FactSet, LSEG and MSCI, now let outside AI tools pull their data directly. BlackRock does not yet offer this for Aladdin.
5. **Studio's product is ahead of its marketing.** The engineering is real. But the documentation sits behind a client login, the open-source SDK is still in beta, and BlackRock has not named a client as building on Studio's APIs or SDK. The nearest thing is Royal London's chief executive crediting the Snowflake implementation in its Aladdin programme, in a BlackRock client video. BlackRock is hiring a full developer team to close these gaps, including this role.

## Where the interview process stands

| Stage | Status | What it covers |
|--------------------|-----------------------------|---------------------------------------------------|
| Rounds 1 and 2 | Complete | Recruiter pre-screen in September, then interviews including Priyanka Singh and Vijay Kasi. His own read: his launch stories were too general. |
| Round 3 | Next | Three 30-minute interviews with Studio product managers, each on how he would work with them |
| Final round | If round 3 goes well | The Managing Director decides whether he can own how Studio is explained and sold |

## What to carry into every conversation

1. **Explain Studio accurately.** It has APIs that read and write data, Data Cloud on Snowflake, a Python SDK and notebooks, and Excel tools. Governance covers all of it. Copilot calls the same APIs as plugins.
2. **Say only what is live.** Label anything on the roadmap with a quarter. Offer to check framing with the PM before using it outside the company.
3. **Name the product, the audience, the decision and the number in every story.** That was the gap in the second round.
4. **Spread the stories across conversations.** The NovoEd AI translation launch is the strongest single story. It covers launch sizing, honest claims, sales alignment and disagreement, and it produced more than $1 million in expansion from CEMEX and Marriott. Lead with other stories where they fit, because the PMs may compare notes.
5. **Frame Studio as account growth and retention.** Studio is sold inside the core contract. Each point of retention on a $2 billion business is worth about $20 million a year.

In every round, he needs to show that he learns technical platforms accurately, keeps claims honest about what is live, and backs every answer with one named story and one number.

# Part 1. The Business

1. What Aladdin is
2. What Aladdin is used for
3. Who the customers are
4. What Aladdin costs
5. What Aladdin replaces and what it complements
6. Competitors
7. Aladdin Studio in depth
8. Studio's developer marketing and adoption

# 1. What Aladdin is

Aladdin is BlackRock's investment operating system: cloud software that large money managers rent so they can run their whole investment business on one shared set of data. BlackRock built it for itself in 1988, began selling it to other firms around 2000, and now earns about $2 billion a year from it.

## The problem it solves

A large investment firm usually runs many separate systems. One builds portfolios, one sends trades, one checks rules, and others handle settlement, accounting and reporting. Each keeps its own copy of the firm's holdings, so the numbers drift apart. Staff then spend hours fixing the gaps.

Aladdin replaces that patchwork with one platform. Every team works from the same record of what the firm owns. BlackRock calls this a "common data language." The industry name for that official, current record of holdings is the investment book of record, or IBOR. Aladdin has been BlackRock's own IBOR since 1990. BlackRock's 10-K notes that most positions on the platform are bonds.

## Where it came from

The name stands for Asset, Liability, Debt and Derivative Investment Network. It started as a risk tool on a single workstation. BlackRock's early business was bonds and mortgage securities, which are hard to value, so it built its own tools to understand their risk. Outside demand came early. In 2000 BlackRock formed BlackRock Solutions to sell Aladdin and risk advice to other firms. Its 2008 work for the New York Fed on Bear Stearns assets made Aladdin a byword for risk management.

**Exhibit 2. Aladdin grew from a bond risk tool into a public and private markets platform**

| Date | Milestone | Label |
|-----------------|-----------------------------------------|-----------------------------------------|
| 2026 (expected) | Aladdin on AWS for new US-hosted Enterprise clients. No launch announced as of October 8. | Confirmed (target) |
| Dec 2025 | Announced Aladdin on Amazon Web Services, with Amazon Treasury as the first user | Confirmed |
| Mar 2025 | Closed the £2.55 billion purchase of Preqin, a private markets data company | Confirmed |
| 2024 | Launched Aladdin Copilot; open-sourced the Aladdin SDK on GitHub | Confirmed |
| 2023 | Launched eFront Copilot | Confirmed |
| Feb 2021 | Launched Aladdin Data Cloud on Snowflake as part of Studio | Confirmed |
| 2020 | Launched Aladdin Studio; began moving to Microsoft Azure; launched Aladdin Climate | Reported (Studio), Confirmed (others) |
| 2019 | Bought eFront, a Paris private markets software firm, for $1.3 billion | Confirmed |
| 2008 | Managed about $30 billion of Bear Stearns assets for the New York Fed | Confirmed |
| 2000 | Formed BlackRock Solutions to sell Aladdin to other firms | Confirmed |
| 1998 | Licensed the analytics to Freddie Mac to value over $500 billion of mortgages | Reported |
| 1988 | Built as a risk tool in BlackRock's first year | Confirmed |

Source: BlackRock annual reports and press releases; AWS joint release, December 2025.

## The product family

BlackRock markets the umbrella as "BlackRock Aladdin," covering the Aladdin platform, eFront, Aladdin Wealth and Preqin. It works as one core engine with separate entry points for each kind of buyer.

**Exhibit 3. One core engine with separate entry points for each kind of buyer**

| Product | What it does | Main users |
|--------------------|----------------------------------------|----------------------------------------|
| Aladdin Enterprise | The full front-to-back system for public markets. It is the same system BlackRock runs internally. | Asset managers, insurers, pension funds, banks |
| Aladdin Wealth | Portfolio risk analysis and proposals for advisors. Its AI "auto commentary" tool launched in October 2025, with Morgan Stanley first. | Wealth managers and private banks |
| eFront | Covers a private fund investment from due diligence through cash flows and reporting | Investors in funds and fund managers |
| Preqin | Private markets data. At the March 2025 closing it covered about 210,000 funds, with performance data on more than 14,000. Folded into eFront in February 2026; private credit analytics added in May 2026. | Private markets investors |
| Aladdin Studio | The developer and data layer: APIs, a Python SDK, data science tools and Aladdin Data Cloud | Client engineers, data analysts, code-curious portfolio managers |
| Aladdin Data Cloud | A managed data service on Snowflake that puts Aladdin and outside data in one place. Sold as an add-on to Aladdin Enterprise. | Data teams |
| Aladdin Copilot | A chat assistant that answers plain-English questions using data from across the platform | All platform users |
| Aladdin Climate | Measures physical climate risk and the risk of moving to a low-carbon economy | Risk and sustainability teams |
| Aladdin Accounting | Investment accounting and performance, sold as software or as a service BlackRock runs | Asset managers and asset owners |
| Aladdin Provider | Connects custodians and fund administrators into a client's Aladdin. Service providers pay BlackRock for its use. | Custodians and administrators |

Source: BlackRock product pages; AWS joint release FAQ, December 2025; iShares prospectus.

BlackRock agreed with Microsoft in April 2020 to host Aladdin on Azure, and the move began that year. Aladdin on AWS was expected to open to new US-hosted Enterprise clients in the second half of 2026. BlackRock said it was not moving existing clients at that time.

## How it makes money

Aladdin is sold as a subscription on long contracts. BlackRock's FY2025 10-K says fees are generally set by the value of positions on the platform or at a fixed rate. Revenue can also depend on the number of subscriptions, implementation go-lives, and delivery and support. Because part of the fee follows position value, revenue moves partly with markets. Falling bond markets in 2022 hurt it, for example. Chapter 4 covers pricing in detail.

BlackRock tracks the business with annual contract value, or ACV. ACV is the expected yearly subscription fees under signed contracts. It leaves out one-time set-up and consulting fees, so it shows momentum before revenue does.

**Exhibit 4. Technology revenue grew 74% from 2020 to 2025, and organic contract value is growing in the mid teens**

Technology services revenue (US$ millions; the original shows this as a bar chart):

| Year | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Revenue | 1,139 | 1,281 | 1,364 | 1,485 | 1,603 | 1,981 |
| Change | | +12.5% | +6.5% | +8.9% | +7.9% | +23.6% |

ACV growth, excluding Preqin:

| Period | ACV growth, excluding Preqin |
|-----------------------------------|-----------------------------------------------------------------|
| 2024 | 12% |
| 2025 | 16% |
| Q1 2026 | 14% |
| Q2 2026 | 15% |
| Long-term target | Low to mid teens |

Source: BlackRock 10-K for FY2020; BlackRock 10-Ks for FY2021 to FY2025; quarterly earnings releases; Q2 2026 earnings call, July 15, 2026. Changes are calculated from the figures in millions. Without Preqin, 2025 technology revenue was about $1.77 billion (Estimate).

In the second quarter of 2026, technology revenue was $566 million, up from $499 million a year earlier. Technology is still a small part of BlackRock's $24.2 billion in 2025 revenue. BlackRock values it because it recurs and is hard to switch away from. It wants private markets and technology to be 30% or more of revenue by 2030, up from about 25% in 2025.

About $25 trillion of assets sat on the platform as of December 2025. BlackRock itself managed a record $15.3 trillion at June 30, 2026, much of it run on Aladdin. A November 2025 BlackRock job posting, since taken down, said 5,500 engineers, financial modelers and data experts support Aladdin (Reported). A 2025 conference talk by BlackRock engineers described about 100 front-end applications maintained by about 4,000 engineers within a 7,000-person Aladdin organization. The two figures likely count different groups.

## Common criticisms

**Concentration risk.** If many big investors use the same risk models, they may reach the same conclusions and sell at once. One outage could also hit many firms together. The UK's Financial Conduct Authority flagged this in 2020. In 2020, the Los Angeles County pension fund (LACERA) cited "groupthink" as one reason it chose MSCI over Aladdin. Its concern was that BlackRock's own money managers use the same platform.

**Conflict of interest.** BlackRock is the world's largest asset manager and sells core software to firms that compete with it. SimCorp's chief executive said in 2018 that some clients avoid Aladdin because they do not want to fund a competitor. Japan's national pension fund (GPIF) listed a specific version of this risk in a 2015 risk register: that information about its investments could leak from BlackRock Solutions to BlackRock's asset management side.

**Cost and lock-in.** Moving a firm's core records onto or off Aladdin is slow and risky. UBS ended Credit Suisse's Aladdin contract in 2025 to cut costs after the merger.

# 2. What Aladdin is used for

Clients use Aladdin for nearly every step of running money, all on one shared record. Each team uses a different part of it, but every team sees the same numbers.

**Exhibit 5. Twelve jobs Aladdin does inside a client firm**

| Area | Job | What teams do in Aladdin |
|------------------|--------------------------------------|--------------------------------------------|
| Front office | Building and running portfolios | Portfolio managers see the whole portfolio, set targets, test a trade before placing it and rebalance. Common tasks include raising orders automatically, projecting settlement cash and running what-if tests on live positions. |
| Front office | Risk and stress testing | Aladdin's oldest strength. Aladdin Risk uses thousands of risk factors across public and private markets; the only public figure above 3,000 is a 2024 Fivetran write-up with BlackRock that says Aladdin "monitors over 5,000 risk factors daily," so cite that source if using the 5,000. Teams break exposure down by factor, sector or security and test shocks such as a rate jump. BlackRock also supplies ready-made "Market-Driven Scenarios." |
| Front office | Trading | A combined order and execution system routes and tracks orders across asset classes. It connects to Tradeweb, MarketAxess, Trumid and Coinbase, pairs with FlexTrade through a 2021 partnership, and since September 2026 trades interest rate swaps through OTCX. |
| Middle office | Compliance | Compliance teams write their investment rules into Aladdin. The system checks trades before they go out and again afterward. The APIs also expose the rules. |
| Middle office | Operations | Settlement, reconciliation, cash and fixing mismatched records. Many firms hand this to a custodian working inside their Aladdin through Aladdin Provider. BlackRock says over 95% of transactions then flow through without manual work. In February 2026, BlackRock named Citi to run some middle-office work for $4.0 trillion of US iShares ETFs on Aladdin. |
| Back office | Accounting | Aladdin Accounting joins holdings, accounting and performance records under GAAP, statutory, IFRS and tax standards. Insurers and pensions close their books on the same data their investors use. |
| Back office | Performance and attribution | Teams measure returns and explain where they came from. Aladdin Accounting produces official, locked returns for client reports. |
| Private markets | Private investments | eFront covers a private investment from finding the deal to reporting to investors. Since February 2026, Preqin data sits inside it, so investors can research funds, do due diligence and monitor what they bought in one system. Private credit data followed in May 2026. In July 2026, Preqin's closed-end fund indices became available across Aladdin, eFront and Aladdin Wealth. The indices cover more than 10,000 funds, a narrower set than the 14,000 funds with performance data. |
| Wealth | Advisors and private bankers | Advisors get risk checks, proposals and client reports. Aladdin Wealth's AI "Auto Commentary" turns analytics into short client-ready notes. Advisors can also compare private holdings against Preqin benchmarks. |
| Risk | Climate | Pensions and insurers use Aladdin Climate to put a number on climate risk and meet reporting rules. The UK pension scheme Nest uses it this way across its whole strategy. |
| Reporting | Board and regulatory reporting | Teams prepare data for regulators and build repeatable board reports. A common need is an "as-was" view of exposure on a past date. |
| Corporate | Corporate treasury | Companies manage the portfolios that hold their cash. Microsoft Treasury has used Aladdin for about 20 years, and Amazon Treasury runs its global portfolio on it. |

Source: BlackRock Aladdin product and Studio pages; client press releases, 2021 to 2026; Fivetran customer write-up with BlackRock, August 2024 (risk factor count).

Every one of these jobs leaves gaps that a firm fills with side tools and spreadsheets. Studio is how those gaps get built inside Aladdin instead of around it.

# 3. Who the customers are

Aladdin's customers are mostly large, regulated institutions that manage other people's money. The core groups are asset managers, insurers, pension funds, banks and wealth managers. Public filings, pension board papers and procurement notices now name dozens of them, which is far more than BlackRock's own press releases show. Recent public wins lean toward Asia and Europe. A 2025 conference talk by BlackRock engineers put the client base at hundreds of firms in 70 countries.

## What each group cares about

| Group | What it wants from Aladdin |
|----------------------------------------------|------------------------------------------------------|
| Asset managers | The full front-to-back system, to replace a patchwork of tools. The classic buyer for Aladdin Enterprise. |
| Insurers | Matching assets to what they owe policyholders, accounting under several standards at once, and capital rules. Many buy Aladdin Accounting. BlackRock says it has more than 150 insurance clients, or more than 200 when clients of Preqin and of Colmore, a private markets monitoring and fund administration firm Preqin bought in 2021, are counted. On scale, BlackRock's Georgette Anderson said in a Big Little Questions video: "we have roughly about 500 billion of insurance asset management on the system and 6 trillion of insurance assets that are actually processed through Aladdin" (Confirmed, BlackRock-published video). |
| Pensions and other asset owners | Whole-portfolio risk, private markets and climate |
| Banks and wealth managers | Risk tools and client-ready insights for advisors at scale. Banks also run their own securities books on Aladdin. |
| Custody banks | Running outsourced middle-office work for shared clients through Aladdin Provider. The client keeps a clear view of the work, as if it were done in-house, while paying the lower cost of outsourcing. |
| Corporate treasuries | Managing the company's cash investments |
| Central banks | Risk analysis on reserves. They appear in every BlackRock annual report, but few are named in public. |

## How many clients

BlackRock does not publish one official client count. The counts it has given use different scopes, so they range from about 200 to 1,100.

**Exhibit 6. BlackRock's own client counts differ because each one measures something different**

| Date | Count | What it covers | Label |
|-----------|----------------------------------|----------------------------------|---------------------|
| Oct 2026 | "Over 200 institutions" | Institutions using the Aladdin APIs, per an Aladdin Graph job posting | Confirmed |
| Nov 2025 | 1,100 Aladdin clients, supported by 5,500 staff | Aladdin overall, per a client experience job posting that is no longer online | Reported |
| May 2025 | 360,000+ users | Aladdin and Preqin users combined, shown at the June 2025 Investor Day; about three times the 2023 figure, mostly Preqin data users | Confirmed |
| Apr 2025 | 87 of the top 100 alternatives investors | Use Aladdin, eFront or Preqin | Confirmed |
| Jun 2024 | "Over 1,000 clients" | Aladdin platform, in the Preqin deal announcement | Confirmed |
| Jun 2023 | 130,000+ users, 98% three-year retention | Aladdin | Confirmed |
| Dec 2021 | 126,000 users; 1,000+ technology clients | Aladdin and related technology | Confirmed |
| Apr 2020 | Nearly 250 outside Aladdin clients | Core Aladdin platform | Reported |
| 2024 to 2026 | 3,000 citizen developers | BlackRock-internal headcount, not a count of Studio clients. Dave Woodhead, Head of Aladdin Studio Engineering, on Snowflake's Data Cloud podcast: "inside of BlackRock we have 3,000 citizen developers" and business engineers, adding "I think that number has probably peaked." Diwakar Goel, Global Head of Data, on a BlackRock pensions webinar: "we have 3,000 people who qualify in this bracket today." | Confirmed |
| Undated | "Over 200 institutions" | Aladdin FAQ page | Reported |
| Undated | Over 900 clients and 100,000+ end users | BlackRock careers page | Reported |
| Undated | Over 300 clients and close to 50,000 users | An Edinburgh job posting | Reported |

Source: BlackRock annual reports, investor days, earnings calls and job postings; Snowflake Data Cloud podcast with Dave Woodhead; BlackRock webinar "Data as a strategic asset for pensions." The higher counts likely include eFront and Aladdin Wealth clients (Estimate).

BlackRock's segment pages give a rough split. They say 400 asset managers, 150 insurers, and 180 pensions, corporations and endowments use Aladdin or eFront. They also say 11 large banks, at the US regulators' category 4 size or above, use Aladdin. The pages are undated and overlap.

Two figures show how sticky the business is. Recurring revenue was 98% of technology revenue in 2024. Client retention averaged 97% from 2022 to 2024.

BlackRock sizes Aladdin's addressable market at more than $20 billion: about $8 billion for public markets investment technology, $5 billion for private markets investment technology and $8 billion for private markets data. The estimates are as of year-end 2024 and come from BlackRock's 2025 Investor Day (Confirmed).

**Exhibit 7. Insurers were once the largest share of Aladdin revenue (historical)**

| Client type | Share of revenue |
|-------------------------------------------------------------------|---------------------------------|
| Insurers | 38% |
| Pensions, corporations and endowments | 21% |
| Banks | 16% |
| Asset managers | 14% |
| Other financial institutions | 11% |

Source: An undated BlackRock Solutions presentation describing "200+ clients," likely many years old. BlackRock has not published a current split. (The original shows this as a bar chart.)

## Named clients

The table below lists named clients by segment, with the type of evidence for each. A filing or a client's own document is stronger than a vendor press release, and a press release is stronger than a job posting.

**Exhibit 8. Named Aladdin clients and the evidence behind each**

*Asset managers*

| Client | What it uses | When | Evidence | Label |
|-----------------------|-------------------------|-----------|-------------------------|----------------|
| Janus Henderson | Moving its investment management, compliance, middle and back office onto Aladdin. A "complex, multi-year initiative." | Decided Q3 2025 | 10-K, Feb 2026 | Confirmed |
| Franklin Templeton | Aladdin Enterprise for public markets, phased in from fiscal 2025 | Jul 2024 | Press release | Confirmed |
| DWS (Deutsche Bank) | ESG data reaches analysts and portfolio managers through Aladdin | 2018 to Mar 2026 | Deutsche Bank filings | Confirmed |
| GMO | Aladdin Enterprise for portfolio management, trading, risk reporting and compliance across all funds | 2021 to Jun 2026 | Fund filings | Confirmed |
| Northwestern Mutual (funds) | Aladdin named as a portfolio management tool and for corporate actions | 2020 to May 2026 | Fund filings | Confirmed |
| Artisan Partners | Aladdin listed among systems that receive fund holdings | 2022 to Sep 2026 | Fund filings | Confirmed (use implied) |
| Ameriprise (Columbia Threadneedle) | Aladdin Accounting in North America; earlier, Aladdin for bond trading | 2014 to 2022 | Proxy and fund filings | Confirmed |
| MetLife Investment Management | Staff access to the "Aladdin Trading System" named in its code of ethics | 2016 to 2018 | Fund filings | Confirmed |
| Sumitomo Mitsui Trust AM (Japan) | Aladdin, about $620 billion at signing | Feb 2025 | Press release | Confirmed |
| Mirae Asset (Korea) | eFront Insight for private markets data | May 2025 | Press release | Confirmed |
| Liontrust | Aladdin, with BNY | Nov 2024 | Press release | Confirmed |
| Royal London AM | Aladdin for £153 billion, with HSBC running the middle office and Snowflake as its data platform | Mar 2024 | Press release | Confirmed |
| M&G | Aladdin, with State Street running the middle office | 2021 | Press release | Confirmed |
| Santander AM | Aladdin across all 10 of its countries: Europe live in 2020, the rest by 2021 | 2019 to 2021 | Santander filings and press releases | Confirmed |
| STANLIB | First South African firm on Aladdin Enterprise | Undated | Press release | Confirmed |
| Vanguard | Uses Aladdin to supplement in-house risk tools | 2018 | Press report | Reported |

*Insurers*

| Client | What it uses | When | Evidence | Label |
|------------------------------|------------------------------|----------|-------------|------------------|
| Corebridge Financial (formerly AIG Life and Retirement) | Full adoption of Aladdin's investment and accounting books of record | 2022 to 2025 | 10-K/A, Apr 2026 | Confirmed |
| AIA Group | Whole-portfolio platform, with BNY | Jul 2024 | Press release | Confirmed |
| MAPFRE AM (Spain) | Aladdin across a €60 billion portfolio, replacing in-house systems; the first Spanish insurer on Aladdin | Dec 2024 | Press release | Confirmed |
| Singlife (Singapore) | Aladdin with Citi for front, middle and back office | 2023 | Press release | Confirmed |
| F&G Annuities and Life | One-time Aladdin Climate pilot | 2024 | 10-K | Confirmed |

*Pensions and other asset owners*

| Client | What it uses | When | Evidence | Label |
|----------------------|----------------------|-----------------|-----------------|----------------------|
| Korea National Pension Service | Aladdin for overseas equity and bonds, with State Street and BNY running the middle office | Live Feb 2025 | Press release | Confirmed |
| GPIF (Japan) | Whole-portfolio risk analysis; multi-year contract awarded after a two-bidder competition | Nov 2024 | Procurement notice | Unconfirmed |
| CalPERS | Its own implementation of the Aladdin risk model; investment data platform contract | 2019 to present | Board materials | Confirmed |
| CalSTRS | Aladdin risk system for the total plan; order system compliance rules | 2023 to Jul 2026 | Quarterly board reports | Confirmed |
| Pennsylvania teachers' fund (PSERS) | BlackRock Solutions listed as its risk management system | FY2019 to FY2025 | Annual financial reports | Confirmed |
| Oregon State Treasury | Aladdin for internal trading and risk analytics | 2015 to present | Investment council books | Confirmed |
| Maryland State Retirement Agency | Aladdin Risk, procured in 2021 | 2021 | Risk assessment report | Confirmed |
| New Mexico State Investment Council | Aladdin Risk and eFront for a whole-portfolio view | 2019 to present | Investment plan; case study | Confirmed |
| Florida State Board of Administration | eFront for alternative investments | Jul 2022 | Annual report | Confirmed |
| Wisconsin Investment Board | eFront and a unified investment book of record | Jan 2026 | State agency news | Confirmed |
| UK Pension Protection Fund | Trading and risk for its liability-matching assets; risk for private markets | Award Jul 2025 | Procurement notice | Confirmed |
| Border to Coast (UK) | Moving its order and portfolio management from Bloomberg to Aladdin by end of 2026 | 2026 | Procurement notice | Confirmed; dates differ across sources |
| Nest (UK) | Whole-portfolio risk and Aladdin Climate | Selected 2023; onboarded 2024 | Press release; climate report | Confirmed |
| OMERS (Canada) | Implementing Aladdin in a public markets overhaul | 2025 | Job posting | Reported |
| Aware Super (Australia) | Completed Aladdin rollout with eFront | Jun 2026 | Trade press | Reported |
| AustralianSuper | Aladdin client since 2017 | Undated | BlackRock case study | Reported |
| Bank of Israel | A tailored version of Aladdin for reserves risk | 2019 to 2022 | Published interview | Confirmed |

*Banks, wealth and corporates*

| Client | What it uses | When | Evidence | Label |
|--------------------------|--------------------------|-----------|------------------|---------------------|
| JPMorgan Chase | Pays BlackRock yearly to access and use Aladdin | 2016 to 2025 | Proxy statements | Confirmed |
| BPI Wealth (Philippines) | Aladdin Enterprise and Aladdin Wealth | Aug 2026 | Press release | Confirmed |
| Cathay United Bank (Taiwan) | Aladdin Wealth for its private bank | Jun 2026 | Trade press | Reported |
| Citi Wealth | Aladdin Wealth for its advisors, as part of a September 2025 deal in which BlackRock manages about $80 billion for Citi clients | 2025 to 2026 | Citigroup proxy, Apr 2026 | Confirmed; deal size Reported |
| Morgan Stanley | Aladdin Wealth; first user of AI auto commentary | Oct 2025 | Press release | Confirmed |
| EFG International | Aladdin Wealth | Nov 2025 | Press release | Confirmed |
| Danske Bank | Aladdin Wealth | Jan 2025 | Press release | Confirmed |
| Allianz Bank; CaixaBank Private Banking | Aladdin Wealth | Nov to Dec 2024 | Press releases | Confirmed |
| HSBC | Aladdin-based portfolio and risk tools for its private bank, delivered through Prism Advisory in Asia | 2019 to 2022 | HSBC filings | Confirmed |
| Envestnet | Aladdin Wealth license, bundled with BlackRock investment models | 2022 to 2023 | Proxy statements | Confirmed |
| UBS | First US wealth firm to roll out Aladdin to advisors | 2017 | Press release | Confirmed |
| Microsoft Treasury | Aladdin for about 20 years; first to move to Azure | Ongoing | Case study | Confirmed |
| Amazon Treasury | First user of Aladdin on AWS | Dec 2025 | AWS joint release | Confirmed |

*Featured in BlackRock-published podcasts or videos*

These clients appear in BlackRock's own podcasts, client-story videos and eFront testimonial videos. A client speaking on the vendor's channel is weaker evidence than a filing but stronger than a job posting. None of them describes building on Studio's APIs or SDK.

| Client | What it uses | When | Evidence | Label |
|-------------------------|-------------------------|------------|----------------------|---------------|
| Intesa Sanpaolo (bank) | Aladdin | Mar 2024 | BlackRock client podcast teaser | Confirmed (featured) |
| SLC Management (Sun Life; insurer-owned asset manager) | Aladdin; the episodes are about data transformation and do not mention Data Cloud, Snowflake, Studio or APIs | Feb 2024; Mar 2026 | BlackRock podcasts | Confirmed (featured) |
| Aviva Investors | Aladdin; its global head of trading on trading data architecture | Dec 2025 | BlackRock podcast | Confirmed (featured) |
| TCW | Aladdin; its global COO on AI and time to insight | Jul 2026 | Never Done podcast | Confirmed (featured) |
| University Pension Plan Ontario (UPP) | Aladdin; its CIO on the Canadian pension model | Sep 2026 | BlackRock podcast | Confirmed (featured) |
| Ingka Investments (IKEA) | Aladdin for its financial markets portfolio | Dec 2024 | BlackRock podcast | Confirmed (featured) |
| Helvetia (Swiss insurer) | Aladdin; its asset management CTO on portfolio management | Undated | BlackRock client-story video | Confirmed (featured) |
| Northstar | Aladdin | May 2024 | BlackRock client podcast teaser | Confirmed (featured) |
| APG, Allianz Capital Partners, Velliv, Mizuho, Bouwinvest, Meridiam, Brown Brothers Harriman, Alter Domus | eFront | Undated | eFront client testimonial videos | Confirmed (featured) |

Source: Company filings on SEC EDGAR; pension board materials; UK Find a Tender notices; GPIF procurement disclosure; BlackRock and client press releases; trade press; BlackRock's Aladdin Client Stories and Never Done podcasts, client-story videos and eFront videos.

Older or secondhand sources also name Prudential plc and State Street Global Advisors as clients. These may be out of date.

## Clients who left or said no

**Exhibit 9. Public losses and rejections found since 2017**

| Firm | Date | What happened | Stated reason | Label |
|------------------------|-----------|------------------------|------------------------|------------------|
| UBS (Credit Suisse Asset Management) | Ended early 2025 | Moved off Aladdin onto UBS's own systems | Cost cuts and system consolidation after the merger | Reported |
| Rhode Island Treasury | Apr 2024 | Kept its incumbent, Solovis, over bids that included Aladdin with eFront, FactSet, and two MSCI products | Not published | Confirmed |
| LACERA (Los Angeles County pension) | Jan 2020 | Chose MSCI over Aladdin and FactSet for total fund risk | "Groupthink" concern; limited ongoing data management help | Reported (from board agenda) |
| Amundi (Pioneer Investments) | 2017 to 2019 | Moved about €240 billion off Aladdin onto its own ALTO platform in 18 months, and now sells ALTO to other firms | Cost, after the acquisition | Reported |

Source: Bloomberg, July 2025; Rhode Island Treasury recommendation memo, April 2024; Institutional Investor, January 2020; Amundi statements.

The two merger-driven exits, UBS and Amundi, followed acquisitions rather than product complaints. Amundi is now both a lost client and a competitor. The LACERA case matters most for Studio, because one of its two reasons was data management.

## Who buys and who uses

Big Aladdin deals are approved by top executives because they replace core systems and take years to install. BlackRock's own content targets chief investment officers, chief operating officers and senior technology leaders. Its implementation teams say installs are as much about changing processes as about technology.

Daily users sit across the whole firm: portfolio managers, traders, risk analysts, compliance officers, operations staff and accountants. A BlackRock executive described the point as giving the portfolio manager, the CEO, the chief accounting officer and the controller the same view. Studio users are engineers, data scientists, quants and analysts.

## What clients say they use it for

Clients talk most about one thing: seeing all their assets in one place.

**Bank of Israel (April 2022).** A senior risk analyst said that besides its own portfolio, the bank can see its holdings with each outside manager every day in Aladdin, so it can analyze both together. This is the clearest public client statement about data access, which is the need Data Cloud and the APIs serve.

**Royal London Asset Management (BlackRock client video, November 2024).** Its chief executive, Hans Georgeson, said the programme was delivered by three organisations, Royal London, Aladdin and HSBC, and that "we are genuinely in a minority of organisations that achieved it largely on time, if not ahead of plan, and we came in under budget." He said the client experience "in the past was multiple order management systems" and that the move allows "a single client statement," and he credited the data side: "the implementation of Snowflake that we did as part of the overall programme has been really successful." He gave no duration and did not call it the firm's largest programme (Confirmed, BlackRock-published video).

**Korea National Pension Service (February 2025).** NPS described one platform for global equity and bond portfolios across Seoul, New York, London and Singapore, with State Street and BNY running middle-office services.

# 4. What Aladdin costs

Aladdin has no public price list, but contracts, tenders and proxy statements show how it is priced. A client pays a fixed base fee plus charges that grow with assets on the platform, users, portfolios and data. Studio is not priced on its own in any public record. It is sold as more seats, data and usage inside the core contract.

## How BlackRock sets fees

BlackRock's FY2025 10-K, filed February 25, 2026, gives the clearest public description (Confirmed).

- Fees "are generally determined using the value of positions on the Aladdin platform, or on a fixed-rate basis."
- Revenue "may be based on several criteria including value of positions, number of subscriptions, implementation go-lives and software solution delivery and support." The FY2022 10-K said "number of users" where the newer filing says "subscriptions."
- Fixed minimum fees on current contracts total about $1.3 billion a year, and contracts run one to five years. That floor is about two thirds of 2025 technology revenue (Estimate). The rest moves with positions, usage and add-ons.
- "Aladdin assignments are typically long-term contracts that provide recurring revenue."
- Over half of new client mandates in 2024 covered more than one Aladdin product.

## How a price is built

The Texas Permanent School Fund contract is the most detailed public example. It was signed in 2014 and amended in 2017, so the dollar amounts are dated. The structure is the useful part.

**Exhibit 10. A public Aladdin contract shows a base fee plus charges for assets, users, portfolios and data**

| Fee element | Amount |
|------------------------------------------|----------------------------------------------------------|
| Base fee | $1.575 million a year, covering the first $16.5 billion of assets |
| Assets above $16.5 billion | 0.85 basis points |
| Users above 30 | $20,000 a year each |
| Portfolios above 16 | $5,000 a year each |
| Derivative lines above 25 | $600 each |
| Implementation | $160,000 a month |
| Outside data | Passed through at cost |
| Actual yearly bills | $1.6 million to $1.9 million |

Source: Texas Education Agency, BlackRock contract for hosted Aladdin (trading, portfolio management and risk), 2014, amended 2017. Confirmed; older than 2018.

If Studio follows this pattern, its price shows up as more users, more data and more usage inside the core contract (Estimate). A BlackRock job posting that was live by November 2024 supports this. It describes Studio as having "free and premium capabilities."

## What clients pay

Public price points fall into three rough bands.

**Exhibit 11. Public Aladdin price points range from about $0.5 million to more than $20 million a year**

| Buyer | Year | What it covers | Yearly cost (USD) | Label |
|----------------------|----------|----------------------|----------------------|----------------------|
| *Risk tools only* | | | | |
| Nest (UK) | 2023 | Investment risk platform, 5-year contract | About $463,000 | Confirmed notice; yearly figure Estimate |
| LACERA (bid, not chosen) | 2019 to 2020 | Total fund risk analytics | $675,000 to $865,000 | Reported |
| US Pension Benefit Guaranty Corporation | 2017; rebid 2023 | Investment risk system from BlackRock; product not named | About $1.39 million, unchanged at rebid | Confirmed contract; Aladdin Estimate |
| *Fuller platform, mid-size fund* | | | | |
| Texas Permanent School Fund | 2014 to 2017 | Hosted Aladdin for trading, portfolio management and risk | $1.6 million to $1.9 million | Confirmed; older than 2018 |
| CalPERS | 2019 to 2024 | Investment data platform and risk and operational reports | About $1.85 million ($9.26 million over five years) | Confirmed; see note |
| *Largest buyers* | | | | |
| UK Pension Protection Fund | 2025 | Trading and risk for liability-matching assets; risk for private markets; 5 + 5 years | About $6.5 million to $9.8 million | Confirmed notice; yearly figure Estimate |
| UBS (Credit Suisse) | 2019 to 2025 | Aladdin for asset management | About CHF 8 million to 17 million (CHF 50 million to 100 million in total) | Reported |
| JPMorgan Chase | 2024 to 2025 | Access to and use of Aladdin | $14.7 million to $25.6 million | Confirmed |
| GPIF (Japan) | 2024 | Portfolio risk and return analysis tool (Aladdin), multi-year | ¥2.78 billion in total; term not published | Unconfirmed |

Source: UK Find a Tender notices; Institutional Investor, January 2020; USAspending.gov; Texas Education Agency; CalPERS board materials, November 2021; Bloomberg, July 2025; JPMorgan Chase proxy statements; GPIF procurement disclosure, March 2025. Pounds converted at $1.32.

Note on CalPERS: a separate November 2025 CalPERS document shows payments of $9.3 million in FY2021 rising to $15.0 million in FY2025 for a fixed income platform, with the note "Payment is based on assets on the investment platform." The two documents may describe different contracts. Read both before citing either. Revision note: the two CalPERS figures come from different sources (board materials of November 2021 and a finance item of November 2025) and need reconciling before either is used in an interview.

Aladdin is cheap relative to the money it oversees. For very large funds, risk and data services cost roughly 0.0004% to 0.0015% of assets a year (Estimate). Once installed, Aladdin tends to stay. CalPERS extended its contracts in 2023 for three more years with "little-to-no fee increase." The US Pension Benefit Guaranty Corporation rebid in 2023 and kept BlackRock at the same price.

## One account over ten years

JPMorgan Chase discloses its Aladdin payments each year in its proxy statement. It is the only public record of one client's spending over many years.

**Exhibit 12. JPMorgan's yearly Aladdin payments rose almost sixfold from 2017 to 2025**

US$ millions (the original shows this as a bar chart):

| Year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|--------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Payments for Aladdin | | 4.4 | 5.0 | 5.3 | 6.8 | 4.6 | 7.6 | 6.9 | 14.7 | 25.6 |
| Integration services | 1.5 | | | | | | | | | |

Source: JPMorgan Chase proxy statements (DEF 14A), filed 2017 to 2026. All years Confirmed.

This series shows the kind of account growth Studio is meant to drive. JPMorgan is a bank and custodian as well as a user. In 2018 it said it was connecting to Aladdin to link directly with its custody clients on the platform (Reported). Part of these payments may therefore reflect JPMorgan's role as a service provider rather than a standard client license.

Envestnet's proxy statements show a smaller example. It paid BlackRock about $3.7 million in 2022 and $4.1 million in 2023 for BlackRock investment models plus a license for Aladdin Wealth (Confirmed).

## How buyers choose

Public tenders show that buyers weight technical fit far above price.

**Exhibit 13. Technical fit outweighs price in every published Aladdin tender score**

| Buyer | Year | How bids were scored | Bids | Outcome |
|-----------------------|--------|-----------------------|-----------------------|-----------------------|
| UK Pension Protection Fund | 2025 | Technical 85, price 6, price sensitivity 6, contract terms 3 | 2 and 4 per lot | Aladdin won both lots. The award came in above the fund's own estimate. |
| Nest (UK) | 2023 | Quality 70, cost 20, social value 10 | 7 | Aladdin won |
| LACERA | 2020 | Not published | 7 responses; MSCI, BlackRock and FactSet as finalists | MSCI won at $478,000 to $730,000. FactSet bid $780,000 to $910,000. |
| US Pension Benefit Guaranty Corporation | 2017 and 2023 | Full and open competition | 4 each time | BlackRock won both times |

Source: UK Find a Tender; LACERA board agenda as reported by Institutional Investor; USAspending.gov.

LACERA's reasons are the most useful for Studio. It cited "groupthink" because BlackRock's own money managers use the same platform. It also said that "unlike MSCI, BlackRock has limited on-going data management services." Choosing Aladdin would have meant hiring an analyst just to load and reconcile private assets data. That is the work Data Cloud is now meant to take over.

## How Studio and its neighbors are packaged

**Exhibit 14. Public signals about how Studio, Data Cloud and related services are packaged**

| Signal | What it says | Label |
|--------------------------------------|--------------------------------------|-----------------------|
| AWS joint release FAQ, December 2025 | Aladdin Data Cloud is listed as an "Enterprise add-on." Prices are the same whichever cloud the client picks. | Confirmed |
| Studio product marketing job posting, live by November 2024 | Studio has "free and premium capabilities" | Confirmed |
| Australian trade press, 2018 | Some Aladdin reporting came free with BlackRock fund management contracts; the full platform cost extra | Reported |
| iShares prospectus | Custodians and administrators pay BlackRock for using Aladdin Provider | Confirmed |

## What this means for Studio

Studio's commercial story is account growth and retention, not a separate price tag. It adds users, data and usage inside contracts that already exist. On a $2 billion business, each point of retention or ACV growth is worth about $20 million a year (Estimate). The UBS exit shows the other side: when a client consolidates for cost, the whole contract is at risk. Studio's argument is that what a client builds on Aladdin is a reason to stay.

# 5. What Aladdin replaces and what it complements

Aladdin replaces the client's record of investment positions and every tool wired directly to it. It sits alongside tools that either feed it inputs, like market data, or act on its outputs, like trading venues and custodians. Clients rarely swap one product for another. They retire a whole group of systems at once. BNP Paribas Asset Management decommissioned "more than 60 applications" in its 2016 to 2020 "Back in the Race" programme, which put Aladdin in the front-to-back chain alongside Salesforce for CRM and a DataHub, so the 60 belong to the whole programme rather than to Aladdin alone (Confirmed, BlackRock client podcast, February 2023). Over half of new mandates in 2024 covered more than one Aladdin product.

**Exhibit 15. Aladdin switches off the tools around the book of record and connects to the rest**

| Category | Effect | Why |
|-----------------------------------|-----------------------------|-----------------------------------|
| Order and portfolio management systems | Replace | Aladdin's order management sits on the same data as risk and compliance |
| Separate risk engines | Replace | One risk model across all asset classes removes manual stitching |
| Book of record and reconciliation tools | Replace | Aladdin becomes the single source of truth |
| Compliance rule engines | Mostly replace | Rules run on Aladdin positions; niche tools such as FundApps for disclosure rules stay |
| Spreadsheets | Replace | They fill gaps between disconnected systems, and the gaps close |
| Private markets tracking | Replace, through eFront | Private assets join public ones in one view |
| In-house data warehouses and file feeds | Replace, through Data Cloud | A managed, preloaded Snowflake store replaces raw file deliveries |
| Custom data engineering | Partly replace, through Studio | APIs and the SDK replace hand-built pipelines; the client's developers stay |
| Official fund accounting | Depends | Aladdin Accounting can replace it, but many clients keep a custodian or administrator |
| Execution management systems | Depends | Aladdin trades directly but also connects to FlexTrade, FactSet's Portware and Talos |
| Market, reference and ESG data | Complement | Aladdin uses the data but does not produce most of it |
| Custodians and fund administrators | Complement | They run services inside the client's Aladdin through Aladdin Provider |
| Trading venues and brokers | Complement | Aladdin routes orders to more than 200 of them |
| Post-trade utilities | Complement | AccessFintech and Saphyre reach counterparties Aladdin cannot |
| Core banking and CRM | Complement | Aladdin Wealth sits beside Avaloq; BNP kept Salesforce |
| Cloud and the firm's own data platform | Complement | Aladdin runs on Azure or AWS and feeds the client's own Snowflake and reporting tools |

Source: BlackRock filings and earnings calls; client case studies; implementation consultants; trade press.

MSCI shows how the line can split one company. Its index and ESG data usually stay, while its Barra risk models may be what Aladdin replaces.

## Why clients choose Aladdin for the replacement

1. **One data model.** Every team reads the same positions, which ends arguments about whose number is right.
2. **The whole portfolio.** Public and private assets appear in one place with one risk model.
3. **Lower long-run cost.** Franklin Templeton and STANLIB both cited it.
4. **Room to grow.** Firms can grow without adding much technology overhead.
5. **Risk depth.** Clients get the same models BlackRock uses on its own money.

## When it depends

Whether Aladdin replaces or complements depends on how much of it a client buys and who runs its back office.

- **Risk bought alone.** Aladdin Risk can be bought on its own. It then replaces a risk engine but sits beside the client's existing order system. Many of those clients later upgrade to the full platform.
- **Middle office.** It can go either way. Royal London handed its middle office to HSBC working on Aladdin. Aegon Asset Management ran its own middle office after moving to Aladdin, then in August 2026 handed it to Citi, covering $380 billion of assets.
- **Preqin.** Preqin is still sold on its own, so it can feed a non-Aladdin setup as easily as it can be part of a migration.

## What switching costs

Public filings now show the cost of a move from the buyer's side.

- **Janus Henderson** booked $14.9 million of faster write-down of its existing cloud software, plus impairments, after deciding in Q3 2025 to move to Aladdin. Its 10-K calls the move "a complex, multi-year initiative" and lists it as a business risk. It says the program will redesign its "systems and data architecture under a global operating model," with connections to custodians, administrators, brokers and data providers.
- **Corebridge Financial** took about three years, from 2022 to 2025, to reach full adoption of Aladdin's investment and accounting books of record, replacing many systems it inherited from AIG.
- **Royal London Asset Management's** chief executive said in a BlackRock client video that the programme came in "largely on time, if not ahead of plan, and we came in under budget," replacing "multiple order management systems" with one platform run with HSBC. No duration has been published, and the video does not call it the firm's largest programme (Confirmed, BlackRock-published video, November 2024).

## Where Studio fits

Studio replaces hand-built data pipelines, nightly file extracts and analytics setups that copy Aladdin data elsewhere. It does not replace the client's own engineers and quants. It changes what they spend time on. Royal London's trading desk is an example. After consolidating its order systems onto Aladdin, it hired an analyst to build its own pre-trade tools on top of one data source (Reported). Public hiring ads show this work clustering around migrations. A contractor ad for a Janus Henderson project asks for help "transforming CRD trading APIs and Python-based workflows" onto Aladdin. CRD is Charles River, a rival order management system.

## Real migrations

**Exhibit 16. Public migrations show clients replacing a group of systems at once**

| Firm | What happened | Label |
|---------------------------------|----------------------------------|----------------------------------|
| Janus Henderson | Decided in Q3 2025 to move its investment platform to Aladdin, after earlier choosing Charles River for its front office | Confirmed |
| Corebridge Financial | Reached full adoption of Aladdin's investment and accounting books of record by 2025 | Confirmed |
| Korea National Pension Service | Went live in 2025 with State Street and BNY services plugged into Aladdin | Confirmed |
| Franklin Templeton | Chose Aladdin across public markets in July 2024 after reportedly planning a move to Charles River's cloud | Confirmed; Charles River plan Reported |
| Royal London AM | Replaced "multiple order management systems" with Aladdin, live by December 2023; its chief executive says the programme came in largely on time and under budget. Trade press named the old systems as thinkFolio and Murex; BlackRock's own video does not name them. | Confirmed (go-live and CEO remarks); system names Reported |
| MAPFRE AM | Replaced in-house systems in December 2024 | Confirmed |
| Border to Coast | Moving from Bloomberg to Aladdin by the end of 2026 | Confirmed |
| BNP Paribas AM | Decommissioned more than 60 applications across its 2016 to 2020 programme, which covered Aladdin front to back, Salesforce for CRM and a DataHub | Confirmed (BlackRock client podcast) |
| Santander AM | Signed in March 2019 to unify risk on Aladdin across its 10 countries. Europe went live on schedule in 2020, and the rest followed by 2021 | Confirmed |
| New Mexico State Investment Council | Its investment office replaced several vendors and manual work with Aladdin Risk and eFront, across about $26 billion of assets at the time of BlackRock's case study, which is undated | Confirmed |
| Amundi (reverse case) | Moved Pioneer off Aladdin onto its own ALTO platform in 18 months, finishing in 2019 | Reported |

## Partners that connect to Aladdin

**Exhibit 17. Trading venues, data firms and token platforms build direct connections to Aladdin**

| Partner | Year | Connection | Label |
|--------------------|--------------|-----------------------------------------|-------------------------|
| Securitize | 2026 | A contract filed with the SEC covers integrations between Securitize's platform and Aladdin. BlackRock created its $2 billion tokenized liquidity fund with Securitize. | Confirmed |
| OTCX | 2026 | Interest rate swap trading inside Aladdin | Confirmed |
| AccessFintech | Nov 2025 | Post-trade workflow integration; BlackRock also invested in the company | Confirmed |
| Tradeweb | 2024 | Integration with Aladdin's order and execution system for US trading | Confirmed |
| FactSet (Portware) | 2022 | Multi-year partnership to connect Portware's execution tools to Aladdin | Confirmed |
| Coinbase | 2022 | Crypto trading and custody for Aladdin's institutional clients | Confirmed |
| MarketAxess | 2013 | Credit trading between Aladdin users and the MarketAxess network | Confirmed |

Source: Partner filings on SEC EDGAR; press releases.

Other partners include Snowflake, Microsoft Azure, AWS, iCapital, FlexTrade and Avaloq. LSEG carries Preqin data in its Workspace platform.

The Securitize link matters for timing. Tokenization is one of the themes of BlackRock's fall 2026 Aladdin Client Forum.

BlackRock keeps adding native features, so a partner today can become a replacement target later.

# 6. Competitors

Only a few vendors compete with the whole Aladdin platform. SimCorp and State Street Alpha are the usual shortlist, and a second group is closing in. Much of what Aladdin beats, though, is the client's own in-house systems. BlackRock's annual report names both threats: rivals with more complete offerings as the industry consolidates, and clients moving toward standalone or in-house solutions.

## How big Aladdin is next to rivals

Aladdin earned $1.98 billion in technology services revenue in 2025, or about $1.77 billion without Preqin. Deutsche Börse's Software Solutions unit, which is SimCorp plus the Axioma risk business, reported €745 million of net revenue for 2025. That is about $840 million at an average 2025 rate of about $1.13 per euro (Estimate). The unit ended 2025 with €680 million of annual recurring revenue, up 18%. Measured revenue to revenue, Aladdin is roughly two to two and a half times SimCorp's size. SimCorp's recurring revenue grew 18% in 2025, against 16% organic contract value growth at Aladdin. Amundi's ALTO ran at about €100 million in 2024.

**Exhibit 18. Three vendors compete for the whole platform, two compete in part, and two more are building toward it**

| Vendor | Full-platform rival? | Strongest with | Key facts |
|---------------------------|-----------------|----------------------------|----------------------------|
| SimCorp One (Deutsche Börse) | Yes | Large asset managers, insurers and pensions, especially in Europe | €680 million annual recurring revenue at the end of 2025, including Axioma; 800+ clients; strong in accounting |
| State Street Alpha (Charles River) | Yes | Firms that want one partner for software and outsourced operations | About $59 trillion on Charles River at the end of 2025, by its own count, including clients that use it only for compliance checks; 28 live Alpha clients by mid-2025; four new mandates in 2025 |
| Amundi ALTO | Yes, mainly in Europe | European managers, banks and wealth firms | 80+ clients; pitched as the European alternative |
| Bloomberg AIM, PORT and MARS | Partly | Mid-size managers, bond desks, insurers | AIM used by more than 14,000 professionals at over 850 firms, per a Bloomberg job ad; needs a partner for accounting |
| Clearwater with Enfusion and Beacon | Emerging | Insurers, hedge funds, midsize managers | Taken private for $8.4 billion in June 2026 |
| Arcesium with Limina | Emerging | Hedge funds and alternatives managers | Bought Limina in February 2026 to add front office |
| SS&C (Eze, Geneva) | Partly | Hedge funds and alternatives | Competes one layer at a time |
| MSCI, FactSet, LSEG | One layer | All segments | Data and risk partners as often as rivals |

Source: Company filings and press releases; trade press.

## The main rivals in brief

**SimCorp** sells the same thing to the same buyers: one platform from portfolio decisions through accounting. Aladdin is seen as stronger in risk and portfolio management, and SimCorp as stronger in accounting and back office. SimCorp is moving into private markets and won Pictet and Marathon in mid-2026. It has hired two former Aladdin product heads, one directly and one by way of S&P Global. In December 2025 it named Iyan Adewuya chief product officer. He joined from S&P Global and earlier led product for Aladdin Portfolio Management and Compliance. In September 2026 it hired Gareth Morris, who spent 16 years in the Aladdin business and was most recently Global Head of Product for Aladdin Portfolio Management.

**State Street Alpha** bundles Charles River's front-office software with State Street's custody and back-office services. The buyer is often outsourcing operations, not only buying software. Named clients include Invesco, BMO, Lazard, LGIM and Challenger. Growth is steady but modest, at four new mandates in 2025 and one in early 2026. State Street is also a partner, running middle office for Aladdin clients such as M&G and Korea's NPS.

**Bloomberg** is strongest in the front office and in bonds. It usually pairs with another vendor for accounting, as at BarmeniaGothaer, where Clearwater covered the back office. That pairing is a real alternative to one Aladdin contract.

**Clearwater** began in accounting for insurers and bought its way to a full platform. It is not yet a common choice for the largest global managers Aladdin targets. **Arcesium** is moving from the back office toward the front and competes mostly at the data layer and in alternatives. **Amundi ALTO** is the clearest case of a firm leaving Aladdin and then selling a rival.

## Decisions from 2024 to 2026

Public announcements from 2024 to 2026 show which platforms firms chose and why. Few name the rivals they considered.

**Exhibit 19. A sample of public platform decisions from 2024 to 2026**

| Date | Firm | Choice | Stated reason | Label |
|--------|-------------------------|-------------------------|-------------------------|---------------|
| Sep 2026 | PREPAR-VIE (French insurer) | Clearwater | French GAAP and IFRS accounting in one tool | Confirmed |
| Sep 2026 | NFU Mutual (UK insurer) | Bloomberg front office plus Clearwater operations | Automated, flexible end-to-end operating model | Confirmed |
| Aug 2026 | BPI Wealth | Aladdin | Institutional-grade tools; growth in alternatives | Confirmed |
| Jul 2026 | MSIG Europe (insurer) | Clearwater | One reliable source of investment data; Solvency II | Confirmed |
| Jun 2026 | Marathon Asset Management | SimCorp One | Unify operations on one platform | Reported |
| May 2026 | Pictet Asset Management | SimCorp One, extended from its back office, with its own tools connected by API | Fewer core systems, one data layer | Confirmed |
| Mar 2026 | BarmeniaGothaer (German insurer) | Bloomberg front office plus Clearwater middle and back office | One front-to-back setup after the 2024 Barmenia and Gothaer merger | Confirmed |
| Feb 2026 | AllianceBernstein | SimCorp One, keeping "specialized in-house technology" | One platform, real-time data | Confirmed |
| Feb 2026 | Lindsell Train | SimCorp One | Reliability; less time reconciling data | Confirmed |
| Dec 2025 | T. Rowe Price | Charles River's cloud, replacing its own systems | Efficiency and scale | Confirmed |
| Dec 2025 | Van Lanschot Kempen | Amundi ALTO | All business lines in one system | Reported |
| Nov 2025 | Ninety One | State Street Alpha | Simpler operating model | Confirmed |
| Q3 2025 | Janus Henderson | Aladdin, after earlier picking Charles River | Global operating model and data architecture | Confirmed |
| Jul 2025 | UK Pension Protection Fund | Aladdin, both lots | Technical fit weighted 85 of 100 | Confirmed |
| Jul 2025 | UBS (Credit Suisse AM) | Left Aladdin for its own systems | Cost cuts after the merger | Reported |
| Jul 2025 | Versicherungskammer (German insurer) | Clearwater | Real-time analytics; insurance focus | Confirmed |
| Feb 2025 | Sumitomo Mitsui Trust AM; Korea NPS | Aladdin | Faster access to new technology; scalable operations | Confirmed |
| Dec 2024 | MAPFRE AM | Aladdin, replacing in-house systems | One connected, scalable platform | Confirmed |
| Sep 2024 | Challenger | State Street Alpha with custody | Track record and global reach | Confirmed |
| Jul 2024 | Franklin Templeton | Aladdin | Unify the platform; lower long-term capital spending | Confirmed |
| Jul 2024 | AIA | Aladdin with BNY | One consistent view across all asset classes | Confirmed |
| Apr 2024 | Rhode Island Treasury | Kept Solovis over Aladdin | Not published | Confirmed |
| Mar 2024 | Royal London AM | Aladdin, with Snowflake | One platform that works with HSBC | Confirmed |

Source: Company and vendor press releases; trade press; Bloomberg; Rhode Island Treasury memo; UK Find a Tender. The table is a sample of public announcements, not a complete list.

**Exhibit 20. The reasons given in the sample of decisions**

| Outcome | Reason | Decisions citing it |
|------------------------------|-----------------------------------|-----------------------------------|
| Chose Aladdin (9 decisions) | One platform or one view of data | 5: Janus Henderson, MAPFRE AM, Franklin Templeton, AIA, Royal London |
| | Scale and lower long-run cost | 4: Sumitomo Mitsui Trust AM, Korea NPS, MAPFRE AM, Franklin Templeton |
| | Technical fit, tools or faster access to new technology | 4: BPI Wealth, UK Pension Protection Fund, Sumitomo Mitsui Trust AM, Korea NPS |
| | Works with the firm's custodian | 2: AIA (BNY), Royal London (HSBC) |
| | Growth in alternatives | 1: BPI Wealth |
| Chose a rival (13 decisions) | One platform, one data layer or one front-to-back setup | 8: NFU Mutual, MSIG Europe, Marathon, Pictet, BarmeniaGothaer, AllianceBernstein, Lindsell Train, Van Lanschot Kempen |
| | Insurance accounting and regulation | 3: PREPAR-VIE, MSIG Europe, Versicherungskammer |
| | Efficiency, scale or a simpler operating model | 2: T. Rowe Price, Ninety One |
| | Keep its own tools connected by API | 2: Pictet, AllianceBernstein |
| | Technology bought together with outsourced operations | 1: Challenger |
| Kept the incumbent (1 decision) | Not published | 1: Rhode Island Treasury |
| Left Aladdin (1 decision) | Cost cuts after a merger | 1: UBS |

Source: Count of the stated reasons in the table above. A decision can give more than one reason. Sumitomo Mitsui Trust AM and Korea NPS share a row above but count as two decisions (Estimate).

Every insurer decision found since July 2025 went at least partly to Clearwater, which is built around insurance accounting. These were Versicherungskammer (July 2025), BarmeniaGothaer (March 2026), MSIG Europe (July 2026), NFU Mutual (September 2026) and PREPAR-VIE (September 2026). Earlier insurer decisions went other ways. AIA and MAPFRE's asset manager chose Aladdin in 2024, and Challenger, an annuity insurer, chose State Street Alpha.

SimCorp's wins at Pictet and AllianceBernstein promised clients they could keep their own tools connected by API, which is Studio's pitch. BlackRock's own 2026 AI adoption report is based on a survey of 303 investment firms. The figure of "68% favor core platforms plus their own builds," used in the earlier draft of this guide, could not be verified against the report; it appears to fuse the report's sample size with a separate BlackRock webinar finding that 68% of surveyed investors call a single view across public and private holdings crucial. Treat it as Unconfirmed until checked against the report itself. BlackRock's own Build vs Buy webinar gives a better-sourced reading of the same question.

**Exhibit 20A. BlackRock's Build vs Buy webinar: what asset managers said about building, buying and maintaining**

| Finding | What was said | Label |
|--------------------------------------|--------------------------------------|-----------------------|
| Where firms sit today (live audience poll) | "mostly built in house at about 15%," "actively reevaluating at 18%," "hybrid second most at 30 and then mostly vendor platforms at 37%" | Confirmed |
| Cost of maintenance | "if you have 60 to 70% of your tech organisation focused on keeping the lights on, well, then you can't deploy that engineering capacity to go build that differentiation" | Confirmed |
| Top driver for re-evaluating (poll) | "AI and data demands at 42%, an exact tie between cost and speed to market. And last place was regulatory complexity" | Confirmed |
| What firms most want to stop maintaining (poll) | "compliance reporting is number one at 53% followed by position and cash management 22%, trade life cycle at 17 and finally risk infrastructure at 9%" | Confirmed |
| Migration timing | "12 to 18 months is what we see most regularly," with return on investment arriving some months after go-live as roles settle | Confirmed |
| What RFPs now ask | "what's the API suite that you have? Are you using connectors to Snowflake or to Databricks? And I think that part of the RFP has become much more prominent" | Confirmed |
| Closing argument | "maintaining plumbing or functions that are solved or commoditized may not be the best source of generating alpha, generating differentiation" | Confirmed |

Source: BlackRock Build vs Buy webinar replay, with Michael Campos and Alisha Sewdass of Aladdin and Clark Schafer of Alpha FMC. The poll is of the webinar's audience, not a representative survey.

## Head-to-head evidence

Firms rarely announce what they left, so the record is thin. Invesco chose State Street Alpha in April 2021, with a phased rollout through 2024. Franklin Templeton chose Aladdin in 2024 after reportedly planning a move to Charles River's cloud. Amundi moved Pioneer off Aladdin after 2017. People move too. SimCorp has hired two former Aladdin product heads, one directly and one by way of S&P Global.

## Rivals that name Aladdin

Rivals list BlackRock as a competitor in their own annual reports. MSCI has done so every year from 2011 to 2026. FactSet has done so from 2013 to 2025, and Clearwater since its 2021 stock listing. In its 2021 listing documents, Enfusion described incumbents including Aladdin as "single-tenant and cloud-migrated rather than cloud-native."

## Analyst rankings

**Exhibit 21. BlackRock's standing in industry rankings has slipped since 2023**

| Ranking | Result | Label |
|---------------------------|------------------------------------|------------------------------------|
| Chartis RiskTech100 | BlackRock Solutions ranked 26th (2021) to 40th (2023), then dropped off the 2024 and 2025 lists | Confirmed |
| Chartis BuySideRisk50, 2024 | 9th, one place below Deutsche Börse, SimCorp's owner | Confirmed |
| WatersTechnology awards | Three Buy-Side Technology Awards in 2023: Best Overall Technology Provider, Best IBOR and Best Portfolio Analysis Tool; in 2024 Bloomberg won best overall and SimCorp won best IBOR | Confirmed (2023, BlackRock's own winner interview video); Reported (2024) |

Two consultant views frame the market. Celent found in April 2025 that 63% of buy-side firms planned to replace or significantly upgrade at least one critical system that year, favoring end-to-end solutions. Deloitte warned in December 2025 of an "integration tax" from joining many systems and of lock-in with front-to-back platforms. It suggested one core data layer with specialist tools joined by open APIs.

## Rivals for each product line

In private markets, eFront competes with Allvue, FIS Investran, SS&C Geneva, Dynamo and Juniper Square. Preqin competes with MSCI's Burgiss and Morningstar's PitchBook on data. Some argue that MSCI's independence as a source of private markets benchmarks is a selling point, now that BlackRock owns both an asset manager and a major data source. He should be ready for that objection. In wealth, Aladdin Wealth competes with Addepar, Envestnet, InvestCloud, Avaloq and FNZ. Its niche is risk analytics for large private banks and wirehouses. Big wealth firms often run several of these tools side by side.

## Who Studio competes with

Studio's main competitor is the client's own data team. A large manager can buy Snowflake or Databricks, hire data engineers and build its own pipelines. Studio has to win on time to value, because Aladdin data arrives already modeled and ready to use. That is why BlackRock built Data Cloud on Snowflake instead of fighting it.

The vendor rivals are the data platforms inside other suites. Arcesium's Aquata is the most direct, with thousands of prebuilt data models and a marketplace of partner integrations. State Street has its Alpha Data Platform, SimCorp has its data services, and Clearwater's Beacon adds developer tools. Bloomberg, LSEG and FactSet sell data feeds that clients use to build their own layer. In practice, Studio rarely wins or loses alone. It is part of the larger Aladdin decision, or an existing client choosing between building on Studio and building next to Aladdin.

**Exhibit 22. Rivals now sell some version of "build on our data with AI"**

| Rival | Recent move | Label |
|-------------------------|--------------------------------------|--------------------------------------|
| SimCorp | Agent Launchpad, April 2026: prebuilt AI agents, or clients build their own on SimCorp One's data layer | Confirmed |
| Clearwater | Agents running in production at about 900 clients, September 2026. Custom-workflow builders up 197% since January. | Confirmed (company figures) |
| FactSet | Public MCP server, December 2025. MCP is a common standard that lets AI assistants pull data from outside tools. | Confirmed |
| LSEG | Claude connector, October 2025; MCP server with about 90 connected customers by April 2026 | Confirmed (connector); Reported (counts) |
| MSCI | AI connectors for Claude, ChatGPT and Copilot, February 2026; SignalLab research tools, October 2026 | Confirmed |
| Arcesium | MCP server for clients, December 2025 | Confirmed |
| S&P Global | Credit ratings reachable from any MCP-enabled AI tool, September 2026 | Confirmed |
| Bloomberg | BQuant Enterprise cloud Python environment, chosen by Fairtree (April 2026) and Maj Invest (September 2026) | Confirmed |
| Snowflake and Databricks | Managed MCP servers | Confirmed |
| Build your own | Consultants list running your own data on Snowflake as a standard option. Goldman Sachs runs its own governed data platform on Databricks. Many vendor platforms, Data Cloud included, are themselves built on Snowflake. | Reported |
| BlackRock | An agent skills repository for its Advisor Center wealth tool, September 8, 2026. BlackRock joined Claude for Financial Advisors as a partner on September 14, 2026, for Advisor Center. No public AI connector exists for Aladdin itself. | Confirmed |

Source: Company press releases and developer pages; LSEG Q1 2026 results materials; BlackRock GitHub.

Studio's case therefore cannot rest on having APIs. Its stronger argument is that it builds on the same data model and controls that already run the client's portfolio. What clients build stays governed and in step with the system of record.

## How it differs by segment and region

For the largest global managers and asset owners, the choice is Aladdin, SimCorp or State Street Alpha, with building in-house as a fourth option. The deciding question is often whether the buyer wants software alone or software plus outsourced operations. Insurers give Clearwater and SimCorp more weight because of their accounting depth. Hedge funds lean toward Enfusion, Arcesium, SS&C and Bloomberg. For wealth firms, Aladdin Wealth is one of several tools rather than the default.

Europe is the most contested region, with SimCorp, ALTO, Bloomberg and Clearwater all active. North America is where Aladdin and Charles River are most deeply embedded. Asia-Pacific has gone both ways: Sumitomo Mitsui Trust and AIA chose Aladdin, while Challenger chose State Street Alpha.

# 7. Aladdin Studio in depth

Aladdin Studio is the part of Aladdin that lets clients build their own tools on top of it. BlackRock calls it "API-first" and uses the tagline "Make Aladdin your own." In 2026 it describes Studio as Aladdin's extensibility layer: the governed place where clients extend and automate their work without breaking the core system.

## Who it is for

The Studio page names three users: "a professional engineer building new workflow applications, a code-curious portfolio manager extracting investment insights, or a data analyst automating reporting." That sentence shows Studio serves both coders and non-coders. An older job posting for this role, no longer online, named the segments as engineer, citizen developer and data scientist, and set the goal to "grow the number of 'Developers' in the Aladdin Community." A citizen developer is a business user who writes some code without being a full-time engineer.

## How the pieces fit together

**Exhibit 23. Studio sits between the people who build and the system of record**

The original shows this as a layered diagram, with governance running down the side of every layer.

| Layer | What sits there |
|--------------------------------------------|--------------------------------------------------------|
| Who builds | Engineers building workflow apps; code-curious portfolio managers; data analysts automating reports; business users working in Excel |
| AI layer | Aladdin Copilot, which answers plain-English questions and calls Aladdin APIs as plugins |
| Aladdin Studio | APIs that read and write data; the Python SDK, Aladdin Compute and notebooks; Aladdin Data Cloud on Snowflake; Aladdin Tools for Excel; the Data Dictionary and Developer Portal, behind a client login |
| System of record | The Aladdin core: one shared record of holdings for portfolio management, trading, risk, compliance, operations and accounting |
| Outside inputs | The client's own models and data, plus vendor and third-party data, flowing into Data Cloud |
| Governance across all layers | Permissions, security and one data model, so what people build stays on the platform |

Here is the same thing in one minute, as a script:

> "Aladdin is the system of record for portfolios, trades, risk and accounting. Studio is how clients build on it. Data flows out through Aladdin Data Cloud on Snowflake, where it is cleaned and combined with the client's own data. Developers reach Aladdin through APIs, both request-response and event-driven. The Python SDK and notebooks make that faster for quants. Excel tools serve business users. Governance runs across all of it, so what people build stays inside Aladdin's controls. Copilot sits on top and uses those same APIs as plugins."

Dave Woodhead, Head of Aladdin Studio Engineering, gives the same picture in three pillars on Snowflake's Data Cloud podcast: Studio "exposes everything Aladdin knows how to do as a set of APIs, events. The Aladdin data cloud built on top of Snowflake takes all of that information that's generated through our analytics factory and inside of Aladdin and pushes that into Snowflake. And increasingly we're building a set of developer tools" (Confirmed).

## The pieces

**Exhibit 24. Eight pieces, from read-and-write APIs to an Excel add-in**

| Piece | What it is, in plain words |
|--------------------------------------------------|--------------------------------------------------|
| APIs | Defined ways for a program to read and write Aladdin data, including trades, orders and compliance rules. BlackRock says there are dozens, with more added often. Aladdin Graph is BlackRock's name for the API layer as a whole: every public specification is an "agraph" API, and the specs refer to naming agreed with the Aladdin Graph team. Within it, named examples include an investment research domain of five APIs (research notes, engagement, analyst coverage, watchlists and criteria) and the trade, order and compliance-rule APIs that the SDK plugins call TradeAPI, OrderAPI and ComplianceRuleAPI. |
| Event-driven APIs | Aladdin tells a program when something happens, such as a trade filling, instead of the program asking. Includes streaming and webhooks. |
| Aladdin Data Cloud | A managed data store on Snowflake. Each client gets its own copy, preloaded with cleaned Aladdin data, and can add its own and outside data. It replaced the older Aladdin Data Warehouse in 2021. |
| Aladdin Compute | A hosted space where developers run Python notebooks next to their Aladdin data |
| Aladdin SDK | An open-source Python library that handles login, retries and errors. Plugins cover trading, analytics, compliance and research. |
| Notebooks and code samples | Jupyter notebooks and code samples that come with the API guides |
| Aladdin Tools for Excel | An Excel add-in that pulls Aladdin data into spreadsheets; the low-code entry point for business users |
| Data Dictionary and Developer Portal | A guide to every data field, and the portal where documentation lives. Both sit behind a client login. |

Source: BlackRock Studio and Data Cloud pages; Aladdin SDK documentation on GitHub and PyPI.

The 11 public SDK plugin packages contain 54 API specifications covering 301 operations. They span trading, compliance, risk, operations, research and portfolio setup. That is the fullest public view of Aladdin's API surface, though it is only visible by unpacking the packages.

The specifications also show how the surface is run (Confirmed, from the public SDK plugin packages):

- Of the 54 specifications, 24 are marked alpha, 6 beta, 23 stable and 1 sunset.
- Every call carries an application-key header and OAuth scopes set per resource, so access is checked twice: once for the application and once for what the user may touch.
- Thirty-five operations are flagged as long-running, the kind that return a job to poll rather than an answer.
- A linter comment in the packages warns that a change "will break all citizen developers code," which shows that backward compatibility is enforced in code review, not only promised.
- Every public specification is tagged Access.Internal.
- The Studio resources listed in the SDK's own files include ADX, the Aladdin Data eXchange, which does not appear among the eight pieces above.

Studio APIs can change data in the system of record, not only read it. That is why governance and permissions run through everything Studio does. Jeff Miller, a BlackRock Managing Director and Global Head of Data Platform and Product Engineering, described Data Cloud's change in a Snowflake video: "We sent flat files, we sent large schema definitions, FTP and related transfers, but the Aladdin Data Cloud and Snowflake makes it much simpler for us to get our clients' data and market data from our third-party providers and Aladdin partners back to our clients and to do so in a way that is open and integrated to their bigger data estate" (Confirmed).

## Data Cloud or APIs?

| | Aladdin Data Cloud | APIs |
|--------------|-------------------------------------------|-------------------------------------------|
| Best for | Bulk analysis | Workflows |
| How it works | A data team pulls large sets of Aladdin data into Snowflake, joins it with its own data, and runs queries or models | A program reads or writes specific records, such as orders or compliance checks, often in real time |
| Typical user | Data teams and quants | Engineers building tools |

Many clients use both.

## What clients build

The Studio page groups its examples under three benefit headings: "Create & automate," "Make Aladdin your own" and "Align internally & externally."

- **Create & automate.** Setting targets and raising orders automatically, projecting future cash, and running what-if tests on live positions.
- **Make Aladdin your own.** Building custom scores that mix Aladdin analytics with the firm's own models.
- **Align internally & externally.** Preparing regulatory data and building repeatable board reports.

Common real uses include custom analytics, automated client reporting, quant research in Snowflake, and joining Aladdin data with CRM or finance systems. A 2026 job posting adds a governance goal: to "reduce off-platform development risk," meaning tools people build outside the governed system in spreadsheets or side scripts.

## How big it is

BlackRock gives few hard numbers. The one headcount it has given is internal. Dave Woodhead, Head of Aladdin Studio Engineering, said on Snowflake's Data Cloud podcast: "inside of BlackRock we have 3,000 citizen developers" and business engineers "that are interacting with all that in using Python or using R. I think that number has probably peaked," because more complex work will be done through natural language. Diwakar Goel, Global Head of Data, gave the same figure on a BlackRock pensions webinar: "we have 3,000 people who qualify in this bracket today." Neither figure counts Studio clients; both describe BlackRock's own staff. Sudhir Nair's podcast as Global Head of Aladdin gives no citizen-developer figure. An Aladdin Graph job posting from October 2026 says the APIs serve "over 200 institutions." BlackRock's 2025 Investor Day estimated that API calls will grow 17 times by 2030, against 2 times for BlackRock portfolios, 4 times for model portfolios and 1.3 times for trade allocations across BlackRock and Aladdin. The estimate sits on a slide about keeping the cost of growth low, and it gives no starting number. It still shows how central API use is to BlackRock's plan.

Woodhead also gives a sense of Data Cloud's scale: "we operate hundreds of Snowflake accounts. We share data to hundreds of Snowflake accounts and we're managing hundreds of vendors, tens of thousands of pipelines." He dates the Data Cloud conversation to "around 2019" and says BlackRock "several years ago crossed the threshold where more of our users are consuming data programmatically through R, through Python" than through Excel (Confirmed).

BlackRock has not named any outside client as building on Studio's APIs or the SDK. The nearest public statement is Royal London's chief executive crediting "the implementation of Snowflake that we did as part of the overall programme" in a BlackRock client video; he does not say Data Cloud or Studio.

## How BlackRock talks about Studio

Studio is absent from BlackRock's investor story. A count of terms across all 26 earnings calls from Q1 2020 to Q2 2026 shows this.

**Exhibit 25. "Studio" has never been named on a BlackRock earnings call**

| Term | Mentions in 26 calls | When and how |
|-----------------------|-----------------------------|------------------------------------------------|
| Studio | 0 | One line on a 2023 Investor Day slide is the only investor mention |
| Data Cloud | 2 | Q3 2022 and Q4 2024, as an add-on sold with Aladdin Enterprise |
| API | 1 | Q4 2021: "clients are really looking to use both data and APIs" |
| Copilot | 1 | Q4 2023: "investments in Aladdin AI copilots" |
| Citizen developer | 0 | Never |
| Agent | 0 | Never |

Source: Third-party transcripts of BlackRock earnings calls, Q1 2020 to Q2 2026. Zero counts are reliable; other counts are approximate (Estimate).

Studio is not absent from product leadership's story, though. In BlackRock's own winner interview after the 2023 Buy-Side Technology Awards, Kunal Khara, Global Head of Aladdin Product, named Studio as a focus for the year ahead: "What we call the Aladdin studio estate, we think is going to this year be a major, major unlock, because we're finding that more users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis at machine scale, over and above what they get through our front end applications as well" (Confirmed, BlackRock-published video, early 2024).

**Exhibit 26. When key terms first appeared in BlackRock's materials**

| Term | First seen | Where |
|-----------------------|---------------------------------------|---------------------------------------|
| Whole portfolio | March 2019 | BlackRock filing |
| Studio | Fall 2020 (Reported); February 2021 (Confirmed) | Trade press; Data Cloud launch release. Never in an SEC filing. |
| Data Cloud | February 2021 | Launch release; in the FY2021 and FY2022 10-Ks only |
| Generative AI | June 2023 | BlackRock engineering podcast |
| Copilot | December 2023 (eFront); January 2024 (Aladdin) | Trade press; Q4 2023 earnings call |
| Open, opening Aladdin | January to February 2024 | Q4 2023 call and FY2023 10-K |
| Citizen developer | November 2023 | A BlackRock speaker on the Global Insurance Report podcast: "citizen developers are what are driving these organizations today." Used again on a March 2024 BlackRock podcast and in the SDK README (May 2024). Replaced on the 2026 Studio page by "code-curious portfolio manager." |
| Multi-cloud | December 2025 | AWS joint release |
| Agents | November 2024, from a guest on a BlackRock podcast. In BlackRock's own materials: a 2025 engineering talk on Copilot's agent design and an agent skills repository for its Advisor Center tool, published September 8, 2026 | Not yet on any product page |
| MCP | 2026, in BlackRock's Forward Deploy Engineer posting | Not on any product page or filing |
| Low-code | Not found | Not on any BlackRock page, filing or public code |

The message has moved up a level. In 2020 and 2021, Studio was pitched on its own as a developer platform. By 2024 the story was openness and a wider audience. In 2026, BlackRock's top-level story is "the whole portfolio" and the "AI chapter," and Studio sits underneath as the "API-first" and "Open Innovation" layer. The 2026 Aladdin home page still lists "Explore Aladdin Studio" as a call to action. The Studio page's own calls to action are "Book a meeting" and "Download the brochure."

## What Studio's leaders say

**Exhibit 27. Public statements from the people closest to Studio**

| Person | Role | What they have said |
|---------------------------------|---------------------------------|---------------------------------|
| Richard Newman | General Manager, Aladdin Studio (January 2025) | Data Cloud "is part of Studio." Analytics once reached only through screens are becoming APIs. "Clients have been requesting more access, more openness to Aladdin content." Also: "speed to market doesn't necessarily imply better data. You still have to have the data governance." |
| Dave Woodhead | Managing Director and Head of Engineering for Aladdin Studio (Snowflake Data Cloud podcast, undated; Fivetran write-up, August 2024) | Studio "exposes everything Aladdin knows how to do as a set of APIs, events." "We are very much on a journey to what we call a whole portfolio view." On Snowflake: "So we love the partnership with Snowflake. It's a key part of our platform, but it's a part of a platform." |
| Cameron Skinner | Global Head of Solutions Engineering, Aladdin (BlackRock podcast, January 2026) | Clients have more choice "because there are APIs, because we've opened up systems over the last five years." On agents: "There are guardrails that we can put in place. There are constraints that we can apply. There's business logic now that we can code. We can't replace the judgment of the trader." |
| Diwakar Goel | Global Head of Data, Aladdin (BlackRock pensions webinar) | "Every single transaction that happens should be available and accessible to you via an event, via an API." Data Cloud is "a data integration hub" with "15 minutes of latency." Citizen developers' code must go "into GitHub in the same governance level that we check code from our software engineer," with "survivorship" when they leave. |
| Pavan Pemmaraju | Head of AI Product and Engineering (Never Done podcast, July 2026) | "The data model itself is structured for agentic use cases and we're even changing the way that we refactor the way that our products are built in order to achieve that." |
| Vedant Naik | Lead Engineer, Aladdin Studio | Plans for SDKs by domain, such as trading, risk and optimization |
| Eli Kalish | Product Manager, Aladdin Studio | Defines the audience as "professionals with financial expertise and some programming proficiency" |
| Syril Smith Garson | Head of Product for AI (Never Done podcast with Microsoft, "Humans in the loop") | "Getting to trust is going to be predominantly about transparency in the short term. So, making sure that we've got human in the loop on the vast majority of operations, particularly in regulated industries, is going to be really, really critical." |
| Kamya Somasundaram | Global Head of Aladdin Partnerships and Trading Product Marketing (BlackRock podcast, December 2025) | "There is a burgeoning community of individuals saying 'I need that in the form of an API.'" |
| Brennan Rosales and Pedro Vicente Valdez | AI engineering lead and Principal AI Engineer (LangChain Interrupt 2025 talk) | 50 to 60 teams register existing Aladdin APIs as Copilot tools. They were evaluating agent-to-agent protocols. On Copilot: "build an evaluation pipeline and make sure that we are never going to give investment advice." |

Source: BlackRock podcasts, webinars, interviews, white papers and engineering blog; Snowflake Data Cloud podcast; LangChain Interrupt 2025 talk recording. Quotations are verbatim from published transcripts or captions.

## What BlackRock is hiring for

**Exhibit 28. Recent job postings show BlackRock building out Studio's developer motion**

| Role | Req ID | Pay (New York) | What it says |
|-------------------------------|---------------------|-----------------|-------------------------------|
| Senior Product Director, Aladdin Studio Developer | R264530 | $215,000 to $275,000 | "Aladdin's extensibility layer" to "build, adapt, and run custom workflows in a governed, enterprise-ready way"; "translate internal success into client adoption" |
| Senior PMM, Technical Product Marketing (this role) | R262376 | $155,000 to $210,000 | Studio is "the next generation of extensibility within the Aladdin platform" |
| Data Platform Architect, Aladdin Data | R266304 | $215,000 to $275,000 | "Aladdin Studio, the builder ecosystem for Aladdin"; "AI and agent-based applications" |
| Forward Deploy Engineer, Aladdin Data | R264906 | Mumbai | "Model Context Protocol (MCP), AI agents, and Copilot extensions," working with client engineering teams |
| Technical Writer, Aladdin Studio | (May 2026; since removed) | New York | "Open APIs and event-driven workflows"; mentions an "Aladdin Studio Developer Portal." A Vice President version is still listed on job boards |
| Software Engineer, Aladdin Graph | R266598 | New York | "API quality and consistency at scale" for "over 200 institutions" |

Source: BlackRock careers site, postings seen on October 8, 2026. The Technical Writer posting, first posted May 7, 2026, has since been removed.

BlackRock is placing engineers with client teams to build MCP and agent connections. And the Studio Developer role is framed as turning internal use into client use, which suggests client adoption trails internal adoption.

## Where it is heading

1. **More of Aladdin exposed as APIs.** Newman and Skinner both describe opening analytics and systems that were once reachable only on screen.
2. **Data Cloud as the data hub.** eFront, Preqin and partner data flow into Data Cloud on Snowflake.
3. **APIs as agent tools.** Copilot already treats Aladdin APIs as tools that AI can call. That is the bridge from Studio to agents.
4. **Context for AI.** BlackRock's October 2026 white paper, "The Intelligence of Investing," says business context must be codified so models and agents can use it. That points to a governed data and context layer, which is Studio and Data Cloud's ground.

How data is defined, its semantics, is the groundwork for any of this; an agent that calls an API needs the fields to mean one thing. Cameron Skinner, Global Head of Solutions Engineering for Aladdin, put the limits of agents this way on a BlackRock podcast in January 2026: "There are guardrails that we can put in place. There are constraints that we can apply. There's business logic now that we can code. We can't replace the judgment of the trader" (Confirmed). On BlackRock's own Never Done podcast, Adrian Crockett, General Manager of Microsoft Cloud for Financial Services, said: "There's no copilot without plugins" (Confirmed, Microsoft Copilot episode, part 2, November 2024).

BlackRock's recent research supports the Studio argument without naming Studio. Its August 2026 insight on the topic says "Build vs buy is no longer a binary question." Its September 2026 AI adoption report is based on a survey of 303 investment firms; the figure of 68% favoring core platforms plus their own builds, cited in the earlier draft, could not be verified against the report and is Unconfirmed. The better-sourced numbers are in Exhibit 20A. The report advises firms to standardize the basics and spend engineering effort where it sets them apart.

Copilot is available to all Aladdin clients, will not give investment advice, filters content to limit made-up answers, and only shows users what they are allowed to see. A September 2026 WatersTechnology roundup reported that BlackRock has released an agent that reads investment management agreements, the long contracts that set a fund's rules (Reported). The fall 2026 Aladdin Client Forum is under way in New York and promises a first look at "where Aladdin goes next." Its announcements were not public as of October 8.

# 8. Studio's developer marketing and adoption

Studio is a mature product with an early-stage marketing motion. The SDK, Data Cloud and Copilot are all live. But almost everything a developer would want sits behind a client login, and there is little public proof of outside use.

## What is public and what is gated

**Exhibit 29. The top of Studio's developer funnel is a sales conversation, not a signup**

| Public | Behind a client login |
|--------------------------------------------------|--------------------------------------------------|
| Marketing pages on blackrock.com/aladdin | The Studio Developer Portal |
| The BlackRock Engineering blog on Medium | Full API documentation and guides |
| The open-source SDK on GitHub and PyPI, with a detailed README | The Data Dictionary and downloadable notebooks |
| Podcasts and executive talks | API tokens, Compute sessions and Data Cloud |

The public Studio page works like a brochure. Its calls to action are "Book a meeting" and "Download the brochure." The APIs page mentions developer guides and notebooks but links to none. Outside firms that tried to catalog Aladdin's APIs found they had to submit a form to see anything. For a platform sold to large institutions, gating is a reasonable choice. It does mean a curious engineer at a prospect firm cannot read the API reference.

## How far an outsider can get

A hands-on test on October 8, 2026 checked how far a developer with no client relationship could get on each platform. Each of eight criteria scored 0, 1 or 2.

**Exhibit 30. Studio scored 4 of 16 for outside developer access, level with State Street and one point behind Bloomberg**

2: Fully public or self-serve. 1: Partial or after signup or approval. 0: None or blocked. Columns: public docs; API catalog; trial or sandbox; first call as a non-client; sample code; community or marketplace; AI connector; call to action (CTA).

| Platform | Docs | Catalog | Sandbox | First call | Samples | Community | AI connector | CTA | Score |
|-----------|-----|-------|-------|-------|-------|-------|-------|-----|-------|
| Snowflake | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 16 |
| Databricks | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 16 |
| LSEG | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 12 |
| FactSet | 2 | 2 | 0 | 0 | 2 | 1 | 2 | 0 | 9 |
| Bloomberg | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 5 |
| Aladdin Studio | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 4 |
| State Street | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 4 |
| Arcesium | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 3 |
| MSCI | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| SimCorp | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Clearwater | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |

Scoring: on each criterion, 2 means fully public or self-serve, 1 means partial, limited, or open only after a free signup or an approval, and 0 means none or blocked. For the AI connector, 2 means an MCP server or connector that outside AI tools can use, 1 means one that is announced or in limited release, and 0 means none, or an assistant that works only inside the vendor's own platform.

Source: Hands-on test with no accounts, logins or payments, October 8, 2026 (Estimate). Bloomberg, Clearwater and MSCI may be underrated because some of their pages blocked automated access.

Studio's strength is openness of code. It is the only incumbent investment platform with an open-source SDK anyone can install and read, and it shows the broadest readable API surface of any incumbent. Its weakness is everything after the install. The test was blocked at step four of eight, when the SDK asked for a firm's Aladdin server address and Studio credentials.

## How rivals market to developers

**Exhibit 31. Rivals show what a public, self-serve developer surface looks like**

| Company | What it does well |
|----------------------------------------|------------------------------------------------------------|
| FactSet | A fully public developer portal with a browsable API catalog and copy-paste code samples |
| State Street | A developer portal with secured APIs, a sample-transactions onboarding API and a sandbox after approval |
| Bloomberg BQuant | A public product page, webinars and named client quant developers, with self-service inside the Terminal |
| Snowflake and Databricks | Large developer relations teams, large conferences, certifications, open-source projects, marketplaces and self-serve entry |

Source: Company developer and product pages.

Databricks shows the scale of the best case. Its 2025 Data + AI Summit drew more than 22,000 people in person and 65,000 online, and it runs a funnel where developer activity feeds sales. Against this field, Aladdin leads on proprietary data and enterprise trust but lags on public docs, self-serve trial, events, developer relations, marketplace and proof.

## The SDK in numbers

**Exhibit 32. The open-source SDK is small, still in beta and hard to install on current tools**

| Measure | Value on October 8, 2026 | Label |
|-------------------------------------|-------------------------------------|--------------------------|
| Repository created | January 3, 2024 | Confirmed |
| Stars | 69, up from about 64 in mid-July | Confirmed |
| Forks | 34, up from about 26 in mid-July | Confirmed |
| Commits | 62 in total, about 85% by one BlackRock engineer | Confirmed; share Estimate |
| People who contributed code | 7, including one from Janus Henderson and two independent developers | Confirmed |
| Issues ever filed | 1 (September 28, 2026), with no reply yet | Confirmed |
| Releases | 14 since May 2024, all alpha or beta; latest 2.0.0b10, July 27, 2026 | Confirmed |
| Installs on Python 3.13 | No. Every release pins an old Snowflake library. | Confirmed |
| Installs alongside the official MCP toolkit | No. It pins an old version of Pydantic, a common Python library. An outside fix was merged on August 11, 2026 but has not shipped. | Confirmed |
| Downloads | About 1,100 to 1,200 a month counting mirrors; lower without mirrors, and falling from July to September 2026 | Reported |
| Public packages that depend on it | 0 | Reported |

Source: GitHub and PyPI, October 8, 2026; download counters pepy.tech and pypistats.org, which count differently.

Forks are the one number rising, which suggests new teams are looking at the code. Downloads jump on release days, which points to automated installs more than new people (Estimate).

## Evidence that outside firms build on Studio

BlackRock has not named a client as building on Studio's APIs or SDK. Public code and hiring ads still show outside building, mostly around migrations.

**Exhibit 33. One firm has contributed code; several others are hiring for Data Cloud work**

| Firm | What the evidence shows | Date | Label |
|---------------------|-----------------------------|-----------------------|---------------------------|
| Janus Henderson | Two code changes merged into the Aladdin SDK from a janushenderson.com address. One lets the SDK run behind an enterprise API gateway; the other adds custom headers for Azure API keys. | December 2025 | Confirmed |
| Franklin Templeton | A staffing firm's ad for an "Aladdin Business Analyst (ADC Experience Required)" asks for hands-on Data Cloud experience and downstream integrations | October 2026 | Reported |
| Barings; Thrivent | Job search results for Data Cloud and Studio skills; postings not opened | October 2026 | Reported (low confidence) |
| SLC Management (Sun Life) | Two BlackRock podcast episodes with SLC are placed on BlackRock's own Data Cloud page, but neither episode mentions Data Cloud, Snowflake, Studio or APIs. The placement is BlackRock's editorial choice, not client evidence. | Live October 2026 | Placement only (Reported) |
| Unnamed UK firm | Spyrosoft ad, no longer online, for a senior specialist with Data Cloud and "strong hands-on experience with Aladdin APIs" | September 2026 | Reported |
| Unnamed London institution | Contract roles for a Data Cloud analyst at £650 to £795 a day and a Data Cloud QA engineer | September 2026 | Reported |
| Unnamed clients | Ads from Smart IT Frame (New Jersey), Acuity Knowledge Partners (India), Change Digital (UK), RITS (Poland) and Insight Global (US) | December 2025 to October 2026 | Reported |
| Strata FSC and EY | Delivery partners. Strata hired Data Cloud analysts (March 2026) and published a Data Cloud white paper (September 2026). | 2026 | Confirmed (Strata); Reported (EY) |

Source: GitHub; job boards and staffing firm pages; Strata FSC website; BlackRock Data Cloud page and podcast transcripts.

Several channels came up empty. No company filing on SEC EDGAR mentions "Aladdin Studio." "Aladdin Data Cloud" appears only in BlackRock's own 10-Ks. Snowflake Marketplace has no Aladdin listing. No public developer discussion of the APIs, SDK or Data Cloud turned up.

Client quotes from BNP Paribas and others talk about adopting Aladdin in general, not about what they built on Studio. Royal London's chief executive goes one step further, crediting "the implementation of Snowflake that we did as part of the overall programme" in a BlackRock client video, but without naming Data Cloud or Studio or describing what was built. The proof exists inside BlackRock, through its own citizen developers, but has not been turned into outside customer evidence. BlackRock says so itself. Kunal Khara, Global Head of Aladdin Product: "Ultimately, we eat our own cooking at BlackRock. We use Aladdin to manage the managed portfolios across the firm" (Confirmed, BlackRock-published winner interview). That is the most fixable credibility gap.

The pattern is clear even without names. Outside building clusters around migrations, such as firms moving off Charles River and rebuilding their old trading APIs and Python scripts on Aladdin. Polish and UK contractors do much of this work, and delivery partners such as Strata publish Data Cloud content.

## Community, events and content

The main event is the Aladdin Client Forum, held regionally; the 2026 forum is in New York and an APAC forum was held in 2025, but BlackRock does not publish a cadence. The job description names it as a channel this role will own for Studio. It is a relationship and thought-leadership event, not a developer conference. BlackRock's HACK:BLK hackathon is internal only, though it produced Aladdin Wealth. At industry events such as InvestOps, Aladdin shows up with booths and one-on-one meetings rather than developer talks. Technical content is thin: a few engineering blog posts, including the SDK launch by Vedant Naik and Eli Kalish, and podcasts that mostly feature executives such as Sudhir Nair, Lance Braunstein and Tarek Chouman. Engineer-led public content does exist, and he should know it: a Snowflake Summit 2024 talk, the LangChain Interrupt 2025 talk on Copilot's agent design by Brennan Rosales and Pedro Vicente Valdez, Dave Woodhead's Snowflake podcast, and a 2023 "Principles of Design" engineering podcast with Afwa Kandawire, Global Head of Aladdin Platforms, and Sue Zheng, Tech Fellow. It is thin next to what rivals publish, but it is not absent.

## Who is staffing it

BlackRock has no roles titled developer advocate or developer relations. Current Studio roles include a Technical Solutions Architect tasked with building a community of citizen developers, technical writers for the Developer Portal, a Senior Product Director for Studio Developer, a product manager for API developer experience, and this product marketing role. That hiring pattern is the clearest sign BlackRock knows the developer motion is behind and is staffing to fix it.

## How big the Studio opportunity is

BlackRock does not publish Studio revenue. A bottom-up estimate puts outside spending on Studio and Data Cloud at about $48 million a year in the middle case.

**Exhibit 34. Studio and Data Cloud are worth an estimated $10 million to $164 million a year, about 2.4% of technology revenue in the middle case**

| Client type | Aladdin clients | Share that could use Studio (low / mid / high) | Studio clients (low / mid / high) | Yearly spend, $ million (low / mid / high) |
|-------------------|----------|---------------------------|--------------------|-------------------------|
| Asset managers | 400 | 20% / 30% / 45% | 80 / 120 / 180 | 6.0 / 24.0 / 81.0 |
| Insurers | 150 | 20% / 35% / 50% | 30 / 52 / 75 | 2.2 / 10.5 / 33.8 |
| Pensions, corporates, endowments | 180 | 10% / 20% / 30% | 18 / 36 / 54 | 1.4 / 7.2 / 24.3 |
| Banks, wealth, official and other | 370 | 3% / 8% / 15% | 11 / 30 / 56 | 0.8 / 5.9 / 25.0 |
| Total | 1,100 | | 139 / 238 / 364 | 10.4 / 47.6 / 164.0 |

Source: Estimate. Client total from a November 2025 BlackRock posting that is no longer online ("1,100 Aladdin clients," Reported); segment counts from BlackRock's segment pages, with banks and others as the remainder. Spend per Studio client of $75,000, $200,000 and $450,000 a year, anchored to $20,000 per extra Aladdin user in the Texas contract and about $9,900 per user at FactSet. Builders per Studio client of 5, 15 and 30, giving about 700, 3,600 and 10,900 outside builders.

The middle case of 238 Studio clients sits close to the "over 200 institutions" BlackRock says use its APIs. Studio's own revenue is the smaller prize. On a $2 billion base, each point of retention or ACV growth is worth about $20 million a year. If Studio helps keep a few large clients or speeds multi-product deals, that is worth as much as its direct sales. That is the case a Studio marketer would make to leadership, and it needs adoption data that is not public today.

## The openings for the lead product marketer

1. **A developer portal people can see.** Public or lightly gated, with real docs, an API explorer and quick-start guides, measured against FactSet's and LSEG's portals. A 2026 BlackRock posting already names a coming Studio Developer Portal.
2. **Named client build stories.** Start with Janus Henderson and the existing citizen-developer base, and with internal BlackRock teams where approval allows.
3. **A general release of the SDK.** It has been in beta for over two years and does not install on current Python. A full release, once engineering fixes these gaps, is a natural launch moment.
4. **Studio as the way AI agents reach Aladdin.** Seven firms, including FactSet, LSEG and MSCI, now offer connectors that let outside AI tools pull their data. BlackRock's Forward Deploy Engineer posting already mentions MCP. One story could tie together the APIs, SDK, Data Cloud and Copilot.
5. **Migrations as the entry point.** Outside building clusters around migrations. Delivery partners such as Strata and EY can carry the Studio story into those projects.
6. **A developer community.** A developer track at the Client Forum or a Studio developer day, client hackathons modeled on HACK:BLK, and a light community function built from the Solutions Architect role.

## How success would be measured

Success would be measured by use: SDK downloads, active API tokens, Compute usage, time to a first successful API call, client-built apps in production, and pipeline influenced by developer activity. Commercial measures would track Studio's effect on ACV expansion and renewals. If adoption stalls at onboarding, effort shifts from events to self-serve help. If it stalls at awareness, effort shifts to the portal and community.

# Part 2. Third Round: Product Manager Interviews

9. How the third round works
10. Technical depth
11. Knowledge of the customers
12. Fit with a large, regulated company
13. Working with product managers

# 9. How the third round works

The third round is three 30-minute interviews, each with a different Aladdin Studio product manager. The same approach works in all three: show that he learns a technical platform accurately, keeps claims honest about what is live, and treats the PM as the owner of the product.

Each conversation leaves time for about four or five questions. Each PM will likely test one or two of four concerns, covered in chapters 10 to 13.

| Chapter | Concern | What the PM is asking |
|----------------|--------------------------------------|-----------------------------------------------|
| 10 | Technical depth | Can he talk to engineers without slowing them down, and describe the platform accurately? |
| 11 | Knowledge of the customers | Does he know how a portfolio manager, risk analyst or operations lead spends the day? |
| 12 | Fit with a large company | Will he work through review cycles, compliance and many stakeholders, not around them? |
| 13 | Working with PMs (main focus) | Will he make the PM's job easier or harder? |

## How to answer

Prepare one main story and one backup story for each concern. Keep answers to about two minutes, in four parts:

1. **Situation.** One sentence. Name the product and the audience.
2. **What he did.** The decision he made or drove, and who was involved.
3. **Result.** A number: pipeline, expansion, deals won or hours saved.
4. **At BlackRock.** What he would do the same way on Studio.

In the second round he spoke about launches too generally. Every story should name the product, the audience, the decision and the number.

He should use a different lead story in each PM conversation where one fits, because the three PMs may compare notes. A workable split is BitcoinComputer.io for technical depth, Mursion healthcare for customer knowledge, NovoEd as a Fidelity company for large-company fit, and the NovoEd AI translation launch for working with PMs.

## The story bank

The same handful of stories covers every concern across both rounds.

**Exhibit 35. Fifteen stories, mapped to the concerns each one answers**

● main story for that concern; ○ backup or supporting story

| Story | Technical depth | Customers | Large-company fit | Working with PMs | Final round |
|-------------------------------|---------------|----------|-----------------|----------------|-----------|
| NovoEd AI translation launch: tiering, a held-back use case, $1M+ expansion | | | ○ | ● | ● |
| NovoEd as a Fidelity company: long cycles, regulated buyers, checked claims | | | ● | | ○ |
| NovoEd vertical positioning: four verticals, 12 to 24 month cycles | | ● | | | ○ |
| NovoEd AI claims discipline: optional AI, no training on client data | | | ○ | | |
| NovoEd sales enablement: NetApp, Delta, Marriott wins; 15 references | | | | ○ | |
| Cascade Insights research: 127-participant value and ROI study | | ○ | | | |
| BitcoinComputer.io: architecture for three audiences, 34 protocols, regulatory review | ● | | ○ | | |
| Mosaic Chello positioning and talk track: live versus roadmap labels | ○ | | | ○ | |
| Mosaic segmentation playbook: 13 sub-industries | | ○ | | | |
| Mosaic CEO partnership: working with a senior decision owner | | | | ○ | |
| Mursion healthcare go-to-market: new market from scratch; Duke University Health System | | ○ | | | ● |
| Mursion original research: 300 learning leaders; Harvard Business Review | | | | ○ | |
| Claude workflow on Gong and Salesforce: case studies from 50 hours to 5 | ○ | ○ | | | |
| Family office venture fund: how investors evaluate deals and use data | | | | | ○ |

# 10. Technical depth

The PMs want to know whether he can talk to engineers without slowing them down, and whether he will describe the platform accurately. He has not been an engineer, so his proof has to be that he has learned technical platforms before and explained them correctly.

A product marketer who overstates an API, or mixes up the data layer and the developer tools, creates work for the PM. The job posting asks for "deep comfort engaging with technical concepts (APIs, data workflows, platform architecture, AI capabilities)." The one-minute explanation in chapter 7 is the version to say out loud.

## Likely questions

1. "Explain Aladdin Studio to a portfolio manager in two sentences."
2. "What is the difference between Aladdin Data Cloud and the APIs? When would a client use each?"
3. "How would you explain event-driven APIs to a business buyer?"
4. "How would you market to a developer differently than to a COO?"
5. "How do you get up to speed on a technical product? What do you do in your first 30 days?"
6. "How would you talk about Copilot or agents without overpromising?"
7. "What is a technical concept you got wrong once, and how did you find out?"

## What strong answers contain

**Data Cloud versus APIs.** "Data Cloud is for bulk analysis. A data team pulls large sets of Aladdin data into Snowflake, joins it with their own data, and runs queries or models. APIs are for workflows. A program reads or writes specific records, like orders or compliance checks, often in real time. Many clients use both." Then add: "I would check this framing with you before using it externally."

**Developer versus COO.** Developers want docs, sample code and a fast first working call. A COO wants fewer side-built tools, less operational risk and faster reporting. The Studio page speaks to both, with its lines about repeatable board reports and regulatory data.

**Getting up to speed.** Give a real plan. Read the docs and API guides. Sit in on engineering standups and demos. Run a sample notebook himself. Write a one-page explainer and have a PM and an engineer mark it up. Keep a glossary.

**Copilot and agents.** Say only what is live. Copilot is available to all clients, stays inside platform permissions and gives no investment advice. Anything about autonomous agents beyond what BlackRock has shown is direction, not product. He can add that rivals such as FactSet, LSEG and MSCI now let outside AI tools pull their data, and ask how the PM sees Studio's role there.

## Stories to use

**Main story: BitcoinComputer.io.** He has an ongoing consulting engagement with BitcoinComputer.io, a pre-revenue Bitcoin smart-contract platform, where his role is [Fill in: his role, in his resume's wording]. He translated the architecture into stories for developers, investors and regulators, narrowed the platform to four use cases, and benchmarked 34 competing protocols. [Fill in: one result.]

> "I had to learn a smart-contract architecture well enough that developers would not roll their eyes, and then explain the same thing to regulators. I narrowed it to four use cases so each audience heard one clear story. Benchmarking 34 protocols forced me to understand what was truly different."

**Backup story: Mosaic AI positioning.** He owned positioning for an AI resource-management agent and an AI planning assistant called Chello. He turned technical capabilities into role-specific stories for operations, resource-management and executive buyers. That maps to Studio's mix of engineers, code-curious portfolio managers and analysts.

**Feedonomics is not a technical story.** His title there was Growth Engineer, but the job was inbound sales development, reporting into marketing. If it comes up, he should describe it that way.

**AI fluency: Claude on Gong and Salesforce.** He built a Claude workflow across Gong and Salesforce that mined sales calls for positioning angles, objections and proof points. It cut case-study production from about 50 hours to 5. The job posting asks for someone who will use generative AI to scale content, insights and competitive intelligence, so this is direct evidence.

He should not claim to code. He can say: "I am not an engineer. I learn fast, I check my work with engineers, and I don't publish a technical claim the PM hasn't reviewed."

# 11. Knowledge of the customers

He has sold to financial services and regulated buyers at NovoEd, but he has not worked inside investment management. The PMs will worry that without knowing how a portfolio manager, risk analyst or operations lead spends the day, his messaging will be generic.

The posting asks him to lead market, customer and competitive insights that shape positioning, target segments and whitespace. Part 1 covers segments, named clients, pricing and competitors. One gap matters here: BlackRock has not named any client as building on Studio's APIs or SDK. Asking the PMs which Studio references they can share is a good question in itself.

## A plain-language primer

| Term | Meaning |
|-----------------------------|-----------------------------------------------------------------------|
| Asset manager | A firm that invests money for others, such as a mutual fund or ETF provider. It earns fees on the assets it manages. |
| Asset owner | An organization that owns the money and its obligations: a pension fund, insurer, endowment or corporate treasury |
| Wealth manager | A firm whose advisors invest for individuals and families |
| Bank | Holds large portfolios of its own and manages rate and liquidity risk. Key measures are net interest income (NII), economic value of equity (EVE), hedge effectiveness, and CCAR, the Fed's yearly capital stress test. |
| Public markets | Stocks and bonds traded on exchanges |
| Private markets | Private equity, private credit, real estate and infrastructure. "Whole portfolio" is BlackRock's term for seeing public and private together. |

**Exhibit 36. Seven steps run from the front office to the back, all on one record in Aladdin**

| Step | What happens |
|--------------------------------------------------|--------------------------------------------------|
| 1. Research and portfolio management | Portfolio managers decide what to own, set targets, test changes and check exposures |
| 2. Trading | Traders turn decisions into orders. Compliance rules are checked first, such as a cap on how much of one issuer a fund can hold. |
| 3. Risk | Risk teams measure how the portfolio could lose money, using stress tests and risk factors: things that move prices, such as interest rates |
| 4. Operations | Teams settle trades, reconcile positions with custodians so two records agree, and manage cash |
| 5. Accounting and data | The IBOR is the live view of positions for decisions. The ABOR is the official books used for reporting and net asset value, a fund's value per share. |
| 6. Reporting | Firms report to clients, boards and regulators, often needing an "as-was" view of exposure on a past date |
| 7. Model risk | Firms that rely on models must test that the models work and are used correctly |

## What Studio solves for these buyers

Buyers want three things. They want to stop copying Aladdin data into side spreadsheets. They want to combine Aladdin data with their own and vendor data. And they want to build tools that set them apart without losing governance. These match the three benefit headings on the Studio page: "Create & automate," "Make Aladdin your own" and "Align internally & externally."

The main alternative is building in-house on Snowflake or Databricks. Data Cloud's pitch is that Aladdin data arrives already cleaned and mapped, with Aladdin's controls. Because Data Cloud runs on Snowflake, Snowflake is often a partner rather than only an alternative.

LACERA's 2020 decision shows what is at stake. It turned Aladdin down partly because choosing it would have meant hiring an analyst to load and reconcile private assets data. That is exactly the work Studio and Data Cloud now aim to remove.

## A segment to test: NAV loan monitoring for bank fund finance teams

He has sketched a demo that points Studio at bank fund finance. The evidence supports the problem but not yet the product fit, and it points to a different first buyer than bank model risk teams.

Fund finance means bank loans to investment funds. A subscription line is backed by investors' promises to put in more money. A NAV loan is backed by the value of the fund's holdings.

**Exhibit 37. The fund finance problem is real, but routine loan checks may fall outside model risk rules**

| Claim | Evidence | Effect on the idea | Label |
|-------------------------|-------------------------|-------------------------|-------------------------|
| The market is large and bank-heavy | Fund Finance Association 2025 Industry Survey, published June 2026: it tallied at least $1.1 trillion in subscription line commitments and estimated the total at $1.4 trillion to $1.75 trillion, with $1.5 trillion as its best estimate. Banks with over $1 trillion in assets hold nearly $800 billion. Over 60% of lenders also offer NAV or hybrid loans. | Supports | Confirmed |
| NAV lending is growing and getting harder | Haynes Boone 2026 survey: 72% expect NAV growth in 2026; NAV facilities in workout or default rose from 2% to 4% of respondents | Supports | Confirmed |
| Supervisors now stress-test it | Bank of England, July 2026: its bank stress test "included stress on fund finance" | Supports strongly | Confirmed |
| Data on this lending is poor | Federal Reserve note, May 2025: disclosures by private credit vehicles "are generally not available" | Supports | Confirmed |
| BlackRock already sells to this buyer | Preqin's banks page offers data to "supercharge your fund finance team," covering subscription and NAV financing | Supports strongly | Confirmed |
| Large banks already use Aladdin | BlackRock says 11 large banks, at category 4 size or above, use Aladdin | Supports a foothold | Confirmed |
| Model risk rules cover vendor models | SR 26-2, issued April 17, 2026, says banks should understand a vendor model's design, data and performance and monitor outcomes | Supports | Confirmed |
| Aladdin for banks covers lending | BlackRock's banks page covers the bank's own securities book, not lending or fund finance | Weakens | Confirmed |
| Any bank uses Aladdin, eFront or Studio for fund finance | None found | Weakens | Not found |
| Routine loan checks count as models | SR 26-2 excludes "deterministic rule-based processes." A subscription line borrowing base is mostly advance rates times eligible commitments, so it may not count as a model. | Weakens | Confirmed; reading of borrowing base Estimate |
| AI tools are in scope | SR 26-2 places generative and agentic AI models outside its scope | Weakens a Copilot-led pitch | Confirmed |
| The field is open | Allvue and Cardo AI already sell borrowing base and exposure tools to bank lenders | Weakens | Confirmed |
| BlackRock is neutral | BlackRock's HPS unit lends to funds itself | Mixed: deep product knowledge, but it competes with the banks | Confirmed |

Source: Fund Finance Association; Haynes Boone; Bank of England Financial Stability Report, July 2026; Federal Reserve FEDS Note, May 2025; Preqin; BlackRock; Federal Reserve SR 26-2 and attachment.

SR 26-2, issued alongside OCC Bulletin 2026-13 and FDIC FIL-15-2026, replaced SR 11-7 and SR 21-8. It is most relevant to banks with over $30 billion in assets, and it is guidance, not binding rules. Any script that cites SR 11-7 needs updating.

Model risk teams are a weak first buyer, because routine subscription line checks are likely rule-based and outside SR 26-2. The stronger fit is the bank's fund finance credit and portfolio team, with model risk as a second reviewer. The best use case is NAV loans and stress testing, where valuation haircuts and loss estimates are real models. There, Studio could join Preqin fund data, eFront private holdings and the bank's own loan data in Data Cloud, and give model validators the data trail SR 26-2 asks for (Estimate).

He could put it this way: "Preqin already sells to bank fund finance desks. I'd want to learn whether Studio and Data Cloud can turn that data relationship into a workflow, starting with NAV loan monitoring. I don't know yet if it's a fit, and I'd test it with you and sales first."

## Likely questions

1. "Who do you think the main buyer of Studio is, and who is the main user?"
2. "Walk me through how a portfolio manager's day might use Studio."
3. "How is selling to a bank different from selling to an asset manager?"
4. "Why would a client pick Studio over building on Snowflake or Databricks themselves?"
5. "How would you find out what customers need if you can't talk to them directly?"
6. "What segment do you think we're under-serving?"

## Stories to use

**Main story: NovoEd vertical positioning.** He built vertical positioning for financial services, energy, manufacturing and hospitality, and sold to regulated buyers through 12 to 24 month sales cycles. The lesson: the buyer, the budget and the use case change by vertical even when the product stays the same. Studio has the same shape. A pension, a bank and a wealth manager use the same platform for different reasons.

**Customer research: Cascade Insights.** At NovoEd he built a customer value and ROI framework from a 127-participant study with Cascade Insights. At Studio he would do the same with value engineering and sales: interview users and buyers, then turn the findings into a value framework the PMs can check.

**Segmentation: Mosaic.** He built a 13-sub-industry segmentation playbook for architecture and engineering firms. [Fill in: one result.] Here he would break "financial institutions" into segments by workflow and buying center, not just firm type.

**New market: Mursion healthcare.** He built Mursion's healthcare go-to-market from scratch and landed Duke University Health System. [Fill in: one result, such as revenue or accounts won.]

**Sales-call mining.** His Claude workflow found objections and proof points in real sales calls. At BlackRock this would need approval for tools and data access, and he should say so before the PM does.

He can close honestly: "I haven't worked inside an asset manager. I know the lifecycle from front office to back office. My plan is to sit with Aladdin users and the client teams in my first weeks and test my understanding against yours."

# 12. Fit with a large, regulated company

His recent work was at small companies, where he was often the only marketer and owned everything. The PMs will wonder whether he will get frustrated by review cycles, go around process to move fast, or forget that the PM, compliance, legal and sales all have a say. The four-day office rule also signals that BlackRock values in-person teamwork.

## How BlackRock says it works

BlackRock lists five principles in its annual report and proxy:

1. **We are a fiduciary to our clients.** A fiduciary is legally bound to act in the client's best interest.
2. **We are One BlackRock.** BlackRock explains this as working together without silos and without turf.
3. **We are passionate about performance.**
4. **We take emotional ownership.**
5. **We are committed to a better future.**

The job posting describes a founder-led culture. It says the four-day office rule supports collaboration, apprenticeship and faster onboarding.

## Where the role sits

The posting calls the role "a senior individual contributor / lead PMM" and "the primary marketing partner to Studio Product," sitting between product, engineering and go-to-market. He will likely have no direct reports and will lead through influence.

**Exhibit 38. Aladdin leaders named in public sources**

| Name | Role | Area | Dated as of |
|---------------|------------------------------|--------------------------|------------------------------|
| Sudhir Nair | Global Head of Aladdin | Aladdin overall | December 2025 |
| Tarek Chouman | Global Head of the Aladdin Client Business | Clients | October 2026 |
| Kunal Khara | Global Head of Aladdin Product | Product | October 2026 |
| Richard Newman | General Manager, Aladdin Studio | Studio | January 2025 |
| Dave Woodhead | Head of Aladdin Studio Engineering (Fivetran write-up); "managing director and head of engineering for Aladdin Studio" (Snowflake Data Cloud podcast) | Studio engineering | August 2024; podcast undated |
| Diwakar Goel | Global Head of Data, Aladdin | Data, next to Data Cloud | October 2026 |
| Pavan Pemmaraju | Head of AI Product and Engineering | Copilot and agents | July 2026 (podcast); October 2026 |
| Syril Smith Garson | Head of Product for AI | AI product | November 2024; current role unverified |
| Cameron Skinner | Global Head of Solutions Engineering, Aladdin | Solutions engineering | January to February 2026 |
| Lance Braunstein | Head of Aladdin Engineering | Engineering | October 2024 |
| Kamya Somasundaram | Global Head of Aladdin Partnerships and Trading Product Marketing | Product marketing; a likely peer | December 2025 to January 2026 |
| Pia Schaefer | Global Head of Value Engineering for the Aladdin Client Business | Value and ROI | July 2025 (BlackRock podcast) |
| Drew Ellis | Head of Partnerships for Aladdin | Partnerships | Undated |
| Ted Stratigos | Global Head of Aladdin Wealth Tech | Wealth | October 2025 (press release) |
| Vedant Naik | Lead Engineer, Aladdin Studio | SDK | July 2026 |
| Eli Kalish | Product Manager, Aladdin Studio | Studio product | May 2024; current title unverified |

Source: BlackRock press releases, white papers, podcasts and engineering blog. Titles may lag. Priyanka Singh (commercial and go-to-market strategy for Studio) and Vijay Kasi (head of Studio sales) are known from his own interviews and did not appear in public sources. There is no public org chart.

## Marketing compliance in plain language

BlackRock is an asset manager, but Aladdin is a technology product, and the rules differ. FINRA Rule 2210 covers broker-dealer communications. They must be fair and balanced, cannot make exaggerated or promissory claims, and need a sound basis for every claim. The SEC Marketing Rule covers registered investment advisers and bars material claims the adviser cannot back up on demand. Compliance guides say AI claims must be provable too. BlackRock has entities under both.

It is not clear which rules formally apply to Aladdin's technology marketing. The Studio page shows how carefully BlackRock treats it anyway: institutional and professional clients only, not investment advice, and features may change or end without notice, with legal language country by country.

In daily work, this means:

- Every external asset goes through compliance and legal review: web pages, decks, white papers, event talks and social posts.
- Claims about performance, AI, data security, or anything that sounds like investment advice get the most scrutiny.
- Global assets need regional checks.
- Review time belongs in every launch plan from the start.

One BlackRock example to point to: the Aladdin Wealth Auto Commentary rollout, announced in October 2025 with Morgan Stanley as the first user. An AI feature that writes client-facing text is the kind of launch that has to satisfy risk, legal, information security and model governance reviewers before it ships, and whose impact shows up only when advisors adopt it. He should describe it in those terms, as his own reading of the launch, rather than attributing the point to a BlackRock executive.

## How decisions get made

At large firms, more people are consulted. Proposals are written and sent ahead. Launches are tied to release schedules and events such as the Client Forum. The skill that matters is getting the right people aligned early so reviews go quickly later. Interviewers usually look for five signs in startup candidates:

1. He has worked through a review process, not around it.
2. He brings people in early and does not surprise them.
3. He understands why the controls exist. Here they protect clients and BlackRock's fiduciary duty.
4. He keeps urgency and momentum inside the process.
5. He does not talk down about big companies.

## Likely questions

1. "You've been at small companies. How will you handle slower review cycles?"
2. "Tell me about a time you had to get many stakeholders aligned."
3. "What would you do if compliance blocked a claim you thought was key?"
4. "How do you keep a launch moving when you don't control every input?"
5. "How do you feel about four days a week in the office?"

## Stories to use

**Main story: NovoEd, a Fidelity company.** His best proof. NovoEd was owned by Fidelity, a large regulated financial firm, and its sales cycles ran 12 to 24 months.

> "NovoEd was a Fidelity company. I worked with long enterprise cycles and regulated buyers. I'm used to claims being checked."

**Stakeholders: the AI translation launch.** He co-led the launch with Sales and Customer Success. The feature only helped customers running large multilingual global programs. He and the head of Sales agreed not to lead with it for new business and sold it as an expansion instead. It took several conversations and some internal disagreement. Tell it as reaching agreement through discussion, not winning an argument. Use it here only if he has not already told it to another PM.

**Claims discipline: NovoEd AI messaging.** He made AI features optional in messaging, with a clear statement that NovoEd was not building its own models and would never train on client data. That is the same instinct as Copilot's "will not give investment advice" line.

> "I've written AI messaging that put client trust first. I'd expect compliance to sharpen that here, and I'd welcome it."

**Regulation: BitcoinComputer.io.** He worked through a federal and 50-state regulatory review and let regulation shape the story.

**On pace.**

> "At a startup I moved fast because I owned everything. Here I'd move fast by planning review time in from day one and getting compliance and the PM early drafts."

**On the office.** He already commutes into the city and told the recruiter the schedule is no problem.

> "Four days in the office suits this role. Most of my job is talking with PMs, engineers and sales. That is easier in person."

# 13. Working with product managers

This is the main focus of the third round. Each PM is asking one question: will this person make my job easier or harder?

PMs commonly fear that a product marketer will try to set the roadmap, promise features that are not built, show up late to a launch, or treat the PM as a source of facts rather than a partner. The posting says he must partner closely with Product to align messaging with roadmap priorities and technical design.

## What good collaboration looks like

| The PM owns product decisions | The product marketer owns market decisions |
|---------------------------------------------|-------------------------------------------------------|
| Priorities, specs, what gets built and when | Positioning, target segments, messaging, launch plans and sales enablement |

Both talk to customers and study usage data.

**Exhibit 39. Sizing launches by impact sets expectations early**

| Tier | Type | What it gets |
|------------------|----------------------------|------------------------------------------------------|
| Tier 1 | Major launch | Full campaign, press, events and sales training. |
| Tier 2 | Significant feature | Focused marketing to the segments it serves |
| Tier 3 | Small update | Release notes and a support brief |

Sources differ on who sets the tier. He should propose a method and agree it with the PMs rather than impose it.

**Customer and market input.** He brings win-loss findings, competitor moves, sales objections and segment data as input to the PM's decisions, not as demands.

**Messaging.** He drafts. The PM checks accuracy. Engineering checks technical claims. Compliance checks the final version. Labeling what is live and what is on the roadmap prevents most problems.

**Feedback loops.** He collects what sales and client teams hear, sorts it, and passes clear patterns to the PMs on a regular schedule.

**Disagreements.** He raises them early and in private, brings evidence, accepts the call of whoever owns the decision, and then commits fully.

## What is specific to Aladdin

The role sits within Aladdin Product. Studio PMs and engineers already write developer content together; Eli Kalish co-wrote the SDK blog post with an engineer. He can offer to help with that kind of content rather than take it over. Many teams across Aladdin contribute to shared surfaces such as Copilot plugins, so Studio messaging will touch other product teams. Adoption matters as much as launch, and BlackRock is itself a heavy Studio user. Internal use cases may be a rich source of proof points, subject to approval.

## Likely questions and what strong answers contain

| Question | What a strong answer contains |
|--------------------------------------------------|--------------------------------------------------|
| "How do you like to work with a PM day to day?" | A rhythm: a weekly sync, a shared launch tracker, early access to specs and a quick review loop for messaging. What he will bring each week: customer insight, sales feedback and competitor moves. |
| "Tell me about a time you disagreed with a PM or product leader." | Evidence, a private conversation, a clear decision owner and commitment after the decision |
| "How do you decide how big a launch should be?" | Tiers, the criteria (customer impact, revenue impact and how new it is) and agreement with the PM |
| "How would you handle a feature that slips after you've started marketing it?" | Roadmap items labeled with a quarter, external claims kept to what is live, and a plan for telling sales |
| "What do you need from me to do your job well?" | Early access, honest timelines and one source of truth on what is live. Not control of the roadmap. |
| "How would you bring customer feedback to us without it becoming a feature request list?" | Group feedback by problem and segment, rank it by frequency and deal impact, and leave the decision to the PM |
| "What would your first 90 days look like?" | Learning first, then a positioning draft tested with PMs, then one launch run end to end |

## Stories to use

**Main story: the NovoEd AI translation launch.** One story that answers launch sizing, honest claims, sales alignment and disagreement.

| Part | Content |
|-------------------------|---------------------------------------------------------------------------|
| Situation | NovoEd was launching AI language translation. The feature only delivered value to customers running large multilingual global programs. |
| What he did | Co-led with Sales and Customer Success; owned positioning, enablement and go-to-market. Agreed with the head of Sales to sell it as an expansion, not a new-business lead. Positioned it against outside translation vendors. Held back the cross-language group-learning use case until learner-post translation shipped, so customer success would not inherit an overpromise. |
| Result | CEMEX and Marriott alone expanded by more than $1 million. |
| At BlackRock | "I sized the launch to where the value really was. I held back a use case until the product supported it. That's how I'd treat Studio features with a PM." |

**Backup story: the Mosaic Chello talk track.** He wrote a talk track for business development reps, the people who book first meetings. It told reps to lead with the planning problem rather than the AI, labeled each capability as live or roadmap with a quarter, and set a naming rule separating the product from the AI assistant. [Fill in: one result.] Naming matters at Aladdin too, since the brand covers Studio, Data Cloud, Copilot, Wealth, eFront and Preqin.

> "Labeling live versus roadmap with a quarter is the simplest way I know to protect a PM's roadmap from sales overpromising."

**Partnership: Mosaic CEO.** He worked directly with the CEO on positioning, which shows he can work with a senior decision owner and accept their call. [Fill in: one result.]

**Sales enablement: NovoEd.** He built a differentiators deck and a map linking each feature to the value it delivers. Enablement supported wins with NetApp, Delta and Marriott and expansions within Centene and 3M. He built a reference program across about 15 enterprise customers and a partnership with Marriott's global head of leadership development, covering case studies, webinars and conference talks. That partnership influenced dozens of deals and helped land Delta Air Lines.

**Thought leadership: Mursion research.** His original research with 300 learning leaders became the basis of a Harvard Business Review article and was cited by Deloitte. The posting asks for thought leadership that positions Studio as a leading extensible, AI-enabled platform.

## Questions to ask the PMs

Pick two or three for each conversation, and avoid repeating the same ones across the three PMs.

1. "What does a great launch look like on your team? What went wrong on the last one?"
2. "How do you decide what is ready to talk about externally?"
3. "Most of the outside hiring I found for the Aladdin APIs and Data Cloud is tied to migrations, like Janus Henderson moving off Charles River. Is a migration the main moment clients start building on Studio?"
4. "I couldn't find a client publicly named as building on Studio's APIs or SDK. Which clients would you be comfortable featuring, and what usually stops a client from going public?"
5. "The Technical Writer posting mentions a Studio Developer Portal. What will a non-client be able to see there?"
6. "The SDK has been in beta since 2024 and doesn't install on Python 3.13 yet. Is a general release planned, and would you want marketing behind it?"
7. "FactSet, LSEG and MSCI now let outside AI tools pull their data, and your Forward Deploy Engineer posting mentions MCP. How will clients connect their own AI agents to Aladdin, and where does Studio fit?"
8. "A 2024 posting said Studio has free and premium capabilities. How do clients move from free to paid, and where does that usually stall?"
9. "Which internal BlackRock builds would make the best client stories, and what approvals would we need to use them?"
10. "What did the Client Forum show about Studio's role, and what is ready to talk about externally?"
11. "Where do you get customer feedback now, and what is missing?"
12. "What would you want from me in the first 30 days?"

# Part 3. Final Round: Managing Director

14. How the final round works
15. Motivation and fit
16. Understanding of the business and strategy
17. Operating at the VP level
18. Closing the final round

# 14. How the final round works

If the product manager interviews go well, the final round is with the Managing Director. The director is mostly deciding one thing: can Jacob be the single person who owns how Aladdin Studio is explained and sold, with specific proof instead of general claims. His best position is the person who takes a broad technical product to new kinds of buyers, with one named example and one number behind every answer.

## The format

Candidate reports describe BlackRock VP interviews as mostly behavioral, in a situation-action-result format, with the final round often led by a manager two levels up.

| Anchor story | What it shows | Best source |
|---------------------------|------------------------------------|------------------------------------|
| A new-vertical launch | He can take a product to a new buyer | Mursion healthcare and Duke University Health System |
| Influence without authority | He can get senior people he does not manage to agree | [Fill in: a story other than the NovoEd translation launch, which is his launch walkthrough] |
| Pushback | He disagrees with evidence and respect | [Fill in: a specific case] |

Answers should run 90 seconds to two minutes: the answer first, then the example, then the result. Placeholders marked [Fill in] are spots where a real name, date or number from his own experience will make the answer land. An honest range is better than a number he cannot explain under follow-up.

## Facts to have ready

**Exhibit 40. Facts to have ready for the Managing Director**

| Topic | Fact | Label |
|------------------------------|-----------------------------------|-----------------------------------|
| BlackRock scale | A record $15.3 trillion in assets at June 30, 2026 | Confirmed |
| 2030 plan | More than $35 billion in revenue, 30% or more from private markets and technology, and $400 billion raised in private markets | Confirmed |
| Recent acquisitions | Global Infrastructure Partners, Preqin (closed March 2025) and HPS Investment Partners (closed July 1, 2025) | Confirmed |
| First whole-portfolio deal | Signed in Q3 2025, covering Aladdin, eFront and Preqin together | Confirmed |
| Technology results | Q2 2026 technology revenue of $566 million, up 13%; ACV up 15% | Confirmed |
| Growth target | CFO Martin Small, July 15, 2026: committed to low to mid-teens ACV growth over the long term | Confirmed |
| Revenue floor | About $1.3 billion a year in fixed minimum fees on current contracts | Confirmed |
| Account growth | JPMorgan's Aladdin payments rose from $4.4 million (2017) to $25.6 million (2025) | Confirmed |
| Studio in investor materials | Never named on an earnings call from 2020 to mid-2026. The only public growth figure is a 2030 estimate of 17 times more API calls, against 2 times for BlackRock portfolios, with no base | Confirmed |
| What leadership says | Larry Fink's 2026 letter: Aladdin sits at the core of how BlackRock scales; Preqin tripled Aladdin's desktop reach. The "language of the portfolio" phrase is Dave Woodhead's, on Snowflake's podcast ("a single symbology, a single language, the language of the portfolio"), and the Aladdin Client Forum 2026 opener says "we built a common language for portfolios." Cite those, not the letter, for the phrase. | Confirmed (letter, per the author's source); phrase sources Confirmed |
| Studio as a leadership priority | Kunal Khara, Global Head of Aladdin Product, in BlackRock's winner interview after the 2023 awards: "the Aladdin studio estate, we think is going to this year be a major, major unlock" because users want to work "on a programmatic basis at machine scale" | Confirmed |
| Private credit | Private credit is becoming a core part of portfolios while its data remains fragmented; this is the author's framing. BlackRock's product response: private credit analytics added in May 2026, and "Preqin indices are also available today in Aladdin Explore and our Aladdin data cloud" (BlackRock webinar, September 2025). | Confirmed (product facts); framing is the author's |
| BlackRock's own research | AI Adoption Report 2026, a global survey of 303 investment firms (September 2026). The figure "68% favor core platforms plus their own builds" could not be verified against the report and should not be quoted until checked. | Unconfirmed (the 68%) |
| Build vs buy evidence | BlackRock's Build vs Buy webinar poll: mostly vendor 37%, hybrid 30%, actively re-evaluating 18%, mostly in-house 15%; "60 to 70%" of a tech organisation "keeping the lights on"; firms most want to stop maintaining compliance reporting (53%) | Confirmed (BlackRock Build vs Buy webinar replay) |
| 2026 partnerships | Deutsche Bank HausFX (February), Apex Group (March), iCapital with Aladdin Wealth (March), Adroit Trading (September), Danske Bank's Butterfly on Aladdin Wealth (September) | Confirmed |
| The role | Requisition R262376; senior individual contributor and lead PMM for Studio; $155,000 to $210,000 plus bonus; four days a week in the New York office | Confirmed |

## Status checks before the interview

| Item | Status on October 8, 2026 |
|-----------------------------------------|-----------------------------------------------------------|
| Q3 2026 earnings | Out on October 14, 2026, before the market opens, with a call at 7:30 a.m. Eastern. Read the release that morning if the interview is later. |
| Aladdin Client Forum | Under way in New York in October. No announcements public yet. |
| Aladdin on AWS | No general availability announced. The target was the second half of 2026. |
| EU critical provider list | BlackRock is not on the November 2025 list of 19 critical tech providers under the EU's DORA rules. Bloomberg, LSEG and FIS are. The list is due for an update around November 2026. |
| Model risk guidance | SR 26-2 replaced SR 11-7 on April 17, 2026. It excludes generative and agentic AI and simple rule-based calculations. |

# 15. Motivation and fit

The motivation questions test whether his reasons are tied to the business rather than the brand, and whether this move makes sense for his career.

## "Why BlackRock?"

Testing: a reason tied to the business, and a sense that he would stay.

- **Start with the point.** BlackRock is one of very few firms that is both a huge investor and a technology company selling its own platform. The people who built the product test it every day.
- **Connect it to his experience.** He has spent his career at startups trying to earn trust for new platforms. At BlackRock the trust already exists. The work is helping more types of clients use what is there.
- **Mention the 2030 goal.** Aladdin is central to it, so product marketing for Aladdin sits near the center of the firm's plan.
- **Close with a personal line.** [Fill in: one honest personal reason, for example what the family office venture fund taught him about how investors use tools and data.]

## "Why Aladdin?" and "Why Aladdin Studio?"

Testing: whether he sees Studio as strategic or as a technical add-on.

- Aladdin already has a strong position with large investment firms. Studio is how it grows further inside those accounts, because it lets each client build what Aladdin does not do out of the box.
- Studio has more than one buyer: the engineer, the code-curious portfolio manager and the data analyst. That is the problem he likes most: one product with several audiences who each need a different reason to care.
- The timing is right. AI agents need clean, well-defined data. Aladdin already has that data model, and Studio is how clients put it to work. Two BlackRock leaders support this on the record. Pavan Pemmaraju, Head of AI Product and Engineering, on the Never Done podcast in July 2026: "the data model itself is structured for agentic use cases." Diwakar Goel, Global Head of Data, on a BlackRock pensions webinar: "every single transaction that happens should be available and accessible to you via an event, via an API." BlackRock's October 2026 white paper makes the same argument in its own words, that business context must be codified for models and agents.

## "Why now?"

Testing: whether the move makes sense in his career.

- He has built marketing from scratch several times. He learned the most from taking a product into new markets and wants to do that on a platform with real scale.
- Aladdin is at a turning point. It is adding AI, expanding to AWS and bringing in private markets data. Studio needs a new kind of product marketing to explain what it makes possible.
- Keep it forward-looking. Do not dwell on what he is leaving.

## "Why move from startups to a firm this large?"

Testing: whether he will get frustrated by process, and whether he knows the tradeoff.

- **Be honest about it.** At startups he moved fast but had little reach. At BlackRock there are more people to align, but the work reaches far more clients.
- **Show he has worked with large organizations.** NovoEd is a Fidelity company. [Fill in: one example of working with Fidelity stakeholders or approval processes, and what he learned.] Mosaic, Mursion and NovoEd all sold to large enterprises.
- **Say what he brings.** Startups taught him to ship quickly and measure everything. That is useful inside a large firm as long as he respects how decisions get made.

## "Why did you leave your last role?"

Testing: whether there is a problem to worry about. The director mostly wants a short, calm answer of three sentences.

> "I joined Mosaic as the founding marketing leader in May 2025 and built [Fill in: the core result]."

> "[Fill in: a neutral, true one-sentence reason.]"

> "That showed me I want to do this work on a platform with real scale, which is why I'm excited about Studio."

Do not criticize Mosaic or anyone there. If the director asks a follow-up, answer briefly and come back to what he learned.

# 16. Understanding of the business and strategy

These questions test whether he understands who buys Studio and why, can explain it to a client on the spot, sees the real competitive threat, and can make clear strategic choices.

## "Who buys Aladdin Studio, and why?"

Testing: whether he knows the person who signs and the people who use it are often different.

Studio is usually sold to firms that already run Aladdin, as an add-on inside the core contract. The buying decision often sits with the CTO, CIO, head of data or COO. The daily users are engineers, quant teams, data analysts and operations staff. Each has a different problem.

| Who | What they want |
|---------------------------------------------|-------------------------------------------------------|
| CTO or head of data | Fewer separate systems and less fragile custom code |
| Quant and investment teams | To test ideas faster using Aladdin data plus their own |
| Operations and reporting teams | To automate manual work such as board and regulatory reports |
| COO and risk teams | Anything built to be governed and controlled |

The reason they buy is the same across all of them: to build what sets their firm apart without leaving the data and controls they already trust. Useful facts: Jeff Miller's line that before Data Cloud BlackRock "sent flat files, we sent large schema definitions, FTP and related transfers," and the goal to "reduce off-platform development risk." [Fill in: anything Priyanka Singh or Vijay Kasi said about where Studio sells best today.]

## "How would you explain Aladdin Studio to the head of technology at an asset manager?"

Testing: partly a live test of how he would sound in front of a client.

> "Your team already runs portfolios, trading and risk on Aladdin. But you still have needs Aladdin doesn't cover out of the box, so your engineers build side tools, pull data into spreadsheets and maintain pipelines. Studio lets you build those things directly on Aladdin. You get APIs that can read and write Aladdin data, a Snowflake-based data cloud with your Aladdin data already loaded and cleaned, and Python tools your team already knows. What you build uses the same data and controls as the rest of Aladdin. So your team spends less time moving data and more time building what makes your firm different."

Then ask a question back: "Where is your team spending the most time today on work outside Aladdin?" That shows he would run a real conversation, not a pitch.

## "Who are the competitors, including clients who build their own?"

Testing: whether he sees the real threat. For Studio, it is often the client's own engineering team.

| Alternative | How to position against it |
|--------------------------------------------------|--------------------------------------------------|
| Building in-house on Snowflake or Databricks | The client would still have to rebuild the investment data model, keep it in step and govern it |
| Other platforms' data layers and AI agents: State Street's Alpha Data Platform, a data layer, and SimCorp One's Agent Launchpad, a set of AI agents | Studio works on top of the system that already runs the client's portfolio |
| Data vendors with AI connectors: FactSet, LSEG, MSCI | They supply data; Studio connects data to the workflows where decisions and trades happen |
| Bloomberg BQuant, a cloud Python environment for analysts | It works on Bloomberg data; Studio code works on the client's own positions, inside the controls they already use |

Be fair. Building in-house makes sense for some firms, and rivals now make a similar promise that clients can keep their own tools connected. The job is to make the tradeoff clear, not to pretend there is none.

## "What would you focus on in your first 90 days?"

Testing: whether he will listen first and still deliver something useful early.

| Period | Focus | What he does |
|-------------------|------------------------------|---------------------------------------------------|
| Days 1 to 30 | Listen and learn | Meet the Studio PMs, Vijay Kasi's sales team, Priyanka Singh's go-to-market team, solutions engineers and value engineering. Talk to [Fill in: a target, such as 10 to 15] clients and internal users. Review Studio win and loss data. |
| Days 31 to 60 | One clear story | Write one positioning document for Studio, with versions for technical and business buyers. Test it with sales. Build or fix the two or three assets reps ask for most. |
| Days 61 to 90 | Prove it in one place | Run one launch or one segment end to end, with measures agreed in advance. Plan Studio's story for the next major event. |

The job asks him to use AI tools to scale content and competitive research, so he would set that up early.

## "Which types of clients would you go after?"

Testing: a clear choice he can defend, not "everyone."

1. **Existing Aladdin Enterprise clients with strong engineering teams.** They adopt fastest, and Studio is sold as an add-on to Enterprise. They are also the best source of proof.
2. **Clients in the middle of a migration.** Public hiring shows outside Studio work clusters around moves such as Janus Henderson's from Charles River. A migration is when a client rebuilds its integrations, so it is the natural moment to build them on Studio.
3. **Firms moving into private markets,** such as insurers and pensions adding private credit. BlackRock is pushing hard here with HPS and the May 2026 private credit analytics. These firms need to combine Aladdin data with Preqin and eFront data.
4. **A segment to test: bank fund finance teams.** Preqin already sells to them, and NAV loan monitoring needs exactly the data BlackRock holds. It is a new buyer with a new budget, the kind of market he is best at opening. He would test it before committing.

He would confirm the order with data in the first 90 days.

## "How would you take the product to a new kind of buyer?"

Testing: his strongest topic. The director wants a method backed by a real example.

The method: find who owns the budget in the new market. Learn their language and their main problem. Change the use case and the value story to fit that buyer. Win a few early clients and make them successful. Turn those results into proof for the rest of the market.

> "At [company], we sold [product] to [original market]. We expanded into [new vertical]. The budget sat with [new buyer] instead of [old buyer]. We changed [use case and message]. The result was [a number]."

Mursion's healthcare move, which landed Duke University Health System, is a natural candidate. Then connect it back: the same steps apply to taking Studio from engineers to business users, or from asset managers to bank fund finance teams.

## "How do you measure whether product marketing is working?"

Testing: results, not activity.

| Level | Measures |
|-------------------------------|---------------------------------------------------------------------|
| Business results | Studio's effect on ACV expansion and renewals; win rate in deals that used his materials; pipeline from new segments |
| Adoption | Clients actively building; time to a new client's first useful build; APIs or datasets used per client |
| Sales readiness | How often reps use the materials, and whether they can tell the Studio story clearly |

These get agreed with sales and product before a launch, not after. He can add that Studio's own revenue is likely the smaller prize: each point of retention on a $2 billion business is worth about $20 million a year. Then a real example: "At [company], I tracked [metric], which went from [start] to [end]."

# 17. Operating at the VP level

The role leads without a team. The director will test how he builds influence, whether he speaks up, how specific his launch stories are, and how he handles two obvious doubts: no asset management background and no large-company experience.

## "How do you get senior people to agree when you don't manage them?"

Testing: how he builds influence without authority.

The method: understand what each leader is measured on. Bring evidence from clients and data, not opinions. Share drafts early so people help shape them. Make the decision easy with a clear recommendation. This ties to BlackRock's "One BlackRock" principle.

> "At [company], I needed [leader] to agree to [decision]. They were worried about [concern]. I [what he did, such as ran customer calls or brought win-loss data]. We agreed to [outcome], and the result was [a number]."

The NovoEd decision with the head of Sales to sell AI translation as an expansion, not a new-business lead, fits this shape. It is also his launch walkthrough, so a different story is better here if he has one: [Fill in: another time he got senior people he did not manage to agree].

## "Tell me about a time you pushed back on a leader."

Testing: whether he speaks up, with respect and facts.

| Part | Content |
|-------------------------------|---------------------------------------------------------------------|
| Situation | "[The leader's role] wanted to [decision]." |
| Why he disagreed | "[The risk he saw, backed by data or client feedback]." |
| What he did | Raised it privately first, brought evidence and offered an alternative |
| Outcome | "[What happened and the result]." If the leader did not change their mind, say so and explain how he supported the final decision. |

## "Walk me through a specific launch you ran and what it achieved."

Testing: the area where the second interview fell short. One named launch with real details.

| Element | Template | NovoEd AI translation |
|--------------|-------------------------------------------|-------------------------------------------|
| The launch | [Launch name] at [company] in [month, year] | AI language translation at NovoEd, [month, year] |
| The goal | [Business goal] | Expansion within existing enterprise accounts |
| The audience | [Buyer title and segment] | Enterprise customers running large multilingual global programs |
| What he did | Positioning, messaging, sales training, content, launch event, [parts he owned] | Co-led with Sales and Customer Success; owned positioning, enablement and go-to-market |
| The result | [Two numbers] | More than $1 million in expansion from CEMEX and Marriott alone |
| Lesson | One honest thing he would do differently | [His lesson] |

Prepare a second launch in case the director asks for another. Ideally one is a new-vertical launch and the other a technical or AI feature launch, since this role covers both. [Fill in: the second launch, with its month, year and two numbers.]

## "Explain something to me on the spot."

Testing: how he would come across to clients.

Ask one quick question first: "Who's the audience?" Then give the plain answer in one sentence, one example, and stop.

| Prompt | Answer |
|--------------------------------------------------|--------------------------------------------------|
| What is an API? | "It's a way for one piece of software to ask another for data or to take an action, without a person in the middle. With Studio, a client's own app can pull positions from Aladdin or send an order automatically." |
| What does Aladdin Data Cloud do? | "It puts a firm's Aladdin data, already cleaned and organized, into Snowflake, so their team can query it and combine it with their own data without building the pipelines themselves." |
| Why does a semantic layer matter for AI? | "AI needs to know what the data means. If one system calls something 'exposure' and another calls it 'risk,' the AI gets confused. A semantic layer defines those terms once, so AI tools give consistent answers." |
| What is MCP? | "It's a common standard that lets AI assistants connect to outside data and tools. Several of Aladdin's rivals now offer one, so clients can ask an assistant like Claude about their data directly." |

## Doubts the director may probe

**"You haven't worked in asset management. How will you get up to speed?"**

Testing: honesty about the gap and a real plan.

- **Acknowledge it plainly.** "That's fair. I haven't worked inside an asset manager."
- **Show what he already has.** He worked on the venture fund at a large family office in Menlo Park, where he saw how investors evaluate deals and use data. NovoEd is a Fidelity company. His fund finance idea shows he is already learning the domain. [Fill in: finance concepts or tools he has used.]
- **Explain why the gap is smaller than it looks.** His best work has always been learning a new industry fast: architecture and engineering firms at Mosaic, new verticals at Mursion and NovoEd. [Fill in: how quickly he became credible with customers.]
- **Give a concrete plan.** BlackRock's internal training, client calls in the first weeks, and time with BlackRock's own investment teams, since BlackRock is Aladdin's largest user. [Fill in: anything he is already reading or studying.]

**"You haven't worked at a company this size. How will you adjust?"**

Testing: whether he will get stuck or frustrated.

- **What changes:** more people to align, longer planning cycles, more review for anything client-facing, including compliance.
- **What doesn't:** clear positioning, strong proof and good sales materials work at any size.
- **Proof he has done some of this:** NovoEd as a Fidelity company, and selling to large enterprise buyers at Mursion and Mosaic. [Fill in: one slow, multi-stakeholder approval he worked through.]
- **How he will start:** build relationships first, learn how decisions get made, and deliver one early win that helps sales.

# 18. Closing the final round

The close is his chance to show judgment through the questions he asks, and to stay consistent on timing.

## Questions to ask the Managing Director

Pick three or four, and ask the first one for sure.

1. "What would make you say, a year from now, that this hire was a clear success?"
2. "Studio hasn't been named on an earnings call, and the only public growth figure is an estimate of 17 times more API calls by 2030. Which adoption numbers matter most to you? Should Studio be judged on its own revenue, or on retention and contract growth?"
3. "Where do you see Studio's biggest growth over the next two years: deeper use by current Aladdin clients, or new types of clients?"
4. "When Studio loses a deal, what is it usually losing to? Another vendor, or the client building it themselves?"
5. "How does Studio fit into the vision for Aladdin that BlackRock is presenting at the Client Forum?" If the forum has already happened, refer to something specific it announced.
6. "Your Build vs Buy webinar poll put most firms in the hybrid or vendor camp, and the firms most wanted to stop maintaining compliance reporting themselves. Preqin already sells data to bank fund finance teams. Would you want me to test whether Studio and Data Cloud can turn that into a workflow, starting with NAV loan monitoring?"
7. "How do you see Studio supporting BlackRock's private markets push, especially with Preqin and eFront?"
8. "What's the hardest part of explaining Studio today, and where do clients get confused?"
9. "How do you like the people on your team to bring you problems or disagreements?"

Questions about pay, time off or remote work belong with the recruiter, not this conversation.

## Timing and other offers

The director wants to know whether he is serious about BlackRock and whether they need to move quickly.

- **Stay consistent.** In September he told Corey Hutchison he was in process with a few other companies, nothing at final stage, no pending offers. Update only if something has changed: "[Fill in: current status]."
- **Say where BlackRock stands.** "This is the role I'm most excited about, and I'd like to make it work."
- **Flag any deadline early.** "I have a decision due on [date], but BlackRock is my first choice, so I wanted you to know."
- **Confirm what is agreed.** Four days a week in the New York office is fine.

Before the final round, he should fill in every placeholder, pick the three anchor stories, and practice each answer out loud in under two minutes. Read the Q3 earnings release and check what BlackRock announced at the Client Forum, then work one specific detail into the questions.

# Appendices

- Appendix A. Evidence notes and caveats
- Appendix B. Key sources
- Verification notes for this revision

# Appendix A. Evidence notes and caveats

Several facts in this report are older, secondhand or estimates. A few could not be confirmed against the primary document. This appendix lists them.

## Check before citing in an interview

| Item | Issue | Where to check |
|---------------------------------|---------------------------------|---------------------------------|
| GPIF contract of ¥2.78 billion | Found in research files; the term of the contract is not published | GPIF procurement disclosure, March 2025 |
| CalPERS figures | One document shows $9.26 million over five years for a data platform and reports. Another shows $9.3 million to $15.0 million a year for a fixed income platform. They may be different contracts. The two figures are from different sources and need reconciling before either is cited. | CalPERS board materials, November 2021 and November 2025 |
| Border to Coast | Sources give the award as December 2025, a notice in July 2026 and a notice in September 2026. All agree the move from Bloomberg to Aladdin finishes around the end of 2026. | UK Find a Tender |
| Texas, UK Pension Protection Fund, Nest and US Pension Benefit Guaranty Corporation prices | Yearly figures for the Pension Protection Fund and Nest divide a published total by the contract length | The linked notices and contract |
| SDK downloads | pepy.tech counts mirrors; pypistats.org can exclude them. The two give different totals. | State the counter and method when citing |
| LSEG's MCP customer counts | From a summary of LSEG's results slides | LSEG Q1 2026 results materials |
| The count of 1,100 Aladdin clients and 5,500 support staff | From a November 2025 BlackRock job posting that is no longer online | No current source; cite as Reported |
| The Technical Writer posting that names an Aladdin Studio Developer Portal | The May 2026 posting has been removed; a Vice President version is still on job boards | Job board listings |
| SimCorp's €680 million of recurring revenue | Covers SimCorp and Axioma together, as reported by Deutsche Börse | Deutsche Börse FY2025 results |
| The New Mexico State Investment Council's $26 billion | BlackRock's case study gives no date | BlackRock case study |
| The September 2026 agent that reads investment management agreements | Reported in a WatersTechnology roundup; the article is paywalled | WatersTechnology |
| Cameron Skinner's September 2026 comment on semantics | Reported by WatersTechnology on September 24, 2026; the article is paywalled. The remark does not appear in any of his five BlackRock-published transcripts, so this revision states the semantics point in the author's own voice and quotes his January 2026 podcast line on guardrails instead. | WatersTechnology |
| The "68% of 303 firms" statistic | The 303-firm sample is the AI Adoption Report 2026; the 68% could not be found in that report and may come from a separate BlackRock webinar on whole-portfolio views | BlackRock AI adoption report, September 2026 |

## Figures to treat as rough

- Client counts use different scopes, from about 200 to 1,100. The higher counts likely include eFront and Aladdin Wealth clients. The 360,000+ user figure is mostly Preqin data users.
- The 3,000 citizen developers figure is BlackRock-internal headcount, given by Dave Woodhead on Snowflake's podcast (who adds that it "has probably peaked") and by Diwakar Goel on a BlackRock webinar. It is not a count of Studio clients, and Sudhir Nair's podcast gives no such figure.
- Aladdin's organization size appears as 5,500 supporting staff in a BlackRock posting and 7,000 people in a conference summary. They likely count different groups.
- The historical revenue mix by client type comes from an undated BlackRock deck that is likely many years old.
- The Studio and Data Cloud sizing is an estimate built on stated assumptions, not a BlackRock figure.
- The developer access scorecard reflects one test run on one day. Some rivals' pages blocked automated access, so their scores may be too low.
- The 2030 goals, the $20 billion market size and the 17 times API growth estimate are BlackRock forecasts, not results.
- Revenue growth in 2025 and early 2026 includes Preqin. Organic ACV growth, 16% for 2025 and 14% to 15% in 2026, is the cleaner measure.
- The risk factor count. BlackRock's own materials give 2,000-plus private markets factors, a 3,000-factor model for Aladdin Wealth and "2500 plus" in a stress-test demo. "Over 5,000 ... daily" appears only in a Fivetran write-up; say "thousands" unless citing Fivetran.

## What could not be found

- BlackRock has not named any outside client as building on Studio's APIs or the SDK. Royal London's chief executive credits the Snowflake implementation in its programme, without naming Data Cloud or Studio.
- No company filing on SEC EDGAR mentions "Aladdin Studio." "Aladdin Data Cloud" appears only in BlackRock's own 10-Ks.
- No public source shows a bank using Aladdin, eFront or Studio for fund finance.
- No formal partnership between State Street Alpha and Aladdin was found, only shared clients and Aladdin Provider work.
- It is not clear which marketing rules formally apply to Aladdin's technology marketing.
- The fall 2026 Client Forum announcements were not public as of October 8.
- The cadence of the Aladdin Client Forum is not published; the 2026 forum is in New York and an APAC forum was held in 2025.

## Quality of the underlying sources

- Competitor figures are mostly company-reported. No independent market share ranking was found.
- Win-loss reasons come from press releases, which rarely name the rivals a firm considered.
- Retired-application counts vary. BNP Paribas's count is 57 in one interview and more than 60 in another; BlackRock's own podcast with BNP's chief technology officer says "more than 60," for the whole 2016 to 2020 programme.
- Some trade press is paywalled, including several 2026 WatersTechnology and FundFire articles, so only their headline points are confirmed.
- Pension board documents are strong primary sources, but many sites blocked automated checking. Only 9 of 53 pension quotes were confirmed automatically; the rest were confirmed by reading during research.
- SEC filing mentions vary in quality. This report uses filings where a company describes its own use of Aladdin or its payments to BlackRock. It leaves out code-of-ethics examples, data source footnotes, personal biographies and filings by funds BlackRock manages. Selective Insurance's 2025 payments to BlackRock are left out because the filing does not clearly separate Aladdin from asset management.
- Job-board evidence of outside building names few end clients. Barings and Thrivent appear only in search result snippets.
- The interview format comes from candidate reports on Glassdoor. BlackRock's own candidate guidance asks applicants to use AI to prepare but to show their own experience, thinking and judgment in the room.

# Appendix B. Key sources

## BlackRock filings and investor materials

- BlackRock 10-K for FY2025
- BlackRock 10-K for FY2024
- BlackRock 10-K for FY2020
- Q2 2026 earnings call transcript, July 15, 2026
- BlackRock and Microsoft partnership to host Aladdin on Azure, April 2020
- Preqin private credit launch, May 2026
- Preqin Benchmarks and Indices expansion, July 2026
- Preqin acquires Colmore, 2021
- 10-K revenue note on fixed minimum fees
- 10-K Note 2 on how fees are set
- Q2 2026 earnings release
- BlackRock 2025 Investor Day presentation (2030 estimates, slide 23; addressable market, slide 34)
- BlackRock and AWS joint release and FAQ, December 2025

## BlackRock pages and research

- Aladdin Studio page
- Aladdin Data Cloud page
- Aladdin Client Forum 2026
- AI adoption report, September 2026
- Build vs buy insight, August 2026
- "The Intelligence of Investing" white paper
- Aladdin for banks and brokers

## BlackRock podcasts, webinars and videos used for this revision

- Snowflake Data Cloud podcast with Dave Woodhead, "From Analytics to Intelligence"
- Never Done podcast: "Data, the key ingredient" (Richard Newman with Snowflake, January 2025)
- Never Done podcast with Microsoft: "Humans in the loop; robots on the team" (Syril Smith Garson and Adrian Crockett) and "Microsoft Copilot episode, part 2" (November 2024)
- Never Done podcast: "Reducing time to insight" (Pavan Pemmaraju, July 2026)
- Aladdin Client Stories: BNP Paribas Asset Management (February 2023); "Capturing change alpha" (Pia Schaefer, July 2025); "How asset managers rethink operating models" (Cameron Skinner, January 2026); "How data architecture shapes modern trading" (Kamya Somasundaram and Aviva Investors, December 2025); Global Insurance Report episode (November 2023); SLC Management episodes (February 2024 and March 2026); Intesa, Northstar, TCW, UPP and Ingka Investments episodes
- Client-story videos: Royal London Asset Management, "Shaping tomorrow with technology" (Hans Georgeson with Tarek Chouman, November 2024); Helvetia
- Webinar replays: Build vs Buy; "Data as a strategic asset for pensions" (Diwakar Goel with Snowflake); "Unifying the whole portfolio across public and private markets" (September 2025); "Navigating private markets"
- Big Little Questions: "Are insurers disruptive or disrupted?" (Georgette Anderson and Brett Sadler); Kunal Khara on how clients shape product development; Randy Fradin and Microsoft on the Azure migration
- WatersTechnology Buy-Side Technology Awards 2023 winner interview with Kunal Khara, published by BlackRock
- Aladdin Client Forum 2026 opener video
- LangChain Interrupt 2025 talk by Brennan Rosales and Pedro Vicente Valdez
- Snowflake video with Jeff Miller on Aladdin Data Cloud
- Fivetran customer write-up with BlackRock, August 2024
- eFront client testimonial videos: APG, Allianz Capital Partners, Velliv, Mizuho, Bouwinvest, Meridiam, Brown Brothers Harriman, Alter Domus

## BlackRock job postings

- Senior Product Director, Aladdin Studio Developer
- Senior PMM, Technical Product Marketing (this role)
- Data Platform Architect, Aladdin Data
- Forward Deploy Engineer, Aladdin Data
- Software Engineer, Aladdin Graph
- Technical Writer, Aladdin Product, Vice President (job board copy)
- Aladdin Client Experience ("1,100 Aladdin clients"), November 2025, no longer online
- Product Marketing Associate, Aladdin Studio, live by November 2024 (archived copy)

## Prices, contracts and tenders

- Texas Permanent School Fund contract (archived copy)
- UK Pension Protection Fund award notice
- Nest award notice
- US Pension Benefit Guaranty Corporation contract
- CalPERS contract report, November 2021
- CalPERS contract extension, November 2023
- CalPERS finance item, November 2025
- GPIF procurement disclosure, March 2025
- LACERA risk system search (Institutional Investor)
- UBS ends Aladdin contract (Bloomberg via WealthManagement.com)
- Rhode Island Treasury recommendation memo
- Envestnet proxy statement, 2024
- JPMorgan Chase proxy statements, by year of payment: 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025

## Client filings

- Janus Henderson 10-K for FY2025
- Janus Henderson Q3 2025 earnings call, October 30, 2025
- Corebridge Financial 10-K/A for FY2025
- Deutsche Bank filing, March 2026
- GMO Trust filing, June 2026
- Northwestern Mutual Series Fund filing, May 2026
- Artisan Partners Funds filing, September 2026
- Ameriprise proxy statement, 2022
- Citigroup proxy statement, 2026
- Santander Asset Management completes Aladdin in Europe, May 2020
- New Mexico State Investment Council case study
- Aegon Asset Management hands its Aladdin middle office to Citi, August 2026
- Royal London trading desk (The TRADE)

## Pension documents

- CalSTRS portfolio risk report, March 2026
- PSERS annual financial report, FY2025
- Oregon Investment Council book, May 2023
- Maryland risk assessment, January 2022
- Florida SBA annual investment report, 2021 to 2022
- Wisconsin Investment Board modernization news
- Border to Coast tender notice
- Nest selects Aladdin
- OMERS job posting
- Aware Super rollout (Markets Group)
- AustralianSuper case study
- Korea NPS go-live

## Client voices and wins

- Bank of Israel (Central Banking)
- Royal London Asset Management
- AIA with BlackRock and BNY
- BPI Wealth
- Cathay United Bank
- Citi middle office for US iShares ETFs on Aladdin, February 2026

## Studio code and outside building

- Aladdin SDK on GitHub
- Janus Henderson code contribution, pull request 52
- Janus Henderson code contribution, pull request 53
- SDK plugin builder
- Aladdin SDK on PyPI
- The 11 public SDK plugin packages (54 API specifications)
- Advisor Center agent skills repository
- Claude for Financial Advisors
- Franklin Templeton Data Cloud job ad
- Janus Henderson migration contractor ad
- Spyrosoft Aladdin specialist ad, September 2026, no longer online
- Strata Data Cloud white paper
- Aladdin Copilot conference talk summary (ZenML)

## Partners, rivals and analysts

- Securitize contract filed with the SEC
- AccessFintech partnership release, November 2025
- Deutsche Börse FY2025 results presentation, with SimCorp figures
- BarmeniaGothaer selects Bloomberg and Clearwater, March 2026
- Marathon Asset Management unifies on SimCorp One (FinTech Global)
- Charles River company profile, Q4 2025
- Bloomberg AIM job ad
- SimCorp hires Gareth Morris from Aladdin, September 2026
- SimCorp names Iyan Adewuya chief product officer, December 2025
- Invesco adopts State Street Alpha, April 2021
- JP Morgan to connect to Aladdin (The Trade News, 2018)
- BlackRock selects Citi for Aladdin ETF support, with AccessFintech note (FOW)
- Tradeweb results release
- FactSet release on Portware and Aladdin
- SimCorp Agent Launchpad
- Clearwater agents in production
- FactSet MCP announcement
- MSCI AI connectors
- Arcesium AI platform
- LSEG Q1 2026 results summary
- S&P Global ratings through MCP
- Chartis RiskTech100
- Celent, April 2025
- Deloitte, December 2025

## Fund finance and regulation

- Federal Reserve SR 26-2 letter
- SR 26-2 guidance attachment
- EU list of critical tech providers (ESMA)
- Fund Finance Association survey
- Haynes Boone Fund Finance Annual Report 2026
- Bank of England Financial Stability Report, July 2026
- Federal Reserve note on bank lending to private credit
- Preqin for banks

# Verification notes for this revision

This revision applies a fact-check of the October 8, 2026 draft against a primary-source corpus: BlackRock's 54 public Aladdin API specifications and the SDK README, its product pages, press releases and job postings, the Fivetran and Microsoft write-ups, and about 120 transcripts of BlackRock talks, podcasts, webinar replays and client videos. The author's prose, structure, exhibit numbers and label scheme are kept. The changes are listed below.

## What was corrected and why

- **API count (section 7).** "58 API specifications" became 54. The 11 public plugin packages hold exactly 54 swagger files; the 301 operations stand.
- **Aladdin Graph (Exhibit 24).** The draft treated Graph as one API and named an "Investment Research API." Every public specification is an "agraph" API, so Graph is the layer; investment research is a domain of five alpha APIs. The row now says so, consistent with Exhibit 28.
- **Citizen developers (section 7, Exhibit 6, Appendix A).** "More than 2,000," attributed to Sudhir Nair, became 3,000, BlackRock-internal, quoted verbatim from Dave Woodhead (with his "has probably peaked" caveat) and Diwakar Goel. Nair's podcast gives no figure.
- **First use of "citizen developer" (Exhibit 26).** May 2024 became November 2023, on a BlackRock podcast, with later uses in March 2024 and the SDK README.
- **SLC Management (Exhibit 33).** Downgraded from "Confirmed (featured)" to placement only: neither SLC episode mentions Data Cloud, Snowflake, Studio or APIs.
- **"Never named a Studio reference client" (Summary, sections 7, 8, 11, 13, Appendix A).** Softened to "not named a client as building on Studio's APIs or SDK," because Royal London's chief executive credits the Snowflake implementation in BlackRock's own video.
- **Royal London (sections 3 and 5, Exhibit 16).** The COO attribution, "largest and most complicated programme," "over two years" and the system names were replaced with the CEO's published remarks: on time, under budget, "multiple order management systems," HSBC as partner, Snowflake in scope. The trade-press system names are kept as Reported.
- **BNP Paribas (section 5, Exhibit 16, Appendix A).** Relabelled Confirmed from BlackRock's own podcast, and the 60 applications attributed to the whole 2016 to 2020 programme (Aladdin, Salesforce, DataHub), not to Aladdin alone.
- **2023 awards (Exhibit 21).** Relabelled Confirmed and completed: Best Overall Technology Provider, Best IBOR and Best Portfolio Analysis Tool.
- **Titles (Exhibits 27 and 38).** Pia Schaefer to Global Head of Value Engineering for the Aladdin Client Business; Ted Stratigos to Global Head of Aladdin Wealth Tech; Sudhir Nair to Global Head of Aladdin; Rosales and Valdez to AI engineering lead and Principal AI Engineer; Woodhead's two published titles shown.
- **Three benefits (sections 7 and 11).** Presented as the Studio page's headings, "Create & automate," "Make Aladdin your own," "Align internally & externally," rather than as a BlackRock sentence.
- **"68% of 303 firms" (sections 6 and 7, Exhibit 40, section 18, Appendix A).** Flagged Unconfirmed: the 303 is the AI Adoption Report's sample, the 68% was not found in it and resembles a separate webinar statistic. Replaced in the closing question with the Build vs Buy poll.
- **Woodhead on Snowflake (Exhibit 27).** The unsupported "central to our strategy" quote was replaced with his verbatim podcast lines.
- **Risk factors (Exhibit 5, Appendix A).** "More than 5,000" is now "thousands," with the 5,000 tied to its only source, the Fivetran write-up.
- **Unsupported attributed quotes removed or re-sourced.** Stratigos on Auto Commentary guardrails (section 12), Skinner on semantics (sections 7 and 15), Goel "must be codified" (Exhibit 27, section 15), Khara on private credit (Exhibit 40), Garson on common copilot services (Exhibit 27) and Rivosecchi on "database ready on day one" (sections 7 and 16) were each replaced with a verbatim line from a BlackRock-published transcript, with speaker, title and source, or restated in the author's voice without attribution. Jeff Miller's flat-files-and-FTP line replaces Rivosecchi. "The language of portfolios" is attributed to Woodhead and the Client Forum 2026 opener, not to the Fink letter.
- **Client Forum cadence and podcast content (section 8).** "Every two years" removed; "executives rather than developers" qualified with the engineer-led talks and podcast that exist.
- **"No copilot without plugins" (section 7).** Upgraded to Confirmed and attributed to Microsoft's Adrian Crockett on BlackRock's Never Done podcast.
- **CalPERS (Exhibit 11, Appendix A).** A one-line note added that the two figures come from different sources and need reconciling. Neither figure was changed.
- **Additions from the corpus.** Exhibit 20A (Build vs Buy webinar poll and cost figures); the insurer scale figure in section 3; the clients featured in BlackRock-published podcasts and videos in Exhibit 8; Khara's "major unlock" and "eat our own cooking" lines in sections 7, 8 and Exhibit 40; the specification facts in section 7 (24 alpha, 6 beta, 23 stable, 1 sunset; application-key header plus OAuth scopes; 35 long-running operations; the linter comment; Access.Internal; ADX); Woodhead's three-pillar definition and Data Cloud scale; Pemmaraju, Somasundaram and Goel lines in Exhibit 27 and section 15.

## What this revision could not check

The pricing, contract, named-deal, competitor-financial and regulatory figures in this guide, including all of section 4 and Exhibits 10 to 13, the named decisions in Exhibits 9, 16 and 19, the competitor figures in Exhibits 18, 21 and 22, the SDK repository statistics in Exhibit 32, the job-posting details in Exhibit 28, the financial and partnership facts in Exhibit 40, and the fund-finance and regulatory material in Exhibit 37, were not checkable against the primary-source corpus used for this revision (BlackRock's public API specifications, product pages, press releases, job postings and about 120 transcripts of its talks and podcasts). They rest on the author's cited external sources, listed in Appendix B. Their labels are the author's and were neither added to nor strengthened here. Several of the dated decisions sit within weeks of the draft date and rest entirely on press releases; the author should be ready to name the public record behind each figure if challenged.
