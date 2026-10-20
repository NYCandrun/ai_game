export const meta = {
  name: 'leave-behind-fact-check-redo',
  description: 'Re-check, with web search, claims whose first pass ran after the search allowance was used up',
  phases: [{ title: 'Redo', detail: 'one agent per five claims, at most 10 web searches each' }],
}
const FC = '/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc'
const V = ['CONFIRMED', 'CONFIRMED (note)', 'CORPUS-ONLY', 'PARTLY', 'UNVERIFIED', 'WRONG']
const SCHEMA = { type: 'object', required: ['rows'], properties: { rows: { type: 'array', items: {
  type: 'object', required: ['id', 'new_verdict', 'agrees', 'searched', 'searches_run', 'receipt', 'finding'],
  properties: { id: { type: 'string' }, new_verdict: { type: 'string', enum: V }, agrees: { type: 'boolean' },
    searched: { type: 'boolean', description: 'false only if web search was unavailable for this claim' },
    searches_run: { type: 'integer' }, receipt: { type: 'string' }, finding: { type: 'string' } } } } } }
const out = await parallel(args.map(rid => () => agent(
  `Read ${FC}/REDO.md and follow it exactly (RID = ${rid}). Your claims, with the earlier verdicts, receipts and findings, are in ${FC}/redo/${rid}.json. ` +
  `Check every claim in that file and nothing else. Write ${FC}/reports/redo_${rid}.md and return every row.`,
  { label: `redo ${rid}`, phase: 'Redo', schema: SCHEMA, agentType: 'general-purpose' })
  .then(r => ({ rid, rows: r ? r.rows : null }))))
const res = out.filter(Boolean)
const unsearched = res.flatMap(r => (r.rows || []).filter(x => !x.searched).map(x => x.id))
const failed = res.filter(r => !r.rows).map(r => r.rid)
log(`redo wave: ${res.length} agents, ${unsearched.length} claims not searched, failed: ${failed.join(',') || 'none'}`)
return { failed, unsearched, searches: res.reduce((n, r) => n + (r.rows || []).reduce((m, x) => m + x.searches_run, 0), 0) }
