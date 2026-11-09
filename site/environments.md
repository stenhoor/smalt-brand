# Supported environments

The smalt family runs in the browser: the engine in a Web Worker, your data in the browser's Origin Private File System
(OPFS). This page lists the browsers and runtimes each product needs, and which of them we test. Everything here is
[work in progress](/stability), so these minimums can still move.

## Browsers

The oldest version each product works in. Edge follows Chrome.

| Product | Chrome and Edge | Firefox | Safari |
|---|---|---|---|
| smaltdb, its plugins and the languages (smaltql, smaltdf) | 108 | 114 | 17 |
| smaltui · query workbench | 111 | 114 | 17 |
| smaltnb · notebooks | 111 | 114 | 17 |
| smaltbi · reports | 111 | 121 | 17 |

Why each line is where it is:

- **The engine** needs OPFS files with synchronous reads and writes (Chrome 108, Firefox 111, Safari 17) in a worker
  loaded as a JavaScript module (Firefox 114). [smaltdb ADR 0002](https://smaltdb.dev/adr/0002-second-round-decisions)
  sets the engine's minimum at Firefox 111; module workers make it 114 today.
- **The apps** also need CSS `color-mix()` for their colours (Chrome 111, Firefox 113).
- **smaltbi** uses CSS `:has()` to keep a slicer's open list above the other visuals (Firefox 121).

Internet Explorer and the original Edge (before it moved to Chromium) are not supported.

### What we test

- **The engine and its plugins** run their browser tests on every pull request in the current stable Chromium,
  Firefox and WebKit (Safari's engine): smaltdb, `@smaltdb/external` and `@smaltdb/parquet`.
- **The apps** (smaltui, smaltbi, smaltnb) run their end-to-end tests in Chromium only.
- **The minimum versions above are not tested.** They come from when each feature shipped. If something breaks in a
  supported version, [tell us](/community/get-involved).
- **Phones and tablets** are not tested yet.

## What the page needs

- **A secure context:** HTTPS, or `localhost` while you develop. Browsers don't give OPFS to plain HTTP pages.
- **OPFS:** some private browsing windows have none. Open the database in memory there
  (`storage: 'memory'`); it is discarded when it closes.
- **Workers:** a page whose Content Security Policy blocks workers can't run the engine.

## Faster where the browser allows it

The engine checks what the browser offers when it starts, and turns these on when it can. Without them it still works, in
one worker, with short queries taking turns with long ones.

| When | You get |
|---|---|
| The page is cross-origin isolated (served with the COOP and COEP headers) | Parallel reader workers, and running statements can be interrupted |
| The browser lets several workers open one OPFS file (Chrome and Edge 121) | Readers open the files themselves; large aggregates are split across them |
| Web Locks, with SharedWorker or BroadcastChannel | One engine shared by every tab of the same site |
| The Content Security Policy allows `new Function` | Expressions are compiled instead of interpreted |

GitHub Pages can't send the COOP and COEP headers, so the hosted demos run without parallel readers. Hosts that can
(Netlify and Cloudflare Pages, through a `_headers` file) get them.

Some app features need a particular browser too. smaltui keeps a linked local file across reloads only in Chrome and
Edge (the File System Access picker); in Firefox and Safari, attach the file again after a reload.

## Node.js

| Package | Node.js |
|---|---|
| smaltdb, smaltql, smaltdf and the plugins | 20 or later |
| smaltnb and smaltkit | 22.18 or later |

In Node, the engine runs in the same thread as your code, with an in-memory database (`Database.openMemory()` from
`smaltdb/engine`). `@smaltdb/external` can read files from the local file system there. Every package's tests run on
Node 22.
