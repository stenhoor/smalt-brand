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

function run(tokens: Token[]): Token[] {
  let rule: ((state: any) => void) | undefined
  playgroundPlugin({ core: { ruler: { push: (_: string, r: any) => (rule = r) } } })
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
    ['CREATE TABLE t(x);', 'INSERT INTO t VALUES (1);'],
    ['CREATE TABLE t(x);', 'INSERT INTO t VALUES (1);', 'SELECT x FROM t;'],
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

test('splitSql splits at semicolons outside strings, names and comments', () => {
  assert.deepEqual(splitSql("SELECT 'a;b'; SELECT \"c;d\" -- x;\n; /* ; */ SELECT [e;f];"), ["SELECT 'a;b'", 'SELECT "c;d" -- x;', '/* ; */ SELECT [e;f]'])
  assert.deepEqual(splitSql("SELECT 'it''s; fine'"), ["SELECT 'it''s; fine'"])
  assert.deepEqual(splitSql('-- only a comment\n'), [])
})

test('share codes round-trip any text', () => {
  for (const s of ['SELECT 1', "SELECT 'ÄÖ 😀' -- ü\n", '']) assert.equal(decodeCode(encodeCode(s)), s)
  assert.match(encodeCode('SELECT ??? >>>'), /^[A-Za-z0-9_-]*$/)
})

test('the SQL runner clears the database, runs the setup, then the code, and shows the last rows', async () => {
  const log: string[] = []
  let tables: unknown[][] = [['table', 'old'], ['view', 'v']]
  const db: SqlDatabase = {
    async query(sql) {
      log.push(`query ${sql}`)
      const rows = sql.startsWith('SELECT type, name FROM sqlite_schema') ? tables : [[1, 'a']]
      return Object.assign(rows.slice(), { columns: sql.startsWith('SELECT type') ? ['type', 'name'] : sql.startsWith('INSERT') ? [] : ['x', 'y'] })
    },
    async exec(sql) {
      log.push(`exec ${sql}`)
      return { changes: 1 }
    },
  }
  const runner = await sqlRunner(async () => db)()
  const r = await runner.run('INSERT INTO t VALUES (1); SELECT * FROM t', ['CREATE TABLE t(x); CREATE VIEW w AS SELECT 1'])
  assert.deepEqual(r, { columns: ['x', 'y'], rows: [[1, 'a']] })
  assert.deepEqual(log.slice(1), [
    'exec DROP VIEW "v"',
    'exec DROP TABLE "old"',
    'exec CREATE TABLE t(x)',
    'exec CREATE VIEW w AS SELECT 1',
    'exec INSERT INTO t VALUES (1)',
    'query SELECT * FROM t',
  ])
  tables = []
  assert.deepEqual(await runner.run('INSERT INTO t VALUES (2)', []), { columns: [], rows: [], note: 'Done: the last statement returns no rows' })
})
