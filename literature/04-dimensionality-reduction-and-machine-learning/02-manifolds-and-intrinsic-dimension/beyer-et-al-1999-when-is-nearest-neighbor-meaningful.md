# When Is "Nearest Neighbor" Meaningful?

| | |
|---|---|
| **Authors** | Kevin Beyer, Jonathan Goldstein, Raghu Ramakrishnan, Uri Shaft (CS Dept., University of Wisconsin–Madison) |
| **Year** | 1999 |
| **Type** | Conference paper — *Database Theory — ICDT'99*, LNCS 1540, pp. 217–235, doi:10.1007/3-540-49257-7_15. Author copy, 19pp |
| **PDF** | `beyer-et-al-1999-when-is-nearest-neighbor-meaningful.pdf` (in this folder; the text layer is font-garbled, so search doesn't work — read it as images) |
| **BibTeX** | `beyer1999nearest` |
| **Status** | Reference |

## What it is

The standard citation for **distance concentration**, the form of the curse of
dimensionality that breaks nearest-neighbour methods.

- **Instability (Definition 1).** A nearest-neighbour query is *unstable* for a given ε if
  most data points are within (1 + ε) times the distance to the nearest neighbour. An
  unstable query has no meaningful answer: the "nearest" point is barely nearer than anything
  else.
- **Theorem 1.** With dimension m growing and n data points fixed, if
  lim var(d_m(P, Q)^p / E[d_m(P, Q)^p]) = 0 (the relative spread of distances vanishes), then
  for every ε > 0, P[DMAX_m ≤ (1 + ε)·DMIN_m] → 1. The nearest and farthest points become
  the same distance away.
- **The condition is much broader than IID dimensions.** It also holds for every dimension
  correlated with every other (Example 3), for variances shrinking to zero like N(0, 1/i)
  (Example 4), and for marginals that change with m (Example 5). It fails when the extra
  dimensions are copies of one another (Example 2): the data lie on a line and the problem
  is really one-dimensional.
- **It bites early.** In simulations with a million points, DMAX/DMIN is about 10⁷ in one
  dimension and falls by six orders of magnitude by ten dimensions. By twenty, the farthest
  point is only about four times as far as the nearest (Fig. 7). On a real 256-dimensional
  colour-histogram set reduced to 64 by PCA, 15% of queries had half the data within 3× the
  nearest-neighbour distance.
- **When NN still works (§4):** when the query sits inside a well-separated cluster (that is
  classification, and the answer is the cluster, not the point), or when the data are
  **implicitly low-dimensional**, so the intrinsic dimension rather than the ambient one
  governs the distances.
- **The methodological point:** most indexing papers of the time didn't check that their
  workloads were meaningful, and didn't compare against a plain linear scan, which would have
  won at 10–15 dimensions.

## Read with care

- It is an **asymptotic result in m with n fixed**. It says nothing directly about a finite
  sample in 30 dimensions; the simulations are what show the effect is already large there.
- The theorem concerns **contrast** (nearest against farthest), not whether the neighbours
  are useful for prediction. A kNN predictor can still help if the target varies along the
  few directions that do separate points.
- Uniform, independent-noise workloads are the worst case. Real feature panels with strong
  factor structure are closer to the paper's "implicitly low-dimensional" case, which is
  why the intrinsic dimension needs measuring.

## Why it's in the library

**It is the warning label for every distance-based method on a wide feature set:** kNN
analogue forecasting ("find past days like today"), clustering of assets or regimes,
kernel methods with a Euclidean distance, and similarity search. On 30–100 raw features,
unless they are dominated by a few factors, "today's nearest historical neighbour" is barely
nearer than a random day.

**It explains why this folder's estimators matter.** Theorem 1 fails, and nearest neighbours
mean something, exactly when the data live on a low-dimensional manifold.
[[levina-bickel-2004]] and [[facco-et-al-2017]] estimate that dimension from
nearest-neighbour distances, so a low estimate is also evidence that neighbour-based
methods on the data are viable. The practical recipe is to measure the intrinsic
dimension, reduce to it (PCA, [[coifman-lafon-2006]] diffusion maps), and only then use
distances.

**The paper's own check is easy to copy.** Before trusting a neighbour method, plot the
distribution of query-to-point distances and the DMAX/DMIN ratio on the actual features. If
the nearest neighbour is not clearly closer than the median point, the method is choosing
at random.

## Links

- [[levina-bickel-2004]] — intrinsic dimension from nearest-neighbour distances, the
  remedy the paper points to in §4.2
- [[facco-et-al-2017]] — TWO-NN, which uses only the two nearest distances and so is
  less exposed to distance concentration
- [[coifman-lafon-2006]] — diffusion maps, a way to work on the manifold instead of in the
  ambient space
- [[kernel-pca]] — a kernel built on Euclidean distance inherits the same concentration
