// node --test themes/test/*.test.ts (Node 22 runs the TypeScript as it is; no packages needed).
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, existsSync } from 'node:fs'
import { tmpdir } from 'node:os'
import path from 'node:path'
import { toTwin, describe, agentDocs, grammarRules } from '../vitepress/agents.ts'

const opts = { product: 'smaltql', version: '0.9.0', url: 'https://example.dev/smaltql/', grammar: "expr ::= literal | expr '+' expr\nliteral ::= 'NULL' /* a value */" }

test('a twin keeps the page, and its anchors, and drops what only a browser shows', () => {
  const src = [
    '---', 'title: Lists', 'outline: deep', '---', '', '<script setup>', "import X from './x.vue'", '</script>', '',
    '## ARRAY {#array}', '', 'See [list_extract](./list#list_extract), [the guide](../../guide/), [here](#array), [outside](../../../bench/x.md) and [web](https://a.b/).',
    '', '<ProductCard name="x" />', '', '<!-- docs:error SMALT_MISMATCH -->', '```sql play', "SELECT list_min(ARRAY['b']);", '```', '',
    '<!-- docs:setup CREATE TABLE t(x); -->', '<!-- a note for people -->', '```railroad', 'expr', '```', '',
    '::: warning Differs from SQLite', 'It does.', ':::', '', '```md', '## not a heading {#x}', '<!-- docs:skip -->', '```',
  ].join('\n')
  const twin = toTwin(src, 'reference/functions/list.md', opts)
  assert.equal(twin, [
    '# Lists', '',
    '> For agents: smaltql 0.9.0. The page for people: https://example.dev/smaltql/reference/functions/list', '',
    '## ARRAY {#array}', '',
    'See [list_extract](https://example.dev/smaltql/reference/functions/list.md#list_extract), [the guide](https://example.dev/smaltql/guide/index.md), [here](#array), [outside](../../../bench/x.md) and [web](https://a.b/).',
    '', 'This example fails with `SMALT_MISMATCH`:', '', '```sql', "SELECT list_min(ARRAY['b']);", '```', '',
    'Run first:', '', '```sql', 'CREATE TABLE t(x);', '```', '', '```ebnf', "expr ::= literal | expr '+' expr", '```', '',
    '> **Differs from SQLite:**', '> It does.', '', '```md', '## not a heading {#x}', '<!-- docs:skip -->', '```', '',
  ].join('\n'))
})

