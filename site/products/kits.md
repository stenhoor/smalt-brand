# Kits

<StageBadge />

The apps aren't built from scratch each time. They're built from **kits**: reusable components for the smaltworks
applications, each doing one thing, from loading the engine and reading files to formatting, charts and the editor.

- **Few options, on purpose.** A kit offers a narrow set of choices. That keeps every app consistent, and it makes the
  kits easy for AI agents to use well. With fewer options, even a smaller agent produces repeatable results.
- **One family.** Components that draw take their colours and type from the smalt brand tokens, so smaltui, smaltbi
  and smaltnb look like one family.

## <Mark product="kit" :size="32" /> smaltkit

**Small. Alternative. Reusable.** Components for the smaltworks applications, built to be reused.

Today the kits live in **smaltkit**: the engine loader, URL rewriting, number and date formatting, SVG chart helpers and
charts, tables, a virtualized grid, SQL text tools, a code editor, a DOM toolkit, the environment manifest's data steps,
value-picking controls, a reader for a local git repository's files, and TypeScript for the apps' tabs and cells.
smaltui, smaltbi and smaltnb use it. smaltkit is 0.12.0 and isn't on npm yet.

[Read the docs →](https://stenhoor.github.io/smaltkit/) · [Repository →](https://github.com/stenhoor/smaltkit)

## smaltml

**[smaltml](/products/smaltml)** is machine learning for the smalt family, with a brand of its own like smaltkit: the
Hardware mark, in the kit layer's jade. Notebooks and pipelines train models with it; apps call `predict()` from
TypeScript.

[Read the docs →](https://stenhoor.github.io/smaltml/) · [Repository →](https://github.com/stenhoor/smaltml)

## smaltlp

**[smaltlp](/products/smaltlp)** is linear and integer programming for the smalt family, with a brand of its own like
smaltml: the Aim mark, in the kit layer's jade. It solves models of costs, limits and choices to their best answer, in
the browser.

[Read the docs →](https://stenhoor.github.io/smaltlp/) · [Repository →](https://github.com/stenhoor/smaltlp)
