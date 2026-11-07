# Plugins

<StageBadge />

smaltdb keeps its core small. Formats and data sources are plugins, so each app loads only what it needs.

| Plugin | What it adds |
| --- | --- |
| [`@smaltworks/smaltdb-io`](https://github.com/stenhoor/smaltdb-io) | CSV, TSV and JSON: external tables, `read_csv()`, `read_json()`, import and export |
| [`@smaltworks/smaltdb-external`](https://github.com/stenhoor/smaltdb-external) | Where data is read from: the web, Amazon S3, Azure Blob Storage, and files the app registers |
| [`@smaltworks/smaltdb-parquet`](https://github.com/stenhoor/smaltdb-parquet) | Parquet files, reading only the columns and row groups a query needs |

All three are version 0.9.0 and will be published together with smaltdb 0.9.0. The plugin interface is stable as API version 1, and
anyone can write a plugin: see [Writing plugins](https://smaltdb.dev/reference/api/plugins) on smaltdb.dev.

## Official, Verified, Works with

A badge says how a plugin relates to smaltdb.

| Badge | Meaning |
| --- | --- |
| <img class="sw-light" src="/media/badges/plugins/official-smaltdb.svg" alt="smaltdb official plugin" height="28"><img class="sw-dark" src="/media/badges/plugins/official-smaltdb-on-dark.svg" alt="smaltdb official plugin" height="28"> | Made and maintained by smaltworks, in the `@smaltworks` npm scope. |
| <img class="sw-light" src="/media/badges/plugins/verified-smaltdb-api-v1.svg" alt="Verified for smaltdb, API v1" height="28"><img class="sw-dark" src="/media/badges/plugins/verified-smaltdb-api-v1-on-dark.svg" alt="Verified for smaltdb, API v1" height="28"> | Made by someone else; passes the smaltworks compatibility tests for plugin API version 1. |
| <img class="sw-light" src="/media/badges/plugins/works-with-smaltdb.svg" alt="Works with smaltdb" height="28"><img class="sw-dark" src="/media/badges/plugins/works-with-smaltdb-on-dark.svg" alt="Works with smaltdb" height="28"> | The author says it works; smaltworks hasn't checked. |

Verified means the compatibility tests pass. It is not a security review. Verification opens once the compatibility
test suite is published.

Naming: the `@smaltworks` scope and names starting with `smalt` are reserved for smaltworks. Name your plugin
`smaltdb-plugin-<name>`.

[Read the docs →](https://smaltdb.dev/reference/api/plugins)
