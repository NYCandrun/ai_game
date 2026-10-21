# Change log: nine targeted edits

- **Base:** the 19-page working version, whose cover reads "Clients' AI tools could act on Aladdin under the same controls BlackRock uses for its own business." The uploaded `Aladdin_Studio_Prep_1.pdf` is word-for-word identical to it.
- **Source:** its editable HTML.
- **Output:** `Aladdin_Studio_Prep_2.html` and `Aladdin_Studio_Prep_2.pdf`.

## The nine edits

1. **Executive summary, page 2.** "An AI tool calling these APIs would work under the same controls" now reads: "An AI tool calling these APIs would face Aladdin's existing API access and service controls, but would not automatically inherit Copilot's AI guardrails." The cover is unchanged.

2. **Finding 2, page 9: the 17x forecast.**
   - The attribution sentence now reads: "The forecast covers API calls across BlackRock and Aladdin together, not Studio specifically. Studio is one route through which those calls could grow." Its source 14 superscript and its Studio-page link went with the old sentence. Source 14 is still cited elsewhere.
   - Two other sentences implied the forecast was about Studio, so I corrected them too:
     - In the same finding, "BlackRock's two growth bets both run through Studio" now reads "Studio is one route for both of BlackRock's growth bets."
     - In Part 3, "It projects API calls to grow 17x" now reads "It projects API calls across BlackRock and Aladdin to grow 17x".
   - No figures, dates or call counts changed.

3. **Part 3 and Exhibit 14: which controls carry over.**
   - **Part 3 sentence:** "A client's AI tools would work under controls BlackRock already relies on…" is replaced with your three sentences, word for word.
   - **Third condition:** it now reads "And BlackRock would have to make appropriate controls available to external AI tools it did not build."
   - **Exhibit 14 note:** "The right-hand controls show how BlackRock governs AI on these APIs today, which is the model a client's own AI tools could follow" is replaced with your caption. Your semicolon became a full stop, following the no-semicolons writing rule. The note keeps "Data Cloud, storage and the Data eXchange have their own access controls" and every existing source.
   - **Layout:** the exhibit's boxes and layout are unchanged.

4. **Exhibit 15, page 13: rows reordered to RFPs, rebalance, named client, AI tools.**
   - **Row 1:** "and how a client's own AI tools would connect" is replaced with your sentence.
   - **Row 3:** now has your case-study description.
   - **Row 4:** now has your "Once BlackRock validates and decides to offer a dedicated integration…" description. Its success measures now begin "After launch:", so publishing the page is not read as a near-term commitment.
   - **Row 2:** written in Edit 4, then replaced by Edit 9.
   - **Existing:** every other success measure, and the three-column design, are unchanged.

5. **Finding 3, page 9.** I added the requested qualification, then removed it when Edit 6 replaced it, as you instructed. It does not appear in the final document.

6. **Finding 3, page 9.** "So I infer that Copilot and Studio use the same APIs" now reads: "Copilot's tools call production Aladdin APIs, and Studio gives clients access to documented Aladdin APIs. Whether the two sets overlap, and by how much, is not public." There is no added caveat after it. The Copilot material and Exhibit 11 are unchanged.

7. **Exhibit 14 and Part 3: API access versus a dedicated connector.**
   - **The "Its AI tools" tile** now reads: "Can call documented APIs using Studio credentials. No dedicated AI connector or access to Copilot's tool registry is public."
   - **Room for the new text:** the tile's two "Nearest public sign: a job posting naming MCP" lines were removed. That fact and its source 73 stay in the note. The tile's line spacing is a little tighter, at the same font size.
   - **The note** now says which part of the hatched box is public: calling the APIs with Studio credentials, per the SDK README (source 29). It says that a dedicated AI connector and access to Copilot's tool registry are not public.
   - **Part 3:** "How those tools would connect is not public" now reads: "They can call documented APIs with credentials registered in Studio[29]. No dedicated AI connector, or access to Copilot's tool registry, is public."
   - **Screen-reader description:** the diagram's description was updated to match.
   - **Not added:** any MCP or A2A proposal.

8. **Broad claims about shared controls.**
   - **Part 3 opening:** now reads "Calls through Studio would use Aladdin's applicable API permissions and service controls. Copilot's AI-specific controls would not automatically carry over."
   - **Exhibit 14 title:** now reads "BlackRock's applications and client programs can call Aladdin APIs. Copilot adds AI-specific controls that external tools would not automatically inherit."
   - **Executive summary:** now reads "BlackRock already uses Copilot across about 100 Aladdin applications, with tools that call production Aladdin APIs."
   - **Cover:** unchanged.

9. **Exhibit 15 row 2, the rebalance.** It now has your description, with one change: "clients build" became "clients can build". Source 6 sits on the what-if and compliance clause, and source 10 on the rebalancing clause. The success measures are unchanged. The text no longer names an authorization operation in the Order API.

## Checks

- **Citations:** 104 sources, all cited. They are in order of first citation, with sequential numbers. Source 29 gained two superscripts. One superscript to source 14 was removed with the deleted sentence.
- **Exhibit numbers and cross-references:** unchanged. Exhibit 3's note still reads "Controls as in Exhibit 14."
- **Cover:** Part 4 now shows page 14, because of the reflow below.
- **Pages inspected:** 2, 9, 12, 13 and 14, plus the pages that follow 14.

## Issues not resolved

1. **The document is now 20 pages, not 19.**
   - **Cause:** the new text adds about six lines to page 12, which had room for about three. Exhibit 14 is set to stay whole, so it moves to page 13 with Exhibit 15. Part 4 starts on page 14.
   - **Result:** white space at the foot of page 12 and the foot of page 14.
   - **What I tried:** tightening the new wording recovered about one line. I then restored your exact wording.
   - **Another option:** placing Exhibit 14 right after the controls paragraph fills page 12, but it is still 20 pages, with the gaps moved to pages 14 and 15.
   - **What 19 pages would take:** cutting about six lines elsewhere, which is outside this revision.

2. **"Clients build" became "clients can build" (Edit 9).** Your wording says BlackRock identified rebalancing tools as something clients build. The webinar source (source 10) says "if clients want to build … their secret sauce rebalancing tools … they can absolutely do so." That describes what clients can do, not what they have done.

3. **The executive summary now says the same thing twice (Edit 8).** The new sentence is followed by the existing "About 100 of its applications carry Copilot. Each Copilot tool matches an Aladdin API already in production[9]." I left both, because the rest of the summary was out of scope. Merging them would mean deleting the middle sentence and keeping source 9 on the last.

4. **Broad wording outside these nine edits is unchanged:**
   - the executive summary heading: "Clients' AI tools could act on Aladdin under the same controls BlackRock's own business runs on";
   - "Part 3 sets out this direction: clients' AI tools acting on Aladdin under BlackRock's own controls";
   - the executive summary's 17x sentence, which does not say "across BlackRock and Aladdin" but also does not name Studio;
   - the Finding 2 heading, "BlackRock's growth story to investors runs through Studio".
