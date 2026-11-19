# <Mark product="lp" :size="40" /> smaltlp

<StageBadge />

**Small. Alternative. Optimal.** Linear and integer programming for smaltdb, in the browser.

smaltlp, said "smalt-L-P", finds the best plan within your costs and limits: how much to make, what to ship where,
which choices to take. It is a [kit](/products/kits), in TypeScript: notebooks in [smaltnb](/products/smaltnb) and apps
call it directly, in the browser or in Node.

- **Two ways in, one solver.** Build a model by name in PuLP 4.2's style, or solve from matrices with scipy's
  `linprog()` and `milp()`, their parameters and status codes kept.
- **Linear and integer programs.** A sparse, bounded dual simplex with presolve, and branch-and-bound for whole-number
  and yes-or-no decisions, with the duals that say what each limit is worth.
- **Model files.** Reads MPS, free and fixed, so models move in from other solvers.
- **Checked against HiGHS.** Every case is compared with scipy, PuLP and HiGHS, and kept as tests that run without
  Python; its speed beside HiGHS is published and rerun with every solver change.

**Status:** in development. Linear programs, integer programs and the modelling layer work; cuts, LP files and
WebGPU come later.

[Read the docs →](https://stenhoor.github.io/smaltlp/) · [Repository →](https://github.com/stenhoor/smaltlp)
