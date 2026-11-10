# How the brand was chosen

A record of the brand work for smaltdb, in order, so later changes can see what was already tried and why.

## Inputs

- **The pigment.** Smalt is cobalt-coloured potash glass ground into powder, `#003399` (sRGB 0, 51, 153). Finer grinds read paler, which became the tonal scale (`smalt-900` → `smalt-100`).
- **The name.** smaltdb also reads as **sm**all **alt**ernate **d**ata**b**ase.
- **The product.** An embedded SQL database for the browser: OPFS storage, Web Worker execution, WAL-durable commits. Speed is treated as a feature. The audience is coders.

## Round 1: three complete directions

| Direction | Idea | Outcome |
| --- | --- | --- |
| A · Ground Glass | Faceted shard mark, serif display, light-first | The pigment idea carried forward; the serif did not. |
| B · Fast Path | Slanted-bar motion mark, Geist, dark-first, cyan accent | Geist carried forward. |
| C · Pane | Page-grid mark, mono wordmark, orange accent | Mono wordmark and orange accent carried forward. |

Feedback: complete directions made it hard to see the options. Round 2 split them into separate categories to mix and match.

## Round 2: alternatives by category

Six marks (Alt key, ⌥ glyph, alternate route, grain, small cube, wordmark only), four palettes, four type pairings, three icon styles and six taglines.

Feedback that shaped round 3:

- Don't pick fights with other databases. Dropped "without the WASM" and anything defined against another engine.
- Liked Ground Glass, Alt key and Alternate route.
- Liked Geist 700 and Martian Mono; monospace suits the coder audience.
- Refine the colours, with a focus on readability.

## Round 3: refined, and the picks

| Category | Options | **Picked** |
| --- | --- | --- |
| Tagline | T1–T5 | **T3: "Small. Alternate. Fast."**, later changed to "Small. Alternative. Fast." (see below) |
| Mark | Ground Glass, Grain, Alt key, Alternate route | **Grain:** a ground-glass particle and the chip it shed |
| Type | S1 mono-forward, S2 Geist-forward | **S2:** Geist 700 headings, Martian Mono for wordmark and labels, Geist Mono for code |
| Palette | P1 Ground Glass, P2 Hot Path, P3 Kiln | **P3 Kiln:** smalt on neutral graphite, kiln orange for commits and focus |

### Readability rules applied to every palette

1. Body text ≥ 12:1, secondary ≥ 7:1 (AAA), tertiary ≥ 4.5:1, on both ground and surface.
2. Every syntax colour ≥ 5:1 on its code background, comments included.
3. Dark mode is off-white on graphite, never `#FFF` on `#000`.
4. Colours that fail text contrast (`kiln-500`, `smalt-300`) are fills only.
5. Status is never colour alone: icon plus word.
6. `danger` is crimson, kept apart from the orange accent. It was orange-red until the check caught that the two were too close.
7. A 2px focus ring, ≥ 3:1 against the ground.

All ratios were computed with the WCAG 2 relative-luminance formula and are recorded in each token's `usage` note.

## After the picks

- **Positioning line:** "A fast alternative database for the browser, written in TypeScript." It was first "pure JavaScript", but the source is TypeScript and "pure JavaScript" undersold the first-class types. "No WASM" was rejected as framing against other engines.
- **"Alternate" became "Alternative".** The tagline is now "Small. Alternative. Fast." and *alt* in the name reads as *alternative*. smaltdb is proposed as an alternative database; "alternative" is the word that audience uses, and it matches the positioning line.
- **Voice rule added:** describe what smaltdb is, never what it isn't.
- **Outlined wordmark:** GitHub strips inline styles from Markdown, so the coloured `alt` can only appear in a README as an image. The wordmark and lockup are Martian Mono 600 converted to paths (now `scripts/brand_assets.py`), switched for light and dark with `<picture>`.
- **Cover simplified:** an early design-system cover scattered grain-sized squares to suggest powder. It read as noise and was replaced by the oversized mark alone.
- **Docs site:** smaltdb.dev uses the VitePress theme in `themes/vitepress/`, with the wordmark in the hero.

## The family: smaltui and smaltbi

Two products built on smaltdb needed brands of their own that still read as part of one family.

- **smaltui** is a query workbench for smaltdb, served as a static site: object explorer, tabbed SQL editors, editable data grids, import tools.
- **smaltbi** is a report designer and viewer: model data, drag fields onto a canvas, publish reports as static sites.

Shared from the start: the Kiln neutrals, Geist and Martian Mono, the `sm`**`alt`**`…` wordmark, and marks built as a smalt body plus a chip. The products could differ in mark shape and, optionally, chip colour. Product colours were drawn from smalt's sibling cobalt pigments: cerulean blue (cobalt stannate), cobalt green, cobalt violet and aureolin (cobalt yellow). Source: [CAMEO, Museum of Fine Arts Boston](https://cameo.mfa.org/wiki/Cobalt_pigments).

