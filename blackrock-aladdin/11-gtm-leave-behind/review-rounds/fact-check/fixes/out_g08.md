# Group g08: drafted fixes

## p14-02+p14-04 (FIX)

**Current:** the APIs by area with their package labels, how permissions work, how a client routes calls through its own gateway, and the Snowflake and Databricks answer, plus

**Proposed:** the APIs by area with their stability labels, how permissions work, how a client routes calls through its own gateway, and an answer on Snowflake and Databricks connectors, plus

**Why:** The labels belong to each specification, and one package can mix them: in asdk_plugin_trading 2.0.0b3, OrderAPI carries “x-aladdin-api-stability”: “stable” and TradeAPI carries “alpha”. The RFP question Schafer quotes is “Are you using connectors to Snowflake or to Databricks?” [9]. No public source shows a Databricks connection, so the row now names the answer to that question and asserts no connection.

## p14-15 (FIX)

**Current:** I could not run anything, open the catalog, guides, notebooks or samples, or test what a client receives;

**Proposed:** I could not run anything, open the catalog, the API guides or their notebooks and code samples, or test what a client receives;

**Why:** The APIs page offers notebooks and code samples “from carefully curated API guides” with no public link [24]. The SDK’s own sample code is public on GitHub (README line 226: “Sample code snippets ... are provided under resources/sample_code_snippets”), so the sentence now names only the guide material.

## p14-18 (FIX)

**Current:** Client forums and the solutions team | the Never Done podcast [28], the Big Little Questions video series [29], Woodhead [1], Rosales and Valdez [8]

**Proposed:** The invitation-only Aladdin Client Forum and the Solutions Engineering team | the Never Done podcast [28], the Big Little Questions video series [29], Woodhead [1], Rosales and Valdez [8], Client Forum page [NEW], Solutions Engineering job posting [NEW]

**New source:** NEW P Aladdin Client Forum 2026. BlackRock Aladdin event page, as of October 20, 2026. https://www.blackrock.com/aladdin/discover/expertise/events/aladdin-client-forum-2026

**New source:** NEW P Job posting: Aladdin Client Business, Solutions Engineering, Vice President (R265631, Singapore). BlackRock Careers, posted October 2, 2026. https://careers.blackrock.com/job/singapore/aladdin-client-business-solutions-engineering-vice-president/45831/98412767088

**Why:** The Forum page says it “is an invitation-only event” whose attendees include “a select group of prospective clients”. BlackRock’s job posting R265631 (October 2, 2026) says the Solutions Engineering team works “to help prospective clients understand how Aladdin and eFront can address” their needs. Both fit the After qualification column and now carry receipts. The Receipt cell grows by about one line.

## p14-24 (FIX)

**Current:** the APIs page, which promises “dozens of APIs”

**Proposed:** the APIs page, which promises “dozens of Aladdin APIs”

**Why:** The APIs page reads “Dozens of Aladdin APIs available – with constant new additions” [24]. The quotation now matches it word for word.

## p14-25 (CITE)

**Current:** The Developer Portal and the API framework guides | Studio page [14], APIs page [24]

**Proposed:** The Developer Portal and the API framework guides | Studio page [14], APIs page [24], developer portal [6, NEW, NEW]

**Also change (Exhibit 16 source note. Shared with p14-28; see the object "p14-25+p14-28 (exhibit note)".):** The After qualification column is what those sources say a client receives; I did not test it.

**Why:** The words hold, but their receipts were missing. Seventeen of the public specifications link to “apps/aladdin-developer-portal/#/guides/developer-guide” [6], and that address redirects to aladdin-login.blackrock.com (rechecked October 20, 2026, HTTP 302). A BlackRock job posting names the “Aladdin Studio Developer Portal”. Both NEW entries are already drafted by g03 (sNEW-g03-portal, sNEW-g03-job). The APIs page says “Learn about our API framework” [24].

## p14-28 (CITE)

**Current:** The API catalog and the Data Dictionary | asdk_plugin packages [6], APIs page [24]

**Proposed:** The API catalog and the Data Dictionary | asdk_plugin packages [6], APIs page [24], developer portal [NEW]

**Also change (Exhibit 16 source note. See the object "p14-25+p14-28 (exhibit note)".):** The After qualification column is what those sources say a client receives; I did not test it.

