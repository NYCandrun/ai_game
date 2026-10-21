# PMM onboarding research kit

`PROMPT.md` is the prompt. This file explains how to use it.

## How to use it

1. Create an empty private GitHub repository for the company.
2. Optionally, put anything you already have in a folder called `00-inputs/` at the top of the repo. For example:
   - PDFs, decks, transcripts or exported pages;
   - a list of links;
   - your own notes, questions or the job description for your role;
   - a design guide for the final deliverable: a brand guide, a sample HTML or PDF page, fonts, or a template.
3. Start a fresh Claude Code session on the repo, in the cloud or locally.
4. Send the company's URL as your chat message, with `PROMPT.md` attached or pasted below it.

The run goes straight through without stopping. It still writes a coverage report and a list of pages it could not reach, so you can check them afterwards. Expect a few hours and dozens of agents. The prompt asks for a workflow, which is what lets it orchestrate agents at that scale.

## Notes from the Aladdin Studio project that shaped this prompt

- **The best evidence was rarely on the product pages.** It came from:
  - API specifications inside public packages;
  - job postings;
  - a customer's proxy statement;
  - government tender records;
  - captions files on the company's media CDN;
  - executives' podcast appearances.

  The channel list above is built to reach those.
- **The errors that survived longest were conceptual, not factual.** The facts were right but tied together wrongly: a diagram arrow, a "runs on", a shortened quote that turned an aim into a fact, or a quote attributed to the wrong speaker. That is why verification checks meaning and speakers, and why Phase 5 has a technical product marketer.
- **Agents' hand-back summaries miss things.** Reading the full reports found fixes the summaries left out.
- **Some sites block automated access.** Plan for a short list of pages to open by hand.
- **Machine transcripts need a spot-check** wherever a quote carries weight.
- **Leave out the heavier rounds for onboarding.** These are the adversarial audit, the expert panel and the extra-information cut. They are worth running only when a document goes to someone outside the company. Phase 3 and Phase 5 are enough for onboarding.
