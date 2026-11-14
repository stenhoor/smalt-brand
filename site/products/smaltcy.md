# <Mark product="cy" :size="40" /> smaltcy

<StageBadge />

**Small. Alternative. Connected.** A graph database for the browser that speaks Cypher.

smaltcy, said "smalt-sigh", keeps a graph of nodes and relationships in the page and answers Cypher queries on it.
It is one of the family's languages, beside [smaltql](/products/smaltql), [smaltdf](/products/smaltdf) and
[smaltts](/products/smaltts).

- **Cypher on plans.** Cypher compiles to graph plans, plain JSON that the engine checks and runs, in the shape of
  smaltdb's plans.
- **Pluggable stores.** The engine runs the same plans on any store: an in-memory adjacency store for writes, or a
  compact CSR store for reads.
- **Paths and history.** Variable-length and shortest paths, aggregates and `EXPLAIN`, and every version of the graph
  kept for time travel (`AT VERSION`, `AT TIME`).
- **Drawn on the GPU.** A WebGPU view draws graphs in 2D and 3D, with the force layout in compute shaders.

**Status:** 0.1.0, in development. Graphs live in memory today; durable storage comes from smaltdb. See
[the playground](https://stenhoor.github.io/smaltcy/playground) and [the tech demo](https://stenhoor.github.io/smaltcy/demo).

[Try the playground →](https://stenhoor.github.io/smaltcy/playground) · [Read the docs →](https://stenhoor.github.io/smaltcy/) · [Repository →](https://github.com/stenhoor/smaltcy)
