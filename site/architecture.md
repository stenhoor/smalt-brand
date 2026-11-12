# How it fits together

The smalt family is one stack. smaltty, the TypeScript it is all written in, is at the base. Data comes in above it,
one engine runs everything, and each layer above the engine is a different way to put it to work.

<EngineBar />

## At the base: smaltty

TypeScript is the language of everything smalt, and smaltty is smalt's TypeScript implementation, in our own code: it parses, strips, binds
and type-checks TypeScript in the page, with no dependencies. It runs the TypeScript you type into an app's tab or a
notebook cell, and checks calls into smaltdf and smaltts as you type, against the declarations the languages publish.
The apps use it through smaltkit. [smaltty →](/products/smaltty)

## Sources

Where the data lives.

- **OPFS, in your browser.** smaltdb keeps its databases in the browser's Origin Private File System, so data persists
  on the visitor's own machine.
- **Memory.** A database can live in memory instead: nothing is written to disk, and it's gone when it closes. Good for
  scratch work, tests and data you load fresh each time. An OPFS database can also keep a materialized view in memory,
  rebuilt when the database opens, so frequent refreshes don't wear storage.
- **External data.** Files on the web, Amazon S3 and Azure Blob Storage, read in place as external tables, through the
  [`@smaltworks/smaltdb-external`](/products/plugins) plugin.
- **Plugins.** Formats and sources are plugins: CSV, TSV and JSON in `@smaltworks/smaltdb-io`, Parquet in `@smaltworks/smaltdb-parquet`,
  and databases in files on disk in Node.js in `@smaltworks/smaltdb-node`.
  Other people can write their own. [Plugins →](/products/plugins)

## The engine: smaltdb

One engine powers everything. smaltdb runs in a Web Worker, so the page never waits on it, and commits through a
write-ahead log, so data survives a crash. Every tool above it uses this same engine.

Tables come in two layouts, and one database can mix them:

- **Row tables,** the default: whole rows in B-trees, fast for reading and writing individual rows, with indexes,
  unique constraints and foreign keys.
- **Columnar tables,** for analytics: each column stored separately in compressed chunks, with zone maps that skip
  blocks of rows a filter can't match. Aggregates and scans over many rows run several times faster. Materialized
  views can be columnar too. [smaltdb →](/products/smaltdb)

## The language layer: smaltql, smaltdf and smaltts

Three ways to tell the engine what you want, over the same tables.

- **smaltql**, the SQL you know, in a dialect that follows SQLite. Install it and you have a SQL database on smaltdb. [smaltql →](/products/smaltql)
- **smaltdf**, a dataframe language in TypeScript: frames, expressions and method chains. It builds plans for the
  same engine as smaltql, so a dataframe gets the same optimizer and the same storage. [smaltdf →](/products/smaltdf)

- **smaltts**, a thin, typed TypeScript API, for code that works with the engine directly, with no query language in
  between. [smaltts →](/products/smaltts)

You don't need one engine for SQL tables and another for dataframes. There is one way to process your data.

## Kits

Small, focused libraries that the apps are built from: charts, tables, number formatting, the engine loader. Each kit
does one thing with few options, which keeps the apps consistent and makes them easier and more repeatable to build with
AI agents, including smaller ones. [Kits →](/products/kits)

## Apps

- **smaltui**, the query workbench: SQL today, with dataframes to come. [smaltui →](/products/smaltui)
- **smaltbi**, reports for analysts who'd rather drag a field than write a query. [smaltbi →](/products/smaltbi)
- **smaltnb**, notebooks for working through data step by step. [smaltnb →](/products/smaltnb)
- **smaltfl**, data pipelines whose steps are smaltnb notebooks: a day that is off is paused, not published.
  [smaltfl →](/products/smaltfl)
