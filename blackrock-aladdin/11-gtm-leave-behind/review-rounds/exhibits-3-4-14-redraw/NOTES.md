# Exhibits 3, 4 and 13 (v23's Exhibit 14) redrawn as one set: notes

**Renumbering.** Exhibits 6 and 7 are being merged, so v23's Exhibit 14 is now **Exhibit 13**. The page and every cross-reference use 13. The file names keep "3_4_14", as asked. Below, "Exhibit 13" means the redrawn exhibit, and "v23's Exhibit 14" means the old one.

Files in this folder:
- `Exhibits_3_4_14.html`: a standalone page. It reuses v23's whole `<head>` (embedded Barlow fonts and the print stylesheet) unchanged and adds one small stylesheet for the diagrams. Page 1 holds Exhibits 3 and 4. Page 2 holds Exhibit 14. Page numbers are switched off, so the page does not look like the real pages 1 and 2. Superscripts use the document's `fnref` markup and v23 source numbers. Their `#sN` targets resolve once the exhibits are folded into v24.
- `Exhibits_3_4_14_compare.pdf`: four vector pages. They are v23 page 4, the new page 1, v23 page 12 and the new page 2, each with a yellow label bar. The bars read "v23 (current): Exhibits 3 and 4, page 4", "Proposed: Exhibits 3 and 4", "v23 (current): Exhibit 14, page 12" and "Proposed: Exhibit 13 (Exhibit 14 in v23)". The link annotations were removed from the two v23 pages so their links do not point into the rest of the v23 file.
- `work/`: the builder (`build.py` = `head_part.py` + `body_part.py`), `compare.py`, `render.sh` and the check renders.

Decisions applied, in order of authority: the brief, the coordinator's later messages (the last one wins where they differ), Decision 3 and the fixes in the review, then the asides audit.
- Exhibit 3 stays complete. The only audit trim is dropping the timestamps from its source line.
- Exhibit 4 takes the audit's tile trims and the accuracy fixes 20, 38, 44, 58 and 61. The workspace panel stays, with Spaces and the Compute naming note. Labels that rest only on the SDK are marked as from "the public SDK".
- Exhibit 13 takes the audit's cuts of material that is not about Studio. It keeps everything about Studio: Studio as the client's route in, five client tiles with the Exhibit 4 parts they use, credentials registered in Studio, the gateway option, and the client AI route through Studio.

## 1. The shared key (identical in Exhibits 3 and 13, and referenced by Exhibit 4)

