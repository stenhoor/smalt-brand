# ADR 0025: smaltai, the AI agent in the smalt apps: gateways, actions and context

- **Status:** proposed. The owner's answers of 2026-11-09 are recorded below; the items under "Still to decide" are
  open.
- **Date:** 2026-11-09
- **Builds on:** smalt-brand's [DECISIONS.md](../../DECISIONS.md) (colour by layer: smaltai runs alongside the layers,
  in violet; outside code: ask first), [smaltworks.dev/environments](https://smaltworks.dev/environments) (supported
  browsers). [ADR 0026](0026-smaltai-in-browser-llm.md) is the in-browser model, one of the gateways described here.

## Context

The owner's direction (2026-11-09): smaltai lets an AI drive the smalt apps (smaltui, smaltbi, smaltnb, and smaltfl when
it exists) and automate work in them. It has three parts:

1. **Calls to AI APIs** that drive the apps.
2. **Context documents** that tell the model what it can do and what it can reach.
3. **A local LLM in the browser,** running on WebGPU, weights included. That is the largest part, and it has its own
   record, [ADR 0026](0026-smaltai-in-browser-llm.md).

**Performance is paramount.** The owner also set what the model is: always something the user brings. A remote API
(Anthropic), a server on their machine (llama.cpp), or the in-browser harness of ADR 0026 are all the same to smaltai.
None of them is required for smalt; the in-browser harness is a convenience.

What is already set:

- **Brand:** smaltai runs alongside the languages, kits and user tools and doesn't touch the engine, coloured
  blue-leaning violet (`layer-ai`). Its first round of words said "bring your own agent", "optional", "inspectable";
  its marks and words are open.
- **The apps share one origin.** smaltui, smaltbi and smaltnb are served from `stenhoor.github.io`, so they share browser
  storage: OPFS, local storage and IndexedDB. Every other page under `stenhoor.github.io` shares it too.

### How ready each app is (the analysis the owner asked for)

| App | How its state is held | What an agent would act through | Ramp-up |
|---|---|---|---|
| smaltnb (2.9k lines in `src/` and `app/`) | A notebook is TypeScript source text. `KernelClient` already has `open`, `update(source)`, `run`, `runAll`, `rows` and `state`. | Read the notebook, change a cell's source, run cells, read a cell's value or rows. The model writes code and SQL, which models are good at. | **Lowest.** The programmatic API exists; the work is the action layer over it and keeping earlier versions of the source for undo. |
| smaltbi (5.8k lines) | A report is one typed JSON document (`Report` in `src/core/types.ts`, described in `docs/REPORT_FORMAT.md`). The designer edits it through `DocStore.change`, which has undo, redo and autosave. | Typed changes to the report: add a measure, a visual, a page, a filter. Each change goes through `DocStore.change`, so it can be undone. | **Low to medium.** The document and the undo are there. The report's schema is large, so its context document needs care, and every change needs checking against the types. |
| smaltui (5.3k lines; `app/main.ts` 2,954) | Module state inside `main.ts`. Actions (`runAdHoc`, `newQueryTab`, `newTsTab`, `openTableTab`, `exportObject`, `loadEnvironment` …) are functions mixed with about 90 UI event handlers. There is no undo. | Run SQL, open a table, open a query or TypeScript tab with code, import, export. | **Medium to high.** The actions have to be moved out of `main.ts` into an action layer first, and changes to data have no undo. |
| smaltfl | Not built yet. | Whatever it is designed with. | Designs its actions in from the start. |

## Decision

### 1. What smaltai is

smaltai is the harness that connects a model the user brings to the apps. It is not a model and not an agent of its
own. In each app, an **AI agent button** appears once the user has set up a gateway. It opens a chat, and through the
chat the model works in that app using the app's actions (section 4). Without a gateway, the apps show no AI at all,
and smaltai's code isn't loaded.

### 2. Gateways: the model the user brings

A gateway is where the model runs. smaltai calls it directly from the browser. There is no smaltworks server between
them. The gateways (owner, 2026-11-09):

| Gateway | How the browser reaches it |
|---|---|
| Anthropic (Claude) | The Messages API, with tool use. Browsers may call it when the request carries `anthropic-dangerous-direct-browser-access: true`, which exists for this "bring your own key" case. |
| OpenAI | Its API, with function calling. |
| Google Gemini | The Gemini API, with function calling. |
| OpenAI-compatible servers | llama.cpp's server, Ollama, LM Studio, on the user's machine or network. The server must allow the app's origin (Ollama: `OLLAMA_ORIGINS`), and Chrome (142 and later) asks the user once before a public page may reach a local address. |
| The in-browser model | [ADR 0026](0026-smaltai-in-browser-llm.md), behind the same interface. No network request. |

One interface covers them: a chat request with tools, streamed back. Each gateway's own format (Anthropic's tool use,
OpenAI's and Gemini's function calling) stays inside its adapter. smaltai uses each gateway's prompt caching where it
offers it (section 7).

### 3. Keys and settings: the user's choice per gateway

When the user sets up a gateway, they choose whether to **remember** it on this device or keep it for **this session
only** (owner, 2026-11-09). A forget button removes a remembered gateway.