### Family round 1

- Taglines: four per product.
- Marks: three per product.
  - smaltui: Tabs, Caret, Panes.
  - smaltbi: Bars, Slice, Trend.
- Colour: three options.
  - A1: all smalt.
  - A2: cerulean and cobalt violet.
  - A3: cobalt green and aureolin. The aureolin chip is 1.7:1 on white.
- Badges: three styles (Pill, Flat, Inline) with four verbs.

Feedback:

- Taglines: "Small. Alternative. ___" for both products. smaltbi: "Small. Alternative. Insight." smaltui: not "Workbench".
- smaltbi positioning: "Business intelligence in the browser, powered by smaltdb."
- smaltui: the terminal feel of the Caret mark was liked, but it didn't fit the idea.
- smaltbi: Trend was liked because it looks unlike other BI tools, but it wasn't there yet.
- Colour: the cobalt blues were close.
- Badges: Pill and Inline were the best. Use "Powered by" as the verb.

### Family round 2

- smaltui words: five tagline words (Console, Terminal, Interface, Query, Studio) and three positioning lines.
- smaltui terminal marks: Prompt, Last line, Chevron, Grain cursor.
- smaltbi trend marks: Breakout, Area, Scatter, Steps.
- Cobalt blues in three tunings: C1 as before, C2 deeper, C4 teal and violet. A brighter variant was dropped at 2.96:1 on white.
- "Powered by" in four pill variants (P1–P4) and four inline variants (I1–I4).

Viewed full-size, Prompt and Chevron read instantly as "terminal" but sit close to the generic terminal icon. Breakout and Scatter break into specks at 16 px. The stacked badge variants' label was about 7 px at real size, too small to read.

### Family round 3: the picks

| | **Picked** |
| --- | --- |
| smaltui tagline | **"Small. Alternative. Query."** |
| smaltui positioning | **"A SQL console for smaltdb that runs entirely in the browser."** |
| smaltui mark | **Chevron:** the prompt, `>` and `_`, as a grain and a chip |
| smaltbi tagline | **"Small. Alternative. Insight."** |
| smaltbi positioning | **"Business intelligence in the browser, powered by smaltdb."** |
| smaltbi mark | **Scatter:** grains along a rising line, the latest point as the chip |
| Colour | **C2 Deeper:** smaltui `#0E7FAE`, smaltbi `#6E4BC2`; text shades `#0B6A91` and `#6141AE` (light), `#5CBDE8` and `#B8A1F2` (dark) |
| Badge | **P1 Pill**, "Powered by", 172 × 28 px |

Applied after the picks:

- smaltbi's 16 px mark uses three larger grains instead of five, so it holds at favicon and badge size.
- Badge colours match the lockups: the suffix takes the product colour (confirmed).
- Badge text contrast on its surface: at least 6.0:1 in light and 7.4:1 in dark.

## After the family: the icon style

Round 2 offered three icon styles for UI icons (I1 Outline, I2 Duotone, I3 Pixel grain), and none was picked, so components kept the I1 outline icons as a placeholder.

