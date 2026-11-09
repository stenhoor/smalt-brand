# ADR 0024: smaltml's scope and architecture

- **Status:** proposed. The owner's answers of 2026-11-09 are recorded below; the items under "Still to decide" are
  open.
- **Date:** 2026-11-09
- **Builds on:** smaltdb [ADR 0002](https://smaltdb.dev/adr/0002-second-round-decisions) (supported browsers),
  [ADR 0012](https://smaltdb.dev/adr/0012-plugins) (plugins), [ADR 0014](https://smaltdb.dev/adr/0014-shared-plan-layer)
  (shared plan layer), [ADR 0015](https://smaltdb.dev/adr/0015-smaltql) (packages and languages); smalt-brand's
  [DECISIONS.md](../../DECISIONS.md) (colour by layer; outside code: ask first).

## Context

smaltml is machine learning for the smalt family: a TypeScript library that trains and runs models on smaltdb data, for
people analysing datasets in smaltnb notebooks and smaltui's TypeScript tabs. The owner's direction (2026-11-09):

- **Native TypeScript and WebGPU.** No runtime dependencies, no WebAssembly builds of other libraries, no code loaded
  from another site.
- **scikit-learn, XGBoost, PyTorch and TensorFlow are references.** They show which models matter, what the parameters
  are called and what results to expect. They are not code to copy.
- **The kinds of machine learning need sorting** into what smaltml covers, what it leaves out, and in which order.

What is already set:

- **Brand:** smaltml is in the Kits layer, coloured jade (`layer-kit`, smalt-brand DECISIONS.md, "Colour by layer").
  Its marks and words are open; a first round is on the family canvas.
- **Browsers:** the family's minimums are on [smaltworks.dev/environments](https://smaltworks.dev/environments). WebGPU
  is newer than all of them: per [Can I use](https://caniuse.com/webgpu) (6 November 2026) it fully works for about 87%
  of users, almost all of them on Chrome and Edge 113 or later. Firefox has it on Windows only, and Safari's support is
  partial.
- **WebGPU computes in 32-bit floats.** WGSL has no `f64` and no `i64` (smaltdb's
  [vectorization review](https://github.com/stenhoor/smaltdb/blob/main/docs/research/vectorization-review.md)). That
  review rejected WebGPU for exact SQL arithmetic and named "vector/ML functions over data kept resident on the GPU" as
  the niche where it fits.
- **Where user code runs today:** smaltnb runs notebook code in a kernel worker. smaltui runs TypeScript tabs on the
  page's main thread (`AsyncFunction` in `app/main.ts`), so a long fit there would freeze the workbench unless smaltml
  moves it off that thread.

## Decision

### 1. Scope: classic machine learning on tables

The owner chose classic supervised learning, gradient-boosted trees, and unsupervised learning with data preparation.
Neural networks are out. Within those, smaltml covers:

| Category | What it holds | Reference | Phase |
|---|---|---|---|
| Data preparation | Scaling (standard, min–max, robust), encoding (one-hot, ordinal), imputing missing values, train/test split, pipelines, per-column transforms | scikit-learn `preprocessing`, `impute`, `compose`, `pipeline` | 1 |
| Linear models | Linear regression, ridge, lasso, elastic net, logistic regression | scikit-learn `linear_model` | 1 |
| Metrics and model selection | Regression and classification metrics (MSE, MAE, R², accuracy, precision, recall, F1, ROC AUC, log loss, confusion matrix), k-fold and stratified folds, cross-validation, grid search | scikit-learn `metrics`, `model_selection` | 1 |
| Trees and forests | Decision trees (CART) for classification and regression, random forests, extra trees, feature importance | scikit-learn `tree`, `ensemble` | 2 |
| Gradient-boosted trees | Histogram-based boosting with XGBoost's semantics: its objectives, missing values sent down a learned default branch, base score, early stopping, feature importance | XGBoost | 3 |
| More supervised models | k-nearest neighbours, naive Bayes (Gaussian, multinomial), linear support vector machines | scikit-learn `neighbors`, `naive_bayes`, `svm` | 4 |
| Clustering | k-means, DBSCAN, agglomerative clustering, Gaussian mixtures | scikit-learn `cluster`, `mixture` | 4 |
| Dimension reduction | PCA, truncated SVD | scikit-learn `decomposition` | 4 |
| Anomaly detection | Isolation forest, local outlier factor | scikit-learn `ensemble`, `neighbors` | 5 |

**Left out (owner, 2026-11-09):** neural networks and deep learning, including tensors and automatic differentiation;
text and embeddings (tokenizing, TF-IDF, vector search); recommenders (matrix factorization, collaborative filtering).

**Not decided yet:** time series forecasting and importing models trained elsewhere beyond XGBoost's format (such as
ONNX). Each gets its own decision when it is reached. Anything not in the table needs a new ADR.

PyTorch and TensorFlow are references for what smaltml leaves out as much as for what it covers. They also inform the
WebGPU work: how they lay out work on a GPU and keep data there between steps.

### 2. References: behaviour, not code

smaltml matches its references' behaviour and writes its own code (owner, 2026-11-09):

- **Same models, same parameters, same defaults.** A parameter keeps scikit-learn's or XGBoost's meaning and default,
  in camelCase (`maxIter`, `nEstimators`, `randomState` becomes `seed`). Where smaltml differs, the reference docs say so.
- **Our own code, from their documentation and the published papers.** No code is copied or translated from
  scikit-learn (BSD-3-Clause), PyTorch (BSD-style), TensorFlow (Apache-2.0) or XGBoost (Apache-2.0), so smaltml carries
  no other project's notices.

### 3. Hardware: CPU everywhere, WebGPU where it helps

- **Every model runs on the CPU** in every browser the family supports, and in Node. smaltml adds no browser
  requirement of its own.
- **WebGPU speeds up the heavy parts where the browser has it:** matrix products for the linear models, distance
  computations for k-means, k-nearest neighbours and DBSCAN, and histogram building for gradient-boosted trees. Data that
  several steps use stays on the GPU between them.
- **The CPU computes in 64-bit floats, the GPU in 32-bit.** A GPU result must agree with the CPU result within a stated
  tolerance per model, and the tests check it. Where 32-bit error matters (solving the normal equations, for example),
  that step stays on the CPU.
- **Choosing:** `device: 'auto'` (the default) uses the GPU when one is present and the data is large enough to gain;
  `'cpu'` and `'gpu'` force one.

### 4. Placement: a library over the engine

smaltml is a library in the Kits layer. It is not a smaltdb plugin and not a language (owner, 2026-11-09):

- **Data in:** a smaltdf frame, a smaltdb query result read as columns, or plain typed arrays. smaltml holds data as a
  column-major `Float64Array` matrix, the shape the engine's columnar results already have.
- **Results out:** predictions and transformed columns as typed arrays, which smaltdf or SQL write back as tables.
- **The engine is not changed.** Scoring rows inside a query (a `predict()` function in SQL or smaltdf) would be a
  smaltdb plugin; it can be proposed later.

### 5. API: scikit-style estimators, asynchronous calls over a synchronous core

```ts
import { StandardScaler } from '@smaltworks/smaltml/preprocessing';
import { LogisticRegression } from '@smaltworks/smaltml/linear';
import { pipeline } from '@smaltworks/smaltml/pipeline';
import { accuracy } from '@smaltworks/smaltml/metrics';

const model = pipeline(new StandardScaler(), new LogisticRegression({ maxIter: 200 }));
await model.fit(XTrain, yTrain);
const yPred = await model.predict(XTest);
accuracy(yTest, yPred);
```

(A sketch of the shape; names are settled in the reference as each phase is built.)

- **Estimators** have `fit`, `predict`, `predictProba`, `transform` and `fitTransform`, with scikit-learn's meanings.
- **Calls are asynchronous** (`await model.fit(…)`), because WebGPU results come back asynchronously and long fits must
  not block a page (owner, 2026-11-09).
- **The core is synchronous** and has no DOM or Node dependencies, so it runs anywhere: in a worker, in Node, in tests.
- **A worker of its own for callers on a page's main thread:** `@smaltworks/smaltml/worker` runs fits and predictions in
  a worker and hands back the same estimator API. smaltnb's kernel already runs off the main thread; smaltui's
  TypeScript tabs need it.
- **Randomness is seeded:** the same `seed` gives the same result on the CPU. Results on the GPU can differ in the last
  bits.
- **Missing values are `NaN`.** Models that can't take them reject them with an error that names the column; the
  imputers fill them; gradient-boosted trees route them as XGBoost does.

### 6. Models are saved as JSON, and boosted trees also in XGBoost's format

- **smaltml's own format:** each fitted model, pipelines included, saves to a versioned JSON document. It can be kept as
  a row in a smaltdb table or as a file, and loads back into the same model. A later smaltml release still loads an older
  document.
- **XGBoost's format for gradient-boosted trees:** smaltml reads and writes XGBoost's saved-model format, the JSON
  documents and the binary UBJSON ones (XGBoost's default since 2.1), so models move between smaltml and Python. XGBoost
  guarantees backward compatibility for these files
  ([saving models](https://xgboost.readthedocs.io/en/stable/tutorials/saving_model.html)).

The owner asked for XGBoost's format if it adds no significant overhead or limits, and otherwise for a converter. The
cost is small because smaltml's boosted trees follow XGBoost's rules (section 1): the trees, base score and objective
map field for field. The limits:

- **It covers boosted trees only.** XGBoost's format has no place for scikit-learn's models, so they use smaltml's own
  format. scikit-learn itself has no portable model format (pickle is neither portable nor safe to load).
- **Only what smaltml implements loads.** A file with an objective, booster (DART, linear) or categorical encoding that
  smaltml doesn't support is refused with an error that names it. It is not loaded partly.
- **XGBoost no longer publishes a schema for the format** (removed in 3.2, the format itself unchanged), so the compare
  tests (section 7) are what hold smaltml to it.

If these limits turn out to constrain the boosted trees themselves, the format moves out of the model code into a
converter, as the owner asked.

### 7. Verification: compared with Python once, then kept as tests

- **First, compare tests.** Each case runs through smaltml and through scikit-learn or XGBoost in Python on the same
  data. The results must agree within the case's stated tolerance. This follows smaltdf's Polars comparison tests.
- **Then the results become the tests** (owner, 2026-11-09). The Python results are written to fixtures in the
  repository, and CI checks smaltml against the fixtures without Python. `npm run compare` reruns Python to add cases or
  check a new reference version; `UPDATE=1` rewrites the fixtures.
- **Cases that depend on randomness** pass the starting point in, such as the first centres for k-means. Python's
  random numbers and smaltml's differ by design.
- **GPU results** are checked against the CPU results (section 3).
- **Outside code:** the compare step uses Python with scikit-learn (BSD-3-Clause), XGBoost (Apache-2.0) and NumPy
  (BSD-3-Clause), pinned in `compare/requirements.txt`. They are for development only and never part of the package.
  Pinning them is adding outside code, so the owner approves the list before the first compare PR.

### 8. Performance: a goal to meet or beat Python's native throughput

**The goal** (owner, 2026-11-09): on the CPU, without the GPU, smaltml trains and predicts at least as fast as
scikit-learn and XGBoost running natively in Python on the same machine. It is a goal, not a release gate: smaltml aims
for it and reports where it stands, and a model that is behind still ships.

- **Measured like for like:** the same data, the same parameters and the same machine, with Python's libraries on the
  CPU. A benchmark states how many threads each side used.
- **Each phase adds benchmarks** for its models (fit and predict, for a few data sizes), kept in `bench/` with their
  results, as smaltdb keeps `bench/results/`. Release notes say which models meet the goal and which are behind, and by
  how much.
- **Where it is hardest:** scikit-learn's linear algebra runs on BLAS, which uses SIMD instructions and every core, and
  XGBoost spreads its work across every core. Plain TypeScript on one thread has neither. Matching them means using
  several workers at once (through `SharedArrayBuffer`, which needs a cross-origin isolated page) and choosing
  algorithms that suit JavaScript. If a model can't get there in TypeScript, the options (for example, smaltml's own
  WebAssembly SIMD kernels) come back to the owner as a decision; they are not taken by default.
- **No performance claim without its benchmark.** As the brand requires, a published number links to the benchmark and
  method behind it.

### 9. Package and repository

- **One package, `@smaltworks/smaltml`, with an entry point per area** (owner, 2026-11-09): `/preprocessing`, `/linear`,
  `/metrics`, `/selection`, `/pipeline`, `/tree`, `/ensemble`, `/boost`, `/neighbors`, `/bayes`, `/svm`, `/cluster`,
  `/decomposition`, `/anomaly`, `/io` (saving, loading and XGBoost's format) and `/worker`. An app loads only what it
  imports. The name follows ADR 0015: `@smaltworks/<repository name>`.
- **No runtime dependencies.** smaltdb and smaltdf are optional peers, used only by the helpers that read their data.
- **The repository, `stenhoor/smaltml`,** is created when the work starts, and follows the family's working rules
  (CLAUDE.md, `packed.json` pins for tests, the family docs theme, brand from smalt-brand). Until then this record lives
  in smalt-brand, beside [WORK.md](../../WORK.md), which tracks it.

## Consequences

- **Phase 1 is a complete small library.** Data preparation, linear models and metrics are what every later phase uses.
  The first release can fit, score and save a model.
- **The CPU path is the product; WebGPU is an accelerator.** Every model has to be right without a GPU first. That
  doubles some work per model, and in return no user is left without a model.
- **Results agree with Python within stated tolerances, not bit for bit.** The tolerances are part of each model's
  reference page.
- **Speed is measured against Python from phase 1.** Meeting it may need several workers, and with them a cross-origin
  isolated page; the demos on GitHub Pages can't send the headers that allow it (smaltworks.dev/environments).
- **smaltui needs the worker entry** to run fits from TypeScript tabs without freezing. smaltnb can call the core
  directly from its kernel.
- **XGBoost compatibility sets the boosted trees' design:** their tree structure, missing-value rule and objectives follow
  XGBoost's.
- **The brand work continues:** smaltml's marks and words, and its page on smaltworks.dev once phase 1 is under way.

## Still to decide

1. **Time series forecasting:** in scope as a later phase, or left out.
2. **Importing other models** (such as ONNX) beyond XGBoost's format.
3. **The outside code for the compare tests** (section 7): the Python packages and their versions.
4. **When phase 2 starts:** after phase 1 is released, or alongside it.
5. **If a model can't reach Python's speed in TypeScript:** whether smaltml may write its own WebAssembly kernels.
