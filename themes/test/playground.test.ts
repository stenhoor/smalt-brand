// node --test themes/test/*.test.ts (Node 22 runs the TypeScript as it is; no packages needed).
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { playgroundPlugin, splitSql, sqlRunner, encodeCode, decodeCode, type SqlDatabase } from '../vitepress/playground.ts'

class Token {
  type: string
  tag: string
  nesting: number
  info = ''
  content = ''
  block = true
  map = null
  constructor(type: string, tag: string, nesting: number) {
    this.type = type
    this.tag = tag
    this.nesting = nesting
  }
}

const fence = (info: string, content: string) => Object.assign(new Token('fence', 'code', 0), { info, content })
const html = (content: string) => Object.assign(new Token('html_block', '', 0), { content })
const para = () => new Token('paragraph_open', 'p', 1)
const table = () => [new Token('table_open', 'table', 1), new Token('tr_open', 'tr', 1), new Token('tr_close', 'tr', -1), new Token('table_close', 'table', -1)]

function run(tokens: Token[], options: Parameters<typeof playgroundPlugin>[1] = { run: 'marked' }): Token[] {
  let rule: ((state: any) => void) | undefined
  playgroundPlugin({ core: { ruler: { push: (_: string, r: any) => (rule = r) } } }, options)
  const state = { tokens, env: {}, Token }
  rule!(state)
  return state.tokens
}

const attr = (tokens: Token[], name: string) =>
  tokens.filter((t) => t.type === 'html_block' && t.content.includes('class="sw-play"')).map((t) => {
    const raw = new RegExp(`${name}="([^"]*)"`).exec(t.content)![1]
    return raw.replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
  })

test('a play fence becomes a playground; its setup is the tested examples above it', () => {
  const out = run([
    fence('sql', 'CREATE TABLE t(x);\n'),
    html('<!-- docs:setup INSERT INTO t VALUES (1); -->\n'),
    html('<!-- docs:error SMALT_ERROR -->\n'),
    fence('sql', 'SELECT nope;\n'),
    fence('ts', 'const x = 1\n'),
    fence('sql play', 'SELECT x FROM t;\n'),
    ...table(),
    para(),
    fence('sql play', "SELECT 'it''s';\n"),
  ])
  assert.deepEqual(attr(out, 'data-setup').map((s) => JSON.parse(s)), [
    ['CREATE TABLE t(x);', 'INSERT INTO t VALUES (1);', { sql: 'SELECT nope;', fails: true }],
    ['CREATE TABLE t(x);', 'INSERT INTO t VALUES (1);', { sql: 'SELECT nope;', fails: true }, 'SELECT x FROM t;'],
  ])
  assert.deepEqual(attr(out, 'data-code'), ['SELECT x FROM t;\n', "SELECT 'it''s';\n"])
  assert.deepEqual(attr(out, 'data-index'), ['0', '1'])
  // The fence keeps its language for highlighting, and the tested result moves inside the playground.
  assert.deepEqual(out.filter((t) => t.type === 'fence').map((t) => t.info), ['sql', 'sql', 'ts', 'sql', 'sql'])
  const types = out.map((t) => (t.type === 'html_block' ? (t.content.includes('sw-play-result') ? 'result' : t.content.includes('class="sw-play"') ? 'open' : t.content.startsWith('</div>\n</div>') ? 'close' : 'html') : t.type))
  const first = types.indexOf('open')
  assert.deepEqual(types.slice(first, first + 8), ['open', 'fence', 'result', 'table_open', 'tr_open', 'tr_close', 'table_close', 'close'])
})

test('a skipped example stays out of the setup, and markers apply to the next fence only', () => {
  const out = run([html('<!-- docs:skip -->\n'), fence('sql', 'DROP TABLE x;\n'), para(), fence('sql', 'SELECT 1;\n'), fence('sql play', 'SELECT 2;\n')])
  assert.deepEqual(JSON.parse(attr(out, 'data-setup')[0]), ['SELECT 1;'])
})

test('by default every tested example runs in place; skipped, plugin and noplay examples do not; errors show their code', () => {
  const out = run(
    [
      fence('sql', 'CREATE TABLE t(x);\n'),
      html('<!-- docs:error SMALT_ERROR -->\n'),
      fence('sql', 'SELECT nope;\n'),
      html('<!-- docs:skip -->\n'),
      fence('sql', 'SELECT 1;\n'),
      html('<!-- docs:plugin @smaltdb/io -->\n'),
      fence('sql', "SELECT * FROM read_csv('x');\n"),
      fence('sql noplay', 'SELECT 2;\n'),
      fence('sql play', 'SELECT 3;\n'),
    ],
    {},
  )
  assert.deepEqual(attr(out, 'data-code'), ['CREATE TABLE t(x);\n', 'SELECT nope;\n', 'SELECT 3;\n'])
  // The failing example is in the setup of the ones after it, expected to fail; skipped and plugin examples are not.
  assert.deepEqual(JSON.parse(attr(out, 'data-setup')[2]), ['CREATE TABLE t(x);', { sql: 'SELECT nope;', fails: true }, 'SELECT 2;'])
  assert.ok(out.some((t) => t.type === 'html_block' && t.content.includes('Fails with <code>SMALT_ERROR</code>')))
  assert.deepEqual(out.filter((t) => t.type === 'fence').map((t) => t.info), ['sql', 'sql', 'sql', 'sql', 'sql', 'sql'])
})

