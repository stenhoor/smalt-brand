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
- **Two tones.** The body is `smalt-700` (`smalt-200` on dark) and the chip takes the product colour, as in the marks. Status icons are drawn entirely in their status colour (`success`, `warning`, `danger`) and still always come with a word.
- **One drawing at every size**, like the marks: draw on a 24 px grid and keep bars at least 2 px thick at 16 px.

`components/StatusBadge` shows the style: a check, an exclamation mark (a bar and a chip) and a cross.

## Social preview cards

`social/` has a card for each product: `smaltdb.png`, `smaltui.png`, `smaltbi.png`, `smaltdf.png`, `smaltnb.png`, `smaltql.png` and `smaltts.png`, each 1280 × 640, with SVG sources beside them.

- **GitHub:** in the repository, open Settings, then under "Social preview" click Edit and upload the PNG (PNG, JPG or GIF under 1 MB; 1280 × 640 displays best).
- **Websites:** reference the PNG from `og:image` and `twitter:image`, with `twitter:card` set to `summary_large_image`.
- Each card is the product's dark lockup, tagline, positioning line and address, on the dark ground, with a bar in the product colour. Regenerate them with `scripts/social_cards.py` after any change to a lockup, tagline or positioning line; don't edit the PNGs by hand.

## Tokens

`tokens/tokens.json` is the source of truth. `tokens/tokens.css` is generated from it (`python3 scripts/build_tokens.py`) and exposes every token as a CSS custom property: light theme on `:root`, dark under `prefers-color-scheme: dark` or `data-theme="dark"`, plus a class per type style (`.h1`, `.body`, `.code` and so on).

## Components

`components/` holds `Button`, `StatusBadge`, `CodeBlock` and `Wordmark` as static HTML and CSS references built on `tokens.css`. Open any `preview.html` in a browser; it follows the system's light or dark setting. There is no JavaScript bundle yet.

## Docs theme

`themes/vitepress/` is the VitePress theme used by smaltdb.dev: the Kiln palette mapped onto VitePress's variables, the type rules, and Shiki code themes built from the `syn-*` tokens.

## The smalt family

smaltdb is the engine. Six products are built on it, and each shares smaltdb's brand: the Kiln neutrals, Geist and Martian Mono, the `sm`**`alt`**`…` wordmark, and marks drawn as a smalt body plus a chip. Each product gets its own mark and one product colour (smalt's sibling cobalt pigments).

| | smaltdb | smaltui | smaltbi | smaltdf | smaltnb | smaltql | smaltts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| What it is | The engine | The SQL console | The reports | The dataframes | The notebooks | The SQL | The typed API |
| Tagline | Small. Alternative. Fast. | Small. Alternative. Query. | Small. Alternative. Insight. | Small. Alternative. Frames. | Small. Alternative. Notebooks. | Small. Alternative. Familiar. | Small. Alternative. Typed. |
| Positioning | A fast alternative database for the browser, written in TypeScript. | A SQL console for smaltdb that runs entirely in the browser. | Business intelligence in the browser, powered by smaltdb. | Dataframes for smaltdb. Small and fast. | TypeScript notebooks for smaltdb. | The SQL you know, for smaltdb. | smaltdb, straight from TypeScript. |
| Mark | Grain | Chevron (`>` and `_`) | Scatter | Axes | Pencil | Star (`*`) | Generic (`<T>`) |
| Product colour | smalt `#003399` | `product-ui`: deep cerulean `#0E7FAE` | `product-bi`: blue-leaning violet `#6E4BC2` | `product-df`: aureolin ochre `#8C6D00` | `product-nb`: cobalt magenta `#B0249F` | `product-ql`: leaf green `#527A10` | `product-ts`: graphite `#4A5163` |
| Suffix colour | ink | `product-ui-text` `#0B6A91` / `#5CBDE8` dark | `product-bi-text` `#6141AE` / `#B8A1F2` dark | `product-df-text` `#7A5F00` / `#E6C24A` dark | `product-nb-text` `#981C89` / `#F57FE6` dark | `product-ql-text` `#456810` / `#9ACD4A` dark | `product-ts-text` `#3F4656` / `#B9BEC9` dark |
| Logos | `logos/smaltdb/` | `logos/smaltui/` | `logos/smaltbi/` | `logos/smaltdf/` | `logos/smaltnb/` | `logos/smaltql/` | `logos/smaltts/` |

Rules:

- `alt` is always smalt (`primary`), in every product's wordmark. The suffix (`db`, `ui`, `bi`, `df`, `nb`, `ql`, `ts`) takes the product's text colour; smaltdb's stays ink.
- The mark body is always smalt; only the chip takes the product colour. That keeps the products reading as one family.
- smaltbi's 16 px mark is a simplified three-grain version; every other mark is the same drawing at every size.
- Product colours are for the product's own mark, wordmark and accents, not for status or links. This matters most for smaltdf: its ochre sits close to the `warning` amber.
- smaltql's leaf green is the nearest product colour to the `success` green (a CIELAB distance of 28 in light mode). Never use it to mean success, and keep status icons and words on every status.
- smaltts's graphite is a neutral, the same grey as `text-2`. As a product colour it marks smaltts only: never use `product-ts` to show something disabled or secondary. Its chip has less contrast against the smalt body than the other products' chips, so the Generic mark relies on its shape.
- smaltts's Generic mark uses two 45° angles, like smaltui's Chevron. Keep the two apart in toolbars and lists, where they could be mistaken for each other at small sizes.
- smaltdb and smaltdf differ by one letter. Keep the `df` in its product colour wherever the wordmark appears, since the colour does most of the work of telling them apart at small sizes.

### smaltts

smaltts is a thin, typed TypeScript API over smaltdb's plan and schema operations, with structured flows, for applications and layers that want neither SQL nor dataframes. It sits at the language layer, beside smaltql and smaltdf. Its name says what it is: plain, typed TypeScript. Say it smalt-T-S.

### smaltdb and smaltql

SQL moves out of the smaltdb repository into smaltql ([smaltdb ADR 0015](https://github.com/stenhoor/smaltdb/blob/main/docs/adr/0015-smaltql.md)). smaltql and smaltdf are peers: two languages on one engine. smaltdb still ships with smaltql by default, so "smaltdb" keeps meaning the database people install and query with SQL, and its tagline and positioning line stay as they are.

smaltql's promise is in its words: familiar SQL always works. It can grow its own syntax, but only by adding to SQL, never by changing what working SQL means.

## npm names

Packages publish to npm under the smaltworks organisation, named after their repositories: `@smaltworks/smaltdb`, `@smaltworks/smaltql`, `@smaltworks/smaltdf`, `@smaltworks/smaltdb-parquet` and so on. The repository name is the package name, so there is one name to remember for each project. smaltdb 0.8.3, the last release under the unscoped name `smaltdb`, stays on npm.

Ready-made distributions (the engine alone, or the engine with particular languages) are planned but not yet named.

## "Powered by" badges

`badges/` has a badge for each product, light and dark: 172 × 28 px, with all text converted to paths. Sites and projects that use a smalt product show the matching badge and link it to the project. `badges/README.md` has the HTML and Markdown snippets.

- Wording is always "Powered by", for every product.
- Badge colours match the lockups: `alt` in smalt, the suffix in the product colour.
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
