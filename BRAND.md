# smaltdb

**Small. Alternative. Fast.**

smaltdb is a fast alternative database for the browser, written in TypeScript. This document is its brand: the Grain mark, the Kiln palette, and a Geist-forward type system with a monospaced voice for coders.

## The name

The name carries three meanings at once:

- **sm** — small
- **alt** — alternative
- **db** — database
- **smalt** — the cobalt-glass pigment, `#003399`, ground into powder. Finer grinds read paler; the brand scale (`smalt-900` → `smalt-100`) follows those grades.

In the wordmark, `alt` is set in `primary`. Write the name in lowercase, as one word: **smaltdb**. In prose, "smaltdb" is fine at the start of a sentence; never "SmaltDB" or "Smalt DB".

## Voice

- Plain and specific. Say what the engine does, such as "runs in a Web Worker", "stores data in OPFS", or "commits through a write-ahead log".
- Describe what smaltdb is, never what it isn't. No "no WASM", "unlike X" or "without Y" framing.
- No comparisons with other databases. Let readers draw their own; never name another engine in marketing copy.
- No unsourced performance claims. A number appears only with its benchmark and method linked beside it.
- Written for coders: show code early, keep sentences short.

Tagline: **Small. Alternative. Fast.** Use it under the wordmark, in social cards, and in the docs hero.

## The family voice — smalty

**What "Stay smalty." means.** It is a nod to "salty" and a counterpoint to it. Salty is annoyed; smalty is having fun doing our own thing. It carries the family's irreverent streak: rather than stitching together separate, disconnected tools, smaltworks builds one family of its own, a database, a console, BI, dataframes and notebooks, designed as one unified approach from the start.

Smalt is pronounced like salt (Merriam-Webster: ˈsmȯlt), so the family plays on salt idioms. Each one keeps `alt` visible, so it still reads small + alternative. Set the smalt part like the wordmark where you can: Martian Mono, `alt` in `primary`.

| Use | Words |
| --- | --- |
| Family tagline, across all products | **Stay smalty.** |
| The group that makes the smalt projects | **smaltworks** |
| Social media handle | **smaltalk** (one word) |
| Community members | **smalties** |
| Community statement | **smalt of the earth.** |

- Each product keeps its own "Small. Alternative. ___." tagline. "Stay smalty." is the family's line: social profiles, stickers, community pages, sign-offs.
- "Smalty" is the opposite of salty: upbeat, a little irreverent, confident in doing things our own way. Say what the family builds and how the pieces fit together; never aim it at other projects or at someone who reports a problem. The voice rule against picking fights still applies: the unified approach is described by what it is, not by what others lack.
- "smaltalk" is one letter from Smalltalk, the programming language. That's fine as a nod, but write it as one lowercase word and never imply a connection to Smalltalk.
- A *smalt works* was a historical factory that made the pigment, which gives smaltworks its meaning.

## smaltworks

smaltworks is the group that makes the smalt family. It has its own mark, but no product colour and no product tagline.

| | |
| --- | --- |
| Mark | **Together:** two L-shaped pieces that lock into one frame. Separate tools, built to fit. |
| Colours | First piece smalt (`primary`); second piece kiln orange (`kiln-500`, `#E5622F`; `#FF8A5C` on dark) |
| Wordmark | `sm`**`alt`**`works`: `alt` in smalt, the rest in ink |
| Line under the name | **Small. Alternative. Together.** |
| Family tagline | Stay smalty. (see below) |
| Logos | `logos/smaltworks/` |
| Avatar | `social/smaltworks-avatar.png`, for the GitHub organisation and @smaltalk |
| Endorsement | `badges/a-smaltworks-project.svg`, light and dark: "A smaltworks project", for product footers and READMEs |

- Kiln orange belongs to smaltworks' mark and to the apps' commit and focus accents. It is a fill only, never text (3.4:1 on white).
- The endorsement goes under a product's own brand, never in place of it: a product page leads with its own lockup.

## How smaltworks works with AI

Most developers don't love code for its own sake. They love to create, and code has been how they do it.

We are developers, and we love to create. AI lets us build at scale and test ideas faster and better than we ever could by hand, so smaltworks works AI-first.

