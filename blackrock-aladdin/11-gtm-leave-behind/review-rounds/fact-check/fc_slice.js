export const meta = {
  name: 'leave-behind-fact-check-slice',
  description: 'Fact-check one slice of claim batches (web first, quoted receipts), then independently re-check every claim not CONFIRMED',
  phases: [
    { title: 'Check', detail: 'one agent per six-claim batch' },
    { title: 'Re-check', detail: 'second independent agent on flagged claims' },
  ],
}
const FC = '/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc'
const V = ['CONFIRMED', 'CONFIRMED (note)', 'CORPUS-ONLY', 'PARTLY', 'UNVERIFIED', 'WRONG']
const BATCH = { type: 'object', required: ['rows'], properties: { rows: { type: 'array', items: {
  type: 'object', required: ['id', 'claim', 'verdict', 'receipt', 'correction'],
  properties: { id: { type: 'string' }, claim: { type: 'string' }, verdict: { type: 'string', enum: V },
    receipt: { type: 'string' }, correction: { type: 'string' } } } } } }
const RECHECK = { type: 'object', required: ['rows'], properties: { rows: { type: 'array', items: {
  type: 'object', required: ['id', 'first_verdict', 'final_verdict', 'agrees_with_first', 'receipt', 'correction'],
  properties: { id: { type: 'string' }, first_verdict: { type: 'string' }, final_verdict: { type: 'string', enum: V },
    agrees_with_first: { type: 'boolean' }, receipt: { type: 'string' }, correction: { type: 'string' } } } } } }
const RC_RULES = `Re-check each one independently on the open web, as a skeptic of the first checker: try hard to find the receipt they missed (a claim marked UNVERIFIED or CORPUS-ONLY may well be on the web), and try to show that a WRONG or PARTLY verdict is itself mistaken. Agree only if your own evidence supports their verdict. Exact quote as receipt for every row. ` +
  `Write your report to ${FC}/reports/BID_recheck.md as a Markdown table | id | claim | first verdict | final verdict | agrees | receipt (URL or file:line, then exact quote) | correction |, then return every row.`

const recheck = (bid, list) => agent(
  `Read ${FC}/CHECK.md for the rules, sources register and corpus map. A first fact-checker flagged the claims below from batch ${bid} (full claim rows in ${FC}/batches/${bid}.tsv; first report ${FC}/reports/${bid}.md). ` +
  RC_RULES.replace('BID', bid) + `\n\n${list}`,
  { label: `re-check ${bid}`, phase: 'Re-check', schema: RECHECK, agentType: 'general-purpose' })

const results = await pipeline(
  args.items,
  (it) => it.mode === 'recheck' ? Promise.resolve({ fromReport: true }) : agent(
    `Read ${FC}/CHECK.md and follow it exactly. Your batch id is ${it.bid}. Your claims are in ${FC}/batches/${it.bid}.tsv (columns: id, page, location, claim, sources). ` +
    `Check only those claims. Web first, an exact quote as the receipt for every row. Write the Markdown report to ${FC}/reports/${it.bid}.md, then return every row in the structured output.`,
    { label: `check ${it.bid}`, phase: 'Check', schema: BATCH, agentType: 'general-purpose' }),
  async (res, it) => {
    if (!res) return { bid: it.bid, failed: 'check' }
    if (res.fromReport) {
      const rc = await agent(
        `Read ${FC}/CHECK.md for the rules, sources register and corpus map. Read the first fact-checker's report ${FC}/reports/${it.bid}.md for batch ${it.bid} (claims in ${FC}/batches/${it.bid}.tsv). ` +
        `Take every row whose verdict is anything other than CONFIRMED or CONFIRMED (note). If there are none, write "No flagged rows." to ${FC}/reports/${it.bid}_recheck.md and return an empty rows array. Otherwise: ` +
        RC_RULES.replace('BID', it.bid),
        { label: `re-check ${it.bid}`, phase: 'Re-check', schema: RECHECK, agentType: 'general-purpose' })
      return { bid: it.bid, mode: 'recheck', rechecked: rc ? rc.rows.length : null, failed: rc ? null : 'recheck' }
    }
    const flagged = res.rows.filter(r => r.verdict !== 'CONFIRMED' && r.verdict !== 'CONFIRMED (note)')
    if (!flagged.length) return { bid: it.bid, rows: res.rows.length, rechecked: 0 }
    const list = flagged.map(r => `- ${r.id}: CLAIM: ${r.claim}\n  FIRST CHECKER: ${r.verdict}. Receipt: ${r.receipt}. Correction: ${r.correction}`).join('\n')
    const rc = await recheck(it.bid, list)
    return { bid: it.bid, rows: res.rows.length, rechecked: rc ? rc.rows.length : null, failed: rc ? null : 'recheck' }
  },
)
const out = results.map((r, i) => r || { bid: args.items[i].bid, failed: 'dropped' })
log(`slice done: ${out.length} items, failures: ${out.filter(r => r.failed).map(r => r.bid + ':' + r.failed).join(',') || 'none'}`)
return out
