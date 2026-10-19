<!-- agent a86af2c2b374cc249; started 2026-10-19T04:11:32.768Z; finished 2026-10-19T04:15:41.934Z -->

## Visual review: aladdin_field_guide.html

Rendered via Playwright/Chromium (fonts loaded: Archivo, Plex Sans, Plex Mono confirmed). 31 screenshots in /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/visual_review/. Most informative:
- .../visual_review/fig2x_overview.png (hub diagram, 2x)
- .../visual_review/fig2x_lifecycle.png
- .../visual_review/light1280_request_hop5.png (hop diagram + empty detail column)
- .../visual_review/light1280_conventions.png (stretched cards)
- .../visual_review/dark1280_overview.png
- .../visual_review/light390_lifecycle.png (mobile figure collapse)

### Verdict
It reads as a considered design, not a template: Archivo/Plex pairing does real work, captions have a voice, the tier colour system exists. What drags it toward template: three of five figures are unlabelled boxes-and-arrows, several grids stretch into empty cards, and on phones every figure is illegible.

### 1. Diagrams

**Overview hub.** The caption says every view "reads the positions a trade creates", but the drawing fans everything out from the trade directly, skipping Positions; the figure contradicts its own caption. Draw the mechanism: trade → Positions (one arrow, "creates"), then Positions → Compliance levels / Cash ladder / Collateral / Accounting lots / Risk exceptions; Broker and Data Cloud stay on the trade. Concrete defects: the six diagonal/vertical labels sit on top of the lines ("re-evaluates" at x=395 is bisected by the x=380 line; same for "creates lots", "projects", "re-prices"). Add `paint-order:stroke;stroke:var(--surface);stroke-width:4px` to `svg .lbl`, or anchor verticals with `text-anchor="start" x="392"`. Diagonal arrowheads are hidden because lines end inside the target rects (e.g. (140,62) inside Positions y 30–70); end them at edges: (175,72), (585,72), (175,258), (585,258). Satellites are all grey although the page has tier colours; give each a 5px top band like the lifecycle nodes (Compliance/Risk = middle, Cash ladder = front, Accounting/Collateral = back, Data Cloud = platform). In dark mode the grey boxes nearly vanish (`--surface-2` #1F2933 on `--surface` #161E27, stroke `--line`); use `stroke:var(--muted)` at `opacity:.6` or lift dark `--surface-2` to #243040.

**Lifecycle.** Best-structured figure (tier band + name), but the three band labels at x=10/500/990 do not bracket the stages (middle office is stages 4 and 9, back is 6–8), and the caption repeats them. Replace the band row with the artefact handed between stages on each arrow: note → portfolio → order → verdict → trade → confirm → entitlement → lot. Draw Oversight as a full-width bar (x 10–990, y 112–128, `--middle-soft`) since the caption says it "runs across all of it". Drop the "front office" sub-text (redundant with the band) and show the domain (`trading`, `compliance`) instead. The top 40px of the viewBox is empty: move y=40→16, viewBox height 150→126.

**Architecture.** Honest stack, labelled arrows. Missing label on the last arrow (add "runs on"). Chips abbreviate "inv-ops"/"pm" while the explorer says "investment operations"/"portfolio management"; use two rows of 6 at width 130 or keep one row with `font-size 9` and full names "inv. ops", "port. mgmt". This is the only figure using tier colours; add a four-swatch legend at y=385 so the colours mean something here.

**Request.** Arrows are unlabelled; the hops are the interesting part. Label: "POST :batchPost", "app key + scoped token", "resolve refs, check perms", "verdict", "operation id", "done: true". The poll loop returns to OrderAPI (x=420) but the polled resource is the LRO store; end it at x=760 and label "GET …/longrunningoperations/{id}". Inactive hops at `opacity:.35` fail contrast; use .55. Empty top band: y=40→16.

**AI pipeline.** The strongest figure (sub-labels, highlighted loop, registry feed). Add arrow labels: "prompt", "cleared prompt", "20–30 tools", "draft answer".

### 2. Typography
Scale and 68ch lead are good. Two inconsistencies: Overview uses h1 (44px) while every other lesson uses h2 (30px); make all lessons h2 and keep h1 for the brand, or vice versa. Pill vocabulary is split three ways: `.pill` mono/999px, `.chip` Archivo/999px, `.states span` and `.apis code` mono/6px. Tier appears as a mono pill in the lifecycle detail but as an Archivo chip in the explorer. Rule: identifiers (API names, versions, states, paths) = mono, 6px radius; categories (tier, stability, filters) = Archivo 999px.

### 3. Layout
- Conventions: open cards stretch closed ones in the same row to ~300px empty height. `.conv{align-items:start}`.
- Request detail: 1.3fr/1fr grid with an empty right column; `#reqDetail{grid-template-columns:1fr}` and put the codebox there, or move Back/Next under the text. Codebox lines truncate; use `white-space:pre-wrap;overflow-wrap:anywhere`.
- Products: 8 cards in 3 columns leaves an orphan row; use `repeat(4,1fr)` at ≥900px or `g2` with minmax 420px for 2×4.
- Domain explorer "All": 7,261px tall, one card per API at 800px wide. `.apilist{grid-template-columns:repeat(auto-fill,minmax(360px,1fr))}`; `.dom small{white-space:nowrap}` (currently wraps "5 APIs · 41 ops").
- Sticky header is 106px (12% of a 900px viewport): move `.brand .sub` and the three stat pills into Overview, `padding-block:8px 4px`, tabs `padding:5px 10px` → ~72px.
- Mobile (390px): `figure svg{max-width:100%}` scales the 1000-wide lifecycle to 358px, text ~4px, and `.fig-scroll` never scrolls. Set `.fig-scroll svg{min-width:720px}` and the hub `min-width:560px`, with a "scroll →" hint in the figcaption.
- Quiz and glossary cards are equal-height with large empty bottoms; `align-items:start` or drop `min-height:150px` to 110px.

### 4. Colour
`--accent` equals `--front` (#1F5FBF): the hub's "Booked trade", primary buttons, selected layers and the "Front office" chip all read as one thing. Since tabs already select with `--fg`, use fg ink for selection states (`.layer.on`, `.lc-node.on`, hub centre) and reserve blue for front office. Stability pills collide with tiers: stable=green=back, alpha=amber=middle, beta=blue=front, so an explorer card shows "stable" and "trading" in the same hue family side by side. Make stability shape-coded (leading ● dot, neutral outline) and colour only sunset red. Muted contrast is fine (5.0:1 light, ~7:1 dark). Dark mode is properly re-tuned (soft tints, accent-ink), not inverted; the one failure is the hub boxes noted above.

### 5. Three changes that raise it most
1. Make the hub depict trade → positions → views, with tier bands and unobstructed labels.
2. Label the handoffs on lifecycle, request and AI arrows, and fix the lifecycle band row.
3. Fix stretching (conventions, request detail, products orphan) and mobile figure scaling; decouple accent from front tier and stability colours from tier colours.
