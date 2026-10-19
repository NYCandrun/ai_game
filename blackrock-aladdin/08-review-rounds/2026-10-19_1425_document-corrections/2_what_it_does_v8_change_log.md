<!-- agent a48f330baad373c75; started 2026-10-19T14:25:57.746Z; finished 2026-10-19T14:41:00.003Z -->

## V8 revision complete

**Outputs** (all in `/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/pdfcheck/out/`):
- `Aladdin_Studio_What_It_Does_V8.md` (75 KB; full document, 32 headings, 35 Markdown tables)
- `Aladdin_Studio_What_It_Does_V8.docx` (pandoc, 42 KB)
- `Aladdin_Studio_What_It_Does_V8.pdf` (soffice from the docx) — **31 pages**. Opened with the Read tool and checked pages 1–6, 12–19, 25–37 of the first build and 2–4, 16–19, 25–27 of the final build: headings, bullet lists and every table render (Exhibits 1–12, glossary, limits table, sources sheet). First build had equal-width columns; I set proportional widths via the separator rows and rebuilt (37 → 31 pages). The other agent's `out/parts/` directory was left untouched.

Every quotation added was grepped verbatim in the named source files (01 Woodhead transcript, 15 reference pages, 11 Newman, 17 Miller, transcripts2/049 webinar, readme.md, unpacked specs). Spec facts (108 hits of VND.com.blackrock.API-Key and X-API-Key, client.blackrock.com OAuth endpoints, Order:read/:write scopes, 35 x-aladdin-lro flags, DATACLOUD permission group) were re-verified against the unpacked packages.

## Change log (section/exhibit · old → new)

**B2 (contradicted framing)**
1. "What Studio is" · "BlackRock shows little of Studio in public" → "shows little of the Studio screens and catalog in public"; added two sentences naming what is public (Studio page, Studio for Aladdin Risk page, APIs page with catalog/Data Dictionary/notebooks/samples, Snowflake podcast with Studio's head of engineering, podcast with Studio's GM, SDK blog, job postings) with new tags S91 S94–S98 S103.
2. "Where the evidence comes from" · "closest an outsider can get to seeing what Studio does" → "…to seeing the API surface Studio exposes. They are the best public view of the APIs, not of Studio as a whole."

