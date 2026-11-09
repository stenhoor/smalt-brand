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
| SQL for the new engine features: fixes for what SQL reaches by accident, Postgres and DuckDB spellings for the types and plan operations that smaltdf uses, `unnest` | smaltdb, smaltql | [smaltdb ADR 0022](https://github.com/stenhoor/smaltdb/pull/181) | Proposed | The owner's decisions 2–5: hide engine names from SQL; empty and NULL lists in `unnest`; `LATERAL`; several lists in `unnest` | Owner |
| smaltts, the typed API: a thin typed language over the engine's plan and schema operations, with schemas as values, change sets reviewed before they run, typed plans, reflecting and interface views, and structured flows | smaltts, smaltdb, smaltfl | [ADR 0023](https://github.com/stenhoor/smaltts/pull/4) | Proposed | The owner's decisions on the ADR's open points: migrations on disk; expression names; plugin descriptors; which engine proposals to open (E1, E2, E10); and the yes on the prototype's dev dependencies (milestone 0) | Owner |

## SQL for the new engine features (smaltdb ADR 0022)

The ADR's order of work. Sizes count tests and docs: S under 300 lines, M 300–800, L over 800. M1 fixes bugs under
accepted ADRs (0018–0020), so it can start before ADR 0022 is accepted.

| Milestone | Repository | Size | PRs | After | Status |
| --- | --- | --- | --- | --- | --- |
| M0 ADR 0022 | smaltdb | S | 1 | | In review: stenhoor/smaltdb#181 |
| M1 Fix the leaks: computed dates, lists and truth values reach SQL as SQLite's; a function allow-list | smaltql | M, ~500 | 1 | | Not started |
| M2 The smaltdb extensions page of the functions reference | smaltql | S, ~250 | 1 | M1 | Not started |
| M3 Dates: `EXTRACT`, `date_trunc`, literals, `INTERVAL`, `strptime` | smaltql | L, ~900 | 2 | M1 | Not started |
| M4 `REGEXP`, `isnan`, `arg_min` / `arg_max`, `IGNORE NULLS` | smaltql | M, ~450 | 1 | M1 | Not started |
| M5 Lists: `ARRAY[…]`, the `array_*` names, `array_agg` | smaltql | M, ~600 | 1 | M1 | Not started |
| M6 `unnest` and struct fields | smaltql | L, ~1,000 | 2 | M5 | Not started |
| M7 `DISTINCT ON`, `TABLESAMPLE`, `ASOF JOIN`, `PIVOT` / `UNPIVOT` | smaltql | L, ~1,800 | 4 | M1 | Not started |
| M8 `TIME` literals (`cast_time` first) | smaltdb, smaltql | S, ~200 | 2 | M3 | Not started |

## smaltts, the typed API (ADR 0023)

The milestones of [smaltts MILESTONES.md](https://github.com/stenhoor/smaltts/blob/main/docs/MILESTONES.md), where
the details are. Sizes are by PRs there: S 1–2, M 3–5, L 6–10. Gates A–C are owner decisions taken on the work before
them.

| Milestone | Repository | Size | After | Status |
| --- | --- | --- | --- | --- |
| M0 The owner's yes on outside code (the prototype's dev dependencies) | smaltts | S | | Waiting on the owner |
| M1 Re-base the prototype on smaltdb 0.9.0 (behaviour names, the language interface, the catalog API) | smaltts | M | M0 | Not started |
| M2 Specs with the engine's types (`bool`, dates and times, lists, structs) | smaltts | M | M1 | Not started |
| M3 Diff, change sets and history, complete | smaltts, smaltdb (the catalog's foreign keys, CHECKs and defaults: S) | L | M1 | Not started |
| M4 Saved change sets | smaltts | S–M | M3, gate A | Not started |
| M5 Typed plans for the whole plan format | smaltts | M | M1 | Not started |
| M6 Views: reflecting and interface | smaltts, smaltdb (E10, view interfaces: L) | M | M3, M5, gate B | Not started |
| M7 Structured flows | smaltts | L | M3, M5, gate C (with smaltfl) | Not started |
| M8 Plan review | smaltts, smaltdb (E2, EXPLAIN with costs: M) | S | M5 | Not started |
| M9 Plugins and external data | smaltts | M | M3 | Not started |
| M10 The client and the browser | smaltts | M | M7 | Not started |
| M11 Docs site and publish (the site is up; the publish waits on smaltdb's) | smaltts | M | M10 | Site done; publish not started |
