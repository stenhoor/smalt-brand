<!--
DRAFT, not published. The news story for smaltworks 0.9.0, for smaltworks.dev and wherever the release is
announced. Publish it the day the packages are on npm, and set the date below then.
-->

<img alt="Work in progress. Come build with us." src="https://raw.githubusercontent.com/stenhoor/smalt-brand/main/badges/work-in-progress.svg" height="56">

# smaltworks 0.9.0: one engine, two languages, and your browser is the data lab

*smaltworks · [date of the publish]*

**smaltworks 0.9.0 is out.** It's the first release of the smalt family as a family: a database engine that lives in your
browser, the SQL you know, dataframes in TypeScript, a query workbench, reactive notebooks, and smalt TypeScript,
smaltty, holding it all together. Open a tab, load some data, and start asking it questions.

It's a preview. It works, it's moving fast, and it will change. If that sounds like fun, read on.

## An engine that speaks languages

smaltdb was a database with SQL built in. In 0.9.0 it becomes an **engine that runs plans**, and languages build those
plans. Every language gets the same optimizer, the same fused scans, the same spilling to disk when the data gets big.

Two languages ship today:

- **smaltql** is the SQL you know. Your queries, views, windows and recursive CTEs work as you'd expect, with the error
  messages you'd expect.
- **smaltdf** is dataframes in TypeScript. Select, filter, group, join (as-of joins included), window, pivot and reshape,
  in method chains your editor can check, and every step runs inside the engine.

```ts
import { table, col } from '@smaltworks/smaltdf';

const top = table('orders')
  .filter(col('qty').gt(0))
  .groupBy('region')
  .agg(col('price').mul(col('qty')).sum().alias('revenue'))
  .sort('revenue', { descending: true });
```

Two languages, one database. Write a table in SQL, read it back as a frame, and the other way round.

## More kinds of data

0.9.0 brings real types to the engine:

- **true and false,** as booleans.
- **Dates, times and durations,** with time zones as values you pass in, never a setting hidden somewhere else.
- **Lists and structs,** with `explode` to turn a list into rows and `implode` to gather rows back into one.
- **Parquet files arrive typed,** dates and nested columns included.

## A workbench and a notebook, right in the page

**smaltui** is a query workbench that lives in your browser. Explore your tables, write SQL in one tab and smaltdf in
the next, and use Explain, Analyze, Stop and Format in both. Point it at a CSV, JSON or Parquet file, or paste a link to
a dataset on GitHub, and you're querying.

**smaltnb** is reactive notebooks. A notebook is a plain TypeScript file: cells are top-level code, and they rerun when
the values they read change. SQL cells, dataframe cells, Markdown text and typed parameters sit side by side, and a
notebook can import another notebook like a library.

Both are static sites: the engine runs in your browser, and your data stays there.

## TypeScript, our way

Typing code into a workbench tab or a notebook cell means TypeScript has to run in the page. **smaltty**, smalt
TypeScript, does that: it parses, strips and binds TypeScript right in the browser. Types are stripped to spaces, so
every line and column of an error points at the code you wrote. It also checks your calls into smaltdf as you type,
and shows TypeScript's errors as warnings while the code still runs.

## Under the hood

- **Parallel readers in every major browser.** On a cross-origin isolated page, queries run on reader workers in
  Chromium, Firefox and Safari alike, so a long report doesn't hold up everything else.
- **A small core with plugins around it.** CSV, TSV and JSON, external files (URLs, S3, Azure Blob Storage), and
  Parquet are plugins you add when you need them, on a plugin API we've committed to keeping.
- **Faster where it counts.** Window functions, page checksums and statement planning all got quicker; the
  [release notes](release-notes.md) link each change to its benchmark.

## Who it's for

smaltworks 0.9.0 is for people who like trying new things, don't mind a breaking change, and want a say in how it turns out.
It's not yet for production, or for data you can't recreate. Before 1.0, any release can change the API or the file
format, and we'll always tell you up front, in a **Breaking** section at the top of every release's notes.
[What that means →](https://smaltworks.dev/stability)

Coming from smaltdb 0.8.3? The package names change, SQL moves to its own package, and 0.9.0 uses a new file format,
so export your data with 0.8.3 and import it again. The [release notes](release-notes.md) walk through it.

## Try it, break it, tell us

- **Open the workbench:** [stenhoor.github.io/smaltui](https://stenhoor.github.io/smaltui/)
- **Open a notebook:** [stenhoor.github.io/smaltnb](https://stenhoor.github.io/smaltnb/)
- **Build with it:**

  ```sh
  npm install --save-exact @smaltworks/smaltdb@0.9.0 @smaltworks/smaltql@0.9.0 @smaltworks/smaltdf@0.9.0
  ```

- **Tell us what broke,** what surprised you, and what you'd build next:
  [Get involved](https://smaltworks.dev/community/get-involved).

Work in progress. Come build with us.

Stay smalty.
