# ADR 0032: git through the local repository: no credentials, no remotes

- **Status:** accepted (2026-11-13), with the owner's answers below ("The owner's decisions").
- **Date:** 2026-11-13
- **Replaces:** smaltnb's [DESIGN.md](https://github.com/stenhoor/smaltnb/blob/main/docs/DESIGN.md) decision 16 ("The
  repo lives in OPFS as real git (isomorphic-git) and syncs with GitHub through its REST Git Data API").
- **Builds on:** smaltnb DESIGN.md decision 19 (credentials: secrets stay secret); smalt-brand's
  [DECISIONS.md](../../DECISIONS.md) (outside code: ask first);
  [smaltworks.dev/environments](https://smaltworks.dev/environments) (supported browsers).

## Context

smaltnb's milestone 2 is git: notebooks in a repository, with per-cell diffs and commits. Decision 16 chose
isomorphic-git in OPFS, synced with GitHub through its API. Working through it (2026-11-12/13), the owner set three
constraints that rule that design out:

1. **smalt holds no credential.** "Any token we take on is a security vector for smalt to now have to worry about."
   Not stored, not encrypted at rest, not held in memory for one request.
2. **Users don't have to install git.**
3. **No heavy framework or tight integrations.** smalt doesn't build host-specific adapters, run a service, ship a
   desktop app, or live inside another product's editor.

What was found:

- **A browser can't talk git to GitHub or GitLab.** Their git endpoints send no CORS headers (checked 2026-11-12:
  `github.com/…/info/refs` and `gitlab.com/…/info/refs` answer without `Access-Control-Allow-Origin`). Their REST APIs do
  (`*`), but they need a token.
- **"Sign in with GitHub" needs a server.** GitHub's token exchange sends no CORS header either; GitHub added PKCE in
  July 2025, but whether the exchange works without a client secret wasn't confirmed.
- **Browser key features don't remove the token.** Non-extractable WebCrypto keys and passkeys never expose their
  secret, but they only sign; GitHub's API and push accept neither. A passkey (WebAuthn PRF) can lock a stored token,
  but the token is decrypted in memory to use. Password managers fill it in, and the page reads it. No browser offers
  to hold a secret and attach it to another site's requests without the page seeing it.
