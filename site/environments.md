# Supported environments

The smalt family runs in the browser: the engine in a Web Worker, your data in the browser's Origin Private File System
(OPFS). This page lists the browsers and runtimes each product needs, and which of them we test. Everything here is
[work in progress](/stability), so these minimums can still move.

## Browsers

The oldest version each product works in, and in brackets the share of that browser's users on a supported version.
Edge follows Chrome. The last column is the share of all browser users worldwide.

| Product | Chrome and Edge | Firefox | Safari | All users |
|---|---|---|---|---|
| smaltdb, its plugins and the languages (smaltql, smaltdf) | 108&nbsp;(99.3%) | 114&nbsp;(99.4%) | 17&nbsp;(94.5%) | 91.1% |
| smaltui · query workbench | 111&nbsp;(98.3%) | 114&nbsp;(99.4%) | 17&nbsp;(94.5%) | 90.4% |
| smaltnb · notebooks | 111&nbsp;(98.3%) | 114&nbsp;(99.4%) | 17&nbsp;(94.5%) | 90.4% |
| smaltbi · reports | 111&nbsp;(98.3%) | 121&nbsp;(91.4%) | 17&nbsp;(94.5%) | 90.2% |

Usage comes from [Can I use](https://caniuse.com/usage-table) (which takes it from StatCounter), as of 6 November 2026
(`caniuse-lite` 1.0.30001823). Each browser includes its phone version: Safari includes Safari on iPhone and iPad, and
Chrome includes Chrome for Android, whose current version is counted as supported. About two thirds of Safari's unsupported share
is Safari on iPhone and iPad before iOS 17; the rest is Safari on the Mac before 17.

Samsung Internet and Opera (4% of users) are built on newer versions of Chrome's engine than these minimums, but we
don't test them, so they aren't counted. To recompute a line, run for example
`npx browserslist --coverage "chrome >= 108, edge >= 108, and_chr >= 0, firefox >= 114, and_ff >= 0, safari >= 17, ios_saf >= 17"`.

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

## Why newer browsers

We build on what browsers can do now, not on what they used to lack.

- **A real database needs real files.** The engine keeps your data in files it reads and writes in place, from a worker,
  without waiting on each call. Browsers gave web pages that only recently: Chrome and Edge 108, Firefox 111 and
  Safari 17. Before then, a page had no file it could update in place like this.
- **Small means no catch-up code.** We ship the JavaScript today's browsers run (ES2022), with nothing added to fill in
  for older ones. Supporting them would mean translating our code down to older JavaScript and adding polyfills: more to
  download, and most of it someone else's code. The family keeps
  outside code out of its core, so we leave it out.
- **One way through.** Every supported browser runs the same code. Where a newer browser offers more, such as files
  that several workers can open at once, the engine uses it on top; there is no slower second path to keep working for
  old browsers.
- **Most people are already there.** Browsers update themselves, and the minimums above reach about nine in ten users
  worldwide today. That share grows on its own.
- **Before 1.0, we move with the platform.** As browsers add what a database can use, we may raise a minimum. Each
  change is listed here and called out under **Breaking** in the release notes.

## Targets, and when they move

Family rules since 2026-11-12 ([smaltty ADR 0030](https://github.com/stenhoor/smaltty/blob/main/docs/adr/0030-changing-smaltty-without-breaking-its-consumers.md),
decisions 5 and 6):

- **Plain ES2022 modules.** What every product ships loads in a current browser as it is, with no bundler.
- **Built-in types follow Baseline.** The browser APIs smaltty's checker knows are web-features Baseline "widely
  available": what you can call in the browsers the apps support. The next step is Baseline 2024.
- **Reviewed once a year.** The output target and the baseline are reviewed together, in a decision record.
- **The latest TypeScript.** Every smalt repository is on the latest stable TypeScript, within one minor release.
  Type checking runs on TypeScript 7; the JavaScript and `.d.ts` files the packages ship are built with TypeScript
  6.0.3 for one more release, then with 7.

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
