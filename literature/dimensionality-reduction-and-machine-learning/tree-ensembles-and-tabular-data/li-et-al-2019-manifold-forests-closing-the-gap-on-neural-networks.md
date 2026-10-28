# Manifold Forests: Closing the Gap on Neural Networks

| | |
|---|---|
| **Authors** | Adam Li, Ronan Perry, Chester Huynh, Tyler M. Tomita, Ronak Mehta, Jesus Arroyo, Jesse Patsolic, Benjamin Falk, Joshua T. Vogelstein (Johns Hopkins; authors from the arXiv record — this PDF is the anonymised review copy) |
| **Year** | 2019 |
| **Type** | Preprint — ICLR 2020 submission (OpenReview paper 1162, under double-blind review), identical in title to arXiv:1909.11799v1. Later arXiv versions (to v5, 2022) were retitled *Manifold Oblique Random Forests: Towards Closing the Gap on Convolutional Deep Networks*; no published venue is listed. |
| **PDF** | `li-et-al-2019-manifold-forests-closing-the-gap-on-neural-networks.pdf` (in this folder) |
| **BibTeX** | `li2019manifold` |
| **Status** | Reference — short; §3 (the method) is the part worth keeping |

## What it is

Decision forests win on tabular data, where the order of the columns means nothing.
Networks win on images, audio and time series, where neighbouring features are related.
The paper argues part of the reason is that a forest never uses the *position* of a
feature, while a convolution does. MORF puts that position back into the forest.

- **Starting point: oblique forests (SPORF).** A standard random forest splits on one
  feature at a time. SPORF splits on a random sparse combination of features, aᵀx, with
  weights of +1 or −1. Each node samples d such combinations and keeps the best split by
  Gini impurity.
- **MORF changes which combinations are sampled.** Instead of random scattered features,
  each candidate sums a **contiguous patch**: a rectangle of pixels in an image, a window
  of time steps in a series, an arc that wraps around a circle. Patch sizes are drawn from
  uniform ranges set as hyperparameters. Everything else is the SPORF algorithm.
- **Feature importance** is how often each input appears in a chosen split across the
  forest.
- **Results:**
  - Three binary simulations: segments on a circle, horizontal vs vertical bars, and a
    decaying impulse in white noise. MORF has the lowest error of all non-CNN methods at
    every sample size, most clearly with few samples. On the circle task most other
    methods are at chance.
  - Against a small two-layer CNN there is no clear winner.
  - On MNIST, MORF beats random forest, SPORF, SVMs, kNN and an MLP at every training
    size but stays below the CNN.
  - Training and test times are close to a random forest's and well below the CNN's.
  - Its feature-importance maps on MNIST are smoother and less noisy than RF or SPORF.

## Read with care

- **An unrefereed early version.** This is the anonymised conference submission; the
  arXiv record went through five versions and a new title, and lists no published venue.
- **Small, friendly tests.** Three toy simulations built so local structure matters, and
  MNIST. The CNN baseline is a small two-layer network, and the comparison methods use
  scikit-learn defaults.
- **The title overstates it.** On the one real data set MORF does not close the gap with
  the CNN; it beats the other non-deep methods.
- **The time-series case is weak.** On the noisy-impulse task all methods are close, and
  the authors suggest continuity matters little there.
- **The manifold has to be known.** MORF needs to be told which features are neighbours
  and how big a patch can be. It does not learn the structure.

## Why it's in the library

**It shows how to give a tree model a time axis.** A ranking model on lagged returns or
rolling features usually treats each lag as an unrelated column. MORF's alternative is to
let splits use sums over contiguous windows of lags: features like "the last 3 to 10 days"
built inside the tree, not hand-engineered beforehand. That is a direct route to
look-back windows the data chooses.

**It explains the limit the other notes in this folder describe.**
[[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
finds trees win partly because they ignore rotations of the feature space. This paper is
the other side: when feature order does carry meaning, plain trees throw it away, and
that is where networks pull ahead.

**Oblique splits are a general tool.** Splitting on combinations of features, not one at
a time, applies to any tree model — including the gradient-boosted rankers and the
tree-based RL in [[fuhrer-tessler-dalal-2025-gradient-boosting-reinforcement-learning]].
The authors suggest building the same patch splits into XGBoost.

## Links

- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — why trees win on tabular data; this paper covers the case where they lose
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the same
  trees-vs-networks comparison on tabular benchmarks
- [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] —
  gradient-boosted trees on windowed time series, the hand-engineered alternative to
  MORF's learned windows
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — the general case for building a domain's structure into the model
- [[fuhrer-tessler-dalal-2025-gradient-boosting-reinforcement-learning]] — tree ensembles
  in RL, a candidate for the same structured splits
- [[chlenski-et-al-2025-mixed-curvature-decision-trees-and-random-forests]] — the same
  keep-the-tree, change-the-split idea for curved (hyperbolic, spherical) spaces
