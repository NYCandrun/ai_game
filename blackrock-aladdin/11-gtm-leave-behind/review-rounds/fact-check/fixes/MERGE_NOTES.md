# Merge notes: FIX_PLAN v1 to v2

Inputs: FIX_PLAN_v1.json (105 items, kept as a copy) and the three readability reviews (read_p01_07.md, read_p08_14.md, read_p15_22.md). Output: FIX_PLAN_v2.json, now also FIX_PLAN.json (105 items: 14 DECIDE, 78 FIX, 10 CITE, 3 NO CHANGE). Every current_html and every also_change current_html occurs exactly once in current.html. The build script is /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/v2work/build_v2.py.

**Final preview: 20 pages** (v1 preview: 22; original: 19). The one extra page is Sources, which grew by 30 new entries.

## Layout check of the final preview.pdf

- Exhibit 9 is back on page 8 with Exhibit 8. Its note is on page 8 too.
- Part 3 text and Exhibit 14 share page 13.
- No page is near-empty except the natural ones. Page 12 ends Part 2 before Part 3 starts a new page, as in the original. Page 20 is the end of Sources. The Exhibit 17 closing paragraph sits under the exhibit on page 15.
- No table cell ends on one word plus a superscript. A browser check at print width found none. It flagged "specification" in Exhibit 2, step 5, but the page image shows "configuration specification" on that line, so that flag is false. No superscript run splits across two lines.
- No box text overflows in Exhibit 3 or Exhibit 14. I checked both at 160 dpi.
- Kept as they are: the Finding 2 heading, and the "Data and cloud platforms" band of Exhibit 17. Both changes are alternative-only, and the fixed apply_preview.py skips them.

## Structural changes

- **p05-41 and p05-32 merged** into "p05-41+p05-32 (Exhibit 3 note)". The note is now one rewrite. It has two plain sentences and one source list grouped by source, with 8 superscript groups and 4 printed lines. In v1 it had 6 lines and 18 superscripts. The note also_changes of p05-04, p05-16, p05-29, p05-36 and p05-15+p05-44 were removed, and the consolidated note carries their citations. The main span of p05-15+p05-44 is now the Studio box subtitle.
- **New item "layout (table cells ending on one word plus a superscript)"**. It is layout only. It adds a non-breaking space in eight cells: Exhibit 2 steps 1, 3 and 5 (two cells), the Exhibit 6 Goel receipt, the Exhibit 9 PPF and PBGC buyer names, and the Exhibit 12 LSEG receipt. Most of these problems were already in the original. The same fix sits inside s31 ("May 2026") and p15-08+p15-10 ("plugin builder").
- **p15-114** goes from CITE to FIX. The sentence drops its citation, because the Exhibit 17 source note directly above cites every page tested.

## Specific issues from the brief

