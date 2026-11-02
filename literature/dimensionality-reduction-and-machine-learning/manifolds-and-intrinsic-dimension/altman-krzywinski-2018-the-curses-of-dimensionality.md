# The Curse(s) of Dimensionality

| | |
|---|---|
| **Authors** | Naomi Altman; Martin Krzywinski |
| **Year** | 2018 |
| **Type** | Column — *Nature Methods* 15, 399–400, "Points of Significance", doi:[10.1038/s41592-018-0019-x](https://doi.org/10.1038/s41592-018-0019-x). Two pages |
| **PDF** | Not redistributable (© Springer Nature); read via the DOI |
| **BibTeX** | `altman2018curses` |
| **Status** | Reference |

## What it is

A two-page primer that splits "the curse of dimensionality" into four separate problems,
each shown with a small simulation of standard-normal data in p dimensions.

- **Sparsity.** Neighbourhoods empty out as p grows.
  - Of 1,000 points from a 2D normal, 6% lie within σ of (1.5, 1.5), against about 30% in
    either 1D projection. The 3D and 4D figures are 1.2% and 0.2%.
  - The fraction within σ of the mean falls from 68% at p = 1 to 0.017% at p = 10, as rare
    as falling beyond 3.8σ in one dimension. So "is this an outlier?" stops having an
    intuitive answer.
  - With five SNPs at 10% minor-allele frequency, a 1,000-sample table already has empty
    cells: there are no similar samples to learn from.
- **Distance and correlation concentration.**
  - Mean pairwise distance grows like √p, about σ√(2p).
  - At p = 100 the closest pair is farther apart than the farthest pair at p below about 15.
  - Correlation between random vectors collapses towards 0: at p = 100, none of 10,000
    random pairs has a correlation above 0.5.
- **Multicollinearity.** With p > n the variables lie in a subspace of dimension at most n,
  so some are exact linear combinations of others. Prediction still works, but no
  individual coefficient can be interpreted.
- **Multiple testing.** With one true predictor and k irrelevant ones, about αk of them come
  out significant. A larger n does not reduce that: k = 50 gives about as many false
  positives at n = 1,000 as at n = 100. Correcting with FWER or FDR costs power, which is
  the same curse as false negatives.
- **Overfitting.** More variables give a more flexible rule, which fits the noise as well as
  the signal.

## Why it's in the library

**It is the clearest short statement of the four problems, and each one needs a different
fix.**

| Problem | What fixes it |
|---|---|
| Sparsity | Fewer effective dimensions (reduction, intrinsic dimension) |
| Concentration | A better norm or work on the manifold |
| Collinearity | Regularisation, or don't interpret coefficients |
| Multiple testing and overfitting | Deflate for the number of things tried; validate out of sample |

**The multiple-testing figure transfers directly to factor research.** Screening k candidate
features at α = 0.05 gives about 0.05k false discoveries however long the history is. More
data does not remove that. Deflating for the number of trials does.

**It is the citation to hand to someone new to the subject.** Two pages, four figures, no
prerequisites.

## Links

- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — the theorem behind the
  distance-concentration figure
- [[aggarwal-hinneburg-keim-2001-surprising-behavior-of-distance-metrics]] — the choice of
  norm changes how fast distances concentrate
- [[levina-bickel-2004]], [[facco-et-al-2017]] — estimate the intrinsic dimension, the p that
  actually matters
- [[coifman-lafon-2006]] — diffusion maps, which work on the manifold instead of in the
  ambient space
- [[salih-2023-the-surprising-behavior-of-data-in-higher-dimensions]] — blog explainer:
  volume moves to the corners of the cube, and the kernel trick as the upside
- [[salih-2023-curse-of-dimensionality-an-intuitive-exploration]] — blog explainer of
  sparsity and distance concentration, with the law-of-large-numbers reason
- [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]] — hubness,
  a fifth curse for anything built on nearest neighbours
