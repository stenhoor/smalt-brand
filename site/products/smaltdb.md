# <Mark product="db" :size="40" /> smaltdb

**Small. Alternative. Fast.** A fast alternative database for the browser, written in TypeScript.

smaltdb is the engine under everything else in the family: an embedded SQL database that runs inside the browser.

- **Runs in a Web Worker,** so queries never block the page.
- **Stores data in OPFS,** the browser's private file system, with atomic, durable commits through a write-ahead log,
  or **in memory** when nothing needs to persist.
- **Row and columnar tables:** B-trees for reading and writing single rows, columns with zone maps for analytics.
- **SQL that follows SQLite,** checked against it with differential tests. SQL is moving into its own package,
  [smaltql](/products/smaltql), which smaltdb ships with by default.
- **A cost-based planner,** views and materialized views, and parallel readers across tabs.
- **External tables** over CSV, JSON and Parquet files on the web, S3 and Azure, through [plugins](/products/plugins).

**Status:** 0.9.0, preview. The current release on npm is 0.8.3, as `smaltdb`; from the next release, packages publish
as `@smaltworks/<repository>`, so smaltdb becomes `@smaltworks/smaltdb`. 0.9.0, with the plugin system, is next. The on-disk
format may still change before 1.0.

[Documentation at smaltdb.dev →](https://smaltdb.dev) · [Repository →](https://github.com/stenhoor/smaltdb)
