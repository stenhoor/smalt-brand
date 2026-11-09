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

## SQL for the new engine features (smaltdb ADR 0022)

The ADR's order of work. Sizes count tests and docs: S under 300 lines, M 300–800, L over 800. M1 fixes bugs under
accepted ADRs (0018–0020), so it can start before ADR 0022 is accepted.

| Milestone | Repository | Size | PRs | After | Status |
| --- | --- | --- | --- | --- | --- |
| M0 ADR 0022 | smaltdb | S | 1 | | In review: stenhoor/smaltdb#181 |
| M1 Fix the leaks: computed dates, lists and truth values reach SQL as SQLite's; a function allow-list | smaltql | M, ~500 | 1 | | In review: stenhoor/smaltql#33 (the allow-list waits for decision 2) |
| M2 The smaltdb extensions page of the functions reference | smaltql | S, ~250 | 1 | M1 | Not started |
| M3 Dates: `EXTRACT`, `date_trunc`, literals, `INTERVAL`, `strptime` | smaltql | L, ~900 | 2 | M1 | Not started |
| M4 `REGEXP`, `isnan`, `arg_min` / `arg_max`, `IGNORE NULLS` | smaltql | M, ~450 | 1 | M1 | Not started |
| M5 Lists: `ARRAY[…]`, the `array_*` names, `array_agg` | smaltql | M, ~600 | 1 | M1 | Not started |
| M6 `unnest` and struct fields | smaltql | L, ~1,000 | 2 | M5 | Not started |
| M7 `DISTINCT ON`, `TABLESAMPLE`, `ASOF JOIN`, `PIVOT` / `UNPIVOT` | smaltql | L, ~1,800 | 4 | M1 | Not started |
| M8 `TIME` literals (`cast_time` first) | smaltdb, smaltql | S, ~200 | 2 | M3 | Not started |