- **Exhibit 9 back on page 8.** The Nest cell is now "Nest chose BlackRock’s Aladdin over six other bids" with the Nest release. The PPF and PBGC cells use the reviewer's shorter text.
- **Exhibit 7.** The four tick columns are replaced by one "Parts they name" column, 108pt wide, which is the old width of the tick columns. So the quote column is as wide as in the original, and every row is two lines. The title is "Four speakers describe parts of Studio, and only Woodhead names them all". The paragraph now opens "Khara, Newman, Goel and Woodhead describe..." and puts Woodhead second. It calls the job posting one "for a product director of Aladdin Studio Developer". It closes with "APIs and data access recur across speakers and years", which every row supports. The alternative (drop Khara) uses the same three-column layout.
- **Exhibit 3 arrows.** With the new title, the arrow from the Apps panel into the API bar still drew every app calling one API layer. The smallest SVG change is text only, in p05-16: the bar is renamed from "Shared API layer" to "Shared services and APIs", with the subtitle "used by apps, Copilot and Studio · public calls need credentials". The arrows then match the Studio page's "shared services". No arrow is removed. The aria label follows. Under the p05-01 alternative the bar keeps its name, as the decide note says.
- **Exhibit 17 orphan.** About 3.5 lines are won back. The Call to action definition joins the AI connector note in one paragraph (p15-38, both options). The scale sentence points to the key instead of restating it (p15-116). The p15-118 sentence is shorter. The title drops "exists" and fits on one line. The p15-114 superscripts are gone.
- **Register.**
  - The Technical Writer entry now reads "Job posting: Technical Writer, Vice President (Edinburgh). BlackRock, posted February 21, 2026, removed February 23, 2026. Copy kept by Built In Bristol."
  - The AWS release no longer gets a duplicate entry. p03-36 and the Exhibit 1 note cite the existing entry (s15), which now lists the full release with its questions and answers (TradingView copy) and the Amazon copy.
  - The Whole Portfolio entry uses the canonical URL https://www.blackrock.com/aladdin/platforms/products/whole-portfolio.
  - The Bloomberg release now links PR Newswire's copy, found with 2 web searches and checked for the title and the Sept. 29, 2026 dateline: https://www.prnewswire.com/news-releases/bloomberg-launches-enterprise-mcp-to-seamlessly-connect-bloomberg-data-with-clients-enterprise-ai-applications-302891331.html. The Exhibit 12 receipt link uses it as well.
  - s60 now reads "Job posting: Forward Deploy Engineer, Aladdin Data, Associate (R264906, Mumbai). BlackRock, posted September 4, 2026. Removed from BlackRock Careers by October 20, 2026. Copy kept by Saarthi."
  - s31 now reads "Snowflake video, May 21, 2026".

## Reviewer text adopted (WORSE or BROKEN, plus some SAME)

- Page 2: p02-05+p02-06+p02-07 (three short sentences). p02-09+p02-10 ("matches an Aladdin API already in production"; the alternative is split as well).
- Page 3: p03-14 (no colon list). The Exhibit 1 note fits on one line.
- Page 4: p04-06 ("beside the original"). p04-11 keeps "resolution comment". p04-28 drops "Examples are". p04-43 cuts the Order Monitor aside.
- Page 5:
  - p05-30 has the shorter caption.
  - p05-47+p05-48 title: "Studio, grouped here into six pieces". The alternative is "eight pieces".
  - p05-48+p05-50 drops the 48-of-54 pattern, and the superscript sits after "Aladdin Graph".
  - p05-65 uses shorter sentences.
- Page 6: p06-63+p06-64 is four short sentences. p06-66+p02-14 reads "I pulled about 125 recordings. Five BlackRock speakers in them describe Studio or its parts", with no semicolon.
- Pages 8 to 13:
  - p08-35 and p08-40+p08-41+p08-42 are shorter.
  - p09-01 replaces both lead sentences, so "to 2030" is said once.
  - p10-07+p10-10+p10-13 puts the inference after its premise and before the Crockett quote.
  - p10-25 is back to a 4-line box.
  - p11-34: the Bloomberg row fits on one line.
  - p11-35 reads "which user groups may use each tool".
  - p13-06+p13-07+p13-08+p13-09 reads "The team that owns each tool".
  - p13-37: the box title is "Access set per API", and the p13-aria label matches.
- Pages 14 to 16:
  - p14-15 has one "or" list and no semicolon.
  - p14-25 gives the Technical Writer posting its own "job posting" label.
  - The Exhibit 16 note now makes clear that "it" is the column.
  - p15-118 recommends "a first API call needs a contract or a relationship". The alternative title narrows to the first call.
  - p15-119 reads "allow a first API call only for licensed clients".
  - p16-02 reads "They also include". Its span now runs to the next sentence, so "endorse it" became "endorse this analysis", because "it" had become unclear.

## Not adopted

- Reviewer note on Exhibit 4: the note still says "BlackRock gives no count" beside the hedged title. Both stay, because the count is the finding.
- p15-08+p15-10: the optional "merged by a BlackRock engineer" wording was not used. The drafted wording is accurate and the row fits.
- The p15-31... source note keeps its 26-number superscript run. Dropping it would leave those register entries uncited.
