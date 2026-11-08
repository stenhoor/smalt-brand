# Where things stand

As of November 2026. Each project's repository has its own roadmap.

| Project | Version | Status |
| --- | --- | --- |
| [smaltdb](/products/smaltdb) | 0.9.0 | **Preview.** On npm: 0.8.3. 0.9.0, with the plugin system, is next. [Docs](https://smaltdb.dev) |
| [smaltdb plugins](/products/plugins) | 0.9.0 | **Preview.** To be published with smaltdb 0.9.0. Plugin API version 1 is stable. [Docs](https://smaltdb.dev/reference/api/plugins) |
| [smaltql](/products/smaltql) | 0.9.0 | **In development.** SQL has moved out of smaltdb into smaltql; to be published with smaltdb 0.9.0. [Docs](https://stenhoor.github.io/smaltql/) |
| [smaltts](/products/smaltts) | — | **Planned.** |
| [smaltdf](/products/smaltdf) | 0.1.0 | **In development,** coming soon. [Docs](https://stenhoor.github.io/smaltdf/) |
| [smaltui](/products/smaltui) | 0.1.0 | **In development.** SQL and smaltdf dataframes, in editor tabs. [Demo](https://stenhoor.github.io/smaltui/workbench/?env=envs/demo/env.json) · [Docs](https://stenhoor.github.io/smaltui/) |
| [smaltbi](/products/smaltbi) | 0.1.0 | **In development.** The designer, viewer and publishing work end to end. [Demo](https://stenhoor.github.io/smaltbi/designer.html?report=examples/sales/report.json) · [Docs](https://stenhoor.github.io/smaltbi/) |
| [smaltnb](/products/smaltnb) | — | **In early development.** The notebook page is out: notebooks run in your browser, with SQL and smaltdf cells. [Demo](https://stenhoor.github.io/smaltnb/app/) · [Docs](https://stenhoor.github.io/smaltnb/) |
| [smaltkit](/products/kits) | 0.5.0 | **In development,** used by smaltui and smaltbi; not on npm yet. Its TypeScript kit, smaltty, runs smaltui's TypeScript tabs. |

Everything before 1.0 can change, including smaltdb's on-disk format: [work in progress, come build with us](/stability).

Packages publish to npm under the smaltworks organisation, named after their repositories: `@smaltworks/smaltdb`,
`@smaltworks/smaltql`, `@smaltworks/smaltdf`, `@smaltworks/smaltdb-parquet` and so on. smaltdb 0.8.3 is the last
release under the old name, `smaltdb`.
