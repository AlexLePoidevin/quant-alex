# A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices

| | |
|---|---|
| **Authors** | Olivier Ledoit; Michael Wolf |
| **Year** | 2004 |
| **Type** | Paper — *Journal of Multivariate Analysis* 88(2), 365–411 |
| **BibTeX** | `ledoit2004wellconditioned` |
| **Status** | To read |

## Key takeaway

Shrink the sample covariance matrix toward a structured target. With N comparable to T the
sample matrix is badly conditioned and its extreme eigenvalues are biased; shrinkage trades
a little bias for a large variance reduction.

## Why it's here

The practical answer to the estimation-error fault. At N≈500 and T≈1250 the ratio q≈0.4 —
squarely in the regime where the raw matrix is mostly noise. Pairs with RMT cleaning from
Bouchaud & Potters.
