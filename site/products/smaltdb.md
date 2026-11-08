# <Mark product="db" :size="40" /> smaltdb

<StageBadge />

**Small. Alternative. Fast.** A fast alternative database for the browser, written in TypeScript.

smaltdb is the engine under everything else in the family: an embedded database engine that runs inside the browser.

- **Runs in a Web Worker,** so queries never block the page.
- **Stores data in OPFS,** the browser's private file system, with atomic, durable commits through a write-ahead log,
  or **in memory** when nothing needs to persist.
- **Row and columnar tables:** B-trees for reading and writing single rows, columns with zone maps for analytics.
- **Plans, not text.** The engine runs plans; languages build them: SQL is [smaltql](/products/smaltql), dataframes
  are [smaltdf](/products/smaltdf), and each language brings its own `open()`.
- **A cost-based planner,** views and materialized views, and parallel readers in Chromium, Firefox and Safari, across
  tabs.
- **External tables** over CSV, JSON and Parquet files on the web, S3 and Azure, through [plugins](/products/plugins).

**Status:** 0.9.0, preview. The current release on npm is 0.8.3, as `smaltdb`; from the next release, packages publish
as `@smaltworks/<repository>`, so smaltdb becomes `@smaltworks/smaltdb`. 0.9.0, with the plugin system, is next. The on-disk
format may still change before 1.0.

[Read the docs →](https://smaltdb.dev) · [Repository →](https://github.com/stenhoor/smaltdb)