**B3 (author's tally / unverified)**
3. "What the packages contain" · new paragraph "A note on the counts": add-on figures (54 APIs, 301 ops, 24/6/23/1) independently recomputed and matched; core-package 4 APIs/25 ops and every derived total (58, 326, 27 alpha/7 beta, 218 scoped, 65 batch, 11 LRO, 90 linter notes) marked once as the author's own tally. Summary KPI source line and "What was read" cross-reference it.
4. Exhibit 12 source note and evidence bullet · PyPI release history (14 releases, two add-on dates) marked "author's own reading… unverified; only 2.0.0b10 as of July 2026 verified"; S69/S70 relabelled likewise.
5. Conclusion 9 evidence · added the independently recomputed add-on-only split 24/6/23/1 beside the author's 27/7/23/1.
6. Conclusion 1 evidence, glossary "ACM", S5 · "Aladdin Credit Management" → "ACM, which this report reads as Aladdin Credit Management; unverified, only the value ACM appears".
7. Exhibit 4, glossary "Studio Space", limits table · "Named only in alert settings. Role not described" / "appears only in alert settings" → "Named in alert settings; not defined in the files" / "It is not defined in the files."

**B4 (additions, ~900 words of prose in the author's style)**
8. (a) "Aladdin and Studio in plain terms" · new row "How BlackRock describes it": Woodhead's three pillars verbatim ("exposes everything Aladdin knows how to do as a set of APIs events", ADC "built on top of Snowflake…pushes that into Snowflake", "a set of developer tools"/"sandboxes, research environments"), "we have 3,000 citizen developers", "I think that number has probably peaked", flagged as BlackRock-internal.
9. (b) Conclusion 6 reasoning · new paragraph "Events, outside the files": Woodhead "APIs events"; technical-writer postings on streaming APIs/webhooks/AsyncAPI; Build vs Buy line "you need access to APIs, you need access to events, and you need to make your workflow much more event based as opposed to batch based".
10. (c) "What the packages contain" · new paragraph "How a program signs in, from the files": VND.com.blackrock.API-Key, OAuth at client.blackrock.com, X-API-Key, basic; per-resource scopes (trading.order_management.order.v1.Order:read/:write) identified as the method section's "access tags"; two-layer authorisation; ADC auth via TokenAPI or Snowflake JWT. Method section's "access tags" sentence and glossary "API Applications" updated to match.
11. (d) Conclusion 1 reasoning + limits-table "behind the login" row · portal catalog, API-framework docs, Data Dictionary, Jupyter notebooks, multi-language samples, ADX, ATX, README's "Aladdin Developer" environment; Studio for Risk "access management and usage monitoring" quote.
12. (e) Conclusion 9 reasoning · APIs page "dozens of APIs"; Newman "We're releasing soon the ability to actually access those analytic APIs, portfolio analysis, security analysis…"; Studio for Risk "Run analytics programmatically: Compute portfolio and security analytics…"; positions/risk outputs/pricing/performance absent from public set.
13. (f) Conclusion 2 reasoning · "Data Cloud, outside the files": "around 2019" start, 2021 launch, Fivetran + Snowflake quote, "hundreds of Snowflake accounts", "tens of thousands of pipelines", Miller "We sent flat files… FTP and related transfers", Newman "part of Studio". Conclusion 3 reasoning · Woodhead 2024 "enabling clients to bring their own data into ADC, and to distribute Aladdin data to their own data ecosystems."
14. (g) Limits table "What Studio offers for AI" · added "Absence in the files is not absence in the product": Copilot "now available to all Aladdin clients", "Will not give investment advice", tools map to existing APIs, Woodhead "a co-pilot to help me build".
15. (h) Conclusion 8 reasoning · "Other design signals" paragraph: protobuf/gRPC-gateway fingerprint, 190/301 POST, 35 x-aladdin-lro (distinguished from Exhibit 9's 11 check-back ops), bitemporal fields, four-eyes state machines, 850-attribute Portfolio, bqlExpression, Dynaconf, keyring, openapi-generator/plugin builder, api_registry.py and domain_apis_list.json.
16. (i) "Aladdin and Studio in plain terms" · new row "Hosting and people": Azure today, AWS H2 2026; ~7,000 people, 4,000+ engineers, hundreds of clients in 70 countries; Woodhead, Newman, Braunstein, Nair, Miller with titles.
17. (j) Exhibit 6 row, conclusion 3 evidence, S23 · DATACLOUD permission group added; Exhibit 10 and S52 · UserAPI's three user types (client employees, BlackRock employees, bots); glossary "Studio Compute" · README's "Aladdin Studio Compute sessions" vs marketing's "Aladdin Compute".
18. Conclusion 7 reasoning · one sentence: Woodhead's 3,000 are BlackRock staff, supporting the citizen-developer group but silent on client count.
19. Sources · new rows S91–S103 (Woodhead podcast, Fivetran blog, Miller video, Newman audiocast, APIs/Studio pages, Studio for Risk + Copilot pages, job postings, Build vs Buy webinar, Microsoft Ignite recap, AWS release, spec recomputation/ZenML, ADC press release, SDK blog).

**Rule 5** · appended "Verification notes for V8" (what changed and why; add-on figures independently recomputed, core-package figures and PyPI history the author's own tally; Woodhead quotes from cleaned auto-captions).

**Format notes (disclosed in the verification notes)**: version set to V8 with "V8 revision October 19, 2026"; bar charts/timeline in Exhibits 3, 8, 12 and the Exhibit 2 diagram rendered as tables with identical figures; page references replaced by section references; Exhibit 1's page column dropped. All original prose, exhibit numbers/titles, flags, S-tags and quoted file text otherwise reproduced unchanged.
