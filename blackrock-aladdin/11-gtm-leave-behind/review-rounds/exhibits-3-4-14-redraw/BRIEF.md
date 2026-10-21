# Redraw Exhibits 3, 4 and 14 as a matched set (separate preview)

The author approved a v24 of "Aladdin Studio from the outside". A separate agent is applying the text changes to scratchpad/v24/preview.html. Your job is ONLY to draw Exhibits 3, 4 and 14 again, as one connected set, for the author to review separately. If the author likes them, they will be folded into v24 later. Do not edit preview.html or any document.

## Inputs (read them)
- **v23 HTML:** scratchpad/gtm/out/Aladdin_Studio_With_AI.html. Exhibit 3 and Exhibit 4 are on page 4 and Exhibit 14 is on page 12. The v23 PDF is scratchpad/gtm/out/Aladdin_Studio_from_the_outside_v23.pdf. Reuse the document's own CSS, fonts and colours exactly, so the new exhibits drop in.
- **Decision 3 in the approved review:** scratchpad/review24/Proposed_v24_changes.html.
- **Editor's shared vocabulary and key:** scratchpad/fixpanel/out_editor.md, section 7.
- **Proposed Exhibit 14 designs:** scratchpad/fixpanel/out_tpm.md (section 3, two routes) and scratchpad/fixpanel/out_eng.md (fix 11, three bands by where each control is enforced).
- **Text fixes for these exhibits** in the review: fixes 6, 9, 12, 20, 29, 30, 37, 38, 58 and 61. Fix 61 adds a Spaces item, and the author chose to keep it. The approved thesis is "Through Studio, clients' own AI tools could use the tools Copilot uses, acting for each user under that user's Aladdin permissions."
- **Primary sources, to check any label you add:** the API specifications in scratchpad/unpacked/ and the Rosales transcript in /home/user/ai_game/blackrock-aladdin/04-transcripts/.

## Design requirements (from the author)
- **Read as one set.**
  - Exhibit 3 is the map.
  - Exhibit 4 zooms into Exhibit 3's Studio box.
  - Exhibit 14 extends Exhibit 3's layout with the controls and the routes.
  - Use the same names, colours and visual key in all three.
  - A reader who saw Exhibit 3 should recognise Exhibit 14 at once.
- **Clean and easy to understand.** Do not crowd them.
- **Exhibit 3:** keep the author's layered style, but put "Built by BlackRock" (BlackRock's applications and Copilot) side by side with Aladdin Studio, above the shared services. "Who builds" points to Studio only. The controls panel attaches to Studio only and ends at the shared layer. Data Cloud and ADX sit inside Studio, with data flowing both ways. Keep the Hosting row with Microsoft Azure and Amazon Web Services as solid boxes, because the author asked for this. Studio is yellow.
- **Exhibit 4:** the same yellow Studio box, opened up. Draw the APIs once, as the shared layer, and turn Studio's tile into "API access" (OAuth apps and tokens). Keep the workspace panel, including Spaces (fix 61). Apply the tile wordings from fixes 20, 38 and 58.
- **Exhibit 14:** use Exhibit 3's layout and add where each control is enforced.
  - (1) Shared, inside Aladdin's services: Aladdin user permissions, compliance on order posts, and the order workflow, in which a portfolio manager authorizes and the public API has no call to authorize.
  - (2) At each connection: Copilot's registry rules (environment, user group, app) on Copilot's link, and credentials and OAuth scopes on Studio's links.
  - (3) Inside Copilot only, attached to the Copilot box and not drawn as a foundation layer: input and output guardrails, planning, and AI-graded tests.
  - Show two client AI routes. The direct route through Studio credentials is solid, because it exists today. The route through Copilot's tools is dashed and labelled "proposed: MCP server or A2A, my inference".
  - The legend covers boxes and arrows.
  - Left heading: "Built by BlackRock · used by BlackRock and clients".
  - Each client tile carries the Exhibit 4 part it uses.
- **Wording:** every label must be true to the sources. Follow the author's rules:
  - Plain English.
  - No em-dashes.
  - No semicolons joining sentences.
  - Never "suggested".
  - Say things explicitly.
- **Notes and citations:** each exhibit keeps a note and a source line with superscripts in the document's style. Use v23 source numbers.

## Output (in scratchpad/v24/exhibits/)
- **Exhibits_3_4_14.html:** a standalone page that uses the document's CSS. Page 1 has Exhibits 3 and 4. Page 2 has Exhibit 14.
- **Exhibits_3_4_14_compare.pdf:** a four-page vector PDF.
  - Page 1: the v23 page 4 (Exhibits 3 and 4). Extract it with pdfseparate.
  - Page 2: the new Exhibits 3 and 4.
  - Page 3: the v23 page 12 (Exhibit 14).
  - Page 4: the new Exhibit 14.
  - Each page gets a yellow label bar at the top: fill (1, 0.81, 0), Helvetica-Bold 11, with text such as "v23 (current): Exhibits 3 and 4" or "Proposed: Exhibits 3 and 4". Use pypdf and reportlab to merge the bar onto each page.
  - Render the HTML with: `cd /home/user/ai_game && node /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/htmlrev/tools/render_chromium.js IN.html OUT.pdf`
- **NOTES.md:** every label and the source behind it, the shared key, and anything you were unsure of.

Look at your renders (pdftoppm, then view the PNG) and iterate until they are clean. Reply with a short summary and anything that needs the author's judgment.