- **A key goes only to its gateway.** It is never put in a URL, a log, an exported file, or anything sent to a model.
- **A remembered key is readable by every page on the same origin.** Browser storage isn't encrypted against scripts on
  the same origin, and today the apps share `stenhoor.github.io` with every other page there. That is a reason to give
  the apps their own domain before remembered keys ship. It is listed under "Still to decide".

### 4. Actions: what the model can do in an app

Each app declares its actions. An action has:

- a name and a description, for the model;
- the shape of its input (a JSON Schema) and of its result;
- its kind: **read** (it looks at something) or **write** (it changes data, a document or the app);
- **what it touches:** which database, whether it reads rows, which document.

The agent loop offers the app's actions to the model as tools, runs the ones the model calls (within the permissions,
section 5), and returns the results. Every action the model takes is shown in the chat with its input and result.
Changes go through the app's undo where the app has it: smaltbi's `DocStore`, and earlier notebook source in smaltnb.
An action that can't be undone says so.

Actions do what a person can do in the app, through the same code paths: an action is not a back door.

### 5. Permissions: what the model may see and change

The user grants what the model can see and what it can change (owner, 2026-11-09). Writes are granted like reads:

| Grant | Covers |
|---|---|
| See the schema | Table, column and type names; the open document's outline. Granted by default, so the model can help at all. |
| See rows | Values from the user's data, in query results, samples and previews. |
| Change data | Actions that write to a database: insert, update, create tables, import. |
| Change documents | Actions that change a report, a notebook, the app's tabs and files. |

- **Grants are per gateway and per database.** Outside its grant, an action asks first, and the user can allow it once
  or grant it.
- **Before rows leave the browser, smaltai warns** (owner, 2026-11-09), and says where they are going: to a remote API,
  or to a server on this machine or network. With the in-browser model, rows never leave the browser.
- **By default, only the schema goes with a request to a remote gateway** (owner, 2026-11-09). Rows go when the user has
  granted them.

### 6. Context documents: what the model is told

The model is told what it can do through context documents, and they are generated from the code so they can't drift
from it:

- **The tools:** the app's actions, from their declarations (section 4).
- **A short guide per app:** what the app is, its parts, and how the actions combine for common work.
- **The languages:** a condensed reference for smaltql and smaltdf, so the model writes queries the engine takes.
- **The current state:** the schema the model is allowed to see and the open document's outline, kept short.

A test fails if an action has no description or input schema, and the generated documents are checked in CI.

### 7. Performance

Performance is paramount (owner, 2026-11-09). smaltai's own share of the time is kept small, and is measured:

- **Nothing when unused.** Without a gateway, smaltai's code isn't loaded and the apps are unchanged.
- **Stable context first.** The tools, guides and language references go first in every request and change rarely, so
  gateways with prompt caching can reuse them. The parts that change (the state, the chat) come after them.
- **Small results.** An action returns what the model needs (row counts, column summaries, the first rows within the
  grant), not whole tables, so requests stay small and fast.
- **Streaming** for every gateway that offers it, with actions run as soon as the model calls them.
- **Measured:** smaltai's own time per step (building the request, running an action) and the tokens a task uses,
  benchmarked per release.

### 8. Where it lives

- **The agent package, `@smaltworks/smaltai`:** the gateways, the agent loop, the permissions and the action types. It
  has no runtime dependencies and no DOM code, and it lives in `stenhoor/smaltai` when the work starts. Until then
  these records live in smalt-brand (owner, 2026-11-09).
- **The chat panel** is shared UI, so it goes in smaltkit, like the editor and the grid.
- **Each app declares its own actions**, beside the code they drive.

### 9. Which app first

The owner left this open, for this analysis (2026-11-09). The recommendation, from the table above:

1. **smaltnb first:** the programmatic API exists, notebooks are text, and the model's strength (writing code) is the
   app's way of working.
2. **smaltbi second:** the typed document and its undo make changes safe.
3. **smaltui third:** its actions need moving out of `main.ts` first. That refactor is useful on its own, and can start
   at any time.
4. **smaltfl** declares its actions as it is built.

## Consequences

- **Each app gains an action layer.** For smaltnb and smaltbi it is a thin layer over what exists; for smaltui it means
  a refactor of `main.ts`.
- **Every action is a documented, typed operation.** The same declarations serve the model, the context documents and
  tests.
- **Remote gateways see the schema by default and rows only when granted.** With the in-browser model, nothing leaves
  the browser.
- **The apps' shared origin matters now.** Keys, grants and cached weights (ADR 0026) are all per origin.
- **The brand words for smaltai need another look.** "Bring your own agent" still holds; "read-only until you approve"
  becomes "what you grant".

## Still to decide

1. **Which app first:** the recommendation in section 9, for the owner's decision.
2. **The apps' own domain before remembered keys ship** (section 3), or another way to keep keys away from other pages
   on `stenhoor.github.io`.
3. **The rows warning for a server on the user's own machine:** warn as for a remote API, or more quietly.
4. **Whether grants are remembered** with the gateway, or asked for again each session.
