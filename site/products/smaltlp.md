# <Mark product="lp" :size="40" /> smaltlp

<StageBadge />

**Small. Alternative. Optimal.** Linear and integer programming for smaltdb, in the browser.

smaltlp, said "smalt-L-P", solves models of costs, limits and choices to their best answer, in TypeScript, in the
browser. It is a [kit](/products/kits), like [smaltml](/products/smaltml).

- **Two ways in, one solver.** `linprog()` and `milp()` take scipy's parameters over matrices; a typed model builder
  names variables and constraints in PuLP's style; and models read from MPS files.
- **Linear and integer programs.** A bounded dual simplex over a sparse factorisation, after a presolve; integer and
  binary variables by branch-and-bound over the same simplex.
- **Answers you can use.** Each solve gives the values, the objective and the duals: what one more unit of a limit is
  worth.
- **Checked against references.** Results are compared with scipy's linprog (HiGHS), PuLP and HiGHS's MPS reader, and
  kept as tests.

**Status:** in early development. Linear programs and the modelling layer are done; integer programs solve by
branch-and-bound with warm starts. Cuts, LP files and WebGPU come later.

[Read the docs →](https://stenhoor.github.io/smaltlp/) · [Playground →](https://stenhoor.github.io/smaltlp/playground) · [Repository →](https://github.com/stenhoor/smaltlp)
