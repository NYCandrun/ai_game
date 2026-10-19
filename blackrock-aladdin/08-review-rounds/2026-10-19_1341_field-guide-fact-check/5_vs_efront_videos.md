<!-- agent a4ff60b1332738176; started 2026-10-19T13:42:07.889Z; finished 2026-10-19T13:43:46.034Z -->

All 32 "eFront video" files (064–095) plus transcripts/34_ and 35_ read in full. Caveats: 077_eFront_Data_Intelligence_Product_Video.md is a mismatched recording (Sarah Melvin "Welcome to BlackRock" UK video, no eFront content); 083 and 089 are unusable garbled Whisper output; the index notes the eFront Copilot video has no speech, so nothing in this set covers Copilot or "eFront Provider".

1. CONTRADICTIONS
- Page: "eFront (acquired 2019) for post-investment workflow and risk". Wrong: eFront covers the pre-investment side too. 075_Dunedin: "We use eFront Invest and we use it for CRM, for deal flow management, and for fund management." 070_BlackRock_Alternative_Investors: "end-to-end platform, all the way from deal management and sourcing to investor reporting."
- Page: "Combined as eFront Insight in February 2026". Misleading: eFront Insight is a long-standing GP-to-LP data exchange product, not a 2026 creation. 095_Velliv: "the unique selling point for us was eFront's data exchange ecosystem, aka eFront Insight." 075_Dunedin: "we are a GP who is compliant with Insight. We are reporting via Insight on a quarterly basis." At most Preqin data was folded into an existing product.
- Page (products): "The products are entry points onto one set of positions and portfolios, not separate systems." For private markets this is wrong: eFront is a separate suite with its own book of record that is integrated with, not inside, Aladdin. 070: "We're going to take eFront and Aladdin together and implement it across all of our asset classes." 081_eFront_Invest_LP: "designed to integrate with E-fronts and BlackRock's other leading products and services."
- Page (overview): users are "Asset managers, insurers, pension funds, wealth managers, banks and corporate treasuries." Omits a major eFront constituency: fund administrators/asset servicers. 080_eFront_Invest_GP: "more than 450 general partners and asset servicers that use E-Front". 073_Brown_Brothers_Harriman: "eFront helps BBH be a technology leader in the fund administration market."

2. REFINEMENTS
- "One system holds what each portfolio owns" – for alternatives the IBOR is eFront, not Aladdin. 070: "for the first time, we have a real-time investment book of record."
- Delivery "Hosted software": eFront historically shipped desktop/on-prem; hosted web is a migration. 085_Madrona: "finishing up the implementation from the desktop version to the web version of the PEO/VC product." 067_Alter_Domus: "started with eFront Invest Classic version, and we recently upgraded to eFront Invest Version."
- eFront is sold as named modules, which the page never lists (see section 4).
- Portfolio Monitoring figure: 082: "comprehensive library of 320 standard financial and operational KPIs".
- Investment Café scale: 35_: "more than 10,000 funds choose to report with e-front investment cafe, securely sharing over 10 million documents."
- Insight scale: 079: "more than 100 dedicated data analysts"; "inclusion of over 1,000 public indices".
- LP footprint: 081: "more than 300 investors are using E-front solutions, including seven of the top 10 limited partners worldwide."
- Client extensibility (page conv card) also holds for eFront: 070: "eFront is a highly configurable system."

3. CONFIRMATIONS
- eFront was acquired by BlackRock and BlackRock is a heavy user: 070: "Following the acquisition of eFront by BlackRock... BlackRock to become the largest user of eFront."
- BlackRock improvements flow to external clients ("internal success to external adoption" quiz theme): 070: "enhancements that we are now using are also going to be rolled out to external BlackRock Solutions clients."
- Single-source-of-truth value proposition: 066_Allianz: "we have one single point of truth"; 092_Old_Mutual: "we now have a single version of the truth."
- Institutional audience, incl. pensions and sovereign/state investors: 069_APG: "500 billion euros of investments under management"; 094_Vaekstfonden: "the Danish state's investment fund."
- API connectivity matters to clients: 071_BNP_Paribas: "We need more API technology to interface e-front with more platform and system that we have."

