# Maximum Likelihood Estimation of Intrinsic Dimension

| | |
|---|---|
| **Authors** | Elizaveta Levina (Michigan); Peter J. Bickel (Berkeley) |
| **Year** | 2004 |
| **Type** | Paper — *Advances in Neural Information Processing Systems 17* (NIPS 2004). 8pp |
| **PDF** | `levina-bickel-2004-maximum-likelihood-estimation-of-intrinsic-dimension.pdf` (in this folder) |
| **BibTeX** | `levina2004mle` |
| **Status** | Reference |

## What it is

A way to estimate how many dimensions data really has (its intrinsic dimension m) from
distances to nearest neighbours, with a likelihood behind it rather than a slope read off
a plot.

- **The idea.** Around any point x, if the density is roughly constant in a small ball,
  the number of other points within distance t grows like tᵐ: a Poisson process whose
  rate depends on m. Writing down that likelihood and maximising it gives m.
- **The estimator.** With T_j(x) the distance from x to its j-th nearest neighbour,

  m̂_k(x) = [ (1/(k−1)) Σ_{j=1}^{k−1} log( T_k(x) / T_j(x) ) ]⁻¹

  So the estimate is the inverse of the average log ratio between the k-th neighbour's
  distance and the closer ones. It is averaged over all points and over a range of k; the
  paper fixes k = 10 to 20 throughout. Dividing by k − 2 instead of k − 1 removes the
  first-order bias. The same fit gives the density at x, so an entropy estimate comes free.
- **Theory.** If the Poisson approximation holds, m·log(T_k/T_j) behave like exponential
  order statistics, so the estimator's mean and variance are known: unbiased to first
  order, with variance of order 1/n.
- **Simulations:**
  - **k matters only at the very small end.** For a 5-dimensional normal, estimates are
    too high for k below about 10 and close to 5 from there on. Larger k gives a negative
    bias that shrinks with more data and grows with dimension.
  - **Correlation doesn't fool it.** On a 5-dimensional normal with equal correlation ρ
    between all coordinates, the estimate stays near 5 until ρ is very close to 1, when
    the cloud really becomes a line. There the answer depends on sample size: 100 points
    look like a line, 2,000 fill in the space around it. Intrinsic dimension depends on the
    scale you look at.
  - **Against the alternatives** (on spheres): the correlation dimension (slope of
    log-pair-counts against log-radius) has slightly less bias but a standard deviation at
    least 10 times larger; regressing log mean distance on log k has low variance but the
    most bias. The MLE has the best balance.
- **Real data** (Table 1):

  | Dataset | Ambient dimension | MLE | Regression | Correlation dim. |
  |---|---|---|---|---|
  | Swiss roll (true 2) | 3 | 2.1 | 1.8 | 2.0 |
  | Isomap faces | 64 × 64 pixels | 4.3 | 4.0 | 3.5 |
  | Rotating hand video | 480 × 512 pixels | 3.1 | 2.5 | 3.91 (or 19.7, depending on the range fitted) |

- **Known weakness.** Every estimator, this one included, underestimates in high
  dimensions, mainly because a small ball needs very many points before it holds enough
  neighbours. Edge effects add to it. Neither trimming edge points nor calibrating on
  simulated data fixed it.

## Why it's in the library

**It is the standard way to answer "how many dimensions does this feature set really
have?"** One pass over k-nearest-neighbour distances, two parameters (the range of k), and
an answer with a standard error. A feature panel with dozens of columns and an intrinsic
dimension of 5 to 10 is the normal case, and it says how far reduction can go before
information is lost.

**Per-point estimates are useful in their own right.** m̂_k(x) can be kept for every point
instead of averaged. Groups of days or assets with different local dimension are a sign the
data is a union of different structures, which is what
[[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
does with it.

**Read the number as a lower bound, at a scale.** The paper is explicit that estimates fall
short in high dimensions and change with sample size and neighbourhood size. Report the k
range, check stability across it, and compare with a second estimator such as
[[facco-et-al-2017]] (two-NN), which uses only the two nearest distances.

## Links

- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — why nearest-neighbour distances
  stop discriminating in high ambient dimension unless the intrinsic dimension is low
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — QCML spectral-gap
  estimator, claimed robust to the noise that inflates local estimates like this one
- [[koulakis-seibold-2026-the-data-manifold-under-the-microscope]] — a controlled benchmark where intrinsic dimension and
  curvature are known, for checking estimators like this one
- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]] — applies this estimator class by class and finds
  intrinsic dimension varies across the data
- [[elhamifar-vidal-2011-sparse-manifold-clustering-and-embedding]] — SMCE; lets each point pick
  its own neighbours and reads off a dimension per cluster, with no fixed k
- [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]] — uses this
  estimator to show hubness tracks intrinsic, not raw, dimension
