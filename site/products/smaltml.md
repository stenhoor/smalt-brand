# <Mark product="ml" :size="40" /> smaltml

<StageBadge />

**Small. Alternative. Predict.** Machine learning for smaltdb, on the hardware you have.

smaltml, said "smalt-M-L", trains models on tables and makes predictions with them, in TypeScript. It is a
[kit](/products/kits): notebooks in [smaltnb](/products/smaltnb) and pipelines in [smaltfl](/products/smaltfl) train
models with it, and apps call `predict()` from TypeScript.

- **Classic machine learning on tables.** Data preparation, linear and logistic regression and their metrics first;
  trees, boosting, clustering and more follow, with scikit-learn's and XGBoost's parameters and defaults.
- **The hardware you have.** Every model runs on the CPU, in every browser the family supports and in Node. WebGPU
  speeds up the heavy steps where the browser has it.
- **Models as JSON.** A fitted model saves to a versioned JSON document, kept as a file or as a row in a smaltdb table,
  and loads back by name for `predict()`.
- **Checked against Python.** Each model's results are compared with scikit-learn's on the same data, and kept as tests.

**Status:** in early development. The first models are being built.

[Repository →](https://github.com/stenhoor/smaltml)