- **Other browser projects fall into three camps** (survey, 2026-11-13):

  | Camp | Projects | Who holds the credential |
  |---|---|---|
  | A token in the browser | TiddlyWiki's GitHub saver, Obsidian Git on mobile (isomorphic-git), Sveltia CMS's remote mode | The app, in localStorage or a settings file. Leaks into saved files have been reported |
  | A server holds it | Decap CMS (an OAuth server with the client secret), marimo Hub, hosted IDEs, JupyterLite with a deployed helper | The service |
  | Files and the user's own git | Observable Framework and Notebook Kit, marimo (notebooks as `.py` files), Sveltia CMS's local repository mode, jupyterlab-git (on the user's own machine) | **Nobody in the app** |

  Every project that refuses to hold credentials is in the third camp; none found a way around it. The closest to
  smalt is Sveltia CMS's local mode: the browser's File System Access API reads and writes a local repository's files,
  with no proxy and no setup, and the user's own tools commit and push.

## Decision

1. **smalt never holds a credential and never talks to a remote repository.** No tokens, no OAuth, no host APIs (GitHub,
   GitLab, …), no proxy or relay, no git network protocol. Syncing with a remote (fetch, pull, push) is done by the
   user's own tools: git, GitHub Desktop, an editor, whatever they use. smalt doesn't know which.
2. **The page works in a local repository folder** (File System Access API, `showDirectoryPicker`). The user picks the
   repository's folder once; from Chrome 122, "Allow on every visit" keeps the grant. In it, the page:
   - opens and saves `.nb.ts` files as plain files in the working tree (and imports other notebooks from it);
   - reads `.git`, never writing it, to show per-cell changes against `HEAD` or any branch, per-cell history and blame,
     and which notebooks changed;
   - shows a merge conflict per cell: git writes conflict markers into the file, and the page resolves them cell by
     cell and saves the file.
3. **Git's format, read by our own code, in smaltkit** (owner, 2026-11-13). The reader handles git's objects (blob, tree, commit, tag), loose and packed,
   including delta-compressed objects (cloned repositories are packed), refs and packed refs, and a line diff (Myers),
   with a per-cell diff on top. SHA-1 from `crypto.subtle`; zlib from the browser's `DecompressionStream('deflate')`. No
   outside code. Tests compare every result with the `git` command in Node CI. Estimated at about 1,200 lines.
4. **No commits from the page** (owner, 2026-11-13: until further notice). Level 2, for the record, would be writing objects, the branch ref and the index into
   `.git`, following git's own lock protocol (`*.lock` files moved into place), refusing while a merge or rebase is in
   progress (`MERGE_HEAD`, `rebase-merge/`), and tested against the `git` command. It is not built: the user makes
   every commit, and all work with remotes, in their own tools.
5. **Headless runs** (`smaltnb run`, `smaltnb build`) read and write ordinary files on disk; git around them is the
   user's, or a CI system's (GitHub Actions commits with the job's own token, which GitHub issues and expires; smalt
   never sees it).
6. **Browsers without folder access** (Firefox and Safari refuse `showDirectoryPicker`; both browsers' positions are
   negative): the page opens and downloads files, as today. Nothing else changes for them.
7. **Outputs are never stored with the notebook** (as in decision 16).

### What it costs and what it leaves out

| | Level 1 (this ADR) | Level 2 (not built) |
|---|---|---|
| Credentials in smalt | none | none |
| Install | none (git, if the user syncs, is theirs) | none |
| Browsers | Chrome and Edge, desktop | Chrome and Edge, desktop |
| Writes to `.git` | no | yes, with git's locks |
| Commit | the user's tools | the page |
| Push, pull, fetch | the user's tools | the user's tools |
| Our code | about 1,200 lines | about 600 more (writing objects, refs, the index) |
| Risk to the user's repository | none (working files only) | medium: must match git exactly |

Not handled at either level: hooks, Git LFS, submodules, a `.git` outside the picked folder (worktrees, `--separate-git-dir`).

### Considered and not chosen

| Option | Why not |
|---|---|
| isomorphic-git, GitHub sync (decision 16) | Outside code; remotes still need a token, and a CORS proxy for git's protocol |
| A token kept by the browser's password manager, or locked by a passkey (WebAuthn PRF) | smalt still holds the token while it is used: a security vector (constraint 1) |
| OAuth through a server we run, or a CORS relay | Tokens pass through our server; a service to run and secure (1, 3) |
| A local helper (`npx smaltnb serve`) running the user's git | Needs Node and git installed (2) |
| GitHub Codespaces running the helper | Ties smalt to GitHub's platform (3) |
| A github.dev / VS Code extension | A second interface inside another product (3) |
| A desktop app (Tauri, Electron) | Heavy; outside code (3) |
| Requiring GitHub Desktop | An install, and a tie to one tool (2, 3) |
| Handing off to GitHub's web editor | Manual, one file at a time, GitHub-only (3) |

## Consequences

- No credential ever enters smalt: there is nothing to steal, leak, rotate or protect, and decision 19 has nothing to
  cover for git.
- smalt stays independent of every git host; whatever the user syncs with works.
- In the page, notebooks in git need Chrome or Edge on a desktop. Phones and the other browsers get files, not git.
- The cell-aware layer (diffs, history, conflicts by cell) is what smalt adds over git; git itself stays git.
- smaltnb's DESIGN.md decision 16 and its milestone 2 are rewritten to match, in smaltnb.

## Order of work

1. **Read git** (in smaltkit): objects, packs with deltas, refs; checked against `git` in CI.
2. **The page in a repository folder:** open and save notebooks there; which notebooks changed.
3. **Per-cell diff** against `HEAD` and branches, then per-cell history and blame.
4. **Conflicts by cell.**

## The owner's decisions (2026-11-13)

1. **The git layer lives in smaltkit**, so smaltui and smaltbi can use it too. It is not a product of its own (no
   smaltcr for now).
2. **No commits from the page.** Until further notice the user makes every commit, and all work with remote
   repositories, in their own tools. Level 2 (section 4 of the decision) is not built.
3. **No signed commits:** no keys in the browser, of any kind.
4. **Firefox and Safari: downloads.** They open and download files; no history kept in the browser, no patch or bundle
   export.

## Sources

- CORS: requests to `github.com` and `gitlab.com` git endpoints and APIs from this project's tooling, 2026-11-12.
- [GitHub changelog: PKCE support (2025-07-14)](https://github.blog/changelog/2025-07-14-pkce-support-for-oauth-and-github-app-authentication/)
- [caniuse: showDirectoryPicker](https://caniuse.com/mdn-api_window_showdirectorypicker);
  [web-features: File System Access](https://web-platform-dx.github.io/web-features-explorer/features/file-system-access);
  [Chrome: persistent permissions for the File System Access API](https://developer.chrome.com/blog/persistent-permissions-for-the-file-system-access-api)
- [Sveltia CMS](https://github.com/sveltia/sveltia-cms) (local repository mode);
  [Decap CMS backends](https://decapcms.org/docs/backends-overview/);
  [Saving JupyterLite notebooks to GitHub](https://www.zonca.dev/posts/2025-01-29-jupyterlite-save-github.html);
  [Obsidian Git sync on mobile](https://www.stephanmiller.com/obsidian-git-sync-mobile/);
  [TiddlyWiki: saving to a Git service](https://tiddlywiki.com/static/Saving%2520to%2520a%2520Git%2520service.html);
  [Observable Notebook Kit](https://observablehq.com/notebook-kit/);
  [marimo: version control](https://www.mintlify.com/marimo-team/marimo/version-control);
  [marimo Hub: syncing](https://marimohub.docs.marimo.io/syncing)
- [Chromium: Intent to Ship, WebAuthn PRF](https://groups.google.com/a/chromium.org/g/blink-dev/c/iTNOgLwD2bI);
  [Google: device bound session credentials](https://blog.google/security/protecting-cookies-with-device-bound-session-credentials/)
