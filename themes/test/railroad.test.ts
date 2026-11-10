// node --test themes/test/*.test.ts (Node 22 runs the TypeScript as it is; no packages needed).
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { parseEbnf, renderRule, rulesUsed, railroadPlugin } from '../vitepress/railroad.ts'

const SQL = `
select-stmt ::= 'SELECT' 'DISTINCT'? result-column (',' result-column)* ('FROM' table-or-subquery)?
                ('WHERE' expr)? ('GROUP' 'BY' expr (',' expr)* ('HAVING' expr)?)? ('ORDER' 'BY' ordering-term (',' ordering-term)*)?
                ('LIMIT' expr ('OFFSET' expr)?)?
result-column ::= expr ('AS'? column-alias)? | '*' | table-name '.' '*'
ordering-term ::= expr ('ASC' | 'DESC')? /* a comment */
expr ::= literal | column-name | expr binary-op expr
`

test('parses rules, terminals, references and suffixes', () => {
  const g = parseEbnf(SQL)
  assert.deepEqual([...g.rules.keys()], ['select-stmt', 'result-column', 'ordering-term', 'expr'])
  assert.deepEqual(g.rules.get('ordering-term'), {
    t: 'seq',
    items: [{ t: 'ref', name: 'expr' }, { t: 'opt', item: { t: 'choice', items: [{ t: 'term', text: 'ASC' }, { t: 'term', text: 'DESC' }] } }],
  })
  assert.equal(g.text.get('ordering-term'), "ordering-term ::= expr ('ASC' | 'DESC')? /* a comment */")
})

test('x (sep x)* becomes one loop with sep on the way back', () => {
  const g = parseEbnf(`list ::= item (',' item)*`)
  assert.deepEqual(g.rules.get('list'), { t: 'rep', item: { t: 'ref', name: 'item' }, sep: { t: 'term', text: ',' } })
})

test('an empty alternative makes the choice optional', () => {
  const g = parseEbnf(`dir ::= 'ASC' | 'DESC' |`)
  assert.equal(g.rules.get('dir')!.t, 'opt')
})

test('x* is an optional loop, x+ a loop', () => {
  const g = parseEbnf(`a ::= x* \n b ::= x+`)
  assert.deepEqual(g.rules.get('a'), { t: 'opt', item: { t: 'rep', item: { t: 'ref', name: 'x' } } })
  assert.deepEqual(g.rules.get('b'), { t: 'rep', item: { t: 'ref', name: 'x' } })
})

test('errors name the line', () => {
  assert.throws(() => parseEbnf(`a ::= 'x'\nb ::= ( 'y'`), /line 2: expected \)/)
  assert.throws(() => parseEbnf(`a ::= 'x`), /unclosed quote/)
  assert.throws(() => parseEbnf(`nonsense`), /no rule found/)
  assert.throws(() => parseEbnf(`a ::= 'x'\na ::= 'y'`), /a is defined twice/)
})

test('rulesUsed follows references through the grammar', () => {
  const g = parseEbnf(SQL)
  assert.deepEqual(rulesUsed(g, ['select-stmt']), ['result-column', 'expr', 'ordering-term'])
})

test('renders keywords, rules that expand and rules that do not, escaped', () => {
  const g = parseEbnf(`r ::= 'a<b' known missing\nknown ::= 'k'`)
  const svg = renderRule(g, 'r')
  assert.match(svg, /^<svg class="sw-rr"/)
  assert.match(svg, /<g class="sw-rr-term">.*a&lt;b/)
  assert.match(svg, /class="sw-rr-ref" data-rule="known" tabindex="0" role="button" aria-expanded="false"/)
  assert.match(svg, /class="sw-rr-ref sw-rr-undefined">/)
  assert.match(svg, /aria-label="r ::= 'a&lt;b' known missing"/)
})

test('a long rule wraps to fit', () => {
  const g = parseEbnf(SQL)
  const width = (s: string) => Number(/width="(\d+)"/.exec(s)![1])
  assert.ok(width(renderRule(g, 'select-stmt')) <= 600)
  assert.ok(width(renderRule(g, 'select-stmt', { maxWidth: 100000 })) > 600)
})

test('a sequence inside a group wraps too, and every rule fits', () => {
  const g = parseEbnf(SQL + `\nwide ::= 'A' ('BBBBBBBBBB' 'CCCCCCCCCC' 'DDDDDDDDDD' 'EEEEEEEEEE' 'FFFFFFFFFF' 'GGGGGGGGGG')? 'Z'`)
  const width = (s: string) => Number(/width="(\d+)"/.exec(s)![1])
  for (const name of g.rules.keys()) assert.ok(width(renderRule(g, name)) <= 600, name)
  assert.ok(width(renderRule(g, 'wide', { maxWidth: 400 })) <= 400)
})

test('the plugin draws ebnf and railroad fences, and carries referenced rules once per page', () => {
  const rules: Record<string, any> = { fence: () => 'CODE' }
  const md = { renderer: { rules } }
  railroadPlugin(md, { grammar: SQL })
  const env = {}
  const fence = (info: string, content: string) => rules.fence!([{ info, content }], 0, {}, env, {})
  const a = fence('railroad', 'ordering-term\n')
  assert.match(a, /id="syntax-ordering-term"/)
  assert.match(a, /data-sw-rr="expr" hidden/)
  assert.match(a, /<details class="sw-rr-ebnf">/)
  const b = fence('railroad', 'result-column')
  assert.doesNotMatch(b, /data-sw-rr="expr"/) // already on the page
  assert.equal(fence('sql', 'SELECT 1'), 'CODE')
  assert.match(fence('ebnf', `local ::= 'x' expr`), /id="syntax-local"/)
  assert.throws(() => fence('railroad', 'nope'), /no rule nope/)
})
