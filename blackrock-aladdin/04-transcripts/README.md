# Transcripts

- `part1-youtube-and-site/`: the first batch, from the YouTube links and BlackRock's site (00_INDEX.md inside lists each file, its source and how it was obtained). File 04 is a different product (Aladdin CMMS), not BlackRock, and is flagged.
- `part2-cloudfront-and-podcasts/`: 95 items crawled from BlackRock's media CDN (captions and published transcripts), the Never Done and Aladdin Client Stories podcast feeds, and webinar replays. `_MANIFEST.tsv` maps each media file to its source page.
- `product-pages/`: text of the BlackRock product pages used as sources.
- `tools/`: the caption converter, Whisper transcription scripts and the assemblers that built the two sets.

Published transcript or caption text was preferred; local Whisper (faster-whisper base.en) was used only where neither existed, and those files say so in their header.
