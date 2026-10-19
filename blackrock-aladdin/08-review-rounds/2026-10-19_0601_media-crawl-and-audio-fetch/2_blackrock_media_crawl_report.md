<!-- agent af3e25602ff6bebc6; started 2026-10-19T06:01:24.614Z; finished 2026-10-19T06:50:31.419Z -->

## Final report: Aladdin / eFront media crawl

All crawler processes (crawl.js / crawl_light.js + Chromium) are killed. No downloads after the stop instruction. Nothing outside media2/ was modified (scripts/logs live in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/crawl2/; media/ untouched).

### Output
Directory: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media2/
Manifest: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media2/MANIFEST.tsv
Columns: filename, source_page_url, title, description, also_on_pages, same_audio_as. 198 rows = 198 files (every file except `picks.json`, which I did not create and is not media). Total size 4.7 GB.

| type | count | size |
|---|---|---|
| .mp4 (new, 720p; 1 only had 480p) | 68 | 3.8 GB |
| .mp3 (art19 podcast audio) | 62 | 970 MB |
| .captions.en.vtt (from d2adqanfijfsj5.cloudfront.net/captions/) | 30 | small |
| .transcript.txt (page transcripts, "Read the full transcript" sections) | 27 | small |
| .whisper.txt (pre-existing, made by another process; rows added) | 11 | small |

The 16 already-downloaded names were skipped (not re-downloaded; they appear only in `also_on_pages` references).

### Key findings
- **Uncharted**: only 2 episodes exist (Uncharted_Ep1_2024-56, Uncharted_Ep2_2024-130). Downloaded.
- **Big Little Questions**: 15 total; 3 were new: BLQ_LP_GP_1227193-901 ("How do private markets players define risk anymore?"), BLQ_AI_AskAladdin_1500737-550, BLQ_Insurers_1215264-320. All three have .vtt captions.
- **Podcasts**: /aladdin/discover/podcast is an empty stub; the hub is /aladdin/discover/expertise/never-done-podcast-by-aladdin. Audio is on art19, two feeds: `https://rss.art19.com/never-done-by-aladdin` (15 eps, Apple id 1817216941) and the older `https://rss.art19.com/aladdin-client-stories` (47 eps incl. teasers). All 62 mp3s downloaded; 13 Never-Done episodes are byte-identical audio re-publishes of Client-Stories episodes (recorded in `same_audio_as`). 30 on-site episode pages crawled; 26 had full text transcripts -> saved as `<slug>.transcript.txt` (header lines give title, source URL, mp3 id). Snowflake audiocast = 64a15752-….mp3 ("Data: the key ingredient"), transcript saved.
- **Webinars**: index page is gated, but 12 individual Aladdin replay pages serve the mp4 ungated: Fundfire1/2 (Data-Driven Approach; Harnessing Risk), TradeTensionsWebinar_2025, ala_build_vs_buy, data_strat-asset_pens_v1, AladdinClimateIntroCut_2024, NavPrivMark_V2, transforming_private_markets, FT_Live_FullVideo, ala_private_markets_africa, 20250912_sctask2738310 (Unifying the Whole Portfolio). eFront webinars likewise: efrontinsight-983, efronts-843, reducingrisk_v1-409, ala_efront_fair_webinar-331, PrivateMarketSustainability-207.
- **Client stories/events**: JPM_Fireside_R6, ninepoint_client_testimonial, 20241113_RLAM (+ RLAM_V8 variant on implementations page), Helvetia_Testimonial_2025, BSTAwards2023WinnerInterview, Preqin_2025_2270877_Captions, ala_client_forum_2026_opener, apac_acf-649 (480p only — meta descriptor lists no other rendition).
- **Product pages**: aladdin-copilot has Landscape_Ask_eFrontCopilot-873 (different cut from the -571 v2 already held); other product pages only re-embed BLQ videos/podcasts already captured.
- **eFront**: portfolio-monitoring mp4 found by interception = eFrontPortfolioMonitoring-14.720p.wide.mp4. Sitemap (/en/sitemap.xml) exposed 8 product explainer videos and ~40 client-testimonial pages, all ungated on the same CloudFront bucket (eFront<Person>-<n> naming); 36 testimonial/explainer mp4s downloaded (6M_Testimonial_Final, ADEPA_REV_2024, BNP_Paribas_Full_Length_R3, SumitomoMitsui, PrivateInvestmentsMizuho, etc.). No vice01 player assets were needed — vice01.* iframes are personalization frames, not video.
- Useful CDN pattern: `https://d2adqanfijfsj5.cloudfront.net/meta/<baseId>.txt` lists every rendition for a video; `…/captions/<baseId>_captions_en.vtt` gives captions when present.

### Pages that yielded nothing (193 of 316 crawled)
- 404s: /aladdin/discover/implementations, /aladdin/discover/aladdin-partnerships, /aladdin/discover/news-and-insights (real pages are /aladdin/discover/resources/implementations, /aladdin/discover/partnerships; no news index). efront /efront-invest and /efront-data-intelligence product pages 404.
- Aladdin: home (/aladdin), /discover/expertise/webinars index, uk-pensions-webinar (gated), /discover/expertise/tech-forces, aladdin-studio-for-aladdin-risk-management, microsoft-treasury-case-study, all 19 /expertise/events/* pages except ACF-2026 and APAC recap, press releases, report/whitepaper pages, all eloqua-form pop-ups (no mp4 leak), aladdin-wealth insights, new-mexico-sio-case-study.
- eFront: ~140 non-video pages (brochures, case studies, press releases, research papers, product pages other than portfolio-monitoring and copilot, webinars index, corporate-videos listing, sustainability/ESG webinars which are form-gated, testimonial pages for acumen and sumitomo-mitsui-trust which had no player).
- Not reached before stop: ~110 remaining eFront sitemap pages (mostly press-release/research/brochure URLs from the /en/ sitemap) — low likelihood of media based on the crawled sample.

Crawl artefacts (scripts, per-page HTML, JSON, logs, both RSS feeds) are in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/crawl2/ if a re-run or the remaining eFront pages are wanted later.
