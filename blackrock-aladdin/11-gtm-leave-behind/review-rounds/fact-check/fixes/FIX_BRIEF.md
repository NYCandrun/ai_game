# Drafting fixes for fact-check findings (do not edit the document)

The document is "Aladdin Studio from the outside", a 19-page leave-behind an applicant for a BlackRock product-marketing role will send to BlackRock's head of go-to-market. It must be accurate, sourced and plainly written. A fact check found claims that are wrong or partly wrong. Your job is to DRAFT the exact fix for each finding in your group. You must not modify any file except your own outputs.

## Inputs
- Your findings: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix/GROUP.json (each has the claim, the finding, the receipt with the quoted source). Page numbers are from an earlier version; text may have moved a page.
- Current document HTML: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix/current.html (the text you replace must come from here, exactly). Plain-text render: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix/current.txt.
- Sources register is inside current.html: entries `<p id="sN"><b class="n">N</b><span class="g">P|S|T</span><span class="t">title</span>. rest. <a href=URL>URL</a></p>`. Citations are `<sup class="fnref"><a href="#sN">N</a>, <a href="#sM">M</a></sup>`.
- Fact-check rules and corpus map: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/CHECK.md. You may re-open the receipt URLs (WebFetch/curl) to confirm wording; use WebSearch at most 3 times in total.

## For each finding, decide one of
- FIX: rewrite the smallest span that makes it true. Keep the author's voice and meaning wherever the facts allow.
- CITE: the words are true; only the citation changes (point to an existing register entry, or add a new entry).
- NO CHANGE: the finding is pedantic or wrong; say why in one sentence, with evidence.
- DECIDE: the fix changes an argument or exhibit structure (e.g. a count in a title, a thesis sentence). Give the recommended fix AND the alternative, and say what else in the document must change with it.

## Style rules for new text (the author is strict about these)
- Plain English. Say what it means; no jargon, shorthand, or allusion. One idea per sentence, about 20 words or fewer.
- No em-dashes, no semicolons in new sentences, no parentheticals where avoidable.
- Do not state what the document is not saying ("this is not X"). Just state what is true.
- Never write "suggested". Do not claim that no other vendor runs its own business on its platform.
- Keep superscript citations on the clause they support. New sources get a full register entry in the existing format (grade P/S/T, title as published, publisher or speaker with title, exact date, URL). Mark new entries as NEW; numbering is redone automatically.
- Do not lengthen page 13 (Part 3 text plus Exhibit 14 must stay on one page) or page 2 materially.


## Author's rule added mid-run (applies to every draft; the consistency reviewer must enforce it)
- New text states only the correct fact. It must not mention, contrast with, or correct the old wrong fact. No "not eight but 13", no "rather than", no "in fact", no "previously reported", no "contrary to". A reader of the fixed document should never learn what the earlier version said.
- Do not cite a source only because it disproves the old wording. Cite sources that support the new sentence.
- Exception: recency of the Bloomberg announcement may be stated, e.g. "Bloomberg launched an MCP server for its data in late September 2026".

## Output
1. /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix/out_GROUP.json: a list of objects {id, action: FIX|CITE|NO CHANGE|DECIDE, current_html (exact substring of current.html, unique, include enough context to be unique), proposed_html (same span rewritten; empty for NO CHANGE), new_sources (list of full register entry HTML, or []), also_change (other places that must change for consistency, with their exact current text), why (one or two plain sentences, citing the receipt)}.
   Check with python that every current_html occurs exactly once in current.html. If two findings touch the same span, merge them into one object listing both ids ("id": "p13-06+p13-07").
2. /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc/fix/out_GROUP.md: the same as a readable list: id, action, current text (visible words, not markup), proposed text (visible words), why.
Reply with counts per action and the ids you marked DECIDE.