**Picked: the Chevron style** (owner's decision). Icons are drawn like the smaltui Chevron mark: solid bars of constant thickness with square-cut ends, angles of 0°, 45° and 90°, and at most one rounded chip in the product or status colour. The rules are in `BRAND.md` under Iconography, and `StatusBadge` was redrawn in this style.

## After the family: the social preview card

One card per product, 1280 × 640 (GitHub's recommended size, 2:1), in `social/`. Built from decisions already made, so no options round:

- The dark Kiln ground (`#14171F`), so the card reads as one piece in both light and dark feeds.
- The product's dark lockup, its tagline (Geist 700), its positioning line (Geist 400, `text-2`) and its address (Martian Mono, `text-3`).
- A 12 px bar along the bottom in the product colour: smalt for smaltdb, `product-ui` for smaltui, `product-bi` for smaltbi.
- Content sits on a 96 px left margin and away from the top and bottom edges, so the 1.91:1 crop used by some sites cuts nothing.

## smaltdf

smaltdf is a dataframe plugin for smaltdb, with its own product brand in the family. Narwhals is the reference for its API; the brand doesn't name it.

The options were shown on the family canvas, in two rounds for the mark and several for the positioning line:

- **Tagline:** Frames, Transform, Columns, Shape.
- **Marks, round 1:** Columns, Brackets, Filter, Tusk. None was picked.
- **Marks, round 2,** built around frames because of the tagline: Frame, Axes, Join, Stack.
- **Colour:** every remaining cobalt pigment lands near a status colour. Measured by CIELAB distance from every colour in use:
  - cobalt teal: distance 38 from smaltui's cerulean, but judged too close by eye;
  - aureolin ochre: distance 15 from `warning`;
  - cobalt green: distance 15 from `success`; cobalt rose: 12 from `danger`;
  - olive and magenta were added as better-separated alternatives;
  - smalt only, with no new colour.
- **Positioning:** the first lines were too long or leaned on TypeScript or Narwhals. The owner set the direction: go back to smaltdb's core principles (small, fast) and end with "for smaltdb".

| | **Picked** |
| --- | --- |
| Tagline | **"Small. Alternative. Frames."** |
| Positioning | **"Dataframes for smaltdb. Small and fast."** |
| Mark | **Axes:** the header row and index column that make a table a dataframe, with one value as the chip |
| Colour | **Aureolin ochre:** `#8C6D00` fill, `#7A5F00` text (light), `#E6C24A` (dark) |

Applied after the picks:

- The ochre's closeness to `warning` is handled by the existing rules: status always carries an icon and a word, and product colours are never used for status.
- The names smaltdb and smaltdf differ by one letter, so the `df` always keeps its product colour.
- The badge text is at least 6.1:1 on its light surface and 9.6:1 on its dark one.

## smaltnb

smaltnb is a notebook for smaltdb, in the spirit of Jupyter and, more closely, marimo, scripted in TypeScript. A notebook mixes TypeScript, smaltdb SQL and smaltdf dataframe cells, with charts from the smalt kits (smaltkit has no charting yet).

The options were shown on the family canvas:

- **Taglines:** Notebooks, Explore, Reactive, Run.
- **Positioning:** "Notebooks for smaltdb. Small and fast.", "TypeScript notebooks for smaltdb.", "Reactive notebooks for smaltdb."
- **Colour:** cobalt magenta, leaf green, smalt only. With the blues, the violet and the ochre taken, these were the hues furthest from every product and status colour. Cobalt teal was ruled out (too close to smaltui), as was terracotta (CIELAB distance 24 from the kiln accent).
- **Marks:** three rounds.
  - Round 1, cells: Cells, Cell and output, Reactive, Page. None was picked.
  - Round 2, objects: Open book, Spiral, Tab, Chart cell, Run, Cursor cell. Spiral came closest.
  - Round 3, pencil to paper (the owner's direction): Writing, Pencil point, Page and pencil, Spiral and pencil, Pad.

| | **Picked** |
| --- | --- |
| Tagline | **"Small. Alternative. Notebooks."** |
| Positioning | **"Reactive notebooks for smaltdb."** (changed 2026-11-07, below; first pick "TypeScript notebooks for smaltdb.") |
| Mark | **Pencil:** a 45° pencil, its point in the product colour |
| Colour | **Cobalt magenta:** `#B0249F` fill, `#981C89` text (light), `#F57FE6` (dark) |

Applied after the picks:

- The Pencil is the same drawing at every size; at 16 px its magenta point is about two pixels (owner's decision).
- A 45° pencil resembles the common "edit" icon. The smalt body and magenta point set it apart, but avoid placing it beside edit buttons in a toolbar.
- The magenta is at least CIELAB distance 33 from the smaltbi violet in light and 34 in dark. The badge text is at least 7.3:1 on its light surface and 7.1:1 on its dark one.
- Positioning changed to **"Reactive notebooks for smaltdb."** (owner, 2026-11-07). A notebook holds SQL (smaltql) and dataframe (smaltdf) cells as well as TypeScript, so "TypeScript notebooks" undersold it; what sets it apart is that cells rerun when what they read changes. smaltnb's DESIGN.md decision 1 uses the same line everywhere.

## smaltql

SQL moves out of smaltdb into its own product, smaltql. smaltdb's work since ADR 0014 put a shared plan layer under the engine, with SQL and smaltdf as two languages on it; splitting SQL out gives the engine one job (execution performance) and lets the query language grow its own identity. The first draft had smaltdb ship with smaltql by default; the accepted ADR changed that. smaltdb has no language built in, and each language exports a ready `open()`: `import { open } from '@smaltworks/smaltql'` gives a SQL database. The technical record is [smaltdb ADR 0015](https://github.com/stenhoor/smaltdb/blob/main/docs/adr/0015-smaltql.md).

Considered and dropped along the way:

- **SQL as a language inside smaltdb's brand, with no colour of its own.** The owner chose full peers: smaltql and smaltdf each get a product brand.
- **A DAX-compatible language.** Dropped (the owner isn't a fan of the language). Microsoft holds an active patent, US9275031B2 "Data analysis expressions", which would also have needed legal review.

The options were shown on the family canvas:

- **Taglines:** Select, Familiar, Ask, Declare. "Query" was out: it is smaltui's tagline word.
- **Positioning:** "SQL for smaltdb. Small and fast.", "The SQL you know, for smaltdb." (the superset promise), "SQL for smaltdb, with a smalty flavour."
- **Colour:** leaf green, jade, smalt only. Green is the only open part of the wheel, and the `success` colour is green, so both coloured options sit nearer a status colour than earlier picks. A pure green (reads as "success") and vermilion (CIELAB distance 22 from kiln) were dropped.
- **Marks:** three rounds.
  - Round 1: Rows, Semicolon, Q, Star, Clauses, Question. Two overlapping squares (a join) were left out because they read as the smaltworks Together mark. The owner liked Star, but it didn't read as `*`: its arms were spaced at 90° and 45°.
  - Round 2: four stars with the arms joined (six arms at 60°, or eight at 0/45/90°), the chip below or in the centre. Not picked: the owner's direction was Round 1's layout, separate arms with the chip in the centre.
  - Round 3: separate arms around a centre chip, spaced evenly. Six arms at 60° in three weights, and eight arms at 0/45/90°. Long, slim arms were needed; short ones read as a sun.

| | **Picked** |
| --- | --- |
| Tagline | **"Small. Alternative. Familiar."** |
| Positioning | **"The SQL you know, for smaltdb."** |
| Mark | **Star (T2):** six separate arms 60° apart around the chip, the `*` of `SELECT *` |
| Colour | **Leaf green:** `#527A10` fill, `#456810` text (light), `#9ACD4A` (dark) |

Applied after the picks:

- The Star is the family's one exception to the 0/45/90° angle rule; icons still follow it.
- Leaf green is CIELAB distance 28 from `success` in light and 38 in dark. It is never used to mean success. Fill 5.1:1 on white, text 6.0:1 on `bg`, dark 9.6:1 on `bg`.
- The Star is the same drawing at every size; at 16 px the chip is about three pixels.
- **npm names (owner's decision):** packages publish under the smaltworks npm organisation, named after their repositories: `@smaltworks/smaltdb`, `@smaltworks/smaltql`, `@smaltworks/smaltdf`, `@smaltworks/smaltdb-parquet` and so on. This replaces the `@smaltdb` scope for plugins; nothing had been published under it.

## smaltts

smaltts (`stenhoor/smaltts`) is a thin, typed TypeScript API over smaltdb's plan and schema operations, adding structured flows for applications and layers that want neither SQL nor dataframes. Under smaltdb ADR 0015 the engine has no language built in, so without smaltts such an application works with the raw plan API. Two readings were shown: a way into the engine beside smaltql and smaltdf, or a layer the languages build on. The owner placed it at the language layer, beside smaltql and smaltdf.

The options were shown on the family canvas:

- **Taglines:** Typed, Direct, Structured, Code.
- **Positioning:** "A typed TypeScript API for smaltdb.", "smaltdb, straight from TypeScript.", "Typed flows for smaltdb. Small and direct."
- **Colour:** jade, smalt only, graphite. With smaltql's leaf green taken, jade was the one hue left with room. Vermilion (CIELAB distance 23 from kiln, 24 from danger) and every other green (within 21 of leaf green) were dropped.
- **Marks:** Generic (`<T>`), Object (`{ }`), Flow, Direct, T.

| | **Picked** |
| --- | --- |
| Tagline | **"Small. Alternative. Typed."** |
| Positioning | **"smaltdb, straight from TypeScript."** |
| Mark | **Generic:** the `<T>` of a TypeScript generic, two 45° angles with the type as the chip |
| Colour | **Graphite:** `#4A5163` fill, `#3F4656` text (light, the same as `text-2`), `#B9BEC9` (dark) |

Applied after the picks:

- Graphite is the family's first neutral product colour. It never means disabled or secondary.
- The graphite chip has less contrast against the smalt body than the other chips, most visibly on the app icon and at 16 px; the mark carries smaltts by its shape.
- The Generic mark's angles echo smaltui's Chevron. Keep them apart in toolbars and lists.
- The smaltts repository is private, so the social card and badge point to smaltworks.dev/products/smaltts.
- The smaltworks social card's product list no longer fit with seven products; it now shows smaltworks.dev, and `scripts/social_cards.py` checks that every address fits.

## Before 1.0: work in progress

For the first public release (a new engine, smaltdf, smaltql as its own language, and smaltui and smaltbi on the new engine), the owner set the aim of the hype: reach people who are excited by new things and willing to work through rough patches, without over-promising, and without anyone building a business on it and being caught out by next week's breaking change.

The preview line went through two rounds. "Fresh from the works. Expect salt." was rejected: the family says no to salty ("Stay smalty" is its counterpoint). The second round offered Wet paint, Still in the kiln, Unfired, First grind, On the workbench, Open studio, Work in progress, in public, and Come build with us. Picked, as a pair: **"Work in progress. Come build with us."**, one saying where things are, the other opening an invitation.

Signs for the two phrases (owner's idea: a cone or warning tape for work in progress, a hard hat for come build with us):

- **Work in progress:** the cone, warning tape and barrier were drawn; the barrier read best.
- **Come build with us:** three rounds of hard hats didn't read convincingly as a hard hat and were dropped; a crane, bricks, a wrench and a block-drawn merge weren't chosen either. The owner then suggested a GitHub-style branch and merge: drawn in Git's own idiom (thin lines, ring nodes, curved branches), the pull request read at once.
- **Picked: one badge, twice the height,** with the pull-request sign at double size, its kiln branch arrowing into the smalt line, and **Work in progress** above **Come build with us**. The barrier is not used.

Applied: the badge, the pull-request sign in `badges/signs/`, the stability page on smaltworks.dev (who it's for and not yet for, what can change, how you'll hear, what to do), the release-notes template with Breaking first, and the rules in BRAND.md.

## Colour by layer

With smaltql's leaf green and smaltts's graphite taken, and smaltml, smaltai and smaltfl on the way, the colour wheel had run out: every hue left sat near a status colour or another product. The owner proposed colouring by layer of the stack instead of by product, and placed the products: smaltfl is a user tool beside smaltui, smaltbi and smaltnb; smaltml sits at the kit level, between the languages and the user tools; smaltai runs alongside the languages, kits and user tools, plugging into each.

The board (FAM-Layers) showed the whole family both ways, light and dark. Picked:

| Layer | Products | Colour |
| --- | --- | --- |
| Engine | smaltdb and its plugins | smalt |
| Languages | smaltql, smaltdf, smaltts | cobalt magenta `#B0249F` |
| Kits | smaltml | jade `#0A7C76` |
| User tools | smaltui, smaltbi, smaltnb, smaltfl | deep cerulean `#0E7FAE` |
| Alongside | smaltai | blue-leaning violet `#6E4BC2` |

- **Every layer colour was already in use and checked** against the status colours; the three that sat near one (ochre, leaf green) or read as disabled (graphite) retire.
- **Violet went to smaltai, not the languages.** It is CIELAB distance 21 from smalt (18 in dark), too close for the layer that sits on the engine; smaltai doesn't touch the engine layer. Every other pair of layer colours is at least 33 apart.
- **This replaces the product colours picked earlier:** smaltbi violet → cerulean; smaltdf ochre, smaltql leaf green and smaltts graphite → magenta; smaltnb magenta → cerulean. Their marks, words and the rounds that chose them stand; only the colour follows the layer now.
- **Jade's reservation for smaltfl lapses:** smaltfl is a user tool, so it takes cerulean, and jade becomes the kit layer's colour.
- **`product-*` tokens stay,** as aliases of their layer's token, so existing uses keep working. New tokens: `layer-language`, `layer-kit`, `layer-tool`, `layer-ai`, each with a `-text` variant.
- **smaltai** went through an outline treatment (not chosen: the owner didn't like it), a first round of marks, and a round about plugging in; its marks are still open. **smaltml** has a first round of words and marks, also open.

## The family voice: smalty

Smalt rhymes with salt (Merriam-Webster: ˈsmȯlt), so salt idioms were explored as a family-wide voice, on one board:

- **Family lines:** Be smalty, Stay smalty, Take it with a grain of smalt, A pinch of smalt.
- **Names:** smalt talk, smaltworks, smalties.
- **Small copy:** Worth your smalt, smalt of the earth, Rub a little smalt in it.

The board flagged that "salty" commonly means annoyed or bitter (Dictionary.com), and recommended "Take it with a grain of smalt" as the family line, since it ties to the Grain mark.

| | **Picked** |
| --- | --- |
| Family tagline | **"Stay smalty."** |
| Group name | **smaltworks:** the group that makes the smalt projects |
| Social media handle | **smaltalk** |
| Community members | **smalties** |
| Community statement | **"smalt of the earth."** |

Applied after the picks:

- **Intent (owner):** "Stay smalty." is both a nod to "salty" and a counterpoint to it: the fun, somewhat irreverent view of doing our own thing. The smalt projects rebuild much of the infrastructure that today comes as separate, disconnected offerings, as one unified family.
- Because "salty" commonly means annoyed or bitter, `BRAND.md` frames smalty as its opposite and keeps the no-fights rule: describe the unified approach by what it is, never by what others lack.
- "smaltalk" is one letter from Smalltalk, the programming language. Old archives already use "SMALTALK" as an 8-character name for Smalltalk, so coders may read it that way.
- Whether the smaltworks and smaltalk names are free on GitHub and the social networks wasn't checked: this session can't look up accounts outside the smalt repositories.

## Plugins and smaltkit

Reasoned through in conversation, then mocked up on one board.

- **smaltkit gets no brand:** it is shared code inside the apps, not a product people choose. It gets only a README header in the wordmark style.
- **Product brands for plugins:** only when people use the plugin directly (smaltdf); infrastructure plugins use smaltdb's brand.
- **Three tiers:**
  - **Official:** from smaltworks, in the `@smaltdb` scope.
  - **Verified:** smaltworks-approved, after passing compatibility tests.
  - **Works with:** self-attested by the author.
- **On the words:**
  - "Compatible" was proposed for the approved tier; "Verified" was chosen because readers can't tell "Compatible" from "Works with".
  - "Reviewed" and "Certified" were ruled out because they imply a security or formal review.
- **Badges:** Official carries the product's own mark, so an official smaltnb plugin would show the Pencil, not the Grain. Verified swaps the mark for a check and adds the API version. Works with has no mark, no brand colour and a dashed border.
- **Proof:** Official and Verified badges link to a list on smaltdb.dev/plugins that smaltworks controls.

All approved by the owner. Still to build before Verified can be granted: the compatibility test suite and the smaltdb.dev/plugins page.

## Outside code: ask first, and plugins carry it

Decided by the owner on 2026-11-08, after a session added third-party tools (Prettier, then sucrase) to an app without
asking, and then took them out again without discussing it.

- **Ask before adding outside code.** A session asks the owner, and waits for a yes, before it adds a package (a
  dependency of any kind, or a pin in `packed.json`), copies or bundles in someone else's code, or loads code from
  another site at run time (a CDN such as jsDelivr). It says what the code is, its licence and size, what it's for, and
  why our own code can't do it. Every repository's `CLAUDE.md` carries the rule, word for word, under "Working rules for
  sessions".
- **Plugins carry outside code.** Outside code that a feature needs goes in a plugin, so it is named and optional and
  its licence travels with it, never in core. This extends smaltdb ADR 0012 from the engine to the whole family. The
  first cases:
  - **Formatting:** JSON and TypeScript formatting is our own code (`smaltkit/pretty`), not Prettier.
  - **Compiling TypeScript at run time:** a plugin, `@smaltworks/smaltdb-sucrase`, replaces loading the TypeScript
    compiler from jsDelivr in smaltui's TypeScript tabs. (Later the same day, our own code replaced it: see "smaltty:
    TypeScript without outside code".)
  - **Parquet codecs:** the Parquet plugin owns `hyparquet-compressors` as its own dependency, instead of each app
    installing it.

## smaltty: TypeScript without outside code

Decided by the owner on 2026-11-08, in an interview with a session that proposed it.

- **Why:** smaltui stripped TypeScript types with sucrase, and smaltnb loaded the TypeScript compiler (8.7 MB) to run
  notebook cells. Both brought outside code into the apps, and neither checked types, so code written against smaltdf
  lost its type checking just before it ran.
- **What:** [smaltty](https://github.com/stenhoor/smaltty), our own TypeScript kit: a parser, a stripper, and later
  scope analysis and type checking against smaltdf. In order: remove the outside code first, measure, and only then
  decide how far checking goes.
- **A kit, not a product.** smaltty is one of the kits, with no brand entry, mark or site of its own. It becomes a
  top-level product only if it grows into our own TypeScript compiler, or a significant part of one, and that is the
  owner's call. smaltworks isn't in the business of writing TypeScript compilers: work that doesn't remove outside code
  or make the apps faster waits.
- **TypeScript only:** no Rust and no WebAssembly. **Follow TypeScript, not sucrase:** where they differ, TypeScript's
  behaviour is right. Types are removed, never compiled (TypeScript's `erasableSyntaxOnly`).
- **smaltkit wraps it:** apps import `smaltkit/typescript`; smaltkit carries smaltty in its build.
- **Retired:** `@smaltworks/smaltdb-sucrase`, once smaltui moved to smaltty (stenhoor/smaltui#33). Its repository stays
  for reference.
- **Later:** checking table and column names against a database is a separate future project, smaltsc (smalt schema
  checker), not part of smaltty.

## How smaltworks works with AI

The owner set out the stance: developers love to create, and code has been how they do it. smaltworks is AI-first because AI lets it create at scale and iterate faster and better than by hand. It builds tools for everyone who creates, whether they code by hand or work AI-first.

Edited for publication, with these changes:

- **Removed:** "not because we have anything against developers". The voice rule says to describe what something is, not what it isn't, so "We are developers" now leads.
- **Scoped:** "faster and better than by hand" is stated as smaltworks' own experience, not as a general claim.
- **Added:** a one-line form, "Built AI-first, by developers, for everyone who creates."

Approved by the owner. The full text is in `BRAND.md`.

## smaltworks

The parent brand took four rounds of marks.

- **Round 1, the works:** Sawtooth, Grain works, Mortar, Family, Kiln grain. None was picked.
- **Round 2, the owner's directions:** a miner's helmet with a lamp (salt mining) and a 3D salt crystal. Two helmets and four crystals; none was picked.
- **Round 3, starting from the words used to describe smaltworks:** Maker's mark, Heap, Out of line, Alt key, Tilt, Hand and spark, Together, Spark. Picked: **Together**.
- **Round 4, colour and words for Together:**
  - colour: kiln orange, pale smalt, or the product colour by context;
  - words: four lines from round 1.

| | **Picked** |
| --- | --- |
| Mark | **Together:** two L-shaped pieces that lock into one frame |
| Second piece | **Kiln orange:** `kiln-500` `#E5622F`, `#FF8A5C` on dark |
| Line under the name | **"Small. Alternative. Together."** |

Applied after the picks:

- The wordmark keeps `alt` in smalt and the rest in ink, like smaltdb.
- An avatar PNG (square; GitHub and social sites round it) and an "A smaltworks project" endorsement badge were added.
- **Correction:** `tokens.json` listed `smalt-300` (`#7B97D4`) as 3.1:1 on white. It is 2.9:1 (2.7:1 on `bg`), under the 3:1 guide for graphics. The token note is fixed. The colour is the chip in smaltdb's Grain mark, where it is decorative and logos are exempt.

## The smaltworks.dev website

The central site for smaltworks and its projects, at smaltworks.dev, built from this repository so the brand and the
site can't drift apart.

- **Where:** `site/` in smalt-brand, not a separate repository (owner's decision). It can move later; the domain just
  points wherever the site lives.
- **Tool:** VitePress with the family theme, the same as smaltdb.dev.
- **Pages:**
  - the family, each product with links out, plugins and kits;
  - the architecture, why smalty, how smaltworks works with AI, status;
  - get involved, core team, code of conduct, open source, the brand kit.
- **Architecture graphic:** four layouts were mocked up (layer cake, engine bar, fan, stacked plates). **Engine bar**
  was picked, for the home page and the architecture page.
- **Small data:** "Small data deserves good tools." It is stated as what we believe, with no row counts, and the
  "make it … again" phrasing is ruled out.
- **Inspired by, not against:** the tools that shaped the products are credited by name (Toad, Power BI, Tableau,
  Jupyter, marimo, Narwhals, pandas, Polars), with a plain statement that the family isn't here to replace them.
- **Core team:** Steve TenHoor, organizing founder. His day job and personal contact details are left out; people
  get in touch through GitHub.

## From 1.0: the release badge

The counterpart of the work-in-progress badge, for a product once it reaches 1.0.

- **Sign: R2 Release commit.** The smalt main line runs on past a release node (a ring round a dot), and the same kiln
  pull request still comes in. Picked over a filled node, a merged sign and a Gitflow in-and-out sign, and over four
  rounds of tags, which the owner didn't like. Git tools rarely draw a tag: they label a commit and mark special
  commits with a different node, which is what R2 does.
- **Top line: "Release 1.x".** It names the major version, so it changes only when a breaking release ships, and it
  says "stable" without the word. "Release 1.0" was rejected because a README badge would go stale at 1.0.1.
- **"Come build with us" stays.** The invitation doesn't end at 1.0.
- **Every product page shows its stage.** Product pages on smaltworks.dev show the work-in-progress badge now and
  switch to the release badge one by one, as each product reaches 1.0. That needs a 1.0 milestone for each product.

## Sites and READMEs

One standard for every product site and README (BRAND.md, "Sites and READMEs"), after a review found each repository
had made its own choices. The shared parts (menu, footer, badges, suffix colours) are in `themes/vitepress/`.

The owner's decisions, 2026-11-07:

- **smaltui: "A query workbench for smaltdb that runs entirely in the browser."** It was "A SQL console…"; dataframes
  are coming to smaltui, so "SQL" undersold it. Its role in menus is "query workbench", and the app is the workbench
  everywhere (it was console in some places, workbench in others). "Query console" was considered; "workbench" was
  picked so the line and the app's name agree.
- **Demos: one nav item, no embedded demos.** smaltui, smaltbi and smaltnb each open their app on sample data from a
  **Demo** nav item, first in the nav. The live demos embedded in smaltui's and smaltbi's home pages go. Before this,
  each site did it differently (embedded and "Workbench"; embedded and "Demo"; "Open a notebook" only). The hero
  keeps one button, Getting started, on every app site: the Demo nav item is the only way into the app (the first pass
  left "Open the workbench", "Open the designer", "View the published sample" and "Open a notebook" in the heroes).
- **No demo on the language sites yet.** smaltql and smaltdf stay documentation only.
- **smaltworks.dev keeps its one-line status details,** kept current by the sessions that change the products: a
  change to a product's status or what it does comes with a smalt-brand PR. Showing only the stage, with a link, was
  considered.
- **Brand first.** Every repository's CLAUDE.md points sessions to BRAND.md and this file before they change a site,
  README or description. Sessions had copied an old line back onto a site after the owner changed it.

## Documentation standard

One standard for every product's documentation (BRAND.md, "Documentation"), from a review of three projects whose docs
the owner admires: Polars for its function entries with sample code, NumPy for its structure, SQLite for its syntax
diagrams. Ten boards were mocked up (docs round 1, in the [exploration archive](exploration/README.md#documentation-standard)).

The owner's decisions, 2026-11-10:

- **Four sections on every site:** Quick start (zero to working), Getting started, User guide, Reference.
- **Every reference entry the same shape,** with examples tested against their printed results, and a **working
  demo** on every language and API page: a complete small program a reader sees run, then changes. **Playgrounds on
  every page,** built from smaltkit.
- **Syntax diagrams from our own generator.** Mermaid has railroad diagrams (beta since v11.16), but it is outside
  code; a small generator of our own draws them in the brand's colours, and the mock-ups use it.
- **Demos and playgrounds** (Sites and READMEs, rule 12, rewritten). In the owner's words: demos are full app
  environments, the full interface; playgrounds have a stripped-down interface, fully functional, to show code actually
  running (tell and show). Playgrounds are in the documentation; apps are in Demo. Keeping playgrounds off the app
  sites, and dropping the rule's "nothing else opens the app", were considered.
- **The standard in BRAND.md, the components in the site kit** (`themes/vitepress/`). A DOCS.md of its own, and the
  components in smaltkit, were considered.
- **smaltql first:** it already has a quick start, a guide and tested examples.
- **The plan format documented as a language** (the owner's lean): the neutral way into the engine gets syntax
  diagrams, an entry per operation and expression, and plan playgrounds, opened by "One query, every language" (SQL,
  smaltdf and the plan they build). Documenting only the TypeScript builders, and only the side-by-side view, were
  considered. It needs smaltql to give the plan of a statement, which it doesn't export yet, and a printer for whole
  plans; the format stays marked experimental until its stability ADR.
- **Docs for agents** (Jake Rastberger's input): beside the people docs, Markdown made for the AI agents that use the
  languages and tools: a twin of every page, an `/llms.txt` index, and one agent guide per product, generated from the
  same tested sources.

Building the playground (stenhoor/smalt-brand#64), the owner agreed, 2026-11-10:

- **smaltkit in the docs sites.** A site with playgrounds pins smaltkit to a commit (`github:stenhoor/smaltkit#…`), as
  smaltui and smaltbi do: playgrounds are built from it, and it is our own code.
- **"Open in the app" waits for the app.** The link shows only where the site can give one that opens the code; smaltui
  can't open code from a link yet, and teaching it to is a task of its own.

## Work items: one register

Decided by the owner on 2026-11-09, when smaltdb ADR 0022 (SQL for the new engine features) needed tracking and review
with other work, and smalt-brand had no place for it.

- **[WORK.md](WORK.md)** lists cross-repository work that is proposed, waiting for decisions or under way: one row per
  item, with its record's link, status, next step and what it waits on. A multi-step item can list its milestones
  below the table.
- **Records stay home.** An ADR or plan lives in its own repository; WORK.md links it and never copies its text, so
  there is one copy to review. Copying the ADR into smalt-brand, and a tracking issue, were considered.
- **Sessions keep it current.** A session that opens, advances or finishes such work updates its row in a smalt-brand
  PR, as product sessions already do for the status page.

## Exploration archive

[`exploration/`](exploration/) keeps every board from every round (77 by the documentation standard's round): a rendered snapshot (PNG) for viewing, and its source (`.dc.html`, the Claude design-canvas format) for reference. Its README lists each board in the order it was shown, with what was picked from it.

## Still open

- **Saying smaltql:** smalt-Q-L (letter by letter, like smalt-D-B) or smalt-quel.
- **smaltai and smaltml:** marks and words are open; their colours are set by layer.
- **smaltql distributions:** the engine alone, the engine with smaltdf, and the engine with both languages. The idea is agreed; names and packaging are not.

- **Research pages on smaltdb.dev** include benchmark comparisons with other engines. The no-comparisons rule covers marketing copy; whether those pages stay on the public site is undecided.