test('front matter playground: false turns a page\'s playgrounds off', () => {
  let rule: ((state: any) => void) | undefined
  playgroundPlugin({ core: { ruler: { push: (_: string, r: any) => (rule = r) } } })
  const state = { tokens: [fence('sql', 'SELECT 1;\n'), fence('sql play', 'SELECT 2;\n')], env: { frontmatter: { playground: false } }, Token }
  rule!(state)
  assert.deepEqual(attr(state.tokens, 'data-code'), [])
  assert.deepEqual(state.tokens.map((t) => t.info), ['sql', 'sql'])
})

test('splitSql splits at semicolons outside strings, names and comments', () => {
  assert.deepEqual(splitSql("SELECT 'a;b'; SELECT \"c;d\" -- x;\n; /* ; */ SELECT [e;f];"), ["SELECT 'a;b'", 'SELECT "c;d" -- x;', '/* ; */ SELECT [e;f]'])
  assert.deepEqual(splitSql("SELECT 'it''s; fine'"), ["SELECT 'it''s; fine'"])
  assert.deepEqual(splitSql('-- only a comment\n'), [])
})

test('share codes round-trip any text', () => {
  for (const s of ['SELECT 1', "SELECT 'ÄÖ 😀' -- ü\n", '']) assert.equal(decodeCode(encodeCode(s)), s)
  assert.match(encodeCode('SELECT ??? >>>'), /^[A-Za-z0-9_-]*$/)
})

test('the SQL runner gives every Run a fresh database: setup, then the code, then close; the next one opens early', async () => {
  const log: string[] = []
  let opened = 0
  const open = async (): Promise<SqlDatabase> => {
    const n = ++opened
    log.push(`open ${n}`)
    return {
      async query(sql) {
        log.push(`${n} query ${sql}`)
        if (sql === 'BAD') throw Object.assign(new Error('near "BAD": syntax error'), { code: 'SMALT_SYNTAX' })
        return Object.assign([[1, 'a']], { columns: sql.startsWith('INSERT') ? [] : ['x', 'y'] })
      },
      async exec(sql) {
        log.push(`${n} exec ${sql}`)
        if (sql === 'BAD') throw Object.assign(new Error('near "BAD": syntax error'), { code: 'SMALT_SYNTAX' })
        return { changes: 1 }
      },
      close() {
        log.push(`close ${n}`)
      },
    }
  }
  const runner = await sqlRunner(open)()
  assert.deepEqual(await runner.run('INSERT INTO t VALUES (1); SELECT * FROM t', ['CREATE TABLE t(x)', { sql: 'SELECT 1; BAD', fails: true }]), { columns: ['x', 'y'], rows: [[1, 'a']] })
  await assert.rejects(runner.run('BAD', []), /syntax error/)
  assert.deepEqual(await runner.run('INSERT INTO t VALUES (2)', []), { columns: [], rows: [], note: 'Done: the last statement returns no rows' })
  assert.deepEqual(log, [
    'open 1',
    'open 2', '1 exec CREATE TABLE t(x)', '1 exec SELECT 1', '1 exec BAD', '1 exec INSERT INTO t VALUES (1)', '1 query SELECT * FROM t', 'close 1',
    'open 3', '2 query BAD', 'close 2',
    'open 4', '3 query INSERT INTO t VALUES (2)', 'close 3',
  ])
})

test('key=value flags and front matter play: are an example\'s attributes, for it and for its setup steps', () => {
  let rule: ((state: any) => void) | undefined
  playgroundPlugin({ core: { ruler: { push: (_: string, r: any) => (rule = r) } } }, { languages: ['cypher'] })
  const state = {
    tokens: [
      fence('cypher', 'CREATE (:A)\n'),
      html('<!-- docs:error E -->\n'),
      fence('cypher dataset=metro', 'MATCH (n) RETURN n\n'),
      fence('cypher dataset=social {2}', 'RETURN 1\n'),
    ],
    env: { frontmatter: { play: { dataset: 'family', size: 300 } } },
    Token,
  }
  rule!(state)
  assert.deepEqual(attr(state.tokens, 'data-attrs').map((s) => JSON.parse(s)), [
    { dataset: 'family', size: '300' },
    { dataset: 'metro', size: '300' },
    { dataset: 'social', size: '300' },
  ])
  assert.deepEqual(JSON.parse(attr(state.tokens, 'data-setup')[2]), [
    { sql: 'CREATE (:A)', attrs: { dataset: 'family', size: '300' } },
    { sql: 'MATCH (n) RETURN n', fails: true, attrs: { dataset: 'metro', size: '300' } },
  ])
  // Attributes leave the info string; other flags stay for highlighting.
  assert.deepEqual(state.tokens.filter((t) => t.type === 'fence').map((t) => t.info), ['cypher', 'cypher', 'cypher {2}'])
})

test('an example with no attributes has no data-attrs, and its setup steps stay plain', () => {
  const out = run([fence('sql', 'SELECT 1;\n'), fence('sql play', 'SELECT 2;\n')], {})
  assert.ok(!out.some((t) => t.type === 'html_block' && t.content.includes('data-attrs')))
  assert.deepEqual(JSON.parse(attr(out, 'data-setup')[1]), ['SELECT 1;'])
})

test('the SQL runner runs a setup step with attributes but no fails as an ordinary step', async () => {
  const log: string[] = []
  const runner = await sqlRunner(async () => ({
    async query(sql) {
      log.push(`query ${sql}`)
      return Object.assign([[1]], { columns: ['x'] })
    },
    async exec(sql) {
      log.push(`exec ${sql}`)
      if (sql === 'BAD') throw new Error('bad')
      return {}
    },
  }))()
  await assert.rejects(runner.run('SELECT 1', [{ sql: 'BAD', attrs: { a: 'b' } }], {}), /bad/)
  assert.deepEqual(log, ['exec BAD'])
})
