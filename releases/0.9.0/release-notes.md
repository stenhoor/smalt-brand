<!--
DRAFT, not published. The release notes for smaltworks 0.9.0, for review before the publish.
After review: each package's section, with Breaking, Try it and Tell us, becomes that repository's GitHub release
(templates/release-notes.md); this whole page is the family's notes. Before publishing, see "Before this goes out" in
the PR that adds this file.
smaltty became a top-level product on 2026-11-12 (DECISIONS.md, "smaltty: a product"): its description below says so,
but its changelog still lists only #1–#3; add its later pull requests (the checker, milestones 6–8) before publishing.
-->

<img alt="Work in progress. Come build with us." src="https://raw.githubusercontent.com/stenhoor/smalt-brand/main/badges/work-in-progress.svg" height="56">

# smaltworks 0.9.0

The first release of the smalt family as a family. smaltdb becomes an engine that runs plans and carries no language,
and two languages run on it: SQL ([smaltql](https://github.com/stenhoor/smaltql)) and dataframes in TypeScript
([smaltdf](https://github.com/stenhoor/smaltdf)). With them come a query workbench (smaltui), reactive notebooks
(smaltnb), smalt TypeScript (smaltty) and the shared browser code the apps are built from (smaltkit).

**Work in progress. Come build with us.** This is a preview: before 1.0, any release can change the API or the file
format. [What that means →](https://smaltworks.dev/stability)

| Package | npm | What it is | In this release |
| --- | --- | --- | --- |
| smaltdb | `@smaltworks/smaltdb` | The engine | 141 pull requests since 0.8.3 |
| smaltql | `@smaltworks/smaltql` | The SQL | First release |
| smaltdf | `@smaltworks/smaltdf` | The dataframes | First release |
| smaltui | (a site) | The query workbench | First release |
| smaltnb | (a site) | The notebooks | First release |
| smaltty | (used through smaltkit) | smalt TypeScript | First release |
| smaltkit | (used by the apps) | Shared browser code for the apps | First release |

The plugins ship with it: `@smaltworks/smaltdb-io` (CSV, TSV and JSON), `@smaltworks/smaltdb-external` (files, URLs, S3,
Azure Blob Storage, and local paths in Node) and `@smaltworks/smaltdb-parquet` (Parquet).

## 💥 Breaking

For anyone upgrading from smaltdb 0.8.3. The other packages are new, so nothing in them breaks.

- **New package names.** Packages publish under the smaltworks organisation, named after their repositories. `smaltdb`
  becomes `@smaltworks/smaltdb`, and `smaltdb/engine` becomes `@smaltworks/smaltdb/engine`. `smaltdb` 0.8.3 stays on npm,
  marked deprecated. ([ADR 0015](https://smaltdb.dev/adr/0015-smaltql))
- **SQL is its own package.** The engine carries no language, so SQL comes from `@smaltworks/smaltql`. Change
  `import { open } from 'smaltdb'` to `import { open } from '@smaltworks/smaltql'`; `open()` and `db.query()` work as
  before. With the engine in the same thread (Node, or a worker of your own), add `import '@smaltworks/smaltql/register'`
  before `Database.openMemory()`. ([#100](https://github.com/stenhoor/smaltdb/pull/100),
  [#158](https://github.com/stenhoor/smaltdb/pull/158))
- **CSV, JSON, external data and Parquet are plugins.** Install the ones you use, and register them with SQL in a
  worker entry of your own: `defineWorker({ languages: [sqlLanguage], plugins: [io, external, parquet] })`, passed to
  `open()` as `options.worker`. `db.exportCSV(sql)` and `db.exportJSON(sql)` become `exportCSV(db, sql)` and
  `exportJSON(db, sql)` from `@smaltworks/smaltdb-io/client`, beside `importCSV` and `importJSON`.
  ([ADR 0012](https://smaltdb.dev/adr/0012-plugins), [#28](https://github.com/stenhoor/smaltdb/pull/28),
  [#38](https://github.com/stenhoor/smaltdb/pull/38), [#39](https://github.com/stenhoor/smaltdb/pull/39))
- **Storage format 4.** 0.9.0 stores definitions instead of SQL text, and adds storage types for booleans, dates and
  times, lists and structs. It refuses a file written by 0.8.3 (format 3) with `SMALT_FORMAT`. To carry a database
  over, export its tables with 0.8.3 (`db.exportCSV()` or `db.exportJSON()`), then create them with 0.9.0 and import the
  files (`importCSV()` or `importJSON()`). Keep your source data, as the [stability page](https://smaltworks.dev/stability)
  advises. ([#88](https://github.com/stenhoor/smaltdb/pull/88),
  [storage format](https://smaltdb.dev/STORAGE_FORMAT#_9-format-versioning))

## 🏆 Highlights

- **Two languages, one engine.** smaltdb runs plans, and every language builds them through the same shared plan layer:
  the same optimizer, fused scans and spilling for SQL and for dataframes. A language registers with the engine
  (`smaltdb/language`), and each exports its own `open()`. ([ADR 0014](https://smaltdb.dev/adr/0014-shared-plan-layer),
  [ADR 0015](https://smaltdb.dev/adr/0015-smaltql), [ADR 0016](https://smaltdb.dev/adr/0016-plan-api-for-every-language))
- **smaltdf: dataframes in TypeScript.** Frames, expressions and method chains that run in the engine, on its row and
  columnar tables: `select`, `filter`, `withColumns`, `groupBy(…).agg(…)`, joins including `joinAsof`, windows,
  `pivot` and `unpivot`, frames from JavaScript data, writes and views. Polars inspired its functions, and 55 comparison
  tests run the shared ones against Polars.
- **New types.** `bool`; NaN as a value with its own place in sort order; `date`, `datetime`, `time` and `duration`,
  with time zones passed as values (`to_zone`, `from_zone`, `zone_offset`); and `list<T>` and `struct<…>`, with
  `explode` and `implode`. Parquet's dates and nested columns arrive as typed columns. SQL keeps SQLite's meaning: it
  reads dates as text and lists and structs as JSON text. ([ADR 0018](https://smaltdb.dev/adr/0018-bool-and-nan),
  [ADR 0019](https://smaltdb.dev/adr/0019-dates-and-times), [ADR 0020](https://smaltdb.dev/adr/0020-lists-and-structs))
- **Parallel readers in every cross-origin isolated browser,** Chromium, Firefox and Safari alike. Where a browser can't
  share file handles, readers read through the owner, with a shared block cache and the WAL index in shared memory.
  ([ADR 0021](https://smaltdb.dev/adr/0021-parallel-readers-everywhere))
- **A dependency-free core, and a plugin API that only grows.** Third-party code lives only in the plugins that need
  it, and plugin API version 1 takes additive changes only. ([ADR 0012](https://smaltdb.dev/adr/0012-plugins),
  [ADR 0013](https://smaltdb.dev/adr/0013-plugin-api-v1))
- **smaltui, the query workbench,** with TypeScript tabs for smaltdf beside its SQL tabs, both with Explain, Analyze,
  Stop and Format.
- **smaltnb, reactive notebooks.** A notebook is a TypeScript file: cells are top-level code, the graph comes from the
  names they define and read, and SQL and smaltdf cells are first-class.
- **smaltty, smalt TypeScript.** It parses, strips, binds and type-checks TypeScript in the browser, runs the
  TypeScript in smaltui's tabs and smaltnb's notebooks, and checks calls into smaltdf as you type.

## Try it

```sh
npm install --save-exact @smaltworks/smaltdb@0.9.0 @smaltworks/smaltql@0.9.0
npm install --save-exact @smaltworks/smaltdf@0.9.0   # dataframes
```

```ts
import { open } from '@smaltworks/smaltql';

const db = await open('app');           // the engine runs in a worker; data lives in OPFS
await db.query('SELECT 1 + 1');
```

Or open the apps, nothing to install: the [query workbench](https://stenhoor.github.io/smaltui/) and the
[notebooks](https://stenhoor.github.io/smaltnb/) run in your browser, with your data in its private storage.

## Tell us

Found something rough? That is what this release is for: try it, break it, tell us. Open an issue in the package's
repository, or start at [Get involved](https://smaltworks.dev/community/get-involved).

---

## smaltdb 0.9.0

The engine. 141 pull requests since 0.8.3.

### Breaking

See **Breaking** at the top: the package name, SQL in its own package, the plugins, and storage format 4.

### Changelog

#### 💥 Breaking changes

- Plugins: dependency-free core and @smaltdb/parquet (ADR 0012 steps 1–2) ([#28](https://github.com/stenhoor/smaltdb/pull/28))
- Plugins: full plugin interface; @smaltdb/external and @smaltdb/io (ADR 0012 steps 3–4) ([#38](https://github.com/stenhoor/smaltdb/pull/38))
- Move the plugins to their own repositories (ADR 0012 step 5) ([#39](https://github.com/stenhoor/smaltdb/pull/39))
- ADR 0015 step 7a: language-neutral catalog storage (format 4) ([#88](https://github.com/stenhoor/smaltdb/pull/88))
- SQL leaves smaltdb: the engine carries no language (ADR 0015 step 9) ([#100](https://github.com/stenhoor/smaltdb/pull/100))
- Use smaltql as @smaltworks/smaltql ([#158](https://github.com/stenhoor/smaltdb/pull/158))

#### 🚀 Performance improvements

- Speed up window functions 3-7x; RANGE frames no longer quadratic ([#44](https://github.com/stenhoor/smaltdb/pull/44))
- Plan path: planning cost within noise of the AST path (ADR 0014, step 6d) ([#62](https://github.com/stenhoor/smaltdb/pull/62))
- Per-statement cost: no residual filter on rowid access, literals out of per-row generated code ([#69](https://github.com/stenhoor/smaltdb/pull/69))
- Cheaper planning per new statement: cached row loaders, no buffer per RecordReader ([#70](https://github.com/stenhoor/smaltdb/pull/70))
- Front end: fewer allocations per statement ([#71](https://github.com/stenhoor/smaltdb/pull/71))
- Cheaper single-row writes: pooled savepoint images, reused row writers ([#72](https://github.com/stenhoor/smaltdb/pull/72))
- CRC-32C reads 32-bit words: about twice as fast ([#73](https://github.com/stenhoor/smaltdb/pull/73))

#### ✨ Enhancements

- Declare plugin API version 1 stable (ADR 0013) ([#40](https://github.com/stenhoor/smaltdb/pull/40))
- Math functions: SQLite's set, inlined into generated code ([#41](https://github.com/stenhoor/smaltdb/pull/41))
- Statistical aggregates: variance, stddev, covariance, corr, skewness, kurtosis, median, percentiles ([#42](https://github.com/stenhoor/smaltdb/pull/42))
- ADR 0015 step 5: plan serialization, the validator, morsels as plans ([#84](https://github.com/stenhoor/smaltdb/pull/84))
- ADR 0015 step 6b: bound statements and bind() ([#86](https://github.com/stenhoor/smaltdb/pull/86))
- ADR 0015 step 6c: DDL as language-neutral schema operations ([#87](https://github.com/stenhoor/smaltdb/pull/87))
- ADR 0015 step 7b: ALTER TABLE as a schema operation on stored definitions ([#89](https://github.com/stenhoor/smaltdb/pull/89))
- ADR 0015 step 8a: preparePlan / queryPlan and the plan namespace (in-process) ([#90](https://github.com/stenhoor/smaltdb/pull/90))
- ADR 0015 step 8b: plans over the worker protocol, in the client and for plugins ([#91](https://github.com/stenhoor/smaltdb/pull/91))
- Views and materialized views through the language interface (ADR 0015 step 9a, part 2) ([#93](https://github.com/stenhoor/smaltdb/pull/93))
- The engine runs no SQL of its own; statements through the language interface (ADR 0015 step 9a, parts 3 and 4) ([#94](https://github.com/stenhoor/smaltdb/pull/94))
- The SQL language behind a boundary, registered by smaltdb's entry points (ADR 0015 step 9b, parts 1 and 2) ([#95](https://github.com/stenhoor/smaltdb/pull/95))
- smaltdb/language: the language boundary as a package export (ADR 0015 step 9) ([#96](https://github.com/stenhoor/smaltdb/pull/96))
- defineWorker: a worker registers languages as it installs plugins (ADR 0015 step 9) ([#97](https://github.com/stenhoor/smaltdb/pull/97))
- Operations get behaviour names; sql.* names stay as aliases (ADR 0016 step 4, part 1) ([#106](https://github.com/stenhoor/smaltdb/pull/106))
- Operations for other meanings: float and floor division, floor modulo, half-even rounding, Unicode case, regular expressions (ADR 0016 step 4, part 2) ([#107](https://github.com/stenhoor/smaltdb/pull/107))
- A logical catalog for every language (ADR 0016 step 6, part 1) ([#110](https://github.com/stenhoor/smaltdb/pull/110))
- Results of plans: column types, write counts and streamPlan (ADR 0016 step 7) ([#115](https://github.com/stenhoor/smaltdb/pull/115))
- Errors that say where they came from: origin and structured fields (ADR 0016 step 7) ([#116](https://github.com/stenhoor/smaltdb/pull/116))
- A language words its statements' errors (ADR 0016 step 7) ([#117](https://github.com/stenhoor/smaltdb/pull/117))
- The engine words constraint failures its own way (ADR 0016 step 7) ([#118](https://github.com/stenhoor/smaltdb/pull/118))
- Order guarantees: stable sort, order-keeping operations, semi and anti joins (ADR 0016 step 8a) ([#119](https://github.com/stenhoor/smaltdb/pull/119))
- Order on request: ordered joins, groups in first-row order (ADR 0016 step 8b) ([#120](https://github.com/stenhoor/smaltdb/pull/120))
- Order-aware operations: first and last, limit from the end, distinct keeping a row (ADR 0016 step 8c) ([#121](https://github.com/stenhoor/smaltdb/pull/121))
- Definitions without source text (ADR 0016 step 9a) ([#122](https://github.com/stenhoor/smaltdb/pull/122))
- Languages provide what they use; plans read views by name (ADR 0016 step 9b) ([#123](https://github.com/stenhoor/smaltdb/pull/123))
- New plan operations (ADR 0016 step 10) ([#130](https://github.com/stenhoor/smaltdb/pull/130))
- Compute a catalog function's result type when it is read ([#135](https://github.com/stenhoor/smaltdb/pull/135))
- Checked arithmetic and strict conversions, and calls of one-argument operations ([#138](https://github.com/stenhoor/smaltdb/pull/138))
- Order contract: unionAll gives its first input's rows, then its second's ([#139](https://github.com/stenhoor/smaltdb/pull/139))
- Order contract: a window without its own order takes its rows in input order ([#140](https://github.com/stenhoor/smaltdb/pull/140))
- Remove the sql.* operation names: behaviour names only ([#143](https://github.com/stenhoor/smaltdb/pull/143))
- NaN in storage and order (ADR 0018 step 2) ([#144](https://github.com/stenhoor/smaltdb/pull/144))
- NaN in operations (ADR 0018 step 3) ([#145](https://github.com/stenhoor/smaltdb/pull/145))
- bool in plans and results (ADR 0018 step 4) ([#146](https://github.com/stenhoor/smaltdb/pull/146))
- Parameters: a language hook, and NaN kept for plans (ADR 0018 step 6, part 1) ([#147](https://github.com/stenhoor/smaltdb/pull/147))
- BOOLEAN storage (ADR 0018 step 5) ([#148](https://github.com/stenhoor/smaltdb/pull/148))
- bool by default, and parameters through the language (ADR 0018 step 6, part 3) ([#149](https://github.com/stenhoor/smaltdb/pull/149))
- Dates and times: the types, storage and results (ADR 0019 step 1) ([#152](https://github.com/stenhoor/smaltdb/pull/152))
- Dates and times as Date or Temporal on request (ADR 0019 step 1) ([#153](https://github.com/stenhoor/smaltdb/pull/153))
- Date and time operations (ADR 0019 step 2) ([#154](https://github.com/stenhoor/smaltdb/pull/154))
- Time zones: to_zone, from_zone and zone_offset (ADR 0019 step 3) ([#156](https://github.com/stenhoor/smaltdb/pull/156))
- Dates and times from external data: FormatColumn.type (ADR 0019 step 4) ([#157](https://github.com/stenhoor/smaltdb/pull/157))
- Lists and structs: types, encoding, storage, results (ADR 0020 step 1) ([#161](https://github.com/stenhoor/smaltdb/pull/161))
- List and struct operations, implode, JSON text (ADR 0020 step 2) ([#163](https://github.com/stenhoor/smaltdb/pull/163))
- explode (ADR 0020 step 3) ([#165](https://github.com/stenhoor/smaltdb/pull/165))
- Lists and structs from external data: FormatColumn.type (ADR 0020 step 4) ([#166](https://github.com/stenhoor/smaltdb/pull/166))
- M9 step 1: parallel readers that read the owner's files through it (ADR 0021) ([#172](https://github.com/stenhoor/smaltdb/pull/172))
- M9 step 2: a block cache shared by the owner and its proxied readers (ADR 0021) ([#173](https://github.com/stenhoor/smaltdb/pull/173))
- M9 step 4: readers that read through the owner by default, without morsels ([#174](https://github.com/stenhoor/smaltdb/pull/174))
- M9 step 3: readers refresh their snapshots from the owner's WAL index in shared memory ([#176](https://github.com/stenhoor/smaltdb/pull/176))
- M9 done: Chromium's readers refresh from the shared WAL index ([#177](https://github.com/stenhoor/smaltdb/pull/177))

#### 🐞 Bug fixes

- Fix the engine and client bugs found while writing the user docs ([#26](https://github.com/stenhoor/smaltdb/pull/26))
- External Parquet: read the size from a range probe, not HEAD (hosts that compress) ([#35](https://github.com/stenhoor/smaltdb/pull/35))
- Fix sum/total/avg and quote() on infinite REALs ([#43](https://github.com/stenhoor/smaltdb/pull/43))
- Plans: text comparisons use the collation their call names, in generated code ([#98](https://github.com/stenhoor/smaltdb/pull/98))
- Logic nodes read every argument (and, or with more than two) ([#162](https://github.com/stenhoor/smaltdb/pull/162))

#### 📖 Documentation

- User documentation: guide, quick start, FAQ, SQL, function and API reference ([#25](https://github.com/stenhoor/smaltdb/pull/25))
- Docs: the query pipeline as built, and the plan-layer implementation plan (ADR 0014 step 1) ([#49](https://github.com/stenhoor/smaltdb/pull/49))
- Docs: an Engine section, the engine API without SQL ([#99](https://github.com/stenhoor/smaltdb/pull/99))
- Docs: send moved SQL pages on to smaltql's site ([#101](https://github.com/stenhoor/smaltdb/pull/101))
- Roadmap: where the plan layer, smaltql and smaltdf stand ([#141](https://github.com/stenhoor/smaltdb/pull/141))
- ADR 0018 done; the roadmap moves on to dates and times ([#150](https://github.com/stenhoor/smaltdb/pull/150))
- Docs site: the smaltworks standard (menu, stage badge, footer, shared theme) ([#160](https://github.com/stenhoor/smaltdb/pull/160))
- Docs: lists and structs are in (ADR 0020 done) ([#167](https://github.com/stenhoor/smaltdb/pull/167))
- Docs: @smaltdb/parquet carries hyparquet-compressors as a dependency ([#170](https://github.com/stenhoor/smaltdb/pull/170))

#### 🛠️ Other improvements

- ADR 0012 (proposed): plugins and a dependency-free core ([#27](https://github.com/stenhoor/smaltdb/pull/27))
- Brand: 'Alternate' becomes 'Alternative' ([#29](https://github.com/stenhoor/smaltdb/pull/29))
- Add CLAUDE.md with repo commands and cross-repo working rules ([#31](https://github.com/stenhoor/smaltdb/pull/31))
- CLAUDE.md: issue workflow ([#33](https://github.com/stenhoor/smaltdb/pull/33))
- CLAUDE.md: adopt the shared issue workflow ([#37](https://github.com/stenhoor/smaltdb/pull/37))
- ADR 0014 (proposed): a shared engine plan layer for several languages ([#45](https://github.com/stenhoor/smaltdb/pull/45))
- Tests: golden corpus of physical plan shapes (ADR 0014 step 2) ([#47](https://github.com/stenhoor/smaltdb/pull/47))
- Plan layer step 3a: plan expression types, SQL semantics as named functions ([#48](https://github.com/stenhoor/smaltdb/pull/48))
- Plan layer step 3b: bind expressions to plan expressions, compile from them ([#50](https://github.com/stenhoor/smaltdb/pull/50))
- Plan layer step 3c: code generation reads plan expressions ([#51](https://github.com/stenhoor/smaltdb/pull/51))
- Plan layer step 4: operators and fusion carry plan expressions ([#52](https://github.com/stenhoor/smaltdb/pull/52))
- Plan layer step 4b-i: mark columns as read when they are compiled ([#53](https://github.com/stenhoor/smaltdb/pull/53))
- Plan layer step 5a: SQL front end for reading queries, checked in shadow mode ([#54](https://github.com/stenhoor/smaltdb/pull/54))
- Plan layer step 5b: the SQL front end covers joins, windows, recursion and sources ([#55](https://github.com/stenhoor/smaltdb/pull/55))
- Plan layer step 6a: access-path and cost analysis on bound conditions ([#56](https://github.com/stenhoor/smaltdb/pull/56))
- Physical planner for single-table plans (ADR 0014, step 6b) ([#57](https://github.com/stenhoor/smaltdb/pull/57))
- Physical planner for join regions (ADR 0014, step 6c-i) ([#58](https://github.com/stenhoor/smaltdb/pull/58))
- Physical planner for subqueries (ADR 0014, step 6c-ii) ([#59](https://github.com/stenhoor/smaltdb/pull/59))
- Physical planner for windows, compounds, VALUES and nested FROM plans (ADR 0014, step 6c-iii) ([#60](https://github.com/stenhoor/smaltdb/pull/60))
- Plan SELECTs through the plan layer by default (ADR 0014, step 6c-iv) ([#61](https://github.com/stenhoor/smaltdb/pull/61))
- Front end flattens views and FROM subqueries (ADR 0014, step 7a) ([#63](https://github.com/stenhoor/smaltdb/pull/63))
- Front end applies materialized-view matching (ADR 0014, step 7c) ([#64](https://github.com/stenhoor/smaltdb/pull/64))
- Decorrelated inner sides through the plan layer (ADR 0014, step 7b) ([#65](https://github.com/stenhoor/smaltdb/pull/65))
- DELETE through the plan layer (ADR 0014, step 8a) ([#66](https://github.com/stenhoor/smaltdb/pull/66))
- UPDATE through the plan layer (ADR 0014, step 8b) ([#67](https://github.com/stenhoor/smaltdb/pull/67))
- INSERT through the plan layer (ADR 0014, step 8c) ([#68](https://github.com/stenhoor/smaltdb/pull/68))
- Benchmarks: native SQLite comparison (bench:native) and 2026-11-04 results against SQLite WASM and native ([#74](https://github.com/stenhoor/smaltdb/pull/74))
- Plan layer covers what still fell back to the AST path ([#75](https://github.com/stenhoor/smaltdb/pull/75))
- Delete the planner's AST path ([#76](https://github.com/stenhoor/smaltdb/pull/76))
- ADR 0015 (proposed): SQL moves to smaltql; packages publish as @smaltworks/<repository> ([#77](https://github.com/stenhoor/smaltdb/pull/77))
- ADR 0015: smaltql and the language API (one record with #77) ([#78](https://github.com/stenhoor/smaltdb/pull/78))
- ADR 0015 step 2: plans carry no closures ([#80](https://github.com/stenhoor/smaltdb/pull/80))
- ADR 0015 step 3: the planner takes plans only ([#82](https://github.com/stenhoor/smaltdb/pull/82))
- ADR 0015 step 4: one expression compiler ([#83](https://github.com/stenhoor/smaltdb/pull/83))
- ADR 0015 step 6a: writes compile from their plans alone ([#85](https://github.com/stenhoor/smaltdb/pull/85))
- ADR 0015 step 9a-1: SQL code out of the engine's exec/ ([#92](https://github.com/stenhoor/smaltdb/pull/92))
- ADR 0016 (proposed): the plan API for every language ([#102](https://github.com/stenhoor/smaltdb/pull/102))
- ADR 0016: accepted, with the owner's decisions ([#103](https://github.com/stenhoor/smaltdb/pull/103))
- The validator checks everything it is given (ADR 0016 step 2) ([#104](https://github.com/stenhoor/smaltdb/pull/104))
- Traits: the planner and code generation read what an operation is, not its name (ADR 0016 step 3) ([#105](https://github.com/stenhoor/smaltdb/pull/105))
- Plan meaning as fields (ADR 0016 step 5) ([#108](https://github.com/stenhoor/smaltdb/pull/108))
- Remove the plan metadata setters from smaltdb/language (ADR 0016 step 5) ([#109](https://github.com/stenhoor/smaltdb/pull/109))
- Remove the function registries and expression compilers from smaltdb/language (ADR 0016 step 6) ([#111](https://github.com/stenhoor/smaltdb/pull/111))
- Tables as the catalog describes them while binding (ADR 0016 step 6) ([#112](https://github.com/stenhoor/smaltdb/pull/112))
- smaltdb/language without the engine's tables and comparison internals (ADR 0016 step 6) ([#113](https://github.com/stenhoor/smaltdb/pull/113))
- Remove bindStoredExprs from the language interface (ADR 0016 step 6) ([#114](https://github.com/stenhoor/smaltdb/pull/114))
- ADR 0017: the remaining SQL dependencies in the engine, client and plugins ([#131](https://github.com/stenhoor/smaltdb/pull/131))
- Remove the engine's and client's remaining SQL dependencies (ADR 0017 step 2) ([#132](https://github.com/stenhoor/smaltdb/pull/132))
- Pin @smaltdb/io that needs no SQL, and run it in the no-SQL project ([#133](https://github.com/stenhoor/smaltdb/pull/133))
- ADR 0017 re-review: nothing the engine runs itself needs an object's language ([#134](https://github.com/stenhoor/smaltdb/pull/134))
- Record a Node baseline after the plan API and SQL split ([#136](https://github.com/stenhoor/smaltdb/pull/136))
- Record the accepted statement-compile cost of the plan API ([#137](https://github.com/stenhoor/smaltdb/pull/137))
- ADR 0018 (proposed): bool and NaN ([#142](https://github.com/stenhoor/smaltdb/pull/142))
- ADR 0019: dates and times ([#151](https://github.com/stenhoor/smaltdb/pull/151))
- ADR 0019: a time zone is a value passed to the operations ([#155](https://github.com/stenhoor/smaltdb/pull/155))
- ADR 0020: lists and structs (accepted) ([#159](https://github.com/stenhoor/smaltdb/pull/159))
- CLAUDE.md: read smalt-brand first; site kit from smalt-brand ([#164](https://github.com/stenhoor/smaltdb/pull/164))
- Tagline: "Small. Alternative." on one line, the product's word on the next ([#168](https://github.com/stenhoor/smaltdb/pull/168))
- Working rules: ask before adding outside code ([#169](https://github.com/stenhoor/smaltdb/pull/169))
- M9 first: ADR 0021, parallel readers everywhere, and the roadmap order ([#171](https://github.com/stenhoor/smaltdb/pull/171))
- M9 research: four CI samples per browser with readers through the owner by default ([#175](https://github.com/stenhoor/smaltdb/pull/175))
- ADR 0022 (proposed): SQL for the new engine features ([#181](https://github.com/stenhoor/smaltdb/pull/181))


## smaltql 0.9.0

The SQL: the SQLite dialect, parsed and bound to smaltdb plans. Its first release, as SQL moves out of smaltdb. `open()`
gives a SQL database in a page; `@smaltworks/smaltql/worker` is the engine worker with SQL registered; constraint errors
are worded as SQLite words them.

### Breaking

- None. (SQL users coming from smaltdb 0.8.3: see **Breaking** at the top.)

### Changelog

#### ✨ Enhancements

- smaltql: SQL as its own package, on smaltdb/language ([#2](https://github.com/stenhoor/smaltql/pull/2))
- open() and smaltql/worker: a SQL database in a page ([#4](https://github.com/stenhoor/smaltql/pull/4))
- Write plan meaning fields directly (smaltdb ADR 0016 step 5) ([#8](https://github.com/stenhoor/smaltql/pull/8))
- Read functions and expression metadata through smaltdb's catalog (smaltdb ADR 0016 step 6) ([#9](https://github.com/stenhoor/smaltql/pull/9))
- Bind against the catalog's tables and comparison rule (smaltdb ADR 0016 step 6) ([#10](https://github.com/stenhoor/smaltql/pull/10))
- Word SQL's errors as SQLite does (smaltdb ADR 0016 step 7) ([#12](https://github.com/stenhoor/smaltql/pull/12))
- Bind stored table expressions only from tables with source text ([#14](https://github.com/stenhoor/smaltql/pull/14))
- SQL names the engine's operations by behaviour, not sql.* ([#17](https://github.com/stenhoor/smaltql/pull/17))
- SQL's bool and NaN: declared int, and NaN parameters as NULL (smaltdb ADR 0018 step 6) ([#18](https://github.com/stenhoor/smaltql/pull/18))
- Date and time columns read as their text (smaltdb ADR 0019 step 5) ([#19](https://github.com/stenhoor/smaltql/pull/19))
- Publish as @smaltworks/smaltql: package name, install commands and imports ([#20](https://github.com/stenhoor/smaltql/pull/20))
- List and struct columns read as their JSON text (smaltdb ADR 0020 step 5) ([#25](https://github.com/stenhoor/smaltql/pull/25))

#### 📖 Documentation

- Docs: the SQL documentation moves here, with its example tests ([#5](https://github.com/stenhoor/smaltql/pull/5))
- Docs: smaltql's own logo, colour and tagline from smalt-brand ([#6](https://github.com/stenhoor/smaltql/pull/6))
- Docs: the front page describes the language, not the engine ([#7](https://github.com/stenhoor/smaltql/pull/7))
- Docs: Parquet DATE and TIMESTAMP are date and datetime columns, read as text ([#22](https://github.com/stenhoor/smaltql/pull/22))
- Site: the smaltworks standard (menu, stage badge, footer, shared theme) ([#23](https://github.com/stenhoor/smaltql/pull/23))
- Docs: the Parquet plugin brings its own codecs ([#28](https://github.com/stenhoor/smaltql/pull/28))

#### 🛠️ Other improvements

- README: smaltdb has no language built in ([#1](https://github.com/stenhoor/smaltql/pull/1))
- Pin smaltdb to main after stenhoor/smaltdb#96 ([#3](https://github.com/stenhoor/smaltql/pull/3))
- Drop the bindStoredExprs placeholder (smaltdb ADR 0016 step 6) ([#11](https://github.com/stenhoor/smaltql/pull/11))
- Pin smaltdb to its main with neutral engine wording; error-words test states SQLite's text ([#13](https://github.com/stenhoor/smaltql/pull/13))
- Pin smaltdb to its main with ADR 0016 steps 8 and 9 ([#15](https://github.com/stenhoor/smaltql/pull/15))
- Pin smaltdb and @smaltdb/io with no SQL in the engine ([#16](https://github.com/stenhoor/smaltql/pull/16))
- Follow-ups to SQL leaving smaltdb: binding tests, FAQ sizes, stale notes ([#21](https://github.com/stenhoor/smaltql/pull/21))
- CLAUDE.md: read smalt-brand first; site kit from smalt-brand ([#24](https://github.com/stenhoor/smaltql/pull/24))
- Tagline: "Small. Alternative." on one line, the product's word on the next ([#26](https://github.com/stenhoor/smaltql/pull/26))
- Working rules: ask before adding outside code ([#27](https://github.com/stenhoor/smaltql/pull/27))


## smaltdf 0.9.0

The dataframes: a TypeScript language with dataframe interfaces, building plans for the engine. Its first release. An
earlier version that compiled to SQL ([#1](https://github.com/stenhoor/smaltdf/pull/1)–[#5](https://github.com/stenhoor/smaltdf/pull/5))
was removed in [#6](https://github.com/stenhoor/smaltdf/pull/6); nothing of it ships.

### Breaking

- None.

### Changelog

#### ✨ Enhancements

- Core frames: table, select, withColumns, filter, sort, head / tail / slice ([#9](https://github.com/stenhoor/smaltdf/pull/9))
- Aggregation: groupBy(…).agg(…), a select of aggregates, unique ([#10](https://github.com/stenhoor/smaltdf/pull/10))
- Joins and concatenation: join, joinAsof, concat ([#11](https://github.com/stenhoor/smaltdf/pull/11))
- Windows: over, cumulative functions, shift, rank ([#12](https://github.com/stenhoor/smaltdf/pull/12))
- Reshaping and data from JavaScript: pivot, unpivot, sample, frame ([#13](https://github.com/stenhoor/smaltdf/pull/13))
- Writing: insertInto, createTable, update, deleteFrom ([#14](https://github.com/stenhoor/smaltdf/pull/14))
- Views: createView, refreshView, and dfLanguage ([#15](https://github.com/stenhoor/smaltdf/pull/15))
- bool and NaN from the engine (smaltdb ADR 0018 step 7) ([#18](https://github.com/stenhoor/smaltdf/pull/18))
- Dates and times (smaltdb ADR 0019 step 6) ([#19](https://github.com/stenhoor/smaltdf/pull/19))
- Lists and structs (smaltdb ADR 0020 step 6) ([#22](https://github.com/stenhoor/smaltdf/pull/22))

#### 📖 Documentation

- Design v3: the order of work and a v0 language reference ([#7](https://github.com/stenhoor/smaltdf/pull/7))
- Record the owner's decisions A–E ([#8](https://github.com/stenhoor/smaltdf/pull/8))
- Docs site: VitePress on GitHub Pages ([#17](https://github.com/stenhoor/smaltdf/pull/17))
- Site: the smaltworks standard (menu, stage badge, footer, shared theme) ([#20](https://github.com/stenhoor/smaltdf/pull/20))

#### 🛠️ Other improvements

- Core library: Polars expressions compiled to smaltdb SQL ([#1](https://github.com/stenhoor/smaltdf/pull/1))
- Map Polars' math methods onto smaltdb's math functions ([#2](https://github.com/stenhoor/smaltdf/pull/2))
- Document the Polars differences by backend, and test every backend ([#3](https://github.com/stenhoor/smaltdf/pull/3))
- Map Polars' statistics onto smaltdb's aggregates ([#4](https://github.com/stenhoor/smaltdf/pull/4))
- smaltdf 0.1: Polars-style dataframes on smaltdb ([#5](https://github.com/stenhoor/smaltdf/pull/5))
- Remove all code that compiles to or runs SQL; revise the design ([#6](https://github.com/stenhoor/smaltdf/pull/6))
- Polars comparison tests, in their own CI job ([#16](https://github.com/stenhoor/smaltdf/pull/16))
- CLAUDE.md: read smalt-brand first; site kit from smalt-brand ([#21](https://github.com/stenhoor/smaltdf/pull/21))
- Tagline: "Small. Alternative." on one line, the product's word on the next ([#23](https://github.com/stenhoor/smaltdf/pull/23))
- Working rules: ask before adding outside code ([#24](https://github.com/stenhoor/smaltdf/pull/24))


## smaltui 0.9.0

The query workbench: an object explorer, SQL and TypeScript tabs, data grids you can browse and edit, and import tools,
in a static site. Its first release.

### Breaking

- None.

### Changelog

#### ✨ Enhancements

- Add smaltui: a static, in-browser query workbench for smaltdb ([#1](https://github.com/stenhoor/smaltui/pull/1))
- Use the smaltdb npm package; add Parquet support ([#2](https://github.com/stenhoor/smaltui/pull/2))
- Accept GitHub links (e.g. TidyTuesday) for import/link; fix Pages version override ([#4](https://github.com/stenhoor/smaltui/pull/4))
- Convert smaltui to TypeScript (strict) ([#14](https://github.com/stenhoor/smaltui/pull/14))
- Use smaltkit/urls instead of app/urls.ts ([#15](https://github.com/stenhoor/smaltui/pull/15))
- Use smaltkit/engine for loading smaltdb and the OPFS catalog ([#16](https://github.com/stenhoor/smaltui/pull/16))
- Run on smaltdb 0.9 with smaltql and the io, external and Parquet plugins ([#18](https://github.com/stenhoor/smaltui/pull/18))
- TypeScript tabs: an editor tab for smaltdf beside the SQL tab ([#25](https://github.com/stenhoor/smaltui/pull/25))
- Workbench chrome like smaltbi: Chevron-style icons, lowercase pane titles ([#26](https://github.com/stenhoor/smaltui/pull/26))
- TypeScript tabs get a SQL tab's toolbar: Explain, Analyze, Stop, Format ([#29](https://github.com/stenhoor/smaltui/pull/29))
- TypeScript tabs strip types with smaltkit/typescript (smaltty), not the sucrase plugin ([#33](https://github.com/stenhoor/smaltui/pull/33))

#### 🐞 Bug fixes

- Fix the live demo on Pages (gzipped Parquet) and add Pages-like tests ([#8](https://github.com/stenhoor/smaltui/pull/8))
- Version asset URLs so deploys never mix new pages with cached CSS/JS; smoke-test the branding ([#13](https://github.com/stenhoor/smaltui/pull/13))

#### 📖 Documentation

- Add a landing page with a live SQL console for the GitHub Pages demo ([#3](https://github.com/stenhoor/smaltui/pull/3))
- Site on the smaltworks docs theme, like smaltworks.dev and smaltbi ([#20](https://github.com/stenhoor/smaltui/pull/20))
- Site: the shared smaltworks menu, footer and badges from smalt-brand ([#22](https://github.com/stenhoor/smaltui/pull/22))
- smaltui as a query workbench; Demo in the nav, no embedded demo; brand first ([#23](https://github.com/stenhoor/smaltui/pull/23))
- Hero: one button, Getting started; the app opens only from Demo ([#24](https://github.com/stenhoor/smaltui/pull/24))
- Tagline: "Small. Alternative." on one line, the product's word on the next ([#27](https://github.com/stenhoor/smaltui/pull/27))

#### 🛠️ Other improvements

- Add CLAUDE.md with repo commands and cross-repo working rules ([#6](https://github.com/stenhoor/smaltui/pull/6))
- CLAUDE.md: document the smoke test and serve --gzip ([#11](https://github.com/stenhoor/smaltui/pull/11))
- Adopt the smalt brand: Chevron mark, Kiln tokens, brand type and voice ([#12](https://github.com/stenhoor/smaltui/pull/12))
- Brand: sync smalt-brand 2192ec3, work-in-progress stage, smaltworks family ([#17](https://github.com/stenhoor/smaltui/pull/17))
- Notebooks: SQL (smaltql) and dataframe (smaltdf) cells ([#19](https://github.com/stenhoor/smaltui/pull/19))
- Remove smaltui's notebooks: notebooks are smaltnb's ([#21](https://github.com/stenhoor/smaltui/pull/21))
- TypeScript tabs strip types with the TypeScript compiler, as smaltnb does ([#28](https://github.com/stenhoor/smaltui/pull/28))
- Working rules: ask before adding outside code ([#30](https://github.com/stenhoor/smaltui/pull/30))
- TypeScript tabs strip types with the sucrase plugin, not a CDN compiler ([#31](https://github.com/stenhoor/smaltui/pull/31))
- Parquet codecs come with the plugin: move the @smaltdb/parquet pin ([#32](https://github.com/stenhoor/smaltui/pull/32))


## smaltnb 0.9.0

Reactive notebooks: milestone 1 ("Run") is complete. The notebook page runs in your browser, with SQL and smaltdf
cells, text cells, run modes, guards, typed parameters and held writes. Its first release.

### Breaking

- None.

### Changelog

#### ✨ Enhancements

- Format and graph: parse .nb.ts notebooks and build their graph (milestone 0) ([#2](https://github.com/stenhoor/smaltnb/pull/2))
- Runtime: run notebooks by the notebook's rules (milestone 1, part 1) ([#4](https://github.com/stenhoor/smaltnb/pull/4))
- Kernel: run notebooks in a Web Worker (milestone 1, part 2) ([#5](https://github.com/stenhoor/smaltnb/pull/5))
- Database: SQL and smaltdf cells, collected results, writes checked by plan kind (milestone 1, part 3) ([#7](https://github.com/stenhoor/smaltnb/pull/7))
- database: read rows from the worker client's array results ([#13](https://github.com/stenhoor/smaltnb/pull/13))
- The notebook page: cells in the browser on the kernel and the database (milestone 1, part 4) ([#14](https://github.com/stenhoor/smaltnb/pull/14))
- SQL cells show their SQL in the page; the file keeps the TypeScript ([#17](https://github.com/stenhoor/smaltnb/pull/17))
- Parameters: param() declares typed values set from outside the notebook ([#20](https://github.com/stenhoor/smaltnb/pull/20))
- Read, bind and strip TypeScript with smaltty: no TypeScript compiler ([#23](https://github.com/stenhoor/smaltnb/pull/23))
- Text cells: md`…` renders Markdown in the page (milestone 1 complete) ([#24](https://github.com/stenhoor/smaltnb/pull/24))

#### 📖 Documentation

- Design: decisions from the initial interview ([#1](https://github.com/stenhoor/smaltnb/pull/1))
- Product site: VitePress docs on GitHub Pages ([#3](https://github.com/stenhoor/smaltnb/pull/3))
- Positioning: "Reactive notebooks in TypeScript for smaltdb." everywhere ([#6](https://github.com/stenhoor/smaltnb/pull/6))
- Positioning: back to "Reactive notebooks for smaltdb." ([#8](https://github.com/stenhoor/smaltnb/pull/8))
- Site: the smaltworks standard (menu, stage badge, footer, shared theme) ([#11](https://github.com/stenhoor/smaltnb/pull/11))
- Positioning: "Reactive notebooks for smaltdb." again where #11 changed it ([#15](https://github.com/stenhoor/smaltnb/pull/15))
- Hero: one button, Getting started; the app opens only from Demo ([#18](https://github.com/stenhoor/smaltnb/pull/18))
- Demo opens the notebook page in the same tab, like smaltui's and smaltbi's ([#19](https://github.com/stenhoor/smaltnb/pull/19))
- Tagline: "Small. Alternative." on one line, the product's word on the next ([#21](https://github.com/stenhoor/smaltnb/pull/21))

#### 🛠️ Other improvements

- Database (milestone 1, part 3), onto main: it was merged into the kernel branch instead ([#9](https://github.com/stenhoor/smaltnb/pull/9))
- CLAUDE.md: never stack PRs ([#12](https://github.com/stenhoor/smaltnb/pull/12))
- CLAUDE.md: read smalt-brand first; Demo in the nav; site kit from smalt-brand ([#16](https://github.com/stenhoor/smaltnb/pull/16))
- Working rules: ask before adding outside code ([#22](https://github.com/stenhoor/smaltnb/pull/22))


## smaltty 0.9.0

**Small. Alternative. Code.** smalt TypeScript, now a product of its own: it parses, strips, binds and type-checks
TypeScript, in our own code with no dependencies. Types are stripped to spaces, so every line and column of the
JavaScript is the one written; parsing gives TypeScript's own syntax tree; and binding says which declaration each name
means, as TypeScript's checker does. The apps use it through
`smaltkit/typescript`, which refuses code that would make code of its own (enums, namespaces with values, parameter
properties) with the line, the column and what to write instead. Checking marks the errors tsc would report on calls
into smaltdf as warnings, while the code still runs. Its first release.

### Breaking

- None.

### Changelog

#### ✨ Enhancements

- Scaffold, corpus and baseline benchmarks; the scanner and parser; the stripper (milestones 1–3) ([#1](https://github.com/stenhoor/smaltty/pull/1))
- The binder (milestone 5) ([#2](https://github.com/stenhoor/smaltty/pull/2))

#### 📖 Documentation

- Docs site: VitePress on smalt-brand's theme, deployed to GitHub Pages ([#3](https://github.com/stenhoor/smaltty/pull/3))

## smaltkit 0.9.0

Shared browser code for the smalt apps: the engine loader, the data grid, the code editor, charts, tables, controls,
formatting, Markdown, pretty printing and TypeScript. Its first release.

### Breaking

- None.

### Changelog

#### ✨ Enhancements

- Scaffold smaltkit: TypeScript package with the urls module ([#1](https://github.com/stenhoor/smaltkit/pull/1))
- Add smaltkit/engine: the smaltdb loader and OPFS catalog ([#2](https://github.com/stenhoor/smaltkit/pull/2))
- Charts, tables, formatting, SVG and DOM modules (from smaltbi) ([#3](https://github.com/stenhoor/smaltkit/pull/3))
- Add smaltkit/grid: the virtualized data grid, moved from smaltui ([#4](https://github.com/stenhoor/smaltkit/pull/4))
- Add smaltkit/sql and smaltkit/editor: the code editor, moved from smaltui ([#5](https://github.com/stenhoor/smaltkit/pull/5))
- Add smaltkit/manifest and smaltkit/controls; engine: npm: false ([#6](https://github.com/stenhoor/smaltkit/pull/6))
- Add smaltkit/markdown: small, safe Markdown, grown from smaltbi's text box ([#9](https://github.com/stenhoor/smaltkit/pull/9))
- Add smaltkit/pretty: JSON and TypeScript formatting, no dependencies ([#10](https://github.com/stenhoor/smaltkit/pull/10))
- Add smaltkit/typescript: strip TypeScript types with smaltty ([#12](https://github.com/stenhoor/smaltkit/pull/12))
- smaltkit/typescript: all of smaltty as `smaltty`; smaltty pinned with its binder ([#13](https://github.com/stenhoor/smaltkit/pull/13))

#### 📖 Documentation

- README: the smaltworks badges and links ([#7](https://github.com/stenhoor/smaltkit/pull/7))
- CLAUDE.md: read smalt-brand first; README: smaltui is the query workbench ([#8](https://github.com/stenhoor/smaltkit/pull/8))

#### 🛠️ Other improvements

- Working rules: ask before adding outside code ([#11](https://github.com/stenhoor/smaltkit/pull/11))

