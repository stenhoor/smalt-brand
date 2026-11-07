# Where things stand

As of November 2026. Each project's repository has its own roadmap.

| Project | Version | Status |
| --- | --- | --- |
| [smaltdb](/products/smaltdb) | 0.9.0 | **Preview.** On npm: 0.8.3. 0.9.0, with the plugin system, is next. |
| [smaltdb plugins](/products/plugins) | 0.9.0 | **Ready,** to be published with smaltdb 0.9.0. Plugin API version 1 is stable. |
| [smaltql](/products/smaltql) | — | **Planned.** SQL works today inside smaltdb; it moves to its own package after the shared plan layer. |
| [smaltts](/products/smaltts) | — | **Planned.** |
| [smaltdf](/products/smaltdf) | 0.1.0 | **In development,** coming soon. [Docs](https://stenhoor.github.io/smaltdf/) |
| [smaltui](/products/smaltui) | 0.1.0 | **Usable,** with a [live demo](https://stenhoor.github.io/smaltui/). |
| [smaltbi](/products/smaltbi) | 0.1.0 | **Working skeleton,** with a [live sample](https://stenhoor.github.io/smaltbi/). |
| [smaltnb](/products/smaltnb) | — | **In early development.** The notebook format works; running notebooks is next. [Docs](https://stenhoor.github.io/smaltnb/) |
| [smaltkit](/products/kits) | 0.2.0 | **In use** by smaltui and smaltbi; not on npm yet. |

Everything before 1.0 can change, including smaltdb's on-disk format: [work in progress, come build with us](/stability).

Packages publish to npm under the smaltworks organisation, named after their repositories: `@smaltworks/smaltdb`,
`@smaltworks/smaltql`, `@smaltworks/smaltdf`, `@smaltworks/smaltdb-parquet` and so on. smaltdb 0.8.3 is the last
release under the old name, `smaltdb`.