**Also change (Exhibit 4 source note (page 5), owned by g03 as p05-65. Same overstatement; g03 already rewrites it from the developer-portal redirect.):** the catalog, guides, notebooks and samples sit behind a client login [24].

**Why:** The APIs page describes the Data Dictionary (“Our Data Dictionary allows you to explore Aladdin data”) and “Dozens of Aladdin APIs available” with no public link [24]. “API catalog” is a plain description of that list. The gate itself is shown by the developer portal address, which redirects to the Aladdin client login (sNEW-g03-portal). The note now says that is the basis.

## p14-25+p14-28 (exhibit note) (FIX)

**Current:** The After qualification column is what those sources say a client receives; I did not test it.

**Proposed:** The After qualification column is what those sources say a client receives. The developer portal opens only after a client login [6, NEW], so I could not test it.

**Why:** Neither BlackRock page says these resources are for clients only. The gate is observed at the developer portal address that the specifications link to, which redirects to aladdin-login.blackrock.com [6, sNEW-g03-portal]. The note now names that basis. It adds about half a line on page 15.

## p15-08+p15-10 (FIX)

**Current:** The open-source SDK on GitHub and PyPI, with a detailed README; the plugin builder | A client host and credentials, which the SDK needs for every call | SDK README [23], PyPI history [65], plugin builder [27] Get help | GitHub issues and pull requests on the SDK, answered by BlackRock engineers; on the Studio page, “Book a meeting” and “Download the brochure” | Notebooks, code samples, support | Pull request 52 [38], pull request 57 [66], Studio page [14]

**Proposed:** The open-source SDK on GitHub and PyPI, with a detailed README, sample code and demo notebooks; the plugin builder | A client host and credentials, which the SDK needs for every call | SDK README [23], PyPI history [65], plugin builder [27] Get help | Pull requests on the SDK, reviewed and merged by a BlackRock engineer; on the Studio page, “Book a meeting” and “Download the brochure” | Jupyter notebooks and code samples from the API guides | Pull request 52 [38], pull request 57 [66], Studio page [14], APIs page [24]

**Also change (Sources register, entry 66. PR 57 is titled “add Pydantic v2 compatibility support” and its patch never mentions MCP.):** Pull request 57, dependency conflict with the MCP toolkit, blackrock/aladdinsdk. GitHub, merged August 2026.  
-> Pull request 57, add Pydantic v2 compatibility support, blackrock/aladdinsdk. GitHub, merged August 11, 2026.

**Why:** The SDK’s only issue (59) has no BlackRock reply. Pull requests 52 (from Janus Henderson) and 57 were both approved (“LGTM”) and merged by Vedant Naik, Lead Engineer, Aladdin Studio [38, 66, 40]. The APIs page offers “Python Jupyter Notebooks” and “code samples ... from carefully curated API guides” [24]. No public source offers support, so that word goes. The SDK’s sample snippets and two demo notebooks (SDK_Demo_template.ipynb, SDK_Demo_ADC_template.ipynb) are public in the repository [23], so the Build row now lists them.

## p15-114 (CITE)

**Current:** deals with [67, 68, 69].

**Proposed:** deals with [4, 7, 14, 57, 67, 68, 69, 70, 71].

**Why:** The count of 10 holds. Sources 67 to 69 cover only FactSet, State Street and LSEG. The citation now matches the exhibit’s own source note, which lists every platform page tested.

## p15-116 (FIX)

**Current:** 2 where the vendor opens it before any sale, 0 where access follows a relationship.

**Proposed:** 2 where the vendor opens it before any sale, 1 where it is partial or needs sign-up or approval, and 0 where it is missing or blocked.

**Why:** The exhibit legend reads “2: Fully public or self-serve, 1: Partial or after sign-up or approval, 0: None or blocked”. State Street’s sandbox scores 1 behind an account (“Start here using your State Street account”). The sentence now uses the exhibit’s three levels. It adds about ten words to page 15.

## p15-118 (FIX)

**Current:** At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, documentation, a sandbox and a first call come after a relationship exists.

**Proposed:** At Aladdin, as at Bloomberg, State Street, SimCorp, Clearwater and Arcesium, full documentation, a sandbox and a first call come mostly after a relationship exists.

