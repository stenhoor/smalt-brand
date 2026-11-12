# Kits

<StageBadge />

The apps aren't built from scratch each time. They're built from **kits**: small, focused libraries that each do one
thing.

- **Few options, on purpose.** A kit offers a narrow set of choices. That keeps every app consistent, and it makes the
  kits easy for AI agents to use well. With fewer options, even a smaller agent produces repeatable results.
- **One look.** Kits draw their colours and type from the smalt brand tokens, so smaltui, smaltbi and smaltnb look
  like one family.

Today the kits live in **smaltkit**: the engine loader, URL rewriting, number and date formatting, SVG chart helpers and
charts, tables, a virtualized grid, SQL text tools, a code editor, a DOM toolkit, the environment manifest's data steps,
value-picking controls and TypeScript (smaltty, below), used by smaltui, smaltbi and smaltnb. smaltkit is 0.5.0 and isn't on npm
yet.

[Repository →](https://github.com/stenhoor/smaltkit)

**[smaltty](/products/smaltty)**, the TypeScript kit, is a product of its own, in the family's kiln: TypeScript for the
apps' tabs and notebook cells, in our own code. smaltkit wraps it as `smaltkit/typescript`, which is how the apps use
it. It removes types without moving a line or column, so an error points where it was written, and checks calls into
smaltdf and smaltts as the code is typed, marking TypeScript's errors as warnings while the code still runs.

[Read the docs →](https://stenhoor.github.io/smaltty/) · [Repository →](https://github.com/stenhoor/smaltty)
