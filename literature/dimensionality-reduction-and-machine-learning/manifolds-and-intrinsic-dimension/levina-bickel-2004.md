# Maximum Likelihood Estimation of Intrinsic Dimension

| | |
|---|---|
| **Authors** | Elizaveta Levina; Peter J. Bickel |
| **Year** | 2004 |
| **Type** | Paper — *NIPS 17* |
| **BibTeX** | `levina2004mle` |
| **Status** | To read |

## Key takeaway

Treats nearest-neighbour distances as a Poisson process and derives a maximum-likelihood
estimator of intrinsic dimension. The standard baseline that TWO-NN is measured against.

## Why it's here

Second opinion. Quoting one intrinsic-dimension number is a claim; quoting two estimators
that agree is evidence.

## Links

- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — why nearest-neighbour distances
  stop discriminating in high ambient dimension unless the intrinsic dimension is low
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — QCML spectral-gap
  estimator, claimed robust to the noise that inflates local estimates like this one
- [[koulakis-seibold-2026-the-data-manifold-under-the-microscope]] — a controlled benchmark where intrinsic dimension and
  curvature are known, for checking estimators like this one
- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]] — applies this estimator class by class and finds
  intrinsic dimension varies across the data