We build tools and libraries that help other people create, whether they write every line by hand or work AI-first. We love developers and the work they do, and everything we make is meant to help them make more.

One line, for profiles and footers: **Built AI-first, by developers, for everyone who creates.**

- Say it as a stance, plainly. Lead with what smaltworks does and loves, not with a defence.
- "Faster and better than we ever could by hand" is smaltworks' own experience. Don't turn it into a general claim about hand-written code, or about developers who work that way.
- Both ways of working are welcome: the tools and docs serve people who code by hand and people who work AI-first.

## Logo — the Grain mark

A ground-glass particle and the chip it shed: small, and a little apart.

| Asset | Use |
| --- | --- |
| `logos/smaltdb/grain-mark.svg` | On light grounds. Body `smalt-700`, chip `smalt-300`. |
| `logos/smaltdb/grain-mark-on-dark.svg` | On dark grounds. Body `smalt-200`, chip `smalt-100`. |
| `logos/smaltdb/app-icon.svg` | App and PWA icons, social avatars. |
| `logos/smaltdb/favicon-32.svg`, `favicon-16.svg` | Browser tabs. The 16 px version simplifies the notch away. |
| `logos/smaltdb/lockup.svg`, `lockup-on-dark.svg` | Mark + wordmark, outlined. README headers, docs nav, slides. |
| `logos/smaltdb/wordmark.svg`, `wordmark-on-dark.svg` | Wordmark alone, outlined, `alt` in `primary`. Where the mark already appears nearby. |

The wordmark and lockup SVGs are Martian Mono 600 (width 112.5, the Google Fonts default) converted to paths, so they render identically everywhere with no font loading.

**In a GitHub README** (GitHub strips inline colour styles, so use the image, switched by theme). Copy the two lockup files into the project, here as in smaltdb's `docs/brand/`:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/brand/lockup-on-dark.svg">
  <img alt="smaltdb" src="docs/brand/lockup.svg" width="320">
</picture>
```

Lockup: the mark to the left of the wordmark (style `wordmark`, Martian Mono 600), with the gap equal to half the mark's width and the mark at about 1.6× the wordmark's cap height. Clear space on every side: the chip's width. Don't recolour, rotate, outline or add effects, and don't put the light mark on dark grounds.

## Colour — Kiln

Smalt on neutral graphite, with kiln orange for commits and focus. Every pairing below was checked with the WCAG 2 contrast formula, in both themes.

**Readability rules**

1. `text` ≥ 12:1, `text-2` ≥ 7:1 (AAA), `text-3` ≥ 4.5:1, on both `bg` and `surface`.
2. Every `syn-*` token ≥ 5:1 on `code-bg`, comments included.
3. Dark theme is off-white on graphite (`#E9EBF0` on `#14171F`), never `#FFF` on `#000`.
4. `kiln-500` and `smalt-300` are fills only: they fail text contrast on light grounds.
5. Status is never colour alone: `success`, `warning` and `danger` always come with an icon and a word.
6. `danger` is crimson, not orange, so it is never confused with `accent`.
7. Focus is a 2px `focus` ring with a 2px offset (≥ 7:1 against `bg` in both themes).

Roles: `primary` for the one main action per view; `link` for links (underlined in body copy); `accent` for commit/write emphasis; `border` for hairlines only.

## Type

- **Geist** (`--font-sans`): headings and body. Headings are Geist 700 with tight negative tracking; body is 17px / 1.6, at most 70 characters a line.
- **Martian Mono** (`--font-brand`): the wordmark, eyebrows, breadcrumbs and labels. Short strings only; never paragraphs or code blocks.
- **Geist Mono** (`--font-mono`): all code, 15px / 1.6 in blocks.

