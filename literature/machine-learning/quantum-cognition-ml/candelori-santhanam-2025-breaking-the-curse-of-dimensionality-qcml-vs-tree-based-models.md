# Breaking the Curse of Dimensionality: QCML vs. Tree-Based Models

| | |
|---|---|
| **Authors** | Luca Candelori, Nag Santhanam (Qognitive, Inc.) |
| **Year** | 2025 |
| **Type** | Blog post — Qognitive, 22 July 2025. Not peer-reviewed |
| **Link** | [qognitiveai.com/blog/tree-benchmarks](https://www.qognitiveai.com/blog/tree-benchmarks/) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22Breaking+the+Curse+of+Dimensionality%3A+QCML+vs.+Tree-Based+Models%22+Candelori) for the title and authors |
| **BibTeX** | `candelori2025trees` |
| **Status** | Reference — short; read alongside the linear-baseline check below |

## What it is

A benchmark post arguing that QCML generalises better than tree ensembles when data have
many features and few samples, because tree size grows exponentially with the number of
features while QCML's parameter count grows linearly.

- **The data.** Synthetic classification from scikit-learn's `make_classification`: 10,000
  points, 10 classes, one Gaussian cluster per class centred on a corner of a hypercube,
  every feature informative, `class_sep=2`, a 70/30 train/test split. The number of
  features is varied.
- **Trees at 1,000 features.** A single decision tree scores 0.131 accuracy (random guessing
  is 0.1) with 2,361 leaves and depth 36; tuning depth and leaf size never takes it above
  0.16. A default random forest (100 trees) scores 0.274. Both fall towards 0.1 as features
  are added.
- **QCML at 1,000 features.** With default settings (Hilbert space of dimension 8, 1,000
  epochs, learning rate 0.1) it scores 0.862, and stays well above the forest across the
  feature range. The authors describe its decline as linear in the number of features and
  the trees' as exponential, from the plots.
- **Gradient boosting.** XGBoost, LightGBM and CatBoost do much better than the forest. At
  20,000 features and 50,000 points the best, CatBoost, scores 0.24 against QCML's 0.68.
- **Training-set size.** At 1,000 features the forest improves roughly with the log of the
  sample size; by extrapolating that line the authors estimate it would need billions of
  points to match QCML trained on a few thousand. At 5,000 features the boosted models also
  need far more data than QCML for the same accuracy.
- **What is not reported.** The tree ensembles run on default settings, each result is one
  split with one seed, and no non-tree baseline (a linear model, a neural network) is
  included. QCML itself is available only through a request-access API.

## Why it's in the library

**The dataset is the case where axis-aligned trees are known to fail.** Gaussian clusters
at the corners of a 1,000-dimensional cube are separated by oblique boundaries that depend
on every feature at once. A tree splits one feature at a time, so it needs a separate
region for every combination, which is exactly the limit proved in
[[bengio-delalleau-simard-2010-decision-trees-do-not-generalize-to-new-variations]] (and
that post cites it). The post is a clean illustration of that result.

**A linear model beats every number in the post.** Re-running the post's 1,000-feature
setup with the same seed (scikit-learn 1.1.1) reproduces the random forest's 0.274 exactly.
On the same split, logistic regression scores **0.901** and linear discriminant analysis
**0.913**, both above QCML's 0.862:

```python
X, y = make_classification(n_samples=10000, n_features=1000, n_informative=1000,
                           n_redundant=0, n_clusters_per_class=1, class_sep=2,
                           n_classes=10, random_state=0)
# 70/30 split, random_state=0
# RandomForestClassifier(random_state=0)          0.274
# LogisticRegression(max_iter=2000)               0.901
# LinearDiscriminantAnalysis()                    0.913
```

The data are close to linearly separable, so the benchmark measures how badly trees handle
oblique boundaries, not whether QCML beats strong models. Any comparison of a new model
against trees needs a linear baseline and a tuned network alongside.

**The real question is what kind of data you have.** On real tabular data with irregular
targets and uninformative columns, trees win
([[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]],
[[freytsis-perelstein-san-2024-anomaly-detection-in-the-presence-of-irrelevant-features]]).
On smooth, dense, all-informative data like this, trees lose to almost anything with
oblique boundaries. Which regime a feature set is in is worth checking before choosing a
model.

## Links

- [[bengio-delalleau-simard-2010-decision-trees-do-not-generalize-to-new-variations]] —
  the theory behind the trees' failure here, cited by the post
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the real-data benchmark where trees win, also cited by the post
- [[freytsis-perelstein-san-2024-anomaly-detection-in-the-presence-of-irrelevant-features]]
  — the opposite regime: most features carry nothing, and trees beat networks
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the
  peer-reviewed QCML method
- [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] — QCML on
  real return data, compared with a neural network rather than trees
- [[candelori-santhanam-2026-the-shape-of-your-data]] — the same authors' QCML white paper
  on imputation