test('links with brackets in their label, and fences indented in a list, are read whole', () => {
  const src = ['# P', '', '| [`first(X [, KEY])`](./aggregate#first) | [`lag(X [, N [, D]])`](./window#lag) |', '', 'See [time', 'columns](./datetime#columns) and `[not](./a-link)`.', '', '1. Step:', '', '   ```ts', '   const a = 1', '   ```', '', '<!-- docs:plugin @smaltdb/parquet -->', '```ts', 'x', '```'].join('\n')
  const twin = toTwin(src, 'reference/functions/index.md', opts)
  assert.match(twin, /\[`first\(X \[, KEY\]\)`\]\(https:\/\/example\.dev\/smaltql\/reference\/functions\/aggregate\.md#first\)/)
  assert.match(twin, /\[`lag\(X \[, N \[, D\]\]\)`\]\(https:\/\/example\.dev\/smaltql\/reference\/functions\/window\.md#lag\)/)
  assert.match(twin, /\[time\ncolumns\]\(https:\/\/example\.dev\/smaltql\/reference\/functions\/datetime\.md#columns\) and `\[not\]\(\.\/a-link\)`/)
  assert.match(twin, /   ```\n\nThis example needs the `@smaltdb\/parquet` plugin:\n\n```ts/)
})

test('grammar rules keep their text and comments', () => {
  assert.equal(grammarRules(opts.grammar).get('literal'), "literal ::= 'NULL' /* a value */")
})

test('a description is the front matter one, or the first sentence of the first paragraph', () => {
  assert.equal(describe('---\ndescription: Lists in SQL.\n---\n# x'), 'Lists in SQL.')
  assert.equal(describe('# Lists\n\n| a |\n\nA [list](./x) holds values. More.'), 'A list holds values.')
})

test('agentDocs writes twins, llms.txt in sidebar order, and agents.md', () => {
  const dir = mkdtempSync(path.join(tmpdir(), 'agents-'))
  const src = path.join(dir, 'src')
  const out = path.join(dir, 'out')
  const page = (p: string, text: string) => {
    mkdirSync(path.dirname(path.join(src, p)), { recursive: true })
    writeFileSync(path.join(src, p), text)
  }
  page('index.md', '---\nlayout: home\n---\n')
  page('guide/agents.md', '# For agents\n\nUse `open()`. Never use X.\n')
  page('guide/quick-start.md', '# Quick start\n\nRun SQL in five minutes.\n')
  page('reference/sql/index.md', '# SQL\n\nThe statements.\n\n## SELECT\n\nReads rows.\n')
  page('reference/sql/insert.md', '# INSERT\n\nAdds rows.\n')
  page('reference/sql/create-index.md', '# CREATE INDEX\n\nBuilds an index.\n')
  const r = agentDocs(
    {
      srcDir: src, outDir: out, pages: ['index.md', 'guide/agents.md', 'guide/quick-start.md', 'reference/sql/create-index.md', 'reference/sql/insert.md', 'reference/sql/index.md'],
      site: { title: 'smaltql', description: 'SQL for smaltdb.', themeConfig: { sidebar: [
        { text: 'Getting started', items: [{ text: 'Quick start', link: '/guide/quick-start' }] },
        { text: 'SQL', items: [{ text: 'Overview', link: '/reference/sql/' }, { text: 'INSERT', link: '/reference/sql/insert' }, { text: 'CREATE INDEX', link: '/reference/sql/create-index' }] },
      ] } },
    },
    { ...opts, versions: { 'plan format': '1' }, intro: 'guide/agents.md', guide: ['reference/sql/'] },
  )
  assert.equal(r.files, 8)
  assert.ok(existsSync(path.join(out, 'guide/quick-start.md')))
  const llms = readFileSync(path.join(out, 'llms.txt'), 'utf8')
  assert.equal(llms, [
    '# smaltql', '', '> SQL for smaltdb.', '',
    'Version: smaltql 0.9.0, plan format 1. Every page is Markdown at the address below. The agent guide is all of it in one file, with the grammar: [agents.md](https://example.dev/smaltql/agents.md).',
    '', '## Getting started', '', '- [Quick start](https://example.dev/smaltql/guide/quick-start.md): Run SQL in five minutes.',
    '', '## SQL', '', '- [Overview](https://example.dev/smaltql/reference/sql/index.md): The statements.', '- [INSERT](https://example.dev/smaltql/reference/sql/insert.md): Adds rows.', '- [CREATE INDEX](https://example.dev/smaltql/reference/sql/create-index.md): Builds an index.',
    '', '## Optional', '', '- [For agents](https://example.dev/smaltql/guide/agents.md)', '- [index](https://example.dev/smaltql/index.md)', '',
  ].join('\n'))
  const guide = readFileSync(path.join(out, 'agents.md'), 'utf8')
  assert.match(guide, /^# smaltql: the guide for agents\n\n> smaltql 0\.9\.0, plan format 1\./)
  assert.match(guide, /Use `open\(\)`\. Never use X\.\n\n## Grammar\n\n/)
  // The section's index first, then its pages; their headings one level down.
  assert.match(guide, /## SQL\n\nFrom https:\/\/example\.dev\/smaltql\/reference\/sql\/index\.md\n\nThe statements\.\n\n### SELECT\n\nReads rows\.\n\n## INSERT\n[\s\S]*\n## CREATE INDEX\n/)
})