All three are Google Fonts (OFL). Load them with:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700&family=Geist+Mono:wght@400;500&family=Martian+Mono:wght@400;600&display=swap" rel="stylesheet">
```

## Iconography — the Chevron style

Icons are drawn the way the smaltui Chevron mark is drawn (`logos/smaltui/chevron-mark.svg`): solid bars and one chip, not outlines.

- **Solid shapes, no strokes.** Every line is a filled bar of constant thickness with square-cut ends. The Chevron's arms are about 15% of the icon's width thick (9.9 units on its 64-unit grid), which is about 3.5 px on a 24 px icon.
- **Angles of 0°, 45° and 90° only**, like the Chevron's arms. The one exception is smaltql's Star mark, whose arms are 60° apart because an asterisk needs six evenly spaced arms. Icons still follow the rule.
- **One chip at most:** a rounded bar with a 3-unit radius on the 64-unit grid (about 1.1 px at 24 px), like the Chevron's cursor `_`. It marks the one detail that matters: the cursor, a dot, the current item.
- **Two tones.** The body is `smalt-700` (`smalt-200` on dark) and the chip takes the layer colour, as in the marks. Status icons are drawn entirely in their status colour (`success`, `warning`, `danger`) and still always come with a word.
- **One drawing at every size**, like the marks: draw on a 24 px grid and keep bars at least 2 px thick at 16 px.

`components/StatusBadge` shows the style: a check, an exclamation mark (a bar and a chip) and a cross.

## Social preview cards

`social/` has a card for each product: `smaltdb.png`, `smaltui.png`, `smaltbi.png`, `smaltdf.png`, `smaltnb.png`, `smaltql.png` and `smaltts.png`, each 1280 × 640, with SVG sources beside them.

- **GitHub:** in the repository, open Settings, then under "Social preview" click Edit and upload the PNG (PNG, JPG or GIF under 1 MB; 1280 × 640 displays best).
- **Websites:** reference the PNG from `og:image` and `twitter:image`, with `twitter:card` set to `summary_large_image`.
- Each card is the product's dark lockup, tagline, positioning line and address, on the dark ground, with a bar in the layer colour. Regenerate them with `scripts/social_cards.py` after any change to a lockup, tagline or positioning line; don't edit the PNGs by hand.

## Tokens

`tokens/tokens.json` is the source of truth. `tokens/tokens.css` is generated from it (`python3 scripts/build_tokens.py`) and exposes every token as a CSS custom property: light theme on `:root`, dark under `prefers-color-scheme: dark` or `data-theme="dark"`, plus a class per type style (`.h1`, `.body`, `.code` and so on).

## Components

`components/` holds `Button`, `StatusBadge`, `CodeBlock` and `Wordmark` as static HTML and CSS references built on `tokens.css`. Open any `preview.html` in a browser; it follows the system's light or dark setting. There is no JavaScript bundle yet.

## Docs theme

`themes/vitepress/` is the VitePress theme every smalt product site uses: the Kiln palette mapped onto VitePress's variables, the type rules, the hero-suffix colour for each layer, and Shiki code themes built from the `syn-*` tokens. It also holds the parts every product site shares: the smaltworks menu and footer (`smaltworks.ts`) and the stage and "A smaltworks project" badges (`stage.ts`). Copy the files unchanged; [`themes/vitepress/README.md`](themes/vitepress/README.md) says how.

## Sites and READMEs

Every product site and README follows the same rules, so the family reads as one. Before changing a product's site, README or description, read this file and [DECISIONS.md](DECISIONS.md): the family table, these rules and the latest decisions. Every repository's CLAUDE.md points here. A product site is the product's own documentation or demo site; smaltworks.dev is the family's.

1. **Header:** the product lockup from `logos/<product>/`, light and dark.
2. **Hero:** the wordmark with its suffix in the layer's text colour (`<span class="suffix language">ql</span>`; smaltdb's suffix has no span). The headline is the tagline, broken after "Small. Alternative." so the product's word always starts the next line (`text: 'Small. Alternative.<br>Fast.'`), and the line under it is the positioning line from [the family table](#the-smalt-family), word for word. Anything more goes in the paragraph under the hero.
3. **Stage badge:** work in progress under the hero and at the top of every page, linked to smaltworks.dev/stability. It becomes Release 1.x when the product reaches 1.0, and not before.
4. **smaltworks menu:** the last item in the top nav, from `smaltworksMenu()`: "The family", then every product as `name · role`, then "Work in progress". The same items, in the same order, on every site.
5. **Footer:** "A smaltworks project", linked to smaltworks.dev, and "MIT License". On pages with a sidebar, where VitePress hides its footer, `stage.ts` puts both at the foot of the page.
6. **Link wording:** a product named in running text links to its own site. Calls to action are "Try the live demo →", "Read the docs →" and "Repository →": every product page on smaltworks.dev ends with those it has, in that order, and nothing else ("Documentation at …" and "See the live sample" are out). On the status page, each row ends with "Demo" and "Docs" links, where they exist. Roles are always the engine, SQL, dataframes, typed API, query workbench, reports and notebooks.
7. **Theme:** `smaltdb.css`, `shiki.ts`, `smaltworks.ts` and `stage.ts` copied from `themes/vitepress/` unchanged. A product's own rules go in a file of its own (smaltbi's `smaltbi.css`), never into the copies.
8. **Install lines:** the [npm names](#npm-names), `@smaltworks/<repository>`. Until a package is published, say so beside the line.
9. **Status:** one stage from Planned, In early development, In development, Preview and Release 1.x. Each repository's status page is the source; smaltworks.dev's status page mirrors it.
10. **README:** the lockup, the stage badge, the tagline and positioning line, then "Documentation" and "smaltworks.dev" links. It ends with the "A smaltworks project" badge.
11. **Page metadata:** site search, and `og:` title, description and image.
12. **Demos and playgrounds:** a **demo** is the app itself: its full interface, on sample data. An app site (smaltui, smaltbi, smaltnb) opens it from one nav item, **Demo**, first in the top nav; the home page embeds no demo, and nothing else on the site opens the app: the hero has one button, **Getting started**, to the guide. A **playground** is a small runner in a docs page: an editor, Run, Reset, Copy and Share, and the result (a grid, a value, a plan or an error), with nothing else of the app's interface (no explorer, tabs, import, settings or saved data). It shows the page's code running: tell and show. Docs pages have playgrounds ([Documentation](#documentation), rule 7); only Demo opens the app. A playground may link to the app ("Open in smaltui"), never embed it. The language sites (smaltql, smaltdf) have no demo yet.
13. **Status on smaltworks.dev:** its status page and product pages keep a one-line detail for each product. A change that alters a product's status or what it does comes with a smalt-brand PR that updates them, linked with `Depends on:`.

smaltui's page is a web app, not VitePress: it follows the same rules in its own HTML, with the family's products as cards in place of the menu.

## Documentation

Every product's documentation follows one standard, for people and for the AI agents that use the products. The
mock-ups are in the [exploration archive](exploration/README.md#documentation-standard) and on the family canvas; the
decisions and what was considered are in [DECISIONS.md](DECISIONS.md#documentation-standard). The components marked
*to build* are not in the site kit yet: until they are, a site follows the rules it can, starting with smaltql.

1. **Four sections:** Quick start, Getting started, User guide and Reference, in that order and with those names. The
   home page opens on the four as cards. The top nav is Quick start, Guide, Reference, Playground, then the smaltworks
   menu (an app site puts Demo first: Sites and READMEs, rule 12). A site leaves a section out only where this table
   does:

   | Site | Quick start | Getting started | User guide | Reference |
   |---|---|---|---|---|
   | smaltdb | yes | yes | Engine concepts | API, the plan language, errors |
   | smaltql, smaltdf | yes | yes | Tasks in the language | The language (statements or methods, functions), its API |
   | smaltts | yes | yes | Specs, changes, flows | API |
   | smaltui, smaltbi, smaltnb | yes | yes | Working in the app | Formats (report, notebook), shortcuts |
   | Plugins | yes | no | Per plugin | Functions, options, API |
   | Kits (smaltkit, smaltty) | yes | no | no | API, module by module |

2. **Quick start:** one page, five minutes, three steps at most, ending in a live playground, so a reader who installs
   nothing still runs something real.
3. **Reference entries:** one shape for every function, method, statement and plan operation: the name; the signature
   with its types; a one-line summary; parameters; what it returns (or its output columns); the errors it raises, with
   their codes; notes; examples with their printed results; a working demo; see also. **One function, method or
   statement per page**, grouped in the sidebar under its kind (String, Math, Aggregate …); a group's page lists its
   members and states the rules they share. Names for the same function (`substr`, `substring`) share a page. A
   language's functions and statements have syntax diagrams, as its grammar does (rule 4).
4. **Syntax diagrams:** every statement and grammar rule of a language has a railroad diagram, drawn from its grammar
   (EBNF, in the W3C notation) by the site kit's generator, our own code (`railroad.ts`): keywords in rounded boxes,
   rules in square boxes that expand in place, long rules wrapped onto rows, and the EBNF beside them. A site keeps its
   grammar in one file, which the diagrams and the agent guide both read. Prose after the diagrams says what they
   can't, such as where an aggregate may appear.
5. **Examples are tests:** every example runs in CI, and its printed result is checked against what it gives.
6. **Working demos:** every language and API reference page ends with a complete small program (its data, its code
   and its result) that runs as written.
7. **Playgrounds:** on every guide and reference page, one component from the site kit (`playground.ts`), built from
   smaltkit (`editor` and `grid`). **Every tested example runs in place:** at rest it is the example, a small Run
   button and its tested result (or the error it is tested to raise), and it loads nothing; Run or Edit turns it into
   a playground where it stands. A fence marked `noplay` doesn't run, nor does an example that needs a plugin the site
   doesn't load; the first Run starts the engine, from the site's own copy and never a CDN, in a
   worker, once per visit. Each Run starts from the page's setup: the tested examples above it, as the examples test
   runs them, in an in-memory database. Run, Edit, Reset, Copy and Share (the code travels in the link's fragment,
   never to a server), and a link to the app where the app can open code from one. What a playground holds, and what it
   leaves to the app, is in Sites and READMEs, rule 12.
8. **The plan format is a language:** smaltdb's reference has a Plan language section, like a language's: syntax
   diagrams of the JSON, an entry for each operation and expression kind, and playgrounds that run plan JSON, with a
   tree view for reading a plan. It opens with "One query, every language": the same query in SQL and in smaltdf, and
   the plan both build. Every SQL and smaltdf playground has a Plan tab (*to build*: smaltql's plan of a statement and
   the plan tree printer). The section is marked experimental, beside the work-in-progress badge, until the plan
   format's stability ADR.
9. **Docs for agents:** every site also publishes Markdown for AI agents, generated from the same sources as its pages
   (the site kit's `agents.ts`, at the end of the build): a Markdown twin of every page (`page.md`), an `/llms.txt`
   index (the [llms.txt proposal](https://llmstxt.org/)), and one agent guide per product (`/agents.md`). An agent guide
   is complete rather than friendly: how to use the product, its rules (a page the site writes for agents), its grammar
   as EBNF text, every signature, tested examples with their results, every error code, and what isn't supported, with
   the alternative (the reference pages it names, in the sidebar's order). Each file names the
   package's version (and the plan format's, where plans appear). The same generator feeds smaltai's context documents
   ([ADR 0025](docs/adr/0025-smaltai-agent-gateways-and-actions.md)).
10. **Voice:** this file's, as everywhere: what it is, short sentences, the stage badge, no number without its
    benchmark.

## The smalt family

smaltdb is the engine. The other products are built on it, and each shares smaltdb's brand: the Kiln neutrals, Geist and Martian Mono, the `sm`**`alt`**`…` wordmark, and marks drawn as a smalt body plus a chip. Each product gets its own mark. Colour comes from the product's layer.

### Colour by layer

Each layer of the stack has one colour, and every product in it takes that colour. The mark tells products in a layer apart; the colour says where a product sits.

| Layer | Products | Colour | Text | Dark |
| --- | --- | --- | --- | --- |
| Engine | smaltdb and its plugins | smalt: the pale chip (`smalt-300`), suffix in ink | ink | `smalt-100` chip |
| Languages | smaltql, smaltdf, smaltts | `layer-language`: cobalt magenta `#B0249F` | `#981C89` | `#F57FE6` |
| Kits | smaltml (smaltkit and the other kits have no brand of their own) | `layer-kit`: jade `#0A7C76` | `#086A65` | `#10C2B9` |
| User tools | smaltui, smaltbi, smaltnb, smaltfl | `layer-tool`: deep cerulean `#0E7FAE` | `#0B6A91` | `#5CBDE8` |
| Alongside | smaltai, which runs alongside the languages, kits and user tools | `layer-ai`: blue-leaning violet `#6E4BC2` | `#6141AE` | `#B8A1F2` |

