# VitePress theme

The theme every smalt product site uses (smaltdb.dev, and the smaltql, smaltdf, smaltnb and smaltbi sites). Copy
these files, unchanged, into the site's `.vitepress/theme/`; a site's own rules go in a file of its own.

- `smaltdb.css`: the Kiln palette mapped onto VitePress's `--vp-*` variables for light and dark, the type rules (Geist,
  17px/1.6 body, Martian Mono labels and hero wordmark), the hero-suffix colour for each layer, and the badge styles.
- `shiki.ts`: light and dark Shiki code themes built from the `syn-*` tokens.
- `smaltworks.ts`: the smaltworks menu and footer, for `.vitepress/config.ts`.
- `stage.ts`: the stage badge and "A smaltworks project", for `.vitepress/theme/index.ts`.
- `railroad.ts`: syntax diagrams from a grammar in EBNF (BRAND.md, Documentation, rule 4): a markdown-it plugin for
  `.vitepress/config.ts` and the handler that expands rules in place, for `.vitepress/theme/index.ts`. Its styles are
  in `smaltdb.css`. Tests: `node --test themes/test/*.test.ts` in smalt-brand.
- `playground.ts`: playgrounds (BRAND.md, Documentation, rule 7): a markdown-it plugin that makes a `play` fence a
  playground, the browser side that runs it with smaltkit's editor and grid, and `sqlRunner()` for a SQL site. Its
  styles are in `smaltdb.css`.
- `agents.ts`: docs for agents (BRAND.md, Documentation, rule 9): Markdown twins of the pages, `/llms.txt` and
  `/agents.md`, written at the end of the build. Node only, for `.vitepress/config.ts`.

Copy these badges from [`badges/`](../../badges/) into the site's public directory: `work-in-progress.svg`,
`work-in-progress-on-dark.svg`, `a-smaltworks-project.svg` and `a-smaltworks-project-on-dark.svg` (from 1.0,
`release-1x.svg` and `release-1x-on-dark.svg` too).

`.vitepress/config.ts`:

```ts
import { smaltLight, smaltDark } from './theme/shiki'
import { smaltworksMenu, smaltworksFooter } from './theme/smaltworks'

const base = '/smaltql/' // '/' for a site on its own domain

export default defineConfig({
  base,
  markdown: { theme: { light: smaltLight, dark: smaltDark } },
  themeConfig: {
    nav: [/* the site's own items */, smaltworksMenu()],
    footer: smaltworksFooter(base),
    search: { provider: 'local' },
  },
})
```

`.vitepress/theme/index.ts`:

```ts
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './smaltdb.css'
import { withSmaltworks } from './stage'

export default { extends: DefaultTheme, Layout: withSmaltworks(DefaultTheme) } satisfies Theme
// From 1.0: withSmaltworks(DefaultTheme, 'release')
// Badges in a folder of the public directory: withSmaltworks(DefaultTheme, 'wip', '/badges/'), smaltworksFooter(base, 'badges/')
```

The hero's wordmark (`docs/index.md`), with the suffix in its layer's colour (`language`, `kit`, `tool` or `ai`;
smaltdb's suffix has no span):

```yaml
hero:
  name: 'sm<span class="alt">alt</span><span class="suffix language">ql</span>'
```

Load the fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700&family=Geist+Mono:wght@400;500&family=Martian+Mono:wght@400;600&display=swap" rel="stylesheet">
```

## Syntax diagrams

Keep the language's grammar in one file, in W3C EBNF (`name ::= expression`; terminals in quotes; `|`, `( )`, `?`, `*`,
`+`; `/* comments */`), such as `docs/grammar.ebnf`. In `.vitepress/config.ts`:

```ts
import { readFileSync } from 'node:fs'
import { railroadPlugin } from './theme/railroad'

markdown: {
  config: (md) => { md.use(railroadPlugin, { grammar: readFileSync('docs/grammar.ebnf', 'utf8') }) },
},
```

In `.vitepress/theme/index.ts`:

```ts
import { enableRailroad } from './railroad'

export default {
  extends: DefaultTheme,
  enhanceApp() { if (typeof document !== 'undefined') enableRailroad() },
} satisfies Theme
```

On a page, a `railroad` fence draws rules of the grammar by name, one per line, and an `ebnf` fence draws the rules it
defines itself:

````md
```railroad
select-stmt
```

```ebnf
limit-clause ::= 'LIMIT' expr ('OFFSET' expr)?
```
````

Each rule gets the anchor `#syntax-<name>` and an EBNF toggle. A rule box expands the rule it names in place (click,
or Enter or Space); a rule the grammar doesn't define has a dashed box and doesn't expand. `x (',' x)*` is drawn as one
loop with `,` on its way back. Diagrams wrap to 600px, the content column beside the outline (`maxWidth` changes it).
A grammar error fails the build and names the page and the line.

