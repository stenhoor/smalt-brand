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
value-picking controls and TypeScript type stripping, used by smaltui and smaltbi. smaltkit is 0.5.0 and isn't on npm
yet.

[Repository →](https://github.com/stenhoor/smaltkit)

**smaltty** is the TypeScript kit inside it: TypeScript for the apps' TypeScript tabs and notebook cells, in our own
code. It removes types without moving a line or column, so an error points where it was written, and type checking
against smaltdf comes next.

[Repository →](https://github.com/stenhoor/smaltty)