**Why:** Exhibit 17 scores Aladdin, Bloomberg and State Street 1 for public docs, and Bloomberg 1 for sandbox and first call. The public SDK README is real documentation [23]. The sentence holds fully for SimCorp, Clearwater and Arcesium, which score 0 on all three.

## p15-119 (DECIDE)

**Current:** Data and cloud platforms sell to developers directly and cluster high.

**Proposed:** Snowflake and Databricks sell to developers directly and score highest, and LSEG comes next. FactSet and MSCI keep trials and first calls for licensed clients [4, 67].

**Alternative:** Keep the sentence and split the “Data and cloud platforms” band of Exhibit 17 in two: “Cloud data platforms” (Snowflake, Databricks) and “Market data vendors” (LSEG, FactSet, MSCI). The sentence then reads: “Cloud data platforms sell to developers directly and score highest. Market data vendors range from open to fully gated.”

**Also change (Exhibit 17, MSCI row (scores owned by g09). The fact-checker found developer.msci.com shows a public catalog (“Explore our catalog to find APIs”). If g09 raises MSCI’s Public docs or API catalog score, recheck the second sentence of the recommended fix.):** MSCI

**Also change (Under the alternative only: Exhibit 17 group row.):** Data and cloud platforms

**Why:** This is the paragraph’s closing claim, so it changes the argument. Snowflake and Databricks score 16 of 16 and offer self-serve trials (“Start your 30-day trial with $400 in free credits”). LSEG scores 12. FactSet scores 9: its “Try for free” is a contact form and its guide says to “contact your FactSet account manager”. MSCI scores 2 and “grants no right or license ... without an appropriate license” [4].

## p16-02 (FIX)

**Current:** The sources are BlackRock product pages, SEC filings, procurement notices, public code and packages on GitHub and PyPI, press releases, job postings, and transcripts of BlackRock recordings.

**Proposed:** The sources are BlackRock product pages, investor presentations, SEC filings, a fund prospectus, procurement notices, press releases and job postings. Others are public code and packages on GitHub and PyPI, other vendors’ product and developer pages, blogs and trade press. Transcripts of recordings and earnings calls with BlackRock speakers complete the set.

**Why:** The register also holds two Investor Day presentations [10, 47], the iShares V plc prospectus [18], earnings call transcripts [46, 48 to 51], blogs by Fivetran, Microsoft and BlackRock Engineering [22, 25, 40], trade press [37, 55] and other vendors’ pages [5, 59, 67 to 71]. The list now covers every kind.

## p16-05 (FIX)

**Current:** AI agents pulled the pages, unpacked the packages, transcribed the recordings and drafted the text.

**Proposed:** AI agents pulled the pages, unpacked the packages, transcribed the recordings that had no published transcript or captions, and drafted the text.

**Why:** The transcript corpus README says “Published transcript or caption text was preferred; local Whisper ... was used only where neither existed”. In the register, 9 recordings are machine transcriptions and 4 use published transcripts, published captions or auto-captions.

## p16-09 (FIX)

**Current:** each source’s grade (P, S or T), title, speaker and date.

**Proposed:** each source’s grade (P, S or T), title, publisher or speaker, and date where one is known.

**Also change (Page 2, “How to read the receipts” (same wording; the added words fit on the short second line, so page 2 does not grow).):** document, giving the grade (P, S or T), title, speaker and date.  
-> document, giving the grade (P, S or T), title, publisher or speaker, and date where one is known.

**Why:** Only S entries name a speaker. P and T entries give a publisher, for example entry 2, “LSEG press release, 2025.” Entries 9, 20, 21 and 31 are undated (“Replay page undated”).

## p16-10 (FIX)

**Current:** BlackRock and Aladdin are registered trademarks of BlackRock, Inc.

**Proposed:** BlackRock and Aladdin are trademarks of BlackRock, Inc. or its affiliates.

**Why:** The ALADDIN registration (US 5829287) is owned by BlackRock Finance, Inc., the renamed former parent that is now a subsidiary. BlackRock’s own Studio page uses this wording: “BLACKROCK and ALADDIN are trademarks of BlackRock, Inc. or its affiliates.”