smaltworks keeps kiln orange: it is the family, not a layer. The `product-*` tokens remain as aliases of their layer's token, so existing uses keep working.

| | smaltdb | smaltql | smaltdf | smaltts | smaltui | smaltbi | smaltnb |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Layer | Engine | Languages | Languages | Languages | User tools | User tools | User tools |
| What it is | The engine | The SQL | The dataframes | The typed API | The query workbench | The reports | The notebooks |
| Tagline | Small. Alternative. Fast. | Small. Alternative. Familiar. | Small. Alternative. Frames. | Small. Alternative. Typed. | Small. Alternative. Query. | Small. Alternative. Insight. | Small. Alternative. Notebooks. |
| Positioning | A fast alternative database for the browser, written in TypeScript. | The SQL you know, for smaltdb. | Dataframes for smaltdb. Small and fast. | smaltdb, straight from TypeScript. | A query workbench for smaltdb that runs entirely in the browser. | Business intelligence in the browser, powered by smaltdb. | Reactive notebooks for smaltdb. |
| Mark | Grain | Star (`*`) | Axes | Generic (`<T>`) | Chevron (`>` and `_`) | Scatter | Pencil |
| Logos | `logos/smaltdb/` | `logos/smaltql/` | `logos/smaltdf/` | `logos/smaltts/` | `logos/smaltui/` | `logos/smaltbi/` | `logos/smaltnb/` |

