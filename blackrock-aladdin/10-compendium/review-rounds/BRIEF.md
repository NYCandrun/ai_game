# Reviewer brief (one recording per reviewer)

You are checking a reference document against one recording's transcript, by reading, not by searching. Do NOT use grep, rg, or any search tool, and do not skim: read the files with the Read tool, in full, start to finish.

Step 1. Read the whole document: /tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/compendium/compendium.md (about 20,000 words, three parts: Aladdin, Aladdin Studio, BlackRock; every sentence ends with a source tag in square brackets). Read it in portions with offset and limit until you reach the end. Keep notes of every statement that could relate to your recording: the topics, the speakers, the numbers, the quotes, and the tags that cite your recording.

Step 2. Read the whole transcript of your recording (path given to you), start to finish, in portions. It is either published captions or an automatic transcription; names may be misspelled.

Step 3. Write your findings to the output path given to you, in Markdown, with exactly these headings:

## Recording
Title, source page, who speaks (names and titles as the transcript gives them, with obvious misspellings normalised and flagged), what the recording is about in three sentences.

## Discrepancies
Every place where the document says something this recording contradicts or states differently: a wrong number, a wrong attribution, a quote that is not verbatim, a wrong date, a speaker title that differs, a claim the recording undercuts. For each: the document's sentence (copied exactly, with its section number), the transcript's wording (copied exactly, with its timestamp or position), and what the correction would be. If there are none, write "None found."

## Confirmations
Document statements that cite this recording (or clearly rest on it) that the transcript confirms, one line each with the section number. Keep this short.

## Additions
Facts in this recording about Aladdin, Aladdin Studio, eFront, Preqin, Aladdin Data Cloud, Copilot, BlackRock's organisation, named clients, named products or capabilities, numbers and dates, that the document does not carry. Quote the transcript verbatim with a timestamp or position, and name the document section (1.x, 2.x or 3.x) where it belongs. Skip market commentary that is not about the platform or the firm.

## Confidence
One paragraph: how well you could hear/read the recording (caption quality), and anything you were unsure about.

Rules: quotes verbatim; no advice; no edits to any file other than your output file; report back with a short summary (counts of discrepancies and additions) when done.

## Two clarifications (added after launch)
1. Scope. Only a part of the document concerns your recording. Judge only the statements your recording bears on: those tagged with it, and those on the same topics, people, products or numbers. Do not flag statements your recording says nothing about; the absence of a topic from your recording is not a discrepancy.
2. Suggested edits. Add a final heading "## Suggested edits". For each discrepancy and for each addition you consider worth carrying, write a concrete edit: the section number, the exact current sentence (or "new sentence after: ...") and the exact replacement or new text, with its source tag in the document's style, for example [T2-047 Introduction to Aladdin Climate, 2024]. Keep the document's voice: declarative, no advice.
