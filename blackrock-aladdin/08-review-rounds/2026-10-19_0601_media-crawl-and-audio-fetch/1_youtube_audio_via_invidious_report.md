<!-- agent a64df60f9de0e8f3f; started 2026-10-19T06:01:24.641Z; finished 2026-10-19T06:12:31.348Z -->

All six videos obtained as audio (AAC m4a, YouTube itag 140, ~128 kbps), each verified with ffprobe. Directory: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media3/

| id | what worked | file | ffprobe duration (listed length) |
|---|---|---|---|
| U1FUBHYIkOU | Invidious instance invidious.schenkel.eti.br, /api/v1/videos/ID?local=true -> instance-proxied /videoplayback itag 140 | /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media3/yt_U1FUBHYIkOU.m4a (97.6 MB) | 6028.3 s (6029 s) |
| oyqeCHFM5U4 | same | /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media3/yt_oyqeCHFM5U4.m4a (14.6 MB) | 905.0 s (905 s) |
| 3iXd7a7_F6g | same | /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media3/yt_3iXd7a7_F6g.m4a (2.2 MB) | 135.2 s (136 s) |
| 0Bl_q4k65Vc | same | /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media3/yt_0Bl_q4k65Vc.m4a (5.9 MB) | 366.6 s (367 s) |
| x5huBDiCLGc | same | /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media3/yt_x5huBDiCLGc.m4a (8.2 MB) | 505.4 s (506 s) |
| BahCi45_BTc | same | /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/yt/media3/yt_BahCi45_BTc.m4a (13.9 MB) | 861.4 s (862 s) |

No captions were obtained for any video (audio suffices per the goal). Caption attempts all failed: Invidious /api/v1/captions returns HTTP 200 with an empty VTT body on both working instances (their servers are also blocked from timedtext); youtube.com/api/timedtext (with and without kind=asr) returns 200 with empty body; youtube-transcript-api raises IpBlocked; yt-dlp web_safari reports auto-captions require a PO token and web_creator demands sign-in (plus 429 on the watch page).

What did not work, for the record: api.cobalt.tools and every reachable cobalt community instance (capi.3kh0.net, cobalt-backend.canine.tools, cobalt-api.meowing.de) require a Turnstile JWT (error.api.auth.jwt.missing); most other cobalt hosts are unreachable through the proxy (CONNECT 502) and instances.cobalt.best fails TLS via the proxy. Piped: piped-instances.kavin.rocks connection reset; of ~40 Piped API hosts tried, the only live ones (pipedapi.ducks.party, api.piped.private.coffee, pipedapi.wireway.ch) return 500 SignInConfirmNotBotException (their IPs are blocked by YouTube too). Invidious: invidious.f5.si has a working API but its media proxy (/videoplayback, /latest_version) sits behind an Anubis proof-of-work challenge (not pursued since schenkel worked); the other listed instances return 403/401/"Endpoint disabled"/"Companion is starting".

Other files left in the directory: dl_rest.sh (the download script) and dl_rest.log (its log). Temporary probe files were removed. Nothing outside media3 was touched; HTTPS_PROXY and TLS verification were left as configured. The youtube-transcript-api package was pip-installed (harmless, unused result).
