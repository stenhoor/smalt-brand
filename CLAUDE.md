# CLAUDE.md

smalt-brand is the source of the smalt family's brand: the voice, logos, colours, tokens, badges, the docs theme and the
shared site kit, and smaltworks.dev (`site/`). Every other smalt repository copies from here and its CLAUDE.md points
here. Several Claude Code sessions work on the smalt repos in parallel and cannot see each other: this file is the shared
starting point for this repository, and its working rules match smaltdb's `CLAUDE.md`.

## Read first

- [BRAND.md](BRAND.md): the rules, the family table (taglines, positioning lines, marks, colours by layer) and "Sites
  and READMEs", the standard every product site and README follows.
- [DECISIONS.md](DECISIONS.md): what the owner decided, when and why, including lines that changed after their first
  pick. A newer decision there wins over an older copy anywhere else.

## Rules for this repository

- **Record decisions.** A change to a line, a mark, a colour or a rule goes into DECISIONS.md with its date and reason,
  and BRAND.md shows the result. Keep earlier picks noted; don't rewrite history in `exploration/`.
- **Generated files are generated.** Badges (`scripts/badges.py`), social cards (`scripts/social_cards.py`) and logos
  (`scripts/brand_assets.py`) come from their scripts; change the script, then regenerate. Commit only the files whose
  content changed (a PNG can differ by rasteriser bytes alone).
- **The site kit is copied verbatim.** `themes/vitepress/` (`smaltdb.css`, `shiki.ts`, `smaltworks.ts`, `stage.ts`) is
  copied unchanged into every product site, by hand or by a sync script (smaltbi, smaltui). A change here reaches a site
  only when that repository copies it again: say in the PR which repositories need to.
- **smaltworks.dev follows the products.** Its status page and product pages keep a one-line detail per product; product
  sessions send the PR that updates them. `npm run build` in `site/` fails on dead links.
- Merging to `main` redeploys smaltworks.dev (`.github/workflows/site.yml`).

## Working rules for sessions

- One task per branch and PR. Do not add unrelated work to an open PR: it holds up everything else in it.
- Mark unfinished work clearly. This repository has no CI on pull requests, so build `site/` before opening one.
- Read review comments on your PR and answer them with commits that say what they address.
- When a PR depends on another repo's PR, add a line such as `Depends on: stenhoor/smaltdb#12`.
- Issues: follow smaltdb's `CLAUDE.md` ("Issues").
- **Ask before adding outside code.** Ask the owner, and wait for a yes, before adding a package (a dependency of any
  kind, or a pin in `packed.json`), copying or bundling in someone else's code, or loading code from another site at run
  time (a CDN such as jsDelivr). Say what it is, its licence and size, what it's for, and why our own code can't do it.
  Outside code that a feature needs goes in a plugin, so it is named and optional, never in core.
