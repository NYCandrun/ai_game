export const meta = {
  name: 'citation-placement-check',
  description: 'Check that each superscript sits on the right words and each cited source supports them',
  phases: [{ title: 'Check', detail: 'ten superscripts per agent' }],
}
const C = '/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/citecheck'
const SCHEMA = { type: 'object', required: ['units'], properties: { units: { type: 'array', items: {
  type: 'object', required: ['uid', 'page', 'verdict', 'per_source', 'evidence', 'fix'],
  properties: { uid: { type: 'string' }, page: { type: 'string' },
    verdict: { type: 'string', enum: ['RIGHT', 'MISSING', 'EXTRA', 'MISPLACED', 'WRONG', 'CANNOT CHECK'] },
    per_source: { type: 'string', description: 'e.g. "8: SUPPORTS; 70: PARTLY (...)"' },
    evidence: { type: 'string' }, fix: { type: 'string' } } } } } }
const out = await parallel(args.map(b => () => agent(
  `Read ${C}/BRIEF.md and follow it, with BATCH = ${b}. Check every unit in ${C}/${b}.json.`,
  { label: `cite ${b}`, phase: 'Check', schema: SCHEMA, agentType: 'general-purpose' }).then(r => ({ b, units: r ? r.units : null }))))
return out
