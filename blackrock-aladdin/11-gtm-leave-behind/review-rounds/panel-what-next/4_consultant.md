# Aladdin Studio leave-behind: a commercial read

## 1. What the evidence indicates

**Direction.** BlackRock is positioning Aladdin as a platform with an extensibility layer, and Studio is that layer. Exhibits 3 and 4 (four executives, same three parts, 2024 to 2025) plus the 2026 job posting calling Studio "Aladdin's extensibility layer" make this a strong inference. The weaker claim is the headline: "Studio is the product behind the growth story." The 17x API-call figure (page 2, Investor Day slide) sits on a cost-of-growth slide, and the 10-K says fees are set by positions on the platform or at a fixed rate, not by API calls (Finding 2). Exhibit 7 and Exhibit 13 show Copilot and 100 internal apps calling the same API layer, so 17x could be mostly Copilot and internal traffic. Moderate inference at best: Studio is a stickiness and expansion lever, not a revenue line.

**Position.** Exhibit 2 says Studio sells like every other system of record: gated, relationship-first, a 4 against Bloomberg's 5. The strong inference is that gating is the category norm, not a Studio defect. The gap that matters is Exhibit 14: eight of nine comparators have announced AI access, and Aladdin's only evidence is a Mumbai job posting. Moderate strength, because Exhibit 13 shows the machinery already exists inside the login. Exhibit 9 adds a maturity signal the document does not draw out: trading, compliance and accounting, the domains a client would build "secret sauce" on, are mostly alpha.

**Buyer.** Exhibit 15 and the Sewdass and Schafer quotes describe an asset-manager COO or CTO mid-way through a build-versus-buy decision, whose RFP now has an "API suite and connectors" section. Self-selected audience, no n given: weak on representativeness, strong on direction. The Janus Henderson pull requests and the SDK's Azure API Management settings (page 4) say the actual user is a platform-engineering team behind a gateway. Strong, small sample. Exhibit 11 is mixed on pricing power: PPF above estimate, PBGC flat for six years.

## 2. The buried insight

Finding 3 says it and walks past it: Copilot's tools map one-to-one onto production Aladdin APIs, the same ones Studio exposes, with per-user permissions, OAuth scopes and four-eyes approval already in the specifications (page 9). So every Copilot deployment is a Studio proof point, and external agent access is a packaging and governance story, not an engineering programme. With poll 2 ("AI and data demands" at 42 percent), it is the strongest commercial lever in the document, and it sits in a sidebar.

## 3. Over-claimed, missing, wrong

- The executive-summary KPIs oversell. JPMorgan's $25.6M (Exhibit 10) may be Aladdin Provider custody fees; the footnote says so, the headline does not. Zero Studio mentions on earnings calls (Exhibit 12) is evidence about investor messaging, not product priority.
- Exhibit 2 weights eight criteria equally and scores vendors whose pages blocked the crawler. It describes selling models; it does not establish disadvantage.
- Missing: Studio attach rate across the "hundreds of clients," packaging and price (Data Cloud is an add-on; is Studio?), win/loss data, PyPI download counts for the SDK (public, uncollected), any segment view, and Snowflake, Fivetran, Microsoft and AWS treated as channels rather than vendors.
- Before acting I would want API calls by client and domain, Compute sessions, Data Cloud consumption, and a count of recent RFPs that asked the Schafer question.

## 4. First six months

1. **Write the positioning and messaging source document first.** Exhibits 3 and 4 show BlackRock already has a consistent three-part definition, but it lives in podcast transcripts; the Studio page says "Create & automate" (Exhibit 1). Marketing produces one messaging house: definition, three named users, proof points, claims product has approved. Owner: this role. Metric: adopted by sales, web and solutions engineering by month two. First, because every other move needs an agreed story and it costs nothing but alignment.
2. **Named reference programme.** Studio's page names no client while the public record (Exhibits 10 and 11, Janus Henderson's commits) already does. Marketing produces two client stories: Janus Henderson first, whose engineers are on GitHub, then one public pension. Metric: two named Studio stories by month six.
3. **RFP answer kit.** The Schafer quote says the API section is now prominent. Marketing produces Exhibit 9 as a sales artifact, the governance story from page 9 as a one-pager, and a Snowflake and Databricks connectivity answer. Metric: usage in RFPs, win-rate delta.
4. **Publish the Copilot plugin model as developer-facing content.** Exhibits 13 and 14: eight comparators have an AI story and Aladdin's is a job posting, though the controls exist. Marketing produces a governance paper and an analyst briefing. Metric: paper live by month four.
5. **Open the "Read" and "See the catalog" steps of Exhibit 1.** Marketing produces a public catalog page listing API names and domains, no sandbox. Engineers in RFP teams unpack PyPI today. Keep gating; remove the friction that makes BlackRock look evasive.

## 5. What the "what next" boxes should say

Each box should name what marketing produces, who owns it, the metric and the evidence still to collect.

- **Finding 1:** Marketing produces two client stories from the public-record list; ask Janus Henderson first. Owner: PMM with client business. Metric: a named logo on the Studio page by Q2. Evidence to collect: reference permission.
- **Finding 2:** Drop API calls from Studio messaging; the 10-K does not tie fees to them. Message Studio as the way clients get more workflows and data onto the platform, internally and externally. Evidence to collect: Studio attach rate and usage by client, so claims rest on numbers.
- **Finding 3:** Marketing produces a governance paper on the plugin model and briefs analysts on it. Owner: PMM with AI product. Evidence to collect: what product will let marketing say about external agent access, and the client asks that justify it.
- **Finding 4:** Marketing produces an RFP kit and positions compliance reporting (53 percent) as the first workload for Studio plus Copilot, after checking Exhibit 9: three of four compliance specifications are alpha. Do not promise what the API cannot carry. Owner: PMM with solutions engineering. Metric: RFP inclusion and win rate.
