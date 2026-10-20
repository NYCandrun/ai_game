# Batch b015 re-check (skeptical second pass)

Flagged rows: p04-05 (CORPUS-ONLY) and p04-06 (PARTLY). The other four rows are CONFIRMED or CONFIRMED (note), so they were not re-checked.

Web attempts for source 21 (https://www.youtube.com/watch?v=BahCi45_BTc):
- oEmbed returned the title "Blackrock Aladdin Explore - Intro" by "jas jas" (@jasjas9597).
- The watch page HTML (fetched 2026-10-20) carries publishDate "2022-12-25", lengthSeconds 861, a shortDescription, and a captionTracks entry "English (auto-generated)".
- The signed caption baseUrl returned HTTP 200 with 0 bytes, for both XML and json3.
- The innertube get_transcript endpoint returned 400 "Precondition check failed".
- The WebSearch budget for this turn was used up, so no new web searches could be run. I did not use third-party transcript sites.
- The video description is the only web text reachable for this recording.

| id | claim | first verdict | final verdict | agrees | receipt (URL or file:line, then exact quote) | correction |
|---|---|---|---|---|---|---|
| p04-05 | The Explore application: its "new what-if model" (Explore classroom recording) | CORPUS-ONLY | CORPUS-ONLY | yes | Web, https://www.youtube.com/watch?v=BahCi45_BTc (shortDescription): "Blackrock Aladdin Explore also provides a framework for modeling changes to portfolios' composition and creating portfolios from scratch, and viewing reporting on the resulting portfolio." Words, /home/user/ai_game/blackrock-aladdin/04-transcripts/timestamped/yt_BahCi45_BTc.m4a.ts.txt:96 [09:34]: "If you go to the New What If model button in the top right corner of Explore, you'll have a couple options pop up." | The web supports what-if modelling in Explore. The exact words "new what-if model" were reachable only in the local machine transcript, because the caption track came back empty. They are the label of a button ("New What If model"). No change to the text needed. |
| p04-06 | Explore's new what-if model compares a changed portfolio with the original before anything is traded | PARTLY | PARTLY | yes | Web, same page (shortDescription): "a framework for modeling changes to portfolios' composition ... and viewing reporting on the resulting portfolio". Corpus, yt_BahCi45_BTc.m4a.ts.txt:101 [10:16]: "I'll see an original column for my original market value and then a modified column for any changes that I've been making."; :106 [11:03]: "That'll then show me each portfolio, my original portfolio, and my new What If portfolio side by side". | The comparison is supported: by the corpus for the side-by-side view, and by the web description for modelling changes. Nothing in source 21 says "before anything is traded". The description and the transcript never mention trading or orders. One BlackRock page (a local crawl of the Aladdin Studio product page) speaks of "conduct what-if portfolio analysis" next to generating orders. It is not about Explore and does not say "before trading" either. Suggested wording: drop the phrase, or write "compares a modified what-if portfolio with the original, side by side 21". |

## Recommended corrections
- p04-05: no change. The source is a machine transcription, and the exact words could be checked only locally.
- p04-06: delete "before anything is traded", or mark it as the author's inference.
