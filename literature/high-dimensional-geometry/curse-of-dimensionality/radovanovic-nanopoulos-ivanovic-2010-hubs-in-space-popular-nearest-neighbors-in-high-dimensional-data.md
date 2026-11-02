# Hubs in Space: Popular Nearest Neighbors in High-Dimensional Data

| | |
|---|---|
| **Authors** | Miloš Radovanović (Novi Sad); Alexandros Nanopoulos (Hildesheim); Mirjana Ivanović (Novi Sad) |
| **Year** | 2010 |
| **Type** | Paper — *Journal of Machine Learning Research* 11, 2487–2531. Extends their ICML 2009 paper. 45pp |
| **PDF** | `radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data.pdf` (in this folder) |
| **BibTeX** | `radovanovic2010hubs` |
| **Status** | Reference |

## What it is

A second nearest-neighbour curse, separate from distances concentrating. Count how often
each point appears in the k-nearest-neighbour lists of the others, its **k-occurrence
N_k(x)**. The counts always average to k, but as dimension grows their distribution becomes
strongly right-skewed: a few **hubs** sit in very many neighbour lists, and many
**antihubs** sit in almost none.

- **It appears in random data.** 10,000 points, k = 5. The skewness of N₅ for IID uniform
  data with Euclidean distance is 0.12 at d = 3, 1.54 at d = 20 and 5.45 at d = 100; for
  IID normal data it reaches 19.2 at d = 100. The same happens with fractional (L₀.₅),
  Bray-Curtis, Canberra and other distances. The one exception shown is cosine distance on
  normal data.
- **It appears in real data.** Across 50 datasets (UCI, gene expression, text), skewness of
  N₁₀ has a Spearman correlation of 0.62 with the number of features, and an even stronger
  one with the intrinsic dimension measured by the Levina–Bickel estimator.
- **Hubs are the points near the centre.** In high dimension, a point's N_k correlates
  strongly with how close it is to the data mean (for clustered data, to its own cluster's
  mean).
- **The mechanism (Theorem 1).** For IID normal data, take two points at fixed offsets
  below the expected distance from the mean, for example one at the expected distance and
  one two standard deviations closer. The gap between their mean distances to all other
  points *grows* with d. Being slightly central becomes a bigger advantage as dimension
  rises, so central points get into far more neighbour lists. It is a finite-dimension
  result that agrees with Newman & Rinott's asymptotic one, where the variance of N₁ goes to
  infinity as d grows faster than n.
- **It tracks intrinsic, not raw, dimension.**
  - Shuffling each column independently destroys the dependence between features and
    raises the skewness sharply.
  - PCA, ICA and SNE barely change the skewness until the number of components falls below
    the intrinsic dimension.
  - Isomap and diffusion maps, which replace raw distances with graph distances, reduce it
    but don't remove it.
- **Hubs and outliers.**
  - Antihubs are the distance-based outliers.
  - Hubs, being unusually close to the centre, are *probabilistic* outliers: they sit
    where there is little density.
  - In high dimension the two definitions of outlier come apart. Points can look like
    distance-based outliers just because of dimension: in uniform random data, the gap
    between the highest and lowest k-th-neighbour distance widens as d grows.
- **Effects on learning.**
  - **k-NN classification:** "bad" hubs, whose label differs from the points that list
    them, spread wrong votes to many points. Down-weighting each neighbour's vote by its
    standardised bad-occurrence count raises accuracy.
  - **SVMs:** bad hubs lie near the class boundary and often become support vectors;
    removing them first hurts accuracy more than removing random points.
  - **AdaBoost:** starting with lower weights on hubs and antihubs generalises better in
    fewer rounds.
  - **Semi-supervised (harmonic functions):** labelling hubs first beats random choice;
    labelling antihubs first is much worse.
  - **Clustering:** hubs and antihubs both have lower silhouette scores than random
    points, hubs because they are close to other clusters too.

## Why it's in the library

**It is the k-NN curse that survives normalisation.** Distance concentration says
neighbours become alike. Hubness says neighbour lists become *dominated by the same few
points*. Any method that builds a k-NN graph (analogue forecasting, nearest-neighbour
regimes, spectral clustering, diffusion maps, UMAP) will over-weight whatever sits near the
centre of the data in high dimension.

**In a market panel the hubs are predictable.** Days or assets near the cross-sectional
average are the "central" points. A nearest-neighbour method on many features will keep
returning the same bland, average days as the closest analogues to everything, and the
unusual days will be antihubs that are never chosen. Counting N_k is a cheap diagnostic:
if the k-occurrence distribution is heavily skewed, the neighbours are being chosen by
geometry rather than by similarity.

**The fixes in the paper are simple and transferable.** Weight neighbour votes by how
often a point is a "bad" neighbour, or rescale distances so central points lose their
advantage. Reducing to roughly the intrinsic dimension (and no further) is the other lever.

**It ties three folders' worth of ideas together:** distance concentration (Beyer,
Aggarwal), intrinsic dimension (Levina–Bickel, used here to explain real data), and graph
methods (diffusion maps, which the paper tests).

## Links

- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — distance concentration, the
  related but distinct curse this paper sets itself against
- [[aggarwal-hinneburg-keim-2001-surprising-behavior-of-distance-metrics]] — fractional
  norms; the paper shows hubness persists under L₀.₅ too
- [[levina-bickel-2004]] — the intrinsic-dimension estimator used to explain hubness in
  real data
- [[coifman-lafon-2006]] — diffusion maps, which reduce hubness but don't remove it
- [[altman-krzywinski-2018-the-curses-of-dimensionality]] — primer on the other curses
- [[salih-2023-curse-of-dimensionality-an-intuitive-exploration]] — blog intuition for why
  distances bunch together, the starting point for hubness
- [[feldbauer-flexer-2019-a-comprehensive-empirical-comparison-of-hubness-reduction-in-high-dimensional-spaces]] — the
  benchmark of fixes: local scaling and mutual proximity work, fractional norms and
  shared neighbours don't
