# <Mark product="ql" :size="40" /> smaltql

**Small. Alternative. Familiar.** The SQL you know, for smaltdb.

smaltql is smaltdb's SQL: the language you query the engine with, in a dialect that follows SQLite. It is moving out
of the smaltdb repository into its own, so the engine can focus on running queries fast and the language can grow its
own identity.

- **Familiar SQL always works.** smaltql can add syntax of its own, but only on top of SQL. It never changes what
  working SQL means.
- **A peer of smaltdf.** Both languages build plans for the same plan layer, so SQL and dataframes get the same
  optimizer and the same storage.
- **Its own `open()`.** Install smaltql and you have a SQL database on smaltdb. Today, SQL is still inside smaltdb.

**Status:** planned. SQL works today, inside smaltdb. The move to its own package comes after the last steps of smaltdb's
shared plan layer.

[Repository →](https://github.com/stenhoor/smaltql)
