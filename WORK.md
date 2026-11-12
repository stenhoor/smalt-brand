# Work in review and in progress

Cross-repository work that is proposed, waiting for decisions, or under way: one row per item, so the owner and the
orchestrator can review it together. Each item's record (an ADR, a plan) stays in its own repository. This page links
the record and says where the item stands, and it never copies the record's text.

Status is one of **Proposed** (a record in review), **Accepted** (decided, not started), **In progress**, **Blocked**
(the next step says on what) or **Done** (merged and verified). A done item leaves this page in the PR that marks it
done; its record keeps the history.

## Items

| Item | Repositories | Record | Status | Next step | Waiting on |
| --- | --- | --- | --- | --- | --- |
| smaltts, the typed API: a thin typed language over the engine's plan and schema operations, with schemas as values, change sets reviewed before they run, typed plans, reflecting and interface views, and structured flows | smaltts, smaltty, smaltdb, smaltql, smaltfl | [smaltts ADR 0023](https://github.com/stenhoor/smaltts/blob/main/docs/adr/0023-the-smaltts-language.md) | In progress | M0–M6, M9 and M10 done (stenhoor/smaltts#5–#26); E10, view interfaces in the engine, done (smaltdb ADR 0027: stenhoor/smaltdb#204–#211, stenhoor/smaltql#66, #67); E11 and the findings F2–F5 fixed in smaltdb (stenhoor/smaltdb#196, #197, #199, #200, #202, #215); the catalog lists connections and external tables (stenhoor/smaltdb#214). M7 waits on gate C, M8 on E2, M11's publish on smaltdb's | The engine issue stenhoor/smaltdb#187 (E2, for M8); the owner on gate C (flows and smaltfl); the 0.9.0 publish (for M11) |
| smaltml, machine learning on tables: classic supervised models, gradient-boosted trees, clustering, dimension reduction and anomaly detection in TypeScript, on the CPU everywhere and WebGPU where it helps, matched against scikit-learn and XGBoost | smaltml, smaltui, smaltnb | [smaltml ADR 0024](docs/adr/0024-smaltml-scope-and-architecture.md) | Proposed | The owner's decisions on the ADR's open points: time series forecasting; importing other models (ONNX); the yes on the compare tests' Python packages; when phase 2 starts; own WebAssembly kernels if TypeScript can't reach Python's speed | Owner |
| smaltai, AI in the smalt apps: an AI agent button that drives smaltui, smaltbi, smaltnb (and smaltfl) through typed actions, with a model the user brings through a local gateway they run (llama.cpp, Ollama, LM Studio, or their own proxy to a hosted model) or our own in-browser LLM on WebGPU; smalt never holds a key; permissions on what it sees and changes, and context documents generated from the code | smaltai (new), the in-browser engine (new), smaltkit, smaltnb, smaltbi, smaltui, smaltfl | [smaltai ADR 0025](docs/adr/0025-smaltai-agent-gateways-and-actions.md), [ADR 0026](docs/adr/0026-smaltai-in-browser-llm.md) | Proposed | The owner's decisions on the ADRs' open points: which app first; remembered grants; the engine's name, first architectures and quantization types; a fallback without WebGPU; the yes on WebLLM for benchmarks | Owner |
| smaltworks 0.9.0, the release: smaltdb, smaltql, smaltdf, smaltui, smaltnb, smaltty and smaltkit, with the plugins | all seven, smaltdb-io, smaltdb-external, smaltdb-parquet, smaltdb-node, smalt-brand | [Release notes](releases/0.9.0/release-notes.md) and [news story](releases/0.9.0/news.md) (drafts); smaltdb ADR 0015 steps 11–12 | Drafting | The owner's review of the drafts; then the package renames (ADR 0015 step 11), the versions set to 0.9.0, an end-to-end check of the 0.8.3 export and 0.9.0 import, the publish (step 12), `smaltdb` 0.8.3 marked deprecated, the GitHub releases, and the news page on smaltworks.dev | Owner |
| TypeScript 7 in every smalt repository: checking (`typecheck`) on TypeScript 7.0.2 now; `dist/` and `.d.ts` built with 6.0.3 for one more release, then 7; smaltty keeps 6.0.3 for its compiler API until 7 has a stable JavaScript API | every smalt repository | [smaltty ADR 0030](https://github.com/stenhoor/smaltty/blob/main/docs/adr/0030-changing-smaltty-without-breaking-its-consumers.md), decision 5; [DECISIONS.md](DECISIONS.md#typescript-and-browsers) | Accepted | Each repository's own session moves its `typecheck` script to TypeScript 7 (the owner's yes to the dev dependency is in the ADR); smaltty first, with its milestone 9; then, one release later, the builds | – |
| The documentation standard: four sections, reference entries, syntax diagrams, working demos, playgrounds, the plan language, docs for agents | smalt-brand (site kit), smaltkit, every product site; smaltql first, smaltdb for the plan language | [BRAND.md, Documentation](BRAND.md#documentation), [DECISIONS.md](DECISIONS.md#documentation-standard) | In progress | M1–M3, the site kit's components, done; M4, smaltql's site: the four sections, playgrounds and agent docs live, the grammar and diagrams in review (stenhoor/smaltql#53), then working demos; then smaltql gives the plan of a statement; smaltdb prints whole plans | – |

## smaltts, the typed API (smaltts ADR 0023)

The milestones of [smaltts MILESTONES.md](https://github.com/stenhoor/smaltts/blob/main/docs/MILESTONES.md), where
the details are. Sizes are by PRs there: S 1–2, M 3–5, L 6–10. Gates A–C are owner decisions taken on the work before
them.

| Milestone | Repository | Size | After | Status |
| --- | --- | --- | --- | --- |
| M0 The owner's decisions on outside code: TypeScript tooling from smaltty, no `typescript` | smaltts | S | | Done: stenhoor/smaltts#5 |
| Alongside: smaltty's checker covers calls into smaltts as well as smaltdf (smaltty milestone 7) | smaltty | L | | Done: stenhoor/smaltty#5–#12 (the built-in types, speed measured, gate C passed), and smaltts's npm run check runs it (stenhoor/smaltts#17, #18) |
| M1 Re-base the prototype on smaltdb 0.9.0 (behaviour names, the language interface, the catalog API) | smaltts | M | M0 | Done: stenhoor/smaltts#6 |
| M2 Specs with the engine's types (`bool`, dates and times, lists, structs) | smaltts | M | M1 | Done: stenhoor/smaltts#7, #8 |
| M3 Diff, change sets and history, complete | smaltts, smaltdb (the catalog's foreign keys, CHECKs and defaults: S) | L | M1 | Done: stenhoor/smaltts#9 |
| M4 Saved change sets (gate A: live diff plus saved change sets) | smaltts | M | M3 | Done: stenhoor/smaltts#16 |
| M5 Typed plans for the whole plan format | smaltts | M | M1 | Done: stenhoor/smaltts#10, #11, #12 |
| M6 Views: reflecting and interface (gate B: names and order before E10) | smaltts, smaltdb (E10, view interfaces: L, stenhoor/smaltdb#188), smaltql | M | M3, M5 | Done: stenhoor/smaltts#14, #15, #23; E10 as smaltdb ADR 0027 (stenhoor/smaltdb#204–#211, stenhoor/smaltql#66, #67) |
| M7 Structured flows | smaltts | L | M3, M5, gate C (with smaltfl) | Not started |
| M8 Plan review | smaltts, smaltdb (E2, EXPLAIN with costs: M, stenhoor/smaltdb#187) | S | M5, E2 | Not started |
| M9 Plugins and external data | smaltts, smaltdb (the catalog's connections: S) | M | M3 | Done: stenhoor/smaltts#24 (stenhoor/smaltdb#214) |
| M10 The client and the browser | smaltts | M | M7 | Done: stenhoor/smaltts#25, #26 (the finding F5 fixed in stenhoor/smaltdb#215); built before M7, whose flows it will run too |
| M11 Docs site and publish (the site is up; the publish waits on smaltdb's) | smaltts | M | M10 | Site done; publish not started |

## smaltml, machine learning on tables (smaltml ADR 0024)

The phases of ADR 0024, section 1. Sizes are by PRs, as for smaltts: S 1–2, M 3–5, L 6–10; they are estimates until
each phase is planned. Every phase adds its compare cases (section 7) and its benchmarks against Python (section 8).

| Milestone | Repository | Size | After | Status |
| --- | --- | --- | --- | --- |
| M0 ADR 0024 and the owner's decisions on its open points; the repository `stenhoor/smaltml` when work starts | smalt-brand, smaltml | S | | In review: ADR 0024 in smalt-brand |
| M1 The owner's yes on outside code (the compare tests' Python packages) | smaltml | S | M0 | Not started |
| M2 Phase 1: data preparation, linear models, metrics and model selection, pipelines, saving models, the worker entry | smaltml | L | M1 | Not started |
| M3 Phase 2: decision trees, random forests, extra trees | smaltml | M | M2 | Not started |
| M4 Phase 3: gradient-boosted trees, and XGBoost's model format | smaltml | L | M3 | Not started |
| M5 Phase 4: k-nearest neighbours, naive Bayes, linear SVMs, clustering, PCA | smaltml | L | M4 | Not started |
| M6 Phase 5: anomaly detection | smaltml | S–M | M5 | Not started |
| M7 Using it from TypeScript tabs and notebooks | smaltui, smaltnb | S each | M2 | Not started |
| M8 Brand (marks and words), docs site and publish | smalt-brand, smaltml | M | M2 | Brand round 1 on the canvas; rest not started |

## smaltai, AI in the smalt apps (ADRs 0025 and 0026)

The order of work in ADR 0025 (the agent, its gateways and the apps' actions) and ADR 0026 (the in-browser LLM). Sizes
are by PRs, as above: S 1–2, M 3–5, L 6–10; they are estimates until each step is planned. The two tracks can run side
by side: the agent works with remote gateways before the in-browser engine exists.

| Milestone | Repository | Size | After | Status |
| --- | --- | --- | --- | --- |
| M0 ADRs 0025 and 0026, and the owner's decisions on their open points | smalt-brand | S | | In review |
| M1 The agent package: local gateways (OpenAI-compatible first), the agent loop, permissions, action types; no keys | smaltai | L | M0 | Not started |
| M2 The chat panel | smaltkit | M | M1 | Not started |
| M3 The first app's actions and context documents (smaltnb recommended) | smaltnb | M | M1, M2 | Not started |
| M4 smaltbi's actions | smaltbi | M | M3 | Not started |
| M5 smaltui: its actions moved out of `main.ts` (can start any time), then its agent | smaltui | L | M3 | Not started |
| M6 smaltfl declares its actions as it is built | smaltfl | – | smaltfl's own plan | Not started |
| M7 In-browser engine: a first end-to-end run (one architecture, a GGUF from a URL, cached in OPFS) | the engine (new) | L | M0 | Not started |
| M8 In-browser engine: speed to the WebLLM goal | the engine | L | M7 | Not started |
| M9 In-browser engine: tool calling and the gateway interface | the engine, smaltai | M | M1, M8 | Not started |
| M10 In-browser engine: safetensors and more architectures | the engine | M–L | M9 | Not started |
| M11 Brand: smaltai's marks and words, and the engine's name | smalt-brand | S–M | M0 | Round 1–2 on the canvas; rest not started |

## The documentation standard (BRAND.md, "Documentation")

Decided 2026-11-10. Sizes are estimates, as above.

| Milestone | Repository | Size | After | Status |
| --- | --- | --- | --- | --- |
| M1 The syntax-diagram generator (grammar in EBNF to SVG, rules expanding in place) | smalt-brand (site kit) | M | | Done (stenhoor/smalt-brand#62) |
| M2 The playground component, from smaltkit's editor, grid, engine, typescript and pretty | smalt-brand (site kit), smaltkit | M | | Done (stenhoor/smalt-brand#67, which landed #64); "Open in the app" waits on the apps opening code from a link |
| M3 The agent-docs build step: Markdown twins, `/llms.txt`, the agent guide | smalt-brand (site kit) | M | | Done (stenhoor/smalt-brand#67, which landed #65) |
| M4 smaltql's site to the standard: diagrams, working demos, playgrounds, agent docs | smaltql | L | M1, M2, M3 | Four sections, playgrounds and agent docs done (stenhoor/smaltql#51, #52); grammar and diagrams in review (stenhoor/smaltql#53); working demos next |
| M5 smaltql gives the plan of a statement, for the Plan tab | smaltql | S | | Not started |
| M6 smaltdb prints whole plans (the tree view) | smaltdb | S | | Not started |
| M7 smaltdb's Plan language section and "One query, every language" | smaltdb | L | M1–M3, M5, M6 | Not started |
| M8 The other sites to the standard: smaltdf, then smaltts, the apps, the plugins and the kits | each | L each | M4 | Not started |
