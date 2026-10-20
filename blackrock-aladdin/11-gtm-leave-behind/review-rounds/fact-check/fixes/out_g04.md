# Group g04: drafted fixes

## p06-58+p06-59 (CITE)

**Current:** Ten specifications expose an endpoint for long-running operations, 35 operations are flagged as long-running, and the SDK polls them [23].

**Proposed:** Ten specifications expose an endpoint for long-running operations, and 35 operations are flagged as long-running [6]. The SDK polls them [23].

**Why:** Both counts are right and come from the 54 specifications in source 6: 10 specs have a /longrunningoperations/{id} endpoint and "x-aladdin-lro" appears on 35 operations. The SDK README (23) supports only the polling ("LRO Utilities to trigger and poll Long Running Operation endpoint calls"), so 23 stays on that clause alone.

## p06-63+p06-64 (FIX)

**Current:** Every request carries an application key plus OAuth 2.0 scopes such as trading.order_management.order.v1.Order:read, and the client ID and secret come from the Studio UI [23].

**Proposed:** Every request carries an application key. It is paired with an OAuth 2.0 token with scopes such as trading.order_management.order.v1.Order:read, a client key, or a user name and password [6]. The client ID and secret come from the Studio UI [23].

**Why:** Every security option in all 54 specs pairs the "VND.com.blackrock.API-Key" header with one of OAuth2 (access code or client credentials), "ClientKeyHeader" or "basicAuth" (OrderAPI/swagger.json:24-45), and the scope string appears only in those specs (source 6, :27-28). The SDK README (23) lists "`Basic Auth` / `OAuth`" with Basic Auth as the default, so OAuth is one option, and 23 stays only on the Studio UI clause.

## p06-66 (FIX)

**Current:** Five BlackRock speakers define Studio in the 128 recordings I pulled for this document [28, 29];

**Proposed:** Five BlackRock speakers describe Studio or its parts in the 128 recordings I pulled for this document [1, 16, 26, 30, 31];

**Why:** Sources 28 and 29 are series index pages whose only "Studio" is navigation text, so the five recordings themselves (1, 16, 26, 30, 31) are cited instead. Goel and Miller describe parts (events, APIs, the Data Cloud) without naming Studio (Goel webinar [28:52] "via an event, via an API"; Miller transcript has 0 hits for "studio"), so "define" becomes "describe Studio or its parts". Sources 28 and 29 stay cited in the Exhibit on where recordings live, so neither is orphaned.

## p07-01 (FIX)

**Current:** Exhibit 6. Five BlackRock executives have defined Studio on the record

**Proposed:** Exhibit 6. Five BlackRock executives describe Studio or its parts on the record

**Why:** Only Woodhead, Newman and Khara name Studio. Miller speaks only about the Data Cloud ("We sent flat files, we sent large schema definitions, FTP and related transfers", 0 hits for "studio") and Goel never says Studio, so the title matches the body text in p06-66.

## p07-16 (CITE)

**Current:** Kunal Khara, Managing Director and Global Head of Aladdin Product, BlackRock, early 2024. https://www.blackrock.com/aladdin/discover This is the hub page; the interview video is linked from it.

**Proposed:** Kunal Khara, Managing Director and Global Head of Aladdin Product, BlackRock, interviewed by Victor Anderson, WatersTechnology, February 8, 2024. https://www.waterstechnology.com/awards-rankings/7951675/bst-awards-2023-best-overall-technology-provider-for-2023-winners-interview-blackrock The video is also on the Aladdin hub page, https://www.blackrock.com/aladdin/discover.

**Why:** The Exhibit 6 cell actually reads "Awards interview, early 2024" next to "as a 2024 focus" in the column before it, and both are right: Khara says the themes are "where we're very, very focused in 2024" [18:59], and WatersTechnology dated the 2023 BST Awards winner's interview "2024-02-08". Only the register entry improves: it gains the exact date and the article URL instead of the hub page alone.

## p07-22+p07-27 (DECIDE)

**Current:** Four of the five describe Studio in the same terms, APIs and events plus the Data Cloud, and two of those four add developer tools. Newman calls Data Cloud “part of Studio” [16]. Goel describes events, APIs and a near-real-time data store [26]. Khara calls it programmatic access to data and reporting [30]. A 2026 job posting calls Studio “Aladdin’s extensibility layer” [32].

**Recommended:** Four of the five describe ways for clients to reach Aladdin through code. Newman calls the Data Cloud and the analytics APIs part of Studio [16]. Goel says every transaction should be available to clients through an event or an API. He also describes a near-real-time data store [26]. Khara calls Studio programmatic access to data and reporting [30]. Only Woodhead adds developer tools [1]. A 2026 job posting calls Studio Developer “Aladdin’s extensibility layer” [32].

**Alternative:** Newman, Goel and Woodhead each name APIs and the Data Cloud. Only Woodhead also names developer tools [1]. Newman calls the Data Cloud and the analytics APIs part of Studio [16]. Goel says every transaction should be available to clients through an event or an API. He also describes a near-real-time data store [26]. Khara calls Studio programmatic access to data and reporting [30]. A 2026 job posting calls Studio Developer “Aladdin’s extensibility layer” [32].

