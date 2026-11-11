# <Mark product="fl" :size="40" /> smaltfl

<StageBadge />

**Small. Alternative. Flow.** Data pipelines for smaltdb.

smaltfl, said "smalt-flow", reads daily files, runs them through steps written as [smaltnb](/products/smaltnb)
notebooks, and publishes datasets, built visually and run in the browser on [smaltdb](/products/smaltdb).

- **A day that is off is paused, not published.** Each day's load is judged against the days before it. A day that is
  off is held, told as one cause with what it reaches, until someone with the right to decides: publish it as is, keep
  it back, fill it from another day, or accept a new level.
- **Notebooks are the steps.** A flow's steps are the cells of smaltnb notebooks, read top to bottom with each step's
  output, the rules it caught and the models beneath it.
- **Gates, bronze to gold.** Written checks hold; learned ones warn. Bands, due dates, scope and dependency rules, and
  a reconciled, sealed gold layer.
- **An ontology people edit.** What each file's columns mean, the rules its rows are held to and the fixes a held day
  may be offered, set once and shared by every flow that reads the file.
- **Every run can be checked.** Content hashes, signed run manifests, a hash-chained record and an audit bag anyone can
  verify offline.

**Status:** in early development, not yet published. The demo runs a control estate in your browser: 600
applications, twelve security controls and a year of history. See [its status page](https://stenhoor.github.io/smaltfl/guide/status).

[Try the live demo →](https://stenhoor.github.io/smaltfl/app/) · [Read the docs →](https://stenhoor.github.io/smaltfl/) · [Repository →](https://github.com/stenhoor/smaltfl)