4. NEW FACTS (priority order)
1. eFront Invest (older name FrontInvest; "Invest Classic" is the legacy version) is the core transaction-based fund management/administration system for GPs, LPs and administrators. 080: "transaction-based approach to fund management"; 091_Ocorian: "main modules are Funds and Investment Management and the General Ledger."
2. Named Invest modules in client use: CRM, Deal Flow, Fundraising, Fund/Direct Investment, General Ledger (eFront GL), Notice, Workflow, Excel plug-in, Input (client onboarding), Loan/Debt, Fee, Consolidation, Lending, Cash Flow Forecasting, Value at Risk, Dashboarding. 067: "eFront loan module... eFront Notice module... eFront Workflow module... eFront Excel... eFront Input module"; 076_EDC lists "Cash Flow Forecasting and the Lending modules."
3. eFront Insight is the GP-to-LP data exchange: GPs upload standard-template fund, cash-flow and asset data (free to the GP), eFront analysts validate it, LPs analyse against peers, benchmarks and public indices. 34_: "dedicated team of e-front data intelligence analysts working with general partners in order to collect and cleanse data"; 075: "there's no cost to the GP of having to use that."
4. Insight has a GP view letting managers see what LPs see and generate investor reports. 079: "review data using the exact same analytical charts, benchmarks, and tools as their investors."
5. eFront Data Intelligence = the analyst service behind Insight (the explainer video in the set is mismatched, so this comes only from 34_).
6. eFront Portfolio Monitoring (clients call it "Front PM") collects monthly financial/operational KPIs from portfolio companies via an investee portal, for direct investors. 074_CapMan: "gathering the financial data every month, automatically"; 082: "secure Investi portal... collection and validation of data directly from Investis" (Whisper for "investee").
7. eFront Investment Café is the cloud investor portal/VDR/CRM for fundraising, onboarding, capital call and distribution notices and reporting. 087_Meridiam: "reporting, sending out capital call notices, fundraising, documents, or marketing."
8. Legacy/other products seen: PEO (Private Equity Office), PEO/VC, web LP, eFront Office, Investor Cloud (outsourced data capture), eFront data warehouse. 076: "transitioning from Private Equity Office... to FrontInvest"; 066: "The last module we bought was actually eFront investor cloud."
9. User types: GPs (buyout, VC, infra, impact), LPs (pensions, insurers, Allianz, APG), fund administrators/asset servicers (BBH, Alter Domus, BNP Paribas SS, Ocorian, IPS, MB Fund, Adepa), state/development funds (EDC, Vaekstfonden, SIS). 086_MB_Fund: "private equity fund administrator for firms that are usually underneath a billion dollars."
10. BAI runs eFront as end-to-end platform with a real-time IBOR and a searchable "collective intelligence" layer; next step is eFront plus Aladdin across asset classes. 070: "type in the words, 'healthcare, technology, and India,' you're able to see a vast array of information."
11. Integration is via APIs to clients' payment, AML/compliance and reporting systems. 071: "interface, for instance, or e-front platform with our payment system."
12. eFront works with ILPA on reporting standards and supports open- and closed-ended and crypto funds in one accounting system. 084_IPS: "their relationship with the ILPA"; 064_6M: "open-ended funds with subscription and redemption and close-ended funds with capital call."
Not in evidence: eFront Copilot, "eFront Provider", Preqin, the Aladdin–eFront data flow mechanics, Feb 2026 dates.

5. TERMINOLOGY
"Alternative investments"/"alternatives" and "private markets" (used interchangeably); GP/LP; "fund administrator"/"asset servicer"; "single source/point/version of truth"; "end-to-end platform", "front to back"; "best of breed for alternative assets" (069); "pure player in the alternative investments market" (095); "data exchange ecosystem" (095); "real-time investment book of record" and "morning newspaper" (070); "collective intelligence" (070); "make alternatives less alternative" (070); "BRS community"/"BlackRock Solutions clients" for external Aladdin clients (070); "the Aladdin Business" (070); "modules" (eFront's packaging unit); "FrontInvest", "Front PM", "PEO"; "investees" for portfolio companies; "capital call notice", "distribution notice", "capital account statement"; "transaction-based approach"; "fit-for-purpose workflows"; "straight through processing" (095).