| Element | Meaning |
|---|---|
| Yellow fill, yellow border | Aladdin Studio only. In Exhibit 13 the yellow chips on the client tiles are Studio parts. |
| Pink fill | Aladdin Copilot only |
| White box, black outline | BlackRock's applications, and the client's own people and programs |
| Black band | Aladdin's shared services and APIs |
| Grey panel | Controls |
| Thin grey outline | Outside data (Exhibit 3's Outside inputs row, which v23 drew dashed) |
| Hatched box with a dashed outline | Proposed, my inference |
| Solid arrow | In the public record |
| Dashed arrow | Proposed, my inference |
| Two-headed arrow | Data moves both ways |
| Black numbered badges 1, 2, 3 (Exhibit 13 only) | Where each control applies: 1 shared, inside Aladdin's services. 2 at each connection. 3 inside Copilot only. |

Shared names across the three exhibits: "Built by BlackRock", "About 100 applications", "Aladdin Copilot, inside them", "About two thousand tools and agents. Each tool maps to an Aladdin API already in production", "Aladdin Studio, built on by clients", "API access" (OAuth applications and tokens), "Aladdin Data Cloud", "Aladdin Data eXchange (ADX)", "Aladdin Tools for Excel (ATX)", "Aladdin Compute", "Aladdin SDK", "Access set per API", "Compliance by default on orders", and "Aladdin's shared services and APIs".

## 2. Every label and its source

Sources are v23 register numbers. "Spec" means the 54 specifications in `scratchpad/unpacked/` (source 6). "Rosales" means `04-transcripts/timestamped/yt_oyqeCHFM5U4.m4a.ts.txt` (source 9), with times given.

### Exhibit 3 (complete, as the author asked)

| Label | Source and check |
|---|---|
| Who builds: client engineers, code-curious portfolio managers, data analysts, Excel users building reports | v23 wording, unchanged. Studio page 14 and ATX page 32. One bracket arrow points to Studio only (fix 12). |
| Row label "BlackRock's applications and Aladdin Studio" | This merges v23's two row labels, because the two now sit side by side. |
| Built by BlackRock | Decision 3 wording |
| About 100 applications, such as Explore, Dashboard and Risk Radar | Rosales 1:53 ("around 100 Aladdin front-end applications"). Explore from source 27, kept because Exhibit 3 stays complete. Dashboard and Risk Radar from the spec (the note keeps "The specifications also name Dashboard and Risk Radar"). |
| Aladdin Copilot, inside them | Rosales 2:32 to 2:41 ("embedded across all of those hundred front-end applications") |
| About two thousand tools and agents | Fix 37. Rosales 6:42 ("a couple thousands agents and tools"). |
| Each tool maps to an Aladdin API already in production | v23 said "matches". It is changed to "maps" so the set uses one verb (editor's vocabulary). Rosales 4:31 to 4:42 ("mapping one-to-one to an existing Aladdin API already out in production"). |
| Aladdin Studio, built on by clients | Decision 3 wording |
| Aladdin Data Cloud, Aladdin Data eXchange (ADX), inside Studio | Fix 37. The APIs, ATX and ADX pages list them as "Additional Aladdin Studio resources" (30, 32, 33). Data Cloud page 20. |
| API access: OAuth applications and tokens | Decision 3 tile. Spec security definitions (6). SDK README (29). It ties the box to Exhibits 4 and 13. |
| The developer and data layer. Exhibit 4 shows all its parts. | v23 Studio row text, reworded into two sentences. Woodhead (1). |
| Note: "Controls as in Exhibit 13" | v23 said "Exhibit 14". It is renumbered for the Exhibit 6 and 7 merge. |
| Controls in the API specifications: Access set per API, "Each API has its own OAuth scopes." Compliance by default on orders, "Posting an order runs compliance unless the caller turns it off, and returns any violations." | v23 text, unchanged. Checked against OrderAPI: `runCompliance` ("Default is true"), `complianceViolations` on `v1PostOrderResponse`, and OAuth scopes per API. The panel is attached to Studio's right edge and ends level with the bottom of the shared layer (fix 37 and the brief). |
| Portfolio management, trading, risk, compliance, operations, accounting | v23 |
| "Aladdin's shared services and APIs. Clients reach them through the 11 public API domains" | v23 said "reached through the 11 public API domains". The marketer's review (fix 12) noted that this says BlackRock's apps and Copilot reach the services through the SDK packaging, so the clause now names clients. The 11 domains are defined in the note (6, 29). |
| Hosting: Microsoft Azure, Amazon Web Services (solid) | Kept, as the author asked. 10-K (12) and Microsoft (35). The source line is unchanged. |
| Outside inputs: "The client's own and third-party data, stored with Aladdin data in Data Cloud or loaded into the Aladdin platform through the Data eXchange, and vendor data such as prices and ESG research" | An accuracy fix the author approved, replacing v23's "loaded into Data Cloud or through the Data eXchange", which read as one-way. The source line cites the Data Cloud page (20) and the ADX page (33) inside "BlackRock's Studio, APIs, ATX, ADX, Data Cloud and Aladdin Risk pages 14, 20, 30, 31, 32, 33", plus 34, 36 and 37. The outline changed from dashed to thin grey, because dashed now means "proposed". The two-way arrows are kept. |
| Two-headed arrows between Outside inputs and Data Cloud and ADX | Fix 37. ADX page 33 ("to and from Aladdin"). Data Cloud page 20 and release 34. |

### Exhibit 4

| Tile or item | Wording and source |
|---|---|
| Header: "Aladdin Studio, built on by clients · the yellow box in Exhibit 3, opened up" | Ties the zoom to the map |
| API access | Replaces the v23 "APIs" tile (Decision 3). "OAuth applications and tokens that let a program call Aladdin's APIs. The APIs themselves are the shared layer below." Spec (6) and README (29). |
| Event-driven workflows | Audit TRIM: "Events run on the same Aladdin Graph runtime" is cut. Fix 44: "No public specification covers business events." Sources 1, 41, 31 and 42. |
| Aladdin SDK | Fix 20, then the audit TRIM: "Open-source Python library with typed clients for the APIs and a Snowflake connection for Data Cloud." The audit cut "with login and retries built in" and the plugin-builder sentence. Source 29. It is marked "public SDK" in the note. |
| Aladdin Data Cloud | Audit CUT of "with Fivetran moving the data": "A managed data store on Snowflake". Sources 20 and 30. |
| Aladdin Compute | Unchanged. Source 43. |
| ATX | Unchanged. Source 32. |
| ADX | Audit TRIM: "Bulk file transfer to and from Aladdin". Source 33. |
| Developer guides and Data Dictionary | Author's wording, replacing fix 38: "Developer guides, Jupyter notebooks, code samples, and a Data Dictionary of Aladdin field definitions, as listed on the APIs page 30. The developer portal sits behind a client login 44." The two superscripts sit in the tile, on the facts they support. The research briefing quotes the APIs page (30) as listing the Data Dictionary, notebooks and code samples. Register 44 says the portal address redirects to the client login. The tile no longer describes the portal's insides. |
| Governance | Fix 38 quotes only "access management and usage monitoring". Source 45. |
| Workspace: Studio UI, API tokens and OAuth applications, Projects, Studio Compute sessions, Spaces (fix 61: "Named alongside Projects. Not described publicly"), S3 storage integration, ADC Admin Center, Studio notifications | v23 wording. Spaces was checked in the SDK clone: the `studio_notification` and `studio_subscription` specs list "STUDIO_NOTIFICATION_EVENT_TYPE_SPACE: Studio Space". Source 29. The note says these items are as named in the public SDK. |
| Shared strip: "Shared layer: Aladdin's APIs. They read and write Aladdin data, built on Aladdin Graph, BlackRock's firm-wide runtime for APIs and events." | The APIs are drawn once, as the shared layer (Decision 3). The text is the v23 APIs tile's, minus the agraph ID sentence (audit TRIM). Sources 38 and 39. |
| Note: "The public SDK uses both names, Studio Compute and Aladdin Compute, for the same hosted environment." | Fix 58. Checked: the README says "Aladdin Studio Compute sessions" and the code says "Aladdin Compute sessions". |

### Exhibit 13 (v23's Exhibit 14)

| Label | Source and check |
|---|---|
| Title: "Where each control applies: in Aladdin's shared services, at each connection, or inside Copilot only" | New. See section 4, item 1. |
| BUILT BY BLACKROCK · USED BY BLACKROCK AND CLIENTS | Brief. Copilot page 23, for client use. |
| About 100 applications | Rosales 1:53. The app names are cut (audit). |
| Aladdin Copilot, inside them / About two thousand tools and agents. Each tool maps to an Aladdin API already in production | Rosales 2:34, 6:42 and 4:31. "From 50 to 60 BlackRock teams" is cut (audit). |
| Badge 3, Inside Copilot only: input guardrails ("catch off-topic requests and personal data"), planning ("picks the tools to call"), output guardrails ("check for hallucinations"), AI-graded tests ("AI models test every system prompt daily") | Rosales 6:09 to 6:30 (input guardrail: off-topic, toxic, PII), 7:22 to 7:46 (planning and action with GPT-4 function calling), 7:48 to 7:53 (output guardrails, hallucinations), and 10:57 to 11:12 (LLMs as judges for every system prompt, daily and on every PR). "LLM judges" is cut (audit TRIM). The panel is attached to the top of the Copilot box, not drawn as a foundation layer. |
| BUILT BY THE CLIENT · CONNECTS THROUGH STUDIO | Studio page 14 |
| Its AI tools: "Can call the APIs with credentials registered in Studio today. No published guide or connector." Uses: API access | APPLY24 wording, from fix 8. Spec: the `OAuth2ClientCredentials` and `OAuth2AccessCode` flows. README (29): "registered via Studio UI". |
| Its applications: "Run in the client's environment or in Aladdin Compute." Uses: API access, Aladdin Compute | Fix 30. README `RUN_MODE` local or compute (29). |
| Its engineers: "Can route calls through the client's own gateway." Uses: Aladdin SDK, API access | Fix 30. PRs 56 and 57. |
| Its data analysts: "Read the client's own Data Cloud." Uses: Aladdin Data Cloud | Added at the coordinator's request (Data Cloud kept as a client-side Studio part). Data Cloud page 20 and release 34. The "BlackRock runs on Snowflake" restatement is dropped. |
| Its Excel users: "Pull Aladdin data into custom reports." Uses: ATX | Added (ATX as a Studio part). ATX page 32. |
| Aladdin Studio, built on by clients / "The client's route into Aladdin. Exhibit 4 shows all its parts." Inner tiles: API access ("Credentials registered in Studio: OAuth applications and tokens"), Aladdin Data Cloud, ATX | Sources 14, 29 and 6 |
| "Direct route through Studio, today" (the solid arrow from Its AI tools) | Brief. Fix 8. |
| Badge 2, Credentials and OAuth scopes (on Studio's link): "An application key, and OAuth scopes: access set per API. Sign-in can be for a user or as an application" | Spec: `APIKeyHeader` (VND.com.blackrock.API-Key) is paired with every OAuth option. The access-code flow signs in a user, and the client-credentials flow signs in an application. |
| Badge 2, Registry rules (on Copilot's link): "The team that owns each tool sets which environments, user groups and apps can use it" | Rosales 6:51 to 7:06 |
| Hatched box with a dashed arrow from Its AI tools to the registry rules: "Route to Copilot's tools. Proposed: MCP server or A2A, my inference" | Brief wording. A2A from Rosales 5:12 to 5:18. The arrow ends at the registry rules, so the route visibly skips Copilot's guardrails. |
| Badge 1, Shared, inside Aladdin's services · applies to every caller | Engineer's fix 11, first band |
| Aladdin user permissions: "The specifications name permissions set by function, action and portfolio. Capital flows need the user's cash permissions and record who authorized and approved them." | PermissionAPI fields `functionalArea`, `action` and `permGroup` (PORTFOLIO). The Capital Flows description says the user needs "standard newcash permissions". Fields `authorizerUserId` and `approverUserId`. This is fix 29 wording, merged into the permissions tile. |
| Compliance by default on orders: "Posting an order runs compliance by default. The caller can turn it off with the scope it uses to post. Any violations are returned." | OrderAPI: `runCompliance` default true. `order:post` needs only `Order:write`. `complianceViolations` comes back in the response. This is APPLY24's wording plus v23's kept "Any violations are returned" (audit KEEP). |
| Order workflow: "A portfolio manager authorizes each order before a trader works it. The public order API has no call to authorize one." | OrderAPI paths are filter, post, batch post, cancel, batch cancel and the LRO status call. `authorizeTime` is readOnly: "The PM authorizes the order … From the authorized PM order, the trader order is created." `activeTime`: "activated by trader". |
| Note: "That route would need BlackRock to apply Copilot's registry rules where a client's AI tools connect. Copilot's team has said it is evaluating A2A and LangChain's agent protocol. Whether Copilot's tools use the APIs clients can call is not public. The exhibit shows the controls on API calls only." | APPLY24 P5 and fix 33. Rosales 5:12. |

## 3. Citations removed, moved or added, and why

Exhibit 3
- Removed the timestamps "at 2:35 and 4:31" (Rosales) and "at 4:49" (Woodhead), and the `&t=` from both links. This is the audit TRIM, the only Exhibit 3 trim the author allowed. Register 9 does not list 2:35. No superscript changed.
- Source 9 now also carries "about two thousand tools and agents" (fix 37). It stays attached to "Rosales, for the apps and Copilot".
- Sources 27, 35, 36 and 37 are kept, because Exhibit 3 stays complete.

Exhibit 4
- Removed 40 (plugin builder). Its sentence was cut by the audit SDK trim, and 40 is still cited in Exhibit 16.
- Removed 28 (Fivetran). "With Fivetran moving the data" was cut by the audit. 28 is still cited in Exhibit 2.
- Source 6's label changed from "for the ids, the portal link and the Admin Center" to "for OAuth, the portal link and the Admin Center". The agraph ID sentence was trimmed, and OAuth now backs the API access tile. **The audit moves the agraph ID evidence to the Exhibit 5 note. The v24 text build must add it there, or it is lost.**
- Sources 38 and 39 moved from the old APIs tile to the shared-layer strip, which now carries "built on Aladdin Graph".
- Source 29's label changed from "the SDK README, for the SDK and the workspace" to "the public SDK's README and source, for the SDK, the workspace, Spaces and both Compute names". Spaces and the code's "Aladdin Compute sessions" come from the SDK source, not the README alone.
- The developer tile now carries superscripts 30 and 44 inside the tile, attached to "as listed on the APIs page" and "behind a client login". Both also stay in the source line. 42's label changed from "for events and the portal" to "for events and developer guides" (a Technical Writer posting), so it no longer stands next to a portal claim.
- Tiles were reordered (row 1: API access, Aladdin SDK, Developer guides) so the long developer tile shares a row with the other three-line tiles and page 1 still fits. Tile padding and gaps were tightened by 0.5 to 1pt.
- The v23 sentence "I read Studio Compute sessions as the SDK's name for Aladdin Compute" is replaced by the fix 58 wording. No citation changed.

Exhibit 13 (v23's Exhibit 14)
- Removed 73 (the job posting). The hatched box and the note sentence were cut (fix 9 and the audit).
- Removed 28 (Fivetran). The Data Cloud line in the API band was cut (audit).
- Removed 1 (Woodhead). Nothing in the redraw rests on it.
- Kept 20 and 34. They now support only the data analysts tile ("each client's own Data Cloud").
- Added 32 (ATX page), for the Excel users tile.
- Did not add 71 (the Smith Garson quote). APPLY24 puts it in this note, but the asides audit ("use the quote once, on page 9, not in Exhibit 14 as well") was accepted later. **The author approved leaving it out.**
- Each source in the line now names what it supports.

## 4. Points that need the author's judgment

1. **Exhibit 13 title: approved** ("Where each control applies: in Aladdin's shared services, at each connection, or inside Copilot only"). The Smith Garson quote stays out of Exhibit 13 (approved).
2. **"Ends at the shared layer".** I read this as: the panel hangs off Studio's right edge and runs down beside the shared layer to its bottom edge, not past it into Hosting. Because it sits beside the black band, it also touches that band. If you meant that it should stop where the shared layer begins, the panel's text will not fit at this size.
3. **The Outside inputs row stays at the bottom.** Its wording now matches the two-way arrows (the approved fix above). The arrows run up the right margin so they don't cross the Hosting and shared rows.
4. **Exhibit 3 wording changes made for consistency or accuracy.** "matches" became "maps". The shared band's clause became "Clients reach them through the 11 public API domains". The two row labels merged. Studio gained "built on by clients" and an API access tile.
5. **Exhibit 13 has five client tiles** (AI tools, applications, engineers, data analysts, Excel users) to carry SDK, API access, Compute, Data Cloud and ATX. Code-curious portfolio managers from Exhibit 3 are not repeated, because no Studio part is tied to them. The data analysts and Excel users tiles have no link drawn down to Aladdin's services, because the controls on Data Cloud and ATX are not public. The note says the exhibit shows the controls on API calls only.
6. **Aladdin user permissions as a shared control.** The specs name the permissions and state some prerequisites (newcash). But PermissionAPI says it is "not intended to be used for Authorization", and the specs do not show enforcement. The tile says "The specifications name…", so it describes rather than asserts. The engineer's review flagged this.
7. **"Sign-in can be for a user or as an application"** on Studio's link. It supports "acting for each user" (N7). Please cut it if it feels like extra detail.
8. **Developer tile: resolved** with the author's wording. The APIs page itself (30) was not re-opened here. The list of contents comes from the research briefing's quotation of it.
9. **Exhibit numbers: done.** Exhibit 13 is renumbered, and Exhibit 3's note reads "Controls as in Exhibit 13". Exhibit 4 has no reference to it. Other exhibits that refer to v23's Exhibit 14, in the text build, need the same change.
10. **Exhibit 13 has no row-label column.** It uses band captions and the numbered badges, so the Copilot-only panel can sit above the Copilot box without a misleading row label. The left-to-right order, colours and box names match Exhibit 3.
11. **Fit.** Exhibits 3 and 4 fill page 1 with about 15pt to spare, after the longer developer tile and outside-inputs text. The row gaps in Exhibit 3 and the tile padding in Exhibit 4 were tightened slightly to keep it on one page. The first exhibit on each page has no top margin, as in the real document after a page break. Any added line in Exhibit 3 or 4 will push Exhibit 4 to the next page.