## Playgrounds

Every tested example runs in place (`run: 'every'`, the default; `run: 'marked'` runs only fences marked `play`).
The result table printed under it is its tested result, and an example marked `docs:error CODE` is tested to fail
with `CODE`. A fence marked `noplay` doesn't run, nor do examples marked `docs:skip` or `docs:plugin`:

````md
```sql
SELECT ARRAY[3, 1, 2] AS numbers;
```

| numbers |
| --- |
| [3,1,2] |
````

At rest it shows that, with a small Run button, and loads nothing. Run or Edit makes it a playground where it stands:
Run loads smaltkit's editor and grid, starts the site's runner once per visit,
and runs the page's setup, then the code. The setup is what the examples test runs first: every example of the same
language above it, and `<!-- docs:setup … -->` markers, leaving out `docs:error` and `docs:skip` examples. Share copies a
link with the code in its fragment (`#play-<n>=…`), which opens that playground with the code, ready to run.

The site needs smaltkit (pinned as `github:stenhoor/smaltkit#<commit>`) and its own build of the engine and language.
In `.vitepress/config.ts`:

```ts
import { playgroundPlugin } from './theme/playground'

markdown: { config: (md) => { md.use(playgroundPlugin) } },  // { languages: ['sql', 'ts'] } for more than SQL
vite: { optimizeDeps: { exclude: ['@smaltworks/smaltql', 'smaltdb'] }, worker: { format: 'es' } },
```

In `.vitepress/theme/index.ts`, a runner for each language: `sqlRunner()` takes a function that opens a database
reading SQL. The runner keeps one in-memory database for the visit and clears it before each Run.

```ts
import { enablePlaygrounds, sqlRunner } from './playground'

export default {
  extends: DefaultTheme,
  enhanceApp() {
    if (typeof document === 'undefined') return
    enablePlaygrounds({
      runners: { sql: sqlRunner(async () => (await import('@smaltworks/smaltql')).open('playground', { storage: 'memory' })) },
      // app: (lang, code) => '<a link that opens the code in the app>',  once the app can
    })
  },
} satisfies Theme
```

A runner for another language implements `run(code, setup)` and returns `{ columns, rows }`, or `{ columns: [], rows:
[], note }`; an Error it throws is shown with its `code`.

## Docs for agents

At the end of the build, `agentDocs()` writes Markdown for AI agents beside the pages:

- **A twin of every page** (`guide/queries.md` beside `guide/queries.html`): the page's source, with what only a browser
  shows made plain. Playground fences lose `play`; a `railroad` fence becomes the EBNF of its rules; the examples test's
  markers become sentences (`docs:error CODE` is "This example fails with `CODE`:", `docs:setup` a "Run first:" block);
  VitePress containers become quotes; components, scripts and other comments go. Links to other pages point at their
  twins, absolute; headings keep their `{#id}`. A line under the title names the version and the page for people.
- **`/llms.txt`:** the twins, grouped as the sidebar is, each with a one-line description (its front matter's
  `description`, or its first sentence), then the pages the sidebar leaves out under "Optional".
- **`/agents.md`, the agent guide:** the site's introduction for agents (`intro`: how to use the product and its rules,
  written for agents), the grammar as EBNF, then the pages `guide` names, each a section in the sidebar's order.

In `.vitepress/config.ts`:

```ts
import { readFileSync } from 'node:fs'
import { agentDocs, packageVersion } from './theme/agents'

buildEnd: (config) => {
  agentDocs(config, {
    product: 'smaltql',
    version: packageVersion('package.json'),
    url: 'https://stenhoor.github.io/smaltql/',
    intro: 'guide/agents.md',
    grammar: readFileSync('docs/grammar.ebnf', 'utf8'),
    guide: ['reference/sql/', 'reference/functions/', 'guide/errors'],
  })
},
```
