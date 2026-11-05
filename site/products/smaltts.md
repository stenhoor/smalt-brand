# <Mark product="ts" :size="40" /> smaltts

**Small. Alternative. Typed.** smaltdb, straight from TypeScript.

smaltts is a thin, typed TypeScript API for smaltdb, for applications and tools that want to work with the engine
directly, without a query language or dataframes in between.

- **Typed.** Tables, columns and results carry their TypeScript types, so the compiler checks your data access.
- **Structured flows.** Each call builds on the last, in plain TypeScript.
- **Thin.** smaltts maps its calls onto the engine's own plans and schema operations. It has no engine of its own,
  so it gets smaltdb's optimizer and storage, like [smaltql](/products/smaltql) and [smaltdf](/products/smaltdf).

**Status:** planned.
