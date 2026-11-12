# <Mark product="ty" :size="40" /> smaltty

<StageBadge />

**Small. Alternative. Code.** TypeScript for the smalt apps.

smaltty is smalt's TypeScript implementation, in our own code: it parses, strips, binds and type-checks TypeScript in the page, with no
dependencies. It runs the TypeScript you type into a [smaltui](/products/smaltui) tab or a [smaltnb](/products/smaltnb)
cell, and checks your calls into [smaltdf](/products/smaltdf) and [smaltts](/products/smaltts) as you type.

- **Types removed, nothing moved.** Types become spaces, so every line and column of the JavaScript is the one you
  wrote, and an error points where it was typed.
- **TypeScript's own rules.** The syntax tree is TypeScript's, node for node; each name is bound to the declaration
  TypeScript's checker names; and every error it reports is one `tsc` reports too. What it doesn't model yet, it
  leaves quiet.
- **Warn and run.** Type errors show as warnings while the code still runs.
- **Small and fast.** Plain ES2022 modules, 58 KB gzipped, that load in a page without a bundler. In Chromium, a cold
  check of app code takes 8 to 10 ms and a re-check after an edit under 1 ms
  ([benchmarks](https://stenhoor.github.io/smaltty/BENCHMARKS#checking-in-a-page)).

The apps use it through [smaltkit](/products/kits), which wraps it as `smaltkit/typescript`.

**Status:** in development, with smaltworks 0.9.0; not on npm yet.

[Read the docs →](https://stenhoor.github.io/smaltty/) · [Repository →](https://github.com/stenhoor/smaltty)
