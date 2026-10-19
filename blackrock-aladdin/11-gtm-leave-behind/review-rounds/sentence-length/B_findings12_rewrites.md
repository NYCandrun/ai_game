# Sentence-length rewrites: Findings 1 and 2 (pages 10 and 11)

Scope: sections `#f1` and `#f2` of the HTML, including the Exhibit 10 chart notes and SVG aria-label, the Exhibit 11 and 12 tables and their source notes, both exhibit titles, both "What this finding suggests about direction" boxes (the Finding 2 box falls on page 12 but belongs to the section). Word counts are whitespace tokens; a hyphenated word (open-source, 10-K) counts as one.

My own re-scan found four sentences at 30 words or more. Two of them were on the splitter's list, one was on the list but counted differently (the splitter tokenised "SDK :" and "headers ," as separate words), and one the splitter missed. One item on the splitter's list is a false positive. No table cell, caption or source note other than those below is over 30 words; the longest remaining prose sentences are 29 words (JPMorgan payments, page 10) and 27 words (Microsoft Azure, page 11).

---

## 1. Page 10, Finding 1, body paragraph after Exhibit 10 (on the splitter's list, 32 by its count, 30 by mine)

**Current text (HTML):**

> In December 2025 a Janus Henderson engineer submitted two changes to the <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a>: <a href="https://github.com/blackrock/aladdinsdk/pull/52">URL rewriting</a> and <a href="https://github.com/blackrock/aladdinsdk/pull/53">custom headers</a>, both for firms that route Aladdin calls through an enterprise gateway.

(No superscript on this sentence; the 32, 47, 48, 49 superscripts sit on the later "The commits name..." sentence and are untouched.)

**Rewrite:**

> In December 2025 a Janus Henderson engineer submitted two changes to the <a href="https://github.com/blackrock/aladdinsdk">open-source SDK</a>: <a href="https://github.com/blackrock/aladdinsdk/pull/52">URL rewriting</a> and <a href="https://github.com/blackrock/aladdinsdk/pull/53">custom headers</a>. Both are for firms that route Aladdin calls through an enterprise gateway.

- Sentence 1: 19 words (all three link phrases kept)
- Sentence 2: 12 words

---

## 2. Page 10, Finding 1, last body paragraph (splitter missed it; exactly 30 words, so not under 30)

**Current text (HTML):**

> Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public, so they are the natural first candidates for a named Studio story.

(No links or superscripts.)

**Rewrite:**

> Public pension funds, and firms whose filings or tenders already name BlackRock, are easier to name in public. So they are the natural first candidates for a named Studio story.

- Sentence 1: 18 words
- Sentence 2: 12 words

Note: this is a borderline case. If the rule is read as "30 or fewer" rather than "under 30", the original can stand.

---

## 3. Page 11, Finding 1, "What this finding suggests about direction" box (on the splitter's list, 31 words)

**Current text (HTML):**

> Adoption is growing among client types whose records are public: between 2023 and 2025, a bank’s proxy statement, an asset manager’s 10-K and three public pension buyers’ notices all record Aladdin.

(No links or superscripts.)

**Rewrite:**

> Adoption is growing among client types whose records are public. Between 2023 and 2025, a bank’s proxy statement, an asset manager’s 10-K and three public pension buyers’ notices all record Aladdin.

- Sentence 1: 10 words
- Sentence 2: 21 words

---

## 4. Page 11, Finding 2, Exhibit 12 title (on the splitter's list, 31 words)

**Current text (HTML, inside `<p class="ex-title">` after `<span class="ex-num">Exhibit 12.</span>`):**

> On 26 earnings calls from Q1 2020 to Q2 2026, no BlackRock executive said “Studio”, “citizen developer” or “agent”; Data Cloud, API and Copilot came up about four times in total

(No links or superscripts. Exhibit titles in this document carry no terminal full stop; the split replaces the semicolon with a full stop and leaves the end as it is. The Finding 2 heading already uses two sentences, so a two-sentence exhibit title fits the house style.)

**Rewrite:**

> On 26 earnings calls from Q1 2020 to Q2 2026, no BlackRock executive said “Studio”, “citizen developer” or “agent”. Data Cloud, API and Copilot came up about four times in total

- Sentence 1: 19 words (all three quoted terms kept intact inside their quotation marks)
- Sentence 2: 12 words

---

## False positive on the splitter's list: page 10, Exhibit 10 source note (38 words by the splitter)

The splitter's 38-word string is the SVG axis labels and bar values ("0 5 10 15 20 25 30 $ millions 2016 ... 25.6") run together with the first sentence of the source note. The actual sentence in the HTML is:

> Source: JPMorgan Chase proxy statements (DEF 14A), filed 2017 to 2026, by year of payment<sup class="fnref"><a href="#s2">2</a>, <a href="#s3">3</a></sup>.

That is 15 words. No rewrite needed. The other sentences in that note are 16, 13, 13 and 12 words. The SVG `aria-label` (not visible prose) is 28 words.

---

## Checked and under 30, for the record

| Page | Sentence (start) | Words |
|---|---|---|
| 10 | JPMorgan Chase’s proxy statements report Aladdin payments of $4.4 million to $7.6 million... | 29 |
| 10 | Janus Henderson’s 10-K says that in the third quarter of 2025 the firm chose... | 26 |
| 10 | Exhibit 10 title: JPMorgan Chase paid BlackRock under $8 million a year... | 25 |
| 10 | Exhibit 11 title and all cells | under 20 |
| 11 | Every sentence of the Finding 2 opening paragraph | 24 or fewer |
| 11 | Exhibit 12 cells and source note | under 20 |
| 11 | Microsoft wrote in December 2024 that all BlackRock’s technology platform clients... | 27 |
| 11 | In December 2025 BlackRock and AWS announced a second option... | 24 |
| 12 | Finding 2 direction box, all sentences | under 25 |