smaltml, smaltai and smaltfl are in progress: their layers and colours are set, their marks and words are not.

Rules:

- `alt` is always smalt (`primary`), in every product's wordmark. The suffix takes the layer's text colour; smaltdb's stays ink.
- The mark body is always smalt; only the chip takes the layer colour. That keeps the products reading as one family.
- Inside a layer, products share a colour, so the mark and the suffix letters tell them apart. Keep marks distinct within a layer.
- smaltbi's 16 px mark is a simplified three-grain version; every other mark is the same drawing at every size.
- Layer colours are for a product's own mark, wordmark and accents, not for status or links.
- Jade (the kit layer) is the nearest layer colour to the `success` green (CIELAB distance 27). Never use it to mean success, and keep status icons and words on every status.
- Violet (smaltai) sits close to smalt (CIELAB distance 21 light, 18 dark). It marks smaltai, which runs alongside the layers and doesn't touch the engine, not a layer that sits on the engine.
- smaltts's Generic mark uses two 45° angles, like smaltui's Chevron. Keep the two apart in toolbars and lists, where they could be mistaken for each other at small sizes.
- If a product moves to another layer, its colour moves with it.

### smaltts

smaltts is a thin, typed TypeScript API over smaltdb's plan and schema operations, with structured flows, for applications and layers that want neither SQL nor dataframes. It sits at the language layer, beside smaltql and smaltdf. Its name says what it is: plain, typed TypeScript. Say it smalt-T-S.

