# VitePress theme

The theme every smalt product site uses (smaltdb.dev, and the smaltql, smaltdf, smaltnb and smaltbi sites). Copy
these files, unchanged, into the site's `.vitepress/theme/`; a site's own rules go in a file of its own.

- `smaltdb.css`: the Kiln palette mapped onto VitePress's `--vp-*` variables for light and dark, the type rules (Geist,
  17px/1.6 body, Martian Mono labels and hero wordmark), the hero-suffix colour for each layer, and the badge styles.
- `shiki.ts`: light and dark Shiki code themes built from the `syn-*` tokens.
- `smaltworks.ts`: the smaltworks menu and footer, for `.vitepress/config.ts`.
- `stage.ts`: the stage badge and "A smaltworks project", for `.vitepress/theme/index.ts`.

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
