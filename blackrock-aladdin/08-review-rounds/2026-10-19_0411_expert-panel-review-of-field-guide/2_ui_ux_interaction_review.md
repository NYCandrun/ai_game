<!-- agent a156527b5de3eba47; started 2026-10-19T04:11:32.743Z; finished 2026-10-19T04:17:46.378Z -->

UX review: aladdin_field_guide.html (4 passes: 1280/390 × light/dark; dark checked via prefers-color-scheme and data-theme="dark"). No console errors or page errors in any pass. Hash deep-links, tab switching, lifecycle nodes, explorer filters/search, layers, stepper, details, glossary and flashcards all function.

HIGH

1. Diagrams are unreadable at 390px. All four `.fig-scroll` SVGs just shrink (svg max-width:100%), so effective text is 3.1–4.6px (lifecycle 3.1–3.9px, architecture 3.5–4.6px, request 3.4–3.9px; overview figure ~5px). Lifecycle hit targets are 33×21px, architecture domain chips 26×12px. The "Click a stage" / "Click a layer" lessons are effectively non-functional on a phone.
Fix: let figures scroll instead of shrink: `@media (max-width:720px){.fig-scroll svg{min-width:760px}}` (and `#archsvg{min-width:700px}`), plus a hint in the figcaption ("scroll sideways →"). Better for lifecycle: on narrow screens also render STAGES as a wrapping row of `.chip` buttons above the SVG.

2. Horizontal body overflow on Domain explorer at 390px: scrollWidth 432 vs innerWidth 390. Cause: `.api .head b` (mono, no wrap) for `CounterPartySettlementInstructionTemplateAPI` measures 401px in a 358px column; the whole page then pans sideways.
Fix: `.api .head b{overflow-wrap:anywhere;min-width:0}` (and `.api .head{min-width:0}`).

3. Sticky header consumes 164px = 19% of an 844px viewport at 390px (brand, subtitle, three stat pills, tab row). Every lesson starts a fifth of the way down and stays that way while scrolling.
Fix: `@media (max-width:600px){.brand .sub,.brand .row{display:none}}` or make only `nav.tabs` + `.progress` sticky (move `position:sticky` from `header.top` to a wrapper around the nav).

MEDIUM

4. Tab bar wayfinding on mobile: 11 tabs in a 957px row inside a 358px viewport, with no fade/mask or chevron; the only clue that more exist is a truncated label. On desktop all fit. The progress bar and "Lesson n of 11" eyebrow are good.
Fix: `nav.tabs{mask-image:linear-gradient(90deg,#000 calc(100% - 32px),transparent)}` when scrollable, or a small "n/11" counter next to the row; also expose the ArrowLeft/Right hint on mobile.

5. Global ArrowLeft/ArrowRight hijacks focus: with focus on a flashcard or lifecycle node, ArrowRight jumps to the next lesson and focus is dropped to <body>; the same focus loss happens after the pager buttons and any tab click (verified: activeElement = BODY after show()).
Fix: in `show()`, after switching, focus the new panel's heading (`h1/h2` with `tabindex="-1"`) or the selected tab; scope the arrow handler to `e.target===document.body || e.target.closest('#tabs')`.

6. Silent wrap-around: "Next hop →" on hop 6 jumps to hop 1; "← Back" on hop 1 goes to hop 6; lifecycle Next/Previous wrap the same way (lcNext ×2 from stage 9 lands on stage 2). No end-of-sequence cue.
Fix: disable at ends (`hn.disabled = i===HOPS.length-1`) or relabel to "Start over ↺".

7. Light-mode contrast failures on small coloured text (11.8–12.8px): `.pill.s-alpha` #B8731A on white 3.8:1; `.pill.s-stable` #2A8A66 on white 4.3:1; `.pill.t-middle` on #FBEEDB 3.3:1; `.pill.t-back` on #DDF2EA 3.7:1; pressed `.chip.c-middle` white on #B8731A 3.8:1; `.chip.c-back` 4.3:1. Dark mode passes everywhere sampled (muted 7.0:1, warn 7.6:1, ok 7.9:1); muted light text passes (5.4:1 on surface, 4.95:1 on bg).
Fix: in light `:root` set `--middle:#8F5710; --back:#1E6E52;` and for pressed tier chips use `color:var(--fg);background:var(--*-soft);border-color:var(--*)`.

8. Explorer empty state is a dead end: search is silently scoped to the selected domain/tier ("cash" with analytics selected → 0 results, "No APIs match. Clear a filter.") but there is no clear control, and the search box keeps its value when the tier changes.
Fix: render a `<button class="btn">Clear filters</button>` in `.empty` that resets curTier='all', curDom=null, #apiSearch and #stab, then rerenders; optionally show "0 in analytics · 4 across all domains".

9. Screen-reader state: `[role=tablist]` tabs lack `aria-controls`, panels lack `aria-labelledby`, and every tab is a tab stop (22 Tab presses to pass the lifecycle figure). `.lc-node`/`.layer` are `role=button` but never expose selection (no aria-pressed). No `aria-live` on #lcDetail/#archDetail/#reqDetail/#domHead, so keyboard/SR users get no notice that content changed.
Fix: set `aria-controls`/`aria-labelledby` and `id`s in the PANELS loop; roving `tabindex` on tabs; in setLC/setLayer toggle `aria-pressed`; add `aria-live="polite"` to the four detail containers.

LOW

10. localStorage resume: a returning visitor with no hash lands on whatever tab they last viewed (verified: reload → "Sources") with no "resumed" cue. Consider restoring only via hash, or a one-line "Resumed at lesson 11" note.
11. Mobile explorer: 11 stacked domain buttons push `#domHead`/`#apiList` below the fold, so tapping a domain gives no visible feedback. Fix: on narrow screens render `.domlist` as a horizontally scrolling row, or `domHead.scrollIntoView({block:'start'})` after selection.
12. Architecture hover and selected fills are identical (`--accent-soft`); selection differs only by a 2px stroke. Acceptable, but a `.layer.on text{fill:var(--accent)}` would help.
13. Flashcards read as plain cards until the eye finds the small "SHOW ANSWER" label; add `.flash:hover{border-color:var(--accent)}` and a chevron. `.lc-node .tier` is 10px mono even at 1280.

WHAT WORKS WELL
Selection state is clear in both themes (lifecycle: accent fill + inverted text; layers: accent stroke+fill; hops: 0.35 opacity for future steps; domains: inset ring; chips: filled). Focus rings (2px accent outline) render on every control including SVG `<g>` nodes in light and dark. Enter/Space activate SVG nodes. Hash routing, Next/Prev pagers with lesson names, and the "Open X in the explorer" cross-link (preselects tier + domain) are good wayfinding. No horizontal overflow at 1280 on any tab.

SCREENSHOTS
/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ux_review/shots/390-lifecycle-node5.png (unreadable SVG, header height)
/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ux_review/shots/390-architecture-hosting.png (unreadable layers, 10px-tall Hosting target)
/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ux_review/shots/390-01-overview.png (mobile overview, full page)
/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ux_review/shots/1280-dark-focus-lc-node.png (dark selection + focus ring)
/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ux_review/shots/1280-explorer-empty.png (empty state with no clear control)

Full log: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/ux_review/log.txt; scripts review.js and probe.js in the same directory. The HTML file was not modified.
