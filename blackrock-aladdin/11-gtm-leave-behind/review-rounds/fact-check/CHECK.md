# Fact-check brief (one batch of claims)

You are one of many fact-checkers. You own ONE batch of five or six claims from "Aladdin Studio from the outside", a 19-page independent analysis of BlackRock's Aladdin Studio. Verify each claim fully. Do not check anything outside your batch.

## Rule 1: original research first
Verify each claim against the open web FIRST, as if you had never seen our files:
- Use WebFetch and WebSearch (load with ToolSearch "select:WebFetch,WebSearch" if not in your tool list) and `curl -sSL -A "Mozilla/5.0" <url>`. sec.gov and github.com return 403 to curl here; use WebFetch for them, or EDGAR full-text search, raw.githubusercontent.com, PyPI JSON (https://pypi.org/pypi/<name>/json).
- Start from the URL the Sources register gives for the claim's source number (/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/sources.tsv: number, entry text, URLs). Then look for a SECOND independent confirmation where one plausibly exists.
- Recordings (podcasts, webinars, YouTube talks): try the recording's page, show notes, a published transcript, or YouTube captions (for YouTube, try fetching https://www.youtube.com/watch?v=ID and look for captions, or a transcript site). If you cannot reach the words, fall back to our local transcripts (corpus map below) and mark the verdict CORPUS-ONLY.
- Claims from the asdk_plugin PyPI packages (spec counts, operation names, fields, maturity labels): download the package fresh from PyPI into a new empty directory under /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/dl/<your batch id>/ (`pip download --no-deps --dest <dir> <name>==2.0.0b3`, then unzip) and read the swagger.json files there. Run scripts with `python3 -I` from outside that directory.

## Rule 2: receipts
Every row must carry a receipt: the URL (or file path + line number / timestamp) AND an exact quote of the words that support or contradict the claim. "Confirmed" with no quote is not acceptable. No receipt after a real search = UNVERIFIED, and say what you tried.

## Verdicts
CONFIRMED | CONFIRMED (note) | CORPUS-ONLY | PARTLY (say exactly which words are wrong) | UNVERIFIED | WRONG (give the correct fact and the receipt).
Also check that the source number attached to the claim actually supports it; if the sentence is true but the cited source does not say it, verdict is "PARTLY: wrong citation" and name the source that does.

## Corpus map (fallback only; say when you use it)
- Repo /home/user/ai_game/blackrock-aladdin/: 04-transcripts/ (part1-youtube-and-site/ with 00_INDEX.md; part2-cloudfront-and-podcasts/ with 00_INDEX.md and _MANIFEST.tsv; product-pages/; requested-recordings/; timestamped/), 02-api-catalog/ (apis.json, api_digest.txt, specs/), 01-research-briefings/, 10-compendium/.
- Scratchpad /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/: yt/transcripts/, yt4/ (timestamped captions), crawl2/ (crawled BlackRock pages), unpacked/ (the 11 packages), clientcheck/ (four BlackRock briefing PDFs as text).
Use grep -rn. The full document text, for context only, is /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/doc_layout.txt.

## Report
Write /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/reports/<batch id>.md: a Markdown table
| id | Claim | Verdict | Receipt (URL or file:line/timestamp, then the exact quote) | Note / correction |
followed by one line per non-CONFIRMED row stating the recommended correction. Reply with that summary only. Do not edit the document.
