# <Mark product="ql" :size="40" /> smaltql

<StageBadge />

**Small. Alternative. Familiar.** The SQL you know, for smaltdb.

smaltql is smaltdb's SQL: the language you query the engine with, in a dialect that follows SQLite. It has its own
repository and package, so the engine can focus on running plans fast and the language can grow its own identity.

- **Familiar SQL always works.** smaltql can add syntax of its own, but only on top of SQL. It never changes what
  working SQL means.
- **A peer of smaltdf.** Both languages build plans for the same plan layer, so SQL and dataframes get the same
  optimizer and the same storage.
- **Its own `open()`.** Install smaltql and you have a SQL database on smaltdb.

**Status:** in development, with smaltdb 0.9.0; neither is on npm yet. SQL has moved out of smaltdb into smaltql
([smaltdb ADR 0015](https://smaltdb.dev/adr/0015-smaltql)).

[Read the docs →](https://stenhoor.github.io/smaltql/) · [Repository →](https://github.com/stenhoor/smaltql)
