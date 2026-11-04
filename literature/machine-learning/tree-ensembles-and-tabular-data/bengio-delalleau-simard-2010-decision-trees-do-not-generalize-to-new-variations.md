# Decision Trees Do Not Generalize to New Variations

| | |
|---|---|
| **Authors** | Yoshua Bengio, Olivier Delalleau, Clarence Simard (Université de Montréal) |
| **Year** | 2010 |
| **Type** | Paper — *Computational Intelligence* 26(4), 449–467, 2010 (Wiley) |
| **Link** | [doi.org/10.1111/j.1467-8640.2010.00366.x](https://doi.org/10.1111/j.1467-8640.2010.00366.x); the authors host a copy at [iro.umontreal.ca/~lisa](https://www.iro.umontreal.ca/~lisa/pointeurs/bengio+al-decisiontrees-2010.pdf) |
| **BibTeX** | `bengio2010decision` |
| **Status** | Reference — §1, §3 up to Corollary 1, and §4 carry the argument; the checkerboard proof is technical |

## What it is

A short theory paper on what a single decision tree cannot learn, and why sums of trees
(forests, boosting) and deeper models escape part of the limit.

- **The core argument.** A tree splits the input space into regions and fits a separate
  constant in each leaf, using only the training points that land there. Every leaf needs
  at least one training example. So if the target function needs N distinct pieces to be
  approximated well, the tree needs at least N training examples (Lemma 1). It cannot
  predict a variation in a region where it has seen no data.
- **Parity: exponential in dimension.** On the d-bit parity function (output depends on
  whether the number of 1s is odd), any leaf shallower than depth d is right half the time.
  To reach error ε, a tree needs at least 2^d(1 − 2ε) examples (Corollary 1), though the
  function itself is described in one line.
- **Checkerboard: the product of the grid sizes.** On a d-dimensional checkerboard where
  neighbouring cells take different values, a tree needs at least as many examples as there
  are cells (Proposition 1), which grows exponentially with d.
- **A different curse from nearest neighbours.** Nearest-neighbour and Gaussian-kernel
  methods suffer because each parameter covers a small ball around a training point.
  Trees can ignore dimensions and let a leaf reach far from its data, so they are not local
  in that sense. The authors argue the real limit for both is the same: a separate set of
  parameters per region, with nothing learned in one region carried over to another. What
  matters is how much the target varies, not the input dimension as such.
- **Why sums of trees help.** A forest of n trees, each with a fixed number of leaves, can
  produce a number of distinct outputs that grows exponentially with n (Proposition 2). Each
  input is described by which leaf it lands in, in every tree, so the forest builds a
  distributed representation rather than one region per pattern. This is offered as one
  more reason forests and boosting beat single trees.
- **Depth.** By the authors' count a tree has two levels of computation and a forest three.
  Parity needs 2^(d−1) leaves in a tree but about 3(d − 1) units in a deep network built by
  composing pairwise parities. The authors conjecture that forests are still too shallow to
  learn checkerboard-like functions with variations unseen in training; this is a
  conjecture, not a result.

## Why it's in the library

**It states the limit of tree models precisely.** A tree can only predict what it has
seen examples of, region by region. Gradient-boosted trees remain the strongest default on
tabular data ([[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]),
but they are not extrapolators. A combination of feature values that never occurred in
training gets a prediction borrowed from whatever leaf it falls into.

**The cost is in interactions, not in features.** A target that depends on many features
at once, with signs that flip between combinations (the parity case), needs examples in
every combination. A target that mostly adds up effects of separate features is easy for a
sum of trees. When a tree model needs very deep trees to fit, that suggests the target has
many interacting variations, and it will need data in every one of them.

**The forest result explains why boosting works here.** Many shallow trees summed together
can represent many more patterns than their total leaf count. That is the argument for
ensembles of small trees over one large tree.

**It sets up the case for deep representations.** This paper sits between the
tree-versus-network debate and Bengio's later review
([[bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives]]):
distributed representations and depth are what let a model generalise to combinations it
has not seen.

## Links

- [[klusowski-2019-analyzing-cart]] — the positive counterpart: CART narrows its leaves
  along the features that matter, at a rate set by their importance
- [[candelori-santhanam-2025-breaking-the-curse-of-dimensionality-qcml-vs-tree-based-models]]
  — a benchmark on data built like this paper's worst case, where trees collapse and a linear
  model does best
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the empirical side: where trees win anyway on real tabular data
- [[li-et-al-2019-manifold-forests-closing-the-gap-on-neural-networks]] — the case where plain
  forests lose (images, time series), and a forest that splits on patches of neighbouring
  features
- [[freytsis-perelstein-san-2024-anomaly-detection-in-the-presence-of-irrelevant-features]]
  — the other side of the same mechanism: splitting one feature at a time lets trees
  ignore features that carry nothing
- [[bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives]] —
  distributed representations and depth, the remedy argued for here
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — the curse of dimensionality for
  local methods, which this paper contrasts with trees
- [[altman-krzywinski-2018-the-curses-of-dimensionality]] — a short primer on the separate
  curses
