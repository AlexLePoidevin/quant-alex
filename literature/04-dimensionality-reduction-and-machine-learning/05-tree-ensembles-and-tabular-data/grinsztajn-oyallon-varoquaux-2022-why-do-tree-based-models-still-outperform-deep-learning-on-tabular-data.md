# Why Do Tree-Based Models Still Outperform Deep Learning on Typical Tabular Data?

| | |
|---|---|
| **Authors** | Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux (Soda, Inria Saclay; MLIA, Sorbonne University) |
| **Year** | 2022 |
| **Type** | Paper — *Advances in Neural Information Processing Systems* 35 (NeurIPS 2022), Datasets and Benchmarks track. arXiv:2207.08815. 14pp (main text only; the appendix is not in this PDF) |
| **PDF** | `grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data.pdf` (in this folder) |
| **BibTeX** | `grinsztajn2022tree` |
| **Status** | Reference — the standard benchmark for "trees vs nets on tabular data", plus three explanations of why |

## What it is

Two contributions: a benchmark, and a set of experiments that change the data to see which
model each change hurts.

- **Benchmark (§3).** 45 datasets, mostly from OpenML, chosen by stated rules:
  heterogeneous columns, d/n < 1/10 and d < 500, real (or practically important) data, i.i.d.
  rows (**time series excluded**), at least 4 features and 3,000 rows, not deterministic, and
  "not too easy" (dropped if a single tree or linear model comes within 5% of both a default
  ResNet and a default HistGradientBoosting). Training sets are truncated to 10,000 rows
  (a 50,000-row setting is in the appendix). Missing data are removed, classification
  targets are binarised and balanced, and features are Gaussianised for the networks.
- **Tuning protocol.** About 400 random-search iterations per model and dataset (20,000
  compute-hours in total), always starting from the defaults. The search order is
  reshuffled 15 times to show the expected test score of the best-on-validation model
  after *n* iterations. Scores are normalised per dataset between the best model and the
  10% (classification) or 50% (regression) error quantile, then averaged. Code and all raw
  search results are public (github.com/LeoGrin/tabular-benchmark).
- **Result (§4, Fig. 1).** Random Forest, gradient-boosted trees and XGBoost beat MLP, ResNet,
  FT-Transformer and SAINT **at every search budget**, from the defaults to 400 iterations,
  in all four settings (numerical-only or mixed features, classification or regression).
  This is before counting that each network iteration is slower. The gap is a little
  narrower with numerical features only, so categorical variables are not the main
  reason the networks lose.
- **Why (§5).** Three inductive biases, each tested by transforming the training data:
  1. **Networks are biased toward smooth functions.** Smoothing the training target with a
     Gaussian kernel hurts trees a lot and networks hardly at all (Fig. 2), so the real
     targets have irregular, non-smooth parts that trees capture and networks miss.
  2. **MLP-like networks are not robust to uninformative features.** A GBT barely changes
     when the least important half of the features is removed (Fig. 3). Removing features
     narrows the ResNet's gap to the trees, and adding Gaussian noise features widens it
     (Fig. 4).
  3. **Tabular data are not rotation invariant, so the learner shouldn't be either.** After
     a random rotation of the features the ranking flips: trees fall below the networks, and
     only ResNet is unaffected (Fig. 5). Each column means something on its own (age,
     weight), and a rotation-invariant learner has to recover that basis before it can
     discard noise columns (Ng 2004: sample complexity grows linearly in irrelevant features).
     The authors suggest this is why per-feature embeddings help FT-Transformer and SAINT:
     they break the invariance.

## Read with care

- **I.i.d. data only, by design.** Time series and stream data are excluded, so nothing here
  speaks directly to non-stationarity, temporal dependence or regime change. For those see
  [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] and
  [[hall-rasheed-2025-survey-of-machine-learning-methods-for-time-series-prediction]].
- **Medium-sized data.** Training sets are capped at 10,000 rows. The paper doesn't claim the
  gap holds at much larger sizes; the appendix's 50,000-row setting has fewer datasets.
- **The selection rules shape the answer.** The "not too easy" filter keeps only datasets
  where flexible models clearly beat a single tree or a linear model, and it uses a default
  GBT as one of its yardsticks. Removing missing values and high-cardinality categoricals
  also removes things some networks handle differently.
- **Averages of normalised scores.** The headline curves average across datasets after a
  per-dataset rescaling, and the ribbons show search-order variation, not dataset-to-dataset
  spread. The authors warn that this variance estimate is optimistic at large budgets.
- **The networks are the 2021 field.** Well-regularised MLPs (Kadra et al. 2021) and later
  tabular architectures are discussed but not all benchmarked. The conclusion has largely
  held since, but the size of the gap depends on the year.
- **The mechanisms are evidence, not proof.** Each one is shown by a single transformation
  averaged across datasets, on numerical-feature classification only.

## Why it's in the library

**It is the strongest version of the "start with boosted trees" result.** Compared with
[[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]], it fixes the main
objections: datasets are chosen by rules before the comparison, every model gets the same
random-search budget, and performance is shown as a function of that budget. Trees still
win at every budget.

**The uninformative-features finding is a feature-engineering lesson.** A financial feature
panel has many weak or useless columns. Trees ignore them cheaply; networks pay for them.
That argues for pruning features before training a network, and for not expecting more
features to help a network the way they might help a tree.

**The rotation result cuts both ways for factor work.** PCA, whitening or any other rotation
of the feature panel mixes columns with different meanings and removes the basis trees
rely on. Feeding principal components to a tree model can lose the axis-aligned structure
that made the raw features useful. If a rotation is used, compare against the raw basis.

**The smoothness finding explains where networks lose.** Return targets have thresholds,
regime breaks and fat tails, the irregular parts trees model with splits. A network that
competes needs per-feature embeddings, periodic encodings or binning to reach that part of
the function.

## Links

- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — the symmetry framework: tabular columns have no rotation group to be invariant to
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the earlier,
  smaller comparison on 11 datasets, which this benchmark supersedes
- [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] — the
  time-series case this paper excludes, with windowed XGBoost against deep forecasters
- [[hall-rasheed-2025-survey-of-machine-learning-methods-for-time-series-prediction]] — a
  tally of 79 tree-vs-deep time-series studies, with the same author-bias effect
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — another reason uninformative
  dimensions hurt methods that treat all features together
- [[gu-kelly-xiu-2021]] — deep models on a return panel, where a tuned tree model belongs in
  the comparison
