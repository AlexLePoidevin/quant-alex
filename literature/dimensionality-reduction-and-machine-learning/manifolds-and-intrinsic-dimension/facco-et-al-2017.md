# Estimating the Intrinsic Dimension of Datasets by a Minimal Neighborhood Information

| | |
|---|---|
| **Authors** | Elena Facco; Maria d'Errico; Alex Rodriguez; Alessandro Laio |
| **Year** | 2017 |
| **Type** | Paper — *Scientific Reports* 7, 12140 |
| **BibTeX** | `facco2017intrinsic` |
| **Status** | To read |

## Key takeaway

The TWO-NN estimator: intrinsic dimension from the ratio of distances to each point's two
nearest neighbours. Needs only local information, so it survives curvature and
non-uniform density that break global methods.

## Why it's here

The concrete way to say "the nonlinear intrinsic dimension is lower than the linear rank."
A PCA scree plot and a TWO-NN estimate on the same panel is a strong two-number figure.

## Links

- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]] — symmetry
  priors, the other way past the curse of dimensionality
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — distance concentration, the
  reason a low intrinsic dimension matters for any neighbour-based method
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — QCML spectral-gap
  estimator, claimed robust to the noise that inflates local estimates like this one