### smaltdb and smaltql

SQL moves out of the smaltdb repository into smaltql ([smaltdb ADR 0015](https://github.com/stenhoor/smaltdb/blob/main/docs/adr/0015-smaltql.md)). smaltql and smaltdf are peers: two languages on one engine. smaltdb has no language built in: each language exports its own `open()`, so installing smaltql gives a SQL database and installing smaltdf gives dataframes. smaltdb's tagline and positioning line stay as they are.

smaltql's promise is in its words: familiar SQL always works. It can grow its own syntax, but only by adding to SQL, never by changing what working SQL means.

## npm names

Packages publish to npm under the smaltworks organisation, named after their repositories: `@smaltworks/smaltdb`, `@smaltworks/smaltql`, `@smaltworks/smaltdf`, `@smaltworks/smaltdb-parquet` and so on. The repository name is the package name, so there is one name to remember for each project. smaltdb 0.8.3, the last release under the unscoped name `smaltdb`, stays on npm.

Ready-made distributions (the engine alone, or the engine with particular languages) are planned but not yet named.

## Before 1.0: work in progress

Until 1.0, the family speaks as a work in progress and an invitation: **"Work in progress. Come build with us."** The first half says where things are; the second asks people in. The hype at this stage is for people who enjoy new things and will work through rough patches, not for anyone building a business on it.

- **The badge:** one, twice the height of the others: **Work in progress** above **Come build with us**, led by a pull-request sign, the contributor's branch in kiln orange arrowing into the smalt main line (`badges/work-in-progress.svg`, `-on-dark`; the sign alone is in `badges/signs/`). Put it at the top of every README, release and preview page, linked to `https://smaltworks.dev/stability`. Signs are signage, not product marks: they may use strokes and rings, which the marks don't.
- **Say who it's for:** people who like trying new things, don't mind breaking changes, and want a say in how it turns out. **Not yet for** production or data you can't recreate.
- **Every release's notes start with Breaking,** even when it says "None" (`templates/release-notes.md`).
- **Install lines pin exact versions** (`npm install --save-exact`).
- **The call to action is "try it, break it, tell us",** not "use it" or "star it".
- **Don't say** production-ready, stable, or enterprise, and don't lead with benchmark numbers. "Fast" stays in smaltdb's tagline as a goal.
- **Not "salty",** in any form: the family's line is "Stay smalty".

## From 1.0: Release 1.x

When a product reaches 1.0, its badge becomes **Release 1.x** above **Come build with us**, led by a release-commit sign: a release node on the smalt main line, which runs on, with the same kiln pull request still coming in (`badges/release-1x.svg`, `-on-dark`; the sign alone is in `badges/signs/`). The invitation stays: 1.0 is stable, not finished.

- **Only from 1.0.** Before 1.0 a product shows the work-in-progress badge, whatever its state. Nothing below 1.0 uses the release badge.
- **The major version, not the exact one.** "Release 1.x" changes only when a breaking release ships, so a README badge never goes stale. At 2.0 it becomes "Release 2.x".
- **Product pages show their stage** under the title, with `<StageBadge />` (work in progress) or `<StageBadge stage="release" />`. Switch one product at a time, as it reaches 1.0.

## "Powered by" badges

`badges/` has a badge for each product, light and dark: 172 × 28 px, with all text converted to paths. Sites and projects that use a smalt product show the matching badge and link it to the project. `badges/README.md` has the HTML and Markdown snippets.

- Wording is always "Powered by", for every product.
- Badge colours match the lockups: `alt` in smalt, the suffix in the layer colour.
- Every text colour on the badge is at least 6:1 against its surface in both themes.

## Plugins

A plugin gets a product brand of its own only when people choose it and use it directly, as with smaltdf (`@smaltworks/smaltdf`). Infrastructure plugins (`@smaltworks/smaltdb-parquet`, `@smaltworks/smaltdb-io`, `@smaltworks/smaltdb-external`) use smaltdb's brand and a plain name, such as "smaltdb Parquet", with no mark or colour of their own.

Three badges, in `badges/plugins/`, say how a plugin relates to smaltdb:

| Tier | Meaning | Badge |
| --- | --- | --- |
| **Official** | Made and maintained by smaltworks, in the `@smaltworks` npm scope | The product's mark, the wordmark, "official plugin" |
| **Verified** | Made by someone else; passes the smaltworks compatibility tests for a stated plugin API version | A check, "Verified for", the wordmark, an "API v1" tag |
| **Works with** | The author says it works; smaltworks hasn't checked | "Works with" and the wordmark in grey, with a dashed border and no mark |

- Product marks appear only on what smaltworks makes. Brand colours appear only on what smaltworks makes or has tested.
- Official and Verified badges link to the plugin's entry on smaltdb.dev/plugins, the list smaltworks controls. A badge image alone proves nothing, since anyone can copy it.
- Verified means the compatibility tests pass for that API version. It is not a security review, and the list page says so.
- The `@smaltworks` npm scope and names that start with `smalt` are reserved for smaltworks. Third-party plugins are named `<product>-plugin-<name>`, for example `smaltdb-plugin-geo`.

## smaltkit

smaltkit is shared UI code inside the smalt apps, not a product people choose, so it has no mark, product colour or badge. Its README header is the name in the wordmark style (`sm`**`alt`**`kit`, ink and smalt) with the line "Shared UI code for the smalt apps. Part of smaltworks."

Its brand job is to carry the brand into the apps: its components should take their colours, type and icons from `tokens/`. Revisit this if smaltkit gains charts that users see (the brand has no chart palette yet), or if outside developers start building on it.

smaltty, the TypeScript kit, is the same: no mark, colour or badge of its own (DECISIONS.md, "smaltty").