**Also change (Exhibit 7 (title, rows, note)):** see object p07-28+p07-31+p07-40+p07-45 -> Must follow the same option: recommended here goes with its recommended table, the alternative here goes with its alternative table.

**Also change (Next sentence, same paragraph (kept in both options)):** The message is consistent across speakers and years, so BlackRock already has a positioning for Studio. -> Keep as is. The author may soften it to "The same parts recur across speakers and years, so BlackRock already has the core of a positioning for Studio."

**Why:** Only Woodhead names APIs, events and the Data Cloud while calling it Studio (Simplecast transcript [00:05:25] "a set of APIs events. The Aladdin Data Cloud"). Newman has the Data Cloud and APIs but no events, Goel has all three without saying Studio, and Khara gives only programmatic access ([18:37] "on a programmatic basis at machine scale"). The job posting gives the label to Studio Developer: "Set and evolve the vision for Studio Developer as Aladdin's extensibility layer". The opening count is the paragraph's thesis, hence DECIDE. Recommended keeps "Four", which holds because Khara describes programmatic access and Miller speaks only about the Data Cloud. The alternative drops Khara from Exhibit 7 and names the three speakers who name APIs and the Data Cloud.

## p07-28+p07-31+p07-40+p07-45 (DECIDE)

**Current:** Exhibit 7. All four speakers name APIs, events and the Data Cloud as parts of Studio


Speaker, date | What they said | APIs and events | Data Cloud | Developer tools | 


Kunal Khara, early 2024 | “More users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis” [30] | Yes | Yes | – | 

Richard Newman, January 2025 | “The Aladdin data cloud ... which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella” [16] | Yes | Yes | – | 

Diwakar Goel, 2025 | “Every single transaction ... via an event, via an API”; “a near real time data store”; exposing “the software and application that we’re building” [26] | Yes | Yes | Yes | 

Dave Woodhead, November 2025 | “It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... developer tools” [1] | Yes | Yes | Yes | 


Source: the four recordings cited [1, 16, 26, 30]. Quotations are verbatim; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. Yes means the speaker names that part; – means not. Only Goel and Woodhead name developer tools.

**Recommended:** Exhibit 7. Four speakers describe parts of Studio, and only Woodhead names them all


Speaker, date | What they said | APIs | Events | Data Cloud | Developer tools | 


Kunal Khara, early 2024 | “More users are craving this ability to interact with our data, with their data, with reporting with dashboards on a programmatic basis” [30] | Implied | – | – | – | 

Richard Newman, January 2025 | “Aladdin data cloud specifically comes in, which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella” [16] | Yes | – | Yes | – | 

Diwakar Goel, 2025 | “Every single transaction ... via an event, via an API”; “a near real time data store”; exposing “the software and application that we’re building” [26] | Yes | Yes | Yes | – | 

Dave Woodhead, November 2025 | “It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... developer tools” [1] | Yes | Yes | Yes | Yes | 


Source: the four recordings cited [1, 16, 26, 30]. Quotations are verbatim; Khara, Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. Yes means the speaker names that part. Implied means the speaker describes it without naming it. A dash means neither. Goel describes these parts as ways to reach Aladdin’s data.

**Alternative:** Exhibit 7. Three speakers name APIs and the Data Cloud, and only Woodhead names developer tools


Speaker, date | What they said | APIs | Events | Data Cloud | Developer tools | 


Richard Newman, January 2025 | “Aladdin data cloud specifically comes in, which is part of Studio”; “those analytic APIs ... That’s all part of the Studio umbrella” [16] | Yes | – | Yes | – | 

Diwakar Goel, 2025 | “Every single transaction ... via an event, via an API”; “a near real time data store”; exposing “the software and application that we’re building” [26] | Yes | Yes | Yes | – | 

Dave Woodhead, November 2025 | “It exposes everything Aladdin knows how to do as a set of APIs events. The Aladdin data cloud built on top of Snowflake ... developer tools” [1] | Yes | Yes | Yes | Yes | 


Source: the three recordings cited [1, 16, 26]. Quotations are verbatim. Goel and Woodhead are machine or auto-caption transcriptions, marked as such in the Sources section at the end of this document. Yes means the speaker names that part. A dash means not. Goel describes these parts as ways to reach Aladdin’s data.

**Also change (Body paragraph before Exhibit 7):** see object p07-22+p07-27 -> The recommended table goes with "Four of the five describe ways for clients to reach Aladdin through code". The alternative table goes with "Newman, Goel and Woodhead each name APIs and the Data Cloud".

**Why:** The legend says Yes means the speaker names the part. Newman never says "event", Khara names none of the three ([18:42] "on a programmatic basis"), and Goel never says "developer tools" ([35:40] is about BlackRock staff). Splitting "APIs and events" into two columns shows Newman's APIs without events. The Newman quote now matches the published transcript word for word: "and Aladdin data cloud specifically comes in, which is part of Studio". The old "The Aladdin data cloud ... which is part of Studio" dropped "data cloud and" without an ellipsis. The new title and column split change the exhibit, hence DECIDE. Optional: Woodhead now has a published transcript (Simplecast, [00:05:25]), so source 1 could cite it instead of YouTube auto-captions.
